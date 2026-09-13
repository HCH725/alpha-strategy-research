---
schema: strategy-research-record-v1
title: "China A-Share Formulaic Factor Overfitting Audit: 456-Factor Library Screen, Amihud Downside Illiquidity Yield, Limit-Locked Board Phantom Fill Bias, and Forward Rotation Falsification"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - china-ashare
  - cross-sectional-equity
  - formulaic-alpha
  - amihud-illiquidity
  - backtest-overfitting
  - pbo
  - deflated-sharpe
  - limit-up-down-bias
  - forward-testing
  - falsification
status: research-only
confidence: high
source_as_of: 2026-09-13
sources:
  - "xuxingjiankr-cpu, 'Perception-XAlpha Lite: falsification-first formulaic factor research', GitHub repository, commit 104ac100551355e39356aa80465dcf2f16c22bb3 (September 13, 2026), https://github.com/xuxingjiankr-cpu/perception-xalpha-lite"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# China A-Share Formulaic Factor Overfitting Audit: 456-Factor Library Screen, Amihud Downside Illiquidity Yield, Limit-Locked Board Phantom Fill Bias, and Forward Rotation Falsification

## Provenance

- **Primary Source:** `xuxingjiankr-cpu`, *"Perception-XAlpha Lite: falsification-first formulaic factor research"*, public GitHub repository: `https://github.com/xuxingjiankr-cpu/perception-xalpha-lite`.
- **Immutable Commit SHA:** `104ac100551355e39356aa80465dcf2f16c22bb3` (committed 2026-09-13 02:36:46 UTC).
- **Exact Primary Source Paths:**
  - `README.md`
  - `CITATION.cff`
  - `docs/PAPERS.md`
  - `docs/USER_SUPPLIED_LITERATURE.md`
  - `docs/data/single_name_rotation_v4.spec.json`
  - `docs/data/library_ranking.json`
  - `docs/data/source_reconciliation.json`
  - `docs/data/rotation.jsonl`
  - `docs/data/next_pick.json`
  - `src/xalpha_lite/forward.py`
  - `src/xalpha_lite/universe.py`
  - `src/xalpha_lite/book.py`
  - `src/xalpha_lite/dsl.py`
  - `examples/selection_artifact.py`
- **Data Scope & Universe:** Mainland China A-share equity panel covering 5,266 constituent symbols across Shanghai and Shenzhen exchanges (SSE Main `sh.60`, STAR `sh.68`, SZSE Main `sz.00`, ChiNext `sz.30`; B-shares and Beijing BSE excluded). Historical panel spans 900 trading sessions, chronologically split at `2024-12-31` into a 261-rebalance training window and a 376-rebalance untouched out-of-sample testing window. Point-in-time universe filters enforce 60-day median daily turnover $\ge 30,000,000$ RMB, $\ge 120$ days seasoning, and active normal trade status with ST/ *ST exclusion (~4,700 eligible names).
- **Repository Deduplication:** Audited all existing `.md` records in `alpha-strategy-research`. Zero prior records cite `xuxingjiankr-cpu`, `perception-xalpha-lite`, or this codebase. Adjacent equity factor captures (`china-ashare-level2-burst-volume-trade-imbalance-2026-09-13.md`, `china-ashare-xgboost-treeshap-behavioral-factor-decomposition-2026-09-04.md`, `us-equity-microstructure-ensemble-lightgbm-fdr-falsification-2026-09-13.md`, `alpharjm-reward-jump-memory-sde-critic-symbolic-alpha-2026-09-11.md`) examine intraday Level-2 order flow, non-linear TreeSHAP tree models, or RL-driven symbolic tree mining on US/China equities. None examine a systematic 456-factor empirical screen across published factor libraries (Kakushadze 101, GTJA 191, Qlib 158, academic), the empirical measurement of the +6.05% limit-locked board fill bias, the 42.1% data provider divergence artifact, or the frozen pre-registered forward live rotation track (`dea0e608`).

## Economic mechanism

### Source-reported

The primary author frames quantitative discovery as an inherently fragile multiple-comparisons problem disguised as an optimization problem. Across published factor libraries (Kakushadze 101 Alphas, Guotai Junan GTJA 191 Alphas, Microsoft Qlib 158 Alphas, and classic academic asset pricing factors), hundreds of formulaic expressions are proposed based on technical momentum, volume surges, price-volume correlations, and valuation spreads.

The author tests whether any of these published factors possess genuine out-of-sample predictive power once evaluated on a point-in-time panel with executable order boundaries:
1. **Downside Price Impact / Illiquidity Premium:** Out of 456 published factors, the only two that survived both in-sample training selection and out-of-sample testing gates are variants of Amihud's (2002) illiquidity ratio: `gtja191/alpha_144` (measuring mean absolute return per unit turnover restricted exclusively to down days) and `academic/illiq` (measuring mean absolute return per unit dollar volume across all days). The economic rationale is an illiquidity premium: investors require higher future expected returns to hold stocks that suffer severe price dislocation during selling pressure.
2. **Limit-Locked Board Phantom Fill Bias:** In markets with daily price limits ($\pm 10\%$ or $\pm 20\%$), sessions that open, trade, and close at a single price (`high == low` with non-zero volume) represent limit-locked boards where quotes exist but counterparties cannot trade. Backtesting with unconstrained OHLCV fills assumes liquidity on these sealed bars, injecting an unexecutable $+6.05\%$ return bias per leg.
3. **Selection-Induced Alpha Hallucination:** Even with zero underlying market edge, selecting the best top-decile factors from an unpreregistered search over 400 noise factors manufactures an apparent annualized Information Ratio (IR) of 4.53 ($+2.00$ bps/day) in-sample, which collapses to $-1.24$ bps/day out-of-sample—a pure selection artifact of $+3.24$ bps/day.

### Research interpretation

The empirical findings provide a rigorous, multi-dimensional falsification of traditional formulaic equity alpha claims:
1. **Training Rank Correlates with Test Rank, Yet Produces Negative Net Alpha:** Across all 456 factors, training-window excess predicts test-window excess with Spearman $\rho = +0.4833$ ($p = 4.53 \times 10^{-28}$). Thus, training performance is not purely random noise. However, the top 10 factors selected on the training window delivered a mean test excess of $-0.2388\%$ per 10-session hold against the equal-weight eligible universe ($+0.8484\%$). While superior to selecting at random (mean test excess $-0.714\%$), the top-ranked candidates still underperformed the simple universe benchmark.
2. **Transaction Cost Eradication:** The sole surviving factors—`gtja191/alpha_144` (downside Amihud illiquidity) and `academic/illiq` (standard Amihud illiquidity)—achieved gross test excess returns of $+0.1696\%$ and $+0.14\%$ per 10-session hold, respectively. At an institutional round-trip cost of 30 bps (0.003), full rotation across holds incurs a 30 bps drag, which completely consumes and erases the entire gross edge.
3. **Data Vendor Fragility:** A single-name rotation strategy is acutely vulnerable to vendor microstructure noise. Reconciling baostock with TDX backward-adjusted bars over 140 sessions showed that two honest data vendors disagree on the top-ranked stock on 42.14% of sessions (agreement rate of only 57.86%), with a median disagreement rank of 4. A strategy whose portfolio identity switches on 42% of sessions based on vendor rounding is not an investment strategy; it is an artifact of the data pipeline.

## Signal

### Formation timestamp

Signals are generated causally at the close of trading session $t$. Orders are executed at the open of session $t+1$ (`buy_at: "open of the next trading session"`). In the forward-testing track, specifications are frozen (`freeze_spec`) with SHA-256 digests and committed to Git prior to session open, ensuring zero hindsight leakage.

### Lookback windows

- **Factor 1: Downside Amihud Illiquidity (`gtja191/alpha_144`):**
  - Lookback: 20 trading sessions ($W = 20$).
  - Calculation: Rolling mean of $|\text{return}_t| / \text{turnover}_t$ computed only over sessions where $\text{return}_t < 0$.
- **Factor 2: Standard Amihud Illiquidity (`academic/illiq`):**
  - Lookback: 21 trading sessions ($W = 21$).
  - Calculation: Rolling mean of $|\text{return}_t| / (\text{close}_t \times \text{volume}_t)$.
- **Factor 3: Trend Goodness-of-Fit 60-Day (`qlib158/rsqr60`):**
  - Lookback: 60 trading sessions ($W = 60$).
  - Calculation: $\text{corr}(\text{close}, \text{session\_index}, 60)^2$, measuring the coefficient of determination $R^2$ of linear price trend.
- **Factor 4: Trend Goodness-of-Fit 30-Day (`qlib158/rsqr30`):**
  - Lookback: 30 trading sessions ($W = 30$).
  - Calculation: $\text{corr}(\text{close}, \text{session\_index}, 30)^2$.
- **Factor 5: Conservative Investment Proxy (`academic/cma`):**
  - Lookback: 60 trading sessions ($W = 60$).
  - Calculation: Negative change in log volume: $-\big(\text{signed\_log1p}(\text{mean}_{60}(\text{volume})) - \text{lag}_{60}(\text{signed\_log1p}(\text{mean}_{60}(\text{volume})))\big)$.

### Entry rules

1. **Point-in-Time Universe Mask:** At session $t$, filter eligible stocks using data strictly up to $t-1$:
   - Trailing 60-day median turnover $\ge 30,000,000$ RMB (`trailing_amount_window: 60`, `minimum_trailing_median_amount: 30000000.0`).
   - Prior observations $\ge 120$ sessions (`minimum_prior_observations: 120`).
   - Exclude ST and *ST special-treatment symbols (`exclude_st: true`).
   - Exclude suspended or halted stocks (`trade_status: 1`, volume $> 0$, amount $> 0$).
2. **Limit-Locked Board Guard:** Evaluate whether the candidate stock at session $t+1$ is sealed at a price limit:
   - Sealed bar condition: $\text{high}_{t+1} == \text{low}_{t+1}$ with $\text{volume}_{t+1} > 0$.
   - Direction: If sealed price exceeds close of $t$, it is limit-up locked.
   - Refusal rule: A stock sealed at limit-up at entry cannot be bought; the trade is refused and the session is skipped.
3. **Composite Scoring & Selection:**
   - For multi-factor composite (Frozen Spec `dea0e608`): Compute cross-sectional percentiles for `qlib158/rsqr60`, `qlib158/rsqr30`, `academic/illiq`, and `academic/cma`.
   - Score: $\text{composite\_rank} = \frac{1}{4} \sum_{i=1}^4 \text{rank}(F_i)$.
   - Book Selection: Select top $N$ names ($N = 1$ in single-name rotation; $N = 10$ in multi-name book). Ties broken deterministically by alphabetical symbol name (`select_names`).

### Exit rules

- **Holding Period:**
  - In single-name rotation (`single_name_rotation_v4`): $H = 1$ session (`holding_days: 1`). Position is exited at the open of session $t+2$.
  - In 10-name benchmark book: $H = 10$ sessions, rebalanced daily across 10 staggered tranches.
- **Stop-Loss / Take-Profit:** The primary source specifies no intraday stop-loss or take-profit triggers; exit occurs purely on holding duration elapsed.

### Parameters

- Base equity universe: SSE Main (`sh.60`), STAR (`sh.68`), SZSE Main (`sz.00`), ChiNext (`sz.30`) (~5,266 stocks) (`source-reported`).
- Minimum median daily turnover: 30,000,000 RMB over trailing 60 sessions (`source-reported`).
- Seasoning threshold: 120 historical sessions (`source-reported`).
- Round-trip transaction cost: 30 bps (0.003) applied on portfolio rotation (`source-reported`).
- Rebalance frequency: Daily at session open (`source-reported`).
- Benchmark: Equal-weight eligible universe over identical holding bars (`source-reported`).

## Required data

- **Instruments:** Mainland China A-shares traded on Shanghai Stock Exchange (SSE) and Shenzhen Stock Exchange (SZSE).
- **Timeframe:** Daily bars (OHLCV, turnover amount).
- **Price Adjustment:** Backward-adjusted prices (`adjust_flag: "1"` in baostock; `hfq` in TDX).
- **Tradability & Status Flags:** Point-in-time listing date, suspension status, trading status flag (`trade_status == 1`), ST/ *ST classification flag (`is_st`).
- **Limit Detection:** Open, high, low, close, volume, and prior close to identify sealed limit-up/limit-down bars.
- **Provider Sensitivity:** Explicit specification requirement: primary source requires `baostock` due to 42.1% top-1 disagreement when using `TDX/mootdx`.

## Execution assumptions

- **Execution Timing:** Next-bar open execution ($t+1$ open for signal computed at $t$ close).
- **Fill Mechanics:** Full execution at open price, provided stock is not sealed at limit-up. Limit-locked bars are dropped (unexecutable).
- **Transaction Costs:** 30 bps round-trip (0.003) deducted on every portfolio rotation, reflecting stamp duty, exchange fees, and bid-ask spread in China A-shares.
- **Short Selling:** Long-only portfolio construction (`long_only_book`); short legs are not assumed executable under mainland China margin/shorting constraints.

## Evidence

### Source-reported

All empirical metrics trace directly to primary source outputs in `xuxingjiankr-cpu/perception-xalpha-lite` (commit `104ac100551355e39356aa80465dcf2f16c22bb3`, files `README.md`, `docs/data/library_ranking.json`, `docs/data/source_reconciliation.json`, `docs/data/rotation.jsonl`, `examples/selection_artifact.py`):

#### 1. 456-Factor Library Audit (900 sessions, 5,266 symbols, split at 2024-12-31)
- **Selection Value Correlation:** Spearman rank correlation between training-window excess and test-window excess across all 456 factors: $\rho = +0.4833$ ($p = 4.53 \times 10^{-28}$).
- **Cross-Sectional Factor Decay:**
  - All 456 factors mean test excess per 10-session hold: $-0.714\%$.
  - Share of all 456 factors beating eligible universe: 21.27% (97 / 456).
  - Training top 10 factors mean test excess per 10-session hold: $-0.2388\%$ (vs eligible universe $+0.8484\%$).
  - Share of training top 10 beating eligible universe: 30.0% (3 / 10).
- **Failure of Top Training Factors:**
  - `academic/hml` (rank 1 in-sample): train excess $+2.2029\% \to$ test excess $-0.0429\%$ (hit rate 49.2%, worst hold $-17.49\%$).
  - `qlib158/imin60` (rank 2 in-sample): train excess $+0.8074\% \to$ test excess $-0.7322\%$ (hit rate 36.7%, worst hold $-11.63\%$).
  - `qlib158/max60` (rank 6 in-sample): train excess $+0.592\% \to$ test excess $-0.687\%$ (hit rate 37.5%, worst hold $-16.13\%$).
- **Surviving Factors (Top 30 Training Screen):**
  - `gtja191/alpha_144` (rank 3): train excess $+0.7322\%$, test excess $+0.1696\%$, big-move odds ratio $1.157\times$, worst hold $-7.48\%$, hit rate 46.5%.
  - `academic/illiq` (rank 30): train excess $+0.27\%$, test excess $+0.14\%$, big-move odds ratio $1.18\times$, worst hold $-7.8\%$, hit rate 47.9%.
  - **Yield:** Exactly 2 out of 30 highest-ranked training factors cleared both test gates. Both represent the same underlying phenomenon (Amihud illiquidity / price impact per turnover).
- **Cost Netting:** At 30 bps round-trip cost, rotating the 10-session book incurs 30 bps drag, fully eliminating the gross test excess of $+0.14\%$ to $+0.17\%$.

#### 2. Quantified Backtest Biases
- **Hindsight Selection Bias:** Outcome-window factor selection generates an apparent $+2.00$ bps/day with annualized IR 4.53, whereas honest trailing selection produces $-1.24$ bps/day—an artifact gap of $+3.24$ bps/day on pure noise.
- **Limit-Locked Board Fill Bias:** Pricing unexecutable limit-locked bars contributes $+6.05\%$ forward return per leg vs $+0.38\%$ for truly executable legs.
- **Point-in-Time Universe Conditioning:** Filtering universe on full-history liquidity yields 391 names in year one vs 77 names under point-in-time filtering.
- **Overlapping Holding Horizon Inflation:** Treating overlapping 10-day returns as independent inflates t-statistics from $-2.25$ to $-5.79$.

#### 3. Data Provider Sensitivity (baostock vs TDX)
- Sessions compared: 140.
- Top-1 symbol agreement between vendors: 57.86% (diverging on 42.14% of sessions).
- Median rank of fallback vendor's pick in primary vendor's ranking: 4th of ~4,700 names.

#### 4. Pre-Registered Forward Live Rotation Track (`dea0e608`, single-name rotation v4)
- Live sessions scored (as of 2026-09-02): 8 trades.
- Compounded excess over universe: $-4.40\%$.
- Mean gross return per trade: $-0.38\%$.
- Trades that rose: 5 / 8 (62.5%).
- Next advance pick published: `SZ_300804` (as of 2026-09-07, rank 0.940379).
- Framework audit verdict: `insufficient_forward_sample` ($N < 60$).

### Independently reproduced

Not independently reproduced. All figures and claims are third-party results reported by `xuxingjiankr-cpu` in GitHub repository `perception-xalpha-lite` (commit `104ac100551355e39356aa80465dcf2f16c22bb3`).

### Negative evidence

- **Factor Decay & Turnover Drag:** The top 10 training factors deliver negative net alpha out-of-sample ($-0.24\%$ per hold), underperforming simple equal weighting. Even the two surviving illiquidity factors are completely consumed by realistic transaction costs (30 bps round-trip).
- **Failure of Classic Value and Min-Price Factors:** Classic Fama-French HML and 60-day minimum price factors experienced severe out-of-sample degradation (HML falling from $+2.20\%$ to $-0.04\%$; `imin60` from $+0.81\%$ to $-0.73\%$).
- **Extreme Single-Name Fragility:** The top-1 recommendation switches on 42% of sessions solely due to price adjustment discrepancies between data vendors.
- **Forward Track Underperformance:** The forward live implementation has generated $-4.40\%$ compounded excess over 8 scored trades.

## Falsification plan

To falsify the hypothesis that Amihud downside illiquidity (`alpha_144` / `illiq`) provides tradable cross-sectional alpha in equity and adapted markets:

1. **Transaction Cost Barrier Test:**
   - *Protocol:* Evaluate the top-decile illiquidity portfolio net of stepped transaction costs (10, 20, 30, and 40 bps round-trip).
   - *Decision Rule (`research-defined falsification threshold`):* If net annualized Sharpe ratio drops below 0.0 or net alpha over the equal-weight universe is $\le 0.0$ at or below 25 bps round-trip, the hypothesis of tradable illiquidity alpha is falsified by turnover drag.
2. **Limit-Locked Bar Audit Test:**
   - *Protocol:* Compare returns when allowing open fills on sessions where $\text{open} == \text{high} == \text{low}$ versus strictly refusing execution.
   - *Decision Rule (`research-defined falsification threshold`):* If the strategy's apparent excess return drops by $>70\%$ upon enforcing limit-locked fill refusal, the strategy is falsified as a non-implementable execution artifact.
3. **Vendor Permutation / Microstructure Noise Test:**
   - *Protocol:* Run identical ranking algorithms over secondary data feeds (e.g. Wind, Choice, or TDX vs baostock).
   - *Decision Rule (`research-defined falsification threshold`):* If portfolio overlap between vendors is $<70\%$ or top-decile return spread across vendors exceeds the net strategy return, the alpha is falsified as vendor noise.
4. **Combinatorially Symmetric Cross-Validation (CSCV) / PBO Test:**
   - *Protocol:* Run CSCV with $S = 16$ splits across the 900-session panel.
   - *Decision Rule (`research-defined falsification threshold`):* If Probability of Backtest Overfitting $PBO \ge 0.50$ or Deflated Sharpe Ratio $DSR < 0.95$ accounting for 456 trials, the candidate is classified as a selection artifact and rejected.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Mechanism Differences:**
  - *No Daily Price Limits:* Crypto spot and perpetual markets operate 24/7 without exchange-mandated $\pm 10\% / \pm 20\%$ daily price-limit bands. The limit-locked board fill bias (+6.05%) does not exist in crypto in this exact form. However, severe liquidity black holes during cascade liquidations create analogous non-executable bid-ask gaps.
  - *Illiquidity Metric Portability:* Amihud's ratio $|\Delta P| / (\text{Price} \times \text{Volume})$ can be directly computed on crypto perpetuals. However, in crypto perps, high illiquidity is heavily confounded with negative funding rates, high borrow costs, and toxic taker flow.
  - *Turnover & Fee Barriers:* Binance and Bybit VIP0 perpetual taker fees are 5 bps (10 bps round trip), while spot fees are 10 bps (20 bps round trip). High-turnover daily rotation would experience severe fee attrition.
- **Crypto-Specific Operational Rules (`research-proposed`):**
  - *Universe Filter (`research-proposed`):* Filter top 50 perpetual futures contracts by 30-day median dollar volume; exclude contracts with open interest $< \$10\text{M}$.
  - *Funding Gate (`research-proposed`):* Filter out tokens with 8-hour funding rates exceeding $\pm 0.10\%$ to prevent adverse carry costs.
  - *Execution Model (`research-proposed`):* Execute via TWAP/VWAP over a 15-minute window following UTC 00:00 boundary to mitigate single-tick market impact.

## Limitations

- **High-Turnover Cost Drag:** The gross premium of illiquidity factors (+14 to +17 bps per 10 sessions) is insufficient to cover realistic execution and transaction costs.
- **Underspecified Intraday Dynamics:** Daily bars obscure intraday order-book depth, queue priority, and slippage on volatile sessions.
- **Data Vendor Dependence:** A 42% discrepancy in single-name selection across vendors demonstrates that daily backward-adjusted data lacks the precision required for ultra-concentrated portfolios.
- **Forward Sample Size:** The forward live track contains only 8 scored trades, which remains below the 60-trade minimum threshold required for statistical conclusiveness (`insufficient_forward_sample`).

## Implementation status

`not-implemented`. This record represents normalized research capture and empirical falsification audit from external public source `perception-xalpha-lite`. No implementation of this 456-factor audit, DSL parsing, or single-name rotation model exists in our research repository, PyBroker, or NautilusTrader codebases.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- **Boundary Declaration:** This research capture serves strictly to document the empirical falsification of published formulaic equity factor libraries, the quantification of limit-locked fill bias, and the methodology of pre-registered forward testing. It does not constitute an approved trading strategy, does not authorize live or testnet capital allocation, and does not validate the profitability of any included factor.

## Related Wiki records

- `[[china-ashare-level2-burst-volume-trade-imbalance-2026-09-13]]` — Intraday Level-2 trade imbalance and burst volume falsification in China A-shares.
- `[[china-ashare-xgboost-treeshap-behavioral-factor-decomposition-2026-09-04]]` — Nonlinear TreeSHAP factor decomposition on CSI300/CSI500 equities.
- `[[us-equity-microstructure-ensemble-lightgbm-fdr-falsification-2026-09-13]]` — Intraday microstructure walk-forward ensemble and Benjamini-Hochberg FDR falsification.
- `[[alpharjm-reward-jump-memory-sde-critic-symbolic-alpha-2026-09-11]]` — Formulaic alpha discovery via RL and continuous-time SDE critic.
- `[[sp500-avellaneda-lee-residual-reversion-implementability-falsification-2026-09-13]]` — Accounting artifact and phantom P&L falsification in equity statistical arbitrage.

## Sources

1. **Primary GitHub Repository:** `xuxingjiankr-cpu`, *Perception-XAlpha Lite: falsification-first formulaic factor research*, public GitHub repository `https://github.com/xuxingjiankr-cpu/perception-xalpha-lite`, immutable commit `104ac100551355e39356aa80465dcf2f16c22bb3` (September 13, 2026).
   - Core README: `https://github.com/xuxingjiankr-cpu/perception-xalpha-lite/blob/104ac100551355e39356aa80465dcf2f16c22bb3/README.md`
   - Single Name Rotation v4 Spec: `https://github.com/xuxingjiankr-cpu/perception-xalpha-lite/blob/104ac100551355e39356aa80465dcf2f16c22bb3/docs/data/single_name_rotation_v4.spec.json`
   - 456-Factor Library Ranking Results: `https://github.com/xuxingjiankr-cpu/perception-xalpha-lite/blob/104ac100551355e39356aa80465dcf2f16c22bb3/docs/data/library_ranking.json`
   - Data Vendor Reconciliation: `https://github.com/xuxingjiankr-cpu/perception-xalpha-lite/blob/104ac100551355e39356aa80465dcf2f16c22bb3/docs/data/source_reconciliation.json`
   - Forward Live Rotation Log: `https://github.com/xuxingjiankr-cpu/perception-xalpha-lite/blob/104ac100551355e39356aa80465dcf2f16c22bb3/docs/data/rotation.jsonl`
   - Selection Artifact Experiment: `https://github.com/xuxingjiankr-cpu/perception-xalpha-lite/blob/104ac100551355e39356aa80465dcf2f16c22bb3/examples/selection_artifact.py`
   - Literature & Scientific Map: `https://github.com/xuxingjiankr-cpu/perception-xalpha-lite/blob/104ac100551355e39356aa80465dcf2f16c22bb3/docs/PAPERS.md`
2. **Academic & Literature References Cited in Source:**
   - Amihud, Y. (2002). *Illiquidity and stock returns: cross-section and time-series effects*. Journal of Financial Markets, 5(1), 31–56.
   - Bailey, D. H., Borwein, J. M., López de Prado, M., & Zhu, Q. J. (2015). *The Probability of Backtest Overfitting*. Journal of Computational Finance.
   - Bailey, D. H., & López de Prado, M. (2014). *The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting and Non-Normality*. Journal of Portfolio Management, 40(5), 94–107.
   - Kakushadze, Z. (2016). *101 Formulaic Alphas*. Wilmott Magazine, 2016(84), 72–81.
