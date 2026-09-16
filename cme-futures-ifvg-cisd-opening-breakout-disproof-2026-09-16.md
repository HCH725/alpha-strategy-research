---
schema: strategy-research-record-v1
title: "CME Equity Futures IFVG-CISD Opening Breakout and Pre-Registered Cross-Instrument Disproof (Drozdz & Maguire 2026)"
created: 2026-09-16
updated: 2026-09-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equity-index-futures
  - cme
  - market-microstructure
  - opening-session
  - smart-money-concepts
  - ifvg
  - cisd
  - walk-forward-optimization
  - cluster-bootstrap
  - empirical-disproof
  - negative-evidence
status: research-only
confidence: high
source_as_of: 2026-07-13
sources:
  - "Aleksander Drozdz and Phil Maguire, 'FYP Trading Strategy', GitHub repository aleks-drozy/fyp-trading-strategy, commit 607355e02b2562e8705d2f34228d7aa44b8cd711, Maynooth University, 2026. https://github.com/aleks-drozy/fyp-trading-strategy"
  - "Aleksander Drozdz and Phil Maguire, 'fyp-strategy-engine', GitHub repository aleks-drozy/fyp-strategy-engine, commit 5a435c62ba9c7bad38f4921936a4b535c229d4e1, Maynooth University, 2026. https://github.com/aleks-drozy/fyp-strategy-engine"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# CME Equity Futures IFVG-CISD Opening Breakout and Pre-Registered Cross-Instrument Disproof (Drozdz & Maguire 2026)

## Provenance

- **Primary Academic & Implementation Sources:**
  - **Author:** Aleksander Drozdz (`aleks-drozy`), Department of Computer Science, Maynooth University (`source-reported`).
  - **Academic Supervisor:** Dr. Phil Maguire, Department of Computer Science, Maynooth University (`source-reported`).
  - **Original Implementation Repository:** `aleks-drozy/fyp-trading-strategy` (`source-reported`).
    - Repository URL: https://github.com/aleks-drozy/fyp-trading-strategy
    - Full Commit SHA: `607355e02b2562e8705d2f34228d7aa44b8cd711`
    - Key Artifacts: `FYP_Bot_1.pine`, `README.md`, `backtests/NQ1_optimised.csv`, `backtests/NQ1_2023_2024` (`source-reported`).
    - License: MIT License (`source-reported`).
  - **Successor Rigorous Research Engine Repository:** `aleks-drozy/fyp-strategy-engine` (`source-reported`).
    - Repository URL: https://github.com/aleks-drozy/fyp-strategy-engine
    - Full Commit SHA: `5a435c62ba9c7bad38f4921936a4b535c229d4e1`
    - Pre-Registration Specs: `docs/specs/2026-07-13-phase4-parameter-tuning-design.md`, `docs/specs/2026-07-13-phase5-exits-costs-volfilter-design.md`, `docs/phase6_freeze.json` (frozen config hash `699fd485e56eeea364c197bc6b47d624ed9939e99c781f87320d93cc09376ed8`, git-timestamped before runner creation) (`source-reported`).
    - Core Implementation Paths: `strategy/signals.py`, `strategy/ifvg.py`, `strategy/cisd.py`, `strategy/ema.py`, `strategy/session.py`, `strategy/params.py`, `backtest/engine.py`, `backtest/exits.py`, `backtest/costs.py`, `run_phase4.py`, `run_phase5.py`, `run_phase6.py`, `phase6_results.json` (`source-reported`).
    - License: MIT License (`source-reported`).
- **Target Universe & Data:**
  - Continuous 1-minute OHLCV bars of CME equity index futures:
    - E-mini Nasdaq-100 (`NQ`) (`source-reported`).
    - E-mini S&P 500 (`ES`) (`source-reported`).
    - E-mini Dow Jones Industrial Average (`YM`) (`source-reported`).
  - Evaluated across up to ~10 years (2016–2025) across 17 rolling walk-forward folds per instrument (`source-reported`).
- **Repository Deduplication Audit:**
  - Audited all existing `.md` files in `alpha-strategy-research` on 2026-09-16:
    - Zero existing records cite `aleks-drozy`, `fyp-strategy-engine`, `fyp-trading-strategy`, Maynooth University, Drozdz, Maguire, Inversion Fair Value Gaps (IFVG), or Change in State of Delivery (CISD).
    - Related retail/technical falsification records in the repository (`retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11.md`, `trend-fib-extension-mechanical-pivot-null-edge-falsification-2026-09-14.md`, `retail-signal-three-gate-falsification-oscillator-volume-calendar-trend-2026-09-04.md`, `tradingview-choppiness-donchian-breakout-filter-2026-09-16.md`) evaluate different indicator families (Fibonacci pivots, CVD/funding patterns, Donchian/choppiness filters) without testing SMC IFVG/CISD transition dynamics or multi-phase walk-forward cluster-bootstrap disproofs.
  - This record represents an independent, source-complete research capture of a pre-registered quantitative disproof.

## Economic mechanism

### Source-reported

1. **"Smart Money Concepts" (SMC) Opening-Drive Thesis:**
   - Proponents of SMC / ICT (Inner Circle Trader) methodologies assert that regular-hours market openings (09:30 NY) initiate institutional liquidity-seeking sequences (`source-reported`).
   - Fair Value Gaps (FVGs) represent three-candle price imbalances where aggressive market orders displace price without counterparty liquidity, creating an un-auctioned gap between bar $t-2$ high and bar $t$ low (bullish) or bar $t-2$ low and bar $t$ high (bearish) (`source-reported`).
   - When subsequent price closes through an existing FVG in the counter direction, the imbalance is termed "inverted" (Inversion FVG or IFVG). The thesis claims that an inverted gap flips polarity from a support/resistance barrier into a directional accelerator (`source-reported`).
   - Change in State of Delivery (CISD) identifies structural shifts in the market's delivery direction by recording pullback origins (potential swing tops/bottoms) and signaling a regime shift when price breaks through the open of the prior opposite-colored pullback candle (`source-reported`).
   - By combining IFVG alignment and CISD state flips on the same 1-minute bar during the New York opening window (09:30–10:30 NY), filtered by a 20-period EMA, the strategy claims to identify high-probability institutional trend continuation with tight 8-bar swing risk (`source-reported`).

### Research interpretation

1. **Microstructure Reality vs. Retail Imbalance Narratives:**
   - The economic premise that 1-minute bar imbalances (FVGs) represent persistent institutional "order-block delivery" is largely behavioral pareidolia. In highly liquid CME index futures (NQ, ES, YM), 1-minute gaps are predominantly mechanical artifacts of discrete time slicing during volatile opening price discovery, rather than structural unfilled inventory.
2. **Selectivity vs. Causal Signal Edge:**
   - The multi-phase study by Drozdz & Maguire reveals that the apparent success of the strategy in published in-sample backtests (+28,400 P&L, 1.703 PF) was not produced by an alpha signal in the IFVG/CISD mechanics.
   - When implemented as a strict, bar-by-bar causal Python engine, the raw logic generated ~4x as many trades as the cherry-picked retail logs (precision only 20–25%), failing to reach breakeven out-of-sample (`source-reported`).
3. **Data Contamination as a Source of Spurious Alpha:**
   - A critical forensic finding of the study is that third-party retail datasets can introduce artificial profitability through timestamp corruption. In the Phase-1 Kaggle NQ dataset, a ±60-minute Daylight Saving Time (DST) bug shifted bars by exactly one hour on 104 days, causing the strategy to trade mid-day sessions while assuming it was capturing the opening drive (`source-reported`).
4. **Pre-Registered Statistical Disproof:**
   - Across 10 years of CME futures data on independent instruments (ES, YM, clean NQ) evaluated over 17 walk-forward folds (1,402 out-of-sample trades over 1,005 trade-days), the pooled net R-multiple profit factor was 0.905 with a 90% day-cluster bootstrap confidence interval of [0.810, 0.996] (`source-reported`).
   - Because the upper bound of the confidence interval is strictly below 1.0, the strategy is statistically certified as losing money net of execution costs (`source-reported`).

## Signal

The signal architecture is fully specified in Python and Pine Script code without ambiguity (`source-reported`):

### 1. Session Gate & Time Convention (`source-reported`)

- Timezone: `America/New_York` (`source-reported`).
- Session Window: Weekdays between `09:30` and `10:30` NY time (left-inclusive, right-exclusive) (`source-reported`).
- Alternative In-Sample Pine Window: `09:32` to `10:00` NY time (`source-reported`).
- Gating Rule: Signal generation and FVG formation are permitted strictly while `in_session == True`. Outside this window, all FVG state tracking is forced to `"None"` and no entry triggers may fire (`source-reported`).
- Frequency Limit: Maximum 1 trade per calendar day (`MAX_TRADES_PER_DAY = 1`) (`source-reported`).
- Position Policy: Flat-only execution; pyramiding or concurrent overlapping trades are strictly disallowed (`source-reported`).

### 2. Inversion Fair Value Gap (IFVG) State Machine (`source-reported`)

- Input: 1-minute OHLCV bars (`source-reported`).
- FVG Formation on bar $t$ (evaluated for $t \ge 2$) (`source-reported`):
  - Bullish FVG forms if:
    $$\text{low}[t] > \text{high}[t-2]$$
    Subject to percentage size threshold (`fvg_threshold`, default $0.0\%$):
    $$\frac{\text{low}[t] - \text{high}[t-2]}{\text{high}[t-2]} \times 100 \ge \text{fvg\_threshold}$$
    Bounds stored: $\text{top} = \text{low}[t]$, $\text{bottom} = \text{high}[t-2]$ (`source-reported`).
  - Bearish FVG forms if:
    $$\text{high}[t] < \text{low}[t-2]$$
    Subject to percentage size threshold (`fvg_threshold`, default $0.0\%$):
    $$\frac{\text{low}[t-2] - \text{high}[t]}{\text{low}[t-2]} \times 100 \ge \text{fvg\_threshold}$$
    Bounds stored: $\text{top} = \text{low}[t-2]$, $\text{bottom} = \text{high}[t]$ (`source-reported`).
- Inversion Rule (evaluated while FVG remains active and un-inverted) (`source-reported`):
  - Bullish FVG inverts when: $\text{close}[t] < \text{fvg.bottom}$ ($\text{high}[t-2]$ at formation). Inverted state becomes `"Bearish"` (`source-reported`).
  - Bearish FVG inverts when: $\text{close}[t] > \text{fvg.top}$ ($\text{low}[t-2]$ at formation). Inverted state becomes `"Bullish"` (`source-reported`).
- Expiry: An inverted FVG expires after 10 bars ($\text{bar\_index} - \text{invert\_bar} > 10$), transitioning state to `"Expired"` (`source-reported`).
- Priority: Most recently inverted active FVG sets the prevailing `ifvg_state` (`source-reported`).
- Daily Reset: FVG memory array is cleared at the start of each new calendar day (`source-reported`).

### 3. Change in State of Delivery (CISD) State Machine (`source-reported`)

- Structure Tracking:
  - Pullback Detection:
    - Bearish pullback detected on bar $t$ when prior bar was bullish: $\text{close}[t-1] > \text{open}[t-1]$. Marks $\text{potential\_top} = \text{open}[t-1]$ and records $\text{bullish\_break\_idx} = t-1$ (`source-reported`).
    - Bullish pullback detected on bar $t$ when prior bar was bearish: $\text{close}[t-1] < \text{open}[t-1]$. Marks $\text{potential\_bottom} = \text{open}[t-1]$ and records $\text{bearish\_break\_idx} = t-1$ (`source-reported`).
  - Market Structure Break:
    - Bullish break: When price breaks structure top, sets `bear_cisd_level` to potential bottom price (`source-reported`).
    - Bearish break: When price breaks structure bottom, sets `bull_cisd_level` to potential top price (`source-reported`).
    - *Neighbor Index Correction:* In bars-ago notation, the reference bar is $t - \text{offset} - 1$ (one bar earlier), correcting a common forward-offset indexing defect (`source-reported`).
  - CISD State:
    - `currentState` flips to `True` (`"Bullish"`) when $\text{close}[t] > \text{bear\_cisd\_level}$ (`source-reported`).
    - `currentState` flips to `False` (`"Bearish"`) when $\text{close}[t] < \text{bull\_cisd\_level}$ (`source-reported`).

### 4. Trend Filter (`source-reported`)

- 20-period Exponential Moving Average (EMA) computed on bar close via continuous recursive formula (`ta.ema` equivalent) (`source-reported`):
  $$\text{EMA}_t = \alpha \cdot \text{close}_t + (1 - \alpha) \cdot \text{EMA}_{t-1}, \quad \alpha = \frac{2}{\text{ema\_length} + 1}$$
- Long filter condition: $\text{close}[t] > \text{EMA}_{20}[t]$ (`source-reported`).
- Short filter condition: $\text{close}[t] < \text{EMA}_{20}[t]$ (`source-reported`).

### 5. Transition Entry Trigger (`double_confirmation`) (`source-reported`)

The strategy executes strictly on **state transitions**, not on persistent static alignment (`source-reported`):

- **Long Entry Trigger fires on bar $t$ if and only if:**
  1. CISD flipped from Bearish to Bullish on bar $t$:
     $$\text{not } \text{cisd\_bull}[t-1] \text{ and } \text{cisd\_bull}[t]$$
  2. IFVG is currently Bullish on bar $t$:
     $$\text{ifvg}[t] == \text{"Bullish"}$$
  3. Bar is inside the session window: $\text{in\_session}[t] == \text{True}$.
  4. Trend filter agrees: $\text{close}[t] > \text{EMA}_{20}[t]$.
  5. Daily quota not exhausted: trades taken today $= 0$.
- **Short Entry Trigger fires on bar $t$ if and only if:**
  1. CISD flipped from Bullish to Bearish on bar $t$:
     $$\text{cisd\_bull}[t-1] \text{ and not } \text{cisd\_bull}[t]$$
  2. IFVG is currently Bearish on bar $t$:
     $$\text{ifvg}[t] == \text{"Bearish"}$$
  3. Bar is inside the session window: $\text{in\_session}[t] == \text{True}$.
  4. Trend filter agrees: $\text{close}[t] < \text{EMA}_{20}[t]$.
  5. Daily quota not exhausted: trades taken today $= 0$.

### 6. Risk Management & Order Execution (`source-reported`)

- **Execution Timing:** Orders fill at the open of the next bar ($\text{open}[t+1]$, `next_open` fill model) (`source-reported`).
- **Stop Loss:**
  - Long: 8-bar swing low inclusive of signal bar:
    $$\text{Stop}_{\text{long}} = \min_{k=0}^{7} \text{low}[t-k]$$
  - Short: 8-bar swing high inclusive of signal bar:
    $$\text{Stop}_{\text{short}} = \max_{k=0}^{7} \text{high}[t-k]$$
- **Risk Unit ($R$):**
  $$R = |\text{entry\_price} - \text{stop\_price}|$$
  If $R \le 0$, order is discarded (`source-reported`).
- **Take Profit (Default Base Mode `fixed_1_5R`):**
  - Target set at $1.5 \times R$:
    $$\text{Target}_{\text{long}} = \text{entry} + 1.5 \cdot R, \quad \text{Target}_{\text{short}} = \text{entry} - 1.5 \cdot R$$
- **Intraday Bar Exit Fill Priority:** Stop-first resolution. If a bar's range touches both stop and target, the stop loss executes first. Gap-through fills resolve at the worse of stop price or bar open (`source-reported`).
- **Alternative Exit Modes (Phase 5 Grid):**
  - `breakeven_1R`: Stop moves to entry price once favorable excursion reaches $+1.0R$ (`source-reported`).
  - `trail_swing`: Once price reaches $+1.0R$, profit target is removed and stop trails behind rolling 5-bar swing lows/highs (`source-reported`).
  - `partial_1R`: Exits 50% position at $+1.0R$, moves stop to breakeven, exits remainder at $+3.0R$ (`source-reported`).
  - `time_stop`: Exits at market close of trading session if neither stop nor target touched (`source-reported`).
- **Volatility Gate (Phase 5/6 Filter):**
  - 14-period True Range percentage ($\text{ATR} / \text{close} \times 100$). New entry skipped if ATR% is below training-window percentile threshold (`p25`, `p50`, or `p75`) (`source-reported`).

## Required data

- **Instruments:** CME equity index futures:
  - E-mini Nasdaq-100 (`NQ` / `NQ1!`), point value $20.00 USD/pt, tick size $0.25$ pt (`source-reported`).
  - E-mini S&P 500 (`ES` / `ES1!`), point value $50.00 USD/pt, tick size $0.25$ pt (`source-reported`).
  - E-mini Dow Jones (`YM` / `YM1!`), point value $5.00 USD/pt, tick size $1.00$ pt (`source-reported`).
- **Timeframe:** 1-minute OHLCV bars (`source-reported`).
- **Venue:** CME Globex (`source-reported`).
- **Session Hours:** Weekdays 09:30 to 10:30 America/New_York (regular trading hours opening drive) (`source-reported`).
- **Point-in-Time & Causality:**
  - Signals evaluated strictly on confirmed bar close at $t$.
  - Execution occurs at open of bar $t+1$.
  - Continuous rolling contract data must avoid look-ahead from backward adjustments or unadjusted contract roll jumps. Trades spanning a contract roll boundary are excluded (`source-reported`).
- **Timestamp Integrity Requirement:** Absolute synchronization with CME exchange clocks, requiring rigorous verification of Daylight Saving Time (DST) transitions (UTC-4 vs UTC-5) (`source-reported`).

## Execution assumptions

- **Fill Model:** Market order filled at open of bar $t+1$ (`open[t+1]`) (`source-reported`).
- **Transaction Costs & Slippage (Phase 5/6 Standard Cost Model):**
  - Commission: $\$5.00$ round-trip per contract ($\$2.50$ per side) (`source-reported`).
  - Slippage: 1 tick on entry fill + 1 tick on market exit fill (`source-reported`):
    - ES: 1 tick = $\$12.50$ per side ($\$25.00$ round-trip slippage; total RT cost $\$30.00$) (`source-reported`).
    - NQ: 1 tick = $\$5.00$ per side ($\$10.00$ round-trip slippage; total RT cost $\$15.00$) (`source-reported`).
    - YM: 1 tick = $\$5.00$ per side ($\$10.00$ round-trip slippage; total RT cost $\$15.00$) (`source-reported`).
- **Holding Period:** Median trade duration is 17 minutes (`source-reported`). Trades never carry overnight.
- **Capacity & Margin:** E-mini futures support multi-million dollar AUM with negligible market impact for single-contract execution during regular morning hours (`research-proposed`).

## Evidence

### Source-reported

All quantitative metrics below trace directly to committed project artifacts, logs, and JSON summaries (`aleks-drozy/fyp-trading-strategy` and `aleks-drozy/fyp-strategy-engine`):

#### 1. In-Sample Pine Script Claim (NQ1!, Jan 2025 – Feb 2026, `backtests/NQ1_optimised.csv`)

- Total Trades: `72` (`source-reported`).
- Win Rate: `56.94%` (41 winners, 31 losers) (`source-reported`).
- Profit Factor: `1.703` (`source-reported`).
- Total Net P&L: `+$28,400.00` (`source-reported`).
- Max Drawdown: `0.95%` (`source-reported`).
- Expectancy: `+$394.44` per trade (`source-reported`).

#### 2. Out-of-Sample Pine Script Test (NQ1!, March 2023 – Dec 2024, `backtests/NQ1_2023_2024`)

- Total Trades: `95` (`source-reported`).
- Win Rate: `37.89%` (36 winners, 59 losers) (`source-reported`).
- Profit Factor: `0.898` (`source-reported`).
- Total Net P&L: `-$4,600.00` (Gross Profit $\$40,335$ vs Gross Loss $\$44,935$) (`source-reported`).
- Expectancy: `-$48.42` per trade (`source-reported`).

#### 3. Phase 2 Python Bar-by-Bar Reimplementation vs. Real Logs (`WRITEUP_STRATEGY.md`)

- Evaluation of default parameters against real TradingView trade logs:
  - **Losing Window (2023–2024):**
    - Real Baseline: 95 trades, $-\$4,600$ PnL, PF `0.90`, WR `37.9%` (`source-reported`).
    - Generated Python: 376 trades, $-\$61,545$ PnL, PF `0.71`, WR `33.8%` (`source-reported`).
    - Trade Matching: 76 matched, 19 missed, 300 extra trades (Recall `0.80`, Precision `0.20`) (`source-reported`).
  - **Winning Window:**
    - Real Baseline: 59 trades, $+\$18,115$ PnL, PF `1.53`, WR `55.9%` (`source-reported`).
    - Generated Python: 179 trades, $+\$11,067.50$ PnL, PF `1.09`, WR `42.5%` (`source-reported`).
    - Trade Matching: 45 matched, 14 missed, 134 extra trades (Recall `0.76`, Precision `0.25`) (`source-reported`).
- Reimplementation Conclusion: High recall (76–80%) confirms correct directional mechanics, but low precision (20–25%) proves that the original track record depended on extreme tuning/discretionary filtering not present in the default rules (`source-reported`).

#### 4. Phase 4 Walk-Forward Optimization (`WRITEUP_PHASE4.md`, `phase4_results.json`)

- Grid: 144 parameter combinations (`fvg_threshold` $\in \{0.0, 0.02, 0.05\}$, `rr` $\in \{1.0, 1.5, 2.0, 3.0\}$, `ema_length` $\in \{10, 20, 50, 100\}$, `swing_lookback` $\in \{3, 5, 8\}$) across 4 rolling 12m-train / 6m-test folds spanning 2024–2025 (`source-reported`).
- Pre-Registered Success Rule Verification:
  - (a) Tuned stitched OOS PF $> 1.0$: **FAIL** (Actual: `0.9945`) (`source-reported`).
  - (b) Tuned minus default OOS PF margin $\ge 0.10$: **FAIL** (Actual: `+0.0747`) (`source-reported`).
  - (c) Tuned beats default in $\ge 3/4$ folds: **PASS** (`3/4` folds) (`source-reported`).
  - (d) Tuned beats median-combo selection-luck null: **PASS** (`0.9945 > 0.9396`) (`source-reported`).
- **Verdict:** `robust_improvement = FALSE` (statistically verified null result) (`source-reported`).
- Performance: Tuned cut net loss from $-\$20,362.50$ (401 trades) to $-\$907.50$ (233 trades) via 42% trade reduction, but failed to cross breakeven (`source-reported`).

#### 5. Phase 5 Exits, Volatility Filter & Costs (`WRITEUP_PHASE5.md`, `phase5_results.json`)

- Grid: 20 combinations of exit modes (`fixed_1_5R`, `breakeven_1R`, `trail_swing`, `partial_1R`, `time_stop`) $\times$ volatility filters (`off`, `p25`, `p50`, `p75`), net of costs (`source-reported`).
- Pre-Registered Success Rule Verification:
  - (a) Tuned net stitched OOS PF $> 1.0$: **PASS** (`1.0707`) (`source-reported`).
  - (b) Tuned minus base net PF margin $\ge 0.10$: **PASS** (`+0.1701`) (`source-reported`).
  - (c) Tuned beats base in $\ge 3/4$ folds: **PASS** (`3/4` folds) (`source-reported`).
  - (d) Tuned net PF $\ge$ 75th percentile of 20 combos: **PASS** (`1.0707 >= 1.0466`) (`source-reported`).
  - (e) Sample gate: $n \ge 60$ AND bootstrap CI 5th percentile $> 1.0$: **FAIL** ($n = 228$, but 5th pct lower bound is `0.807`) (`source-reported`).
- **Verdict:** `robust_improvement = FALSE` (null result stopped by statistical confidence gate) (`source-reported`).
- Root-Cause of Failure (Fold 4 Concentration):
  - Fold 4 alone generated `+$18,845.00` on 25 trades (OOS PF `2.248`, expectancy `+$753.80/trade`) (`source-reported`).
  - The other three folds combined lost `-$9,050.00` (F1 $-\$3,860$, F2 $-\$14,085$, F3 $+\$8,895$) (`source-reported`).
  - Without Fold 4, the strategy is deeply negative; bootstrap resampling accurately flagged the fragility (`source-reported`).

#### 6. Phase 6 Definitive Cross-Instrument Disproof (`WRITEUP_PHASE6.md`, `phase6_results.json`)

- Sample: ~10 years (2016–2025) of unadjusted CME 1-minute futures across 17 walk-forward folds each on `ES` and `YM`, plus independent clean `NQ` (`source-reported`).
- Configuration frozen under pre-registered hash `699fd485...` before runner execution (`source-reported`).
- Primary Statistical Test: Unit-risk net R-multiple profit factor with joint calendar-day cluster bootstrap ($B = 10,000$, seed 42) (`source-reported`).
- **Primary Disproof Result:**
  - Pooled ES + YM net R-multiple Profit Factor: **`0.905`** (`0.905486`) across 1,402 OOS trades over 1,005 trade-days (`source-reported`).
  - Joint Day-Cluster Bootstrap 90% Confidence Interval: **`[0.8095, 0.9957]`** (`source-reported`).
  - Clause Fired: The upper bound (`0.9957`) is strictly below $1.0$ (breakeven). With $\ge 90\%$ statistical confidence, the strategy loses money net of costs on independent data (`source-reported`).
  - **Verdict:** **`DISPROVEN`** (`source-reported`).
- Instrument Breakdown:
  - **ES:** Tuned R-PF `0.847` (574 trades, net $-\$21,347.50$) vs Base R-PF `0.829` (1,527 trades, net $-\$39,735.00$) (`source-reported`).
  - **YM:** Tuned R-PF `0.948` (828 trades, net $-\$9,435.00$) vs Base R-PF `0.876` (1,624 trades, net $-\$19,675.00$) (`source-reported`).
  - **Clean NQ Replication:** Tuned R-PF `0.851` (914 trades, net $-\$82,438.00$) vs Base R-PF `0.899` (1,726 trades, net $-\$96,798.00$). Tuned was worse than base (`nq_agreement = False`) (`source-reported`).
- Fixed Replication Arm Verification:
  - Arm B1 (`partial_1R + p50`): Pooled R-PF `0.904`, Bonferroni 2.5th pct lower bound `0.781` ("not supported") (`source-reported`).
  - Arm B2 (`trail_swing + p50`): Pooled R-PF `0.836`, Bonferroni 2.5th pct lower bound `0.716` ("not supported") (`source-reported`).
- Cost Sensitivity:
  - At **0.0x cost** (zero commissions, zero slippage), ES is still negative (R-PF `0.983`), while YM is barely above breakeven (`1.058`) (`source-reported`).
  - At **2.0x cost**, ES drops to `0.733` and YM drops to `0.851` (`source-reported`).
- Subperiod & Regime Invariance:
  - Pre-2020 Pooled R-PF: `0.871` (423 trades) (`source-reported`).
  - Post-2020 Pooled R-PF: `0.922` (979 trades) (`source-reported`).
  - Excluding 2023+ Formation Era: `0.898` (1,048 trades) (`source-reported`).
  - NQ Pre-2023: `0.887`; NQ Post-2023: `0.735` (`source-reported`).
  - The strategy loses in every single historical subperiod slice (`source-reported`).

### Independently reproduced

- `Not independently reproduced.`

### Negative evidence

1. **Statistically Certified Disproof:**
   - The primary research program constitutes a rigorous, pre-registered disproof. The pooled net R-multiple profit factor across independent instruments is $0.905$ with an upper confidence bound of $0.996 < 1.0$, definitively rejecting the hypothesis of a tradable edge.
2. **Gross Unprofitability on Benchmark Equities:**
   - Even assuming zero commissions and zero slippage ($0\times$ costs), the tuned strategy fails to achieve profitability on the E-mini S&P 500 (R-PF $0.983$). The underlying entry signal provides negative gross expectancy.
3. **Forensic Identification of Timestamp Defects (The ±60-Minute DST Bug):**
   - The program proved that 104 days in the widely used Kaggle NQ 1-minute dataset suffered from a 1-hour timestamp displacement. The strategy appeared to perform well because it was inadvertently executing during mid-day regular trading sessions rather than the stated opening drive.
4. **Failure of Walk-Forward Optimization:**
   - Parameter sweeps across 144 combinations in Phase 4 and 20 exit/filter combinations in Phase 5 failed pre-registered acceptance criteria. In-sample optimization merely fit noise and concentrated sample luck.

## Falsification plan

### Pre-Registered Program Decision Criteria & Audit Thresholds

1. **Cross-Instrument Pooled CI Disproof Rule (`research-defined falsification threshold`):**
   - *Test:* Compute unit-risk net R-multiples across independent instruments (`ES`, `YM`) using a joint calendar-day cluster bootstrap ($B = 10,000$ resamples, carrying both instruments simultaneously).
   - *Rule:* If the 90% confidence interval upper bound $\le 1.0$, the hypothesis is certified `DISPROVEN`. (Condition satisfied in Phase 6: upper bound $0.9957 < 1.0$).
2. **In-Sample Selection Luck Null Gate (`research-defined falsification threshold`):**
   - *Test:* For each walk-forward fold, evaluate the full parameter grid on out-of-sample data to establish a selection-luck distribution.
   - *Rule:* Reject the optimization process if the selected configuration fails to exceed the 75th percentile of the grid's out-of-sample distribution across folds.
3. **Concentration & Subperiod Robustness Gate (`research-defined falsification threshold`):**
   - *Test:* Perform a leave-one-out fold ablation on out-of-sample cumulative P&L.
   - *Rule:* Reject profitability claims if more than 80% of net cumulative returns depend on a single fold or if excluding any single fold turns cumulative P&L negative. (Demonstrated in Phase 5: Fold 4 alone generated $192\%$ of total net returns).
4. **Friction Invariance Stress Test (`research-defined falsification threshold`):**
   - *Test:* Measure strategy performance at $0.0\times$, $1.0\times$, and $2.0\times$ standard transaction costs ($1\text{ tick slippage} + \$5\text{ RT commission}$).
   - *Rule:* Disprove tradability if the strategy requires zero transaction costs to achieve PF $\ge 1.0$, or if gross profit factor at $0.0\times$ cost is $< 1.10$.

## Crypto portability

- **Portability Classification:** `adapted / unproven`.
- **Structural Differences & Failure Vulnerabilities in Crypto:**
  - *Absence of Cash Market Opening Auction:* The core rationale of the strategy is built around the 09:30 America/New York equity opening cross and subsequent institutional order-flow imbalances. In 24/7 cryptocurrency perpetual markets (Binance, Bybit, OKX), there is no centralized opening bell; volatility is distributed across global timezone handoffs (Asia open, London open, NY open).
  - *Higher Friction & Spread-to-ATR Ratios:* In CME E-mini futures, bid-ask spreads are tightly compressed to 1 tick ($0.25$ pt on ES/NQ). In crypto perpetuals, volatile 1-minute order-book imbalances incur substantial taker fees ($2$–$5\text{ bps}$) and volatile bid-ask bounce.
  - *Perpetual Funding Drag:* Any multi-hour hold in crypto perps risks adverse funding rate shocks during crowded momentum squeezes.
  - *Transfer Conclusion:* Given that the IFVG-CISD opening breakout model failed conclusively on the most liquid equity futures in the world, porting this exact logic to crypto perpetuals without external structural flow is strongly unproven and highly likely to fail.

## Limitations

1. **Discrete Bar Fill Approximation:**
   - The Python backtest engine simulates order fills at the open of bar $t+1$ (`next_open`) on 1-minute aggregates rather than simulating tick-by-tick queue priority in the CME Central Limit Order Book (`execution limitation`).
2. **Unadjusted Futures Continuation Splicing:**
   - Evaluating multi-year futures strategies requires handling quarterly expiration rolls. While intra-day price patterns are invariant to levels, cross-roll holding periods require contract roll masking (`data limitation`).
3. **Retail SMC Heuristic Fragility:**
   - "Smart Money Concepts" rules (IFVG, CISD) lack formal continuous mathematical definitions and rely on arbitrary threshold conventions (e.g., 3-bar gap checks, 8-bar swing lookbacks, 10-bar gap expiry) (`methodological limitation`).
4. **Vendor Dataset Contamination:**
   - The presence of the ±60-minute DST error in the initial Phase-1 dataset highlights the severe hazard of unverified third-party historical intraday data (`data quality limitation`).

## Implementation status

- Frontmatter: `implementation_status: not-implemented`.
- This record captures external published academic and open-source research from Aleksander Drozdz and Dr. Phil Maguire (Maynooth University, 2026).
- No implementation exists in our proprietary quantitative research stack, `nautilus-quant-system`, PyBroker, or NautilusTrader.
- This research capture does not authorize strategy development, backtesting campaigns, paper trading, testnet, or live trading.

## Adoption boundary

- Frontmatter: `status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.
- This record captures a negative result and definitive empirical disproof.
- Presence in this repository confirms that the retail SMC IFVG-CISD breakout hypothesis has been thoroughly audited and falsified, establishing an authoritative negative evidence barrier against deploying similar heuristic opening breakout models.

## Related Wiki records

- `[[tradingview-choppiness-donchian-breakout-filter-2026-09-16]]` (TradingView breakout filter and choppiness gating)
- `[[retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11]]` (Microstructure signal falsification of retail order-flow patterns)
- `[[trend-fib-extension-mechanical-pivot-null-edge-falsification-2026-09-14]]` (Mechanical pivot null-edge falsification)
- `[[retail-signal-three-gate-falsification-oscillator-volume-calendar-trend-2026-09-04]]` (Three-gate retail indicator falsification)
- `[[us-equity-vortex-top2-cross-sectional-trend-phase-robustness-2026-09-13]]` (Walk-forward robustness and parameter decay testing)

## Sources

- Aleksander Drozdz and Phil Maguire, *"FYP Trading Strategy"*, GitHub repository `aleks-drozy/fyp-trading-strategy`, commit `607355e02b2562e8705d2f34228d7aa44b8cd711`, Maynooth University Department of Computer Science, 2026.
  - Repository URL: https://github.com/aleks-drozy/fyp-trading-strategy
  - Pine Script Source: https://github.com/aleks-drozy/fyp-trading-strategy/blob/main/FYP_Bot_1.pine
  - In-Sample Trade Log: https://github.com/aleks-drozy/fyp-trading-strategy/blob/main/backtests/NQ1_optimised.csv
  - Out-of-Sample Trade Log: https://github.com/aleks-drozy/fyp-trading-strategy/blob/main/backtests/NQ1_2023_2024
- Aleksander Drozdz and Phil Maguire, *"fyp-strategy-engine"*, GitHub repository `aleks-drozy/fyp-strategy-engine`, commit `5a435c62ba9c7bad38f4921936a4b535c229d4e1`, Maynooth University Department of Computer Science, 2026.
  - Repository URL: https://github.com/aleks-drozy/fyp-strategy-engine
  - Pre-Registration Freeze Hash: `docs/phase6_freeze.json` (SHA256: `699fd485e56eeea364c197bc6b47d624ed9939e99c781f87320d93cc09376ed8`)
  - Phase 2 Strategy Engine Writeup: https://github.com/aleks-drozy/fyp-strategy-engine/blob/master/WRITEUP_STRATEGY.md
  - Phase 4 Walk-Forward Optimization Writeup: https://github.com/aleks-drozy/fyp-strategy-engine/blob/master/WRITEUP_PHASE4.md
  - Phase 5 Exits, Volatility Filter, and Costs Writeup: https://github.com/aleks-drozy/fyp-strategy-engine/blob/master/WRITEUP_PHASE5.md
  - Phase 6 Cross-Instrument Confirmation & Disproof Writeup: https://github.com/aleks-drozy/fyp-strategy-engine/blob/master/WRITEUP_PHASE6.md
  - Empirical Phase 6 Result JSON: https://github.com/aleks-drozy/fyp-strategy-engine/blob/master/phase6_results.json
