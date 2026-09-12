---
schema: strategy-research-record-v1
title: "Coinbase BTC-USD Order-Flow and Book Imbalance Online-SGD Microstructure Direction and Retail Taker Cost Falsification"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - microstructure
  - order-flow-imbalance
  - book-imbalance
  - online-learning
  - falsification
  - negative-evidence
  - retail-fee-drag
status: research-only
confidence: high
source_as_of: 2026-08-31
sources:
  - "https://github.com/jarvisss007/crypto-microstructure/tree/fe6267d39dd412b1a404ba61614fd41420ec4bab"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Coinbase BTC-USD Order-Flow and Book Imbalance Online-SGD Microstructure Direction and Retail Taker Cost Falsification

## Provenance

- **Primary Source Codebase:** Anupam Patil, *Crypto Microstructure Lab: Live crypto order-flow dashboard, self-learning 15-min forecaster, and an honest backtest harness* (`jarvisss007/crypto-microstructure`), Leo's Trading Firm, concluded August 17–31, 2026 (`source-reported`).
- **Canonical Source Identity:** GitHub repository `jarvisss007/crypto-microstructure` at immutable commit `fe6267d39dd412b1a404ba61614fd41420ec4bab`, dated 2026-09-12 17:04:05 UTC.
- **Repository URL:** [https://github.com/jarvisss007/crypto-microstructure](https://github.com/jarvisss007/crypto-microstructure)
- **Primary Source Research Files:**
  - `research/NULL_RESULT.md` — Formal null result writeup: *"Short-horizon crypto direction is not forecastable from this desk's features — a null result"* (Anupam Patil, Leo's Trading Firm, 2026-08-17, status: concluded).
  - `research/backtest_all.py` — Cumulative walk-forward sequential online SGD backtest engine over continuous recorded minute bars.
  - `research/horizon_sweep.py` — Pre-registered multi-horizon hypothesis sweep ($H \in \{1, 5, 10, 15\}$ minutes) with Bonferroni multiple-testing correction.
  - `research/learned_weights.json` — Fully trained online weight vector and complete out-of-sample skill/hit-rate/net-bps audit across 38 continuous recorded days (2026-07-05 through 2026-08-11).
  - `research/backtest.py` — Single-file microstructure validation harness evaluating Information Coefficient (IC), permutation test p-values, and cost-aware returns.
  - `research/exact_minute_study.py` — Point-forecast random-walk benchmark comparison.
  - `agent/minute_forecaster.py` — Desk ruling implementation under institutional rule CRYP-002 (2026-08-12) designating the instrument as a non-trading calibration device.
  - `forecast.html` & `index.html` — Live client-side WebSocket microstructure pipeline streaming Coinbase trades and Level-2 order book depth.
- **Underlying Instrument and Venue:** Bitcoin spot (`BTC-USD`) on Coinbase, streaming via Coinbase public WebSocket endpoints (`matches` trade channel and `level2_batch` order book channel).
- **Repository Deduplication Audit:** Audited all existing markdown records in `alpha-strategy-research`. Zero prior records cite `jarvisss007`, `Anupam Patil`, Leo's Trading Firm, commit `fe6267d`, or this continuous 38-day live-recorded online SGD order-flow study. Adjacent microstructure records in the repository evaluate different sources, asset classes, or mechanisms:
  - `order-flow-imbalance-predictive-decoupling-cost-falsification-2026-09-12.md` evaluates Tejas Mungale's C++ LOBSTER study on NASDAQ equities (INTC/GOOG) contrasting contemporaneous CKS OFI against static queue imbalance.
  - `retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11.md` evaluates Mykola-Quant's analysis of retail cumulative volume delta (CVD) divergence and funding rate extremes on crypto perpetuals.
  - `crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01.md` evaluates Pindza's cross-asset transferability across Binance spot and futures.
  - `crypto-smc-fvg-bpr-liquidity-retracement-random-walk-falsification-2026-09-12.md` evaluates haoyueOuo's random-walk control of Smart Money Concepts geometry.
  This record captures an independent, source-complete empirical falsification combining live forward prediction tracking, multi-horizon decay analysis, and metric tie-density correction.

## Economic mechanism

### Source-reported

1. **Microstructure Information Decay Hypothesis:**
   - Order-flow imbalance (buyer-initiated versus seller-initiated trade volume) and limit-order book imbalance (bid volume versus ask volume across the top 20 levels) reflect immediate inventory absorption and aggressive participant demand.
   - The primary source hypothesizes that order-flow and book-depth signals decay within seconds; hence, any directional predictability should concentrate at ultra-short horizons (such as 1 minute) and dissipate rapidly by 5 to 15 minutes.
2. **Adaptive Online Gradient Descent:**
   - Rather than fitting an offline static model prone to look-ahead bias and structural regime shifts, an online linear model with Stochastic Gradient Descent (SGD) and $L_2$ weight decay continuously adapts weights based strictly on past realized prediction errors.
   - The economic expectation is that if market microstructure features contain persistent alpha, online weights will maintain stable predictive signs; if features represent noise, weights will shrink toward zero without causing persistent directional bias.
3. **Retail Friction Decoupling:**
   - Even if high-frequency order flow carries statistically significant directional information at ultra-short intervals ($H = 1$ minute), retail exchange execution fees (e.g., Coinbase retail taker fee of 60 bps) impose a structural hurdle that exceeds the gross informational edge by multiple orders of magnitude.

### Research interpretation

The source documents a textbook structural breakdown between statistical significance and economic exploitability in crypto market microstructure:
- **Fast Information Dissipation:** Aggressive taker flow generates a localized, fleeting price impact that is fully incorporated into mid-prices within seconds. By the time a 1-minute bar closes, the residual drift available to a subsequent taker is infinitesimal (+0.051 bps gross).
- **Cost Multiplier on Ultra-Short Horizons:** Trading at 1-minute frequency implies up to 1,440 turnover cycles per day. Even with an edge that is statistically distinguishable from a random walk ($z = 5.21$), the 60 bps retail taker fee consumes $1,183\times$ the gross signal return per trade.
- **Metric Distortion via Flat-Bar Ties:** The source's methodological discovery regarding flat minute bars highlights a prevalent trap in high-frequency research: binary scoring that penalizes zero price changes ($\Delta P = 0$) manufactures artificial negative skill and spurious horizon trends due entirely to variation in tie density across timescales.

## Signal

### Mathematical Formulation

The strategy evaluates an online linear model producing a normalized return prediction $z_t \in [-4.0, 4.0]$ at each minute boundary $t$:

$$z_t = \text{clip}\left(w_t^T f_t, -4.0, 4.0\right)$$

where $f_t = [f_0, f_1, f_2, f_3, f_4, f_5]^T \in \mathbb{R}^6$ represents the standardized feature vector:
1. **$f_0$ (Bias):** Constant intercept term equal to $1.0$ (`source-reported`).
2. **$f_1$ (1-Minute Momentum):**
   $$r_{1, t} = \text{clip}\left(\frac{\ln(P_t / P_{t-1})}{\sigma_t}, -4.0, 4.0\right)$$
   where $P_t$ is the 1-minute close price (last mid-price from Level-2 snapshots) and $\sigma_t$ is the rolling 300-minute standard deviation of 1-minute log-returns (`source-reported`).
3. **$f_2$ (5-Minute Momentum):**
   $$r_{5, t} = \text{clip}\left(\frac{\ln(P_t / P_{t-5})}{\sigma_t \sqrt{5}}, -4.0, 4.0\right)$$
   set to $0.0$ if historical bar index $t < 5$ (`source-reported`).
4. **$f_3$ (15-Minute Mean-Reversion):**
   $$rev_{15, t} = \text{clip}\left(\frac{\ln(\bar{P}_{15, t} / P_t)}{\sigma_t \sqrt{15}}, -4.0, 4.0\right)$$
   where $\bar{P}_{15, t} = \frac{1}{15} \sum_{k=0}^{14} P_{t-k}$ is the trailing 15-minute moving average price (`source-reported`).
5. **$f_4$ (Order-Flow Imbalance, OFI):**
   Trailing 60-second volume-weighted aggressor flow imbalance evaluated strictly at the minute boundary:
   $$OFI_{60s, t} = \frac{\sum_{s \in [t-60s, t]} \left(V_{s}^{\text{buy}} - V_{s}^{\text{sell}}\right)}{\sum_{s \in [t-60s, t]} V_{s}^{\text{total}}}$$
   calculated from real-time execution matches (`source-reported`).
6. **$f_5$ (Book Imbalance, BI):**
   Instantaneous top-20 level depth imbalance at the minute boundary:
   $$BI_t = \frac{V_{\text{bid}}^{(20)} - V_{\text{ask}}^{(20)}}{V_{\text{bid}}^{(20)} + V_{\text{ask}}^{(20)}}$$
   calculated from Coinbase `level2_batch` order book snapshots (`source-reported`).

### Online SGD Update Rule

At horizon maturity $t + H$ ($H \in \{1, 5, 10, 15\}$ minutes):
- Actual normalized return:
  $$z_{\text{act}, t} = \text{clip}\left(\frac{\ln(P_{t+H} / P_t)}{\sigma_t \sqrt{H}}, -6.0, 6.0\right)$$
- Prediction error:
  $$err_t = z_t - z_{\text{act}, t}$$
- Weight vector update with learning rate $\eta = 0.002$ and $L_2$ weight decay $\lambda = 0.002$:
  $$w_{t+1} = w_t \cdot (1 - \eta \cdot \lambda) - \eta \cdot err_t \cdot f_t$$
  *(Note: An initial learning rate of $\eta = 0.02$ tested by the author allowed the model to wander into a confidently wrong state with skill $-0.60$ and hit rates $< 30\%$; shrinking $\eta$ to $0.002$ restored proper regularization, `source-reported`).*

### Directional Trade Trigger and Sizing

- **Predicted Return (bps):**
  $$\hat{r}_{\text{bps}, t} = z_t \cdot \sigma_t \sqrt{H} \times 10^4$$
- **Directional Position:**
  $$\text{pos}_t = \text{sign}(\hat{r}_{\text{bps}, t}) \in \{-1, 0, +1\}$$
  - Long if $\hat{r}_{\text{bps}, t} > 0$ (`source-reported`).
  - Short if $\hat{r}_{\text{bps}, t} < 0$ (`source-reported`).
  - Flat / no trade if $\hat{r}_{\text{bps}, t} = 0$ (`source-reported`).
- **Position Sizing:** Fixed unit position sizing of 1.0 contract without leverage or compounding (`source-reported`).
- **Alternative Maker Execution Adaptation:** Research-proposed overlay where quotes are posted at the bid/ask rather than paying taker fees; labeled `research-proposed` (not tested by the primary source).

## Required data

- **Instrument:** Bitcoin spot priced against USD (`BTC-USD`) (`source-reported`).
- **Venue:** Coinbase Advanced Trade / WebSocket API (`source-reported`).
- **Data Feeds:**
  - Public WebSocket `matches` channel: individual trade execution timestamp (ms), price, size, and taker side (`isBuy` boolean) (`source-reported`).
  - Public WebSocket `level2_batch` channel: 1-second order book depth snapshots providing aggregated bid/ask volume across the top 20 levels and top-of-book mid-price/spread (`source-reported`).
- **Derived Fields:**
  - 1-minute close prices (last recorded mid-price within each UTC minute) (`source-reported`).
  - 60-second trailing signed order-flow imbalance (`source-reported`).
  - Trailing 300-minute realized volatility $\sigma_t$ from 1-minute log returns (`source-reported`).
- **Point-in-Time Availability:** Full causal alignment. The feature vector $f_t$ uses only data timestamped $\le t$. Weights $w_t$ are updated only after the outcome at $t+H$ has fully transpired (`source-reported`).
- **Tie and Flat-Bar Handling:** Flat minute bars ($P_{t+H} = P_t$) and zero-prediction intervals ($\hat{r}_{\text{bps}} = 0$) are classified as non-scorable for directional hit-rate calculations (`source-reported`). Imputation of missing bars is forbidden; gaps are forward-filled (`source-reported`).

## Execution assumptions

- **Order Type:** Taker market orders executing immediately at the close of the observation minute (`source-reported`).
- **Signal-to-Order Latency:** Modeled as zero-latency instantaneous fill at mid-price (`source-reported`).
- **Transaction Costs (Baseline):** 60.0 bps per round-trip trade, reflecting Coinbase standard retail taker tier fee (`source-reported`).
- **Alternative Fee Scenarios:**
  - High-volume institutional taker fee: 5.0 bps (`research-proposed`).
  - Passive maker rebate / zero-fee tier: 0.0 bps or -1.0 bps (`research-proposed`).
- **Slippage and Impact:** Slippage assumed zero in the primary baseline; any non-zero slippage further deepens negative returns (`source-reported`).
- **Borrow and Shorting:** Unconstrained spot margin shorting assumed with zero borrow fee (`source-reported`).

## Evidence

### Source-reported

The primary source documents empirical results across three distinct experimental setups:

#### 1. Live Forward Out-of-Sample Forecasting (1-Minute Horizon)
Evaluated live in production with predictions logged and timestamped prior to observing outcomes:
- **Sample Period:** 6 UTC days in August 2026 (`source-reported`).
- **Sample Size:** 5,424 resolved out-of-sample forecasts (`source-reported`).
- **Direction Hit Rate:** 50.17% versus 47.94% base rate (statistically indistinguishable from a random coin toss; `source-reported`).
- **Brier Score:** 0.2539 versus 0.2500 climatological random-walk benchmark (`source-reported`).
- **Brier Skill Score:** **$-0.0154$**, negative on **every single individual UTC day** (daily skill sequence: $-0.0075$, $-0.0180$, $-0.0093$, $-0.0273$, ...; `source-reported`).

#### 2. Cumulative Walk-Forward Replay (38 Continuous Days, 15-Minute Horizon)
Sequential online SGD replay over unbroken 24/7 minute bars from 2026-07-05 through 2026-08-11:
- **Dataset Scale:** 53,346 minute bars; 53,311 resolved predictions (`source-reported`).
- **Scorable Sample:** 45,587 predictions (after excluding 7,724 ties; `source-reported`).
- **Base Rate Up:** 49.48% (0.494768) (`source-reported`).
- **Model Long Share:** 51.99% (0.519929) (`source-reported`).
- **Naive Base-Rate-Matched Null Hit Rate:** 49.98% (0.499791) (`source-reported`).
- **Realized Model Hit Rate:** **49.12%** (0.491193) (`source-reported`).
- **Directional Edge:** **$-0.86\text{ pp}$** ($-0.859881\text{ pp}$) with $z\text{-score} = \mathbf{-3.67}$ against the matched null (`source-reported`).
- **Overall Skill Score vs Random Walk:** **$-0.0313$** ($-0.031267$) (`source-reported`).
- **Gross Mean Return:** **$-0.19\text{ bps}$** per trade ($-0.194797\text{ bps}$) (`source-reported`).
- **Net Mean Return (60 bps Fee):** **$-60.19\text{ bps}$** per trade ($-60.194797\text{ bps}$) (`source-reported`).
- **Converged Model Weights ($H=15\text{m}$):**
  - Intercept (bias): $-0.049649$ (`source-reported`)
  - 1-min momentum: $+0.005950$ (`source-reported`)
  - 5-min momentum: $-0.009216$ (`source-reported`)
  - 15-min mean-reversion: $+0.095411$ (`source-reported`)
  - Order-flow imbalance (OFI): $-0.032730$ (`source-reported`)
  - Book depth imbalance (BI): $-0.115662$ (`source-reported`)

#### 3. Pre-Registered Multi-Horizon Hypothesis Sweep ($H \in \{1, 5, 10, 15\}$ Minutes)
Hypothesis tested: *"Order-flow signals decay in seconds; they matter far more on a 1-minute forecast than 15."*
Pre-declared pass bar: Skill $> 0.0$, Hit-rate $z \ge 2.50$ (Bonferroni-corrected for 4 tests), Net return $> 0.0\text{ bps}$.
- **1-Minute Horizon:**
  - Direction edge over base-rate null: **$+1.38\text{ pp}$**, $z = \mathbf{5.21}$ (statistically significant; clears Bonferroni bar $z \ge 2.50$; `source-reported`).
  - Gross return per trade: **$+0.051\text{ bps}$** (`source-reported`).
  - Taker fee: $60.0\text{ bps}$ (`source-reported`).
  - Net return per trade: **$-59.95\text{ bps}$** (`source-reported`).
  - Economic Ratio: The gross edge is approximately **$1/1,183\text{rd}$ of the retail taker fee** ($60 / 0.0507 \approx 1,183$; `source-reported`).
  - Source verdict: *"Significant, NOT tradeable"* (`source-reported`).
- **5-Minute, 10-Minute, and 15-Minute Horizons:**
  - All longer horizons exhibit negative direction edges, negative skill scores ($< 0$), and negative gross/net returns (`source-reported`).
  - Source verdict: *"No improvement"* (`source-reported`).

### Independently reproduced

Not independently reproduced. All figures reflect primary-source empirical logs and code execution outputs from `jarvisss007/crypto-microstructure` at commit `fe6267d39dd412b1a404ba61614fd41420ec4bab`.

### Negative evidence

1. **Systemic Negative Skill Across All Horizons:** Across 53,311 resolved predictions on continuous 38-day data, the online linear model underperforms a skill-free random-walk baseline (skill $-0.0313$).
2. **Persistent Daily Underperformance:** In live forward testing, Brier skill was strictly negative on 100% of individual UTC days tested, demonstrating that the failure is not an artifact of a single anomalous regime.
3. **Economic Decoupling of the 1-Minute Edge:** While a 1-minute direction edge exists statistically ($+1.38\text{ pp}$, $z=5.21$), its gross magnitude ($+0.051\text{ bps}$) is completely extinguished by transaction costs, requiring an unachievable $>1,100\times$ fee reduction to break even as a retail taker.
4. **Institutional Trading Prohibition (CRYP-002):** Concluded on 2026-08-12 by Leo's Trading Firm, ruling that the microstructure forecasting engine is permanently barred from deployment as an active trading strategy and restricted strictly to serving as a calibration and monitoring device.

## Falsification plan

To falsify the source's null result and demonstrate positive economic alpha from online crypto microstructure forecasting, an independent researcher must satisfy all of the following:

1. **Alternative Execution Venue and Fee Tier:**
   - Test the 1-minute OFI/BI signal on maker orders with negative fees (maker rebates of $-0.5$ to $-1.5\text{ bps}$) or institutional VIP taker tiers ($\le 1.5\text{ bps}$).
   - `research-defined falsification threshold`: Post-fee net return $> +1.0\text{ bps}$ per trade with annualized Sharpe $> 1.5$ after modeling realistic queue priority and adverse selection.
2. **Cross-Asset and Derivative Portability Test:**
   - Execute the identical 6-feature online SGD pipeline on Binance or Bybit BTC perpetual futures (`BTCUSDT`).
   - `research-defined falsification threshold`: Out-of-sample direction hit rate $> 52.0\%$ with $z > 3.0$ over $\ge 50,000$ consecutive minute bars.
3. **Adverse Selection and Fill Probability Audit:**
   - For passive limit orders, model fill probability conditioned on subsequent price moves. If fills occur predominantly when price moves against the quote (toxic flow), passive edge is falsified.
   - `research-defined falsification threshold`: Maker adverse selection penalty $< 0.5\text{ bps}$ over a 5-second post-fill window.
4. **Nonlinear Model Architecture:**
   - Test whether nonlinear models (e.g., GBDTs, MLPs, or temporal CNNs) extract higher gross edge from the same 6 features than the linear SGD formulation.
   - `research-defined falsification threshold`: Gross edge $> +5.0\text{ bps}$ per trade at $H=1\text{m}$.
5. **Action Upon Continued Failure:**
   - If gross edge remains $< 0.10\text{ bps}$ and net return under institutional costs remains negative, permanently uphold the CRYP-002 trading bar across all spot and perpetual venues.

## Crypto portability

- **Direct:** For spot Bitcoin on Coinbase (`BTC-USD`) (`source-reported`).
- **Adapted / Unproven:**
  - Crypto perpetual futures (`BTCUSDT` on Binance, Bybit, Hyperliquid): labeled `adapted/unproven`. Perpetual contracts feature funding rates, liquidation cascades, and tighter taker fee schedules ($1.5$ to $4.0\text{ bps}$), which could alter net economics; however, faster latency competition may exacerbate adverse selection.
  - Altcoin spot pairs (ETH, SOL, small-caps): labeled `adapted/unproven`. Wider bid-ask spreads on altcoins would further amplify taker cost drag unless compensated by dramatically higher predictability.
- **Portability Risks:**
  - 24/7 continuous trading requires uninterrupted WebSocket connection infrastructure and handling of exchange maintenance windows.
  - Fragmentation of order-flow across venues: Coinbase flow represents only a fraction of global crypto price discovery; Binance and Hyperliquid flow often leads Coinbase.

## Limitations

- **Single Venue Evidence:** Primary dataset is derived exclusively from Coinbase spot WebSocket feeds; findings may not reflect order-flow dynamics on high-leverage perpetual exchanges.
- **Retail Fee Assumption:** The primary economic rejection relies on Coinbase's 60 bps retail taker fee; institutional high-volume fee tiers were not empirically tested in the codebase.
- **Linear Feature Combination:** The model restricts interactions to a 6-parameter linear formulation; complex nonlinear cross-terms (e.g., interaction between OFI and spread width) were omitted.
- **Absence of Passive Maker Execution:** The backtester evaluates only taker execution; passive quoting with queue simulation was not implemented.
- **Not Independently Reproduced:** All reported metrics trace to author-provided backtest scripts and JSON/MD artifacts without third-party replication.

## Implementation status

Not implemented in the research stack. No PyBroker, NautilusTrader, Paper, Testnet, or Live execution has been conducted.

## Adoption boundary

This record is `research-only`, `not-implemented`, and `not-approved`. It documents a rigorous negative result and structural cost falsification. It does not authorize strategy adoption, live trading, paper trading, or testnet deployment.

## Related Wiki records

- `[[quant/retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11]]` — Microstructure falsification of cumulative volume delta (CVD) and retail order flow patterns on crypto perpetuals.
- `[[quant/order-flow-imbalance-predictive-decoupling-cost-falsification-2026-09-12.md]]` — Falsification of taker alpha from order flow imbalance on NASDAQ equity order books.
- `[[quant/crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01]]` — Microstructure alpha transferability and retail fee decay across Binance spot and futures.
- `[[quant/crypto-smc-fvg-bpr-liquidity-retracement-random-walk-falsification-2026-09-12]]` — Random-walk benchmark falsification of Smart Money Concepts retail order-flow patterns.

## Sources

1. Patil, Anupam. (2026). *Crypto Microstructure Lab: Live crypto order-flow dashboard, self-learning 15-min forecaster, and an honest backtest harness*. GitHub repository `jarvisss007/crypto-microstructure`, commit `fe6267d39dd412b1a404ba61614fd41420ec4bab` (2026-09-12). URL: https://github.com/jarvisss007/crypto-microstructure
2. Patil, Anupam. (2026-08-17). *Short-horizon crypto direction is not forecastable from this desk's features — a null result*. Technical Report `research/NULL_RESULT.md`, Leo's Trading Firm. URL: https://github.com/jarvisss007/crypto-microstructure/blob/fe6267d39dd412b1a404ba61614fd41420ec4bab/research/NULL_RESULT.md
3. Patil, Anupam. (2026-08-12). *Institutional Ruling CRYP-002: Unit definition and trading prohibition*. Technical implementation in `agent/minute_forecaster.py`. URL: https://github.com/jarvisss007/crypto-microstructure/blob/fe6267d39dd412b1a404ba61614fd41420ec4bab/agent/minute_forecaster.py
4. Patil, Anupam. (2026-08-12). *Pre-registered multi-horizon hypothesis sweep*. Script `research/horizon_sweep.py`. URL: https://github.com/jarvisss007/crypto-microstructure/blob/fe6267d39dd412b1a404ba61614fd41420ec4bab/research/horizon_sweep.py
5. Patil, Anupam. (2026-08-11). *Cumulative walk-forward online-SGD backtest over 38 continuous days*. Data and weights in `research/learned_weights.json` and script `research/backtest_all.py`. URL: https://github.com/jarvisss007/crypto-microstructure/blob/fe6267d39dd412b1a404ba61614fd41420ec4bab/research/learned_weights.json
