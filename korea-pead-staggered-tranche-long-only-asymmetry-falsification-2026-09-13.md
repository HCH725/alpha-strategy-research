---
schema: strategy-research-record-v1
title: "Korean Equities Post-Earnings Announcement Drift: Staggered Tranche Execution, Payoff Asymmetry, and Cap-Weighted Mega-Cap Melt-Up Falsification"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - korea-equities
  - kospi
  - pead
  - earnings-momentum
  - staggered-execution
  - payoff-asymmetry
  - benchmark-falsification
  - survivorship-bias
status: research-only
confidence: medium
source_as_of: 2026-09-13
sources:
  - "https://github.com/younghwan91/kr-quant/tree/cc1b6f6a8a85b3b3aecb147d87a2c6e4defe4396/docs/pead-strategy.md"
  - "https://github.com/younghwan91/kr-quant/tree/cc1b6f6a8a85b3b3aecb147d87a2c6e4defe4396/docs/alpha-research.md"
  - "https://github.com/younghwan91/kr-quant/tree/cc1b6f6a8a85b3b3aecb147d87a2c6e4defe4396/docs/GUARDRAILS.md"
  - "https://github.com/younghwan91/kr-quant/tree/cc1b6f6a8a85b3b3aecb147d87a2c6e4defe4396/src/kr_quant/strategies/pead.py"
  - "https://github.com/younghwan91/kr-quant/tree/cc1b6f6a8a85b3b3aecb147d87a2c6e4defe4396/src/kr_quant/engine/sim_crosssectional.py"
  - "https://github.com/younghwan91/kr-quant/tree/cc1b6f6a8a85b3b3aecb147d87a2c6e4defe4396/src/kr_quant/features/fundamentals.py"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Korean Equities Post-Earnings Announcement Drift: Staggered Tranche Execution, Payoff Asymmetry, and Cap-Weighted Mega-Cap Melt-Up Falsification

## Provenance

- **Author:** Younghwan Chae (GitHub: `younghwan91`)
- **Repository:** `https://github.com/younghwan91/kr-quant`
- **Full Commit SHA:** `cc1b6f6a8a85b3b3aecb147d87a2c6e4defe4396`
- **As-of Date:** 2026-09-13 (Repository commit date: 2026-09-12T16:40:53Z; empirical evaluation spans 2016 through July 2026)
- **Primary Source Files Inspected:**
  - `docs/pead-strategy.md` (Comprehensive strategy specification, parameter stability, performance tables, capacity, benchmark adjudication, and failure modes)
  - `docs/alpha-research.md` (Systematic research gate documentation, edge anatomy, trade-level distributions, null hypotheses, and 5 falsified retail strategies)
  - `docs/GUARDRAILS.md` (Preregistered validation requirements, deflated Sharpe, walk-forward purge/embargo, survivorship test)
  - `src/kr_quant/strategies/pead.py` (Implementation of `pead_backtest`, `staggered_backtest`, `pead_rank_ic`, `market_cap_panel`, `recommend_holdings`)
  - `src/kr_quant/engine/sim_crosssectional.py` (Core execution simulator: `rank_tilt_backtest`, `staggered_tranche_backtest`, `rank_ic`)
  - `src/kr_quant/features/fundamentals.py` (Implementation of `earnings_yoy_panel`, `earnings_yield_panel`, `blend_rank`, `combined_signal`)
- **Verification Summary:** Primary source code, simulation loops, unit test suites, and empirical markdown logs at commit `cc1b6f6a8a85b3b3aecb147d87a2c6e4defe4396` were directly examined. All reported statistical metrics (IC, t-ratios, IR, Sharpe, win rate, payoff ratio, drawdown, turnover, and benchmark differentials) map directly to the author's primary research records.

## Economic mechanism

### Source-reported

1. **Information Underreaction to Regulatory Disclosures (DART Filings):**
   In Korean equity markets (KOSPI and KOSDAQ), companies disclose quarterly financial statements via the DART (Data Analysis, Retrieval, and Transfer System) filing platform. Because corporate earnings reports arrive with varying statutory deadlines (quarter-end plus 45 to 90 days), the market exhibits systematic cognitive and structural underreaction to disclosed operating performance. Ranking liquid equities cross-sectionally by year-over-year (YoY) Net Profit growth identifies firms with fundamental earnings acceleration that has not been fully impounded into market prices on the announcement date.

2. **Event-Study Drift Fingerprint:**
   Calendar-time alignment frequently obscures true post-announcement dynamics. In event-aligned event studies tracking Cumulative Abnormal Returns (CAR) relative to peer groups from filing date $t_0$:
   - At day $t+5$: CAR is approximately $0.0\%$, showing zero immediate post-announcement price jump.
   - At day $t+60$: CAR expands monotonically to $+2.12\%$ for positive-surprise firms, while deteriorating peers drift to $-2.28\%$, generating an aggregate spread of $+4.39\%$.
   - Forward rank Information Coefficient (rank-IC) peaks between 60 and 90 trading days (Newey-West $t = +5.43$) and persists up to 6 months ($t > 2.5$), demonstrating a multi-month institutional drift rather than a transitory microstructure spike.

3. **Structural Payoff Asymmetry (Long-Only vs. Long-Short Collapse):**
   When structured as a traditional dollar-neutral Long-Short (L/S) factor portfolio, the strategy collapses: the profit-to-loss payoff ratio drops to $0.96$, erasing net profitability. Conversely, when structured as a Long-Only excess-return strategy, it preserves an asymmetric, convex right-tail payoff distribution (payoff ratio of $1.79$ for top 40 names, and $2.05$ for top 5 names). Individual trades show a modest win rate ($42\%\text{--}45\%$) but extreme positive skewness ($+4.06$, maximum single trade $+376\%$). The top $5\%$ of winning bets generate $170\%$ of aggregate net excess returns, confirming that PEAD in Korea operates as a convex right-tail asset.

4. **Timing Diversification via Staggered Tranches:**
   A standard single-portfolio rebalance executed once every 60 trading days exposes capital to substantial entry-timing luck (Information Ratio $\approx 0.52$). By decomposing the 60-day holding horizon into three overlapping tranches entered 20 trading days apart (rotating one-third of the portfolio each step), timing noise is averaged out. This doubles the Information Ratio to $1.12\text{--}1.15$ ($t = 3.01\text{--}3.06$) while reducing measured one-way portfolio turnover to $0.33$ per 20-day rebalance period.

5. **Cap-Weighted Benchmark Falsification (The Mega-Cap Melt-Up Barrier):**
   Evaluating PEAD against an equal-weighted universe benchmark creates an illusion of persistent outperformance (IR $= 0.87\text{--}1.15$). However, when benchmarked against the actual cap-weighted KOSPI index (which returned $+21.5\%$ annualized with Sharpe $0.85$ from 2016 to 2026), equal-weighted PEAD only beat the index in 5 out of 9 years.
   Crucially, within the top 20 mega-cap equities, PEAD rank-IC is statistically insignificant ($t = 0.62$). Mega-caps are heavily covered by sell-side analysts and trade on forward revisions rather than trailing disclosures. In 2025–2026, when semiconductor mega-caps (Samsung Electronics, SK Hynix) drove an extreme AI/HBM index melt-up ($+84\%$ in early 2026), equal-weighted PEAD underperformed the index by $-66\%\text{p}$ in 2026 (despite achieving a $+41\%$ absolute return). Thus, PEAD is structurally falsified as a core replacement for cap-weighted equity beta; it survives only as a Sharpe-enhancing mid-to-large cap diversifying satellite.

6. **The Survivorship Bias Paradox in Relative-Return Alpha:**
   Restoring delisted and bankrupt stocks into the historical universe database *increased* PEAD excess return against the market. In relative-return strategies, distressed companies systematically drag down the market index, while the fundamental net profit growth ranking systematically avoids deteriorating firms.

### Research interpretation

- **Institutional Diffuse Edge vs. Trader Convex Edge:** The source demonstrates an important taxonomy: while retail breakout/swing strategies rely on a few clustered lottery trades that fail walk-forward validation and random null controls, PEAD is a diffuse institutional edge with positive expectation across thousands of independent bets.
- **Component Roles:**
  - `earnings_yoy_panel` (YoY net profit growth): Primary directional selection signal.
  - Trailing 20-day ADV floor ($\ge 20\text{B KRW}$): Liquidity filter that excludes noise-dominated small caps.
  - Staggered tranche engine: Execution overlay eliminating point-in-time entry volatility.
  - Market-cap rank restriction (ranks 21 to 100): Eliminates over-efficient mega-caps where trailing PEAD has $t = 0.62$.
- **Falsification Insight:** Demonstrates why quant researchers must benchmark against real cap-weighted investable indices rather than synthetic equal-weighted universes. Equal-weighting can report stellar IR while severely underperforming market beta during concentrated index rallies.

## Signal

### Formation timestamp

- Evaluated at trading day boundaries following corporate earnings disclosures on DART (`source-reported`).
- Lookahead-safe execution convention: signals are formed based on disclosures available at market close of date $t$, with position entry dispatched at date $t+1$ (`source-reported`).
- Reporting lag rule: Statutory filing deadline is quarter-end plus 45 calendar days (unconsolidated/quarterly) or plus 90 calendar days (annual audit reports) (`source-reported`).

### Lookback

- Rolling 4 quarters (1 calendar year) for Year-over-Year (YoY) Net Profit calculation:
  $$\text{YoY}_t = \frac{\text{NetProfit}_t - \text{NetProfit}_{t-4}}{|\text{NetProfit}_{t-4}|}$$
  (`source-reported`).
- Trailing 20 trading days for Average Daily Volume (ADV) calculation:
  $$\text{ADV}_{i,t} = \frac{1}{20} \sum_{k=0}^{19} \text{TradeValue}_{i, t-k}$$
  (`source-reported`).

### Long entry

1. **Universe Eligibility:**
   - Common stock actively traded on KOSPI or KOSDAQ (`source-reported`).
   - Trailing 20-day ADV $\ge 20,000\text{ million KRW}$ ($\approx 20\text{B KRW}$ or $\$15\text{M USD}$) (`source-reported`).
   - Finite Net Profit YoY growth value at date $t$ (`source-reported`).
   - Market capitalization tier filter: Rank between 21st and 60th (or 21st and 100th) by descending market capitalization among liquidity-qualified names (`source-reported`).
2. **Cross-Sectional Ranking:**
   - Sort eligible universe in descending order of $\text{YoY}_t$ (`source-reported`).
3. **Portfolio Construction:**
   - Select top $N$ stocks (concentrated: $N=5$ or $N=10$; diversified: $N=40$) (`source-reported`).
   - Equal-weighted allocation within the tranche: $w_i = 1 / N$ (`source-reported`).

### Short entry

- Standalone shorting is deactivated in the recommended production model due to the structural collapse of the short-leg payoff ratio ($0.96$) and Korean short-sale regulatory restrictions (`source-reported`).
- In research-only dollar-neutral L/S configuration (`pead_backtest`): bottom quantile short with gross exposure $0.5$ (`source-reported`).

### Exit

- Time-based expiration: Each tranche is held for exactly $H = 60$ trading days (`source-reported`).
- Tranche rotation: Every $S = 20$ trading days, the oldest tranche ($1/3$ of the portfolio) is liquidated and replaced with the newly formed top-$N$ basket (`source-reported`).
- Delisting exit rule: If an asset is delisted during the holding window, it is liquidated at its final observed transaction price during the 7-day statutory cleanup auction period (`delisting_exit=True`) (`source-reported`).
- Stop-loss / take-profit: No intermediate stop-loss or profit target is applied; cutting positions early truncated right-tail winners and damaged the strategy (`source-reported`).

### Holding period

- Total holding horizon per tranche: 60 trading days ($\approx 3$ calendar months, matching the corporate reporting cycle) (`source-reported`).
- Rebalance step cadence: 20 trading days ($\approx 1$ calendar month) (`source-reported`).
- Overlapping tranches: 3 active tranches held concurrently (`source-reported`).

### Parameters

- `horizon`: 60 trading days (`source-reported`).
- `step`: 20 trading days (`source-reported`).
- `n_tranches`: $\text{horizon} // \text{step} = 3$ (`source-reported`).
- `adv_floor`: $20,000\text{ million KRW}$ ($20\text{B KRW}$) (`source-reported`).
- `adv_window`: 20 trading days (`source-reported`).
- `top_n`: 10 stocks (recommended mid-large) or 40 stocks (all-round diversified) (`source-reported`).
- `cap_rank`: `(20, 60)` or `(20, 100)` (excluding top 20 mega-caps) (`source-reported`).
- `cost_one_way`: $0.0018$ ($0.18\%$ baseline one-way friction) (`source-reported`).
- `stress_cost_one_way`: $0.0050$ ($0.50\%$ 3x friction) (`source-reported`).
- `min_names`: 20 stocks minimum eligible universe (`source-reported`).
- `start_index`: 130 trading days warm-up period (`source-reported`).
- Intraday execution time-of-day slice: `research-proposed` (source uses daily close-to-close accounting).
- Maximum single-stock allocation cap ($15\%$): `research-proposed`.

## Required data

- **Instrument:** Korean equity market common stocks (KOSPI and KOSDAQ) (`source-reported`).
- **Venue:** Korea Exchange (KRX) Cash Equities (`source-reported`).
- **Market Type:** Spot equity (cash market) (`source-reported`).
- **Timeframe:** Daily OHLCV plus quarterly corporate filings (`source-reported`).
- **Data Fields:**
  - Daily Close price (`close`), daily Trading Value (`trade_value`) in million KRW (`source-reported`).
  - Shares outstanding (`shares`) from regulatory filings to construct daily market capitalization (`source-reported`).
  - Quarterly corporate Net Income / Profit after tax from DART financial statements (`source-reported`).
  - Filing disclosure timestamps and official publication dates (`source-reported`).
- **Point-in-Time Availability:**
  - Corporate earnings are strictly gated to publication dates (quarter-end $+45$ to $+90$ days) (`source-reported`).
  - Trading value ADV is trailing 20-day average strictly strictly preceding the rebalance date (`source-reported`).
  - Forward returns constructed strictly as $C_{t+H} / C_{t+1} - 1$, preventing same-day close-to-close lookahead (`source-reported`).
- **Missing-Data & Delisting Handling:**
  - Forward-fill shares outstanding between reporting periods (`source-reported`).
  - Delisted stocks liquidated at last observed price during the KRX 7-day liquidation auction (`source-reported`).

## Execution assumptions

- **Order Timing:** Orders executed at date $t+1$ market open/close following signal generation at date $t$ (`source-reported`).
- **Order Type:** Market / marketable orders participating in continuous auction or closing auction (`source-reported`).
- **Fill Model:** Immediate fill assumed at closing prices (`source-reported`).
- **Transaction Costs & Taxes:**
  - Baseline: $0.18\%$ one-way ($18\text{ bps}$), covering KRX transaction fees, broker commissions, and Korean securities transaction tax (`source-reported`).
  - Turnover accounting: Costs assessed strictly on measured weight changes ($\sum |w_{t} - w_{t-1}|$) rather than assuming full $100\%$ portfolio liquidation each step (`source-reported`).
  - Average turnover: $0.33$ one-way turnover per 20-day step (`source-reported`).
- **Borrow / Shorting:** Zero borrow requirement for the recommended long-only specification (`source-reported`).
- **Execution Capacity:**
  - Trailing ADV of selected top 10 names has median of $49.9\text{B KRW/day}$ (25th percentile $31.4\text{B KRW/day}$) (`source-reported`).
  - At $5\%\text{--}10\%$ market participation rate over a 3-to-5 day execution window, fund capacity is estimated at $62.8\text{B}$ to $1.2\text{ trillion KRW}$ ($\approx \$45\text{M}$ to $\$900\text{M USD}$) (`source-reported`).
  - Slippage model for orders exceeding 5% of daily ADV: `research-proposed` (quadratic market impact function).

## Evidence

### Source-reported

1. **Information Coefficient & Multi-Regime Persistence:**
   - Daily cross-sectional rank-IC of YoY Net Profit vs. 60-day forward return exhibits a Newey-West $t\text{-statistic} = +5.43$ over the full 2018–2026 sample (`source-reported`).
   - Divided into 4 equal chronological regimes, rank-IC remains positive with Newey-West $t > 2.0$ in all 4 regimes (`source-reported`).
   - Parameter stability: holding periods from 10 to 30 days and horizons from 40 to 80 days all generate $t\text{-statistics}$ between $2.4$ and $3.3$ (`source-reported`).

2. **Staggered Long-Only Portfolio Performance:**
   - **Top 40 (Diversified):** Information Ratio $= 1.12$, full-sample $t = 3.01$, payoff ratio $= 1.79$, maximum drawdown $= -7\%$ (`source-reported`).
   - **Top 20 (Intermediate):** Information Ratio $= 1.15$, full-sample $t = 3.06$, payoff ratio $= 1.65$, maximum drawdown $= -15\%$ (`source-reported`).
   - **Top 10 (Mid-Large Cap Tier, Ranks 21–100):** Annualized excess return over peer group $= +14.9\%\text{p/yr}$, Sharpe ratio $= 1.29$, positive excess return in 6 out of 8 years (`source-reported`).
   - **Top 5 (Concentrated):** Cumulative return $= +376\%$ over 8 years, annualized return $= +37.7\%$, Sharpe ratio $= 1.05$, payoff ratio $= 2.05$ (average gain $+14.5\%$ vs. average loss $-7.1\%$), expected return per period $= +6.4\%$, maximum drawdown $= -28\%$ (`source-reported`).

3. **Block Bootstrap Validation:**
   - Block bootstrap resampling ($B = 2,000$ iterations, top 40 staggered book) yielded a median Information Ratio of $+1.19$ with a $95\%$ confidence interval of $[+0.30, +2.20]$ (`source-reported`).
   - $100\%$ of bootstrap resamples produced an Information Ratio $> 0.0$ (`source-reported`).

4. **Cost Tolerance & Signal Degradation:**
   - At $1\text{x}$ baseline cost ($0.18\%$ one-way), top 40 IR $= 0.87$, top 5 IR $= 0.75$ (`source-reported`).
   - At $3\text{x}$ stress cost ($0.50\%$ one-way), IR remains positive: top 40 IR $= 0.50$, top 5 IR $= 0.70$ (`source-reported`).
   - Execution latency test: delaying signal action by 5, 20, and 40 trading days produced IRs of $0.98$, $0.69$, and $0.75$ respectively, proving absence of lookahead and low sensitivity to immediate execution (`source-reported`).

5. **Downside Protection & Factor Attribution:**
   - Correlation with broader market excess return is $+0.21$, with market beta of $+0.10$ (`source-reported`).
   - In the worst $10\%$ market drawdown periods, the market declined by an average of $-8.6\%$ while the PEAD strategy declined by $-7.4\%$ (defensive resilience) (`source-reported`).
   - Pure price momentum and short-term reversal factors tested in the identical framework yielded $t < 1.0$, confirming the alpha originates from fundamental earnings surprise rather than price momentum proxies (`source-reported`).

6. **Benchmark Adjudication & Failure Modes:**
   - Cap-weighted KOSPI proxy returned $+21.5\%$ annualized, Sharpe $0.85$ (2016–2026) (`source-reported`).
   - Top 10 PEAD beat cap-weighted KOSPI in only 5 out of 9 years: 2018 ($+20\%\text{p}$), 2019 ($-19\%\text{p}$), 2020 ($+6\%\text{p}$), 2021 ($+20\%\text{p}$), 2022 ($-2\%\text{p}$), 2023 ($+58\%\text{p}$), 2024 ($+66\%\text{p}$), 2025 ($-13\%\text{p}$), 2026 ($-66\%\text{p}$ through July) (`source-reported`).
   - In 2026, semiconductor mega-cap melt-up propelled KOSPI $+84\%$, while PEAD gained $+41\%$, generating a $-66\%\text{p}$ relative deficit (`source-reported`).
   - Within top 20 mega-caps, PEAD rank-IC $t\text{-statistic} = 0.62$ (insignificant) (`source-reported`).
   - Core-satellite blending: $50\%$ KOSPI core $+ 50\%$ PEAD satellite achieved $+31.6\%$ annualized return with Sharpe $1.22$ vs. KOSPI $0.95$ (`source-reported`).

### Independently reproduced

Not independently reproduced. This research is captured directly from primary code and empirical logs in repository `https://github.com/younghwan91/kr-quant` (commit `cc1b6f6a8a85b3b3aecb147d87a2c6e4defe4396`).

### Negative evidence

1. **L/S Symmetry Breakdown:** Symmetrical dollar-neutral long-short construction fails completely; short positions show a payoff ratio of $0.96$, destroying the strategy edge (`source-reported`).
2. **Mega-Cap Inefficacy:** Trailing earnings surprise exhibits zero predictive power in the top 20 mega-cap equities ($t = 0.62$), which trade on forward consensus expectations (`source-reported`).
3. **Severe Multi-Year Drawdowns vs. Index:** In concentrated configurations (top 5), the strategy experiences maximum drawdowns of $-28\%$ and underwater periods lasting $2.5\text{--}3.0$ years (`source-reported`).
4. **Failure in Extreme Momentum Melt-Ups:** During hyper-concentrated index rallies driven by a few mega-caps (e.g., 2026 semiconductor surge), equal-weighted PEAD lags the benchmark by over $60\%\text{p}$ (`source-reported`).
5. **Ablation of Upgrades:** Combining PEAD with foreign investor net buying or earnings acceleration metrics was explicitly tested and rejected as horizon-mined statistical artifacts (`source-reported`).

## Falsification plan

1. **Out-of-Sample Forward Testing:**
   - Evaluate performance on newly filed DART financial statements from 2026H2 onward.
   - *Failure Metric:* If out-of-sample forward rank-IC over a minimum of 6 quarterly reporting cycles yields a mean $\text{IC} \le 0.01$ or Newey-West $t < 1.96$ (`research-defined falsification threshold`), reject the hypothesis of structural drift persistence.
2. **Surprise Formulation Ablation:**
   - Compare pure Net Profit YoY against Standardized Unexpected Earnings (SUE) computed against analyst consensus revisions from Naver/FnGuide.
   - *Failure Metric:* If analyst consensus SUE achieves an Information Ratio $> 1.50$ while YoY growth collapses to $\text{IR} < 0.30$ in mid-cap stocks (`research-defined falsification threshold`), the YoY proxy is subsumed and must be deprecated.
3. **Transaction Cost and Liquidity Stress:**
   - Test execution at one-way costs ranging from $25\text{ bps}$ to $75\text{ bps}$ under simulated market impact.
   - *Failure Metric:* If the 3-tranche staggered book's net Information Ratio drops below $0.20$ under $35\text{ bps}$ one-way cost (`research-defined falsification threshold`), falsify the strategy as an un-tradable friction casualty.
4. **Sector and Breadth Neutrality Test:**
   - Apply industry-neutral cross-sectional ranking (demeaning Net Profit YoY by KRX sector median).
   - *Failure Metric:* If industry-neutralized PEAD explains less than $30\%$ of the unconstrained strategy return ($R^2 < 0.30$ or neutralized IR $< 0.35$) (`research-defined falsification threshold`), the anomaly is primarily an uncompensated cyclical sector bet rather than company-level underreaction.
5. **Random Entry Null Adjudication:**
   - Benchmark the staggered book against a 500-draw random entry null distribution with matching portfolio turnover and holding horizon.
   - *Failure Metric:* If the realized strategy R-multiple distribution fails to exceed the 90th percentile of the random null (`p > 0.10`) (`research-defined falsification threshold`), reject the strategy as noise overfitting.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Structural Differences:**
  - Crypto assets do not have quarterly regulatory filing requirements (SEC Form 10-Q or DART financial statements).
  - Fundamental financial disclosures are replaced by on-chain economic metrics (e.g., protocol revenue, token burns, fees generated, and treasury inflows tracked via DeFiLlama or Artemis).
- **Adaptation Thesis:**
  - A crypto-adapted version would condition on sudden jumps or quarterly/monthly growth in protocol fees and revenue (e.g., Uniswap LP fees, Maker/Sky protocol fees, Solana network transaction fees).
  - Positions would be taken on crypto perpetuals or spot pairs following verifiable on-chain fee growth milestones (`research-proposed`).
- **Crypto-Specific Frictions:**
  - Extreme token-unlock dilution (FDV vs. circulating market cap) can completely overwhelm fundamental protocol earnings.
  - Crypto market beta is dominated by Bitcoin dominance cycles; during liquidity droughts, fundamental protocol growth does not protect altcoins from severe sell-offs.
  - Perpetual funding rate costs can rapidly consume multi-month drift returns if positive-surprise tokens attract crowded long positioning.

## Limitations

- **Sample Size Limitation:** The DART panel covers approximately 8 years of quarterly corporate disclosures, representing $\approx 32$ non-overlapping quarterly filing events (`source-reported`).
- **Benchmark Mismatch:** The strategy is an equal-weighted mid/large-cap alpha. It cannot track or beat cap-weighted indices during mega-cap hyper-concentration (`source-reported`).
- **Severe Cyclical Drawdowns:** Long-only equity risk exposes the strategy to broad market beta drawdowns; during systemic equity bear markets (e.g., 2022 interest rate shock), positive earnings surprise stocks still sustained substantial absolute losses (`source-reported`).
- **Delisting Liquidity Risk:** While liquidating delisted stocks during the 7-day KRX cleanup auction was modeled, real-world executions during bankruptcy liquidations may encounter frozen order books and zero bids (`research-proposed`).
- **Data Availability Gaps:** Historical share counts are snapshot-based and required forward filling, creating minor tracking discrepancies in historical market capitalization tiers (`source-reported`).

## Implementation status

- Frontmatter status: `implementation_status: not-implemented`.
- The strategy has been validated in the external author's repository (`kr_quant` Python backtest framework) but has not been implemented or integrated into our internal quantitative research stack (`nautilus-quant-system`, PyBroker, or NautilusTrader).
- No paper trading, testnet verification, or live execution has been conducted.

## Adoption boundary

- Frontmatter status: `adoption: not-approved`, `status: research-only`, `approval_scope: research-only`.
- This record serves strictly as normalized research material for ChatGPT Research Intake Review and Hermes Wiki Brain ingestion.
- Presence in this repository does not constitute approval for live capital allocation, automated execution, or strategy deployment.

## Related Wiki records

- `[[quant/earnings-announcement-premium-jump-risk-decay-falsification-2026-09-13]]` (Distinguishes ex-ante jump risk premium from post-earnings underreaction drift)
- `[[quant/retail-signal-three-gate-falsification-oscillator-volume-calendar-trend-2026-09-04]]` (Multi-gate falsification of retail technical anomalies)
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` (Methodological standard for purge and embargo boundaries in overlapping holding horizons)

## Sources

1. **Younghwan Chae (`younghwan91`), "PEAD Strategy Documentation & Empirical Verification"**, `https://github.com/younghwan91/kr-quant/tree/cc1b6f6a8a85b3b3aecb147d87a2c6e4defe4396/docs/pead-strategy.md` (As-of: 2026-09-12).
2. **Younghwan Chae (`younghwan91`), "Alpha Research Adjudication & Edge Taxonomy"**, `https://github.com/younghwan91/kr-quant/tree/cc1b6f6a8a85b3b3aecb147d87a2c6e4defe4396/docs/alpha-research.md` (As-of: 2026-09-12).
3. **Younghwan Chae (`younghwan91`), "Quantitative Validation Guardrails & Pre-Registration"**, `https://github.com/younghwan91/kr-quant/tree/cc1b6f6a8a85b3b3aecb147d87a2c6e4defe4396/docs/GUARDRAILS.md` (As-of: 2026-09-12).
4. **`kr_quant` Core Implementation Files**, Commit SHA `cc1b6f6a8a85b3b3aecb147d87a2c6e4defe4396`:
   - `src/kr_quant/strategies/pead.py`
   - `src/kr_quant/engine/sim_crosssectional.py`
   - `src/kr_quant/features/fundamentals.py`
