---
schema: strategy-research-record-v1
title: "Crypto Perpetual Regime-Aligned Right-Tail Trend Following: Standardized Return t-Statistic Momentum, 4-Hour SMA200 Macro Gating, Pre-Trade All-In Cost Hurdle, and Multi-Window Stress Falsification"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto-perpetual
  - trend-following
  - right-tail-momentum
  - regime-gating
  - cost-hurdle
  - stress-testing
  - forward-testing
  - falsification
status: research-only
confidence: high
source_as_of: 2026-09-13
sources:
  - "TheLitis, 'Deterministic historical evaluation framework for Kairos strategies', GitHub repository, commit 758d1a383364726fe1f7b7ce8e9155f33da750bf (September 13, 2026), https://github.com/Kairos-cryptoAI/kairos-backtest"
  - "Kairos-cryptoAI, 'kairos-strategy-engine: Canonical strategy execution and intent generation', GitHub repository, commit fb7d406c6e1a3060f481b91668ff3bc23a1b4b0d, https://github.com/Kairos-cryptoAI/kairos-strategy-engine"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Perpetual Regime-Aligned Right-Tail Trend Following: Standardized Return t-Statistic Momentum, 4-Hour SMA200 Macro Gating, Pre-Trade All-In Cost Hurdle, and Multi-Window Stress Falsification

## Provenance

- **Primary Source:** TheLitis, *"Deterministic historical evaluation framework for Kairos strategies"*, public GitHub repository: `https://github.com/Kairos-cryptoAI/kairos-backtest`.
- **Immutable Commit SHA:** `758d1a383364726fe1f7b7ce8e9155f33da750bf` (committed September 13, 2026).
- **Downstream Dependency Repositories:**
  - `kairos-strategy-engine`: `https://github.com/Kairos-cryptoAI/kairos-strategy-engine` (commit `fb7d406c6e1a3060f481b91668ff3bc23a1b4b0d`).
  - `kairos-core`: `https://github.com/Kairos-cryptoAI/kairos-core` (commit `91cd95c8e5bd4393ed04606df08c205583092df7`).
- **Exact Primary Source Paths Examined:**
  - `README.md`
  - `STRATEGY_V2.md`
  - `DATA_QUALITY_POLICY.md`
  - `kairos_backtest/regime_aligned_screen.py`
  - `kairos_backtest/cost_risk.py`
  - `kairos_backtest/scenarios.py`
  - `kairos_backtest/right_tail_screen.py`
  - `reports/regime-aligned-screen/REPORT.md`
  - `reports/regime-aligned-screen/summary.json`
  - `reports/regime-aligned-forward/WARMUP.md`
  - `reports/development-screen/REPORT.md`
  - `reports/orderflow-screen/REPORT.md`
  - `reports/regime-retest-screen/REPORT.md`
  - In `kairos-strategy-engine`:
    - `kairos_strategy/sleeves/regime_aligned_right_tail.py`
    - `kairos_strategy/sleeves/right_tail_trend.py`
- **Data Scope & Universe:** Binance USD-M perpetual futures across five liquid large-cap crypto contracts (`BTCUSDT`, `ETHUSDT`, `SOLUSDT`, `BNBUSDT`, `XRPUSDT`). Point-in-time 1-minute OHLCV price-volume bars validated against official Binance monthly and daily archive SHA-256 and ZIP CRC checksums (6,055,200 rows with zero missing or quarantined rows across preflight). Evaluated across two independent historical windows: Selection (July 2024 through June 2025, 12 months) and Robustness (July 2021 through June 2024, 36 months).
- **Repository Deduplication:** Audited all existing `.md` records in `alpha-strategy-research`. Zero prior records cite `Kairos-cryptoAI`, `TheLitis`, or this evaluation framework. Related crypto trend-following records (`hyperliquid-vol-targeted-tsmom-drawdown-calibrated-ratchet-2026-09-12.md`, `crypto-smc-fvg-bpr-liquidity-retracement-random-walk-falsification-2026-09-12.md`, `crypto-bitcoin-cvar-risk-aware-q-learning-adaptive-controller-2026-09-02.md`) investigate time-series momentum with ATR ratchets on Hyperliquid, retail SMC/FVG retracement falsifications, or Q-learning CVaR controllers on Bitcoin. None examine this specific combination: standardized return t-statistic momentum, 4h SMA200 macro gating, pre-trade cost-hurdle sizing, empirical stress survival across 48 months of Binance perpetual data, and pre-registered forward tracking.

## Economic mechanism

### Source-reported

1. **Convex Right-Tail Skewness Harvesting vs. Negative Baseline:** The author observes that unconstrained multi-timeframe crypto trend-following strategies deliver negative net returns under realistic market frictions (`-4.2317%` under baseline costs and `-9.7632%` under stress costs over a 12-month baseline). Rather than optimizing for win rate or trade frequency, the strategy is constructed as an asymmetric right-tail harvester: it accepts a low hit rate (~33%) and negative median returns (~-1.10R) in exchange for convex right-tail payoff events ($+3.55\text{R}$ to $+4.0\text{R}$) that overcome trading friction.
2. **Dimensionless Standardized Return t-Statistic:** Raw price momentum is confounded by local volatility surges. By scaling the sum of 24 hourly log returns by the Euclidean norm of return increments ($\sum r_t / \sqrt{\sum r_t^2}$), the strategy measures the statistical significance (t-statistic) of the 24-hour drift. Only directional moves with $|t| \ge 1.0$ qualify for entry.
3. **Macro Regime Filter (`regime_aligned_right_tail_v1`):** In choppy or counter-trend regimes, short-term momentum signals frequently fail into adverse inventory accumulation. Filtering daily right-tail signals by a slow 4-hour 200-bar Simple Moving Average ($\approx 800\text{ hours} \approx 33.3\text{ days}$) ensures that long entries are taken only during macro bull regimes ($\text{close}_{4h} > \text{SMA200}_{4h}$) and short entries only during macro bear regimes ($\text{close}_{4h} < \text{SMA200}_{4h}$).
4. **Pre-Trade All-In Cost Hurdle & Sizing:** A trade is admissible only when its gross expected reward exceeds the estimated round-trip trading cost (taker fees, spread, slippage, adverse funding carry, and uncertainty buffer) and yields an expected net reward-to-risk ratio $\ge 1.25$. Sizing is strictly computed against the protective stop distance ($2.0 \times \text{ATR}_{24}$) to cap trade risk at $0.25\%$ of cell equity.

### Research interpretation

1. **Dual-Timeframe Trend-Regime Decoupling:** The strategy decouples signal formation (24-hour standardized return t-statistic) from regime gating (800-hour 4h SMA200). This avoids indicator stacking on the same horizon. The 4h SMA200 suppresses counter-trend whipsaws during prolonged bear or bull regimes, reducing total trade count while boosting profit factor under stress from 1.0382 to 1.1071 in the robustness window.
2. **Rigorous Preregistration & Trial Accounting:** Unlike commercial crypto bots that tune hundreds of indicator combinations post hoc, Kairos enforces strict trial accounting. `regime_aligned_right_tail_v1` was designated Trial 15 in an append-only registry. Three earlier retail sleeves—pullback reclaims, order-flow expansions, and breakout retests—were formally rejected on the same infrastructure after failing pre-registered cost and retention gates.
3. **Cost Netting Reality in Crypto Perps:** High turnover is the primary killer of quantitative crypto alphas. Binance VIP0 perpetual taker fees are 4.5 to 5.0 bps per leg (9.0 to 10.0 bps round-trip). By enforcing an explicit mathematical hurdle ($\text{net reward} / \text{loss at stop} \ge 1.25$) before order dispatch, the strategy systematically refuses unfeasible trades during high-volatility, high-spread, or adverse-funding conditions.

## Signal

### Formation timestamp

- **Observation Clock:** Evaluated causally at UTC epoch-aligned 24-hour boundaries (`decision_interval_hours = 24`, checking `open_time_ms % (24 * 3600 * 1000) == 0`).
- **Tradability Timing:** Signals are generated at bar close ($t$ close) and become tradable at the next minute bar ($t$ close + 1 ms, `entry_eligible_ts_ms = close_time_ms + 1`).
- **Intent Expiry:** Intents remain valid for 1 hour (`intent_valid_hours = 1`, `entry_expires_ts_ms = close_time_ms + 3,600,000`). If unexecuted within 60 minutes, the intent expires without fill.

### Lookback windows

- **Trend Score Lookback ($W_{\text{trend}}$):** 24 hours of hourly closed bars ($W = 24$).
- **Volatility Normalization Lookback ($W_{\text{ATR}}$):** 24 hours of hourly closed bars using Wilder's Average True Range ($W = 24$).
- **Macro Regime Lookback ($W_{\text{regime}}$):** 200 bars of 4-hour closed bars ($200 \times 4\text{h} = 800\text{ hours} \approx 33.3\text{ days}$).

### Entry rules

1. **Hourly Log Returns & Trend Score:**
   $$\text{score} = \frac{\sum_{i=0}^{23} r_{t-i}}{\sqrt{\sum_{i=0}^{23} r_{t-i}^2}}, \quad \text{where } r_t = \ln\left(\frac{\text{close}_t}{\text{close}_{t-1}}\right)$$
2. **Directional Threshold:**
   - Long Candidate: $\text{score} \ge 1.0$ (`minimum_trend_score = 1.0`).
   - Short Candidate: $\text{score} \le -1.0$ (`minimum_trend_score = 1.0`).
   - Flat: $-1.0 < \text{score} < 1.0$.
3. **Macro Regime Alignment Gate:**
   - Long Allowed: Most recent complete 4-hour close exceeds 4h SMA200 ($\text{close}_{4h} > \text{SMA200}_{4h}$).
   - Short Allowed: Most recent complete 4-hour close is below 4h SMA200 ($\text{close}_{4h} < \text{SMA200}_{4h}$).
   - Staleness Guard: The completed 4-hour regime bar must not be older than 4 hours ($\text{age} < 4\text{ hours}$).
4. **Pre-Trade All-In Cost Admission Hurdle:**
   - Calculate all-in cost hurdle:
     $$\text{cost\_hurdle} = 2 \times \text{fee} + \text{spread} + 2 \times \text{slippage} + \text{adverse\_funding} + \text{latency} + \text{uncertainty\_buffer}$$
   - Baseline hurdle: $2 \times 4.5 + 2.0 + 2 \times 1.0 + 0.0 + 0.0 + 2.0 = 15.0\text{ bps}$.
   - Reject if gross reward $\le \text{cost\_hurdle}$ (`REWARD_BELOW_COST_HURDLE`).
   - Reject if $\text{net\_reward\_to\_risk} < 1.25$ (`REWARD_RISK_TOO_LOW`).
5. **Overlapping Position Guard:**
   - If an open position in the symbol already exists, new intents for that symbol are refused (`overlapping_position`).

### Exit rules

- **Protective Stop-Loss:**
  - Placed at $2.0 \times \text{ATR}_{24}$ from reference entry price (`stop_atr_multiple = 2.0`).
  - Long: $P_{\text{stop}} = P_{\text{entry}} - 2.0 \times \text{ATR}_{24}$.
  - Short: $P_{\text{stop}} = P_{\text{entry}} + 2.0 \times \text{ATR}_{24}$.
- **Profit Target (Take-Profit):**
  - Placed at $4.0 \times \text{risk\_distance} = 8.0 \times \text{ATR}_{24}$ from entry (`target_reward_to_risk = 4.0`).
  - Long: $P_{\text{target}} = P_{\text{entry}} + 8.0 \times \text{ATR}_{24}$.
  - Short: $P_{\text{target}} = P_{\text{entry}} - 8.0 \times \text{ATR}_{24}$.
- **Time-Based Exit (Holding Horizon):**
  - Maximum holding duration: 72 hours (`max_hold_hours = 72`).
  - Upon reaching 72 hours without hitting stop or target, the position is liquidated at market with a finite terminal liquidation deadline.

### Position sizing logic

- **Risk Budgeting:** Risk fraction is strictly capped at $0.25\%$ of isolated cell equity per trade ($0.0025 \times \text{equity}$).
- **Unit Loss Formulation:**
  $$\text{loss\_per\_unit} = |P_{\text{entry}} - P_{\text{stop}}| + \max(P_{\text{entry}}, P_{\text{stop}}) \times \frac{\text{cost\_hurdle}}{10{,}000}$$
- **Notional Cap:**
  $$\text{notional\_cap} = \text{equity} \times 0.25 \times 1.0 = 0.25 \times \text{equity}$$
- **Executable Quantity:**
  $$Q = \min\left(\frac{\text{equity} \times 0.0025}{\text{loss\_per\_unit}}, \frac{\text{notional\_cap}}{P_{\text{entry}}}\right)$$
- Sizing is independent of signal strength; confidence cannot increase position size.

### Parameters

- Trend lookback: 24 hours (`source-reported`).
- Minimum trend score: 1.0 (`source-reported`).
- ATR period: 24 hours (`source-reported`).
- Stop ATR multiple: 2.0 (`source-reported`).
- Target reward-to-risk: 4.0 (`source-reported`).
- Maximum hold: 72 hours (`source-reported`).
- Decision interval: 24 hours (`source-reported`).
- Intent validity: 1 hour (`source-reported`).
- Regime SMA timeframe: 4 hours (`source-reported`).
- Regime SMA window: 200 bars (`source-reported`).
- Risk fraction: 0.25% per trade (`source-reported`).
- Maximum notional fraction: 25% per trade (`source-reported`).
- Maximum leverage: 1.0x (unleveraged) (`source-reported`).
- Minimum net reward-to-risk: 1.25 (`source-reported`).
- Minimum stop distance: 10 bps (`source-reported`).
- Maximum stop distance: 500 bps (`source-reported`).

## Required data

- **Instruments:** Binance USD-M perpetual contracts: `BTCUSDT`, `ETHUSDT`, `SOLUSDT`, `BNBUSDT`, `XRPUSDT`.
- **Timeframe:** 1-minute base OHLCV bars aggregated to 1-hour bars for signal and ATR calculations, and 4-hour bars for SMA200 regime state.
- **Data Integrity Requirements:** High-frequency Binance monthly and daily archives verified against official Binance SHA-256 and ZIP CRC checksums. Contiguous rows required (1,440 minute rows per day); zero missing rows or NaN values allowed.
- **Price Adjustment:** Raw continuous perpetual prices. Funding rates are tracked separately and not back-adjusted into OHLCV.
- **Volume & Liquidity:** 1-minute volume is preserved solely for execution capacity checks (participation cap); taker volume fields are zeroed for pricing.

## Execution assumptions

- **Order Types:** Entry via market order at open of next minute bar after intent formation. Stop-loss and take-profit modeled as resting venue orders.
- **Latency:** Modeled at 250 ms baseline and 500 ms stress (`source-reported`).
- **Bid-Ask Spread:** 2.0 bps baseline and 4.0 bps stress (`source-reported`).
- **Slippage:** 2.0 bps baseline and 4.0 bps stress (`source-reported`).
- **Taker Fees:** 4.5 bps per fill (9.0 bps round-trip) (`source-reported`).
- **Funding Carry:** 0.0 bps baseline; 5.0 bps per 8-hour settlement adverse carry under stress (`source-reported`).
- **Execution Scenarios:**
  - *Baseline Scenario:* 250 ms latency, 2.0 bps spread, 2.0 bps slippage, 4.5 bps fee, 0.0 bps funding.
  - *Stress Scenario:* 500 ms latency, 4.0 bps spread, 4.0 bps slippage, 4.5 bps fee, 5.0 bps/8h adverse funding.
- **Portfolio Construction:** Five isolated capital cells of $20,000 each ($100,000 total portfolio equity). Capital is not pooled dynamically across symbols.

## Evidence

### Source-reported

All empirical results trace directly to committed JSON artifacts and evaluation reports in `Kairos-cryptoAI/kairos-backtest` (commit `758d1a383364726fe1f7b7ce8e9155f33da750bf`, files `reports/regime-aligned-screen/REPORT.md`, `reports/regime-aligned-screen/summary.json`, and `reports/regime-aligned-forward/WARMUP.md`):

#### 1. Reused Historical Performance Across Two Windows

| Window | Scenario | Total Return | Profit Factor | HAC Sharpe | Max Drawdown | Trades | Win Rate | Trade Retention vs Base |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **Selection (Jul 2024–Jun 2025)** | Baseline | +3.7322% | 1.3719 | 1.4231 | 1.1569% | 312 | 33.3% | 67.97% |
| Selection (Jul 2024–Jun 2025) | Stress | +1.7354% | 1.2040 | 0.8541 | 1.0891% | 312 | 33.3% | 67.97% |
| **Robustness (Jul 2021–Jun 2024)** | Baseline | +3.3046% | 1.3011 | 1.0798 | 1.7651% | 342 | 33.0% | 69.23% |
| Robustness (Jul 2021–Jun 2024) | Stress | +0.9812% | 1.1071 | 0.4239 | 1.6233% | 339 | 32.7% | 69.33% |

#### 2. Exact Base Benchmark Comparison (`right_tail_trend_v1` without 4h SMA200 Gate)

| Window | Scenario | Base Return | Base Profit Factor | Base Max Drawdown | Base Trades | Added Gate Effect |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| Selection | Baseline | +5.5692% | 1.3756 | 1.2308% | 459 | Lower gross return, lower drawdown |
| Selection | Stress | +2.3079% | 1.1833 | 1.2801% | 459 | **Higher PF (+0.0207), lower DD (-0.191%)** |
| Robustness | Baseline | +4.0817% | 1.2624 | 1.4780% | 494 | Lower gross return, higher DD |
| Robustness | Stress | +0.4968% | 1.0382 | 1.7652% | 489 | **Double return (+0.98% vs +0.50%), higher PF (+0.0689), lower DD (-0.142%)** |

#### 3. Per-Symbol Stress Breakdown

- **Selection Window Stress (Jul 2024–Jun 2025):**
  - `BTCUSDT`: 63 trades, return $+0.1389\%$, expectancy $+\$0.44$/trade.
  - `ETHUSDT`: 64 trades, return $+2.5360\%$, expectancy $+\$7.93$/trade.
  - `SOLUSDT`: 68 trades, return $+4.1266\%$, expectancy $+\$12.14$/trade.
  - `BNBUSDT`: 67 trades, return $-1.0497\%$, expectancy $-\$3.13$/trade.
  - `XRPUSDT`: 50 trades, return $+2.9251\%$, expectancy $+\$11.70$/trade.
  - *Positive expectancy symbols:* 4 out of 5 (BNB negative).
- **Robustness Window Stress (Jul 2021–Jun 2024):**
  - `BTCUSDT`: 68 trades, return $-0.2817\%$, expectancy $-\$0.83$/trade.
  - `ETHUSDT`: 68 trades, return $+2.1893\%$, expectancy $+\$6.44$/trade.
  - `SOLUSDT`: 66 trades, return $-0.6609\%$, expectancy $-\$2.00$/trade.
  - `BNBUSDT`: 70 trades, return $+1.6607\%$, expectancy $+\$4.75$/trade.
  - `XRPUSDT`: 67 trades, return $+1.9987\%$, expectancy $+\$5.97$/trade.
  - *Positive expectancy symbols:* 3 out of 5 (BTC and SOL negative).

#### 4. Pre-Registered Forward Observation Ledger Status

- **Freeze Status:** Frozen as `FORWARD_FREEZE_CANDIDATE` on August 27, 2026.
- **Forward Tracking Horizon:** Commenced September 1, 2026.
- **As of Date (September 13, 2026):** 12 complete blind-period days collected (`WARMUP.md`, SHA-256 `9344fc0cf82987eda1f61627eee9c3b780305fb09d86e36b7e88e807fb0d6bc9`). Zero gaps across 374,400 forward minute bars.
- **Promotion Hurdles:** Pre-declared 365 complete forward calendar days and 500 closed simulated trades required before any promotion to paper or canary trading can be considered.

### Independently reproduced

Not independently reproduced. All figures, tables, and hash digests are third-party results reported by TheLitis in GitHub repository `Kairos-cryptoAI/kairos-backtest` (commit `758d1a383364726fe1f7b7ce8e9155f33da750bf`).

### Negative evidence

1. **Rejection of Three Pre-Registered Alternative Sleeves on Same Data:**
   - *Trend Pullback Reclaim (`trend_pullback_reclaim_v1`):* Evaluated three pullback depths (`shallow`, `medium`, `deep`). Medium produced 105 baseline trades but lost $-0.7125\%$ (PF 0.683). Shallow lost under stress ($-0.0568\%$, PF 0.840). Deep produced only 10 stress trades. Decision: `REJECT_ALL`.
   - *Order-Flow Volatility Expansion (`orderflow_volatility_expansion_v1`):* Attempted entry on volume/range expansion. Generated 387 baseline and 301 stress trades, but produced severe net losses ($-2.9005\%$ baseline, $-3.2540\%$ stress). Decision: `REJECT_ALL`.
   - *Regime-Veto Retest Reclaim (`regime_veto_retest_reclaim_v1`):* Stacked expansion, retest, and reclaim gates. Out of 41,741 breakout candidates, only 1 baseline trade occurred ($-0.0155\%$) and 0 stress trades survived. Strategy failed due to over-filtering. Decision: `REJECT_ALL`.
2. **Fragile Single-Symbol Expectancy Under Stress:**
   - In the 3-year robustness window under stress, BTC lost $-0.2817\%$ and SOL lost $-0.6609\%$. Positive expectancy was maintained on only 3 out of 5 symbols (ETH, BNB, XRP), exactly meeting the preregistered 3-symbol minimum floor with zero safety margin.
3. **Severe Skew Dependence & Low Win Rate:**
   - The strategy relies entirely on right-tail outliers. Win rate is only ~33%, median trade return is negative ($\approx -1.10\text{R}$), and profits are driven by top-decile winners ($p90 \approx +3.55\text{R}$). Traders must endure extended losing runs of 10 to 15 consecutive stopped-out trades.
4. **Modest Absolute Return:**
   - Annualized return across 2021–2024 is $+3.30\%$ baseline and $+0.98\%$ stress on 1x unleveraged capital. While positive net of costs, it provides low nominal return per unit of operational complexity.

## Falsification plan

To falsify the hypothesis that standardized return t-statistic momentum with 4h SMA200 macro gating extracts durable alpha net of crypto perpetual frictions:

1. **Adverse Fee & Slippage Stress Barrier Test:**
   - *Protocol:* Replay the 48-month panel with stepped taker fees (5.0, 7.5, 10.0, and 12.5 bps per leg) and slippage (3.0, 5.0, 8.0 bps).
   - *Decision Rule (`research-defined falsification threshold`):* If total portfolio net return over either Selection or Robustness drops below $0.0\%$ at or below 8.0 bps taker fee + 4.0 bps slippage, the strategy is falsified as a fee-intolerant trading artifact.
2. **Holding Horizon Truncation & Take-Profit Elimination Test:**
   - *Protocol:* Perturb the take-profit multiple from 4.0R down to 2.0R, 1.5R, and 1.0R (capping right-tail gains) and test maximum holding horizons of 24h, 48h, 72h, and 120h.
   - *Decision Rule (`research-defined falsification threshold`):* If capping the profit target at 2.0R causes net return to drop below zero, the strategy is confirmed to be strictly dependent on right-tail convexity and cannot operate under capped-gain regimes.
3. **Macro Regime Ablation & Random-State Placebo Test:**
   - *Protocol:* Replace the 4h SMA200 filter with: (a) no filter, (b) inverted filter (long below SMA, short above), and (c) random binary regime assignment.
   - *Decision Rule (`research-defined falsification threshold`):* If the inverted regime filter achieves positive stress return or the real SMA200 filter does not outperform random regime assignment by $>1.0\%$ net return, the 4h SMA200 macro alignment hypothesis is falsified.
4. **Cross-Sectional Breadth Expansion Test:**
   - *Protocol:* Expand universe from 5 assets to top 30 Binance USD-M perpetuals by 30-day median turnover.
   - *Decision Rule (`research-defined falsification threshold`):* If fewer than 50% of symbols achieve positive expectancy or portfolio maximum drawdown exceeds $5.0\%$ under stress, the edge is falsified as an asset-selection artifact confined to ETH/BNB/XRP.
5. **Pre-Registered Forward Drift Gate:**
   - *Protocol:* Evaluate the live forward ledger upon reaching the 365-day and 500-trade completion milestones.
   - *Decision Rule (`research-defined falsification threshold`):* If forward profit factor drops below 1.05 under baseline costs or below 1.00 under stress, the strategy is declared falsified out-of-sample and permanently rejected.

## Crypto portability

- **Portability Classification:** `direct` for Binance USD-M perpetual futures; `adapted` / `unproven` for DEX perpetuals and alternative CEX venues.
- **Venue & Contract Considerations:**
  - *Binance USD-M Perpetuals (`direct`):* The primary source was designed, calibrated, and evaluated directly on Binance USD-M perpetuals using Binance archive tick data. Portability is direct.
  - *DEX Perpetuals (Hyperliquid / Bybit / dYdX) (`adapted` / `unproven`):*
    - *Fee Discrepancy:* Hyperliquid taker fees are 2.5 to 3.5 bps (lower than Binance 4.5 bps), which would loosen the pre-trade cost hurdle. However, lower order-book depth on altcoins (BNB, XRP) on Hyperliquid could increase slippage.
    - *Funding Settlement Cadence:* Binance settles funding every 8 hours; Hyperliquid updates funding continuously every hour. Adverse funding calculations must be adapted to 1-hour intervals.
    - *24/7 Continuous Operation:* Crypto operates 24/7 without market closes. The 24-hour decision interval must remain synchronized to UTC 00:00 to match historical daily candle boundaries.
- **Porting Operational Rules (`research-proposed`):**
  - *DEX Universe Filter (`research-proposed`):* Require 30-day median daily volume $\ge \$20\text{M}$ and open interest $\ge \$10\text{M}$ to prevent excessive market impact.
  - *Pre-Trade Funding Ceiling (`research-proposed`):* Reject entries if 8-hour funding rate in trade direction exceeds $+0.05\%$ (for longs) or $-0.05\%$ (for shorts), mitigating persistent carry decay.
  - *Execution Delay Guard (`research-proposed`):* Enforce execution strictly within 5 minutes of UTC 00:00; abort intent if latency exceeds 300 seconds.

## Limitations

- **Low Win Rate (~33%):** The strategy loses on roughly two-thirds of trades. Psychological and capital drawdown management requires strict adherence to risk budgets ($0.25\%$ equity risk).
- **Narrow Asset Universe:** Evaluated on only 5 large-cap assets (`BTCUSDT`, `ETHUSDT`, `SOLUSDT`, `BNBUSDT`, `XRPUSDT`). In the 3-year robustness window, BTC and SOL were net negative under stress.
- **Modest Nominal Return:** At 1x leverage, total return is $+3.3\%$ over 36 months baseline ($+0.98\%$ stress). The strategy cannot support high leverage due to 15-trade consecutive loss potential.
- **Reused Research Data Warning:** Both the trend score and the 4h SMA200 filter were selected after observing historical data across 2021–2025. The positive result represents a `FORWARD_FREEZE_CANDIDATE`, not confirmed out-of-sample alpha.
- **Early Stage of Forward Validation:** As of September 13, 2026, only 12 days of the required 365-day forward validation period have elapsed.

## Implementation status

`not-implemented`. This record captures research and empirical evaluation from external public repository `Kairos-cryptoAI/kairos-backtest`. No implementation of `regime_aligned_right_tail_v1`, its cost hurdle, or its 4h SMA200 gate exists in our research repository, PyBroker, or NautilusTrader codebases.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- **Boundary Declaration:** This research record documents an empirical study on crypto perpetual right-tail trend following, macro regime gating, and pre-trade cost hurdles. It does not constitute strategy approval, does not authorize live or paper trading, and does not certify profitability.

## Related Wiki records

- `[[hyperliquid-vol-targeted-tsmom-drawdown-calibrated-ratchet-2026-09-12]]` — Volatility-targeted time-series momentum with drawdown-calibrated ratchet exits on Hyperliquid perpetuals.
- `[[crypto-smc-fvg-bpr-liquidity-retracement-random-walk-falsification-2026-09-12]]` — Empirical falsification of retail SMC/FVG retracement strategies across crypto timeframes.
- `[[crypto-bitcoin-cvar-risk-aware-q-learning-adaptive-controller-2026-09-02]]` — Risk-aware adaptive controller for crypto downside tail preservation.
- `[[gt-score-anti-overfitting-objective-multi-metric-gate-2026-09-05]]` — Multi-metric objective and anti-overfitting gate for trading strategy validation.
- `[[china-ashare-factor-library-overfitting-audit-amihud-illiquidity-falsification-2026-09-13]]` — Formulaic factor library overfitting audit and forward rotation falsification.

## Sources

1. **Primary GitHub Repository:** `TheLitis`, *Deterministic historical evaluation framework for Kairos strategies*, public GitHub repository `https://github.com/Kairos-cryptoAI/kairos-backtest`, immutable commit `758d1a383364726fe1f7b7ce8e9155f33da750bf` (September 13, 2026).
   - Core Strategy Contract: `https://github.com/Kairos-cryptoAI/kairos-backtest/blob/758d1a383364726fe1f7b7ce8e9155f33da750bf/STRATEGY_V2.md`
   - Regime Aligned Screen Implementation: `https://github.com/Kairos-cryptoAI/kairos-backtest/blob/758d1a383364726fe1f7b7ce8e9155f33da750bf/kairos_backtest/regime_aligned_screen.py`
   - Cost Hurdle & Sizing Engine: `https://github.com/Kairos-cryptoAI/kairos-backtest/blob/758d1a383364726fe1f7b7ce8e9155f33da750bf/kairos_backtest/cost_risk.py`
   - Execution Scenarios & Assumptions: `https://github.com/Kairos-cryptoAI/kairos-backtest/blob/758d1a383364726fe1f7b7ce8e9155f33da750bf/kairos_backtest/scenarios.py`
   - Regime Aligned Screen Report: `https://github.com/Kairos-cryptoAI/kairos-backtest/blob/758d1a383364726fe1f7b7ce8e9155f33da750bf/reports/regime-aligned-screen/REPORT.md`
   - Summary Metrics JSON: `https://github.com/Kairos-cryptoAI/kairos-backtest/blob/758d1a383364726fe1f7b7ce8e9155f33da750bf/reports/regime-aligned-screen/summary.json`
   - Forward Observation Ledger Warmup: `https://github.com/Kairos-cryptoAI/kairos-backtest/blob/758d1a383364726fe1f7b7ce8e9155f33da750bf/reports/regime-aligned-forward/WARMUP.md`
2. **Strategy Engine Dependency Repository:** `Kairos-cryptoAI`, *kairos-strategy-engine*, public GitHub repository `https://github.com/Kairos-cryptoAI/kairos-strategy-engine`, immutable commit `fb7d406c6e1a3060f481b91668ff3bc23a1b4b0d`.
   - Regime Aligned Right Tail Sleeve: `https://github.com/Kairos-cryptoAI/kairos-strategy-engine/blob/fb7d406c6e1a3060f481b91668ff3bc23a1b4b0d/kairos_strategy/sleeves/regime_aligned_right_tail.py`
   - Right Tail Trend Sleeve: `https://github.com/Kairos-cryptoAI/kairos-strategy-engine/blob/fb7d406c6e1a3060f481b91668ff3bc23a1b4b0d/kairos_strategy/sleeves/right_tail_trend.py`
