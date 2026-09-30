---
schema: strategy-research-record-v1
title: Inverse-Volatility Fund-of-Strategies Combination Across Equity, Crypto and Pairs Sleeves with a 10 Percent Vol-Target Overlay
created: 2026-10-01
updated: 2026-10-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-01
sources:
  - https://github.com/SashRajj/QuantBook/tree/d164dd8929e7aaffd7d24ae57ab9ac2e66098de8
  - https://github.com/SashRajj/QuantBook/blob/d164dd8929e7aaffd7d24ae57ab9ac2e66098de8/README.md
  - https://github.com/SashRajj/QuantBook/blob/d164dd8929e7aaffd7d24ae57ab9ac2e66098de8/multi_strategy.py
  - https://github.com/SashRajj/QuantBook/blob/d164dd8929e7aaffd7d24ae57ab9ac2e66098de8/helper.py
  - https://github.com/SashRajj/QuantBook/blob/d164dd8929e7aaffd7d24ae57ab9ac2e66098de8/config.yaml
  - https://github.com/SashRajj/QuantBook/blob/d164dd8929e7aaffd7d24ae57ab9ac2e66098de8/.gitignore
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "C1: the crypto cross-sectional momentum HAC t is printed as 1.51 in the headline results table (README line 34, column HAC t) and as 1.56 in the crypto section prose (README line 183). Both are described as the same HAC t for the same optimised standalone crypto momentum sleeve. Unreconciled."
  - "C2: the headline combined OOS Sharpe of 0.94 is labelled net of 5 bps/side in the combiner section (README line 277), while the headline cost statement says costs are 5 bps/side on equity and 10 bps/side on crypto (README line 24). The combination contains a crypto sleeve priced at 10 bps/side, so the two descriptions of the cost basis behind the same 0.94 number are inconsistent."
  - "C3: the realism paragraph claims the pipeline reports t = 0.21 for the strategy a no-cost backtest would report as t = 4.53 (README lines 68-69). t = 0.21 is the notebook 01 rank-weighted mean-reversion figure (README line 29), while the only 4.53 in the document is the notebook 09 pairs selection-window HAC t (README lines 40 and 234). The pairing of the two numbers as before/after-cost readings of one strategy is not supported elsewhere in the source."
  - "C4: the source states that Bonferroni correction at family-wise 5% over roughly 65 evaluated configurations makes the bar |t| > 3.0 (README lines 51-53). Research-computed, a two-sided Bonferroni critical value at family-wise 5% over 65 tests is 3.3636 (normal approximation), and a two-sided bar of exactly 3.0 corresponds to about 18.5 tests. The stated method and the stated critical value are inconsistent with each other."
---

# Inverse-Volatility Fund-of-Strategies Combination Across Equity, Crypto and Pairs Sleeves with a 10 Percent Vol-Target Overlay

## Provenance

Source identity (primary source, read directly this run):

- Repository: https://github.com/SashRajj/QuantBook
- Immutable commit: `d164dd8929e7aaffd7d24ae57ab9ac2e66098de8` (default branch `main`, HEAD at fetch time), commit date `2026-05-26T21:29:17Z`, git author `Sashrik Rajesh`, parent commit `96789881f0b9306ea9e337d91421961b0296600d`, message `Re-execute all 11 notebooks fresh end-to-end`.
- Repository metadata from the GitHub REST repository object at fetch time: `created_at 2026-05-11T14:23:09Z`, `pushed_at 2026-05-26T21:29:19Z`, `updated_at 2026-09-21T07:22:13Z`, `stargazers_count 1`, `forks_count 0`, `open_issues_count 0`, `license: null`, `default_branch main`, `size 9980` KB, `language Jupyter Notebook`, `archived false`, `disabled false`.
- Recursive tree at that commit: `truncated: false`; 9 top-level blobs, 11 notebooks under `research/`, 2 test files, 1 cpp directory. No `LICENSE` file anywhere in the tree. No `data/` and no `logs/` entries: `.gitignore` explicitly excludes `data/` (comment: `Data (regenerated from download_sp500.py)`), `logs/`, `*.jsonl` and `_rerun_logs/`.
- Publication status: **not a paper**. No arXiv id, no DOI, no journal reference, no preprint landing page and no peer-review statement anywhere in the source. One commit message (`8c052dc17929d8c2efef04e96967a605f9f7b7ad`, `Notebook 10: add paper figures (Fig 1-4); align README with paper`) refers to a paper, but no paper artifact exists in the tree, so that reference is a data gap. The README contains no author or affiliation statement; the only identity evidence is the git author name `Sashrik Rajesh`.

Pinned files, each fetched from `raw.githubusercontent.com` at the immutable commit and byte-matched against the tree sizes (SHA-256 computed locally over the downloaded bytes):

| file | bytes | SHA-256 | git blob | read status |
|---|---:|---|---|---|
| `README.md` | 24908 | `3dcf16bb3f236a553c7597df0ee4a1b0e3e7a871269813036593c5831161c673` | `32751c6913faba0b05a715b7e1ff014cfc607d2d` | read end to end, 489 lines |
| `multi_strategy.py` | 10263 | `ad955c9db868cb8b755b4e2cc734d2baa93ca134adcf6442d2909aab4f5a249e` | `046c9de0f319e45aab8007de45d2e08db110bf87` | read end to end, 251 lines |
| `helper.py` | 26726 | `8d5943bb3fea1ea801f7dc5b56e8925d940e2aa8e6ed8d3d6987dbf71ddd2723` | `9823216ca6b7f918ce3172bc5f98ab8c164fd16d` | lines 218-377 read (port_ret, vol_target, stats, ic) plus symbol index of lines 377-463; the rest not read |
| `config.yaml` | 2541 | `f145dd917c872c473856a2535abb4e3c7c9da6eac64e3e33673c1048ca82ab42` | `1a70cc49871aa1be3dd6decb773441f5bf918dd3` | read end to end, 56 lines |
| `signals.py` | 4632 | `8255665fd6c18b5bd3a5d1b89351ca50c465498769e9ef05a44410c97819d5da` | `84daf908417b9587214c1df3056250cf3642be5f` | not read; pinned for identity only |
| `.gitignore` | 364 | `79f2c48308ff27c81a1b791ed3b1a38e8c76b169a06f56eb4685c076bc29b3df` | `a0688d4f876029199816bee9afb8c94c4e15c0d0` | read end to end |

Notebook blobs pinned by sha and size but **not parsed this run** (they are where most printed numbers are ultimately produced): `research/04_portfolio.ipynb` 424217 bytes blob `f1a5e85de640cce25eab71fa874159d99588dc40`; `research/07_crypto.ipynb` 248780 bytes blob `d771bf12dcff1a6fb48c9dedaa8c4e2ef1959788`; `research/09_pairs.ipynb` 391359 bytes blob `8349636b54d3d059e6733fee907c376197c6e035`; `research/10_multi_strategy.ipynb` 747248 bytes blob `694dc06b79757eddf5c12ebc0f7db6d693a8d4d4`. Every performance figure in this record is therefore source-reported from README prose and tables, not extracted from notebook output cells.

Data artifacts referenced by the code but absent from the repository because `data/` is gitignored: `sp500.parquet`, `signal_01_mean_reversion.parquet`, `signal_02_momentum.parquet`, `signal_03_low_volatility.parquet`, the `weights_*_oos.parquet` panels, `pnl_07_crypto_volmom.parquet`, `pnl_09_pairs_oos.parquet` and `data/weights_combined_oos.parquet` (`config.yaml` line 56). **data gap**: the headline combination cannot be recomputed from the published tree alone.

What was done and not done: no repository code was executed, no notebook was executed, no market data was downloaded from yfinance, Binance.US, Wikipedia or any other vendor, no dependency was installed, and no third-party program was run. Deterministic text searches, arithmetic on the pinned text, and arithmetic on calendar/critical-value identities are the only computation performed.

Pre-write dedup: `grep -rliF` across all `*.md` in the checkout plus a hidden-inclusive `rg -uuu` sweep for `SashRajj`, `Sashrik`, `QuantBook`, `github.com/SashRajj`, `crypto-momentum-backtest`-style identity strings, `pnl_07_crypto_volmom`, `weights_combined_oos`, `ic_weighted_combine`, `combine_weights` and `inverse-vol-fund-of-strategies` each returned **0 files** before this write; `coverage_manifest.csv` returned 0 matches for the same identity tokens; positive control `novy-marx` returned 57 files among 2672 markdown files in the checkout. `git log --oneline -20` was used as a convenience glance only, not as the dedup proof.

## Economic mechanism

### Source-reported

The source frames the combination as diversification plus risk-budgeting, not as a new premium (README lines 12-20, 249-252, 282-288):

- Three sleeves are combined: an equity sleeve (mean reversion, momentum and low volatility on point-in-time S&P 500 membership), a crypto sleeve (five cross-sectional signals on top-30 USDT pairs, of which volume-adjusted momentum is the one that enters the combination) and a pairs sleeve (cointegration z-score mean reversion within S&P 500 sub-industries).
- The source reports sleeve cross-correlations of equity vs crypto `-0.04`, equity vs pairs `-0.23`, crypto vs pairs `-0.02` (README line 251) and states that the lift comes from inverse-volatility weighting across these uncorrelated sleeves plus a 10 percent annualised vol-target overlay, `not from search or tuning` (README lines 16-17, 287-288).
- The source explicitly downgrades its own overlay claim: the vol-target overlay `does not add any further Sharpe` because inverse-vol alone is already at 0.95 and the 10 percent target produces no meaningful rescaling (README lines 283-286). It also notes that equal-weight is dragged down by the high-kurtosis crypto sleeve, whose combined-PnL kurtosis is reported as 191 (README lines 260-262).
- The source states that none of the combination rules is search-found: `the three rules are textbook and the overlay is the standard 60-day inverse-vol scale` (README lines 286-288), and `multi_strategy.py` documents the same claim in its module docstring (lines 1-12).

### Research interpretation

Falsifiable restatement of the mechanism, with component roles:

- Regime: none. There is no regime filter, no market-state gate and no conditional activation anywhere in the combination layer.
- Combination rule (primary claim): capital is allocated across the three sleeve PnL streams in proportion to `1 / sigma_i`, where `sigma_i` is the trailing 60-trading-day realised standard deviation of sleeve `i`, with the weight panel shifted by one day before it is multiplied into sleeve returns (`multi_strategy.py` lines 137-159, `lookback=60`, `min_periods=lookback`, `held = w.shift(1)` at line 156).
- Risk overlay: a 10 percent annualised vol target computed on a 60-day trailing realised vol, shifted one day, with leverage clipped to 5x and pre-warm-up rows zero-filled (`helper.py` lines 259-282).
- Alpha sources (not created by the combination): the three sleeves themselves. The combination layer is a pure risk-allocation mechanism; it can only re-scale and blend sleeve returns, never create a return stream the sleeves do not already contain.
- Hypothesis in falsifiable form: because sleeve correlations are small and negative-to-near-zero, inverse-vol weighting of the three sleeve PnLs produces a higher out-of-sample Sharpe than any single sleeve and than equal-weight, after each sleeve's own transaction costs, and this survives a family-wise multiple-testing correction.
- The source's own evidence does not establish the second half of that statement: it reports that nothing in the repository survives its own family-wise correction (README lines 54-56).

## Signal

Everything below is source-reported unless explicitly marked. Line references are to the pinned `README.md` unless another file is named.

Combination layer (exact, from `multi_strategy.py`):

- Formation timestamp: combination weights at date `t` are built from sleeve PnLs observed strictly before `t`; the rolling windows are shifted by one day before use (module docstring lines 9-11, `held = w.shift(1)` line 156, `held = weights.shift(1)` lines 207 and 217-231).
- Lookback: inverse-vol `lookback=60` days with `min_periods=lookback`, so the first 60 sleeve observations are burned in rather than partially used (lines 150-153). Minimum-variance uses `lookback=252` days of sleeve covariance, re-solved per day with cvxpy SCS and an explicit `sum(w)=1, w>=0` constraint (lines 162-210).
- Entry: no discrete entry. The combiner emits a daily weight vector over the three sleeve PnLs; `combine_equal_weight` is `df.mean(axis=1)` (lines 124-134).
- Exit: none; the panel is an inner join of the three sleeve calendars (lines 103-109, 116-121).
- Holding period: daily, continuous. The source does not state a rebalance cadence for the combination beyond the daily PnL aggregation.
- Parameters: inverse-vol lookback 60; min-variance lookback 252; vol-target 0.10 with lookback 60, `ppy=252`, `max_leverage=5.0`; equity-sleeve cost constants `_EQUITY_TCOST_BPS = 5` and `_EQUITY_EXEC_LAG = 2` (`multi_strategy.py` lines 38-39); all are fixed constants in code, described by the source as non-searched (README lines 254-258, 286-288).

Sleeve signals (source-reported, README):

- Equity mean reversion: negated rolling z-score of price; hypothesis `short-horizon overreaction reverts in days-weeks` (line 124).
- Equity momentum: `12-1 month total return`; hypothesis `slow news diffusion -> 1-12 month trends` (line 125).
- Equity low volatility: negated rolling realised vol; hypothesis `leverage / lottery preferences underprice low-vol names` (line 126).
- Crypto candidates: mean reversion, momentum, low volatility, market-residual momentum and volume-adjusted momentum, the last given verbatim as `mean_return * sqrt(volume / rolling_mean_volume)` (lines 176-179).
- Pairs: selection window 2010-2017 within each GICS sub-industry with correlation > 0.65, Engle-Granger cointegration p < 0.05 on log prices and OU residual half-life in [5, 60] trading days; second tier same-sector correlation > 0.80; 33 pairs survive. Trading from 2018 uses a static OLS hedge ratio fixed from the selection window, a 60-day rolling z-score, entry at `|z| > 2`, exit at `z = 0`, hard stop at `|z| > 3.5`, gross-1 position per pair, per-pair PnL normalised by 120-day calibration vol, aggregate scaled to a 10 percent annualised vol target (lines 218-230).
- Optimised per-sleeve portfolios use `helper.Optimizer`, a per-date mean-variance program `minimise -alpha' w + w' Sigma w + lambda ||w - w_prev||_1` with optional dollar neutrality, per-name cap, gross leverage limit, long-only and ex-post vol scaling, Ledoit-Wolf shrinkage on a trailing window, and the transaction-cost penalty inside the objective (README lines 426-438).
- Combination-layer weights are equal-weight, inverse-vol or minimum-variance; the source states there is no parameter grid and no search over these rules (`multi_strategy.py` lines 1-12).

Items the source does not specify (underspecified): the exact rebalance cadence of the executed equity book beyond `daily`; the exact borrow rate used in any run; the exact crypto download window end; the exact definition of `top 30 USDT pairs by today's market cap`; the number of candidate configurations behind each notebook's `optimized` label; and the seeds used by the regime Monte Carlo (notebook 06) and the LightGBM model (notebook 08).

No operational rule in this record is Scout-generated. Anything not stated by the source is labelled `research-proposed` and appears only in the falsification plan.

## Required data

- Instrument and universe (equity): S&P 500 constituents, reconstructed point-in-time from the Wikipedia historical changes table; the union of all ever-members forms a download universe of about 830 tickers against 500 names today, with a date-by-date membership mask so positions only open in names actually in the index on that date (README lines 445-449).
- Instrument and universe (crypto): top 30 USDT pairs on Binance.US, curated list with per-date masking that drops names with no data yet (README lines 167-171).
- Instrument and universe (pairs): S&P 500 names screened by GICS sub-industry correlation and cointegration, 33 survivors (README lines 220-223).
- Venue and market type: US equities via yfinance daily OHLCV; crypto spot OHLCV from Binance.US; the source states that crypto dollar neutrality is `implicit - spot shorting is limited` and is intended to be expressed with perpetual futures (README line 173).
- Timeframe: daily bars, close-to-close (README line 476). Equity and pairs are business-day; crypto is 365 days per year (README line 172).
- Sample windows: equity download window fixed in `download_sp500.py` as 2005-01-01 to 2026-04-01 so outputs are reproducible (README lines 105-107); crypto `2019-09 -> present` with the end not pinned (README line 167, data gap); pairs selection 2010-2017, trading 2018-2026 (README lines 220, 225); headline combination OOS 2021-04 to 2026-03 over 1,255 trading days after a 60-day inverse-vol warm-up on a sleeve panel starting 2021-01-05 (README lines 14-15).
- Benchmark: SPY, used as the regressor for the alpha and beta HAC statistics (README lines 18, 277-279; `helper.py` lines 337-348).
- Fields used: adjusted close and volume for signals, ADV for the risk gate, index membership dates, and sleeve PnL streams.
- Point-in-time requirements: index membership is point-in-time; covariance refits on a trailing 252-day window refit monthly inside `run()`, with a test asserting that perturbing future returns no longer changes past weights (README lines 461-464); execution lag `exec_lag=2` on equities and `exec_lag=1` on crypto.
- Missing data: `clean_prices` masks any same-day absolute return greater than 100 percent to catch yfinance adjusted-close errors on delisted tickers (README lines 458-460); `helper.py` mean-fills in-window signal entries (line 25) and zero-fills non-finite signal values (line 47); crypto per-date masking drops names without data.
- Fee and funding needs: 5 bps/side equity, 10 bps/side crypto, 5 bps/side/leg pairs; short-book holding fee at a configurable borrow rate; crypto perpetual funding acknowledged but not modelled. Each is addressed in Execution assumptions.
- Timestamps and timezone: not stated in the source; `config.yaml` line 7 says all times are UTC unless otherwise noted. data gap for bar boundary convention.

## Execution assumptions

Source-reported cost and execution model, determined from the Methods-equivalent material (README sections `Realism corrections`, `Multi-strategy combiner`, `Remaining limitations`, plus `helper.py` `port_ret`, `multi_strategy.py` constants and `config.yaml`):

- Signal-to-order timing: `exec_lag=2` on equities, meaning a signal computed at the close of day `t` is acted on at the close of `t+1` and earns the `t+1 -> t+2` return; `exec_lag=1` on crypto; `exec_lag=0` is described as a zero-latency diagnostic only (`helper.py` lines 226-230, README lines 24-25, 172, 450-451).
- Transaction cost function: `tc = (long_turn * tcost_bps + short_turn * tcost_short_bps) / 10000` where long and short turnover are the sums of absolute day-over-day changes of the clipped long and short weight blocks; `tcost_short_bps` defaults to the long value (`helper.py` lines 237-251). Applied values: 5 bps/side on equity (README line 24, `_EQUITY_TCOST_BPS = 5`), 10 bps/side on crypto (README lines 24, 172), 5 bps/side/leg on pairs (README line 229).
- Borrow: `borrow = gross_short * borrow_bps_annual / 252 / 10000` with `borrow_bps_annual` defaulting to 0 (`helper.py` lines 221-256). README line 453 says a daily holding fee on the short book at a configurable borrow rate exists, but the rate actually used in any run is never stated. **data gap**; the default of 0 must not be read as evidence that zero borrow was charged.
- Combination-layer cost: **none**. `combine_inverse_vol`, `combine_equal_weight`, `combine_min_variance` and `evaluate_combination` contain no cost term, and `evaluate_combination` calls `stats()` with `weights=None`, so no combination-layer turnover is even reported (`multi_strategy.py` lines 124-251). Changing inverse-vol weights therefore reallocates capital between sleeves for free.
- Slippage, commission, spread, impact: the research backtests charge only the bps-per-turnover term above. README line 474 states `No market-impact cost. Transaction cost is per-bps of turnover, no square-root or non-linear size dependence.` README line 476 states intraday latency, opening auctions and tick-level effects are out of scope. A separate execution-layer split exists for the paper broker only: `slippage_bps: 4.0` plus `commission_bps: 1.0`, documented as `round-trip total = 2 * (slippage + commission) = 10 bps`, chosen to match `port_ret(tcost_bps=5)` (`config.yaml` lines 12-19).
- Funding: crypto perpetual funding `acknowledged but not modelled` (README lines 174, 187). **data gap**, not zero.
- Fill model: the research side is a close-to-close bar model with deterministic next-lag weights; the execution layer uses a `PaperBroker` with deterministic fills and configurable slippage/commission (README lines 354-356).
- Order type and latency: execution layer supports `market`, `twap` (8 slices) and `vwap` (`config.yaml` lines 29-38); latency is not modelled in the backtest.
- Leverage, limits, capacity: research-side dollar-neutral optimisation with 2 percent per-name cap (README line 141); execution-side pre-trade gates `max_gross_leverage 1.5`, `max_net_exposure 0.10`, `max_position_pct 0.05`, `max_positions 200`, `max_adv_participation_pct 0.05` vs 20-day ADV, `max_daily_turnover_pct 2.0`, `drawdown_kill_pct 0.15`, with any single breach rejecting the entire basket (`config.yaml` lines 40-48, README lines 365-370).
- Partial fills and failures: stale feed hard-fails the rebalance and the runner exits non-zero; positions are never silently shrunk on a stale feed (README lines 372-380). Reconciliation compares internal book to broker with a 5 percent price-divergence threshold (`config.yaml` lines 50-52).
- Capacity: **not stated in source**. No ADV-based capacity study, no participation-curve analysis and no AUM ceiling appear anywhere in the pinned corpus (census: `capacity` 0 occurrences).

## Evidence

### Source-reported

All figures below are third-party claims from the pinned `README.md` at commit `d164dd8929e7aaffd7d24ae57ab9ac2e66098de8`. None has been independently reproduced.

Headline combination (README lines 12-20 and 270-280), OOS 2021-04 to 2026-03, 1,255 trading days, HAC Newey-West lag 5, two-day execution lag on equities, costs 5 bps/side equity and 10 bps/side crypto:

| configuration | Sharpe | skew | kurt | HAC t | max DD | ann vol |
|---|---:|---:|---:|---:|---:|---:|
| equal-weight | 0.92 | -0.57 | +10.15 | 2.35 | -16.2% | 17.74% |
| min-variance | 0.77 | -0.06 | +2.22 | 1.62 | -7.7% | 8.16% |
| inverse-vol | 0.95 | -0.05 | +1.35 | 2.47 | -7.6% | 8.70% |
| inverse-vol + 10% vol-target | 0.94 | -0.00 | +1.90 | 2.39 | -7.9% | 10.38% |

Also reported for the headline: SPY beta `-0.05` (README lines 13, 278); it `clears |t| > 2 HAC against SPY (HAC t = 2.39)` but `not the family-wise Bonferroni bar across the 65 strategy configurations evaluated` (README lines 18-20, 279-280); sleeve cross-correlations equity/crypto `-0.04`, equity/pairs `-0.23`, crypto/pairs `-0.02` (README line 251); equal-weight combined-PnL kurtosis 191 (README lines 260-262).

Per-sleeve results (README lines 27-43), same cost and HAC framework:

| notebook | strategy | Sharpe | alpha (ann) | HAC t | DSR | passes abs(t)>2 |
|---|---|---:|---:|---:|---:|:---:|
| 01 | rank-weighted mean reversion (IS) | 0.17 | +0.28% | 0.21 | - | no |
| 01 | optimised mean reversion (IS / OOS) | 0.12 / -0.45 | -1.54% / -11.1% | -0.40 / -1.80 | approx 0 | no |
| 02 | optimised momentum (IS / OOS) | -0.30 / 0.09 | -3.65% / +2.55% | -0.60 / 0.27 | - | no |
| 03 | optimised low-vol (IS / OOS) | -0.68 / -0.52 | -7.04% / +2.56% | -1.65 / 0.34 | - | no |
| 04 | combined equity (IS / OOS) | -0.30 / -0.17 | -2.02% / +1.48% | -0.36 / 0.16 | - | no |
| 07 | standalone crypto momentum (opt) | 0.87 | +34.1% | 1.51 | - | borderline |
| 07 | standalone crypto volume-adjusted momentum (opt) | 0.83 | +51.1% | 2.15 | - | yes |
| 07 | crypto combined IC-weighted (IS / OOS) | 0.15 / -0.50 | +5.3% / -20.2% | 0.26 / -0.74 | 0.16 / 0.03 | no |
| 08 | ML decile spread, 5d rebal (IS) | 0.99 | +28.94% | 2.47 | 0.70 | yes |
| 08 | ML decile spread (OOS) | -0.01 | -0.86% | -0.06 | 0.03 | no |
| 08 | ML optimised portfolio (full) | 0.26 | +1.46% | 0.45 | - | no |
| 09 | pairs selection 2010-2017 (diagnostic) | 1.68 | - | 4.53 | - | n/a |
| 09 | pairs IS 2018-2020 | 0.41 | +0.7% | 0.20 | - | no |
| 09 | pairs OOS 2021-2026 | 0.64 | +5.4% | 1.12 | - | no |
| 11 | options/variance-risk-premium cross-sectional (IS / OOS) | 0.18 / 0.12 | +1.50% / +1.12% | 0.48 / 0.25 | 0.008 | no |

Other source-reported specifics: crypto volume-adjusted momentum `HAC alpha t = 2.15 vs BTC - the only crypto strategy past |t| > 2`, with cross-sectional momentum borderline at t = 1.56 (README lines 181-184); pairs per-year Sharpes 2018-2026 of `-0.03, 1.34, 0.36, 2.07, -0.23, 0.63, 0.69, 0.43, 1.83` (README line 237); pairs selection-window 1.68 versus IS/OOS, which the source calls `what overfitting in pair selection looks like even with a stationarity test and an economic prior` (README lines 239-243); the options sleeve's signal sign was flipped from the literature direction after IS IC inspection and that binary choice is counted in `N_TRIALS = 16` for DSR (README lines 309-311); the ML walk-forward retrains on the prior 5 years with an 11-day embargo and predicts the next year, with a full OOS prediction panel spanning 2010-2026 (README lines 203-205); DSR and PSR implementations follow Bailey and Lopez de Prado 2012/2014 (`helper.py` lines 438-463).

The source's own headline conclusions: `Nothing in this repo survives a family-wise multiple-testing correction` (README lines 54-56); `The classical equity factors don't pass at any significance bar. That is the project's main result.` (README lines 64-65); `Both fail OOS - the documented factor-decay pattern of the post-2020 era` (README lines 48-49); and on the execution layer, `The equity book's OOS HAC t is 0.16, so live-paper PnL is expected to be flat-to-negative net of costs` (README lines 326-328).

### Independently reproduced

not independently reproduced

Arithmetic-only consistency checks performed this run (research-computed; these are not a reproduction of the backtest, and no market data or repository code was used):

1. **Warm-up identity reproduced exactly.** Starting from the stated sleeve panel date 2021-01-05 (a Tuesday) and counting NYSE weekday sessions with a standard US holiday set, the 60th session is 2021-03-31, so the first day a non-null inverse-vol weight can be applied after `rolling(60, min_periods=60).std()` plus `shift(1)` is **2021-04-01**. This matches the stated OOS start of `2021-04` after a `60-day inverse-vol warmup on a 2021-01-05 sleeve panel`.
2. **Day count.** NYSE sessions from 2021-04-01 through 2026-03-31 inclusive compute to **1,256**, against the stated **1,255** (README line 14). One session of difference, consistent with a boundary or execution-lag convention; not resolvable from the published tree.
3. **Bonferroni critical value.** Two-sided Bonferroni at family-wise 5% over N=65 tests gives `norm.ppf(1 - 0.05/(2*65)) = 3.3636`; over N=64 it is 3.3594 and over N=66 it is 3.3678. A two-sided bar of exactly 3.0 corresponds to N = 18.5 tests. The source's stated bar of 3.0 (README line 53) is therefore looser than the method it names. No headline statistic is affected: the largest reported HAC t in the repository is 2.47, which clears neither 3.0 nor 3.3636, so the source's conclusion (`nothing survives`) is strengthened, not weakened, by the correction.
4. **Cost-schedule arithmetic.** The execution-layer split `slippage_bps 4.0 + commission_bps 1.0` gives `2 * (4 + 1) = 10` bps round trip, exactly the `2 * tcost_bps(5)` hurdle the source says it matches (`config.yaml` lines 12-19). Consistent.
5. **Combination-layer cost absence confirmed by reading.** No cost, turnover, fee, borrow or slippage term exists in `combine_equal_weight`, `combine_inverse_vol`, `combine_min_variance` or `evaluate_combination`; `evaluate_combination` passes `weights=None` to `stats`, so combination turnover is not reported either.
6. **Calendars.** The headline panel is an inner join of a 7-day crypto calendar with business-day equity and pairs calendars (`multi_strategy.py` lines 103-108), and `evaluate_combination` annualises with `periods_per_year=252` (line 220). A 252-day annualisation over 2021-04 to 2026-03 is consistent with the 1,255/1,256 session counts above; the crypto weekend returns excluded by the inner join are not quantified anywhere.
7. **README versus metrics.** Every headline number quoted in this record was located at a specific README line in the pinned file (0.94 at lines 12, 275, 277; 0.95 at 274, 284; 2.39 at 18, 275, 279; 2.15 at 35, 58, 182; 1.51 at 34; 1.56 at 183; 4.53 at 40, 69, 234; 0.21 at 29, 68; 1.68 at 40, 234, 241; 0.64 at 42, 236). No number in this record is carried over from a secondary summary.

Corpus census over the six pinned text files (69,120 characters total), counted case-insensitively: `transaction cost` 2, `tcost` 16, `slippage` 4, `spread` 8, `bid-ask` 0, `borrow` 8, `commission` 5, `fee` 16, `tax` 0, `funding` 2, `liquidation` 0, `leverage` 12, `margin` 1, `market impact` 0, `capacity` 0, `limit order` 0, `market order` 0, `participation` 2, `latency` 2, `turnover` 7, `newey` 2, `hac` 27, `p-value` 0, `bootstrap` 3, `benjamini` 0, `fdr` 0, `multiple-comparison` 1, `deflated` 5, `dsr` 8, `walk-forward` 3, `purge` 4, `embargo` 13, `look-ahead` 6, `survivorship` 3, `point-in-time` 6, `crypto` 30, `perpetual` 1, `24/7` 2, `sharpe` 55, `license` 0, `licence` 0, `seed` 0, `random` 0, `bonferroni` 3. Unmodelled frictions are recorded as data gaps, never as zero, wherever the census shows 0 but the README discusses the item elsewhere (for example market impact appears as `market-impact` with a hyphen at README line 474).

### Negative evidence

1. The headline combination fails the source's own family-wise correction: HAC t 2.39 against a bar the source puts at 3.0 (README lines 18-20, 51-56, 279-280).
2. Research-computed: the bar the source names is itself arithmetically loose; two-sided Bonferroni at family-wise 5% over 65 tests requires 3.3636 (see Independently reproduced item 3).
3. The source states outright that `nothing in this repo survives a family-wise multiple-testing correction` (README lines 54-56).
4. The combination layer charges **no cost** for the cross-sleeve reallocation that inverse-vol weighting implies, while the headline is labelled `net of costs` (code: `multi_strategy.py` lines 124-251; label: README lines 12, 277).
5. The equity sleeve entering the combiner is a **proxy**, not notebook 04's optimised output: `_equity_sleeve_pnl` docstring states that notebook 04 `does not persist the result` and that the IC-weighted mean of the three saved per-signal PnLs is `a defensible proxy` (`multi_strategy.py` lines 42-50).
6. The execution configuration describes `combined_equity` as `the IC-weighted combination of mean_reversion, momentum, low_volatility from notebook 04` (`config.yaml` lines 21-27) while `multi_strategy.py` says notebook 04's combined result is never written to disk. Two different objects are both called the equity sleeve.
7. Crypto weekend returns are dropped from the headline combination by the inner join of a 7-day crypto calendar onto business-day equity and pairs calendars (`multi_strategy.py` lines 103-108). The README never mentions this.
8. `data/` is gitignored, so none of the parquet inputs behind the headline number ships with the repository; reproducing 0.94 requires two download scripts, 11 notebooks and a C++-optional build (README lines 94-107, `.gitignore`).
9. Every individual equity sleeve fails: combined equity IS/OOS Sharpe -0.30 / -0.17 with HAC t -0.36 / 0.16; mean reversion 0.17 IS; momentum -0.30 / 0.09; low vol -0.68 / -0.52 (README lines 29-33).
10. The ML sleeve collapses out of sample: IS decile-spread Sharpe 0.99 with HAC t 2.47 and DSR 0.70 becomes OOS Sharpe -0.01 with t -0.06 (README lines 37-38, 209-210).
11. The pairs sleeve falls from a selection-window Sharpe of 1.68 with HAC t 4.53 to IS 0.41 and OOS 0.64 with alpha t 1.12 (README lines 40-42, 234-243).
12. The options/variance-risk-premium sleeve is null in both halves (0.18 / 0.12, DSR 0.008) and its signal sign was flipped after inspecting in-sample IC (README lines 43, 307-311).
13. The crypto survivorship caveat is the source's own: the volume-adjusted-momentum t = 2.15 is computed on the top 30 USDT pairs by **today's** market cap, so LUNA, FTT, UST and other 2021-22 blow-ups are structurally excluded from the long leg, and the source instructs the reader to treat the t-stat as upper-bounded (README lines 58-62).
14. Crypto perpetual funding is acknowledged but not modelled (README lines 174, 187). data gap.
15. The short-book borrow rate is configurable with a code default of 0 and no stated used value (README line 453, `helper.py` lines 221-256). data gap.
16. No market impact is modelled at all (README line 474).
17. Intraday latency, opening auctions and tick-level effects are out of scope (README line 476).
18. Residual survivorship: about 175 delisted tickers have no yfinance data, so the point-in-time membership mask records them but the strategy cannot trade them; the source calls this `reduced, not eliminated` (README lines 468-470).
19. Single-factor Ledoit-Wolf covariance rather than a structural risk model (README lines 471-473).
20. The Sharpe convention is raw `mean / std * sqrt(ppy)` with **no risk-free subtraction** (`helper.py` line 324) and the README never states a risk-free rate for the headline number. data gap for comparability with rf-adjusted Sharpes.
21. No p-values, no confidence intervals, no Benjamini-Hochberg or FDR control appear anywhere in the pinned corpus (census: `p-value` 0, `benjamini` 0, `fdr` 0); `bootstrap` appears only in the regime Monte Carlo notebook description (README lines 155-163), not for the headline.
22. No seeds and no randomness declaration in the pinned corpus (census: `seed` 0, `random` 0) although notebook 06 runs a Monte Carlo and notebook 08 trains LightGBM.
23. The crypto sleeve entering the headline inherits both the survivorship bias of item 13 and the funding omission of item 14, so the headline combination inherits them too.
24. Narrow crypto breadth: about 6 years of history centred on the 2021-22 boom-bust with 30 names against 500 (README lines 186-188).
25. Source quality: single-author self-published repository, 1 star, 0 forks, no `LICENSE` file (`license: null`) while the README openly invites `pip install` reuse (README lines 92-107), no paper artifact in the tree, no peer review, and identity available only as a git author name.
26. The notebook output cells where the reported numbers are actually produced were not parsed this run, so all performance figures here rest on README prose and tables.
27. The source expects its own live result to fail: `live-paper PnL is expected to be flat-to-negative net of costs. That's the point` (README lines 326-328).

## Falsification plan

Every threshold below is a **research-defined falsification threshold**; every operational choice below that is not literally in the source is marked **research-proposed**. The plan is designed so a failed gate cannot be rescued by retuning; see the no-retuning rule at the end.

- **F1 - Printed-value reproduction.** Rebuild `data/` from `download_sp500.py` and `download_crypto.py`, re-run notebooks 01-03, 07, 09 and 10 at the pinned commit, and recompute the headline row. Threshold (research-defined): absolute deviation of at most 0.02 in Sharpe, 0.10 in HAC t, 1.0 percentage point in max drawdown and 5 sessions in day count from the printed 0.94 / 2.39 / -7.9% / 1,255. Action on failure: mark every performance figure in this record unreproducible and set `confidence: low`.
- **F2 - Combination-layer cost gate (research-proposed).** Price the cross-sleeve reallocation turnover of the inverse-vol rule at the sleeve-appropriate schedule (5 bps/side for capital moving in or out of the equity and pairs sleeves, 10 bps/side for the crypto sleeve) and recompute the headline net Sharpe. Threshold: net Sharpe at or above 0.80. Action: if below, reject the phrase `net of costs` for the headline and restate it as gross-of-combination-cost.
- **F3 - Family-wise gate.** Enumerate the actual number N of strategy configurations evaluated across notebooks 01-11 and require `abs(t) >= norm.ppf(1 - 0.05/(2*N))` two-sided, plus a Benjamini-Hochberg FDR result at q = 0.10 (research-proposed as a companion report, not a substitute). Threshold: the headline must clear its own Bonferroni critical value. Action: if not, the combination is recorded as not distinguishable from selection luck.
- **F4 - Equity-sleeve object gate (research-proposed).** Recompute the combination twice, once with the IC-weighted proxy and once with notebook 04's optimised combined-signal PnL, and compare. Threshold: absolute Sharpe difference at most 0.05. Action: if larger, the headline is object-dependent and must be reported for both objects.
- **F5 - Calendar-alignment gate (research-proposed).** Rebuild the combination on a 7-day calendar that retains crypto weekend returns, and on the current business-day inner join. Threshold: absolute Sharpe difference at most 0.05. Action: if larger, the inner join is a material, previously undisclosed aggregation choice.
- **F6 - Sleeve-ablation gate.** Drop each sleeve in turn (equity, crypto, pairs) and recompute. Threshold: the three-sleeve inverse-vol combination must exceed the Sharpe of every two-sleeve subset and of the best single sleeve. Action: if a single sleeve or subset matches it, the diversification thesis is not supported by this sample.
- **F7 - Crypto-universe survivorship gate (research-proposed).** Rebuild notebook 07 on a point-in-time top-30 universe ranked by trailing market cap at each date, including names since delisted or collapsed. Threshold: volume-adjusted-momentum HAC t at or above 1.96 against BTC. Action: if below, treat the crypto sleeve's contribution to the headline as survivorship-inflated.
- **F8 - Borrow and funding gate (research-proposed).** Charge the short book at 100 / 200 / 500 bps annual borrow and charge crypto perpetual funding at the observed daily rate. Threshold: combined net Sharpe at or above 0.70 at the middle rung. Action: if below, the dollar-neutral crypto leg is not implementable as stated.
- **F9 - Cost ladder.** Re-run every sleeve at 5, 10, 20 and 50 bps per side. Threshold: combined Sharpe at or above 0.50 at 20 bps per side. Action: if below, the combination is a low-cost-regime artifact.
- **F10 - Benchmark gate.** Compare the combined net series against SPY buy-and-hold and against a 1/3-1/3-1/3 equal-weight of the three sleeves. Threshold: combined net Sharpe above both, with HAC alpha t at or above 2.0 versus SPY. Action: if not, the combination adds no value over trivial alternatives.
- **F11 - Deflated-Sharpe selection gate.** Compute DSR over the full configuration ledger (3 sleeves x 5 crypto signals x 3 combination rules x 2 overlay states x 4 cost rungs), using the repository's own `deflated_sharpe` implementation. Threshold: DSR at or above 0.95 (research-defined). Action: if below, record the headline as selection-affected.
- **F12 - Turnover and capacity gate (research-proposed).** Report combination-layer daily turnover, map it to an implied AUM ceiling at 5 percent 20-day ADV participation, and require the ceiling to exceed any intended deployment size. Threshold: capacity at least 10x the intended book. Action: if not, record capacity as the binding constraint.
- **F13 - Execution-lag sensitivity.** Re-run with `exec_lag` of 1, 2 and 3 on equities. Threshold: combined Sharpe stable within 0.10 across the range. Action: if not, the headline depends on an unverified execution assumption.
- **F14 - Frozen forward window.** From 2026-10-01, collect at least 12 months of forward sleeve and combination returns with the rules frozen. Threshold (research-defined): forward net Sharpe above 0 and forward HAC alpha t above 1.0 versus SPY. Action: if below, retire the hypothesis.

No-retuning rule (research-defined): F1 through F14 must all be evaluated with the pinned 60-day inverse-vol lookback, 252-day min-variance lookback, 10 percent vol target, 60-day vol-target lookback, 5x leverage cap, the three fixed combination rules, the 5/10/5 bps cost schedule, `exec_lag` values 1 to 3 only, the point-in-time S&P 500 membership procedure, the top-30 USDT crypto universe rule, the pairs screening thresholds, the 2005-01-01 to 2026-04-01 equity download window and the HAC lag of 5. Any gate that fails may not be re-run with a modified parameter to obtain a pass; a modified parameter starts a new, separately reported experiment.

## Crypto portability

Marked **adapted**, with economic viability unproven.

- One of the three sleeves is already crypto (top-30 USDT spot pairs on Binance.US, 365-day calendar, `exec_lag=1`, 10 bps/side), so that component is native.
- The combination layer itself is asset-agnostic arithmetic over sleeve PnLs and ports mechanically.
- What does not port unchanged: the equity and pairs sleeves, point-in-time S&P 500 membership, the NYSE business-day calendar that the inner join imposes on the combined panel, the SPY benchmark used for the headline HAC t, the `exec_lag=2` equity convention, and the 252-day annualisation.
- Crypto-specific gaps in the source: perpetual funding is acknowledged but not modelled (README lines 174, 187); dollar neutrality is described as `implicit - spot shorting is limited` with perpetual futures assumed rather than specified (README line 173); borrow availability, liquidation and ADL mechanics, mark and index price conventions, cross-venue fragmentation and custody risk are never discussed (census: `liquidation` 0, `margin` 1 in an unrelated sense).
- The crypto universe is curated by today's market cap, so porting it forward repeats the survivorship problem the source itself flags (README lines 58-62).
- Crypto portability is not authorization to trade.

## Limitations

- **not independently reproduced.** No backtest was re-run; no notebook was executed; no market data was downloaded.
- **data gap**: `data/` is gitignored, so none of the parquet inputs behind the headline number is published; F1 is the only path to reproduction.
- **data gap**: the crypto download window end, the borrow rate actually charged, the seeds for notebook 06 and notebook 08, the count of configurations per `optimized` label, the risk-free convention behind the headline Sharpe, bar timezone and boundary conventions, and any capacity number.
- **underspecified**: the exact rebalance cadence of the executed equity book; whether the crypto sleeve's short leg is spot, perp or synthetic in the backtest; whether notebook 04's optimiser output is ever persisted anywhere outside the ignored `data/` directory.
- **unproven**: the diversification claim is an in-sample-to-OOS statement over a single 2021-04 to 2026-03 window that contains one crypto boom-bust cycle; the source says as much (README lines 186-188).
- **source quality**: self-published single-author repository, no license file, no paper artifact in the tree, no peer review, identity only from a git author name.
- The notebook cells that produce the printed numbers were pinned but not parsed, so the numbers in this record are README-level claims with line-level provenance rather than cell-level provenance.
- Incremental-write check: this record contributes a new source identity, a new combination-layer mechanism for this repository (sleeve-level inverse-vol risk allocation rather than a single-signal alpha), new negative evidence (combination-layer cost absence, equity-sleeve proxy, calendar inner join, four source-internal contradictions) and a new falsification ladder; it is not a paraphrase of an existing capture.

## Implementation status

`implementation_status: not-implemented`.

No part of this record has been implemented in our research stack. No Qlib full backtest, no candidate-pool entry, no Paper, Testnet or Live run, no NautilusTrader change and no strategy family has been created. The source repository itself contains a paper-trading execution layer (`runner.py`, `execution.py`, `risk.py`, `price_feed.py`) with `broker.type: paper`, but that is the third party's artifact, not ours, and it has not been run here. Nothing in this record should be read as implying that any downstream validation stage has occurred.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

The presence of this record in the staging repository does **not** mean: that it passed Research Intake Review; that it entered Hermes Wiki Brain; that it entered the production candidate pool; that it completed Qlib full-backtest validation; that it became a frozen survivor or leaderboard entry; that it is profitable; that it is validated alpha; or that it is approved for implementation, paper trading, testnet or live trading. Confidence `medium` describes confidence in the research interpretation of the source only; it is not confidence that the strategy works and not authorization to trade it. Any later adoption decision must be explicit, separately reviewed, and based on this record plus current sources.

## Related Wiki records

Links below were returned by a read-only Wiki Brain search this run; only paths that the search actually returned are listed, and no page was written.

- [[quant/sharpe-deflated-multiple-testing-2026-08-27]] - the vault's canonical DSR and multiple-testing reference; F3 and F11 in this record should be read against it, including its warning that a DSR threshold is a risk-policy choice, not a literature constant.
- [[quant/johansen-cointegration-etf-pairs-friction-asymmetry-falsification-2026-09-12]] - pairs-trading falsification under friction asymmetry; the natural counterparty for the pairs sleeve reported here.
- [[quant/sp500-statistical-arbitrage-johansen-ou-ablation-multiple-testing-2026-09-12]] - S&P 500 cointegration stat-arb with family-wise deflation, the closest methodological neighbour to notebook 09.

Recorded distinction against existing repository captures (source identity, mechanism, signal construction, universe/market type, horizon or regime, material data dependency all differ):

- Versus `crypto-convex-optimized-cross-sectional-momentum-btc-regime-2026-09-19.md`: different source, and the mechanism here is portfolio-level risk allocation across three sleeves rather than a single cross-sectional momentum signal with a BTC regime gate; different universe (three-asset-class blend) and different data dependency (sleeve PnL parquets).
- Versus `crypto-cross-sectional-volatility-managed-momentum-2026-08-31.md`: different source, different signal construction (vol-managed single signal versus volume-adjusted momentum embedded in an inverse-vol sleeve blend), different market type mix.
- Versus `crypto-walk-forward-window-optimization-double-oos-momentum-2026-09-04.md`: different source and a different hypothesis (window-length optimisation robustness versus sleeve diversification), different horizon and different material data dependency.
- Versus `quant` records on Johansen and OU pairs falsification: different source, and here pairs is one input sleeve of a combination rather than the object under test.

## Sources

Primary source (all fetched 2026-10-01 from the immutable commit `d164dd8929e7aaffd7d24ae57ab9ac2e66098de8`):

- https://github.com/SashRajj/QuantBook/tree/d164dd8929e7aaffd7d24ae57ab9ac2e66098de8
- https://github.com/SashRajj/QuantBook/blob/d164dd8929e7aaffd7d24ae57ab9ac2e66098de8/README.md (24908 bytes, SHA-256 `3dcf16bb3f236a553c7597df0ee4a1b0e3e7a871269813036593c5831161c673`, read in full)
- https://github.com/SashRajj/QuantBook/blob/d164dd8929e7aaffd7d24ae57ab9ac2e66098de8/multi_strategy.py (10263 bytes, SHA-256 `ad955c9db868cb8b755b4e2cc734d2baa93ca134adcf6442d2909aab4f5a249e`, read in full)
- https://github.com/SashRajj/QuantBook/blob/d164dd8929e7aaffd7d24ae57ab9ac2e66098de8/helper.py (26726 bytes, SHA-256 `8d5943bb3fea1ea801f7dc5b56e8925d940e2aa8e6ed8d3d6987dbf71ddd2723`, lines 218-377 read)
- https://github.com/SashRajj/QuantBook/blob/d164dd8929e7aaffd7d24ae57ab9ac2e66098de8/config.yaml (2541 bytes, SHA-256 `f145dd917c872c473856a2535abb4e3c7c9da6eac64e3e33673c1048ca82ab42`, read in full)
- https://github.com/SashRajj/QuantBook/blob/d164dd8929e7aaffd7d24ae57ab9ac2e66098de8/signals.py (4632 bytes, SHA-256 `8255665fd6c18b5bd3a5d1b89351ca50c465498769e9ef05a44410c97819d5da`, pinned for identity only, not read)
- https://github.com/SashRajj/QuantBook/blob/d164dd8929e7aaffd7d24ae57ab9ac2e66098de8/.gitignore (364 bytes, SHA-256 `79f2c48308ff27c81a1b791ed3b1a38e8c76b169a06f56eb4685c076bc29b3df`, read in full)
- Notebook blobs pinned by identity only, not parsed: https://github.com/SashRajj/QuantBook/blob/d164dd8929e7aaffd7d24ae57ab9ac2e66098de8/research/10_multi_strategy.ipynb and the sibling notebooks 01, 02, 03, 04, 07, 08, 09 and 11 in the same directory.

No secondary summary, search-result snippet or model-generated description was used to fill any strategy rule or empirical claim in this record; search results were used for discovery only, and every cited figure was located in the pinned primary source.
