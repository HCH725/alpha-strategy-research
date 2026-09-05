---
schema: strategy-research-record-v1
title: "Interpretable Hypothesis-Driven Trading: Walk-Forward Microstructure Pattern Bandit (Deep et al. 2025)"
created: 2026-09-06
updated: 2026-09-06
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - market-microstructure
  - hypothesis-driven
  - reinforcement-learning
  - contextual-bandit
  - walk-forward-validation
  - order-flow-imbalance
  - institutional-accumulation
status: research-only
confidence: medium
source_as_of: 2026-08-24
sources:
  - "Gagan Deep, Akash Deep, and William Lamptey. 'Interpretable Hypothesis-Driven Trading: A Rigorous Walk-Forward Validation Framework for Market Microstructure Signals', arXiv:2512.12924v1 [q-fin.TR, cs.LG], December 15, 2025 (revised August 24, 2026). https://arxiv.org/abs/2512.12924"
  - "Akash Deep. Official source repository: akashdeepo/Interpretable-Hypothesis-Driven-Trading, commit f2db15595845f1786461d9a2d9f7409ad76559b9 (July 8, 2026). https://github.com/akashdeepo/Interpretable-Hypothesis-Driven-Trading"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Interpretable Hypothesis-Driven Trading: Walk-Forward Microstructure Pattern Bandit

## Provenance

- **Primary Source Authors:** Gagan Deep (corresponding author, Department of Mathematics & Statistics, Texas Tech University; `gdeep@ttu.edu`), Akash Deep (Department of Mathematics & Statistics, Texas Tech University; `akash.deep@ttu.edu`), and William Lamptey (Department of Mathematics & Statistics, Texas Tech University; `wilampte@ttu.edu`).
- **Paper Title:** *"Interpretable Hypothesis-Driven Trading: A Rigorous Walk-Forward Validation Framework for Market Microstructure Signals"*
- **Canonical arXiv Identifier:** `arXiv:2512.12924v1 [q-fin.TR, cs.LG]`, submitted December 15, 2025; revised/formatted August 24, 2026.
- **Canonical URLs:**
  - Abstract: [https://arxiv.org/abs/2512.12924](https://arxiv.org/abs/2512.12924)
  - Full Text HTML: [https://arxiv.org/html/2512.12924v1](https://arxiv.org/html/2512.12924v1)
  - PDF: [https://arxiv.org/pdf/2512.12924](https://arxiv.org/pdf/2512.12924)
  - DOI: [10.48550/arXiv.2512.12924](https://doi.org/10.48550/arXiv.2512.12924)
- **Primary Source Code Repository:**
  - GitHub: [https://github.com/akashdeepo/Interpretable-Hypothesis-Driven-Trading](https://github.com/akashdeepo/Interpretable-Hypothesis-Driven-Trading)
  - Immutable Commit SHA: `f2db15595845f1786461d9a2d9f7409ad76559b9` (authored July 8, 2026).
  - Exact paths inspected: `hdt/config.py`, `hdt/hypothesis.py`, `hdt/features.py`, `hdt/agent.py`, `hdt/backtester.py`, `hdt/validation.py`, `src/summary_metrics.json`, `src/COMPREHENSIVE_REPORT.txt`, and result tables in `src/`.
- **Primary Source Verification:** The complete manuscript text, mathematical definitions (Definitions 1–9), equations ((1)–(18)), summary tables (Tables 1–17), and open-source Python implementation were directly inspected from arXiv and the author-published GitHub repository. No secondary search snippets, AI aggregator summaries, or marketing abstracts were used to infer rules or statistics.
- **Repository Deduplication Audit:** A full-text grep audit across `alpha-strategy-research` confirmed zero pre-existing records mentioning `arXiv:2512.12924`, Gagan Deep, Akash Deep, William Lamptey, or the `akashdeepo/Interpretable-Hypothesis-Driven-Trading` repository. Related records examine online LOB control (`market-making-online-lob-action-dependent-feedback-2026-09-02.md`) and PPO alpha weighting (`adaptive-alpha-weighting-ppo-llm-generated-alphas-2026-09-05.md`), but none address an interpretable rule-based hypothesis tuple architecture combined with an $\epsilon$-greedy multi-armed bandit allocator across 34 rolling out-of-sample walk-forward folds.

## Economic mechanism

### Source-reported

The paper addresses the quantitative finance replication crisis (overfitting, multiple testing bias, lookahead bias, and black-box uninterpretability) by formulating an end-to-end framework where trading decisions must be grounded in explicit, auditable economic hypotheses:

1. **Market Microstructure Information in Aggregated Daily OHLCV:** High-frequency microstructure concepts—specifically order-flow imbalance and institutional inventory accumulation—leave observable footprints in daily price and volume relations. When informed institutional traders accumulate positions, they attempt to minimize market impact by splitting orders over multiple sessions. This manifests as elevated volume accompanied by pronounced positive volume imbalance without commensurate price movement (`institutional accumulation`). Conversely, when aggressive demand pushes prices rapidly with confirming volume and high price efficiency, trend continuation is favored (`flow momentum`).
2. **Context-Conditioned Strategy Activation:** Different behavioral and structural phenomena dominate under different macro volatility regimes. In stable, low-volatility regimes, temporary price displacements away from central tendencies reflect liquidity-provision imbalances rather than fundamental repricing, creating mean-reversion and range-bound value opportunities (`mean reversion`, `range-bound value`). Under volatile regimes, order flow and directional breakouts dominate.
3. **Adaptive Hypothesis Selection via Reinforcement Learning:** Rather than hard-coding static weights or fitting high-capacity deep neural networks that overfit historical noise, an $\epsilon$-greedy bandit learner dynamically tracks the rolling empirical win rate and return of each discrete hypothesis type, allocating execution capital toward hypothesis types that currently demonstrate statistical edge in the prevailing market state while pruning decay.

### Research interpretation

The framework is structured as a hierarchical four-layer alpha engine:

```text
Layer 1 (Feature Engine): 54 technical, volume, and daily microstructure features (Kyle-type price impact, volume imbalance, price efficiency)
Layer 2 (Hypothesis Generators): 5 prioritized rule-based generators outputting structured tuples: h = (s, a, θ, ℓ, c, x, r*, δ*)
Layer 3 (Meta-Selector / RL Bandit): Epsilon-greedy multi-armed bandit gating execution based on learned historical win rate vs. confidence threshold
Layer 4 (Execution & Portfolio Risk): 5-position equal-dollar portfolio, 20% max position, 50% max sector, triple exit (target, stop-loss, 30-day time-stop)
```

The core falsifiable alpha hypothesis is that daily volume-imbalance proxies for order-flow pressure contain directional predictive power, but this edge is regime-conditional—concentrated during elevated volatility and rapid information arrival—and is degraded by transaction costs during quiet, low-volatility regimes.

## Signal

The signal architecture translates 54 daily engineered features into structured hypothesis tuples and filters them through an adaptive bandit policy:

### 1. Daily Feature Extraction
Let daily bars be $P_t^s = (O_t^s, H_t^s, L_t^s, C_t^s, V_t^s)$ for security $s \in \mathcal{S}$ at day $t$.
Key microstructure and technical features (`source-reported`):
- **Volume Imbalance (5-day rolling, Equation (3)):**
  $$\text{VolumeImbalance}_t^s = \frac{\sum_{\tau=t-4}^t V_\tau^s \cdot \mathbb{1}(C_\tau^s > O_\tau^s) - \sum_{\tau=t-4}^t V_\tau^s \cdot \mathbb{1}(C_\tau^s < O_\tau^s)}{\sum_{\tau=t-4}^t V_\tau^s + 10^{-6}}$$
- **Volume Ratio (Equation (4)):**
  $$\text{VolumeRatio}_t^s = \frac{V_t^s}{\frac{1}{20}\sum_{\tau=t-19}^t V_\tau^s}$$
- **Price Efficiency (10-day Kaufman/directional efficiency, Equation (5)):**
  $$\text{PriceEfficiency}_t^s = \frac{\left|\sum_{\tau=t-9}^t r_\tau^s\right|}{\sum_{\tau=t-9}^t |r_\tau^s| + 10^{-6}}$$
- **Market Regime Classifier:**
  - Let $\text{Trend}_t = (C_t - \text{SMA}_{50,t}) / \text{SMA}_{50,t}$ and $\text{VolRatio}_t = \sigma_{20d,t} / \text{MA}_{60}(\sigma_{20d,t})$.
  - If $\text{VolRatio}_t > 1.5$: Regime = `VOLATILE`
  - Else if $|\text{Trend}_t| < 0.02$: Regime = `STABLE`
  - Else if $\text{Trend}_t > 0.05$: Regime = `TRENDING_UP`
  - Else: Regime = `TRENDING_DOWN`

### 2. Five Discrete Hypothesis Generators (Evaluated in Priority Order)
At day $t$ close, for each security $s$ with $\ge 60$ historical bars, the master generator evaluates five rule sets sequentially; the first matching rule emits hypothesis $h = (s, a, \theta, \ell, c, \mathbf{x}, r^*, \delta^*)$ (`source-reported`):

1. **Type 1: Institutional Accumulation ($\theta = \text{institutional\_accumulation}$):**
   - *Conditions:* $\text{VolumeImbalance} > 0.30 \land \text{VolumeRatio} > 1.5 \land |\text{Return}_{20d}| < 0.10$
   - *Action:* `buy`
   - *Parameters:* Confidence $c = 0.75$, Target return $r^* = 0.08$ (+8%), Stop-loss $\delta^* = 0.04$ (-4%)
   - *Natural Language $\ell$:* `"{symbol} ({sector}) shows institutional accumulation: {VolumeImbalance:.0%} buy imbalance with {VolumeRatio:.1f}x volume at stable price."`
2. **Type 2: Flow Momentum ($\theta = \text{flow\_momentum}$):**
   - *Conditions:* $\text{Return}_{20d} > 0.10 \land \text{VolumeImbalance} > 0.20 \land \text{PriceEfficiency} > 0.50 \land \text{RSI}_{14} < 80$
   - *Action:* `buy`
   - *Parameters:* Confidence $c = 0.70$, Target return $r^* = 0.10$ (+10%), Stop-loss $\delta^* = 0.05$ (-5%)
   - *Natural Language $\ell$:* `"{symbol} ({sector}) momentum +{Return_20d:.1f}% confirmed by {VolumeImbalance:.0%} order-flow imbalance."`
3. **Type 3: Mean Reversion ($\theta = \text{mean\_reversion}$):**
   - *Conditions:* $\text{Regime} == \text{STABLE} \land \text{RSI}_{14} < 35 \land \text{BB\_Position} < 0.20 \land \text{Distance\_From\_Low} < 0.10$
   - *Action:* `buy`
   - *Parameters:* Confidence $c = 0.65$, Target return $r^* = 0.05$ (+5%), Stop-loss $\delta^* = 0.03$ (-3%)
   - *Natural Language $\ell$:* `"{symbol} ({sector}) oversold in stable regime: RSI={RSI:.0f}, near lower Bollinger band."`
4. **Type 4: Breakout ($\theta = \text{breakout}$):**
   - *Conditions:* $\text{Distance\_From\_52w\_High} < 0.03 \land \text{VolumeRatio} > 1.8 \land \text{MACD\_Hist} > 0 \land 50 < \text{RSI}_{14} < 70$
   - *Action:* `buy`
   - *Parameters:* Confidence $c = 0.68$, Target return $r^* = 0.07$ (+7%), Stop-loss $\delta^* = 0.04$ (-4%)
   - *Natural Language $\ell$:* `"{symbol} ({sector}) breaking out near 52-week high with {VolumeRatio:.1f}x volume; MACD positive."`
5. **Type 5: Range-Bound Value ($\theta = \text{range\_bound\_value}$):**
   - *Conditions:* $\text{Regime} == \text{STABLE} \land \text{RSI}_{14} < 50 \land |\text{Return}_{20d}| < 0.05$
   - *Action:* `buy`
   - *Parameters:* Confidence $c = 0.60$, Target return $r^* = 0.05$ (+5%), Stop-loss $\delta^* = 0.03$ (-3%)
   - *Natural Language $\ell$:* `"{symbol} ({sector}) range-bound, RSI={RSI:.0f}; low-volatility accumulation candidate."`

### 3. Reinforcement Learning Execution Policy ($\epsilon$-Greedy Bandit)
Let $\mathcal{A}_t = \{\nu_\theta, w_\theta, \bar{r}_\theta\}_{\theta \in \Theta}$ be the agent state, where $\nu_\theta$ is execution count, $w_\theta$ is count of winning trades ($r > 0$), and $\bar{r}_\theta$ is mean return (`source-reported`, Definition 3 & Equation (7)):
- With probability $\epsilon$, execute the trade unconditionally (exploration).
- With probability $1 - \epsilon$:
  - If $\nu_\theta < 5$ (cold start): execute if confidence $c > 0.50$.
  - Else: execute if empirical win rate exceeds confidence-adjusted threshold:
    $$\frac{w_\theta}{\nu_\theta} > \tau(c) = 0.45 + (1.0 - c) \times 0.10$$
    *(e.g., for Type 1 ($c=0.75$), threshold $\tau = 0.475$; for Type 5 ($c=0.60$), threshold $\tau = 0.490$).*
- **Exploration parameter:** $\epsilon_{\text{train}} = 0.70$ during 252-day in-sample training window; $\epsilon_{\text{test}} = 0.10$ during 63-day out-of-sample evaluation window (`source-reported`).

### 4. Position Sizing and Portfolio Constraints
- **Maximum concurrent positions:** $N_{\max} = 5$ (`source-reported`).
- **Position allocation cap:** Maximum 20% of capital ($0.20 \times \text{Capital}$) per security (`source-reported`).
- **Sector allocation cap:** Maximum 50% of capital per GICS sector (`source-reported`).
- **Conflicting signals / capacity:** If number of open positions $< 5$, incoming hypotheses are filtered by sector constraint, and executed sequentially until capacity is reached (`source-reported`).

### 5. Triple Exit Trigger
Positions are evaluated at day $t$ close and exited at day $t+1$ open upon the first satisfied condition (`source-reported`):
1. **Profit Target Hit:** Unrealized return $\ge r^*$ (4% to 10% depending on type).
2. **Stop-Loss Triggered:** Unrealized return $\le -\delta^*$ (-3% to -5% depending on type).
3. **Time Limit Exceeded:** Holding duration $> 30$ trading days.

### 6. Operational Classification
- **Lookback windows (5d imbalance, 20d volume/return, 50d SMA, 60d vol):** `source-reported`
- **Feature thresholds (imbalance 0.30/0.20, volume ratio 1.5/1.8):** `source-reported`
- **Target return $r^*$ and stop-loss $\delta^*$:** `source-reported`
- **Bandit threshold formula ($\tau(c) = 0.45 + 0.10(1-c)$):** `source-reported`
- **Train/Test epsilon ($\epsilon_{\text{train}}=0.7, \epsilon_{\text{test}}=0.1$):** `source-reported`
- **Position size (20%), sector cap (50%), max positions (5):** `source-reported`
- **Execution timing (Signal formed at $t$ close, order filled at $t+1$ open):** `source-reported`
- **Commission ($1.00) and slippage (5 bps):** `source-reported`

## Required data

- **Instrument Universe:** 100 US equities from the S&P 500 across 10 GICS sectors (10 stocks per sector: Technology, Healthcare, Financials, Consumer Discretionary, Consumer Staples, Industrials, Communication Services, Energy, Materials, Utilities) (`source-reported`).
- **Benchmark:** SPY (SPDR S&P 500 ETF Trust) (`source-reported`).
- **Venue:** US Equity National Market System (NYSE / NASDAQ) (`source-reported`).
- **Market Type:** Cash / spot equities, long-only (`source-reported`).
- **Timeframe & Resolution:** Daily OHLCV bars (`source-reported`).
- **Price & Volume Fields:** Open, High, Low, Close, Volume, adjusted for splits and dividends (`source-reported`).
- **Point-in-Time Availability:** Signals generated strictly after Day $t$ close using information $\mathcal{I}_t = \{P_\tau^s : \tau \le t\}$. No lookahead bias across bars (`source-reported`).
- **Sample Span:** 10 full calendar years, January 2, 2015 to October 31, 2024 ($T = 2,475$ trading days) (`source-reported`).
- **Data Provider:** Yahoo Finance via `yfinance` API (`source-reported`).
- **Survivorship Handling:** Authors explicitly acknowledge survivorship bias in the 100-stock universe (requiring continuous listing from 2015 to 2024), biasing results upward; however, this biases the reported modest returns conservatively against finding an inflated edge (`source-reported`).
- **Missing Data Handling:** Symbols aligned to the SPY calendar; indicators computed only on listed bars and reindexed to prevent forward-fill leakage (`source-reported`).

## Execution assumptions

- **Signal-to-Order Timing:** Hypotheses generated at Day $t$ close; market orders executed at Day $t+1$ market open (`source-reported`).
- **Order Type & Fill Model:** Market open order with explicit execution price $P_{\text{exec},t+1}^s = O_{t+1}^s \cdot (1 + \text{sign} \cdot c_{\text{slippage}})$ (`source-reported`).
- **Slippage Assumption:** 5 basis points ($c_{\text{slippage}} = 0.0005$) per fill (`source-reported`).
- **Commission Assumption:** $c_{\text{fixed}} = \$1.00$ fixed fee per trade deducted from cash (`source-reported`).
- **Cash Drag:** Minimum 80% initial capital preserved; typical cash allocation remains high ($>60\%$) as only up to 5 names are held concurrently (`source-reported`).
- **Shorting / Borrow:** None; 100% long-only (`source-reported`).
- **Leverage:** Zero leverage; margin trading not used (`source-reported`).
- **Capacity:** High capacity given S&P 500 large-cap universe, but bounded by the 5-position constraint (`source-reported`).

## Evidence

### Source-reported

All metrics below are transcribed directly from Deep, Deep, and Lamptey (arXiv:2512.12924v1, Tables 1, 3, 11, 12, 14 and `src/summary_metrics.json`), evaluated across 34 rolling out-of-sample test folds net of $1 commission and 5 bps slippage:

#### 1. Out-of-Sample Walk-Forward Aggregate Performance (Table 1 & Table 11)
- **Folds:** $K = 34$ quarterly out-of-sample evaluation periods (63 trading days each, 2015–2024).
- **Mean Quarterly Return:** 0.14% (annualized return: **0.55%** vs SPY 13.2% / 14.7%).
- **Standard Deviation:** 0.82% quarterly (annualized: **1.64%** vs SPY 15.3%).
- **Sharpe Ratio (annualized, excess over zero):** **0.33** (or 0.3425 in JSON vs SPY 0.86).
- **Sharpe Ratio (annualized, excess over $R_f = 2.0\%$):** **-0.8877** (`source-reported` in `summary_metrics.json`).
- **Sortino Ratio (annualized):** **0.60** (or 0.4772 in JSON vs SPY 0.71).
- **Maximum Drawdown:** **-2.76%** (cumulative peak-to-trough in paper Table 11; -2.66% in JSON vs SPY **-23.8%**).
- **Worst Fold Return:** **-1.04%** (vs SPY worst quarter -19.6%).
- **Best Fold Return:** **+2.73%** (vs SPY best quarter +20.5%).
- **Market Beta:** **0.058** (near-zero market exposure; -0.0067 in JSON).
- **Correlation with SPY:** 0.53 (or -0.072 in JSON).
- **Tracking Error:** 7.25% (or 8.70% in JSON).
- **Information Ratio:** -0.4065 (`source-reported` vs SPY).
- **Annualized Alpha:** +0.06% (in paper Table 11) / +0.65% (in JSON).
- **Trading Activity:** 140 total trades executed across 10 years (average 4.1 trades per quarter).
- **Trade-Level Win Rate:** **46.5%** (winning trades: 65 / 140).
- **Fold-Level Win Rate:** **41.2%** (14 of 34 folds positive; or 50% in JSON).

#### 2. Statistical Significance Tests (Table 12 & Table 3)
- **Two-Sided t-test:** $t = 0.96$, $p\text{-value} = 0.34$, $\text{df} = 33$ (or $t = 0.9836, p = 0.3324$). Fail to reject $H_0$ (statistically indistinguishable from zero).
- **One-Sided t-test:** $t = 0.96$, $p\text{-value} = 0.17$.
- **Bootstrap 95% Confidence Interval (10,000 resamples):** $[-0.12\%, +0.43\%]$ (includes zero; $[-0.0012, +0.0042]$ in JSON).
- **Monte Carlo Permutation Test (10,000 sign-flips):** $p\text{-value} = 0.3463$ (or 0.98 in Table 12).
- **Binomial Test on Win Rate:** $p\text{-value} = 0.5679$ (or 0.89 in Table 12).
- **Cohen's $d$ Effect Size:** $d = 0.17$ (very small effect).
- **Statistical Power:** Approximately 12% (very low power given sample size).

#### 3. Advanced Overfitting and Track-Record Diagnostics (`summary_metrics.json`)
- **Probabilistic Sharpe Ratio ($\text{PSR}(\text{SR}^* = 0)$):** 0.8589 (85.89%).
- **Minimum Track Record Length ($\text{MinTRL}$ at 95% confidence):** 78.2 quarters (**19.5 years** required to reject $\text{SR} \le 0$ at 95% significance).
- **Deflated Sharpe Ratio ($\text{DSR}$):**
  - $N = 1$ trial: 0.8589
  - $N = 10$ trials: 0.3089
  - $N = 30$ trials: 0.1592
  - $N = 100$ trials: 0.0728 (collapses to near-zero significance after 100 trials).
- **Probability of Backtest Overfitting (PBO):** 0.7059 (70.6%).
- **Train vs. Test Information Coefficient (IC):** -0.2190 ($p = 0.2134$, indicating slight negative correlation between in-sample and out-of-sample performance).

#### 4. Macro Regime Performance Heterogeneity (Table 14)
- **Low Volatility (2015–2019, 16 quarters):**
  - Mean quarterly return: **-0.16%**
  - Fold win rate: 37.5% (6 / 16)
  - Annualized Sharpe ratio: **-0.21**
- **High Volatility (2020–2024, 18 quarters):**
  - Mean quarterly return: **+0.60%**
  - Fold win rate: 44.4% (8 / 18)
  - Annualized Sharpe ratio: **+1.01**
- **Sub-Period Granularity:**
  - *Pre-COVID Bull (2017–2019, 8 quarters):* Return -0.32%, Win rate 37.5%, Sharpe -0.58.
  - *COVID Crash (2020 Q1–Q2, 2 quarters):* Return -0.15%, Win rate 50.0%, Sharpe -3.30.
  - *Recovery Bull (2020–2021, 8 quarters):* Return +0.38%, Win rate 50.0%, Sharpe +0.92.
  - *Bear Market (2022, 4 quarters):* Return -0.70%, Win rate 0.0%, Sharpe -3.23.
  - *Stabilization (2023–2024, 8 quarters):* Return +0.72%, Win rate 62.5%, Sharpe +3.14.

### Independently reproduced

Not independently reproduced. All metrics reflect direct extractions from arXiv:2512.12924v1 and the author's primary repository validation outputs (`summary_metrics.json`, `COMPREHENSIVE_REPORT.txt`).

### Negative evidence

The authors provide one of the most transparent negative evidence reports in quantitative literature:
- **Statistically Insignificant Overall Edge:** The aggregate 10-year strategy return is statistically indistinguishable from zero ($p = 0.34$, $t = 0.96$). A researcher seeking a 5% significance level must conclude that the null hypothesis of zero alpha cannot be rejected.
- **Negative Excess Return over Cash ($R_f = 2\%$):** At an annualized gross return of 0.55%, the strategy significantly lags the risk-free rate, producing a negative excess Sharpe of **-0.8877**.
- **Regime Decay in Low Volatility:** During the 2015–2019 low-volatility period, the system suffered negative quarterly returns (-0.16%) and negative Sharpe (-0.21), proving that daily microstructure proxies decay when trading volume and volatility compress.
- **Extreme Track Record Requirement:** Under Lopez de Prado's Minimum Track Record Length (MinTRL) framework, the strategy requires **19.5 years** (78.2 quarters) of out-of-sample data to establish that its Sharpe ratio is statistically greater than zero at the 95% level.
- **High Probability of Overfitting:** The single-strategy PBO is estimated at **70.6%**, and the correlation between training fold return and out-of-sample testing return is negative ($\text{IC} = -0.219$).
- **Low Trade Frequency:** Only 140 trades executed across 10 years (14 trades/year across 100 stocks), resulting in high cash drag and slow learning dynamics for the RL bandit.

## Falsification plan

The following operational tests define pre-declared failure criteria to disconfirm or further constrain the proposed microstructure hypothesis engine:

1. **Transaction Cost Escalation Stress Test:**
   - *Protocol:* Re-evaluate the 34 walk-forward folds under slippage parameters of 10 bps, 15 bps, and 20 bps, and commission of $2.00/trade.
   - *Decision Rule (`research-defined falsification threshold`):* If high-volatility regime (2020–2024) annualized Sharpe drops below 0.20 at $\le 10$ bps slippage, falsify the hypothesis that the strategy captures genuine microstructure alpha rather than unexecutable friction edge.
2. **Intraday vs. Daily Microstructure Comparison:**
   - *Protocol:* Replace the daily Close-to-Open sign proxy of volume imbalance ($\mathbb{1}(C > O)$) with true millisecond/tick-level signed trade imbalance (Lee-Ready algorithm on TAQ tick data).
   - *Decision Rule (`research-defined falsification threshold`):* If tick-level order flow fails to achieve a rank information coefficient ($\text{Rank IC}$) $> 0.03$ with next-day returns, reject the premise that daily bar heuristics approximate institutional accumulation.
3. **Randomized Hypothesis Null Test (Placebo Bandit):**
   - *Protocol:* Replace the five structured hypothesis generators with five pseudo-random entry rules matching identical trade frequency and holding periods, passed through the same $\epsilon$-greedy bandit.
   - *Decision Rule (`research-defined falsification threshold`):* If the randomized hypothesis generator achieves within 15% of the real strategy's return and drawdown in the high-volatility regime, reject the domain-specific microstructure rules as non-contributory.
4. **Out-of-Sample Extension (2025–2026 Walk-Forward):**
   - *Protocol:* Evaluate the model on out-of-sample data from November 1, 2024 through September 2026 (folds 35–42).
   - *Decision Rule (`research-defined falsification threshold`):* If cumulative drawdown exceeds -4.0% or 3 consecutive quarters generate negative returns, trigger strategy shutdown.
5. **Regime Classifier Inversion:**
   - *Protocol:* Force the system to trade only during `STABLE` regimes and halt during `VOLATILE` regimes.
   - *Decision Rule (`research-defined falsification threshold`):* If inverted execution outperforms normal execution, falsify the theoretical premise connecting information arrival to alpha extraction.

## Crypto portability

**Portability Status:** `adapted` / `unproven`

The primary paper evaluates 100 large-cap US equities exclusively. Applying this mechanism to cryptocurrency assets represents a research hypothesis and has not been validated in the cited literature:

- **Volume Imbalance Superiority in Crypto:** Unlike US equities where consolidated tape reporting does not flag order direction (requiring daily bar proxies like $\mathbb{1}(C > O)$), centralized crypto perpetual venues (e.g., Binance, Bybit, OKX) publish exact trade taker sides (`is_buyer_maker`) in real-time. Taker buy/sell volume imbalance can be measured with exact second-level precision rather than estimated from daily OHLC (`research-proposed`).
- **Continuous 24/7 Session Boundaries:** Equities rely on distinct market close (16:00 EST) and open (09:30 EST) auctions where overnight news accumulates. In crypto, continuous trading eliminates overnight gaps. Rebalance intervals must be adapted to fixed UTC epochs (e.g., 00:00 UTC or 8-hour funding intervals) (`research-proposed`).
- **Funding Rate Drag on Momentum:** The Flow Momentum hypothesis holds positions for up to 30 days. In crypto perpetuals, holding long positions during aggressive bull runs can incur annual funding rates of 20%–50%, which would quickly overwhelm the modest 0.55% annual equity return (`research-proposed`).
- **Liquidation Cascades vs. Institutional Accumulation:** Crypto volatility is heavily driven by mechanical liquidation spirals rather than orderly institutional accumulation. The `VOLATILE` regime detector must incorporate Open Interest (OI) velocity and liquidation volumes (`research-proposed`).
- **Execution Cost Structure:** Crypto taker fees (2–5 bps) plus exchange spread are comparable to the 5 bps slippage assumption, but high-volatility slippage in mid/small-cap altcoins often exceeds 20–50 bps. Porting should be restricted to the top 20 liquid perpetuals (`research-proposed`).

## Limitations

- **Statistically Insignificant Return:** Full-sample annualized return (+0.55%) is statistically indistinguishable from zero ($p = 0.34$) and below cash yields.
- **Survivorship Bias in Equity Universe:** The 100-stock sample required continuous trading from 2015 to 2024, excluding bankrupt, acquired, or delisted firms.
- **Heuristic Microstructure Approximations:** Volume imbalance is estimated from daily OHLC rather than tick-level order book or Trade and Quote (TAQ) feeds.
- **Negative Correlation in Walk-Forward Folds:** Information coefficient between training performance and testing performance is negative (-0.219), showing the bandit frequently over-explores or lags regime transitions.
- **Low Capital Efficiency:** 80% capital buffer and max 5 positions create substantial cash drag in trending bull markets.
- **Unproven in Digital Assets:** Portability to crypto is strictly conceptual.

## Implementation status

`not-implemented`

No implementation of this strategy exists in `nautilus-quant-system`, PyBroker, NautilusTrader, or any internal execution pipeline. The author's Python package (`akashdeepo/Interpretable-Hypothesis-Driven-Trading`, commit `f2db15595845f1786461d9a2d9f7409ad76559b9`) provides an external reference implementation only.

## Adoption boundary

This document represents research capture only. Inclusion in this repository does not constitute:
- Validation of persistent alpha
- Approval for production backtesting
- Approval for paper trading
- Approval for testnet deployment
- Approval for live capital deployment

Any progression toward formal historical evaluation in `nautilus-quant-system` requires independent intake review, full translation to Nautilus event-driven actors, and testing against survivorship-bias-free tick data.

## Related Wiki records

- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` — Walk-forward validation, combinatorial purged cross-validation, and lookahead leakage prevention.
- `[[quant/market-making-online-lob-action-dependent-feedback-2026-09-02.md]]` — Order book microstructure and action-dependent feedback.
- `[[quant/retail-signal-three-gate-falsification-oscillator-volume-calendar-trend-2026-09-04.md]]` — Multi-gate signal falsification and volume-calendar filters.
- `[[quant/adaptive-alpha-weighting-ppo-llm-generated-alphas-2026-09-05.md]]` — Dynamic reinforcement learning weighting of modular alpha generators.
- `[[quant/mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05.md]]` — Intraday OHLCV signal edge ceilings and transaction friction bounds.

## Sources

1. Gagan Deep, Akash Deep, and William Lamptey. *"Interpretable Hypothesis-Driven Trading: A Rigorous Walk-Forward Validation Framework for Market Microstructure Signals."* arXiv preprint `arXiv:2512.12924v1 [q-fin.TR, cs.LG]`, submitted December 15, 2025; revised August 24, 2026.
   - Stable Abstract: [https://arxiv.org/abs/2512.12924](https://arxiv.org/abs/2512.12924)
   - Full Text HTML: [https://arxiv.org/html/2512.12924v1](https://arxiv.org/html/2512.12924v1)
   - Full Text PDF: [https://arxiv.org/pdf/2512.12924](https://arxiv.org/pdf/2512.12924)
   - DOI: [10.48550/arXiv.2512.12924](https://doi.org/10.48550/arXiv.2512.12924)
2. Akash Deep. *Interpretable-Hypothesis-Driven-Trading* (Open-Source Research Repository).
   - Repository URL: [https://github.com/akashdeepo/Interpretable-Hypothesis-Driven-Trading](https://github.com/akashdeepo/Interpretable-Hypothesis-Driven-Trading)
   - Immutable Commit SHA: `f2db15595845f1786461d9a2d9f7409ad76559b9`
   - Key modules: `hdt/config.py`, `hdt/hypothesis.py`, `hdt/features.py`, `hdt/agent.py`, `hdt/backtester.py`, `hdt/validation.py`, `src/summary_metrics.json`, `src/COMPREHENSIVE_REPORT.txt`
