---
schema: strategy-research-record-v1
title: "APFF Multi-Asset Perpetual Adaptive Factor Factory (FMZ 548843)"
created: 2026-09-16
updated: 2026-09-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - multi-asset
  - factor-factory
  - adaptive-weighting
  - cross-sectional-momentum
  - funding-rate
  - open-interest
  - basis-premium
  - fmz
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - "FMZ strategy page and full JavaScript source: 'APFF多品种永续合约自适应因子工厂策略 v0.1.0' (Adaptive Perpetual Factor Factory v0.1.0), created 2026-09-04 17:30:03, last modified 2026-09-08 11:12:25. Strategy ID: 548843. https://www.fmz.com/strategy/548843"
  - "FMZ companion digest topic (English): 'Put Factors Under Continuous Evaluation: Implementing the APFF Multi-Asset Perpetual Strategy on FMZ', created 2026-09-08 10:36:45, updated 2026-09-08 10:44:28. Topic ID: 11036. https://www.fmz.com/digest-topic/11036"
  - "FMZ companion digest topic (Chinese): '让因子接受持续考核：在 FMZ 实现 APFF 多品种永续合约策略', created 2026-09-08 10:36:45, updated 2026-09-08 10:44:28. Topic ID: 11035. https://www.fmz.com/digest-topic/11035"
  - "Author FMZ user profile: '发明者量化-小小梦' (User ID: 105ed6e51bcc97792c610fdbb7e2a1d6). https://www.fmz.com/user/105ed6e51bcc97792c610fdbb7e2a1d6"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# APFF Multi-Asset Perpetual Adaptive Factor Factory (FMZ 548843)

## Provenance

- **Strategy Title [source-reported]:** APFF多品种永续合约自适应因子工厂策略 v0.1.0 / Adaptive Perpetual Factor Factory v0.1.0
- **Strategy ID [source-reported]:** FMZ strategy `548843` (https://www.fmz.com/strategy/548843)
- **Author [source-reported]:** FMZ official/community account `发明者量化-小小梦` (User ID: `105ed6e51bcc97792c610fdbb7e2a1d6`, https://www.fmz.com/user/105ed6e51bcc97792c610fdbb7e2a1d6)
- **Release & As-of Dates [source-reported]:**
  - Strategy created: 2026-09-04 17:30:03; last modified: 2026-09-08 11:12:25.
  - Companion technical articles published: 2026-09-08 10:36:45; updated: 2026-09-08 10:44:28 (Digest Topic `11036` English; Topic `11035` Chinese).
  - Version metadata: System version `v0.1.0`, build `20260908-01` (article references development build `20260905-05`), research definition version `2`, schema version `1`.
- **Primary Source Availability [source-reported]:** Complete public 3,190-line JavaScript implementation and UI parameter schema accessible directly on the FMZ strategy page.
- **Deduplication Audit:** Repository-wide audit of all 626 records in `alpha-strategy-research` on 2026-09-16 confirmed zero prior records citing FMZ strategy `548843`, digest topic `11035`, digest topic `11036`, or the APFF framework. Adjacent multi-asset and factor-weighting records in this repository (`crypto-cross-sectional-meme-momentum-funding-dynamic-rotation-2026-09-14.md` on high-volatility meme perps, `adaptive-alpha-weighting-ppo-llm-generated-alphas-2026-09-05.md` via PPO on equity alphas, `kronos-kline-foundation-multi-sample-quantile-trend-overlay-2026-09-15.md` on single-pair foundation-model overlays) address different universes, mechanisms, and architectures. APFF uniquely introduces a closed-loop factor factory with observation/trial promotion gates, unallocated budget preservation, and asynchronous GTX post-only reconciliation barriers.

## Economic mechanism

### Source-reported

The author presents APFF as an architecture to resolve factor allocation dilemmas (e.g., conflicting signals, factor decay, and admission of untrusted candidates) in cryptocurrency perpetual futures:

1. **Cross-Sectional Relative-Strength Premia:** Rather than predicting directional market beta, the strategy sorts a dynamic cross-section of liquid perpetual contracts. A market-neutral or beta-hedged long-short portfolio profits from the return dispersion between relatively strong and relatively weak assets.
2. **Multi-Family Factor Foundations:**
   - *Momentum excluding immediate shocks (`MOM_EX`):* Postulates that 7-day medium-term price trends persist, but the most recent 4-hour bar contains microstructure noise/reversal pressure; skipping the recent bar enhances signal quality.
   - *Short-term Reversal (`REV`):* Assets exhibiting extreme 4-hour drops normalized by 24-hour realized volatility tend to experience short-term liquidity-replenishment rebounds.
   - *Funding Rate Crowding (`FUND_Z`):* Perpetual funding rates normalized to standard 8-hour intervals reflect directional leverage crowding; historically extreme positive funding predicts underperformance due to long carry drag and vulnerability to long squeezes.
   - *Premium Mean Reversion (`PREMIUM_Z`):* The basis spread between perpetual mark price and spot index tends to mean-revert around funding settlement boundaries.
   - *Open Interest Confirmation (`OI_CONFIRM`):* Price momentum accompanied by positive 24-hour notional open interest growth signals aggressive institutional participation rather than short-covering.
3. **Endogenous Factor Lifecycle & Evidence-Based Reweighting:** Factors transition through `OBSERVING` (pure shadow tracking), `TRIAL` (5% budget cap), `ACTIVE` (up to 25% budget), and `DORMANT` (weight zeroed upon performance failure). Weights adapt based on rolling shrunk Rank IC, cost-adjusted net return, subperiod stability, and block bootstrap significance.
4. **Capital Budget Preservation:** When active factors are missing data or unproven, the unused budget remains idle rather than being re-leveraged across remaining factors, reducing overall gross exposure.
5. **Limited Beta Hedging:** Net portfolio beta relative to Bitcoin (`BTC_USDT.swap`) is dynamically calculated and offset using a capped BTC perpetual position to isolate idiosyncratic alpha from macro crypto market beta.

### Research interpretation

APFF is an institutional-style quantitative equity market-neutral (QMN) framework adapted to crypto perpetual derivatives. Its core hypothesis is that cross-sectional alpha in crypto is fragmented across distinct economic drivers (behavioral trend, liquidity shocks, leverage costs, and speculative interest) and that no single factor maintains constant efficacy across market regimes.

By formalizing factor promotion and demotion via pre-declared statistical and cost hurdles (including a doubled-cost test and Benjamini-Hochberg false discovery control), the strategy aims to mitigate factor decay and multiple-testing bias in live production. The structural inclusion of cash-idle budget preservation prevents the common quantitative trap of forced full gross exposure during low-conviction or data-sparse environments.

## Signal

### Cadence & Multi-Scale Timers [source-reported]

- **Market Data & Microstructure:** Continuous WebSocket stream for Best Bid/Ask, Mark Price, and order updates; health timeout at 30,000 ms (`FIXED.wsNoDataMs`).
- **Factor Base Candles:** Completed 4-hour OHLCV candles (`periodH4() = 4 * 3600`), refreshed every 30 minutes (`FIXED.recordsRefreshMs = 30 * 60 * 1000`). Forming bars are excluded.
- **Portfolio Decisions & Forward Samples:** Executed every 8 hours (`FIXED.decisionMs = 8 * 3600 * 1000`).
- **Universe Rebalancing:** Executed daily (`FIXED.universeRefreshMs = 24 * 3600 * 1000`).
- **Factor Evaluation & Reweighting:** Executed every 7 days (`FIXED.selectorMs = 7 * 24 * 3600 * 1000`).
- **Candidate Factory Generation:** Executed at startup and every 30 days (`FIXED.factoryMs = 30 * 24 * 3600 * 1000`).

### Universe Selection [source-reported]

- **Eligible Contracts:** Binance USDⓈ-M USDT linear perpetuals (`USDT.swap`).
- **Target Size:** Default 30 symbols (`UniverseSize = 30`, configurable 15–60).
- **Inclusion Filters:** Contract status must be `TRADING`, valid two-sided quotes, spread within limits, and minimum 90-day listing history (where listing metadata is provided).
- **Ranking Metric:** Sorted descending by 24-hour quote volume (`Turnover`).
- **Buffer Retention Rule:** Existing universe members are retained if their volume rank remains within the top 40 (`FIXED.reserveRank = 40`), preventing unnecessary universe turnover.
- **Benchmark / Hedge Instrument:** `BTC_USDT.swap` is maintained for beta calculations and hedging but strictly excluded from the alpha cross-section.
- **Minimum Cross-Section:** Portfolio formation requires at least 15 valid non-BTC symbols (`FIXED.minUniverse = 15`).

### Factor Definitions [source-reported]

Let $c_t$ be the latest closed 4-hour bar close, $\text{RET}(k) = \ln(c_t / c_{t-k})$ be log return over $k$ bars, and $\text{RV}(k) = \sqrt{\frac{1}{k-1}\sum_{j=0}^{k-1} (\Delta \ln c_{t-j} - \overline{\Delta \ln c})^2}$ be 4-hour realized sample return standard deviation over $k$ bars:

1. **`SEED_MOM_7D_EX4H` (Momentum excluding recent 4H bar):**
   $$\text{Raw} = (+1) \times \frac{\text{RET}(42) - \text{RET}(1)}{\text{RV}(42)}$$
   (42 4-hour bars correspond to 7 days; skips the most recent 1 bar).
2. **`SEED_REV_4H` (Short-term 4H Reversal):**
   $$\text{Raw} = (+1) \times (-1) \times \frac{\text{RET}(1)}{\text{RV}(6)}$$
   (1 4-hour bar return normalized by 24-hour / 6-bar realized volatility).
3. **`SEED_FUNDING_30D` (Funding Crowding):**
   $$\text{Raw} = (-1) \times Z_{\text{TS}}\left( f_t \times \frac{8\text{h}}{\text{Interval}_t}, 90 \text{ points} \right)$$
   (Normalizes funding rates to an 8-hour scale; computes rolling time-series z-score over up to 90 settlement points / 30 days).
4. **`SEED_PREMIUM_7D` (Basis Premium Mean Reversion):**
   $$\text{Raw} = (-1) \times Z_{\text{TS}}\left( \frac{\text{Mark}_t}{\text{Index}_t} - 1, 168 \text{ points} \right)$$
   (Hourly premium index series z-scored over 168 hours / 7 days).
5. **`SEED_OI_CONFIRM_24H` (Open Interest Confirmation):**
   $$\text{Raw} = (+1) \times \text{sign}(\text{RET}(6)) \times Z_{\text{TS}}\left( \ln(\text{OI}_t) - \ln(\text{OI}_{t-6}), 180 \text{ points} \right)$$
   (Directional return over 24 hours multiplied by the time-series z-score of 24-hour log change in notional open interest).

### Candidate Blueprint Templates [source-reported]

The built-in factory periodically generates batches of up to 12 deduplicated candidate factors (`FIXED.factoryBatchSize = 12`) from parametric templates:
- `MOM` and `REV`: Lookback horizons $k \in \{1, 6, 18, 42\}$ bars with $\text{rvBars} = \max(6, k)$.
- `FUND_Z`: Points $\in \{21, 90, 180\}$.
- `PREMIUM_Z`: Points $\in \{168, 720, 1440\}$.
- `OI_CONFIRM`: Bars $= 6$, points $\in \{42, 180\}$.
- `PRICE_VOLUME`: $\text{Raw} = \text{RET}(k) \times Z_{\text{TS}}(\text{Volume}, \max(21, k))$ for $k \in \{6, 18, 42\}$.
- `LOW_VOL`: $\text{Raw} = (-1) \times \text{RV}(k)$ for $k \in \{6, 18, 42\}$.

### Cross-Sectional Normalization & Composite Score [source-reported]

1. **Winsorization:** For each factor across valid universe symbols, raw values are clipped to the 5th and 95th percentiles: $v_i \leftarrow \text{clamp}(v_i, Q_{0.05}, Q_{0.95})$.
2. **Rank Mapping:** Ranks $R_i \in [0, N-1]$ (with average rank for ties) are mapped linearly to $[-1, +1]$:
   $$\text{Score}_{ij} = \frac{2 R_{ij}}{N - 1} - 1$$
3. **Factor & Asset Coverage Checks:** A factor is valid only if valid values cover $\ge 80\%$ of symbols (`FIXED.minFactorCoverage = 0.80`). A symbol is valid only if covered by $\ge 80\%$ of the active factor weights.
4. **Weighted Composite Score:**
   $$\text{Alpha}_i = \frac{\sum_{j \in \text{valid}} w_j \cdot \text{Score}_{ij}}{\sum_{j \in \text{valid}} w_j}$$

### Portfolio Target Construction [source-reported]

1. **Gross Notional Budget:**
   $$\text{Gross} = \text{Equity} \times \text{GrossExposurePct} \times \text{Confidence} \times \min\left(1, \sum w_j\right) \times \text{DrawdownScale}$$
   - Default `GrossExposurePct` = 60%.
   - `DrawdownScale`:
     - $\text{Drawdown} < 4\% \implies 1.00$
     - $4\% \le \text{Drawdown} < 7\% \implies 0.70$
     - $7\% \le \text{Drawdown} < 10\% \implies 0.40$
     - $\text{Drawdown} \ge 10\% \implies 0.00$ (target flattened, new risk paused).
2. **Factor Budget Caps:**
   - Single `ACTIVE` factor: max 25% (`FIXED.activeFactorCap = 0.25`).
   - Single factor family: max 35% (`FIXED.familyCap = 0.35`).
   - Single `TRIAL` factor: max 5% (`FIXED.trialFactorCap = 0.05`).
   - Total `TRIAL` factors combined: max 10% (`FIXED.trialTotalCap = 0.10`).
   - Unallocated budget is preserved as cash idle (denominator uses $\max(1, \text{total})$).
3. **Asset Selection & Buffering:**
   - Long candidates: top 20% of cross-section by composite score (capped at 6 symbols).
   - Short candidates: bottom 20% of cross-section by composite score (capped at 6 symbols).
   - Retention buffer: existing long/short positions are retained if they remain within the top/bottom 35% (`keepBoundary = floor(N * 0.35)`).
4. **Inverse Volatility Weighting:**
   $$\text{RawWeight}_i \propto \frac{\max(0.05, |\text{Alpha}_i|)}{\text{RV}_{7\text{D}, i}}$$
   Allocated equally between long and short sides ($\text{Gross}/2$ each), with per-symbol target notional capped at 8% of equity (`MaxSymbolPct = 8%`, max 15%).
5. **BTC Beta Neutralization:**
   - Beta $\beta_i$ of each symbol against `BTC_USDT.swap` is calculated via rolling aligned 4-hour returns over 42 bars.
   - Net portfolio beta exposure: $\text{BetaExp} = \sum \text{Target}_i \times \beta_i$.
   - If $|\text{BetaExp}| > 2\% \times \text{Equity}$, hedge with BTC perp: $\text{Hedge}_{\text{BTC}} = \text{clamp}(-\text{BetaExp}, -10\% \times \text{Equity}, +10\% \times \text{Equity})$, subject to the per-symbol cap.
6. **Turnover Soft Cap:**
   - Rebalance turnover $\sum |\text{Target}_i - \text{CurrentNotional}_i|$ is soft-capped at 20% of NAV (`FIXED.maxTurnoverNav = 0.20`).
   - Adjustments exceeding 20% are scaled proportionally toward target: $\text{Target}'_i = \text{Current}_i + (\text{Target}_i - \text{Current}_i) \times \frac{0.20 \times \text{Equity}}{\text{Turnover}}$, unless risk deleveraging applies.

### Factor Lifecycle & Statistical Promotion Gates [source-reported]

- **States:** `OBSERVING` (shadow tracking), `TRIAL` (5% budget), `ACTIVE` (full budget), `DORMANT` (0% weight), `REJECTED` (redundant/failed).
- **Maturity & Forward Samples:** Decisions mature 8 hours later. Mid-price collection is bounded by a 60-second window (`FIXED.labelPriceGraceMs = 60000`) and funding settlements by a 5-minute window (`FIXED.labelFundingGraceMs = 300000`). Missing data skips the entire sample.
- **Factor Long-Short Return Accounting:**
   $$r_{\text{long}, i} = \frac{P_{1, i}}{P_{0, i}} - 1 - \sum_k \frac{f_{k, i} \cdot M_{k, i}}{P_{0, i}}$$
   $$\text{Net Return} = \sum w_i r_i - \text{Turnover} \times \text{EstimatedOneWayCostBps}$$
- **Promotion Hurdles (`factorPasses`):**
  1. Sample count: $n \ge 180$ samples (~60 days) for `OBSERVING`; $n \ge 90$ samples (~30 days) for `TRIAL`.
  2. Shrunk Rank IC: $\text{ShrunkIC} = \frac{n}{n + 60} \times \text{MeanIC} > 0$.
  3. Doubled-Cost Robustness: $\text{MeanNet} - \text{Turnover} \times \text{OneWayCost} > 0$ (must remain positive after subtracting the cost charge a second time).
  4. Subperiod Stability: $\ge 75\%$ of 4 equal subperiods must show positive mean net return.
  5. Bootstrap Significance: Block bootstrap positive net return frequency $p_{\text{positive}} \ge 90\%$.
  6. Historical Coverage: Mean data coverage across evaluation samples $\ge 98\%$.
  7. Benjamini-Hochberg False Discovery Control: P-values evaluated under dependence-adjusted FDR.
  8. Redundancy Rejection: Correlation with existing active factor return series $|\rho| > 0.85$ results in immediate `REJECTED` status (`FIXED.correlationReject = 0.85`).
  9. Slot Caps: Max 2 factors in `TRIAL`, max 6 in `ACTIVE`, max 1 promotion per family per batch, max 2 promotions per batch.
- **Demotion / Dormancy:** Active factors with $n \ge 180$ enter `DORMANT` (weight zeroed) if both mean IC and mean net return over the most recent 90 samples are negative.
- **Weekly Weight Smoothing:**
  $$w_{\text{new}} = 0.70 \times w_{\text{old}} + 0.30 \times w_{\text{target}}$$
  Maximum weekly shift per factor is capped at 5 percentage points (`FIXED.maxWeeklyWeightMove = 0.05`).

## Required data

- **Instrument / Market Type [source-reported]:** Binance USDⓈ-M USDT linear perpetual contracts (`USDT.swap`).
- **Venue [source-reported]:** Binance Futures via FMZ exchange API and live WebSockets.
- **Timeframe [source-reported]:** 4-hour completed OHLCV candles (`records`), live 1-hour funding rates (`GetFundings` / `/fapi/v1/fundingRate`), 1-hour premium index (`Premium Index Klines` or `Mark/Index - 1`), 4-hour notional Open Interest snapshots (`openInterest`).
- **Point-in-Time Availability [source-reported]:** Current forming 4-hour candle is strictly excluded (`records[:-1]`). Forward return labels are locked strictly 8 hours post-decision.
- **Missing Data Handling [source-reported]:**
  - If a contract has fewer than 42 completed 4H bars, factor returns `NaN` and is excluded from cross-section.
  - If terminal price is missing within 60s or funding is incomplete within 5m, the entire forward sample is invalidated. Imputation is strictly forbidden.
- **Fee & Cost Modeling [source-reported]:**
  - Default one-way transaction cost: 4 bps (`EstimatedOneWayCostBps = 4`).
  - PAPER mode: fills at live BBO (Ask for buy, Bid for sell), with 4 bps charged as fee haircut.
  - LIVE mode: exchange maker/taker fee schedules apply.

## Execution assumptions

### Source-reported

- **Order Type:** GTX (Post-Only) passive limit orders (`orderOptions.postOnly = true`). Market orders are restricted to risk-reducing emergency closes (`REDUCE_TO_ZERO`).
- **Order Timing & Horizon:** 15-minute execution window (`FIXED.executionWindowMs = 15 * 60 * 1000`). Orders rest for a minimum of 120 seconds (`FIXED.orderMinRestMs`) before repricing. Orders older than 10 minutes are cancelled.
- **Concurrency & Rate Limits:** Maximum 1 active order intent per symbol, maximum 4 concurrent active orders globally (`FIXED.maxActiveOrders = 4`), and maximum 8 asynchronous exchange tasks (`FIXED.maxTasks = 8`).
- **Sign-Flip Execution:** If a symbol flips from long to short (or vice versa), the existing position is completely closed and reconciled before the reverse entry order is dispatched.
- **Position Reconciliation Barrier State Machine:**
  - Client order IDs are deterministically generated and persisted before transmission: `APFF1` prefix + base36 timestamp + sequence.
  - Position barriers store $\text{expected} = \text{initial} + \text{cumulativeFilled}$.
  - Symbol remains locked in `WAIT_POSITION` until an exchange position query initiated *after* terminal order state confirms position within half of contract step size (`tolerance = max(1e-12, step / 2)`).
  - Resilient to `-2011` "Unknown order" cancel/fill race conditions.
- **Margin & Leverage:** Gross exposure capped at 60% of equity (default) with 8% single-symbol limit; leverage is strictly $< 1.0\times$ (sub-1x deleveraged).

### Research interpretation

GTX passive execution minimizes taker fees (benefiting from maker rebates or 0–2 bps maker fees on Binance VIP tiers). However, on volatile alts, 15-minute resting limits risk non-execution (adverse selection where only losing fills occur while winners run away). The 4 bps one-way cost estimate assumes a blend of maker fees and minimal adverse fill slippage.

## Evidence

### Source-reported

1. **System & Workflow Validation [source-reported]:**
   - 23 order-regression unit tests verified.
   - 34 dedicated audit tests verified, including 36 accelerated simulated decision cycles (clock-manipulated) and 500 randomized portfolio weight constraint tests.
   - Binance testnet/simulation retest confirmed graceful recovery from `-2011` cancel-fill race conditions within 2.17 seconds.
2. **Empirical Track Record & Performance Claims [source-reported]:**
   - **Provenance Gap:** The author explicitly discloses that the strategy page and technical article contain **zero published long-term historical backtest tables, annualized returns, Sharpe ratios, or live win rates**.
   - The authors state: *"The 36 cycles use synthetic data and a controlled clock to validate sampling, maturity, accounting, and recovery workflows; they are not a 12-day historical return backtest... Runtime retesting covers simulated matching, restart recovery, and reconciliation, but is not sufficient to report conclusions about annualized return, Sharpe ratio, or long-term win rate."*
   - Page engagement as of capture: 56 hits, 6 forks.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- **Adverse Selection in Passive Orders:** Sole reliance on GTX limit orders in cross-sectional momentum can lead to asymmetric execution: momentum leaders gap up without filling, while momentum laggards fill immediately and continue falling.
- **Funding Drag in Sustained Regimes:** Carrying short positions against high-funding alts during strong bull runs can accumulate severe negative funding cash flows before price mean-reversion occurs.
- **Tracking Error in BTC Beta Hedge:** Cross-sectional altcoin betas to BTC are non-stationary and rise sharply toward 1.0 during market crashes; a static 42-bar beta estimate can fail to provide adequate tail hedging during sudden deleveraging events.

## Falsification plan

To empirically evaluate or falsify the APFF framework, the following operational tests are specified:

1. **Long-Horizon Walk-Forward Multi-Asset Out-of-Sample Test:**
   - *Data & Universe:* Binance USDⓈ-M top 30 perpetual contracts by volume from 2023-01-01 to 2026-09-01.
   - *Cost Model:* 2 bps maker fee + 3 bps adverse selection slippage on passive fills; 8-hour funding cash flows modeled tick-for-tick.
   - *Research-defined falsification threshold:* If the net Sharpe ratio is $\le 0.0$ or annualized net return $\le 0.0\%$ over $\ge 540$ consecutive 8-hour decision periods (~180 days), the strategy's multi-factor cross-sectional premise is falsified.
   - *Action:* Reject strategy for live consideration; retain individual factors for standalone decomposition.
2. **Adaptive Factor Reweighting vs. Static Equal-Weight Seed Factor Ablation:**
   - *Benchmark:* Run the exact same universe, sizing, risk, and execution overlay using a fixed, static $20\%$ equal allocation to the 5 seed factors without adaptive reweighting or candidate factory churn.
   - *Research-defined falsification threshold:* If the adaptive factor factory does not achieve a statistically significant net Sharpe improvement ($\Delta \text{Sharpe} \ge 0.20$, paired bootstrap $p < 0.05$) over the static benchmark over $\ge 360$ samples, the factory and adaptive selector layer is non-load-bearing and adds gratuitous complexity.
   - *Action:* Strip factory machinery; simplify to static multi-factor ensemble.
3. **BTC Beta Hedge Efficiency Ablation:**
   - *Test:* Compare portfolio performance with BTC beta hedging enabled versus an unhedged long-short portfolio.
   - *Research-defined falsification threshold:* If the beta-hedged portfolio exhibits lower net risk-adjusted return ($\text{Sharpe}_{\text{hedged}} < \text{Sharpe}_{\text{unhedged}} - 0.15$) or higher maximum drawdown due to hedging turnover costs and beta-mismatch tracking error, reject the limited BTC beta hedge.
   - *Action:* Disable BTC beta hedge; enforce strict dollar-neutral gross balance instead.
4. **Cross-Sectional Placebo Permutation Test:**
   - *Test:* At each 8-hour rebalance, randomly shuffle the composite alpha scores across the universe while preserving identical volatility scaling, turnover constraints, and position barriers.
   - *Research-defined falsification threshold:* If the true strategy does not outperform the 95th percentile of 500 shuffled placebo paths in net profit after transaction costs, the cross-sectional ranking is spurious.
   - *Action:* Reject all factor specifications.
5. **Drawdown Circuit-Breaker Stress Test:**
   - *Test:* Historical replay across high-volatility liquidation cascade episodes (e.g., March 2020, May 2021, August 2024).
   - *Research-defined falsification threshold:* If portfolio equity drawdown exceeds $15\%$ despite the $10\%$ zero-budget halt rule (due to execution slippage, basis blowout, or liquidation gap), the risk control model is rejected as inadequate for live capital.
   - *Action:* Re-engineer execution with hard market-order stop loss barriers.

## Crypto portability

- **Binance Linear Perpetuals (`USDT.swap`):** `direct`. The source code is natively designed for Binance USDⓈ-M futures API, WebSocket feeds, and fee structures.
- **Other Perpetual Venues (Bybit, OKX, Hyperliquid):** `adapted`. Porting requires:
  - Replacing Binance `/fapi/v1/fundingRate` and WebSocket endpoints with venue-specific equivalents.
  - Handling differing funding settlement frequencies (e.g., 1-hour continuous on Hyperliquid vs. 8-hour on Binance/Bybit).
  - Adjusting order step size and minimum notional logic.
- **Spot Markets:** `not applicable`. The strategy relies on shorting, funding arbitrage, and basis premium mean reversion, which are impossible or cost-prohibitive on un-margined spot assets.
- **Traditional Assets:** `adapted` / `unproven`. Cross-sectional multi-factor investing originates in equities, but funding rate and perpetual premium factors are unique to crypto derivatives.

## Limitations

- **No Public Historical Track Record [source-reported]:** The source provides no verifiable backtest curve or live performance metrics; confidence in profitability is strictly unproven (`confidence: medium` reflects code audit completeness, not profitability).
- **Adverse Selection on Passive Orders [research-proposed]:** Reliance on GTX limits without active chasing can result in systematic underfills on high-momentum winning tokens.
- **Point-in-Time Universe Survivorship [source-reported]:** The current script ranks current 24-hour volume rather than rolling 30-day volume and cannot verify 90-day listing age without exchange metadata, introducing mild survivorship bias in real-time screening.
- **High Turnover Sensitivity [research-proposed]:** Rebalancing across 12 contracts every 8 hours incurs continuous turnover; if real-world slippage exceeds the 4 bps estimate, alpha may be entirely eroded.
- **Small Candidate Universe [source-reported]:** The factory blueprint space is bounded to simple parametric permutations rather than open-ended symbolic discovery.

## Implementation status

- `not-implemented` in NautilusTrader or PyBroker.
- The external FMZ JavaScript implementation (Strategy `548843`) exists and has passed simulated unit/regression checks, but has not been ported or backtested in our canonical research stack.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

This record is an objective research capture of a public multi-asset crypto perpetual factor-factory architecture. It does not constitute investment advice, backtested profitability verification, or authorization for live, testnet, or paper execution in any trading account.

## Related Wiki records

- `crypto-cross-sectional-meme-momentum-funding-dynamic-rotation-2026-09-14.md` — Multi-asset dynamic rotation combining momentum and funding rate on high-volatility crypto perpetuals.
- `adaptive-alpha-weighting-ppo-llm-generated-alphas-2026-09-05.md` — Reinforcement-learning based dynamic factor weighting.
- `rl-market-making-funding-rate-capture-crypto-perpetual-2026-09-12.md` — Crypto perpetual funding rate harvesting mechanics.
- `crypto-futures-term-structure-roll-yield-carry-2026-08-31.md` — Basis and carry term-structure dynamics in crypto derivatives.

## Sources

1. **Primary FMZ Strategy Implementation:**
   - Author: 发明者量化-小小梦 (`105ed6e51bcc97792c610fdbb7e2a1d6`)
   - Title: APFF多品种永续合约自适应因子工厂策略 v0.1.0 (Adaptive Perpetual Factor Factory v0.1.0)
   - Strategy ID: `548843`
   - Created: 2026-09-04 17:30:03; Last Modified: 2026-09-08 11:12:25
   - Stable URL: https://www.fmz.com/strategy/548843
2. **Primary Technical Digest Articles:**
   - English: "Put Factors Under Continuous Evaluation: Implementing the APFF Multi-Asset Perpetual Strategy on FMZ", Topic ID: `11036`, published 2026-09-08 10:36:45, updated 2026-09-08 10:44:28. URL: https://www.fmz.com/digest-topic/11036
   - Chinese: "让因子接受持续考核：在 FMZ 实现 APFF 多品种永续合约策略", Topic ID: `11035`, published 2026-09-08 10:36:45, updated 2026-09-08 10:44:28. URL: https://www.fmz.com/digest-topic/11035
3. **Official Exchange / Platform References Cited by Source:**
   - Binance USDⓈ-M Futures Market Data API Documentation: `/fapi/v1/fundingRate`
   - FMZ Quant API Documentation: `exchange.Go`, `GetFundings`, `GetMarkets`, `GetTickers`, `EventLoop`
