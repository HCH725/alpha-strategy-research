---
schema: strategy-research-record-v1
title: "Binance Spot Candle ML Extrema Timing Falsification: Predict-Then-Optimize Disconnect and Coverage Risk"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - negative-result
  - falsification
  - crypto
  - binance-spot
  - machine-learning
  - market-timing
  - predict-then-optimize
status: research-only
confidence: high
source_as_of: 2026-07-21
sources:
  - "arXiv:2607.19453v1 [cs.LG], July 21 2026. https://arxiv.org/abs/2607.19453"
  - "https://github.com/AyoubJadouli/Quantbot-Research-Framework"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Binance Spot Candle ML Extrema Timing Falsification: Predict-Then-Optimize Disconnect and Coverage Risk

## Provenance

- **Primary Source:** Ayoub Jadouli (Computer Science and Smart Systems, Faculty of Sciences and Technology, Abdelmalek Essaâdi University, Tangier, Morocco), *"Predictive Extrema, Unprofitable Policies: An AI-Assisted Audit of Candle-Based Binance Spot Timing Models"*, arXiv preprint `arXiv:2607.19453v1 [cs.LG]`, submitted July 21, 2026 (manuscript date July 20, 2026).
- **Canonical DOI:** [10.48550/arXiv.2607.19453](https://doi.org/10.48550/arXiv.2607.19453)
- **Stable Abstract URL:** [https://arxiv.org/abs/2607.19453](https://arxiv.org/abs/2607.19453)
- **Full Text HTML:** [https://arxiv.org/html/2607.19453v1](https://arxiv.org/html/2607.19453v1)
- **Companion Repository (Discovery):** `https://github.com/AyoubJadouli/Quantbot-Research-Framework`
- **Data Period Examined:**
  - Intraday mandatory-daily campaign: March 1, 2025 – July 19, 2026 (ten USDT pairs, 1-minute klines).
  - Intraday 5-minute local-extrema campaigns: March 3, 2025 – July 12, 2026 (BTCUSDT, ETHUSDT, SOLUSDT).
  - Paired daily extrema adaptation: June 1, 2021 – July 1, 2026 (BTCUSDT, ETHUSDT).
  - Monthly slow-rotation control: June 1, 2021 – July 1, 2026 (ten USDT pairs, 45 scored months October 2022 – June 2026).
- **Data Source:** Public Binance Spot REST API klines (`open`, `high`, `low`, `close`, `volume`, `quote_asset_volume`, `number_of_trades`, `taker_buy_base_asset_volume`, `taker_buy_quote_asset_volume`).

## Economic mechanism

### Source-reported

The primary source audits whether candle-based machine learning models that successfully predict rare cryptocurrency extrema (peaks and troughs) or short-horizon rank-outcomes can be converted into profitable executable spot trading policies after deducting realistic transaction costs.

The source investigates three structural hypotheses:
1. **Predict-then-optimize alignment hypothesis:** Models exhibiting high statistical discrimination (ROC AUC > 0.75 to 0.97) for retrospective local price extrema translate into positive trading policy returns when combined with causal post-extrema entry triggers and barrier exits.
2. **Temporal persistence hypothesis:** A frozen intraday selection model trained on historical klines retains positive economic edge during a subsequent, untouched prospective evaluation period without architectural retraining or retuning.
3. **Mandatory coverage hypothesis:** Imposing daily mandatory execution across a top-ranked crypto universe guarantees active market exposure without eroding the sparse edge discovered during unconstrained historical periods.

### Research interpretation

This paper presents a formal empirical falsification study demonstrating that:
- **Predictive accuracy does not equal decision value:** Classifiers can effectively distinguish completed local extrema from non-extrema in retrospective sample data (ROC AUC up to 0.974), yet fail completely in live policy simulation because entry must occur at the *next open* (after the extremum has already printed and partially rebounded). By the time an extremum is verified causally, the favorable entry price is exhausted, and subsequent price paths are dominated by unfavorable asymmetric barrier geometry (+60 gross bps target vs. -50 gross bps stop) and round-trip transaction costs.
- **Coverage destroys sparse edge:** Mandatory daily selection forces trading on days without genuine predictive signal. In the prospective 19-cycle July test, the mandatory selector compounded a -6.72% loss (15.79% win rate, -36.40 bps/cycle net mean), showing that lack of an abstention/cash mechanism accelerates account depletion.
- **Severe lookahead and leakage hazards in crypto ML:** The paper's forensic audit reveals that conventional holding-period evaluations often produce illusory out-of-sample alpha due to: (a) failure to purge forward-looking label horizons (e.g., 4-hour forward windows leaking across train/validation splits), (b) optimistic same-close fill assumptions that ignore execution latency, and (c) adaptive selection bias where dozens or hundreds of candidate model architectures consume the evaluation period.

## Signal

The paper analyzes four distinct experimental campaign signals on Binance Spot:

### 1. Mandatory-Daily Multi-Pair Selector (`source-reported`)
- **Universe (`source-reported`):** Ten high-liquidity USDT Spot pairs: ADA, AVAX, BNB, BTC, DOGE, ETH, SHIB, SOL, TRX, and XRP.
- **Data Timeframe (`source-reported`):** 1-minute OHLCV klines.
- **Formation / Decision Timestamp (`source-reported`):** Daily exactly after the 16:00 UTC bar completes (16:00:59 UTC).
- **Execution Timestamp (`source-reported`):** Next open at 16:01 UTC.
- **Model Architecture (`source-reported`):** Single ExtraTrees regressor trained to predict 4-hour realized net returns. Features include causal price location, multi-horizon returns, volume flow, and clock features.
- **Pair Selection (`source-reported`):** Ranks the ten pairs by predicted net return; unconditionally buys the top-ranked pair (mandatory 100% allocation, no abstention permitted).
- **Holding Period / Barriers (`source-reported`):**
  - Gross profit target: +100 bps (`source-reported`).
  - Gross stop-loss: -150 bps (`source-reported`).
  - Maximum holding horizon / Timeout: 240 1-minute bars (4 hours) (`source-reported`).
  - Exit price on timeout: Open of bar 241 (`source-reported`).
  - Intrabar tie resolution: Adverse stop-first assumption if both target and stop are crossed in the same bar (`source-reported`).

### 2. 5-Minute Causal Local Extrema Detector Policies (`source-reported`)
- **Universe (`source-reported`):** BTCUSDT, ETHUSDT, SOLUSDT.
- **Data Timeframe (`source-reported`):** 5-minute OHLCV klines; 48-bar causal lookback window ($T=4$ hours).
- **Extrema Target Construction (`source-reported`):**
  - Symmetric radius $b \in \{6, 12, 24\}$ bars (30, 60, or 120 minutes on each side); $b=24$ bars (120 minutes) was selected by validation scout (`source-reported`).
  - Minimum label: Bar $t$ low is the strictly lowest price across the centered $2b+1$ window ($t-b$ to $t+b$), AND the subsequent $b$ bars achieve a rebound of at least +40 bps (`source-reported`). Positive prevalence = 1.418% (`source-reported`).
  - Maximum label: Bar $t$ high is the strictly highest price across the centered $2b+1$ window, AND the subsequent $b$ bars achieve a pullback of at least -40 bps (`source-reported`). Positive prevalence = 1.603% (`source-reported`).
- **Policy Mechanics (`source-reported`):**
  - **Local-Minimum Policy:** Enters long from 100% cash at the next 5-minute open. Target: +60 gross bps; Stop: -50 gross bps; Timeout: 24 bars (2 hours) (`source-reported`).
  - **Local-Maximum Policy:** Sells an already-held Spot position to cash at the next 5-minute open, then repurchases at -60 gross bps target pullback, +50 gross bps adverse rebound stop, or 24-bar timeout. Evaluated as cash-cycle advantage vs. continuous holding (`source-reported`).
- **Models Audited (`source-reported`):** 14 model architectures per direction (28 total), including Attention CNN-LSTM (validation-selected), Logistic Regression, Histogram Gradient Boosting (HGB), Weighted Linear SVM, Random Forest, MLP, GRU Feature Boosting, LSTM, GRU, CNN-GRU, Gaussian Causal Bayes, CNN, Transformer, and PLR Attention CNN-LSTM.

### 3. Paired Daily Extrema Adaptation (`source-reported`, adapted from Gurgul et al. 2025)
- **Universe (`source-reported`):** BTCUSDT and ETHUSDT daily OHLCV.
- **Model (`source-reported`):** 14-day Histogram Gradient Boosting (HGB) proxy, calibrated with a 0.80 probability score threshold.
- **Policy (`source-reported`):** Two 50% capital sleeves starting in cash; long-only spot purchases on minimum signals at next daily open, sales to cash on maximum signals; no shorting or leverage; terminal liquidation on July 1, 2026.

### 4. Consumed Monthly Slow-Rotation Control (`source-reported`)
- **Universe (`source-reported`):** Ten USDT pairs (ADA, AVAX, BNB, BTC, DOGE, ETH, SHIB, SOL, TRX, XRP).
- **Logic (`source-reported`):** Cross-sectional momentum over 30/45/60/90/120-day horizons, scored across 240 candidate trailing policies with a 12-month past-only calibration window; rebalanced monthly at next open.

## Required data

- **Instruments (`source-reported`):** Binance Spot USDT trading pairs (BTCUSDT, ETHUSDT, SOLUSDT, ADAUSDT, AVAXUSDT, BNBUSDT, DOGEUSDT, SHIBUSDT, TRXUSDT, XRPUSDT).
- **Venue (`source-reported`):** Binance Spot exchange.
- **Market Type (`source-reported`):** Spot cash market (long-only, no margin borrow, no perpetual funding rates).
- **Timeframes (`source-reported`):** 1-minute, 5-minute, and 1-day OHLCV klines.
- **Fields (`source-reported`):** Timestamp, Open, High, Low, Close, Volume, Quote Asset Volume, Number of Trades, Taker Buy Base Asset Volume, Taker Buy Quote Asset Volume.
- **Point-in-Time & Purging Constraints (`source-reported`):**
  - Signal evaluation must use only completed klines.
  - Forward-looking labels spanning $H$ bars (e.g., 4 hours = 48 5-minute bars) must be purged across training, validation, and test split boundaries to eliminate label leakage (`source-reported`).
- **Missing Data Handling (`source-reported`):** Strict fail-closed policy. Missing klines or corrupted records must cause immediate cycle abort to `NO_TRADE`; no synthetic imputation permitted.

## Execution assumptions

- **Execution Timing (`source-reported`):** All actions enter at the next open price following candle close (e.g., 16:01:00 UTC open for decisions formed on the 16:00:00–16:00:59 UTC candle; next 5-minute open for 5-minute extrema).
- **Order Types (`source-reported`):** Modeled as market orders executed at the bar's open price.
- **Transaction Costs (`source-reported`):**
  - Baseline/Primary assumption: flat 31 bps (0.31%) round-trip / completed-cycle deduction (`source-reported`).
  - Stress testing levels: 20/21 bps lower-bound stress (approx. two 10 bps VIP-0 taker fee legs plus 1 bp buffer) and 51 bps upper-bound stress (`source-reported`).
  - Paired daily convention: 15.5 bps applied multiplicatively per executed side (entry, exit, terminal liquidation) (`source-reported`).
  - Rotation convention: 15.5 bps applied per unit of one-way portfolio turnover (`source-reported`).
- **Fill Model & Intrabar Ties (`source-reported`):**
  - Fills occur at exact barrier trigger prices if crossed within bar range $[Low, High]$.
  - Intrabar tie resolution: If both profit target and stop-loss price levels fall within the $[Low, High]$ range of the same bar, the simulator applies an adverse **stop-first** convention (`source-reported`).
- **Slippage, Spread & Market Impact (`source-reported`):** Unmodeled in source paper; flat fee deductions serve as a lower bound. Any execution in live markets would incur additional spread crossing, queue latency, and price impact (`source-reported`).
- **Operational Fill Model (`research-proposed`):** In live execution, limit orders pegged to the opening microsecond quote with immediate-or-cancel (IOC) fallback to market taker within 100ms; if market spread exceeds 5 bps, cancel and abstain (`research-proposed`).

## Evidence

### Source-reported

All empirical figures trace directly to Ayoub Jadouli (arXiv:2607.19453v1, Sections 5–7, Tables 2, 3, 4, 6, and Figures 2, 3, 4, 5):

#### 1. Mandatory-Daily Multi-Pair Selector (July 1–19, 2026 prospective evaluation)
- **Support:** 19 mandatory daily cycles (1 cycle/day).
- **Predecessor Search (`source-reported`):** Within-family candidate selected on Jan–Mar 2026 data; then at least 946 enumerated candidates across 8 campaign summaries evaluated on April–June 2026; least-negative candidate refit through June 30, 2026. Stored model SHA-256 hash: `484d501b...f2eae` (`source-reported`).
- **Performance at 31 bps primary cost (`source-reported`):**
  - Compounded portfolio return: **-6.72%** (-671.85 bps), compounding 100 USDT to 93.2815 USDT.
  - Win/Loss record: 3 wins, 16 losses (win rate = **15.79%**).
  - Net mean return: **-36.40 bps/cycle**.
  - Descriptive Clopper-Pearson 95% confidence interval on win rate: 3.4% to 39.6% (`source-reported`).
  - Disjoint prospective extension (July 8–19, 12 cycles): lost **-354.28 bps** with 3 wins, 9 losses (`source-reported`).
  - Daily cycle outcomes ranged from -134.75 bps to +69.00 bps (`source-reported`).
  - Asset concentration: TRXUSDT selected in 9 of 19 cycles, contributing -334.28 summed net bps (`source-reported`).
  - Sensitivity to cost: At 20 bps ended at 95.2579 USDT; at 51 bps ended at 89.7873 USDT (`source-reported`).

#### 2. 5-Minute Local Extrema Models (July 1–12, 2026 model-specific evaluation)
- **Support:** 10,293 held-out 5-minute bars per direction (146 positive minima, 165 positive maxima).
- **Validation-selected Local-Minimum Model (Attention CNN-LSTM) (`source-reported`):**
  - ROC AUC: 0.729
  - Average Precision (AP): 0.043 (vs. event prevalence 1.418%)
  - Precision / Recall: 0.10 / 0.04
  - Completed cycles: 9 (5 wins, 4 losses; 55.6% win rate)
  - Gross mean advantage: **+11.1 bps/cycle**
  - Net mean return (31 bps): **-19.9 bps/cycle**
  - Compounded return / Max Drawdown: **-1.79%** / 2.07%
  - Exact zero-return break-even cost: **10.9616 bps** (fails 21-bps floor)
- **Validation-selected Local-Maximum Model (Attention CNN-LSTM) (`source-reported`):**
  - ROC AUC: 0.750
  - Average Precision (AP): 0.053 (vs. event prevalence 1.603%)
  - Precision / Recall: 0.13 / 0.05
  - Completed cycles: 15 (8 wins, 7 losses; 53.3% win rate)
  - Gross mean advantage: **+12.2 bps/cycle**
  - Net mean return (31 bps): **-18.8 bps/cycle**
  - Compounded cash-cycle advantage vs. continuous holding / Max Drawdown: **-2.80%** / 2.91%
  - Exact zero-return break-even cost: **12.0690 bps** (fails 21-bps floor)
- **Post-hoc High-AUC Detector Diagnostics (`source-reported`):**
  - Logistic detector (minimum): ROC AUC = **0.973**, AP = **0.360**, but policy returned **-4.02%** over 15 cycles (gross mean +3.8 bps, net mean -27.2 bps).
  - Hist Gradient Boosting detector (maximum): ROC AUC = **0.969**, AP = **0.288**, but policy returned **-16.50%** over 45 cycles (gross mean -8.9 bps, net mean -39.9 bps).
  - Across all 28 evaluated models (14 per direction), **zero models** achieved a gross mean advantage exceeding the minimum 21-bps fee floor (`source-reported`).

#### 3. Paired Daily Extrema Adaptation (July 1, 2025 – June 30, 2026 evaluation)
- **Support:** 704 label-valid held-out symbol-days; 7 completed policy cycles (`source-reported`).
- **Predictive Metrics (`source-reported`):**
  - Minimum event: ROC AUC = 0.8742, AP = 0.1341 (prevalence 2.983%).
  - Maximum event: ROC AUC = 0.8962, AP = 0.1158 (prevalence 2.131%).
- **Trading Policy Performance at 31 bps (`source-reported`):**
  - Strategy compounded return: **-44.30%** (100 USDT to 55.70 USDT).
  - Cost-matched equal-weight BTC/ETH buy-and-hold benchmark: **-41.20%** (100 USDT to 58.80 USDT).
  - Strategy excess vs. benchmark: **-3.10 percentage points**.
  - Cycle win/loss: 1 win (+15.55%), 6 losses (worst: -29.56%).
  - Lowering cost to 21 bps changed return only to -44.10% (`source-reported`).

#### 4. Forensic Invalidation of Archival One4All Holdout (`source-reported`)
- Nominal 30-day "holdout" (May 24 – June 23, 2026) in an earlier 3-layer LSTM with 3,996 profile combinations was downgraded and invalidated due to:
  1. Overlapping evaluation dates previously used to guide architecture design;
  2. Unpurged 4-hour label horizon across split boundaries (leaking up to 48 5-minute bars);
  3. Optimistic same-close entry execution;
  4. Complete absence of underlying raw trade and summary directories, with earlier scripts silently using hardcoded summaries and synthetic plot fallbacks (`source-reported`).

#### 5. Consumed Slow-Rotation Control (`source-reported`)
- 45 scored months (Oct 2022 – Jun 2026) compounded to +313.01% at 31 bps vs. +78.69% for equal-weight hold.
- Disqualified from promotion: Extreme concentration where November 2024 alone gained +160.422%, supplying **67.48%** of total net log gain (removing November 2024 drops terminal wealth from 413.01 to 158.59 USDT); only 15 months were target-active; lack of prospective validation (`source-reported`).

### Independently reproduced

Not independently reproduced. All figures, metrics, parameters, and forensic audit results reflect the direct empirical reporting of Ayoub Jadouli (arXiv:2607.19453v1, July 2026).

### Negative evidence

The entirety of this study constitutes rigorous, multi-tiered negative evidence against candle-based extrema detection and mandatory daily crypto selection:
1. **Gross edge shortfall:** Even before deducting transaction fees, the gross cycle edge of the best validation-selected models was only +11.1 bps (minima) and +12.2 bps (maxima), failing to clear even the minimum possible exchange fee floor (21 bps) (`source-reported`).
2. **Break-even fee thresholds:** Zero-return break-even cost levels for observed cycles were 10.96 bps and 12.07 bps, confirming that the strategies are economically underwater under any retail or non-VIP Binance Spot fee tier (`source-reported`).
3. **Mandatory daily selection catastrophe:** Forcing daily exposure on an ExtraTrees pair-ranking regressor generated a 15.79% win rate and -6.72% loss over 19 cycles, confirming that mandatory coverage without an explicit cash/abstention threshold destroys capital (`source-reported`).
4. **Predictive-to-decision breakdown:** ROC AUCs as high as 0.969–0.973 failed to translate into positive policy returns, documenting a fundamental predict-then-optimize failure in high-frequency crypto pattern labeling (`source-reported`).

## Falsification plan

To falsify the primary negative conclusion (that candle-based ML extrema timing models cannot yield positive executable spot crypto policies after costs), any future candidate model must pass the following operational research battery:

1. **Pre-declared Selective Risk / Abstention Gate (`research-proposed`):**
   - Protocol: The model must evaluate a cash action with an explicit acceptance score threshold $q_{min}$ calibrated strictly on past-only walk-forward data.
   - Requirement: Coverage must be unconstrained (policy is allowed to abstain 100% of the time).
   - Failure metric (`research-defined falsification threshold`): If the policy cannot achieve positive net Sharpe ($Sharpe_{net} > 0.0$) and positive annualized return net of 31 bps costs over at least 50 trade cycles across an out-of-sample window of $\ge 6$ months, the hypothesis of exploitable extrema alpha is rejected.

2. **Gross Edge vs. Fee Clearance Test (`research-proposed`):**
   - Protocol: Compute the arithmetic gross mean cycle return before any fee deductions across all executed trades in out-of-sample data.
   - Failure metric (`research-defined falsification threshold`): If gross mean return $\le 25.0\text{ bps/cycle}$, the strategy is immediately rejected as economically unviable, as normal taker fees (20 bps) plus conservative slippage (5 bps) consume the entire edge.

3. **Strict Split-Boundary Purging & Embargo Audit (`research-proposed`):**
   - Protocol: For any target spanning $H$ future bars, purge exactly $H$ bars before and after each split boundary, and apply an additional $H$-bar embargo before test evaluation.
   - Failure metric (`research-defined falsification threshold`): If applying the $H$-bar purge causes the model's test Sharpe or ROC AUC to degrade by more than 20% relative to the unpurged split, the apparent edge is classified as label leakage artifact and rejected.

4. **Next-Open Execution Timing Verification (`research-proposed`):**
   - Protocol: Replace any same-close entry convention with next-bar open entry plus 1-bar execution delay.
   - Failure metric (`research-defined falsification threshold`): If net return drops below zero under next-open execution, the strategy is rejected as non-executable.

5. **Concentration & Single-Period Sensitivity Test (`research-proposed`):**
   - Protocol: Leave-one-out cross-validation across all active trading months/weeks.
   - Failure metric (`research-defined falsification threshold`): If omitting any single month reduces the cumulative net log return by $> 40\%$, the strategy is rejected as an artifact of a single outlier regime rather than systematic alpha.

## Crypto portability

- **Portability Status (`source-reported`):** Direct. The empirical experiments were designed, calibrated, and executed specifically on Binance Spot cryptocurrency klines.
- **Spot vs. Perpetual Nuances (`research-proposed`):**
  - The studied strategies operated strictly on Spot cash markets without margin borrow, meaning short exposure on local maxima could only be realized by selling an existing inventory to cash.
  - In crypto perpetual futures, shorting is native, but strategies become exposed to 8-hour funding rates, liquidation mechanics, and mark-to-index basis risk (`research-proposed`).
- **Session & Liquidity Characteristics (`source-reported`):**
  - Crypto operates 24/7/365 without exchange closes or market-on-close auctions, making same-close fills unexecutable without dedicated algorithmic execution slicing (`source-reported`).
  - Intrabar price discovery in crypto klines contains severe jump risks and adverse stop-first execution dynamics during volatility bursts (`source-reported`).

## Limitations

- **No Measured Microstructure Data (`source-reported`):** The study relies on 1-minute and 5-minute klines and does not model tick-level order book depth, queue priority, latency jitter, or realized bid-ask spread crossing costs (`source-reported`).
- **Flat Fee Assumption (`source-reported`):** The 31-bps primary cost is a synthetic uniform completed-cycle deduction rather than exchange-matched tiered fees (`source-reported`).
- **Sample Support (`source-reported`):** The prospective mandatory selector contains only 19 daily cycles; the selected local-extrema policies contain only 9 and 15 cycles; and the paired daily adaptation contains only 7 cycles. While small, the sample uniformly failed to demonstrate positive edge (`source-reported`).
- **Absence of Multimodal Data (`source-reported`):** The daily extrema adaptation used only OHLCV klines and did not incorporate on-chain metrics, order flow, or sentiment data present in the original Gurgul et al. (2025) study (`source-reported`).

## Implementation status

- `not-implemented`. This record captures negative empirical research from arXiv:2607.19453v1.
- No trading strategy, family, or operational pipeline has been created or modified in `nautilus-quant-system`, PyBroker, or NautilusTrader.
- All operational decisions across all audited families remain strictly `NO_TRADE`.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`
- This record serves as methodological and negative evidence warning against deploying candle-based ML extrema timing models and mandatory daily pair selectors without selective risk abstention, label purging, and next-open execution validation.
- It does not authorize paper trading, testnet deployment, or live capital allocation.

## Related Wiki records

- [[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]
- [[quant/backtest-overfitting-pbo-cscv-2026-08-27]]
- [[quant/phase8-financial-ml-sample-leakage-contract-2026-08-28]]
- [[quant/phase8-temporal-validation-calibration-uncertainty-2026-08-28]]

## Sources

1. Ayoub Jadouli (Computer Science and Smart Systems, Faculty of Sciences and Technology, Abdelmalek Essaâdi University, Tangier, Morocco), *"Predictive Extrema, Unprofitable Policies: An AI-Assisted Audit of Candle-Based Binance Spot Timing Models"*, arXiv preprint `arXiv:2607.19453v1 [cs.LG]`, submitted July 21, 2026 (manuscript dated July 20, 2026). DOI: [10.48550/arXiv.2607.19453](https://doi.org/10.48550/arXiv.2607.19453). Stable URL: [https://arxiv.org/abs/2607.19453](https://arxiv.org/abs/2607.19453). Full text HTML: [https://arxiv.org/html/2607.19453v1](https://arxiv.org/html/2607.19453v1).
2. Ayoub Jadouli, *Quantbot Research Framework: Simulation-only spot-crypto research repository*, GitHub repository: [https://github.com/AyoubJadouli/Quantbot-Research-Framework](https://github.com/AyoubJadouli/Quantbot-Research-Framework) (accessed 2026-07-20).
3. V. Gurgul, S. Lessmann, and W. K. Härdle, *"Deep learning and NLP in cryptocurrency forecasting: integrating financial, blockchain, and social media data"*, International Journal of Forecasting, Vol. 41, No. 4, pp. 1666–1695, 2025. DOI: [10.1016/j.ijforecast.2024.11.002](https://doi.org/10.1016/j.ijforecast.2024.11.002).
4. A. Bysik and R. Ślepaczuk, *"Machine learning-based bitcoin trading under transaction costs: evidence from walk-forward forecasting"*, arXiv preprint `arXiv:2606.00060v1 [q-fin.TR]`, June 2026. Stable URL: [https://arxiv.org/abs/2606.00060](https://arxiv.org/abs/2606.00060).
5. Binance Developer Documentation, *Spot REST API: kline/candlestick data*, [https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/market](https://developers.binance.com/en/docs/catalog/core-trading-spot-trading/api/rest-api/market) (accessed 2026-07-20).
