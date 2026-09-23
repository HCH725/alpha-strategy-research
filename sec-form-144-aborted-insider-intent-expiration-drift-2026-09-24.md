---
schema: strategy-research-record-v1
title: "SEC Form 144 aborted insider-intent expiration drift (calendar-time DGTW long portfolio on non-executed sale notices)"
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equities
  - insider-trading
  - sec-form-144
  - event-study
status: research-only
confidence: low
source_as_of: 2026-02-19
sources:
  - "https://arxiv.org/abs/2602.17890"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# SEC Form 144 aborted insider-intent expiration drift (calendar-time DGTW long portfolio on non-executed sale notices)

## Provenance

- **Primary source (author, exactly as the source):** **Krishna Neupane** (single author; title page `kneupan@gmu.edu`, ORCID `0000-0003-1689-0557`; email domain implies George Mason University, but the paper states no affiliation line). Author identity agrees in three places: arXiv abstract-page authors field (`Neupane, Krishna`), PDF title page, and PDF `/Author` metadata (`Krishna Neupane`).
- **Version / date:** **arXiv v1 only** — abstract page shows a single `[v1]`, dateline "[Submitted on 19 Feb 2026]", citation_date `2026/02/19`; PDF stamp `arXiv:2602.17890v1 [q-fin.CP] 19 Feb 2026`; PDF title page dated `2026-02-19`. Abstract page has **no Comments, no `journal_ref`, no publisher DOI** (re-checked 2026-09-24) → `preprint only`; every PDF page is footered `PREPRINT/WORKING PAPER` and the title page adds "on going review for publication". arXiv DOI `10.48550/arXiv.2602.17890` verified to resolve (HTTP 302 → `https://arxiv.org/abs/2602.17890`, final 200; 2026-09-24). License statements conflict: PDF `/License` metadata = CC BY 4.0, while the title-page copyright text claims "All rights reserved… may be reproduced without prior permission" (`underspecified`); this record cites and normalizes only.
- **PDF checksum (pinned, read in full):** 28 pages, 389,824 bytes, SHA-256 `7a9cbf24247306e0e61e88ca30a6e9f882e07156f8c1d29c5ba6489b66943949`. `pypdf` extraction yielded 87,637 characters / 1,246 lines; all lines read directly (§1–§7, Tables 1–12, Figures 1–4, references).
- **Sample period (primary source):** **January 2003 – November 2025**, LSEG Insider database (formerly Thomson Reuters) via WRDS (§4). Event-study factor estimation uses a 100-day window `T−120 → T−20` relative to each intent filing.
- **Universe (primary source):** US-listed securities with CRSP daily returns linked at the **PERMCO** level; insiders must appear in **both** LSEG and BoardEx (personid → directorid → companyid → PERMCO bridge, §4.1–4.2); filings without a valid PERMCO excluded; securities need ≥100 days of CRSP history. Scale: **111,800 unique insiders, ~2.6M matched transactions (Table 5 N = 2,614,577)**, reduced to a "high-conviction" analytical sample of **≈1.5M** (Signal Magnitude `SM > 0`, duplicates/non-standard types dropped; Figure 1 notes call it 1.52 million). Exchange split (NYSE/NASDAQ/AMEX) is **not stated** (`data gap`). Attrition is admitted to come "primarily from insiders at smaller companies not covered by BoardEx" — i.e. coverage-selected.
- **Transaction-cost treatment (must-read sections checked):** Methods (§3.1–3.5), Data (§4), Results (§5), Discussion/Conclusion (§6–7) were read in full plus a full-text keyword scan: bare `cost(s)` → 8 hits, **all non-trading-cost contexts** (reputational cost, welfare cost, `scale_pos_weight` cost-sensitive learning ×3, Seyhun-title citation, and one qualitative sentence in §6 that small-cap signals face "higher transaction costs and lower liquidity"); `turnover|slippage|bid-ask|spread|borrow|short sale|fees|commission|latency|market impact|hedge` → **0 hits**; `Sharpe|drawdown|CER` → 0 hits. Cost/fill treatment is therefore **`not stated in source`** (`data gap`) — **not** inferred as zero — and every performance figure below must be read as **gross**.
- **Core performance numbers:** see Evidence → Source-reported; every figure carries its Table/Panel/Figure anchor.
- **Pre-write dedup (deterministic, whole repository):** ripgrep across **all files in the repository root** (all `*.md` records plus `coverage_manifest.csv`) for `2602.17890`, `10.48550/arXiv.2602.17890`, exact title `The Information Dynamics of Insider Intent`, `insider intent`, `[Ff]orm 144`, `Neupane`, `krishpn`, `Franzen`, `reporting inversion` → **0 matches** on every term. The phrase `predictive decoupling` (the paper's own coinage) exists in 7 records but only as references to `order-flow-imbalance-predictive-decoupling-cost-falsification-2026-09-12.md` (Tejas Mungale, `Tejas356/limit_order_book_engine`) — a different source and a different mechanism (order-flow-imbalance microstructure, not disclosure-regime event study); `git log --oneline -20` inspected as a convenience glance only, not as dedup. Wiki Brain `kb_search`: `"Form 144 insider intent expiration non-execution drift"` → 0 results; `"insider trading filing event study disclosure regime"` → 4 results, all different sources (`sec-form4-microcap…`, `sec-form-13f…`, `sec-form-10-12b…`, `news-event-tag-drift…`) — recorded as-is, no Wiki link invented.

## Economic mechanism

### Source-reported

The paper frames the SEC Form 144 regime (Notice of Proposed Sale of Securities) as a violation of the First Fundamental Theorem of Welfare Economics: a privately generated sell intent becomes public through a delayed notice whose execution is uncertain, so prices during the filing window do not reflect symmetric information. Its two hypotheses (§2, Table 1):

- **H1 (executed filings):** the interval between the Form 144 filing and the Form 4 execution is "a period of incomplete price discovery" during which the stock shows "a persistent negative price drift" as the proposed divestment gets priced — i.e. adding a signal → drift.
- **H2 (unexecuted filings):** expiration of the 90-day statutory window **without** (full) execution withdraws the selling signal; "this non-event triggers a price reversal" that removes the window's distortion — i.e. removing a signal → reversal. This is the record's tradable core.

Supporting narrative elements (all source-reported): a post-SOX "reporting inversion" where Form 4 lands within two business days while Form 144 is often delayed (citing **Franzen, Li & Vargus 2013**: Form 144 preceded Form 4 in 93.7% of pre-SOX cases but only 17.5% post-SOX — that statistic belongs to Franzen et al., relayed by this paper, not estimated here); insiders "sell into" market-wide appreciation to mask idiosyncratic signal (Lakonishok & Lee 2001; Cohen, Malloy & Pomorski 2012); an ML audit (SMOTE + `scale_pos_weight` XGBoost + deep architectures) is claimed to prove aborted intents are *not* pre-pricable from public data (the "opacity floor"), which is what makes the expiration surprise real; and a causal-ML ensemble (DML / GRF / X-Learner) is claimed to link the abort to an illiquidity (ΔAmihud) jump that scales with intent size. Large-cap significance is attributed to "Institutional Salience" (reputational cost of a false notice).

### Research interpretation

Falsifiable hypothesis: **a long-only disclosure-event premium** — stocks whose Form 144 notice expired with executed volume below the proposed amount deliver positive characteristic-adjusted (DGTW) returns after expiration, because the market had priced a "danger discount" against a sale that never cleared. Component roles (hybrid structure):

- **Event/regime:** Form 144's 90-day window closes with `Σ executed volume < proposed − ε` (the source's Eq. 6 / Table 2 "Non-executed Filing" — note this includes **partial** executions, not only zero execution).
- **Primary signal:** non-execution status, determinable from public data at filing + 91 days (Form 144 proposed shares vs. in-window Form 4 volumes — although the paper's own pipeline uses commercial vendor data, see Required data).
- **Portfolio:** monthly calendar-time aggregation on the expiration date; headline spec is equal-weighted (Eq. 8), with value-weighted and size-split variants.
- **Risk adjustment (not alpha by itself):** DGTW 5×5×5 size/value/momentum characteristic matching removes 125-cell benchmarks; no stop, sizing, or timing overlay is proposed by the source.

Two directions are internally contested **inside the source** and must not be treated as settled: Tables 10–11 implement H2 as a **positive** recovery, yet §5.3's volatility interpretation calls the withdrawal a "salient negative catalyst … more severe correction" (and mislabels it "a planned purchase" — Form 144 covers sales), §6 describes the market "processing the abortion as an indication of deteriorating firm prospects," and the introduction calls prior idiosyncratic volatility a "signal amplifier" whose sign is never pinned down (see Negative evidence 5/9). H1's short side (filing-window negative drift) is source-hypothesized but has **no supporting negative-drift table** (Negative evidence 4) — this record treats only the H2 long leg as an evidenced (if weak) hypothesis.

## Signal

All items `source-reported` unless marked otherwise.

- **Formation timestamp:** Form 144 filing date `F` (EDGAR); execution status becomes determinable at **`F + 91 days`** (source: a filing with no corresponding Form 4 by t+91 "is classified as a non-execution", §4.1); the calendar-time portfolio forms **monthly on expiration of the 90-day window (`T0`)** (§3.4.1). Timezone/session conventions are **not stated** (`data gap`; US equities implied).
- **Classification rule (source):** `Non-Execution = 1` if `Σ V_executed < V_proposed − ε` over `[F, F+90]` (Eq. 6); `ε` is "a tolerance threshold for market microstructure noise" whose **value is never given** (`underspecified`). Form 4 linkage: greedy search — each notice opens a 90-day window; Form 4 trades map to the earliest open window with remaining volume capacity; window closes at the declared `pshares` limit or expiry (§4.1).
- **Event-study calibration (source):** Carhart four-factor expected returns estimated on `T−120 → T−20` daily data (Eq. 4); `CAR[0,+2]` around the intent date and around the execution date; paired t-test on `CAR144 − CAR4`. A separate `CAR[+1,+5]` post-expiration test is claimed in §5.2 but its numbers are untraceable (Negative evidence 6).
- **Long entry (H2):** hold the non-executed names in the monthly calendar-time portfolio from `T0`; returns are DGTW-cell-adjusted daily excesses averaged across active names (Eq. 7–8). The paper **never states the holding window** after `T0`, the execution day/price, or the order type (`underspecified`). `research-proposed` operationalization (not source): confirm non-execution at `F+91`, enter at the **next trading day's close**, market orders, hold 1 calendar month, rebalance on monthly expirations.
- **Short entry (H1):** source hypothesizes shorting during the active filing window of executed notices, but **no negative-drift evidence table exists** — treat as unevidenced; any short leg is `research-proposed` and unsupported by this source.
- **Position sizing (source):** equal-weighted average (Eq. 8) as headline; value-weighted variant (Table 10 Panel A); below-/above-median size split (Table 11). No leverage, capacity, or participation rules (`data gap`).
- **Parameters (all `source-reported`):** 90-day statutory window; t+91 non-execution test; `T−120..T−20` estimation; `CAR[0,+2]`; DGTW 125-cell (5×5×5) benchmark; monthly CTP formation; `SM > 0` economic-significance filter; ML-only: SMOTE, `scale_pos_weight = 32.5`.
- **`underspecified` / `data gap`:** holding period after expiration; `ε` value; exact execution timing/price/order type; timezone/session; exchange split; tie/overlap handling when several notices for one stock expire in the same month; delisting-return treatment; EDGAR-only replication path (the source's identifier bridge is WRDS/BoardEx-proprietary and `EDGAR` is never mentioned — 0 hits). Because of these, the signal is **understandable but not fully reproducible from the paper alone**.

## Required data

- **Instrument / universe:** US-listed common stocks with CRSP history (exchange split not stated); affiliate/restricted sellers filing Form 144.
- **Venue / market type:** US equity exchanges, spot; SEC disclosure filings (Form 144 notices, Form 4 executions).
- **Vendors (commercial, as used by the source):** **LSEG Insider (ex-Thomson Reuters) via WRDS**, **BoardEx**, **CRSP**, **Compustat**, Fama-French factor library (SMB, HML, UMD; risk-free proxied by one-month T-bill). An EDGAR-only public replication would need its own person/firm identifier bridge — `underspecified` by the source.
- **Fields:** Form 144 filing date, proposed shares (`pshares`), security; Form 4 transaction date/volume/price; daily returns; market cap, book-to-market, 12-month momentum (DGTW cells); Amihud illiquidity (causal-analysis outcome).
- **Point-in-time:** filings are public at filing time; the t+91 status check only uses information observable by then (no inherent look-ahead in the tradable rule). However the executed-cohort matching **conditions on Form 144 preceding Form 4** (`File Date ≤ Transaction Date ≤ File Date + 90`) — per the paper's own Franzen et al. relay, that ordering is the 17.5% minority post-SOX — and on BoardEx coverage / valid PERMCO / ≥100-day CRSP history, all of which shape the sample (selection not discussed → `underspecified`).
- **Missing data:** dropped when CMER/SM missing, `SM ≤ 0`, duplicates, non-standard transaction types, unresolved identifiers, insufficient CRSP history; no imputation stated.
- **Timestamp / timezone:** not stated (`data gap`).

## Execution assumptions

**The source states essentially none.** No order type, fill model, signal-to-order delay, fees, slippage, spread, impact/capacity model, leverage/margin, borrow, latency, turnover, or failure handling appears anywhere in v1 (full-text scan: `turnover|slippage|bid-ask|spread|borrow|fees|commission|latency|market impact` = 0 hits; the single "transaction costs" sentence in §6 is qualitative commentary on small-cap limits to arbitrage, with no number). Reported alphas are therefore **gross of all trading frictions**, and turnover is never reported (`data gap`), so cost sensitivity cannot be inferred. The long-only H2 leg avoids short-borrow entirely; the unevidenced H1 short leg would additionally require borrow that the source never treats.

`research-proposed` operationalization (not from the source): confirm non-execution at `F+91` from public filings; enter next trading day close with market orders; equal-weight with a liquidity floor; net at κ ∈ {0, 10, 20, 50} bps per side; measure realized turnover (source reports none) before any tradability claim.

## Evidence

### Source-reported

All figures are third-party claims from Krishna Neupane, arXiv:2602.17890v1, **US equities, sample Jan 2003 – Nov 2025, gross of any cost**, not independently reproduced; each carries its Table/Figure anchor.

- **Table 5 (H1 univariate):** cumulative market excess return over the filing gap `μ = 1.6484%` (SE 0.000030, t = 553.930, p < 0.001), N = 2,614,577. Note the paper's Eq. 2 compounds **the market's** return in excess of the risk-free rate over `[F+1, E]` — this is a market-level quantity, not the stock's drift.
- **Figure 1:** mean Signal Magnitude rises from 1.63% (CMER decile 1) to 51.13% (decile 10) — insiders scale up sales into market appreciation.
- **Table 6 (paired event study, `CAR[0,+2]`, Carhart):** `CAR144 = +0.16%` (0.001589), `CAR4 = +1.45%` (0.014532), difference `CAR144 − CAR4 = −1.29%` (t = −3.094, p = 0.00216). Both mean CARs are **positive**; the paper nonetheless narrates the execution as the "more negative" event (Negative evidence 5).
- **Table 7:** mean estimation alpha 0.07%, mean β 1.0066 (IQR 0.68–1.22); `CAR4` mean +1.45% vs median −0.01%, SD 6.53% (heavy right skew).
- **Table 8 (abort-prediction audit; PR-AUC / recall / precision):** Elastic Net 0.2511 / 0.76% / 0.21; Weighted SVM 0.2509 / 0.76% / 0.21; Isolation Forest 0.2317 / 3.68% / 0.18; Balanced RF 0.4219 / 67.56% / 0.35; XGBoost 0.3972 / 53.00% / 0.36; NODE 0.3710 / 0.87% / 0.66; TabNet 0.3610 / 2.29% / 0.55; FT-Transformer 0.3698 / 4.03% / 0.56; DNDF-Proxy 0.2995 / 0.00% / 0.00; TFT-Proxy 0.3000 / 0.03% / 0.43.
- **Table 9 (XGBoost baseline):** row-normalized confusion — executed 69.31% correct / 30.69% false-alarm; aborted 46.77% missed (Type II "Strategic Opacity") / 53.23% detected; precision executed 0.82, aborted 0.36; recall 0.69 / 0.53; F1 0.75 / 0.43; accuracy 0.65; AUC-ROC 0.66. The table note references a "Panel C" that does not exist (Panels A/B only).
- **Figure 3 (SMOTE stress, 1.52M observations):** PR-AUC stuck ≈0.36, TPR ≤ 0.476, FN locked at **52.4%** under `scale_pos_weight = 32.5` and SMOTE ratio up to 1.0 — this 52.4% is the figure the abstract/discussion/conclusion headline as the "opacity rate" (baseline Table 9 FN is 46.77%).
- **Table 10 Panel A (headline calendar-time portfolio, monthly DGTW alpha, long expired non-executed notices):** equal-weighted **32.21 bps/month** (SE 0.003, **t = 1.03, p = 0.304 — not significant**), annualized ≈3.86% (§5.3); value-weighted **0.46 bps** (t = 0.03, p = 0.979).
- **Table 10 Panel B (cross-sectional alpha determinants):** Intercept 0.0046 (p = 0.116); Signal Magnitude −0.0014 (p = 0.227); Illiquidity −0.0000 (p = 0.990); **Prior Volatility −0.0034 (z = −2.312, p = 0.021)**; Filing Gap Days 0.0003 (p = 0.885).
- **Table 11 (size split):** small-cap (below median) 30.96 bps (t = 0.56, p = 0.574, n.s.); **large-cap (above median) 14.49 bps (t = 2.30, p = 0.021)** — the paper's only significant portfolio spec.
- **Figure 4 (causal ML):** six estimators put the abort's effect on Δ Amihud between **0.02 and 0.10** across the signal-magnitude distribution.
- **Table 12 (causal robustness):** Linear DML mean effect 0.0415, tail multiplier 2.01×, consensus ρ = 1.00; **Orthogonal Forest 0.0176, tail 2.63×, ρ = 0.66** (the abstract's "illiquidity jump of up to 2.63 times" is this *tail* multiplier — effect at the 1M-share threshold ÷ sample mean, not a mean effect); X-Learner 0.0007, 1.06×, ρ = 1.00; Honest/GRF anchor ≈ 0.00, 1.03×, ρ = 0.24, p < 0.001; XGBoost-DML −0.0026, 2.67×, ρ = −1.00 (sign-inverted).
- **Cited external estimate (not this paper's):** Franzen, Li & Vargus (2013), *Research in Accounting Regulation* — Form 144 preceded Form 4 in 93.7% of pre-SOX vs 17.5% of post-SOX cases (as relayed in §1; we did not open that paper).

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Only one of four reported portfolio specs is significant:** EW t = 1.03 (p = 0.304), VW t = 0.03 (p = 0.979), small-cap t = 0.56 (p = 0.574) are all nulls; only large-cap 14.49 bps reaches t = 2.30 (p = 0.021) — a single subsample among the reported splits, with no multiple-testing correction (`research interpretation`).
2. **Zero friction treatment:** no cost, turnover, slippage, spread, borrow, fee, or market-impact modeling anywhere in v1 (0-hit scan); no turnover figure; no Sharpe, drawdown, or CER anywhere. All results are gross; the small-cap leg (the larger point estimate) is the one §6 itself admits faces "higher transaction costs and lower liquidity."
3. **No out-of-sample discipline:** `out-of-sample|holdout|walk-forward|k-fold|test set|validation set` → 0 hits; the ML audit states **no train/test protocol at all** (`data gap`), so even "in-sample" cannot be confirmed — the opacity numbers should be treated as in-sample unless proven otherwise.
4. **H1 (the short side) has no supporting evidence table:** H1 predicts "a persistent negative price drift" during the filing window, yet Table 6's intent-window `CAR144` is **+0.16%** — which the paper itself calls "a routine liquidity event" — and no table reports a negative stock drift over the gap. Table 5's significant +1.65% is (per Eq. 2) the *market's* excess return over overlapping windows, with t = 553.93 computed on 2.6M heavily overlapping gap windows (pseudo-replication risk, `research interpretation`).
5. **Table 6 vs. its narrative have opposite signs:** the table is internally consistent (0.16% − 1.45% = −1.29%), but §5.1 claims the execution "prices the stock 1.3% lower relative to the initial intent signal" — the printed means show the execution-window CAR **exceeding** the intent-window CAR by 1.29pp. Compounding it, `CAR4` mean +1.45% with median −0.01% (SD 6.53%) means the mean is tail-driven, unaddressed by the source.
6. **Untraceable result:** §5.2 states "As shown in Table 4, the CAR[+1,+5] following the expiration date is significantly positive (μ = 0.00%, p < 0.05)" — Table 4 is the evidence-hierarchy summary (contains no such numbers), the mean is reported as 0.00%, and no other table carries this test (`data gap`).
7. **The ML evaluation sample's composition is arithmetically incoherent (`research interpretation`, our calculation):** Table 9's reported precision 0.36 with recall 0.5323 and row-normalized false-alarm 0.3069 imply an aborted-class prevalence of ≈24.5%; its accuracy 0.65 implies ≈26.8%. That is ~8× §3.5's stated "3.08% class imbalance (N = 2,614,577)" (which `scale_pos_weight = 32.5` corroborates: minority ≈ 3%), and it matches neither that nor the introduction's claim of a "non-execution frequency of 52.4%." Three mutually inconsistent prevalence statements; the evaluation set is `underspecified`.
8. **The 52.4% headline is regime-shifted and mislabeled:** abstract/discussion/conclusion cite 52.4% opacity (Figure 3's SMOTE-stressed FN rate), while the baseline XGBoost FN is 46.77% (Table 9 / §5.2), and the introduction relabels 52.4% as the *non-execution frequency* — contradicting §3.5's ~3% class share. Table 9's note also cites a non-existent "Panel C."
9. **Directional narrative conflict inside the source:** H2 and Tables 10–11 implement a **positive** recovery on expiration (EW +32.21 bps; large-cap +14.49 bps), yet §5.3 interprets the significant negative Prior-Volatility coefficient as the withdrawal being "a salient negative catalyst … leading to a more severe correction" (and calls it "the withdrawal of a planned **purchase**" — Form 144 is a sale notice), §6 says the market "processes the abortion as an indication of deteriorating firm prospects" / converges on "the negative impact of the decoupling," and the introduction calls prior volatility a "signal amplifier" without fixing a sign. The source never reconciles positive-recovery vs negative-signal framing — hence `confidence: low`.
10. **Abstract misattributes its own number:** the abstract credits 32.21 bps to "small-cap portfolios," but Table 10's 32.21 bps is the full-sample **equal-weighted** CTP; Table 11's small-cap figure is 30.96 bps.
11. **The "causal consensus" is mostly near-zero:** of five Table 12 estimators, mean effects are ≈0.00 (Honest anchor, ρ = 0.24), 0.0007 (X-Learner) and −0.0026 with ρ = −1.00 (XGBoost-DML, directionally inverted); the abstract's 2.63× is a *tail* multiplier from one estimator; the GRF's p < 0.001 is asserted alongside a ≈0.00 mean effect without explanation.
12. **Sample selection & label breadth:** the executed cohort is conditioned on Form 144 preceding Form 4 — the 17.5% minority ordering post-SOX by the paper's own cited statistic — plus BoardEx-coverage, PERMCO-resolution and history filters, none discussed as selection; "aborted/non-executed" **includes partial executions** (`ΣV < proposed − ε`, ε unstated), so the tradable label is "under-executed," not "zero-execution."
13. **Source-quality negatives:** single-author preprint with no journal status; no `replication|code availability|data availability|supplement` statement (the 29 bare `github` hits are all the `krishpn.github.io` homepage footer); commercial-data dependency (WRDS/LSEG/BoardEx) with a proprietary identifier bridge; sample ends Nov 2025 with no holdout; AI copy-editing disclosed; license metadata (CC BY 4.0) conflicts with the title-page "All rights reserved."

## Falsification plan

Thresholds are `research-defined falsification threshold`; operational choices are `research-proposed`. None are source-specified.

- **F1 — post-sample point-in-time persistence (`research-defined`):** rebuild the t+91 non-execution signal from public EDGAR filings for 2025-12-01 → present with no re-tuning (90-day window, Eq. 6 rule). Fail if the EW long-expired monthly DGTW alpha is ≤ 0 or its one-sided t < 1.645.
- **F2 — the source's only significant claim (`research-defined`):** re-run the Table 11 above-median-cap split. Fail if large-cap alpha is ≤ 0 or |t| < 1.96 — the entire significance story rests on this one cell.
- **F3 — capacity red flag (`research-defined`):** the value-weighted spec must be economically positive (source: 0.46 bps, t = 0.03). Fail if VW alpha ≤ 0 — then the "alpha" is an equal-weight small/mid-cap artifact that §6 admits is cost-fragile.
- **F4 — cost stress (`research-proposed` grid):** net at κ ∈ {0, 10, 20, 50} bps per side using **measured** turnover (source reports none, `data gap`). Fail if net CER at κ = 20 bps ≤ a passive large-cap benchmark over the same sample.
- **F5 — placebo (`research-defined`):** 500 shuffles of expiration dates (±10 trading days) through the identical pipeline; require the empirical alpha beyond the 95th percentile of the shuffle distribution (p < 0.05).
- **F6 — direction ablation, the source's own contradiction (`research-defined`):** split the portfolio into prior-idiosyncratic-volatility quintiles. Fail if the high-vol cohort is ≤ 0 (the §5.3 "negative catalyst" reading) while the headline depends only on low-vol names, or if sign coherence between H2 and §5.3 cannot be established — either outcome invalidates the mechanism as stated.
- **F7 — classification-rule robustness (`research-defined`):** re-run under a strict zero-execution definition (exclude partials) and ε ∈ {0, 1%, 5%} of proposed shares. Fail if |alpha| collapses ≥ 50% vs the source rule — that would make the signal an artifact of the unstated tolerance.
- **F8 — vendor-selection replication (`research-defined`):** an EDGAR-only identifier bridge (no WRDS personid/BoardEx matching) must reproduce the sign. Fail if bridge attrition flips or nulls the result — that would attribute the finding to vendor sample selection.
- **Action on failure:** keep the record research-only; log the failed test as negative evidence against this family; no implementation, no candidate promotion.

## Crypto portability

**unproven.** The mechanism is bolted to a specific US regulatory construct: a public notice of proposed sale with a **90-day statutory execution window** and a separate next-day execution report, whose *cancellation* is observable only by comparing the two. Crypto has no Form 144/Form 4 analogue — the closest candidates (token-unlock schedules, team/insider lockup releases, exchange reserve attestations) have no notice-vs-execution split, no statutory window, and no "aborted intent" state to fade. Additional porting risks: 24/7 sessions with no month/calendar boundary for the monthly calendar-time portfolio, venue fragmentation of any disclosure signal, perp funding and borrow mechanics absent from the design, and the long-only H2 leg's dependence on US listing/insider-identity structures. Any crypto version would be a **different data structure, not this signal** — a ported hypothesis at best, not crypto empirical evidence; crypto portability is not authorization to trade.

## Limitations

- `not independently reproduced`; all performance figures are `source-reported`, **gross**, and only 1 of 4 portfolio specs is significant.
- `data gap`: transaction costs, slippage, spread, borrow, fees, turnover, capacity, fill model, holding window after expiration, ε in the classification rule, timezone/session, exchange split, the `CAR[+1,+5]` result's provenance, and the ML evaluation set's composition/protocol.
- `underspecified`: within-sample changes to Form 144 filing requirements over 2003–2025 are never discussed (the pre/post-SOX ordering shift is cited but never used to split the sample); the EDGAR-only replication path (the source's bridge is vendor-proprietary); partial-vs-zero execution conflation under the unstated ε; tie/overlap handling in the monthly CTP.
- `unproven`: persistence after 2025-11; net-of-cost tradability; the H1 short side (no supporting table); coherence of the expiration response's direction (positive recovery vs "negative catalyst / deteriorating prospects" inside the same paper).
- Source-quality: single-author preprint only (no journal_ref/DOI as of 2026-09-24), no code/data availability statement, commercial data dependency, disclosed AI copy-editing, license metadata conflict, and at least eight internal inconsistencies catalogued in Negative evidence — hence `confidence: low` (confidence in the *research interpretation*, not a claim about profitability).
- Selection/publication bias: coverage- and ordering-conditioned sample; no multiple-testing correction across the reported splits; publication/selection bias unaddressed by the source.

## Implementation status

`implementation_status: not-implemented`. Nothing in this record has been implemented in our research stack: no signal pipeline, no backtest, no Qlib full-backtest validation, no survivor bundle, no Paper, Testnet, or Live activity. This record is normalized research material only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this record does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; or approved for implementation, paper trading, testnet, or live trading.

## Related Wiki records

Wiki Brain `kb_search "Form 144 insider intent expiration non-execution drift"` returned **0 results** (no Form 144 page exists); `kb_search "insider trading filing event study disclosure regime"` returned four pages, all different sources — linked here as the retrieval hook:

- [[quant/sec-form4-microcap-insider-purchases-gradient-boosting-momentum-2026-09-05]] — same broad insider-disclosure family, but a different source (Zhao, arXiv 2602.06198) and a materially different mechanism: **Form 4 purchases** in microcaps with XGBoost detection and disclosure momentum, vs this record's **Form 144 sale-intent non-execution** calendar-time expiration portfolio.
- [[quant/sec-form-13f-institutional-cloning-staleness-falsification-2026-09-13]] — different SEC form (13F), different mechanism (45-day institutional cloning staleness).
- [[quant/sec-form-10-12b-spinoff-drift-decay-falsification-2026-09-13]] — different form/event (spin-off distribution drift).
- [[quant/news-event-tag-drift-rumor-resolution-placebo-adjusted-momentum-2026-09-02]] — generic news-event drift family, different sources.

Related records in this repository (different sources, distinct mechanisms): `buyback-announcement-drift-smallcap-illiquidity-falsification-2026-09-13.md` (issuer-repurchase event, not insider notice); `order-flow-imbalance-predictive-decoupling-cost-falsification-2026-09-12.md` (shares the phrase "predictive decoupling" only — order-flow microstructure from a different author/repo).

## Sources

1. Krishna Neupane, *"The Information Dynamics of Insider Intent: How Reporting Inversions (Form 144) Mask Informational Rents in Insider Sales (Form 4)"*, arXiv preprint **arXiv:2602.17890v1 [q-fin.CP]**, submitted 19 February 2026 (28 pages; SHA-256 `7a9cbf24247306e0e61e88ca30a6e9f882e07156f8c1d29c5ba6489b66943949`). https://arxiv.org/abs/2602.17890 ; arXiv-issued DOI `10.48550/arXiv.2602.17890` (302 → abstract page, verified 2026-09-24). Preprint only: no Comments, no `journal_ref`, no publisher DOI on the abstract page as of 2026-09-24; PDF pages footer "PREPRINT/WORKING PAPER". Sample/data source of record: LSEG Insider via WRDS, January 2003 – November 2025 (§4).
2. Laurel Franzen, Xu Li, Mark E. Vargus (2013), *"The Effect of Sarbanes-Oxley on the Timely Disclosure of Restricted Stock Trading"*, Research in Accounting Regulation 25(1): 47–52 — **cited by source 1 (§1) for the 93.7% / 17.5% Form-144-before-Form-4 ordering statistics; we did not open this paper; those figures are Franzen et al.'s as relayed, not verified here.**
