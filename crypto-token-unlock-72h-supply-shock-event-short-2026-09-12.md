---
schema: strategy-research-record-v1
title: Crypto Token Unlock 72-Hour Supply Shock Event-Driven Short with Cliff and Recipient Filtering
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - token-unlock
  - supply-shock
  - event-study
  - binance
  - cross-sectional
status: research-only
confidence: medium
source_as_of: 2026-09-12
sources:
  - "HoKwang Kim, 'The 72-Hour Shock? Preliminary Evidence from 52 Token Unlock Events on Binance: A Cross-Sectional Analysis of Unlock Events and Their Asymmetric Impact on Cryptocurrency Prices', Working Paper Version 3.1, GitHub repository gameworkerkim/vibe-investing, commit ea0b6f20c6ea59c494ce5e981006472693256f00, dated April 2026, as-of 2026-09-12"
  - "HoKwang Kim, 'UNL-10 Hybrid Strategy Backtest Implementation', 01.Trading Strategy/Token unlock 72h shock analysis /src/unl10_strategy_backtest.py, commit ea0b6f20c6ea59c494ce5e981006472693256f00"
  - "HoKwang Kim, 'Token Unlock Counter-Trading Bot', 01.Trading Strategy/Token unlock 72h shock analysis /src/unlock_counter_trading_bot.py, commit ea0b6f20c6ea59c494ce5e981006472693256f00"
  - "HoKwang Kim, 'Token Unlock Strategies Backtest Results Matrix', 01.Trading Strategy/Token unlock 72h shock analysis /data/05_unlock_trading_strategies_backtest.csv, commit ea0b6f20c6ea59c494ce5e981006472693256f00"
  - "HoKwang Kim, 'Binance Token Unlock Events 2023-2025 Dataset', 01.Trading Strategy/Token unlock 72h shock analysis /data/01_binance_token_unlock_events_2023_2025.csv, commit ea0b6f20c6ea59c494ce5e981006472693256f00"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Token Unlock 72-Hour Supply Shock Event-Driven Short with Cliff and Recipient Filtering

## Provenance

- **Author / Research Lab:** HoKwang Kim (Dennis Kim), ORCID: [0009-0002-0962-2175](https://orcid.org/0009-0002-0962-2175), Independent Researcher, Seoul, Republic of Korea (Chief Executive Officer of Betalabs Inc., operating in an independent academic research capacity).
- **Title:** *The 72-Hour Shock? Preliminary Evidence from 52 Token Unlock Events on Binance: A Cross-Sectional Analysis of Unlock Events and Their Asymmetric Impact on Cryptocurrency Prices* (Working Paper Version 3.1, April 2026 / updated September 2026).
- **Canonical Repository:** `https://github.com/gameworkerkim/vibe-investing`
- **Immutable Commit SHA:** `ea0b6f20c6ea59c494ce5e981006472693256f00`
- **Source As-Of Date:** 2026-09-12 (commit timestamp `2026-09-12T01:54:47Z`).
- **Primary Source Code & Documentation Paths:**
  - Full Working Paper: `01.Trading Strategy/Token unlock 72h shock analysis /Token unlock 72h shock ssrn v3 1 en.MD`
  - Hybrid Strategy Backtest Script: `01.Trading Strategy/Token unlock 72h shock analysis /src/unl10_strategy_backtest.py`
  - 10-Strategy Backtest Matrix Script: `01.Trading Strategy/Token unlock 72h shock analysis /src/backtest_10_strategies.py`
  - Operational Execution Bot: `01.Trading Strategy/Token unlock 72h shock analysis /src/unlock_counter_trading_bot.py`
  - Primary Event Study Dataset: `01.Trading Strategy/Token unlock 72h shock analysis /data/01_binance_token_unlock_events_2023_2025.csv`
  - Backtest Results Dataset: `01.Trading Strategy/Token unlock 72h shock analysis /data/05_unlock_trading_strategies_backtest.csv`
  - Regression Inputs Dataset: `01.Trading Strategy/Token unlock 72h shock analysis /data/10_regression_analysis_inputs.csv`
  - Statistical Validation Test Scripts: `src/test_01_primary_binomial.py`, `src/test_02_bonferroni_adjustment.py`, `src/test_03_btc_regime_anova.py`, `src/test_04_recipient_analysis.py`, `src/test_05_multivariate_regression.py`.
- **License & Rights:** MIT License declared in repository root. Data and code are published under open academic replication terms.
- **Deduplication Audit:** A comprehensive repository-wide audit confirms zero prior records referencing `gameworkerkim/vibe-investing`, `HoKwang Kim`, `72-Hour Shock`, `UNL-10`, `UNL-03`, or token unlock event-driven supply-shock shorting. Adjacent records in `alpha-strategy-research` referencing token locked supply (`crypto-cross-sectional-locked-supply-staking-conviction-2026-09-01.md`, citing Ainsley To 2023/2026) examine cross-sectional long-horizon holding premia from on-chain staking lockup fractions. In contrast, this capture targets acute event-driven shorting within a discrete 96-hour window ($T-24\text{h}$ to $T+72\text{h}$) around scheduled cliff vesting releases on Binance derivatives.

## Economic mechanism

### Source-reported

Token unlock events represent scheduled, publicly known releases of previously restricted cryptocurrency supply encoded into project smart contracts and vesting schedules. Keyrock (2024) previously documented across 16,000+ events that approximately 90% of token unlocks exhibit negative 30-day cumulative abnormal returns. 

Kim (2026) investigates the temporal microstructure and market beta dependence of this supply shock across a hand-curated dataset of 52 major Binance unlock events from 2023 to 2025, identifying three key empirical drivers:
1. **Front-Loaded Liquidity Inelasticity:** Rather than bleeding continuously over 30 days, selling pressure is acutely concentrated within the first 72 hours following the unlock timestamp. In cryptocurrency spot and derivatives markets, short-term buyer depth is relatively inelastic; when large tranches of newly liquid tokens hit order books, absorption capacity is rapidly overwhelmed, resulting in severe downward price dislocations (mean $-16.97\%$).
2. **Beta Independence Across Market Regimes:** The downward price impact is driven by token-specific supply influx rather than broader market direction. Even during strong Bitcoin rallies ($\ge +5\%$), unlocked tokens generated negative absolute returns (mean $-10.5\%$, market-adjusted $-17.3\%$). An ANOVA across five Bitcoin regimes confirms no statistically significant modulation ($p = 0.24$), refuting the hypothesis that unlock drawdowns are merely passive altcoin beta during market selloffs.
3. **Recipient Incentive Asymmetry:** Recipient category dictates liquidation propensity. Early private investors and team members face massive unrealized paper gains and powerful personal diversification/tax incentives to liquidate immediately upon cliff release, producing an average return of $-20.8\%$. In contrast, ecosystem and foundation development grants are retained or deployed into protocol incentives, generating $-18.5\%$ less negative price drift ($p < 10^{-4}$).

### Research interpretation

The strategy captures an **inelastic order-book inventory shock anomaly** around **deterministic calendar supply releases**:
- **Information Underpricing via Structural Search Costs:** Although vesting schedules are public, retail market participants suffer from bounded attention and lack continuous calendar tracking tools. Market makers widen spreads and withdraw passive bid depth ahead of known cliff releases, compounding the impact of incoming recipient market sell orders.
- **Limits to Arbitrage:** Borrowing spot altcoins to short ahead of cliff events carries punitive borrow rates or inventory limits on centralized exchanges. Perpetual futures mitigate borrow constraints but expose short sellers to volatile funding rates and liquidation wicks. These structural frictions prevent capital from fully arbitrating away the 72-hour dislocation.
- **Component Roles in the UNL-10 Hybrid Architecture:**
  - *Regime / Market Filter:* Evaluated across Bitcoin regimes, but empirically robust without market beta conditioning; optional exclusion of severe market crash days ($BTC \le -5\%$) to avoid exchange liquidation engine freezes.
  - *Primary Event Trigger:* Scheduled cliff unlock event timing window: entry at $T-24\text{h}$, exit at $T+72\text{h}$.
  - *Magnitude Filter:* Unlock size threshold $\ge 5\%$ of current circulating supply, ensuring the physical volume shock exceeds daily market absorption capacity.
  - *Structure Filter:* Cliff vesting structure only (linear streaming unlocks distribute volume evenly over months, diffusing the acute price shock).
  - *Incentive Filter:* Recipient category restricted to Team or Investor tranches, pruning non-liquidating Ecosystem or Community allocations.
  - *Risk Management / Execution Overlay:* Hard stop-loss ($+10\%$), take-profit ($-15\%$), and fixed 96-hour maximum holding duration (`time_exit`).

## Signal

### Formation timestamp

The observation schedule is determined by the on-chain smart contract vesting cliff timestamp $T$ (recorded in UTC). The entry signal forms exactly 24 hours prior to unlock:
$$T_{\text{entry}} = T - 24\text{ hours}$$
The trade is entered via a short market order (or taker marketable limit order) on the liquid Binance USDT perpetual contract associated with the unlocking token at $T-24\text{h}$.

### Mathematical Definition and Filter Conditions

For any scheduled unlock event $i$ occurring at UTC timestamp $T_i$ on token $S_i$:

1. **Circulating Supply Unlock Ratio ($U_{size, i}$):**
   $$U_{size, i} = \frac{\Delta \text{Tokens}_i}{\text{CirculatingSupply}_{i, T-1}} \times 100\%$$
   where $\Delta \text{Tokens}_i$ is the number of tokens scheduled for release at $T_i$.

2. **Vesting Structure Indicator ($I_{cliff, i}$):**
   $$I_{cliff, i} = \begin{cases} 1 & \text{if vesting schedule is discrete cliff} \\ 0 & \text{if vesting is linear continuous} \end{cases}$$

3. **Recipient Incentive Indicator ($I_{recipient, i}$):**
   $$I_{recipient, i} = \begin{cases} 1 & \text{if recipient category contains 'Team' or 'Investor'} \\ 0 & \text{otherwise (e.g., pure 'Ecosystem', 'Community', 'Liquidity')} \end{cases}$$

4. **Anniversary Proximity (Exploratory / Priority Score):**
   $$\Delta \text{Days}_{listing, i} = \frac{T_i - \text{ListingDate}_i}{86,400\text{ seconds}}$$
   $$I_{365d, i} = \begin{cases} 1 & \text{if } 335 \le \Delta \text{Days}_{listing, i} \le 395 \text{ and } I_{cliff, i} = 1 \\ 0 & \text{otherwise} \end{cases}$$
   *(Note: As emphasized by the primary source, $I_{365d}$ is an exploratory, post-hoc indicator used only for priority scoring in allocation, not as a solitary confirmatory signal).*

### Entry Rules

An entry short signal (`enter_short`) is triggered at timestamp $t = T_i - 24\text{h}$ if and only if all of the following conditions hold simultaneously:
1. $I_{cliff, i} == 1$ (Vesting structure is a discrete cliff).
2. $U_{size, i} \ge 5.0\%$ (Unlock magnitude equals or exceeds 5.0% of circulating supply; source-reported in `unl10_strategy_backtest.py`).
3. $I_{recipient, i} == 1$ (Recipient category includes Team or Investor).
4. Continuous price history and liquid Binance USDT perpetual market exist for token $S_i$.

If multiple qualifying events occur concurrently, events with $I_{365d, i} == 1$ or higher priority score are allocated first up to the portfolio concurrency limit.

### Exit Rules and Execution Precedence

A short position on token $S_i$ is closed upon the earliest occurrence of any of the following triggers:
1. **Primary Scheduled Time Exit (`TIME_EXIT`):** Current timestamp reaches $T_i + 72\text{ hours}$ (holding duration exactly 96 hours from entry).
2. **Stop-Loss Trigger (`STOP_LOSS`):** Token price increases by $\ge 10.0\%$ above entry price:
   $$\text{PnL}_{\text{short}, t} = \frac{P_{\text{entry}} - P_t}{P_{\text{entry}}} \le -0.10 \implies P_t \ge 1.10 \times P_{\text{entry}}$$
3. **Take-Profit Trigger (`TAKE_PROFIT`):** Token price decreases by $\ge 15.0\%$ below entry price:
   $$\text{PnL}_{\text{short}, t} = \frac{P_{\text{entry}} - P_t}{P_{\text{entry}}} \ge +0.15 \implies P_t \le 0.85 \times P_{\text{entry}}$$
4. **Hard Maximum Duration Stop (`MAX_HOLD_EXIT`):** Position age reaches 96 elapsed hours (`max_hold_hours = 96`).

### Position Sizing and Portfolio Management

- **Single-Trade Allocation:** Maximum 5.0% of account capital per position (`max_position_pct_of_capital = 0.05`).
- **Concurrent Position Cap:** Maximum 5 active short positions simultaneously (`max_concurrent_positions = 5`).
- **Leverage:** Conservative 2x leverage (`leverage = 2`).
- **Weighting:** Equal-weighted across qualifying active events.

## Required data

- **Instruments:** Centralized cryptocurrency perpetual futures contracts (USDT-margined linear perpetuals) listed on Binance.
- **Universe:** All Binance-listed tokens with scheduled on-chain token unlock events.
- **Data Vendor / Sourcing:**
  - Token unlock calendar, cliff dates, unlock sizes, and recipient classifications verified across at least two public aggregators (Tokenomist / TokenUnlocks, DefiLlama Unlocks, CoinMarketCap, DropsTab) or direct smart-contract vesting parameters.
  - Hourly ($1\text{h}$) OHLCV price series from Binance Perpetual Futures (`UM` futures).
  - Benchmark market series: Bitcoin perpetual ($BTC/USDT$), Ethereum perpetual ($ETH/USDT$), and Top-10 market-cap weighted index (recalculated event-by-event to exclude the event token).
- **Timeframe & Session:** Hourly candle intervals, operating 24/7 UTC. Timestamps strictly synchronized to UTC on-chain event schedules.
- **Look-Ahead Protection:** All unlock metadata (date, size, recipient, cliff structure, listing date) are immutable parameters established at token genesis or published weeks in advance. No post-unlock data is used during signal formation at $T-24\text{h}$.

## Execution assumptions

- **Order Types:** Market orders for entry at $T-24\text{h}$ and exit at $T+72\text{h}$ (`next-bar execution` at the start of the hourly bar).
- **Transaction Costs (Source-Reported):** 20.0 bps ($0.20\%$) total round-trip trading fees (10 bps taker fee per side, reflecting standard Binance retail/VIP0 tier).
- **Funding Costs (Source-Reported):** Modeled at 5.0 bps per day ($0.05\%/\text{day}$) for holding perpetual short positions, totaling 15.0 bps ($0.15\%$) across the 3-day holding window.
- **Slippage & Market Impact:** In source backtests, slippage is assumed absorbed within the 20 bps cost buffer for large-cap assets; for smaller tokens ($<\$50\text{M}$ market cap), execution slippage can be substantially higher (`research-proposed: 15-25 bps additional slippage per side`).
- **Borrow & Short Availability:** Short exposure executed via USDT perpetual futures, eliminating spot borrow requirements. Where perpetuals are not listed, spot margin borrow is required, introducing potential borrow-fee spikes and recall risk.

## Evidence

### Source-reported

Across the primary sample of 52 Binance unlock events (January 2023 to December 2025):

#### 1. Primary 72-Hour Return Distribution (Table 1 of paper)
- Sample size: $N = 52$ events.
- Negative outcomes: 46 of 52 events ($88.5\%$).
- Mean 72-hour return ($R_{72}$): $-16.97\%$ (bootstrap 95% CI: $[-20.1\%, -13.8\%]$).
- Median 72-hour return: $-18.57\%$.
- Standard deviation: $10.84\%$.
- Return range: Min $-40.2\%$, Max $+10.4\%$.
- Binomial test ($H_0: p = 0.5$): $p = 2.2 \times 10^{-9}$.
- Wilcoxon signed-rank test: $p < 10^{-7}$.
- Clopper-Pearson 95% exact CI for negative proportion: $[76.6\%, 95.6\%]$.
- Bonferroni multiple testing correction across 17 formal tests ($\alpha = 0.05/17 \approx 0.00294$): **Survives as highly significant**.

#### 2. Bitcoin Regime Independence (Table 2 of paper)
Decomposed across 5 Bitcoin market regimes during the 72-hour event window:
- *Strong Up ($\ge +5.0\%$ BTC return, $N=6$):* Mean Token $R_{72} = -10.5\%$, Mean BTC Return $= +6.8\%$, BTC-Adjusted Return $= -17.3\%$.
- *Mild Up ($0.0\%$ to $+5.0\%$ BTC, $N=11$):* Mean Token $R_{72} = -14.2\%$, Mean BTC $= +2.5\%$, BTC-Adjusted $= -16.7\%$.
- *Flat ($-1.0\%$ to $+1.0\%$ BTC, $N=13$):* Mean Token $R_{72} = -16.8\%$, Mean BTC $= +0.2\%$, BTC-Adjusted $= -17.0\%$.
- *Mild Down ($-5.0\%$ to $0.0\%$ BTC, $N=16$):* Mean Token $R_{72} = -19.2\%$, Mean BTC $= -2.1\%$, BTC-Adjusted $= -17.1\%$.
- *Strong Down ($\le -5.0\%$ BTC, $N=6$):* Mean Token $R_{72} = -28.5\%$, Mean BTC $= -6.8\%$, BTC-Adjusted $= -21.7\%$.
- One-way ANOVA across the 5 regimes: $F\text{-statistic } p = 0.24$ (confirms no statistically significant modulation by BTC regime).
- Alternative benchmarks: Ethereum-adjusted mean return $= -15.9\%$ ($86.5\%$ negative, correlation with BTC-adjusted $= 0.94$); Top-10 index-adjusted mean return $= -16.2\%$ ($86.5\%$ negative, correlation $= 0.97$).

#### 3. Recipient Heterogeneity & Multivariate Regression
- Team + Investor tranches ($N=31$): Mean return $-20.8\%$, $93.5\%$ negative.
- Ecosystem tranches ($N=4$): $+18.5$ percentage points less negative than Team+Investor ($p < 10^{-4}$, survives Bonferroni).
- Multivariate OLS regression ($R_{72} = \beta_0 + \beta_1 U_{size} + \beta_2 R_{BTC} + \beta_3 \text{Days} + \beta_4 \text{Recipient} + \varepsilon$):
  - Unlock size coefficient: $\beta_1 = -0.0089$ ($p < 0.01$).
  - Market return coefficient: $\beta_2 = 0.52$ (substantially below unity).
  - Days since listing: $\beta_3$ marginally significant ($p = 0.062$).

#### 4. Strategy Backtest Matrix (Table E.1 and `05_unlock_trading_strategies_backtest.csv`)
- **UNL-10 Hybrid Strategy (All 3 Filters: Cliff + $\ge 5\%$ + Team/Investor):**
  - Qualifying events: $N = 11$ (out of 52).
  - Win rate: $100.0\%$.
  - Mean return: $+32.5\%$.
  - Maximum drawdown: $-5.5\%$.
  - Annualized Sharpe ratio proxy: $6.25$.
- **UNL-03 Acute 72h Short (Baseline core):** $N = 52$, Win rate $88.5\%$, Mean return $+16.97\%$, Max DD $-12.5\%$, Sharpe $3.15$.
- **UNL-04 Team Unlock Only Short:** $N = 39$, Win rate $92.3\%$, Mean return $+21.16\%$, Max DD $-8.5\%$, Sharpe $3.45$.
- **UNL-05 Huge Cliff Short ($\ge 5\%$):** $N = 18$, Win rate $94.4\%$, Mean return $+28.5\%$, Max DD $-6.2\%$, Sharpe $4.12$.
- **UNL-06 1-Year Anniversary Cliff Short:** $N = 14$, Win rate $100.0\%$, Mean return $+27.5\%$, Max DD $-3.2\%$, Sharpe $5.85$.
- **UNL-01 Naive Long Control:** $N = 52$, Win rate $11.5\%$, Mean return $-16.97\%$, Max DD $-41.67\%$, Sharpe $-2.45$.

### Independently reproduced

Not independently reproduced. The empirical metrics above are captured directly from HoKwang Kim's published research paper, Python replication scripts, and underlying CSV datasets in `gameworkerkim/vibe-investing` (commit `ea0b6f20c6ea59c494ce5e981006472693256f00`).

### Negative evidence

The primary source documents several critical limitations and contrary conditions:
1. **Severe Small-Sample Limitations:** The UNL-10 hybrid strategy relies on only $N = 11$ events over 36 months, while the 1-year anniversary cliff strategy has $N = 14$. A $100\%$ in-sample win rate on 11 events represents an upper-bound statistical illustration rather than an all-weather production guarantee.
2. **Post-Hoc Data-Mining Invalidation on 365-Day Anniversary:** The 1-year anniversary cliff observation ($N=14$, 100% negative) was identified through post-hoc exploratory data analysis. The nominal $p$-value ($6.1 \times 10^{-5}$) is formally invalid under statistical testing standards because the effective search space during exploratory discovery was unconstrained.
3. **Short Squeeze Tail Risk:** While 46 of 52 events declined, 6 events ($11.5\%$) experienced sharp price increases of up to $+10.4\%$ within the 72-hour window. Without a disciplined stop-loss, unhedged short positions face unbounded upside loss during speculative short squeezes.
4. **Funding Rate Volatility During Crowded Events:** When market participants anticipate a major unlock, perpetual funding rates frequently plunge to extreme negative values (e.g., $-0.10\%$ to $-0.50\%$ per 8 hours), significantly increasing the cost of holding short positions beyond the 5 bps/day baseline assumption.
5. **Ecosystem & Community Mismatch:** Shorting unlock events where tokens are distributed to ecosystem development funds or community DAOs yielded weak or negative performance ($p < 10^{-4}$ vs Team unlocks), confirming that non-liquidating tranches fail to produce supply shocks.

## Falsification plan

To falsify the 72-hour token unlock supply shock hypothesis:
1. **Prospective Out-of-Sample Event Test:** Collect the next 30 consecutive Binance-listed token unlock events meeting the UNL-10 hybrid criteria ($I_{cliff}=1$, $U_{size} \ge 5\%$, Team/Investor recipient) occurring after 2026-09-12.
   - *Falsification Rule:* If the proportion of negative 72-hour returns drops below $70.0\%$ ($p > 0.05$ against binomial null of $0.50$; labeled `research-defined falsification threshold`), or if the mean net return after actual realized taker fees and funding drops below $+5.0\%$ (labeled `research-defined falsification threshold`), reject the predictability of the supply shock.
2. **Pre-Registered 365-Day Anniversary Replication:** Track a clean prospective sample of at least 20 first-year anniversary cliff events across Binance, OKX, and Bybit. If the win rate falls below $80.0\%$ (labeled `research-defined falsification threshold`), confirm that the historical 14/14 result was a post-hoc data-mining artifact.
3. **Funding-Rate Drag Stress Test:** Model realistic dynamic perpetual funding rates using historical funding logs during event windows. If subtracting actual 8-hour funding rates erodes more than $50.0\%$ of cumulative strategy PnL across qualifying events (labeled `research-defined falsification threshold`), the edge is falsified as an illusion caused by unmodeled negative-carry friction.
4. **Randomized Event-Date Placebo Test:** Shift the unlock timestamp $T_i$ for each token randomly by $\pm 30$ to $\pm 90$ days while preserving token-specific volatility. If the mean short return on actual unlock dates is not statistically distinguishable from the randomized placebo dates at the $95\%$ confidence level ($p \ge 0.05$; labeled `research-defined falsification threshold`), reject the causality of the unlock schedule.

## Crypto portability

**Portability Classification: Direct.**

The strategy was conceptualized, measured, and backtested natively on cryptocurrency spot and perpetual futures markets on Binance:
- **Native Alignment:** Token vesting cliffs and scheduled smart-contract supply unlocks are unique structural features of digital asset tokenomics.
- **Perpetual Derivatives Market Mechanics:** The short trade is executed via centralized linear USDT perpetual futures contracts, directly leveraging 24/7 continuous trading sessions without traditional weekend market closures.
- **Cross-Venue Portability:** The underlying mechanism (order book liquidity exhaustion from recipient liquidation) is exchange-agnostic and directly portable to other major cryptocurrency derivatives venues with deep perpetual liquidity (e.g., OKX, Bybit, Hyperliquid).
- **Portability Caveats:**
  - *Spot Borrow Constraints:* On exchanges lacking perpetual futures for long-tail altcoins, executing short positions requires spot margin borrowing, which often faces zero borrow inventory or exorbitant borrow APRs ($>50\%$) immediately prior to major unlocks.
  - *DEX Liquidity Differences:* On decentralized exchanges (Uniswap, PancakeSwap), liquidity pools experience automated constant-product price impact without order-book depth, altering the slippage profile.

## Limitations

- **Small Sample Size:** The primary dataset contains only 52 events, and the filtered UNL-10 hybrid subset contains only 11 events, limiting statistical power for high-dimensional factor analysis.
- **Selection Bias & Survivor Bias:** Only tokens listed on Binance were included. Binance listings represent higher-liquidity, survivor-biased assets; long-tail tokens on minor exchanges may experience total illiquidity or immediate delisting upon massive cliff releases.
- **Post-Hoc Anomaly Contamination:** The 365-day anniversary cliff finding was discovered through data exploration and remains exploratory until prospectively validated.
- **Unmodeled Negative Carry:** Extreme negative funding rates during widely anticipated unlock events can impose severe daily drag on short perpetual positions, which was modeled with a flat 5 bps/day proxy rather than tick-level funding logs.
- **Regulatory and Exchange Delisting Risk:** Several tokens undergoing major unlocks face regulatory scrutiny or potential spot trading halts in specific jurisdictions (e.g., Korea VAUPA, EU MiCA), potentially impairing exit liquidity.

## Implementation status

`not-implemented`. No implementation in PyBroker, NautilusTrader, paper trading, testnet, or live trading has been created or modified. This record is a research-only capture of an open-source empirical working paper and backtest codebase.

## Adoption boundary

`research-only` / `not-approved`.
Cataloged strictly as upstream research material for ChatGPT Research Intake Review and Wiki Brain handoff. Ingestion of this record does not constitute:
- Evidence of persistent live profitability;
- Approval for portfolio inclusion or capital allocation;
- Authorization for paper trading, testnet deployment, or live trade execution.

Any practical implementation requires independent historical data verification, dynamic borrow/funding rate integration, and pre-registered out-of-sample forward tracking.

## Related Wiki records

- `[[crypto-cross-sectional-locked-supply-staking-conviction-2026-09-01]]` — Cross-sectional locked supply and staking conviction premium from Ainsley To (2023/2026).
- `[[crypto-perpetual-liquidation-cascade-overshoot-reversal-2026-08-31]]` — Order book liquidity shock reversals in cryptocurrency perpetual contracts.
- `[[crypto-open-interest-crash-rebound-flow-gap-2026-09-03]]` — Open interest liquidations and order flow gaps.
- `[[news-event-tag-drift-rumor-resolution-placebo-adjusted-momentum-2026-09-02]]` — Event-study methodologies and post-event drift in digital asset markets.
- `[[crypto-funding-carry-fade-turnover-cost-dissipation-falsification-2026-09-12]]` — Perpetual funding rate cost drag and turnover dissipation.

## Sources

1. **Kim, HoKwang (2026).** *The 72-Hour Shock? Preliminary Evidence from 52 Token Unlock Events on Binance: A Cross-Sectional Analysis of Unlock Events and Their Asymmetric Impact on Cryptocurrency Prices*. Working Paper Version 3.1, April 2026 / updated September 2026. Published in GitHub repository `gameworkerkim/vibe-investing`, commit `ea0b6f20c6ea59c494ce5e981006472693256f00`. Path: `01.Trading Strategy/Token unlock 72h shock analysis /Token unlock 72h shock ssrn v3 1 en.MD`.
2. **Kim, HoKwang (2026).** *UNL-10 Hybrid Strategy Backtest Implementation*. Script `01.Trading Strategy/Token unlock 72h shock analysis /src/unl10_strategy_backtest.py`, commit `ea0b6f20c6ea59c494ce5e981006472693256f00`. Details UNL-10 filter logic, cost modeling (20 bps trading, 15 bps funding), and in-sample metrics.
3. **Kim, HoKwang (2026).** *Token Unlock Counter-Trading Bot*. Script `01.Trading Strategy/Token unlock 72h shock analysis /src/unlock_counter_trading_bot.py`, commit `ea0b6f20c6ea59c494ce5e981006472693256f00`. Provides operational bot configuration, risk limits (10% SL, 15% TP, 96h max hold), and Binance futures client structure.
4. **Kim, HoKwang (2026).** *Token Unlock Strategies Backtest Results Matrix*. Dataset `01.Trading Strategy/Token unlock 72h shock analysis /data/05_unlock_trading_strategies_backtest.csv`, commit `ea0b6f20c6ea59c494ce5e981006472693256f00`. Reports comparative performance metrics across all 10 tested strategy specifications (UNL-01 through UNL-10).
5. **Kim, HoKwang (2026).** *Binance Token Unlock Events 2023-2025 Dataset*. Dataset `01.Trading Strategy/Token unlock 72h shock analysis /data/01_binance_token_unlock_events_2023_2025.csv`, commit `ea0b6f20c6ea59c494ce5e981006472693256f00`. Full metadata for all 52 analyzed unlock events.
6. **Keyrock (2024, December).** *From locked to liquidity: What 16,000+ token unlocks teach us*. Keyrock Research Report. URL: https://keyrock.com/research. Cited for the benchmark 30-day post-unlock negative return rate (90%).
7. **Brav, A., & Gompers, P. A. (2003).** *The role of lockups in initial public offerings*. Review of Financial Studies, 16(1), 1–29. Cited for the foundational IPO lockup expiration supply shock theoretical framework.
