---
schema: strategy-research-record-v1
title: "Execution-aware short-horizon sector-residual 5-day reversal with EWMA turnover control in US equities (CRSP 2000-2024; in-sample net Sharpe 0.34 at 7 bps, one-shot 2019-2024 holdout net -0.15) - GitHub andrewzhang615-star/equity-statarb commit f6519366"
created: 2026-09-28
updated: 2026-09-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - us-equity
  - cross-sectional
  - reversal
  - transaction-costs
  - capacity
  - github-research
status: research-only
confidence: medium
source_as_of: 2026-07-07
sources:
  - "https://github.com/andrewzhang615-star/equity-statarb/tree/f65193666d16c7d13a925266a31e4158568d5804"
  - "https://github.com/andrewzhang615-star/equity-statarb/blob/f65193666d16c7d13a925266a31e4158568d5804/reports/memo.md"
  - "https://github.com/andrewzhang615-star/equity-statarb/blob/f65193666d16c7d13a925266a31e4158568d5804/research_log.md"
  - "https://github.com/andrewzhang615-star/equity-statarb/blob/f65193666d16c7d13a925266a31e4158568d5804/config.yaml"
  - "https://github.com/andrewzhang615-star/equity-statarb/blob/f65193666d16c7d13a925266a31e4158568d5804/reports/oos_summary.txt"
  - "https://api.github.com/repos/andrewzhang615-star/equity-statarb"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Cost-sensitivity range: README 'Honest limitations', memo section 9.1 and research_log all state a '2-10 bps' sensitivity, while scripts/cost_sensitivity.py sweeps np.arange(0, 15.5, 1.0) = 0-15 bps and the research_log cost table itself lists 0 and 12 bps - unreconciled."
  - "Turnover reduction: memo section 4 says turnover control 'approximately halves turnover' and the README says 'roughly halves turnover', while memo Table 1 shows turnover 0.64 -> 0.23 for that step (a 64 percent reduction) - unreconciled."
  - "Usable capacity: the memo abstract/section 5 and README advertise 'roughly $10-100M', while the research_log capacity table shows $100M net Sharpe -0.01 / -0.36 / -0.84 at eta 0.3 / 0.6 / 1.0 and the research_log text states 'mid/conservative eta caps it at ~$10-30M' - unreconciled."
  - "Delisting sensitivity: config.yaml sets delisting.sensitivity [0.0, -0.30, -0.55] and research_log calls it the 'main table', but no result table for that sensitivity is printed anywhere in memo, README, research_log or the committed figures - data gap, unreconciled."
  - "Dependency pinning: requirements.txt pins no versions and both CI workflows run 'pip install -r requirements.txt' unpinned, yet the README advertises a green 37-test CI badge; an independent run on 2026-09-28 with the current resolution (pandas 3.0.6) fails 1 of the 37 tests - unreconciled."
---

# Execution-Aware Short-Horizon Sector-Residual Reversal with EWMA Turnover Control (US Equities, CRSP 2000-2024)

## Provenance

- Source type: public GitHub research repository (code + memo + experiment journal). Not a paper, preprint, working paper or journal article; no DOI, arXiv ID, SSRN ID, publisher, or peer-review statement was identified, so publication/peer-review status is `not stated in source` (data gap).
- Repository: https://github.com/andrewzhang615-star/equity-statarb
- Immutable pin: full commit SHA `f65193666d16c7d13a925266a31e4158568d5804` (message "Correct research log dates"). Verified 2026-09-28 with `git ls-remote https://github.com/andrewzhang615-star/equity-statarb HEAD refs/heads/main`, which returned that same SHA for both `HEAD` and `refs/heads/main`, so the pin is the current remote head.
- Paths read at that pin on 2026-09-28, with SHA-256 of the locally retrieved copies: `README.md` (`c1c548716da9f58bf85b2d9cc7e3f4b82bc940bb460fdc314c776120770d6d60`), `reports/memo.md` (`f892103f43ba786b9b7ab213b06a6b5b96d474263ef3c914b841fbb59655e56d`), `reports/oos_summary.txt` (`a949f99153bab3a285c094f6ffe5af45791405942c76f9cb602415ca10c70ec8`), `config.yaml` (`74053d56f93d3be75456fdec011dcbbe639259e253be63e79e747096acf51ffa`), `research_log.md` (`a9332f2a0d95a4d2a51d50769e99733bc184d803e0e18436eccb05c3eb595e36`), `scripts/cost_sensitivity.py` (`407bc5085bb829e70a5dcab9e89539f0bf41523cbfff773263dff171e6c12c19`), plus `src/backtest/engine.py`, `src/backtest/metrics.py`, `scripts/cost_sensitivity.py`, `scripts/capacity.py`, `requirements.txt`, `.github/workflows/ci.yml`, `.github/workflows/python-app.yml` and `LICENSE`.
- Author identity: memo frontmatter prints `author: "Andrew Zhang"`; the GitHub API contributors endpoint read 2026-09-28 returns a single login `andrewzhang615-star` with 43 contributions, matching the 43 commits reported for `main`.
- Repository metadata (GitHub REST API read 2026-09-28): created `2026-06-30T19:18:16Z`, pushed `2026-07-07T00:24:50Z`, default branch `main`, stargazers 0, forks 0, open issues 0, license SPDX `MIT` (`LICENSE` header "MIT License, Copyright (c) 2026 Andrew Zhang").
- CI provenance (GitHub Actions API read 2026-09-28): total action runs 29; two workflows, `tests` (`.github/workflows/ci.yml`, Python 3.12) and `Python tests` (`.github/workflows/python-app.yml`, Python 3.11); both install with `pip install -r requirements.txt` (unpinned); the latest run of each workflow is at `head_sha f65193666d16c7d13a925266a31e4158568d5804` with `conclusion: success`, `created_at 2026-07-07T00:24:51Z`.
- Sample period: CRSP daily, `data.start_date 2000-01-01` to `data.end_date 2024-12-31` (`config.yaml`); memo section 2 reports 27.2 million name-days across 12,859 securities.
- Universe: CRSP share codes 10-11, exchange codes 1/2/3 (NYSE/AMEX/NASDAQ); point-in-time top 1,000 names by trailing dollar volume rebalanced daily (`universe_size 1000`, `adv_window 60`, `adv_min_periods 20`), prior-close price >= $5.0, delisting rows excluded from eligibility.
- Transaction-cost treatment: flat 7 bps per unit turnover = `commission_bps 2.0` per side + `slippage_bps 5.0` (`config.yaml`), applied linearly as `cost = turnover * cost_bps / 1e4` (`src/backtest/engine.py`); square-root market impact enters only the separate capacity analysis; short borrow is explicitly not modeled.
- Pre-write source-identity dedup (2026-09-28, hidden-inclusive `rg -uuu` across the whole checkout including `.git/`, `.mimo-worktrees/`, `.agents/`, `.hermes/` and `coverage_manifest.csv` at 1,088,787 bytes): zero hits for `equity-statarb`, `andrewzhang615`, the full SHA, `Equity_StatArb_Memo`, the exact titles `Evidence of Decay, Costs, and Capacity Limits` and `Execution-Aware Short-Horizon`, and `sector-residual`; positive control `novy-marx` returned hits in the same session; `git log --oneline -20` was used only as a convenience glance; Wiki Brain `kb_search` (read-only) returned only the adjacent pages listed under Related Wiki records.

## Economic mechanism

### Source-reported

The repository frames short-horizon reversal as a textbook effect (Lehmann 1990; Lo and MacKinlay 1990): individual names that fell over the last five days tend to outperform names that rose, over days to weeks. Common variation is removed first (rolling market residual, then leave-one-out two-digit SIC sector residual) so that the traded object is idiosyncratic reversal rather than sector or market co-movement. The source attributes the historical decay of the effect to crowding, decimalization and tighter markets (memo section 6.1), describes the resulting book as "short momentum and long reversion with a liquidity-provision profile" (memo section 6.3), and states that the contribution is methodological - a leak-safe pipeline, execution and capacity layer, pre-registration and a one-shot out-of-sample test - rather than a new alpha claim (memo section 9).

### Research interpretation

Hypothesized mechanism: cross-sectional mean reversion of idiosyncratic five-day moves in liquid US equities, where the return comes from supplying liquidity to transient price pressure after removing market and sector common factors. The falsifiable friction-adjusted thesis is that per-trade edge (break-even cost) decays toward and below realistic execution cost as the anomaly becomes crowded, so the strategy's economic value is a cost-tolerance question, not a forecasting question. Component roles: primary signal = negative five-day sector-residual return; turnover control = five-day-half-life EWMA smoothing of the signal (reduces cost drag, not the signal itself); risk/exit = none beyond daily re-optimization plus a 2% per-name cap and dollar-neutral demeaning; regime dependence = high-volatility/high-dispersion episodes. The record does not assume each component adds alpha; the ablation ladder in F7 is required.

## Signal

All items below are source-reported unless explicitly labeled `research-proposed` or `research-defined`.

- Formation timestamp: weights are formed at each day's close (memo sections 2 and 3.2). Timezone, session and clock convention are `not stated in source` beyond "CRSP daily" (data gap).
- Lookback: trailing five trading days (`signals.reversal.lookback 5`, `skip 0` in `config.yaml`); daily returns winsorized at +/-20% for signal formation only and never for realized PnL (`signals.winsorize`, memo section 3.1); market residual from a rolling regression on the equal-weighted eligible universe with `residual.estimation_window 60` trading days; leave-one-out sector residual demeaning within point-in-time two-digit SIC with `sector_min_peers 5` (excludes the name itself).
- Smoothing: EWMA over the signal with `portfolio.smoothing_halflife 5` trading days, described by the source as the locked turnover control.
- Long entry: buy the strongest recent losers (reversal decile 10 side); short entry: sell the strongest recent winners (reversal decile 1 side) (memo sections 3.1 and 6.2, Figure 1 description).
- Weight construction: cross-sectionally demeaned dollar-neutral weights at `gross_leverage 1.0`, clipped to `max_weight 0.02` per name and re-demeaned to restore neutrality (committed weight-application block in `src/backtest/engine.py`).
- Execution timing: `applied = w.shift(1).fillna(0.0)` with `gross_ret = (applied * returns_full.fillna(0.0)).sum(axis=1)` (`src/backtest/engine.py`), i.e. a weight decided at the close of day t-1 earns the return from t-1 close to t close (committed comment: "decided at prior close -> no look-ahead"). Because the signal itself is computed from prices up to t-1 close, this implies execution at the same close that produces the signal. Order type, fill price, latency and partial fills are `not stated in source` (data gap).
- Exit / holding period: daily re-optimization; no stop, no take-profit, no explicit maximum holding period, no re-entry rule beyond the next day's optimization. The realized-return panel is never masked; the lagged eligibility mask (top-1,000 by trailing dollar volume, price >= $5, delisting rows excluded) gates only which names may receive new weight, so an ineligible position still realizes its terminal loss (memo section 2).
- Delisting handling: missing performance-delisting returns (CRSP `dlstcd` 500 and 520-584) imputed at -30% following Shumway (1997), applied at panel-build time; delisting rows are forced ineligible while their realized delisting return is kept (`config.yaml` delisting block; research_log data-construction entries).
- Turnover: 0.228/day reported for the locked candidate in the research_log cost-sensitivity entry, and `turn 0.23` for both IS and OOS in `reports/oos_summary.txt`.
- Parameters: all fixed in `config.yaml` with `seed 42`; no threshold search is reported for the locked candidate. Phase 2 pre-registered three candidate configurations for the multiple-testing adjustment, and the research_log declares EWMA halflife grid {2,3,5,10} and holding-period grid {2,3,5,10} as sensitivities on the fixed candidate rather than separate alphas.
- Reconstructibility: the rule is reconstructible from `config.yaml` plus the committed code, except for execution price/order type, timezone/session convention and the never-printed delisting sensitivity - these are `underspecified`.

## Required data

- Instrument / universe: US common shares (CRSP share codes 10-11) on NYSE/AMEX/NASDAQ (exchange codes 1/2/3), point-in-time top-1,000 by trailing 60-day dollar volume (min 20 periods), prior-close price >= $5, delisting rows excluded from eligibility; reconstituted daily.
- Venue / vendor: CRSP daily data via WRDS (institutional account required). Phase 2 additionally requires Compustat quarterly `rdq` earnings dates plus point-in-time CRSP/Compustat CCM link history (`config.yaml` `earnings_path`, `ccm_link_path`).
- Market type / timeframe: US cash equities, daily bars, US trading days; daily rebalance; simulated capital 10,000,000 (`config.yaml` `backtest.capital`).
- Fields: close price, shares outstanding or price for dollar-volume ranking, `dlret`/`dlstcd`/`dlstdt`, point-in-time `siccd` (explicitly not header `hsiccd`), realized-return panel, eligibility mask, sector panel, Compustat `rdq`.
- Point-in-time / look-ahead protections: two distinct panels (unmasked `returns_full` for PnL, lagged `eligible` mask for tradability); weights lagged one day; delisting losses attached at or before `dlstdt`; no forward-fill of eligibility.
- Missing data: `dlret` missing for 44.5% of delisting events (research_log: 481 missing-or-performance rows imputed -0.30); non-delisting NaN returns treated as 0 (carry) while held, applied only after delisting rows are set; raw pull stays raw with no imputation beyond the documented delisting rule.
- Cost data: flat 7 bps per unit turnover; no observed spread, fee, borrow or funding dataset is used (borrow cost is a data gap, not zero).
- Availability: `data/` at the pinned commit contains only `.gitkeep`; CRSP/Compustat inputs are institutional and not redistributable, so performance cannot be rebuilt from the repository alone (data gap).

## Execution assumptions

Source-reported:

- Signal-to-order: decision at prior close, return earned from prior close to current close (`w.shift(1)`), implying same-close execution with no latency model.
- Order type / fill model / partial fills / latency / session: `not stated in source` (data gap).
- Fees: commission 2.0 bps per side plus slippage 5.0 bps = flat 7 bps floor per unit turnover, applied linearly to daily turnover (`config.yaml`; `src/backtest/engine.py`).
- Spread: no separate spread line (data gap).
- Market impact: excluded from every headline number; added only in `scripts/capacity.py` as square-root impact `eta * sigma * sqrt(|dw| * AUM / ADV$)` on top of the 7 bps floor, with `eta` in {0.3, 0.6, 1.0} and AUM on a log grid from $10M to $10B (`np.logspace(7, 10, 7)`), citing Almgren et al. (2005) and Toth et al. (2011).
- Borrow / shorting: explicitly not modeled (memo section 9.1; README "Honest limitations") even though the alpha is short-side concentrated in $5-25 names (memo section 6.2) - `data gap`, never zero.
- Leverage / margin: gross leverage 1.0, dollar neutral; financing, margin and collateral treatment `not stated in source` (data gap).
- Taxes: `not stated in source` (data gap).
- Capacity: square-root impact model with a stated eta range; an ADV position cap (5%/10%/25% of ADV) is evaluated as a risk control and is reported by the source as limiting downside without extending the net-positive frontier (research_log participation-cap entry); a path-dependent trade/participation cap is named as a future refinement only.

Research-proposed (our operationalization, not source-reported):

- Substituting next-open or intraday VWAP/TWAP execution for the same-close assumption in any replication.
- The borrow-fee ladder values, cost-ladder failure cutoffs, capacity frontier cutoffs and placebo percentiles used in the Falsification plan; every threshold there is `research-defined`.

## Evidence

### Source-reported

All figures in this subsection are third-party claims from the pinned commit, each with its table/section provenance. None of them has been reproduced by us.

1. Construction ladder, in-sample (IS) 2000-2018 (memo Table 1): raw reversal gross Sharpe 0.67 / turnover 0.63 / break-even 4.4 bps; plus market residual 1.00 / 0.63 / 5.1 bps; plus leave-one-out sector residual 1.22 / 0.64 / 5.5 bps; plus EWMA turnover control 0.90 / 0.23 / 11.3 bps.
2. IS versus one-shot out-of-sample (OOS) (memo Table 2 and `reports/oos_summary.txt`): IS 2000-2018 4,779 days - gross 0.90, net@2 0.74, net@5 0.50, net@7 0.34, ann@7 2.2%, maxDD -14.0%, break-even 11.3 bps, turnover 0.23; OOS 2019-2024 1,510 days - gross 0.23, net@2 0.12, net@5 -0.04, net@7 -0.15, ann@7 -2.1%, maxDD -23.1%, break-even 4.2 bps, turnover 0.23.
3. Selection-adjusted statistics (`reports/oos_summary.txt`; memo sections 7 and 8.4): deflated Sharpe over 12 examined IS specifications gives P(true Sharpe > 0 after selection) = 0.20; Phase 2 deflated Sharpe 0.83 over 3 candidates.
4. Cost ladder (research_log entry "2026-06-28 - Cost sensitivity", turnover 0.228/day): assumed cost 0 / 5 / 7 / 10 / 11.3 / 12 bps maps to net Sharpe 0.90 / 0.50 / 0.34 / 0.10 / approximately 0 / -0.06, roughly -0.08 Sharpe per bp; `scripts/cost_sensitivity.py` sweeps `np.arange(0, 15.5, 1.0)`.
5. Subperiod decay (research_log robustness entries): 2000-2006 gross 1.11, net@7 0.67, net ann 6.0%, break-even 17.6 bps; 2007-2012 0.71 / 0.09 / 0.4% / 8.0 bps; 2013-2018 0.85 / -0.01 / -0.1% / 6.9 bps. Subperiod net Sharpe at 2/5/7/10 bps: 2000-2006 = 0.98/0.79/0.67/0.48; 2007-2012 = 0.54/0.27/0.09/-0.18; 2013-2018 = 0.61/0.24/-0.01/-0.38; ALL IS = 0.74/0.50/0.34/0.10.
6. Leg attribution (research_log, CAPM versus the equal-weighted eligible market, gross IS): long leg contribution 5.5% annualized, beta +0.63, alpha 0.8% annualized, IR 0.18; short leg contribution -0.8% annualized, beta -0.51, alpha 4.6% annualized, IR 1.37.
7. Universe tiers (research_log, 7 bps): top-500 (448 names/day) gross 0.79, net 0.31, net ann 2.2%, break-even 11.6 bps; top-1000 (940 names/day) 0.90 / 0.34 / 2.2% / 11.3 bps; top-1500 (1418 names/day) 1.05 / 0.44 / 2.8% / 12.2 bps.
8. Capacity under square-root impact (research_log capacity entry, 7 bps floor): net Sharpe at $10M = 0.23 / 0.12 / -0.03 and max participation 3.6%; at $100M = -0.01 / -0.36 / -0.84 and 35.8%; at $1B = -0.78 / -1.90 / -3.38 and 358% (columns eta 0.3 / 0.6 / 1.0); the same entry states "Even optimistic eta=0.3 caps useful capacity ~$50-100M; mid/conservative eta caps it at ~$10-30M" and that participation exceeds 100% by about $316M.
9. Participation cap (research_log, eta = 0.6, 7 bps floor, net Sharpe): $10M = 0.12 uncapped / 0.12 cap5% / 0.12 cap10% / 0.12 cap25%; $100M = -0.36 / -0.32 / -0.36 / -0.36; $1B = -1.90 / -0.94 / -1.19 / -1.54; $10B = -6.61 / -1.43 / -1.91 / -2.75; max participation at $1B falls from 358% uncapped to 26% (cap5%) and 25% (cap10%).
10. Phase 2 pre-registered refinements (memo section 8): volume conditioning rejected by its own diagnostic - one-day rank IC +0.0130 after high-volume moves versus +0.0074 after low-volume moves with the five-day gradient gone, so per the pre-registered rule no variant was built; earnings exclusion - signals whose five-day window contains an announcement have IC -0.0105 versus +0.0125 for clean signals, exclusion raises gross Sharpe 0.90 -> 1.03 but raises turnover roughly 16%, leaving break-even essentially unchanged; PCA residualization - `k=15` pre-registered, top 15 components explain roughly 52% of standardized variance, gross Sharpe 0.80 -> 1.22 at identical turnover by cutting volatility 6.0% -> 4.3%. Memo Table 3 (IS common dates 2001-2018, gross / net@7 / break-even): sector-LOO 0.80 / 0.14 / 8.5 bps; sector-LOO + exclusion 0.92 / 0.16 / 8.5 bps; PCA k=15 1.22 / 0.26 / 8.9 bps; PCA k=15 + exclusion 1.37 / 0.28 / 8.8 bps. On the already-spent 2019-2024 window the combined candidate shows gross -0.07 and net -0.64 at 7 bps (memo section 8.4).
11. Diagnostics (memo section 6): rolling three-year break-even falls from about 50 bps in the earliest windows to below 10 bps by the mid-2000s and later oscillates around the assumed 7 bps line; the ten largest contributors account for roughly 8% of gross profit and 2,356 names contribute positively; profitable shorts are concentrated in $5-25 names; worst episodes are the 2000 dot-com peak, the 2009 rebound and the calm 2003-2007 bull market; the edge is concentrated in high-volatility and high-dispersion regimes.
12. Data scale and hygiene (memo section 2 and research_log): 27.2 million name-days across 12,859 securities; delisting returns missing for 44.5% of delisting events with -30% imputation for performance delistings per Shumway (1997); a documented bug fix (dlstcd 100 "still trading" rows wrongly flagged) with panels rebuilt; a suite of 37 unit tests guarding metrics, look-ahead and disappearing-position safeguards.

### Independently reproduced

- Performance figures: `not independently reproduced`. The pinned repository ships no raw or processed data (`data/` contains only `.gitkeep`) and CRSP/WRDS requires an institutional account, so no headline Sharpe, break-even, drawdown or capacity number can be rebuilt in this environment. Everything in the Source-reported subsection remains a third-party claim.
- What we did run (our own execution on 2026-09-28, clone of the pinned SHA with a clean worktree):
  - Run A, 2025-era dependency set: `uv run --python 3.12 --with pytest --with pandas==2.2.3 --with 'numpy<2.3' ... pytest -q` -> `37 passed, 3 warnings`, exit 0 (warning: `invalid value encountered in matmul` in `src/signals/pca.py:65`).
  - Run B, current unpinned resolution: pandas 3.0.6 / numpy 2.5.3 / scipy 1.18.1 -> `1 failed, 36 passed`, with `tests/test_earnings.py::test_weekend_announcement_hits_next_trading_day` failing at `src/data/earnings.py:83` with `ValueError: assignment destination is read-only` (pandas 3.0 copy-on-write behavior on `panel.values[...] = True`).
  - Root cause we identified: `requirements.txt` lists numpy, pandas, scipy, matplotlib, pyyaml, pyarrow, wrds and pytest with no version pins, and both CI workflows install from that file unpinned (Python 3.11 and 3.12), so the dependency set resolved on 2026-07-07 is not the one resolved today.
  - Scope of this evidence: the look-ahead / leak-guard / metrics test suite passes under a pandas 2.x environment and partially fails under pandas 3.0.6. This validates nothing about profitability; it only characterizes the code's test health and its dependency fragility.

### Negative evidence

1. The frozen one-shot OOS test on 2019-2024 is net-negative at the headline cost: net Sharpe -0.15 at 7 bps, break-even 4.2 bps (memo Table 2; `reports/oos_summary.txt`).
2. OOS gross Sharpe collapses to 0.23 from 0.90 in-sample (memo Table 2).
3. OOS net Sharpe is negative already at 5 bps (-0.04) and positive only at an implausible 2 bps (+0.12) (`reports/oos_summary.txt`).
4. Selection-adjusted evidence: deflated Sharpe 0.20 over 12 trials means only a 20% assigned probability that the true IS Sharpe is positive after selection (memo section 7).
5. Monotone in-sample decay of break-even: 17.6 bps (2000-2006) -> 8.0 bps (2007-2012) -> 6.9 bps (2013-2018), with 2013-2018 net Sharpe -0.38 at 10 bps (research_log).
6. OOS max drawdown -23.1% versus -14.0% in-sample, with the largest OOS drawdown in the 2020 COVID crash and rebound (memo sections 6 and 7).
7. Capacity is small and turns negative fast: at $100M the net Sharpe is -0.01 / -0.36 / -0.84 across eta 0.3 / 0.6 / 1.0 with 35.8% max ADV participation, and at $1B it is -0.78 / -1.90 / -3.38 with 358% max participation (research_log) - participation that cannot actually be executed.
8. The advertised usable capacity of "roughly $10-100M" is contradicted by the source's own capacity text ("mid/conservative eta caps it at ~$10-30M") and by the $100M row (research_log) - see contradictions.
9. Alpha is concentrated on the expensive-to-borrow short side: alpha IR 1.37 short versus 0.18 long, in low-price $5-25 names, with borrow explicitly not modeled (memo sections 6.2 and 9.1).
10. Turnover stays at 0.23 per day even after smoothing (roughly 57x per year on the sum-of-absolute-weight-change convention), so results are dominated by the assumed cost per unit turnover.
11. The source itself calls flat 7 bps anachronistic post-2001 decimalization, i.e. the early sample is overcharged and the recent sample depends on 2-5 bps execution (research_log).
12. One of the three pre-registered Phase 2 hypotheses (volume conditioning) was rejected by its own diagnostic (memo section 8.1).
13. Earnings exclusion buys gross Sharpe 0.90 -> 1.03 at roughly +16% turnover, leaving break-even unchanged (memo section 8.2).
14. PCA residualization improves volatility (6.0% -> 4.3%) rather than per-trade edge; break-even moves only 8.5 -> 8.9 bps (memo sections 8.3-8.4 and Table 3).
15. The Phase 2 combined candidate has no gross edge on the spent 2019-2024 window (gross -0.07, net -0.64 at 7 bps) (memo section 8.4).
16. The 2019-2024 holdout was unsealed during Phase 1, so the Phase 2 check is explicitly non-independent; the only genuinely fresh window (2025 onward) does not yet exist in the source (memo sections 8.4 and 9.1).
17. Cost-range reporting mismatch: README, memo section 9.1 and research_log all say "2-10 bps sensitivity" while `scripts/cost_sensitivity.py` sweeps 0-15 bps and the research_log table lists 0 and 12 bps - see contradictions.
18. Turnover-reduction claim mismatch: "approximately/roughly halves turnover" versus the Table 1 step 0.64 -> 0.23 (-64%) - see contradictions.
19. The declared delisting-return sensitivity {0.0, -0.30, -0.55} ("main table" in research_log, `delisting.sensitivity` in `config.yaml`) has no printed result anywhere in memo, README, research_log or the committed figures - data gap.
20. Dependency fragility: with the current unpinned resolution (pandas 3.0.6) one of the 37 tests fails (our run, 2026-09-28), so the green CI badge is a snapshot of a moving dependency set.
21. The results are not externally reproducible from the repository alone: raw CRSP/Compustat inputs are absent and non-redistributable.
22. No t-statistics, standard errors or confidence intervals are reported for the headline IS/OOS Sharpe values in the memo; the only selection-adjusted statistic is the deflated Sharpe ratio.
23. Zero stars, zero forks, one contributor, no preprint/journal/peer-review statement, and no third-party replication identified (GitHub API read 2026-09-28) - publication and replication status `not stated in source`.
24. Regime dependence: worst episodes are momentum extremes (2000 peak, 2009 rebound, calm 2003-2007 bull) and the edge lives in high-volatility/high-dispersion states (memo section 6.3), so a volatility-regime shift can invert results without any parameter decay.

## Falsification plan

Every threshold below is `research-defined` (our acceptance/failure cutoffs), and any operational substitution not in the source is `research-proposed`.

- F1 Reproduction gate (`research-defined`): rebuild the panels from our own WRDS pull at the pinned commit and rerun `scripts/run_backtest.py`, `oos_evaluation.py`. Fail if IS gross Sharpe differs from 0.90 by more than 0.10, or IS/OOS break-even differs from 11.3/4.2 bps by more than 1.5 bps. Action: record reproduction failure and stop downstream consideration.
- F2 Frozen forward test: run the frozen `config.yaml` specification on 2025-01-01 onward data for at least 24 months with no retuning. Fail if net Sharpe at 7 bps <= 0 or break-even < 7 bps. Action: reject the strategy as non-viable under current costs.
- F3 Cost ladder: recompute IS and OOS net Sharpe at 0/2/5/7/10/15/20 bps per unit turnover. Fail if OOS net Sharpe at 5 bps <= 0 (the source already reports -0.04, so this test is expected to fail as published). Action: report cost fragility as confirmed.
- F4 Borrow audit: apply an annualized borrow-fee ladder of 0/50/100/200 bps on short-leg market value (`research-defined` values), focusing on the $5-25 short names. Fail if IS break-even drops below 7 bps or OOS break-even drops below 2 bps. Action: treat the short-side alpha as unimplementable without a borrow screen.
- F5 Execution-realism replay (`research-proposed`): replace the same-close fill with next-open and VWAP-with-latency fills. Fail if break-even falls by more than 30% (`research-defined`). Action: restate the whole ladder under realistic fills.
- F6 Capacity and participation audit: recompute capacity with 1% and 5% ADV position caps plus a trade/ADV (not position/ADV) participation cap. Fail if the net-positive frontier at eta 0.6 is below $10M (`research-defined`). Action: declare capacity sub-scale.
- F7 Component ablation: rerun raw reversal vs market-residual vs sector-LOO, and EWMA halflife {2,3,5,10} (source-declared grid). Fail the mechanism claim if residualization and smoothing do not each lift break-even in the replication. Action: attribute the result to a single component or drop it.
- F8 Placebo test: 1,000 circular shifts of the signal panel. Fail if the observed IS break-even does not exceed the 95th percentile of the placebo distribution (`research-defined`). Action: treat the in-sample edge as indistinguishable from noise.
- F9 Leakage audit: independently re-derive the eligibility mask, delisting attachment and `w.shift(1)` timing. Fail on any instance where a position vanishes from PnL or a weight earns same-bar returns. Action: block the record from any downstream use.
- F10 Delisting sensitivity: run the source-declared grid {0.0, -0.30, -0.55} and print the missing table. Fail if IS break-even moves by more than 2 bps across the grid (`research-defined`). Action: close the source's data gap and note the sensitivity either way.
- F11 Subperiod / regime stability: recompute break-even per rolling three-year window. Fail if the last three windows all sit below the 7 bps floor (`research-defined`; the source's own figure suggests this already fails). Action: treat decay as structural rather than episodic.
- F12 Dependency gate: pin `requirements.txt` and require 100% of the 37 tests to pass on both the pinned set and the current latest set (`research-defined`). Currently failing under pandas 3.0.6. Action: no adoption of the code base until green.
- F13 Selection control: recompute the deflated Sharpe with the full trial count including every grid disclosed in research_log. Fail if DSR < 0.95 (`research-defined`). Action: treat reported performance as selection-inflated.
- F14 Alternative-universe replication: repeat on the source-declared top-500 and top-1500 tiers and on a second point-in-time data source. Fail if the sign of OOS net Sharpe at 7 bps flips across tiers (`research-defined`). Action: mark the result universe-fragile.

## Crypto portability

`unproven`. The source tests US cash equities only and makes no crypto claim. A port would be a `research-proposed` hypothesis, not evidence, and needs: a cross-sector peer structure replacing two-digit SIC (crypto has no SIC mapping, so sector baskets or factor clusters would be a Scout-defined proxy); no direct analogue of the earnings-announcement exclusion; treatment of crypto-specific frictions that this record lists as data gaps even in their own setting - 24/7 sessions versus US trading days and daily bar boundaries, perpetual funding and margin financing for the short leg, venue fragmentation and per-venue liquidity, mark/index price versus last price, coin borrow availability and recall risk, listing survivorship in a point-in-time top-N universe, and thin-tail market impact. Adjacent crypto reversal/residual records exist (see Related) but are different sources with different mechanisms, so they do not transfer validation to this record.

## Limitations

- `underspecified`: order type, fill price, latency, session/timezone convention, spread model, margin/financing, tax treatment, path-dependent participation cap, and any real borrow-cost figure.
- `data gap`: raw CRSP/Compustat inputs absent from the repository; the declared delisting sensitivity table is never printed; t-statistics/confidence intervals for headline Sharpe values are absent; publication/peer-review status not stated.
- `not independently reproduced`: all performance numbers (source-reported only); only the test suite was executed by us.
- `unproven`: every capacity figure, since it depends on one square-root impact parameterization with an acknowledged uncertain eta.
- Internal contradictions: five, listed in frontmatter, all unreconciled by the source.
- Source quality: a single-author public repository with zero stars/forks and no preprint or peer review; CI is unpinned and currently rotting under pandas 3.0.6.
- Incremental value of this capture is the falsification story (decay, cost ladder, capacity ceiling, short-side borrow caveat, pre-registered negative holdout) for a well-known anomaly, not a tradable signal.
- Dedup: canonical source identity is unique in this repository; mechanism-adjacent records are listed below and differ in source identity and in at least one of mechanism, signal construction, universe/market type or horizon.

## Implementation status

`implementation_status: not-implemented`. Nothing has been implemented in our research stack: no strategy family, no Qlib or other backtest run of our own, no Paper, Testnet or Live activity, no candidate-pool entry, no Hermes Wiki Brain write, and no Kanban task. The only local action taken by this run was cloning the pinned repository and running its own test suite (see Independently reproduced). The source repository itself contains a Python research/backtest codebase, not an execution system.

## Adoption boundary

Presence of this record in the staging repository means only normalized research material. It does not mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed any full-backtest validation of ours; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. Crypto portability is `unproven` and is not authorization to trade. Any adoption, implementation or approval decision must be a separate, explicit, reviewed step based on this record plus current sources.

## Related Wiki records

Repository records (same broad family, different source identity and mechanism):

- [[sp500-avellanada-lee-residual-reversion-implementability-falsification-2026-09-13]] - Avellaneda-Lee s-score residual reversion on S&P 500 with an implementability falsification frame; different signal construction (OU s-score) and different universe.
- [[fourier-residue-sign-magnitude-equity-reversal-decomposition-2026-09-04]] - Fourier residue decomposition of equity reversal; microstructure-decomposition mechanism rather than a sector-residual plus smoothing ladder.
- [[lstm-learnable-sector-embeddings-cross-sectional-reversal-2026-09-02]] - learned sector embeddings with an LSTM; deep-learning signal construction versus a linear residual plus EWMA.
- [[vol-conditional-liquidity-provision-reversal-micro-price-execution-overlay-2026-09-23]] - volatility-conditional liquidity provision with a micro-price execution overlay; execution-layer-first mechanism.
- [[crypto-residual-momentum-market-beta-neutralization-2026-09-11]] - residual momentum (not reversal) in crypto with market-beta neutralization; different market, direction and horizon.

Hermes Wiki Brain pages (verified read-only via `kb_search` on 2026-09-28):

- [[quant/lstm-learnable-sector-embeddings-cross-sectional-reversal-2026-09-02]]
- [[quant/crypto-residual-momentum-market-beta-neutralization-2026-09-11]]
- [[quant/crypto-perpetual-pca-factor-residual-reversion-falsification-2026-09-12]]
- [[quant/crypto-stat-arb-cointegration-fdr-tiering-drifting-hedge-turnover-2026-09-13]]
- [[quant/crypto-world-order-flow-cross-sectional-quintile-weekly-2026-08-31]]

No Wiki Brain page exists for this source identity; the pages above are adjacent (reversal/residual/turnover themes) and were not used to fill any field in this record.

## Sources

- https://github.com/andrewzhang615-star/equity-statarb/tree/f65193666d16c7d13a925266a31e4158568d5804 (repository at the pinned commit; observed via `git ls-remote` on 2026-09-28)
- https://github.com/andrewzhang615-star/equity-statarb/blob/f65193666d16c7d13a925266a31e4158568d5804/README.md (read in full 2026-09-28)
- https://github.com/andrewzhang615-star/equity-statarb/blob/f65193666d16c7d13a925266a31e4158568d5804/reports/memo.md (179 lines, Tables 1-3 and sections 1-9.1, read in full 2026-09-28)
- https://github.com/andrewzhang615-star/equity-statarb/blob/f65193666d16c7d13a925266a31e4158568d5804/reports/oos_summary.txt (one-shot OOS summary, read 2026-09-28)
- https://github.com/andrewzhang615-star/equity-statarb/blob/f65193666d16c7d13a925266a31e4158568d5804/research_log.md (772-line dated experiment ledger; cost, capacity, subperiod, leg, tier and participation entries read 2026-09-28)
- https://github.com/andrewzhang615-star/equity-statarb/blob/f65193666d16c7d13a925266a31e4158568d5804/config.yaml (67 lines, all fixed parameters, read in full 2026-09-28)
- https://github.com/andrewzhang615-star/equity-statarb/blob/f65193666d16c7d13a925266a31e4158568d5804/src/backtest/engine.py (weight timing, turnover and cost application, read 2026-09-28)
- https://github.com/andrewzhang615-star/equity-statarb/blob/f65193666d16c7d13a925266a31e4158568d5804/scripts/cost_sensitivity.py (cost sweep grid, read in full 2026-09-28)
- https://github.com/andrewzhang615-star/equity-statarb/blob/f65193666d16c7d13a925266a31e4158568d5804/scripts/capacity.py (square-root impact grid, read 2026-09-28)
- https://github.com/andrewzhang615-star/equity-statarb/blob/f65193666d16c7d13a925266a31e4158568d5804/requirements.txt (unpinned dependency list, read 2026-09-28)
- https://github.com/andrewzhang615-star/equity-statarb/blob/f65193666d16c7d13a925266a31e4158568d5804/.github/workflows/ci.yml and https://github.com/andrewzhang615-star/equity-statarb/blob/f65193666d16c7d13a925266a31e4158568d5804/.github/workflows/python-app.yml (unpinned CI installs, read 2026-09-28)
- https://api.github.com/repos/andrewzhang615-star/equity-statarb (repository metadata, contributors and Actions run conclusions; read 2026-09-28)

Literature cited inside the source (not independently read for this record, recorded only as the source's own references): Lehmann (1990); Lo and MacKinlay (1990); Shumway (1997); Almgren, Thum, Hauptmann and Li (2005); Toth et al. (2011); Avellaneda and Lee (2010); Bailey and Lopez de Prado (2014); Bernard and Thomas (1989); Campbell, Grossman and Wang (1993); Harvey, Liu and Zhu (2016).
