---
schema: strategy-research-record-v1
title: "Cost-sensitive online window-size expert aggregation over rolling mean-variance portfolios (Hedge / Fixed Share, arXiv:2609.29887)"
created: 2026-09-25
updated: 2026-09-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-24
sources:
  - "https://arxiv.org/abs/2609.29887 (arXiv:2609.29887v1 [math.OC primary, cs.LG, q-fin.PM], submitted Thu 24 Sep 2026 14:35:25 UTC, 2,309 KB; only version — https://arxiv.org/abs/2609.29887v2 and https://arxiv.org/html/2609.29887v2 both HTTP 404, checked 2026-09-25)"
  - "https://arxiv.org/html/2609.29887v1 (pinned full text, 512313 bytes, SHA-256 5db73795770314df2e3224ef855a9166c173f8a9e516d736e67786a6e4ced3a2, converted to 83839 characters / 1351 lines and read end to end on 2026-09-25: Abstract, Sections 1-5, References, Appendix A proofs, Appendix B.1-B.5, Appendix C ticker lists, Tables 1-7, Figures 1-13 captions)"
  - "https://doi.org/10.48550/arXiv.2609.29887 (DataCite DOI, HTTP 302 -> https://arxiv.org/abs/2609.29887, checked 2026-09-25; no journal-ref field, no arXiv Comments field, no publisher DOI, no peer-review statement anywhere in the pinned text -> preprint only)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions:
  - "Tables 2-7 report a positive 'Sample Mean of Return(%)' in 27 of 30 metric rows while the same rows print a negative 'Annualized Sharpe Ratio' in 28 of 30 rows (25 rows are positive-mean AND negative-Sharpe; our count on the pinned v1 tables). The paper never states a Sharpe convention (risk-free rate, annualization factor, sign, or which return series), and no plausible risk-free rate can flip a +0.1142%/day sample mean negative. Reconstructing the printed column from the printed inputs under the conventional formula does not match either: our arithmetic gives (0.1142/100)/0.0174*sqrt(252) = +1.042 against printed -1.0535 for the DJIA 5-day expert, and +0.377 against printed -1.8158 for the DJIA 10-day expert (pinned v1 text, read 2026-09-25). Every Sharpe figure below is therefore reported verbatim as source-reported and treated as a data gap, never as a usable statistic."
---

# Cost-sensitive online window-size expert aggregation over rolling mean-variance portfolios (Hedge / Fixed Share, arXiv:2609.29887)

## Provenance

- **Paper**: Yi-Chen Liu (Interdisciplinary Program of Management and Technology, National Tsing Hua University) and Chung-Han Hsieh (Department of Quantitative Finance, National Tsing Hua University, Taiwan; `ch.hsieh@mx.nthu.edu.tw`), *Cost-Sensitive Online Window Size Selection for Portfolio Management*, `arXiv:2609.29887v1 [math.OC]`, cross-listed to `cs.LG` and `q-fin.PM`.
- **Version/date**: only `v1`, submitted 24 Sep 2026 14:35:25 UTC; `v2` and `html/...v2` both return **HTTP 404** (checked 2026-09-25). arXiv **Comments field absent** and **journal-ref absent** (0 occurrences in the landing page); no publisher DOI beyond DataCite; no peer-review statement in the pinned text → **preprint only, unrefereed as captured**.
- **DOI**: DataCite `10.48550/arXiv.2609.29887` → HTTP 302 → `https://arxiv.org/abs/2609.29887` (checked 2026-09-25).
- **Licence**: arXiv **perpetual non-exclusive distribution licence** (`arxiv.org/licenses/nonexclusive-distrib/1.0/`, link on the abs page) → this record cites and normalises short claims and printed figures only; no reproduction of the text.
- **Pinned primary source**: `https://arxiv.org/html/2609.29887v1`, **512,313 bytes, SHA-256 `5db73795770314df2e3224ef855a9166c173f8a9e516d736e67786a6e4ced3a2`**, converted to 83,839 characters / 1,351 lines and **read end to end on 2026-09-25** (Sections 1–5, References, Appendices A–C, Tables 1–7, figure captions).
- **Keywords printed by the source**: Online Learning, Optimal Sliding Window, Fixed Share Algorithm, Portfolio Optimization, Financial Optimization Algorithm.
- **Code / data**: **no repository URL, no code link, no data-availability statement, no dataset vendor, and no solver invocation is stated anywhere in the pinned text** (the only solver mention is the generic suggestion "can be solved efficiently by a standard solver such as CVXPY", §2.1). Word-boundary scan for `github`, `dataset`, `yfinance`, `yahoo`, `vendor`, `data source`: 0 relevant hits → **the empirical pipeline is a data gap and cannot be re-run from the source alone**.
- **AI-use disclosure by the source** (§5, AI Use Statement): "Generative AI tools (ChatGPT 5.6 sol and Gemini 3.8 Flash) were used to assist with language editing and presentation, and to provide feedback on mathematical derivations and proofs. The authors reviewed and independently verified all AI-assisted content."
- **Same-author adjacent record already in this repo**: Chung-Han Hsieh also co-authored *Certified High-Dimensional Wasserstein Robust Portfolio Optimization* (`arXiv:2608.07032v1`), captured as `wasserstein-robust-portfolio-hyperplane-dual-lp-2026-09-02.md` — **different source identity and different mechanism** (static ambiguity-set-robust mean-variance certification, no online aggregation, no window experts, no regret bound).

## Economic mechanism

### Source-reported

The paper's thesis is that **the estimation window is the consequential free parameter in rolling portfolio construction, and it should be treated as a sequential model-selection problem rather than a fixed choice.** Its two-level framework (§1, §2.1) is: (i) each candidate window `j ∈ N` runs its own **cost-sensitive mean-variance program** over the last `j` days — `max_w μ̂_j(t)ᵀw − ½wᵀΣ̂_j(t)w − c(t)‖w − w_j(t−1)‖₁` on the long-only simplex `W = {w ∈ ℝ₊^m : wᵀ1 = 1}` (Problem 2.1); (ii) an outer online learner aggregates the resulting portfolios, `ŵ(t) = Σ_j q_j(t) w_j(t)`, with weights `q(t)` updated from **turnover-inclusive expert losses** `ℓ̃_j(t) = ℓ(w_j(t), y(t)) + c(t)‖w_j(t) − w_j(t−1)‖₁` (Problem 2.4). Two aggregators are used: **Hedge** (Littlestone–Warmuth, static case `α = 0`) and **Fixed Share** (Herbster–Warmuth, mixing parameter `α > 0`), whose mixing step keeps `q_j(t+1) ≥ α/n` so every window expert keeps a floor weight (§3.2).

The source's stated economic argument (§1) is the familiar bias–variance/adaptation trade-off: long windows smooth noise and capture persistent structure, short windows react quickly, and **changing the aggregation weights itself induces turnover even when no expert portfolio changed** — hence "each window expert's transaction costs do not, by themselves, account for the cost of the aggregate portfolio". The theoretical contribution is a decomposition of cost-sensitive tracking regret into an expert-loss regret term plus an **additional turnover-cost term `Σ_t c(t)‖q(t) − q(t−1)‖₁`** whose coefficient 1 is proved sharp (Theorem 3.1, eqs. 3–7), leading to Corollary 3.4 (finite-horizon bound), Proposition 3.5 (optimal `α* = K/(T−1)` and cost-dependent `η*`) and Corollary 3.7 (asymptotic cost-sensitive no-regret for `K(T) = o(T)`).

Crucially, the source **does not claim to predict returns**. Appendix B.5 states the empirical studies are "intended solely to demonstrate the practical application of our framework over a restricted timeframe … rather than to assert any predictive capability regarding the future performance of specific financial instruments."

### Research interpretation

Falsifiable hypothesis: **estimation-window length is a latent, slowly changing regime variable; aggregating several fixed windows with turnover-inclusive losses and a mixing floor delivers lower cost-sensitive tracking regret, lower drawdown and (in some samples) higher net cumulative return than any single fixed window and than frictionless-tuned online portfolio baselines, net of a proportional turnover cost.**

Component roles (as in the source, with our labels):
- **Regime / adaptive layer**: Fixed Share mixing `α` over the window-expert simplex (source-reported); Hedge is the `α = 0` ablation.
- **Primary signal**: rolling mean–variance weights from the last `j` days of **price** data only — no forecast, no factor, no exogenous signal (source-reported). Any alpha here would come from *allocation and turnover control*, not from return prediction; that is a risk/allocation hypothesis, not a predictive-alpha hypothesis.
- **Confirmation filter**: none in the source.
- **Risk / exit**: none — the simplex forces full investment (with BIL as the cash sleeve); no stop, no drawdown control, no de-risking rule exists in the source.
- **Sizing**: output of the MV program (source-reported); no position caps, no ADV or concentration limits are stated.

Competing explanations we must test rather than assume: (a) the aggregation may simply be a **drawdown smoother that sacrifices return** (our count below shows exactly that on DJIA); (b) the reported advantage may be an **artifact of ex-post universe construction**; (c) the baselines may be **mistuned for costs**, which the source itself concedes; (d) the synthetic win may be **by construction** because the DGP hard-codes the window switch.

## Signal

All items `source-reported` unless marked otherwise.

- **Formation timestamp**: at each trading day `t`, expert `j` estimates `μ̂_j(t), Σ̂_j(t)` from returns `y(s), s ∈ [t−j, t−1]` — i.e. **prices through `S(t)`** — and the aggregate weight `ŵ(t)` is chosen **before `y(t)` is revealed** (§2.2), where `y(t) = (S(t+1) − S(t))/S(t)`. The source calls the moment "immediately before rebalancing at time t" (Problem 2.1). Timezone, session, and whether the trade is struck on the close of `t` or the open of `t+1` are **not stated in source**; under the printed equations the portfolio earns `S(t)→S(t+1)` from data through `S(t)`, which implies same-close execution.
- **Lookback**: candidate set `N = {5, 10, 21, 30, 41, 50, 63, 126}` trading days for both empirical studies (§4.2, App. B.4, B.5) and `N = {5, 10, 21, 63}` for the synthetic study (§4.1); endpoints inclusive over the last `j` returns; no warm-up rule stated beyond needing `max N` returns of history.
- **Long / short**: **long-only** — `w ∈ ℝ₊^m`, `wᵀ1 = 1`; no shorting, no leverage, no margin anywhere in the source (0 hits for `short sell`, `shorting`, `leverage`, `margin`).
- **Entry / exit / holding**: there is no discrete entry or exit. The book is **re-estimated every trading day** (each `t` produces a new `ŵ(t)`); implied holding period is one bar between successive rebalances; overlapping positions do not apply (single portfolio). Trade flow is `‖ŵ(t) −ŵ(t−1)‖₁` on the aggregate plus each expert's own `‖w_j(t) − w_j(t−1)‖₁`.
- **Aggregation parameters**: Hedge/Fixed Share exponentiated update `q_j^exp(t) ∝ q_j(t)e^{−η ℓ̃_j(t)}` (eq. 9) then the share step `q_j(t+1) = (1−α)q_j^exp(t) + α/n` (eq. 10); optimal settings from Proposition 3.5 are `α* = K/(T−1)` and `η* = (1/(b−a))·sqrt((8/T)((K+1)log n + (T−1)H(K/(T−1))))` for `C_T > 0`, with the `K = 0, α = 0` Hedge case `η* = sqrt(log n / A_T)`.
- **Switching budget**: `K(T) = ⌊ T / (log T · (log log T)^{1+ε}) ⌋` for any constant `ε > 0` (App. B.4), satisfying the `o(T)` condition of eq. 2; the source states "we use this `K(T)` as our switching budget `K` estimator" in the empirical studies.
- **Underspecified / not reproducible from the text**: the **numeric values of `η`, `α`, `ε`, `b − a`, horizon `T`, and the initial portfolio `w_0` actually used in Tables 1–7 are never printed** (0 hits for `hyperparameter`, `grid`, `seed`, `in-sample`, `test set`); the unit of "Sample Standard Deviation" is not labelled; no solver, tolerance, or re-optimisation cadence beyond "at time `t`" is stated. **The signal is therefore reproducible in structure but not in numbers** — reconstruction requires re-deriving `η`/`α` from an unstated `b − a` and `T`.

## Required data

Source-reported (§4.2, App. B.4–C):

| Study | Universe | Window | Extra sleeve | Source-stated construction |
|---|---|---|---|---|
| Synthetic | 32 artificial stocks `SYN_1`–`SYN_32`, 2,000 business days from 1 Jan 2020 | full span | none | DGP `y(t) = μ + α((1/j_t)Σ_k y(t−k) − μ) + ε(t)` with `j_t = 63` for the first 1,000 days and `j_t = 5` after, i.e. **the regime switch is inserted by the designer** (§4.1) |
| DJIA | the **30 exact DJI components over 2021/03/04–2024/02/25**, chosen because that span contains "no asset additions or removals", plus **BIL** (1–3 Month T-Bill ETF) as risk-free sleeve | 2021/03/04–2024/02/25 | BIL | App. B.4, ticker list App. C |
| S&P 500 | **481 GSPC components present across 2020/01/02–2026/08/01** after "we remove all the changed stocks", plus **BIL** | 2020/01/02–2026/08/01 | BIL | App. B.5, ticker list App. C |

- **Fields**: adjusted closing prices only (the sole price definition in the source, §2.1); returns derived from them. No volume, book, funding, OI, borrow, or fundamental field is used.
- **Point-in-time**: **fails by construction** — both universes are defined by what stayed in the index over the *whole* sample (a name that entered or left during the window is removed). Membership is not dated, no vendor is named, no survivorship/delist handling is described → `data gap`.
- **Timestamp / missing data**: timezone, calendar, corporate-action treatment beyond "adjusted", and stale/missing-bar handling are `not stated in source`.
- **Cash sleeve**: BIL is included in every empirical portfolio (App. B.4–C).

## Execution assumptions

- **Cost model (the paper's central design point)**: a **proportional transaction-cost rate `c(t)` charged on L1 turnover**, `c = 0.001 = 10 bps` in every experiment (§4.1, §4.2, Table 1 caption, App. B.4). The cost appears **three times**: inside each expert's MV objective, inside the expert loss `ℓ̃_j` that drives Hedge/Fixed Share, and inside the account-value recursion `V(t+1) = V(t)(1 + ŵ(t)ᵀy(t) − c‖ŵ(t) − ŵ(t−1)‖₁)` (App. B.1, with the standing assumption that the bracket stays positive).
- **Cost coverage (Methods-level word-boundary scan of the pinned v1 text, 2026-09-25)**: `transaction cost` 12, `turnover` 20, `rebalancing` 1, `risk-free` 4 (portfolio definition + BIL), `slippage` **0**, `bid-ask` **0**, `spread` **0**, `commission` **0**, `fee`/`fees` **0**, `leverage` **0**, `margin` **0**, `borrow` **0**, `market impact` **0**, `latency` **0**, `fill` **0**, `participation` **0**, `ADV` **0**, `capacity` **0**, `dividend` **0**, `liquidation` **0**, `funding` **0** (the single hit is arXiv's own "Major funding support" footer). → **spread, slippage, impact, latency, fill, borrow, capacity, dividend treatment and any fee other than the flat 10 bps are `data gap` — never read as zero.**
- **Per-side vs round-trip**: `underspecified` — the source says only "10 bps for turnover trades"; `‖Δw‖₁` on a long-only simplex equals 2× one-way turnover, so whether 10 bps applies per unit of `‖Δw‖₁` or per unit of traded notional is not clarified.
- **Single cost point**: only `c = 0.001` is ever run; **no cost ladder, no spread scenario, no cost sensitivity exists in the source**.
- **Fill / timing**: order type, market vs limit, partial fills, and signal-to-order delay are `not stated in source`; the printed timing implies same-close rebalancing with data through that same close.
- **Leverage / shorting / margin**: excluded structurally (simplex, `ℝ₊`); BIL is the only cash instrument.
- **Capacity / participation**: `not stated in source` (no ADV, no position limits, no concentration cap; HHI or max single-name weight never printed).

## Evidence

### Source-reported

All figures below are `source-reported` from the pinned `arXiv:2609.29887v1` (Table captions cited per row); none has been independently reproduced. Both studies run at `c = 0.001`.

**Table 1 summary (source caption: "Cumulative return and maximum drawdown (MDD) are reported in percent; MDD is signed"):**

| Algorithm | DJIA Return % | DJIA MDD % | S&P 500 Return % | S&P 500 MDD % |
|---|---|---|---|---|
| Hedge | 41.6977 | −12.6326 | 578.6997 | −56.0818 |
| Fixed Share | 38.1074 | −12.9282 | 471.0522 | −57.8097 |
| UP (Cover 1991) | 48.9870 | −20.3914 | 205.2483 | −38.3269 |
| EG | 48.5459 | −20.3837 | 205.7900 | −38.2862 |
| PAMR | −88.2410 | −88.9765 | −52.0775 | −84.5912 |
| CWMR | −88.4022 | −89.1155 | 205.5993 | −59.5749 |
| OLMAR | −38.8878 | −61.0217 | −44.0283 | −81.6301 |

**Per-window and per-algorithm detail (Tables 2–4 = DJIA 2021/03/04–2024/02/25; Tables 5–7 = S&P 500 2020/01/02–2026/08/01; rows: Cumulative Return % / Sample Mean of Return % / Sample SD / Annualized Sharpe Ratio / Max Drawdown %):**

| Row | DJIA | S&P 500 |
|---|---|---|
| 5-day | 109.8576 / 0.1142 / 0.0174 / −1.0535 / −22.5798 | 256.0875 / 0.1840 / 0.0468 / −0.1767 / −62.5062 |
| 10-day | 21.0539 / 0.0394 / 0.0166 / −1.8158 / −28.3883 | 640.7924 / 0.2313 / 0.0476 / −0.0160 / −63.1732 |
| 21-day | 7.6831 / 0.0216 / 0.0153 / −2.1586 / −34.2497 | 361.6846 / 0.2013 / 0.0473 / −0.1167 / −74.2201 |
| 30-day | 57.0513 / 0.0740 / 0.0165 / −1.4931 / −24.3892 | 261.9684 / 0.1857 / 0.0469 / −0.1708 / −76.1460 |
| 41-day | 85.2425 / 0.0943 / 0.0155 / −1.3843 / −22.2521 | 1173.9300 / 0.2605 / 0.0464 / 0.0837 / −64.1657 |
| 50-day | 50.2176 / 0.0672 / 0.0160 / −1.6089 / −26.1014 | 385.5686 / 0.1995 / 0.0460 / −0.1261 / −78.5935 |
| 63-day | 35.3917 / 0.0526 / 0.0155 / −1.8141 / −26.8669 | 316.8115 / 0.1851 / 0.0445 / −0.1817 / −67.1939 |
| 126-day | 157.8256 / 0.1367 / 0.0140 / −1.0478 / −22.2768 | 1881.7486 / 0.2771 / 0.0440 / 0.1480 / −60.4582 |
| Hedge | 41.6977 / 0.0533 / 0.0115 / −2.4214 / −12.6326 | 578.6997 / 0.1816 / 0.0364 / −0.2373 / −56.0818 |
| Fixed Share | 38.1074 / 0.0500 / 0.0117 / −2.4308 / −12.9282 | 471.0522 / 0.1737 / 0.0372 / −0.2663 / −57.8097 |
| UP | 48.9870 / 0.0499 / 0.0093 / −3.0639 / −20.3914 | 205.2483 / 0.0711 / 0.0129 / −2.0168 / −38.3269 |
| EG | 48.5459 / 0.0495 / 0.0093 / −3.0720 / −20.3837 | 205.7900 / 0.0712 / 0.0129 / −2.0159 / −38.2862 |
| PAMR | −88.2410 / −0.2262 / 0.0190 / −3.8025 / −88.9765 | −52.0775 / 0.0094 / 0.0321 / −1.1188 / −84.5912 |
| CWMR | −88.4022 / −0.2278 / 0.0190 / −3.8207 / −89.1155 | 205.5993 / 0.0827 / 0.0199 / −1.2206 / −59.5749 |
| OLMAR | −38.8878 / −0.0365 / 0.0200 / −2.1119 / −61.0217 | −44.0283 / 0.0826 / 0.0501 / −0.4843 / −81.6301 |

- **Theory (source-reported)**: Theorem 3.1 gives `R^c_track(T,K) ≤ [Σ_t (Σ_j q_j(t)ℓ̃_j(t) − ℓ̃_{j_t}(t))] + Σ_t c(t)‖q(t) − q(t−1)‖₁` and proves the coefficient 1 sharp via a 2-asset, 2-expert, `T = 2` construction; Lemma 3.3 bounds one-step weight variation by `η(max ℓ̃ − min ℓ̃) + 2α(1 − 1/n)`; Corollary 3.4 combines them; Proposition 3.5 optimises `α* = K/(T−1)` and `η*`; Corollary 3.7 gives asymptotic no-regret for `K(T) = o(T)`.
- **Synthetic (§4.1, Figures 1–2)**: with the regime shift inserted at day 1,000, "Fixed Share reallocates its weights to the newly dominant expert faster than Hedge" — **qualitative only; no regret, return, or drawdown numbers are printed for the synthetic study** → `data gap`.
- **Online-portfolio-selection comparison (App. B.3, Figure 5; repeated as Figures 8 and 12 for the two empirical spans)**: the source states its two-level framework attains a lower `R_stock` (tracking regret vs the best stock sequence with ≤ K switches) than UP/EG/PAMR/CWMR/OLMAR, with "negative regret indicat[ing] that our framework incurs lower cumulative loss than the best stock sequence" — **again figure-only, no printed values** → `data gap`.
- **Narrative claims (§4.2)**: on DJIA "Hedge and Fixed Share have smaller drawdown magnitudes than the listed baselines, while UP and EG achieve higher cumulative returns"; on S&P 500 "Hedge and Fixed Share achieve higher cumulative returns than the listed baselines, but have larger drawdown magnitudes than UP and EG" — both consistent with the printed tables (checked cell by cell).
- **Account-value figures (Figures 9 and 13)**: the source asserts the two-level framework "progressively accumulates a higher account value, even when subjected to these transaction cost penalties" and that Table 2 shows "the lowest Maximum Drawdown" — no plotted values are printed → `data gap`.

**Our own arithmetic on the printed cells (labelled `our count`, not source-reported):**
- Across Tables 2–7 there are **30 metric rows**: 27 have a positive sample mean, 25 have a positive cumulative return, 28 print a negative Sharpe, and **25 rows are simultaneously positive-mean and negative-Sharpe**.
- **Best single fixed window beats both aggregators**: DJIA 126-day **157.83%** vs Hedge 41.70% (3.79×) and Fixed Share 38.11%; S&P 500 126-day **1881.75%** vs Hedge 578.70% (3.25×) and Fixed Share 471.05%; the S&P 41-day expert (1173.93%) also beats both.
- **Return rank of the aggregators among the 15 rows per market**: Hedge **8th of 15** and Fixed Share **9th of 15** on DJIA; Hedge **4th of 15** and Fixed Share **5th of 15** on S&P 500.
- **Drawdown rank**: Hedge has the **smallest-magnitude MDD of all 15 DJIA rows (−12.6326%)** but ranks only **3rd of 15** on S&P 500 (−56.0818% behind EG −38.2862% and UP −38.3269%).
- Conventional Sharpe reconstruction from the printed inputs (`mean(%)/100 ÷ SD × √252`) gives **+1.042 (DJIA 5-day)**, **+0.377 (DJIA 10-day)**, **+0.736 (Hedge DJIA)** against printed −1.0535, −1.8158, −2.4214 — the printed column is not reconstructable (see frontmatter contradiction).

### Independently reproduced

`Not independently reproduced.` This run performed only: (a) direct reading of the pinned `arXiv:2609.29887v1` HTML landing page and full text, (b) arithmetic checks on the printed table cells (the `our count` items above), (c) a word-boundary scan of the pinned text for cost/execution terms, and (d) version/DOI/licence verification. **No portfolio was reconstructed, no MV program was solved, no return series was downloaded, and no figure was regenerated.**

### Negative evidence

1. **Aggregation does not maximise return in either sample** (our count, printed tables): the best fixed window beats Hedge by 3.79× (DJIA) and 3.25× (S&P 500); Hedge ranks 8th/15 and 4th/15 by cumulative return. The source's own §4.2 text concedes UP and EG beat Hedge/FS on DJIA return. The defensible claim is therefore *drawdown/rank*, not *return*.
2. **The drawdown claim is sample-specific** (our count): Hedge's MDD advantage holds on DJIA (1st of 15) but fails on S&P 500, where UP and EG are ~18 pp shallower (−38.3% vs −56.1%) — the same §4.2 sentence admits this.
3. **Baselines are not cost-tuned, and three of them collapse** — the source states the comparators "are initialize[d] … to the theoretically optimal values prescribed in their respective foundational papers", that "these standard configurations were originally derived under frictionless assumptions", and that they are run this way "not to claim they are fully optimized for our specific setting". Result: PAMR −88.24% and CWMR −88.40% on DJIA, PAMR −52.08% and OLMAR −44.03% on S&P 500 at 10 bps. A comparison against collapsed frictionless baselines is weak evidence for the framework.
4. **The Sharpe column is unusable** (frontmatter contradiction): 25 of 30 rows print a positive sample mean with a negative annualised Sharpe, no convention is stated, and our reconstruction of two cells is off in both sign and magnitude.
5. **Zero statistical inference anywhere**: word-boundary scan of the pinned text gives `significan*` 0, `t-stat` 0, `p-value` 0, `confidence interval` 0, `bootstrap` 0, `win rate` 0, `seed` 0, `grid` 0, `in-sample` 0, `test set` 0. There is **no hypothesis test, no confidence interval, no multiplicity control across 30 metric rows × 2 markets × 7 algorithms**, and no repeated-run dispersion for any empirical number.
6. **Ex-post universe construction**: DJIA window chosen to contain no constituent changes; S&P 500 keeps only the 481 names present across the entire span ("we remove all the changed stocks"). Membership is not point-in-time, so names that left the index (and their underperformance/delistings) are absent by design — a survivorship-shaped selection the source does not test.
7. **The synthetic result is by construction**: the DGP explicitly switches the true window from 63 to 5 at exactly day 1,000, i.e. the environment is built for Fixed Share to win; §4.1 reports no numbers at all for it.
8. **The authors disclaim predictive power**: App. B.5 — the empirical studies are "intended solely to demonstrate the practical application of our framework over a restricted timeframe … rather than to assert any predictive capability regarding the future performance of specific financial instruments." Read as a *method* demonstration, not an alpha claim.
9. **Cross-record evidence from a different source in this repo**: `forecast-vol-targeting-student-t-hmm-hrp-regime-momentum-tilt-2026-09-13.md` (source `Olivesz/kronos-quant` @ `2e112e4e5f01a39d89121921df86ef2970e237a4`) reports that "Online Hedge and fixed-share learning algorithms failed to beat hand-crafted regime weights (all tied at Sharpe ≈ 0.99), because sleeves were heavily co-dependent through the shared HRP covariance backbone" — i.e. **the same aggregator family failed to add value over hand-set weights in a different setting** (attribution kept with its own source).
10. **Single cost point, no ladder**: only `c = 0.001` is ever run; with no spread, slippage or impact model, the 10 bps assumption carries the whole cost story.
11. **Extreme realised drawdowns**: MDD as deep as −78.59% (S&P 500, 50-day expert) and −89.12% (DJIA, CWMR) on long-only books with no stated concentration or position caps; maximum single-name weights are never reported, so capacity and concentration risk are untested.
12. **Not reproducible**: no code, no data vendor, no numeric `η`/`α`/`w_0`/`b−a`/`T` → an independent team cannot regenerate Tables 1–7 from the paper.

## Falsification plan

Every threshold below is `research-defined` / `research-proposed` — none appears in the source. Action on failure for all tests: **the hypothesis is rejected for that setting and the record stays `research-only` / not adopted**; a failure of F1 or F2 additionally downgrades `confidence` to `low`.

1. **F1 — Point-in-time universe repair** (`research-proposed`): rebuild both universes from dated index membership including entries, exits and delistings, with adjusted closes from a named vendor; execute `research-proposed` at next-bar open with data through the prior close. **Fails if** either headline claim breaks in ≥ 2 of 3 equal sub-periods: (a) DJIA Hedge MDD is no longer the shallowest in the comparison set, or (b) S&P 500 Hedge cumulative return no longer exceeds UP/EG.
2. **F2 — Cost ladder** (`research-defined`): rerun at 0/5/10/20/30 bp per unit of `‖Δw‖₁` plus a paid-spread scenario at 20% ADV participation. **Fails if** at 20 bp Hedge's net cumulative return falls below UP or its MDD advantage over UP/EG disappears.
3. **F3 — Selection-aware best-window horse race** (`research-defined`): choose the single best window on a training sub-span only, then freeze it for the remainder. **Fails if** Hedge does not beat that training-selected window on either net return or net MDD out of sample.
4. **F4 — Hyperparameter integrity** (`research-defined`): publish `η`, `α`, `ε`, `b − a`, `T`, `w_0` and the solver settings, then perturb `η` and `α` by ±2×. **Fails if** any printed cumulative return or MDD in Tables 1–7 moves by more than 20% relative, or if the required values cannot be recovered at all (current state → immediate fail).
5. **F5 — Sharpe-column repair** (`research-defined`): reproduce every printed "Annualized Sharpe Ratio" from the printed inputs to within ±0.05 under a documented convention. **Fails if** the convention cannot be stated or two or more cells miss by >0.05 (our reconstruction currently misses by >0.6 on two cells → immediate fail as printed).
6. **F6 — Statistical significance** (`research-defined`): moving-block bootstrap (5-day blocks, 10,000 draws) on the daily Hedge-minus-baseline and Hedge-minus-best-window return differentials. **Fails if** the 95% CI includes 0 or the paired t-statistic is < 2.0 for the return differential, or if Hedge's MDD differential is not significant at the 5% level.
7. **F7 — Multiplicity audit** (`research-defined`): apply Benjamini–Hochberg at `q = 0.10` over the full family of printed comparisons (2 markets × 7 algorithms × 5 metrics). **Fails if** fewer than half of the claimed advantages survive.
8. **F8 — Placebo on the window labels** (`research-defined`): circularly shift the sequence of expert-weight updates by 1,000 random offsets. **Fails if** the observed cost-sensitive tracking regret is not above the 95th percentile of the placebo distribution.
9. **F9 — Cost-tuned baseline re-run** (`research-defined`): re-tune UP/EG/PAMR/CWMR/OLMAR for the same 10 bps with an equal tuning budget. **Fails if** any re-tuned baseline beats Hedge on both net return and net MDD — that would attribute the source's win to baseline mistuning.
10. **F10 — Ablation of the two levels** (`research-proposed`): compare (i) single fixed window, (ii) Hedge (`α = 0`), (iii) Fixed Share, (iv) equal-weight aggregation, (v) aggregation with `c = 0`. **Fails if** Fixed Share does not beat equal-weight aggregation on net MDD — i.e. if the online learner, rather than plain diversification across windows, is not doing the work.
11. **F11 — Frozen forward window** (`research-defined`): hold `N`, `η`, `α`, `c` frozen for a post-capture period not in the paper. **Fails if** Hedge's forward net return is below the median of the eight individual windows in the same window.

## Crypto portability

`unproven`

The formulation itself is market-agnostic (a long-only simplex over generic return vectors including a risk-free asset), so nothing in the *mathematics* forbids crypto — but the source demonstrates **only US equities**, discusses no crypto evidence at all, and its cost model omits every crypto-specific cost. Porting would require re-specification of:

- **Market type**: the source is single-name equities plus a T-bill ETF; crypto would need spot vs perpetual choice, and the long-only/no-borrow structure means no short leg is available even if the hypothesis wanted one.
- **Funding / liquidation / borrow**: `not in source` — perp funding, mark-price liquidation and isolated-margin mechanics are entirely absent from a model that only knows a flat proportional turnover rate.
- **24/7 session structure**: the source's `t` is a trading day with adjusted closes and index-membership calendars; crypto has no session boundaries, so "day" must be redefined (timezone and candle-boundary convention `research-proposed`), and windows of 5–126 "days" change meaning.
- **Venue fragmentation / candle boundaries**: single-price-series assumption; index membership, survivorship handling and BIL have **no crypto counterpart**, so the cash sleeve must be redefined (stablecoin yield vs simple cash) — `research-proposed`.
- **Costs**: with no spread, depth, impact or funding model in the source, a crypto port inherits the same `data gap` on top of crypto's fatter spreads and fragmented books.

No crypto result — positive or negative — exists in the source; portability is neither demonstrated nor refuted.

## Limitations

- `underspecified`: numeric `η`, `α`, `ε`, `b − a`, `T`, `w_0`, solver and tolerance for every printed experiment; unit of "Sample Standard Deviation"; per-side vs round-trip reading of the 10 bps; order type, fill model, signal-to-order delay; dividend/corporate-action treatment beyond "adjusted closing price"; timezone and calendar; data vendor; position concentration and capacity.
- `data gap`: every value that exists only inside Figures 1–13 (tracking-regret curves, `R_stock` comparisons, account-value curves, weight-evolution panels) — the source prints no numeric values for them, so the paper's central regret claim is **not numerically checkable from the text**.
- `data gap`: all spread/slippage/impact/latency/fill/borrow/shorting/leverage/dividend/liquidation/funding/capacity fields (word-boundary scan = 0 each).
- `not independently reproduced`: every number in this record is source-reported.
- Ex-post universe construction in both empirical studies; no point-in-time membership; no delisting/survivorship treatment.
- Single cost point (10 bps), no cost sensitivity, no inference of any kind (no tests, CIs, seeds, or multiplicity control across 30 metric rows).
- Baselines deliberately left at frictionless foundational settings, with three of five collapsing under costs.
- The synthetic experiment encodes its own regime switch and reports no numbers.
- The source explicitly disclaims any predictive-capability claim for its empirical results (App. B.5).
- Preprint only: no journal-ref, no Comments field, no peer-review statement, no code, no data-availability statement; generative-AI assistance acknowledged by the authors for language editing and derivation feedback (§5).
- No trading record, no live or paper result of any kind is claimed by the source or by us.

## Implementation status

`implementation_status: not-implemented`. Nothing from this record has been implemented in our research stack: no portfolio builder, no MV solver run, no Hedge/Fixed Share aggregator, no backtest, no Qlib run, no Paper/Testnet/Live activity. This capture is a normalised research reading plus arithmetic checks on printed cells only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

Presence of this record in the staging repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, Paper, Testnet, or Live. The mechanism is an allocation/turnover-control hypothesis, not a demonstrated predictive alpha, and the source itself says so.

## Related Wiki records

- `[[quant/tda-persistent-homology-finbert-sentiment-portfolio-optimization-2026-09-02]]` — closest adjacent Wiki page found this run: dynamic rebalanced mean–variance portfolio construction with transaction-cost awareness (different signal source, no online expert aggregation).
- Pre-write `kb_search` for `online portfolio selection window size expert aggregation Fixed Share Hedge`, `regret bound expert advice non-stationary regime adaptive model selection trading`, and `online portfolio selection OLMAR PAMR universal portfolio benchmark` each returned **0 pages**; `mean-variance portfolio transaction cost turnover rebalance rolling estimation window` returned 8 adjacent pages of which only the one linked above was used. **No dedicated window-selection / expert-aggregation page exists in Wiki Brain**, and none was written (Scouts must not write to Wiki Brain).

Adjacent records already in this repository (dedup and contrast, not links to be created):

- `wasserstein-robust-portfolio-hyperplane-dual-lp-2026-09-02.md` (`arXiv:2608.07032`, same author Chung-Han Hsieh) — static Wasserstein-robust mean–variance certification; **distinct source identity and mechanism**: no window experts, no Hedge/Fixed Share, no tracking regret, no cost-sensitive turnover term in the objective.
- `regret-driven-portfolio-ftl-llm-hedging-sentiment-gated-2026-09-05.md` (`arXiv:2601.17021`) — shares the "regret" vocabulary but uses greedy follow-the-leader over LLM-clustered sectors with sentiment gating; no window-expert aggregation and no cost-sensitive regret bound.
- `smart-predict-then-optimize-spo-plus-robust-portfolio-2026-09-05.md` (`arXiv:2601.04062`) — shares "turnover costs", but learns one predictive model decision-focused; the present source aggregates fixed hand-specified windows with a proven regret bound.
- `active-equal-weight-tilt-sdd-diversity-dispersion-control-2026-09-24.md` (`arXiv:2609.27113`) — overlapping S&P 500 universe but a regime-state tilt between market and equal weight, not window aggregation.
- `forecast-vol-targeting-student-t-hmm-hrp-regime-momentum-tilt-2026-09-13.md` — supplies the cross-record negative evidence on Hedge/fixed-share aggregation quoted above (its own source, `Olivesz/kronos-quant` @ `2e112e4…`).

## Sources

1. Liu, Y.-C., & Hsieh, C.-H. (2026). *Cost-Sensitive Online Window Size Selection for Portfolio Management*. arXiv:2609.29887v1 [math.OC] (cross-list cs.LG, q-fin.PM), submitted 24 September 2026. https://arxiv.org/abs/2609.29887 — pinned full text https://arxiv.org/html/2609.29887v1 (512,313 bytes; SHA-256 `5db73795770314df2e3224ef855a9166c173f8a9e516d736e67786a6e4ced3a2`), read end to end 2026-09-25. DataCite DOI https://doi.org/10.48550/arXiv.2609.29887 (302 → abs, checked 2026-09-25).
2. Version/metadata checks (all 2026-09-25): `https://arxiv.org/abs/2609.29887v2` → HTTP 404; `https://arxiv.org/html/2609.29887v2` → HTTP 404; landing page shows no Comments field, no journal-ref, no peer-review statement; licence = arXiv perpetual non-exclusive distribution licence.
3. Methodological antecedents cited *by the source* (not opened by this run, recorded for provenance only): Herbster & Warmuth (1998) Fixed Share; Littlestone & Warmuth (1994) Hedge; Helmbold, Schapire, Singer & Warmuth (1998) EG; Cover (1991) universal portfolio; Li & Hoi (2014) OLMAR; Li et al. (2012, 2013) PAMR/CWMR; Markowitz (1952); Diamond & Boyd (2016) CVXPY.
4. Cross-record negative evidence: `forecast-vol-targeting-student-t-hmm-hrp-regime-momentum-tilt-2026-09-13.md` in this repository, sourced to `Olivesz/kronos-quant` commit `2e112e4e5f01a39d89121921df86ef2970e237a4`.
