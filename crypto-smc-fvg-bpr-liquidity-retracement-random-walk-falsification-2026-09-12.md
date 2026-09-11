---
schema: strategy-research-record-v1
title: "Smart Money Concepts Liquidity Retracement: Empirical Falsification of Fair Value Gap and Balanced Price Range Edge via Driftless Random Walk Controls"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - smart-money-concepts
  - fair-value-gap
  - balanced-price-range
  - order-blocks
  - negative-evidence
  - random-walk-control
  - selective-execution
  - perpetual-futures
status: research-only
confidence: high
source_as_of: 2026-08-28
sources:
  - "haoyueOuo, '加密貨幣 × 台股 量化交易研究 · Systematic Trading Research', GitHub repository haoyueOuo/crypto-quant-research, commit 5840a4b51ec39fe67bb019a9fdf9b55141433821 (August 28, 2026), files: README.md, backtests/smc_snr_backtest.py, backtests/fvg_crosscheck.pine, backtests/exposure_matched_benchmark.py, backtests/funding_edge.py, backtests/README_規格回測.md, docs/Trading_Strategy_Essentials.md"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Smart Money Concepts Liquidity Retracement: Empirical Falsification of Fair Value Gap and Balanced Price Range Edge via Driftless Random Walk Controls

## Provenance

- **Author / Research Repository:** `haoyueOuo`, *Systematic Trading Research: Crypto × Taiwan Equities Quantitative Research Pipeline* (`haoyueOuo/crypto-quant-research`).
- **Repository URL:** `https://github.com/haoyueOuo/crypto-quant-research`
- **Immutable Commit SHA:** `5840a4b51ec39fe67bb019a9fdf9b55141433821` (August 28, 2026).
- **Inspected Primary Source Files:**
  - Executive summary and methodology overview: `README.md`.
  - Core backtest and synthetic random walk harness: `backtests/smc_snr_backtest.py`.
  - Independent Pine Script v5 validation script: `backtests/fvg_crosscheck.pine`.
  - Exposure-matched benchmark and drawdown compression audit: `backtests/exposure_matched_benchmark.py`.
  - Funding rate circular shift permutation harness: `backtests/funding_edge.py`.
  - Formal upgrade specification and quantitative stress test results: `backtests/README_規格回測.md`.
  - Conceptual taxonomy of market archetypes: `docs/Trading_Strategy_Essentials.md`.
- **Source As-of Date:** August 28, 2026.
- **Repository Deduplication Audit:** Audited all existing markdown records in `alpha-strategy-research`. Zero prior records cite `haoyueOuo`, `crypto-quant-research`, or the random-walk null-control falsification of Smart Money Concepts (SMC) Fair Value Gaps (FVG) and Balanced Price Ranges (BPR). An adjacent negative study (`retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11.md`, citing Mykola-Quant) examined high-frequency CVD order flow and session opening gaps, but did not investigate limit-order selective execution geometry, structural FVG/BPR mechanics, or synthetic random-walk controls. This record captures an independent, source-complete empirical falsification.

## Economic mechanism

### Source-reported

In retail technical analysis and "Smart Money Concepts" (SMC / ICT), market makers and institutional participants are hypothesized to leave structural footprints in order flow when deploying aggressive liquidity:
1. **Fair Value Gap (FVG):** A 3-bar price formation where a large directional expansion candle creates an imbalance between the high of bar $i-2$ and the low of bar $i$ (bullish FVG) or the low of bar $i-2$ and the high of bar $i$ (bearish FVG). The retail narrative claims this un-traded price interval represents a "liquidity void" that price is magnetically compelled to re-visit and fill, after which institutional resting limit orders defend the level and drive price toward an impulsive continuation.
2. **Balanced Price Range (BPR):** A region where opposing bullish and bearish FVGs overlap in price space within a tight temporal window ($\le 10$ bars). Proponents claim this double-imbalance is "cleaner" than a single FVG, offering higher predictive accuracy.
3. **Apparent Empirical Edge:** Proponents point to empirical backtest results showing that waiting for price to retrace into an FVG and entering via limit order yields an apparent win rate of 43.2% to 46.1% on 4h/1d crypto bars with a 2.0R profit-target versus 1.0R stop-loss (and 46.2% to 53.3% for BPR), well above the 33.3% breakeven win rate of a naive 2.0R trade.

**The Source-Reported Falsification:**
The author designed a fully causal, mechanical backtest engine and paired it with a **driftless geometric random walk control**. The central discovery is that:
- When the identical FVG limit-order entry rule is evaluated on synthetic driftless random walks, the win rate is **44.4%** (identical to real market data).
- When the narrower BPR overlap rule is evaluated on synthetic driftless random walks, the win rate is **49.2% to 51.5%** (identically elevated).
- The elevated win rate is **not an economic edge or institutional footprint**, but a **mechanical artifact of selective limit-order execution**. Any rule requiring price to retrace to a specific limit price before entering unconditionally discards paths that immediately trend away. Conditional on an order filling without having already hit the stop, the path geometry creates an inherent mathematical win-rate distortion on any Brownian motion or Markovian price process.
- When evaluating the total strategy after transaction costs (taker fees + slippage), gross expectation across 15m, 1h, and 4h timeframes is $\approx 0$, yielding strictly negative net PnL. Furthermore, waiting for limit fills imposes a massive opportunity cost by systematically forfeiting the strongest right-tail trending moves.

### Research interpretation

This source provides a formal falsification of a massive class of retail trading strategies:
- **The Retracement Selection Trap:** In path-dependent barrier options and conditional first-passage time problems, conditioning entry on a limit order fill inside a retracement zone alters the distribution of subsequent barrier hits. Because the stop is anchored at the far side of the gap and entry is at the near side, the trade is only initiated after price has already made an adverse excursion to the limit price without exceeding the stop during the fill window. On a driftless random walk, this boundary condition generates a conditional survival probability that mechanically shifts the realized hit rate on a 2:1 barrier payoff from 33.3% to ~44.4%.
- **The Complexity–Artifact Scaling Law:** As the spatial restriction becomes narrower (moving from a broad FVG to a narrow BPR intersection), the selection conditioning becomes more severe, pushing the apparent win rate even higher (up to 51.5% on pure noise). This explains why discretionary and retail traders perceive complex multi-condition SMC patterns as having higher "win rates" despite having zero underlying predictive alpha.
- **Trend-Following Self-Cannibalization:** By definition, the strongest price trends exhibit immediate impulse continuation with shallow or absent pullbacks. Requiring a complete retracement to enter filters out precisely the high-momentum right-tail runs that compensate trend-following strategies for chop.

## Signal

The primary source operationalizes five mechanical, strictly causal SMC/SNR patterns in `backtests/smc_snr_backtest.py`:

### 1. Fair Value Gap Retracement (`fvg_fill`)
- **Formation Horizon:** Formed over 3 consecutive bars ($i-2$, $i-1$, $i$).
  - Bullish FVG: $	ext{Low}_i > 	ext{High}_{i-2}$ and $(	ext{Low}_i - 	ext{High}_{i-2}) \ge 	ext{min\_atr} 	imes 	ext{ATR}_{14, i}$. Gap range: $[	ext{High}_{i-2}, 	ext{Low}_i]$.
  - Bearish FVG: $	ext{High}_i < 	ext{Low}_{i-2}$ and $(	ext{Low}_{i-2} - 	ext{High}_i) \ge 	ext{min\_atr} 	imes 	ext{ATR}_{14, i}$. Gap range: $[	ext{High}_i, 	ext{Low}_{i-2}]$.
  - Filter threshold: $	ext{min\_atr} = 0.25$ (gap height must exceed 0.25 14-period ATR; source-reported).
- **Signal Availability:** Available at close of bar $i$.
- **Order Placement:** At bar $i+1$, place a limit order at the near edge of the gap:
  - Long: Limit entry at $	ext{High}_{i-2}$; stop loss at far edge $	ext{Low}_i$.
  - Short: Limit entry at $	ext{Low}_{i-2}$; stop loss at far edge $	ext{High}_i$.
- **Order Time-to-Live (TTL):** Cancel limit order if unfilled after $	ext{ENTRY\_TTL} = 12$ bars (source-reported).
- **Invalidation / Cancel Rule:** If price closes beyond the far-edge stop before limit execution, the pending order is canceled immediately (source-reported).
- **Order Replacement:** A newer FVG signal on the same asset replaces any pending older unfilled order (source-reported).
- **Profit Target:** Fixed reward-to-risk multiple: $	ext{Target} = 	ext{Entry} + R_{	ext{target}} 	imes |	ext{Entry} - 	ext{Stop}|$ with $R_{	ext{target}} = 2.0$ (source-reported).
- **Time Exit:** Maximum holding period of $	ext{MAX\_BARS} = 50$ bars; exit at market close on bar 50 if neither stop nor target hit (source-reported).
- **Execution Collision Rule:** If high touches target and low touches stop in the identical bar, trade is conservatively assigned as a stop-loss (pessimistic fill execution; source-reported).

### 2. Balanced Price Range (`bpr`)
- **Formation:** Intersection of one bullish FVG and one bearish FVG separated by at most $	ext{BPR\_MAX\_SEP} = 10$ bars where price intervals overlap:
  $$\text{BPR} = [\max(\text{Low}_A, \text{Low}_B), \min(\text{High}_A, \text{High}_B)] \quad \text{with } \text{Low}_{\text{BPR}} < \text{High}_{\text{BPR}}$$
- **Direction:** Determined by the chronologically later gap (bullish followed by bearish $\to$ resistance/short; bearish followed by bullish $\to$ support/long; source-reported).
- **Execution:** Limit order placed at the near edge of the BPR intersection zone; stop at far edge; $R_{\text{target}} = 2.0$, $\text{TTL} = 12$ bars.

### 3. Order Block Retracement (`ob`)
- **Formation:** The last opposing candle preceding an impulse expansion whose real body satisfies $|\text{Close}_i - \text{Open}_i| \ge 1.5 \times \text{ATR}_{14, i}$ ($\text{OB\_IMPULSE} = 1.5$; source-reported).
- **Execution:** Limit order placed at high/low range of that preceding opposing candle; stop at extreme; $R_{\text{target}} = 2.0$.

### 4. Liquidity Sweep Reversal (`sweep`)
- **Formation:** Price pierces the trailing $N=20$ bar extreme ($\text{Low} < \min(\text{Low}_{i-20:i-1})$) but closes back inside the prior range ($\text{Close}_i > \min(\text{Low}_{i-20:i-1})$) (source-reported).
- **Execution:** Market order executed on bar $i+1$ open; stop loss placed at the pierced extreme.

### 5. Support/Resistance Pivot Bounce and Break (`snr_bounce`, `snr_break`)
- **Causal Pivots:** Pivot high/low identified with causal confirmation lag $L=5$ bars ($\text{PIVOT\_L} = 5$). A pivot at bar $i$ can only be utilized at or after bar $i+L$ (strictly causal, avoiding look-ahead bias; source-reported).

## Required data

- **Instruments:** Binance USD-M Perpetual Futures contracts (`BTCUSDT`, `ETHUSDT`, `BNBUSDT`, `SOLUSDT`, `XRPUSDT`, `ADAUSDT`, `DOGEUSDT`, `LINKUSDT`).
- **Timeframes:** 15m, 1h, 4h, 1d OHLCV bars.
- **Fields:** Open, High, Low, Close, Volume.
- **History Duration:** 1,095 days (~3 years, covering the 2022 bear market and 2023–2024 bull market).
- **API Endpoint:** Binance Futures public endpoint (`https://fapi.binance.com/fapi/v1/klines`).
- **Synthetic Control Panel:** Driftless geometric Brownian motion / random walk OHLCV series generated with matching volatility and bar count (`source-reported`).
- **Missing Data Handling:** Incomplete bars dropped; minimum history requirement of 200 bars per series.

## Execution assumptions

- **Order Types:**
  - Retracement models (`fvg_fill`, `bpr`, `ob`, `snr_bounce`): Limit orders placed at the specified price level; executed if price low $\le$ limit price (for longs) or high $\ge$ limit price (for shorts).
  - Breakout/Sweep models (`sweep`, `snr_break`): Market order executed at next-bar open ($\text{Open}_{i+1}$).
- **Transaction Costs (Source-Reported):**
  $$\text{Cost}_{\text{round-trip}} = 2 \times (0.04\% \text{ taker fee} + 0.05\% \text{ slippage}) = 0.18\%$$
  - Fee model reflects Binance standard VIP0 taker fee (0.04% per side) plus 0.05% conservative execution slippage per side.
  - Limit orders that cross the spread or execute on touch are modeled conservatively under taker fees, acknowledging that resting queue priority on Binance Futures is highly competitive.
- **Intrabar Ambiguity / Conservative Fill:** If both target and stop are reachable within the high-low span of the same bar, execution is assigned 100% to stop-loss (source-reported).
- **Position Sizing:** Equal-risk sizing ($1.0R$ risk per trade based on distance between entry and stop loss). Portfolio allocation capped at available capital (`research-proposed`).
- **Funding Rate Friction:** Excluded on 15m/1h/4h due to short average holding periods (hours to days); source notes that 1d holding across multi-week horizons requires explicit funding rate deduction (source-reported).

## Evidence

### Source-reported

#### 1. Real Crypto Perpetual Data vs. Random Walk Control

The primary source reports a comparison between real Binance crypto perpetuals and synthetic driftless random walks under identical execution logic ($R_{\text{target}} = 2.0R$ target, $1.0R$ stop):

| Strategy / Rule | Real Crypto Data Win Rate (4h / 1d) | Driftless Random Walk Win Rate | Source Empirical Verdict |
|---|---|---|---|
| **FVG Retracement Fill (`fvg_fill`)** | **43.2% – 46.1%** | **44.4%** | **Zero edge; mechanical selection artifact** |
| **BPR Overlap (`bpr`)** | **46.2% – 53.3%** | **49.2% – 51.5%** | **Zero edge; narrower zone amplifies artifact** |
| **Naive Random Baseline (2.0R Target)** | 33.3% | 33.3% | Theoretical benchmark: $\frac{1}{1 + R} = 33.3\%$ |

- **Source Finding:** On pure random walk data with zero drift and zero autocorrelation, the FVG limit-order entry strategy produces an apparent win rate of **44.4%**, which matches the 43.2%–46.1% win rate observed on real Bitcoin/Ethereum data.
- **BPR Zone Narrowing Effect:** As the zone becomes narrower and more "refined" (BPR requiring two overlapping opposite-direction gaps), the random walk win rate climbs to **49.2%–51.5%**. The author deduces: *"The rule 'more refined zone definition $\to$ higher win rate' is a universal mathematical property of selective execution and is completely independent of market dynamics."*

#### 2. Cross-Timeframe Gross vs. Net Expectancy

Testing across all 8 symbols and 4 timeframes (15m, 1h, 4h, 1d) over 3 years:
- **Gross Expectancy:** Gross returns across 15m, 1h, and 4h hover around $0.00\%$ per trade.
- **Net Expectancy:** After deducting the $0.18\%$ round-trip fee and slippage drag, net expectancy is negative across all short-horizon combinations.
- **No Parameter Rescue:** The author notes that low-timeframe losses are approximately equal to transaction costs ($\text{Loss} \approx \text{Cost}$), confirming that gross edge is approximately zero and cannot be salvaged by tuning parameters.

#### 3. Selection Opportunity Cost Audit (Limit vs. Market Entry)

Evaluating individual FVG occurrences comparing limit pullback execution vs. immediate market entry:
- Limit orders fill on only a subset of signals (~35%–50% fill rate).
- Unfilled signals systematically encompass the strongest right-tail continuation moves that impulse directly into the profit target without pulling back.
- By waiting for a limit fill, the strategy experiences significant opportunity cost on unfilled trades, negating any micro-pricing advantage obtained on filled trades.

#### 4. Additional Falsifications from the Same Research Corpus

- **Exposure-Matched Benchmarking (`exposure_matched_benchmark.py`):** The strategy's apparent drawdown reduction (-13% max drawdown vs. BTC -77%) was audited against market exposure. The strategy had an average exposure of only 4.1% (median 1.1%). An unmanaged benchmark of 3% BTC + 97% cash produced the identical -13% drawdown with zero active trading friction. Calmar ratio was scale-invariant (1.41–1.48 across exposure levels).
- **Funding Rate Autocorrelation Permutation (`funding_edge.py`):** An apparent +1.33 pp quadrant return spread on funding rate extremes was falsified via circular shift permutation. The null standard deviation was 0.90 pp ($p = 0.170$), because serial autocorrelation and cross-asset correlation collapsed 3,647 nominal days into only ~200 effective independent events.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Synthetic Random Walk Equivalence:** The primary source demonstrates that FVG and BPR win rates are indistinguishable from those obtained on pure noise, completely disproving the hypothesis that FVGs represent institutional limit-order defense.
2. **Transaction Cost Barrier:** A round-trip cost of 0.18% (18 bps) exceeds the gross edge across 15m, 1h, and 4h timeframes.
3. **Single-Symbol Selection Bias:** In `single_symbol_check.py`, testing individual tokens across 6 years showed a 94 percentage point spread in CAGR; removing the single largest winning trade on ETH flipped strategy expectancy from $+13.90\%$ to $-4.92\%$.
4. **Opportunity Cost Drag:** The subset of price moves that do not retrace into the FVG represent the strongest momentum events; filtering them out systematically degrades trend capture.

## Falsification plan

To test whether any variant of an FVG/SMC retracement signal can possess genuine alpha beyond the mechanical selection artifact:

1. **Random-Walk Control Baseline (`research-defined falsification threshold`):** Any proposed FVG/BPR signal must be benchmarked against 1,000 synthetic driftless geometric random walk simulations matching the asset's realized volatility and bar frequency. If the empirical win rate or Sharpe does not exceed the 95th percentile of the random walk distribution ($p > 0.05$), the strategy is deemed falsified as a selection artifact.
2. **Opportunity Cost Invariant Test (`research-defined falsification threshold`):** Measure the total return of all FVG signals executed at market open ($i+1$) versus limit retracement. If the limit strategy fails to beat the market-entry strategy by at least $2 \times \text{Cost}_{\text{round-trip}}$ per signal after accounting for missed trades, the limit filter is rejected.
3. **Fee and Slippage Stress Test (`research-defined falsification threshold`):** Evaluate net expectancy at 0, 10, 18, 25, and 35 bps round-trip transaction costs. If net expectancy turns negative at or below 15 bps round-trip, the strategy is deemed un-tradeable.
4. **Exposure-Matched Benchmark Test (`research-defined falsification threshold`):** If the strategy claims risk reduction or drawdown compression, it must be matched against a cash-diluted buy-and-hold benchmark ($f \times \text{Asset} + (1-f) \times \text{Cash}$) with identical max drawdown. If the strategy's CAGR is lower than the exposure-matched benchmark, the strategy is rejected as a passive beta scaler.

## Crypto portability

**Direct** — The primary source designed, tested, and falsified these rules natively on Binance cryptocurrency perpetual futures across 8 liquid pairs (`BTCUSDT`, `ETHUSDT`, `BNBUSDT`, `SOLUSDT`, `XRPUSDT`, `ADAUSDT`, `DOGEUSDT`, `LINKUSDT`).

**Crypto-Specific Considerations:**
- **24/7 Continuous Trading:** Crypto markets do not have standard session opens/closes outside of funding intervals, making bar-boundary definitions dependent on UTC timestamps.
- **Funding Rates:** For daily (1d) holding periods exceeding several days, funding payments paid by long positions during bull markets create a substantial drag not present in traditional equities.
- **Taker/Maker Fee Structure:** High turnover on lower timeframes (15m, 1h) exposes strategies to aggressive taker fees (0.04%–0.05%) and bid-ask spread crossing, which erases marginal gross edges.

## Limitations

- **Mechanical Win-Rate Illusion:** The 44.4% win rate on a 2.0R target is a mathematical artifact of the limit-order entry barrier, not evidence of market predictability.
- **Lack of Volume / Liquidity Information in Pure Price Gaps:** Standard 3-bar FVGs measure only price range exclusions and do not incorporate resting depth, book replenishment speed, or taker flow imbalances.
- **Survivorship in Token Universe:** While the source evaluated 8 top liquid tokens, testing on smaller altcoins introduces severe survivorship bias due to listing/delisting dynamics.
- **Not Independently Reproduced:** The findings reflect the source author's codebase and backtests; they have not been independently reproduced in an external execution harness.

## Implementation status

Not implemented. No implementation in our research stack (`nautilus-quant-system`, PyBroker, or NautilusTrader). This record is an empirical falsification capture documenting why SMC/FVG retracement rules should not be prioritized for production backtesting.

## Adoption boundary

This record is research material only. It does not indicate:
- profitable strategy
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet trading
- approved for live trading

This record serves as negative evidence and an econometric falsification benchmark against retail Smart Money Concepts claims.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` (canonical strategy-research record specification)
- `[[quant/retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11]]` (adjacent negative-evidence record falsifying retail CVD order-flow divergence and calendar patterns)
- `[[quant/retail-signal-three-gate-falsification-oscillator-volume-calendar-trend-2026-09-04]]` (falsification of retail technical indicator combinations)

## Sources

1. haoyueOuo, "加密貨幣 × 台股 量化交易研究 · Systematic Trading Research", GitHub repository `haoyueOuo/crypto-quant-research`, commit `5840a4b51ec39fe67bb019a9fdf9b55141433821` (August 28, 2026). URL: https://github.com/haoyueOuo/crypto-quant-research
2. `backtests/smc_snr_backtest.py` (Smart Money Concepts and Support/Resistance backtest engine and random-walk control harness).
3. `backtests/fvg_crosscheck.pine` (Pine Script v5 FVG detector cross-validation script).
4. `backtests/exposure_matched_benchmark.py` (Exposure-matched benchmark and drawdown compression falsification harness).
5. `backtests/funding_edge.py` (Funding rate circular shift permutation harness and effective sample size analysis).
6. `backtests/README_規格回測.md` (Specification backtest report, Calmar tables, and parameter sweep audits).
7. `docs/Trading_Strategy_Essentials.md` (Market archetypes, mean reversion, trend following, and Kelly sizing limits).
