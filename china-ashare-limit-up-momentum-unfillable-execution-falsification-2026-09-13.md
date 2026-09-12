---
schema: strategy-research-record-v1
title: "Chinese A-Share Limit-Up Momentum: Unfillable One-Word Ceiling Falsification and Daily Cross-Sectional Reversal Breakdown"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - china-a-shares
  - price-limits
  - limit-up-chasing
  - execution-falsification
  - market-microstructure
  - fill-viability
  - negative-evidence
status: research-only
confidence: medium
source_as_of: 2026-09-11
sources:
  - "https://github.com/fkchaos/a-share-quant-sim/tree/2622c2dbccde5c0b05eb9089b891976f2cc6bf90"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Chinese A-Share Limit-Up Momentum: Unfillable One-Word Ceiling Falsification and Daily Cross-Sectional Reversal Breakdown

## Provenance

- **Author:** fkchaos (`https://github.com/fkchaos`)
- **Repository URL:** https://github.com/fkchaos/a-share-quant-sim
- **Full Immutable Commit SHA:** `2622c2dbccde5c0b05eb9089b891976f2cc6bf90`
- **Canonical Tree URL:** https://github.com/fkchaos/a-share-quant-sim/tree/2622c2dbccde5c0b05eb9089b891976f2cc6bf90
- **Commit Date:** 2026-09-11T10:38:09Z
- **Primary Source Files Examined:**
  - `README.md` (project architecture, single adapter execution invariant, walk-forward methodology, summary of 26 falsified strategies)
  - `docs/strategy/STRATEGIES_DISCARDED.md` (detailed post-mortems of falsified strategies, notably `v65` BigQuant yesterday's limit-up falsification and the systematic negative IC of 55+ daily reversal factors)
  - `docs/strategy/RESULTS_LOG.md` (experimental ledger across 15-fold walk-forward sweeps for `v66`, `v67`, `v75j`, `v39g`)
  - `scripts/strategies/v65_yesterday_limit.py` (implementation of BigQuant's two-day limit-up, concept heat, market-cap rank selection rules)
  - `scripts/strategies/v66_two_day_limit.py` (multi-factor integration adding two-day limit-up factor weight $W = 0.35$ to baseline)
  - `scripts/tools/v65_test.py` (full backtest harness implementing original BigQuant filters, commissions, stamp taxes, and slippage)
  - `scripts/tools/v65_test_no_concept.py` (unconstrained two-day limit-up momentum backtest without concept filtering)
  - `scripts/tools/v65_test_no_concept_v2.py` (critical ablation study filtering out unfillable one-word limit-up bars)
  - `scripts/tools/v66_test.py` and `scripts/tools/v66_test_no_one_word.py` (empirical walk-forward and full-sample evaluation of limit-up sentiment factors)
- **Repository Deduplication:** Audited all existing `.md` records in `alpha-strategy-research`. Zero prior records cite `fkchaos/a-share-quant-sim`, BigQuant limit-up chasing rules, or the unfillable one-word limit-up (`一字涨停板`) execution falsification. Adjacent records (`china-ashare-mask-first-upstream-contamination-adjusted-mse-2026-09-04.md`, `price-limit-retained-hidden-excess-memory-2026-09-11.md`) address statistical training-mask adjustments and Indian NSE circuit-breaker volatility memory, but do not provide a code-level empirical falsification of limit-up opening auction execution viability.

## Economic mechanism

### Source-reported

In mainland Chinese equity markets (Shanghai and Shenzhen exchanges), regulatory rules impose daily price fluctuation limits ($\pm 10\%$ for main-board stocks, $\pm 20\%$ for ChiNext and STAR market names). A popular retail and proprietary trading motif known as "limit-up chasing" (打板 / 昨日涨停策略, popularized on retail platforms such as BigQuant) posits that stocks achieving consecutive limit-up closes exhibit intense behavioral momentum, lottery-demand attention, and institutional price-discovery pressure. When such stocks open with an upward gap on day $T+1$, the strategy expects momentum continuation into day $T+2$, allowing traders to capture short-horizon premium with high turnover.

However, the author's primary research finding is that this apparent alpha is entirely an artifact of execution fillability blindness:
1. **The Phantom Alpha of One-Word Limit-Ups:** Naive daily-bar backtests that purchase stocks at the $T+1$ open report spectacular in-sample returns (+1115% total return, Sharpe 1.610). Crucially, this performance is driven almost entirely by "one-word limit-up" bars (一字涨停板, where $\text{Open} = \text{High} = \text{Low} = \text{Close} = +9.5\%\text{--}10\%$). In real market microstructure, such stocks open locked at the price ceiling during the 9:15–9:25 AM call auction, with millions of shares queued on the bid and zero willing sellers. Physical market orders cannot be filled.
2. **Post-Exclusion Performance Collapse:** When unfillable one-word limit-up sessions are filtered out (requiring $\text{Open} \neq \text{High}$ or $\text{Open} \neq \text{Low}$ so that actual two-sided trading occurred), the strategy suffers a catastrophic collapse from +1115% profit to -75.38% cumulative loss (Sharpe -0.824).
3. **Cross-Sectional Reversal Failure:** Across 55+ factor evaluations, the author further discovers that daily cross-sectional reversal factors (oversold oscillators, narrow consolidation breakouts, negative momentum) systematically yield negative Information Coefficients (IC) in A-shares. The short-term market regime is characterized by rapid momentum continuation or liquidity traps, rendering dip-buying counter-productive.

### Research interpretation

The fundamental friction underlying price-limit markets is the truncation of price discovery. In an unconstrained market, sudden positive information is immediately reflected via continuous price adjustment. Under an artificial daily $+10\%$ bound, price cannot reach equilibrium, creating order queue rationing.

When a stock opens at the limit ceiling ("one-word limit-up"):
- Uninformed liquidity takers face extreme adverse selection: they can only get filled when negative news or institutional dumping breaks the limit ("炸板"), meaning fills occur selectively on losing trades.
- Conversely, when the stock continues to surge through consecutive limit-ups, buy queues are never executed.
- Backtests relying on daily OHLCV files treat the `Open` field as an unconstrained execution price, assuming infinite liquidity at the printed price. This introduces massive forward-looking execution contamination.
- Once fillability is conditioned on observable trading variance (requiring at least one non-limit print during the session), the strategy captures only the adverse-selection tail—buying failed breakouts that immediately mean-revert into severe losses on day $T+2$.

**Component Roles in the Evaluated Limit-Up Architecture:**
- **Regime / Eligibility Filter:** Exclude ST (special treatment), Beijing Stock Exchange, STAR market, low-turnover (< 5M RMB), and micro-caps (< 2B RMB) (`source-reported`).
- **Primary Momentum Trigger:** Consecutive two-day limit-up close ($\text{pct\_change} \ge 9.5\%$ on day $T-2$ and day $T-1$) (`source-reported`).
- **Confirmation Gate:** Popular concept heat rank $\ge 98\%$ (or $\ge 95\%$) over 3-day and 15-day trailing returns (`source-reported`).
- **Execution Gate (Original):** Morning call auction gap up $\ge 2\%$ (`source-reported`).
- **Fillability Filter (Ablation):** Explicit rejection of one-word limit-up bars ($\text{Buy} = \text{High} = \text{Low}$) (`source-reported`).
- **Exit Logic:** Fixed 1-day holding horizon with next-day open exit, plus $\pm 5\%$ bracket stops (`source-reported`).

## Signal

### Formation Timestamp
- Evaluated daily after market close at 15:00 CST (UTC+8) using closed daily bars (`source-reported`).
- Selection determines eligible buy candidates for execution at the following morning's market open (09:30 CST on day $T$) (`source-reported`).

### Lookback Windows
- Daily return calculation: 1-day close-to-close change (`pct_change(1)`) (`source-reported`).
- Concept heat momentum: 3-day (`pct_change(3)`) and 15-day (`pct_change(15)`) return ranks across the cross-section (`source-reported`).
- Market cap liquidity proxy: 20-day rolling average turnover amount (`amount_panel.rolling(20).mean()`) (`source-reported`).

### Exact Mathematical Definitions

1. **Limit-Up Identification:**
   $$\text{LimitUp}_{i, t} = \mathbb{I}\left(0.095 \le \frac{P_{i, t}^{\text{close}} - P_{i, t-1}^{\text{close}}}{P_{i, t-1}^{\text{close}}} \le 0.105\right) \quad (\text{source-reported})$$

2. **Two-Day Consecutive Limit-Up:**
   $$\text{TwoDayLimit}_{i, t} = \text{LimitUp}_{i, t} \land \text{LimitUp}_{i, t-1} \quad (\text{source-reported})$$

3. **Concept Heat Momentum Rank:**
   $$\text{Rank}_{3d}(i, t) = \text{PercentileRank}\left(\frac{P_{i, t}^{\text{close}}}{P_{i, t-3}^{\text{close}}} - 1\right) \quad (\text{source-reported})$$
   $$\text{Rank}_{15d}(i, t) = \text{PercentileRank}\left(\frac{P_{i, t}^{\text{close}}}{P_{i, t-15}^{\text{close}}} - 1\right) \quad (\text{source-reported})$$
   $$\text{ConceptHeat}_{i, t} = \frac{\text{Rank}_{3d}(i, t) + \text{Rank}_{15d}(i, t)}{2} \quad (\text{source-reported})$$

4. **Market-Cap Sizing Score:**
   $$\text{CapScore}_{i, t} = \text{Rank}_{\text{ascending}}\left(\frac{1}{20}\sum_{k=0}^{19} \text{Amount}_{i, t-k}\right) \quad (\text{source-reported})$$

### Entry Triggers and Conditions
On trading day $T$ morning call auction (using signals formed at $T-1$ close, observing past two limit-ups at $T-2$ and $T-1$):
- **Candidate Pool:** $\text{TwoDayLimit}_{i, T-1} == \text{True}$ (`source-reported`).
- **Concept Filter:** $\text{ConceptHeat}_{i, T-1} \ge \text{Quantile}_{0.98}(\text{ConceptHeat})$ (or $\ge 0.95$ in relaxed variant; or unconstrained in Variant C) (`source-reported`).
- **Turnover Filter:** Daily trading volume $\text{Amount}_{i, T-1} \ge 5,000,000\text{ RMB}$ and market capitalization $\ge 2,000,000,000\text{ RMB}$ (`source-reported`).
- **Ranking:** Candidates sorted by $\text{CapScore}$ ascending (prioritizing smaller-cap, higher-elasticity names) (`source-reported`).
- **Execution Condition:**
  $$\text{GapUp}_{i, T} = \frac{P_{i, T}^{\text{open}}}{P_{i, T-1}^{\text{close}}} - 1 \ge 0.02 \quad (\text{or } \ge 0.01\text{ in Variant C}) \quad (\text{source-reported})$$
- **Fillability Gate (The Crucial Falsification Condition):**
  $$\text{Fillable}_{i, T} = \neg \left(P_{i, T}^{\text{open}} == P_{i, T}^{\text{high}} == P_{i, T}^{\text{low}}\right) \quad (\text{source-reported})$$
  If $P_{i, T}^{\text{open}} == P_{i, T}^{\text{high}} == P_{i, T}^{\text{low}}$, the session is classified as an unfillable one-word limit-up; order generation is aborted (`source-reported`).

### Exit Rules
- **Holding Period:** Maximum 1 trading day (`HOLD_DAYS_MAX = 1`) (`source-reported`).
- **Exit Execution:** Unconditional market sell at day $T+1$ open (`opn.loc[date, code]`) (`source-reported`).
- **Intraday Bracket Stops:** Optional stop-loss at $-5.0\%$ (`STOP_LOSS = -0.05`) and take-profit at $+5.0\%$ (`TAKE_PROFIT = 0.05`) (`source-reported`).

### Position-Sizing Logic
- **Initial Portfolio Cash:** 200,000 RMB (`source-reported`).
- **Max Daily Buys:** Up to 3 names per day (`MAX_DAILY_BUY = 3`) (`source-reported`).
- **Max Portfolio Holdings:** 5 names (`MAX_HOLDINGS = 5`) (`source-reported`).
- **Per-Trade Allocation:** Fixed 20% of cash equity per position (`cash * 0.20`), rounded down to board lots of 100 shares (`int(amount / buy / 100) * 100`) (`source-reported`).

## Required data

- **Universe:** CSI 1800 index constituents (`zz1800`, combining CSI 300, CSI 500, and CSI 1000) representing liquid mainland Chinese equities (`source-reported`).
- **Exclusions:** Excludes ChiNext / STAR market (科创板, 20% limits), Beijing Stock Exchange (北交所, 30% limits), and ST / *ST distressed stocks (`source-reported`).
- **Timeframe:** Daily OHLCV bars (`source-reported`).
- **Fields Required:** `open`, `high`, `low`, `close`, `volume`, `amount` (`source-reported`).
- **Sample Period:** 2021-01-01 to 2026-06-24 (5.5 calendar years, ~1,325 trading sessions) (`source-reported`).
- **Data Vendor / Source:** Local SQLite cache populated via free public quote endpoints (BaoStock / Tencent Finance API) (`source-reported`).
- **Point-in-Time Discipline:** Daily bar features strictly reference bar $T-1$ and earlier closes; open prices are used only for order execution on day $T$ (`source-reported`).

## Execution assumptions

- **Execution Timing:** Buy orders executed at day $T$ open; sell orders executed at day $T+1$ open (`source-reported`).
- **Transaction Costs (Mainland A-Share Standard):**
  - Commission: 0.03% (万分之三, `COMMISSION = 0.0003`) on buys and sells (`source-reported`).
  - Stamp Tax (印花税): 0.10% (千分之一, `STAMP_TAX = 0.0010`) on sell orders only (`source-reported`).
  - Slippage: 0.10% (千分之一, `SLIPPAGE = 0.0010`) adverse price penalty on buys ($P_{\text{open}} \times 1.001$) and sells ($P_{\text{open}} \times 0.999$) (`source-reported`).
- **Shorting Availability:** None. Chinese A-shares follow a long-only regime for ordinary retail participants (`source-reported`).
- **Settlement Rule:** Mainland China $T+1$ trading rule (stocks purchased on day $T$ cannot be sold until day $T+1$) strictly enforced by 1-day minimum holding window (`source-reported`).
- **Liquidity / Price Limit Mechanics:**
  - Standard main-board limit bands: $\pm 10\%$ relative to prior close (`source-reported`).
  - One-word limit-up (`一字涨停板`): $\text{Open} = \text{High} = \text{Low} = \text{Close} = \text{LimitPrice}$. Trades cannot be physically executed due to order queue priority (`source-reported`).

## Evidence

### Source-reported

All quantitative metrics below trace directly to committed files in `fkchaos/a-share-quant-sim` (`docs/strategy/STRATEGIES_DISCARDED.md`, `docs/strategy/RESULTS_LOG.md`, `scripts/tools/v65_test_no_concept.py`, and `scripts/tools/v65_test_no_concept_v2.py` at commit `2622c2dbccde5c0b05eb9089b891976f2cc6bf90`):

#### 1. Falsification of Yesterday's Limit-Up Chasing Strategy (v65 / BigQuant Logic)
Evaluated on CSI 1800 (`zz1800`), 2021-01-01 to 2026-06-24:

| Configuration Variant | Total Return | Sharpe Ratio | Max Drawdown | Win Rate | Execution Realism Note |
|---|---|---|---|---|---|
| **BigQuant Original** (Concept $\ge 98\%$, Gap $\ge 2\%$) | **-29.33%** | **-0.028** | **-48.82%** | 49.4% | Direct retail loss under original parameters |
| **Relaxed Parameters** (Concept $\ge 95\%$, Gap $\ge 1\%$) | **+5.91%** | **0.200** | **-55.54%** | 49.5% | Marginally positive return, unviable risk |
| **Naive Momentum (No Concept Filter, Blind Fill)** | **+1115%** | **1.610** | (not reported) | (not reported) | **❌ Phantom returns from unfillable one-word limit-up opens** |
| **Realistic Fill (No Concept Filter, Exclude One-Word Limit-Up)** | **-75.38%** | **-0.824** | **-55.54%** | (not reported) | **彻底亏损 (Total collapse after removing unexecutable fills)** |

The source reports that omitting one-word limit-up filters causes backtests to simulate purchases on days where stocks gap to $+10\%$ at the opening print and remain locked there all day. Because such stocks often continue higher the next day, naive backtests record massive compounding gains (+1115%). In live trading, however, market orders are rejected or queued behind hundreds of millions of RMB in institutional priority queues. When the backtest enforces execution viability by skipping bars where `buy == buy_high == buy_low`, the strategy plunges into a severe -75.38% drawdown.

#### 2. Limit-Up Factor in Multi-Factor Walk-Forward (v66 vs. v39g Baseline)
Tested across 15 walk-forward folds (train = 252 days, test = 126 days, step = 63 days, CSI 1800, 2021–2026):

| Strategy | Average WF Return | Average WF Sharpe | Average WF Max Drawdown | Positive Folds |
|---|---|---|---|---|
| **v39g Baseline** (7-factor multi-factor model, $W_{\text{size}}=0.35$) | **+8.59%** | **1.189** | **-14.53%** | 11/15 (73%) |
| **v66 (+ Two-Day Limit-Up Factor $W=0.35$)** | **+7.56%** | **1.178** | **-13.70%** | 11/15 (73%) |

The author concludes that adding consecutive two-day limit-up as an explicit factor provides zero incremental alpha over the multi-factor baseline (Sharpe 1.178 vs. 1.189, return +7.56% vs. +8.59%).

#### 3. Systematic Breakdown of Daily Cross-Sectional Reversal Factors (v58a, v58b, v59a, v79, v80)
Evaluated across 55+ single-factor tests on CSI 1800 (2020/2021–2026, 5-day forward horizon):

| Factor Category | Tested Factor | Horizon | Mean Rank IC | Information Ratio (IR) | Empirical Outcome |
|---|---|---|---|---|---|
| **Price Oversold** | `drop_10d` | 20 days | -0.028 | -0.18 | Failed: negative IC (oversold stocks continue to bleed) |
| **Volatility Compression** | `atr_compression` | 20 days | -0.046 | -0.34 | Failed: negative IC (consolidation breakouts fail) |
| **Volume-Price** | Price-Volume Correlation (20d) | 5 days | -0.0266 | -0.2545 | Failed: negative IC (45.4% positive IC days) |
| **Capital Flow** | Net Fund Flow (close-open $\times$ vol) | 5 days | -0.0393 | -0.2782 | Failed: negative IC (~40% positive IC days) |
| **Valuation** | $PE_{\text{TTM}}$ | 5 days | -0.0324 | -0.2023 | Failed: negative IC (cheap stocks underperform) |
| **Valuation** | $PB$ | 5 days | -0.0481 | -0.2882 | Failed: negative IC |

The author documents the systematic conclusion:
> *"所有'逆向/反转/回归'因子在日频截面 IC 上全部为负... A 股短周期是动量延续而非反转的市场结构，任何截面 IC 选股的信号都极弱... 启示：不应继续在'A股日频截面 IC 挖掘'和'线性多因子选股'方向投入。"*
> *(All reversal / mean-reversion factors have negative daily cross-sectional IC... Chinese A-shares exhibit short-horizon momentum continuation rather than reversal; contrarian dip-buying is systematically unprofitable).*

### Independently reproduced

Not independently reproduced. All metrics and findings reflect third-party reported backtest logs, ablation test scripts, and markdown documentation committed by fkchaos in repository `fkchaos/a-share-quant-sim` (commit `2622c2dbccde5c0b05eb9089b891976f2cc6bf90`).

### Negative evidence

This repository provides code-level negative evidence against two widespread quantitative assumptions:
1. **The Limit-Up Backtesting Illusion:** Chasing consecutive limit-ups produces spectacular backtest profits only when the backtester ignores call-auction execution rationing. Realized performance drops by over 1,190 percentage points (+1115% to -75.38%) when physically unexecutable one-word limit-up opens are filtered out.
2. **Reversal / Dip-Buying Failure in A-Shares:** Contrary to equity literature from Western markets where short-term (1-week) reversal is often an established stylized fact, Chinese A-share daily cross-sections display negative reversal IC across 55+ technical factors. Buying oversold or consolidating stocks results in systematic underperformance.

## Falsification plan

To independently confirm or challenge the author's execution falsification findings across global markets with price bands or circuit breakers, the following operational tests are proposed:

1. **Intraday Tick / Level-2 Queue Emulation Test:**
   - Re-test the two-day limit-up strategy using tick-level order book snapshots or 1-minute bars (`research-proposed`).
   - `research-defined falsification threshold`: If a simulated order queued at 09:25:00 CST receives a fill ratio $< 5\%$ across all non-one-word limit-up days, confirm that even partial fills are economically unviable.

2. **Cross-Sectional Reversal Horizon Extension:**
   - Test whether reversal factors flip from negative IC to positive IC at longer horizons (e.g., $h = 20, 60, 120$ trading days) (`research-proposed`).
   - `research-defined falsification threshold`: If Rank IC remains negative ($\text{Mean IC} < 0.0$) across all horizons up to 60 trading days, reject mean-reversion as an alpha driver in liquid A-shares.

3. **Transaction Cost Sensitivity Stress:**
   - Sweep round-turn execution friction from 15 bps to 50 bps across the relaxed parameter variant (`research-proposed`).
   - `research-defined falsification threshold`: If the $+5.91\%$ return of the relaxed variant turns negative at total round-turn friction $\le 25\text{ bps}$, reject parameter relaxation as a viable mitigation.

## Crypto portability

**Adapted / Unproven (`adapted/unproven`):**
- The primary source focuses exclusively on mainland Chinese A-share equities subject to daily $\pm 10\%$ statutory price bands and $T+1$ settlement rules.

**Crypto Microstructure Mapping and Adaptation Risks:**
- **Absence of Hard Daily Price Limits:** Crypto spot and perpetual markets operate 24/7 without statutory $\pm 10\%$ price ceilings. A direct equivalent to "one-word limit-up" does not exist in standard centralized exchanges (`research-proposed`).
- **Synthetic Analogues (Liquidation Cascades and Extreme Funding):** Analogous unfillability phenomena occur during market flash crashes and liquidation cascades:
  - During rapid perpetual liquidations, the order book can experience complete liquidity vacuums where top-of-book prices jump discretely across multiple percentage points (`research-proposed`).
  - Chasing momentum on tokens that have surged $+50\%$ to $+100\%$ intraday often results in immediate adverse fills at the peak of an order-flow exhaustion candle (`research-proposed`).
- **DEX Bonding Curve / Front-Running Contamination:** On automated market makers (AMMs), memecoin pump-and-dump mechanics resemble limit-up chasing. Backtests assuming fills at the historical block-header price fail in live trading due to MEV sandwich bots, slippage limits, and liquidity drain (`research-proposed`).

## Limitations

- **Daily Bar Resolution:** The primary source operates on daily OHLCV data. While the author uses `buy == buy_high == buy_low` to catch one-word limit-ups, intraday limit-up locks that opened normally but locked within seconds cannot be fully detected without minute or tick data (`source-reported`).
- **Single Market Context:** The findings are derived on CSI 1800 constituents in China; behavioral dynamics and retail participation may differ in other emerging or developed markets (`source-reported`).
- **Data Endpoint Reliance:** Data is cached from public endpoints (BaoStock / Tencent API) rather than institutional Level-2 tick feeds (`source-reported`).
- **Not Independently Reproduced.**

## Implementation status

- **Status:** `not-implemented`.
- No implementation exists in NautilusTrader, PyBroker, paper trading, testnet, or live trading execution systems.
- This record serves as an essential methodology benchmark and cautionary case study on execution realism, order-fill viability, and data contamination in momentum strategies.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- This record captures an open-source empirical research and falsification artifact. It does not constitute approval for live trading, algorithmic implementation, or capital allocation.

## Related Wiki records

- `[[quant/china-ashare-mask-first-upstream-contamination-adjusted-mse-2026-09-04]]` — Mathematical treatment of limit-up execution contamination in machine learning cross-sectional models (Du 2025/2026).
- `[[quant/price-limit-retained-hidden-excess-memory-2026-09-11.md]]` — Price-limited volatility memory and circuit-breaker spillover dynamics on the National Stock Exchange of India (Das 2026).
- `[[quant/retail-signal-three-gate-falsification-oscillator-volume-calendar-trend-2026-09-04.md]]` — Multi-gate falsification of popular retail technical indicators and breakout signals.
- `[[quant/sp500-pairs-trading-forensic-falsification-unbounded-beta-kalman-phantom-pnl-2026-09-12.md]]` — Forensic falsification of unbounded beta artifacts and phantom PnL in pairs trading.

## Sources

1. **Primary GitHub Source Repository:**
   - URL: https://github.com/fkchaos/a-share-quant-sim
   - Full Commit SHA: `2622c2dbccde5c0b05eb9089b891976f2cc6bf90`
   - Tree URL: https://github.com/fkchaos/a-share-quant-sim/tree/2622c2dbccde5c0b05eb9089b891976f2cc6bf90
   - Commit Date: 2026-09-11T10:38:09Z
   - Author: fkchaos (`https://github.com/fkchaos`)
2. **Primary Documentation and Post-Mortem Records:**
   - Falsified Strategy Ledger: `docs/strategy/STRATEGIES_DISCARDED.md` (v65 BigQuant yesterday limit-up analysis; v58a/v58b/v59a/v79/v80 reversal IC breakdown)
   - Experiment Results Log: `docs/strategy/RESULTS_LOG.md` (v66/v67 15-fold walk-forward validation and parameter sweeps)
   - Architecture and Code Path Invariant: `README.md`
3. **Primary Implementation and Ablation Scripts:**
   - Strategy Definition: `scripts/strategies/v65_yesterday_limit.py`
   - Multi-Factor Integration: `scripts/strategies/v66_two_day_limit.py`
   - Full BigQuant Backtest: `scripts/tools/v65_test.py`
   - Unconstrained Momentum Test: `scripts/tools/v65_test_no_concept.py`
   - One-Word Limit-Up Ablation Test: `scripts/tools/v65_test_no_concept_v2.py`
   - Walk-Forward and Factor Scripts: `scripts/tools/v66_test.py` and `scripts/tools/v66_test_no_one_word.py`
