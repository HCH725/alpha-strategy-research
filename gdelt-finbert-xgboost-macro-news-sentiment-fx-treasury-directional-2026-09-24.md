---
schema: strategy-research-record-v1
title: "GDELT–FinBERT–XGBoost Macro News-Sentiment Next-Day Directional Trading on FX and 10Y Treasury Futures"
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - news-sentiment
  - macro
  - fx
  - treasury-futures
  - nlp
status: research-only
confidence: low
source_as_of: "2025-05-22"
sources:
  - "https://arxiv.org/abs/2505.16136v1"
  - "https://arxiv.org/html/2505.16136v1"
  - "https://doi.org/10.48550/arXiv.2505.16136"
  - "https://github.com/crypto-tao/macro-news-sentiment-trading/tree/f411ece07a6b9124479a6bcdd02a14c0059f6127"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# GDELT–FinBERT–XGBoost Macro News-Sentiment Next-Day Directional Trading on FX and 10Y Treasury Futures

## Provenance

- **Primary source:** Yuke Zhang, *"Interpretable Machine Learning for Macro Alpha: A News Sentiment Case Study"*, arXiv:2505.16136 [q-fin.CP].
- **Author list (exactly as source):** **Yuke Zhang** — sole author. The HTML front matter prints the footnote *"This research was conducted in the author's personal capacity. The views expressed herein are solely those of the author and do not necessarily represent the views of any institution."* and the address `yukez@seas.upenn.edu` (UPenn School of Engineering and Applied Sciences domain). **The paper body itself never prints an institutional affiliation** → affiliation is `data gap` (inferred only from the e-mail domain, not asserted here).
- **Version pinned:** **v1 only** — submitted **Thu, 22 May 2025 02:24:45 UTC (663 KB)**; no v2 exists as of 2026-09-24. Comments field: *"18 pages (including references), 1 figure, 1 table. Code available at https://github.com/yukepenn/macro-news-sentiment-trading"* plus a keyword list.
- **Rendered-manuscript date anomaly (recorded, not repaired):** the HTML body carries the date line **"August 24, 2026"**, which postdates the only submission (22 May 2025). The landing-page submission history still shows a single v1 → treated as a rendering/`data gap`, not as evidence of a later version.
- **Publication status:** **preprint only.** No journal-ref, no publisher DOI on the landing page; arXiv-issued DataCite DOI **10.48550/arXiv.2505.16136** present. License badge: **"arXiv.org perpetual non-exclusive license"** (not a CC license). Not peer-reviewed as far as the primary source shows.
- **Sample period (source):** market data and GDELT retrieval window **1 Jan 2015 – 30 Apr 2025** (§3.1, §3.4); stated training block **Jan 2015 – Dec 2016**, stated OOS **"c. early 2017 – April 2025"** via 5-fold expanding-window `TimeSeriesSplit` (§3.5). **Committed artifacts span 2015-02-05 → 2025-04-28** (2,640 rows FX / 2,549 rows ZN — see Negative evidence §2 and §3).
- **Universe / instrument (source):** three single instruments — **EUR/USD spot**, **USD/JPY spot**, **10-year U.S. Treasury futures (ZN)**. Cross-sectional universe: none (three independent single-asset books).
- **Venue / data vendor (source + code):** **Yahoo Finance** tickers `EURUSD=X`, `USDJPY=X`, `ZN=F` (`scripts/fetch_market_data.py`, lines 27–31; defaults `--start-date 2015-01-01 --end-date 2025-04-30`). The paper states *"A continuous front-month 10-year Treasury futures series (ZN) … with standard continuous contract roll adjustments applied to mitigate price gaps from contract expiration"* — **the pinned code contains no roll/adjustment logic of any kind** (plain `yf.download` → `pct_change`); roll rule therefore `underspecified` and the paper's claim `contradicted by the pinned code`.
- **Transaction-cost treatment in source:** §3.5(c) — *"Transaction costs are deducted from these returns: 0.02% of the traded value per round-trip for FX pairs and 0.05% for ZN Treasury futures, reflecting reasonably competitive brokerage costs."* Verified in code: a **flat 2 bp (FX) / 5 bp (ZN) deduction on every position flip** (`run_backtest.py` lines 102–127), `trades = |Δposition|`. Arithmetic check (ours): 1,158 × 0.0002 = **0.2316** = the committed `Total Cost` for EUR/USD XGB; 1,043 × 0.0005 = **0.5215** = ZN XGB. **No bid–ask spread, slippage, market impact, latency, borrow, funding/rollover, margin or capacity assumption is stated anywhere in v1**, and the code's optional `--spread-fx/--spread-fut` flags default to `None` (no spread is charged in the reported results) → those are `data gap`, **not** zero-cost claims; the only modeled friction is the flat per-flip deduction above.
- **Code provenance (verified 2026-09-24):**
  - The URL printed in the paper, `https://github.com/yukepenn/macro-news-sentiment-trading`, **returns HTTP 404** (GitHub API `Not Found`); the `yukepenn` account exists but does not list that repository → the paper's own code link is **dead**.
  - The repository that reproduces the paper's Table 1 exactly is **`crypto-tao/macro-news-sentiment-trading`** (created 2025-05-25, pushed 2025-05-22), pinned here at commit **`f411ece07a6b9124479a6bcdd02a14c0059f6127`** (author *and* committer **`yukepenn <yukez@seas.upenn.edu>`**, 2025-05-22T21:43:13Z, message `chore(git): hide .github folder`). The matching author e-mail plus a value-for-value match of all six `backtest/*_performance_metrics.txt` files to Table 1 (same nine metrics, same printed precision) is the identity evidence; the paper never cites this org → repository attribution to the author is **strongly evidenced but not stated by the source** (`underspecified`).
  - Recursive tree at the pinned commit: **48 entries, non-truncated**, containing `scripts/` (fetch_gdelt_data, fetch_market_data, sentiment_analysis, prepare_features, train_model, run_backtest, run_all_models, analyze_performance), `utils/`, `backtest/*_daily_returns.csv` (6 files) and `backtest/*_performance_metrics.txt` (6 files), `plots/shap_*.png` (6 files). **`data/` and `models/` contain only `.gitkeep`** — the GDELT extract, the daily sentiment CSV, the engineered feature CSVs and the trained model pickles are **not committed**, and **GitHub API reports `license: null`** (no license file) → full reproduction from the pinned commit is **not possible**; `tests/` and `api/`/`guides/` directories described in that README do not exist in the tree.
- **Repository-wide source-identity dedup (performed 2026-09-24 before writing; `rg --hidden` over ALL `*.md` including `.mimo-worktrees` / `.agents` / `.hermes` — 2,495 files — plus `coverage_manifest.csv`, 5,807 data rows):** patterns `2505.16136`, `10.48550/arXiv.2505.16136`, `Macro Alpha`, `Yuke Zhang`, `yukez@seas`, `yukepenn`, `crypto-tao`, `macro-news-sentiment`, `g7 currency`, `Filippou`, `Audrino`, `USDJPY=X`, `ZN=F` → **zero hits** in any existing record or manifest row. `GDELT` hits 7 files (3 unique records + 4 worktree copies: crypto-prediction-market skill-score, llm-strategy-discovery-leakage-safe, mfast-market-friction-aware) — none of them trades FX or rates on news sentiment. `EURUSD=X` hits only `cross-asset-hybrid-ensemble-short-horizon-drawdown-alpha-2026-09-06.md` (drawdown-gated cross-asset ensemble, different source, mechanism and horizon). **This source identity is not in the repository.**
- **Family distinction vs adjacent in-repo captures:** existing sentiment records are equity cross-sections (Benzinga daily-headline rank-IC null, earnings-call speaker-weighted FinBERT, `hybrid-xgboost-finbert-regime-adaptive-equity`), a commodity time-series sign rule (aluminum news sentiment), an equity quintile with a GDELT *replication arm* (mfast), and FX handled through **fundamental/Taylor-rule momentum** (`quant/foreign-exchange-macro-news-fundamental-momentum-llm-taylor-rule-2026-09-02` in Wiki Brain) rather than sentiment. This record is materially distinct on at least four axes: **(a) universe/market type** — spot FX pairs and a rate future rather than an equity cross-section or a metal; **(b) signal construction** — daily *time-series* long/short on a classifier probability (always-in-market ±1), not rank sorts, quintiles or sign-of-mean; **(c) horizon/regime** — close-to-close daily with next-day holding, no regime layer; **(d) material data dependency** — GDELT Events API (EventCode 100–199, top-100/day by `num_articles`) + scraped article headlines + FinBERT polarity, vs proprietary or equity-news feeds.
- **Wiki Brain was read only** (`kb_read` of the canonical spec `quant/strategy-research-record-spec-v1.md`, `kb_search` for spec-v2 → 0 hits, and `kb_search` for Related links). No Wiki Brain write, no Kanban, no backtest of our own, no candidate-pool write.

## Economic mechanism

### Source-reported

The author's stated rationale (§1, §4.1, §5.1, §6): macro assets are moved by unstructured text — press releases, central-bank statements, geopolitical and economic reports — and finance-pretrained language models (FinBERT) extract that text's tone better than lexicons. The claimed channels are (i) **mean tone** (bullish/bearish news shifts risk-on/risk-off flows, strongest in FX), (ii) **dispersion** of tone (conflicting headlines ⇒ disagreement ⇒ downward drift; consensus ⇒ upward drift, read off the Figure 1 SHAP plot), (iii) **article impact** = tone × log news volume (coverage intensity scales the move), and (iv) a **sign-flipping, non-linear news→price map** that differs between FX and bonds (good news ⇒ lower Treasury prices via tightening expectations / risk-on flow), which the author argues is why XGBoost beats a linear logit. The author explicitly frames SHAP as the interpretability/"sanity check" layer that shows the model leans on economically sensible news features rather than noise.

### Research interpretation

Stated falsifiably: **attention-driven information diffusion with a slow, non-linear price response in macro assets.** Daily global macro headlines (filtered to GDELT EventCode 100–199) are aggregated into a low-dimensional state (tone, tone dispersion, coverage volume, event-impact score, plus lags/MA/rolling moments); if marginal participants absorb that state with a lag, the *conditional* sign of the next close-to-close return is predictable, and the mapping is non-monotone (e.g. positive tone ⇒ down for ZN), which a linear model cannot represent. An alternative, less flattering reading that the same evidence supports: the state variable proxies a **volatility/risk-off regime** that the model exploits together with the leaky volatility feature (Negative evidence §4), rather than news itself carrying alpha.

Component roles (hybrid structure as described by the source):

```text
Regime:        none — no entry filter, no volatility gate, no event-date conditioning
               (volatility_20d is a *model input*, not a trading filter)
Primary signal: XGBoost P(next-day return > 0); position +1 if p̂ > 0.5, else −1
Baseline arm:   L2 logistic regression on the same features, same threshold
Risk / exit:    none — position is re-derived every day, always ±1 unit, no stop,
               no take-profit, no cash state, no size rule
```

No component is assumed to contribute alpha; the sentiment block in particular must be ablated against the price-only features before any weight is placed on it (F4/F5 below).

## Signal

All rules below are source-reported unless explicitly labelled.

- **Formation timestamp:** features are *"constructed using information available up to the market close of day t"* and used to *"predict the market direction from the close of day t to the close of day t+1"* (§3.4). GDELT rows are keyed by **day** (`sqldate`, UTC) — **no timezone convention is stated for the close or for GDELT's day boundary**, so headlines recorded late in the UTC day can belong to the same feature day while the market has already closed → boundary leakage is `underspecified`, not cleared.
- **Lookback:** sentiment features use day t plus lags t−1..t−3, MA5/MA20 of mean sentiment, 5/10-day rolling std of mean sentiment, 5/10-day rolling sums of volume (§3.3); market features use lagged return `r_t` and a **20-day** volatility; warm-up ≈ 20 trading days dropped at the head of each split (§3.5).
- **News sampling (§3.1 + `fetch_gdelt_data.py`):** GDELT **Events** table, `eventcode` prefix **100–199**, per calendar day keep the **top 100** rows ranked by `num_articles` (`scope_top_events(top_n=100)`), then scrape each event's `sourceurl` page for its headline in parallel (`fetch_headline`: `og:title` else `<title>`); rows whose headline fetch fails are dropped.
- **Sentiment scoring (§3.2):** `ProsusAI/finbert`, headlines lowercased/symbol-stripped/truncated to 512 WordPiece tokens, softmax over {neg, neu, pos}, per-headline polarity `s = P_pos − P_neg ∈ [−1, +1]`.
- **Aggregates (§3.3):** mean `S_t`, dispersion `σ_t`, volume `N_t` and `log(1+N_t)`, article impact `AI_t = S_t · log(1+N_t)`, mean and dispersion of the GDELT **Goldstein** scale, plus lags/MA/Δ(=MA5−MA20)/rolling std/rolling sums.
- **Code-vs-paper feature discrepancy (`prepare_features.py`, pinned commit):** the committed builder creates `sentiment_lag1..3`, `log_articles`, `sentiment_diff`, `sentiment_accel`, three `goldstein_momentum_{0.1,0.3,0.5}` columns **that are in fact EWMs of `sentiment_mean` (no Goldstein column is ever read)**, `article_zscore`, `article_spike` (z>2), `sentiment_smoothed(_std)`, `sentiment_std_{5,10,20}d`, `sentiment_vol_{5,10,20}d`, `volatility_20d`, `sentiment_vol_interaction`, **`article_impact = sentiment_diff · log_articles` (a first *difference*, not the paper's `S_t · log(1+N_t)`)**, `spike_sentiment`. **No Goldstein mean/dispersion, no MA5/MA20-acceleration and no rolling volume-sum column is produced** → the §3.3 feature list and the pinned implementation do not agree; the sentiment CSV's own extra columns (not committed) could in principle supply some of them → `underspecified`.
- **Leaky feature (verified in code, line 66):** `df["volatility_20d"] = df["return_t+1"].rolling(20).std()` where `return_t+1 = close.pct_change().shift(-1)`. At row t this rolling window spans rows t−19…t, i.e. it **contains `return_t+1` itself — the exact label being predicted** — plus 19 returns of which the last is `r_t`. The feature set fed to the model is `[c for c in df.columns if c not in ("date","return_t+1")]`, so this column **is** in `X_train`/`X_test`. This is target leakage into a feature, source-verified, not an inference.
- **Long entry / short entry / exit:** `position = +1 if p̂_t > threshold else −1` (`run_backtest.py` line 84); P&L `strategy_ret = position · return_t+1 − cost` where `cost = 0.0002` (FX) or `0.0005` (ZN) **only on days the position flips**, `trades[0] = 0`. **Never flat** — the book is always fully invested ±1 unit of *compounding equity*, so every flip is a full reversal (close + reverse). Verified: committed `trades` column equals the count of position flips exactly (1,158 / 917 / 1,043 / 1,186 / 215 / 778), and committed positions take only values {−1, +1}.
- **Holding period:** one trading day by construction (signal re-formed daily); overlapping positions impossible.
- **Threshold parameter:** the backtest path that produced the committed results uses the paper's stated **fixed 0.5** (`run_all_models.py --threshold` default `0.5`, matching §3.5(b)). The separate walk-forward path (`train_model.py::optimize_threshold`) by default **optimizes the threshold on train only over `linspace(0.3, 0.7, 41)` by Sharpe** — a hyperparameter the paper never mentions; it does not feed Table 1, but it means "threshold = 0.5" is a property of the reported artifact, not of the code base as a whole.
- **Model parameters (code, pinned):** `XGBClassifier(n_estimators=100, max_depth=3, learning_rate=0.1, subsample=0.8, colsample_bytree=0.8, random_state=42, eval_metric=logloss)`; `LogisticRegression(random_state=42, max_iter=1000)` with **default C**. **No grid search, no `GridSearchCV`, no CV-selected C exists anywhere in the pinned tree**, contradicting §3.5's *"hyperparameters … tuned via a grid search methodology coupled with 5-fold time-series cross-validation"* and *"The regularization strength … is selected using time-series cross-validation"* → the tuning claim is `not implemented in the pinned source`.
- **Reconstruction status:** the *logic* (GDELT 100–199 top-100 → FinBERT polarity → daily aggregates + lags → XGB/logit probability → ±1 daily book with 2/5 bp per flip) is reconstructable in principle; the *artifacts* are not: the GDELT extract, sentiment CSV, feature CSVs and model pickles are uncommitted, `GDELT_API_KEY` is required, headline scraping was performed **once, around May 2025, over 2015–2025 history** (so headline text is "as retrieved in 2025", not as-of-event), and the committed GDELT fetch script starts **2015-02-18** while the committed return file starts **2015-02-05** — the pinned code as shipped **cannot regenerate the committed date range** → `underspecified` / `data gap`.

## Required data

- **Instrument:** EUR/USD spot, USD/JPY spot (Yahoo `EURUSD=X`, `USDJPY=X` — indicative closes, not tradable quotes); 10-year Treasury future `ZN=F` front-month series with **no roll rule implemented**.
- **Universe:** three single assets; no screen, no survivorship/constituent issue; corporate actions not applicable.
- **Venue / market type:** FX spot + exchange-traded rate future, both proxied by Yahoo daily OHLC; no order-book, no fill venue.
- **Timeframe:** daily bars, close-to-close, ~260 FX rows/yr and ~252 ZN rows/yr.
- **Text data:** GDELT v2 **Events** table (`gdelt` Python client `Search(..., table="events")`), fields used: `sqldate`, `actor1name`, `actor2name`, `eventcode`, `goldsteinscale`, `nummentions`, `numsources`, `numarticles`, `avgtone`, `sourceurl`; filtered to EventCode 100–199; top-100/day by `numarticles`; headline text scraped from each `sourceurl` (failures dropped, 20→50 worker pool); requires a GDELT API key.
- **Model artifact:** `ProsusAI/finbert` via HuggingFace Transformers.
- **Point-in-time:** **not addressed for (a) `num_articles`** — the top-100/day selection uses a count that GDELT updates over time, so day-t selection may embed information unavailable at day-t close; **(b) headline text** — pages were fetched retrospectively (revisions, paywall changes, dead links and their silent removal all enter the sample); **(c) GDELT UTC day vs market close** — no timezone statement; **(d) feature/label window** — `volatility_20d` contains the label (see Signal). All four are `data gap` / `underspecified`; none is a claim that leakage *did* occur beyond the code-verified `volatility_20d` case.
- **Timestamp/timezone:** daily only; no intraday resolution, no out-of-order handling → `not stated in source`.
- **Missing data:** headline-fetch failures dropped (not imputed) — stated in code, not in the paper; Yahoo NaN handling, FX weekend/holiday alignment and the ZN/FX calendar merge are `not stated in source`.
- **Funding/fee/spread/borrow needs:** only the flat per-flip 2/5 bp exists; **spot-FX overnight rollover/interest differential, futures margin financing, spread, impact and capacity are all `data gap`** — any later cost model is `research-proposed`.

## Execution assumptions

Everything below is quoted from the source or explicitly labelled; nothing is inferred as source-reported.

- **Signal-to-order timing:** prediction formed on close of day t, applied to the close-to-close return t→t+1 (§3.4, and `return_t+1` alignment in `prepare_features.py`); execution is implicitly **at the close of day t at the same price used to compute `r_t`** → same-bar fill assumption, `data gap` (no next-bar rule is stated).
- **Order type / fill model:** `not stated in source`; returns are computed from Yahoo closes, which behaves like *fill-at-close, full fill, no failure*.
- **Fees:** flat 2 bp (FX) / 5 bp (ZN) of **that day's equity**, charged once per position flip (`strategy_ret = position·return_t+1 − cost`, cost independent of position size). Base mismatch with the prose: §3.5(c) says *"0.02% of the traded value per round-trip"*, but a ±1→∓1 reversal trades two units of notional — under a *traded-value* reading that would be 4 bp of equity while the code deducts 2 bp (half the stated rule), whereas under a *one-round-trip-per-flip* reading the code matches. The base is `underspecified` in the source and we do not pick one.
- **Spread / slippage / impact / capacity:** **not modeled** (code flags default `None`; no statement in v1) → reported results are *after* the flat fee only, and must not be read as net-of-spread or net-of-impact.
- **Leverage / margin / financing:** `not stated in source`. The book compounds daily at ±1× equity and never holds cash, which for spot FX implies holding an FX position overnight with **no rollover/interest differential modeled at all**, and for ZN implies no margin financing statement.
- **Borrow / shorting:** `not stated in source`; the short leg is assumed always available (no borrow fee, no recall risk).
- **Latency / partial fills / failures:** `not stated in source`.
- **Position sizing:** fixed ±1 unit of equity; `research-proposed` if anything else is ever added.

## Evidence

### Source-reported

All figures below are third-party claims from arXiv:2505.16136v1, read directly from that pinned version (HTML full text, **Table 1**, plus §3.5/§4 prose); none is our result. Table 1's caption reads *"Out-of-Sample Performance Metrics (c. Jan 2017 – Apr 2025) … Sharpe = Annualized Sharpe Ratio (assuming risk-free rate of 0) … Cost = Cumulative trading cost as a fraction of initial capital."*

| Asset | Model | CAGR % | Sharpe | Vol % | MaxDD % | Win % | Total Ret % | # Trades | Cost |
|---|---|---|---|---|---|---|---|---|---|
| EUR/USD | Logistic | 6.6 | 0.83 | 7.9 | −19.8 | 53.1 | +91.7 | 1186 | 0.237 |
| EUR/USD | XGBoost | 55.4 | **5.87** | 7.4 | −15.6 | 72.7 | **+8989.3** | 1158 | 0.232 |
| USD/JPY | Logistic | 6.2 | 0.66 | 9.5 | −14.9 | 56.9 | +84.4 | 215 | 0.043 |
| USD/JPY | XGBoost | 53.2 | **4.65** | 9.1 | −22.9 | 72.1 | **+7753.7** | 917 | 0.183 |
| 10Y Treasury (ZN) | Logistic | −0.8 | −0.15 | 4.6 | −20.4 | 47.1 | −7.9 | 778 | 0.389 |
| 10Y Treasury (ZN) | XGBoost | 22.1 | **4.65** | 4.4 | −9.3 | 66.1 | **+568.5** | 1043 | 0.522 |

- §4 prose: *"Sharpe ratios exceeding 4.6 are indicative of highly effective alpha generation, a result particularly noteworthy given the inclusion of realistic transaction costs and the rigorous OOS evaluation methodology."* Abstract/§1/§6 repeat 5.87 / 4.65 / 4.65 with CAGRs *"exceeding 50% in FX and 22% in bonds"* and call the results cost-adjusted and robust across subperiods.
- §4.1 / Figure 1 (SHAP, EUR/USD XGB): `sentiment_std` and `article_impact` described as top drivers; high dispersion → negative SHAP, high positive impact → bullish; `sentiment_mean`, `sentiment_lag1`, `sentiment_ma5`, `goldstein_mean`, `volatility_20d` mid-ranked. Analogous patterns claimed for USD/JPY and ZN (**the figure for those two assets is not published — only one figure exists**).
- §3.5: block bootstrap (1,000 resamples, 20-day blocks) 95% CIs were computed for Sharpe and CAGR but *"not explicitly detailed in Table 1"* → **no confidence intervals are reported anywhere in v1**.
- §5.2 claims: consistent subperiod performance across folds (fold results *"not detailed exhaustively"*), costs included, SHAP as a spurious-correlation sanity check.
- These results have **not** been reproduced by re-running the pipeline (the data and models are not public).

### Independently reproduced

not independently reproduced

What this run **did** verify, read-only, against the pinned commit `f411ece07a6b9124479a6bcdd02a14c0059f6127` (no strategy was re-run; no data were acquired; GDELT/Yahoo inputs are unavailable to us):

1. **Table 1 == the committed `backtest/*_performance_metrics.txt` == our recomputation from the committed `backtest/*_daily_returns.csv`.** Recomputing Sharpe (`√252 · mean/sd`), CAGR (calendar-year compounding of `Π(1+r)`), volatility, max drawdown, win rate, total return, flip count and summed cost **over the full committed file (2015-02-05 → 2025-04-28)** reproduces all six Table 1 rows to the printed precision, e.g. EUR/USD XGB: Sharpe **5.87217** (paper 5.87), CAGR **0.554272** (55.4), Vol **0.073833** (7.4), MaxDD **−0.155475** (−15.6), Win **0.726515** (72.7), Total **89.893375** (+8989.3), Trades **1158**, Cost **0.2316** (0.232); ZN XGB 4.652852 / 0.220699 / 0.043551 / −0.092782 / 0.661044 / 6.685062 / 1043 / 0.5215 ≡ 4.65 / 22.1 / 4.4 / −9.3 / 66.1 / +568.5 / 1043 / 0.522; and likewise for the four logit rows.
2. **The metric window is the *full* file, not the stated OOS window.** Restricting the same committed returns to **≥ 2017-01-01** (the paper's stated OOS start) changes every headline number: EUR/USD XGB Sharpe **5.1008**, CAGR **0.4284**, total **+1840%**; USD/JPY **3.9802 / 0.4202 / +1750%**; ZN **4.1054 / 0.1972 / +347%** — none matches Table 1. Only the full-file computation matches.
3. **80 % of the reported metric window is the final model's training window.** The code path that writes those artifacts (`train_model.py::prepare_data` → chronological 80/20 split → `run_backtest.py` applies that one model to the *entire* feature file) puts the training cut at row `int(n·0.8) = 2112` of 2,640 → **train = 2015-02-05 → 2023-04-14, held-out tail = 2023-04-17 → 2025-04-28 (528 FX rows / 512 ZN rows, 20 % of rows)**. Recomputed over that post-training tail only:

| Asset | Model | Sharpe | CAGR | Total ret | MaxDD | Win % | Flips |
|---|---|---|---|---|---|---|---|
| EUR/USD | XGBoost | **−0.808** | −5.95 % | −11.7 % | −15.6 % | 50.8 | 224 |
| USD/JPY | XGBoost | **−0.289** | −4.22 % | −8.4 % | −22.9 % | 46.6 | 145 |
| 10Y Treasury (ZN) | XGBoost | **−0.229** | −1.38 % | −2.8 % | −9.3 % | 45.5 | 205 |
| EUR/USD | Logistic | +0.687 | +4.85 % | +10.1 % | −6.6 % | 49.2 | 169 |
| USD/JPY | Logistic | +0.357 | +3.74 % | +7.8 % | −13.5 % | 57.8 | 0 |
| 10Y Treasury (ZN) | Logistic | −0.314 | −1.84 % | −3.7 % | −11.3 % | 45.7 | 76 |

   For all three XGBoost books the **entire-sample maximum drawdown occurs inside this post-training tail** (tail MaxDD == full-sample MaxDD), i.e. each XGB equity curve peaks at/just after the training cut and its worst-ever drawdown follows; and the logit/XGB ordering **reverses** relative to Table 1 (logit positive in 2 of 3 tails, XGB negative in 3 of 3).
4. **Code-level target leakage (source-verified):** `volatility_20d` is built from `return_t+1` and is fed to the model (Signal section, `prepare_features.py` line 66).
5. **Cost accounting basis:** per-flip deduction × flip count reproduces `Total Cost` exactly (0.2316 / 0.5215 …). Because each deduction is 2/5 bp of *that day's compounding equity*, the **equity-weighted** sum of the same deductions — Σ `cost_t` × the equity carried into day t — is **8.48× initial capital for EUR/USD XGB** (and 2.06× for ZN XGB) versus the caption's "0.232 / 0.522 as a fraction of initial capital" → the caption's basis is `underspecified`/incorrect as written (terminal equity 90.89× / 7.69×); we do not assert which convention the author intended.
6. **Dead code link:** the paper's GitHub URL is 404; the reproducing repository is `crypto-tao/macro-news-sentiment-trading` (commit author e-mail identical to the paper's corresponding address).
7. **Paper-vs-code field checks:** no roll adjustment (paper claims one), no grid search/CV hyperparameter tuning (paper claims both), `article_impact` defined on a first difference (paper defines it on the level), Goldstein features absent from the builder, GDELT fetch start 2015-02-18 vs claimed 2015-01-01, and the walk-forward path's `TimeSeriesSplit(n_splits=5)` default puts the **first** test block at row 440 = **2016-10-17** for n = 2,640 (second block ends 2018-06-29), not "early 2017" as stated (dates read from the committed return file).

### Negative evidence

1. **The headline result does not survive its own held-out segment.** On the model's post-training tail, all three XGBoost strategies are negative (Sharpe −0.81 / −0.29 / −0.23; −11.7 % / −8.4 % / −2.8 %), and their worst drawdowns of the whole sample sit in that tail (audit §3).
2. **Table 1 is not the protocol the paper describes.** §3.5/§4 describe an aggregated 5-fold expanding-window OOS series ("c. early 2017 – April 2025"); Table 1 instead equals a **single final model applied to the full 2015-02-05 → 2025-04-28 file** (audit §1–§2), of which **80 % of rows predate that model's own training cut** (audit §3). The described walk-forward metrics are only logged, never written to the repo.
3. **The stated OOS window and the reported window disagree** (audit §2): ≥2017 numbers are 5.10 / 3.98 / 4.11, not 5.87 / 4.65 / 4.65 — so the caption's date range does not describe the numbers beneath it.
4. **Target leakage in a feature is present in the shipped code** (audit §4): `volatility_20d` contains the very `return_t+1` being predicted. Any clean re-run must drop it before the current numbers can be interpreted at all.
5. **A 66–73 % daily directional hit rate sustained over 8–10 years in liquid FX and Treasuries is far outside anything credible** for a daily close-to-close book with no latency, spread or rollover costs; the source reports no confidence intervals (bootstrap CIs were computed but never shown), no multiple-testing control across 3 assets × 2 models × a threshold/hyperparameter search, and no deflated-Sharpe or holdout discipline.
6. **Linear baseline gap flips out of sample.** Logit ≈ 0.83/0.66/−0.15 vs XGB 5.87/4.65/4.65 in Table 1; in the post-training tail logit is +0.69/+0.36/−0.31 while XGB is negative on all three — the "non-linearity is the alpha" story (§5.1) is contradicted by the only segment where the model was not fitted.
7. **USD/JPY logit never trades in the tail** (0 flips after 2023-04-17), so its positive tail return is a constant-position bet, not a signal — evidence that flip counts, not just returns, must be reported.
8. **Costs are the only friction and are weakly specified:** 2 bp / 5 bp flat per flip, **no spread, slippage, impact, latency, borrow, rollover/interest differential on spot FX, futures financing or capacity anywhere in v1 or in the code defaults** (audit + §3.5). The claimed "realistic transaction costs" reduce to one constant; the caption's cost basis is itself `underspecified` (audit §5).
9. **Retrospective headline scraping (May 2025 over 2015–2025 URLs):** dead/updated pages are silently dropped, and headline text is as-retrieved, not as-published → text survivorship and revision bias unquantified; `num_articles` top-100 selection uses a GDELT counter whose point-in-time value is never addressed.
10. **Timezone boundary is unstated:** GDELT days are UTC, the trading day is a Yahoo close; news logged after the close but within the same UTC day can inform a prediction about a return window that has already begun → alignment is `underspecified`, not cleared.
11. **Reproduction is blocked by construction:** `data/` and `models/` are `.gitkeep`-only, `GDELT_API_KEY` is required, no license file exists, the README describes `tests/` that are absent, and the paper's own code URL is dead (audit §6) — the artifact can be *audited* (as here) but not *regenerated* from the pinned commit.
12. **Paper-vs-code discrepancies accumulate:** roll adjustment claimed/absent, grid search + CV tuning claimed/absent, article-impact and Goldstein features mismatched, GDELT start date 2015-01-01 claimed vs 2015-02-18 coded, first walk-forward fold starting 2016-10-17 vs "early 2017" claimed, hidden threshold optimization available in code though §3.5 states a fixed 0.5 (audit §7). Each is individually small; together they mean the prose protocol cannot be trusted as a description of the artifact.
13. **Internal arithmetic/label tension in Table 1:** `Total Ret +8989 %` with `CAGR 55.4 %` over 10.23 years is internally consistent *only* because the window is the full 2015–2025 file (an 8.3-year window at 55.4 % would give ≈ +3,800 %) — further confirmation that the caption's window is wrong (audit §2).
14. **Single unreviewed preprint, sole author, one figure, no CIs, no fold table, no *working* code link (the printed URL is 404), no data** — publication-bias and provenance risk are high.

None of the above was contradicted by any other reviewed source; absence of an external replication is not evidence that no negative result exists.

## Falsification plan

Tests and thresholds below that are not printed in the source are labelled `research-proposed` (design choices) or `research-defined falsification threshold` (accept/reject cutoffs). Data assumed: a point-in-time GDELT article stream with publication timestamps, an explicitly chosen tradable FX/rate instrument, and a published fee/rollover schedule.

- **F1 — Leakage removal (`research-proposed`; threshold `research-defined`):** rebuild features with `volatility_20d` computed from *lagged* returns only (no `return_t+1` in any input window), then re-estimate on a strictly walk-forward protocol. **Fail if** the EUR/USD XGB full-period Sharpe falls below **1.0** or its edge over the logit baseline falls below **+0.30** Sharpe units ⇒ the reported effect is leakage-driven.
- **F2 — True out-of-sample window (`research-proposed`; threshold `research-defined`):** freeze every parameter at 2023-04-14 and evaluate only 2023-04-17 → 2025-04-28 (and extend forward). **Fail if** any of the three XGB books has Sharpe **≤ 0**, or if 2 of 3 are ≤ 0 ⇒ `regime-limited`/falsified as a general claim (this test already fails on the committed artifacts — audit §3).
- **F3 — Protocol-fidelity audit (`research-defined`):** publish the aggregated walk-forward (5-fold expanding) daily series and recompute Table 1 from it. **Fail if** walk-forward Sharpe is < 50 % of the Table 1 value on any asset ⇒ Table 1 must be reclassified as in-sample-contaminated.
- **F4 — Sentiment ablation (`research-proposed`; threshold `research-defined`):** price-only features (lagged return + true trailing vol) vs full feature set, same protocol. **Fail if** the full set does not beat price-only by **≥ +0.30** Sharpe units ⇒ news carries no incremental information (mechanism rejected even if the book profits).
- **F5 — Placebo (`research-proposed`; threshold `research-defined`):** circularly shift the daily sentiment series by ±1…±20 days (1,000 draws) and recompute Sharpe. **Fail if** the true Sharpe's |z| < **2.0** against the placebo distribution or ≥ 5 % of shifts beat it.
- **F6 — Execution/cost stress (`research-proposed`; threshold `research-defined`):** apply a round-trip ladder of 0 / 2 / 5 / 10 / 20 bp **plus** the observed FX bid–ask, a **rollover/interest-differential ledger for spot FX**, futures financing, and next-bar (not same-close) fills. **Fail if** net Sharpe ≤ 0 at 10 bp round-trip, or if the rollover ledger alone erases > 50 % of gross P&L.
- **F7 — Multiple-testing control (`research-defined`):** report Deflated Sharpe over the full grid actually searched (3 assets × 2 models × 41 thresholds × any feature variants). **Fail if** deflated Sharpe < **1.0** ⇒ the headline is a selection statistic.
- **F8 — Data/point-in-time audit (`research-defined`):** rebuild day-t features strictly from articles published ≤ close(t) in the instrument's timezone, with `num_articles` as of day t. **Fail if** the hit rate drops below **55 %** or Sharpe halves ⇒ the effect depended on post-hoc news selection/alignment.
- **F9 — Vendor/instrument replication (`research-proposed`; threshold `research-defined`):** rerun with an executable FX instrument (any prime-broker feed) and a roll-adjusted ZN series from a second vendor. **Fail if** the sign of full-period return flips on either vendor ⇒ Yahoo-close artifact.
- **F10 — Baselines (`research-proposed`):** compare against (a) always-long, (b) sign of trailing 5-day return, (c) a pure-volatility/risk-off timing rule. **Fail if** sentiment does not beat (b) and (c) after F6 costs ⇒ sentiment is redundant with beta/vol timing.
- **Failure action (`research-defined`):** F1, F2 or F3 failing ⇒ record stays `research-only` and the mechanism is marked falsified in any future update; F4–F10 failing ⇒ narrow the claim (window-, vendor- or implementation-specific) rather than discard wholesale.

## Crypto portability

**`unproven`.**

- The source contains **zero** crypto evidence: three traditional instruments, daily Yahoo closes, GDELT headlines. Porting is a hypothesis, not a finding — and the README forbids `direct` for non-crypto evidence.
- Mechanism-level plausibility is mixed: crypto trades 24/7 (a "day" and its close must be defined, e.g. UTC 00:00), macro headlines reach CEX books within seconds (faster absorption should *weaken* a diffusion lag — and the source's own EMH-style claims cut the same way), and GDELT's macro EventCode filter is heavily USD/rates-centric, i.e. thin coverage of crypto-native events.
- Concrete porting risks (`research-proposed`): venue choice spot vs USDT-perp changes P&L identity because the source models **no funding at all** (8-hour accrual can flip a daily book's sign); funding/borrow on the short leg, liquidation and leverage are unaddressed; venue fragmentation and index/mark-price differences; listing/delisting churn; UTC-candle vs exchange-candle boundaries; wash-traded prints on thin pairs.
- Label stays `unproven` — not `adapted` (nothing has been adapted or tested), not `direct`.

## Limitations

- **The reported "OOS" metrics are computed over the model's training window** (80 % of rows) — code-verified; `underspecified` in the source, contradicted by our audit.
- **A shipped feature leaks the target** (`volatility_20d` from `return_t+1`) — code-verified; until removed, no number in Table 1 can be interpreted.
- **Cost model is one flat constant**; spread, slippage, impact, latency, borrow, spot-FX rollover, futures financing and capacity are `data gap`, and the caption's cost basis is `underspecified`.
- **Same-close fill assumption** (signal and fill at the same close price) → `data gap`.
- **Retrospective headline scraping + `num_articles` selection + unstated UTC/close timezone** → point-in-time integrity `unproven`.
- **Reproduction blocked:** data, sentiment CSV, feature CSVs and model pickles absent from the pinned commit; no license; paper's code link dead; GDELT API key required. `data gap`.
- **Paper-vs-code discrepancies** in roll handling, hyperparameter tuning, feature definitions and dates (Evidence §7) → the prose is not a faithful description of the artifact.
- **No confidence intervals, no fold-level table, one figure (EUR/USD only), no model/data cards**; bootstrap CIs were computed but never reported.
- **Three single assets, one 10-year window, one vendor (Yahoo), one preprint**; sample ends **2025-04-28**; no subperiod robustness table is published.
- **Not independently reproduced** by this run: we recomputed metrics *from the author's own published return series* and audited the shipped code, but did not re-run training, re-fetch GDELT/Yahoo, or obtain any market/text data.

## Implementation status

`not-implemented`.

Nothing has been implemented in our research stack: no signal code, no data acquisition (GDELT extract and Yahoo series were not fetched by us), no backtest of our own, no Qlib run, no production card, no Paper/Testnet/Live activity. This document is a normalized research capture plus a read-only audit of the author's committed artifacts. Any later implementation would first have to remove the leaked feature, pin a point-in-time news build, define fills/timezones and add rollover + spread costs — all currently `underspecified`, `data gap` or `research-proposed`.

## Adoption boundary

`status: research-only` · `implementation_status: not-implemented` · `adoption: not-approved` · `approval_scope: research-only`.

The presence of this record does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. No confidence value in this record is a profit claim — `confidence: low` describes confidence in the **research interpretation** (single unreviewed preprint whose reported window, protocol and features do not match its own committed artifacts, plus code-verified target leakage and a negative held-out tail).

## Related Wiki records

Read-only `kb_search` hits (real vault paths, not fabricated):

- [[quant/foreign-exchange-macro-news-fundamental-momentum-llm-taylor-rule-2026-09-02]] — closest in *universe* (FX macro news) but a fundamental/Taylor-rule momentum mechanism via LLM classification, not FinBERT sentiment → next-day direction.
- [[quant/same-day-open-to-close-directional-spy-walk-forward-2026-09-02]] — walk-forward tree-ensemble daily direction with threshold conditioning on SPY; same methodological failure family (daily direction, threshold choice, sample-support degradation), different asset class.
- [[quant/small-cap-alpha-beta-separation-uncertainty-aware-llm-portfolio-2026-09-02]] — multimodal LLM news + macro + technicals, equity small-cap allocation.
- [[quant/crypto-news-peer-overreaction-reversal-4w-2026-09-03]] — news-identified event reaction with an explicit reversal horizon; different universe and horizon.

Adjacent **repository files (not Wiki links):**

- `hybrid-xgboost-finbert-regime-adaptive-equity-2026-09-04.md` — same model stack (FinBERT + XGBoost) on equities with a regime layer; different universe and signal construction.
- `mfast-market-friction-aware-llm-news-sentiment-quintile-2026-09-22.md` — news-sentiment cross-sectional quintile with friction modeling and a GDELT replication arm; the friction discipline this record's source lacks.
- `benzinga-daily-headline-sentiment-cross-sectional-rank-ic-null-2026-09-24.md` — headline sentiment with FDR-controlled null results; closest in-family negative evidence.
- `aluminum-news-sentiment-topic-event-conditional-long-short-2026-09-24.md` — commodity time-series sentiment sign rule; different asset class, monthly horizon.
- `llm-news-probing-excess-return-sentiment-timing-2026-09-06.md` — news-sentiment timing hypothesis, equity.
- `cross-asset-hybrid-ensemble-short-horizon-drawdown-alpha-2026-09-06.md` — uses `EURUSD=X` too, but a drawdown-gated cross-asset ensemble (no text).
- `climate-attention-global-warming-search-treasury-excess-return-predictor-2026-09-23.md` — Treasury excess-return prediction from a non-news attention signal.
- `llm-strategy-discovery-leakage-safe-search-deflated-eval-2026-09-04.md` — leakage-safe / deflated evaluation, directly relevant to F1, F7 and F8.

## Sources

1. Yuke Zhang. "Interpretable Machine Learning for Macro Alpha: A News Sentiment Case Study." arXiv:2505.16136v1 [q-fin.CP], submitted 22 May 2025 02:24:45 UTC. https://arxiv.org/abs/2505.16136v1 — landing (author block, personal-capacity footnote, v1-only submission history, Comments field with the code URL, license, DOI).
2. arXiv HTML v1 (primary full text used for every paper-attributed number here): https://arxiv.org/html/2505.16136v1 — §1, §3.1–§3.5 (data, FinBERT scoring, feature definitions, cost statement, walk-forward protocol, 0.5 threshold), §4 / **Table 1** (all six performance rows), §4.1 / Figure 1 (SHAP), §5.1–§5.3, §6.
3. arXiv-issued DataCite DOI: https://doi.org/10.48550/arXiv.2505.16136
4. Code repository (reproduces Table 1 exactly; not the URL printed in the paper): https://github.com/crypto-tao/macro-news-sentiment-trading/tree/f411ece07a6b9124479a6bcdd02a14c0059f6127 — pinned commit `f411ece07a6b9124479a6bcdd02a14c0059f6127` (author/committer `yukepenn <yukez@seas.upenn.edu>`, 2025-05-22T21:43:13Z); audited files: `scripts/fetch_gdelt_data.py`, `scripts/fetch_market_data.py`, `scripts/prepare_features.py`, `scripts/train_model.py`, `scripts/run_backtest.py`, `scripts/run_all_models.py`, `utils/gdelt_utils.py`, `utils/headline_utils.py`, `backtest/*_daily_returns.csv` (6), `backtest/*_performance_metrics.txt` (6); recursive tree 48 entries, `license: null`, `data/` and `models/` empty (`.gitkeep` only). Audit run 2026-09-24 (read-only).
5. Dead link as printed in the paper (verified 2026-09-24, HTTP 404 via GitHub API): https://github.com/yukepenn/macro-news-sentiment-trading
