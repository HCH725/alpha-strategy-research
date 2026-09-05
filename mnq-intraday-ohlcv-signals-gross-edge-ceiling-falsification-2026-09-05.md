---
schema: strategy-research-record-v1
title: "Structural Limits of OHLCV-Based Intraday Signals in MNQ Futures: Gross Edge Ceiling and Friction-Aware Falsification"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - futures
  - nasdaq-100
  - falsification
  - intraday-momentum
  - transaction-costs
  - negative-evidence
status: research-only
confidence: high
source_as_of: 2026-05-15
sources:
  - "arXiv:2605.04004v1 [q-fin.TR]"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Structural Limits of OHLCV-Based Intraday Signals in MNQ Futures: Gross Edge Ceiling and Friction-Aware Falsification

## Provenance

- **Primary Research Paper:** Mathias Mesfin, *"Structural Limits of OHLCV-Based Intraday Signals in MNQ Futures: A Systematic Falsification Study"*, arXiv preprint `arXiv:2605.04004v1 [q-fin.TR]`, manuscript date May 2026 (research period 2024–2026). Canonical URL: [https://arxiv.org/abs/2605.04004](https://arxiv.org/abs/2605.04004). Direct PDF: [https://arxiv.org/pdf/2605.04004](https://arxiv.org/pdf/2605.04004).
- **Author & Affiliation:** Mathias Mesfin, Independent Researcher (`mathiasmesfin.research@gmail.com`).
- **Verification Basis:** The complete 15-page manuscript PDF was directly downloaded and inspected. Every reported numerical statistic, parameter threshold, empirical table (Tables 1 through 11), figure analysis (Figures 1 through 4), and project decision ledger entry (Appendix Table A1, decisions D001 through D213) was verified directly from the primary manuscript.

## Economic mechanism

### Source-reported

In retail futures trading communities, widespread consensus asserts that simple price and volume patterns—such as Opening Range Breakouts (ORB), overnight gap fades, volume spike momentum, and liquidity grab sweeps—yield profitable intraday directional edges. Mesfin (2026) evaluates fourteen distinct intraday signal families across 947 trading days (72,604 5-minute bars) of continuous front-month Micro E-Mini Nasdaq-100 (MNQ) futures under an institutional execution protocol (signal formed at bar close, fill at next bar open, with a realistic 2.0-point round-trip friction deduction).

The central finding of the study is the existence of a structural **Gross Edge Ceiling**:
1. *Magnitude of the Gross Ceiling:* Across all fourteen tested OHLCV signal families, the maximum gross return before transaction costs ranges between $0.07$ and $1.50$ points per trade at the most favorable horizons.
2. *Friction Floor Exceeds Gross Edge:* A realistic round-trip friction cost in MNQ is $2.0$ points ($\approx \$4.00$ per micro contract, comprising half-spread, CME exchange/clearing fees, and conservative execution slippage). Consequently, every single-bar directional signal family fails economically, producing net losses after realistic trading costs.
3. *Intra-Bar Exhaustion:* For breakout and expansion signals (such as Asia session expansion bars), momentum exists intra-bar but is fully consumed within the 5-minute formation period. Systematic execution at the close of the expansion bar captures only the subsequent exhaustion reversal ($T = -10.96$ at bar+1).
4. *Regime Separation in Positive Controls:* True tradeable edge in MNQ exists only when signals incorporate structural regime conditioning (e.g., Gaussian Mixture Model state transitions) and longer holding horizons (12–15 bars / 60–75 minutes), allowing gross point drift to accumulate sufficiently above the fixed 2.0-point friction floor (demonstrated via two validated positive control strategies: RTH Confluence with $T = 5.83$, mean net $+15.77$ pts, and London Session Signal B with $T = 5.15$, mean net $+5.77$ pts).

### Research interpretation

Mesfin (2026) provides a rigorous empirical demonstration of Grossman-Stiglitz information equilibrium and competitive alpha decay in high-liquidity financial futures:
1. *Friction-Bounded Efficiency:* Liquid electronic futures markets do not need to be zero-arbitrage efficient at the gross price level. Rather, competitive trading by low-latency market makers and institutional prop desks drives gross predictability down to the marginal transaction friction of institutional participants ($\approx 0.5$ to $1.0$ point). For retail and systematic traders paying typical broker/exchange fees and spread crossings ($2.0$ points), net alpha is structurally negative.
2. *Causal Latency & Bar-Close Adverse Selection:* OHLCV bar aggregations impose an artificial information lag. When a volume or price breakout candle closes, aggressive informed flow has already transacted. Entering at the open of the subsequent candle forces the systematic strategy to provide liquidity to high-frequency participants unwinding their inventory, resulting in severe post-breakout mean reversion.
3. *Horizon-Friction Mismatch:* Low-frequency predictive features (e.g. regime states, order-flow transitions) have low per-minute signal-to-noise ratios. Truncating trades to $1$–$6$ bars ($5$–$30$ minutes) exposes the strategy to high turnover drag where transaction costs dominate variance. Only strategies with holding periods long enough for conditional drift to compound past the bid-ask spread ($\ge 12$ bars) can survive.

## Signal

### Signal Architecture & Execution Interface

- **Observation Timestamp:** Step $t$, formed at the completed close of 5-minute bar $t$ (`source-reported`).
- **Execution Timestamp:** Step $t+1$, strictly filled at the opening print of bar $t+1$ (`source-reported`).
- **Instrument Tick Size:** 0.25 index points ($\$0.50$ per micro contract) (`source-reported`).
- **Friction Model:** Fixed 2.0 index points deduction per round-trip trade ($\$4.00$ per contract, accounting for 0.5 pt half-spread, 0.5 pt exchange fees, and 1.0 pt slippage) (`source-reported`).

### Validation Standards (Five Simultaneous Criteria)

A signal candidate is validated if and only if it satisfies all five criteria simultaneously (`source-reported`, Table 2):
1. **Out-of-Sample (OOS) $T$-Statistic:** $T \ge 2.0$ on expanding walk-forward test data.
2. **OOS Trade Count:** Minimum $N \ge 30$ trades.
3. **Net Return:** Positive mean net return after the 2.0-point friction cost.
4. **Year-by-Year Stability:** Directional consistency across all tested calendar years (2022, 2023, 2024, 2025). Single-year windfalls masking flat/negative surrounding years are classified as regime changes, not persistent alpha.
5. **Permutation Test:** Monte Carlo label shuffling $p < 0.05$.

### Evaluated Signal Families & Operational Logic

Mesfin (2026) systematically tested fourteen distinct signal families:

1. **Opening Range Breakout (ORB) (Section 4.1):**
   - *Lookback Window:* Opening 25 minutes of Regular Trading Hours (09:30–09:55 ET).
   - *Trigger:* Price breakout above session high or below session low.
   - *Tested Horizons:* Bar+1 (5 min) and Bar+15 (75 min).
   - *Pullback Variant:* Limit order entry waiting for price to retrace within 5 points of breakout level with a 20-point stop loss (`source-reported`).
2. **Asia Session Opening Range Expansion (Section 4.2):**
   - *Session:* 20:00–02:00 ET.
   - *Trigger:* Bar range exceeds $1.5\times$, $2.0\times$, or $2.5\times$ rolling 20-bar average range.
   - *Direction:* Tested in the expansion continuation direction at horizons Bar+1 and Bar+6.
3. **Asia Session Liquidity Grab Reversal (Section 4.3):**
   - *Trigger:* Price pierces recent session high or low during 20:00–02:00 ET but closes back inside the prior range (identifying stop sweeps).
   - *Tested Modes:* Fade the grab (counter-trend) vs. trade with the grab (trend).
4. **Overnight Gap Fill Fade & Gap Continuation (Section 4.4):**
   - *Gap Fill Fade:* Enter counter-trend at 09:30, 09:45, or 10:00 ET targeting the prior session close.
   - *Gap Continuation Short:* Enter short at 09:30 ET on gap-down days where a 1D Kalman filter velocity exceeds $v > 2.5$ (`source-reported`).
5. **Volume Signature Signals (Section 4.5):**
   - *Volume Spike Momentum:* Firing on bars where volume exceeds $+2.0\sigma$ rolling volume, testing continuation in bar direction.
   - *Volume Dry-Up Exhaustion:* Firing on bars with volume in bottom decile following strong trend, testing reversal.
6. **Volatility-Volume-Gap (VVG) Regime Classifier (Section 4.6):**
   - *Condition:* Days simultaneously in top tercile of: (1) absolute first-30-minute return, (2) absolute overnight gap, and (3) first-bar volume deviation from 20-day baseline (activates on $\approx 4.4\%$ of days).
   - *Tested Strategies:* Reversal entry, continuation entry, and 15:30 ET close fade.
7. **Event Day Post-News Drift (Section 4.7):**
   - *Universe:* 993 macroeconomic releases from ForexFactory (FOMC, CPI, NFP, PCE, 2022–2025).
   - *Horizon:* Drift from bar+6 through bar+12 following release.
8. **Cross-Instrument Mean Reversion (MGC Micro Gold) (Section 4.8):**
   - *Instrument:* Micro Gold Futures (MGC) (lower Hurst exponent: $H \approx 0.50$ vs. MNQ $H = 0.59$).
   - *Signal:* Ornstein-Uhlenbeck z-score threshold crossing ($1.5\sigma$, $2.0\sigma$, $2.5\sigma$) on 5-minute and 60-minute bars.

### Positive Control Architectures (Section 5)

Two independently developed positive control strategies were included to confirm the methodology does not mechanically reject all hypotheses:

1. **RTH Confluence Signal (ATR-Adaptive) (Section 5.1):**
   - *Regime Conditioning:* Completed 5-minute bar where Gaussian Mixture Model (GMM) regime label = 1 (Active Flow) AND rolling 200-bar Markov transition probability to Regime 2 (Bullish Trend) $> 0.15$ AND rolling 50-bar volume z-score $> +0.5$.
   - *Entry:* Limit order placed on a 25-point ATR-scaled pullback from signal bar close (`source-reported`, decision D026).
   - *Exit:* Time-based deterministic exit at bar 13 ($\approx 65$ minutes) (`source-reported`, decision D041).
2. **London Session Signal B (R0 to R2 Transition) (Section 5.2):**
   - *Session:* London session (03:00–08:30 ET) on 15-minute bars.
   - *Regime Conditioning:* GMM classifier detects clean transition from Regime 0 (Bearish Chop) to Regime 2 (Bullish Drift) with zero Regime 1 contamination in prior 2 bars.
   - *Entry:* Long at next 15-minute bar open.
   - *Exit:* 60 minutes holding period or 08:30 ET session close, whichever occurs first.

## Required data

- **Primary Instrument:** CME Micro E-Mini Nasdaq-100 continuous front-month futures (MNQ) (`source-reported`).
- **Contract Specifications:** Multiplier $\$2.00 \times \text{index}$, minimum tick $0.25$ points ($\$0.50$/tick).
- **Secondary Cross-Instrument:** COMEX Micro Gold continuous front-month futures (MGC), 1,091 trading days (`source-reported`).
- **Bar Resolution:** 5-minute OHLCV sampled bars.
- **Session Timings:** Regular Trading Hours (RTH) 09:30–16:00 US Eastern Time (ET); Asia session 20:00–02:00 ET; London session 03:00–08:30 ET.
- **Dataset Sample:** 72,604 5-minute RTH bars across 947 complete trading days from December 2021 through August 2025 (`source-reported`, Table 1).
- **Macroeconomic Calendar:** ForexFactory high/medium impact events (993 events across 2022–2025, covering FOMC, CPI, NFP, PCE) (`source-reported`).
- **Data Provenance:** NinjaTrader platform, aggregated up from raw 1-minute historical data (`source-reported`).
- **Point-in-Time Partitioning:** Expanding walk-forward validation:
  - Train 2022 $\rightarrow$ Test 2023
  - Train 2022–2023 $\rightarrow$ Test 2024
  - Train 2022–2024 $\rightarrow$ Test 2025
  Parameters fitted strictly on training slices; test periods remained untouched until final evaluation.

## Execution assumptions

- **Signal-to-Order Timing:** Decisions formed at bar close $t$ execute at open of bar $t+1$ (`source-reported`).
- **Order Fill Model:** Simulated market order fill at exact opening price of bar $t+1$ (`source-reported`); RTH Confluence positive control uses 25-point limit order pullback (`source-reported`).
- **Round-Trip Friction Deduction:** Fixed $2.0$ index points ($\$4.00$ per micro contract), decomposed into $0.5$ pt half-spread, $0.5$ pt exchange/clearing/broker fees, and $1.0$ pt slippage buffer (`source-reported`).
- **Position Sizing:** Unit single micro contract ($1.0$ contract); returns tracked in un-leveraged index points (`source-reported`).
- **Market Impact & Capacity:** Assumed zero market impact beyond the fixed 1.0-point slippage buffer (`research-proposed limitation`). Valid only for small retail/prop trading sizes ($1$–$10$ contracts).

## Evidence

### Source-reported

All figures below are directly cited from Mesfin (2026), *arXiv:2605.04004v1*, Tables 3 through 11:

#### 1. Opening Range Breakout (ORB) Results (Table 3)
*Evaluated on 09:30–09:55 ET range, net after 2.0-point friction:*

| Variant | Trades ($N$) | Mean Net (pts) | $T$-Statistic | Win Rate (%) | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **ORB Long – bar+1** | 447 | $-0.82$ | $1.17$ | $51.9\%$ | **FAIL** |
| **ORB Long – bar+15** | 447 | $+2.82$ | $1.50$ | $55.5\%$ | **FAIL** |
| **ORB Short – bar+1** | 428 | $-3.45$ | $-1.33$ | $47.2\%$ | **FAIL** |
| **ORB Short – bar+15** | 428 | $-2.16$ | $-0.04$ | $47.7\%$ | **FAIL** |
| **ORB Pullback Entry** | 83 | $-4.44$ | $-1.27$ | $19.3\%$ | **FAIL** |

*Note on Year Stability:* For ORB Long (bar+15), calendar year net returns were $-1.42$ pts (2022), $+2.43$ pts (2023), and $+7.04$ pts (2024). The strategy was rejected due to lack of year stability despite the strong 2024 windfall. The pullback variant suffered an $80.7\%$ stop-out rate at a 20-point stop.

#### 2. Asia Session Opening Range Expansion Results (Table 4)
*Session 20:00–02:00 ET, tested in continuation direction:*

| Range Threshold | Horizon | Gross Return (pts) | Net Return (pts) | $T$-Statistic | Win Rate (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1.5x Rolling Mean** | Bar+1 | $-0.27$ | $-2.27$ | **$-10.96$** | $35.5\%$ |
| **1.5x Rolling Mean** | Bar+6 | $-0.08$ | $-2.08$ | **$-4.75$** | $44.4\%$ |
| **2.0x Rolling Mean** | Bar+1 | $-0.35$ | $-2.35$ | **$-7.42$** | $36.0\%$ |
| **2.5x Rolling Mean** | Bar+6 | $+1.06$ | $-0.94$ | **$-0.90$** | $48.5\%$ |

*Author finding:* At Bar+1, expansion bars exhibit massive statistically significant reversals ($T = -10.96$), proving that momentum is fully exhausted intra-bar before bar close.

#### 3. Asia Session Liquidity Grab Reversal
*Identified 6,442 events (3,419 long sweeps, 3,023 short sweeps):*
- **Fading the Grab (Counter-trend):** Mean net $-2.20$ points, $T = -14.12$.
- **Trading with the Grab (Trend):** Mean net $-1.80$ points, $T = -13.24$.
- *Conclusion:* Gross directional content is only $0.20$ to $0.80$ points in either direction, structurally below the 2.0-point friction floor.

#### 4. Overnight Gap Strategy Results (Table 5)
*Evaluated across 238–245 sessions/year:*

| Strategy Variant | Entry Time (ET) | Trades ($N$) | Mean Net (pts) | $T$-Statistic | Win Rate (%) | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Gap Fill Fade** | 09:30 | $\approx 240$/yr | $-1.92$ | $-0.44$ | $48.1\%$ | **FAIL** |
| **Gap Fill Fade** | 09:45 | $\approx 240$/yr | $-1.31$ | $-0.32$ | $47.2\%$ | **FAIL** |
| **Gap Fill Fade** | 10:00 | $\approx 240$/yr | $-2.24$ | $-0.59$ | $47.9\%$ | **FAIL** |
| **Gap Continuation Short** | 09:30 (Kalman $v > 2.5$) | 22 | $+14.52$ | **$+3.23$** | $68.2\%$ | **FAIL ($N < 30$)** |

*Note:* Gap fill fade produces $T$-stats indistinguishable from noise. The Kalman velocity gap continuation short achieved strong edge ($+14.52$ pts, $T = 3.23$), but generated only 22 trades across three years (12 in 2022, 6 in 2023, 4 in 2024), failing the minimum sample threshold ($N \ge 30$).

#### 5. Volume Signature Signal Results (Table 6)
*Evaluated after 2.0-point friction:*

| Signal Family | Direction / Condition | Trades ($N$) | Mean Net (pts) | $T$-Statistic | Win Rate (%) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Volume Spike Momentum** | Up Spike ($> +2\sigma$) | 2,119 | $-1.94$ | $+0.07$ | $51.6\%$ |
| **Volume Spike Momentum** | Down Spike ($> +2\sigma$) | 2,409 | $-2.50$ | $-0.64$ | $50.1\%$ |
| **Volume Dry-Up Exhaustion** | Up Exhaustion (bottom decile) | 1,060 | $-2.42$ | $-0.92$ | $47.4\%$ |
| **Volume Dry-Up Exhaustion** | Down Exhaustion (bottom decile) | 723 | $-1.99$ | $+0.03$ | $49.7\%$ |

*Conclusion:* Large sample sizes with $T$-statistics clustered near zero provide precise empirical proof that 5-minute volume magnitude does not predict subsequent bar direction.

#### 6. Volatility-Volume-Gap (VVG) Classifier Results (Table 7)
*Activates on $\approx 4.4\%$ of days; demonstrates $25.6$ bps next-day return spread:*

| Strategy on Classifier Days | Trades ($N$) | Mean Net (pts) | $T$-Statistic | Win Rate (%) | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Reversal Entry** | 289 | $+1.37$ | $+0.86$ | $51.9\%$ | **FAIL** |
| **Continuation Entry** | 1,175 | $-3.22$ | $-0.44$ | $48.8\%$ | **FAIL** |
| **Close Fade (15:30 ET)** | $<30$ | Insufficient | $1.08$ | $50.0\%$ | **FAIL ($N < 30$)** |

*Year Breakdown on Continuation:* 2024 showed $T = 2.07$ (mean $+9.14$ pts on 312 trades), but 2022 showed $T = -1.27$ and 2023 showed $T = -0.70$, failing year stability.

#### 7. Cross-Instrument MGC Gold Mean Reversion (Table 8)
*Tested on Micro Gold Futures (MGC, 1,091 days) after 2-point friction:*

| Configuration | Trades ($N$) | Mean Net (pts) | $T$-Statistic | Win Rate (%) | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **OU 5-min (1.5 threshold)** | 380 | $-2.76$ | $-4.49$ | $32.1\%$ | **FAIL** |
| **OU 5-min (2.0 threshold)** | 154 | $-2.19$ | $-2.19$ | $36.4\%$ | **FAIL** |
| **OU 5-min (2.5 threshold)** | 49 | $-1.72$ | $-1.12$ | $34.7\%$ | **FAIL** |
| **OU 60-min (varied)** | Varies | $\approx -2.00$ | $-1.46$ | $<40\%$ | **FAIL** |

*Finding:* 60-minute gold mean reversion half-life is $\approx 8$ hours (longer than an RTH session), rendering it structurally unviable for intraday execution.

#### 8. Validated Positive Controls (Tables 9 & 10)
*Demonstrating that the validation framework successfully detects genuine alpha:*

| Metric | Positive Control 1: RTH Confluence (Table 9) | Positive Control 2: London Signal B (Table 10) |
| :--- | :--- | :--- |
| **Conditioning Engine** | GMM Regime 1 + Markov Prob $> 0.15$ + Vol $z > 0.5$ | GMM London R0 $\rightarrow$ R2 Clean Transition |
| **Execution Horizon** | Bar 13 ($\approx 65$ min) | 60 min or 08:30 ET close |
| **Total Trades ($N$)** | 538 (in-sample) / 196 (OOS walk-forward) | 289 |
| **Mean Net Return** | **$+15.77$ pts** (IS) / **$+11.82$ pts** (OOS) | **$+5.77$ pts** |
| **$T$-Statistic** | **$5.83$** (IS) / **$3.11$** (OOS) | **$5.15$** |
| **Win Rate** | $61.0\%$ | $64.7\%$ |
| **Sharpe Ratio** | Not reported | **$5.09$** (Profit Factor: $2.42$) |
| **Permutation $p$-value** | $p < 0.001$ | $p < 0.001$ |
| **1-Bar Execution Delay** | Not reported | **$T = -3.56$** (Edge completely destroyed) |

#### 9. Gross vs. Net Return Ceiling Benchmark (Table 11)

| Signal Family | Best Gross Return | $T$-Stat (Gross) | Net After 2pt Friction | $T$-Stat (Net) |
| :--- | :--- | :--- | :--- | :--- |
| **ORB Long (bar+15)** | $+4.82$ pts | $1.50$ | $+2.82$ pts | $1.50$ |
| **Asia ORB Expansion 2.5x** | $+1.06$ pts | $-0.90$ | $-0.94$ pts | $-0.90$ |
| **Gap Fill Fade (best)** | $-1.31$ pts | $-0.32$ | $-1.31$ pts | $-0.32$ |
| **Gap Continuation Short** | **$+16.52$ pts** | **$+3.23$** | **$+14.52$ pts** | **$+3.23$** ($N=22$) |
| **Volume Spike Momentum** | $-1.94$ pts | $+0.07$ | $-1.94$ pts | $+0.07$ |
| **VVG Classifier Reversal** | $+3.37$ pts | $+0.86$ | $+1.37$ pts | $+0.86$ |
| **MGC OU (5-min, 2.0x)** | $-0.19$ pts | $-2.19$ | $-2.19$ pts | $-2.19$ |

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Gross Edge Ceiling:** In 5-minute MNQ futures, raw directional predictability from single-bar OHLCV features is bounded below $1.50$ points, falling short of the $2.0$-point round-trip friction floor.
2. **Immediate Exhaustion of Intra-Bar Breakouts:** Asia expansion bars show strong, statistically significant post-breakout reversals ($T = -10.96$ at bar+1), demonstrating that directional energy is consumed before the candle close.
3. **Spurious Year Instability:** ORB Long and VVG Continuation produced isolated profitable years (e.g. 2024: $T = 2.07$, $+9.14$ pts), but collapsed in preceding years (2022: $T = -1.27$; 2023: $T = -0.70$). Relying on single-year backtests produces catastrophic deployment failure.
4. **Volume Predictability Null Result:** Volume spikes and volume dry-ups fail to forecast direction ($T \approx 0.0$ across $> 6,300$ trades), contradicting conventional retail volume-spread analysis lore.
5. **Sample Starvation on Conditional Alpha:** Gap continuation short showed high edge ($+14.52$ pts, $T = 3.23$), but decayed from 12 trades in 2022 to 4 in 2024, indicating non-stationary occurrence frequency.

## Falsification plan

To empirically test or refute the Gross Edge Ceiling and the validity of regime-conditioned intraday momentum, the following operational falsification tests are pre-declared:

1. **Sub-Tick Order Flow & Microstructure Resolution Test:**
   - *Protocol:* Re-evaluate the fourteen signal families using full Level 2/Level 3 tick data (via Databento or CME MDP 3.0) on MNQ futures. Trigger entries dynamically intra-bar upon the breakout print rather than waiting for bar close.
   - *Failure Rule:* `research-defined falsification threshold`: If tick-level intra-bar execution fails to achieve an out-of-sample gross return $\ge 3.0$ points per trade or net Sharpe $\ge 1.0$ after realistic bid-ask spread crossing, confirm that intra-bar momentum is an illusion of adverse selection.
2. **Direct Market Access (DMA) Fee & Spread Sensitivity Stress Test:**
   - *Protocol:* Vary round-trip friction from $0.5$ points (institutional maker/DMA tier) to $3.5$ points (stressed volatile market condition) across all fourteen families.
   - *Failure Rule:* `research-defined falsification threshold`: If any of the fourteen single-bar OHLCV families produces a positive net Sharpe $> 1.0$ at a friction cost $\ge 1.5$ points, falsify the claim that the gross edge ceiling is bounded at $1.50$ points.
3. **Out-of-Sample Walk-Forward Period Extension (2025–2026):**
   - *Protocol:* Evaluate the two positive control strategies (RTH Confluence and London Signal B) on untouched MNQ data from September 2025 through August 2026.
   - *Failure Rule:* `research-defined falsification threshold`: If the OOS walk-forward $T$-statistic for either positive control drops below $1.50$ or annualized net return turns negative, reject the hypothesis that GMM regime transitions generate persistent multi-year alpha.
4. **Execution Latency Perturbation on Positive Controls:**
   - *Protocol:* Introduce artificial execution delays of 1 bar, 2 bars, and 3 bars to the London Session Signal B entry.
   - *Failure Rule:* `research-defined falsification threshold`: If a 1-bar execution delay maintains $T \ge 2.0$, falsify the author's reported finding that the edge is hyper-sensitive to exact transition timing ($T$ dropping from $+5.15$ to $-3.56$).

## Crypto portability

- **Portability Classification:** `adapted/unproven` (research interpretation; primary research is demonstrated exclusively on CME MNQ equity index futures and COMEX MGC gold futures).
- **Structural Differences & Translation to Cryptocurrency Derivatives:**
  1. **Continuous 24/7 Session vs. Segmented Cash Session:** MNQ exhibits distinct session segmentation (Asia, London, RTH 09:30–16:00 ET) driven by institutional cash market opens. BTC and ETH perpetual futures trade continuously 24/7/365. While Asia and London time-of-day volume seasonality exists in crypto, liquidity does not abruptly jump at 09:30 ET as in US equity index futures.
  2. **Fee Schedule & VIP Tier Asymmetry:** CME micro futures impose fixed per-contract exchange and NFA fees ($\approx \$0.50$–$\$0.70$/side), which represent a large percentage of micro contract value. In crypto perpetuals (Binance, Bybit, Hyperliquid), fees are basis-point proportional: taker fees range from $2.0$ to $5.0$ bps, while high-volume maker tiers enjoy negative or zero fees. A strategy with a gross edge of $1.0$ index point in BTC ($\approx 1.5$ bps) would be completely unviable with taker orders, but could theoretically be harvested via passive maker limit orders.
  3. **Order-Book Spread Dynamics & Flash Liquidity Exhaustion:** Crypto perpetual markets experience non-linear order-book sweeps during volatility cascades. Breakout signals executed at bar close are especially prone to adverse fills during liquidations.
  4. **Funding Rate & Basis Frictions:** Crypto perpetual positions held over multiple hours incur 8-hour funding rates ($\pm 1$–$10$ bps), adding holding-cost friction that does not exist in CME equity index futures.

## Limitations

- **Fixed Friction Simplification:** The 2.0-point friction model assumes constant liquidity. Real-world bid-ask spreads widen significantly during economic data releases and market opens (`source-reported limitation`).
- **Absence of Tick-Level Resolution:** Relying on 5-minute bar close eliminates intra-bar execution dynamics where momentum bursts may be extractable before bar completion (`source-reported limitation`).
- **Sample Timeframe Constraint:** The 2021–2025 dataset reflects modern algorithmic dominance; results may not reflect earlier market regimes prior to widespread retail prop-firm participation (`source-reported limitation`).
- **Single-Instrument Focus:** Falsification is demonstrated on MNQ (with cross-check on MGC gold), but has not been exhaustively evaluated on energy, agricultural, or foreign exchange futures (`source-reported limitation`).
- **Omission of Non-Linear Market Impact:** Models do not account for price impact or order-book consumption at institutional position sizing ($> 50$ contracts) (`research-proposed limitation`).

## Implementation status

- `implementation_status: not-implemented`
- Neither the 14 falsified OHLCV signal families nor the two GMM-conditioned positive control architectures have been implemented or benchmarked in our quantitative research codebase (`nautilus-quant-system`, PyBroker, or NautilusTrader).
- No historical backtesting, paper trading, testnet verification, or live trading has been conducted or authorized.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- This record serves strictly as normalized research capture of an empirical falsification study documenting the structural limits of OHLCV-based intraday signals and the gross edge ceiling in equity index futures. It does not authorize strategy adoption or capital allocation.

## Related Wiki records

- `retail-signal-three-gate-falsification-oscillator-volume-calendar-trend-2026-09-04.md` (Systematic three-gate falsification of retail technical indicators across equity and crypto markets)
- `binance-spot-candle-ml-extrema-timing-falsification-2026-09-02.md` (Falsification study of candle extrema classification in cryptocurrency spot markets)
- `crypto-walk-forward-window-optimization-double-oos-momentum-2026-09-02.md` (Walk-forward window optimization and out-of-sample stability in momentum strategies)
- `intraday-overreaction-momentum-finbert-emotion-classifier-2026-09-05.md` (Intraday overreaction momentum and NLP emotion classifiers)
- `decomposable-reward-forex-rl-mask-aware-doubledqn-2026-09-05.md` (Anti-lookahead execution timing and friction modeling in systematic trading)

## Sources

1. **Primary Research Paper:** Mathias Mesfin, *"Structural Limits of OHLCV-Based Intraday Signals in MNQ Futures: A Systematic Falsification Study"*, arXiv preprint `arXiv:2605.04004v1 [q-fin.TR]`, May 2026. Stable abstract: [https://arxiv.org/abs/2605.04004](https://arxiv.org/abs/2605.04004). Direct PDF: [https://arxiv.org/pdf/2605.04004](https://arxiv.org/pdf/2605.04004).
2. **Primary Manuscript Empirical Tables & Evidence (arXiv:2605.04004v1):**
   - Table 1: Dataset summary (72,604 5-min RTH bars, 947 days, 2021–2025, NinjaTrader platform)
   - Table 2: Five simultaneous validation criteria (OOS $T \ge 2.0$, $N \ge 30$, net return $> 0$, year stability, permutation $p < 0.05$)
   - Table 3: Opening range breakout (ORB) performance and pullback variant
   - Table 4: Asia session expansion bar results (1.5x, 2.0x, 2.5x thresholds)
   - Table 5: Gap strategy results across entry times (09:30, 09:45, 10:00 ET) and Kalman velocity continuation
   - Table 6: Volume signature signals (momentum up/down, dry-up up/down)
   - Table 7: Volatility-Volume-Gap (VVG) classifier directional strategy results
   - Table 8: MGC gold mean reversion results across configurations
   - Table 9: RTH Confluence Signal performance summary (Positive Control 1)
   - Table 10: London Session Signal B performance summary (Positive Control 2)
   - Table 11: Gross vs. net return comparison across signal families
   - Table A1: Locked project decision ledger (decisions D001 through D213)
