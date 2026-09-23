---
schema: strategy-research-record-v1
title: Fractional-Momentum Cross-Sectional Equity Factor (Fractional-Difference Filter Score) with Weekly Rebalance and Crash-Drawdown Mitigation
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cross-sectional-momentum
  - fractional-differencing
  - us-equity
  - ssrn-source
status: research-only
confidence: medium
source_as_of: 2022-11-23
sources:
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4280465 (SSRN abstract_id=4280465, DOI 10.2139/ssrn.4280465)"
  - "https://doi.org/10.2139/ssrn.4280465"
  - "https://www.sfi.ch/en/publications/n-22-87-momentum-without-crashes (Swiss Finance Institute Research Paper No. 22-87)"
  - "https://ideas.repec.org/p/chf/rpseri/rp2287.html (RePEc handle for the same working paper)"
  - "https://ideas.repec.org/a/taf/apeclt/v32y2025i18p2664-2668.html (Kim & Kim 2025, Applied Economics Letters 32(18):2664-2668, DOI 10.1080/13504851.2024.2337329 — contrary/rebalancing-frequency evidence, abstract only)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Fractional-Momentum Cross-Sectional Equity Factor (Fractional-Difference Filter Score) with Weekly Rebalance and Crash-Drawdown Mitigation

## Provenance

- **Source type:** public working paper on SSRN in the Swiss Finance Institute research-paper series (grey literature; **journal/peer-review status: `not stated in source`** — the paper asserts no journal reference, DOI other than the SSRN DOI, or acceptance).
- **Exact title:** *Momentum Without Crashes*.
- **Complete author list exactly as the source (PDF cover page 1 and title page, p. 2):** Soros Chitsiripanich (University of Zurich); Marc S. Paolella (University of Zurich; Swiss Finance Institute); Pawel Polak (Stony Brook University — Department of Applied Mathematics and Statistics; Institute for Advanced Computational Science); Patrick S. Walker (University of Zurich; Swiss Finance Institute per PDF cover). **No other authors.** The PDF footnote marks Chitsiripanich, Polak and Walker with "∗These authors contributed equally" and names Pawel Polak as corresponding author (`pawel.polak@stonybrook.edu`). **Provenance inconsistency (recorded, not repaired):** the SSRN metadata block lists Walker's affiliation as "University of Zurich; OLZ AG", which differs from the PDF cover; the SFI landing page lists authors in the order "M. Paolella, S. Chitsiripanich, P. Polak, P. S. Walker", which differs from the PDF order.
- **Version / date:** Date Written **November 14, 2022** (PDF title page); SSRN **Posted 18 Nov 2022, Last revised 23 Nov 2022**, **53 pages**; Swiss Finance Institute Research Paper **No. 22-87**; SFI landing page date **10 Nov. 2022**. The SSRN abstract page, SFI page and RePEc record all describe this same version; **no later version was located**.
- **Primary artifact actually read:** SSRN PDF delivery URL `https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID4283823_code623849.pdf?abstractid=4280465&mirid=1&type=2`, downloaded **2026-09-23**, **4,982,327 bytes**, **SHA-256 `3257d72c1e38d2b931838b311821f65a45b43cab890c6589d7f4d6c5a3430ab2`**, **53 pages**, text-extracted and read directly (abstract, §1 opening, §2.1–§2.3, §3.1, §3.2, §3.4, §3.5.1, §3.6.1–§3.6.3, §3.7, §3.8, §4, and Tables 1, 2, 3, 4, 5, 6 including captions). **Appendices A–B and the reference list were not reviewed → `data gap` for any appendix-only claim; no claim in this record depends on them.**
- **Sample period as stated in the source — internally inconsistent (recorded, not repaired):** §3.1 Data says the sample "begins in January 1972, ends in December 2020 … totals 48 years and 24,098 securities"; Tables 1, 2, 3 and 4 captions say **January 1973 to December 2020**; Figures 4, 5, 6, 11, 12, 14–17 captions say **January 1972 to December 2020**; Table 5 caption says **Jan 1972 – Dec 2020**. 1973→2020 is 48 years, matching the "48 years" statement, so the start year is `underspecified` / `contradictory within source`. International sample (§3.8, Table 6): "at the earliest, from September 1990 until March 2022", market-dependent (per-panel windows printed in Table 6).
- **Code / data availability:** the paper states it evaluates truncated fractional differences with the FFT method of Jensen and Nielsen (2014) "in our implementation" but **states no code URL in the sections read**; a repository search on 2026-09-23 located **no public code artifact** for this paper (search was keyword-based, not exhaustive → `data gap`). Data are proprietary CRSP and Compustat.
- **Deduplication (this run):** deterministic source-identity search across **all 905 `*.md` files** in the repository (identity index of 484 arXiv IDs, 853 DOIs, 50 SSRN IDs, 216 GitHub orgs/repos, 2,833 URLs, 903 titles) plus direct content `ripgrep` for `4280465`, `10.2139/ssrn.4280465`, `Chitsiripanich`, `Momentum Without Crashes`, `fractional momentum`, `rp2287`, `Swiss Finance Institute Research Paper` → **no existing record for this source identity**. `git log --oneline -20` was inspected as a convenience glance only and does not constitute dedup. Nearest neighbours are different sources with different mechanisms (see **Related Wiki records**).
- **Wiki Brain spec resolution (local Scout):** `kb_read quant/strategy-research-record-spec-v1.md` (sha256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`) is the canonical spec used here; `kb_search "strategy-research-record-spec-v2"` → **0 results**, so no newer contract exists.
- **Review date of every external page cited here:** 2026-09-23.

## Economic mechanism

### Source-reported

The authors' stated rationale: classical cross-sectional momentum uses only the first and last price points of the lookback window, which they describe as "too stringent a transformation". They apply the **fractional-difference filter** `(1−B)^d` to log-prices, forecast the resulting (assumed covariance-stationary) series by its sample mean, then invert the filter to obtain a one-step-ahead **predicted log-return**, and rank stocks by that prediction. The weighting scheme therefore "incorporates all the price data, over the entire lookback period". They give it an economic reading: for `d ∈ (0,1)` the forecast decomposes into a **mixture of momentum signals over different subperiods** plus a **mixture of short-horizon reversal signals with rapidly decaying weights** (§2.3), so the factor "coherently combin[es] reversal and momentum patterns in the returns". Their empirical claim is that this raises risk-adjusted returns **and** shallows the drawdowns ("crashes") of classical momentum and of short-term reversal, with results "robust with respect to transaction costs and other real world frictions" (Abstract).

### Research interpretation

- **Hypothesized mechanism (falsifiable form):** *signal-construction* improvement rather than a new risk premium. Fractional weights `π_s = (−1)^s · ∏_{i<s}(d−i)/s!` decay polynomially (~`s^{d−1}/Γ(d)`), so the score is a damped path-average of prices instead of an endpoint difference. Two candidate channels must be separated: (i) **richer extraction of persistent drift** across the whole window, and (ii) an **implicit short-term reversal tilt** that is always present for `d < 1`. The source supports (ii) analytically (§2.3, decomposition (13)) and via correlations (Table 5: weekly, FF universe — the `d=0.9` long-short series correlates **−0.22** with `d=0` reversal and **+0.42** with `d=1` classical momentum), but it reports **no component-ablation P&L**, so the attribution between (i) and (ii) is **not identified in the source** → ablation is mandatory (see Falsification plan).
- **Crash-mitigation claim as a mechanism, not a result:** the drawdown reduction is attributed to the score being less endpoint-driven and hence less exposed to the violent winner/loser rotation that produces momentum crashes (Daniel–Moskowitz style). This is the authors' interpretation; it is **source-reported as a hypothesis**, and only the reported drawdown numbers are source-reported as evidence.
- **Component roles (hybrid structure preserved):**
  - Signal construction: fractional-difference predicted-return score (`d`, `τ`, full-history mean).
  - Cross-sectional selection: sort ascending; long the top `q` fraction, short the bottom `q` fraction (dollar-neutral).
  - Weighting: value-weight (market cap) or equal-weight — the source tests both.
  - Rebalance/holding cadence: weekly, with five overlapping daily-formed sleeves averaged to remove the weekday effect.
  - Risk layer: dollar-neutral long-short (plus a separate long-only variant, §3.7). **No regime filter, no stop, no volatility targeting, no sizing overlay in the source.**
- **Confound flagged for reviewers:** because the reported optimum `d ∈ [0.8, 0.9]` sits close to classical momentum, an alternative explanation is "classical momentum plus a small reversal overlay", not a genuinely better momentum estimator. The source does not run that head-to-head component test after costs.

## Signal

All items below are **source-reported unless explicitly labelled otherwise**.

- **Formation timestamp:** portfolios are formed **each trading day** from the previous close of the dividend/split-adjusted total-return price series (§2.2, §3.1); positions are held for **one week** and recomputed at rebalance. Weekday neutralisation: "we follow the methodology used by Jegadeesh and Titman (1993) and Moskowitz et al. (2012) to form these quintile portfolios every day and average the return across the five implementations, corresponding to five trading days in one week" (§2.2). **Tradability convention:** headline results assume trades execute **at the closing prices used for portfolio estimation**; §3.6.3 adds explicit 1-, 2- and 3-day implementation lags (Figure 13) and reports that performance deteriorates clearly at 2–3 day lags while the fractional-vs-classical ordering is preserved. Timezone/session convention: US exchange session, close-based; **the paper does not state a timezone string** → `data gap` (implied US equity trading calendar).
- **Lookback:** "For the size of the moving window (τ), we select the single value **τ = 250 days**, this being consistent with the common one-calendar-year lookback period" (§2.2). The sample mean of the fractionally differenced series in the *non-truncated* formulation uses **all available history**, not only the τ-window (§2.2, case 4, weights (11)) → the effective memory is full-history with polynomially decaying weights. Warm-up / minimum history before a stock first enters a sort: **not stated** → `data gap`. Endpoints inclusion convention for the τ-window: not explicitly stated → `underspecified`.
- **Long entry:** buy the stocks with the **highest predicted return**, i.e. the top `q` fraction of the ascending sort.
- **Short entry:** sell short the **bottom `q` fraction** (lowest predicted return). Portfolio is described as **dollar-neutral long-short** ("High–Low").
- **Portfolio concentration `q`:** the source evaluates **`q ∈ {0.2, 0.4, 0.6}`** of the universe (§3.2; `q = 0.4` = top/bottom quintiles). **Table 4 uses a different concentration:** FM, MOM and STR are set to `q*`, the average concentration of the STRMOM benchmark, which the source measures at **12%–17% of the universe depending on the universe**; Table 6 uses **`q = 0.2`**. Both are source-specified, but they are **not interchangeable** — any reproduction must state which table it targets.
- **Scoring parameter `d`:** a **single common market parameter** applied to every asset; the source sweeps **`d = 0, 0.1, …, 1.0`** and reports the optimum at **`d = 0.9`** for the long-short variants and **`d = 0.8`** for the long-only variant (§3.7). Tables 1, 2, 3, 4 and 6 fix **`d = 0.9`**. The `d = 0` boundary is a reversal ensemble and `d = 1` is exactly classical Jegadeesh–Titman momentum (§2.2). Values of `d` outside `[0,1]` were tried and reported as "blatantly inferior out-of-sample" (§2.1).
- **Weighting within portfolio:** value-weight by market capitalisation, or equal-weight; the source reports both and finds equal-weight materially stronger.
- **Exit / holding period / cadence:** **one week** (5 trading days) then re-sort; overlapping sleeves are averaged, i.e. the reported series is a **five-sleeve average portfolio**, not a single realised book → single-sleeve results would differ (`underspecified` for a single-book implementation).
- **Rebalancing frequency variants:** weekly (headline), monthly (§3.6.1), plus long-only (§3.7).
- **Position sizing:** within-sleeve weights only (cap-weight or equal-weight). **No leverage, no gross-exposure scaling, no risk targeting, no cash buffer** is specified → `not stated in source`.
- **Ties, suspensions, unpriced stocks, delistings, entry-price rules for partial histories:** **not stated** → `data gap`. Any choice here is **`research-proposed`**, not source-reported.
- **Reproducibility verdict:** the *mathematical* score and the portfolio construction are reconstructible from §2 (equations (5)–(13)); the *data-engineering* layer (warm-up, ties, delisting returns, missing days) is **underspecified**, so this record does **not** present the signal as fully reproducible.

## Required data

- **Instrument / universe (US):** ordinary common shares incorporated in the US on **NYSE, AMEX, NASDAQ**, **CRSP share codes 10 and 11**; foreign shares, certificates, ADRs, shares of beneficial interest, depository units, trust components, closed-end funds and REITs filtered out (§3.1).
- **Two source-defined universes:** (i) **FF universe** — Fama–French (1993)-style, "approximately **2000 to 5500 stocks at each point in time**"; (ii) **AMP universe** (Asness–Moskowitz–Pedersen, top **90% of total market capitalisation** on each rebalancing date), "around **500 to 1000 assets** at each point in time" (§3.1). The source states both universes are changing over time and therefore "free from survivorship bias" (**source-reported claim**, not independently verified here).
- **Venue / market type:** US listed equity **spot**, daily bars; long-short requires a shortable-book assumption the source does not make explicit → `data gap`.
- **Fields:** daily total-return adjusted price `p_{t,i}` (constructed from the total-return series, accounting for splits, stock dividends and cash dividends — §3.1); market capitalisation for value weighting; **no volume, order-book, funding, borrow, open-interest or options fields are used.**
- **International extension (§3.8, Table 6):** **Compustat** daily data, Issue Type Code 0, adjustments via cumulative adjustment factor **AJEXDI** and daily total-return factor **TRFD**; universes = top **90%** of that country's market cap (Brazil **95%**, to avoid universes that "in some rolling windows go[] even below 10 stocks"); six countries — Brazil (01/2000–03/2022), France (09/1990–03/2022), Germany (03/1994–04/2021), Hong Kong (10/1995–03/2022), Japan (11/1990–09/2021), U.K. (04/1995–09/2021) (per Table 6 panel captions). Average number of stocks: Brazil 38, France 73, Germany 65, Hong Kong 45, Japan 615, U.K. 208 (§3.8).
- **Point-in-time / availability:** formation uses only past closes of the adjusted series; the source reports a replication check against Kenneth French's daily momentum factor (mean difference of the six size×momentum portfolios **2.6%** over the sample — §3.1). Publication-lag issues do not apply (prices only). **Corporate-action handling:** stated (adjusted total-return series). **Delisting / removal handling: not stated** → `data gap`.
- **Timestamp / timezone:** daily US equity trading calendar; no timezone string given → `data gap`.
- **Missing data:** **no null/stale/halt/suspension/imputation policy is stated** → `data gap`.
- **Funding / fee / spread needs:** only a **flat linear turnover cost** is modelled (see Execution assumptions). Borrow fees, stock-loan availability, bid-ask spread by name, and financing on the short leg are **not stated in source** → `data gap`, **not** to be read as zero.

## Execution assumptions

Distinguishing what the source assumes from what is unknown:

- **Signal-to-order timing:** same-close execution in all headline results (source), with 1/2/3-day lags reported separately in §3.6.3 / Figure 13 — **clear deterioration at 2–3 days, ordering preserved** (source-reported).
- **Order type / fill model / latency / partial fills / failed trades:** **not stated in source** → `underspecified`. Fills are implicitly assumed at the reference closing prices with no queue, no participation cap and no rejection.
- **Fees — modelled:** "We model transaction costs as proportional to portfolio turnover, as suggested by DeMiguel et al. (2009). Our base assumption for the level of transaction fees is **ten basis points of the value of rebalanced positions**" (§3.6.2). Justification given by the source from AQR real-fund evidence (Israel et al., 2021, **as cited by the primary source — not independently opened for this record**): US large-cap momentum fund realised **6.4 bps** average total cost Jul-2009–Dec-2016 (0.21 bps fees + 6.19 bps impact), US small-cap **18.27 bps** (0.35 + 17.92), international **13.16 bps** (4.89 + 8.28). Net results in Table 4 are computed with this **flat 10 bps × turnover** rule; sensitivity is swept from **0 to 100 bps** in Figure 12.
- **Spread / market impact:** **no separate spread or impact model exists**; impact is only implicitly absorbed inside the flat 10 bps assumption (the source itself concedes 10 bps "might be too low for the FF data set, due to the large number of small-cap stocks with shallow liquidity"). Record this as **cost model = single flat proportional-to-turnover term, name-level spread/impact `not stated in source`** — explicitly *not* inferred as zero.
- **Turnover:** source-reported — under weekly rebalancing the fractional strategies with **`d ∈ (0.6, 0.9)` incur turnover "almost up to a factor of three" that of classical momentum** (`d = 1`), an effect that disappears under monthly rebalancing where the reversal strategy becomes the highest-turnover one (§3.6.2, Figure 11). Table 4 reports turnover **44.4%** for FM vs **17.9%** for classical MOM (FF, value-weighted) at the `q*` concentration — **the Table 4 caption lists turnover among the columns that are *not* annualised, so its period basis is not stated beyond that** → `underspecified`.
- **Borrow / shorting availability and stock-loan fees:** **not stated in source** → `data gap`.
- **Leverage / margin:** **not stated in source** → `data gap`.
- **Capacity / market impact at scale / participation limits:** **not modelled** → `data gap` (the only capacity-adjacent argument is the citation to AQR's fund sizes).
- **Cost break-even reported by the source:** weekly rebalancing — for **every κ > 0** in the FF and AMP universes the best net strategy has **`d ∈ [0.1, 0.9]`** (i.e. fractional beats `d = 1`); monthly rebalancing in the FF universe — classical momentum achieves slightly higher net risk-adjusted returns once **κ ≥ 67 bps** (§3.6.2, Figure 12). All `source-reported`.
- Anything a reproducer must choose beyond the above (order type, borrow cost model, participation cap, tie handling, delisting handling) is **`research-proposed`** for this record.

## Evidence

### Source-reported

Every figure below traces to the pinned primary source (SSRN `abstract_id=4280465`, PDF SHA-256 `3257d72c…a3430ab2`, 53 pp., read 2026-09-23). All are third-party backtest claims; **none has been independently reproduced by us**.

- **Table 1** — *Returns on Portfolios Sorted by Fractional Momentum (d = 0.9)*, average **monthly** excess returns and factor alphas, **gross (no cost line in this table)**, weekly rebalance, Newey–West t in parentheses, sample caption **Jan 1973 – Dec 2020**:
  - FF universe, **value-weighted**: `High–Low` excess **2.16 (t = 9.06)**; `High–Low` 4F alpha **1.58 (7.95)**; 3F alpha 2.05 (9.11); CAPM alpha 1.98 (8.07). Quintile `High` excess **1.89 (6.27)**; `Low` **−0.26 (−1.08, not significant)**.
  - FF universe, **equal-weighted**: `High–Low` excess **5.02 (12.60)**; 4F alpha **4.66 (11.89)**. `High` 3.73 (10.12); `Low` −1.29 (−3.38).
  - AMP universe, value-weighted: `High–Low` excess **1.68 (9.43)**; 4F alpha **1.18 (7.44)**. Equal-weighted: `High–Low` **1.73 (8.85)**; 4F alpha **1.25 (7.76)**.
- **Table 2** — independent double sorts against 9 controls (BETA, book-to-market, SIZE, MOMENTUM, SHORT-TERM-REV, TIME-SERIES-MOM, EWMA, SMA, OLS), VW, monthly, gross, columns `High–Low` and `High–Low (4F alpha)`: FF-universe (Panel A) 4F alpha **4.07 (t = 12.53)** under SIZE control (raw `High–Low` 4.45, t = 13.11) and **3.77 (11.04)** under MOMENTUM control (raw 3.95, t = 11.39); AMP-universe (Panel B) 4F alpha **1.36 (8.95)** under SIZE control (raw 1.74, t = 9.18) and **2.12 (8.56)** under MOMENTUM control (raw 2.24, t = 9.54).
- **Table 3** — subsample splits (gross, monthly, VW except the EW subperiod rows): FF-universe `High–Low` **3.02 (8.36) / 2.46 (5.15) / 0.97 (2.97)** for **1973-1988 / 1989-2004 / 2005-2020** (VW); EW equivalents **4.34 / 8.60 / 2.14**. AMP-universe EW **2005-2020**: `High–Low` **0.53 (2.05)**, `High–Low (4F alpha)` **0.26 (1.47 — not significant at 10%)**.
- **Table 4** — gross **and** net (`10 bps` linear cost), `d = 0.9`, weekly, concentration `q* ≈ 12–17%`, sample caption **Jan 1973 – Dec 2020**. **Column basis per the caption:** return, volatility, Sharpe and Sortino are annualised, while **max drawdown, 4F alpha and turnover are explicitly *not* annualised**:
  - FF value-weighted **fractional momentum**: gross return **45.7%**, volatility **25.5%**, **Sharpe 1.79**, Sortino 2.86, max DD **63.9%**, 4F alpha **2.47 (6.52)**, turnover **44.4%**; **net** return **34.5%**, **net Sharpe 1.35**, net Sortino 2.14.
  - FF value-weighted **classical momentum** benchmark: gross return 24.6%, **Sharpe 0.81**, max DD 82.9%, turnover 17.9%; net return 20.0%, **net Sharpe 0.66**.
  - FF **equal-weighted fractional momentum**: gross return **94.1%**, volatility 15.9%, **Sharpe 5.93**, Sortino 10.97, max DD 36.4%, 4F alpha **7.47 (10.61)**, turnover 38.0%; net return **84.4%**, **net Sharpe 5.33**. Classical momentum EW: gross return 0.6%, Sharpe 0.03, 4F alpha −1.01 (−4.04); net return −2.8%, net Sharpe −0.16.
  - AMP value-weighted FM: gross **Sharpe 1.38** / net **0.92**; AMP equal-weighted FM: gross **1.64** / net **1.18**.
- **Figures 4 and 5** (gross, weekly, VW, FF): across `d ∈ [0,1]` the optimal `d = 0.9` for all three `q`, with the highest annualised **Sharpe ≈ 1.6 and Sortino ≈ 2.5** at `q = 0.4`; the most favourable specification (FF universe, equal-weight) has annualised Sharpe "**close to 6.0**"; the AMP value-weighted best case is "**above 1.3**".
- **§3.6.1 monthly rebalancing:** FF equal-weight best annualised **Sharpe 1.75 at `d = 0.8`**; classical momentum under monthly rebalancing lands at **Sharpe ≈ 0.3–0.5**, which the source notes is "closely aligned to the performance reported in the literature".
- **§3.6.3 implementation lag (Figure 13):** 1/2/3-day lags — performance deteriorates, "especially with lags of two and three days", but the fractional-over-classical advantage and the concave `d`-shape remain.
- **§3.7 long-only variant:** optimal `d* = 0.8` (slightly below the long-short `d* = 0.9`); long-only `d = 1` "barely outperforms the equally-weighted benchmark" while all `d < 1` beat it in return; best net performance at `d ≈ 0.8` in both universes; **turnover lower than long-short but still well above `d = 1`**.
- **Table 6** — international, `d = 0.9`, `q = 0.2`, long-short and long-only, weekly, **annualised; this table states no cost line → cost treatment for Table 6 is `underspecified` (treat as gross)**. Value-weighted long-short **Sharpe**: Brazil **0.56** (`d=1`: −0.19), France **0.43** (−0.22), Germany **0.40** (−0.03), Hong Kong **0.65** (0.02), Japan **0.99** (−0.42), U.K. **1.11** (0.01). Equal-weighted long-short Sharpe: Brazil 0.58, France 0.89, Germany 0.71, Hong Kong 0.80, Japan 1.38, U.K. 1.09. Source's own summary: fractional beats benchmarks in all six countries under both constructions and both weightings, strongest in the historically most liquid markets (U.S., then U.K., Japan) and "relatively modest" in the remaining four.

### Independently reproduced

`not independently reproduced`

### Negative evidence

**Source-acknowledged (primary paper, pinned PDF):**

1. **Time decay of the effect.** §3.5.1: "the fractional momentum effect appears to be weakening over time, as depicted by the flattening of the slopes"; performances for every `d ∈ (0,1)` are stronger before 2000 than after. Table 3 quantifies it: FF VW `High–Low` **3.02 → 2.46 → 0.97 %/month** across 1973-88 / 1989-2004 / 2005-2020, and the **AMP equal-weight 2005-2020 4F alpha is 0.26 with t = 1.47 (insignificant)**.
2. **Much higher turnover.** Weekly FM (`d ∈ (0.6,0.9)`) turnover is "almost up to a factor of three" classical momentum (§3.6.2); the Conclusion calls higher turnover a "drawback" and says the strategy "works best with more frequent portfolio rebalancing than proposed in the original framework of Jegadeesh and Titman (1993)".
3. **Cost/frequency interaction.** Monthly-rebalanced FF: classical momentum edges out `d = 0.9` once **κ ≥ 67 bps** (§3.6.2, Figure 12). The source also concedes **10 bps may be too low for the FF universe** given small-cap illiquidity, and that reversal profits "are known to be concentrated in stocks with low liquidity" (citing Avramov et al., 2006).
4. **Parameter sensitivity.** `d` outside `[0,1]` was "blatantly inferior out-of-sample" (§2.1); the reported optimum is a narrow band `d ∈ [0.8, 0.9]` across the paper.
5. **Long-short-dependent crash benefit.** §3.7: "the reduction of the maximum drawdown is not as consistent as in the long-short case" for the long-only variant; §3.8: without the short portfolio "there is mixed evidence on the drawdown performance".
6. **Weak short leg in value-weighted specs.** Table 1, Panel A/B: the `Low` quintile excess return is **−0.26 (t = −1.08)** in FF VW and **−0.26 (t = −1.09)** in AMP VW — **not statistically different from zero** — so a large share of the value-weighted long-short claim rests on the long leg (`research interpretation` of the source's own table).
7. **Internal date inconsistency** in the stated sample window (1972 vs 1973 vs "48 years") — recorded in Provenance.
8. **Very high equal-weight headline numbers** (Table 4, FF equal-weighted: gross return **94.1%**, gross **Sharpe 5.93**, net Sharpe 5.33, 4F alpha 7.47) are **source-reported for an equal-weighted, small-cap-heavy, friction-light specification priced with a single flat 10 bps × turnover term**; there is no capacity or name-level liquidity check behind them → treat as an upper bound, not as an implementable expectation.

**External / contrary findings:**

9. **Kim & Kim (2025), "A note on the fractional momentum strategy", *Applied Economics Letters* 32(18): 2664–2668, DOI `10.1080/13504851.2024.2337329`** — the published abstract (read via RePEc record `taf:apeclt:v:32:y:2025:i:18:p:2664-2668`, 2026-09-23; **full text is subscription-restricted → abstract-level evidence only**) states the strategy's reported gains hold "albeit under weekly rebalancing" and that fractional momentum "**performs inferior to the traditional momentum strategy as rebalancing frequency is decreased**". This directly targets the paper's central implementation condition (weekly rebalancing is what makes FM work). This claim is **source-reported by the contradicting paper, not independently reproduced**.
10. **None identified beyond the above** for the crash-mitigation claim itself; absence of further contrary evidence in the reviewed sources is not evidence of no negative result.

## Falsification plan

Every threshold below is **`research-defined`** (chosen by this Scout, not by the source). Every operational choice not fixed by the source is **`research-proposed`**. Failure action throughout: **do not promote; keep `research-only`, record the failing metric and stop rather than retuning.**

1. **Frozen-parameter reproduction (`research-defined`).** Rebuild the FF-universe daily sort with `d = 0.9`, `τ = 250`, `q = 0.4`, VW and EW, weekly five-sleeve averaging, 1973–2020. **Fail if** the gross monthly `High–Low` excess is `≤ 0`, **or** its Newey–West `|t| < 2.0`, **or** the 4F alpha `|t| < 2.0` — compared against the source's Table 1 values (2.16 / 9.06 and 1.58 / 7.95 for FF VW).
2. **True out-of-sample selection (`research-defined`).** Select `d` using **1973–2004 only**, freeze it, evaluate **2005–2020**. **Fail if** the frozen-`d` fractional strategy's net Sharpe `≤` classical momentum's (`d = 1`) net Sharpe at the same frequency, **or** if the 2005-2020 4F alpha `|t| < 2.0` (source's own AMP-EW value there is 0.26 with `t = 1.47`).
3. **Rebalancing-frequency stress (`research-defined`, mirrors Kim & Kim).** Repeat with **monthly and quarterly** rebalancing at identical `d`, `q`, universe and cost. **Fail if** fractional net Sharpe `<` classical net Sharpe at either lower frequency in both universes.
4. **Cost sweep (`research-defined`).** Apply `κ ∈ {10, 20, 30, 50}` bps × turnover, plus a name-level spread proxy proportional to 1/ADV (`research-proposed`). **Fail if** fractional net Sharpe `≤` classical net Sharpe at `κ = 20` bps under weekly rebalancing, **or** if the turnover differential alone (FM ≈ 3× classical) erases the gross advantage at `κ = 30` bps.
5. **Implementation-lag stress (`research-defined`).** Force `+1 trading day` between formation and fill. **Fail if** the fractional-over-classical net Sharpe advantage becomes `≤ 0`. (Source reports ordering survives lags — Figure 13 — so this is directly checkable.)
6. **Component ablation / mechanism test (`research-defined`).** Using the decomposition in equation (13), run (a) momentum-mixture component only, (b) reversal-mixture component only, (c) full fractional score, plus (d) classical `d = 1` and (e) `d = 1` + a matched short-horizon reversal overlay. **Fail the stated mechanism if** the full score does **not** beat (e) after costs — i.e. the result is reducible to "momentum plus reversal", not to better signal extraction.
7. **Parameter-surface stability (`research-defined`).** Sweep `d ∈ {0.7, 0.8, 0.9, 1.0}`. **Fail if** net Sharpe at the adjacent grid points drops **more than 20%** below the peak (knife-edge optimum), or if the optimum drifts by `≥ 0.2` between the 1973–2004 and 2005–2020 halves.
8. **Universe / liquidity placebo (`research-defined`).** Repeat in the AMP universe and within the top liquidity quintile only (`research-proposed` liquidity proxy: 60-day median dollar volume). **Fail** if the effect disappears entirely in the most liquid quintile — that would indicate a microstructure/illiquidity artifact rather than a ranking signal.
9. **Borrow-cost stress (`research-defined`).** Charge an annualised stock-loan fee of `100 bps` on the short leg (`research-proposed`; the source models none). **Fail if** net long-short advantage over classical goes `≤ 0`.
10. **Capacity bound (`research-defined`).** Cap participation at `10%` of daily volume (`research-proposed`). **Fail if** the equal-weight headline performance collapses by `> 50%` under that cap — the source's headline numbers sit on a small-cap-heavy equal-weight book.
11. **Placebo (`research-defined`).** Shuffle the cross-sectional score within each date. **Fail if** the shuffled-label `High–Low` produces `|t| ≥ 2.0` — that would signal a structural long/short-leg or universe artifact.
12. **No rescue by retuning (`research-defined`).** A failed threshold may not be re-opened by re-choosing `d`, `q`, the window or the cost level on the evaluation sample; any such re-run is exploratory and cannot flip a recorded failure.

## Crypto portability

**`unproven`.**

The source contains **zero crypto evidence** — every sample is listed equity (US CRSP, six Compustat markets), and the mechanism depends on equity-specific structure: a single daily closing auction for formation and execution, an established cross-sectional universe with corporate-action-adjusted total returns, an equity borrow market, and weekly rebalancing conventions borrowed from the Jegadeesh–Titman/Asness literature. Nothing in the paper supports porting it to crypto as-is, so this is a **ported hypothesis, not crypto empirical evidence**.

Crypto-specific risks if someone adapts it:

- **No natural universe / survivorship:** no continuous "all investable coins" panel; delistings, renames, hard forks and rug pulls break a 250-day lookback and a top/bottom `q` sort unless a point-in-time listing table is built.
- **Shorting:** perp/spot borrow for a short leg is venue- and capital-dependent, with funding and stock-loan-analogue costs the source never models; the equity short-leg evidence is itself weak in the value-weighted specs (Table 1 `Low` quintile `t ≈ −1.1`).
- **24/7 sessions and candle boundaries:** "daily close" is ambiguous across venues/timezones; formation and fill timestamps must be pinned per venue (`research-proposed`).
- **Venue fragmentation and index/mark prices:** cross-sectional ranks differ by venue; perp mark/index versus spot basis can dominate a daily-frequency equity-style signal.
- **Funding and carry:** a perp-based implementation has funding flows on both legs that the source's turnover-cost model does not represent.
- **Liquidity and impact:** the top/bottom `q` deciles of a crypto cross-section are dominated by thin coins; the source's own warning about small-cap illiquidity applies with more force.
- **Adaptation direction (`research-proposed`, untested):** a **long-only** fractional score (the source's §3.7 variant, `d ≈ 0.8`) over a liquidity-filtered top-`N` universe is the least-friction port; it has **not been tested by the source or by us**.

## Limitations

- **Working paper, unreviewed:** SSRN / SFI RP No. 22-87; **peer-review status `not stated in source`**. All performance numbers are **source-reported**, single research group, **`not independently reproduced`**.
- **Sample-window contradiction inside the source:** January 1972 (§3.1) vs January 1973 (Tables 1–4) vs "48 years" — `underspecified`.
- **Data-engineering layer `underspecified`:** warm-up/minimum history, tie handling, suspended/stale/missing days, delisting returns, timezone string, single-book (non-averaged) implementation — all `data gap`.
- **Cost model is one flat number:** 10 bps proportional to turnover; **no name-level spread, impact, latency, partial-fill, borrow or financing model** → `underspecified`, **not** "unmodeled = zero".
- **No capacity analysis;** equal-weight headline Sharpe ≈ 5.9 gross / 5.33 net (Table 4, FF EW) sits on a small-cap-heavy book with turnover **44.4%** (period basis `underspecified` — the Table 4 caption excludes turnover from annualisation) → treat as an upper bound.
- **Parameter selection is in-sample in the sections reviewed:** the `d` grid is searched and reported over the same sample used for evaluation; **no train/test split of the `d`-selection step is described** → `underspecified`.
- **Mechanism attribution incomplete:** Table 5 correlations exist but there is **no component-ablation P&L**, so "better momentum estimator" vs "momentum + short-horizon reversal overlay" is unresolved.
- **Contrary external evidence** on the rebalancing-frequency condition (Kim & Kim 2025, abstract-level) — see Negative evidence item 9.
- **Reproduction requires licensed data** (CRSP, Compustat); no public code artifact was located and none is stated in the source → `data gap`.
- **Appendices A–B not reviewed** for this record → `data gap` (no claim here depends on them).
- **Later same-author working paper exists and is NOT this source:** an author publication page lists "Smoothing Out Momentum and Reversal" (Chitsiripanich, Paolella, Polak, Walker, 2025) as a separate title; it was **not opened and must not be conflated** with this record → deferred as a distinct candidate for a future run.
- **`not independently reproduced`** (stated twice deliberately: our own evidence class is empty).
- **`unproven`** for any crypto or non-equity use.

## Implementation status

`not-implemented`.

Nothing from this record has been implemented in our research stack. No score computation, no portfolio construction, no backtest, no Qlib run, no Paper/Testnet/Live activity exists for this hypothesis. The source's own implementation (FFT truncated fractional differencing per Jensen & Nielsen, 2014) is described in prose only; no code URL is given and no repository was located in a keyword search on 2026-09-23 (`data gap`). This record does not modify any engine and does not authorize implementation.

## Adoption boundary

Presence of this record in this repository **does not mean** any of the following: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading.

All reported Sharpe, return, alpha, drawdown and turnover figures are **third-party source-reported backtest claims** from an unreviewed working paper and must never be restated as our verified results. `status: research-only`, `implementation_status: not-implemented`, `adoption: not-approved`, `approval_scope: research-only`.

## Related Wiki records

Hermes Wiki Brain `kb_search "fractional momentum cross-sectional momentum crash"` returned six records, **none of which shares this source identity or this signal construction**; **no stable Wiki Brain page for fractional-difference cross-sectional momentum is known, so no Wiki link is asserted for the mechanism.** The specification page itself is known: `[[quant/strategy-research-record-spec-v1]]`.

Adjacent records **in this repository** (different source identities and/or materially different mechanisms — noted for reviewers, not claimed as duplicates):

- `crypto-cross-sectional-momentum-30d-top-quintile-7d-2026-08-31.md` and `crypto-cross-sectional-volatility-managed-momentum-2026-08-31.md` — classical-window cross-sectional momentum in crypto; **different asset class, different signal construction** (endpoint returns, not fractional-difference scores).
- `spatio-temporal-momentum-multitask-shrinkage-turnover-regularization-2026-09-06.md` (arXiv 2302.10175) — learned joint time-series/cross-sectional momentum with turnover regularisation; **different mechanism (learned multi-task model) and different source**.
- `crypto-macro-sentiment-contrarian-fear-greed-ema-2026-09-03.md` — uses fractional differencing (`d = 0.5`, `K = 200`) but as a **sentiment-index smoothing step**, not as a cross-sectional return-scoring factor → **technique overlap only**.
- `crypto-risk-managed-tsmom-crash-state-de-risking-drawdown-control-2026-09-14.md` and `aegis-momentum-gated-hierarchical-minimax-sortino-allocation-2026-09-12.md` — share the **crash-mitigation goal** but use regime gating / allocation overlays instead of signal construction.
- `spy-intraday-momentum-noise-area-band-vwap-stop-dynamic-sizing-2026-09-23.md` (SSRN 4824172, Zarattini/Aziz/Barbon) and `ensemble-donchian-trend-following-crypto-top20-rotational-2026-09-20.md` (SSRN 5209907) — different SSRN identities in the same SFI working-paper series; **explicitly not the same source**.

## Sources

1. Soros Chitsiripanich, Marc S. Paolella, Pawel Polak, Patrick S. Walker. *Momentum Without Crashes.* Swiss Finance Institute Research Paper Series N°22-87; Date Written November 14, 2022; 53 pages; SSRN posted 18 Nov 2022, last revised 23 Nov 2022. Abstract page: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4280465 ; DOI: https://doi.org/10.2139/ssrn.4280465 . **Primary source; every performance number, parameter and table anchor in this record comes from the PDF downloaded 2026-09-23** (delivery URL `https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID4283823_code623849.pdf?abstractid=4280465&mirid=1&type=2`), 4,982,327 bytes, SHA-256 `3257d72c1e38d2b931838b311821f65a45b43cab890c6589d7f4d6c5a3430ab2`, 53 pages, read 2026-09-23 (§2, §3.1–§3.8, §4, Tables 1–6; Appendices A–B not reviewed).
2. Swiss Finance Institute landing page, "N°22-87: Momentum Without Crashes" (category: Working Papers; date 10 Nov. 2022): https://www.sfi.ch/en/publications/n-22-87-momentum-without-crashes — opened 2026-09-23 (author list, working-paper category, abstract).
3. IDEAS/RePEc record for the same working paper (handle `chf:rpseri:rp2287`): https://ideas.repec.org/p/chf/rpseri/rp2287.html — opened 2026-09-23 (author affiliations, citation form).
4. Saejoon Kim, Hyuksoo Kim. "A note on the fractional momentum strategy." *Applied Economics Letters*, vol. 32(18), pp. 2664–2668, October 2025. DOI `10.1080/13504851.2024.2337329`. RePEc record opened 2026-09-23: https://ideas.repec.org/a/taf/apeclt/v32y2025i18p2664-2668.html — **abstract only (full text subscription-restricted)**; used solely as contrary/rebalancing-frequency evidence.
5. Secondary works **cited inside** source 1 and reported here only as the source cites them (not independently opened for this record): DeMiguel et al. (2009) linear turnover-cost formulation; Israel et al. (2021, AQR) realised fund cost figures; Jegadeesh (1990), Jegadeesh & Titman (1993), Asness et al. (2013), Zhu & Yung (2016) benchmark definitions; Daniel & Moskowitz (2016) momentum-crash reference; Jensen & Nielsen (2014) FFT fractional-differencing method; Kenneth French Data Library replication check.
