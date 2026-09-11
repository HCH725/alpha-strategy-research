---
schema: strategy-research-record-v1
title: "Cross-Sectional Crypto Perpetual Funding Carry-Fade: Pre-Registered Empirical Falsification via Turnover-Cost Dissipation and Absent Price Convergence"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - funding-rate
  - carry-fade
  - cross-sectional
  - negative-evidence
  - pre-registered
  - turnover-cost
  - deflated-sharpe-ratio
status: research-only
confidence: high
source_as_of: 2026-08-03
sources:
  - "Joseph Berachah, 'Cross-Sectional Crypto Alpha Research: Pre-Registered Study of Return Predictability in Binance Perpetual Futures', GitHub repository JosephBerachah/crypto-fundingrate-alpha, commit 9d26979a1b2d4714c1f893574f01418332ce276c (August 3, 2026), files: README.md, docs/preregistration.md, docs/results_primary.md, research_log.md, src/strategy/build_signal.py, src/strategy/build_portfolio.py, src/strategy/apply_costs.py, src/strategy/evaluate.py, src/strategy/validate_signal.py, src/strategy/validate_portfolio.py, src/strategy/validate_costs.py, src/strategy/validate_evaluate.py, src/data/measure_halfspread.py, src/data/floor_sweep.py, src/data/oi_profile.py, src/data/sample_start.py"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Sectional Crypto Perpetual Funding Carry-Fade: Pre-Registered Empirical Falsification via Turnover-Cost Dissipation and Absent Price Convergence

## Provenance

- **Primary Repository:** Public GitHub repository `https://github.com/JosephBerachah/crypto-fundingrate-alpha`
- **Author:** Joseph Berachah (`JosephBerachah`)
- **Immutable Commit SHA:** `9d26979a1b2d4714c1f893574f01418332ce276c` (August 3, 2026)
- **Primary Source Documents and Implementation Scripts Inspected Directly:**
  - `README.md`: Executive research summary, pre-registered headline metrics, turnover findings, and research discipline rules.
  - `docs/preregistration.md`: Formal pre-registered research contract sealed on 2026-07-28 UTC prior to downloading funding data, defining hypothesis, universe, signal, portfolio, cost model, evaluation statistics, and explicit kill criteria.
  - `docs/results_primary.md`: Primary empirical evaluation report across 1,322 training days (2021-05-15 to 2024-12-31) detailing the headline market-neutral Sharpe, stationary bootstrap confidence intervals, return component decomposition, era splits, and cost ladder.
  - `research_log.md`: Chronological experiment ledger documenting trial count ($N=1$), design freezes, probe analyses, and the final training verdict.
  - `src/strategy/build_signal.py`: Causal 24h rolling funding sum signal construction, timestamp hour-snapping, 24h interval tiling verification, and lagged universe screening.
  - `src/strategy/build_portfolio.py`: Daily decile long/short spread portfolio formation, $1/k$ equal weighting, gross notional 2.0, dollar-neutral accounting, and delisting cash settlement.
  - `src/strategy/apply_costs.py`: Realistic transaction cost engine applying 5.0 bps taker fees plus empirical half-spread step-function tiers estimated from tick-level trade data, tracking realized dynamic turnover.
  - `src/strategy/evaluate.py`: Statistical adjudication engine computing OLS market-neutral $\beta$ against BTC, Deflated Sharpe Ratio (DSR), Politis-White automatic block-length stationary bootstrap (10,000 replicates, seed `20260730`), and component return decomposition.
  - `src/data/measure_halfspread.py`: Deterministic empirical half-spread estimator computing median price differences between adjacent opposite-aggressor trades separated by $< 1000$ ms in Binance `aggTrades`.
- **Source As-of Date:** August 3, 2026.
- **Repository Deduplication Audit:** Audited all existing records in `alpha-strategy-research`. Zero existing records cite `JosephBerachah/crypto-fundingrate-alpha` or commit `9d26979a1b2d4714c1f893574f01418332ce276c`. An adjacent record (`crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11.md`, citing Bryan Vine's blog paper) investigated a survivor-biased 30-coin universe with weekly rebalancing and a fixed 6 bp cost assumption. In contrast, this record documents an independent, pre-registered study on a point-in-time universe (including delisted contracts) with daily decile turnover, tick-measured half-spreads, a sealed out-of-sample holdout, and formal statistical falsification of the underlying price-convergence mechanism.

## Economic mechanism

### Source-reported

In cryptocurrency perpetual futures, positions pay or receive an 8-hour (or 4-hour/1-hour) funding payment designed to tether perpetual contract prices to the underlying spot index. The theoretical foundation of the funding carry-fade hypothesis rests on two coupled economic assertions:
1. **Euphoric Long Crowding and Perpetual Overpricing:** When retail and speculative sentiment becomes excessively bullish on an altcoin, demand for leveraged long exposure pushes the perpetual futures price above spot. Longs are willing to pay an elevated funding rate to maintain leveraged upside exposure. Because carry arbitrageurs must short the perpetual and hold long spot (facing short-squeeze risk, inventory limits, and margin constraints), the elevated funding rate persists as an equilibrium risk premium.
2. **Dual-Channel Return Expectation (Price Convergence + Funding Harvest):** The carry-fade thesis posits that trading a dollar-neutral long/short spread (shorting the highest-funding decile and longing the lowest-funding decile) captures two additive return drivers:
   - **Funding Accrual:** The short leg collects positive funding from euphoric longs; the long leg collects funding from crowded shorts (or pays negligible funding).
   - **Price Convergence:** The elevated premium of the euphoric perpetual contract over spot is temporary and mean-reverts toward spot over a 24-hour holding horizon, inflicting a capital loss on crowded longs and generating capital gains for the short leg.
3. **The Empirical Falsification:**
   The pre-registered empirical backtest demonstrates that while the gross funding premium is genuine and mechanically positive (+0.001525/day), the strategy fails as an active trading alpha:
   - **High Turnover Pay-Away:** Selecting the extreme deciles on daily 24h rolling funding produces a daily portfolio turnover of 1.85×/day (nearly the entire book rotates daily). Measured taker fees and effective half-spreads consume ~74% of the gross funding stream.
   - **Absence of Price Convergence:** The short leg's price component is statistically indistinguishable from zero ($-0.000198$/day, 95% CI $[-0.002648, +0.002206]$) and flips sign across market eras. The hypothesized price convergence does not exist; the strategy is purely harvesting funding while paying massive execution friction.

### Research interpretation

This pre-registered study provides a critical structural falsification for cross-sectional crypto factor research:
- **The Turnover–Decile Trap:** In cross-sectional crypto factors, the cross-sectional ranking of trailing 24h funding rates is noisy and non-persistent. Extreme funding spikes are transient, causing individual altcoins to rapidly drop in and out of the top and bottom 10% buckets. Daily rebalancing to target equal weights inside the deciles forces near-total portfolio churn (185% notional traded daily). Because crypto perpetual trading incurs taker fees (5 bps VIP0) and bid-ask spreads, high turnover rapidly erodes the modest daily funding yield.
- **Decoupling of Funding Yield from Directional Drift:** Retail and discretionary literature frequently equates high funding with an imminent "reversal" or "long squeeze." The empirical data shows that crowded perpetual contracts do not systematically experience negative directional price drift over a 1-day holding horizon. High funding indicates aggressive leverage demand, but momentum and trend continuation often balance or overwhelm mean-reversion pressure, resulting in an expected price return centered at zero.
- **Market-Neutral vs. Dollar-Neutral Divergence:** Dollar-neutral crypto portfolios are inherently exposed to market risk ($\beta$). In bull markets (such as the 2023–2024 expansion), the top-funding decile is populated by high-beta speculative altcoins that outperform BTC, imparting a persistent negative market $\beta$ ($\beta = -0.116$) to a dollar-neutral short-top / long-bottom book. Without explicit market-neutral beta adjustments, raw returns conflate factor returns with being short market beta during an uptrend.

## Signal

The primary source operationalizes a strictly causal, point-in-time cross-sectional signal in `src/strategy/build_signal.py`:

- **Observation Timestamp:** $t = \text{00:00:00 UTC}$ daily (`source-reported`).
- **Settlement Timestamp Snap:** Binance records settlement timestamps with minor network/engine jitter (measured: 100% within 1.001s, 55% exact on the second). Timestamps are snapped to the exact round hour so settlements occurring at `00:00:00.xxx` are correctly included in $(t-24\text{h}, t]$ rather than leaking into the next window (`source-reported`).
- **Lookback Window:** Rolling 24-hour window $(t - 24\text{h}, t]$ ending at 00:00:00 UTC (`source-reported`).
- **Signal Definition:** For each candidate asset $i$ on date $t$:
  $$F(i, t) = \sum_{s \in (t-24\text{h}, t]} f(i, s)$$
  where $f(i, s)$ is the realized funding rate settlement for contract $i$ at timestamp $s$ (`source-reported`).
- **Complete Funding Coverage Check:** Rather than counting prints (which breaks because Binance utilizes 8h, 4h, and 1h funding intervals across different symbols and regimes), coverage is verified by tiling: the sum of `funding_interval_hours` across settlements in the window must equal exactly 24. Symbol-days with incomplete tiling (pass rate 99.7%, mostly delisting/listing boundaries) are discarded (`source-reported`).
- **Universe Decile Formation:** Eligible universe assets on date $t$ are ranked descending by $F(i, t)$:
  - **Short Leg (Top Decile):** The $k = \lfloor n / 10 \rfloor$ contracts with the highest $F(i, t)$ (euphoric longs paying funding) (`source-reported`).
  - **Long Leg (Bottom Decile):** The $k = \lfloor n / 10 \rfloor$ contracts with the lowest $F(i, t)$ (depressed/crowded shorts receiving funding) (`source-reported`).
  - **Middle 80%:** The remaining 8 deciles are untraded (`source-reported`).
  - **Minimum Universe Size Gate:** If total eligible universe $n < 100$, the date is skipped entirely ($k=0$) (`source-reported`).
- **Execution Timing Lag:** 1-hour causal execution delay. The observation is formed at 00:00:00 UTC; orders are executed at the open of the 01:00:00 UTC bar (equivalent to the close of the 00:00:00 UTC bar) (`source-reported`).
- **Holding Period:** Exactly 24 hours, from 01:00:00 UTC on date $t$ to 01:00:00 UTC on date $t+1$, chaining seamlessly without gaps (`source-reported`).
- **Rebalance Cadence:** Daily full rebalance at 01:00:00 UTC (`source-reported`).
- **Position Sizing and Weighting:**
  - Equal weighting within each leg: weight $w_i = +1/k$ for long-leg assets, $w_i = -1/k$ for short-leg assets (`source-reported`).
  - Total gross notional exposure: 2.0 ($1.0 long + $1.0 short). Net dollar exposure: 0.0 (strictly dollar-neutral) (`source-reported`).
  - No individual position caps tighter than $1/k$ were applied to maintain consistency across thin and thick eras (`source-reported`).
- **Delisting / Mid-Hold Termination:** If an asset is delisted or ceases trading mid-hold, it is liquidated at its last available trade price, and the proceeds remain in cash for the remainder of the 24-hour holding window. Dropping mid-hold delistings was explicitly forbidden in the pre-registration to avoid survivorship bias (`source-reported`).

## Required data

- **Universe:** Point-in-time reconstruction of all Binance USDT-margined perpetual futures listed on `data.binance.vision`, including active and delisted pairs (`source-reported`).
- **Listing History Filter:** Assets must possess $\ge 30$ days of listing history prior to date $t$ (`source-reported`).
- **Liquidity Inclusion Filter:** Trailing 30-day median dollar volume $\ge \$1,000,000/\text{day}$, computed using klines through date $t-1$ only (lagged by 1 day to strictly prevent look-ahead bias at 00:00:00 UTC) (`source-reported`). Robustness sweeps tested $0.5M and $2.0M floors (`source-reported`).
- **Fields:**
  - Hourly klines (Open, High, Low, Close, Volume) for entry/exit execution pricing at 01:00:00 UTC (`source-reported`).
  - Funding rate settlement tables: timestamp, symbol, funding rate, funding interval hours (`source-reported`).
  - Trade-level `aggTrades` archive: used to estimate empirical half-spreads from opposite-aggressor trade sequences (`source-reported`).
- **Sample Periods:**
  - **Full Dataset:** 2021-05-15 to 2026-06-30 (`source-reported`).
  - **Training Period:** 2021-05-15 to 2024-12-31 (1,322 trading days) (`source-reported`).
  - **Sealed Holdout Period:** 2025-01-01 to 2026-06-30 (18 calendar months, completely untouched after training failure) (`source-reported`).
- **Market Benchmark:** Binance BTCUSDT perpetual daily return, used as the exogenous regressor to compute market $\beta$ and market-neutral $\alpha$ (`source-reported`).

## Execution assumptions

- **Order Type:** Taker market orders executed at the 01:00:00 UTC hourly bar open (`source-reported`).
- **Maker Assumption Rejection:** The author explicitly rejected passive maker order modeling, noting that assuming passive limit fills on a cross-sectional daily rebalance provides an unverified ~6 bps/side subsidy that cannot be reliably falsified with historical OHLCV data (`source-reported`).
- **Fee Model:** Flat 5.0 bps (0.05%) taker fee per side, reflecting Binance standard VIP 0 retail tier without BNB fee discounts (`source-reported`).
- **Half-Spread Model (Empirical Measurement from Tick Data):**
  - Half-spreads were directly estimated by sampling Binance `aggTrades` data across all calendar years using opposite-aggressor trades separated by $< 1000$ ms (`source-reported`).
  - Frozen into 5 liquidity-volume step tiers based on lagged 30-day median dollar volume (`source-reported`):
    * Tier 1 (\$1M–\$3M): ~2.5–3.0 bps half-spread.
    * Tier 2 (\$3M–\$10M): ~1.8–2.2 bps half-spread.
    * Tier 3 (\$10M–\$30M): ~1.4–1.7 bps half-spread.
    * Tier 4 (\$30M–\$100M): ~0.8–1.2 bps half-spread.
    * Tier 5 (>\$100M): ~0.2–0.5 bps half-spread.
  - Hard Floor: Every half-spread is floored at half the asset's published exchange tick size (`source-reported`).
- **Turnover Accounting (Dynamic Book Drift):**
  - Between daily rebalance turns, position notionals drift with the individual asset price return $r_{\text{price}, i}$:
    $$\text{Carried}_i = \frac{1}{k_{t-1}} (1 + r_{\text{price}, i})$$
  - Traded notional is computed exactly as $\sum_i |\text{Target}_i - \text{Carried}_i|$ over the union of names across consecutive days (`source-reported`).
  - Costs are charged against gross PnL on the entry day (`source-reported`).
- **Slippage and Market Impact:** Zero market impact assumed (labeled "Framing A" — small capital capacity where trades do not shift the order book) (`source-reported`).
- **Borrow Fees:** Zero borrow cost (perpetual futures positions do not require physical borrow; funding rate payments are the sole cost of carry) (`source-reported`).

## Evidence

### Source-reported

The primary study reports results for the pre-registered primary hypothesis ($N=1$ trial count) evaluated over the complete 1,322-day training window (2021-05-15 to 2024-12-31):

#### 1. Headline Training Results (at 1× Measured Cost)

| Metric | Point Estimate | 95% Stationary Bootstrap CI | Pre-Registered Bar | Outcome |
|---|---|---|---|---|
| **Market-Neutral Net Sharpe ($\text{Sharpe}_{\text{mn}}$)** | **+0.37** (ann.) | — | Reliably > 0 | **Fails (weak / insignificant)** |
| **Raw Net Sharpe** | **+0.35** (ann.) | — | (Companion diagnostic) | Positive but weak |
| **Market-Neutral Daily Alpha ($\alpha$)** | **+0.000424** / day | **[−0.000732, +0.001593]** | Reliably > 0 (CI excludes 0) | **FAILED (CI spans zero)** |
| **Deflated Sharpe Ratio (DSR)** | **0.762** | Bootstrap $p(\text{Sharpe} \le 0) = 0.238$ | **> 0.95** | **FAILED (0.762 $\le$ 0.95)** |
| **BTC Market Beta ($\beta$)** | **−0.024** | [−0.088, +0.044] | Diagnostic (near 0) | Uncorrelated overall |
| **Daily Return Skew / Kurtosis** | **+0.54 / 7.94** | — | Distributional diagnostics | Heavy-tailed returns |

- **Agreement of Statistical Checks:** The analytic DSR ($0.762$) and the independent stationary bootstrap probability ($1 - 0.238 = 0.762$) matched to three decimal places, proving that failure to reject the null is not an artifact of parametric tail assumptions.
- **Sample Power Diagnostic:** At the observed market-neutral Sharpe of $+0.37$, achieving a statistically significant DSR $> 0.95$ would require approximately 7,000 trading days (~19 years) of continuous live data. The null is not a marginal sample-size issue that could be rescued by extending data into the holdout.

#### 2. Market-Neutral Daily Return Decomposition (Sums to Net $\alpha$)

| Return Component | Daily Contribution | Economic Interpretation |
|---|---|---|
| **Gross Funding Accrual** | **+0.001525** / day | The gross funding premium is genuine, positive, and mechanical. |
| **Market-Neutral Price Component** | **+0.000068** / day | Economically indistinguishable from zero; wrong sign relative to carry-fade theory. |
| **1× Measured Trading Costs** | **−0.001169** / day | **Consumes ~74.2% of the gross funding harvest.** |
| **Net Market-Neutral Alpha ($\alpha$)** | **+0.000424** / day | Insignificant net residual; CI spans zero. |

- **Turnover Measurement:** Daily turnover averaged **1.85× per day**, meaning ~92.5% of the long and short portfolios rotated every single day.

#### 3. Pre-Registered Mechanism Kill: Short-Leg Price Component

| Metric | Point Estimate | 95% Bootstrap CI | Pre-Registered Rule (§9.2) | Outcome |
|---|---|---|---|---|
| **Short-Leg Price Return / Day** | **−0.000198** / day | **[−0.002648, +0.002206]** | Reliably negative (CI < 0) | **FALSIFIED (CI spans zero)** |

- **Mechanism Falsification Verdict:** While the point estimate has the theoretical negative sign ($-0.0198\%$ per day), the bootstrap confidence interval widely covers positive and negative values. Crowded altcoins do not reliably mean-revert toward spot over a 24-hour horizon. The economic premise of carry-fade is falsified.

#### 4. Cost Sensitivity Ladder

| Cost Multiple | Net Annualized $\text{Sharpe}_{\text{mn}}$ | Deflated Sharpe Ratio (DSR) | Net Daily Alpha ($\alpha$) |
|---|---|---|---|
| **1× Measured Cost** | **+0.37** | 0.762 | +0.000424 / day |
| **2× Measured Cost** | **−0.66** | 0.109 | −0.000745 / day |
| **5× Measured Cost** | **−3.73** | 0.000 | −0.004251 / day |

- **Cost Fragility:** Breakeven execution is reached at only **1.34×** the base measured cost. Any slight increase in execution slippage or adverse selection immediately plunges net performance into severe losses.

#### 5. Subperiod / Era Split Analysis

| Regime Era | Days | $\text{Sharpe}_{\text{mn}}$ | Net Daily $\alpha$ (95% CI) | DSR | Short-Leg Price Return (95% CI) | BTC $\beta$ (95% CI) |
|---|---|---|---|---|---|---|
| **Thin Era (2021-05 → 2022-12)** | 591 | +0.56 | +0.000735 [−0.0011, +0.0026] | 0.763 | −0.002302 [−0.0062, +0.0016] | +0.035 [−0.05, +0.13] |
| **Thick Era (2023-01 → 2024-12)** | 731 | +0.51 | +0.000486 [−0.0012, +0.0023] | 0.766 | +0.001504 [−0.0014, +0.0044] | **−0.116 [−0.18, −0.05]** |

- **Era Consistency:** Both eras fail identically to clear the DSR $> 0.95$ threshold (DSR $\approx 0.76$ in both), and net $\alpha$ spans zero in both eras.
- **Price Component Instability:** The short-leg price drift changes sign across eras ($-0.0023$ in thin era vs. $+0.0015$ in thick era), confirming zero structural stability.
- **Negative Beta Drift:** In the mature, thick market era, high-funding altcoins were strongly correlated with market momentum, imparting a statistically significant negative market beta ($\beta = -0.116$) to the dollar-neutral spread.

#### 6. Out-of-Sample Holdout Discipline

- **Holdout Status:** **SEALED AND UNTOUCHED.**
- Because the strategy tripped both the primary significance kill (§9.1) and the mechanism kill (§9.2) on the training set, the pre-registration protocol strictly prohibited evaluating the 2025-01-01 to 2026-06-30 holdout. Preserving the sealed holdout prevents data mining and overfitting.

### Independently reproduced

Not independently reproduced in internal quantitative backtesting frameworks (PyBroker/Nautilus). Independent source verification was performed directly on the primary Python code, pre-registration text, test suites, and empirical tables in the GitHub repository `JosephBerachah/crypto-fundingrate-alpha` at commit `9d26979a1b2d4714c1f893574f01418332ce276c`.

### Negative evidence

1. **Massive Turnover Cost Drag:** A 1.85× daily turnover consumes 74.2% of the gross funding harvest, leaving a tiny residual that fails standard significance tests.
2. **Absence of Mean-Reverting Price Drift:** The hypothesized price convergence toward spot does not exist ($p > 0.05$ across all tests), refuting the behavioral narrative that crowded perpetuals suffer immediate capital losses.
3. **Severe Cost Asymmetry:** A modest 34% increase in trading costs (from 1.0× to 1.34×) completely eliminates all gross alpha, making the strategy unviable in production execution environments.
4. **Cross-Era Sign Inversion:** The directional price component reversed from negative in 2021–2022 to positive in 2023–2024, demonstrating that shorting high-funding tokens frequently fights strong market trend momentum.

## Falsification plan

To evaluate whether any cross-sectional funding-based strategy can overcome this documented failure mode:

1. **Turnover Reduction via Hysteresis Banding (`research-proposed`):** Rather than full daily rebalancing, implement a dual-threshold buffer where an asset is only entered when entering the top/bottom 10th percentile, but held until it crosses back past the 25th percentile (`research-proposed`).
   - *Falsification Criterion (`research-defined falsification threshold`):* If the hysteresis rule fails to reduce daily turnover below 0.60×/day while maintaining an annualized market-neutral Sharpe $> 1.0$ at 1.5× measured costs, the low-turnover hypothesis is rejected.
2. **Execution Model Stress Test (`research-defined falsification threshold`):** Evaluate candidate strategies under a cost ladder of 5, 8, 12, and 20 bps per side. If the annualized net Sharpe falls below 0.50 at 8 bps/side, the strategy is classified as un-executable in live crypto liquidity pools.
3. **Pure Price Component Independence Test (`research-defined falsification threshold`):** Regress the daily return of the short leg solely on forward 24-hour spot price returns. If the slope is not reliably negative ($t < -2.0$) on out-of-sample data, any reported profitability must be categorized strictly as funding yield harvesting rather than directional alpha.
4. **Pre-Registered Holdout Integrity Audit (`research-defined falsification threshold`):** Any future revision or alternative model must declare a frozen holdout date prior to running backtests. If parameters are tuned on data within the holdout period, the entire experiment is declared invalid.

## Crypto portability

**Direct** — This research was conceived, implemented, and empirically evaluated directly on Binance USDT-margined perpetual futures across hundreds of active and delisted cryptocurrency contracts.

**Microstructure and Portability Considerations:**
- **Funding Rate Mechanics:** Funding rate payments are unique to cryptocurrency perpetual swaps (and certain prediction markets) and have no direct analog in traditional futures (which settle via basis roll to physical or spot delivery).
- **Exchange Fragmentation:** Funding rates diverge across exchanges (e.g., Binance vs. Bybit vs. OKX vs. Hyperliquid). Cross-exchange funding arbitrage introduces counterparty and collateral fragmentation risks not captured in single-venue studies.
- **Taker/Maker Fee Tiers:** High VIP levels (e.g., VIP 5+) or market-maker fee rebates could theoretically improve net margins; however, relying on fee tier subsidies shifts the source of return from predictive market alpha to institutional infrastructure access (`research-proposed`).

## Limitations

- **Underspecification of Liquidity Depth Impact:** The study assumes negligible market impact (Framing A), appropriate for capital allocations $< \$50,000$. Executing this strategy at institutional scale (\$5M–\$50M) would incur significant market impact across illiquid altcoins, further eroding the 26% surviving gross edge (`source-reported`).
- **Single-Venue Scope:** The dataset is restricted to Binance USD-M futures. While Binance represents the deepest perpetual liquidity pool, funding dynamics may exhibit different persistence profiles on decentralized exchanges (e.g., Hyperliquid) (`source-reported`).
- **Equal Weighting Vulnerability:** Equal weighting ($1/k$) inside the top/bottom deciles allocates identical capital to volatile microcap altcoins as to large-cap assets, amplifying idiosyncratic noise and slippage on thin books (`source-reported`).
- **Not Independently Reproduced:** The findings reflect the source author's codebase and backtests; they have not been independently reproduced in an external execution harness (`research-only boundary`).

## Implementation status

Not implemented. No implementation in our research stack (`nautilus-quant-system`, PyBroker, or NautilusTrader). This record is an empirical falsification capture documenting why naive daily-rebalanced funding decile strategies must not be deployed without strict turnover-suppression mechanisms.

## Adoption boundary

This record is research material only. It does not indicate:
- profitable strategy
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet trading
- approved for live trading

This record serves as a rigorous negative-evidence baseline and pre-registered falsification benchmark for all future crypto funding-rate alpha proposals.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` (canonical strategy-research record specification)
- `[[quant/crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11]]` (adjacent study examining cross-sectional funding factors under weekly rebalancing and fixed cost assumptions)
- `[[quant/retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11]]` (falsification of retail CVD and funding rate extremes)
- `[[quant/crypto-smc-fvg-bpr-liquidity-retracement-random-walk-falsification-2026-09-12]]` (falsification of selective limit order execution and retail patterns)

## Sources

1. Joseph Berachah, "Cross-Sectional Crypto Alpha Research: Pre-Registered Study of Return Predictability in Binance Perpetual Futures", GitHub repository `JosephBerachah/crypto-fundingrate-alpha`, immutable commit SHA `9d26979a1b2d4714c1f893574f01418332ce276c` (August 3, 2026). URL: https://github.com/JosephBerachah/crypto-fundingrate-alpha
2. `docs/preregistration.md` (Pre-registered study design, formal hypotheses §1–§9, volume floor justification, and kill criteria).
3. `docs/results_primary.md` (Primary empirical training results, return decomposition, bootstrap confidence intervals, and era splits).
4. `research_log.md` (Chronological research ledger, experiment trial counter N=1, and cost probe methodology).
5. `src/strategy/build_signal.py` (Causal 24h rolling funding sum signal construction, timestamp hour-snapping, and interval tiling).
6. `src/strategy/build_portfolio.py` (Daily decile spread formation, gross exposure 2.0, equal weighting, and delisting settlement).
7. `src/strategy/apply_costs.py` (Transaction cost engine, VIP 0 fee schedule, aggTrades half-spread table, and realized turnover).
8. `src/strategy/evaluate.py` (OLS market-neutral beta regression, Deflated Sharpe Ratio, and stationary bootstrap).
9. `src/data/measure_halfspread.py` (Opposite-aggressor tick-level effective half-spread estimation from Binance aggTrades).
