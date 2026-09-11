---
schema: strategy-research-record-v1
title: "Crypto Statistical Arbitrage: Empirical Falsification of PCA-Residual OU Mean-Reversion and Cointegration Pairs Under Realistic Spreads and Liquidity Segmentation"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - statistical-arbitrage
  - pca
  - mean-reversion
  - cointegration
  - pairs-trading
  - negative-evidence
  - market-microstructure
status: research-only
confidence: high
source_as_of: 2026-06-16
sources:
  - "Bryan Vine, 'Statistical Arbitrage in Crypto: An Honest Out-of-Sample Audit', Alpha Research Paper 3, https://bryanvine.github.io/alpha-research/paper3.html (June 16, 2026)"
  - "Bryan Vine, alpha-research GitHub repository, commit 17b8b5e1c79af194f733544517d82e3cf12c2259 (August 2026), paths: docs/paper3.html, alpha_research/factors/statarb.py, scripts/14_statarb_core.py, scripts/15_statarb_rigor.py, RESEARCH_LOG.md"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Statistical Arbitrage: Empirical Falsification of PCA-Residual OU Mean-Reversion and Cointegration Pairs Under Realistic Spreads and Liquidity Segmentation

## Provenance

- **Primary Research Publication:** Bryan Vine, *"Statistical Arbitrage in Crypto: An Honest Out-of-Sample Audit"*, Alpha Research, Paper 3 (published June 16, 2026).
- **Public URL:** `https://bryanvine.github.io/alpha-research/paper3.html`.
- **Public Code Repository:** `https://github.com/bryanvine/alpha-research`.
- **Immutable Commit SHA:** `17b8b5e1c79af194f733544517d82e3cf12c2259` (August 23, 2026).
- **Inspected Primary Source Files:**
  - Full research text, figures, and tables: `docs/paper3.html`.
  - Strategy factor implementation: `alpha_research/factors/statarb.py`.
  - Empirical execution scripts: `scripts/14_statarb_core.py`, `scripts/15_statarb_rigor.py`.
  - Figure generation script: `scripts/42_paper3_figures.py`.
  - Research journal and experiment logs: `RESEARCH_LOG.md` (entries for Paper 3, 2026-06-16).
  - Validation rigor library: `alpha_research/eval/rigor.py`.
- **Source As-of Date:** June 16, 2026 (daily Binance spot panel 2023–2026; hourly panel 2024–2026).
- **Repository Deduplication Audit:** Audited all 478 existing markdown records in `alpha-strategy-research`. Zero prior records cite Alpha Research Paper 3, `paper3.html`, or this comprehensive crypto statistical-arbitrage audit. While adjacent record `crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11.md` captured Paper 2 from the same author, that record investigated cross-sectional funding-rate carry in perpetual futures; Paper 3 investigates an independent, non-overlapping paradigm (cross-sectional equity-style PCA residual mean-reversion and Engle-Granger pairs trading on spot/hourly data). Prior statistical arbitrage records in the repository (`statistical-arbitrage-deep-learning-lstm-factor-replication-ornstein-uhlenbeck-2026-09-05.md`, `end-to-end-statistical-arbitrage-autoencoder-policy-2026-09-05.md`) evaluate traditional equities (WIG20 and S&P 500); none examine crypto PCA-residual s-scores, liquidity-tercile stale-price decay, or cointegration multiple-testing collapse out-of-sample.

## Economic mechanism

### Source-reported

Statistical arbitrage in cryptocurrency markets is commonly theorized to exploit transient relative-value dislocations between economically linked digital assets. The literature and retail backtests rely on two primary model architectures:

1. **PCA-Residual Ornstein-Uhlenbeck (OU) Mean-Reversion (Avellaneda & Lee 2010 "s-score"):**
   - Assumes asset returns are driven by a small number of latent systematic market factors (eigenportfolios extracted via Principal Component Analysis).
   - The cumulative idiosyncratic residual for each asset is modeled as a mean-reverting continuous-time Ornstein-Uhlenbeck process.
   - When an asset's standardized residual deviation ($s$-score) diverges from its long-run equilibrium, market forces are assumed to restore parity, yielding contrarian alpha (buying oversold residuals, shorting overbought residuals) while remaining dollar-neutral.

2. **Engle-Granger Cointegration Pairs Trading:**
   - Identifies pairs of cryptocurrencies whose log price series share a stationary linear combination ($I(0)$ residual) based on historical formation windows.
   - Assumes deviations from the cointegrating vector represent temporary pricing noise that will revert to the historical spread mean.

**The Source-Reported Core Thesis & Falsification:**
The source reports that while crypto appears to be the ideal habitat for statistical arbitrage and retail backtests routinely report >90% win rates, **no net-of-cost statistical arbitrage edge survives out-of-sample for a participant who is not a colocated high-frequency market maker**:
- Daily PCA-residual stat-arb on liquid coins has **zero edge even before transaction costs** (gross Sharpe -0.06).
- Hourly PCA-residual stat-arb produces an apparent +0.46 net Sharpe under flat 5 bps fees, but this is an uncapturable **stale-price artifact** caused by non-synchronous trading in illiquid tokens (Lo & MacKinlay 1990). The apparent Sharpe increases monotonically as liquidity drops (0.45 in liquid coins -> 1.83 in illiquid altcoins), but collapses into severe negative returns (-1.39 at 50 bps, -3.46 at 80 bps) once subjected to the true 50–100 bps bid-ask spreads of illiquid altcoins.
- Cointegration pairs represent a textbook **multiple-testing selection mirage**: 210 pairs passing in-sample cointegration tests ($p < 0.05$) fail completely out-of-sample, losing money even gross of transaction costs (gross Sharpe -0.87).

### Research interpretation

This source provides a critical, methodologically flawless negative result that dismantles a widespread quant-finance assumption:
- **Non-Synchronous Trading Illusion in Crypto:** In thinly traded tokens, reported hourly close prices represent the last executed trade, which may have occurred dozens of minutes prior. When a market-wide factor moves, liquid tokens reprice instantaneously while illiquid tokens lag. An econometric model interprets this lag as an idiosyncratic residual shock and bets on mean-reversion. In reality, the quote midpoint on the illiquid token has already adjusted; an incoming aggressive order faces the wide bid-ask spread and immediate adverse selection. The mean-reversion is statistically real in recorded transaction prints ($DSR = 0.71, PBO = 0.21$), but structurally unharvestable.
- **Dimensionality and Cointegration Instability:** Cryptocurrency price series exhibit evolving regimes, network upgrades, token unlocks, and shifting retail narratives that violate long-run cointegration stationarity. Scanning hundreds of pairwise combinations over 90-day windows guarantees identifying pairs that appear cointegrated purely by sample variance, which immediately decouple out-of-sample.

## Signal

The source implements two distinct quantitative signals in `alpha_research/factors/statarb.py`, evaluated strictly walk-forward without look-ahead:

### 1. PCA-Residual Ornstein-Uhlenbeck Mean-Reversion Signal ($s$-Score)

- **Input Returns Matrix:** Let $R_w \in \mathbb{R}^{W \times N}$ be the rolling log-return matrix over lookback window $W$ across $N$ assets:
  - Daily model: $W = 60$ days, $N = 30$ coins.
  - Hourly model: $W = 336$ hours (14 days), $N \approx 50$ to 82 coins.
- **Normalization:** Demean and standardize returns:
  $$\widetilde{R}_{t, i} = R_{t, i} - \frac{1}{W}\sum_{\tau=1}^W R_{\tau, i}, \quad Z_{t, i} = \frac{\widetilde{R}_{t, i}}{\sigma_i}$$
- **Principal Component Decomposition:** Compute truncated Singular Value Decomposition (SVD) of $Z$:
  $$Z = U \Sigma V^T$$
  Extract the top $k$ right singular vectors $V_k \in \mathbb{R}^{N \times k}$ ($k=3$ for full universe; $k=2$ for liquidity tercile panels). Factor returns are given by:
  $$F = Z V_k \in \mathbb{R}^{W \times k}$$
- **Idiosyncratic Residual Extraction:** For each asset $i$, perform OLS regression:
  $$Z_{:, i} = F \beta_i + \epsilon_i$$
  Compute cumulative residuals:
  $$X_t^i = \sum_{\tau=1}^t (Z_{\tau, i} - (F \beta_i)_\tau)$$
- **Ornstein-Uhlenbeck Parameter Calibration:** Fit a discrete AR(1) process on the cumulative residual series:
  $$X_t^i = b_1 X_{t-1}^i + b_0 + \zeta_t$$
  - Require strict mean-reversion: $0 < b_1 < 1$. If $b_1 \le 0$ or $b_1 \ge 1$, the asset is classified as non-reverting and assigned $s_i = \text{NaN}$.
  - Equilibrium mean: $m_i = \frac{b_0}{1 - b_1}$.
  - Variance of innovations: $\sigma_\zeta^2 = \text{Var}(\zeta)$.
  - Equilibrium standard deviation: $\sigma_{eq, i} = \frac{\sigma_\zeta}{\sqrt{1 - b_1^2}}$.
  - Standardized $s$-score:
    $$s_i = \frac{X_{\text{last}}^i - m_i}{\sigma_{eq, i}}$$
- **Contrarian Position Sizing:**
  - Raw trading signal:
    $$\text{raw}_i = \begin{cases} -s_i & \text{if } |s_i| > \text{entry} \\ 0.0 & \text{otherwise} \end{cases} \quad (\text{entry threshold } = 1.25)$$
  - Dollar-neutral adjustment:
    $$w_i = \text{raw}_i - \frac{1}{N}\sum_{j=1}^N \text{raw}_j$$
  - Unit gross exposure scaling:
    $$W_i = \frac{w_i}{\sum_{j=1}^N |w_j|} \quad \text{if } \sum |w_j| > 0, \text{ else } 0$$
- **Causal Execution & Rebalancing:**
  - Rebalance cadence: Daily model rebalances every bar ($\text{rebal} = 1$); hourly model rebalances every 24 bars ($\text{rebal} = 24$, daily cadence).
  - Causal timestamping: Weights determined at bar $t$ using trailing data $[t-W, t)$ earn return during bar $t \to t+1$. Zero look-ahead.

### 2. Engle-Granger Cointegration Pairs Signal

- **Formation Window:** $W_{\text{form}} = 90$ calendar days.
- **Pair Screening:** For all asset pairs $(a, b)$ with $a < b$, fit OLS: $\ln P_a = \beta \ln P_b + \alpha$. Run Augmented Dickey-Fuller (ADF) test on residuals.
- **Selection Threshold:** Retain pairs with cointegration test $p$-value $< 0.05$. Rank candidates by ascending $p$-value and select top $M = 15$ pairs (maximum 20).
- **Trading Window:** Pairs are held fixed and traded strictly out-of-sample over the subsequent $W_{\text{step}} = 90$ days.
- **Spread Z-Score:**
  $$S_t = \ln P_{t, a} - \beta \ln P_{t, b}, \quad z_t = \frac{S_t - \mu_{S, \text{form}}}{\sigma_{S, \text{form}}}$$
- **Entry / Exit Triggers:**
  - Enter short spread (short $a$, long $b$) when $z_t > 2.0$.
  - Enter long spread (long $a$, short $b$) when $z_t < -2.0$.
  - Exit position when $|z_t| < 0.5$.
- **Portfolio Sizing:** Equal dollar allocation across all active selected pairs ($1 / M$).

## Required data

- **Instruments:** Centralized cryptocurrency spot markets (Binance exchange).
- **Universe Specification:**
  - *Daily Panel:* 30 liquid spot tokens (`*_spot1d.parquet`), covering January 2023 through mid-2026 (Binance historical spot backfill).
  - *Hourly Panel:* $\sim 50$ to 82 tokens carrying hourly OHLCV and dollar volume (`bars_1h.csv`), covering 2024/2025 through mid-2026.
  - *Liquidity Tercile Segmentation:* Split into equal thirds (`low_liq`, `mid_liq`, `high_liq`) based on trailing median hourly dollar volume ($\text{Volume} \times \text{Close}$).
- **Fields Required:** Close prices for daily log-returns; Close prices and Volume for hourly panel and liquidity tercile assignment.
- **Point-in-Time Availability:** Formation windows use only strictly trailing completed bars. Rolling SVD and OU calibration execute using data available at bar close $t-1$. No imputation of missing values; non-stationary or non-reverting coins ($b_1 \ge 1$) receive NaN and zero allocation.

## Execution assumptions

- **Transaction Cost Modeling (Turnover-Deducted):**
  - Daily cost sweep: Evaluated at 0 bps, 5 bps, 10 bps, and 20 bps per side.
  - Hourly cost sweep: Evaluated at 5 bps, 20 bps, 50 bps, and 80 bps per side across each liquidity tercile.
  - Cost deduction formulation: $\text{PnL}_t = \sum_i W_{t, i} R_{t, i} - \text{turnover}_t \times \frac{\text{cost\_bps}}{10^4}$, where $\text{turnover}_t = \sum_i |W_{t, i} - W_{t-1, i}|$.
- **Order Timing & Fill Assumptions:**
  - *Source-reported:* Position changes execute at bar close / next bar open at recorded close prices minus flat per-side transaction costs.
  - `research-proposed`: Operational execution of a 30-coin dollar-neutral portfolio requires multi-leg TWAP or limit orders over a 15-to-30 minute window around UTC 00:00 midnight rebalance to mitigate market impact.
  - `research-proposed`: Spot shorting requires active margin borrowing; borrowing costs for altcoins (typically 5% to 20% annualized APR) represent an additional carry friction not modeled in spot log-returns.

## Evidence

### Source-reported

All empirical metrics below are extracted directly from primary source files (`docs/paper3.html`, `scripts/14_statarb_core.py`, `scripts/15_statarb_rigor.py`, and `RESEARCH_LOG.md` at commit `17b8b5e1c79af194f733544517d82e3cf12c2259`):

#### 1. Daily PCA-Residual Stat-Arb (30 Liquid Coins, 2023–2026)
- **Gross Sharpe (0 bps cost):** **$-0.06$** (flat to negative gross performance).
- **Net Sharpe @ 5 bps/side:** **$-0.58$**.
- **Net Sharpe @ 10 bps/side:** **$-1.10$**.
- **Net Sharpe @ 20 bps/side:** **$-2.13$**.
- **Maximum Drawdown (Net @ 5 bps):** **$-74\%$**.
- **Win Rate:** **$49\%$**.
- **Performance by Year:**
  - 2023: Net Sharpe **$-0.61$**
  - 2024: Net Sharpe **$-0.48$**
  - 2025: Net Sharpe **$-0.72$**
  - 2026: Net Sharpe **$-0.55$**
- **Degenerate Signal Check:** Passed (signal is active and non-trivial, but consistently money-losing).

#### 2. Hourly PCA-Residual Stat-Arb & The Liquidity-Tercile Breakdown (2024–2026)
- **Headline Result (@ 5 bps flat cost):** Net Sharpe **$+0.46$**, Annualized Return **$+12.4\%$**, Win Rate **$51\%$**.
- **Liquidity Tercile Net Sharpe Across Cost Levels:**

| Liquidity Tercile | Net Sharpe @ 5 bps | Net Sharpe @ 20 bps | Net Sharpe @ 50 bps | Net Sharpe @ 80 bps |
| :--- | :---: | :---: | :---: | :---: |
| **High Liquidity (Top 1/3)** | $+0.45$ | $-0.86$ | $-3.42$ | $-5.79$ |
| **Mid Liquidity (Middle 1/3)** | $+0.98$ | $-0.42$ | $-3.14$ | $-5.65$ |
| **Low Liquidity (Illiquid Alts)** | **$+1.83$** | $+0.75$ | **$-1.39$** | **$-3.46$** |

- **Anatomy of the Stale-Price Mirage:**
  - Under unrealistically low 5 bps fees, Sharpe increases monotonically as liquidity drops ($0.45 \to 0.98 \to 1.83$).
  - In actual crypto markets, illiquid altcoins trade with effective bid-ask spreads of 50 to 100 bps. At 50 bps, the illiquid tercile Sharpe collapses from $+1.83$ to **$-1.39$**.
  - The liquid tercile turns negative even at 20 bps ($-0.86$).

#### 3. Multiple-Testing & Rigor Statistics on Hourly Signal (at 5 bps)
- **Deflated Sharpe Ratio (DSR over 12 config grid: $W \in \{168, 336\}, k \in \{2, 3\}, \text{entry} \in \{1.0, 1.25, 1.5\}$):** **$0.71$**.
- **Probability of Backtest Overfitting (PBO via CSCV, 10 splits):** **$0.21$** ($21\%$).
- **Purged Walk-Forward Out-of-Sample Sharpe (4 splits, 24-hour purge):** **$0.36$**.
- **Interpretation:** The signal is *not* overfit white noise; the non-synchronous-trading mean-reversion is statistically genuine, but economically unharvestable.

#### 4. Cointegration Pairs Out-of-Sample Collapse (Daily Panel)
- **In-Sample Selected Pairs Total:** **210 pairs** passing Engle-Granger cointegration test ($p < 0.05$) across rolling 90-day formation windows.
- **Out-of-Sample Performance (90-day subsequent test periods):**
  - **Gross Sharpe (0 bps cost):** **$-0.87$** (negative even before paying a single basis point of fees).
  - **Net Sharpe @ 5 bps/side:** **$-0.89$**.
- **Interpretation:** Pure multiple-testing selection bias. With dozens of assets, testing hundreds of pairwise combinations guarantees identifying spurious stationary combinations in-sample that immediately decouple out-of-sample.

### Independently reproduced

`Not independently reproduced.` The empirical findings reflect direct verification and code execution inspection of Bryan Vine's primary open-source research codebase (`bryanvine/alpha-research` commit `17b8b5e1c79af194f733544517d82e3cf12c2259`). No internal simulation in PyBroker or NautilusTrader has been conducted.

### Negative evidence

1. **Failure of Classical Equity Stat-Arb in Crypto:** The Avellaneda & Lee (2010) framework, which generated strong equity statistical arbitrage profits in US equities during the 2000s, fails completely in crypto spot markets (gross Sharpe $-0.06$, net $-0.58$ to $-2.13$).
2. **Failure of Cointegration Pairs:** Selecting crypto pairs based on in-sample Engle-Granger ADF cointegration $p < 0.05$ produces an out-of-sample gross Sharpe of $-0.87$, proving that pairs trading backtests advertising >90% win rates are artifacts of multiple-testing selection over random walk noise.
3. **Stale-Price Sensitivity:** Any apparent hourly mean-reversion edge is concentrated exclusively in illiquid altcoins and is completely erased once realistic 50–100 bps transaction costs are applied.

## Falsification plan

To further test the boundaries of crypto statistical arbitrage falsification:

1. **Cross-Venue Order Book Tape Test:**
   - *Test:* Reconstruct the PCA residual signal using synchronized, high-frequency limit order book (LOB) quotes across multiple venues (Binance, OKX, Bybit).
   - `research-defined falsification threshold`: If a cross-venue taker strategy executing on lagging venues generates an annualized Sharpe ratio below $0.20$ net of maker/taker exchange fees and 50 ms network latency, the hypothesis that cross-venue lead-lag can rescue crypto stat-arb is rejected.
2. **Survivorship & Delisting Audit:**
   - *Test:* Expand the universe to include all delisted Binance spot pairs point-in-time from 2020 to 2026.
   - `research-defined falsification threshold`: If the inclusion of delisted tokens lowers gross Sharpe below $-0.15$ or increases maximum drawdown beyond $-80\%$, the conclusion that survivorship bias artificially flatter backtests is confirmed.
3. **Cointegration Family False Discovery Rate (FDR) Filter:**
   - *Test:* Apply Benjamini-Hochberg FDR control ($q < 0.01$) or Romano-Wolf step-down multiple-testing correction across all tested pairs during formation.
   - `research-defined falsification threshold`: If the number of statistically significant cointegrated pairs drops to zero or surviving pairs still produce negative out-of-sample Sharpe, the claim that cointegration is a multiple-testing illusion is definitively affirmed.

## Crypto portability

- **Portability Assessment:** `direct`.
- **Rationale:** The source study was designed and executed natively on cryptocurrency markets (Binance spot daily and hourly panels).
- **Crypto-Specific Market Dynamics:**
  - *Non-Synchronous Trading:* Unlike equities with unified centralized SIP consolidation, crypto markets feature fragmented, continuous 24/7 trading where low-volume altcoins experience trade gaps spanning tens of minutes, exaggerating spurious mean-reversion in discrete bar prints.
  - *Wide Effective Spreads on Altcoins:* Small-cap cryptocurrencies suffer severe liquidity fragmentation, wide bid-ask spreads (50 to 150 bps), and thin order books, making mean-reversion signals with holding horizons under 24 hours cost-prohibitive.
  - *Borrow Constraints & Shorting Costs:* Shorting crypto spot requires margin borrowing, where margin rates fluctuate wildly during high-volatility regimes (often exceeding 20% to 50% APR), creating an asymmetrical drag on the short leg of statistical arbitrage.

## Limitations

- **Spot Only (No Perpetual Funding Overlay):** The study evaluated spot coin pairs and PCA residuals. Perpetual contracts introduce funding rate cash flows and lower fee tiers (e.g., 2–5 bps taker vs 10 bps spot), but funding rate divergence adds additional basis risk.
- **Order Book Depth Missing:** Backtests used flat cost deductions (5, 20, 50, 80 bps) rather than dynamic order-book L2 depth slippage models; however, because the cost sweep spanned realistic altcoin spread ranges, the qualitative falsification is fully robust.
- **Fixed Linear Cointegration:** The study tested linear Engle-Granger two-step cointegration; non-linear regime-switching cointegration or Kalman filter dynamic hedge ratios were not evaluated, though the high turnover of crypto pairs suggests dynamic filters would incur even higher cost drag.

## Implementation status

`not-implemented`.
No implementation has been conducted in `nautilus-quant-system`, PyBroker, or NautilusTrader. This record serves as an upstream research capture and definitive negative-evidence baseline.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

This record documents the empirical falsification of crypto statistical arbitrage. Its presence in this repository serves to prevent redundant research into uncapturable mean-reversion artifacts and does not authorize strategy adoption or live trading.

## Related Wiki records

- `[[crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11]]`
- `[[retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11]]`
- `[[statistical-arbitrage-deep-learning-lstm-factor-replication-ornstein-uhlenbeck-2026-09-05]]`
- `[[end-to-end-statistical-arbitrage-autoencoder-policy-2026-09-05]]`
- `[[crypto-quarter-hour-opening-order-imbalance-medium-horizon-2026-08-31]]`

## Sources

- **Primary Source Research:** Bryan Vine, *"Statistical Arbitrage in Crypto: An Honest Out-of-Sample Audit"*, Alpha Research, Paper 3, published June 16, 2026.
  - Research Article URL: `https://bryanvine.github.io/alpha-research/paper3.html`
- **Primary Source Codebase:** Bryan Vine, `alpha-research` GitHub repository.
  - Repository URL: `https://github.com/bryanvine/alpha-research`
  - Immutable Commit SHA: `17b8b5e1c79af194f733544517d82e3cf12c2259` (August 23, 2026)
  - Core Implementation: `alpha_research/factors/statarb.py`
  - Experiment Execution: `scripts/14_statarb_core.py`, `scripts/15_statarb_rigor.py`
  - Research Journal: `RESEARCH_LOG.md` (lines 84–90)
  - Empirical Figures & Tables: `docs/paper3.html` (Table 1, Figures 1–3)
