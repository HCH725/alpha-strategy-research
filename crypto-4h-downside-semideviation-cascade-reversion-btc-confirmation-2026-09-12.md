---
schema: strategy-research-record-v1
title: Crypto 4h Downside-Semideviation Liquidation Cascade Reversion with Bitcoin-Drop Confirmation
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - okx
  - kraken
  - liquidation-cascade
  - mean-reversion
  - downside-semideviation
  - walk-forward
  - deflated-sharpe
status: research-only
confidence: medium
source_as_of: 2026-09-11
sources:
  - "loveolu, 'Crypto strategy research: a validation gate that says no', GitHub repository loveolu/crypto-strategy-research, commit 3059293e5edbc1a429c77fec9ff94957d94604a8, published September 2026, as-of 2026-09-11"
  - "loveolu, 'B2Cascade4h Freqtrade Strategy Implementation', user_data/strategies/B2Cascade4h.py, commit 3059293e5edbc1a429c77fec9ff94957d94604a8"
  - "loveolu, 'B2Cascade4h Forward-Paper Plan & Port-Parity Audit', research/experiments/B2_FORWARD_PAPER_PLAN.md, commit 3059293e5edbc1a429c77fec9ff94957d94604a8, dated 2026-09-05"
  - "loveolu, 'Current Crypto Research Report — Through CRYPTO-EXP-040', research/experiments/RESEARCH_REPORT_2026-09-04_CURRENT.md, commit 3059293e5edbc1a429c77fec9ff94957d94604a8, dated 2026-09-04"
  - "loveolu, 'Research Report — Top 3 After Walk-Forward (CRYPTO-EXP-012 → 015)', research/experiments/RESEARCH_REPORT_2026-09-05_top3.md, commit 3059293e5edbc1a429c77fec9ff94957d94604a8, dated 2026-09-05"
  - "loveolu, 'Handoff and Validation Pipeline Guide', HANDOFF.md, commit 3059293e5edbc1a429c77fec9ff94957d94604a8"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto 4h Downside-Semideviation Liquidation Cascade Reversion with Bitcoin-Drop Confirmation

## Provenance

- **Author / Research Lab:** `loveolu` (`love.olu33@gmail.com`), systematic crypto research initiative on OKX and Kraken perpetual futures.
- **Title:** *Crypto strategy research: a validation gate that says no* / Strategy `B2Cascade4h` (Candidate from `CRYPTO-EXP-013`).
- **Canonical Repository:** `https://github.com/loveolu/crypto-strategy-research`
- **Immutable Commit SHA:** `3059293e5edbc1a429c77fec9ff94957d94604a8`
- **Source As-Of Date:** 2026-09-11 (experiments finalized through 2026-09-05).
- **Primary Source Code & Documentation Paths:**
  - Production / Freqtrade Strategy: `user_data/strategies/B2Cascade4h.py`
  - Forward-Paper & Port-Parity Audit: `research/experiments/B2_FORWARD_PAPER_PLAN.md`
  - Consolidated Research Report: `research/experiments/RESEARCH_REPORT_2026-09-04_CURRENT.md`
  - Walk-Forward Leaderboard Report: `research/experiments/RESEARCH_REPORT_2026-09-05_top3.md`
  - Experiment Ledger & Leaderboard: `research/experiments/LEADERBOARD.md`
  - Research Handoff & Validation Standard: `HANDOFF.md`
  - DSR Engine: `freqtrade_dsr.py` (Bailey & López de Prado 2014)
- **Licence & Rights:** Strategy code and research documents are published under the MIT / AGPL-3.0 licenses (extracted from a Freqtrade fork, original research paths retained). No proprietary or private invite-only scripts involved.
- **Deduplication Audit:** Repository-wide inspection confirms zero prior records citing `loveolu/crypto-strategy-research`, `B2Cascade4h`, or `downside-semideviation` ranking. Existing records in `alpha-strategy-research` referencing liquidation cascades (`crypto-perpetual-liquidation-cascade-overshoot-reversal-2026-08-31.md` and `crypto-perpetual-liquidation-cascade-early-warning-taker-flow-variance-2026-09-01.md`) rely on high-frequency 1-minute order book L2 feeds, tick liquidation trade z-scores, and open-interest contraction data. In contrast, `B2Cascade4h` is a sparse 4h multi-bar OHLCV construct operating on 42-bar downside semideviation percentile ranks, market-wide BTC liquidation-drop conditioning, and dual moving-average trend gates.

## Economic mechanism

### Source-reported

In cryptocurrency perpetual futures, severe intra-day price declines frequently trigger mechanical cascades as automated exchange liquidation engines forcefully market-sell underwater long positions to protect exchange solvency. 

The author establishes two critical empirical distinctions regarding these cascades:
1. **Market-Wide vs. Idiosyncratic Cascades:** Uncorrelated, single-altcoin price crashes are overwhelmingly driven by fundamental negative news, project failures, or token-specific dumping, which tend to persist rather than bounce. Conversely, concurrent crashes where Bitcoin also drops (`btc_mom_24h < 0.0`) reflect broad, market-wide leverage flushes and liquidation contagion across cross-margined accounts. Once forced liquidation volume subsides, non-informational price overshoot mean-reverts.
2. **Regime Preservation via Trend Gates:** Dip-buying liquidation cascades during structural bear markets is severely unprofitable (bull beta masquerading as alpha). Enforcing a macro trend regime filter (completed daily close above the 200-day SMA, with 20-day EMA above 50-day EMA) ensures that long reversion entries only occur when the structural market trend is upward, shielding capital during prolonged multi-month drawdowns.

### Research interpretation

This strategy captures a **structural liquidity-shock mean-reversion anomaly** conditioned on **macro regime alignment**:
- **Downside Semideviation as a Pure Tail Measure:** Unlike standard standard deviation or ATR (which treat upside explosive momentum symmetrically with downside crashes), rolling downside semideviation ($DSD_{42}$) isolates downside return dispersion. Converting $DSD_{42}$ into an empirical percentile rank ($DSD_{pct}$) over a trailing 180-bar window (30 days) establishes an adaptive, scale-free threshold for extreme tail selloffs without curve-fitting absolute dollar or percentage volatility.
- **Component Roles in the Hybrid Architecture:**
  - *Regime Filter:* Daily $SMA_{200}$ and $EMA_{20} > EMA_{50}$ trend filter acting as a hard capital preservation gate.
  - *Primary Signal:* 4h Downside semideviation percentile ($\ge 0.80$) combined with short-term price dislocation ($\le -3.85\%$ over 24h).
  - *Confirmation Filter:* Market-wide liquidation confirmation via Bitcoin negative 24h return ($BTC\_ROC_{24h} < 0.0$), pruning un-reverting idiosyncratic altcoin collapses.
  - *Risk / Exit Mechanism:* Recovery exit when downside dispersion normalizes below the median ($DSD_{pct} < 0.50$) or a hard 28-hour open-to-open time stop (`time_stop_28h`), combined with a 1-candle post-exit cooldown.

## Signal

### Formation timestamp

Signals are evaluated at the close of each completed UTC 4h candle $T$. Orders are placed for execution at the open of the subsequent 4h candle $T+1$ (`next-bar execution`). To eliminate look-ahead bias from higher-timeframe data, completed daily indicators are strictly lagged by an informative offset of one full 4h candle (ensuring the daily gate is evaluated only on completed daily candles closed at 00:00 UTC).

### Mathematical Definition of Indicators

1. **Simple Returns:**
   $$r_t = \frac{P_t}{P_{t-1}} - 1$$
   where $P_t$ is the 4h candle close price.

2. **Downside Semideviation ($DSD_{42}$):**
   Evaluated over a rolling lookback of $W = 42$ 4h bars (7 days):
   $$DSD_{42, t} = \sqrt{\frac{1}{42} \sum_{i=0}^{41} \min(r_{t-i}, 0)^2}$$

3. **Downside Semideviation Percentile Rank ($DSD_{pct}$):**
   Calculated over a rolling percentile window of $PW = 180$ 4h bars (30 days):
   $$DSD_{pct, t} = \text{PercentileRank}_{180}(DSD_{42, t}) \in [0.0, 1.0]$$

4. **24h Rolling Momentum ($ROC_{24h}$):**
   Evaluated over 6 consecutive 4h bars (24 hours):
   $$ROC_{24h, t} = \frac{P_t}{P_{t-6}} - 1$$

5. **Bitcoin 24h Market Rebound / Confirmation Momentum ($BTC\_ROC_{24h}$):**
   $$BTC\_ROC_{24h, t} = \frac{P^{BTC}_t}{P^{BTC}_{t-6}} - 1$$

6. **Daily Macro Trend Gate Indicators:**
   Evaluated on completed 1d candles:
   $$SMA200_{1d, \tau} = \frac{1}{200} \sum_{k=0}^{199} P^{1d}_{\tau-k}$$
   $$EMA20_{1d, \tau} = \text{EMA}_{20}(P^{1d}_\tau), \quad EMA50_{1d, \tau} = \text{EMA}_{50}(P^{1d}_\tau)$$

### Entry Triggers

A long entry order (`b2_cascade`) is submitted at the open of candle $T+1$ if all of the following conditions are simultaneously satisfied at the close of candle $T$:
1. $DSD_{pct, T} \ge 0.80$ (Downside semideviation is in the top 20th percentile of the trailing 30-day distribution).
2. $ROC_{24h, T} \le -0.0385$ (Instrument 24h return drops by $-3.85\%$ or worse).
3. $BTC\_ROC_{24h, T} < 0.0$ (Bitcoin 24h return is strictly negative, confirming market-wide cascade).
4. $P^{1d}_{\text{completed}} > SMA200_{1d}$ (Completed daily close price is above the 200-day daily SMA).
5. $EMA20_{1d} > EMA50_{1d}$ (20-day daily EMA is above the 50-day daily EMA).
6. $Volume_T > 0.0$ (Trading volume is non-zero).

Short positions are disabled (`can_short = False`).

### Exit Triggers

A position is closed at the open of the next bar following the occurrence of either condition:
1. **Dispersion Recovery Exit (`dispersion_recovered`):**
   $$DSD_{pct, t} < 0.50$$
   (Downside volatility recedes below the trailing 30-day median).
2. **Time Stop Exit (`time_stop_28h`):**
   $$\text{ElapsedTime} \ge 28 \text{ hours}$$
   Corresponding to 7 completed 4h open-to-open intervals.

### Post-Exit Protection

A `CooldownPeriod` of 1 candle (4 hours) is enforced immediately following trade exit to prevent re-entering on residual signals generated during the exit bar.

### Parameters

| Parameter | Value | Source Classification |
|---|---|---|
| Downside Semideviation Window ($W$) | 42 4h bars (7 days) | Source-reported |
| Percentile Lookback Window ($PW$) | 180 4h bars (30 days) | Source-reported |
| DSD Entry Threshold ($DSD_{\text{entry}}$) | $\ge 0.80$ | Source-reported |
| 24h Momentum Lookback | 6 4h bars (24 hours) | Source-reported |
| Momentum Entry Threshold ($ROC_{\text{entry}}$) | $\le -0.0385$ ($-3.85\%$) | Source-reported (walk-forward fit) |
| BTC Confirmation Threshold ($BTC\_ROC$) | $< 0.0$ | Source-reported |
| Daily Trend SMA Window | 200 daily bars | Source-reported |
| Daily Fast EMA Window | 20 daily bars | Source-reported |
| Daily Slow EMA Window | 50 daily bars | Source-reported |
| DSD Exit Threshold ($DSD_{\text{exit}}$) | $< 0.50$ | Source-reported |
| Maximum Holding Duration | 28 hours (7 4h candles) | Source-reported |
| Post-Exit Cooldown Period | 1 candle (4 hours) | Source-reported |
| Informative Gate Shift | 4 hours / 1 candle offset | Source-reported |
| Execution Order Type | Market order at bar open | Source-reported |
| Taker Transaction Fee Override | 9.0 bps per side ($0.0900\%$) | Source-reported |
| Target Position Sizing | Equal fraction (1/9th capital per coin) | Source-reported |
| Fixed Stake Simulation | 500 USDT / position (5,000 USDT book) | Source-reported |
| Margin / Leverage | 1.0x unleveraged long-only | Source-reported |
| Minimum 24h Volume Cutoff | Top 9 OKX perpetuals by liquidity | `research-proposed` |
| Slippage Model | 2.3 bps half-spread / book-walk | `research-proposed` |
| Portfolio Capacity Ceiling | $1.0\text{M}–$5.0\text{M} USD | `research-proposed` |

## Required data

- **Instruments:** OKX USDT Perpetual Contracts for 9 major liquid cryptocurrency assets:
  `BTC/USDT:USDT`, `ETH/USDT:USDT`, `SOL/USDT:USDT`, `BNB/USDT:USDT`, `XRP/USDT:USDT`, `ADA/USDT:USDT`, `AVAX/USDT:USDT`, `DOT/USDT:USDT`, `LINK/USDT:USDT`.
  (Independent cross-exchange validation conducted on Kraken perpetual futures: `BTC`, `ETH`, `SOL`, `ADA`, `DOT`, `LINK`, `XRP`).
- **Venue:** OKX Perpetual Swaps (primary); Kraken Futures (transfer test).
- **Market Type:** Centralized exchange linear USDT-margined perpetual futures.
- **Timeframe:** 4h candle OHLCV for signal generation; 1d candle OHLCV for daily trend regime filters.
- **Required Fields:** `open`, `high`, `low`, `close`, `volume`, and `date` (UTC timestamp).
- **Point-in-Time Availability:** The 4h informative shift ensures that 1d candle closes (00:00 UTC) are not accessed before the 00:00 4h candle boundary, preventing intra-day look-ahead bias.
- **Data Integrity Manifest:** All historical OHLCV series verified against exchange archives via SHA-256 hash manifest (`research/DATA_INTEGRITY_AUDIT_2026-09-08.md`).
- **Missing-Data Handling:** Incomplete candles dropped; historical delisted tokens preserved in backtest panel without forward imputation.

## Execution assumptions

- **Execution Timing:** Next-bar open execution. Signal evaluated at close of candle $T$ triggers market order fill at open of candle $T+1$.
- **Order Type:** Taker market orders on both entry and exit.
- **Transaction Costs:** 9.0 basis points ($0.0900\%$) per side (18.0 bps round trip), derived from OKX order-book depth analysis under a $5,000 notional order size (base taker 5.0 bps + half-spread + book-walk slippage).
- **Slippage & Impact:** Stress-tested at 1x, 2x, and 3x taker costs (up to 54.0 bps round trip); book-walk impact modeled from 360 L2 order book snapshots.
- **Leverage / Margin:** 1.0x unleveraged notional exposure. Long-only; no short selling, short margin borrow, or liquidation risk assumed.
- **Position Allocation:** At most 9 concurrent positions, each sized at $1/9$ of portfolio equity (or 500 USDT in a 5,000 USDT test account).
- **Execution Delay Tolerance:** Tested with 1-bar (4h) and 2-bar (8h) execution latency delays.
- **Capacity:** Estimated by research desk at $1\text{M}–$5\text{M} USD portfolio AUM (`research-proposed`); higher order sizes face wider book-walk impact during severe market-wide liquidation spikes.

## Evidence

### Source-reported

All quantitative performance figures are directly extracted from the primary source research reports: `research/experiments/RESEARCH_REPORT_2026-09-04_CURRENT.md` and `research/experiments/RESEARCH_REPORT_2026-09-05_top3.md` over the sample period **2023-01-22 to 2026-09-01** (3.6 years):

#### 1. True Rolling Walk-Forward Results (11 Windows)
- **Protocol:** 12-month train / 3-month test / 3-month step, rolling over 11 out-of-sample windows, re-fitting only the momentum threshold.
- **Cumulative Net Return:** **+40.6%**
- **Annualized Return:** **+13.9%**
- **Sharpe Ratio (annualized):** **1.23**
- **Sortino Ratio:** **3.54**
- **Maximum Drawdown:** **−5.5%**
- **Calmar Ratio:** **2.55**
- **Positive Windows:** **6 / 11** windows positive (3 windows had zero trades due to regime lockouts).
- **Return by Year:**
  - 2024: **+37.3%**
  - 2025: **+1.9%**
  - 2026: **+0.5%**
  - Last 365 Days: **+1.6%**

#### 2. Fixed Out-of-Sample Split (21 Months)
- **Sample Window:** 2024-11-22 to 2026-09-01 (held-out test segment).
- **Net Return:** **+30.8%** (expectancy: **+149 bps / trade**)
- **Sharpe Ratio:** **1.42**
- **Profit Factor:** **1.97**
- **Trade Count:** **168 trades**
- **Win Rate:** **63.0%**
- **Mean Holding Duration:** **28 hours**

#### 3. Real Freqtrade 2026.5 Engine Parity Run (Full 3.6-Year History)
- **Parity Verification:** Exact **368 / 368** entry and exit timestamps matched between the research harness and the production Freqtrade engine across all 9 coins.
- **Fixed Stake ($500 / position):** Cumulative return **+59.08%**, CAGR **13.71%**, Sharpe **1.45**, Sortino **2.07**, Profit Factor **2.22**, Max Drawdown **−5.95%**.
- **Fractional Allocation (1/9th exposure):** Cumulative return **+88.35%**, Max Drawdown **−10.49%**.

#### 4. Independent Exchange Transfer (Kraken Perpetual Futures)
- Evaluated on 7 perpetual pairs (`BTC`, `ETH`, `SOL`, `ADA`, `DOT`, `LINK`, `XRP`):
- **Trade Count:** **259 trades**
- **Net Cumulative Return:** **+82.06%** (**18.06% annualized**)
- **Sharpe Ratio:** **1.35**
- **Sortino Ratio:** **2.98**
- **Profit Factor:** **2.09**
- **Maximum Drawdown:** **−13.16%**
- **Coin Breadth:** **7 / 7** coins net positive.

#### 5. Robustness, Cost, and Delay Stress Tests
- **Top-5% Trade Removal:** Dropping the top 5% most profitable trades leaves **+13.3%** net return (proves edge is not driven by single-trade outliers).
- **3x Taker Cost Stress (27 bps/side):** Annualized Sharpe remains **1.17** on walk-forward.
- **Execution Latency Delay:**
  - 1-bar delay (4h): Sharpe drops to **0.97**.
  - 2-bar delay (8h): Sharpe drops severely to **0.18**.
- **Regime Conditional Breakdown:**
  - High-volatility regime: **+32%** annualized
  - Low-volatility regime: **−2%** annualized
  - Bull regime: **+37%** annualized
  - Bear regime: **−2%** annualized

#### 6. Deflated Sharpe Ratio & Multiple Testing Audit (Bailey & López de Prado 2014)
- **Daily Deflated Sharpe Ratio (DSR):** Under 200 cumulative project trials, walk-forward daily DSR is **0.543** (fails the pre-registered 0.95 hurdle).
- **Block Bootstrap (10,000 draws):** $P(\text{Sharpe} > 0) = 0.975$.

### Independently reproduced

Not independently reproduced. All empirical metrics and parity verifications are source-reported by `loveolu` (2026).

### Negative evidence

The primary source explicitly details material negative findings and structural fragilities:
1. **Severe Multi-Testing Deflation:** While the unadjusted walk-forward Sharpe is 1.23, the Deflated Sharpe Ratio is only **0.543** at 200 cumulative experiment trials, failing the pre-registered 0.95 gate. Roughly half of the backtested Sharpe is attributable to selection luck across the research program.
2. **Extreme 2024 Regime Concentration:** The strategy generated virtually all of its alpha during the 2024 crypto bull market (+37.3%). In 2025 (+1.9%) and 2026 (+0.5%), returns were essentially flat because the macro trend gate kept the system in cash (~45% time in cash). In bear regimes, annualized return is −2%.
3. **Execution Delay Sensitivity:** Liquidation cascades revert rapidly. Introducing an 8-hour (2-bar) execution delay erodes the Sharpe ratio from 1.23 down to 0.18, proving that late fills forfeit the bulk of the mean-reversion premium.
4. **Idiosyncratic Crash Failure:** In the S2 ablation (removing the Bitcoin-drop condition), trades triggered on single-token crashes suffered frequent continuation and higher drawdown (−10.4% vs −5.5%), demonstrating that isolated altcoin drops reflect unhedged project-specific impairment.
5. **No Capacity for Small-Cap Altcoins:** Tested strictly on top-9 liquid perpetuals; expanding into illiquid tokens during market crashes incurs severe market impact and slippage that eliminates the edge.

## Falsification plan

To falsify the 4h downside-semideviation liquidation cascade reversion hypothesis:
1. **Forward Paper Out-of-Sample Test:** Monitor the frozen `B2Cascade4h` implementation in forward dry-run mode until at least 100 closed trades accumulate.
   - *Falsification Condition:* If Profit Factor across two consecutive 90-day quarters falls below $1.0$, or if the forward Probabilistic Sharpe Ratio $PSR(\text{Sharpe} > 0) < 0.95$ (labeled `research-defined falsification threshold`), reject the live deployability of the strategy.
2. **Cross-Exchange Synchronous Fill Test:** Execute identical signals across Binance, OKX, and Bybit perpetual order books. If realized execution slippage exceeds 12.0 bps per side due to order book exhaustion during crashes (labeled `research-defined falsification threshold`), the net alpha thesis is falsified by market microstructure friction.
3. **Circular Date Permutation Placebo Test:** Apply the 999-draw event-block circular date shift to Bitcoin and altcoin price series while preserving marginal distributions. If the actual strategy Sharpe falls below the 95th percentile of the circular shift null distribution ($p > 0.05$; labeled `research-defined falsification threshold`), the predictive timing of the cascade trigger is falsified.
4. **Macro Downtrend Inversion Test:** Invert or remove the daily $SMA_{200}$ and $EMA_{20} > EMA_{50}$ trend gates during an out-of-sample bear market regime. If the un-gated cascade reversion strategy incurs a maximum drawdown exceeding $-25.0\%$ (labeled `research-defined falsification threshold`), confirm that the alpha is strictly regime-dependent dip-buying rather than an all-weather anomaly.

## Crypto portability

**Portability Classification: Direct.**

The strategy was designed, tested, and validated natively on cryptocurrency centralized perpetual futures (OKX and Kraken):
- **Native Alignment:** Linear USDT perpetual contracts feature automated liquidation engines with transparent liquidation waterfalls, directly creating the mechanical price dislocations exploited by the 4h downside semideviation signal.
- **24/7 Session Continuity:** 4h candle boundaries (00:00, 04:00, 08:00, 12:00, 16:00, 20:00 UTC) align with global 8-hour perpetual funding cycles and run uninterrupted over weekends.
- **Portability across Venues:** Independent transfer testing on Kraken confirmed that the signal generalises across major derivatives exchanges with comparable liquid book depth.
- **Portability Caveats:**
  - *Spot vs. Perpetual Basis:* On spot markets without leverage and automated liquidation engines, cascade intensity is significantly muted, reducing mean-reversion magnitude.
  - *DEX Perpetuals (Hyperliquid, dYdX):* On decentralized perpetual exchanges, oracle latency and liquidation keeper priority gas auctions create wider price dislocations, which may enhance gross alpha but incur higher MEV and execution risk.

## Limitations

- **Selection Bias & Deflated Sharpe:** Daily DSR of 0.543 reflects that ~95 prior strategy constructs were evaluated in the parent research initiative; historical metrics overstate out-of-sample forward expectancy.
- **Regime Dependency:** The strategy requires an active daily bull trend to trade; it produces zero or negligible returns during chop and prolonged bear cycles.
- **Lack of Intraday Tick Precision:** Evaluating signals on 4h candle boundaries aggregates intra-bar spikes; limit orders placed immediately at the liquidation bottom could potentially capture higher edge than next-open market orders.
- **Slippage Under Market Stress:** While 9 bps per-side taker fees were verified in standard order books, extreme systemic market crashes (e.g., March 2020 or FTX collapse) can cause order book blackouts where taker slippage exceeds 50 bps.
- **Capital Capacity Bounds:** Limited to major liquid contracts; scaling past $5M USD notional would require algorithmic VWAP/TWAP execution over multiple bars, conflicting with the fast 28-hour holding period.

## Implementation status

`not-implemented`. No implementation exists within our NautilusTrader, PyBroker, paper trading, testnet, or live production stack. This record represents an upstream academic research capture of open-source Freqtrade findings.

## Adoption boundary

`research-only` / `not-approved`.
Cataloged strictly for research knowledge handoff. Ingestion of this record does not constitute:
- Verification of positive expected net economic alpha;
- Approval for portfolio inclusion or capital allocation;
- Authorization for paper trading, testnet deployment, or live order execution.

Any future adoption requires independent historical reproduction on tick/order-book data, live forward execution tracking, and formal portfolio risk budgeting.

## Related Wiki records

- `[[crypto-perpetual-liquidation-cascade-overshoot-reversal-2026-08-31]]` — 1-minute order book L2 and tick liquidation cascade reversal.
- `[[crypto-perpetual-liquidation-cascade-early-warning-taker-flow-variance-2026-09-01]]` — High-frequency early warning cascade signals via taker flow variance.
- `[[extreme-negative-funding-contrarian-btc-return-2026-09-06]]` — Extreme negative funding contrarian reversals.
- `[[crypto-adaptive-trailing-stop-volatility-filtered-cointegrated-pairs-trading-2026-09-07]]` — Volatility-filtered cointegrated pairs trading in crypto perpetuals.
- `[[crypto-hyperliquid-momentum-funding-carry-combo-2026-09-12]]` — Cross-sectional momentum and funding carry combination in perpetuals.

## Sources

1. **loveolu (2026).** *Crypto strategy research: a validation gate that says no*. GitHub repository `loveolu/crypto-strategy-research`, commit `3059293e5edbc1a429c77fec9ff94957d94604a8`, dated 2026-09-11. Open-source under MIT and AGPL-3.0 licenses. URL: https://github.com/loveolu/crypto-strategy-research
2. **loveolu (2026).** *B2Cascade4h Freqtrade Strategy Implementation*. `user_data/strategies/B2Cascade4h.py`, commit `3059293e5edbc1a429c77fec9ff94957d94604a8`. Defines the mathematical indicators, entry/exit logic, informative lag shift, and cooldown protections.
3. **loveolu (2026).** *B2Cascade4h Forward-Paper Plan & Port-Parity Audit*. `research/experiments/B2_FORWARD_PAPER_PLAN.md`, commit `3059293e5edbc1a429c77fec9ff94957d94604a8`, dated 2026-09-05. Details the 368/368 trade parity audit against Freqtrade 2026.5 and forward paper gate criteria.
4. **loveolu (2026).** *Current Crypto Research Report — Through CRYPTO-EXP-040*. `research/experiments/RESEARCH_REPORT_2026-09-04_CURRENT.md`, commit `3059293e5edbc1a429c77fec9ff94957d94604a8`, dated 2026-09-04. Reports walk-forward metrics, Kraken transfer results, cost and latency stress tests, and selection-bias DSR calculations.
5. **loveolu (2026).** *Research Report — Top 3 After Walk-Forward (CRYPTO-EXP-012 → 015)*. `research/experiments/RESEARCH_REPORT_2026-09-05_top3.md`, commit `3059293e5edbc1a429c77fec9ff94957d94604a8`, dated 2026-09-05. Details comparative performance of B2 vs S2-strict, annual returns, and drawdown metrics across 2023–2026.
6. **loveolu (2026).** *Handoff and Validation Pipeline Guide*. `HANDOFF.md`, commit `3059293e5edbc1a429c77fec9ff94957d94604a8`. Summarizes cumulative trial counts, validation hurdles, and execution cost calibration.
7. **Bailey, D. H., & López de Prado, M. (2014).** *The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting, and Non-Normality*. Journal of Portfolio Management, 40(5), 94–107. Implemented in `freqtrade_dsr.py`.
