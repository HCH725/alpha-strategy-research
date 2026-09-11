---
schema: strategy-research-record-v1
title: "Crowded-Position Flush Reversal: 5-Minute Microstructure Cascade Alpha on Binance Perpetual Futures with Purged Walk-Forward Parameter Optimization and Depth-Model Slippage"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetuals
  - microstructure
  - order-flow
  - liquidations
  - open-interest
  - funding-rate
  - mean-reversion
status: research-only
confidence: high
source_as_of: 2026-09-04
sources:
  - "Harshit Kumar (HarshitK2814), 'High-Frequency Crypto Perpetual Futures Strategy: Crowded-Position Flush Reversal', GitHub repository HarshitK2814/crypto-perp-hft-strategy (commit 4526669f73ac46a86d05c8028a96236c7fa228cb, September 2026)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crowded-Position Flush Reversal: 5-Minute Microstructure Cascade Alpha on Binance Perpetual Futures with Purged Walk-Forward Parameter Optimization and Depth-Model Slippage

## Provenance

- **Author / Research Lab:** Harshit Kumar (`HarshitK2814`), *High-Frequency Crypto Perpetual Futures Strategy Development*.
- **Public Repository:** `https://github.com/HarshitK2814/crypto-perp-hft-strategy`.
- **Immutable Commit SHA:** `4526669f73ac46a86d05c8028a96236c7fa228cb` (Date: 2026-09-06T20:19:09Z).
- **Inspected Primary Source Files:**
  - Executive Overview & Structure: `README.md`, `docs/00_OVERVIEW.md`.
  - Data Architecture & Survivorship Handling: `docs/01_DATA.md`.
  - Strategy Specification & Logic: `docs/02_STRATEGY_SPEC.md`.
  - Order-Book Depth & Cost Model: `docs/03_COST_MODEL.md`.
  - Validation Protocol, Leakage Audit & Multiple Testing: `docs/04_VALIDATION.md`.
  - Comprehensive Research Memo: `docs/05_MEMO.md`.
  - Structural Failure Modes: `docs/06_FAILURE_MODES.md`.
  - Production Deployment & Execution Guidelines: `docs/07_LIVE_DEPLOYMENT.md`.
  - Configuration Files: `config/strategy.yaml`, `config/costs.yaml`.
  - Empirical Summaries & Tables: `reports/summary.txt`, `reports/tables/acceptance_check.csv`, `reports/tables/cost_sensitivity.csv`, `reports/tables/conditioning_study.csv`, `reports/tables/signal_stability_by_year.csv`, `reports/tables/beta_diagnostics.csv`.
- **Source As-of Date:** September 4, 2026 (UTC data vintage pulled from Binance public vision archive).
- **Deduplication Audit:** Audited all 478 existing markdown records in `alpha-strategy-research`. Zero prior records cite `HarshitK2814`, `crypto-perp-hft-strategy`, or the four-quadrant price/open-interest cascade reversal model conditioned on funding persistence and volatility regimes with breakeven-stop ratchets.

## Economic mechanism

### Source-reported

The Crowded-Position Flush Reversal strategy exploits structural liquidity dislocations caused by automated liquidation cascades in cryptocurrency perpetual futures:

1. **Forced Deleveraging vs. Informed Flow:** In linear cryptocurrency derivatives, sharp price declines can stem either from informed sellers initiating short positions or from mechanical liquidation engines executing forced market sell orders on overleveraged long accounts. A decline driven by new short positioning *increases* aggregate open interest. Conversely, a sharp decline accompanied by a simultaneous *collapse* in open interest uniquely identifies forced liquidation, margin stop-outs, or panicked debt unwinds. Because liquidation orders are non-discretionary, price-insensitive market orders fired into an already thinning limit order book, price temporarily overshoots fundamental value.
2. **Funding-Rate Crowding as Pre-Condition:** Liquidations do not occur in a vacuum; they cluster where excessive leverage has accumulated on one side of the market. The strategy measures crowding via the conjunction of unusually elevated funding rates and persistent sign-consistency across rolling 8-hour settlements. When longs have paid high funding premiums over extended windows, the long book is structurally vulnerable to cascading margin calls.
3. **Volatility Regime Gating:** Liquidation cascades require sufficient market volatility to trigger chain-reaction margin breaches across exchange tier thresholds. In a low-volatility, quiet regime, small declines with declining open interest represent routine position closures rather than insolvency spirals; attempting to trade reversals in low-volatility regimes produces negative expectancy.
4. **Post-Cascade Reversion (Drift):** Once forced selling exhausts resting bid liquidity and the liquidation engine finishes unloading delinquent accounts, the artificial selling pressure abruptly vanishes. Natural market makers and non-urgent liquidity providers step in, driving a drift-like price recovery over the subsequent 8 to 12 hours.

### Research interpretation

The strategy captures a classic structural liquidity-provision risk premium in high-frequency crypto market microstructure:
- **Structural Asymmetry:** The source's empirical findings reveal a profound directional asymmetry: long reversals following downward flushes exhibit positive expectancy across diverse regimes, whereas the mirror-image short setup (fading an upward short squeeze) suffers catastrophic loss clustering on high-activity days. This stems from the structural upside drift of crypto assets, exchange liquidation mechanics (which liquidate long collateral denominated in declining margin currency faster than cash-secured shorts), and the unbounded left-tail risk of shorting explosive token rallies.
- **Microstructure Drift vs. Barrier Dynamics:** The source documents that reversion post-cascade behaves as an 8-to-12-hour continuous drift (+5 to +12 bps expected move per trade) rather than an instant barrier touch. Tight stop-loss or take-profit barriers truncate positive trajectories prematurely, turning an otherwise profitable statistical expectation negative. The wide-barrier structure with an armed breakeven-stop ratchet protects the left tail while allowing the trade to capture the underlying mean-reversion drift.
- **Macro Beta Confounding:** The source's beta diagnostics demonstrate that approximately 50% of the raw 16.0 bps edge constitutes directional market beta to Bitcoin (+8.0 bps excess-of-BTC edge, $t = 4.18$). The strategy acts as a systematic, microstructure-timed dip-buyer during broader market shakeouts.

## Signal

The signal operates causally on 5-minute bars across an active point-in-time universe of Binance USD-M perpetual contracts.

### 1. Feature Definitions (Computed strictly at bar close $t$, zero look-ahead)

- **1-Hour Price Shock Z-Score (`px_ret_z_12`):**
  $$\text{ret}_{1\text{h}, i, t} = \ln(P_{i, t}) - \ln(P_{i, t-12})$$
  $$\text{px\_ret\_z\_12}_{i, t} = \frac{\text{ret}_{1\text{h}, i, t} - \text{median}_{7\text{d}}(\text{ret}_{1\text{h}, i})}{\text{MAD}_{7\text{d}}(\text{ret}_{1\text{h}, i}) \times 1.4826}$$
  where the lookback window is 7 calendar days (2,016 five-minute bars).
- **1-Hour Open-Interest Change Z-Score (`oi_z_2d`):**
  $$\Delta \text{OI}_{1\text{h}, i, t} = \ln(\text{OI}_{i, t}) - \ln(\text{OI}_{i, t-12})$$
  $$\text{oi\_z\_2d}_{i, t} = \frac{\Delta \text{OI}_{1\text{h}, i, t} - \text{median}_{2\text{d}}(\Delta \text{OI}_{1\text{h}, i})}{\text{MAD}_{2\text{d}}(\Delta \text{OI}_{1\text{h}, i}) \times 1.4826}$$
  where the lookback window is 2 calendar days (576 five-minute bars). Open interest carries an explicit 1-bar publication lag to guarantee causal availability.
- **Funding Crowding Metric (`fund_crowding_long`):**
  $$\text{fund\_z\_7d}_{i, t} = \frac{F_{i, t} - \text{median}_{21\text{ settlements}}(F_i)}{\text{MAD}_{21\text{ settlements}}(F_i) \times 1.4826}$$
  $$\text{fund\_persistence}_{i, t} = \frac{1}{9} \sum_{k=0}^8 \text{sign}(F_{i, t-k})$$
  $$\text{fund\_crowding\_long}_{i, t} = \max(0, \text{fund\_z\_7d}_{i, t}) \times \max(0, \text{fund\_persistence}_{i, t})$$
  Evaluated across the trailing 21 settlements (7 days of 8-hour funding rates) and 9 settlements (3 days). Forward-filled causally from settlement timestamps.
- **Volatility Regime Z-Score (`vol_atr_z`):**
  $$\text{ATR}_{96, i, t} = \text{WilderATR}_{96}(\text{High}, \text{Low}, \text{Close})$$
  $$\text{vol\_ratio}_{i, t} = \ln\left(\frac{\text{ATR}_{96, i, t}}{P_{i, t}}\right)$$
  $$\text{vol\_atr\_z}_{i, t} = \frac{\text{vol\_ratio}_{i, t} - \text{median}_{7\text{d}}(\text{vol\_ratio}_i)}{\text{MAD}_{7\text{d}}(\text{vol\_ratio}_i) \times 1.4826}$$

### 2. Entry Conditions (Long Only)

At the close of bar $t$, a long entry order is generated for contract $i$ if **all** of the following conditions hold:
1. `px_ret_z_12[t] <= flush_ret_z` (Default: $-2.5$; walk-forward grid: $\{-3.0, -2.5, -2.0\}$).
2. `oi_z_2d[t] <= oi_drop_z` (Default: $-1.0$; walk-forward grid: $\{-1.5, -1.0\}$).
3. `fund_crowding_long[t] >= crowding_z` (Default: $0.25$; walk-forward grid: $\{0.0, 0.25, 0.5\}$).
4. `vol_atr_z[t] >= min_vol_z` (Default: $2.0$; walk-forward grid: $\{2.0\}$).
5. `tradable[t] == True` (Symbol is in the current month's point-in-time Top-20 liquidity universe).
6. Symbol is not currently held, and no signal was generated for symbol $i$ within `cooloff_bars` (Default: 24 bars = 2 hours).

### 3. Execution & Order Placement

- **Order Type:** Post-only maker limit order.
- **Price Reference:** Placed at `close[t] - limit_offset_atr * risk_unit` (Default: `limit_offset_atr = 0.05`).
- **Time-in-Force:** Order remains active for `entry_valid_bars = 6` bars (30 minutes) starting at $t+1$.
- **Fill Rule:** Requires a strict trade-through (`low < limit_price`), never a mere touch. A bar that gaps below the limit price fills at the bar Open. If unfilled after 6 bars, the order is cancelled and logged as an unfilled miss.

### 4. Position Sizing & Risk Units

- **Risk Unit Definition:** Volatility-scaled holding-horizon expected excursion:
  $$\text{risk\_unit}_{i, t} = \text{ATR}_{96, i, t} \times \sqrt{\text{vol\_horizon\_bars}} \quad (\text{vol\_horizon\_bars} = 144 \text{ bars} = 12\text{ hours})$$
- **Capital Allocation:** Fixed-fractional risk per trade sized off closed equity:
  $$\text{risk\_usd}_t = \text{risk\_per\_trade} \times \text{closed\_equity}_t \times \text{drawdown\_throttle}_t$$
  where `risk_per_trade = 0.0045` (0.45% of equity risked per trade).
- **Position Quantity:**
  $$\text{stop\_distance}_{i, t} = \text{stop\_atr} \times \text{risk\_unit}_{i, t} \quad (\text{stop\_atr} = 1.5)$$
  $$\text{qty}_{i, t} = \frac{\text{risk\_usd}_t}{\text{stop\_distance}_{i, t}}, \quad \text{notional}_{i, t} = \text{qty}_{i, t} \times P_{\text{entry}, i}$$

### 5. Risk Governor & Capacity Constraints

- **Drawdown Governor:**
  - If $\text{DD} \le 12\%$: Full position sizing ($\text{throttle} = 1.0$).
  - If $12\% < \text{DD} \le 17\%$: Linear scaling down to a $40\%$ floor ($\text{throttle} = 1.0 - 0.6 \times \frac{\text{DD} - 0.12}{0.17 - 0.12}$).
  - If $17\% < \text{DD} \le 19\%$: Held at $40\%$ floor ($\text{throttle} = 0.40$).
  - If $\text{DD} > 19\%$: Hard trading halt ($\text{throttle} = 0.0$), protecting the mandate's $20\%$ maximum drawdown ceiling.
- **Concentration & Leverage Limits:**
  - Maximum single-symbol notional: $\le 35\%$ of closed equity.
  - Maximum aggregate gross leverage: $\le 3.0\times$ closed equity.
  - Maximum concurrent positions: $\le 8$ active positions.
  - Order participation cap: $\le 15\%$ of resting notional within $\pm 1\%$ of mid-market order-book depth.
  - Minimum trade notional: $\$500.00$.

### 6. Exit Architecture & Breakeven-Stop Ratchet

- **Stop-Loss (Taker Market Order):**
  $$\text{StopPrice} = P_{\text{entry}} - \text{stop\_atr} \times \text{risk\_unit} \quad (\text{stop\_atr} \in \{1.2, 1.5\})$$
- **Take-Profit (Maker Limit Order):**
  $$\text{TargetPrice} = P_{\text{entry}} + \text{target\_atr} \times \text{risk\_unit} \quad (\text{target\_atr} \in \{2.2, 2.5\})$$
- **Time Stop (Taker Market Order at Close):**
  Exit at close of bar `entry_bar + time_stop_bars` (Default: 144 bars = 12 hours; grid includes 96 bars = 8 hours).
- **Breakeven-Stop Ratchet:**
  - Once unrealized favorable excursion reaches $\ge \text{breakeven\_trigger\_atr} \times \text{risk\_unit}$ (Grid: $\{90.0 \text{ (off)}, 0.35, 0.70\}$), the stop price moves to breakeven:
    $$\text{RatchetStopPrice} = P_{\text{entry}} + \text{breakeven\_buffer\_atr} \times \text{risk\_unit} \quad (\text{buffer} = 0.0)$$
  - *Conservative Timing:* The ratchet is evaluated after confirming the original stop was not hit, and takes effect only starting from the **subsequent** bar ($t+1$), never within the trigger bar.
- **Ambiguity Precedence Rule:** If a single 5-minute bar's range spans both the stop-loss and the take-profit price, the engine always resolves the **stop-loss** first (conservative execution assumption).

## Required data

- **Instruments:** Binance USD-M perpetual futures (`futures/um`).
- **Universe Selection:** Candidate pool formed by the union of active contracts and all historical symbol folders from the Binance archive (recovering 31 delisted contracts). Re-ranked monthly on the trailing 30-day median USD quote volume (shifted by 1 day to eliminate look-ahead). Top 20 contracts selected monthly, requiring listing history $\ge 92$ days and trailing 30-day median quote volume $\ge \$30,000,000$. Over the 44-month sample, the traded universe spanned **67 distinct symbols** with $\sim 24.8\%$ monthly turnover.
- **Data Feeds & Granularity:**
  - `klines` (5-minute): Open, High, Low, Close, Volume, Quote Volume, Trade Count, Taker-Buy Base Volume, Taker-Buy Quote Volume.
  - `fundingRate` (per settlement, 8-hour): Realized funding rates, timestamps.
  - `metrics` (5-minute): Aggregate Open Interest (units and USD), Top-Trader Long/Short Ratio (accounts and positions), Global Long/Short Ratio, Taker Long/Short Volume Ratio.
  - `bookDepth` (~30-second snapshots): Cumulative resting notional at $\pm 1\%, 2\%, 3\%, 4\%, 5\%$ of mid-price.
- **Point-in-Time Availability:** Klines stamped at bar close. Open interest metrics carry a 1-bar publication lag. Funding rates forward-filled from settlement timestamps. Missing data flagged and never interpolated.

## Execution assumptions

- **Transaction Costs (Mandated Baseline):**
  - Maker fee: $0.03\%$ (3.0 bps) per executed side.
  - Taker fee: $0.05\%$ (5.0 bps) per executed side.
- **Bid-Ask Spread Model:** Half of the Corwin-Schultz estimated effective spread charged on all taker fills; zero spread charged on maker fills.
- **Market Impact (Convex Depth Model):**
  - Derived from Binance `bookDepth` power-law fit: $N(x) = a \cdot x^b$, where $x$ is percentage distance from mid and $N$ is cumulative USD notional.
  - Volume-weighted average slippage:
    $$\text{slippage}(\%) = \left(\frac{b}{b+1}\right) \cdot \left(\frac{Q}{a}\right)^{1/b}$$
  - Empirical universe median curvature $b \approx 0.71$, confirming convexity in order size. For unobserved bars, $a$ is predicted via causal out-of-sample regression on log quote volume and log ATR ($R^2 = 0.954$).
  - Stress multiplier of $1.5\times$ applied to market impact on stop-loss executions during volatility outliers ($|z| > 2$).
- **Fill Timing:** Post-only maker limit orders placed at $t+1$ following signal generation at $t$ close.
- **Operational Classification:**
  - *Source-reported:* Taker fee 5 bps, maker fee 3 bps, Corwin-Schultz half-spread, power-law depth impact model, stop-wins ambiguity precedence, 3.0x leverage cap, 15% depth participation cap.
  - `research-proposed`: Execution engine deployment using WebSocket private order feeds on Binance AWS Tokyo infrastructure (`ap-northeast-1`); automated fallback to immediate taker market sweep if post-only cancel-replace latency exceeds 450 ms during high-urgency stop triggers.

## Evidence

### Source-reported

All empirical metrics below are extracted directly from primary source files (`reports/summary.txt`, `reports/tables/acceptance_check.csv`, `reports/tables/cost_sensitivity.csv`, `reports/tables/conditioning_study.csv`, `reports/tables/beta_diagnostics.csv`, `docs/05_MEMO.md` at commit `4526669f73ac46a86d05c8028a96236c7fa228cb`):

#### 1. Out-of-Sample Walk-Forward Headline Results (2024-01-01 to 2026-08-31, 32 Months, 11 Folds)
- **Evaluation Protocol:** 11 expanding walk-forward folds, 12-month minimum training window, 3-month test window, 48-hour (576 bars) purge + embargo gap. Parameters refit per fold from training data only and evaluated as a single continuous out-of-sample simulation.
- **Trade Frequency:** **41.9 trades/month** (1,329 total trades across 32 months; mandate $\ge 30$).
- **Net Maximum Drawdown (MTM):** **15.53%** (mandate $\le 20\%$).
- **Realized Reward:Risk Ratio (Mean Win / Mean Loss):** **1.38** (mandate $> 1.00$).
- **Reward:Risk Expectancy Basis:** **+0.0247 R** per trade (mandate $> 0$).
- **Profit Factor:** **1.14** (mandate $> 1.00$).
- **Net Profit After All Costs:** **+$131,654.49** (+13.17% net return on $1,000,000 initial capital).
- **Compound Annual Growth Rate (CAGR):** **4.75%**.
- **Annualized Sharpe Ratio:** **0.5239** (0.52).
- **Annualized Sortino Ratio:** **0.3284**.
- **Annualized Calmar Ratio:** **0.3058**.
- **Annualized Volatility:** **9.58%**.
- **Annual Portfolio Turnover:** **59.88x**.
- **Win Rate (Hit Ratio):** **45.2%** (demonstrating positive expectancy driven by payout asymmetry rather than win rate).
- **Average Holding Time:** **8.37 hours**.
- **Average Trade Notional:** **$60,129.57**.
- **Positive Fold Consistency:** **7 of 11 folds positive** (63.6%).
- **Exit Breakdown:** $73\%$ time stops, $19\%$ breakeven-ratchet exits, $7\%$ full stop-losses, $1\%$ profit targets.

#### 2. Cost Stack Breakdown & Drag Analysis
- **Gross PnL:** **+$227,162.89**
- **Total Friction Costs:** **-$95,508.40** (Total drag: **42.04% of gross profit**)
  - Exchange Fees: **-$63,763.80** (66.8% of cost)
  - Estimated Spread: **-$24,221.36** (25.4% of cost)
  - Market Impact (Depth Slippage): **-$4,158.77** (4.4% of cost)
  - Realized Funding: **-$3,364.47** (3.5% of cost)

#### 3. Statistical Significance & Multiple-Testing Adjustment
- **Configurations Evaluated in Search:** **2,376 trials** (11 folds $\times$ 216 grid points).
- **Probabilistic Sharpe Ratio (PSR vs. 0):** **0.7949** (79.5%).
- **Deflated Sharpe Ratio (DSR across 2,376 trials):** **0.2132** (21.3%).
- **Minimum Track Record Length (MinTRL for 95% confidence):** **3,878 days** ($\sim 10.6$ years).
- *Honest Reporting:* On the formal Deflated Sharpe Ratio metric, the 0.52 Sharpe is not statistically significant due to the 2,376-configuration search breadth; evidence rests on mechanical conditioning, ablation tests, and randomisation nulls.

#### 4. Randomization & Hypothesis Tests
- **Sign Randomization Null (Direction randomized, timing preserved, 40 runs):** Real Sharpe 1.46 vs. Null Mean +0.02 ($\sigma = 0.44$), rejecting null at **$p = 0.000$**.
- **Time-Shift Randomization Null (Direction preserved, timestamps jittered $\pm 1$ day):** Real Sharpe 1.46 vs. Null Mean +0.99, rejecting null at **$p = 0.000$**.

#### 5. Component Ablation Analysis (Shipped baseline parameters)
- **Full Model:** Sharpe 1.46, Expectancy +0.109 R, Net PnL +$172,111.
- **No Open-Interest Unwind Filter:** Sharpe 1.20, Expectancy +0.073 R, Net PnL +$159,982.
- **No Funding Crowding Filter:** Sharpe 0.87, Expectancy +0.039 R, Net PnL +$223,223 (trades rise to 38.1/mo, but Sharpe drops).
- **No Volatility Gate:** Sharpe **-0.88**, Expectancy **-0.036 R**, Net PnL **-$150,338** (confirms volatility regime is decisive).
- **Pure Technical Analysis (Price-only, stripping derivatives):** Sharpe **-0.39**, Expectancy **-0.017 R**, Net PnL **-$128,606** (Gross PnL +$471 on 315 trades/mo; completely erased by costs).
- **Derivatives Only (No price shock, trading OI + Funding + Vol):** Sharpe **1.24**, Expectancy **+0.085 R**, Net PnL **+$199,695** (demonstrates edge originates from derivatives positioning, not price pattern).

#### 6. Cost Stress Grid
- **Base Case:** Net Sharpe 1.46, Net PnL $172,111.
- **Slippage 2x:** Net Sharpe 1.45, Net PnL $171,314.
- **Slippage 4x:** Net Sharpe 1.44, Net PnL $169,725.
- **Funding 2x:** Net Sharpe 1.44, Net PnL $168,709.
- **All-Taker Fills (Forced taker entries):** Net Sharpe 1.40, Net PnL $162,320.
- **VIP-0 Higher Fees (5 bps maker / 5 bps taker):** Net Sharpe 1.43, Net PnL $167,850.
- **Slippage Multiplier Sweep:** System remains profitable up to $8\times$ baseline depth slippage ($+$166,560 net PnL).

### Independently reproduced

`Not independently reproduced.` The strategy has been validated via exhaustive line-by-line inspection of the public codebase, configurations, data manifests, and report logs; no independent replication in PyBroker or NautilusTrader has been conducted.

### Negative evidence

1. **Failure of Mirror-Image Short (Short-Squeeze Fade):** Fading upward rallies on collapsing open interest generated positive raw event-study means (+26.4 bps), but day-clustered analysis revealed extreme loss concentration on volatile squeeze days. Tested short implementations consistently failed.
2. **Failure of Sleeve 2 (Crowded-Book Fade):** An alternative short thesis (fading multi-day extreme open interest and positive funding during upward price extensions) failed all 32 tested walk-forward configurations net of execution costs.
3. **Pure Technical Analysis Failure:** A pure price-action version of the flush reversal generated zero gross edge (+$471 gross across 10,000+ trades) and severe net losses (-$128,606), demonstrating that technical price indicators alone cannot overcome crypto derivatives exchange fees.
4. **Calendar Year Instability in Unconditioned Signal:** The unconditioned price + open-interest signal produced negative forward returns in 2025 (-14.4 bps median return), proving that without the funding crowding and volatility regime gates, the effect is vulnerable to structural market competition.
5. **Drawdown Duration:** Longest drawdown duration reached 899 calendar days, reflecting extended low-volatility regimes where qualifying cascade events are infrequent.

## Falsification plan

The hypothesis that crowded long liquidation cascades provide tradeable post-event mean reversion will be considered falsified if:

1. **Cross-Exchange Portability Test:**
   - *Test:* Ingest 5-minute klines, open interest, and depth metrics from Bybit and OKX USD-M perpetuals across the identical 2023–2026 sample.
   - `research-defined falsification threshold`: If the strategy produces a negative net PnL or an annualized Sharpe ratio below $0.20$ net of standard exchange taker/maker fees on Bybit and OKX, the claim that the edge reflects universal liquidation microstructure rather than Binance-specific matching-engine idiosyncrasies is falsified.
2. **Deflated Sharpe Horizon Test:**
   - *Test:* Extend out-of-sample forward paper testing by an additional 12 months (minimum 400 new trades).
   - `research-defined falsification threshold`: If the cumulative realized Sharpe ratio over the extended out-of-sample period falls below $0.30$ or the Deflated Sharpe Ratio remains below $0.35$, the hypothesis of genuine edge is falsified in favor of data-mining across the 2,376 evaluated parameter combinations.
3. **Beta-Neutral Residual Alpha Audit:**
   - *Test:* Run the strategy with a continuous contemporaneous BTC beta hedge (shorting BTC perpetual contracts proportional to rolling 30-day realized beta).
   - `research-defined falsification threshold`: If the beta-hedged residual strategy produces a net Sharpe ratio $< 0.15$ or negative cumulative net PnL, the hypothesis that the edge constitutes microstructure liquidation reversion rather than directional beta timing is falsified.
4. **Execution Churn & Fill-Rate Decay Test:**
   - *Test:* Simulate execution under live WebSocket order feeds where resting post-only limits experience adverse fill selection (unfavorable fills executed, favorable fills missed).
   - `research-defined falsification threshold`: If the realized maker fill ratio drops below $35\%$ or net Sharpe decays below $0.25$ when incorporating 200 ms placement latency, the strategy is falsified as operationally unviable.

## Crypto portability

- **Portability Assessment:** `direct`.
- **Rationale:** The strategy is formulated natively on cryptocurrency market microstructure mechanisms (Binance USD-M perpetuals, funding rate settlements, and crypto exchange auto-liquidation engines).
- **Crypto-Specific Market Dynamics:**
  - *Perpetual Funding Rate Dynamics:* Funding rates settle periodically (typically every 8 hours on Binance/Bybit, hourly on dYdX, continuous on Deribit), directly measuring retail margin positioning imbalances.
  - *Automated Liquidation Engines:* Unlike traditional futures where margin calls allow intraday grace periods or broker negotiations, crypto perpetual exchanges execute automated, programmatic liquidation orders directly into the book once maintenance margin thresholds are crossed.
  - *24/7 Session Continuity:* Continuous trading prevents overnight gaps, but concentration of volume around US equity open and Asian session opens creates intraday volatility clusters.
  - *Collateral Devaluation Cascades:* In crypto markets, long margin calls often coincide with broader collateral liquidations across DeFi and cross-margined accounts, generating non-linear sell spirals.

## Limitations

- **Directional Limitation (Long Only):** The strategy operates strictly on the long side; in an extended multi-year secular bear market without sharp recovery bounces, the strategy will suffer sustained stagnation or drawdowns.
- **Search Breadth & Deflated Sharpe:** With 2,376 parameter configurations evaluated across the walk-forward grid, the Deflated Sharpe Ratio of 0.213 does not meet asymptotic statistical significance ($p < 0.05$), indicating a non-negligible probability that backtest profitability reflects selection bias.
- **Fee Tier Sensitivity:** Profitability relies heavily on maker execution on entries (paying 3.0 bps vs 5.0 bps taker fees). If adverse execution conditions force taker entry fills, net Sharpe declines.
- **Synthetic Liquidation Inference:** Due to the absence of public historical liquidation order archives on Binance, liquidations are inferred through open-interest and price co-movement rather than directly observed.
- **Capacity Constraint:** Orders are capped at 15% of resting depth within 1% of mid; scaling beyond $10M–$20M AUM will cause market impact to erode net margin on mid-cap perpetuals.

## Implementation status

`not-implemented`.
No implementation has been performed in `nautilus-quant-system`, PyBroker, or NautilusTrader. The strategy exists exclusively as an audited upstream research capture.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

This record is an upstream research capture. It does not constitute investment advice, quantitative validation, or authorization for live or paper trading execution.

## Related Wiki records

- `[[crypto-trend-atlas-causal-multi-speed-perpetual-portfolio-2026-09-12]]`
- `[[crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11]]`
- `[[crypto-funding-rate-mean-reversion-ema-taker-filter-2026-09-11]]`
- `[[crypto-quarter-hour-opening-order-imbalance-medium-horizon-2026-08-31]]`
- `[[retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11]]`

## Sources

- **Primary Source Codebase:** Harshit Kumar (`HarshitK2814`), *High-Frequency Crypto Perpetual Futures Strategy Development*, GitHub repository: `https://github.com/HarshitK2814/crypto-perp-hft-strategy`.
- **Immutable Commit SHA:** `4526669f73ac46a86d05c8028a96236c7fa228cb` (September 6, 2026).
- **Core Architecture & Specifications:**
  - Executive Brief: `README.md`.
  - Data Pipelines & Survivorship Audit: `docs/01_DATA.md`.
  - Formal Strategy Specification: `docs/02_STRATEGY_SPEC.md` (Sections 0–6).
  - Empirical Order-Book Depth & Cost Model: `docs/03_COST_MODEL.md` (Sections 1–2).
  - Validation Protocol & Leakage Controls: `docs/04_VALIDATION.md` (Sections 1–4).
  - Research Memo & Full Statistical Evidence: `docs/05_MEMO.md` (Sections 1–8).
  - Failure Modes & Mitigation: `docs/06_FAILURE_MODES.md`.
- **Machine Configurations:** `config/strategy.yaml` (portfolio constraints, parameter grids, risk parameters), `config/costs.yaml` (base cost model, sensitivity scenarios).
- **Primary Data Reports:**
  - Comprehensive Run Summary: `reports/summary.txt`.
  - Mandate Criteria Check: `reports/tables/acceptance_check.csv`.
  - Cost Stress Scenarios: `reports/tables/cost_sensitivity.csv`.
  - Factor Conditioning Analysis: `reports/tables/conditioning_study.csv`.
  - Regime Stability Breakdown: `reports/tables/signal_stability_by_year.csv`.
  - Directional Beta Diagnostics: `reports/tables/beta_diagnostics.csv`.
