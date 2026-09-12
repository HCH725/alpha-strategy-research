---
schema: strategy-research-record-v1
title: "Crypto Pairs Trading: Cointegration Selection Data Snooping, In-Sample Overfitting, and Out-of-Sample Falsification"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - pairs-trading
  - cointegration
  - data-snooping
  - multiple-testing
  - crypto-spot
  - negative-evidence
status: research-only
confidence: medium
source_as_of: 2026-09-06
sources:
  - "https://github.com/rfukuda06/crypto-pairs-bot/tree/aa6fe8d741867cdf12ae00761d0cbab1a6ed536d"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Pairs Trading: Cointegration Selection Data Snooping, In-Sample Overfitting, and Out-of-Sample Falsification

## Provenance

- **Author:** rfukuda06
- **Repository URL:** https://github.com/rfukuda06/crypto-pairs-bot
- **Full Immutable Commit SHA:** `aa6fe8d741867cdf12ae00761d0cbab1a6ed536d`
- **Canonical Tree URL:** https://github.com/rfukuda06/crypto-pairs-bot/tree/aa6fe8d741867cdf12ae00761d0cbab1a6ed536d
- **Commit Date:** 2026-09-06T21:30:39Z
- **Primary Source Files Examined:**
  - `README.md` (project overview, empirical results, in-sample vs. out-of-sample comparison, Šidák multiple-testing correction analysis)
  - `config.yaml` (runtime parameters, data window, transaction fee, slippage, exposure, risk boundaries)
  - `src/pairsbot/strategy/pairs.py` (exact rolling spread z-score calculation, entry/exit signal state logic)
  - `src/pairsbot/research/screen.py` (Engle-Granger cointegration screening across $C(N, 2)$ pairs, OLS hedge ratio $\beta$, Šidák correction)
  - `src/pairsbot/research/split.py` (strict non-overlapping chronological in-sample / out-of-sample partition)
  - `src/pairsbot/research/optimize.py` (in-sample grid search across 144 parameter combinations)
  - `src/pairsbot/risk/manager.py` (dollar-neutral sizing, position flattening, peak-to-trough drawdown kill-switch)
  - `src/pairsbot/execution/broker.py` (`PaperBroker` execution model with fees and slippage; `LiveBroker` stub raising `NotImplementedError`)
  - `src/pairsbot/backtest/engine.py` (strict no-lookahead event loop with next-bar open fills)
  - `src/pairsbot/reporting/report.py` (annualized Sharpe with $\sqrt{8760}$ hourly factor, drawdown, and trade accounting)
  - `tests/test_no_lookahead.py` and `tests/test_split.py` (automated regression verification of no-lookahead invariants)

## Economic mechanism

### Source-reported

The author implements a classic statistical arbitrage pairs trading strategy in cryptocurrency spot markets. The stated premise is that two crypto assets whose log-price spread exhibits cointegration will tend to mean-revert over time. When the spread drifts significantly away from its historical equilibrium, a market-neutral position (long the undervalued coin, short the overvalued coin) is opened under the expectation that the spread will revert to its mean.

However, the primary contribution of the source repository is an empirical demonstration of strategy falsification:
1. **Data snooping in pair selection:** Screening across 55 candidate pairs ($C(11, 2)$) to identify the pair with the lowest Engle-Granger cointegration p-value ($p = 0.02166$ for LTC/XLM) yields a selection artifact. When adjusted via the Šidák multiple-testing correction, the p-value rises to $\approx 0.700$, indicating that apparent in-sample cointegration was largely a product of chance.
2. **In-sample parameter overfitting:** Optimizing entry, exit, stop-loss, and holding-period thresholds across 144 parameter sets produces seemingly attractive in-sample performance (+61.89% return, Sharpe 1.68), which completely collapses out-of-sample (-16.37% return, Sharpe -1.39).

### Research interpretation

The underlying economic thesis of pairs trading rests on common unobserved factor exposures and cross-asset substitution. In traditional equities, cointegration often reflects structural economic ties (e.g., dual-listed shares, royal parent-subsidiary structures, or close industry competitors with shared supply chains). In cryptocurrency spot markets, tokens such as LTC (Litecoin) and XLM (Stellar) do not share cash flows, business operations, or common structural settlement guarantees; their co-movement is driven primarily by macro liquidity and broad market beta.

Consequently, pairwise cointegration in crypto spot panels is frequently non-stationary, regime-dependent, or an empirical artifact of multiple hypothesis testing over short windows. When transaction costs (fees and slippage) are introduced alongside a strict next-bar execution rule, the pseudo-mean-reversion disappears, and the spread undergoes random walk drift or structural decoupling, triggering stop-losses or protracted drawdown.

**Component roles:**
- **Pair Selector:** Engle-Granger two-step cointegration screen selecting the lowest p-value pair in-sample (`source-reported`).
- **Hedge Ratio Estimator:** OLS static regression of $\ln(A)$ on $\ln(B)$ (`source-reported`).
- **Signal Generator:** Rolling 168-bar (7-day) z-score of the log-price spread (`source-reported`).
- **Entry Filter:** Divergence threshold ($|z| \ge 2.0$) (`source-reported`).
- **Exit Logic:** Multi-criteria exit consisting of mean-reversion ($|z| \le 0.5$), blow-out stop ($|z| \ge 3.5$), and maximum holding horizon (168 bars) (`source-reported`).
- **Risk Gate:** Maximum drawdown kill-switch blocking new entries once drawdown from peak reaches 20% (`source-reported`).

## Signal

### Formation timestamp
- Evaluated on closed 1-hour OHLCV bars (`timeframe: 1h`) (`source-reported`).
- Context at bar $t$ incorporates closes strictly up to and including bar $t$ (`closes.iloc[:t+1]`) (`source-reported`).
- Signal evaluated at bar $t$ close; executable orders generated for fill at bar $t+1$ open (`source-reported`).

### Lookback
- Cointegration screening and static OLS hedge ratio estimation: 540 days (12,960 hourly bars) in-sample (`source-reported`).
- Rolling spread normalization window: `z_window = 168` hourly bars (7 days) (`source-reported`).

### Spread and Z-Score Definition
- Log prices: $a_t = \ln(P_{A, t})$, $b_t = \ln(P_{B, t})$ (`source-reported`).
- Spread: $s_t = a_t - \beta \cdot b_t$, where $\beta = 0.2980$ (estimated via OLS on in-sample training window) (`source-reported`).
- Rolling window mean: $\mu_{t} = \frac{1}{168} \sum_{i=0}^{167} s_{t-i}$ (`source-reported`).
- Rolling window standard deviation: $\sigma_{t} = \sqrt{\frac{1}{168} \sum_{i=0}^{167} (s_{t-i} - \mu_t)^2}$ (`source-reported`).
- Z-score: $z_t = \frac{s_t - \mu_t}{\sigma_t}$ (if $\sigma_t == 0$, $z_t = 0.0$) (`source-reported`).

### Entry Logic
- **Long Spread (Long Asset A, Short Asset B):**
  - Trigger: $z_t \le -2.0$ (`entry_z = 2.0`) while flat and risk manager permits entry (`source-reported`).
  - Action: Generate buy order for Asset A and sell order for Asset B at bar $t+1$ open (`source-reported`).
- **Short Spread (Short Asset A, Long Asset B):**
  - Trigger: $z_t \ge +2.0$ while flat and risk manager permits entry (`source-reported`).
  - Action: Generate sell order for Asset A and buy order for Asset B at bar $t+1$ open (`source-reported`).

### Exit Logic
When in position, any of the following triggers immediately flattens both legs (`source-reported`):
1. **Mean Reversion:** $|z_t| \le 0.5$ (`exit_z = 0.5`) (`source-reported`).
2. **Stop Loss (Divergence Blowout):** $|z_t| \ge 3.5$ (`stop_z = 3.5`) (`source-reported`).
3. **Time Stop:** Holding duration $\ge 168$ hourly bars (`max_holding_bars = 168`) (`source-reported`).

### Position-Sizing Logic
- **Gross Exposure:** 50% of total portfolio equity (`gross_exposure_pct = 0.50`) (`source-reported`).
- **Leg Allocation:** Dollar-neutral sizing, allocating half of gross exposure to each leg (`source-reported`):
  $$\text{Notional}_A = \text{sign}_A \times \frac{\text{equity} \times \text{gross\_exposure\_pct}}{2} = \text{sign}_A \times (0.25 \times \text{equity})$$
  $$\text{Notional}_B = -\text{sign}_A \times \frac{\text{equity} \times \text{gross\_exposure\_pct}}{2} = -\text{sign}_A \times (0.25 \times \text{equity})$$
- Note: Dollar-neutrality means equal USD notional per leg, not $\beta$-adjusted risk parity or cointegration-vector shares (`source-reported`).

### Risk Management Kill-Switch
- Running peak equity $\text{Peak} = \max(\text{Peak}, \text{Equity}_t)$ (`source-reported`).
- Kill-switch activation threshold: $\text{Equity}_t \le \text{Peak} \times (1.0 - \text{max\_drawdown\_pct})$, where `max_drawdown_pct = 0.20` (20% drawdown) (`source-reported`).
- Behavior: Once triggered, new entries are blocked; portfolio remains flat for the remainder of the backtest (`source-reported`).

## Required data

- **Universe:** 11 major cryptocurrencies: `[ETH, SOL, AVAX, ADA, DOT, NEAR, BTC, LTC, XRP, LINK, XLM]` (`source-reported`).
- **Selected Pair:** LTC/XLM (identified as the lowest p-value pair in-sample) (`source-reported`).
- **Venue:** Bitstamp spot exchange (`exchange: bitstamp`) (`source-reported`).
- **Market Type:** Spot market (`quote: USD`) (`source-reported`).
- **Timeframe:** 1-hour OHLCV bars (`timeframe: 1h`) (`source-reported`).
- **Fields Required:** `open`, `high`, `low`, `close`, `volume` (`source-reported`).
- **Data Period:** Historical series starting `2024-01-01` (`source-reported`).
  - Total duration: 23,229 hourly bars (~967.8 days) (`source-reported`).
  - In-sample window: 12,960 hourly bars (540 calendar days) (`source-reported`).
  - Out-of-sample holdout: 10,269 hourly bars (~427.8 calendar days) (`source-reported`).
- **Point-in-Time Alignment:** Exact inner-join timestamps across assets; missing or misaligned bars dropped (`source-reported`).
- **Look-Ahead Protections:** Strictly verified via unit tests (`test_no_lookahead.py`), demonstrating that truncating bars after $t$ produces byte-identical equity paths up to bar $t$ (`source-reported`).

## Execution assumptions

- **Execution Timing:** Next-bar open execution (`source-reported`). Orders computed from bar $t$ close are filled at bar $t+1$ open.
- **Order Type:** Simulated market order crossing spread at open (`source-reported`).
- **Transaction Fees:** 0.10% per trade leg (`fee_pct = 0.001`), deducted directly from cash balance (`source-reported`).
- **Slippage Model:** 0.05% adverse price penalty per trade leg (`slippage_pct = 0.0005`) (`source-reported`):
  $$\text{Fill Price} = P_{\text{open}} \times (1 + \text{slippage\_pct}) \quad (\text{for buys})$$
  $$\text{Fill Price} = P_{\text{open}} \times (1 - \text{slippage\_pct}) \quad (\text{for shorts})$$
- **Total Round-Turn Friction per Leg:** 0.30% (two legs $\times$ [10 bps fee + 5 bps slippage] $\times$ round turn = 60 bps total spread round turn) (`source-reported` / `research-proposed` synthesis).
- **Starting Equity:** $\$10,000$ USD (`source-reported`).
- **Spot Shorting Assumption:** The source's `PaperBroker` simulates short sales by crediting notional cash and tracking negative quantity (`qty < 0`), marking value at $-qty \times P_t$. In live spot markets, shorting requires asset borrowing with daily borrow interest and margin requirements (`research-proposed`).
- **Borrow Cost / Margin Frictions:** Omitted from source simulation (`source-reported`).

## Evidence

### Source-reported

All figures below are directly reported by rfukuda06 (`crypto-pairs-bot`, commit `aa6fe8d741867cdf12ae00761d0cbab1a6ed536d`, September 2026):

#### 1. In-Sample Cointegration Screening and Data-Snooping Bias
- Screening universe: 11 crypto majors, yielding $C(11, 2) = 55$ pairwise regressions.
- Winning pair: **LTC/XLM**
- OLS Hedge Ratio: $\beta = 0.2980$
- Raw Engle-Granger Cointegration p-value: $p = 0.02166$ (passes nominal $\alpha = 0.05$ threshold).
- **Šidák Multiple-Testing Correction:**
  $$p_{\text{Šidák}} = 1 - (1 - p_{\text{raw}})^N = 1 - (1 - 0.02166)^{55} \approx 0.700$$
  The Šidák-adjusted p-value is $\approx 0.70$, indicating that the winning pair is statistically indistinguishable from a null distribution of independent random walks subjected to 55 trials.

#### 2. Default Configuration Backtest Results
- In-sample window: 12,960 bars (540 days); Out-of-sample window: 10,269 bars.
- Default parameters: `z_window=168`, `entry_z=2.0`, `exit_z=0.5`, `stop_z=3.5`, `max_holding_bars=168`.
- **Out-of-Sample Performance:**
  - Total Return: **-17.76%**
  - Annualized Sharpe Ratio: **-2.15** (annualized with $\sqrt{8760}$)
  - Final Equity: **$8,223.62** (from $10,000 initial cash)
  - Max Drawdown: **-20.97%**
  - Trade Fills: **268 fills**
  - Kill-Switch Status: Triggered at -20% drawdown, halting all subsequent trading.

#### 3. In-Sample Parameter Optimization Overfitting Collapse
The author performed a grid search over 144 parameter combinations on in-sample data:
- `entry_z` $\in [1.5, 2.0, 2.5, 3.0]$
- `exit_z` $\in [0.0, 0.25, 0.5, 1.0]$
- `stop_z` $\in [3.5, 4.0, 4.5]$
- `max_holding_bars` $\in [72, 168, 336]$
- Constraint: `exit_z < entry_z < stop_z`

| Configuration | In-Sample (12,960 bars) | Out-of-Sample (10,269 bars) |
|---|---|---|
| **Default Parameters** | (not tuned in-sample) | Return: **-17.76%**, Sharpe: **-2.15**, 268 fills |
| **In-Sample Tuned Best** | Return: **+61.89%**, Sharpe: **1.68** | Return: **-16.37%**, Sharpe: **-1.39**, 68 fills |

The source reports that across all 144 parameter combinations searched in-sample, the optimized parameters collapsed out-of-sample to a negative Sharpe (-1.39) and substantial drawdown (-16.37%), demonstrating that the in-sample optimization curve-fit noise rather than structural alpha.

### Independently reproduced

Not independently reproduced. All figures and performance metrics represent third-party reported findings from rfukuda06 (`crypto-pairs-bot`, commit `aa6fe8d741867cdf12ae00761d0cbab1a6ed536d`).

### Negative evidence

This repository is itself an explicit, code-backed negative result and falsification study for naive cointegration pairs trading in liquid cryptocurrencies:
1. **Selection Snooping:** A nominal p-value of 0.02166 across 55 tests translates to an effective false positive probability of 70% under family-wise error control.
2. **Post-Selection Drift:** The chosen pair (LTC/XLM) exhibited persistent divergence rather than mean-reversion during the out-of-sample holdout, bleeding capital until tripping the risk kill-switch.
3. **Overfitting Fragility:** Tuning entry/exit thresholds against in-sample history increased in-sample Sharpe from negative to 1.68, but failed completely out-of-sample (-1.39 Sharpe), confirming severe parameter hypersensitivity.
4. **Friction Drag:** Even with conservative retail fees (10 bps) and minimal slippage (5 bps), round-turn friction of 60 bps across two legs erodes marginal mean-reverting excursions.

## Falsification plan

To test whether cryptocurrency pairs trading can survive rigorous multiple-testing discipline or whether pairwise cointegration is universally spurious in crypto, the following operational tests are proposed:

1. **Family-Wise Error Rate / False Discovery Rate Control:**
   - Instead of selecting the minimum raw p-value, enforce a Benjamini-Hochberg FDR threshold ($q < 0.05$) or Šidák significance threshold ($p_{\text{Šidák}} < 0.05$) across all candidate pairs (`research-proposed`).
   - `research-defined falsification threshold`: If zero pairs in the 11-asset universe achieve $p_{\text{Šidák}} < 0.05$ over rolling 180-day or 360-day windows, reject the hypothesis that cointegration exists among crypto spot majors.

2. **Walk-Forward Cointegration Re-Estimation:**
   - Instead of freezing static $\beta$ and pair selection over a 540-day window, evaluate rolling or recursive cointegration tests every 30 days (`research-proposed`).
   - `research-defined falsification threshold`: If the estimated hedge ratio $\beta$ fluctuates by $> 50\%$ between consecutive months, classify the relationship as non-stationary structural shift rather than cointegration.

3. **Perpetual Contract Translation with Funding Cost Modeling:**
   - Port the pairs trading logic from spot (where shorting is borrow-constrained) to perpetual futures (where shorting is native) (`research-proposed`).
   - Account for cross-venue or cross-asset funding rate differentials:
     $$\text{Funding Drag} = \sum_{t} \left(\text{Pos}_{A, t} \cdot F_{A, t} + \text{Pos}_{B, t} \cdot F_{B, t}\right)$$
   - `research-defined falsification threshold`: If net funding rate divergence erodes $> 30\%$ of gross trading PnL, falsify funding-unaware pairs trading on perpetuals.

4. **Spread Volatility Targeting and Adaptive Sizing:**
   - Test whether replacing dollar-neutral sizing with volatility-adjusted inverse-beta sizing ($\text{Weight}_A / \text{Weight}_B = 1 / \beta$) stabilizes spread variance (`research-proposed`).
   - `research-defined falsification threshold`: If volatility-adjusted sizing fails to achieve positive out-of-sample Sharpe ($> 0.0$) after transaction costs, falsify sizing misspecification as the failure cause.

## Crypto portability

**Direct (Empirical Crypto Spot Context):**
- The primary source explicitly tests spot cryptocurrencies on Bitstamp (`ETH, SOL, AVAX, ADA, DOT, NEAR, BTC, LTC, XRP, LINK, XLM`).

**Crypto-Specific Structural Constraints and Adaptation Risks:**
- **Spot Shorting Mechanics:** Spot crypto markets do not permit native unbacked short selling. Implementing this strategy on spot requires margin accounts with borrow interest (often 5–20% annualized for altcoins) and collateral maintenance haircuts (`research-proposed`).
- **Perpetual Futures Adaptation (`adapted/unproven`):** Porting to USDT-margined or coin-margined perpetuals resolves spot borrow constraints, but introduces funding rate carry risk, liquidation buffers, and exchange maintenance margin differences (`research-proposed`).
- **Exchange Fragmentation and Fee Structures:** Bitstamp taker fees for retail are often 0.30%–0.40%, higher than the 0.10% assumed in the backtest. Taker execution on Binance/Bybit is typically 0.04%–0.05%, which would lower friction, but funding rate volatility on high-beta altcoins (XLM) frequently exceeds spot mean-reversion drift (`research-proposed`).
- **24/7 Liquidity Gaps:** Hourly bar boundaries are continuous, but liquidity depth varies strongly across Asian, European, and US trading sessions, causing time-varying slippage during volatile hours (`research-proposed`).

## Limitations

- **Single Pair In-Depth:** The out-of-sample backtest focuses on the single pair selected in-sample (LTC/XLM). Performance on other sub-threshold pairs is not evaluated out-of-sample in the source repository (`source-reported`).
- **Simplified Spot Shorting Model:** The execution engine simulates short sales without borrow fees, margin calls, or inventory borrowing availability (`source-reported`).
- **No Dynamic Hedge Ratio:** $\beta$ is estimated once statically over the 540-day in-sample period and held constant throughout the 427-day out-of-sample period (`source-reported`).
- **Fixed Lookback Window:** Spread rolling mean and standard deviation use a fixed 168-hour window without volatility adaptation (`source-reported`).
- **Not Independently Reproduced.**

## Implementation status

- **Status:** `not-implemented`.
- No implementation exists in NautilusTrader, PyBroker, paper trading, testnet, or production execution systems.
- This capture serves as a methodological benchmark and negative evidence case study on data-snooping corrections and in-sample parameter overfitting in crypto statistical arbitrage.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- This record captures a third-party open-source research artifact. Presence in this repository does not constitute approval for live trading, testnet trading, paper trading, or algorithmic implementation.

## Related Wiki records

- `[[quant/crypto-pairs-trading-copula-cointegration-2026-08-31]]` — Alternative non-linear copula approach to cointegrated crypto pairs on Binance futures.
- `[[quant/us-etf-pairs-trading-cointegration-cost-viability-falsification-2026-09-13]]` — Independent negative evidence record by Michael M. Ross documenting cointegration-cost anti-correlation in liquid US ETF pairs.
- `[[quant/sp500-pairs-trading-forensic-falsification-unbounded-beta-kalman-phantom-pnl-2026-09-12]]` — Falsification study analyzing Kalman filter unbounded beta and phantom PnL artifacts in pairs trading.
- `[[quant/crypto-statistical-arbitrage-pca-residual-cointegration-falsification-2026-09-12]]` — Falsification of PCA-residual OU mean reversion under transaction costs in crypto perpetuals.

## Sources

1. **Primary GitHub Source Repository:**
   - URL: https://github.com/rfukuda06/crypto-pairs-bot
   - Full Commit SHA: `aa6fe8d741867cdf12ae00761d0cbab1a6ed536d`
   - Tree URL: https://github.com/rfukuda06/crypto-pairs-bot/tree/aa6fe8d741867cdf12ae00761d0cbab1a6ed536d
   - Date: 2026-09-06T21:30:39Z
   - Author: rfukuda06 (`rfukuda06@gmail.com`)
2. **Primary Specification and Test Files:**
   - Strategy Implementation: `src/pairsbot/strategy/pairs.py`
   - Cointegration Screening and Šidák Formula: `src/pairsbot/research/screen.py`
   - In-Sample Grid Search: `src/pairsbot/research/optimize.py`
   - Chronological Partitioning: `src/pairsbot/research/split.py`
   - Risk Gate and Drawdown Kill-Switch: `src/pairsbot/risk/manager.py`
   - Execution Simulation: `src/pairsbot/execution/broker.py`
   - Event Loop and No-Lookahead Verification: `src/pairsbot/backtest/engine.py` and `tests/test_no_lookahead.py`
