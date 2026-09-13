---
schema: strategy-research-record-v1
title: "Crypto Perpetual Funding-Rate-Extreme Reversion: Quantile Crowding Fade, Cascading-Liquidation Regime Drag, and Volatility Expansion Gating"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - funding-rate
  - mean-reversion
  - crowding
  - cascading-liquidations
  - regime-filter
  - volatility-expansion
  - maker-fill-queue
  - adverse-selection
  - transaction-costs
  - walk-forward
status: research-only
confidence: high
source_as_of: 2026-09-07
sources:
  - "https://github.com/cybereow/crypto-market-microstructure/tree/34dbe408aebdf5bdbeeae4e0b4aef5378dd87dd6"
  - "https://github.com/cybereow/crypto-market-microstructure/blob/34dbe408aebdf5bdbeeae4e0b4aef5378dd87dd6/README.md"
  - "https://github.com/cybereow/crypto-market-microstructure/blob/34dbe408aebdf5bdbeeae4e0b4aef5378dd87dd6/docs/RESEARCH_LOG.md"
  - "https://github.com/cybereow/crypto-market-microstructure/blob/34dbe408aebdf5bdbeeae4e0b4aef5378dd87dd6/src/labeling.py"
  - "https://github.com/cybereow/crypto-market-microstructure/blob/34dbe408aebdf5bdbeeae4e0b4aef5378dd87dd6/src/execution.py"
  - "https://github.com/cybereow/crypto-market-microstructure/blob/34dbe408aebdf5bdbeeae4e0b4aef5378dd87dd6/src/significance.py"
  - "https://github.com/cybereow/crypto-market-microstructure/blob/34dbe408aebdf5bdbeeae4e0b4aef5378dd87dd6/scripts/train_ml.py"
  - "https://github.com/cybereow/crypto-market-microstructure/blob/34dbe408aebdf5bdbeeae4e0b4aef5378dd87dd6/scripts/backtest_funding_reversion.py"
  - "https://github.com/cybereow/crypto-market-microstructure/blob/34dbe408aebdf5bdbeeae4e0b4aef5378dd87dd6/scripts/backtest_funding_reversion_walkforward.py"
  - "https://github.com/cybereow/crypto-market-microstructure/blob/34dbe408aebdf5bdbeeae4e0b4aef5378dd87dd6/scripts/paper_test_funding_live.py"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Perpetual Funding-Rate-Extreme Reversion: Quantile Crowding Fade, Cascading-Liquidation Regime Drag, and Volatility Expansion Gating

## Provenance

- **Primary Source Repository:** `cybereow/crypto-market-microstructure` (*Crypto Quant Research Framework: tick-level data pipelines, meta-labeling ML, execution simulation, and statistical significance testing*), authored by Ali Sajedi (`codesjd` / `cybereow`) (`source-reported`).
- **Canonical Source Identity:** GitHub repository `https://github.com/cybereow/crypto-market-microstructure` at immutable commit SHA `34dbe408aebdf5bdbeeae4e0b4aef5378dd87dd6` (pushed 2026-09-07) (`source-reported`).
- **Primary Source Files Directly Inspected:**
  - `README.md`: Research synthesis summarizing statistical validation (§6–§8), maker-fill queue simulation (§9), cross-sectional momentum (§15–§17), and funding-rate-extreme reversion results (§19, §23–§26) (`source-reported`).
  - `docs/RESEARCH_LOG.md`: Experimental log detailing the mathematical identity of breakeven geometry, the retail taker cost wall, adverse selection in passive order queues, the failure of unconditioned funding reversion in liquidation crashes, and the empirical resolution of the volatility-expansion regime gate (§19, §23, §24, §25, §26) (`source-reported`).
  - `src/labeling.py`: Implementation of `funding_extreme_reversion_entries`, `funding_reversion_regime_filtered_entries`, `scan_triple_barrier`, and `triple_barrier_labels` (`source-reported`).
  - `src/execution.py`: Implementation of `simulate_maker_fills` (passive limit order pricing at an ATR offset with queue timeout) and `triple_barrier_from_fill` (`source-reported`).
  - `src/significance.py`: Implementations of `bootstrap_mean_pvalue`, `permutation_test`, and `deflated_pvalue` (`source-reported`).
  - `scripts/train_ml.py`: Calculation of `ATR_14`, `ATR_50`, and `ATR_ratio = ATR_14 / (ATR_50 + 1e-9)` (`source-reported`).
  - `scripts/backtest_funding_reversion.py`: Main backtest harness evaluating taker vs maker economics on multi-year Binance perpetual futures klines and funding histories (`source-reported`).
  - `scripts/backtest_funding_reversion_walkforward.py`: Sub-period stability evaluation across 6 equal-width annual calendar folds (`source-reported`).
  - `scripts/paper_test_funding_live.py`: Real-time shadow paper execution engine polling live Kraken Futures quotes (`source-reported`).

## Economic mechanism

### Source-reported

1. **Perpetual Funding Rate as Speculative Crowding Indicator:** In cryptocurrency perpetual contracts, the funding mechanism charges periodic payments between long and short contract holders to tether the perpetual price to the underlying spot index. An unusually elevated positive funding rate indicates that aggressive leveraged longs are paying a heavy premium to maintain directional exposure, reflecting crowded speculative long positioning. Conversely, an extreme negative funding rate reflects crowded speculative short positioning (`source-reported`).
2. **Mean-Reversion Thesis (Crowding Fade):** The source hypothesizes that extreme speculative crowding creates structural vulnerability to contrarian reversals. When funding crosses above its recent upper quantile, crowded longs are susceptible to margin exhaustion or cascading profit-taking, prompting a short entry. When funding crosses below its lower quantile, crowded shorts are susceptible to short-squeeze covering, prompting a long entry (`source-reported`).
3. **The Cascading-Liquidation Failure Mode (Regime Drag):** Unconditional funding reversion fails statistical significance over a multi-year panel (pooled maker Profit Factor 1.07, expectancy +0.14%, $p = 0.112$) (`source-reported`). A 6-fold walk-forward analysis reveals the root failure mode: during sustained market crashes with cascading forced liquidations (specifically Fold 3: 2022-03 to 2023-04, spanning the Terra/Luna, 3AC, and FTX collapses), forced liquidations continuously drive price downward in the same direction as the funding rate, completely overwhelming mean reversion (Fold 3 net expectancy −0.49%, PF 0.80, $p = 0.960$) (`source-reported`).
4. **Volatility-Expansion Regime Gate:** To isolate orderly positioning unwinds from disorderly liquidation cascades, the source introduces an objective, un-tuned volatility-expansion filter ($ATR_{ratio} = ATR_{14} / ATR_{50} < 1.05$) (`source-reported`). When short-horizon volatility is expanding ($ATR_{ratio} \ge 1.05$), the contrarian signal is suppressed because the market is experiencing structural liquidation momentum rather than liquidity-providing mean reversion (`source-reported`).
5. **Execution Taker Fee Wall:** At retail taker fees (0.40% round-trip: 0.10% fee + 0.10% slippage per side), every directional signal in the framework produces negative net expectancy (taker PF 0.87, expectancy −0.29%, $p = 0.998$). Survival requires passive maker execution (0.08% round-trip), resting limit orders inside the spread, and accepting execution queue timeout risk (`source-reported`).

### Research interpretation

- **Speculative Imbalance vs Liquidation Cascade Asymmetry:** The economic validity of funding rate contrarianism depends strictly on whether marginal price discovery is driven by discretionary positioning or mechanical liquidation engines. In stationary or compressing volatility regimes ($ATR_{ratio} < 1.05$), high funding reflects discretionary over-optimism or pessimism that decays as funding costs bite. However, in expanding volatility regimes ($ATR_{ratio} \ge 1.05$), exchange risk engines and auto-deleveraging protocols liquidate underwater collateral via price-insensitive aggressive market orders, turning the crowded positioning signal into a powerful momentum cascade.
- **Microstructural Adverse Selection in Maker Fills:** While passive limit execution eliminates the retail taker fee drag (0.40% → 0.08%), resting limit orders priced $0.15 \times ATR$ away from the market suffer severe adverse selection. As demonstrated across the author's other tests (e.g. OBV divergence where unfilled orders had an 76.4% win rate vs 46.5% for filled orders), resting limit orders fill preferentially when adverse order flow traverses the book against the trader, while winning breakouts move immediately away without filling.
- **Ineffectiveness of Technical Price Confirmation:** Adding standard technical filters (such as Bollinger Band price extremity confirmation) degrades performance ($p = 0.112 \to 0.310$, candidate pool filtered by 62%). Requiring price to already be extreme before entering forces execution into the late, exhausted stage of the move, after the high-expectancy phase of the reversion has already elapsed.

## Signal

### Signal Specification (Regime-Filtered Funding Reversion)

- **Formation Timestamp:** Evaluated strictly on the close of bar $t$ (`source-reported`).
- **Data Dependencies:** 4-hour OHLCV klines and funding rate time-series (`source-reported`).
- **Funding Quantile Calculation:**
  - Evaluated over a rolling lookback window of $N = 90$ bars (15 calendar days on 4h bars) (`source-reported`).
  - Rolling upper quantile: $Upper_t = \text{Quantile}_{0.90}(Funding_{t-90:t-1})$ (`source-reported`).
  - Rolling lower quantile: $Lower_t = \text{Quantile}_{0.10}(Funding_{t-90:t-1})$ (`source-reported`).
  - The quantiles explicitly use `.shift(1)` to ensure the current bar's funding rate is not included in the quantile calculation, eliminating look-ahead bias (`source-reported`).
- **Volatility Expansion Gate:**
  - True Range: $TR_t = \max(High_t - Low_t, |High_t - Close_{t-1}|, |Low_t - Close_{t-1}|)$ (`source-reported`).
  - Normalized ATR: $ATR_{k, t} = \left(\frac{1}{k}\sum_{i=0}^{k-1} TR_{t-i}\right) / Close_t$ (`source-reported`).
  - Volatility Ratio:
    $$ATR_{ratio, t} = \frac{ATR_{14, t}}{ATR_{50, t} + 10^{-9}}$$
  - Filter Condition: Entries are permitted only when $ATR_{ratio, t} < 1.05$ (`not_expanding`) (`source-reported`).
- **Direction Triggers:**
  - **Short Entry Candidate ($Side = -1$):**
    $$Funding_t > Upper_t \quad \text{AND} \quad ATR_{ratio, t} < 1.05$$
    Fades extreme positive funding (crowded longs) (`source-reported`).
  - **Long Entry Candidate ($Side = +1$):**
    $$Funding_t < Lower_t \quad \text{AND} \quad ATR_{ratio, t} < 1.05$$
    Fades extreme negative funding (crowded shorts) (`source-reported`).
  - If $ATR_{ratio, t} \ge 1.05$, the signal evaluates to 0 (suppressed) (`source-reported`).

### Execution & Order Model

- **Order Type:** Passive resting limit order (`source-reported`).
- **Limit Price Offset:** Priced a fraction better than the signal bar close in the maker direction:
  $$LimitPrice = Close_t - Side \times (offset\_mult \times ATR_{14, t} \times Close_t)$$
  where $offset\_mult = 0.15$ (`source-reported`). (A long bids below $Close_t$; a short asks above $Close_t$).
- **Queue Timeout:** The resting limit order remains open for up to $queue\_timeout = 3$ bars (12 hours) (`source-reported`).
- **Fill Resolution:** Evaluated sequentially on subsequent bars $j \in [t+1, t+3]$:
  - For Long ($Side = +1$): Filled at $LimitPrice$ if $Low_j \le LimitPrice$ (`source-reported`).
  - For Short ($Side = -1$): Filled at $LimitPrice$ if $High_j \ge LimitPrice$ (`source-reported`).
  - If untouched after 3 bars, the order is cancelled; no position is opened and no trade outcome is recorded (`source-reported`).
- **Triple-Barrier Exit Logic:** Anchored at fill bar $j$ and execution price $LimitPrice$:
  - **Profit Target ($PT$):** $LimitPrice + Side \times (pt\_mult \times ATR_{14, t} \times Close_t)$, where $pt\_mult = 2.0$ (`source-reported`).
  - **Stop Loss ($SL$):** $LimitPrice - Side \times (sl\_mult \times ATR_{14, t} \times Close_t)$, where $sl\_mult = 2.0$ (`source-reported`).
  - **Time Exit (Vertical Barrier):** $max\_holding = 18$ bars (72 hours = 3 days) from fill bar. Position is closed at bar $j + 18$ close (`source-reported`).
  - **Intrabar Ambiguity Resolution:** If both $PT$ and $SL$ price thresholds are touched within the high-low span of the same 4h bar, the stop-loss is conservatively resolved first (`source-reported`).
- **Operational Status:** Fully specified in Python source (`source-reported`). Position sizing is not dynamically tuned by the signal and is modeled on a fixed 1-unit risk per trade (`research-proposed`).

## Required data

- **Instrument / Universe:** Liquid cryptocurrency perpetual futures: Binance USDⓈ-M perpetual contracts `BTCUSDT`, `ETHUSDT`, `SOLUSDT` (`source-reported`). Cross-verified on Kraken Futures `BTC/USD:USD`, `ETH/USD:USD`, `SOL/USD:USD` (`source-reported`).
- **Venue:** Binance Futures public archive (`data.binance.vision`) (`source-reported`); Kraken Futures (`ccxt.krakenfutures`) for live forward monitoring (`source-reported`).
- **Market Type:** Centralized exchange USD(T)-margined linear perpetual futures (`source-reported`).
- **Timeframe:** 4-hour OHLCV klines (`source-reported`).
- **Data Fields:** Open, High, Low, Close, Volume, and historical funding rate series (`source-reported`).
- **Funding Rate Frequency:** Historical Binance funding rates settle at 8-hour intervals (00:00, 08:00, 16:00 UTC) and are forward-filled onto 4-hour klines (`source-reported`). Kraken Futures accrues funding continuously/hourly at a smaller per-observation magnitude (~$10^{-5}$ to $10^{-6}$ vs Binance's $10^{-4}$ to $10^{-2}$), necessitating quantile-only evaluation rather than absolute thresholding (`source-reported`).
- **Point-in-Time Alignment:** Funding rate joins onto klines using left-join on timestamp; quantiles shifted by 1 bar (`shift(1)`) to ensure complete point-in-time causality without look-ahead (`source-reported`).

## Execution assumptions

- **Model Execution Venue:** Binance Futures / Kraken Futures (`source-reported`).
- **Taker Execution Baseline:** Round-trip transaction cost assumed at 0.40% (0.10% commission + 0.10% slippage per side) (`source-reported`).
- **Maker Execution Baseline:** Round-trip transaction cost assumed at 0.08% (0.02% maker fee + 0.02% slippage per side) (`source-reported`).
- **Fill Model:** Optimistic OHLC limit queue simulation. A bar touching $LimitPrice$ is assumed filled (`source-reported`). True order book queue position, order cancellation ahead of the queue, and book depth depletion are not modeled in the historical engine (`source-reported`).
- **Funding Payment Accounting:** Sized on the directional position return; cash flows are bounded by the 72-hour maximum holding horizon (`source-reported`).
- **Execution Latency:** 4-hour bar close to next-bar order placement allows ample compute time (~seconds) relative to the bar interval (`research-proposed`).

## Evidence

### Source-reported

1. **Unconditioned Funding Reversion (§19):**
   - Sample Period: 2020-01-01 to 2026-07-31 (6.5 years).
   - Universe: Binance perpetuals `BTCUSDT`, `ETHUSDT`, `SOLUSDT` pooled (4h bars).
   - Candidate Set: 2,439 signals generated (`source-reported`).
   - Taker Result: 2,439 trades, Win Rate 51.7%, Profit Factor 0.87, net expectancy −0.29% per trade, bootstrap $p = 0.998$ (unprofitable) (`source-reported`).
   - Maker Result: 2,167 filled trades (88.8% fill rate), Win Rate 52.2%, Profit Factor 1.07, net expectancy +0.14% per trade, bootstrap $p = 0.112$ (promising, but not statistically significant) (`source-reported`).
2. **Sub-Period Walk-Forward Breakdown of Unconditioned Signal (§24):**
   - Tested across 6 sequential, equal-width annual calendar folds (`source-reported`):
     - Fold 1 (2020-01 to 2021-02): $n = 271$, Win Rate 54.6%, PF 1.24, Expectancy +0.69%, $p = 0.070$ (`source-reported`).
     - Fold 2 (2021-02 to 2022-03): $n = 310$, Win Rate 54.8%, PF 1.17, Expectancy +0.45%, $p = 0.126$ (`source-reported`).
     - **Fold 3 (2022-03 to 2023-04, Crash Regime):** $n = 348$, Win Rate 49.4%, **PF 0.80, Expectancy −0.49%, $p = 0.960$** (severe failure) (`source-reported`).
     - Fold 4 (2023-04 to 2024-05): $n = 346$, Win Rate 53.8%, PF 1.06, Expectancy +0.09%, $p = 0.344$ (`source-reported`).
     - Fold 5 (2024-05 to 2025-06): $n = 395$, Win Rate 52.9%, PF 1.30, Expectancy +0.48%, **$p = 0.016$** (individually significant) (`source-reported`).
     - **Fold 6 (2025-06 to 2026-07):** $n = 497$, Win Rate 49.7%, **PF 0.92, Expectancy −0.13%, $p = 0.803$** (`source-reported`).
3. **Price Confirmation Ablation Failure (§23):**
   - Adding Bollinger Band position filter ($bb\_position > 0.5$): Candidates reduced from 2,439 to 926 (filtered by 62%). Win Rate 51.6%, PF 1.04, Expectancy +0.10%, $p = 0.310$ (degraded significance) (`source-reported`).
4. **Volatility-Expansion Regime-Filtered Funding Reversion (§25):**
   - Filter: Gated off when $ATR_{ratio} \ge 1.05$ (`source-reported`).
   - Pooled Results (2020–2026, BTC/ETH/SOL):
     - Candidate Set: 1,456 signals (40% filtered out) (`source-reported`).
     - Filled Trades: 1,287 trades (88.4% fill rate) (`source-reported`).
     - Win Rate: 53.5% (`source-reported`).
     - Profit Factor: **1.15** (`source-reported`).
     - Net Expectancy: **+0.26% per trade** (`source-reported`).
     - Pooled Bootstrap Significance: **$p = 0.0130$** (`source-reported`).
     - Deflated Significance (correcting for 3 configuration trials via `deflated_pvalue`): **$p_{deflated} = 0.0385 < 0.05$** (`source-reported`).
   - Walk-Forward 6-Fold Stability:
     - Fold 1 (2020-01 to 2021-02): $n = 125$, PF 1.52, Expectancy +1.12%, **$p = 0.023$** (`source-reported`).
     - Fold 2 (2021-02 to 2022-03): $n = 199$, PF 1.43, Expectancy +0.90%, **$p = 0.009$** (`source-reported`).
     - Fold 3 (2022-03 to 2023-04): $n = 210$, PF 0.89, Expectancy −0.24%, $p = 0.763$ (loss halved vs unconditioned −0.49%) (`source-reported`).
     - Fold 4 (2023-04 to 2024-05): $n = 203$, PF 1.34, Expectancy +0.40%, **$p = 0.033$** (`source-reported`).
     - Fold 5 (2024-05 to 2025-06): $n = 231$, PF 1.15, Expectancy +0.21%, $p = 0.180$ (`source-reported`).
     - Fold 6 (2025-06 to 2026-07): $n = 319$, PF 0.88, Expectancy −0.19%, $p = 0.845$ (`source-reported`).
5. **LLM Decision Gate Falsification (§22):**
   - Pre-trade filtering by an LLM (Claude API) on funding candidates: out of 1,508 candidates, the LLM approved only 2 (0.13% approval rate). The 2 approved trades suffered net expectancy of −2.02% (PF 0.48), performing substantially worse than the unfiltered baseline (`source-reported`).

### Independently reproduced

- Not independently reproduced.

### Negative evidence

- **Complete Annihilation under Taker Fees:** At realistic retail taker fees (0.40%), the unconditioned signal has an expectancy of −0.29% ($p = 0.998$). Even the regime-filtered signal cannot overcome retail taker fees (`source-reported`).
- **Persistent Residual Crash Drag in Fold 3:** While the $ATR_{ratio} < 1.05$ filter halved the loss during the 2022 liquidation cascade (expectancy improved from −0.49% to −0.24%), it did not eliminate the drawdown. A coarse volatility ratio is an imperfect proxy for recursive insolvency cascades (`source-reported`).
- **Recent Regime Decay in Fold 6:** Fold 6 (2025-06 to 2026-07) remained negative (PF 0.88, expectancy −0.19%), indicating that either funding rate crowding signals are decaying in recent market regimes or low-volatility chop generates false signals (`source-reported`).

## Falsification plan

1. **Exchange Queue Fill Reality Test:**
   - *Test:* Replay the 1,287 trades using full Level 2 order book tick data or live quote logs from Kraken/Binance instead of OHLC high/low touch simulation.
   - *Decision Rule:* If real queue priority drops fill rate below 75% or exacerbates adverse selection such that filled-trade PF drops below 1.00 (`research-defined falsification threshold`), reject the passive limit order execution model as an unviable artifact.
2. **Transaction Cost Sensitivity Stress:**
   - *Test:* Progressively increase round-trip maker execution costs from 0.08% to 0.16% in steps of 0.02%.
   - *Decision Rule:* If net expectancy turns negative at round-trip costs $\le 0.14\%$ (`research-defined falsification threshold`), classify the strategy as non-implementable for non-VIP fee tiers.
3. **Out-of-Sample Calendar Window Test (Post-July 2026):**
   - *Test:* Evaluate the strategy on post-2026-07 data across BTC, ETH, and SOL perpetuals without parameter retraining.
   - *Decision Rule:* If out-of-sample Profit Factor remains below 0.95 over $\ge 200$ trades (`research-defined falsification threshold`), reject the funding extreme reversion hypothesis as permanently degraded.
4. **Placebo Shuffled Funding Test:**
   - *Test:* Randomly permute the funding rate series relative to OHLCV while preserving funding autocorrelation.
   - *Decision Rule:* If synthetic shuffled funding series produce Profit Factors $\ge 1.10$ in $> 5\%$ of trials (`research-defined falsification threshold`), reject the claim that funding rate extremes carry unique causal predictive information.

## Crypto portability

- **Portability Classification:** `direct` (`source-reported`).
- **Rationale:** The funding rate mechanism is an idiosyncratic structural feature of cryptocurrency perpetual futures contracts (invented by BitMEX and adopted across Binance, Bybit, OKX, and Kraken). It has no direct equivalent in traditional equity spot or dated futures markets.
- **Portability Risks & Considerations:**
  - *Funding Interval Discrepancies:* Binance charges funding every 8 hours, whereas Kraken Futures accrues funding continuously/hourly, and decentralized perpetual protocols (e.g. dYdX, Hyperliquid) update funding hourly or per block. Quantile definitions must be normalized to contract settlement cadence.
  - *Perpetual vs Spot Basis Volatility:* During rapid market crashes, perpetual prices trade at steep discounts to spot; fading negative funding during such events exposes the trader to widening basis risk.
  - *Auto-Deleveraging (ADL) and Liquidation Spreads:* Large market extremes triggering the signal coincide with exchange margin stress, elevating the probability of contract ADL or unexpected liquidation engine spread widening.

## Limitations

- **Queue Fill Optimism:** Historical backtesting assumes that touching a price guarantees order execution. In shallow order books or rapid market movements, resting limit orders frequently fail to fill before price turns away.
- **Asset Universe Breadth:** The empirical study evaluates only 3 major cryptocurrency perpetuals (`BTCUSDT`, `ETHUSDT`, `SOLUSDT`). Generalization to long-tail altcoin perpetuals with erratic funding spikes remains unproven.
- **Unresolved Degradation in Fold 6:** The strategy loses money in the 2025–2026 annual fold (PF 0.88), which is not fully accounted for by the liquidation cascade thesis and may reflect changing participant structure or algorithmic crowding.
- **Strict Maker Dependency:** The edge cannot be executed with taker market orders; it exists strictly on the margin between the raw move and passive fee rebates.

## Implementation status

- Frontmatter: `implementation_status: not-implemented`
- The strategy has been researched and backtested in the upstream `cybereow/crypto-market-microstructure` repository.
- No NautilusTrader, PyBroker, paper trading, testnet, or live trading implementation exists in the current system.

## Adoption boundary

- Frontmatter: `status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.
- Inclusion of this record in the repository is strictly for quantitative research capture and hypothesis logging.
- It does not authorize implementation, automated signal generation, paper trading, testnet execution, or capital allocation.

## Related Wiki records

- `[[quant/crypto-funding-rate-mean-reversion-ema-taker-filter-2026-09-11]]`
- `[[quant/crypto-funding-rate-feedback-regime-capital-stability-band-2026-09-12]]`
- `[[quant/crypto-funding-carry-fade-turnover-cost-dissipation-falsification-2026-09-12]]`
- `[[quant/retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11]]`
- `[[quant/extreme-negative-funding-contrarian-btc-return-2026-09-06]]`

## Sources

- **Primary Repository:** GitHub repository `https://github.com/cybereow/crypto-market-microstructure` at commit SHA `34dbe408aebdf5bdbeeae4e0b4aef5378dd87dd6` (`source-reported`).
- **Project Overview & Executive Summary:** `README.md` (`source-reported`).
- **Detailed Experimental Documentation:** `docs/RESEARCH_LOG.md` (Sections §6, §7, §8, §9, §19, §23, §24, §25, §26) (`source-reported`).
- **Signal Logic & Filter Implementation:** `src/labeling.py` (`funding_extreme_reversion_entries`, `funding_reversion_regime_filtered_entries`, `scan_triple_barrier`) (`source-reported`).
- **Maker Queue Simulation:** `src/execution.py` (`simulate_maker_fills`, `triple_barrier_from_fill`) (`source-reported`).
- **Inference & Deflated Significance:** `src/significance.py` (`bootstrap_mean_pvalue`, `deflated_pvalue`) (`source-reported`).
- **Feature Engineering:** `scripts/train_ml.py` (`create_features`, `ATR_ratio` calculation) (`source-reported`).
- **Backtest Drivers:** `scripts/backtest_funding_reversion.py` and `scripts/backtest_funding_reversion_walkforward.py` (`source-reported`).
- **Live Shadow Monitoring:** `scripts/paper_test_funding_live.py` (`source-reported`).
