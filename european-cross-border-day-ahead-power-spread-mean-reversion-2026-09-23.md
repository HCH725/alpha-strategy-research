---
schema: strategy-research-record-v1
title: Cross-Border Day-Ahead Power Spread Mean Reversion with Hysteresis (DE/LU vs Six Neighbour Zones)
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - electricity
  - day-ahead-market
  - mean-reversion
  - cross-border-spread
  - github-source
status: research-only
confidence: medium
source_as_of: 2026-05-21
sources:
  - "https://github.com/CodingxFaisal/power-spread-trader (pinned commit c8205b932c085ab0469a6f86594a6d5a6774c058)"
  - "https://raw.githubusercontent.com/CodingxFaisal/power-spread-trader/c8205b932c085ab0469a6f86594a6d5a6774c058/README.md"
  - "https://www.smard.de/en/downloadcenter/download-market-data/ (day-ahead price data provenance, data window 2021-01-01 → 2024-12-31)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Border Day-Ahead Power Spread Mean Reversion with Hysteresis (DE/LU vs Six Neighbour Zones)

## Provenance

- **Source type:** public GitHub research repository (single-author, self-published; grey literature — no paper, no peer review).
- **Repository URL:** https://github.com/CodingxFaisal/power-spread-trader
- **Full commit SHA (pinned, = `main` HEAD at capture):** `c8205b932c085ab0469a6f86594a6d5a6774c058` (commit author date 2026-05-21T08:15:00Z, message "Correct instrument count in README (seven, not ten)"; repo `pushed_at` 2026-07-28T10:50:18Z). Prior commits at capture: `dd2e942f73c20b24ff15d50021582004570cc123` (2026-05-20), `510b0fb2e83c9e93b6db96a60e84f35b2865ac34` (2026-05-14).
- **Exact paths used (all read at the pinned SHA):** `README.md`, `config/strategy.yaml`, `src/spreadtrader/signals.py`, `src/spreadtrader/backtest.py`, `src/spreadtrader/config.py`, `src/spreadtrader/metrics.py`, `src/spreadtrader/data/smard_prices.py`, `scripts/run_robustness.py`, `scripts/run_cost_sensitivity.py`, `scripts/download_prices.py`, `results/portfolio_metrics.csv`, `results/per_instrument_oos_metrics.csv`, `results/cost_sensitivity.csv`, `results/param_heatmap.csv`.
- **Author (exactly as source):** Mohammad Faisal, M.Sc. Power Engineering (Renewable Energy) — GitHub `CodingxFaisal` (README §Author). No other authors stated.
- **License:** MIT (LICENSE at pinned SHA). Data belongs to SMARD.de / Bundesnetzagentur, used under its terms (README §License).
- **Repository metadata (GitHub API, read 2026-09-23):** created 2026-07-28T09:04:22Z, default branch `main`, 0 stars, 0 forks, 3 commits, MIT. **Provenance quirk / `data gap`:** all three commit author dates (2026-05-14 → 2026-05-21) precede the repository's `created_at` (2026-07-28), so the history was evidently imported or re-created; the commit graph itself is intact and pinned above.
- **Source as-of:** pinned HEAD commit 2026-05-21 (repo last pushed 2026-07-28); README states "Project developed May 2026". **Data as-of:** day-ahead prices 2021-01-01 → 2025-01-01 exclusive (`config/strategy.yaml` `data.start`/`data.end`), i.e. through 2024-12-31.
- **Primary-source checksum (performed 2026-09-23):** opened the repository at the pinned SHA and read the files above in full (code + config + all committed result CSVs). SHA-256 of the pinned bytes: `README.md` = `4628ad0a43ba052b7886d7bcd982e9045f4e3ad95a4c0fbe120763de109a810d` (10,221 bytes); `config/strategy.yaml` = `e6721085c47404cb23c0b0193f228cea3f852ea05b33239f2bf2f2a9658d4370` (1,643 bytes); `src/spreadtrader/signals.py` = `c5b8cdc684a3696ab9986736ee118b2728f133263eabb000f66096bc17069d86`; `src/spreadtrader/backtest.py` = `d85711f16db0abd2c45a0370fc9ced00fb2a33a3ce413d42d5130328e43b9a41`; `src/spreadtrader/metrics.py` = `7462e13542355d563ce3d72e9459d3a4c3200be642990f687f70c11be7053d7e`. Author list, commit version/date, sample window, universe, cost treatment and every number below were verified **inside those pinned files**, not from any summary.
- **Whole-repository source-identity deduplication (before writing, 2026-09-23):** ripgrep across **all 903 `*.md` records plus `coverage_manifest.csv`** for `CodingxFaisal`, `power-spread-trader`, `SMARD`, `DE_LU`, `DK1`, "cross-border day-ahead", "transmission capacity", "power spread", "transmission rights" → **0 hits** (an earlier `FTR`/`PTR` substring scan returned only unrelated inside-word matches). Identity probes against the built index (921 arXiv IDs, 1,137 DOIs, 3,289 URLs): repository URL, author handle and `smard.de` all absent. Adjacent electricity records are different source identities and different market stages: `electricity-spread-thief-forecast-reconciliation-bess-arbitrage-2026-09-22.md` (Lipiecki, Kourentzes & Weron, arXiv:2609.23223 — temporal-hierarchy forecast reconciliation for battery arbitrage) and `orderfusion-plus-intraday-electricity-buy-sell-price-trajectory-orderbook-dynamic-mask-2026-09-22.md` (Yu & Bunn, arXiv:2609.23598 — orderbook trajectory forecasting in the continuous intraday market). Materially distinct on source identity, mechanism (z-score fade of cross-border spreads vs. forecast reconciliation vs. orderbook deep learning), market stage (day-ahead daily position vs. day-ahead forecast accuracy vs. 15-minute continuous intraday) and signal construction.

## Economic mechanism

### Source-reported

The author frames the strategy as "deliberately simple … the point of the project is the evaluation around it" (README, opening). Stated rationale: the German (DE/LU) day-ahead price level and each DE-vs-neighbour cross-border spread exhibit short-lived, one-day mean reversion, so fading a large 20-day z-score deviation captures the next-day move; seven imperfectly correlated instruments lift the portfolio Sharpe above that of any single instrument ("Diversification across imperfectly correlated spreads is what lifts the portfolio Sharpe above the roughly 2.9 to 4.2 of any single instrument", README §The strategy). The author explicitly says the value "lives entirely in the next-day reversion, which is a known and fragile property of power spreads" (README §Is the signal real?) and, crucially, that the binding constraint is **tradability rather than transaction cost**: cross-border capacity is auctioned (FTR/PTR), the daily position economically is a spread swap/CfD with a wide bid-ask, the day-ahead auction clears only once (no round-trip inside it), and "Persistence is itself evidence of friction" (README §So why is this not a money printer?).

### Research interpretation

Falsifiable mechanism statement: **day-ahead price levels and cross-zone price differentials revert toward their trailing 20-day mean over a one-day horizon**, driven by (i) persistence/reversal of weather- and demand-driven bidding in the day-ahead auction and (ii) re-convergence of cross-zone differentials as transmission constraints, fuel and carbon cost differentials reprice — a mean-reversion / friction-capture hypothesis, not a fundamental-information hypothesis. Component roles (hybrid structure preserved):

```text
Regime:        none — no regime filter, no volatility gate, no session filter (source has none)
Primary signal: fade the 20-day z-score of each instrument (hysteresis entry 1.5 / exit 0.5)
Confirmation:  none in the source
Risk / exit:   go flat when |z| < 0.5 (mean-reversion take-profit); no stop-loss,
               no max holding period, no drawdown control — this is a pure
               predictive rule, the source has no separate risk layer
Sizing:        |position| ≤ 1.0 (MWh notional) per instrument; portfolio = equal
               weight (mean) across the 7 instruments → 1/7 of notional each
```

Do not assume each of the seven legs contributes alpha: the outright DE/LU level leg and the six cross-border spreads are different bets (level reversion vs. spatial reversion) and the source reports materially different OOS Sharpes per leg (Evidence below); an ablation is part of the falsification plan.

## Signal

All of the following is **source-reported** from `config/strategy.yaml` + `src/spreadtrader/signals.py` + `src/spreadtrader/backtest.py` at the pinned SHA (not Scout-invented).

- **Instruments (7):** the outright DE/LU daily-baseload price level (`include_outright: true`) plus six spreads `DE_LU−FR`, `DE_LU−NL`, `DE_LU−BE`, `DE_LU−AT`, `DE_LU−CH`, `DE_LU−DK1`, each defined as `reference_zone − other_zone` (`build_instruments`).
- **Formation timestamp:** position for day *t* is decided at the close of day *t* from information through day *t* (`zscore` uses `rolling(lookback, min_periods=lookback)` on daily bars, Europe/Berlin calendar days); it becomes tradable for the *t → t+1* move. P&L is enforced with an explicit one-day shift: `gross_pnl[t] = position[t-1] * (level[t] − level[t-1])` (`run_backtest`), i.e. next-day execution in the daily-baseload book, no same-bar fill.
- **Lookback:** `lookback_days: 20` calendar days, trailing mean and trailing standard deviation (`ddof=1`), `min_periods = 20` (first 20 rows → NaN → flat), endpoints inclusive of day *t* and exclusive of anything after *t*; `std == 0` is mapped to NaN → flat.
- **Long entry:** `z < −1.5` → `position = +1.0`.
- **Short entry:** `z > +1.5` → `position = −1.0` (fade the overshoot).
- **Exit:** `|z| < 0.5` → `position = 0`.
- **Ties / dead zone:** all comparisons are strict (`z > entry`, `z < −entry`, `|z| < exit`); a z exactly equal to ±1.5 or 0.5 hits none of the three branches and **holds the previous position** (NaN → `ffill()`), with `fillna(0.0)` only before the first signal. This is source-specified by code.
- **Holding period:** until `|z|` falls back inside 0.5; **no maximum holding period, no stop-loss, no time-based exit, no re-entry cooldown** — `data gap` / `underspecified` (a persistently trending instrument can stay in a losing position indefinitely).
- **Overlap / rebalance:** positions are re-evaluated every calendar day; overlapping positions across instruments are allowed and simply averaged.
- **Parameters (all fixed, none tuned per the source's own text, all from `config/strategy.yaml`):** `start 2021-01-01`, `end 2025-01-01`, `zones [DE_LU, FR, NL, BE, AT, CH, DK1]`, `reference_zone DE_LU`, `include_outright true`, `lookback_days 20`, `entry_z 1.5`, `exit_z 0.5`, `max_position 1.0`, `oos_split_frac 0.50`, `trading_days_per_year 365`. Config validation requires `entry_z > exit_z` (`config.py __post_init__`).
- **Fully specified or underspecified:** the trading rule itself is **fully specified and reconstructible from code**. The estimation/tuning history of `20 / 1.5 / 0.5` is **`underspecified`**: `config/strategy.yaml` comments say the first half of the sample is "used to sanity-check the params", so in-sample parameter selection cannot be excluded; there is no committed pre-registration or tuning log.

## Required data

- **Instrument / universe:** day-ahead wholesale electricity prices (EUR/MWh) for bidding zones `DE_LU` (Germany/Luxembourg), `FR`, `NL`, `BE`, `AT`, `CH`, `DK1` — seven EPEX SPOT / Nord Pool zones coupled through market coupling (README §Data).
- **Venue / vendor:** SMARD.de, the German Bundesnetzagentur open-data platform, free chart-data API (`https://www.smard.de/app/chart_data`), no API key (`src/spreadtrader/data/smard_prices.py`). SMARD filter IDs are pinned in code: DE_LU 4169, FR 253, NL 254, BE 4996, AT 255, CH 257, DK1 4170 (plus unused PL 256, CZ 259, NO2 4997).
- **Market type:** day-ahead physical/power market, traded here as a daily-settled **financial** position (swap/CfD) — not a crypto, equity or futures instrument.
- **Timeframe:** hourly day-ahead series fetched in weekly JSON chunks, UTC epoch-milliseconds parsed to `Europe/Berlin` (so DST-length days resolve correctly), then **averaged to a daily baseload** bar (README §Data; `smard_prices.py`, `download_prices.py`).
- **Fields used:** one price field per zone per day. **No** volume, order book, transmission capacity, fuel/carbon price, weather, load, fuel spread, auction-allocated FTR/PTR, financing or borrow data is used — all of those are `data gap` in this source.
- **Window:** 2021-01-01 → 2025-01-01 exclusive (config), 1,460 daily portfolio rows reported in `results/portfolio_metrics.csv` (`full` = 1460 days ≈ 4 calendar years incl. leap 2024). **`data gap`:** the exact first/last dates of the assembled panel are only *printed* by `scripts/download_prices.py` at runtime and are not committed, and a 20-day warm-up would ordinarily remove 20 rows — the artifacts do not reconcile the 1,460-row count against the config window, so the effective sample boundaries are `underspecified`.
- **In-sample / out-of-sample split:** `oos_split_frac 0.50`; `split_date = index[int(len(idx) * 0.50)]`, `out_of_sample()` = `loc[split_date:]`, `in_sample()` = `loc[:split_date].iloc[:-1]` (`backtest.py`). 730 days each. **Exact split calendar date is `data gap`** (computed at runtime, never committed); from the 4-year window it is approximately 2023-01-01.
- **Point-in-time:** day-ahead prices are published by the market operator after each day's auction, so the day-*t* close value is available for a position earning *t → t+1*; no revision/look-ahead handling beyond the one-day shift is described → `underspecified` for revised/re-stated prices.
- **Missing data:** no null/stale/holiday handling is documented (`data gap`); `std == 0 → NaN → flat` and `dropna()` on the portfolio row are the only explicit missing-value rules in code.
- **Cost data needs:** a flat per-MWh turnover cost (see below). No observed spread series, no auction price for capacity, no borrow/short-fee data.

## Execution assumptions

**Modelled by the source (all source-reported):**

- **Signal-to-order:** position fixed at day *t* close, earns *t → t+1*; effectively next-day execution at the day-ahead clearing price level.
- **Cost model:** `cost[t] = |position[t] − position[t−1]| × cost_per_unit_turnover`, with `transaction_cost_eur_per_mwh: 0.30` + `slippage_eur_per_mwh: 0.20` = **0.50 EUR/MWh per unit of position change** (`config/strategy.yaml`, `config.py cost_per_unit_turnover`). The config comment states this "covers exchange fees, bid-ask half-spread and slippage" and is a "**liquid-execution** baseline".
- **Capacity / participation:** none — `max_position 1.0` MWh notional per instrument; equal-weight averaging across 7 instruments.
- **Fills:** perfect fills at the day-ahead clearing level, **zero market impact** (README §Assumptions: "No market impact, constant per-unit costs, perfect fills").
- **Settlement:** price-taker, cash settlement against the day-ahead clearing ("Price-taker, financial settlement", README §Assumptions).
- **Shorting:** the source assumes a spread can be sold (swap/CfD) with no borrow fee, margin, financing or counterparty treatment → `data gap`.
- **Sensitivity analysis:** `scripts/run_cost_sensitivity.py` sweeps a single round-trip friction from 0.0 to 18.0 EUR/MWh in 1.0 steps, moving the whole amount into `transaction_cost_eur_per_mwh` and zeroing slippage, re-measuring OOS Sharpe and annualized P&L (`results/cost_sensitivity.csv`).

**Explicitly NOT modelled by the source (stated in the README, not inferred by the Scout):**

- Cross-border transmission-capacity (FTR/PTR) auction cost — the item the author calls the main reason the backtest overstates realizable edge.
- Order-book/bid-ask dynamics, spread series, partial fills, queue position, latency, market impact at size.
- Intraday or hourly execution (daily baseload only); the day-ahead auction clears once, so no intra-auction round trip.
- Financing, margin, leverage, borrow fees, credit/settlement default.

Scout-added execution assumptions used later in this record are labeled `research-proposed` / `research-defined`.

## Evidence

### Source-reported

All figures below are **source-reported**, read from the pinned commit, **not independently reproduced**. Metric definitions are theirs: Sharpe = `mean/std(ddof=1) × sqrt(365)` on the daily P&L series with risk-free = 0; Sortino = `mean/std(negative days only, ddof=1) × sqrt(365)` (non-standard — downside deviation computed only over losing days, `metrics.py`); Calmar = annualized P&L ÷ |max drawdown|; hit rate = share of **active (non-zero) P&L) days** that are winners (`metrics.py`). P&L is per unit of notional (EUR per MWh of position) — see the unit-labeling caveat in Negative evidence.

**Headline portfolio metrics — `results/portfolio_metrics.csv` (rows `full` / `in_sample` / `out_of_sample`):**

| Segment | days | total P&L | annualized P&L | Sharpe | Sortino | max drawdown | Calmar | hit rate | avg daily turnover |
|---|---|---|---|---|---|---|---|---|---|
| full | 1460 | 4705.11 | 1176.28 | 4.9790 | 8.1909 | −100.58 | 11.6948 | 0.6026 | 1.1150 |
| in_sample | 730 | 2717.16 | 1358.58 | 4.8561 | 8.6142 | −80.47 | 16.8822 | 0.5776 | (n/a) |
| out_of_sample | 730 | 1987.96 | 993.98 | **5.4512** | 8.0056 | **−100.58** | 9.8824 | 0.6252 | (n/a) |

README's rounded headline ("Annualized Sharpe **5.45**, Sortino 8.01, Max drawdown −101, Calmar 9.9, Hit rate 62.5%, Break-even ≈16.6 EUR/MWh", all "out-of-sample and net of a 0.50 EUR/MWh round-trip cost") matches the `out_of_sample` row of the committed CSV.

**Per-instrument OOS Sharpes — `results/per_instrument_oos_metrics.csv` (730 days each):** `DE_LU-DK1` 4.1999, `DE_LU-FR` 4.0460, `DE_LU` 3.9470, `DE_LU-NL` 3.7127, `DE_LU-BE` 3.4937, `DE_LU-AT` 3.0874, `DE_LU-CH` 2.8716 → README's "roughly 2.9 to 4.2" ✓. Per-leg hit rates 0.5132–0.5496; per-leg max drawdowns −36.09 to −228.33.

**Cost sweep — `results/cost_sensitivity.csv` (OOS):** cost 0.0 → Sharpe 5.6056, annualized P&L 1024.80; 1.0 → 5.2955; 8.0 → 2.9981; 16.0 → 0.2180 / 38.51; 17.0 → −0.1307 / −23.13 (first non-positive). README reports break-even **≈16.6 EUR/MWh** (interpolated between the 16.0 and 17.0 rows) and notes this is "roughly twice the typical daily spread move"; `run_cost_sensitivity.py` prints "typical daily spread move is ~8-9 EUR/MWh". Cost-to-Sharpe slope is essentially linear, ≈ −0.35 Sharpe per +1 EUR/MWh (Scout-computed from the committed CSV — arithmetic, `research-proposed` framing only).

**Parameter plateau — `results/param_heatmap.csv`, *in-sample* Sharpe over lookback ∈ {10,15,20,30,40,60} × entry_z ∈ {1.0,1.25,1.5,2.0,2.5}:** min 2.4039 (lb 10, ez 2.5), max 6.5550 (lb 60, ez 1.0), deployed cell (lb 20, ez 1.5) = 4.8561 → README's "every combination … profitable in-sample (Sharpe roughly 2.4 to 6.6)". **This grid is in-sample only** (`run_robustness.param_heatmap` calls `res.in_sample()`); no committed OOS parameter grid exists.

**Lag decay (README table + `results/lag_decay.png`, no CSV):** execution lag 1 day → gross Sharpe 5.09; 2 days → 3.47; 3 days → 1.41; 5 days → −0.40. Code (`run_robustness.lag_decay`) computes `positions.shift(k) × level_diff` over the **full sample, gross** (no costs) — **not** the OOS window, and the README header just says "Gross Sharpe" → window ambiguity `data gap`.

**Surrogate / null test (README prose + stdout only):** shuffling each instrument's daily changes and re-running, 50 surrogates, OOS Sharpe −0.05 ± 0.62 against 5.45 on real data, "a separation of about 8.9 standard deviations". `run_robustness.null_test` (`n_surrogates=50, seed=0`) computes this but only **prints** it — **no committed CSV**, so the exact figures are traceable to the README prose only → `data gap` at artifact level.

**Validation claims (README §Is the signal real?):** (1) no look-ahead — the signal decays with execution delay; (2) not cherry-picked — whole parameter neighbourhood positive in-sample; (3) not a backtest artifact — edge dies on shuffled data. All three are the author's own tests, none re-executed by us.

### Independently reproduced

not independently reproduced.

We did not run `scripts/run_all.py`, did not download SMARD data, and did not recompute any metric in this run; `data/raw` and `data/processed` are git-ignored (not committed), so reproduction requires re-fetching the SMARD API at the pinned SHA.

### Negative evidence

**Source-reported (in the pinned README/config/code):**

1. **Tradability, not cost, is the binding constraint:** cross-border spread capture requires auctioned transmission capacity (FTR/PTR) whose value is already priced in; the daily position is a financial spread swap/CfD with a wide bid-ask; the day-ahead auction clears once so you cannot round-trip inside it; market impact assumed zero. The author's own conclusion: "There is a real, robust mean-reversion signal … Turning it into P&L is a transmission-rights and liquidity problem, not a signal problem."
2. **Persistence as a warning:** "A freely capturable Sharpe-5 effect would not survive four years. That it persists is a sign the frictions above are real."
3. **Short-lived signal:** gross Sharpe falls 5.09 → 3.47 → 1.41 → −0.40 at lags 1/2/3/5 days — value is entirely in the next-day move; a 3-day delay removes most of it.
4. **Cost fragility:** OOS Sharpe is already 0.22 at 16 EUR/MWh and negative at 17 EUR/MWh; the whole edge is ≈16.6 EUR/MWh of friction wide.
5. **Diversification dependence:** single-leg OOS Sharpes (2.87–4.20) are well below the 5.45 portfolio figure — the headline requires all seven legs.
6. **In-sample-only robustness grid:** the parameter plateau is measured in-sample while the same in-sample window is where the params were "sanity-checked" (`config/strategy.yaml` comment) → in-sample selection risk not excluded.
7. **No statistical inference anywhere:** no t-statistics, standard errors, confidence intervals, multiple-testing correction or deflation appear in the repository (`data gap`).
8. **Internal cost-model inconsistency:** README says "Tripling the assumed cost from the original 0.15 to 0.50", but `config/strategy.yaml` at the pinned SHA **and** at the first implementation commit `510b0fb2e83c9e93b6db96a60e84f35b2865ac34` both specify `0.30 + 0.20 = 0.50`. The "original 0.15" baseline is not traceable to any committed configuration → source-internal contradiction, recorded rather than repaired.
9. **Unit-labeling ambiguity:** `results/*.csv` columns are named `*_eur`, while `metrics.py` states "return is the daily P&L per unit of notional (EUR per MWh position)" and README reports max drawdown as "−101 EUR / MWh notional". The two labels are used interchangeably in the source.
10. **Single unreviewed personal repository** (0 stars, 0 forks, 3 commits, single author, no paper, commit dates predating repository creation) — no third-party scrutiny of any claim.

**Scout-identified (not in the source):**

11. **Single 50/50 chronological split, no walk-forward, no rolling OOS, no refit discipline** — one lucky two-year window cannot be distinguished from a regime effect on the committed artifacts alone.
12. **Regime concentration:** the 2021–2022 European energy crisis sits inside the *in-sample* half, where parameters were sanity-checked; the OOS half (≈2023–2024) is a calmer price-level regime, so the record does not show behaviour under extreme levels — and, symmetrically, does not show whether params fitted on crisis data decay in normal data beyond the one reported window.
13. **No capacity/impact/financing model at all**, and no treatment of shorting availability, margin or settlement risk for the financial position.
14. **Repository-adjacent contrary evidence in the wider literature** is *not* something we verified here; absence of a published critique is not evidence of none.

## Falsification plan

Every threshold below is **`research-defined`** (Scout-chosen, not from the source) unless marked `source-specified`. Data for all tests: SMARD hourly day-ahead prices for the seven zones, fetched at the pinned SHA. Action on failure: mark the hypothesis weakened/failed in this record and **do not** advance any implementation; data unavailable → record `not run`, never `pass`.

1. **Exact reproduction (gate).** Re-fetch SMARD and re-run `scripts/run_all.py` at the pinned SHA. *Fail* if OOS Sharpe differs from 5.4512 by more than ±0.5, or if the OOS row is not 730 days. `research-defined`.
2. **Frozen-config OOS extension.** Hold `20 / 1.5 / 0.5 / 1.0` frozen and run 2025-01-01 → latest available. *Fail* if OOS Sharpe ≤ 0 over ≥12 months. `research-defined`.
3. **Walk-forward without re-tuning.** Rolling 12-month non-overlapping evaluation windows, parameters never adjusted. *Fail* if the median rolling Sharpe ≤ 0. `research-defined`.
4. **Cost stress at the natural scale.** Re-run the cost sweep with round-trip friction = 8 EUR/MWh (≈ the typical daily spread move the source itself prints). *Fail (realizability claim)* if OOS Sharpe ≤ 1. `research-defined`.
5. **Transmission-rights netting (the source's own objection, made operational).** Subtract observed FTR/PTR auction clearing cost per MWh from the captured spread. *Fail* if net OOS P&L ≤ 0 at prevailing auction prices. Requires capacity-auction data **not present in the repo** → may legitimately be `not run`. `research-defined`.
6. **Placebo / surrogate replication.** Repeat `run_robustness.null_test` (n = 50, seed = 0), writing the CSV the source omits. *Fail* if the real OOS Sharpe is less than 3 σ above the surrogate mean. `research-defined`.
7. **Lag robustness on the OOS window.** Recompute lag-2 gross **and** net OOS Sharpe (the source reports lag decay on the full sample only). *Fail* if lag-2 OOS Sharpe ≤ 0 → the "next-day reversion" mechanism is unsupported. `research-defined`.
8. **Component ablation.** Run (a) outright DE/LU leg alone, (b) six spreads only. *Fail the cross-border claim* if spreads-only Sharpe ≤ 0 (the distinguishing claim is spatial, not level, reversion). `research-defined`.
9. **Aggregation-artifact test.** Re-run on hourly prices with intraday execution (the source's own listed extension). *Fail* if the edge exists only in the daily-baseload average → mark as aggregation artifact. `research-defined`.
10. **Anti-rescue rule.** No post-hoc retuning of `lookback/entry/exit` may be used to revive a failed test; a second, independently chosen parameter set may be tested only as a new predeclared hypothesis. `research-defined`.

## Crypto portability

**`unproven`.**

The source contains **zero** crypto evidence: its mechanism is anchored to a physical commodity market with a once-daily auction, weather/demand-driven price levels, and auctioned cross-border transmission capacity. None of those frictions exists in crypto, so the causal channel does not transfer as stated; at most the *statistical* shape (fade a trailing z-score of a cross-venue differential with hysteresis) is portable as a hypothesis.

Crypto-specific portability risks if someone ports it anyway (`research-proposed` framing only):

- **No daily auction / 24/7 sessions:** no single clearing price to mark a "daily baseload" against; timestamp and candle-boundary conventions become the whole signal, and the one-day-shift no-lookahead argument must be rebuilt per exchange.
- **Venue fragmentation:** the analog of a cross-border spread is a cross-exchange or spot–perpetual basis, fragmented across many venues with different listing/survivorship and no central coupling mechanism.
- **Funding vs. congestion:** perpetual funding replaces transmission constraints as the differential's driver; funding is paid/received on a schedule and can invert under crowding, unlike a congestion-driven power spread.
- **Mark / index price and contract specification:** basis strategies live or die on mark-vs-index definitions, maintenance margin and liquidation — none modelled in the source.
- **Liquidity/impact and capacity:** crypto perp depth is thin at size; the source's zero-impact assumption is even less defensible there.
- **Protocol/venue risk:** custody, withdrawal halts, de-pegged stablecoin quote currencies — risks with no analog in the source.

Crypto portability is not authorization to trade.

## Limitations

- `not independently reproduced` — every performance figure is the author's own committed output; we ran no code and downloaded no data.
- `underspecified`: parameter estimation history for 20 / 1.5 / 0.5 (config says the in-sample half was used to "sanity-check the params"); exact OOS split date; exact first/last panel dates; missing-data/holiday handling; price revision handling; maximum holding period / stop; margin, financing, borrow, counterparty risk.
- `data gap`: no statistical inference (no t/SE/CI/DSR) anywhere; no committed CSV for the surrogate-null or lag-decay results (PNG/prose only); lag-decay window (full-sample vs OOS) ambiguous in README; cost-sweep baseline "0.15" not traceable to any committed config; `*_eur` column names vs EUR-per-MWh metric definition; no capacity/auction-price data; no volume or order-book data; single author, unreviewed, 0 stars/forks, commit dates predating repo creation.
- `unproven`: that the pattern persists post-2024, that it survives transmission-rights costs, or that it transfers to any other asset class (including crypto).
- Regime: one market (EPEX/Nord Pool coupled zones), one 4-year window containing the 2021–2022 energy crisis in-sample; no cross-market replication.
- Source-quality: grey literature (personal GitHub repository), chosen because it is unusually self-critical and fully traceable — self-criticism is not peer review.
- Note on framing: the source itself argues the backtest **overstates** the realizable edge. This record must not be read as claiming a tradable Sharpe-5 strategy.

## Implementation status

`implementation_status: not-implemented`.

Nothing in our research stack has been implemented, backtested or executed for this record: no Qlib full backtest, no production card, no Paper, Testnet or Live run, and the upstream repository's scripts were not executed by us in this run (we only read its pinned files). This record does not modify any engine, create a strategy family, or authorize execution.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

Presence of this record in the staging repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool (`/results/_handoff/candidates.json`); completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet or live trading. No record may promote itself by wording, evidence count, confidence or schedule behaviour.

## Related Wiki records

Pre-write `kb_search` in Hermes Wiki Brain for "electricity day-ahead power spread mean reversion" returned **0 results**; "cross-border spread mean reversion futures basis" returned only the generic `quant/ssrn-3247865-151-trading-strategies-compendium-2026-08-26` compendium (not a strategy-identity match). **No stable Wiki Brain page for this mechanism is known, so no Wiki link is asserted.**

Adjacent records in this repository (same broad asset class, materially different source identity / market stage / mechanism — noted for reviewers, not claimed as duplicates):

- `electricity-spread-thief-forecast-reconciliation-bess-arbitrage-2026-09-22.md` — arXiv:2609.23223; temporal-hierarchy reconciliation of hourly price/spread forecasts for battery arbitrage (forecast-accuracy mechanism, day-ahead Germany/Spain).
- `orderfusion-plus-intraday-electricity-buy-sell-price-trajectory-orderbook-dynamic-mask-2026-09-22.md` — arXiv:2609.23598; orderbook deep learning for the continuous German intraday market.
- `commodity-soybean-crush-spread-cointegration-stat-arb-2026-09-12.md` and `crude-oil-crack-spread-seasonally-adjusted-mean-reversion-stop-lockout-2026-09-12.md` — spread mean-reversion relatives in different asset classes.

## Sources

1. Mohammad Faisal. *power-spread-trader — Backtest of a cross-border day-ahead spread mean-reversion strategy on European power prices, with honest out-of-sample and tradability analysis.* GitHub: https://github.com/CodingxFaisal/power-spread-trader ; pinned commit `c8205b932c085ab0469a6f86594a6d5a6774c058` (2026-05-21); primary file `README.md` at that commit, SHA-256 `4628ad0a43ba052b7886d7bcd982e9045f4e3ad95a4c0fbe120763de109a810d`, 10,221 bytes. MIT license. Read in full 2026-09-23.
2. Same repository, `config/strategy.yaml` at the pinned commit (zones, `lookback_days 20`, `entry_z 1.5`, `exit_z 0.5`, `max_position 1.0`, costs `0.30 + 0.20 EUR/MWh`, `oos_split_frac 0.50`, `trading_days_per_year 365`), SHA-256 `e6721085c47404cb23c0b0193f228cea3f852ea05b33239f2bf2f2a9658d4370`.
3. Same repository, `src/spreadtrader/signals.py` (SHA-256 `c5b8cdc684a3696ab9986736ee118b2728f133263eabb000f66096bc17069d86`), `src/spreadtrader/backtest.py` (SHA-256 `d85711f16db0abd2c45a0370fc9ced00fb2a33a3ce413d42d5130328e43b9a41`), `src/spreadtrader/config.py`, `src/spreadtrader/metrics.py` (SHA-256 `7462e13542355d563ce3d72e9459d3a4c3200be642990f687f70c11be7053d7e`) at the pinned commit — signal rule, P&L/cost accounting, IS/OOS split and metric definitions.
4. Same repository, committed results at the pinned commit: `results/portfolio_metrics.csv`, `results/per_instrument_oos_metrics.csv`, `results/cost_sensitivity.csv`, `results/param_heatmap.csv`, `results/lag_decay.png` — source of every performance number above.
5. Same repository, `scripts/run_robustness.py` (parameter grid, lag decay, surrogate null), `scripts/run_cost_sensitivity.py` (0–18 EUR/MWh sweep, break-even), `scripts/download_prices.py`, `src/spreadtrader/data/smard_prices.py` (SMARD zone filter IDs, UTC → Europe/Berlin) at the pinned commit.
6. SMARD.de (Bundesnetzagentur) Market data download centre: https://www.smard.de/en/downloadcenter/download-market-data/ — day-ahead price provenance (EPEX SPOT / Nord Pool zones), data window 2021-01-01 → 2024-12-31.
7. GitHub repository metadata for `CodingxFaisal/power-spread-trader` via the GitHub REST API (`created_at` 2026-07-28, `pushed_at` 2026-07-28, default branch `main`, MIT, 0 stars, 0 forks, 3 commits), read 2026-09-23 — provenance only, no strategy claim.
