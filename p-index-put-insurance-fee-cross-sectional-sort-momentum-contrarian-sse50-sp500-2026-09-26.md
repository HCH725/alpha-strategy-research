---
schema: strategy-research-record-v1
title: "p-index (put insurance-fee) cross-sectional sort with weekly momentum/contrarian overlay on SSE 50 and S&P 500"
created: 2026-09-26
updated: 2026-09-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - option-derived-risk-measure
  - put-call-parity
  - momentum-contrarian
  - weekly-rebalance
  - china-a-shares
  - us-equities
status: research-only
confidence: medium
source_as_of: 2026-06-07
sources:
  - "https://arxiv.org/abs/2606.08569 — arXiv:2606.08569v1 [q-fin.PM], sole version, submitted Sun 7 Jun 2026 10:51:47 UTC, CC BY 4.0, checked 2026-09-26"
  - "https://arxiv.org/pdf/2606.08569v1 — pinned PDF, 23 pages, 1,702,220 bytes, SHA-256 e3151492c41204fbd4053e906d04cd4ed6b3548b3c99b548b975a71e92c29823, PDF CreationDate D:20260604193208+08'00'"
  - "https://doi.org/10.48550/arXiv.2606.08569 — DataCite DOI, HTTP 302 → abs → 200, checked 2026-09-26"
  - "https://arxiv.org/abs/2510.11074 — earlier same-group paper named by the arXiv admin text-overlap note; read for identity only, not used for any claim in this record"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Source-internal (significance scope): Section 3.1 prose (PDF p.12) states that 'in these four holding periods, the p-index exhibits statistically significant differences between high- and low-yield firms', but Table 2 (PDF p.12, visually verified 2026-09-26) prints Median-test p = 0.543472 for the Two-weeks column, which is not significant at 0.05 (Wilcoxon for the same column is 0.016622). The blanket claim therefore fails for one of the eight printed tests."
  - "Source-internal (comparison scope): Section 3.2 / Concluding Remarks (PDF pp.15, 19) state that 'the MCIRS method employing the p-index consistently delivered higher returns than its beta-based approach', but among the four matched arms the printed cells favour beta in two of them (inefficient-contrarian: beta −11.47% vs p-index −17.2%; efficient-momentum: beta −8.6% vs p-index −9.69%). Figure 8 (PDF p.16), whose legend was visually verified on 2026-09-26, plots only the two arms where p-index wins (p-index-efficient-contrary, p-index-inefficient-momentum, beta-efficient-contrary, beta-inefficient-momentum plus the Shanghai Composite line), so 'consistently' holds only over the figure's subset, not over all printed arms."
---

# p-index (put insurance-fee) cross-sectional sort with weekly momentum/contrarian overlay on SSE 50 and S&P 500

## Provenance

- **Primary source (sole version):** Xinzhao Xie, Bopei Nie, and Kuo-Ping Chang, *"Stock Investment: The p-index Approach"*, arXiv preprint `arXiv:2606.08569v1 [q-fin.PM]`, submitted **Sun 7 Jun 2026 10:51:47 UTC** (1,662 KB). `abs/2606.08569v2`, `html/2606.08569v1` and `html/2606.08569v2` all returned **HTTP 404** on 2026-09-26 → v1 is the only version and there is no arXiv HTML rendering; the record was built from the pinned PDF.
- **Affiliation (from PDF p.1):** all three authors at the *Jinhe Center for Economic Research, Xi'an Jiaotong University*, Xianning West Road 28#, Xi'an, Shaanxi 710049, China; Kuo-Ping Chang is corresponding author (`kpchang@mx.nthu.edu.tw`). The arXiv abs page prints no per-author affiliation block, so abs-level affiliation is a data gap and the affiliation above is taken from the PDF title page.
- **Status / licence / identifiers:** Comments field contains exactly one item — **"arXiv admin note: text overlap with arXiv:2510.11074"**; no journal-ref cell (`tablecell jref` absent), no publisher DOI beyond the DataCite `10.48550/arXiv.2606.08569` (HTTP 302 → abs → 200), no peer-review statement → **preprint only**. Licence = **CC BY 4.0** (`creativecommons.org/licenses/by/4.0/`). JEL G12, G13. Subject: Portfolio Management (q-fin.PM) only, no cross-list.
- **Pinned PDF:** `https://arxiv.org/pdf/2606.08569v1`, **1,702,220 bytes**, **SHA-256 `e3151492c41204fbd4053e906d04cd4ed6b3548b3c99b548b975a71e92c29823`**, **23 pages**, Producer `Microsoft: Print To PDF`, `CreationDate D:20260604193208+08'00'`, document title `Stock Investment _ The p-index Appraoch` (sic, "Appraoch" in PDF metadata).
- **How this record was read (2026-09-26):** full text extracted with `pdf2txt.py` (46,718 bytes / 1,659 lines) and read end-to-end (title page, Abstract, §1 Introduction, §2 p-index theory incl. eqs. 1–7 and footnotes 1–4, §3 Data and Empirical Results incl. §3.1–3.2, eqs. 8–10, Tables 1–2, Figures 1–16 captions, footnote 5–7, §4 Concluding Remarks, Declarations, References); **pages 9, 11, 12 and 16 additionally rendered to images and read visually** to verify the typeset form of eq. (9), the step-by-step p-index construction, the full grid of Table 1 and Table 2 cells, and the legend of Figure 8 (text extraction of multi-line tables/legends is otherwise ambiguous).
- **Code / data availability:** no code, no repository, no data-availability statement, no data-vendor statement beyond the in-text mentions of CSMAR, Yahoo Finance and Choice Data (East Money). No GitHub/URL other than the arXiv and SSRN references.
- **Text-overlap flag:** the arXiv admin note points at `arXiv:2510.11074` — *"Evaluating Investment Performance: The p-index and Empirical Efficient Frontier"*, Jing Li, Bowei Guo, Xinqi Xie, Kuo-Ping Chang, submitted 13 Oct 2025 (read for identity only). The two papers are distinct manuscripts (different titles, different samples, different author lists sharing the corresponding author); the overlap note is recorded as a source-quality caveat, not as evidence for or against any number in this record.
- **Epistemic status:** every performance figure below is **source-reported** from the pinned v1 PDF and none has been independently reproduced. All thresholds, screens and decision rules added by us are labelled `research-proposed` or `research-defined`.

## Economic mechanism

### Source-reported

The authors define risk as "the probability that a party will fail to meet a stated obligation or promise" and read a European put as insurance: holding the asset plus a put guarantees at least `K` at maturity. Starting from put-call parity `c + K/(1+r) = S0 + p` (eq. 1) and a one-period binomial representation (eq. 6), they set the strike to `K = (1+δ)·S0` and define (eqs. 4–5, restated operationally in the three numbered steps on PDF p.9):

> **p-index = p_i / K_i = p_i / [(1+r)·S0i]** — "the insurance fee for each insured dollar so that the i-th stock can achieve at least r rate of return at the end of the week."

Higher p-index ⇒ higher measured risk. The companion statistic (eq. 9, visually verified on PDF p.9) is

> **p-ratio = (r_i − r) / [ p_i / ( S0i · (1+r) ) ]**, where `r_i` is the i-th stock's rate of return in the week,

i.e. excess weekly return per unit of model-implied insurance fee — described by the authors as analogous to the Treynor ratio ("an asset's risk-adjusted excess return"). Cross-sectionally they then classify names as **efficient** (top group by p-ratio, or by an MCIRS efficiency score with p-index as input) vs **inefficient** (bottom group) and apply one of four one-week arms: momentum or contrarian on each group. A second construction, the **fair-price strategy**, compares a model-implied "fair" Monday close against the actual Monday close and buys undervalued / short-sells overvalued names. MCIRS (minimum convex input requirement set, eq. 10) is a non-parametric quasi-concave efficiency score in which capital, labour and beta (or p-index) are inputs and rate of return is the output; top 10% = efficient, bottom 10% = inefficient.

### Research interpretation

- **Hypothesis in falsifiable form:** a *model-implied downside-insurance scale* (built only from weekly high/low closes, a binomial probability calibrated on a broad index, and a government-bond coupon) divided into recent excess returns carries cross-sectional information about one-week persistence — specifically, that the top p-ratio group **reverses** in China (short the recent winners) while the same sort **persists** in US large caps (long the recent winners). The two market-level conclusions point in opposite directions, so the honest reading of the source is *market-dependent conditional persistence*, not a universal anomaly.
- **Component roles** (as normalised by us): *signal* = weekly p-ratio / MCIRS cross-sectional sort; *direction* = one of four fixed arms (efficient-momentum, efficient-contrarian, inefficient-momentum, inefficient-contrarian); *regime overlay* = none pre-specified by the source (the volume-based split in Figure 10 is reported after the fact); *risk/exit* = fixed one-week time exit, no stop, no sizing rule beyond an illustrative $100 example. The fair-price strategy is a separate, signal-only rule (mispricing vs model price) with the same execution frame.
- **Competing mechanism we consider at least as likely (research interpretation, not source-reported):** the p-index is **never taken from a traded option** — no option chain, no implied volatility, no exchange price enters the computation. It is a binomial model output whose up/down factors are the *same week's* index high/low closes and whose probability is a linear function of the index range. The construction therefore behaves largely like a **range/volatility-scaled return rank**, so any edge may be ordinary risk-scaled short-term reversal/momentum rather than option-market information. Falsification test F6 is designed to separate these two explanations; until it runs, the option/parity framing is an interpretation, not an established channel.
- **Named frictions (our framing):** behavioural overreaction/underreaction in weekly large-cap returns, with an A-share-specific shorting and sentiment structure. No liquidity-provision, funding, or carry channel is claimed by the source.

## Signal

Everything in this section is `source-reported` unless marked otherwise.

**A. Weekly p-index / p-ratio construction (PDF p.9, eqs. 8–9 and the three numbered steps; visually verified):**

1. **Inputs per week (Mon–Fri):** Shanghai Composite Index Monday close `S0_SH`, the index's highest and lowest **closing** prices of that week (`u_SH`, `d_SH`); each stock's highest and lowest closing price of that week. Risk-free `r = (10-year China government bond coupon rate) / 52`.
2. **Risk-neutral probability:** `π` and `1−π` from the binomial representation (eq. 6 / eq. 8). **Source fallback rule:** "If it is found that 1 > π > 0 does not hold, then use this week's and the previous week's closing prices to calculate π."
3. **Theoretical price:** `S0i = 1/(1+r) · [π·S_u,i + (1−π)·S_d,i]` — the stock's "theoretical (fair) closing price on Monday of the week" (eq. 8).
4. **Strike and put:** `K_i = (1+δ)·S0i` with **`δ = r`**; `p_i` = model put price from the same binomial structure (eq. 7); **p-index = `p_i/[(1+r)·S0i]`** = insurance fee per insured dollar guaranteeing at least `r` over the week.
5. **p-ratio (eq. 9):** `(r_i − r) / p-index`, `r_i` = the stock's realised return in that week.
6. **US variant:** for the S&P 500 section the index used "to calculate the p-index and π from eq. (8)" is the **Dow Jones Total Stock Market Index**; the US value of `r` (risk-free rate) is **not stated in the source → data gap**.

**B. Fair-price strategy (§3.1, PDF pp.10–11):** compute the fair Monday close from the week's five closes; if fair > actual Monday close the stock is "undervalued" → **buy at the following Monday's closing price and sell at the next Monday's closing price**; if fair < actual → **short-sell at that Monday's close and buy back one week later** (worked example: $100 → 10 shares → $110 = +10%; short example −50%). Holding periods reported: **one week, two weeks, one month, two months**. The mechanics of the two-week/one-month/two-month cycles (re-evaluation cadence, overlap handling) are **underspecified**.

**C. Momentum/contrarian cycle (§3.2, PDF p.12, verbatim structure):** a three-week cycle —

- (i) **Week 1:** classify the top 10% of firms by p-ratio as *efficient* and the bottom 10% as *inefficient* (for SSE 50 = **5 names per group**; for the S&P 500 section the source switches to **top/bottom 30%** = 150 names per group, applied to p-ratio, p-index and beta sorts).
- (ii) For an **efficient** stock: (a) momentum = **buy at Monday close of Week 2, sell at Monday close of Week 3**; (b) contrarian = **short-sell at Monday close of Week 2, cover at Monday close of Week 3**.
- (iii) For an **inefficient** stock: (c) contrarian = **buy at Monday close of Week 2, sell at Monday close of Week 3**; (d) momentum = **short-sell at Monday close of Week 2, cover at Monday close of Week 3**.
- Portfolios are **equally weighted**; the only sizing illustration in the source is the $100 example. Signal formation uses Week-1 Monday–Friday closes; the first tradable action is the Week-2 Monday close → **one-week holding, close-to-close, weekly rotation**.
- **MCIRS variant (eq. 10):** weekly linear program; inputs capital, labour, beta (or p-index in place of beta) taken from Choice Data (East Money Information); beta "is calculated using stock price data over a 100-week period"; output = rate of return; efficiency score `u_k ∈ [0,1]`; top 10% = efficient, bottom 10% = inefficient. **Frequency of the capital and labour inputs is not stated → data gap.**

**D. Underspecified / not reconstructable from the source (do not treat as reproducible):**

- compounding and annualisation convention (arithmetic vs geometric, reinvestment) — only "derived by aggregating weekly rates of return" is stated;
- tie handling at the 10% / 30% cut, treatment of suspended/missing weeks, and whether classification uses inclusive or exclusive endpoints;
- index-membership point-in-time construction for either universe (see Required data);
- the US risk-free rate, and the sector-assignment source for the "seven economic sectors";
- order type beyond "closing price", fill model, and how positions are carried if a name cannot be shorted;
- any ex-ante regime filter (the volume regime split is reported ex post).

## Required data

- **Universe 1:** the **50 constituent stocks of the SSE 50 Index**, daily data **2018–2023**, from the **China Stock Market & Accounting Research Database (CSMAR)** [source-reported]. Point-in-time membership, listing/delisting handling and the constituent snapshot date are **not stated → survivorship/point-in-time data gap**.
- **Calibration index (China):** Shanghai Composite Index daily closes (Monday close, weekly high/low closes) [source-reported].
- **Risk-free (China):** 10-year China government bond **coupon rate**, divided by 52 for the weekly rate [source-reported]; the exact series/vendor is not named → data gap.
- **Universe 2:** **500 stocks of the U.S. S&P 500 index, 2018–2023, from Yahoo Finance**; calibration index = **Dow Jones Total Stock Market Index** [source-reported]. Point-in-time S&P 500 membership is not stated → survivorship data gap.
- **MCIRS inputs:** capital, labour, beta (100-week window) from **Choice Data (East Money Information)** [source-reported]; capital/labour frequency unstated.
- **Sector labels:** seven SSE 50 sectors (financial, healthcare, industrial, consumer, materials, technology, energy); vendor not stated → data gap.
- **Market-volume series** for the sentiment split (weekly RMB turnover) — vendor not stated → data gap.
- **Not required by the source:** option chains, implied volatilities, order-book, funding, borrow, open interest, tick data. *(Noting this explicitly because the "put option" wording invites the wrong data requirement: the put is model-derived, not observed.)*
- **Timestamp/timezone:** exchange local time implied (SSE and US equity sessions); the source states no timezone convention → data gap. Weekly candles are Monday–Friday close based.

## Execution assumptions

**Source-reported:**

- Signal → order timing: classification uses Week-1 closes; **both entry and exit are at Monday closing prices** (Week 2 open of the cycle = Monday close; exit = next Monday close). No same-bar look-ahead in the trade itself is claimed by the source: the Week-1 data used for the sort are complete before the Week-2 Monday close.
- Order type: closing price execution is assumed implicitly; no market/limit distinction, no fill model, no latency, no partial-fill or failure handling → **all data gaps**.
- **Costs / fees / spread / slippage / impact / capacity / turnover / borrow / dividend / margin / leverage / funding:** a word-boundary scan of the pinned PDF text returns **0 occurrences** of *transaction cost*, *commission*, *slippage*, *bid-ask*, *spread*, *stamp duty*, *borrow*, *turnover*, *market impact*, *capacity*, *dividend*, *latency*, *fill*, *ADV*, *participation*; the only occurrences of "fee" are the phrase **"insurance fee"** (pp. 1, 3–6, 9, 20) and the only occurrences of "liquidity" are in the literature review, the SSE 50 index description and a reference title. Section 3 (Data and Empirical Results) — the paper's methods/experimental-setup equivalent, read in full — contains no cost treatment at all. Therefore **every cost field is a `data gap`, never zero**, and every printed return must be read as **gross of all costs**.
- Shorting: the source instructs short-sell and buy-back legs for A-share names and S&P 500 names without discussing borrow availability, locate, price limits, T+1 settlement or margin → **underspecified feasibility** (our note: A-share shorting constraints are a real-world feasibility issue; this is a `research-proposed` screen in F2, not a source claim).
- Leverage/margin/position limits: none stated.

**Our assumptions (research-proposed, not from the source):** none are adopted as defaults in this record; any implementation-grade assumption (order type, borrow model, cost ladder, position caps) must be created inside a falsification test and labelled accordingly.

## Evidence

### Source-reported

All figures below are `source-reported` from arXiv:2606.08569v1 (pinned PDF, SHA-256 `e3151492…`), gross of any cost, and have **not** been independently reproduced.

**Table 1 (PDF p.11; cell grid visually verified 2026-09-26)** — "Annualized rates of return of equally-weighted portfolios under different investment periods" (fair-price strategy, 2018–2023):

| Portfolio | Weekly | Two weeks | Monthly | Two months |
|---|---|---|---|---|
| SSE 50 stocks (50 names) | 0.91% | 0.71% | 4.92% | −3.03% |
| Three largest weights | 2.31% | −10.24% | 9.78% | −1.25% |
| Materials sector | 11.04% | 11.93% | 10.18% | −1.02% |

Cross-checks inside the source: §3.1 prose and §4 repeat 11.04 / 11.93 / 10.18 for materials and 2.31 / 9.78 for the top-three weights, consistent with the table.

**Table 2 (PDF p.12; visually verified 2026-09-26)** — "p-values for the differences in the p-index between high- and low-yield companies" (top vs bottom 10% by cumulative return; these tests are on the **p-index distribution, not on strategy returns**):

| | Weekly | Two weeks | Monthly | Two months |
|---|---|---|---|---|
| Median test | 0.014088 | **0.543472** | 0.004586 | 0.002811 |
| Wilcoxon test | 0.001684 | 0.016622 | 0.000006 | 0.000057 |

**SSE 50 one-week momentum/contrarian arm returns (§3.2 prose, Figures 2–7, PDF pp.12–15):**

| Sort | efficient-momentum | efficient-contrarian | inefficient-momentum | inefficient-contrarian |
|---|---|---|---|---|
| p-ratio | −21.62% | **+9.97%** | +1.17% | −1.24% |
| beta (MCIRS) | −8.6% | +5.98% | +7.21% | −11.47% |
| p-index (MCIRS) | −9.69% | +6.48% | +9.01% | −17.2% |

Provenance: p-ratio row from §3.2 pp.12–13 (Figures 2–3); beta row pp.13–14 (Figures 4–5); p-index row p.15 (Figures 6–7); all three rows repeated in the Abstract and §4.

**Our count on the 12 printed cells:** 6 of 12 positive; range −21.62% to +9.97%; simple mean across the 12 arms ≈ **−2.50% annualized** (our arithmetic) — i.e. the positive results are concentrated in the anti-persistence pairings rather than being a level effect. Source's directional claim holds in **3 of 3** sort families: efficient-contrarian > efficient-momentum (spreads +31.59, +14.58, +16.17 pp) and inefficient-momentum > inefficient-contrarian (spreads +2.41, +18.68, +26.21 pp), i.e. "efficient stocks failed to sustain their momentum, while inefficient stocks exhibited no mean reversion" for the SSE 50.

**Figure 8 (PDF p.16; legend visually verified 2026-09-26):** plots only `p-index-efficient-contrary`, `p-index-inefficient-momentum`, `beta-efficient-contrary`, `beta-inefficient-momentum` and the Shanghai Securities Composite Index, weekly x-axis 2018-01 → 2023-46, right axis −40% … +80% (weekly percentage bars) — this is the entire evidential basis for the "consistently higher than beta" claim (see `contradictions`). The legend spells "contrary" where the body text writes "contrarian".

**Figure 10 regime split (§3.2, PDF p.17):** weekly market volume **RMB 13.3429B** for 2018–Q2 2020 vs **RMB 18.9739B** post-Q2 2020 (source states a **+42%** surge in participation); within these two ex-post blocks, p-index-efficient-contrarian outperformed p-index-inefficient-momentum in the low-volume block and underperformed in the high-volume block. No test statistic is attached.

**S&P 500 section (§3.2, PDF pp.17–19; Figures 11–16; top/bottom 30% groups):** p-index-efficient-momentum **+3.69%**, p-ratio-inefficient-contrarian **+3.67%**, beta-efficient-momentum **+3.48%**; source states that for the US sample "efficient stocks (outperforming) maintained momentum, whereas inefficient stocks (underperforming) exhibited mean reversion—contrary to the behavior observed in China's SSE 50 index". The short-side arm returns for the US sample are not reported in the text.

**Statistical apparatus actually present:** median and Wilcoxon tests on p-index group differences (Table 2, 8 p-values). **No** Sharpe, volatility, drawdown, maximum drawdown, win rate, turnover, t-statistic on any strategy return, confidence interval, bootstrap, or multiple-testing correction appears anywhere in the pinned PDF (word scan: "Sharpe" occurs once, only as the Sharpe 1964 reference).

### Independently reproduced

**not independently reproduced.**

What we did do this run (verification only, no strategy recomputation): pinned the v1 PDF (SHA-256 above) and read it end-to-end from a `pdf2txt.py` extraction; visually re-read pages 9, 11, 12 and 16 to confirm typeset eq. (9), the numbered construction steps, every Table 1 / Table 2 cell and the Figure 8 legend; word-boundary scans for cost, fill and statistical terms; confirmed version status (`v2` and both `html` endpoints 404), licence (CC BY 4.0), DOI resolution (302 → 200), absence of journal-ref and of code/data statements; repo-wide and Wiki-Brain source-identity dedup. **No return, sort, p-value or annualised figure was recomputed** — the source publishes no code, no data and no machine-readable series that would allow it.

### Negative evidence

1. **Zero cost model.** No transaction cost, commission, spread, slippage, stamp duty, borrow, impact, capacity or turnover treatment exists anywhere in the pinned source (Methods-level read of §2–§3 plus word scan; all such fields are `data gap`). The one-week rotation with a short leg implies very high annual turnover — our interpretation, not a source number.
2. **Zero risk metrics.** No Sharpe, volatility, drawdown, win rate or beta of the strategy returns; "annualized rate of return" is the only reported statistic, with the aggregation convention unstated.
3. **Feasibility of the A-share short legs is never addressed** (borrow/locate, price limits, T+1, margin) — a `research-proposed` screen, F2, because the source is silent rather than wrong.
4. **Very small long/short groups:** SSE 50 top/bottom 10% = **5 names per side**, equally weighted; no liquidity, capacity or concentration screen; single-name idiosyncratic risk dominates.
5. **No out-of-sample design.** One 2018–2023 window per market; no walk-forward, no holdout, no pre-registration; the only regime analysis (Figure 10) uses an ex-post volume break at Q2 2020.
6. **No multiplicity control** over 8 reported tests (Table 2) or over the 12-strategy arm grid (4 arms × 3 sorts) from which the headline "9.97%" is selected as the maximum.
7. **Source-internal contradiction #1 (frontmatter):** blanket significance claim vs the Two-weeks Median-test p = 0.543472 in Table 2.
8. **Source-internal contradiction #2 (frontmatter):** "consistently higher returns than beta" vs two printed arms where beta loses less; Figure 8's legend (visually verified) shows only the four p-index-favouring series.
9. **Momentum/contrarian mirror hazard:** footnote 6 (PDF p.13) says "the graph of momentum strategy is the vertically inverted version of the contrarian strategy", yet the paired annualised numbers are not exact negatives in either pair (1.17% / −1.24%; 9.97% / −21.62%). Exact mirroring would require a compounding convention the source never states → reconciliation is a `data gap`.
10. **Opposite conclusions across the two markets** (A-share anti-persistence vs US persistence) from two 6-year samples — the thesis is regime- and market-dependent on its own evidence.
11. **Survivorship / point-in-time gaps:** "the five hundred stocks comprising the U.S. S&P 500 index from Yahoo Finance" over 2018–2023 and "the fifty stocks of the SSE 50 index" imply a fixed modern membership with no reconstitution history stated.
12. **Post-hoc subgroup reporting:** the materials-sector and top-three-weight rows are 1 of 7 sectors / 1 of many groupings, reported with no adjustment.
13. **Source-quality flags:** preprint only (no journal, no peer review, no code, no data, no availability statement) plus an arXiv admin text-overlap note pointing to `arXiv:2510.11074` (same corresponding author group).
14. **Model-derived, not option-derived, signal:** no traded option price, IV or option volume enters the p-index (see Economic mechanism) — so the option-insurance framing may be decorative relative to a range-scaled return rank.
15. **Contrary neighbours in our own pool (cross-record, named as distinct sources):** records in this repository document A-share execution infeasibility (limit-up/unfillable momentum), short-term-reversal decay under honest cost treatment, and option-derivative signals that fail falsification — see *Related Wiki records* and *Sources*. They are separate sources and are cited only as contrary context, never as evidence about this paper's numbers.

## Falsification plan

Every threshold below is `research-defined`; every operational rule not present in the source is `research-proposed`. Failure action for all tests: **keep `adoption: not-approved`; do not advance the record beyond research-only.**

- **F1 — Cost ladder (research-proposed).** Re-run all 12 SSE 50 arms and the 6 reported US arms with one-way costs of 0/5/10/20/30 bp plus a separate China stamp-duty rung and a 20%-ADV participation cap. **Fails (research-defined)** if the source's headline arm (p-ratio-efficient-contrarian) has net annualized return ≤ 0 at 10 bp, or if fewer than 4 of the 6 positive SSE arms stay positive at 10 bp.
- **F2 — Short-feasibility audit (research-proposed).** Mark every short leg against point-in-time borrow availability, price-limit and T+1 rules. **Fails (research-defined)** if ≥ 25% of short legs are unfillable in any year, or if removing unfillable legs flips the sign of the headline arm.
- **F3 — Point-in-time universe repair (research-proposed).** Rebuild SSE 50 and S&P 500 membership from historical reconstitutions. **Fails (research-defined)** if the sign of the headline arm changes, or if its annualized return shrinks by more than 50% relative to the source-reported 9.97%.
- **F4 — Random-group placebo (research-proposed).** Replace the p-ratio sort with 1,000 random top/bottom groups of identical size on identical dates. **Fails (research-defined)** if the real arm's annualized return sits below the 95th percentile of the placebo distribution in both markets.
- **F5 — Parameter perturbation (research-proposed).** Cut-offs 5/10/15/20% (SSE) and 20/30/40% (US); δ ∈ {0, r, 2r}; calibration index SSEC vs a broad A-share alternative; π fallback rule on/off. **Fails (research-defined)** if the headline result appears only in the originally printed cell (i.e. shrinks by more than 50% under any single adjacent setting).
- **F6 — Mechanism ablation: option/parity vs plain risk scaling (research-proposed).** Replace the p-index with (a) realised weekly downside deviation, (b) realised weekly range, (c) a raw past-return rank. **Fails (research-defined)** for the *option/parity mechanism claim* if a plain scaling matches the p-ratio arm within one bootstrap standard error; (the strategy may still be interesting, but the source's stated mechanism would be rejected).
- **F7 — Walk-forward / per-year sign consistency (research-defined).** Six rolling one-year folds per market. **Fails** if the anti-persistence pair ordering (efficient-contrarian > efficient-momentum) holds in fewer than 4 of 6 years in the A-share sample.
- **F8 — Block bootstrap (research-defined).** 52-week moving-block bootstrap, 1,000 draws, on the headline arm's weekly P&L. **Fails** if the 95% interval of the annualized return includes 0.
- **F9 — Multiplicity audit (research-defined).** Benjamini–Hochberg at q < 0.10 over the full arm × sort × market grid. **Fails** if no arm survives.
- **F10 — Third-market replication (research-proposed).** Pre-declare which direction (persistence or anti-persistence) is hypothesised, then test on one additional large-cap universe not used by the source. **Fails (research-defined)** for a *general* claim if the direction differs from the pre-declared one; the record then narrows to market-specific.
- **F11 — Execution-timing sensitivity (research-proposed).** Monday close vs next-open execution, plus a one-day-later exit. **Fails (research-defined)** if the edge exists only in the exact Monday-close cell (treated as a microstructure/rounding artefact).
- **F12 — Ex-ante regime split (research-proposed).** Replace the ex-post Q2-2020 volume break with a rolling median-volume rule computed only from past data. **Fails (research-defined)** if the reported low-volume/high-volume ordering of the two arms does not reproduce in both halves.

## Crypto portability

**`unproven`.**

- The source contains **no crypto evidence**: universes are SSE 50 and S&P 500 equities, 2018–2023, with an equity index as the binomial calibrator and a government-bond coupon as the risk-free rate.
- Structural portability is conceivable (the p-index needs only weekly OHLC of an index and its members plus a funding-ish rate, not an options chain), but every empirical claim — the A-share anti-persistence, the US persistence, the volume regime split — is equity-specific.
- Crypto-specific gaps a port must resolve, none of which the source addresses: perpetual funding and mark/index price, 24/7 candle boundaries (no "Monday close" analogue; weekly boundaries are a convention choice), venue fragmentation and per-venue survivorship, borrow/short mechanics and liquidation for the short legs, stablecoin/quote-currency effects, and the absence of a government-bond coupon proxy (a funding rate or T-bill would be a `research-proposed` substitution).
- Portability labelling must not be read as authorisation to trade; see Adoption boundary.

## Limitations

- **Not independently reproduced**; no code or data exist to reproduce it.
- **`data gap`:** all trading costs, spread, slippage, borrow, impact, capacity, turnover, dividends, margin/leverage, latency and fill model; US risk-free rate; sector-assignment vendor; volume-series vendor; MCIRS capital/labour frequencies; timezones; point-in-time membership; annualisation convention.
- **`underspecified`:** two-week/one-month/two-month fair-price cycle mechanics, tie handling, missing-week handling, US short-side arm returns, any ex-ante regime filter.
- **`unproven`:** mechanism (option/parity framing vs plain risk scaling), crypto portability, cross-market generality.
- **Source-quality:** preprint only, no peer review, arXiv admin text-overlap note, no data/code availability.
- This record is a normalised research capture. It contains no claim that any arm works after costs, and no claim that we verified any figure.

## Implementation status

`implementation_status: not-implemented`.

Nothing has been implemented in our research stack: no code, no data pipeline, no backtest, no Qlib run, no Paper/Testnet/Live activity, no production card, no candidate-pool entry, no Wiki Brain record. This document is the only artefact produced by this run.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

Presence of this record does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet or live trading. Any adoption decision must be explicit, separately reviewed, and based on this record plus current sources.

## Related Wiki records

Verified via `kb_search` on 2026-09-26 (only paths returned by the search are linked; nothing fabricated):

- Queries `p-index put option risk measure insurance fee` and `momentum contrarian China A-share weekly` returned **0 results** → **no mechanism-identical or strategy-identical Wiki page exists**, so no such link is asserted.
- `[[quant/china-ashare-limit-up-momentum-unfillable-execution-falsification-2026-09-13]]` — same market family (A-share), but unfillable-execution falsification of a limit-up momentum rule; contrary execution evidence, different signal and different mechanism.
- `[[quant/put-call-parity-implied-borrow-dividend-confounding-falsification-2026-09-13]]` — shares the put-call-parity identity as an input, but uses traded option prices to infer borrow/dividend; ours is a model-implied put with no traded option.
- `[[quant/option-implied-surface-cremers-weinbaum-skew-crash-regimes-2026-09-02]]` — equity option-implied cross-sectional signal, but market-priced IV surface vs our index-range binomial construct.
- `[[quant/drift-regime-gated-cross-sectional-value-reversal-2026-09-05]]` — cross-sectional reversal with regime gating; different signal construction and no option-flavoured scaling.
- `[[quant/m2-alpha-micro-macro-attention-a-share-deep-learning-ranking-2026-09-13]]` — A-share cross-sectional ranking from a different signal family (deep ranking), different data dependency.

Four-axis distinction vs adjacent repository records (all distinct source identities): mechanism (put-call-parity insurance-fee scaling vs L2/order-flow, factor-decomposition, IV-surface and parity-carry mechanisms), signal construction (weekly p-ratio/MCIRS top/bottom sort with a four-arm overlay), universe/market (SSE 50 + S&P 500 weekly large-cap equity), and material data dependency (index weekly high/low closes + bond coupon only — no option chain, no order book, no fundamentals beyond the MCIRS inputs).

## Sources

1. Xinzhao Xie, Bopei Nie, Kuo-Ping Chang, *"Stock Investment: The p-index Approach"*, arXiv:2606.08569v1 [q-fin.PM], submitted 7 Jun 2026, CC BY 4.0. https://arxiv.org/abs/2606.08569 ; pinned PDF https://arxiv.org/pdf/2606.08569v1 (1,702,220 bytes, 23 pages, SHA-256 `e3151492c41204fbd4053e906d04cd4ed6b3548b3c99b548b975a71e92c29823`); DOI https://doi.org/10.48550/arXiv.2606.08569. Read 2026-09-26; all quantitative claims in this record come from Tables 1–2, Figures 2–16 captions, §3.1–3.2 and §4 of this PDF.
2. arXiv admin comment on source 1: "arXiv admin note: text overlap with arXiv:2510.11074" — https://arxiv.org/abs/2606.08569 (Comments field), checked 2026-09-26.
3. Jing Li, Bowei Guo, Xinqi Xie, Kuo-Ping Chang, *"Evaluating Investment Performance: The p-index and Empirical Efficient Frontier"*, arXiv:2510.11074, submitted 13 Oct 2025 — https://arxiv.org/abs/2510.11074 ; read **for identity only** on 2026-09-26; no number, sample or method from it is used in this record.

**Deduplication evidence (pre-write, 2026-09-26):** deterministic source-identity search across **2,554 `*.md` files (990 top-level plus `.mimo-worktrees`, `.agents`, `.hermes`)** and **`coverage_manifest.csv` (5,808 lines)** for `2606.08569`, `2510.11074`, `p-index`, `p-ratio`, `MCIRS`, `minimum convex input requirement`, `Stock Investment: The p-index`, `insurance fee for each insured dollar`, `Kuo-Ping`, `Xinzhao`, `Bopei Nie`, `Jinhe Center`, `CSMAR` → **0 exact-identity hits before the write**; the only near hits were the substring `p-ratio` inside `…market-cap-to-thermocap-ratio…` filenames and unrelated `CSMAR` data-vendor mentions, all cleared as different sources. Wiki Brain `kb_search` found no p-index/mechanism page (queries above).
