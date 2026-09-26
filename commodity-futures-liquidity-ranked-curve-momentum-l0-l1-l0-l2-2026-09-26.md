---
schema: strategy-research-record-v1
title: "Commodity-futures within-curve basis momentum — Goldman-style F0/F6 replication plus liquidity-ranked L0-L1 / L0-L2 extension (GitHub ddxmy/Basis-Momentum @ 6f0127f3, 5 bp one-way cost, results through 2026-07-10)"
created: 2026-09-26
updated: 2026-09-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - commodity-futures
  - term-structure
  - within-curve-momentum
  - transaction-costs
  - github-replication
status: research-only
confidence: medium
source_as_of: "2026-07-10 (last performance date in the pinned source; source snapshot commit dated 2026-07-29; read by Scout 2026-09-26)"
sources:
  - "https://github.com/ddxmy/Basis-Momentum — public MIT-licensed research repository; pinned commit 6f0127f3f0513261297c650361c432adb01cc080 (branch main, sole branch, no tags), commit date 2026-07-29T08:19:44Z"
  - "https://github.com/ddxmy/Basis-Momentum/tree/6f0127f3f0513261297c650361c432adb01cc080 — README.md, docs/{methodology,results,limitations,index}.md|html, docs/provenance.html, data/{README.md,schema.sql}, notebooks/methodology_and_results.ipynb, src/*.py, scripts/*.py, results/** (all read by Scout 2026-09-26)"
  - "https://api.github.com/repos/ddxmy/Basis-Momentum and /branches /tags /commits?per_page=5 — repository metadata read 2026-09-26"
  - "https://ddxmy.github.io/Basis-Momentum/ — static documentation site generated from the same docs/ tree (same content; no additional claims read)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Commodity-futures within-curve basis momentum — Goldman-style F0/F6 replication and liquidity-ranked L0-L1 / L0-L2 extension

## Provenance

- **Primary source (pinned snapshot):** public GitHub repository `ddxmy/Basis-Momentum`, *"Goldman-style basis momentum replication and liquidity-ranked commodity futures extensions"* (repository description, GitHub API). Pinned commit **`6f0127f3f0513261297c650361c432adb01cc080`** — the sole commit at the head of the sole branch `main`, **no tags** (verified via GitHub REST `branches` / `tags`, read 2026-09-26). Commit date **2026-07-29T08:19:44Z**; repository created **2026-07-08T14:01:18Z**; last push **2026-07-29T08:19:48Z**. Full history is only four commits (`99eb95299b7cdd012950b8baac778dd797f68d7a` initial 2026-07-08 → `70455f7de93cdcacef9b42267d6e607521dc7c31` publish → `25be2d8cbf1a964f2222a23fc389f4265164b29e` scope tightening → `6f0127f3…` merge), i.e. earlier history was squashed at publication.
- **Author list exactly as the source:** **no human author is named anywhere in the repository.** The only attribution strings are the GitHub account **`ddxmy`** and the LICENSE copyright line **"Copyright (c) 2026 Basis Momentum contributors"** (MIT). There is no `AUTHORS`, `CITATION`, `CITATION.cff`, paper, DOI, affiliation, ORCID or contact address → authorship identity is a **`data gap`**. Repository metadata at capture: 0 stars, 0 forks, 0 open issues, size 4,775 KB, license MIT, homepage `https://ddxmy.github.io/Basis-Momentum/`.
- **Repository metadata at capture:** repository description "Goldman-style basis momentum replication and liquidity-ranked commodity futures extensions"; default branch `main`.
- **Files read in full by the Scout on 2026-09-26:** `README.md` (2,341 bytes); `docs/methodology.md`; `docs/results.md`; `docs/limitations.md`; `docs/provenance.html`; `docs/index.html`; `data/README.md` (data contract); `data/schema.sql`; `notebooks/methodology_and_results.ipynb` (11 cells — all markdown cells read verbatim, code cells read for their inputs/outputs); `src/liquidity_curve_data.py` lines 1-125 (eligibility screen and curve selection); `src/liquidity_basis_momentum_factor.py` lines 96-175 (signal accumulation and rank mapping); `src/goldman_basis_momentum_factor.py` lines 1-80 (F0/F6 extraction); `src/goldman_basis_momentum_backtest.py` lines 66-125 (`build_rank_weights`), 233-258 (weekly-Friday selection, trailing vol) and 408-480 (`run_backtest`, cost accounting); `src/goldman_basis_momentum_report.py` lines 51-91 (`compute_performance_metrics`); `scripts/run_liquidity_extension.py` `CONFIG`; `.github/workflows/tests.yml` (CI: `pytest -q`, `shasum -a 256 -c results/checksums.sha256`, publication safety scan); `LICENSE`.
- **Integrity check performed by the Scout (artifact integrity, not a reproduction):** the tarball of the pinned SHA was fetched from `https://codeload.github.com/ddxmy/Basis-Momentum/tar.gz/6f0127f3…` (5,276,418 bytes) and `shasum -a 256 -c results/checksums.sha256` returned **OK for all 37 manifest entries** on 2026-09-26. Headline metrics in every `summary.csv` were re-derived arithmetically from the committed `daily_performance_with_drawdown.csv` and matched to floating-point tolerance. This confirms the committed artifacts are internally consistent; it does **not** re-run the backtest, because the underlying market database is not published.
- **Sample period verified:** Goldman-style baseline `summary.csv` = **2008-01-21 → 2026-07-10, 4,487 trading days**; the retained parameter record states `sample_start 20070101` / `sample_end 20260710`, i.e. 2007-01-01 is the history start used for signal warm-up and the first dated return is 2008-01-21 (warm-up + minimum-asset start; the source does not narrate the gap → the exact reason for the 12.5-month start lag is a `data gap`). Liquidity extension = **2019-01-07 → 2026-07-10, 1,820 aligned trading days**, with `warm_up_history: "signals are formed from pre-display history; the source run begins 20070101"` (`results/liquidity/parameters.csv`).
- **Universe verified at the level the source discloses:** the source repeatedly says **"commodity futures"** (`docs/index.html`: "Commodity futures research") and `data/README.md` describes a "tradable commodity universe". **No exchange, country, market venue, product list, or contract count is stated anywhere in the repository** → venue / geography / exact product set is a **`data gap`**. Disclosed data contract: SQLite tables `fut_daily(ts_code, trade_date, close, settle, vol, amount, oi)`, `fut_basic(ts_code, exchange, fut_code, list_date, delist_date)`, `tradable_universe(trade_date, exchange, fut_code, category, main_contract, is_tradable, method)`; retained experiments use `method = 'top2_volume_by_day'`. The raw database and all raw quotes are deliberately excluded ("Licensed raw data and the SQLite database are excluded") → **the published results are not publicly reproducible from data alone**.
- **Transaction-cost treatment verified at Methods level:** `docs/methodology.md` ("The baseline deducts a 5 bp one-way turnover cost"), `results/goldman_style/parameters.csv` (`baseline,one_way_cost,5 bp`; `target_vol,one_way_cost,5 bp`), `results/liquidity/parameters.csv` (`all,one_way_cost,5 bp`), and the executable path `src/goldman_basis_momentum_backtest.py::run_backtest` lines 460-463: `turnover = Σ|new_weight − old_weight|` over the union of names (`fillna(0.0)` on both sides, so an exited name counts as a full close), `day_turnover = turnover if position == 0 else 0` (charged once, on the first day after the rebalance date), `cost = day_turnover * cost_rate` with default `cost_rate = 0.0005`, `portfolio_return = gross_return − cost`. A whole-repository term scan for `bid-ask`, `spread`, `slippage`, `commission`, `impact`, `margin`, `financing`, `funding`, `capacity`, `latency`, `fill`, `participation`, `limit move` finds these concepts only inside `docs/limitations.md` as explicitly **out-of-scope exclusions** ("inverse-volatility weighting, capacity, ADV/OI limits, category constraints, integer lots, margin, limit moves, and detailed roll execution") → **every one of those cost/fill fields is `data gap`, never zero.**
- **Publication status:** public source-code repository only. **Not peer reviewed, no paper, no working-paper listing, no preprint server, no DOI.** The repository itself disclaims: "This is not an exact Bloomberg index replication and not investment advice."
- **`docs/results.md` states:** "The source provenance and transformations are documented in the implementation report maintained with this publication task." That implementation report is **not present in the repository** → provenance of the transformation from the private database to the committed CSVs is a **`data gap`**.
- **Whole-repository source-identity dedup (2026-09-26; programmatic scan of ALL 2,561 `*.md`/`*.csv` files in this repository including the hidden trees `.mimo-worktrees/`, `.agents/`, `.hermes/`, plus `coverage_manifest.csv` — `git log -20` was used only as a glance):** `github\.com/ddxmy` = **0**; `ddxmy\.github\.io` = **0**; `6f0127f3` / the full 40-char SHA = **0**; `liquidity-ranked contract-curve|Goldman-style basis momentum replication` = **0**; `top2_volume_by_day` = **0**; `L0-L1|L0-L2|L0L1|L0L2` = **0**; `F0/F6|F0 and F6|seventh listed contract` = **0**; `F3 same-contract` = **0**; `liquidity curve screen|amount_threshold` = **0**. **No existing record carries this source identity.**
  - Family-level near matches (expected, **not** source-identity matches): 20 records contain the string `basis-momentum` / `Basis-Momentum`, all using it as the **Boons & Porras Prado (JF 2019)** signal name.
  - Four-axis neighbours checked and kept distinct: (1) `crypto-futures-cross-sectional-basis-momentum-slope-2026-08-31.md` — different source (Boons & Prado JF 2019 DOI 10.1111/jofi.12740), different universe (crypto futures), different construction (cross-sectional across commodities, first-vs-second-nearby momentum); this record is **within a single product's curve** (nearest vs deferred maturities) on unnamed commodity futures. (2) `crypto-futures-term-structure-roll-yield-carry-2026-08-31.md` — different source and a **static carry/roll-yield level** signal, not a 120-day **momentum of the curve** signal; crypto universe. (3) `g10-fx-carry-fx-value-energy-roll-yield-net-cost-audit-2026-09-23.md` — different source, FX/energy universe, and it **refutes** energy basis-momentum at 10 bp (Sharpe −0.06); used here as contrary evidence. (4) `commodity-seasonal-dvr-ssa-rlssa-benchmark-null-2026-09-14.md` — different source, different mechanism (calendar/delivery-month **seasonality**, not term-structure momentum), same broad asset class. (5) `crypto-adjacent-futures-weekly-basis-return-reversal-2026-09-03.md` — different source, crypto, weekly **basis-return reversal** rather than 120-day curve momentum. Source identity, mechanism, signal construction and material data dependency all differ in every pair.

## Economic mechanism

### Source-reported

- **The source states no economic mechanism.** It is a reproduction-and-extension package, not a thesis: `README.md` ("A compact, public research package for a Goldman-style commodity basis-momentum replication and a liquidity-ranked contract-curve extension"), `docs/methodology.md`, `docs/results.md`, `docs/index.html` and the notebook's markdown cells describe **construction and results only**. There is no hypothesis paragraph, no participant-behaviour story, no friction/pressure channel, no citation of the academic basis-momentum literature, and no reference explaining what "Goldman-style" refers to. **No mechanism claim may be attributed to this source.**
- The only quasi-mechanistic statement in the source is a scope restriction, not an explanation: the liquidity screen "ranks eligible contracts by maturity after the liquidity screen" (`README.md`) and the notebook notes the screen "makes it a more selective cross section".
- The source's own honesty framing is recorded verbatim in substance: "Results require out-of-sample and implementation robustness checks before investment use" (notebook, *Limitations*).

### Research interpretation

- **Hypothesized mechanism (Scout-generated, NOT source-reported — falsifiable form):** *within-curve term-structure demand-imbalance persistence.* A single commodity's futures curve prices the same physical asset at different maturities; transient hedging/inventory/inventory-financing demand hits the front of the curve first and decays over weeks, so the accumulated difference between near-maturity and deferred-maturity contract returns over the past 120 days carries information about where the curve relative prices are heading next. If that pressure persists rather than reverses, ranking products by the sign/scale of `Σ[log(1+r_near) − log(1+r_deferred)]` and going long the highest / short the lowest should earn a continuation return. Two sub-channels must be separated in testing: (a) *curve-momentum continuation* (the pressure persists); (b) *liquidity-selection effect* (the screen only keeps products whose near contract is actively traded, so the book is simply a better-traded subset). The source does not distinguish them.
- **Component roles of the hybrid (Scout-labelled):** *Signal*: 120-day sum of near-minus-deferred log-return spread within each product, cross-sectionally converted to a centered rank. *Universe filter (tradeability precondition, not alpha)*: close > 0, `amount ≥ 2000`, `oi > 0`, `maturity ≥ 30 days` before a contract may enter the curve ranking. *Risk/sizing overlay (not alpha)*: centered-rank dollar-neutral weights, ±0.5 gross per side, gross exposure 1.0; optional separate 10 % target-volatility overlay on the F0/F6 book only. *Cost*: 5 bp one-way turnover. **No regime filter, no stop, no take-profit, no time exit, no position cap beyond the ±0.5/±0.5 normalization exists in the source — any such addition would be `research-proposed`.**
- Adjacent literature (Boons & Porras Prado, *Basis-Momentum*, JF 74(1) 2019; curve-momentum studies) is cited here **only as Scout context for why the mechanism could be real**; the source itself cites none of it and none of those papers' numbers are used in this record.

## Signal

Everything in this section is **source-reported** (paths relative to pinned commit `6f0127f3…`), except where explicitly marked `research-proposed`.

**A. Goldman-style F0/F6 baseline** (`docs/methodology.md`, `notebooks/methodology_and_results.ipynb` cell 1, `src/goldman_basis_momentum_factor.py`)

- **Curve rank:** for each product `fut_code` on each date, all listed delivery-month contracts are ordered by maturity; **F0 = nearest, F6 = seventh listed**, F3 = third (`rank ∈ {0,6}` selected in `extract_f0_f6_prices`, inner-joined on `(trade_date, fut_code)` so a product needs **both** F0 and F6 present).
- **Signal:** `BM(F0/F6) = Π_{k=t−251}^{t}(1 + r(F0)_k) − Π_{k=t−251}^{t}(1 + r(F6)_k)` — the difference of 252-trading-day compounded **same-contract** close-to-close returns (`DEFAULT_LOOKBACK = 252`), computed daily (`min_periods = lookback` warm-up).
- **Formation timestamp:** the signal is evaluated on the trading date `t`; `select_weekly_rebalance_dates` keeps dates whose weekday is **Friday** (`weekday == 4`). Weights are applied **from the next trading day after the Friday** (`start_idx = date_pos[rebalance_date] + 1`) → the book is never traded on the signal's own close. Timezone / exchange session is **not stated** (`data gap`).
- **Weighting:** `compute_centered_rank` → cross-sectional centered rank score; `build_rank_weights` maps, per rebalance date, `weight_i = 0.5 × score_i / Σ_{score>0} score` on the long side and `weight_i = 0.5 × |score_i| / Σ_{score<0} |score|` on the short side → **long gross 0.5, short gross 0.5, gross 1.0, dollar-neutral**, size proportional to centered rank. Names with `rank_score == 0` get weight 0.
- **Return leg:** **F3 same-contract close-to-close return** (`read_curve_contract_returns(curve, curve_rank=3)`), i.e. the book's P&L is taken on the third contract, not on F0/F6 — the signal leg and the P&L leg are deliberately different maturities.
- **Exit / holding period:** none specified beyond weekly re-signalling; weights are held constant until the next Friday rebalance, with daily P&L accrual. No stop, no take-profit, no delisting/liquidation rule (`data gap` for forced exits).
- **Parameters** (`results/goldman_style/parameters.csv`): `signal_lookback 252 trading days`, `signal_price close`, `rebalance weekly Friday signal then next trading day active`, `weighting cross-sectional centered rank dollar neutral`, `one_way_cost 5 bp`, `target_volatility disabled` (baseline). All are **fixed**, not tuned, as presented; the source reports no tuning procedure (`data gap`).
- **Target-volatility overlay** (separate strategy, `target_vol` rows): 10 % annualized target, **60**-trading-day realized-volatility lookback, **40**-observation minimum, **3.0×** leverage cap; costs are scaled with leverage (`out["cost"] = base_cost * leverage`, `run_backtest` post-processing). Same signal, same F3 leg.

**B. Liquidity-ranked extension** (`docs/methodology.md`, `src/liquidity_curve_data.py`, `src/liquidity_basis_momentum_factor.py`, `scripts/run_liquidity_extension.py::CONFIG`)

- **Eligibility screen** (`prepare_liquidity_candidates`, defaults): `close > 0` AND `amount ≥ 2000.0` AND `oi > 0` AND `maturity_days ≥ 30` where `maturity_days = delist_date − trade_date`. **Units of `amount` are not documented anywhere → `data gap`.**
- **Curve selection** (`select_liquidity_curve`): eligible contracts sorted by `(trade_date, fut_code, delist_date, ts_code)`; `liquidity_rank` = cumulative count → **L0 = nearest eligible, L1 = next, L2 = next after that** (the screen can remove the literal front contract).
- **Signal:** for `j ∈ {1, 2}`, `BM(L0-Lj) = Σ_{k=t−119}^{t} [log(1 + r(L0)_k) − log(1 + r(Lj)_k)]` — a **120**-trading-day rolling sum of daily log-return spreads (`rolling(window=120, min_periods=120)`), deliberately in log space "so daily return differences can be added across time without creating price jumps at contract switches" (source docstring).
- **Cross-sectional mapping:** identical centered-rank → dollar-neutral rule as A (`build_ranked_liquidity_basis_momentum` explicitly "reuse[s] the V0 ranking rule so experiment results differ only in the signal construction").
- **Day filter:** rebalance days additionally require `asset_count ≥ 10` (`minimum_assets: 10` in `CONFIG`, applied to the signal subset before weighting). Fridays failing the filter are not rebalance dates, so the previous book is simply held to the next qualifying Friday (source behaviour read from `run_backtest`).
- **Return leg:** **main-contract close-to-close proxy** — a single `main_contract` per product per day supplied by `tradable_universe(method='top2_volume_by_day')`. The source is explicit: "Main contracts may change during a holding period, so this is not a locked-contract execution simulation."
- **Blend:** `0.5 × (separate L0-L1 book) + 0.5 × (separate L0-L2 book)`, combined at the weekly **weight** level before the backtest, so "its gross return is exactly the half-and-half gross-return identity; costs can differ after position netting" (source).
- **Parameters** (`results/liquidity/parameters.csv`): `signal_lookback 120 trading days`, `rebalance weekly Friday signal then next trading day active`, `return_leg main-contract close-to-close proxy`, `one_way_cost 5 bp`, `minimum_assets 10`, `comparison_start 20190107`, `comparison_end 20260710`, `aligned_trading_days 1820`, `warm_up_history … the source run begins 20070101`.
- **Fully specified vs underspecified:** signal formula, lookback, rebalance day, execution delay, weight map, cost rate and eligibility screen are **fully specified and reconstructible from the published code**. Universe membership, `amount` units, price/session/timezone, contract-selection main-contract rule details, and any roll/exit handling are **underspecified** (`data gap`).

## Required data

- **Instrument:** listed delivery-month futures contracts on (unnamed) **commodity futures** products; per-contract `close` (price), `settle`, `vol`, `amount` (turnover), `oi` (open interest); contract reference `list_date`, `delist_date`; product-level `fut_code`, `exchange`, `category`, `main_contract`, `is_tradable`, `method`.
- **Market type:** futures (exchange-traded, daily settlement implied by the `settle` field). **No options, no spot, no perpetuals.**
- **Universe:** a "tradable commodity universe" keyed by `(trade_date, exchange, fut_code, method)` with `method = 'top2_volume_by_day'` and `is_tradable = 1`; product-level `category` exists (the code supports category-neutral and category-demeaned weighting, but the published runs use plain cross-sectional `rank` → **category is not used in the published strategies**). Number of products is **not stated** → `data gap` (Scout-derived mean names in the daily book: ~24 for the F0/F6 baseline, ~44–50 for the extension, ~44–49 for the blend; see *Negative evidence*).
- **Venue / geography:** **not stated in the source → `data gap`.** The schema shape (`ts_code`/`trade_date`/`settle`/`oi`, `top2_volume_by_day`) is consistent with a vendor-style daily futures database, but **the source never names an exchange, a country, or a data provider**, and the Scout will not infer one.
- **Timeframe:** daily bars (close-to-close), weekly rebalance decision on Friday.
- **Point-in-time:** the `tradable_universe.main_contract` and `is_tradable` fields are supplied by the dataset and **their construction (and whether they are free of forward-looking information) is not documented → `data gap`** and a required falsification target (F11).
- **Timestamp / timezone:** not stated anywhere → `data gap`.
- **Missing data:** contracts require `close IS NOT NULL AND close > 0`; missing prices are dropped (`dropna(subset=['price'])`, `price > 0`); imputation is not used in the published path. Suspended/halted-session handling is not documented → `data gap`.
- **Funding / fee / spread needs:** only a flat **5 bp one-way turnover cost** is modelled (see *Execution assumptions*). Commission, exchange/clearing fees, bid-ask spread, slippage, market impact, margin/financing, borrow, roll cost and capacity are **`data gap` — not observed, not modelled, and must not be read as zero**.
- **Reproducibility dependency:** a caller-supplied SQLite database matching `data/README.md` **and a data licence permitting use** are required to regenerate anything; neither is distributed.

## Execution assumptions

### Source-reported

- **Signal-to-order timing:** Friday close signal → **next trading day** entry; P&L accrues from that day onward on the held weights. No intraday timing, no VWAP/arrival-price specification, no explicit order type anywhere in the source.
- **Fill model:** **none stated.** Returns are applied to weights directly (`run_backtest` aligns `weight × return` per date) — i.e. an implicit same-day, complete-fill, zero-slippage assumption on the return leg. The source does **not** label this as a cost assumption; it is a modelling simplification the source leaves implicit.
- **Costs:** 5 bp one-way × `Σ|Δw|`, charged once on the first day after each rebalance (`run_backtest` lines 460-463). **No commission, no exchange/clearing fee, no bid-ask, no slippage, no market impact, no participation/ADV cap, no capacity limit, no margin/financing cost, no borrow cost, no roll cost, no integer-lot or limit-move handling** — all explicitly excluded in `docs/limitations.md` → `data gap`, never zero.
- **Leverage / margin:** baseline and liquidity books are gross-1.0, dollar-neutral (`long 0.5 / short 0.5`). The separate F0/F6 target-vol overlay may lever up to **3.0×** against a 10 % vol target. Margin requirements, margin calls and collateral financing are not modelled → `data gap`.
- **Shorting:** short futures legs are assumed freely available at the same cost as the long legs; no borrow/locate constraint is mentioned (nor would one normally exist for futures, but the source does not discuss it) → treated as `data gap` rather than verified.
- **Exit / failure handling:** no stop, no take-profit, no liquidation rule, no partial-fill or rejected-order handling, no latency model → all `data gap`.

### Research interpretation (Scout-labelled)

- Any choice to execute at next-day **open** vs next-day **close**, to charge a spread or a participation cap, to model margin financing, or to lock a delivery-month contract for the holding period is **`research-proposed`** — the source specifies none of them.
- The main-contract return proxy is the single largest execution assumption in this record: it silently permits a contract switch inside a holding period. Replacing it with locked-contract returns plus an explicit roll is **`research-proposed`** (F9).

## Evidence

### Source-reported

All figures below are read directly from the committed CSVs at pinned commit `6f0127f3…` and are **net of the 5 bp one-way turnover cost** (the summary metric function computes on `portfolio_return = gross_return − cost`, `src/goldman_basis_momentum_report.py` lines 51-91). Nothing here has been reproduced by the Scout.

**Headline tables (`results/**/summary.csv`)**

| Strategy | Window | Days | Total | Annual | Vol | Sharpe | MaxDD | Win | Calmar | VaR95 | Worst day |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Goldman-style F0/F6 baseline (unscaled) | 2008-01-21 → 2026-07-10 | 4,487 | 87.17 % | 3.5833 % | 5.4908 % | **0.6526** | −14.763 % | 52.44 % | 0.2427 | −0.5423 % | −1.7621 % |
| F0/F6 + 10 % target-vol overlay | 2008-01-21 → 2026-07-10 | 4,487 | 252.48 % | 7.3317 % | 10.3720 % | **0.7069** | −28.655 % | 52.44 % | 0.2559 | −1.0138 % | −3.9755 % |
| Liquidity L0-L1 | 2019-01-07 → 2026-07-10 | 1,820 | 36.45 % | 4.3977 % | 4.5629 % | **0.9638** | −4.833 % | 52.20 % | 0.9099 | −0.4249 % | −1.2609 % |
| Liquidity L0-L2 | 2019-01-07 → 2026-07-10 | 1,820 | 59.39 % | 6.6680 % | 5.3312 % | **1.2508** | −7.453 % | 53.02 % | 0.8947 | −0.4963 % | −1.7200 % |
| Liquidity 50/50 blend | 2019-01-07 → 2026-07-10 | 1,820 | 48.32 % | 5.6099 % | 4.6549 % | **1.2052** | −5.472 % | 52.91 % | 1.0253 | −0.4249 % | −1.4206 % |

Provenance for each row: `results/goldman_style/baseline/summary.csv`, `results/goldman_style/target_vol/summary.csv`, `results/liquidity/l0_l1/summary.csv`, `results/liquidity/l0_l2/summary.csv`, `results/liquidity/blend_50_50/summary.csv`, cross-checked in `results/liquidity/comparison_summary.csv`.

**Metric convention (important, source-read):** `sharpe = annual_return / annual_volatility` where `annual_return = (1 + total_return)^(252/N) − 1` (geometric) and `annual_volatility = std(daily) × √252`; **no risk-free rate is subtracted**. This is not the conventional excess-return arithmetic-mean Sharpe and is not directly comparable to Sharpe ratios reported elsewhere in this repository without adjustment.

**Predictive-link statistics (`results/liquidity/l0_l1/ic_summary.csv`, `…/l0_l2/ic_summary.csv`)**

- L0-L1: **358** weekly observations; mean **IC 0.0326** (std 0.1809, **IR 0.1802**, positive rate 56.70 %); mean **Rank IC 0.0351** (std 0.1772, IR 0.1979, 57.26 %).
- L0-L2: **358** weekly observations; mean **IC 0.0411** (std 0.2091, **IR 0.1964**, positive rate 56.98 %); mean **Rank IC 0.0419** (std 0.2033, IR 0.2059, 58.66 %).
- **No t-statistic, p-value, confidence interval or Newey-West correction is printed anywhere in the source** → statistical significance of the predictive link is a `data gap`.

**Calendar-year net returns of the F0/F6 baseline (`results/goldman_style/baseline/annual_performance.csv`)** — the source's own annual table also carries `total_turnover`, `total_cost`, `average_daily_cost`, `annualized_cost` columns:

2008 +5.40 %, 2009 +2.58 %, 2010 +3.17 %, **2011 −2.15 %**, 2012 +7.23 %, 2013 +15.96 %, 2014 +10.63 %, 2015 +6.62 %, 2016 +5.91 %, 2017 +8.09 %, 2018 +3.80 %, **2019 −5.69 %**, 2020 +4.44 %, **2021 −6.85 %**, 2022 +0.90 %, 2023 +1.14 %, 2024 +0.90 %, 2025 +3.15 %, 2026 (to 07-10) +0.70 %. Annualized cost in that table is ≈0.46–0.64 % per year (e.g. 2015 `total_turnover 11.7427`, `total_cost 0.0059`).

**Calendar-year net returns of the L0-L2 book (`results/liquidity/l0_l2/annual_performance.csv`)**

2019 +1.92 % (Sharpe 0.3602), **2020 +21.55 % (Sharpe 3.1662)**, 2021 +3.00 % (0.5519), 2022 +9.70 % (2.0580), 2023 +4.88 % (1.2815), 2024 +3.14 % (0.6711), 2025 +1.94 % (0.4806), 2026 (to 07-10) +3.28 % (1.1092).

**Source-stated scope facts:** repository description and `docs/index.html` ("Goldman-style F0/F6 replication and a liquidity-ranked L0-L1 / L0-L2 extension … 5 bp one-way cost"); `README.md` alignment statement; CI green-path definition in `.github/workflows/tests.yml`.

### Independently reproduced

not independently reproduced

### Negative evidence

1. **The replicated baseline does not work in the extension's own window (Scout-derived from the source's committed daily CSVs; the source does not publish this slice).** Restricting `results/goldman_style/baseline/daily_performance_with_drawdown.csv` to the extension's exact display window 2019-01-07 → 2026-07-10 gives **net annual −0.14 %, net Sharpe −0.03** (gross +0.39 %, gross Sharpe 0.08); the target-vol overlay over the same dates gives **net annual −0.54 %, net Sharpe −0.05**. The headline L0-L1/L0-L2 Sharpes of 0.96/1.25 are therefore **not** a property of "basis momentum in this window" — the F0/F6 replication is flat-to-negative there while the liquidity-ranked construction is positive. Either the construction or the display window (or both) is doing the work.
2. **Extreme single-year concentration in the headline book.** L0-L2's 59.39 % cumulative over 2019-2026 includes **+21.55 % in 2020 alone (Sharpe 3.17)**; 2019, 2021, 2024 and 2025 each returned ≤ 3.14 % with Sharpe ≤ 0.67, and 2025 returned +1.94 % (Sharpe 0.48). Removing 2020 removes more than a third of the cumulative result.
3. **The baseline has already decayed.** Its own annual table shows +0.90 %, +1.14 %, +0.90 %, +3.15 % for 2022-2025 versus 6-16 % through 2013-2018, with negative years in 2011, 2019 and 2021. Full-period net Sharpe 0.65 over 4,487 days with a −14.76 % max drawdown.
4. **Weak predictive link, no inference.** Mean weekly IC 0.033-0.041 with IR ≈ 0.18-0.21 over 358 observations and **no printed t-statistic, p-value, or multiple-testing control**. The source prints no benchmark whatsoever — no passive long-short commodity book, no conventional price momentum, no carry, no index — so **outperformance is untestable from the repository**.
5. **Costs are modelled at 5 bp one-way and nothing else.** Scout-derived from the committed daily files: total summed cost 5.28 % (L0-L1), 5.85 % (L0-L2), 5.10 % (blend), 9.80 % (baseline) of one unit of notional across the windows ≈ **0.73 %, 0.81 %, 0.71 %, 0.55 % per year**; average `turnover` on rebalance days 0.295 / 0.327 / 0.285 / 0.225 with 358 (liquidity) / 870 (baseline) rebalance days. Gross-vs-net (also Scout-derived): L0-L2 gross 7.54 % / Sharpe 1.414 vs net 6.67 % / 1.251; L0-L1 gross 5.16 % / 1.133 vs net 4.40 % / 0.964; blend gross 6.36 % / 1.367 vs net 5.61 % / 1.205; baseline gross 4.15 % / 0.757 vs net 3.58 % / 0.653. **Commission, exchange fees, spread, slippage, impact, margin financing, capacity and roll costs are all absent**, so even the "net" figures are net of one modelled friction only.
6. **Return-leg realism gap.** The extension's P&L is a **main-contract close-to-close proxy** that "may change contract during a holding period" (source). No locked-contract, no roll execution, no tick/limit-move handling. The baseline's own P&L leg is F3 while its signal uses F0/F6 — a maturity mismatch the source does not justify.
7. **No out-of-sample discipline.** There is no train/test split, no walk-forward, no parameter-sensitivity table, no placebo or shuffled-signal test, and no deflated/multiple-testing correction. The display window (2019-01-07 onward) is chosen by the source **without stated justification**, while warm-up history begins 2007-01-01 — window selection is an undisclosed degree of freedom (the source itself concedes "Aligned dates make strategies comparable but do not eliminate model-selection risk").
8. **Not publicly reproducible.** Raw quotes, the SQLite database and the "implementation report" referenced by `docs/results.md` are all withheld. `src/goldman_basis_momentum_factor.py` still carries stale module defaults pointing at `outputs/contract_curve_full_20110101_20220228.csv`, i.e. the published window is produced by the wrapper scripts, not by the module defaults — a foot-gun for anyone re-running.
9. **Source quality / status.** Unreviewed personal GitHub repository, **0 stars / 0 forks**, four squashed commits, no named author, no paper, no peer review, no benchmark, no disclosure of how many candidate signals were tried before the retained ones ("retained" and "excluded" families are described but not enumerated) → publication-bias and selection risk are unquantified.
10. **The source's own caveats (recorded verbatim in substance):** not an exact Bloomberg index replication; licensed data excluded; L0-L1/L0-L2 is "a research proxy … not a locked-contract execution simulation"; "The L0-L2 eligibility condition can reduce the cross section"; inverse-vol weighting, capacity, ADV/OI limits, category constraints, integer lots, margin, limit moves and roll execution are out of scope; "Historical performance is not evidence of future performance".
11. **Contrary evidence from this repository's other records (different sources, retained for the record):** `g10-fx-carry-fx-value-energy-roll-yield-net-cost-audit-2026-09-23.md` **refutes** energy basis-momentum at 10 bp (Sharpe −0.06, pre-2010 positive / post-2010 negative); `commodity-seasonal-dvr-ssa-rlssa-benchmark-null-2026-09-14.md` finds no robust commodity seasonal benchmark outperformance after Holm adjustment; `published-equity-anomaly-zoo-large-cap-post-2005-luck-adjusted-null-arxiv-2607.06502-2026-09-23.md` and `crypto-cross-sectional-intraday-alpha-perpetual-futures-cost-rejection-2026-09-14.md` document how quickly similar published signals fail once costs and point-in-time discipline are applied. None of these are the same source; they are included as *reasons for scepticism*, not as direct tests of this strategy.

## Falsification plan

Every threshold below is a **`research-defined falsification threshold`** and every operationalisation the source does not itself specify is **`research-proposed`**. Data assumed: a point-in-time version of the same contract-level futures history plus an independent price vendor for cross-checking.

- **F1 — Frozen forward window.** Re-run L0-L1, L0-L2 and the blend on all data after the source's last date (2026-07-11 onward), untouched, for ≥ 12 months. *Metric:* net Sharpe under the 5 bp model **and** under a 20 bp all-in ladder. *Fail:* forward net Sharpe < 0.50 at 5 bp, or < 0 at 20 bp. *Action:* mark the mechanism unsupported and do not advance.
- **F2 — Subperiod stability.** Split 2007-2026 into non-overlapping 3-year windows (out-of-sample-only). *Fail:* fewer than 2/3 of windows have positive net Sharpe, or the sign of the pooled result is driven by one window. *Action:* downgrade to a regime-dependent anomaly.
- **F3 — Benchmark/control.** Compare against (i) an equal-weight long-short commodity-futures book, (ii) conventional 12-1 price momentum, (iii) a static carry/roll-yield book, over identical dates and the same cost model. *Fail:* the extension's **net** alpha is ≤ 0 versus any one of them. *Action:* mechanism collapses to "beta to a known commodity factor".
- **F4 — Cost ladder / break-even.** 5 / 10 / 20 / 50 bp one-way **plus** commission + exchange/clearing fee + spread + a 10 %-of-ADV participation cap. *Fail:* break-even all-in cost < 10 bp one-way (i.e. the book dies at realistic all-in friction). *Action:* reject as untradeable at any plausible size.
- **F5 — Signal placebo.** 1,000 draws of (a) weekly sign-shuffled BM signals and (b) randomly assigned maturity pairs (L0 vs a randomly chosen eligible far contract), same weighting engine, same dates. *Fail:* the real book's net Sharpe is not above the 95th percentile of the placebo distribution. *Action:* reject as a weighting-engine artifact.
- **F6 — Parameter grid.** Lookback ∈ {60, 90, 120, 180, 252} × `minimum_assets` ∈ {5, 10, 15} × `amount` threshold ∈ {1000, 2000, 4000} × maturity floor ∈ {15, 30, 60} days. *Fail:* fewer than 60 % of grid cells have positive net Sharpe, **or** the published cell sits in the top decile of the grid (headline = lucky cell). *Action:* treat the published number as overfit.
- **F7 — Window-selection audit.** Re-run the liquidity strategies over the **full** 2007/2008-2026 span (warm-up respected) rather than only 2019-01-07 onward, and report the 2019 start's rank among all candidate start dates. *Fail:* full-period net Sharpe < 0.5 × the published 1.251, or 2019-01-07 is shown to be a chosen optimum. *Action:* flag window selection as the likely source of the effect.
- **F8 — Single-year removal.** Recompute net Sharpe excluding 2020 (and, in turn, each other single year). *Fail:* pooled net Sharpe < 0.5 excluding 2020, **or** excluding any single year pushes it below 0.40. *Action:* reclassify as a crisis-episode effect.
- **F9 — Execution realism.** Replace the main-contract proxy with **locked-contract** returns, roll explicitly at expiry with observed spread + slippage, charge commission, and model one day of latency. *Fail:* net Sharpe drops by > 30 % relative, or changes sign. *Action:* the reported performance is a data artifact.
- **F10 — Predictive-link inference.** Compute weekly ICs with Newey-West (lag ≥ lookback/5) t-statistics and a Benjamini-Hochberg correction over the whole tested family. *Fail:* L0-L2 rank-IC t < 2.0 after correction, or BH q ≥ 0.10. *Action:* no evidence of a forward link; stop.
- **F11 — Point-in-time / universe audit.** Rebuild `tradable_universe(is_tradable, method, main_contract)` from raw listing/volume history with no forward-looking information (no backfilled contract lists, no post-hoc tradability flags). *Fail:* any surviving product or any main-contract switch uses information not available at the decision time. *Action:* invalidate the whole backtest until re-run point-in-time.
- **F12 — Selection / multiplicity.** Obtain from the author, or reconstruct, the number of candidate signals and windows tried before the retained families (the repo mentions "retained" and "excluded" families without enumerating them); apply a Deflated Sharpe Ratio correction. *Fail:* DSR < 0.95 for the headline L0-L2 cell, or the number of trials is undisclosed and cannot be bounded. *Action:* treat the headline Sharpe as an order statistic.

*Common action on any fail:* the record stays `research-only` and is proposed to Research Intake Review as `REJECT`/`REMEDIATE`; no Qlib backtest, no Paper/Testnet/Live staging.

## Crypto portability

**`unproven`.**

- The source contains **zero crypto evidence** — it never names its own market, and nothing in it discusses spot, perpetuals, funding, mark/index price or any crypto venue. Labelling it `direct` or `adapted` would be unsupported.
- **Why a port is plausible in shape only:** crypto does have dated futures (quarterly / bi-quarterly) on a handful of underlyings, so a maturity-ranked curve and an L0-vs-L1 spread can be written down mechanically.
- **Why the mechanism likely breaks (research-proposed risk list):** (i) crypto dated curves usually have **only 1-4 live maturities**, so F6 does not exist and L2 is frequently absent — the cross-section collapses from ~44-50 names to a handful; (ii) **24/7 sessions** destroy the Friday-signal/next-session convention and the daily candle boundary; (iii) **funding on perpetuals** is an additional, dominant carry term absent from commodity curves; (iv) **venue fragmentation** (each exchange has its own curve, no single `tradable_universe`), plus listing/survivorship as contracts get delisted in short cycles; (v) **liquidation cascades and price limits** alter the near contract's behaviour precisely during stress, when the signal is largest; (vi) no physical-delivery convergence anchor exists for a coin-settled quarterly on most venues, so the "deferred contract" leg behaves differently; (vii) stablecoin/quote-currency and custody/withdrawal risk are unpriced.
- Any crypto deployment of this construction would be a **new hypothesis requiring its own point-in-time test**, not an extension of this source.

## Limitations

- **`data gap` — venue, geography, exchange, product list and product count of the universe are never stated.** The record deliberately does not infer a market from the database schema.
- **`data gap` — authorship.** No named author, affiliation, contact, DOI, paper or peer review; only a GitHub account and "Basis Momentum contributors".
- **`data gap` — units of `amount` in the eligibility screen** (`amount ≥ 2000`), and the exact `top2_volume_by_day` main-contract rule.
- **`data gap` — timezone, session calendar, price/session convention, tick size, and how a non-trading Friday is handled.**
- **`data gap` — all costs except a flat 5 bp one-way turnover charge**: commission, exchange/clearing fees, bid-ask, slippage, market impact, participation/capacity, margin/financing, roll cost, integer lots, limit-move rejection, latency, partial fills.
- **`data gap` — no benchmark, no inference, no out-of-sample split, no parameter sensitivity, no placebo, no multiple-testing control, no turnover/cost columns in the liquidity annual tables, no enumeration of signals tried.**
- **`data gap` — the referenced "implementation report" is not in the repository**, so the private-database → committed-CSV transformation is unauditable.
- **`underspecified` — the economic mechanism**: the source states none; everything in *Economic mechanism → Research interpretation* is Scout-generated.
- **`underspecified` — "Goldman-style"**: no citation, index name or methodology document identifies what is being replicated; the source only asserts it is "not an exact Bloomberg index replication".
- **`not independently reproduced`**: no result in this record has been re-run; only artifact-integrity (37/37 checksums) and summary-consistency checks were performed, which require the withheld database to go further.
- **Metric convention risk:** the source's Sharpe is geometric-annual-return ÷ annualized vol with no risk-free subtraction — not comparable to excess-return Sharpes without restating.
- **Selection risk:** the 2019-01-07 display start is unjustified by the source, the retained/excluded experiment families are not enumerated, and the repo is an unreviewed zero-star personal repository.
- **Provenance risk:** history was squashed to four commits at publication; there is no pre-publication record of the results.

## Implementation status

`implementation_status: not-implemented`.

No part of this strategy exists in our research stack. Nothing has been coded, no Qlib full backtest has been run, no production card exists, and no Paper, Testnet or Live staging has been attempted or approved. The only code that exists is the third-party repository itself, pinned above; the Scout did not modify, run, or fork it (the wrapper scripts require a licensed SQLite database that is not distributed).

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

The presence of this record means only that a public source was located, read at Methods level, checksummed, deduplicated and normalized. It does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, Paper, Testnet or Live trading. A push to this repository is a staging event only.

## Related Wiki records

Wiki Brain was read **read-only** this run (`kb_search` × 3 — one returned 0 hits, one returned 6 hits, one returned 10 hits — plus `kb_read` × 2 on the canonical spec, `strategy-research-record-spec-v1` resolved as canonical and `v2` returning file-not-found). No Wiki Brain write, no Kanban task, no backtest.

- [[quant/futures-quad-trend-carry-skew-vov-composite-2026-09-11]] — adjacent futures multi-alpha composite (trend/carry/skew/vol-of-vol); different source and signal family, useful as the "known futures premia" control family for F3.
- [[quant/commodity-futures-hierarchical-graph-learning-calendar-spread-2026-09-02]] — the closest mechanism neighbour (futures calendar/curve structure), different source and an ML estimator.
- [[quant/cwt-wavelet-bandpass-mean-reversion-hmm-stress-overlay-2026-09-12]] — commodity-futures mean-reversion + stress overlay; different source and horizon.
- [[quant/crypto-adjacent-futures-weekly-basis-return-reversal-2026-09-03]] — weekly basis-return reversal on crypto adjacent futures; different source, market and reversal-vs-continuation direction.
- [[quant/forecast-to-fill-gold-futures-friction-adjusted-kelly-alpha-2026-09-02]] — friction-adjusted gold futures execution record; useful precedent for the cost/fill discipline F4/F9 demand.

Query `futures carry roll yield curve contango backwardation cross-sectional` returned **0** Wiki pages → no carry/roll page exists to link; none was fabricated. Repository filename neighbours cited in *Provenance* are plain filenames (read for dedup only), **not** Wiki links, and were not written or modified this run.

## Sources

1. `https://github.com/ddxmy/Basis-Momentum` — repository landing page; description "Goldman-style basis momentum replication and liquidity-ranked commodity futures extensions"; MIT; created 2026-07-08.
2. `https://github.com/ddxmy/Basis-Momentum/tree/6f0127f3f0513261297c650361c432adb01cc080` — pinned tree read 2026-09-26. Files used: `README.md`; `docs/methodology.md`; `docs/results.md`; `docs/limitations.md`; `docs/provenance.html`; `docs/index.html`; `data/README.md`; `data/schema.sql`; `notebooks/methodology_and_results.ipynb`; `src/goldman_basis_momentum_factor.py`; `src/goldman_basis_momentum_backtest.py`; `src/goldman_basis_momentum_report.py`; `src/liquidity_curve_data.py`; `src/liquidity_basis_momentum_factor.py`; `src/liquidity_basis_momentum_combination.py`; `scripts/run_goldman_style.py`; `scripts/run_liquidity_extension.py`; `results/checksums.sha256`; `results/goldman_style/{baseline,target_vol}/{summary,annual_performance}.csv` + `results/goldman_style/parameters.csv`; `results/liquidity/{l0_l1,l0_l2,blend_50_50}/{summary,annual_performance,ic_summary}.csv` + `results/liquidity/comparison_summary.csv` + `results/liquidity/parameters.csv`; `results/*/daily_performance_with_drawdown.csv`; `.github/workflows/tests.yml`; `LICENSE`.
3. `https://api.github.com/repos/ddxmy/Basis-Momentum`, `.../branches`, `.../tags`, `.../commits?per_page=5`, `https://api.github.com/users/ddxmy` — repository/branch/tag/commit metadata, read 2026-09-26 (branch `main` = `6f0127f3f0513261297c650361c432adb01cc080`, no tags).
4. `https://codeload.github.com/ddxmy/Basis-Momentum/tar.gz/6f0127f3f0513261297c650361c432adb01cc080` — source tarball (5,276,418 bytes) fetched 2026-09-26 and checked against `results/checksums.sha256` (37/37 OK).
5. `https://ddxmy.github.io/Basis-Momentum/` — static documentation site generated from the same `docs/` content (no distinct claims).
6. Context-only, **no number taken from them**: Boons & Porras Prado, *Basis-Momentum*, Journal of Finance 74(1) 239-279 (2019), DOI 10.1111/jofi.12740 — cited by other records in this repository and used only as Scout-side mechanism context.
