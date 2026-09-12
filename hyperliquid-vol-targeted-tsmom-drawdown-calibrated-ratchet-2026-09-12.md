---
schema: strategy-research-record-v1
title: "Hyperliquid Vol-Targeted Time-Series Momentum with Drawdown-Calibrated Leverage and Asymmetric Ratchet"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - hyperliquid
  - tsmom
  - time-series-momentum
  - volatility-targeting
  - perpetual-futures
  - crypto
status: research-only
confidence: medium
source_as_of: 2026-09-11
sources:
  - "https://github.com/SilvestriLorenzo/TSMOM-on-Hyperliquid/tree/a0f63cc2d7a4d3d9d516b4dd16ce8789e73a5c80"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Hyperliquid Vol-Targeted Time-Series Momentum with Drawdown-Calibrated Leverage and Asymmetric Ratchet

## Provenance

- **Primary Source:** Lorenzo Silvestri, `TSMOM-on-Hyperliquid`: "A vol-targeted time-series momentum (TSMOM) strategy for BTC/ETH/SOL perpetuals on Hyperliquid, built to pass and run on Propr funding challenges."
- **Repository URL:** [https://github.com/SilvestriLorenzo/TSMOM-on-Hyperliquid](https://github.com/SilvestriLorenzo/TSMOM-on-Hyperliquid)
- **Immutable Commit SHA:** `a0f63cc2d7a4d3d9d516b4dd16ce8789e73a5c80`
- **Key Source Paths:**
  - Strategy specification and research findings: [`README.md`](https://github.com/SilvestriLorenzo/TSMOM-on-Hyperliquid/blob/a0f63cc2d7a4d3d9d516b4dd16ce8789e73a5c80/README.md)
  - Core hypothesis & trailing stop backtester: [`research/tsmom_hypothesis.py`](https://github.com/SilvestriLorenzo/TSMOM-on-Hyperliquid/blob/a0f63cc2d7a4d3d9d516b4dd16ce8789e73a5c80/research/tsmom_hypothesis.py)
  - Walk-forward out-of-sample harness: [`research/tsmom_walkforward.py`](https://github.com/SilvestriLorenzo/TSMOM-on-Hyperliquid/blob/a0f63cc2d7a4d3d9d516b4dd16ce8789e73a5c80/research/tsmom_walkforward.py)
  - Analytical expected maximum drawdown calibration: [`research/mi_atiya_drawdown.py`](https://github.com/SilvestriLorenzo/TSMOM-on-Hyperliquid/blob/a0f63cc2d7a4d3d9d516b4dd16ce8789e73a5c80/research/mi_atiya_drawdown.py)
  - Path-dependent barrier simulation: [`research/tsmom_barrier_sim.py`](https://github.com/SilvestriLorenzo/TSMOM-on-Hyperliquid/blob/a0f63cc2d7a4d3d9d516b4dd16ce8789e73a5c80/research/tsmom_barrier_sim.py)
  - Multi-combo pooled portfolio barrier simulation: [`research/tsmom_joint_portfolio_barrier_sim.py`](https://github.com/SilvestriLorenzo/TSMOM-on-Hyperliquid/blob/a0f63cc2d7a4d3d9d516b4dd16ce8789e73a5c80/research/tsmom_joint_portfolio_barrier_sim.py)
- **Source As-Of Date:** 2026-09-11 (commit timestamp `2026-09-11T19:14:55Z`).
- **Data Universe & Horizon:** Historical candle data on Hyperliquid perpetuals for BTC, ETH, and SOL across 4h, 8h, and 12h intervals, with out-of-sample test overlap window of ~250 days.
- **Repository Deduplication Audit:** A full audit of all records in `alpha-strategy-research` confirmed zero matching records for `SilvestriLorenzo`, `TSMOM-on-Hyperliquid`, `Magdon-Ismail`, or `Propr`. Adjacent momentum records (`crypto-dynamic-time-series-momentum-volatility-impulse-2026-08-31.md`, `crypto-hyperliquid-momentum-funding-carry-combo-2026-09-12.md`) either evaluate multi-day academic momentum factors or cross-sectional ranking across 30 assets. None evaluate single-asset vol-targeted time-series momentum with Magdon-Ismail & Atiya analytic drawdown calibration and asymmetric trailing ratchet on Hyperliquid perpetuals.

## Economic mechanism

### Source-reported

The primary source establishes that time-series momentum (TSMOM)—taking long exposure following positive historical returns and short exposure following negative returns—exploits intermediate-term trend persistence in cryptocurrency perpetual markets. When applied at intermediate intraday-to-daily bar resolutions (4h, 8h, 12h), directional price changes continue over multiple subsequent bars due to order flow autocorrelation, leveraged participant liquidations, and retail chasing. 

However, raw unscaled momentum in crypto suffers from severe volatility clustering and heavy-tailed crash risk. To harvest trend beta while respecting strict drawdown constraints (such as proprietary evaluation barriers of +9% target vs. -3% static drawdown), the source proposes a tripartite architecture:
1. **Dynamic Volatility Targeting:** Sizing positions inversely proportional to trailing realized volatility normalizes risk across market regimes, dampening exposure during turbulent sell-offs and expanding exposure during low-volatility drifts.
2. **Asymmetric Trailing Ratchet Exit:** Using an Average True Range (ATR) trailing stop that ratchets strictly in favor of the position (never loosening) truncates adverse excursions while allowing winning trends to run without an arbitrary profit cap.
3. **Analytic Drawdown-Calibrated Leverage:** Rather than heuristically guessing account leverage, the leverage scalar $k$ is calibrated via Magdon-Ismail & Atiya's (2004) Brownian motion drawdown theorem to target an expected maximum drawdown equal to half the catastrophic loss barrier ($1.5\%$ target vs. $3.0\%$ barrier).
4. **Cross-Horizon Multi-Asset Pooling:** Combining four uncorrelated or imperfectly correlated (pairwise correlation $0.50$–$0.75$) asset-timeframe configurations on a single pooled account diversifies path-dependent risk, elevating barrier survival rates beyond any single asset in isolation.

### Research interpretation

The economic thesis represents a disciplined institutional adaptation of Moskowitz, Ooi, & Pedersen (2012) time-series momentum into a high-leverage crypto perpetual framework. 

The strategy operates as a composite hybrid system:
- **Directional Trend Core:** Positive feedback from market participants chasing breakouts and forced stop cascades in perpetual futures.
- **Volatility Sizing Filter:** Realized volatility dampening preventing position bloat during violent deleveraging cascades.
- **Asymmetric Exit Mechanism:** Right-skewed payoff generation via tight stop ratcheting, accepting a low win rate ($43\%$–$45\%$) compensated by substantial upside tail capture.
- **Portfolio-Level Diversification:** Exploitation of lead-lag and horizon divergence among large-cap crypto perpetuals (BTC, ETH, SOL) across 4h, 8h, and 12h frequencies.

## Signal

The trading logic is deterministic and fully specified in the primary codebase:

- **Signal Formation Timestamp (`source-reported`):** Evaluated at the boundary of each completed bar ($4\text{h}$, $8\text{h}$, or $12\text{h}$ UTC).
- **Causal Timing Discipline (`source-reported`):** All indicators (momentum sign, 20-bar realized volatility, 14-bar ATR) are computed strictly from data through bar $t-1$. No information from bar $t$ enters entry or sizing decisions.
- **Lookback Windows (`source-reported`):**
  - BTC 4h: $L = 1$ bar ($4\text{ hours}$)
  - ETH 8h: $L = 1$ bar ($8\text{ hours}$)
  - ETH 12h: $L = 1$ bar ($12\text{ hours}$)
  - SOL 12h: $L = 2$ bars ($24\text{ hours}$)
- **Entry Logic (`source-reported`):**
  - At the start of bar $t$, if currently flat ($\text{position} = 0$):
    - Compute momentum: $\text{mom}_t = \frac{\text{close}_{t-1} - \text{close}_{t-1-L}}{\text{close}_{t-1-L}}$.
    - If $\text{mom}_t > 0$, set position direction $\text{pos\_dir} = +1$ (long).
    - If $\text{mom}_t < 0$, set position direction $\text{pos\_dir} = -1$ (short).
    - If $\text{mom}_t = 0$ or any metric is NaN, remain flat.
- **Position Sizing Logic (`source-reported`):**
  - Trailing realized volatility is estimated from rolling 20 bars of log returns:
    $$\sigma_{\text{realized}, t} = \text{std}(\ln(1 + r)_{t-20:t-1})$$
  - Base target volatility per bar:
    $$\sigma_{\text{target\_bar}} = \frac{\sigma_{\text{target\_annual}}}{\sqrt{N_{\text{bars\_year}}}}$$
    where $\sigma_{\text{target\_annual}} = 0.20$ ($20\%$ annual target vol), and $N_{\text{bars\_year}} \in \{2190, 1095, 730\}$ for 4h, 8h, 12h bars respectively.
  - Sizing ratio:
    $$\text{pos\_size}_t = \min\left(\frac{\sigma_{\text{target\_bar}}}{\sigma_{\text{realized}, t}}, \text{cap}_{\text{coin}}\right) \times k$$
    where exchange leverage caps $\text{cap}_{\text{coin}}$ are $5.0$ for BTC, $5.0$ for ETH, and $2.0$ for SOL.
  - Leverage multiplier $k$ is calibrated via Magdon-Ismail & Atiya (2004) to target an expected maximum drawdown of $1.5\%$ over a 1095-day horizon:
    - BTC 4h: $k = 0.479$
    - ETH 8h: $k = 0.488$
    - ETH 12h: $k = 0.479$
    - SOL 12h: $k = 0.437$
- **Exit & Ratchet Logic (`source-reported`):**
  - True Range is computed over 14 bars:
    $$\text{TR}_t = \max(\text{high}_{t-1} - \text{low}_{t-1}, |\text{high}_{t-1} - \text{close}_{t-2}|, |\text{low}_{t-1} - \text{close}_{t-2}|)$$
    $$\text{ATR}_{14, t} = \text{rolling\_mean}(\text{TR}, 14)$$
  - Initial stop level set at entry:
    $$\text{stop\_level} = \text{close}_{t-1} - \text{pos\_dir} \times 2.5 \times \text{ATR}_{14, t}$$
  - Intrabar stop breach check: During bar $t$, if $\text{pos\_dir} = +1$ and $\text{low}_t \le \text{stop\_level}$, position is stopped out at $\text{exit\_px} = \text{stop\_level}$. If $\text{pos\_dir} = -1$ and $\text{high}_t \ge \text{stop\_level}$, position is stopped out at $\text{exit\_px} = \text{stop\_level}$.
  - Favorable-only ratchet update: If not stopped out, stop updates at close of bar $t$:
    - For Long: $\text{stop\_level}_{t+1} = \max(\text{stop\_level}_t, \text{close}_t - 2.5 \times \text{ATR}_{14, t+1})$
    - For Short: $\text{stop\_level}_{t+1} = \min(\text{stop\_level}_t, \text{close}_t + 2.5 \times \text{ATR}_{14, t+1})$
  - Take-profit: None (`source-reported`: capped take-profit was explicitly tested and eliminated due to severe negative alpha impact).
- **Portfolio Weighting (`source-reported`):**
  - The 4 locked combos run simultaneously on a single pooled account with equal quarter-allocation ($w_i = 0.25$ each).

## Required data

- **Instrument (`source-reported`):** BTC-PERP, ETH-PERP, SOL-PERP perpetual futures contracts.
- **Venue (`source-reported`):** Hyperliquid DEX.
- **Market Type (`source-reported`):** Perpetual futures (USDC-collateralized).
- **Timeframe (`source-reported`):** 4-hour, 8-hour, and 12-hour OHLC candle bars.
- **Fields (`source-reported`):** Timestamp, Open, High, Low, Close (candle data extracted from Hyperliquid public API and stored as JSON in `research/output/`).
- **Sample Period (`source-reported`):** Full multi-year historical dataset with a common chronological overlap window of ~250 days across all 4 out-of-sample combo test slices.
- **Point-in-Time Discipline (`source-reported`):** Strictly causal bar-by-bar processing; 70% chronological train slice used for parameter selection, 30% held-out test slice for OOS metrics.
- **Funding & Open Interest Needs (`research-proposed`):** Although Hyperliquid perpetuals settle funding hourly, the primary repository abstracts funding away into the net price return series. In live trading, historical 1h/8h funding rates must be tracked to verify funding drag does not erode trend gains.
- **Missing Data Handling (`research-proposed`):** Drop any candle with zero or NaN price; if a bar is missing, hold previous position and stop level without modifying leverage until valid OHLC prints resume.

## Execution assumptions

- **Order Type & Execution Timing (`source-reported`):** Limit or market taker orders. Entry occurs at the bar open price (assumed equal to prior bar close); stop-loss fills are executed intrabar at the exact stop level when the bar's High/Low breaches the threshold.
- **Transaction Costs (`source-reported`):** Flat $9.0\text{ bps}$ round-trip taker fee ($4.5\text{ bps}$ per side), verified against actual Hyperliquid L2 order book depth profiles.
- **Fill Model (`source-reported`):** Immediate fill at intrabar stop price upon breach. No queue delay or partial fills modeled in backtest.
- **Slippage & Market Impact (`source-reported`):** Stress tests in the repository validate that real L2 order book depth on Hyperliquid shifts total returns by less than $0.5\text{ percentage points}$ for account sizes up to $\$100,000$.
- **Account Capital & Evaluation Budget (`source-reported`):**
  - Simulated account size: $\$100,000$ USD.
  - Evaluation fee: $\$450$ one-time fee.
  - Profit target: $+9.0\%$ ($+\$9,000$).
  - Static drawdown floor: $-3.0\%$ ($-\$3,000$ from starting balance).
  - Daily loss floor: $-3.0\%$ from day start equity.
- **Margin & Leverage (`source-reported`):** Isolated margin per position bounded by exchange caps ($5\text{x}$ for BTC/ETH, $2\text{x}$ for SOL), with effective leverage constrained by the calibrated $k$ scalar ($k \approx 0.44$–$0.49$).
- **Funding Cost Treatment (`research-proposed`):** The primary source backtester omits funding payments; in live production, funding drag must be monitored, particularly when holding long positions during hyper-bullish funding spikes.

## Evidence

### Source-reported

All performance figures trace directly to Lorenzo Silvestri's repository (`SilvestriLorenzo/TSMOM-on-Hyperliquid`, commit `a0f63cc2d7a4d3d9d516b4dd16ce8789e73a5c80`, `README.md`, `research/tsmom_walkforward.py`, and `research/tsmom_joint_portfolio_barrier_sim.py`):

1. **Standalone Out-of-Sample Walk-Forward Results (70/30 Chronological Split):**
   - **BTC 4h ($L=1$, $k=0.479$):** Standalone OOS $P(\text{pass}) = 32.4\%$.
   - **ETH 8h ($L=1$, $k=0.488$):** Standalone OOS $P(\text{pass}) = 36.0\%$.
   - **ETH 12h ($L=1$, $k=0.479$):** Standalone OOS $P(\text{pass}) = 33.0\%$.
   - **SOL 12h ($L=2$, $k=0.437$):** Standalone OOS $P(\text{pass}) = 29.2\%$.
2. **Pooled Portfolio Results (4 Combos Quarter-Weighted on Single Account):**
   - **Evaluation Barrier Pass Probability ($P(\text{pass})$):** **$81.0\%$** full-sample (across 2,000 joint block-bootstrap simulations).
   - **Ex-Rally Robustness Pass Probability:** **$62.2\%$** when excluding the primary market rally episode.
   - **Annualized Sharpe Ratio:** **$2.07$** full-sample; **$1.09$** ex-rally episode.
   - **Cross-Combo Pairwise Daily Correlation:** Ranges between $0.50$ and $0.75$, demonstrating genuine cross-asset diversification.
   - **Trade-Level Distribution Diagnostics:**
     - Win rate: $43\%$ to $45\%$.
     - Median give-back ratio of peak unrealized gain: $119\%$ (the median trade that shows green closes as a small net loss due to trailing stop lag).
     - Gini concentration of winning trades: $0.58$ (standard trend-following right-skewed profile).
3. **External Reference Benchmark:**
   - Bui & Nguyen (arXiv:2602.11708) reported Sharpe $1.83$ and maximum drawdown $-16.1\%$ for a vol-scaled TSMOM baseline on Binance Futures (2022–2024), confirming the structural baseline validity of the mechanism.

### Independently reproduced

Not independently reproduced. All figures cited represent third-party empirical results published in `SilvestriLorenzo/TSMOM-on-Hyperliquid`. No independent reproduction has been run in our internal execution engine.

### Negative evidence

The repository provides explicit documentation of multiple ablated and rejected hypotheses:
1. **Capped Take-Profit:** Adding a fixed take-profit target or capping winning trades uniformly degraded out-of-sample Sharpe and pass rates. Trend following relies entirely on unconstrained right-tail winners.
2. **Directional Restrictions (Long-Only or Short-Only):** Restricting trades to one direction increased cross-asset correlation from $0.50$–$0.75$ up to $0.70$–$0.95$, destroying multi-asset diversification and severely reducing pooled pass probability.
3. **Cross-Asset Leader Signal:** Using BTC momentum to drive ETH and SOL entries (instead of computing independent momentum per asset) degraded pooled performance by inducing correlated simultaneous errors.
4. **Partial Profit-Taking (Scale-Outs):** Taking partial profits at favorable excursion thresholds normalized the trade distribution (lifting win rate above $50\%$), but significantly slowed capital progression toward the $+9\%$ evaluation barrier, resulting in strictly lower overall pass probability per unit time.

## Falsification plan

- **Test 1: Out-of-Sample Regime Decay (`research-defined falsification threshold`):**
  - *Data & Method:* Evaluate the pooled 4-combo strategy over rolling 180-day out-of-sample forward windows across both bull and bear markets on Hyperliquid.
  - *Metric & Threshold:* If net annualized Sharpe ratio drops below $0.35$ or total net return turns negative over any rolling 180-day period after deducting 9 bps round-trip fees, reject the short-to-medium-term momentum persistence hypothesis.
- **Test 2: Correlation Breakdown Stress Test (`research-defined falsification threshold`):**
  - *Data & Method:* Monitor the pairwise daily return correlation among BTC 4h, ETH 8h, ETH 12h, and SOL 12h during high-volatility market drawdowns.
  - *Metric & Threshold:* If the mean pairwise correlation exceeds $0.88$ over a 30-day window, causing pooled portfolio drawdown to breach $-2.5\%$, reject the multi-combo diversification hypothesis.
- **Test 3: Execution Cost & Slippage Friction Gate (`research-defined falsification threshold`):**
  - *Data & Method:* Simulate execution under tiered Hyperliquid fee schedules and stressed market depths (e.g. 15 bps round-trip taker fee + 5 bps adverse slippage on market orders).
  - *Metric & Threshold:* If doubling round-trip execution friction from 9 bps to 18 bps reduces pooled pass rate $P(\text{pass})$ below $50.0\%$, reject the operational viability of 4h taker-execution momentum.
- **Test 4: Trailing Stop Ablation Control (`research-defined falsification threshold`):**
  - *Data & Method:* Replace the ATR-14 2.5x ratchet stop with a naive fixed-time exit (holding exactly $L$ bars) and a fixed percentage stop (e.g. 2.0%).
  - *Metric & Threshold:* If the naive fixed-time exit achieves an identical or superior out-of-sample Sharpe ratio with comparable drawdown, reject the claim that the asymmetric ATR ratchet stop provides independent alpha.

## Crypto portability

- **Portability Status (`source-reported`):** Direct.
- **Venue & Contract Alignment:** The strategy was designed, backtested, and deployed specifically on crypto perpetual futures on Hyperliquid DEX.
- **Spot vs. Perpetual Considerations:** The strategy requires symmetric shorting capability with built-in leverage; executing on spot would incur borrow fees and asymmetric short availability.
- **24/7 Session Dynamics:** Crypto markets run continuously without weekend market closes. The 4h, 8h, and 12h candle boundaries partition continuous trading into discrete decision epochs.
- **Funding Rate Impact:** Perpetual futures require funding settlement (hourly on Hyperliquid). In high-momentum bull markets, funding rates can exceed $50\%$–$100\%$ APR annualized. While long momentum captures price appreciation, funding payments represent a continuous cash drag not fully isolated in the primary backtest.

## Limitations

- **Short Common Calendar Overlap (`source-reported`):** The joint multi-asset correlation structure and Monte Carlo barrier simulations are estimated from an overlapping test window of approximately 250 days across the 4 combos.
- **Omission of Funding Drag (`research-proposed`):** The backtest evaluates price returns net of taker fees, but omits explicit deduction of Hyperliquid's 1-hour funding rate settlements.
- **Taker Order Execution:** Strategy relies on taker orders at bar boundaries and stop triggers; elevated taker fees or market illiquidity during extreme flash crashes could induce adverse slippage beyond the modeled 9 bps.
- **Evaluation Barrier Specificity:** Sizing parameters ($k$) and portfolio pass probabilities are optimized against Propr's specific $+9\%$ profit target and $-3\%$ drawdown limits. Running on standard non-challenge capital requires recalibrating $k$ to conventional Kelly or volatility-budgeting criteria.

## Implementation status

- `not-implemented`: No implementation of Lorenzo Silvestri's Hyperliquid TSMOM system, Magdon-Ismail & Atiya drawdown calibrator, or ATR ratchet state machine exists in `alpha-strategy-research`, `nautilus-quant-system`, PyBroker, or NautilusTrader.
- This record serves strictly as a normalized research capture and hypothesis specification.

## Adoption boundary

- `research-only`: Research capture does not authorize deployment.
- `not-approved`: Not approved for live trading, paper trading, or capital allocation.
- A successful record entry indicates only that the research thesis meets normalization and auditability standards.

## Related Wiki records

- `crypto-hyperliquid-momentum-funding-carry-combo-2026-09-12.md`: Hyperliquid cross-sectional momentum and funding carry ranking across 30 assets.
- `crypto-dynamic-time-series-momentum-volatility-impulse-2026-08-31.md`: Academic analysis of crypto time-series momentum and volatility impulse (Borgards 2021).
- `hyperliquid-cex-cross-venue-funding-spread-carry-2026-09-03.md`: Cross-venue arbitrage on Hyperliquid perpetuals.
- `sp500-statistical-arbitrage-johansen-ou-ablation-multiple-testing-2026-09-12.md`: Methodological framework for walk-forward ablation and multiple testing controls.
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`: Core Hermes Wiki Brain methodology on causal validation and leakage prevention.

## Sources

1. **Primary Source Code Repository:**
   - Author: Lorenzo Silvestri
   - Repository: `https://github.com/SilvestriLorenzo/TSMOM-on-Hyperliquid`
   - Commit: `a0f63cc2d7a4d3d9d516b4dd16ce8789e73a5c80`
   - Files:
     - `README.md`: [`https://github.com/SilvestriLorenzo/TSMOM-on-Hyperliquid/blob/a0f63cc2d7a4d3d9d516b4dd16ce8789e73a5c80/README.md`](https://github.com/SilvestriLorenzo/TSMOM-on-Hyperliquid/blob/a0f63cc2d7a4d3d9d516b4dd16ce8789e73a5c80/README.md)
     - `research/tsmom_hypothesis.py`: [`https://github.com/SilvestriLorenzo/TSMOM-on-Hyperliquid/blob/a0f63cc2d7a4d3d9d516b4dd16ce8789e73a5c80/research/tsmom_hypothesis.py`](https://github.com/SilvestriLorenzo/TSMOM-on-Hyperliquid/blob/a0f63cc2d7a4d3d9d516b4dd16ce8789e73a5c80/research/tsmom_hypothesis.py)
     - `research/tsmom_walkforward.py`: [`https://github.com/SilvestriLorenzo/TSMOM-on-Hyperliquid/blob/a0f63cc2d7a4d3d9d516b4dd16ce8789e73a5c80/research/tsmom_walkforward.py`](https://github.com/SilvestriLorenzo/TSMOM-on-Hyperliquid/blob/a0f63cc2d7a4d3d9d516b4dd16ce8789e73a5c80/research/tsmom_walkforward.py)
     - `research/mi_atiya_drawdown.py`: [`https://github.com/SilvestriLorenzo/TSMOM-on-Hyperliquid/blob/a0f63cc2d7a4d3d9d516b4dd16ce8789e73a5c80/research/mi_atiya_drawdown.py`](https://github.com/SilvestriLorenzo/TSMOM-on-Hyperliquid/blob/a0f63cc2d7a4d3d9d516b4dd16ce8789e73a5c80/research/mi_atiya_drawdown.py)
     - `research/tsmom_barrier_sim.py`: [`https://github.com/SilvestriLorenzo/TSMOM-on-Hyperliquid/blob/a0f63cc2d7a4d3d9d516b4dd16ce8789e73a5c80/research/tsmom_barrier_sim.py`](https://github.com/SilvestriLorenzo/TSMOM-on-Hyperliquid/blob/a0f63cc2d7a4d3d9d516b4dd16ce8789e73a5c80/research/tsmom_barrier_sim.py)
     - `research/tsmom_joint_portfolio_barrier_sim.py`: [`https://github.com/SilvestriLorenzo/TSMOM-on-Hyperliquid/blob/a0f63cc2d7a4d3d9d516b4dd16ce8789e73a5c80/research/tsmom_joint_portfolio_barrier_sim.py`](https://github.com/SilvestriLorenzo/TSMOM-on-Hyperliquid/blob/a0f63cc2d7a4d3d9d516b4dd16ce8789e73a5c80/research/tsmom_joint_portfolio_barrier_sim.py)
2. **Foundational Methodological Citations:**
   - Malik Magdon-Ismail and Amir F. Atiya. "On the Maximum Drawdown of a Brownian Motion." *Journal of Applied Probability* 41, no. 1 (2004): 147–161. DOI: [10.1239/jap/1082552194](https://doi.org/10.1239/jap/1082552194).
   - Tobias J. Moskowitz, Yao Hua Ooi, and Lasse Heje Pedersen. "Time series momentum." *Journal of Financial Economics* 104, no. 2 (2012): 228–250. DOI: [10.1016/j.jfineco.2011.11.003](https://doi.org/10.1016/j.jfineco.2011.11.003).
   - Tri-Dung Bui and Bao-Ngoc Nguyen. "Volatility-scaled time series momentum on cryptocurrency futures." arXiv preprint arXiv:2602.11708 [q-fin.TR] (2026). Stable URL: [https://arxiv.org/abs/2602.11708](https://arxiv.org/abs/2602.11708).
