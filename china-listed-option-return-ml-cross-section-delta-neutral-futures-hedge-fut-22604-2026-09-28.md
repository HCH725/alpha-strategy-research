---
schema: strategy-research-record-v1
title: "Machine-learning cross-section of Chinese listed option returns with futures-hedged delta-neutral portfolios (Huang, Wang & Xiao, Journal of Futures Markets 45(9):1232-1252; full text paywalled so every performance number is a data gap, companion code pinned at 42fe83ca)"
created: 2026-09-28
updated: 2026-09-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - options
  - listed-options
  - index-options
  - etf-options
  - china
  - delta-hedged
  - delta-neutral
  - machine-learning
  - cross-section
  - factor-screening
  - ipca-benchmark
  - published-journal
status: research-only
confidence: low
source_as_of: "2025-06-04"
sources:
  - "https://doi.org/10.1002/fut.22604 — canonical DOI (Journal of Futures Markets, Volume 45, Issue 9, September 2025, Pages 1232-1252; article page prints 'First published: 04 June 2025'); abstract landing read 2026-09-28 at https://onlinelibrary.wiley.com/doi/abs/10.1002/fut.22604"
  - "https://onlinelibrary.wiley.com/doi/10.1002/fut.22604 — full-text URL read 2026-09-28: renders only ABSTRACT / Conflicts of Interest / Data Availability Statement / References headings, no section text; https://onlinelibrary.wiley.com/doi/pdf/10.1002/fut.22604 returned HTTP 403 on 2026-09-28 -> paper Methods/Results/Tables are NOT readable in this run"
  - "https://github.com/yuxiangh383/option-return-prediction — companion code, public, MIT; main/HEAD = 42fe83ca32675834d90f1f73819bd580903819a2 (git ls-remote 2026-09-28), single commit 'first commit' 2026-09-02T16:21:18+08:00; GitHub API created_at 2026-09-02T08:07:44Z, pushed_at 2026-09-02T08:22:56Z, updated_at 2026-09-12T06:48:35Z, 29 stars, 0 forks"
  - "https://ideas.repec.org/a/wly/jfutmk/v45y2025i9p1232-1252.html — secondary bibliographic record (author list + abstract) read 2026-09-28; used only to cross-check citation metadata, never for results"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Third-author name printed two ways for the same DOI: 'Zhengyan Xiao' on the Wiley article page, on RePEc/IDEAS and in the companion repo CITATION.cff, versus 'Zhengyang Xiao' in the Semantic Scholar Graph API record for DOI 10.1002/fut.22604 (both read 2026-09-28). Unreconciled; the Wiley spelling is used below because it is the publisher of record."
  - "Cost-claim vs companion-code gap: the abstract states that 'The out-of-sample performance remains economically significant after accounting for transaction costs', but the committed backtest notebook selects label 'r' or 'r_s' (financing-adjusted delta-hedged returns with no spread charge) and models/model.py construct_portfolio() contains no commission, slippage, spread or impact term at all. Spread-charged variants (skip = 0.25 / 0.5 / 1.0 x bid_ask_spread) are built one stage earlier in 1-DataPreprocess.ipynb as separate columns, and nothing in the repo states which column the published net-of-cost numbers come from -> unreconciled, paper Methods not readable."
  - "Three different sample-window expressions inside the pinned companion repo: configs/default.yaml start_date '2015-04-01'; models/factortest.py line 20 and models/IndexFactors.py line 18 start_date '2015-01-01'; research notebooks carry a commented pd.date_range(start='2015-02-01', end='2024-07-31', freq='MS'). The paper's own sample period is not readable (paywall) -> unreconciled, treated as data gap."
  - "Data-availability tension: the Wiley Data Availability Statement says 'The data that support the finding of this paper are available from the authors upon reasonable request', while the companion README says raw option quotes are proprietary and are NOT included and expects a private ClickHouse extract (option / underlying tables) via environment variables. The two statements describe different replication paths and are not reconciled."
  - "Two different quantities are both called R-squared in the companion code: models/model.py calc_R2(y_pred, y_true) (line 34) returns 1 - SSE/sum(y_true^2), yet it is invoked as calc_R2(Y, y_pred) in construct_portfolio (line 277) and as calc_R2(y_test, yhat) in fit_evaluate (line 69), so the denominator in both call sites is the sum of squared FORECASTS, whereas the neighbouring helper benchmark_r2 (line 27) carries the comment '论文中以超额收益为0，计算出的R方' - the R-squared computed in the paper with excess return benchmarked at zero, which requires the sum of squared realized returns. sklearn's R2(Y, y_pred) is reported alongside it in the same row -> two differently defined R-squared columns, unreconciled."
  - "Two incompatible IPCA specifications sit in the same call path: get_randomcv_model() builds InstrumentedPCA(n_factors=20, intercept=True) at models/model.py line 497, but back_test_daily() then re-creates InstrumentedPCA(n_factors=3, intercept=True) at line 591 whenever name == 'IPCA', discarding the first. The 'outperform the IPCA benchmark' claim therefore rests on an undefined choice between 3 and 20 factors -> unreconciled."
---

# Machine-learning cross-section of Chinese listed option returns (futures-hedged delta-neutral portfolios)

> Epistemic boundary: everything under **Source-reported** is the primary source's claim, marked `source-reported`, with the exact artifact it came from (Wiley abstract vs. companion-code path). Everything under **Research interpretation**, **Research-proposed** and **Research-defined** is Scout-generated. This record is `research-only / not-implemented / not-approved / approval_scope: research-only`; the results are **not independently reproduced**, and — because the article body is paywalled — **every performance number that would normally anchor this record is a `data gap`**.

## Provenance

- **Title (exactly as printed):** *Option Return Predictability via Machine Learning: New Evidence From China*.
- **Complete author list (exactly as printed on the Wiley article page):** Yuxiang Huang; Zhuo Wang; Zhengyan Xiao. The same three names and order appear in RePEc/IDEAS and in the companion repo `CITATION.cff` (`family-names: Huang/Wang/Xiao`, `given-names: Yuxiang/Zhuo/Zhengyan`). Semantic Scholar returns the third author as "Zhengyang Xiao" for the same DOI → frontmatter contradiction 1.
- **Venue / version:** *Journal of Futures Markets*, Volume 45, Issue 9, September 2025, Pages 1232–1252; article type badge "RESEARCH ARTICLE"; `First published: 04 June 2025`; DOI `10.1002/fut.22604`; publisher John Wiley & Sons. No ORCID, no funder, no preprint/working-paper version and no arXiv/SSRN mirror were found in this run → **publication status: peer-reviewed journal article; preprint status `not stated in source`**.
- **Full-text access status (step 5b, read at Methods level):** the abstract landing page (`/doi/abs/10.1002/fut.22604`) and the full-text URL (`/doi/10.1002/fut.22604`) both render only the ABSTRACT, Conflicts of Interest, Data Availability Statement, References and tab headings — **no section text, no tables, no figures**; `/doi/pdf/10.1002/fut.22604` returned **HTTP 403** on 2026-09-28. Semantic Scholar `openAccessPdf.url` is empty; OpenAlex reports `is_oa: false` with a single location (the DOI). → **Paper Methods / Experimental Setup / Results tables were NOT read this run.** Sample period, universe counts, model grid, portfolio rule, and every Sharpe/return/drawdown/t-statistic in the article are **`data gap`**, never inferred.
- **Pinned primary source actually read:** companion repository `https://github.com/yuxiangh383/option-return-prediction`, `main` = **`42fe83ca32675834d90f1f73819bd580903819a2`** (`git ls-remote` 2026-09-28; GitHub API `pushed_at 2026-09-02T08:22:56Z`; one commit, message `first commit`, author `yuxiangh383`, 2026-09-02 16:21:18 +0800). 51 tracked files, 6,102 lines of Python, 14,400 lines of notebook JSON. Read this run: `README.md` (4,010 B), `CITATION.cff` (833 B), `LICENSE` (MIT, "Copyright (c) 2026 JFM-OptionReturn-Factor contributors"), `configs/default.yaml` (135 B), `docs/factors.md` (2,143 B), `docs/data-schema.md` (1,487 B), `data/README.md`, `notebooks/pipeline/README.md`, `.github/workflows/ci.yml`, `tests/test_factors.py`, `tests/test_repo_hygiene.py`, and the executed cell sources of `notebooks/pipeline/1-DataPreprocess.ipynb` (31,801 B) and `notebooks/pipeline/7-BackTest-daily-regression.ipynb` (14,468 B), plus `models/model.py` (28,855 B), `models/summary.py`, `models/factortest.py`, `models/IndexFactors.py`, `notebooks/pipeline/5-ContractLevelFactor.ipynb` and `notebooks/pipeline/6-FilterSummarySelect.ipynb`.
- **Authorship linkage between paper and repo:** asserted by the repo itself (`README.md`: "Companion code for Huang, Wang, and Xiao (2025), *Option return predictability via machine learning: new evidence from China*, *Journal of Futures Markets*"; `CITATION.cff` `preferred-citation` carries the exact title, journal, volume 45, issue 9, pages 1232–1252 and DOI). Not independently verified beyond the DOI/CITATION metadata match → `source-reported`.
- **CI / tests (source-reported, read via GitHub API 2026-09-28):** workflow `CI`, run at `42fe83ca3267`, `status: completed`, `conclusion: success`, created `2026-09-02T08:23:02Z`; workflow = Python 3.11, `pip install -e ".[dev]"`, then `pytest`. The suite is `tests/test_factors.py` (89 lines, 8 tests: put-call parity, ATM delta band 0.48–0.56, vega/gamma positivity, `ivslope` and risk-neutral moments on a synthetic panel, Newey–West one-sample t, two split/lookahead guards) plus `tests/test_repo_hygiene.py` (58 lines, 2 tests asserting three private-warehouse tokens are absent from the tree — token values intentionally not reproduced here). **They do not run any empirical backtest.**
- **Independent check performed by us:** `python3 -m compileall -q models option_factors tests examples scripts` on the pinned clone → exit 0 (all committed Python compiles). We did **not** install the dependency stack and did **not** execute the test suite or any notebook (dependency installation is not permitted in this run's environment) → code-level verification stops at syntax.
- **Dedup (step 5, hidden-inclusive `rg -uuu` over the whole checkout including `.git`, `.mimo-worktrees`, `.agents`, `.hermes`, `coverage_manifest.csv`):** identity terms `fut.22604`, `yuxiangh383`, `option-return-prediction`, `JFM-OptionReturn`, `Zhengyan Xiao`, `Option Return Predictability via Machine Learning`, `option return predictability` → **zero hits anywhere**. `delta-neutral portfolio` matched 3 records (`crypto-perpetual-funding-rate-carry-spot-perp-2026-08-31.md`, `crypto-two-tiered-cex-dominant-funding-discovery-structural-arbitrage-2026-09-12.md` and their `.mimo-worktrees` copies) — those are spot-plus-perpetual **funding-carry** books, a different source identity and a different mechanism (carry/funding vs. cross-sectional delta-hedged option-return prediction), so no dedup conflict. Positive control `novy-marx` → 22 files in the same session (search is alive; 23 including this draft, which names the control). `git log --oneline -20` used only as a convenience glance. **Re-run immediately before commit, after `git pull origin main` (Already up to date, head still `ef90830`):** `fut.22604`, `yuxiangh383`, `option-return-prediction`, `JFM-OptionReturn`, `Zhengyan Xiao`, `Zhengyang Xiao` and the exact article title each match **exactly one file — this draft**; `novy-marx` control = 22 other files. Wiki Brain `kb_search "option return predictability machine learning China delta-neutral"` → **0 pages** (read-only; no Wiki write this run).
- **source vs research:** no Scout-computed performance number exists in this record — there are no performance numbers to compute. The only `research-computed` items are code-reading arithmetic (the 5-window evaluation slice, the decile/weight algebra) and are labelled as such.

## Economic mechanism

### Source-reported

`source-reported` — all four claims are quoted or paraphrased from the Wiley abstract (the only paper text readable in this run; read 2026-09-28):

1. The paper "extend[s] the literature on empirical asset pricing to the Chinese options market by building and analyzing a comprehensive set of return prediction factors using various machine learning methods."
2. It "investigate[s] daily hedging strategies to construct delta-neutral portfolios, and identif[ies] the most important characteristics for return prediction."
3. **Friction channel:** "Short-selling restrictions in China's financial market diminish the effectiveness of spot hedging, whereas delta-neutral portfolios based on futures hedging deliver substantial improvements in both annual returns and Sharpe ratios."
4. **Benchmark / generalization channel:** "Machine learning models not only outperform the IPCA benchmark, but also demonstrate strong generalization ability when applied to newly issued option contracts. The out-of-sample performance remains economically significant after accounting for transaction costs."

`source-reported` (companion code, pinned SHA above): `docs/factors.md` documents the predictor families the "comprehensive set" is built from — implied-volatility slope (`ivslope`, "ATM IV of longest maturity minus 30-day ATM IV", cited to Xing, Zhang, Zhao RFS 2010), risk-neutral skew/kurtosis (`risk_neutral_skew`, `risk_neutral_kurt`, Bakshi–Kapadia–Madan RFS 2003), implied-variance asymmetry, option-implied tail loss (`tlm30`, "Bali, Hu, Murray and related tail papers"), put-call ratio, stock-vs-option volume (`so`, `lso`, `dso`, Roll–Schwartz–Subrahmanyam), proportional bid-ask spread (`pba`, Goyenko–Holden–Trzcinka), absolute/percentage option illiquidity, `atm_iv`/`ivvol`/`dciv`/`dpiv`, implied-vs-realized variance spread (`ivrv`, `ivrv_ratio`, Carr–Wu), `amihud`/`roll`/`pzeros`, bucket-level `weighted_iv`/`oistock`/`turnover` (Horenstein–Vasquez–Xiao), and Black–Scholes Greeks (`delta`, `vega`, `gamma`, `theta`, `rho`, `vanna`, `vomma`).

### Research interpretation

`research-proposed` — the falsifiable mechanism as Scout normalizes it:

- **Mispricing-with-friction-biased-hedge channel:** option prices in a short-sale-constrained, retail-heavy listed-options market drift relative to their delta-hedged fair value, and observable option/underlying characteristics forecast the *residual* (delta-hedged) option return cross-sectionally rather than the raw option return. The economic thesis therefore has two separable parts: (a) a cross-sectional predictability claim, and (b) a hedge-instrument claim — the same signal is more tradeable when the hedge leg is a **stock-index futures** contract than when it is the underlying stock, because the spot leg carries the short-sale constraint.
- **Component roles (hybrid structure):** Regime/universe screen = the six filters in `notebooks/pipeline/6-FilterSummarySelect.ipynb` (see `Signal`); Primary signal = ML-predicted one-day-ahead delta-hedged option return; Confirmation/selection = decile split on the model's prediction; Position sizing = dollar-open-interest weighting inside each leg; Risk/exit = daily re-formation (no stop, no holding-period rule) plus a financing charge and a margin-based capital base in the return definition.
- **Do not assume every component contributes alpha:** the delta-hedge choice, the open-interest weighting, and each of the ~20 factor families are separate ablation targets (F5/F6 below). The source does not decompose them in any text we can read → `data gap`.

## Signal

**A. Source-reported from the companion code** (pinned `42fe83ca`; `source-reported (companion code)`, with file/cell provenance). Equivalence between this code and the published article's exact specification is **`unproven`** — the article body is paywalled.

- **Formation timestamp / target variable** (`notebooks/pipeline/1-DataPreprocess.ipynb`, cells 32 and 34):
  - Futures-hedged label: `PnL = next_close − close − delta × (next_synthetic_futures_price − synthetic_futures_price) − gap_days/365 × rf/100 × (close − delta × synthetic_futures_price)`; `r = PnL / |close − delta × synthetic_futures_price|`.
  - Spot-hedged label: `PnL_s = next_close − close − delta_s × (next_stock_close − stock_close) − gap_days/365 × rf/100 × (close − delta × stock_close)`; `r_s = PnL_s / |close − delta × stock_close|`.
  - Both labels are **one panel step (one trading day) forward** from a formation close; the denominator is the hedge-adjusted capital outlay (option premium minus delta × hedge notional), so the label is a return on hedged capital, not a return on option premium.
- **Label actually consumed by the backtest** (`notebooks/pipeline/7-BackTest-daily-regression.ipynb`; `models/model.py` `back_test_daily`, line 583): `label = 'r' if 'r' in subsample.columns else 'r_s'` → the futures-hedged label is preferred when present. The notebook is run with `iv_name = 'spot'` and `data/Train/{iv_name}_data.pkl`, so which label column reaches a given run depends on a data artifact that is **not shipped** → `data gap`.
- **Universe screens** (`notebooks/pipeline/6-FilterSummarySelect.ipynb` section headers): `# 1. miss iv`, `# 2. zero trading volume`, `# 3. nonarbitrage`, `# 4. due in 2 weeks`, `# 5. openinterest`, `# 6. Convexity`, plus markdown "数据首先需要筛选起止日期" (start/end dates must first be filtered) and "剔除存在较多缺失数据的月份" (drop months with many missing values). Exact thresholds for screens 1/3/5/6 are `underspecified` (cells are commented or threshold not printed) → `data gap`.
- **Instrument identifiers** (`docs/data-schema.md`): contract-day panel, `underlying_code` examples `SH510300` (CSI 300 ETF) and `SH000300` (CSI 300 index); `option_type ∈ {认购 (call), 认沽 (put)}`; README narrows the market to "CSI index options and SSE/SZSE ETF options". `SH510050` and `SH588080` appear in commented plotting cells of notebook 6.
- **Rolling walk-forward protocol** (`models/model.py` lines 567–619): for each step, `subsample` = panel rows with `datetime ∈ (date_list[idx], date_list[idx+length]]`, `testsample` = rows with `datetime ∈ (date_list[idx+length], date_list[idx+length+1]]`; `length = 20` panel dates of training, one panel date of test, rolled forward. Notebook 7 passes `length = 20`, `test_num = 6`, `begin_idx = 0` (IPCA/NN) and `begin_idx = 2000` (lasso onward).
- **`research-computed` evaluation slice:** the loop is `for idx, date in enumerate(date_list[length:-1])` over a list of `length + test_num = 26` dates → **5 rolling out-of-sample evaluations per cell as committed**, not a full-sample sweep. The sweep loop that would produce a full-period result is not present in the committed notebook → `data gap` on how the article's full-sample numbers were produced.
- **Models compared** (`models/model.py` `get_randomcv_model`, lines 425–501, and notebook 7 cells 4–33): `IPCA` (vendored `models/ipca.py`; see the 3-vs-20 factor conflict in frontmatter contradiction 6), `NN`, `lasso`, `rf` (RandomForest, `criterion='absolute_error'`), `GBR`, `xgboost`. **`NN` cannot run as committed** — its branch is an empty `pass` (line 492) and `get_randomcv_model` then executes `return model, ravel` with `model` never assigned (see Negative evidence 16). Hyperparameter search = `RandomizedSearchCV` with **`fold_num = 5`** and **`n_iter = 10`** (`models/model.py` lines 23–24; sklearn default `n_iter` where not passed); grids: `lasso/ridge alpha ~ loguniform(1e-3, 1)`; RF/GBR `n_estimators ∈ [32,64)`, `max_depth ∈ [5,10)`, `min_samples_split ∈ [3,10)`; GBR `learning_rate ∈ [0.01,0.1)`; XGBoost additionally `min_child_weight ∈ [2,5)`, `max_depth ∈ [3,10)`, `learning_rate ∈ [0.01,0.1)`, `subsample=0.8`, `colsample_bytree=0.8`, `objective='reg:squarederror'`. Random seed `1234`.
- **Label winsorization:** `subsample[label] = clip(q(0.01), q(0.99))` inside `back_test_daily` when `clip=0.99` (notebook 7 passes `clip=0.99`).
- **Portfolio rule** (`models/model.py` `construct_portfolio`, lines 263–342, called with `strategy='all'`, `weighted=True`, `normalized=True`):
  - Features `X = sample.iloc[:, 1:-1]` are re-standardized on the *evaluation sample itself* (`X = (X − X.mean())/X.std()`, zero-variance columns set to 1) before prediction.
  - **Long leg** = contracts with `y_pred ≥ quantile(y_pred, 0.9)`; **short leg** = contracts with `y_pred ≤ quantile(y_pred, 0.1)` (top/bottom decile of the cross-sectional prediction).
  - **Weights** = `exp('doi')` renormalized within each leg, where `doi = log(openinterest × close + eps)` (`notebooks/pipeline/5-ContractLevelFactor.ipynb`, raw .ipynb JSON lines 242 and 251) → `research-computed`: weights are proportional to **dollar open interest** (`exp(log x) = x`), i.e. each leg is a liquidity-weighted basket summing to 1.
  - **Combined book** = `0.5 × (leg_long + leg_short)` → gross exposure 1.0, dollar-neutral across the two legs, each leg separately normalized.
  - Reported per step: `r_long`, `r_short`, `r_longshort`, sklearn `R2(Y, y_pred)`, the `calc_R2` variant (see frontmatter contradiction 5), and one-sided (`alternative='greater'`) Pearson / Spearman / Kendall statistics.
- **Performance statistics used by the notebook** (notebook 7 cells 8/18/23/27/32): `empyrical.sharpe_ratio(..., risk_free = 0.03/242, period='daily')` and `empyrical.max_drawdown` for the long, short and long-short return series — a **hard-coded 3% annual risk-free rate and a 242-day year**.
- **No exit / holding-period rule:** positions are re-formed every panel date; no stop, take-profit, or maximum holding period appears anywhere in the committed code (`not stated in source`).
- **Position sizing cap:** none found in `construct_portfolio` (no per-contract, per-underlying or per-date weight cap) → `underspecified`, not "no cap".

**B. Scout operationalization** (`research-proposed`, none of this is from the source)

- If this is ever reconstructed: keep the six screens, the decile split, the dollar-OI weighting and the `0.5/0.5` gross split exactly as the code states them, and label anything else (a weight cap, a turnover budget, a spread-charged label, a full-sample sweep loop, contract-level position limits) `research-proposed`.

## Required data

| Item | What the source pins | Status |
|---|---|---|
| Instruments | Chinese **listed** options: CSI index options and SSE/SZSE ETF options; `underlying_code` examples `SH510300`, `SH000300`; commented `SH510050`, `SH588080`; calls `认购` and puts `认沽` | source-reported (README, `docs/data-schema.md`, notebook 6) |
| Fields | `datetime`, `underlying_code`/`StockID`, `option_type`, `strike_price`, `expiration_date`, `calendardays_to_expiration`, `close`, `stock_close`, `implied_volatility`, `implied_volatility_raw`, `is_at_the_money`, `rf` (in **percent**), `volume`, `openinterest`, `stock_volume`, optional `bid`/`ask`, `multiplier`; derived: `delta`, `delta_s`, Greeks (`gamma`, `vega`, `theta`, `rho`, `vanna`, `vomma`), `synthetic_futures_price`, `next_close`, `next_stock_close`, `gap_days`, `doi = log(openinterest × close + eps)`, factor columns | source-reported (`docs/data-schema.md`, notebooks 1/3a-3c/4/5) |
| Hedging instrument | `synthetic_futures_price` (a synthetic index-futures price used for the futures hedge) and `stock_close` for the spot hedge; `delta` vs `delta_s` are the two hedge ratios | source-reported (notebook 1, cells 32/34) |
| Dividends | notebook 1 step is described as "dividends, returns, transaction costs" (`notebooks/pipeline/README.md`); a `dividend_df` enters `models/utils.py get_shrtfee` | source-reported; exact dividend convention `data gap` |
| Costs inputs | `bid_ask_spread` per contract-day (feeds `skip`); `rf` for the financing term | source-reported (notebook 1, cells 43–45, 50) |
| Margin | `ratio = 0.2` (comment: 保证金比率 = margin ratio) used to build the capital base `M_long`/`M_short` for the margin-based return variant | source-reported (notebook 1, cell 50) |
| Universe / screens | six screens listed under `Signal`; months with many missing values dropped; start/end dates filtered first | source-reported headers; numeric thresholds `data gap` |
| Sample period | **not readable in the article (paywall)**. Repo signals only: `configs/default.yaml start_date "2015-04-01"`; `models/factortest.py:20` / `models/IndexFactors.py:18` `start_date = '2015-01-01'`; commented `pd.date_range('2015-02-01', '2024-07-31', freq='MS')` in research notebooks | **`data gap` + frontmatter contradiction 3** |
| Timezone / session | `datetime` is a trading date; no timezone, no session boundary, no auction-time convention is stated anywhere in the repo | `data gap` |
| Point-in-time | new-issue generalization is claimed in the abstract ("newly issued option contracts") but the point-in-time rules and any delisting/expiry handling are in the unread article → `data gap`; screens 4 and 6 remove near-expiry and convexity-violating contracts | source-reported screens; PIT rules `data gap` |
| Missing data | months with many missing values are dropped (notebook 6 markdown); no imputation policy stated | source-reported; policy detail `data gap` |
| Redistribution | raw quotes are proprietary and not shipped; `data/` holds only a README and a synthetic-panel generator marked "for code checks only, not for empirical results"; factor pickles are gitignored; a private ClickHouse extract is expected via env vars | source-reported (README, `data/README.md`) → replication needs licensed exchange data |

## Execution assumptions

`source-reported (companion code)` where the code states it; `data gap` where neither the readable abstract nor the code says.

- **Signal-to-order timing:** labels are built from `close` to `next_close`, i.e. the position is formed at a panel-date close and marked at the next panel-date close. Whether the paper's reported results assume same-close fills or a next-session delay is **not stated in source** → `data gap`.
- **Order type / fill model / latency / participation / partial fills:** **no occurrence** of an order type, fill model, latency, participation cap or partial-fill handling anywhere in the committed code → `data gap`, never "filled at close".
- **Fees and spread:** the backtest's consumed label (`r`/`r_s`) contains **no** commission and **no** spread charge; only financing. Spread is modelled in preprocessing as `skip = k × bid_ask_spread` with **k ∈ {0.25, 0.5, 1.0}** (cells 43–45), applied symmetrically (entry price inflated by `skip`, PnL reduced by `skip`, denominator inflated by `skip`) → three cost ladders `r_l25T/r_l50T/r_l100T` and spot-hedged twins exist as *columns*, and cell 50 folds the `k = 1.0` ladder into `r_long`/`r_short` via `min(r_l100T, (PnL − skip)/max(M_long, D))`. Which of these the article reports as "net of transaction costs" is **not stated in source** → `data gap` (frontmatter contradiction 2).
- **Financing:** `gap_days/365 × rf/100 × outlay` is charged inside both PnL definitions (financing on the hedge outlay over calendar gaps). `rf` is an input column in percent; its source/term structure is `data gap`.
- **Margin / leverage:** margin-based capital base uses `ratio = 0.2` with a floor: long base `M_long = (close + skip) + max(hedge × 0.2 − V, 0.5 × hedge × 0.2)` where `V = max(0, strike − hedge)`; the short base uses `max(hedge × 0.2 − V, 0.5 × ratio × strike)`. Leverage beyond that base, initial-margin haircut rules, maintenance margin and **liquidation are not modelled** → `data gap`.
- **Borrow / shorting:** the abstract asserts that China's short-selling restrictions weaken spot hedging (the *hedge leg* of a long option position), which is a market-structure claim about hedging, not about securities-lending availability for the short decile of options. Short option legs' margin and assignment are not modelled beyond the base above → `data gap`.
- **Impact / capacity / turnover:** no impact model, no ADV/participation screen, no turnover report anywhere in the committed code → `data gap`. Screens 1/2/5 remove illiquid and zero-volume contracts but do not price impact.
- **Taxes, borrow fees, exchange fee schedules:** no occurrence → `data gap`.

## Evidence

### Source-reported

`source-reported (paper abstract)` — the only paper text readable (Wiley abstract, read 2026-09-28):

- Delta-neutral portfolios **based on futures hedging** "deliver substantial improvements in both annual returns and Sharpe ratios" relative to spot-hedged ones, and short-selling restrictions are the stated reason spot hedging is weaker.
- ML models "outperform the IPCA benchmark" and "demonstrate strong generalization ability when applied to newly issued option contracts".
- Out-of-sample performance "remains economically significant after accounting for transaction costs".
- **No magnitude is attached to any of these claims in readable text:** no Sharpe, no annual return, no drawdown, no t-statistic, no sample period, no universe size. **Every such number is a `data gap`.** (Wiley has no open-access badge; Semantic Scholar `openAccessPdf` empty; OpenAlex `is_oa: false`.)

`source-reported (companion code)` — reproducible facts about the pinned artifact, not results:

- GitHub Actions `CI` at `42fe83ca3267`: `completed` / `success` (2026-09-02T08:23:02Z), Python 3.11, `pip install -e ".[dev]"` + `pytest`.
- All fifteen committed `.ipynb` files were parsed this run: **0 stored outputs and `execution_count: null` throughout** (the repo ships `scripts/sanitize_notebooks.py`), so **the repository contains no printed result of any kind** — no Sharpe, no table, no figure. `data gap`.
- `python3 -m compileall -q models option_factors tests examples scripts` on our clone → exit 0 (`research-computed` verification of syntax only).

### Independently reproduced

**Nothing.** `not independently reproduced`. We did not install the dependency stack (blocked in this run's environment), did not run `pytest`, did not run any notebook, and had no access to the licensed option panel. The only checks performed are (a) `compileall` exit 0, (b) reading the CI conclusion from the GitHub API, and (c) `research-computed` arithmetic on committed source lines (the 5-window evaluation slice, `exp(log(openinterest × close)) = openinterest × close`, `0.5 × (long + short)` gross = 1.0). None of these reproduces an empirical result.

### Negative evidence

`source-reported unless marked otherwise` (each item is the source's own artifact, the publisher's own access state, or a `research-computed` reading of the pinned code)

1. **The headline claim is unreadable.** "Economically significant after accounting for transaction costs" is a magnitude-free assertion in an abstract; the supporting tables are behind HTTP 403 → the central empirical claim cannot be inspected.
2. **The repository cannot substantiate any result:** every notebook output is stripped (15/15 files, verified this run) and `data/` ships only a synthetic panel explicitly marked "not for empirical results".
3. **The committed backtest does not charge the cost the abstract claims to survive.** Its label is `r`/`r_s` (financing only) and `construct_portfolio` has no cost parameter at all; the spread ladders live one stage upstream and are never referenced by notebook 7 → `research-computed` from the pinned code (frontmatter contradiction 2).
4. **Evaluation slice is 5 out-of-sample days per cell** (`date_list[length:-1]` over `length + test_num = 26` dates) → `research-computed`; a full-sample sweep is not in the committed artifact, so the article's period-long numbers are not reconstructable from it.
5. **Possible one-day boundary leakage:** `subsample` includes rows dated `date`, whose label `r` is realized from `date` to the next panel date — i.e. the last training label overlaps the test interval — while `testsample` starts strictly after `date`. `research-computed` from `back_test_daily` (lines 577–578); materiality `underspecified`.
6. **Normalization asymmetry:** `construct_portfolio` re-standardizes features on the *evaluation* sample's own mean/std, while training standardizes on the 20-date training pool. If a test window ever contains more than one panel date, the two are on different scales; with a single-date window it is a cross-sectional standardization. `research-computed`; which convention the article used is `data gap`.
7. **Two incompatible R-squared columns** in the same output row (frontmatter contradiction 5) — a diagnostic-integrity issue in the artifact readers would use to judge signal quality.
8. **Sample window is triple-expressed and unverifiable** (frontmatter contradiction 3); the newest hint, `2024-07-31`, means even the most generous reading leaves mid-2024 onward untested, and the article itself is dated 2025-06-04 → no evidence covering the 2024-09 Chinese liquidity regime change, the 2024–2025 program-trading regulatory changes, or any 2025–2026 period (`research-computed` from repo dates).
9. **Universe selection is aggressive:** zero-volume contracts, near-expiry contracts (2 weeks), missing-IV contracts, convexity violators and months with many missing values are all removed before training (`notebooks/pipeline/6`), and months are date-filtered first. Selection sensitivity is not reported anywhere readable → `data gap`.
10. **Liquidity tilt is load-bearing but undescribed:** legs are weighted by dollar open interest, so the book is dominated by the largest OI contracts; the abstract never mentions weighting → mechanism vs. liquidity confound unresolved.
11. **No position limits, no impact model, no turnover report** (all `data gap`) — any "net" claim inherits that blind spot, exactly the failure mode this repository's cost-aware records exist to catch.
12. **Data-availability contradiction** (frontmatter contradiction 4): "available from the authors upon reasonable request" vs. a proprietary, non-shipped panel behind a private warehouse → independent replication is not practically open.
13. **Confined to one market and one hedge instrument:** China's listed index/ETF options only; the whole hedging claim is *about* a Chinese short-sale constraint, so the result does not carry to unconstrained markets without re-testing (`source-reported` scope from the abstract).
14. **Prior literature on the same object exists and is not adjudicated in readable text:** the article's own "Recommended" panel on the Wiley page surfaces *Commodity Option Return Predictability* (Aka, Gagnon, Power, JFM) and *The Dynamics of Option Volatility Smirk and Option Returns Predictability: Evidence From Chinese SSE50 ETF Options* (Guo, Liu, Chen, Lung, JFM) — i.e. the mechanism is contested in the same journal, and we cannot read how this paper distinguishes itself beyond "ML + China + delta-neutral" (`data gap`).
15. **Publication-bias / single-artifact risk:** one squashed commit, one CI run, no issue tracker activity (0 open issues), no independent replication link, and a paper whose quantitative body is closed → all evidence in this record traces to two artifacts controlled by the same author group.
16. **A committed backtest cell cannot execute:** notebook 7 cell 13 calls `back_test_daily('NN', …)`, which reaches `model, ravel = get_randomcv_model(name)` (`models/model.py` line 581); the `'NN'` branch at line 492 is `pass` with the comment "strcuture of NN need data to determine", so `model` is never bound and `return model, ravel` (line 501) raises `UnboundLocalError`. `research-computed` **static reading** — we did not execute the cell (no dependencies installed), so the failure mode is inferred from the source, not observed. Consequence: at least one of the six advertised model comparisons is non-runnable as published, which weakens confidence that the committed artifact matches the paper's experiment set.

## Falsification plan

`research-defined` = thresholds below are Scout-proposed falsification gates, **not** source-specified. `research-proposed` marks operational choices the source does not pin. A FAIL weakens or abandons the hypothesis; this record approves nothing.

- **F1 Reproduction gate (research-defined):** rebuild the panel from licensed exchange data and re-run the pinned walk-forward protocol (20-date train, 1-day test, decile split, dollar-OI weights, `rf = 0.03/242`). FAIL if the long-short series' annualized Sharpe is not `> 0` in the reconstruction window **and** the article's reported Sharpe (once obtainable) is not reproduced within `± 0.20` (`research-defined` tolerance; source prints no accessible number).
- **F2 Cost ladder (research-defined):** evaluate the same book under `skip ∈ {0, 0.25, 0.5, 1.0} × bid_ask_spread` (the source's own ladders) **plus** `research-proposed` per-side commission grids of 0/1/2/5 bp. FAIL the "survives transaction costs" claim if long-short Sharpe ≤ 0 at `0.5 × spread`, or if it is not positive at the source's `1.0 × spread` ladder.
- **F3 Full-sample sweep (research-defined):** replace the 5-window slice with a sweep over every eligible test date from the sample start to end. FAIL if full-sample Sharpe ≤ 60% of the 5-window value (selection-on-start-date sensitivity; `research-defined`).
- **F4 Boundary-leakage audit (research-defined):** re-run with the training window truncated one panel date earlier (`subsample` ends at `date − 1`) so no training label overlaps the test interval. FAIL if long-short Sharpe drops by more than 30% (`research-defined`) — i.e. if the reported edge depends on the overlapping label.
- **F5 Hedge ablation (research-defined):** run the identical signal under futures-hedged, spot-hedged and unhedged labels. FAIL the abstract's hedge claim if futures-hedged Sharpe is not strictly greater than spot-hedged Sharpe in at least 70% of sub-windows (`research-defined`); FAIL the *predictability* claim if the unhedged label shows the same edge (meaning the "delta-neutral" framing adds nothing).
- **F6 Factor-family ablation (research-defined):** re-run with each `docs/factors.md` family removed in turn (IV-slope; risk-neutral moments; tail loss; liquidity/spread; volume/OI; Greeks). FAIL if removing any single family cuts long-short Sharpe by more than half (concentration risk) **or** if a placebo family (random daily ranks) reaches Sharpe ≥ 0.5.
- **F7 New-issue generalization (research-defined):** hold out every contract in its first N sessions, N ∈ {5, 10, 20} (`research-proposed` ladder), as the abstract's "newly issued option contracts" claim implies. FAIL if held-out-new-issue Sharpe ≤ 0 or below 50% of the in-protocol value.
- **F8 Universe-selection sensitivity (research-defined):** re-run with screens 1–6 toggled individually, and with the "drop months with many missing values" rule removed. FAIL if any single screen accounts for more than half of the total edge (i.e. the alpha is a filter artifact).
- **F9 Weighting audit (research-defined):** compare dollar-OI weights against equal weights and against inverse-variance weights. FAIL if the edge disappears under equal weights (confound: the abstract's claim may be a large-OI liquidity effect, not predictability).
- **F10 Statistical robustness (research-defined):** Newey-West t on the daily long-short series at lags 5 and 10, plus a 1,000-draw circular-shift placebo (`research-proposed`). FAIL if |t| < 1.96 or the placebo p ≥ 0.05.
- **F11 Model-selection audit (research-defined):** fix hyperparameters in advance (no per-window `RandomizedSearchCV`) and repeat with a pre-registered single model. FAIL if the pre-registered model's Sharpe ≤ 0 or the reported edge survives only under in-window tuning.
- **F12 Diagnostic-integrity gate (research-defined):** recompute both R² columns with a single definition (sklearn `R2`) and confirm the reported `r2` column is not used anywhere downstream. FAIL the artifact as a validation instrument if the two columns' disagreement changes any model ranking.
- **F13 Forward window (research-defined):** extend the frozen protocol through 2025-2026 data with no re-tuning beyond the source's own rolling rule. FAIL if long-short Sharpe ≤ 0 out of sample or if its sign flips versus the paper window.
- **F14 Crypto port test (research-defined):** translate only the *mechanism* (cross-sectional predictability of delta-hedged option returns + futures-style hedge leg) to a point-in-time crypto option universe (e.g. Deribit BTC/ETH options with perpetual hedges), charging funding, maker/taker fees and a `research-proposed` impact term. FAIL portability if net Sharpe ≤ 0, or if a point-in-time universe cannot be built without listing survivorship, or if the Chinese short-sale-constraint rationale (the source's stated channel) has no analogue and the edge still requires it.

## Crypto portability

**Status: `unproven`.**

The readable source text makes **no crypto claim** — the abstract is about "the Chinese options market" and Chinese short-selling restrictions, and the article body (where any broader statement would live) is paywalled → **absence of a crypto statement is a `data gap`, not evidence of non-portability**.

What would have to change (`research-proposed`, untested):

- **Instrument:** Chinese listed index/ETF options → crypto options (Deribit/Binance/OKX), where the "hedge leg" question flips: the natural hedge is a **perpetual** (funding-bearing, 24/7) or the spot, and index-futures hedging does not exist in the same form. The source's central channel — *short-sale restrictions make spot hedging inferior* — is specific to Chinese equity-asset constraints and may be irrelevant or reversed in crypto, where shorting is cheap and open.
- **Hedge accounting:** the source's financing term (`gap_days/365 × rf/100 × outlay`) must be replaced by 8-hourly funding, plus mark/index-price basis and liquidation semantics.
- **Sessions and timestamps:** 24/7 candles, exchange-local midnight vs. UTC, and expiry/expiry-auction conventions; `gap_days` and "due in 2 weeks" screens need re-definition.
- **Universe/liquidity:** crypto option chains are far thinner per contract; dollar-OI weighting would concentrate in 1–2 expiries, so F9's weighting audit becomes a hard requirement rather than a robustness check.
- **Venue fragmentation and listing survivorship:** contracts appear/disappear quickly; the source's screens (zero volume, near expiry, missing IV) would need point-in-time discipline.

`crypto portability is not authorization to trade` — this record's `approval_scope` remains `research-only`.

## Limitations

1. Results are `source-reported` and **not independently reproduced**; the quantitative body of the article is **paywalled (HTTP 403)**, so sample period, universe counts, model list in the paper, portfolio rule, cost assumptions and every performance number are `data gap`.
2. The record's empirical content therefore rests entirely on the **companion code's** behaviour, whose equivalence to the published specification is `unproven`.
3. The repository ships **no data** (proprietary quotes, synthetic panel only) and **no notebook outputs** → nothing in the artifact can be checked against a printed number.
4. Cost coverage in the *consumed* label is financing-only; spread ladders exist upstream but are not wired into the committed backtest; commission/impact/latency/fill/participation/capacity/liquidation are `data gap` — never read as modelled at zero.
5. Three mutually inconsistent sample-window expressions exist in the repo; the article's own window is unreadable (frontmatter contradiction 3).
6. The committed evaluation slice is 5 out-of-sample days per cell, with a possible one-day label overlap at the training boundary (`research-computed`) — both are materiality `underspecified`.
7. Diagnostic integrity: two differently defined R² columns are emitted side by side (frontmatter contradiction 5).
8. Universe screens (missing IV, zero volume, non-arbitrage, near-expiry, OI, convexity, month-dropping) are partially threshold-less and never sensitivity-tested → selection risk.
9. The book is implicitly a large-dollar-OI tilt; the abstract does not mention weighting, so liquidity and predictability are confounded (F9).
10. Data availability is contradictory (author-request vs. proprietary warehouse) and no working paper/preprint mirror of the article was found → closed evidence base.
11. Single author group controls both artifacts; CI runs the unit tests only; no independent replication link exists.
12. Metadata risk: the third author's given name is printed two ways across sources (frontmatter contradiction 1).
13. Scope: one market (China listed index/ETF options), one hedge-instrument comparison, one (unreadable) cost treatment; not a validated alpha, not a crypto result, not a general option-factor claim.
14. This record covers only what the abstract and the companion code jointly expose; the article's Internet-style appendices, figures and tables were never seen → `data gap` on their contents.

## Implementation status

- **status:** `research-only`
- **implementation_status:** `not-implemented`
- **adoption:** `not-approved`
- **approval_scope:** `research-only`
- **reproduction:** `not independently reproduced`
- No code was written by us, no data was licensed, no backtest was run, no candidate pool / Qlib / Paper / Testnet / Live artifact was touched. Scratch artifacts (clone, feed XML, CI/API reads) live in the Hermes cache and are **not** committed.

## Adoption boundary

Adoption is **not-approved** and out of scope: this is a source-backed hypothesis card only. Moving beyond `research-only` would require (i) obtaining the article body or an author working paper, (ii) F1/F2/F3 passing on licensed data with an explicit cost ladder, (iii) F7/F9 generalization and weighting gates, and (iv) a separate decision record with its own approval scope. `approval_scope: research-only` forbids wiring this into any paper/testnet/live path from this record alone.

## Related Wiki records

- [[quant/strategy-research-record-spec-v1]] — canonical record contract read for this run (`sha256 4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`); no `*-spec-v2.md` exists.
- Wiki Brain `kb_search "option return predictability machine learning China delta-neutral"` → **0 pages**; no related Wiki page could be linked without fabricating one.

Repo-internal neighbors (not Wiki), all with different source identity and mechanism:

- `option-implied-tail-factor-zoo-ds-lasso-arxiv-2609.31263-2026-09-28.md` — option-implied *equity* factor zoo with DS-LASSO; this record's object is the option contract's own hedged return, not equity cross-sectional factors.
- `spy-options-svi-surface-rv-falsification-adverse-selection-2026-09-12.md` — surface/realized-vol falsification on US single-name/index options; different market, different claim.
- `crypto-cross-sectional-instrumented-latent-mispricing-ipca-2026-09-01.md` — uses the same IPCA lineage but on a crypto cross-section with a latent-mispricing mechanism.
- `china-ashare-xgboost-treeshap-behavioral-factor-decomposition-2026-09-04.md` — China ML cross-section on *equities*, so the useful contrast is asset class (stocks vs listed options), not method.
- `crypto-perpetual-funding-rate-carry-spot-perp-2026-08-31.md` and `crypto-two-tiered-cex-dominant-funding-discovery-structural-arbitrage-2026-09-12.md` — the only records sharing the phrase "delta-neutral portfolio"; they are spot-plus-perpetual funding-carry books, explicitly checked and distinct in source identity, instrument, horizon and mechanism.

## Sources

1. Huang, Y., Wang, Z., & Xiao, Z. (2025). *Option Return Predictability via Machine Learning: New Evidence From China*. **Journal of Futures Markets, 45(9), 1232–1252.** DOI: https://doi.org/10.1002/fut.22604 (article page https://onlinelibrary.wiley.com/doi/10.1002/fut.22604, "First published: 04 June 2025", badge "RESEARCH ARTICLE"; abstract landing https://onlinelibrary.wiley.com/doi/abs/10.1002/fut.22604 — read 2026-09-28). PDF endpoint returned HTTP 403 on 2026-09-28; **full text not read**.
2. Publisher metadata printed on that page: Data Availability Statement — "The data that support the finding of this paper are available from the authors upon reasonable request"; Conflicts of Interest — "The authors declare no conflicts of interest"; Volume 45, Issue 9, September 2025, Pages 1232–1252.
3. Companion code (primary source actually read end-to-end): https://github.com/yuxiangh383/option-return-prediction — `main` / `HEAD` = **`42fe83ca32675834d90f1f73819bd580903819a2`** (`git ls-remote` 2026-09-28); single commit `first commit`, 2026-09-02T16:21:18+08:00; GitHub API `created_at 2026-09-02T08:07:44Z`, `pushed_at 2026-09-02T08:22:56Z`, `updated_at 2026-09-12T06:48:35Z`, `license: MIT`, 29 stars, 0 forks, 0 open issues; Actions run `CI` at `42fe83ca3267` `completed/success` 2026-09-02T08:23:02Z (Python 3.11, `pip install -e ".[dev]"`, `pytest`).
4. Specific pinned paths read: `README.md`, `CITATION.cff`, `LICENSE`, `configs/default.yaml`, `docs/factors.md`, `docs/data-schema.md`, `data/README.md`, `notebooks/pipeline/README.md`, `notebooks/README.md`, `.github/workflows/ci.yml`, `tests/test_factors.py`, `tests/test_repo_hygiene.py`, `scripts/sanitize_notebooks.py` (existence), `models/model.py`, `models/summary.py`, `models/factortest.py`, `models/IndexFactors.py`, `models/utils.py`, `notebooks/pipeline/1-DataPreprocess.ipynb`, `notebooks/pipeline/5-ContractLevelFactor.ipynb`, `notebooks/pipeline/6-FilterSummarySelect.ipynb`, `notebooks/pipeline/7-BackTest-daily-regression.ipynb`.
5. Secondary bibliographic cross-check only (never used for results): RePEc/IDEAS https://ideas.repec.org/a/wly/jfutmk/v45y2025i9p1232-1252.html (author list + abstract, read 2026-09-28); Semantic Scholar Graph API record for DOI `10.1002/fut.22604` (paperId `661ccfc4fed50d3fd51412f0c0fc32de04b18bb3`, third author rendered "Zhengyang Xiao", `openAccessPdf.url` empty, read 2026-09-28); OpenAlex `https://api.openalex.org/works/doi:10.1002/fut.22604` (`is_oa: false`, single location = the DOI, read 2026-09-28).
6. Works surfaced by the publisher's own "Recommended" panel on the article page (titles/metadata only, **not read**, listed as context for the contested-claim landscape): Aka, Gagnon & Power, *Commodity Option Return Predictability* (JFM, DOI `10.1002/fut.22614`); Guo, Liu, Chen & Lung, *The Dynamics of Option Volatility Smirk and Option Returns Predictability: Evidence From Chinese SSE50 ETF Options* (JFM).
7. Factor-lineage citations named by `docs/factors.md` (source-reported references, not re-read this run): Xing, Zhang & Zhao (RFS 2010); Bakshi, Kapadia & Madan (RFS 2003); Feunou et al.; Bali, Hu & Murray; Roll, Schwartz & Subrahmanyam; Goyenko, Holden & Trzcinka; An, Ang, Bali & Cakici; Carr & Wu; Amihud (2002); Roll (1984); Horenstein, Vasquez & Xiao; Kelly, Pruitt & Su (IPCA, vendored from `bkelly-lab/ipca`, MIT notice in `option_factors/NOTICE-ipca.txt`).
