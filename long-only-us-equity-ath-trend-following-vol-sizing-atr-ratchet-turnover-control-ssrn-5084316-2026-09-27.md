---
schema: strategy-research-record-v1
title: Long-only US equity all-time-high trend-following with volatility sizing, 10xATR ratchet stops and an AUM-by-AUM turnover-control cost audit
created: 2026-09-27
updated: 2026-09-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equities
  - us-stocks
  - trend-following
  - momentum
  - transaction-costs
  - turnover-control
  - ssrn
status: research-only
confidence: medium
source_as_of: 2026-09-27
sources:
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5084316
  - https://doi.org/10.2139/ssrn.5084316
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "SSRN landing abstract vs pinned PDF abstract: sample end '1950 through November 2024' (landing) vs '1950 through October 2024' (PDF p.1); gross CAGR '15.19%' (landing) vs '15.02%' (PDF); annualized alpha '6.18%' (landing) vs '6.19%' (PDF). Unreconciled; this record quotes PDF values for all table-level numbers and records the landing values only as the alternate version."
  - "PDF Section 2 states the Norgate database covers '1950 until August 2024' while the PDF abstract and Section 1 state 'January 1950 until October 2024'. Unreconciled inside the pinned PDF."
  - "Four version-date expressions: PDF title block 'First Version: November 26, 2024 / This Version: January 17, 2025'; SSRN 'Date Written: January 06, 2025'; SSRN 'Posted: 9 Jan 2025'; SSRN header 'Last revised: 17 Jan 2025' vs the SSRN citation widget 'Last revised: 22 Jan 2025'. PDF /CreationDate is 2025-01-17. Unreconciled."
  - "Cost assumption tension inside the pinned PDF: Section 3.3 states 'A transaction cost of 0.50% per round turn is deducted from each trade', while footnote 5 on the same page concludes 'Taken together, 25 bps represents a reasonable, conservative assumption for average trading costs'. The implemented deduction is 0.50%; the footnote's 25 bps is not applied anywhere in the text. Unreconciled."
  - "Author affiliations differ between surfaces: SSRN landing lists Carlo Zarattini and Alberto Pagani both under 'Concretum Group' and Cole Wilcox under 'Longboard Asset Management, LP'; PDF p.1 lists Zarattini at 'Concretum Research, Piazza Molino Nuovo 8, 6900 Lugano', Pagani at 'Universita degli Studi di Parma', and Wilcox at 'Longboard Asset Management, 213 West Comstock Ave, Suite 104 Winter Park, FL'. Unreconciled."
  - "Title wording differs: SSRN landing 'Does Trend-Following Still Work on Stocks?' (hyphenated) vs PDF p.1 'Does Trend Following Still Work on Stocks?' (unhyphenated). Unreconciled; both spellings preserved."
  - "Benchmark ambiguity for the alpha columns: Tables 2 and 3 print 'Alpha' without naming the regression, while Section 4.9 states the alpha-stability exercise uses an equally weighted Russell 3000 benchmark and Section 4.6 compares against a market-cap-weighted all-US-stock index from Kenneth French. Which regression produces the Table 2/3 alpha column is underspecified."
---

# Long-only US equity all-time-high trend-following with volatility sizing, 10xATR ratchet stops and an AUM-by-AUM turnover-control cost audit

## Provenance

**Primary source (pinned and fully read in this run):**

- Carlo Zarattini, Alberto Pagani, Cole Wilcox. *"Does Trend Following Still Work on Stocks?"* (PDF title block, p.1). SSRN landing heading: *"Does Trend-Following Still Work on Stocks?"*.
- SSRN abstract id: `5084316`; DOI: `https://doi.org/10.2139/ssrn.5084316`; landing: `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5084316`.
- **Complete author list exactly as printed on PDF p.1:** Carlo Zarattini (1, concretumgroup.com), Alberto Pagani (2, studenti.unipr.it), Cole Wilcox (3, longboardfunds.com). Affiliations as printed: (1) Concretum Research, Piazza Molino Nuovo 8, 6900 Lugano, Switzerland; (2) Universita degli Studi di Parma, Str. dell'Universita, 12, 43121 Parma PR, Italy; (3) Longboard Asset Management, 213 West Comstock Ave, Suite 104 Winter Park, FL 32789, United States. No other authors; no editor or mentor line.
- **Version / date:** PDF p.1 prints `First Version: November 26, 2024` and `This Version: January 17, 2025`. PDF metadata `/CreationDate` = `D:20250117184345+01'00'`, `/Producer` = `pdfTeX-1.40.25`, `/Creator` = `LaTeX with hyperref`. SSRN landing (read in a browser session on 2026-09-27 after the Cloudflare interstitial cleared): `37 Pages`, `Posted: 9 Jan 2025`, `Last revised: 17 Jan 2025`, `Date Written: January 06, 2025`. The SSRN citation widget on the same page prints `Last revised: 22 Jan 2025`. All four date expressions are preserved unreconciled (see frontmatter).
- **Pinned PDF retrieval (2026-09-27):** the landing-page `Open PDF in Browser` delivery link returned `HTTP 200`, `application/pdf`, `content-length 1714240`; file saved locally, **1,714,240 bytes, 37 pages, SHA-256 `ae9b740ccf82bdeb850aaaf3d86488e92203b1e357655ba9e6075d7999d1aa44`**, text-extracted page by page with `pypdf 6.16.2` to 55,354 characters covering all 37 pages. Pages 1-37 include the abstract, Sections 1-5, Tables 1-3, Figures 1-21 captions, author biographies and the 10-entry reference list. The presigned download URL used for retrieval is deliberately not reproduced anywhere in this record.
- **Landing statistics observed 2026-09-27:** 9,736 downloads, 31,619 abstract views, 1 citation, 10 references.
- **License:** SSRN landing license block: *"The copyright holder has granted SSRN a license. All rights reserved. No reuse allowed without permission."* No open licence, no redistribution grant; only quoted values and normalized rules are recorded here.
- **Publication status:** SSRN working paper. No journal, no issue, no peer-review statement anywhere in the landing or the PDF -> peer-review status `not stated in source`. Keyword line (landing): `Trend-Following, Momentum, Algo-Trading, Trading Systems, Stock Investing`.
- **Code / replication package:** none referenced in the PDF; no repository, no appendix of code, no data-availability statement -> `data gap`. The Turnover Control thresholds are explicitly withheld (Section 4.8 footnote 11: *"For additional information about the Turnover Control mechanism, please contact us via email at carlo@concretumgroup.com."*).

**Sample periods and universe (primary-source checksum):**

- Statistical study (Part 1): Norgate survivorship-bias-free end-of-day data, **31,000 common stocks traded on NYSE, AMEX and Nasdaq from 1950 until August 2024 (Section 2) / through October 2024 (abstract and Section 1)**, including approximately 24,000 delisted stocks, with dividends, splits and other corporate actions accounted for. Abstract states **"more than 66,000 simulated long-only trend trades"**; Section 3.5 says "approximately 66,000 trades".
- Tradable portfolio (Part 2): **January 1991 to October 2024**, investable universe = Russell 3000 members (see Signal).
- **Out-of-sample framing:** no held-out window. The only temporal split is the pre-/post-2005 comparison around the Wilcox and Crittenden (2005) white paper (Section 3.5, Figures 9-11).

**Deterministic source-identity dedup (performed before writing, 2026-09-27):** `rg -uuu -F` across the **entire repository, hidden-inclusive** (3,471 files, including `.mimo-worktrees/`, `.agents/`, `.hermes/`, `tests/`, `coverage_manifest.csv`) for `5084316`, `10.2139/ssrn.5084316`, `Does Trend-Following Still Work`, `Does Trend Following`, `Crittenden`, `Longboard`, `66,000 simulated`, `Turnover Control`, `Norgate`, and the exact word `Wilcox` -> **zero source-identity hits**. `coverage_manifest.csv` (1,088,787 bytes) returns 0 for `5084316` and 0 for the title. The only `Norgate` hits are an unrelated continuous-futures record; the only `Turnover Control` hits are two formulaic-alpha records using the phrase for a different, generic daily-swap cap; `Wilcox` appears only inside `Wilcoxon`. `git log --oneline -20` was inspected as a convenience glance only and does not by itself satisfy dedup. Wiki Brain `rg -uuu -F` for `5084316`, `Trend-Following Still Work`, `Crittenden`, `Longboard` -> **0 hits** (no matching Wiki page; no page fabricated below).

## Economic mechanism

### Source-reported

The authors argue that single-name US equities exhibit a long-only, time-series trend that can be harvested by an extreme-selectivity filter: a stock printing a **new all-time high** is, "by any standard, in an uptrend" (Section 3.2), and that filter simultaneously keeps the number of holdings manageable. Profitability is explicitly tail-driven: the return distribution is positively skewed, a minority of trades generates the whole result, and long holding periods (average winning trade 370 calendar days) let the winners compound while a volatility-scaled stop controls the losers. The second half of the paper reframes the same idea as an implementation problem: the baseline model trades every day to maintain equal risk contribution, so small-account commission floors and large-account market impact can destroy the gross edge, and a proprietary **Turnover Control** mechanism (skip tiny rebalances, spread trades over days, skip rebalances whose expected commission is too large relative to traded notional) is introduced to keep net-of-cost results aligned with the theoretical curve (Sections 4.7-4.8).

### Research interpretation

- **Regime / trend persistence:** the economic claim is behavioral-and-structural time-series momentum in individual equities - winners keep winning while slow information diffusion and underreaction leave the trend intact.
- **Tail compensation as the payoff structure:** the strategy is not a high-hit-rate signal; it is a long right-tail harvesting rule whose viability depends on letting a small number of >1R winners pay for a majority of small losses. Any implementation that truncates the tail (early profit-taking, tight stops, mandatory diversification limits) damages the thesis directly.
- **Friction as the binding constraint:** the alpha hypothesis and the cost hypothesis are separable - Part 1 tests the signal, Part 2 tests whether a specific cost structure (per-share commission floors for small AUM, square-root-style impact for large AUM) leaves anything. This record treats "alpha survives realistic cost at a stated AUM" as the falsifiable object.
- **Component roles:** primary signal = all-time-high breakout at the close; risk/exit = 10xATR ratcheting trailing stop checked at the close; sizing = inverse-volatility equal-risk weighting with a concentration floor and a 200% leverage cap; execution layer = market-on-open next-day orders plus a turnover-control overlay. **No component should be assumed to carry alpha on its own**; the turnover overlay is an execution/cost device, not a predictive signal, and the leverage cap is a risk rule, not alpha.

## Signal

All items below are `source-reported` unless marked otherwise. Formation timestamp, entry, exit, sizing and parameters are read from Sections 3.1-3.3 and 4.1-4.5 of the pinned PDF.

**Signal formation timestamp.** Evaluated at the **close of day t** (US equity regular session close; exchange timezone not stated in source -> `data gap`). The signal becomes tradable at the **market open of day t+1**. No intraday or post-close timestamp convention is given.

**Universe / eligibility filter (Part 1, Section 3.1).** At the close of day t a stock qualifies if (a) closing price is above **$10**, applied to the **unadjusted** close, and (b) average dollar volume over the last **42 trading days** exceeds **$1,000,000**, a threshold decayed over time with CPI (CPIAUCSL): approximately **$80,000 in 1951, $300,000 in 1980, $600,000 in 2005**. A stock already held that stops qualifying is **retained until its stop-loss is hit**.

**Universe (Part 2, Section 4.1).** New potential long positions must (a) be **Russell 3000** members, (b) trade above **$10**, (c) have 42-day average dollar volume above **$1 million**, back-adjusted for inflation with CPI.

**Long entry.** If at the close of day t the stock passes the filters and its **closing price equals or exceeds the highest adjusted close (split- and dividend-adjusted) in its history**, a buy order is placed **at the open on day t+1** (Sections 3.2, 4.2). Ties are inclusive (`>=`). Entry for stocks already held: no re-entry rule after an exit is stated beyond the same ATH condition, which can only re-fire after the stock makes a new adjusted all-time high -> partially `underspecified` (the paper never states whether a re-entry is permitted once a position was stopped out at a loss while price is still below the prior ATH; by construction it cannot re-enter until a new ATH prints).

**Exit / stop.** Trailing stop set at the close of day t as

`Stop_t = ATH_t x (1 - ATR_t / Close_t)^10`

where `ATH_t` is the all-time high through day t and `ATR_t` is the **42-day Average True Range** (Section 3.2, Section 4.4). The stop is updated daily and **never lowered**: `StopLoss_t = max(StopLoss_(t-1), ATH_t x (1 - ATR_t/Close_t)^10` (Section 4.5). It is a **soft stop checked at the close**, not a resting broker order (Section 4.4 footnote 7); if the close is below the stop, the position is **sold at the next day's open**. The multiplier `10` and the `42`-day window are fixed in the source; their selection rationale is not given -> `not stated in source` (fixed, not described as tuned).

**Position sizing (Section 4.3).** Volatility-targeted equal-risk weight, computed at the close of day t and traded at the open of t+1:

`ew_(t,i) = (30% / sigma_(t,i)) x (1 / max(200, N_holdings,t))`

with `sigma_(t,i)` the **42-day annualized volatility** of stock i. The `max(200, N)` term prevents concentration when most names are stopped out. Total ideal exposure `fW_t = sum_i ew_(t,i)` is then scaled to a **200% leverage cap**: `w_(t,i) = ew_(t,i) x max(1, 2/fW_t)`. Target annualized portfolio volatility = **30%**.

**Order handling.** Market-on-open orders for every name on the buy list; stops and exits are executed at the following open (Sections 4.2-4.4). Same-bar/simultaneous signal collisions, partial fills, order rejects and halt handling are `not stated in source`.

**Position sizing / overlap / cadence.** Daily rebalance of weights; entries and exits are event-driven (new ATH, stop breach); holding period is unbounded (average winning trade **370 calendar days**, Section 3.5). The statistical study normalizes each trade's PnL in risk units `PnL_R = (ExitPrice - EntryPrice) / (EntryPrice - StopLoss)` (Equation 1).

**Turnover Control (Section 4.8) - `underspecified` by construction.** Three qualitative design points are given: (1) skip trades whose required rebalancing adjustment falls below a defined threshold; (2) distribute trades over multiple days to reduce market impact of new positions or large rebalances; (3) skip rebalances when expected commission exceeds a preset threshold relative to traded notional. **No thresholds, no lookback, no scheduling rule and no pseudocode are published** (footnote 11 withholds them). Therefore Table 3's numbers cannot be reconstructed from the paper alone -> `data gap`, not a reproducible rule.

**Sizing-vs-alpha boundary.** The 30% volatility target, the 200% leverage cap, the `max(200, N)` concentration floor and the $10 / $1M liquidity filters are **risk and implementability rules, not predictive signals** (README rule 8).

## Required data

- **Instrument / universe:** common stocks on NYSE, AMEX and Nasdaq (Part 1: 31,000 names, approx. 24,000 of them delisted, i.e. survivorship-bias-free); Part 2: Russell 3000 constituents. Long-only, no shorting, no options, no derivatives.
- **Vendor:** **Norgate Database** end-of-day survivorship-bias-free data with delisted and merged securities (Section 2, footnote 2). The point-in-time **Russell 3000 membership source is not stated** -> `data gap`; without a point-in-time membership history the universe cannot be rebuilt without survivorship bias.
- **Market type / venue:** US listed cash equities; venue not specified beyond listing exchanges -> `data gap`.
- **Timeframe:** daily EOD bars plus next-day opening prices.
- **Fields:** adjusted and unadjusted close, high, low, volume (42-day average dollar volume; 30-day ADV and 30-day volatility for the I-Star impact model), corporate actions (splits, dividends), all-time-high history on adjusted closes, 42-day ATR, 42-day annualized volatility.
- **External series:** **CPIAUCSL** (FRED) for the inflation-decayed dollar-volume threshold; **Kenneth French data library** for the risk-free rate (cash interest and borrowing cost) and for the market-cap-weighted all-US-stock benchmark daily return (Sections 4.6, 4.7, footnote 8/10).
- **Point-in-time:** eligibility and signals are computed at the close and traded at the next open, so no same-bar look-ahead is claimed by the source. Whether Russell 3000 membership is used point-in-time or with a constituent lag is `not stated in source`.
- **Timestamp / timezone:** not stated -> `data gap`.
- **Missing data / delisting handling:** delisted names are included in Part 1 and corporate actions are adjusted, but the treatment of a position that delists while held (gap to cash, partial recovery, forced exit price) is `not stated in source` -> `data gap`.
- **Cost fields observed:** commission (per-share with a minimum), SEC clearing fee on sells, modelled market impact (I-Star), interest earned on cash, interest paid on borrowing. **Spread, latency, partial fills, exchange/marketplace fees, short borrow (long-only so not applicable), tax and turnover percentage are not modelled or not reported** -> `data gap` (never read as zero).

## Execution assumptions

Everything in this section is `source-reported` from Sections 3.3 and 4.7 unless marked.

- **Signal-to-order timing:** close-of-day signal -> **market-on-open order on t+1**; stop breach at the close -> **sell at the t+1 open** (soft stop, not a resting order; Section 4.4 footnote 7).
- **Fill model:** fills at the opening price; no partial fills, no queue position, no latency, no order-reject handling -> `data gap`.
- **Order type:** market-on-open. No limit orders, no VWAP/TWAP scheduling except the qualitative "distribute trades over multiple days" inside the undisclosed Turnover Control.
- **Statistical-study cost:** a flat **0.50% per round turn** deducted from each trade for commissions and slippage (Section 3.3), justified as a proxy for the whole 1950-2024 sample; footnote 5 on the same page argues 25 bps would be a reasonable conservative figure (contradiction recorded in frontmatter; only the applied 0.50% is used here).
- **Portfolio cost model (Section 4.7):**
  1. **Commission:** Interactive Brokers tier pricing, **$0.0035 per share**, **minimum $0.35 per transaction**; for sell transactions the source also accounts for **SEC clearing fees** and states it will "double the commission assumed for buy orders" (whether the doubling applies to the commission rate or to the combined charge is `underspecified`).
  2. **Slippage / market impact:** I-Star model of Kissell and Malamut - `I*_bp = a1 x (Q/ADV)^a2 x sigma^a3` with `Q` shares, `ADV` = 30-day average daily volume, `sigma` = 30-day price volatility, and the all-US-universe parameters **a1 = 708, a2 = 0.55, a3 = 0.71** (Section 4.7).
  3. **Interest:** cash earns the French-library risk-free rate; borrowing costs are **2x the risk-free rate with a minimum spread of 100 bps annualized**.
  4. **Shares:** the costed backtests disallow fractional shares; the theoretical backtest allows them.
  5. **AUM protocol:** eight portfolios from **$100,000 to $100,000,000**, and **AUM is reset to its original value at the start of every calendar year** (profits notionally distributed) - an artificial compounding construct the source states explicitly.
- **Leverage / margin:** long-only, gross exposure capped at **200%** "to comply with U.S. brokerage limits" (source-stated rationale, not sourced to a rule -> `not stated in source` for the regulatory citation).
- **Capacity / participation:** no explicit participation cap or ADV-percent limit; capacity enters only through the I-Star `Q/ADV` term -> partially `underspecified`.
- **Spread, latency, borrow availability, partial fills, exchange fees:** not modelled or not reported -> `data gap`.
- **Turnover:** no numeric turnover figure is printed anywhere; Figures 16-17 and 19 are chart-only -> `data gap`.

## Evidence

### Source-reported

Every figure below is `source-reported` from the pinned PDF (37 pages, SHA-256 `ae9b740c...`) and has not been independently reproduced.

**Part 1 - trade-level statistics, 1950-2024, approx. 66,000 simulated trades, flat 0.50% round-turn cost (Section 3.5, Figures 6-12):**

- Average return per trade **0.50R**; average winning trade **1.90R**; average losing trade **-0.70R**; **win rate 43.90%**; average winning-trade duration **370 calendar days**.
- **5,497 trades (8% of all trades)** lost more than the initial risk; **more than 14,800 trades (22%)** earned more than the risk taken.
- Sorted-cumulative decomposition: **56% of trades lost money**, about **37% roughly broke even**, and **less than 7% of trades generated all of the strategy's profits**.
- Average PnL per trade fell from **0.39R pre-2005** (before the Wilcox and Crittenden white paper) to **0.31R post-2005**, while average total return per year increased (Figures 9-10).

**Part 2 - Theoretical Trend Portfolio, January 1991 - October 2024, no costs, no slippage, no interest, fractional shares allowed (Section 4.6, Table 1, Table 2 bottom rows):**

| Row | CAGR | Vol | Sharpe | Sortino | MDD | Alpha | Beta |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Theoretical (Table 2/3 bottom row) | 15.02 | 14.93 | 0.85 | 1.11 | 31.75 | 6.19 | 0.66 |
| Market (French all-US-stock cap-weighted) | 11.18 | 18.19 | 0.54 | 0.68 | 54.68 | 0.00 | 1.00 |

- Prose in Section 4.6: strategy CAGR "approximately 15%" vs market CAGR 11.18%; Sharpe 0.85 vs 0.54; maximum drawdown "about 32%" vs "nearly 55%" for the market; **annualized alpha 6.19% with p-value 0.05%**.
- **Open risk** (NAV lost if every stop were hit the same day) "remains quite stable around **17%**" (Figure 14). Drawdowns can exceed open risk for three stated reasons: compounding of successive stop-outs, upward re-weighting of survivors while more than 200 names are held, and overnight gap-downs.
- Table 1 prints monthly and annual returns for 1991-2024; the 2024 row carries ten monthly cells (data end October 2024) with `Yearly 29.2` and `Mkt 22.5`.
- Average portfolio exposure is stated as roughly **120%** with an average beta of **0.63** after Turnover Control (Section 4.8 prose).

**Part 2 with costs, no Turnover Control - Table 2 (Section 4.7), Jan 1991 - Oct 2024:**

| AUM | CAGR | Vol | Sharpe | Sortino | MDD | Alpha | Beta |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.10M | 2.45 | 12.83 | 0.06 | 0.08 | 39.79 | -4.63 | 0.55 |
| 0.25M | 4.76 | 14.00 | 0.23 | 0.29 | 39.31 | -2.75 | 0.68 |
| 0.50M | 6.87 | 14.48 | 0.36 | 0.46 | 38.99 | -0.88 | 0.62 |
| 1M | 9.01 | 14.75 | 0.49 | 0.64 | 36.54 | 0.91 | 0.64 |
| 5M | 12.13 | 14.96 | 0.67 | 0.86 | 34.44 | 3.73 | 0.65 |
| 10M | 12.53 | 15.00 | 0.70 | 0.91 | 34.29 | 4.13 | 0.65 |
| 50M | 11.87 | 15.02 | 0.66 | 0.88 | 35.25 | 3.54 | 0.65 |
| 100M | 10.97 | 15.03 | 0.65 | 0.87 | 36.23 | 2.72 | 0.65 |
| Theoretical | 15.02 | 14.93 | 0.85 | 1.11 | 31.75 | 6.19 | 0.66 |
| Market | 11.18 | 18.19 | 0.54 | 0.68 | 54.68 | 0.00 | 1.00 |

Table 2 caption: "Alphas in bold are statistically significant at the 2.5% level" (which specific rows are bold cannot be recovered from the text layer -> `data gap`).

**Cost-drag decomposition (Figure 17, Section 4.7):** for the **$100,000** portfolio the yearly performance drag **exceeds 10%**, with **commissions accounting for more than 95%** of total cost; for the **$100 million** portfolio **slippage exceeds 3% per year**; the stated **sweet spot is about $10 million, where yearly cost drag is about 2.50%**.

**Turnover Control - Table 3 (Section 4.8), same window:**

| AUM | CAGR | Vol | Sharpe | Sortino | MDD | Alpha | Beta |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.10M | 12.97 | 14.23 | 0.75 | 0.98 | 32.97 | 4.94 | 0.59 |
| 0.25M | 13.49 | 15.12 | 0.75 | 0.98 | 33.98 | 5.00 | 0.65 |
| 0.50M | 13.30 | 15.04 | 0.74 | 0.97 | 33.59 | 4.83 | 0.65 |
| 1M | 13.40 | 14.92 | 0.75 | 0.98 | 32.91 | 4.93 | 0.64 |
| 5M | 13.48 | 15.10 | 0.75 | 0.97 | 33.45 | 4.86 | 0.65 |
| 10M | 13.38 | 15.12 | 0.74 | 0.97 | 33.33 | 4.86 | 0.65 |
| 50M | 12.84 | 14.95 | 0.72 | 0.93 | 33.18 | 4.47 | 0.64 |
| 100M | 12.43 | 14.72 | 0.70 | 0.91 | 32.30 | 4.28 | 0.64 |
| Theoretical | 15.02 | 14.93 | 0.85 | 1.11 | 31.75 | 6.19 | 0.66 |
| Market | 11.18 | 18.19 | 0.54 | 0.68 | 54.68 | 0.00 | 1.00 |

**Turnover Control effect (Figure 19, Section 4.8):** commission drag for the **0.10M** portfolio falls from roughly **10% to less than 1%** per year; slippage for the **100M** portfolio falls from **3% per year to 1.3% per year**; the 0.10M portfolio then even outperforms the 100M portfolio in total return (Figure 20).

**Alpha stability (Section 4.9):** yearly regressions of the theoretical portfolio's daily excess return on an **equally weighted Russell 3000** daily excess return; the cumulative abnormal return trends upward but is volatile; weak patches coincide with post-crash rebounds (**2009, 2020**) when the trend book sits in cash; **2024 annual alpha exceeds 15%**, attributed to 2024 cross-sectional dispersion.

### Independently reproduced

`not independently reproduced`

This run performed only source-side verification: direct browser read of the SSRN landing page, pinned-PDF download through the landing delivery link, page-by-page text extraction of all 37 pages, re-hash of the pinned file, arithmetic self-checks of the reported ratios (e.g. the 2024 Table 1 row compounds to the printed 29.2% partial-year figure), and hidden-inclusive source-identity dedup. **No backtest was run, no ledger was executed, no test suite was executed, and no table was recomputed.**

### Negative evidence

Numbered items are contiguous. Items 1-8 are the source's own negative results; the remainder are limitations, structural counter-evidence and unresolved gaps identified while reading the primary source.

1. **The costless edge does not survive small accounts.** At $100,000 AUM without Turnover Control, CAGR collapses from the theoretical 15.02% to **2.45%** and alpha turns **-4.63%** (Table 2) - the strategy is, in the source's own words, "not viable for smaller portfolios (AUM less than $1M)".
2. **Risk-adjusted return is non-monotonic in AUM.** Sharpe rises 0.06 -> 0.70 from 0.10M to 10M, then falls to 0.65 at 100M because of market impact (Table 2); there is no size at which the untuned model matches the theoretical Sharpe of 0.85.
3. **Persistent net-of-cost shortfall even after Turnover Control.** Table 3 tops out at CAGR 13.49% and Sharpe 0.75 versus the theoretical 15.02% / 0.85 - roughly 1.5 to 2.6 percentage points of annual drag remains at every tested size.
4. **The decisive mechanism is not disclosed.** Turnover Control thresholds are withheld (Section 4.8 footnote 11), so the improvement from Table 2 to Table 3 cannot be independently rebuilt; the headline "attractive across all tested portfolio sizes even after fees" rests on an `underspecified` rule.
5. **Per-trade profitability already decayed after publication.** Average PnL per trade fell from **0.39R to 0.31R** after the 2005 white paper (Section 3.5) - the source itself documents a roughly 20% decline in per-trade edge once the idea was public.
6. **Extreme tail dependence.** Fewer than **7% of trades** produce all profits and **56% of trades lose** (Section 3.5); the thesis fails outright if the right tail is truncated by costs, forced diversification, or exit rules.
7. **Stops leak on gaps.** **8% of trades (5,497)** lose more than the initial risk because of adverse overnight moves; drawdowns exceed the 17% open-risk budget (observed MDD 31.75% theoretical, 39.79% net at 0.10M).
8. **Recovery regimes are structurally missed.** Section 4.9 shows the cumulative abnormal return stalling in the 2009 and 2020 rebounds because the book is in cash - a known long-only trend failure mode.
9. **No out-of-sample test of the portfolio.** The tradable backtest runs once over the full 1991-2024 window; there is no holdout, no walk-forward, no embargo and no parameter sensitivity analysis (overfitting risk is `unproven`, not refuted).
10. **Parameters are fixed but not justified.** The 10xATR multiplier, 42-day ATR/vol/ADV windows, 30% volatility target, $10 price floor, $1M ADV floor and 200-name concentration floor are all stated without derivation or tuning disclosure -> `not stated in source`.
11. **Alpha column provenance is ambiguous.** Tables 2 and 3 do not name the regression behind `Alpha`, while Section 4.6 benchmarks a cap-weighted French index and Section 4.9 uses an equal-weight Russell 3000 -> the headline 6.19% and the 4.28-5.00% net alphas are not directly comparable -> `underspecified`.
12. **Bold-significance rows are unrecoverable.** "Alphas in bold are statistically significant at the 2.5% level" cannot be mapped to rows from the text layer -> `data gap`; no standard errors, t-statistics or confidence intervals are printed for CAGR, Sharpe or drawdown.
13. **Cost model gaps.** Spread, latency, order rejects, partial fills, marketplace/exchange fees, short-borrow availability (long-only) and tax are not modelled; the SEC-clearing / doubled-commission sentence is ambiguous; the flat 0.50% statistical-study cost is a single point assumption with no ladder.
14. **Turnover is never quantified.** No numeric daily trade count, annual turnover or participation rate is printed; Figures 16, 17 and 19 are chart-only -> `data gap`.
15. **AUM reset is artificial.** Resetting AUM to its original value every January decouples compounding from the reported CAGR and makes the eight AUM rows a controlled experiment rather than a real track record (source-disclosed, still a limitation).
16. **Universe survivorship for Part 2 is unresolved.** Part 1 uses a survivorship-bias-free Norgate panel, but the point-in-time Russell 3000 membership source for Part 2 is `not stated in source`.
17. **Sample-window inconsistency inside the PDF.** Section 2 says the database runs "1950 until August 2024" while the abstract and Section 1 say "through October 2024"; the landing says "November 2024".
18. **Landing-vs-PDF numeric divergence.** The landing abstract's 15.19% / 6.18% and the PDF's 15.02% / 6.19% cannot both describe the same pinned version -> unreconciled.
19. **Internal cost-text conflict.** 0.50% round turn (applied) versus the footnote's 25 bps "reasonable, conservative assumption" (not applied).
20. **Leverage without a financing stress test.** The book averages about 120% exposure and is capped at 200%; borrowing is charged at 2x risk-free with a 100 bps floor, but no stress of a rate shock or a margin-call/liquidation path is provided.
21. **Benchmark dependence of the headline claim.** The strategy's Sharpe 0.85 and alpha 6.19% are measured against a cap-weighted index whose own Sharpe is 0.54; against the equal-weight Russell 3000 used in Section 4.9 the same book looks materially different, and the source does not print that comparison as a table -> `data gap`.
22. **2024 dependence.** The source highlights 2024 alpha above 15% as evidence of robustness while also noting post-publication per-trade decay; a single dispersion-rich year is doing visible work in the narrative.
23. **No code, no data release, no third-party replication.** No repository, no scripts, no replication package, and `no independent third-party replication identified` in this run's searches.
24. **Conflicts of interest are structural.** Two authors are affiliated with the product side (Concretum Research; Longboard Asset Management runs a systematic US-equity strategy) and the withheld Turnover Control is described on contact; the paper is a non-peer-reviewed SSRN working paper with `All rights reserved. No reuse allowed without permission.`

## Falsification plan

Every threshold, sample split and failure rule below is a `research-defined falsification threshold` chosen by this Scout, not by the source. Items marked `research-proposed` add operational choices the source does not specify.

1. **F1 - Frozen forward replication (`research-defined`).** From **2026-10-01**, run the frozen rule (Signal section exactly as printed) for 24 months on point-in-time Russell 3000 membership. **Failure:** net-of-cost alpha versus the equal-weight Russell 3000 is <= 0 over the window, or realized one-way annual turnover exceeds the source's implied level by more than 2x. **Action:** mark the record `rejected` in a later update; do not advance.
2. **F2 - Source reproduction gate (`research-defined`).** Rebuild Table 2 and Table 3 from Norgate-grade data. **Failure:** the Theoretical row (CAGR 15.02, Sharpe 0.85, MDD 31.75, alpha 6.19) or any Table 2/3 row differs by more than **0.50 pp CAGR / 0.05 Sharpe / 1.00 pp alpha**. **Action:** treat the source numbers as unreproducible and downgrade all evidence to `unverified`.
3. **F3 - Cost ladder (`research-defined`).** Re-run at commission ladders of $0.0035 / $0.0070 / $0.0140 per share with minimums of $0.35 / $1.00, plus I-Star parameter perturbation of `a1` by +/-50% and a flat **25 bps** and **50 bps** round-turn overlay (to adjudicate the Section 3.3 vs footnote 5 conflict). **Failure:** any tested AUM's alpha is negative at the source's own $0.0035/$0.35 baseline, or the $10M sweet-spot drag exceeds **2.50%/yr**.
4. **F4 - Turnover Control ablation, the decisive test (`research-defined`, `research-proposed` implementation).** Because thresholds are withheld, implement a public proxy bundle (`research-proposed`): a rebalance band that skips weight changes below 10 bps of NAV, trade netting across names, a minimum trade notional of 0.5 bps of NAV, and 5-day execution spreading for trades above 25 bps of NAV. **Failure:** the proxy cannot bring the 0.10M net CAGR within **1.00 pp** of Table 3's 12.97 or reduce its commission drag below 2%/yr. **Action:** record that the paper's practical claim depends on undisclosed parameters and cannot be adopted.
5. **F5 - Turnover and capacity audit (`research-defined`).** Publish numeric daily trade counts and annual one-way turnover (the source prints none). **Failure:** at $10M the Turnover Control version still trades more than **400% one-way per year** or the largest single order exceeds **1% of 30-day ADV** in more than 5% of days. **Action:** capacity claim rejected.
6. **F6 - Point-in-time universe rebuild (`research-defined`).** Rebuild Part 2 with point-in-time Russell 3000 membership and the delisting-aware Norgate panel. **Failure:** alpha versus equal-weight Russell 3000 falls below **3.00 pp** or changes sign. **Action:** survivorship/mechanism claim rejected.
7. **F7 - ATH construction audit (`research-defined`).** Compare adjusted-close ATH (source) with unadjusted-price ATH and with dividend-reinvested ATH. **Failure:** the entry-signal set differs by more than **20%** of entries, or the sign of alpha flips. **Action:** the breakout claim is treated as data-construction dependent.
8. **F8 - Fill and gap realism (`research-defined`, `research-proposed` variants).** Replace next-open market-on-open fills with `research-proposed` next-open fills plus a 10 bp and 25 bp slippage term, and separately with a next-close fill. **Failure:** net CAGR at 0.10M or 10M falls by more than **2.00 pp** under either variant. **Action:** execution-fragile.
9. **F9 - Competing baselines (`research-defined`).** Race the strategy against (a) buy-and-hold Russell 3000, (b) equal-weight Russell 3000, (c) a 12-1 monthly time-series momentum rule on the same universe, and (d) the Keltner-Donchian industry-trend construction audited in the sibling repository record. **Failure:** the Turnover Control portfolio does not beat the equal-weight Russell 3000 by at least **1.00 pp CAGR** with a Newey-West t-statistic of at least **1.96** on daily excess returns. **Action:** no incremental alpha.
10. **F10 - Subperiod stability (`research-defined`).** Split 1991-2024 into 1991-2007, 2008-2015, 2016-2024. **Failure:** alpha is <= 0 in **at least 2 of 3** subperiods, or the post-2005 per-trade decay continues (post-2019 average PnL_R below 0.25R). **Action:** regime-fragile.
11. **F11 - Multiplicity control (`research-defined`).** Test the 8 AUM rows x 2 variants (with and without Turnover Control) as one family with Benjamini-Hochberg at **q < 0.10**. **Failure:** fewer than half the Table 3 rows survive, or the Theoretical alpha loses significance at 5%. **Action:** treat Table 3 as selection-affected.
12. **F12 - Rebalance-day sensitivity (`research-defined`).** Because daily ATH entries are calendar-driven, shift the eligibility/evaluation weekday by +/-1 trading day and add a 3-tranche staggered entry `research-proposed`. **Failure:** the CAGR range across schedules exceeds **100 bp**, i.e. rebalance timing luck is material relative to the claimed alpha. **Action:** report timing luck alongside every performance number.
13. **F13 - Data-vendor cross-check (`research-defined`).** Rebuild on an independent survivorship-free vendor (CRSP/Compustat-grade). **Failure:** sign change or more than **20% alpha loss** versus the Norgate build. **Action:** vendor-dependent.
14. **F14 - Crypto portability test (`research-defined`, `research-proposed` port).** Port the ATH + 10xATR ratchet + inverse-vol sizing rule to the top-40 liquid crypto perps with a 0/5/10 bps cost ladder and funding charged separately. **Failure:** net-of-cost Sharpe below **0.30** at 5 bps, or no positive-alpha cell after BH q < 0.10. **Action:** portability rejected; keep `unproven`.

## Crypto portability

**Marked `unproven`.**

The evidence is entirely US listed cash equities over 1950-2024; the source never tests crypto, so this is a **ported hypothesis, not crypto empirical evidence**.

- **Session structure:** US equities have one continuous regular session with an auction open; crypto trades 24/7. The "signal at the close, trade at the next open" rule has no clean counterpart - a 00:00 UTC candle boundary would have to be chosen (`research-proposed`), and the ATH/ATR windows would span a different number of calendar days.
- **ATH semantics:** many crypto perps are young listings with short price histories, so "all-time high" is measured over a much shorter and more manipulation-prone history; delisting and re-listing are common, breaking the monotone ATH series.
- **Funding and leverage:** the source models equity borrow at 2x risk-free with a 100 bps floor; crypto perp funding, mark/index price and liquidation mechanics have no counterpart and are not in the source's cost model at all.
- **Venue fragmentation / liquidity:** the I-Star parameters `a1=708, a2=0.55, a3=0.71` are fitted to the US stock universe and are not transportable to crypto books.
- **Long-only and leverage:** the 200% cap rationale (US brokerage limits) does not apply; margin, ADL and liquidation rules would replace it.

## Limitations

- `underspecified`: Turnover Control thresholds, the alpha regression behind Tables 2/3, the "double the commission" sell-side sentence, capacity/participation, and re-entry after a losing exit.
- `not stated in source`: parameter derivation, point-in-time Russell 3000 membership source, timezone and timestamp conventions, delisting-while-held handling, regulatory basis for the 200% leverage cap, any turnover statistic, any confidence interval for CAGR/Sharpe.
- `data gap`: no code, no replication package, no numeric turnover, no per-row significance in the text layer, no spread/latency/fill model, no peer-review statement.
- `not independently reproduced`: all performance figures are source-reported from the pinned PDF; nothing was recomputed beyond arithmetic consistency checks.
- `unproven`: crypto portability, out-of-sample persistence, and the claim that a public implementation of Turnover Control can reproduce Table 3.
- Source-quality: a non-peer-reviewed SSRN working paper with `All rights reserved` licensing, authored partly by the managers of systematic products; two of the six recorded contradictions (landing-vs-PDF abstract numbers, sample end date) sit directly on the headline claim.
- Incremental-write threshold: this capture adds a new source identity (SSRN 5084316) whose mechanism (single-name all-time-high time-series trend with inverse-vol sizing and an AUM-by-AUM cost audit) is materially different from every existing repository record; it is not a reframing of any existing artifact.

## Implementation status

`implementation_status: not-implemented`.

No implementation exists in our research stack: no Qlib full backtest, no production card, no Paper, Testnet or Live run, and no candidate-pool entry has been produced by this Scout. Nothing in this record implies Research Intake Review, Wiki Brain ingestion, survivor promotion, or trading approval. The record is a normalized research capture only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

Presence of this file in the staging repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet, or live trading. All of those stages remain separate and gated, and this Scout wrote none of them.

## Related Wiki records

Pre-write search of `/Users/hong/.hermes/wiki` for `5084316`, `Trend-Following Still Work`, `Crittenden` and `Longboard` returned **0 hits** - no Wiki Brain record exists for this source, and no page is fabricated here. Verified-existing adjacent pages used as retrieval hooks:

- `[[quant/strategy-research-record-spec-v1]]` - canonical record contract used for this capture.
- `[[quant/us-equity-vortex-top2-cross-sectional-trend-phase-robustness-2026-09-13]]` - adjacent US-equity trend record; different signal construction and source.
- `[[quant/llm-news-enhanced-cross-sectional-momentum-tilt]]` - adjacent momentum record that also cites the Concretum/Zarattini author line; different mechanism (LLM news tilt).

Four-axis distinction against the closest **repository** records (source identity and mechanism differ in every pair):

- `industry-trend-keltner-donchian-fallback-wfa-falsification-arxiv-2412.14361-2026-09-23.md` - arXiv 2412.14361 / SSRN 4857230 auditing an **industry-level** Keltner-Donchian rotation over 48 portfolios; this record is **single-name** all-time-high breakout with a 10xATR ratchet and a different source identity.
- `spy-intraday-momentum-noise-area-band-vwap-stop-dynamic-sizing-2026-09-23.md` - shares first author Zarattini but is SSRN 4824172, a **half-hour intraday SPY** rule with Noise Area bands and a VWAP stop; distinct horizon, universe and source.
- `ensemble-donchian-trend-following-crypto-top20-rotational-2026-09-20.md` - shares first author Zarattini (SSRN 5209907) but is **crypto top-20 rotational Donchian** trend; distinct asset class and channel construction.
- `pure-momentum-wild-bootstrap-drift-significance-filter-us-equities-2026-09-26.md` - same asset class but a **cross-sectional pure-momentum** hypothesis with bootstrap significance filtering; distinct signal construction and evidence type.

## Sources

1. Carlo Zarattini, Alberto Pagani, Cole Wilcox. *"Does Trend Following Still Work on Stocks?"* (PDF title block). SSRN abstract `5084316`, DOI `https://doi.org/10.2139/ssrn.5084316`, landing `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5084316`. PDF p.1 prints `First Version: November 26, 2024` and `This Version: January 17, 2025`; SSRN landing prints `Posted: 9 Jan 2025`, `Last revised: 17 Jan 2025`, `Date Written: January 06, 2025`, `37 Pages`, 9,736 downloads / 31,619 abstract views / 1 citation / 10 references observed 2026-09-27. Pinned PDF: 1,714,240 bytes, 37 pages, SHA-256 `ae9b740ccf82bdeb850aaaf3d86488e92203b1e357655ba9e6075d7999d1aa44`, retrieved 2026-09-27 through the landing `Open PDF in Browser` delivery link and text-extracted with `pypdf 6.16.2`. All Sections 1-5, Tables 1-3 and Figure captions were read; every quantitative claim above traces to Section 3.5, Section 4.6, Section 4.7 (Table 2, Figure 17), Section 4.8 (Table 3, Figure 19) or Section 4.9 of that pinned file.
2. Cole Wilcox and Eric Crittenden. *"Does trend following work on stocks?"* The Technical Analyst, 14:1-19, 2005 - the baseline white paper the source revisits; cited as reference [1] of source 1 and **not** used as an evidence source in this record.
3. Robert Kissell. *Algorithmic trading methods: Applications using advanced statistics, optimization, and machine learning techniques.* Academic Press, 2020 - cited by source 1 (reference [10]) for the I-Star impact model used in Section 4.7; cited here only to attribute the cost model.

No secondary summary, aggregator or model-generated abstract was used to fill any rule, parameter or performance figure in this record.
