---
schema: strategy-research-record-v1
title: "Cross-Sectional Vortex Indicator Top2 Equity Trend Strategy with Liquidity Gating and Rebalance Phase Robustness"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equity
  - momentum
  - trend-following
  - vortex-indicator
  - cross-sectional
  - rebalance-phase
  - execution-drag
  - survivorship-bias
  - backtest-audit
status: research-only
confidence: medium
source_as_of: 2026-09-12
sources:
  - "SailorChina, 'us-stock-factor-backtest: US Stock Factor Strategy Backtest and Live Execution Toolkit', GitHub repository, commit 46d81b4416dad28906265acf2bcb6099ef1a69c7, September 12, 2026. https://github.com/SailorChina/us-stock-factor-backtest"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Sectional Vortex Indicator Top2 Equity Trend Strategy with Liquidity Gating and Rebalance Phase Robustness

## Provenance

- **Repository:** `https://github.com/SailorChina/us-stock-factor-backtest`
- **Full Commit SHA:** `46d81b4416dad28906265acf2bcb6099ef1a69c7`
- **Primary Source Author:** SailorChina
- **As-of Date:** 2026-09-12 (Commit date: 2026-09-12T22:39:45Z; historical price data: 2018-01-02 to 2026-09-11)
- **Primary Files Inspected:**
  - `README.md`: Project overview, 69-strategy tournament, and methodology synthesis.
  - `_update_signal.py`: Live production signal generator, liquidity gate mask, Vortex formula, and 103-item test suite.
  - `_v30_phase.py`: 156-phase sensitivity audit across 6 rebalancing periods (5, 10, 15, 21, 42, 63 trading days).
  - `_v32_window.py`: Lookback window sensitivity audit across 8 windows ($n \in \{5, 7, 10, 14, 21, 30, 42, 63\}$).
  - `_v33_gate.py`: Liquidity gate threshold scan across 8 dollar-volume cutoffs ($0.5M to $50M).
  - `_v29_slippage.py`: Execution timing (Open vs Close) and slippage impact quantification.
  - `_v28_smallcap.py`: Fixed-commission drag model across capital tiers ($500 to $50,000).
  - `_v31_stagger.py`: Leg-staggered rebalancing breakdown and weight deviation audit.
  - `美股回测深度审计_v25.1.md`: Forensic audit documenting three silent backtest defects (volume ffill bug F1, halted position erasure bug F2, omitted buy commission bug F3).
  - `美股周期相位稳健性_v30.md`: Rebalance phase audit and pairwise comparison.
  - `美股最强两策略_最终测试_v34.md`: Comparative head-to-head analysis of Vortex Top2 @10-day vs Golden Cross + MA50 Distance @21-day.
- **Dataset Universe:** 81 liquid US common stocks (Futu US hot list with market cap $\ge \$10\text{B}$ in 2026, non-ETF/non-leveraged, $\ge 253$ valid trading days).
- **Historical Sample Period:** 2018-01-02 to 2026-09-11 (2,185 daily bars; first 252 bars reserved for indicator warmup; actual investment window: 2019-01-03 to 2026-09-11 = 7.69 years).

## Economic mechanism

### Source-reported

The source proposes a cross-sectional trend-following strategy based on the **Vortex Indicator** difference ($\text{VI}^+ - \text{VI}^-$) calculated over an $n=14$ daily window. Originally developed by Etienne Botes and Douglas Siepman (inspired by Viktor Schauberger's water vortex principles), the Vortex Indicator measures directional movement by connecting current price extremes to preceding opposite extremes ($|H_t - L_{t-1}|$ for upward trend energy and $|L_t - H_{t-1}|$ for downward trend energy), normalized by True Range. 

The source argues that ranking assets cross-sectionally by Vortex difference identifies equities exhibiting the strongest upward directional price persistence relative to total volatility. In an empirical tournament of 69 quantitative factor strategies over 7.69 years on the same 81-stock universe, the source reports that `Vortex Top2` combined with a 10-day rebalancing frequency emerged as the risk-adjusted champion (Sharpe 1.67, Calmar 2.65, maximum drawdown $-35.8\%$, and 100% positive annual returns across 8 calendar years 2019–2026).

To prevent investing in illiquid or suspended shell companies, the strategy integrates a pre-ranking **liquidity gate**: an asset must have a rolling 60-day median dollar volume ($\text{Close} \times \text{Volume}$) $\ge \$5\text{M}$ and possess an un-forward-filled real trading bar on decision day.

### Research interpretation

The hypothesized economic mechanism is **cross-sectional intermediate-horizon trend continuation driven by retail and institutional momentum herding in mega/large-cap equities**, screened through an operational liquidity filter.

However, the primary source's exceptionally rigorous forensic audits demonstrate that the raw backtest results cannot be taken as unconstrained structural alpha:
1. **Severe Survivorship Bias:** The 81-stock pool was selected retroactively using 2026 market capitalization ($\ge \$10\text{B}$) from Futu's most actively traded list. A naive equal-weighted buy-and-hold of this 81-stock pool compounded at **44.2% CAGR (+1,566%)**, compared to the S&P 500 ETF (VOO) at **17.8% CAGR (+252%)**. Thus, more than half of the apparent cumulative performance is driven by survivorship/universe selection of decade-long mega-cap winners (e.g. NVDA, SMCI, AAPL, META), rather than pure selection timing.
2. **Rebalance Phase Luck:** Rebalance frequency is not a smooth scalar parameter; it represents an execution phase offset $\text{anchor} \bmod \text{rebal}$. Shifting the starting day by just 1 trading day causes the 10-day rebalance CAGR to swing widely between **51.3% and 100.6%** (a 49.3 percentage point range; phase standard deviation 17.2pp). The default headline CAGR of 94.8% ranked #2 out of the 10 possible phases, indicating substantial positive phase luck. The median across all phases is 79.9%.
3. **Window-Cadence Interaction:** The lookback window $n=14$ is a legacy technical analysis convention. Testing across 8 lookback windows ($n \in \{5, 7, 10, 14, 21, 30, 42, 63\}$) revealed that 10-day rebalance outperforming 21-day rebalance held in only 4 out of 8 windows; $n=14$ happened to produce the single highest outperformance margin (+21.9pp), demonstrating selection bias along the lookback dimension.

## Signal

- **Formation Timestamp:** Market close on trading day $t$ (4:00 PM EST).
- **Execution Timestamp:** Market open on trading day $t+1$ (9:30 AM EST).
- **Lookback Window ($n$):** $n=14$ trading days (source-reported standard parameter).
- **Indicator Construction (source-reported):**
  For each asset $j$ on daily bar $t$:
  $$\text{TR}_t = \max\left(H_t - L_t, \, |H_t - C_{t-1}|, \, |L_t - C_{t-1}|\right)$$
  $$\text{VM}^+_t = |H_t - L_{t-1}|$$
  $$\text{VM}^-_t = |L_t - H_{t-1}|$$
  $$\text{VI}^+_t(n) = \frac{\sum_{k=0}^{n-1} \text{VM}^+_{t-k}}{\sum_{k=0}^{n-1} \text{TR}_{t-k}}$$
  $$\text{VI}^-_t(n) = \frac{\sum_{k=0}^{n-1} \text{VM}^-_{t-k}}{\sum_{k=0}^{n-1} \text{TR}_{t-k}}$$
  $$\text{Vortex\_diff}_{j,t} = \text{VI}^+_{j,t}(n) - \text{VI}^-_j(n)$$
- **Liquidity Gating Rule (source-reported):**
  Prior to ranking, an asset $j$ on day $t$ is evaluated:
  $$\text{DV}_{j,t} = C_{j,t} \times \text{Volume}_{j,t}$$
  $$\text{Tradable}_{j,t} = \left(\text{median}_{k=0}^{59} \text{DV}_{j,t-k} \ge \$5,000,000\right) \land \text{RealBar}_{j,t}$$
  Assets failing this gate or lacking finite prices are masked to `NaN` before cross-sectional operations to prevent distorting cross-sectional statistics.
- **Cross-Sectional Ranking & Selection:**
  Eligible assets are sorted by $\text{Vortex\_diff}_{j,t}$ in descending order.
  The top $K=2$ assets are selected (`tgt = [top1, top2]`).
- **Rebalance Grid (source-reported):**
  Fixed trading-day grid defined by:
  $$\text{RebalanceDays} = \{ i \ge \text{anchor} \mid (i - \text{anchor}) \bmod \text{rebal} == 0 \}$$
  Default: $\text{rebal} = 10$ trading days; $\text{anchor} = 252$ (first investment bar 2019-01-03).
- **Long Entry:**
  On rebalance day $i$ at Open price:
  If a new target asset $j \in \text{tgt}$ is not currently in the portfolio, it is purchased with allocated cash.
- **Short Entry:**
  Not applicable; long-only equity model.
- **Exit Trigger:**
  On rebalance day $i$ at Open price:
  Any currently held asset $j \notin \text{tgt}$ is completely liquidated at the Day $i$ Open price $O_{i,j}$.
- **Position Sizing (source-reported):**
  Equal-weight allocation across the top $K=2$ assets:
  $$\text{budget\_per\_asset} = \max\left(0, \, \frac{\text{Cash} - K \times \text{Commission}}{K}\right)$$
  $$\text{shares}_j = \frac{\text{budget\_per\_asset}}{O_{i,j}} \quad (\text{fractional shares permitted})$$
- **Operational Rules Classification:**
  - *Source-reported:* $n=14$, $K=2$, liquidity threshold $\$5\text{M}$ rolling 60-day median dollar volume, 10-day and 21-day rebalance grids, $T+1$ open execution, $\$2.00$ fixed commission per order ticket, fractional share allocation.
  - *Research-proposed:* Intraday stop-loss triggers (not implemented in the primary source), crypto perpetual funding adjustments, crypto exchange fee models, leverage scaling ($> 1\text{x}$).

## Required data

- **Instrument:** US Listed Equities (common stocks only; no ETFs, no leveraged instruments).
- **Universe:** 81 liquid US common equities (market cap $\ge \$10\text{B}$ in 2026, minimum 253 valid daily trading bars).
- **Venue:** US Equities (NASDAQ, NYSE). Data acquired via Futu OpenD API (port 11111).
- **Timeframe:** Daily OHLCV bars.
- **Adjustment:** Forward-adjusted (QFQ - Qian Fu Quan) for stock splits, reverse splits, and cash dividends.
- **Fields:** `open`, `high`, `low`, `close`, `volume`.
- **Point-in-Time Integrity:**
  - Signal calculated strictly at day $t$ close using data up to and including day $t$.
  - Truncation tests confirmed: zero future leakage across 2,164 overlapping bars upon removing the final 21 bars.
  - Uncompleted intraday bars are rejected; historical data files confirmed post-market timestamp (00:40 EST next day).
- **Missing Data Handling (source-reported):**
  - Volume is strictly *not* forward-filled (`ffill` is prohibited for volume).
  - The `REAL` mask confirms the bar is a valid trade day; days with zero volume or halted trading are excluded from rolling statistics.
- **Costs Modeled:** Fixed brokerage commission of $\$2.00$ per order ticket (Futu US standard rate). Zero slippage in base backtest; slippage analyzed separately.

## Execution assumptions

- **Signal-to-Order Timing:** Signal generated after day $t$ close; execution executed at day $t+1$ market open.
- **Order Type & Fill Model:** Market order assumed filled at exact official Day $t+1$ Open price (`Ov[i, j]`).
- **Execution Timing Cost (source-reported):**
  Moving execution from Open to Close on the same rebalance day costs **$-4.21\text{pp}$ CAGR** on 10-day rebalance (reducing CAGR from 93.1% to 88.9% at $\$1,490$ capital). The source proves empirically that new momentum entries exhibit positive intraday drift ($+0.0806\%$ on rebalance days), meaning buying at open captures this intraday edge.
- **Commission Assumptions (source-reported):**
  Fixed $\$2.00$ per trade (both buy and sell).
  At small capital ($\$1,490$), commission imposes a **$5.45\text{pp}$ drag** on 10-day rebalance and **$2.88\text{pp}$ drag** on 21-day rebalance. Empirical formula: $\text{Drag (pp)} \approx \frac{7700}{\text{Capital (\$)}} \text{ for 10-day rebalance}$.
- **Slippage Sensitivity (source-reported):**
  For a $\$1,490$ account ($\$745$ per leg), order size represents $0.0009\%$ of the daily volume of the least liquid universe asset (negligible market impact). However, sensitivity is high: **$-0.87\text{pp}$ CAGR per $1\text{bp}$ of one-way slippage** on 10-day rebalance due to ~25 annual portfolio turnovers.
- **Borrow & Leverage:** Cash only (no shorting, no margin, leverage = 1.0x).

## Evidence

### Source-reported

All figures trace directly to `SailorChina/us-stock-factor-backtest` (commit `46d81b4416dad28906265acf2bcb6099ef1a69c7`, files `美股最强两策略_最终测试_v34.md`, `美股周期相位稳健性_v30.md`, `_v30_phase.txt`, `_v29_slippage.txt`, `_v28_smallcap.txt`):

1. **Long-Term Performance (2019-01-03 to 2026-09-11, 7.69 years, $\$3,000$ initial capital, with liquidity gate, $\$2$ commission):**
   - Ending Equity: $\$504,672.39$ ($+16,722\%$)
   - CAGR: **94.8%**
   - Maximum Drawdown: **$-35.8\%$**
   - Sharpe Ratio: **1.67**
   - Calmar Ratio: **2.65** (ranked #1 in the 69-strategy tournament)
   - Sortino Ratio: **2.48**
   - Annualized Volatility: **46.4%**
   - Win Rate: Monthly 63.4%, Annual **100.0%** (8 out of 8 positive years)
   - Total Trades: 388 orders
2. **Small Capital Scale-Down ($\$1,500$ initial capital):**
   - Ending Equity: $\$221,249.46$ ($+14,650\%$)
   - CAGR: **91.5%** (a $-3.3\text{pp}$ drag vs $\$3\text{k}$ due to fixed $\$2$ ticket commission)
   - Maximum Drawdown: **$-35.8\%$**
   - Sharpe Ratio: **1.64**, Calmar: **2.55**, Sortino: **2.43**
3. **Calendar Year Breakdown (10-day Vortex @ $\$3,000$ vs Golden Cross + MA50 Distance):**
   - 2019: $+56\%$ (Golden Cross $+16\%$)
   - 2020: $+173\%$ (Golden Cross $+116\%$)
   - 2021: $+123\%$ (Golden Cross $+44\%$)
   - 2022 (Bear Market): **$+3\%$** (Golden Cross **$-38\%$**, Max DD $-67.2\%$)
   - 2023: $+95\%$ (Golden Cross $+195\%$)
   - 2024: $+174\%$ (Golden Cross $+339\%$)
   - 2025: $+45\%$ (Golden Cross $+180\%$)
   - 2026 YTD: $+124\%$ (Golden Cross $+156\%$)
4. **Phase Robustness Audit (10-day rebalance, 10 phases, common window 7.42 years, $\$1,490$ capital):**
   - Worst Phase: **51.3% CAGR**
   - 25th Percentile: **66.1% CAGR**
   - Median Phase: **81.0% CAGR**
   - 75th Percentile: **94.0% CAGR**
   - Best Phase: **100.6% CAGR**
   - Standard Deviation: **17.2pp**; Range: **49.3pp**
   - Default Backtest Anchor was Phase #3 (one of the strongest phases).
5. **Pairwise Phase Superiority (10-day vs 21-day):**
   - Across $10 \times 21 = 210$ pairwise phase combinations, 10-day rebalance beats 21-day rebalance in **161 of 210 pairings (76.7% win rate)**.
   - Median outperformance margin: **$+21.9\text{pp}$**.
6. **Benchmark Performance:**
   - 81-stock Equal-Weighted Buy-and-Hold: CAGR **44.2%** ($+1,566\%$), Max Drawdown **$-40.0\%$**.
   - VOO (S&P 500 ETF): CAGR **17.8%** ($+252\%$), Max Drawdown **$-34.0\%$**.

### Independently reproduced

`Not independently reproduced.` All results represent third-party empirical findings from `SailorChina/us-stock-factor-backtest`.

### Negative evidence

The repository itself conducts an unusually transparent defect and limitation audit:
1. **Severe Survivorship / Selection Bias:** The 81-stock universe consists of companies selected in 2026 with market caps $\ge \$10\text{B}$. Naive buy-and-hold of this basket yielded 44.2% CAGR (16.7x gain), while the S&P 500 yielded 17.8% CAGR. A substantial portion of the nominal return stems from ex-post inclusion of mega-winners (e.g. NVDA, SMCI).
2. **Phase Instability:** Depending solely on the calendar start day, realized 10-day CAGR drops from 100.6% to 51.3%. Phase diversification by splitting capital across multiple anchors is cost-prohibitive at small capital: splitting into $N=3$ portfolios increases commission drag to $-20.1\text{pp}$, and $N=5$ causes $-71.8\text{pp}$ drag with a 15% probability of account ruin.
3. **Window Conditioning:** The superiority of 10-day over 21-day rebalance is conditional on the lookback window $n=14$. Across 8 tested windows, 10-day only won in 4 out of 8 ($n \in \{10, 14, 15, 30\}$); for $n \in \{5, 7, 42, 63\}$, 21-day rebalancing achieved higher median CAGRs.
4. **Regime Vulnerability:** In prolonged monotonic bull runs (such as the post-COVID rally from 2020-03 to 2021-05), 10-day rebalance underperformed 21-day rebalance because frequent rebalancing prematurely truncated runaways.
5. **Forensic Backtest Bugs in Predecessor Versions:**
   - *Bug F1:* Volume forward-filling allowed halted/bankrupt stocks to pass the liquidity gate.
   - *Bug F2:* Halted positions were erased from portfolio accounting, generating an artificial $-34.6\%$ single-day drop.
   - *Bug F3:* Buy-side commissions were omitted in 93 historical rebalances, inflating small-capital ending wealth by up to 34.5%.

## Falsification plan

1. **Point-in-Time Survivorship Elimination Test:**
   Re-run the Vortex Top2 strategy on the historical Russell 1000 or S&P 500 universe using point-in-time constituent data (including delisted, acquired, and bankrupt firms) over 2010–2026.
   - `research-defined falsification threshold`: If the strategy's excess CAGR relative to the point-in-time universe equal-weighted benchmark drops to $\le 0.0\%$, the strategy's apparent alpha is falsified as pure survivorship bias.
2. **Out-of-Sample Phase Spread Test:**
   Evaluate the strategy across all 10 calendar phase offsets on an out-of-sample period (e.g. 2000–2018 or prospective 2026–2028).
   - `research-defined falsification threshold`: If more than 30% of phases produce negative excess returns over the universe benchmark, or if the interquartile range (IQR) of phase CAGRs exceeds the median CAGR, the 10-day rebalance frequency is falsified as unidentifiable phase noise.
3. **Execution Delay and Friction Stress Test:**
   Apply 10 bps one-way slippage and execute at Market Close rather than Market Open.
   - `research-defined falsification threshold`: If net CAGR falls below the 81-stock equal-weighted benchmark (44.2%), the strategy is falsified as non-viable under realistic institutional or delayed execution.
4. **Parameter Stability Perturbation:**
   Perturb the Vortex lookback window $n$ from 14 to $n \in \{12, 13, 15, 16\}$.
   - `research-defined falsification threshold`: If a $\pm 1$ or $\pm 2$ day shift in $n$ reduces median CAGR by more than $20\text{pp}$, reject the parameter robustness of the Vortex indicator.

## Crypto portability

**adapted** — The primary source demonstrates the mechanism exclusively on US listed cash equities. Porting to cryptocurrency spot or perpetual futures is an unproven research interpretation.

Crypto-specific adaptation requirements and risks:
- **24/7 Continuous Trading:** Unlike equity markets with 252 discrete sessions and opening auctions, crypto trades continuously 24/7/365. A 10-day rebalancing grid requires an arbitrary UTC cutoff (e.g. 00:00 UTC). Phase noise is expected to be even larger due to lack of synchronized market open/close auctions.
- **Perpetual Funding Rate Drag:** High-momentum crypto assets frequently trade at substantial funding rate premiums. Holding long positions in the top 2 momentum leaders in crypto perpetuals over 10-day windows would incur substantial continuous funding payments to short sellers.
- **Liquidity Quality & Delisting Risks:** The crypto equivalent of the 81-stock universe requires dynamic point-in-time market cap filtering (e.g. top 50 tokens by circulating market cap, excluding stablecoins and wrapped assets) and rolling 30-day median volume $\ge \$10\text{M}$ (`research-proposed`).
- **Extreme Tail Risk in 2-Asset Concentration:** Allocating 50% of the portfolio to each of two altcoins carries catastrophic drawdown risk in crypto flash crashes. In crypto, a minimum basket of $K \ge 5$ to $10$ assets and explicit volatility parity sizing would be required (`research-proposed`).

## Limitations

- **underspecified** execution outside Futu OpenD; fractional-share execution conventions vary widely across retail brokerages.
- **not independently reproduced** on institutional frameworks (e.g. NautilusTrader, PyBroker).
- **data gap:** Daily bar data from Futu OpenD lacks intraday order-book depth and tick-level execution verification.
- **Extreme survivorship bias:** Universe composed of 2026 large-cap survivors.
- **High phase sensitivity:** 49.3pp CAGR spread across calendar starting phases.
- **unproven** in cryptocurrency markets.

## Implementation status

`not-implemented`. No implementation exists in our research stack (`nautilus-quant-system`, PyBroker, or NautilusTrader).

## Adoption boundary

This record is research material only. A record being present in this repository does **not** mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

The strategy exhibits substantial universe selection bias and phase noise that must be subjected to rigorous survivorship-free point-in-time testing before any implementation candidate could be considered.

## Related Wiki records

- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`
- `[[quant/sp500-sector-pairs-causal-residual-pca-area-asymmetry-2026-09-12]]`
- `[[quant/statistical-arbitrage-methodology-degradation-ladder-falsification-2026-09-12]]`
- `[[quant/retail-signal-three-gate-falsification-oscillator-volume-calendar-trend-2026-09-04]]`

## Sources

1. SailorChina. *"us-stock-factor-backtest: 美股因子策略回测与实盘信号工具集 (US Stock Factor Strategy Backtest and Live Execution Toolkit)"*, GitHub repository, commit `46d81b4416dad28906265acf2bcb6099ef1a69c7`, committed September 12, 2026.
   - Repository URL: `https://github.com/SailorChina/us-stock-factor-backtest`
   - Primary Code Files: `_update_signal.py`, `_v30_phase.py`, `_v32_window.py`, `_v33_gate.py`, `_v29_slippage.py`, `_v28_smallcap.py`, `_v31_stagger.py`
   - Primary Audit Markdown: `README.md`, `美股回测深度审计_v25.1.md`, `美股周期相位稳健性_v30.md`, `美股最强两策略_最终测试_v34.md`, `美股执行成本与滑点_v29.md`
   - Empirical Data: `_rank_all.json`, `_rank_all_1500.json`, `_rank_all_phase.json`, `_v30_phase.txt`, `_v29_slippage.txt`, `_v28_smallcap.txt`
