---
schema: strategy-research-record-v1
title: Bitcoin Semivolatility Timing — Upside/Downside Exposure Management for Monthly BTC Returns
created: 2026-09-27
updated: 2026-09-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - bitcoin
  - volatility-management
  - semivolatility
  - risk-timing
  - single-asset
  - ssrn
status: research-only
confidence: medium
source_as_of: 2026-08-03
sources:
  - "Daniel Batista and Marcelo Fernandes, 'Upside risk and return timing in Bitcoin', SSRN preprint, 20 pages, posted 3 Aug 2026, DOI: 10.2139/ssrn.7226305, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7226305"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Semivolatility Timing — Upside/Downside Exposure Management for Monthly BTC Returns

## Provenance

- **Primary source:** Daniel Batista and Marcelo Fernandes, "Upside risk and return timing in Bitcoin."
  - **Complete author list (exactly as source):** two authors — Daniel Batista (PDF title block: `1` Université de Genève, `2` Swiss Finance Institute; SSRN author block: "Swiss Finance Institute; University of Geneva - Geneva School of Economics and Management"; corresponding author, `daniel.batistadasilva@unige.ch`) and Marcelo Fernandes (PDF title block: `3` Sao Paulo School of Economics, FGV; SSRN author block: "Getulio Vargas Foundation (FGV) - Sao Paulo School of Economics", `marcelo.fernandes@fgv.br`).
  - **Status / date:** SSRN landing page states verbatim "This is a preprint article, it offers immediate access but has not been peer reviewed."; **Posted: 3 Aug 2026**; **20 Pages**; PDF title block dated **"July, 2026"** (title-block month differs from the SSRN posting date; both recorded, neither reconciled by the source). SSRN suggested citation: "Batista da Silva, Daniel and Fernandes, Marcelo." **No journal, no volume, no DOI other than the SSRN DOI, no peer review.**
  - **Stable URL / DOI:** `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7226305`, `https://ssrn.com/abstract=7226305`, `http://dx.doi.org/10.2139/ssrn.7226305`.
  - **Public-use rights:** SSRN License Information on the landing page reads "All rights reserved. No reuse allowed without permission." This record therefore only normalises claims, rules and printed figure/table values; no source text is reproduced wholesale.
- **Pinned PDF (read in full for this record):** retrieved on **2026-09-27** through the SSRN "Open PDF in Browser" delivery link; **1,826,803 bytes**; **SHA-256 `4bafa7d03619787697a2cb7177ed548bd0e53923df84455841b62b8fe0951163`**; **20 pages**. Text was extracted page by page in the browser with pdf.js 3.11.174. Body text occupies **pp. 1–11**; **pp. 12–20 each contain one raster image and no text layer** (image captions/axis text are not machine-readable in this pin, so every figure-only value below is marked as figure-read or as a gap).
- **Data / code provenance as stated by the source:** "The data used in this study are publicly available from Yahoo Finance and CoinCodex. Replication code and processed data are available from the corresponding author upon reasonable request." **No public repository, no commit, no public code.**
- **Pre-write dedup (repo-wide, hidden-inclusive, deterministic):** `grep -rlE "7226305|Upside risk and return timing|semivolatility|Semi.?volatility|Batista|4891824|Semivolatility-managed portfolios" --hidden -I .` over the whole repository (all `*.md`, `*.csv`, `*.json`, `*.txt`, including `.mimo-worktrees/`, `.agents/`, `.hermes/`) returned **zero files**, and `coverage_manifest.csv` (1,088,787 bytes) returned **zero matches** for `7226305|semivolatility|Batista|Upside risk`.
- **Four-axis distinction against the nearest existing records** (source identity differs in every pair, and the mechanism differs too):
  - `crypto-cross-sectional-volatility-managed-momentum` (source: Ao Yang, *Finance Research Letters* 85, 107879, 2025) — cross-sectional **momentum** portfolio risk-managed by total volatility; this record is **single-asset BTC exposure timing by an upside/downside semivolatility ratio with no momentum leg**.
  - `crypto-cross-sectional-realized-signed-jump-good-bad-volatility` — jump-conditional cross-sectional pricing; mechanism is jump decomposition, not an exposure scaler.
  - `stablecoin-dry-powder-volatility-targeting-copula` — copula-routed stablecoin dry-powder targeting; different instrument set and different signal construction.
  - `crypto-risk-managed-tsmom-crash-state-de-risking-drawdown-control` — time-series momentum de-risking; this record has no directional forecast component at all.
- **Wiki Brain (read-only) pre-write search:** `kb_search "volatility managed portfolio Bitcoin semivolatility upside downside timing"` → **0 pages**; `kb_search "volatility management risk timing cryptocurrency"` → 10 pages, of which only verified adjacent pages are linked in `## Related Wiki records`. **No Wiki Brain write was performed.**

## Economic mechanism

### Source-reported

- Standard volatility management (Moreira and Muir, 2017) scales Bitcoin exposure **inversely with total variance**, which implicitly treats volatility spikes as adverse states. The authors argue Bitcoin is different: "in Bitcoin, volatility spikes are frequently due to price rallies, which typically indicate subsequent positive returns," because upside variation, not downside variation, often drives large BTC moves.
- The proposed rule is **semivolatility management** (Batista and Fernandes, 2025): scale exposure by the **upside-volatility-to-downside-variance ratio**, which the source says "reflects both skewness and downside risk concerns" (crediting Bianchi, De Polis and Petrella, 2022).
- Stated causal story for the gains: separating upside from downside variation "avoids indiscriminate deleveraging after upside-driven volatility shocks" and "maintains or even increases exposure when total volatility reflects subsequent positive returns."
- The source explicitly rules out two competing explanations: **(a) not volatility persistence** — BTC half-life estimates for realized variance and semivariance sit "close to the sample modes" of the 87-coin cross-section (Figure 3, p. 6); **(b) not linear return predictability** — predictive-regression coefficients on lagged downside and upside semivariances are "noisy and statistically insignificant, including those for Bitcoin," and the BTC adjusted R² is "slightly negative" (Figure 4, p. 7).
- Decomposition (Wang-Yan style, p. 4): annualized **return-timing component `+0.160`**, **volatility-timing component `-0.012`**, so "return timing accounts for more than the entire alpha of `0.148` per year." The source's own conclusion: the rule "does not generate alpha by systematically reducing risk; if anything, volatility timing slightly deteriorates BTC performance."

### Research interpretation

- **Falsifiable hypothesis:** for monthly BTC, `P(r_t > 0 | lagged realized upside variance in top decile) > P(r_t > 0 | lagged realized total variance in top decile)`, i.e. high-volatility months that are upside-driven are followed by positive months more often than high-volatility months in general. An exposure scaler monotone in the upside/downside (semi)volatility ratio therefore loads more capital in exactly those states.
- **Component roles (per README rule 8 — risk management is not automatically alpha):**
  - *Signal / rule family:* an **exposure scaler** applied to an otherwise long-only BTC holding. It carries **no directional forecast**; the source itself shows the linear predictability regression is null.
  - *Risk layer:* the 200% exposure cap and the inverse-variance scaling.
  - *Benchmark:* buy-and-hold BTC, plus the two ablation rules (total-variance, downside-variance).
  - Therefore the alpha claim, if any, is entirely **conditional risk-timing (skewness-conditional exposure)**, not forecast skill. Any later Intake decision should treat this as a volatility-targeting overlay hypothesis.
- **Expected ablation outcome:** replacing the ratio with total variance should destroy the gain (the source shows it does); flipping the ratio to downside/upside should produce a worse-than-benchmark result; if a flipped or shuffled rule performs comparably, the mechanism claim fails.
- **Prior plausibility caveat (Scout interpretation):** the equity literature cited by the source (Cederburg et al., 2020; Liu, Tang and Zhou, 2019) documents that volatility-managed results are fragile and leverage-dependent; the source's own Figure 7 says cumulative returns **rise** as the exposure cap rises, which is consistent with the gain being an exposure/leverage effect rather than a risk-reduction effect.

## Signal

- **Formation timestamp / frequency:** monthly rebalancing; "Managed strategies use information available up to month `t-1`" (Table 1 notes, p. 4). Realized (semi)variance measures are built **from daily returns**; the exact daily-to-monthly aggregation window and whether the month boundary is calendar-based are **not stated in source**.
- **Rule family (source-reported):**
  - `buy-and-hold` benchmark — full BTC exposure, no scaling.
  - `total volatility` — "scale the Bitcoin investment … by the inverse of the total variance" (Moreira-Muir, 2017).
  - `downside volatility` — "scale … by the inverse of the downside variance" (Wang-Yan, 2021).
  - `downside-and-upside volatility` — "the third considers the **upside-volatility-to-downside-variance ratio**" (p. 3). Figure 1 legend (figure-read, verbatim) labels the three managed curves `f(σ)`, `f(-)`, `f(√+/√-)`, i.e. the winning curve is indexed by a **square-root (volatility rather than variance) upside/downside ratio**; the prose on p. 2 instead says "the ratio of upside volatility to downside variance." **The prose and the figure legend are not identical; the exact functional form is therefore `underspecified` in this source.**
- **Exact transformation:** the source defers explicitly — "See Batista and Fernandes (2025) for details on how to run each strategy at the monthly frequency using realized measures based on daily returns." That companion working paper (SSRN 4891824) is a **separate source that was not opened for this record**, so its constants, normalization, demeaning, floor and any volatility-target denominator are **`not stated in source`** here.
- **Exposure cap:** "impose a maximum exposure of **200%**" (Table 1 notes); "our baseline specification caps exposure at 200%, corresponding to a maximum leverage of 100%, as in Batista and Fernandes (2025)" (p. 9).
- **Position floor / shorting:** **`not stated in source`.** The rules are described as scaling a Bitcoin investment, so a long-only `0–200%` range is the natural reading, but neither a zero floor nor an explicit prohibition of negative exposure is printed; shorting is never discussed.
- **Entry / exit / holding period:** one continuous BTC position rescaled monthly; no entry trigger, no stop, no take-profit, no re-entry rule exists in this design. Holding period = one month between rescalings.
- **Cross-sectional selection step (diagnostic only, not part of the BTC trading rule):** asymmetry measure `A_i = Pr(r_{i,t} > 0 | UV_{i,t-1} in top decile) - Pr(r_{i,t} > 0 | RV_{i,t-1} in top decile)` estimated on the **first half** of the sample, coins sorted into quartiles, performance compared **out-of-sample in the second half** (Equation 1, p. 4). BTC's `A_i` sits at the **83rd percentile** of that cross-sectional distribution (p. 5).
- **Parameter provenance:** the 200% cap is `source-reported` (chosen as in the companion paper); the choice to test monthly rather than weekly/daily is `source-reported`; any threshold, floor or normalization used later by us would be `research-proposed`.

## Required data

- **Instrument / universe:** Bitcoin (BTC), single asset; plus a **87-coin** cross-sectional panel for the diagnostic analysis.
- **Venue / market type:** **not stated in source.** Prices are pulled from **Yahoo Finance**, which the source says "sources crypto data from **CoinMarketCap**"; the robustness vendor is **Coin Codex**. No exchange, no order book, no funding, no open interest, no on-chain input is used.
- **Footnote 1 (p. 4) ticker list, verbatim set:** 1INCH, AAVE, ADA, ALGO, AMP, AR, ATOM, AVAX, AXS, BAT, BCH, BNB, BSV, CAKE, CFX, CHZ, CKB, CRO, CRV, CVX, DAI, DASH, DCR, DOGE, DOT, EGLD, ENS, ETC, ETH, FET, FIL, FLOW, FTT, GLM, GNO, GT, HBAR, HNT, ICP, INJ, IOTX, JST, KAVA, KCS, KSM, LDO, LEO, LINK, LPT, LTC, MANA, MX, NEAR, NEO, NEXO, OKB, PAXG, QNT, QTUM, RAY, RSR, RUNE, SAND, SHIB, SNX, SOL, SUN, TFUEL, THETA, TRX, TUSD, TWT, USDC, USDT, VET, WEMIX, XAUt, XCN, XDC, XEC, XLM, XMR, XRP, XTZ, ZEC, ZIL (86 non-BTC tickers; **Scout arithmetic**: 86 + BTC = the stated 87).
- **Timeframe / fields:** **daily** BTC (and cross-sectional) returns → **monthly** realized variance, realized upside variance, realized downside variance, monthly returns.
- **Timestamp / timezone:** **`not stated in source`** — no timezone, no candle-boundary convention, no 24/7 session handling is described for a market that trades continuously.
- **Sample period:** **`data gap` — the source never states a start or end date anywhere in its text.** The only dating evidence is figure-read: Figure 1's x-axis carries ticks `2015`, `2020`, `2025` (labelled "Date"), so the plotted window spans roughly 2015–2025/26; this is an approximate axis reading, **not a declared sample window**. The first-half/second-half split used for the 87-coin diagnostic inherits the same undeclared window.
- **Point-in-time / survivorship:** **`not stated in source`.** The 87-coin panel is described as "daily data for 87 crypto coins in Yahoo Finance" with no listing-date filter, no delisting handling, no as-of date of collection; the panel includes currently-pegged instruments (USDT, USDC, DAI, TUSD, PAXG, XAUt) whose cross-sectional variance/semivariance statistics are degenerate by construction (the source itself drops USDT and USDC from one scatter plot because their predictive-regression coefficients are `(46.73, -41.22)` and `(18.36, -15.26)`).
- **Missing-data handling:** **`not stated in source`.**
- **Vendor risk acknowledged by the source:** it cites Schwenkler, Shah and Yang (2026), "Aggregate confusion in crypto market data," *Management Science* Forthcoming, and states only qualitatively that "our quantitative results remain virtually the same using Coin Codex data" — **no numbers are printed for that robustness check** (`data gap`).

## Execution assumptions

- **Signal-to-order timing:** information through month `t-1`; rescaling "at the monthly frequency." **The exact rebalance date, clock time, and whether the rescale happens at month open, month close, or a VWAP are `not stated in source`.**
- **Order type / fill model:** **`not stated in source`.** No market-vs-limit discussion, no partial-fill or failure handling anywhere in pp. 1–11.
- **Fees / spread / slippage / impact / capacity:** **`data gap`.** The words for transaction cost, fee, bid-ask, spread, slippage, market impact, participation and capacity do not appear in the paper's text; **no cost figure is printed anywhere.** Nothing in this record may be read as "costs are zero."
- **Leverage / margin / borrow:** exposure capped at **200%**, i.e. up to **100% leverage** (source-reported). The financing cost of that borrowed 100%, the margin regime, and any liquidation rule are **`not stated in source`** (`data gap`).
- **Shorting / borrow availability:** **`not stated in source`.**
- **Funding:** no perpetual futures are used; funding is therefore **`not applicable` to the source's own design**, but becomes a first-order cost if the rule is ported to perps (see `## Crypto portability`).
- **Risk-free rate:** **`not stated in source`.** Scout arithmetic check on Table 1: `0.503/0.679 = 0.741`, `0.323/0.584 = 0.553`, `0.539/0.745 = 0.723`, `0.703/0.866 = 0.812`, i.e. every printed Sharpe equals `average return / volatility`, so the reported Sharpe ratios are consistent with an **implicitly zero risk-free rate** (Scout arithmetic, not a source statement).
- **Turnover:** **`not reported`** (`data gap`); without it the cost drag of a monthly rescale that can move exposure from 0% to 200% is unknown.
- **Latency:** **`not stated in source`** (immaterial at monthly frequency, but recorded rather than assumed away).

## Evidence

### Source-reported

All figures below trace to the pinned PDF (SHA-256 `4bafa7d0…0951163`) with page/table/figure provenance. **Third-party results; not our results.**

- **Table 1, p. 4 — "Performance of Bitcoin strategies."** Columns: `average return`, `volatility`, `Sharpe`, `Sortino`. Notes verbatim: "Average returns and volatilities are annualized and reported in decimal units. Managed strategies use information available up to month `t-1` and impose a maximum exposure of 200%."

| management strategy | average return | volatility | Sharpe | Sortino |
|---|---|---|---|---|
| buy-and-hold benchmark | 0.503 | 0.679 | 0.740 | 1.256 |
| total volatility | 0.323 | 0.584 | 0.554 | 0.900 |
| downside volatility | 0.539 | 0.745 | 0.723 | 1.386 |
| downside-and-upside volatility | 0.703 | 0.866 | 0.811 | 1.704 |

- **Wang-Yan alpha decomposition, p. 4 (source-reported):** annualized return-timing component `+0.160`; volatility-timing component `-0.012`; stated total alpha `0.148` per year.
- **Cross-sectional diagnostic, pp. 4–5 + Figure 2:** 87 coins; `A_i` asymmetry estimated on the first half, quartiles evaluated out-of-sample in the second half; **"on average, both volatility and downside-volatility management outperform downside-and-upside volatility management in every quartile"**, with smaller differences in the top quartile; the gains "clearly stand out for Bitcoin, even if they are not exactly unique." BTC's `A_i` = **83rd percentile**.
- **Mechanism diagnostics, p. 7 + Figures 4–5:** predictive regressions of next-month returns on lagged downside/upside semivariances are noisy and insignificant **including BTC**, and the BTC adjusted R² is **slightly negative**; separately, BTC lies "in the right tail" of the cross-sectional distribution of `Pr(positive return | past upside variance in top decile)` (numeric values not printed in text → `data gap`).
- **Regime split, p. 8 + Figure 6:** bull = "months in which the Bitcoin price index is above its trailing 12-month moving average." Semivol timing delivers "a Sharpe ratio similar to the buy-and-hold strategy in bull markets, while improving the Sortino ratio," and "both Sharpe and Sortino ratios are substantially higher in bear markets." **No numeric bull/bear Sharpe or Sortino values are printed in the text** (figure-only) → `data gap`.
- **Cap sensitivity, p. 9 + Figure 7:** "cumulative returns increase as we increase maximum exposure, indicating that gains are mainly due to higher exposure in favorable upside-volatility states rather than to risk reductions." Numeric values are figure-only → `data gap`.
- **Figure 1, p. 3 (figure-read):** x-axis labelled `Date` with ticks `2015`, `2020`, `2025`; y-axis `Cumulative returns` with ticks `0 … 2500`; legend labels `Benchmark`, `f(σ)`, `f(-)`, `f(√+/√-)`.
- **Publication/citation status:** preprint, not peer reviewed (explicit SSRN banner); SSRN page at read time showed **47 downloads, 110 abstract views, 0 citations, 8 references**.

### Independently reproduced

Not independently reproduced.

### Negative evidence

Numbered items; items 1–19 are `source-reported` (read out of the pinned PDF), items 20–24 are explicitly labelled.

1. The standard rule **fails** in BTC: total-volatility management lowers Sharpe from **0.740 to 0.554** and Sortino from **1.256 to 0.900** (Table 1).
2. Downside-volatility management is also unhelpful: Sharpe **0.723 vs 0.740** buy-and-hold (Table 1).
3. The headline win is **small in Sharpe terms**: **0.811 vs 0.740** (Scout arithmetic: +0.071 absolute, +9.6% relative) and **no statistical test of any kind is reported** — no t-statistic, no confidence interval, no Newey-West, no Jobson-Korkie/Memmel, no white-reality check anywhere in pp. 1–11.
4. The larger-looking number is the **Sortino** gain (1.704 vs 1.256), but Sortino divides by downside deviation only, and the source's own Figure 6 explanation says the rule wins mainly by cutting bear-market losses — so the headline is **metric-choice sensitive**.
5. **It is not a broad crypto anomaly.** Across the 87-coin panel, in **every quartile** of the asymmetry measure, volatility management and downside-volatility management **beat** downside-and-upside management on average out-of-sample (p. 5).
6. BTC's asymmetry measure is only at the **83rd percentile**, i.e. the source concedes BTC is "very pronounced, but not extremely so."
7. **No linear predictability**: predictive-regression coefficients insignificant including BTC, BTC adjusted R² slightly negative (p. 7). Any "forecast" framing of this rule is contradicted by the source itself.
8. **No unusual volatility persistence**: BTC half-life sits near the sample modes (Figure 3), so the persistence explanation is ruled out.
9. **The gain is exposure-driven, not risk-driven**: cumulative returns rise monotonically with the exposure cap (Figure 7), and the Wang-Yan volatility-timing component is **negative (-0.012)**. The rule earns more by being more long, not by controlling risk.
10. **Leverage up to 100% is used with no financing cost modelled** — the borrowed half of the 200% exposure is uncompensated in the reported numbers (`data gap`).
11. **Zero transaction-cost treatment**: no fee, spread, slippage, impact or capacity discussion and no cost number anywhere in the pinned PDF (`data gap`, never zero).
12. **Turnover is not reported at all** (`data gap`), so the cost drag of a rule that can swing exposure across the 0–200% band monthly is unquantified.
13. **Sample period is never stated** (`data gap`) — the single largest provenance gap; only Figure 1's axis (2015/2020/2025) dates the exercise approximately.
14. **Bull-market Sharpe is not better than buy-and-hold** (p. 8); the entire Sharpe edge must therefore come from the bear regime, i.e. one regime out of two.
15. **Vendor/index risk is acknowledged but not quantified**: Yahoo Finance ← CoinMarketCap data, robustness to Coin Codex asserted only as "virtually the same" with no numbers, while the source itself cites Schwenkler et al. (2026) on "aggregate confusion in crypto market data" (`data gap`).
16. **Single asset, single frequency, single rule family**: one monthly BTC series; no alternative horizon, no alternative market, no cross-venue check.
17. **The executable rule lives in a different paper**: exact construction is delegated to Batista and Fernandes (2025), SSRN 4891824, which was not opened for this record; the prose ("upside volatility to downside variance") and the Figure 1 legend (`f(√+/√-)`) are not identical → `underspecified`.
18. **A single first-half/second-half split** for the 87-coin diagnostic, with no rolling re-estimation, no multiple-testing correction across 87 coins × 3 rules, and no reported dispersion of the quartile differentials.
19. **No public replication code** — "available from the corresponding author upon reasonable request" — so no independent verification path exists today.
20. *Scout-labelled:* **Preprint status** — explicitly "has not been peer reviewed"; 11 body pages, 8 references; SSRN licence "All rights reserved. No reuse allowed without permission."
21. *Scout-labelled:* **Risk-free rate and Sharpe construction are not stated**; the printed Sharpes are reproducible only under `rf = 0` (Scout arithmetic, above), which overstates nothing for BTC but is undocumented.
22. *Scout-labelled:* **Survivorship/point-in-time**: the 87-coin Yahoo panel has no listing-date or delisting treatment, and the paper drops two degenerate stablecoins from one plot while keeping them in the panel elsewhere.
23. *Scout-labelled:* **AI-assisted authorship disclosed**: the source declares use of OpenAI's ChatGPT "to improve language and readability and to assist with code review."
24. *Scout-labelled:* **No third-party replication identified** in the reviewed sources; absence of a replication is not evidence that replication would fail or succeed.

## Falsification plan

All thresholds below are **`research-defined falsification thresholds`** and all operational choices not printed by the source are **`research-proposed`**. Data = daily BTC closes from at least two independent vendors plus the source's own vendor; frequency = monthly, matching the source.

- **F1 — Frozen forward replication.** Pre-register the rule (exact form must first be recovered, see F2) and rebalance from **2026-10-01** for **≥ 24 months**. **Fail** if, over that window, the semivolatility rule's annualized Sharpe ≤ buy-and-hold Sharpe.
- **F2 — Sample-window and rule-recovery gate.** Obtain the exact start/end dates and the exact transformation (either from the authors or by reproducing Table 1 from the Yahoo series). **Fail** if the declared window cannot be recovered to **±1 month**, or if Table 1's four Sharpe ratios cannot be reproduced within **±0.03** (`research-defined`). An unrecoverable rule is itself a fail for implementability.
- **F3 — All-in cost ladder.** Apply **0 / 5 / 10 / 20 / 50 bps per side** to measured turnover. **Fail** if the Sharpe advantage over buy-and-hold is erased at or below **20 bps** (`research-defined`).
- **F4 — Turnover and capacity audit.** Report annual one-way turnover of each managed rule. **Fail** if turnover exceeds **100% per year** while no sub-5 bps execution path is documented, or if a 10% participation cap makes the strategy infeasible (`research-defined`).
- **F5 — Decisive mechanism ablation (four-way).** Run (a) total-variance scaling `f(σ)`, (b) downside-only `f(-)`, (c) **sign-flipped** `f(√-/√+)`, (d) month-shuffled exposure series, all at the same 200% cap. **Fail the mechanism** if (c) or (d) lands within **0.05 annualized Sharpe** of the published rule, or if (a) matches it — i.e. if the *direction* of the upside/downside ratio does not matter, the skewness-conditional story is dead (`research-defined`).
- **F6 — Conditional-probability mechanism test.** Estimate `Δ = Pr(r_t > 0 | UV_{t-1} top decile) - Pr(r_t > 0 | RV_{t-1} top decile)` on ≥ 120 months. **Fail** if a 95% stationary-block-bootstrap CI for `Δ` includes **0** (`research-defined`).
- **F7 — Data-vendor robustness.** Recompute Table 1 from Binance/Coinbase or CoinGecko daily closes as well as Yahoo. **Fail** if the Sharpe differential vs buy-and-hold changes sign or falls by more than **50%** (`research-defined`).
- **F8 — Point-in-time universe rebuild.** Rebuild the 87-coin panel with listing-date-aware, delisting-aware sampling and degenerate-asset exclusion declared ex ante. **Fail** if the top-quartile advantage reported on p. 5 disappears (`research-defined`).
- **F9 — Leverage-cap sensitivity.** Repeat with caps at **100% / 150% / 200% / 300%**. **Fail** if the Sharpe gain exists only at **≥ 200%** exposure (`research-defined`) — that would reclassify the result as a leverage artefact rather than a timing effect.
- **F10 — Statistical significance.** Paired monthly-return differential (semivol vs buy-and-hold) with Newey-West/HAC lags = 12: **fail** if `|t| < 1.96`, and report a 95% block-bootstrap CI that must exclude 0 (`research-defined`).
- **F11 — Subperiod / regime stability.** Split the recovered sample into **≥ 3** subperiods plus bull/bear halves by the source's own trailing-12-month MA definition. **Fail** if **≥ 2** subperiods show a negative differential (`research-defined`).
- **F12 — Placebo null.** **1,000** circular-shift permutations of the exposure series. **Fail** if the observed differential does not exceed the **95th percentile** of the null (`research-defined`).
- **F13 — Cross-sectional breadth with multiplicity control.** Re-run the quartile test on a pre-declared top-20 liquid-coin panel and apply Benjamini-Hochberg at `q < 0.10`. **Fail** if no quartile survives — the source's own Figure 2 already predicts this failure, so confirming it downgrades the record to a BTC-only curiosity (`research-defined`).
- **F14 — Reproducibility gate.** After F2, a second independent implementation must match Table 1's four Sharpe and four Sortino values within **±10%** (`research-defined`).
- **Action on failure:** any of F1, F5, F6, F10 failing ⇒ reject the mechanism claim; F3/F4/F9 failing ⇒ reject implementability as stated (leverage- and cost-dependent); F7 failing ⇒ reject the data provenance; F13 failing ⇒ keep only as single-asset BTC observation, never as a crypto-wide factor.

## Crypto portability

**direct.**

The evidence base is itself Bitcoin: a single crypto asset, crypto prices, and a rule applied at crypto trading frequency, so no asset-class porting assumption is required. The source does **not** use perpetual futures, so `funding` is `not applicable` **inside the source's own design** — but it becomes a first-order cost the moment the ≤200% exposure is implemented on perps instead of spot/margin. Residual gaps even within this `direct` setting:

- **Spot vs perpetual / funding / mark price / liquidation:** `data gap` — the source names no venue and no instrument type; implementing 100% leverage on a perp introduces funding, mark-price and liquidation dynamics that the reported Sharpe/Sortino never see.
- **24/7 session structure:** `data gap` — no timezone, candle-boundary or month-boundary convention is stated for a market that never closes; "month `t-1`" is undefined for a 24/7 series.
- **Venue fragmentation / index construction:** `data gap` — Yahoo Finance ← CoinMarketCap is a composite index, not an executable price; a tradable BTC leg will differ from the measured leg.
- **Borrow / margin cost for the borrowed 100%:** `data gap`.
- **Custody / withdrawal / venue risk:** `not stated in source`.

`direct` describes the evidence domain only. It is **not** authorization to trade, and not a claim that the numbers survive costs.

## Limitations

- **`data gap` — sample period never stated** (only Figure 1's `2015/2020/2025` axis, figure-read).
- **`underspecified` — exact rule transformation** delegated to a companion working paper (SSRN 4891824) not read for this record; the prose ratio and the Figure 1 legend `f(√+/√-)` differ.
- **`data gap` — all transaction-cost, spread, slippage, impact, capacity, financing and turnover fields**; nothing may be inferred as zero.
- **`data gap` — no statistical significance, confidence intervals, or multiplicity control** anywhere in the source.
- **`data gap` — bull/bear and cap-sensitivity numeric results** are figure-only in this pin (pp. 12–20 carry raster images with no text layer).
- **`not stated in source`** — venue, instrument type, timezone, position floor, shorting, risk-free rate, rebalance timing, missing-data handling, point-in-time universe construction.
- **`not independently reproduced`** — we ran no backtest, opened no code, and have no code to open.
- **`unproven`** — the causal channel (asymmetric conditional sign probability) is asserted from figure-read distributions, not from a printed conditional-probability table with uncertainty quantification.
- **Single asset, single frequency, single split** — one BTC monthly series, one first-half/second-half diagnostic split, one cap choice.
- **Source-quality:** SSRN preprint, not peer reviewed, 0 citations at read time, AI-assisted drafting/code-review disclosed, thin (8-item) reference list.
- **Publication-bias / selection:** the paper is a short positive-result note; the negative cross-sectional result is reported but the headline framing remains BTC-specific.

## Implementation status

`implementation_status: not-implemented`. **Nothing has been implemented in our research stack.** No signal code was written, no data was downloaded, no backtest was run, and no Qlib, Paper, Testnet or Live stage was touched by this record. The only actions taken were: reading the primary source, hashing the pinned PDF, and running read-only repository and Wiki Brain dedup searches. Replication code for the source itself is **not public** ("available from the corresponding author upon reasonable request").

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. The presence of this record in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. No wording, evidence count or figure in this record promotes itself, and the reported Sharpe/Sortino are third-party preprint claims that have not been reproduced.

## Related Wiki records

Verified by `kb_search` in this run (read-only; no page was written):

- [[quant/stablecoin-dry-powder-volatility-targeting-copula-2026-09-01]] — adjacent family: volatility-targeted exposure control in crypto.
- [[quant/market-regime-routed-specialist-gbt-asymmetric-hysteresis-2026-09-12]] — adjacent family: regime-conditional exposure routing with volatility targeting.
- [[quant/crypto-volatility-risk-premium-variance-swap-estimator-fragility-decay-2026-09-12]] — adjacent family: crypto volatility as the return source being harvested.

A search for the exact mechanism (`semivolatility`, upside/downside timing on Bitcoin) returned **0 pages**, so no identical or near-identical Wiki record exists.

## Sources

- Daniel Batista and Marcelo Fernandes, "Upside risk and return timing in Bitcoin," SSRN preprint, 20 pages, **Posted 3 Aug 2026** (PDF title block "July, 2026"). DOI: `10.2139/ssrn.7226305`. Landing page: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7226305. Pinned PDF read 2026-09-27: 1,826,803 bytes, SHA-256 `4bafa7d03619787697a2cb7177ed548bd0e53923df84455841b62b8fe0951163`. Provenance for every number above: **Table 1 (p. 4)**, decomposition paragraph (p. 4), footnote 1 (p. 4), Equation 1 and quartile discussion (pp. 4–5), Figure 1 (p. 3, figure-read), Figure 2 (p. 6), Figures 3–4 (pp. 6–7), Figure 5 and regime discussion (p. 8), Figure 6 (p. 8), Figure 7 and cap discussion (p. 9), Data availability and AI declaration (p. 10), References (pp. 10–11).
- Works **cited by the source** for the rule families and the data-quality caveat, **not read for this record** and carrying no imported numbers here: Moreira and Muir (2017), *Journal of Finance* 72, 1611–1644; Wang and Yan (2021), *Journal of Banking and Finance* 131, 106198; Barroso and Santa-Clara (2015), *JFE* 116, 111–120; Cederburg, O'Doherty, Wang and Yan (2020), *JFE* 138, 95–117; Bianchi, De Polis and Petrella (2022), SSRN 4182040; Batista and Fernandes (2025), "Semivolatility-managed portfolios," SSRN 4891824; Schwenkler, Shah and Yang (2026), "Aggregate confusion in crypto market data," *Management Science* Forthcoming.
