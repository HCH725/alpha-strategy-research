---
schema: strategy-research-record-v1
title: "Retail Equity Anomaly Falsification under Point-in-Time Membership and Search-Aware Inference: PEAD, Long-Only Momentum/Reversal, Beaten-Down Mid-Cap Reversal, with a HAR Volatility Positive Control (When Equity Signals Disappear)"
created: 2026-09-27
updated: 2026-09-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equities
  - survivorship-bias
  - point-in-time-universe
  - falsification
  - volatility-forecasting
  - github-source
status: research-only
confidence: medium
source_as_of: 2026-07-22
sources:
  - "https://github.com/abhikoppulu-ai/Equity-Signal-Research at full commit 175d5691822fccfb8aeca85918099ab433b9b453 (main HEAD at read time), file README.md, 17,922 bytes, SHA-256 35449d6bcdf2d9d89ad4635155c6f1c512514f6ec3e7e871fde72ce3ed3395c0; commit date 2026-07-22T18:18:41-04:00, subject 'Switch all figures to high-contrast dark theme'"
  - "https://github.com/abhikoppulu-ai/Equity-Signal-Research/blob/175d5691822fccfb8aeca85918099ab433b9b453/research/results/pead_pit.json (6,099 bytes, SHA-256 84b3f49a1642aa936369bd6a13608f5c7f6bfff1905357307d313983b3822f3d) and research/results/vol_forecast_pit.json (7,037 bytes, SHA-256 da4aa3036b19cebff4bdefd601a2e2d97849415e11a7a94be7e62f46f3475a47), both re-hashed locally at the pinned commit on 2026-09-27"
  - "https://github.com/abhikoppulu-ai/Equity-Signal-Research/blob/175d5691822fccfb8aeca85918099ab433b9b453/ research notebooks 01-08 (research/01-pead-earnings-drift.md, 02-factor-reversal-and-self-correction.md, 03-midcap-out-of-sample-overfitting.md, 04-methodology-costs-and-deflated-sharpe.md, 05-volatility-forecasting.md, 08-statistical-upgrades.md), signal code (signals/pead.py, signals/factors.py, signals/midcap.py, signals/vol_forecast.py, signals/vol_targeting.py), docs (docs/universe-construction.md, docs/limitations.md, docs/pit-impact.md, docs/v4-changelog.md) and registration files (validation/prereg_bootstrap.json, validation/prereg_mcs.json, validation/prereg_reality_check.json, validation/criterion.json), all read at the pinned commit"
  - "https://api.github.com/repos/abhikoppulu-ai/Equity-Signal-Research (repository metadata read 2026-09-27: created_at 2026-07-21T15:36:55Z, pushed_at 2026-07-22T22:18:55Z, updated_at 2026-07-22T22:18:59Z, default_branch main, visibility public, stargazers_count 0, forks_count 0, open_issues_count 0, archived false, license.spdx_id NOASSERTION)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "README.md section 3.1 table states '0 of 33 statistics clear the 3.16 Sidak bar' for the PIT PEAD family, while research/01-pead-earnings-drift.md (same commit) states 'The single statistic in the whole family to clear the 3.16 bar is the 2022 positive-surprise leg (+1.19, t=3.47) ... one leg, one regime, out of 33 statistics'; research/results/pead_pit.json /subperiods_20d/periods/2022/pos_surprise_20d/t = 3.47 confirms the t-value exceeds 3.16, so both statements cannot be true of the same 33-statistic family; recorded unreconciled"
  - "README.md section 3.1 momentum row prints a single 'DSR 0.0013' against a row that carries two different estimates (-8.2% window-matched and -30.5% extended), while docs/v4-changelog.md, docs/pit-impact.md and research/04-methodology-costs-and-deflated-sharpe.md all pair DSR 0.0118/0.012 with the -8.2% window-matched figure and 0.0013 with the -30.5% extended figure (research/results/factors_raw_recompute_pit_windowmatched.json /MOM_HI_excess/dsr = 0.0118); recorded unreconciled"
  - "validation/criterion.json (registered kill-criterion config) declares costs as 'one_way_bps: 35' for the whole five-signal surface, while README.md section 2.2 and research/04-methodology-costs-and-deflated-sharpe.md describe 20 bps large-cap and 35 bps mid-cap as ROUND-TRIP charges and signals/midcap.py / signals/factors.py charge COST_BPS = 35.0 and COST = 0.20 (percent) respectively per holding period; both the one-way versus round-trip label and the uniform 35 versus 20/35 value disagree; recorded unreconciled"
  - "LICENSE file reads 'MIT License / Copyright (c) 2026 Abhinav Koppulu' and the README carries an MIT badge, while the GitHub API reports license.name 'Other' with license.spdx_id NOASSERTION; recorded unreconciled"
---

# Retail Equity Anomaly Falsification under Point-in-Time Membership and Search-Aware Inference: PEAD, Long-Only Momentum/Reversal, Beaten-Down Mid-Cap Reversal, with a HAR Volatility Positive Control (When Equity Signals Disappear)

## Provenance

- **Source type:** public GitHub repository containing code, committed machine-readable results and prose research notebooks. This is **not** a paper: no journal, no preprint server, no DOI, no peer-review statement exists anywhere in the repository, so **publication status = public code repository only, peer-review status `not stated in source`** (verified 2026-09-27 at the pinned commit).
- **Repository URL:** https://github.com/abhikoppulu-ai/Equity-Signal-Research
- **Full commit SHA (pinned, used for every citation in this record):** `175d5691822fccfb8aeca85918099ab433b9b453` - `main` HEAD at read time, commit date `2026-07-22 18:18:41 -0400` (= 2026-07-22T22:18:41Z), subject `Switch all figures to high-contrast dark theme`. Branch `main` is the default branch; 150 tracked files at that commit.
- **Author, exactly as source:** README header line prints the three fields `Abhinav Koppulu`, `Independent research`, `July 2026` (the source separates them with middle-dot characters, normalized to ASCII in this record); README section 9 `Independent research by **Abhinav Koppulu** (Finance and Supply Chain & Operations Management, Carlson School of Management, University of Minnesota), conducted 2025-2026`. No co-authors are listed anywhere.
- **Repository history:** first commit `64fab477269d689998b58a9c22ae7cd03912e1a3` (`2026-07-21 11:37:04 -0400`, `v4 baseline: imported from public v3 (abhikoppulu-ai/equity-signal-lab @ 3980869)`); README section 10 states V4 was imported from the public `abhikoppulu-ai/equity-signal-lab` V3 repository at commit `3980869` and extended with point-in-time universes, the 2013-2026 panel, rerun studies, registered statistical upgrades, executed notebooks and reproducibility gates.
- **GitHub API metadata (read 2026-09-27):** `created_at 2026-07-21T15:36:55Z`, `pushed_at 2026-07-22T22:18:55Z`, `visibility public`, `stargazers_count 0`, `forks_count 0`, `open_issues_count 0`, `archived false`, `size 11980` KiB, description: `A point-in-time, search-aware evaluation of retail-constrained equity anomalies: no tested return edge survives honest evaluation; volatility predictability replicates as the positive control. Fully reproducible.`
- **Version/date:** single frozen version = commit `175d5691...`; source data as-of 2026-07-22 (last push). Landing page, commit, README and result JSONs were all opened directly for this record; no secondary summary was used to fill any field.
- **Pinned-file integrity re-computed this run (2026-09-27, local clone at the pinned SHA):** `README.md` 17,922 bytes SHA-256 `35449d6bcdf2d9d89ad4635155c6f1c512514f6ec3e7e871fde72ce3ed3395c0`; `research/results/pead_pit.json` 6,099 bytes SHA-256 `84b3f49a1642aa936369bd6a13608f5c7f6bfff1905357307d313983b3822f3d`; `research/results/vol_forecast_pit.json` 7,037 bytes SHA-256 `da4aa3036b19cebff4bdefd601a2e2d97849415e11a7a94be7e62f46f3475a47`.
- **Transcription convention:** this record is ASCII-only. Where quoted source text contains Unicode punctuation (en dashes in ranges such as `26-36%`, middle dots in the README header line), it is transcribed with ASCII equivalents; **no numeric value, sign or unit was altered.**
- **Registration ordering checked, not assumed:** `git merge-base --is-ancestor 4d14c5c8edad82daf3cddc8f6a5dfd58ce02d9c4 9344cf2ac96d28ce5d4276f417fa19d923c7108d` returned success, i.e. the three method registrations (`validation/prereg_bootstrap.json`, `validation/prereg_mcs.json`, `validation/prereg_reality_check.json`, all `registered_utc 2026-07-21`) sit strictly before the results commit `9344cf2a` in branch history, exactly as `stats_upgrades.json /preregistration/note` asserts. `validation/criterion.json` registers `2026-07-20`, `registered_commit 4cf22f4`.
- **Toolchain stated by source:** Python 3.12 with committed `uv.lock`; `make setup` / `make test` / `make research` / `make compare`; CI runs Ruff, scoped mypy, pytest, an 85% coverage gate over the statistical core, a prose-number consistency check, and a weekly offline smoke workflow on fixture panels with the network downloader poisoned (README section 6).
- **Repository-wide source-identity deduplication (performed BEFORE writing, 2026-09-27):** `rg -uuu` across the entire repository hidden-inclusive (`.mimo-worktrees/`, `.agents/`, `.hermes/`, `.git`) for `abhikoppulu`, `Equity-Signal-Research`, `equity-signal-lab`, `When Equity Signals Disappear`, `Abhinav Koppulu`, `3980869`, `175d5691` returned **zero matches (rg exit 1)**; `coverage_manifest.csv` (5,808 lines) returned `0` for `abhikoppulu`, `0` for `Koppulu`, `0` for `Equity-Signal-Research`. `git log --oneline -20` was read only as a convenience glance and does not by itself satisfy dedup. Adjacent-phrase scans (`positive control`, `retail-constrained`, `point-in-time, search-aware`, `PEAD`, `survivorship`) hit only unrelated records listed under *Related Wiki records*, each with a different source identity.
- **Boundary:** this record was produced by a Research Scout. Nothing was written to Hermes Wiki Brain, `/results/_handoff/candidates.json`, Qlib, Paper, Testnet or Live.

## Economic mechanism

### Source-reported

The repository asks one narrow question (README section 1): *does any tested signal improve on the passive benchmark after the investable universe, execution rule, costs, holdout and the full research search are accounted for?* It evaluates four pre-specified claim families and attributes any surviving appearance of edge to three named distortions: universe construction (current-constituent lists silently condition on survival), return construction (market-model abnormal returns strip the beta a long-only account actually earns), and selection over the research space (best-of-N search with no trial-count deflation). The author's stated contribution is explicitly *not* a trading strategy but an auditable apparatus that separates survivorship bias, market exposure and selection artifact, with a volatility-forecasting experiment used as a positive control so that "the apparatus rejects everything" is itself falsifiable (README sections 1, 3.4, 4).

### Research interpretation

Falsifiable restatement of the four claims, with component roles kept separate (no component is assumed to contribute alpha):

- **H1 - PEAD (candidate alpha):** a scheduled earnings surprise produces delayed incorporation, so post-announcement abnormal return over a 5/20/60-session horizon should be predictable from the sign/magnitude of the initial earnings-announcement return. Mechanism class: information diffusion / post-event drift.
- **H2 - cross-sectional momentum/reversal long-only (candidate alpha):** cross-sectional price strength/weakness over 5/21/252-session windows should identify a long-only quintile book that beats SPY net of 20 bps. Mechanism class: cross-sectional continuation/reversal plus benchmark-relative beta.
- **H3 - beaten-down mid-cap reversal (candidate alpha):** the most price-beaten-down liquid S&P 400 names, gated by a short-term stabilizer, should revert enough over a 21-session hold to beat MDY net of 35 bps. Mechanism class: liquidity-provision / overreaction-reversal with a "falling knife" filter.
- **H4 - next-21-session volatility forecasting (positive control, not an alpha claim):** daily realized volatility has long memory, so a HAR-style forecast should beat persistence out of sample under a robust loss. Role of this component: it certifies that the shared pipeline can distinguish durable predictability from noise; it is the discriminator, not a return source.
- **Risk overlay (separate from alpha):** conditional volatility forecast -> exposure scaling on a single long-only asset. The source itself argues the economic mechanism is *exposure reduction*, not a newly discovered return source (README section 3.4), and reports the risk-matched hindsight controls needed to test that reading.

## Signal

Every rule below is `source-reported` from code and prose at the pinned commit; nothing operational in this section is invented by the Scout.

**Shared event-study harness (README section 2.2):** $AR_{i,t} = R_{i,t} - (\alpha_i + \beta_i R_{m,t})$ with $\alpha_i,\beta_i$ fitted on approximately 250 sessions ending **before** the event. Features at date *T* use information available through *T*; portfolios earn returns beginning at *T+1*. The return studies report abnormal returns for inference and raw benchmark-relative returns for investability.

**H1 - PEAD (`signals/pead.py`, `research/01-pead-earnings-drift.md`):**
- Formation timestamp: earnings date from the committed free earnings feed (`data/cache/earnings_dates.json`), aligned to the first session at/after that date (`pdata.align(d, "after")`); sample window `WINDOW_LO/WINDOW_HI = 2020-07-01 / 2026-04-01`.
- Lookback: market-model $\alpha,\beta$ on ~250 sessions ending before the announcement session.
- Entry: `entry = announcement_session + DRIFT_OFFSET` with `DRIFT_OFFSET = 2` sessions; drift measured over `HORIZONS = (5, 20, 60)` sessions from entry. The 2-session offset is the registered construction; offsets 1-5 are reported as an *exploratory* grid outside the registered family (research/01, "Parameter sensitivity").
- Ranking: events sorted by the announcement-period abnormal return `ear`; quintile means and the Q5-Q1 spread are computed within each horizon.
- Family and threshold (source-defined): 3 horizons x (positive-surprise leg, negative-surprise leg, five quintile means, Q5-Q1 spread) = 24 statistics, plus three subperiod blocks = **33 statistics**, family-wise 5% two-sided Sidak critical value **|t| = 3.16** (`pead_pit.json /multiple_testing`), explicitly to be treated as "search noise" below the bar. Inference is clustered by announcement date with date-clustered t-statistics and a stationary-bootstrap CI (`cluster_bootstrap_ci`).
- PIT variant: the event list is filtered to index members as of each announcement date (`membership(d, "sp500")`).
- Fully specified for reconstruction except: earnings-feed vendor identity, timezone/session calendar and tie handling between equal-`ear` events are **`underspecified` / `data gap`**.

**H2 - cross-sectional factors (`signals/factors.py`):**
- Four signals, all on closing prices at formation index `t_idx` (require `t_idx >= 260` and a finite close): `ret_5 = c[t]/c[t-5]-1`, `ret_21 = c[t]/c[t-21]-1`, `mom_252_21 = c[t-21]/c[t-252]-1`, `pct_off_high = 1 - c[t]/max(c[t-252..t])`, all in percent.
- Formation cadence: every `SAMPLE_STEP = 5` sessions; abnormal-return study horizons `HORIZONS = (5, 20)`.
- Windows: static run `START/END = 2021-01-01 / 2026-04-01`; PIT run `PIT_START = 2014-02-03` (binding constraint is the 252-session lookback, membership reliable from 2013-03-18), `PIT_MIN_OBS = 260`, cross-section restricted to S&P 500 members as of each formation date; per-regime subperiod blocks `pre_2020 / 2020_21 / 2022 / 2023_26`.
- Tradable construction (`run_raw_recompute`): long-only top- and bottom-quintile books per signal, `HOLD = 21` sessions, `COST = 0.20` (percent, round trip) per hold, benchmark = SPY raw return over the same hold, entry at `t_idx + 1`. The registered SPA/Reality-Check family is **8 long-only quintile legs** (4 signals x top/bottom, 21-day hold, net 20 bps) as monthly excess-vs-SPY series (`validation/prereg_reality_check.json`).
- Fully specified except: quintile tie-breaking, price-adjustment/vendor conventions and the benchmark's total-return vs price-return nature are **`data gap`**.

**H3 - mid-cap reversal (`signals/midcap.py`):**
- Universe: S&P 400 members as of each rebalance date (PIT reconstruction covers the S&P 400 only, ~400 names/day; the frozen v3 static blend was ~540 current S&P 400 + S&P 600 names - `midcap_pit.json /universe`).
- Screen per rebalance: require `t_idx >= 260`, a 252-session high, a finite 10-session return, and dollar volume `>= MIN_DOLLAR_VOL = 5e6`; **stabilizer** `ret10 > 0` (default `stabilize=True`); rank by distance below the 52-week high in **descending** order (most beaten-down first); need at least `top_n` candidates or the rebalance is skipped.
- Entry/exit: rebalance every `hold` sessions (`HOLD = 21` default), entry at `t_idx + 1`, equal-weight mean of the top `top_n = 15` forward returns, minus `COST_BPS = 35.0` (percent-per-hold as implemented by `strat.append(mean - cost/100 - bm)`), benchmark MDY over the same hold.
- Registered grid: `top_n in {15, 30, 50, 80}` x `hold in {21, 63}` = **8 configurations**, with $5M ADV floor (`validation/prereg_reality_check.json`); the "primary" cell is `(15, 21)` and is not double-counted.
- Windows: discovery/IS 2021-01-01 to 2024-01-01, forward OOS 2024-01-01 to 2026-03-01, backward OOS 2014-02-03 to 2020-01-01 (possible only under PIT data).
- Fully specified except: the dollar-volume lookback window inside `pdata.dollar_volume` and the ADV-window convention are **`data gap`** (not read for this record).

**H4 - volatility forecasting (`signals/vol_forecast.py`, `research/05-volatility-forecasting.md`):**
- Panel: pooled cross-section of names with `min_obs >= 1200` sessions; target = **next 21-session realized volatility**; features = Parkinson high-low variance aggregated to daily/weekly/monthly HAR terms; split `SPLIT = 2024-01-01`; training rows whose 21-session target window crosses the split are **purged** (`purge_train`).
- Models: `har` (level OLS), `har_log` (log-log OLS with a lognormal half-variance retransformation `exp(Xb + resid_var/2)`), `ewma`, `naive` (persistence), `train_mean` (per-name purged-train mean constant), `har_pername` (per-name level HAR, `min_obs 500`).
- Loss and tests: QLIKE in variance space, per-date mean across names; Diebold-Mariano on per-date mean loss differentials with Newey-West lag 21; Bonferroni gate `survives_correction` at `p < 0.01` for a family of 5 tests (`vol_forecast_pit.json /dm_multiple_testing`); Model Confidence Set with statistic `T_R` (range), elimination `argmax_i max_j t_ij`, stationary bootstrap mean block 21, `n_boot 10000`, `seed 20260721`, primary 90% level and secondary 75% level, membership re-run at blocks 10 and 42 (`validation/prereg_mcs.json`).
- Era robustness: refit per era `pre_2020 / 2020_21 / 2022_23 / 2024_26` on a 2013+ panel.
- Fully specified except: the exact realized-volatility estimator inputs (realized variance vs Parkinson) differ between the panel build and the report rows in ways the JSON does not restate, and the pre-2020 era's DM loss differential is reported at a scale inconsistent with every other era (see Negative evidence 15) - both **`data gap`**.

**Risk overlay (`signals/vol_targeting.py`):** asset SPY; `TARGET_VOL = 15.0`% annualized; exposure rule `w_t = min(cap, target / forecast_t)` with `cap = 1.0` (long-only, no leverage); daily rebalance; **T+1 execution** (`weight.shift(1) * ret`); `cash_rate = 0.0`; forecast model `har_pooled_level`; `execution_lag_days = 1`. Controls (all source-reported): `no_model_inverse_rv = min(1, 15/rv_m)` on raw trailing 21-session vol; `no_model_vol_matched` with target `12.05` chosen **with hindsight** to match the strategy's realized OOS vol; `constant_mean_exposure` at the realized OOS mean weight `0.9516`; `constant_equal_vol` at hindsight weight `0.8212`; and a `vol_target_har_log` variant. The source labels the hindsight controls as hindsight by construction.

## Required data

- **Instrument / universe:** US-listed common equity inside the S&P 500 (large-cap/PEAD/factors) and S&P 400 (mid-cap) as point-in-time index members; benchmarks SPY (large) and MDY (mid); single-asset overlay on SPY. Universe rules: static runs use **current** constituent lists (`loaders/universe_largecap.json` = 218 tickers, `loaders/universe_midcap.json` = 540 tickers per `validation/criterion.json`) while PIT runs use event-dated membership intervals; survivorship handling is the object under test, not an afterthought.
- **Venue / market type:** US equity cash market via a free daily data source (`yfinance` daily adjusted OHLCV, `data/pit_prices_manifest.json` fingerprints committed). No futures, no options, no crypto.
- **Timeframe:** daily bars; formation grids of 5 sessions (factors), 21 sessions (mid-cap and factor books), and event-time (PEAD); volatility target daily.
- **Fields:** adjusted OHLCV and derived dollar volume; 52-week high; index membership intervals (from two Wikipedia-derived reconstructions: quarterly revision snapshots and dated changes-table replay, reconciled to event-dated intervals, 52 ticker renames resolved through date-aware chains); earnings announcement dates; realized/Parkinson variance features.
- **Point-in-time:** membership at date *T* depends only on events dated at or before *T*; features use information through *T*; returns start at *T+1*; purged train/test boundary at 2024-01-01 for volatility; factor PIT start bounded by the 252-session lookback.
- **Timestamp / timezone:** daily session alignment only; **timezone, session calendar, and half-day handling are `data gap`** (never stated in source).
- **Missing data:** unfetchable members are dropped and reported (141 S&P 500 and 336 S&P 400 distinct historical members have no free price history); earnings events require a price panel match; names failing the lookback/ADV/financeness checks are skipped. Imputation is not used for returns.
- **Funding/fee/spread needs:** round-trip cost is a flat charge (20 bps large-cap, 35 bps mid-cap); spread, impact, taxes, borrow and gap slippage are **not modeled** (explicitly out of scope); volatility overlay is reported gross with 1/5/10 bp one-way sensitivity.

## Execution assumptions

- **Signal-to-order timing:** formation at *T*, portfolio earns from *T+1* ("enter at the next session (T+1), never at a frictionless mid-price" - README section 2.2 / research/04). Volatility overlay: weight decided at *t* earns day *t+1* (`execution_lag_days = 1`).
- **Order type / fill model:** next-session execution at the session price implied by the adjusted close series; **order type, bid/ask, partial fills, queue position and latency are `data gap` / `underspecified`** (never stated in source).
- **Fees / spread / slippage:** flat round-trip approximation only - 20 bps on large-cap names, 35 bps on mid-cap names, charged per holding period. README section 5 states market impact, taxes, borrow and gap-dependent slippage are outside scope, so every one of those is a **`data gap`, never zero**.
- **Volatility overlay costs:** headline is **gross**; `cost_note` states that at 5 bp one-way a daily rebalance costs ~21.4 bp/yr, with net variants at 1/5/10 bp one-way committed in `cost_sensitivity_oos`.
- **Impact / capacity:** no capacity or participation model anywhere; the mid-cap `$5M` dollar-volume floor is a liquidity filter, **not** a capacity claim (`data gap`).
- **Leverage / margin / borrow / shorting:** long-only, no leverage, cash rate 0% (source-stated); no shorting in any of the four families; no margin or liquidation logic.
- **Funding:** not applicable to cash equities.
- **What the source assumes vs what we assume:** all of the above are source-stated; this record adds no execution assumption of its own - any operational choice not listed here is **`research-proposed`** and none is needed to restate the source.

## Evidence

### Source-reported

All figures below are `source-reported` from the pinned commit; every row carries its file + JSON-key/notebook-section provenance. Market/universe and gross/net status are stated per row. **None has been independently reproduced.**

| Claim | Value (source-reported) | Provenance (pinned path + key) | Universe / window | Cost status |
|---|---|---|---|---|
| Static long-only momentum excess vs SPY | cum **+55.3%**, ann Sharpe 0.533, DSR 0.2419 | `research/results/factors_raw_recompute.json /MOM_HI_excess` | S&P 500 static current-constituent panel, 2021-01-01 to 2026-04-01 | net 20 bps round trip |
| Same rule, PIT membership, window-matched | cum **-8.2%**, ann Sharpe -0.165, DSR 0.0118 | `research/results/factors_raw_recompute_pit_windowmatched.json /MOM_HI_excess` | PIT S&P 500, same window | net 20 bps |
| Same rule, PIT membership, extended | cum **-30.5%**, DSR 0.0013 | `research/results/factors_raw_recompute_pit.json /MOM_HI_excess` | PIT S&P 500, 2014-02-03 to 2026-04-01 | net 20 bps |
| Survivorship decomposition | 55.3 -> -8.2 -> -30.5; "removes **63.5 percentage points**" | README section 3.2 Figure 3 caption | identical rule/cost/window, universe swap only | net 20 bps |
| Market-neutral Q5-Q1 20-day abnormal spread, `mom_252_21` | static **-6.949 pp**, window-matched **-4.777 pp**, PIT **-4.599 pp**; extended-window t = -30.8 (prose) | `factors.json`, `factors_pit_windowmatched.json`, `factors_pit.json` each at `/signals/mom_252_21/20d/q5_minus_q1`; t from `research/02-factor-reversal-and-self-correction.md` closing section | S&P 500 | gross of the 20 bps for the spread series |
| Momentum beta shift | beta near **1.5** on the survivor cohort vs just under **1** on the honest universe; monthly alpha statistically zero on both | `research/02-factor-reversal-and-self-correction.md` closing section | as above | n/a |
| PEAD event count after PIT filter | **3,728** events (867 of 4,595 removed) | `research/results/pead_pit.json /n_events`; removal count from `research/01-pead-earnings-drift.md` | S&P 500, 2020-07-01 to 2026-04-01 | n/a (event study) |
| PEAD full-sample 20-day legs | positive leg **+0.3523 pp, t = 1.866**; negative leg **-0.3191 pp, t = -1.687**; Q5-Q1 **+1.12 pp** | `pead_pit.json /horizons/20d/{pos_surprise,neg_surprise,ear_quintiles}` | same | n/a |
| PEAD multiplicity | **33** statistics, Sidak family-wise bar **\|t\| = 3.16**, method "Sidak, two-sided, alpha=0.05" | `pead_pit.json /multiple_testing` | same | n/a |
| PEAD 2022 sub-period positive leg | **+1.1917 pp, t = 3.47**, CI95 [0.5194, 1.8904], n = 354, 116 clusters | `pead_pit.json /subperiods_20d/periods/2022/pos_surprise_20d` | 2022-01-01 to 2023-01-01 block | n/a |
| Mid-cap static discovery (top15/21d) | IS **+57.5%** (36 months, Sharpe 0.984, DSR 0.4112, hit 0.611) -> OOS **-3.1%** (26 months, Sharpe -0.076, DSR 0.0228, hit 0.462) | `research/results/midcap.json /primary_top15` | static ~540 current SP400+SP600 names vs MDY | net 35 bps |
| Mid-cap PIT primary rule | IS 2021-2023 **+31.4%** (35 months, Sharpe 0.468, DSR 0.1209, hit 0.543); OOS 2024-2026 **-27.9%** (26 months, Sharpe -0.943, DSR 0.0008, hit 0.346); backward OOS 2014-2019 **-36.1%** (DSR 0.003 per `research/03`) | `research/results/midcap_pit.json /primary_top15` and `/backward_oos_2014_2019_top15` | PIT S&P 400 vs MDY | net 35 bps |
| Mid-cap search-adjusted inference | IS SPA consistent **p = 0.1122**, RC p = 0.085, best strategy `top15_h21`, best t = 1.776, 8 strategies, 10,000 draws, seed 20260721; OOS SPA p = 1.0; full-window SPA p = 0.1109 | `research/results/stats_upgrades.json /reality_check/midcap_family_daily_vs_MDY` | daily excess vs MDY | net 35 bps |
| Factor-family search-adjusted inference | 8 long-only legs, best `ret_5_bottom`, best t = 1.61, RC p = 0.2198, SPA consistent p = 0.2655 | `stats_upgrades.json /reality_check/factor_family_monthly_vs_SPY` | monthly excess vs SPY | net 20 bps |
| Volatility positive control, PIT OOS R2 | **log-HAR 0.4792**, level HAR 0.4464, per-name HAR 0.4674, EWMA 0.4231, naive 0.3454 | `research/results/vol_forecast_pit.json /oos_r2` | pooled PIT panel, holdout from 2024-01-01, n_dates 606 | n/a (forecast) |
| Volatility DM vs persistence | log-HAR vs naive: dm_stat **-2.917**, p = **0.003538**, mean loss diff -0.024671, n_dates 606, `survives_correction: true` (family of 5, Bonferroni alpha 0.01) | `vol_forecast_pit.json /dm_harlog_vs_naive`, `/dm_multiple_testing` | same | n/a |
| Model Confidence Set | 90% MCS = **{log-HAR, EWMA}** (MCS p: har_log 1.0, ewma 0.5593, har 0.0129, naive 0.0119, train_mean 0.0); unchanged at 75% and at blocks 10/42 | `stats_upgrades.json /vol_mcs/{mcs,mcs_block_sensitivity}` | same, QLIKE variance space | n/a |
| Per-year OOS R2 | 2024: log-HAR 0.4803 vs naive 0.3569; 2025: log-HAR 0.3436 vs naive 0.1124; 2026 (partial year): EWMA 0.6158 leads, naive 0.5422 edges out log-HAR 0.5407, level HAR 0.5168 | `vol_forecast_pit.json /oos_r2_by_year` | same | n/a |
| Era R2 (refit per era) | pre-2020 log-HAR 0.3856; 2020-21 0.3019; 2022-23 0.5700; 2024-26 0.4792 | `vol_forecast_pit.json /era_subperiods/*/oos_r2` | 2013+ panel | n/a |
| Risk overlay (SPY, 15% target) | OOS 627 days: vol-target **ann 18.04%, vol 13.08%, Sharpe 1.334, MDD -15.05%** vs buy-and-hold **21.22% / 15.93% / 1.288 / -18.76%** | `research/results/vol_targeting_pit.json /oos` | SPY, holdout from 2024-01-01 | **gross** headline |
| Overlay cost sensitivity | net 1 bp 17.99% (Sharpe 1.330, MDD -15.06%); net 5 bp 17.78% (1.316, -15.10%); net 10 bp 17.52% (1.299, -15.15%) | `vol_targeting_pit.json /cost_sensitivity_oos` | same | net, one-way bps |
| Overlay controls | `no_model_inverse_rv` 18.49% / -17.40%; `no_model_vol_matched` (hindsight 12.05) 17.39% / 1.291 / **-15.18%**; `constant_mean_exposure` 20.17% / 1.288 / -17.91%; `constant_equal_vol` (hindsight 0.8212) 17.34% / 1.288 / **-15.61%**; `vol_target_har_log` 18.45% / 1.325 / -15.63% | `vol_targeting_pit.json /controls_oos` | same | gross |
| PIT universe reconstruction accuracy | mean Jaccard **0.9997** (min 0.996) vs an independent curation, **72 of 78** monthly dates in exact agreement; constituent-day coverage **95.35%** (S&P 500, 2020-26) and **85.77%** (S&P 400, 2019-26) | `docs/universe-construction.md` lines 98 and 156-157; README section 2.1 | index membership series | n/a |
| Registered thresholds | kill criterion `min_n = 30`, `min_oos_excess_pct = 0.5`, `ci_low_must_exceed = 0.0`, registered 2026-07-20 at commit `4cf22f4` | `validation/criterion.json` | all five signals | costs block as recorded in contradiction C3 |

### Independently reproduced

`Not independently reproduced.`

This run performed only read-side verification of the pinned primary source: (a) direct reading of the landing page, README, five signal modules, six research notebooks, four docs and four registration files at commit `175d5691...`; (b) programmatic loading of the cited result JSON keys quoted above; (c) local SHA-256 re-hash of three pinned files; (d) a `git merge-base --is-ancestor` check of registration-before-results ordering; (e) a GitHub API metadata read; (f) repository-wide source-identity dedup. **No backtest was re-run, no yfinance panel was rebuilt, no figure or statistic was regenerated, and no strategy was traded.** The repository's own reproducibility contract (`make test`, `make research`, `make compare`) was **not** executed by this Scout.

### Negative evidence

Numbered items are contiguous from 1; all are `source-reported` unless marked otherwise.

1. Long-only momentum excess **sign-flips** under point-in-time membership: +55.3% static -> -8.2% window-matched -> -30.5% extended, on identical rule/cost/window (README 3.1-3.2; `factors_raw_recompute*.json`).
2. Deflated Sharpe never approaches a deployment bar: 0.2419 static, 0.0118 window-matched, 0.0013 extended (`factors_raw_recompute*.json /MOM_HI_excess/dsr`).
3. The excess is beta, not alpha: momentum book beta near 1.5 on the survivor cohort versus just under one on the honest universe, with monthly alpha statistically zero on both (research/02 closing section).
4. The market-neutral spread does **not** become a long-only edge: Q5-Q1 remains statistically large (extended t = -30.8) yet is classified by the source as a market-neutral beta/survivorship artifact; the PIT spread itself shrinks from -6.949 to -4.599 pp.
5. PEAD full-sample PIT legs are all far below the family bar: +0.3523 (t 1.866), -0.3191 (t -1.687), Q5-Q1 +1.12 against \|t\| = 3.16.
6. The static PEAD "strongest statistic" halves under PIT membership: negative 20-day leg -0.684 (t -2.429) -> -0.3191 (t -1.687), and the Q5-Q1 spread drops from +2.22 to +1.12 (research/01).
7. PIT event filtering removes **867 of 4,595** PEAD events, i.e. part of the published drift was itself universe construction (research/01).
8. The free earnings feed covers only **26-36% of member tickers by year** and only current-cohort names, so the event sample remains survivor-tilted even after PIT membership filtering (README section 5; `docs/limitations.md`).
9. The single statistic that clears 3.16 under the source's own account is a **2022-only** positive-surprise leg, with 2023-26 showing the opposite tilt (negative leg -0.61, t -2.55, uncertified) - labelled by the source as a "regime-conditional curiosity, not a certified effect" (research/01), and in direct conflict with the README's "0 of 33" statement (contradiction C1).
10. PEAD family composition depends on the sample start: the pre-2020 regime block is infeasible because the committed earnings feed starts 2020-07-01, so 2020H2 folds into the 2020-21 block (`pead_pit.json /subperiods_20d/note`) - the "33" is not a stable, design-invariant count.
11. Mid-cap reversal fails on both holdouts under PIT: IS +31.4% -> forward OOS -27.9% -> backward OOS -36.1%, with DSR 0.1209 -> 0.0008 -> 0.003 (`midcap_pit.json`).
12. The mid-cap discovery was already explicable as search: SPA consistent p = 0.1122 over the registered 8-configuration family in the IS window (RC p = 0.085), and SPA p = 1.0 in the OOS window (`stats_upgrades.json`).
13. The mid-cap breadth x hold sensitivity surface is broadly positive on the static panel and **negative across the displayed grid** under PIT forward data (README section 3.3 Figure 4).
14. The factor family as a whole fails its registered reality check: RC p = 0.2198, SPA consistent p = 0.2655 over 8 legs (`stats_upgrades.json`).
15. Era-level DM output for the volatility panel is internally inconsistent in scale: `vol_forecast_pit.json /era_subperiods/pre_2020/dm_harlog_vs_naive/mean_loss_diff = -1712214782604810.8`, nine-plus orders of magnitude away from every other era's differential (~1e-2 to 1e-3), so pre-2020 era DM loss differences are **not interpretable as reported** (`data gap`, Scout observation from the committed value).
16. Model supremacy is **not** established for the positive control: EWMA sits inside both the 90% and 75% MCS alongside the best fitted model (README 3.1-3.4; `stats_upgrades.json /vol_mcs`).
17. On the partial 2026 holdout year, EWMA (R2 0.6158) leads log-HAR (0.5407), so the per-year ranking is not stable (`vol_forecast_pit.json /oos_r2_by_year`).
18. On the **static** panel the pairwise DM result (log-HAR vs naive, p = 0.0059) does **not** clear the registered 10-test Bonferroni bar of p < 0.005; the source itself re-sources the "beats persistence after multiplicity correction" claim to the MCS, not to the pairwise DM table (research/05 line 398; research/08).
19. The overlay returns **less** than buy-and-hold (18.04% vs 21.22%); its value is drawdown reduction only, and even that is nearly matched by controls that use no forecast: `no_model_vol_matched` MDD -15.18% and `constant_equal_vol` MDD -15.61% versus the strategy's -15.05%.
20. Pure de-risking at the realized mean exposure reproduces buy-and-hold's Sharpe exactly (1.288), demonstrating that the Sharpe improvement is not a timing effect (`controls_oos /constant_mean_exposure`, source-noted as scale-invariance-tested).
21. Swapping the forecast model changes nothing material: `vol_target_har_log` gives 18.45% / Sharpe 1.325 / MDD -15.63% versus level-HAR 18.04% / 1.334 / -15.05% (source: "model choice is second-order for this application").
22. The headline overlay result is **gross**; at 5 bp one-way the daily rebalance costs ~21.4 bp/yr and net return falls to 17.78% (`cost_note`, `/cost_sensitivity_oos`).
23. Benchmark comparisons are sensitive to data vintage: SPY buy-and-hold reads +71.3% on the frozen panel and +74.8% on a fresh one, ~3.5 pp of any cumulative comparison attributable to yfinance snapshot drift (research/02).
24. The DSR implementation knowingly **biases toward certification**: it substitutes sqrt(1/(T-1)) for the Bailey-Lopez de Prado trial-variance term, which understates the deflation threshold - yet every DSR still failed (research/04).
25. Trial counting is a declared **lower bound**: v1/v2 predecessors are each counted as one configuration because their tuning histories were not preserved (`prereg_reality_check.json /trial_counting`), so the deflation is understated rather than conservative.
26. Residual survivorship remains: 141 historical S&P 500 members and 336 S&P 400 members have no free price history, disproportionately removals (README section 5; `docs/limitations.md`), and S&P 400 membership before ~2021 is quarterly-resolution with no external cross-check.
27. Execution realism is bounded by a flat cost approximation with no market impact, taxes, borrow or gap-dependent slippage and no capacity model (README section 5), so no net-of-frictions claim can be stronger than "flat 20/35 bps".
28. The registered kill-criterion config declares `one_way_bps: 35` for the whole signal surface, disagreeing with both the labels and the per-universe values actually charged (contradiction C3) - the registration and the code are not aligned on cost.
29. One finite historical path (2013-2026) covers several shocks but not future regimes; the source states statistical correction controls overfitting and sampling luck, **not** regime risk (README section 2.3, research/04).
30. No external replication, review or citation exists at read time: 0 stars, 0 forks, 0 open issues, no journal/preprint/DOI, and no third-party replication was identified in this repo's or Wiki Brain's records (`data gap` on independent verification).
31. Crypto/multi-venue/24-7 behaviour is entirely untested: the whole apparatus runs on US equity index membership and a single free daily vendor, so nothing here speaks to perpetual funding, liquidation, mark price or venue fragmentation (see Crypto portability).
32. Positive-control scope is narrow: the volatility result is one horizon (21 sessions), one loss (QLIKE), one panel construction, and one split (2024-01-01); model rank flips across years (item 17) and EWMA is never separated (item 16).

## Falsification plan

All thresholds and decision rules in this section are **`research-defined`** (Scout-authored falsification thresholds) or **`research-proposed`** (Scout-authored operationalizations); none of them is source-reported. Failure action for every test: record the outcome in this record's Negative evidence / Evidence sections and leave `status: research-only` unchanged unless the relevant claim is revived.

1. **F1 - PIT universe reproduction gate (`research-defined`).** Rebuild index membership per `docs/universe-construction.md` from an independent source. Fail the source's universe claim if mean Jaccard < 0.99 against the independent curation or constituent-day coverage < 90% on the stated windows.
2. **F2 - Momentum sign-pattern reproduction (`research-defined`).** Re-run the identical rule/cost/window under static vs window-matched PIT vs extended PIT membership. Fail the artifact diagnosis if the three cumulative excess values do not land within +/-2 pp of +55.3 / -8.2 / -30.5 or any sign changes.
3. **F3 - Universe-swap ablation (`research-defined`).** With rule, cost and window frozen, the static-to-PIT effect must be at least 20 pp (source measures 63.5 pp). Fail if |effect| < 20 pp, meaning universe construction cannot explain the published edge.
4. **F4 - Raw-vs-abnormal-return ablation (`research-defined`).** Report long-only raw excess vs market-neutral AR spread side by side on both universes. Fail the source's "return construction distorts the claim" argument if the long-only excess tracks the AR spread within 5 pp on both universes.
5. **F5 - PEAD multiplicity and cross-vendor gate (`research-defined`).** Recompute the 33-statistic family with a second, point-in-time earnings feed. Resurrect PEAD only if a **full-sample** statistic reaches \|t\| >= 3.16 **and** its stationary-bootstrap 95% CI excludes zero **and** the result replicates across both vendors; fail the source's null if that condition holds.
6. **F6 - PEAD offset/placebo gate (`research-defined`).** Repeat at drift offsets 1,3,4,5 and with announcement-date placebo shifts. Fail if the (null) verdict depends on `DRIFT_OFFSET = 2` or if a placebo family produces a comparable max \|t\|.
7. **F7 - Mid-cap search-aware gate (`research-defined`).** Extend the registered 8-cell family forward from 2026-10-01. Resurrect H3 only if SPA consistent p < 0.05 on the fresh window with net excess > 0 at 35 bps and a bootstrap CI excluding zero.
8. **F8 - Mid-cap liquidity/impact stress (`research-defined`).** ADV floor ladder $1M / $5M / $20M crossed with cost ladder 35 / 70 / 105 bps plus a 10-50 bps impact add-on. Fail the "no edge" verdict only if net OOS excess stays > 0 at the source's own 35 bps with impact modeled.
9. **F9 - Positive-control forward gate (`research-defined`).** On data from 2026-10-01 for 15 months, PIT log-HAR must reach pooled OOS R2 >= 0.30 with DM p < 0.01 vs persistence to keep the apparatus certified; fail the apparatus claim if R2 < 0.10 (the pipeline would then be rejecting everything, nullifying the negative results).
10. **F10 - Model-supremacy adjudication (`research-defined`).** Registered MCS over >= 600 holdout dates: if log-HAR enters the 90% MCS **alone** (EWMA excluded) in two consecutive non-overlapping windows, revise the "model choice is immaterial / EWMA indistinguishable" statement; fail the current reading if EWMA remains in the 90% MCS (current state).
11. **F11 - Overlay mechanism ablation (`research-defined`).** Compare the 15%-target overlay against `constant_equal_vol` and `no_model_vol_matched`. Add value only if overlay Sharpe exceeds the risk-matched control by > 0.10 with a bootstrap CI excluding zero (currently 1.334 vs 1.288 / 1.291, so it fails today); fail the "exposure reduction, not alpha" reading only when that condition is met.
12. **F12 - Overlay cost ladder (`research-defined`).** Net 0 / 1 / 5 / 10 / 20 bp one-way. The drawdown advantage must persist at 10 bp (currently MDD -15.15% vs -18.76%) and must not rely on gross reporting.
13. **F13 - Registration-integrity gate (`research-defined`).** For every results file, verify `git merge-base --is-ancestor <registration commit> <results commit>` (already true for the three 2026-07-21 registrations). Fail the search-aware claims if any result file predates its registration, or if the trial log is a lower bound that would change a verdict under a +50% trial count.
14. **F14 - End-to-end independent reproduction (`research-defined`).** Fresh clone at the pinned SHA: `make setup && make test && make research && make compare` must exit 0 with no tolerance-exceeding diff and with echoed input SHA-256 matching `data/pit_prices_manifest.json`. Any unexplained divergence downgrades this record's Evidence section to `data gap` for every affected number.

## Crypto portability

**`unproven`.** The source contains **zero** crypto evidence: every universe is an S&P 500 / S&P 400 member list, every price series is US equity daily bars from one free vendor, and both benchmarks are US equity ETFs. Porting is not a parameter change:

- **Mechanism:** PEAD requires scheduled earnings disclosures (no counterpart for tokens), mid-cap reversal requires an index-membership survivorship structure, and momentum/reversal requires a stable point-in-time constituent history - none of which exists for crypto spot or perpetuals.
- **Data dependency (material):** the PIT membership reconstruction is built from Wikipedia index revision snapshots; no equivalent point-in-time listing history exists on crypto venues, so the very bias being measured cannot be reconstructed the same way.
- **24/7 / candle boundaries:** daily session alignment, T+1 fills and the 2/21/252-session lookbacks have no 24/7 analogue; candle boundary, timezone and funding-settlement interactions are `data gap`.
- **Spot vs perpetual, funding, liquidation, mark price, venue fragmentation, custody:** all `data gap` - never mentioned in the source, never modeled.
- **Positive control:** the one component that might port (HAR-style volatility forecasting) was tested only on equity realized/Parkinson variance; whether it survives crypto's jump-heavy, 24/7 variance process is untested.
- **Boundary statement:** this is a ported hypothesis at best, **not** crypto empirical evidence; crypto portability is not authorization to trade.

## Limitations

- `underspecified`: timezone/session calendar, order type, fill model, latency, partial fills, ADV window, earnings-feed vendor, benchmark total-return vs price-return convention, price-adjustment/vendor conventions.
- `data gap` (never stated in source, never inferred here): market impact, spread, taxes, borrow, capacity/participation, gap slippage, funding, leverage/margin, and all pre-2020 era DM loss-differential scale (Negative evidence 15).
- `not independently reproduced`: every performance and statistical figure in this record; this Scout verified only that the pinned files contain them.
- `unproven`: any claim that the null verdicts generalize beyond US large/mid-cap daily equity in 2013-2026, or to market-neutral/intraday implementations (the source explicitly bounds its conclusion this way in README section 4).
- Source quality: independent single-author public repository, no peer review, no preprint, no DOI, 0 stars/0 forks, no third-party replication identified - traceable and reproducible by construction, but uncorroborated.
- Publication/selection bias in the other direction: a repository whose thesis is "nothing survives" is also a selected artifact; the registered expectations (`prereg_bootstrap.json`, `prereg_reality_check.json`) anticipated null verdicts, which the source discloses rather than hides.
- Two internal inconsistencies in the source's own reporting are recorded unreconciled in the frontmatter (README "0 of 33" vs notebook 01 "one statistic clears 3.16"; README single DSR vs two documented DSRs), plus a registration/code cost mismatch and a licence metadata mismatch.
- Scope: no cross-venue, no options, no futures, no crypto, no shorting, no leverage; the contribution is methodological (README section 1 explicitly disclaims being a trading strategy).

## Implementation status

`implementation_status: not-implemented`. Nothing from this record has been implemented in our research stack: no Qlib full backtest, no production card, no Paper, Testnet or Live run, and no survivor/pipeline entry exists. The source repository is itself research code that "does not place, simulate, or recommend orders" and states "No capital was traded on any tested signal" (README banner). This record changes none of that.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this record in the staging repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain or the production candidate pool; completed Qlib validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, Paper, Testnet or Live. Any later adoption or implementation decision must be explicit, separately reviewed, and based on this record plus current sources. No wording, evidence count, confidence value or schedule implies promotion.

## Related Wiki records

Verified Wiki Brain pages (paths returned by `kb_search` this run; no page was fabricated):

- [[quant/llm-strategy-discovery-leakage-safe-search-deflated-eval-2026-09-04]] - closest methodological neighbour: leakage-safe, search-aware, deflated evaluation with null verdicts for LLM-discovered strategies on a 453-stock and 39-ETF universe.
- [[quant/us-equity-vortex-top2-cross-sectional-trend-phase-robustness-2026-09-13]] - US equity cross-sectional trend with an acknowledged retroactive-universe survivorship caveat.
- [[quant/sp500-index-reconstitution-announcement-drift-decay-falsification-2026-09-13]] - S&P 500 membership-event falsification, deletion side purged for survivorship.
- [[quant/drift-regime-gated-cross-sectional-value-reversal-2026-09-05]] - cross-sectional value/reversal whose universe is current-constituent S&P 500 over 2004-2024 (the exact distortion this record measures).
- [[quant/statistical-arbitrage-methodology-degradation-ladder-falsification-2026-09-12]] - null after survivorship bias and multiple-testing corrections.

Repository records (different source identities, cited for adjacency only): `korea-pead-staggered-tranche-long-only-asymmetry-falsification-2026-09-13.md` (GitHub `younghwan91/kr-quant` @ `cc1b6f6a`, Korean PEAD); `retail-investor-horizon-pead-stocktwits-long-short-2026-09-23.md` (arXiv 2512.00280); `pure-momentum-wild-bootstrap-drift-significance-filter-us-equities-2026-09-26.md` (Amundi WP #188); `reviving-anomalies-expected-net-return-double-sort-1n-implementable-2026-09-23.md` (SSRN 6468806); `crypto-weekly-momentum-survivor-liquidity-fragility-2026-09-04.md`.

**Four-axis distinction from the nearest records** (source identity and mechanism differ in every pair): (1) vs arXiv 2608.27734 - that source's mechanism is a registry-validated leak-proof agent toolchain plus trial-count deflation for *LLM-generated* strategies, whereas this source's mechanism is point-in-time **universe reconstruction** and raw-vs-abnormal return decomposition on *hand-specified classic* anomalies, with a positive control; (2) vs SSRN 6468806 - that source ranks 153 characteristics by ML expected net returns with an explicit impact model, while this source freezes four textbook signals and three anomaly families and reports their failure; (3) vs the Korea PEAD record - different market, different source, and a tranche-asymmetry mechanism rather than a family-wise Sidak verdict; (4) vs Amundi WP #188 - that source proposes a wild-bootstrap drift-significance filter on momentum as a positive contribution, while this source reports the long-only momentum book as negative after a universe swap; (5) vs the crypto survivorship record - different market type and a liquidity/transient-coin mechanism rather than index-membership reconstruction.

## Sources

1. Abhinav Koppulu. *When Equity Signals Disappear - A Point-in-Time, Search-Aware Evaluation of Retail-Constrained Equity Anomalies.* Public GitHub repository https://github.com/abhikoppulu-ai/Equity-Signal-Research, pinned at full commit `175d5691822fccfb8aeca85918099ab433b9b453` (main, 2026-07-22T22:18:41Z). `README.md` 17,922 bytes, SHA-256 `35449d6bcdf2d9d89ad4635155c6f1c512514f6ec3e7e871fde72ce3ed3395c0`. Read in full 2026-09-27.
2. Same repository, machine-readable results at the pinned commit: `research/results/pead_pit.json` (SHA-256 `84b3f49a1642aa936369bd6a13608f5c7f6bfff1905357307d313983b3822f3d`), `research/results/vol_forecast_pit.json` (SHA-256 `da4aa3036b19cebff4bdefd601a2e2d97849415e11a7a94be7e62f46f3475a47`), plus `factors.json`, `factors_raw_recompute.json`, `factors_raw_recompute_pit.json`, `factors_raw_recompute_pit_windowmatched.json`, `factors_pit.json`, `factors_pit_windowmatched.json`, `midcap.json`, `midcap_pit.json`, `vol_targeting.json`, `vol_targeting_pit.json`, `stats_upgrades.json` - all loaded programmatically at the pinned commit on 2026-09-27.
3. Same repository, method and provenance documents at the pinned commit: `research/01-pead-earnings-drift.md`, `research/02-factor-reversal-and-self-correction.md`, `research/03-midcap-out-of-sample-overfitting.md`, `research/04-methodology-costs-and-deflated-sharpe.md`, `research/05-volatility-forecasting.md`, `research/08-statistical-upgrades.md`; `docs/universe-construction.md`, `docs/limitations.md`, `docs/pit-impact.md`, `docs/v4-changelog.md`; `validation/prereg_bootstrap.json`, `validation/prereg_mcs.json`, `validation/prereg_reality_check.json`, `validation/criterion.json`; `signals/pead.py`, `signals/factors.py`, `signals/midcap.py`, `signals/vol_forecast.py`, `signals/vol_targeting.py`; `LICENSE`.
4. Same repository, immutable commit references used for ordering checks: `4d14c5c8edad82daf3cddc8f6a5dfd58ce02d9c4` (method registrations), `9344cf2ac96d28ce5d4276f417fa19d923c7108d` (registered results), `64fab477269d689998b58a9c22ae7cd03912e1a3` (first commit), `4cf22f4` (kill-criterion registration, as printed in `validation/criterion.json`).
5. GitHub REST metadata, read 2026-09-27: https://api.github.com/repos/abhikoppulu-ai/Equity-Signal-Research (created/pushed/updated timestamps, visibility, stars, forks, issues, licence fields).
6. Upstream provenance declared by the source: https://github.com/abhikoppulu-ai/equity-signal-lab at commit `3980869` (V3 imported as V4 baseline; not opened for this record - `data gap` on V3 content).
