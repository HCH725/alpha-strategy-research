---
schema: strategy-research-record-v1
title: "Prediction Market Pricing Anomalies vs. Execution Friction: Empirical Falsification of the Wang Transform Wedge, Favourite-Longshot Bias, and Digital Option VRP on Kalshi"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - prediction-markets
  - kalshi
  - wang-transform
  - execution-costs
  - bid-ask-spread
  - falsification
  - negative-results
  - variance-risk-premium
  - digital-options
status: research-only
confidence: high
source_as_of: 2026-09-13
sources:
  - "elraffaello123-art, 'Falsification-first systematic trading research: a leak-proof backtest harness, an honest graveyard of killed edges, and a live replication of the Kalshi pricing wedge on the book rather than the mid', GitHub repository 'elraffaello123-art/quant-research', commit 511fab83791a81a96ff64b3e5dadc1636cc5b698, accessed 2026-09-13. https://github.com/elraffaello123-art/quant-research"
  - "Primary audit document: elraffaello123-art, 'The Kalshi pricing wedge is the spread: Replication and honest-cost audit of Yang (2026), Pricing Prediction Markets: Incomplete Markets, Selection Rules, and Risk Premia (SSRN 6468338)', docs/KALSHI_WEDGE_RESULT.md (commit 511fab83791a81a96ff64b3e5dadc1636cc5b698). https://github.com/elraffaello123-art/quant-research/blob/511fab83791a81a96ff64b3e5dadc1636cc5b698/docs/KALSHI_WEDGE_RESULT.md"
  - "Primary empirical code: elraffaello123-art, 'pm/wedge.py', 'pm/favourites.py', 'pm/calibration.py', 'pm/vrp.py', 'pm/kalshi_fetch.py', and 'pm/wedge_report.txt' (commit 511fab83791a81a96ff64b3e5dadc1636cc5b698)"
  - "Academic primary target 1: Fan Yang, 'Pricing Prediction Markets: Incomplete Markets, Selection Rules, and Risk Premia', SSRN Working Paper 6468338, 2026. https://ssrn.com/abstract=6468338"
  - "Academic primary target 2: Charles Lee, Joseph Lee, and Suji Lee, 'Systematic Underconfidence in Prediction Markets: Evidence from Digital Options and Cryptocurrencies', SSRN Working Paper 6748186, 2026. https://ssrn.com/abstract=6748186"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Prediction Market Pricing Anomalies vs. Execution Friction: Empirical Falsification of the Wang Transform Wedge, Favourite-Longshot Bias, and Digital Option VRP on Kalshi

## Provenance

- **Repository:** `https://github.com/elraffaello123-art/quant-research` (`source-reported`).
- **Author / Research Lab:** `elraffaello123-art` (collaborating with Claude Opus 5) (`source-reported`).
- **Canonical Immutable Commit SHA:** `511fab83791a81a96ff64b3e5dadc1636cc5b698` (`source-reported`).
- **Commit Date:** 2026-09-07T18:45:19Z (`source-reported`).
- **Source As-Of Date:** 2026-09-13 (`source-reported`).
- **Primary Source Documents & Code Directly Audited:**
  - `README.md`: Harness architecture, dual lookahead traps (fill vs. signal), graveyard of killed edges, and core methodology findings on permutation null construction, concentration risk, and tradeability decay (`source-reported`).
  - `docs/KALSHI_WEDGE_RESULT.md`: Core research writeup containing the replication and honest-cost audit of Yang (2026, SSRN 6468338) and Lee, Lee & Lee (2026, SSRN 6748186). Details the collapse of the Wang transform pricing parameter $\lambda$ from midpoint to executable bid, fee arithmetic on high-probability contracts, transaction-pooling artifacts in reliability diagrams, and the unhedgeability of binary option variance risk premia (`source-reported`).
  - `pm/wedge.py`: Maximum likelihood estimation script fitting directional and complement-invariant Wang transform parameters on opening quotes across midpoint, executable, and net fee tiers (`source-reported`).
  - `pm/favourites.py`: Empirical evaluation of buying favourite-side contracts ($p \ge 0.80$), quantifying the exact fee drag imposed by Kalshi's upward-rounded fee formula (`source-reported`).
  - `pm/calibration.py`: Reliability diagram reconstruction evaluating observation-weighted versus contract-weighted calibration curves across 2,184 crypto contracts (`source-reported`).
  - `pm/vrp.py`: Continuous-time delta-hedging simulation of 924 15-minute Kalshi digital binaries hedged against Binance 1-second spot data across 8 cryptocurrency pairs (`source-reported`).
  - `pm/kalshi_fetch.py`: API harvester querying Kalshi REST API endpoints (`https://api.elections.kalshi.com/trade-api/v2`) for market metadata and hourly candlestick bid/ask paths (`source-reported`).
  - `pm/wedge_report.txt`: Exact console reproduction log from `wedge.py` executed across 17,671 settled contracts (`source-reported`).
- **Target Academic Literature:**
  - Fan Yang (2026), *Pricing Prediction Markets: Incomplete Markets, Selection Rules, and Risk Premia*, SSRN 6468338. Evaluates 291,309 resolved event contracts and reports a headline pricing wedge $\lambda = 0.178$ on Kalshi hourly midpoint prices (`source-reported`).
  - Charles Lee, Joseph Lee, & Suji Lee (2026), *Systematic Underconfidence in Prediction Markets: Evidence from Digital Options and Cryptocurrencies*, SSRN 6748186. Evaluates 113,338 BTC/ETH digital options on Kalshi, asserting systematic underconfidence (favourite underpricing) and a positive variance risk premium using transaction VWAP (`source-reported`).
- **Underlying Sample & Universe:** Stratified random sample of 17,671 settled Kalshi contracts from 2026 with trading volume $\ge 100$, drawn from a 486,929-contract population (`source-reported`). A complementary sample of 2,207 minute-resolution crypto/randomness shards (`source-reported`), and 924 15-minute crypto binary contracts matched to tick-level Binance spot data across 8 symbols (`BTC`, `ETH`, `SOL`, `BNB`, `DOGE`, `ZEC`, etc.) over 11 days (`source-reported`).
- **Primary Venues:** Kalshi (CFTC-regulated central limit order book for event contracts) and Binance (spot market for delta hedging) (`source-reported`).
- **Repository Deduplication Audit:** A full grep across all existing strategy records in `alpha-strategy-research` confirmed zero prior records citing `elraffaello123-art`, commit `511fab83791a81a96ff64b3e5dadc1636cc5b698`, SSRN 6468338 (Yang 2026), or SSRN 6748186 (Lee, Lee & Lee 2026). Existing prediction-market records (`prediction-market-optimal-market-making-latent-belief-hjb-2026-09-01.md`, `prediction-market-proper-betting-accuracy-profit-conversion-2026-09-02.md`, `polymarket-15m-crypto-tri-transformer-market-making-2026-09-13.md`) focus on market-making HJB PDEs, AI forecasting score gaps, or lead-lag arbitrage, but do not provide an empirical execution-cost falsification of academic pricing anomalies.

## Economic mechanism

### Source-reported

1. **The Wang Transform Pricing Wedge Hypothesis (Yang 2026):**
   - In incomplete markets, market prices $p_{\text{mkt}} \in (0, 1)$ do not equal objective physical probabilities $p^*$, but are mapped via a one-parameter distorted probability measure known as the Wang transform:
     $$p_{\text{mkt}} = \Phi\left(\Phi^{-1}(p^*) + \lambda\right)$$
     where $\Phi$ is the standard normal cumulative distribution function.
   - A parameter $\lambda > 0$ indicates that market-quoted prices sit systematically *above* objective probabilities. Yang (2026) reports $\lambda = 0.178$ on Kalshi contracts ($N = 199,671$) and $\lambda = 0.172$ for 2026 alone ($N = 169,072$), with $\lambda$ being larger for low-volume contracts ($\ln \text{Volume} = -0.057$) and longer durations ($\ln \text{Duration} = +0.109$).
   - The paper evaluated $\lambda$ using hourly **midpoint** prices: $p_{\text{mid}} = \frac{p_{\text{bid}} + p_{\text{ask}}}{2}$.

2. **The Falsification Thesis: Mispricing vs. Liquidity Risk Premium:**
   - `elraffaello123-art` observes that midpoint prices cannot be traded. If $\lambda > 0$ reflects a behavioral mispricing (excessive demand for longshot contracts), a taker strategy can harvest alpha by selling the overpriced longshot side.
   - However, selling the longshot contract requires hitting the **bid** price, not the midpoint.
   - If $\lambda$ survives at the executable bid net of exchange fees, an executable taker edge exists. If $\lambda$ collapses or inverts between the midpoint and executable bid, the apparent wedge is simply the bid-ask spread—representing the compensation required by market makers for bearing inventory holding costs and adverse-selection risk in thin books.

3. **Favourite-Side Underpricing & Fee Rounding Barrier:**
   - Lee, Lee & Lee (2026) hypothesize that prediction market participants exhibit "systematic underconfidence," anchoring contract prices toward 0.50. This implies that favourite contracts ($p > 0.50$, e.g., 90¢–99¢) should be systematically underpriced, offering positive expected drift to buyers.
   - `elraffaello123-art` audits this hypothesis by analyzing Kalshi's exact taker fee schedule:
     $$\text{Fee} = \left\lceil 0.07 \cdot C \cdot p \cdot (1 - p) \cdot 100 \right\rceil / 100$$
     Because Kalshi rounds fees **up to the whole cent**, contracts trading near 99¢ incur a minimum fee of 1.00¢ (despite a continuous theoretical fee of 0.069¢), raising total acquisition cost to 100.00¢ for a maximum gross payout of 100.00¢.

4. **Digital Option Variance Risk Premium (VRP) & Gamma Explosion:**
   - Lee, Lee & Lee (2026) report that implied volatility ($\sigma_{\text{IV}}$) extracted from Kalshi 15-minute crypto binary options exceeds realized volatility ($\sigma_{\text{RV}}$) of the underlying spot across all asset classes, suggesting that a short binary position delta-hedged on spot yields a positive variance risk premium.
   - `elraffaello123-art` models the operational mechanics of delta-hedging a cash-or-nothing binary call, where delta is given by:
     $$\Delta = \frac{n(d_2)}{S \sigma \sqrt{\tau}}$$
     As time to expiry $\tau \to 0$ near the strike $S \approx K$, delta and gamma explode. Discrete-time hedging requires turnover that scales to thousands of dollars of spot per \$1 binary contract, rendering the trade structural fee churn.

### Research interpretation

- The findings from `elraffaello123-art` expose a pervasive econometric pitfall in empirical prediction market research: confusing the **cost of liquidity** with an **inefficient pricing anomaly**.
- In central limit order books (CLOBs) with discrete tick sizes and wide spreads, taking midpoints assigns half of the bid-ask spread to the researcher's theoretical gross margin. When an econometrician measures an apparent anomaly on midpoint prices, they are unknowingly measuring the bid-ask half-spread:
  $$\mathbb{E}[R_{\text{mid}}] = \mathbb{E}[Y - p_{\text{mid}}] = \mathbb{E}[Y - p_{\text{bid}}] - \frac{S}{2}$$
- When evaluated at executable market prices ($p_{\text{bid}}$ for sellers, $p_{\text{ask}}$ for buyers), the apparent positive alpha completely inverts. Rather than the market overpricing longshots by +1¢ to +3¢, takers who sell longshots lose −6¢ to −19¢ per contract.
- Furthermore, academic reliability diagrams that pool trade transactions without clustering or weighting across contracts suffer from severe survival and activity selection bias: contracts with long lifetimes and frequent trading dominate the sample, fabricating an optical S-curve of "underconfidence" that vanishes when each unique contract is weighted once.

## Signal

### Strategy 1: Longshot Selling (Wang Transform Wedge Fade)

1. **Formation Timestamp & Universe:**
   - Evaluated at opening of contract life, specifically the first candlestick observation at or beyond 5% of total contract lifetime:
     $$\tau_{\text{open}} = t_0 + 0.05 \cdot (t_1 - t_0) \quad (\text{source-reported})$$
   - Instrument Universe: Settled Kalshi binary event contracts with volume $\ge 100$ and midpoint $p_{\text{mid}} \in (0.02, 0.98)$ (`source-reported`).
2. **Signal & Direction:**
   - Fold contract onto its longshot side:
     $$q = \min(p_{\text{mid}}, 1 - p_{\text{mid}}) \quad (\text{source-reported})$$
   - If $p_{\text{mid}} \le 0.50$, the longshot is the YES token; enter short YES at executable bid $p_{\text{bid}}$ (`source-reported`).
   - If $p_{\text{mid}} > 0.50$, the longshot is the NO token; enter short NO (equivalent to buying YES or hitting NO bid at $1 - p_{\text{ask}}$) (`source-reported`).
3. **Exit & Holding Period:**
   - Position is held passively until contract resolution ($t_1$), settling to \$1.00 if the outcome occurs and \$0.00 otherwise (`source-reported`).

### Strategy 2: Favourite Buying (Underconfidence Fade)

1. **Formation & Filters:**
   - Screen for contracts with ask price $p_{\text{ask}} \in [0.80, 0.99]$ (`source-reported`).
   - Book quality filter: Require tight book with bid-ask spread $S \le 5¢$ ($S = p_{\text{ask}} - p_{\text{bid}}$) (`source-reported`).
2. **Signal & Entry:**
   - Buy the favourite YES contract at the market ask $p_{\text{ask}}$ (`source-reported`).
3. **Exit:**
   - Held to contract expiration; receives \$1.00 upon affirmative resolution, \$0.00 upon negative resolution (`source-reported`).

### Strategy 3: Hedged Variance Risk Premium Capture

1. **Formation & Signal:**
   - On 15-minute crypto binary contracts, invert the Black-Scholes cash-or-nothing call pricing equation to obtain implied volatility $\sigma_{\text{IV}}$:
     $$\text{Price} = \Phi(d_2), \quad d_2 = \frac{\ln(S / K) - \frac{1}{2} \sigma^2 \tau}{\sigma \sqrt{\tau}} \quad (\text{source-reported})$$
   - Calculate realized volatility $\sigma_{\text{RV}}$ from Binance high-frequency spot klines (`source-reported`).
   - If $\sigma_{\text{IV}} > \sigma_{\text{RV}}$, sell the binary contract at the market bid $p_{\text{bid}}$ (`source-reported`).
2. **Dynamic Delta Hedging:**
   - Continuously or discretely rebalance spot hedge position:
     $$\Delta_{\text{spot}} = -\frac{n(d_2)}{S \sigma \sqrt{\tau}} \quad (\text{source-reported})$$
   - Rebalancing cadence tested: 30 seconds and 180 seconds (`source-reported`).

## Required data

1. **Instruments & Markets:**
   - Binary event contracts listed on Kalshi (CFTC-regulated Designated Contract Market) (`source-reported`).
   - Spot cryptocurrency markets on Binance (`BTCUSDT`, `ETHUSDT`, `SOLUSDT`, `BNBUSDT`, `DOGEUSDT`, `ZECUSDT`) (`source-reported`).
2. **Data Fields:**
   - Kalshi candlestick paths: `end_period_ts`, `yes_bid.close_dollars`, `yes_ask.close_dollars`, `last_price_dollars`, `volume_fp` (`source-reported`).
   - Kalshi market metadata: `ticker`, `title`, `category`, `series`, `open_time`, `close_time`, `result` (`yes`/`no`), `fee_multiplier` (`source-reported`).
   - Binance high-frequency spot data: 1-second klines containing `timestamp_us`, `open`, `high`, `low`, `close`, `volume` (`source-reported`).
3. **Filtering & Preprocessing Rules:**
   - Contracts must possess at least 4 hourly candlestick observations (`source-reported`).
   - Locked or crossed markets ($p_{\text{ask}} \le p_{\text{bid}}$) are rejected (`source-reported`).
   - Empty placeholder quotes ($p_{\text{bid}} \le 0.0$ and $p_{\text{ask}} \ge 1.0$) are rejected (`source-reported`).
   - Sub-hourly automated randomness shards (prefix `KXMVE`, frequencies `fifteen_min`, `hourly`) are partitioned and evaluated separately (`source-reported`).

## Execution assumptions

1. **Fill Mechanism:**
   - **Academic Midpoint Baseline:** Assumes frictionless fills at $(p_{\text{bid}} + p_{\text{ask}})/2$ (`source-reported` academic assumption).
   - **Executable Taker Fill Model:** Taker sells execute against the resting bid $p_{\text{bid}}$; taker buys execute against the resting ask $p_{\text{ask}}$ (`source-reported`).
2. **Fee Structures:**
   - **Kalshi Taker Fee:** Exact regulatory schedule:
     $$\text{Fee} = \left\lceil 0.07 \cdot C \cdot p \cdot (1 - p) \cdot \text{multiplier} \cdot 100 \right\rceil / 100 \quad (\text{source-reported})$$
   - **Binance Spot Taker Fee:** Standard non-VIP tier of 0.10% (10 bps) per turn (`source-reported`).
3. **Slippage & Impact:**
   - Strategy models instant execution at top of book with zero market impact. Because real-world sizing on wide books would walk the limit order book, this assumption represents a conservative, optimistic bound (`source-reported`).

## Evidence

### Source-reported

All quantitative figures below trace directly to committed files in `elraffaello123-art/quant-research` (`docs/KALSHI_WEDGE_RESULT.md`, `pm/wedge.py`, `pm/favourites.py`, `pm/calibration.py`, `pm/vrp.py`, and `pm/wedge_report.txt` at commit `511fab83791a81a96ff64b3e5dadc1636cc5b698`):

#### 1. The Wang Transform Pricing Wedge ($\lambda$) Collapse

Across 17,671 settled 2026 Kalshi contracts (volume $\ge 100$, median spread 7.90¢, mean spread 30.22¢, p90 spread 91.00¢):

| Estimator Specification | Estimated $\lambda$ | Standard Error (SE) | $t$-statistic | Sample Size ($N$) |
| :--- | :--- | :--- | :--- | :--- |
| Directional, Midpoint (Paper's Estimator) | +0.0255 | 0.0103 | +2.48 ($p < 0.05$) | 17,671 |
| Complement-Invariant, Midpoint | **+0.0356** | 0.0103 | +3.45 ($p < 0.001$) | 17,671 |
| Complement-Invariant, **Executable Bid** | **−0.4413** | 0.0112 | **−39.34** ($p < 0.0001$) | 14,393 |

#### 2. Spread Stratification: The Wedge is the Spread

| Spread Bucket | $N$ | $\lambda$ at Midpoint | $\lambda$ at Executable Bid |
| :--- | :--- | :--- | :--- |
| Tight ($\le 2¢$) | 3,088 | −0.0600 ($t = -2.31$) | −0.0807 ($t = -3.08$) |
| Moderate (2¢–10¢) | 6,794 | −0.0306 ($t = -1.78$) | −0.1129 ($t = -6.45$) |
| Wide (> 10¢) | 7,789 | **+0.1141** ($t = +7.72$) | **−1.0073** ($t = -56.00$) |

- When books are tight ($\le 2¢$), there is zero positive pricing wedge at the midpoint ($\lambda = -0.060$).
- The entire positive $\lambda$ documented in academic literature lives exclusively in wide books (> 10¢ spread) and violently inverts to $\lambda = -1.0073$ once evaluated at executable bids.

#### 3. Realized Taker Payoffs (Gross vs. Net Cents per Contract)

| Quoted Probability ($q$) | Theoretical Edge @ Mid | Executable Edge @ Bid | Exchange Fee | **Net Realized Payoff** |
| :--- | :--- | :--- | :--- | :--- |
| 0.05 | +0.36¢ | −6.44¢ | 1.00¢ | **−7.44¢** |
| 0.10 | +0.61¢ | −10.04¢ | 1.00¢ | **−11.04¢** |
| 0.20 | +0.98¢ | −14.45¢ | 2.00¢ | **−16.45¢** |
| 0.35 | +1.31¢ | −17.23¢ | 2.00¢ | **−19.23¢** |
| 0.50 | +1.42¢ | −17.05¢ | 2.00¢ | **−19.05¢** |

- Selling the longshot contract at the executable bid loses 6¢ to 17¢ per contract before exchange fees, resulting in net losses between −7.44¢ and −19.23¢ per dollar of contract.

#### 4. The Two-Sided Book Correction (2026-09-01 Audit)

Filtering out placeholder books (e.g. 0.02 bid / 0.98 ask quotes that have no active market) demonstrates that functional books possess no mid-price pricing wedge:

| Book Quality Filter | $N$ | $\lambda$ at Midpoint ($t$-stat) | $\lambda$ at Executable Bid ($t$-stat) |
| :--- | :--- | :--- | :--- |
| Spread $\le 2¢$ | 2,605 | −0.023 ($t = -0.81$) | −0.047 ($t = -1.62$) |
| Spread $\le 5¢$ | 6,723 | −0.036 ($t = -2.07$) | −0.081 ($t = -4.55$) |
| Spread $\le 10¢$ | 9,137 | −0.024 ($t = -1.59$) | −0.093 ($t = -6.12$) |
| **Spread > 10¢** | 7,312 | **+0.109** ($t = +7.18$) | **−1.005** ($t = -55.97$) |

#### 5. Favourite Buying Performance (Underconfidence Falsification)

Across tight books (spread $\le 5¢$), buying favourite contracts yields negative net returns across all probability bands:

| Ask Price Band | $N$ | Win Rate | Mean Ask Price | Gross Edge | Mean Fee | **Net Return per Contract** |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0.80–0.85 | 133 | 83.46% | 82.39¢ | +1.07¢ | 1.47¢ | **−0.40¢** |
| 0.85–0.90 | 131 | 83.97% | 86.94¢ | −2.97¢ | 1.00¢ | **−3.97¢** |
| 0.90–0.93 | 86 | 88.37% | 91.15¢ | −2.78¢ | 1.00¢ | **−3.78¢** |
| 0.93–0.96 | 79 | 89.87% | 94.09¢ | −4.22¢ | 1.00¢ | **−5.22¢** |
| 0.96–0.98 | 58 | 91.38% | 96.71¢ | −5.33¢ | 1.00¢ | **−6.33¢** |
| 0.98–1.00 | 79 | 97.47% | 98.65¢ | −1.18¢ | 1.00¢ | **−2.18¢** |

- At $p = 0.99$, raw fee is 0.07¢, charged fee is 1.00¢, total cost is 100.00¢, making maximum profit exactly 0.00¢ with 99¢ capital at risk.

#### 6. Reliability Diagram Path-Length Skewness

Testing Lee, Lee & Lee (2026) Figure 4 (claiming a 24-cent underconfidence wedge):
- In Kalshi quote paths across 2,184 contracts (48,280 observations), the top 1% of contracts generate 17.6% of observations, and the top 10% generate 42.2% (maximum path length 858 observations, median 14).
- When each observation is pooled equally, an apparent 5% to 8% miscalibration curve appears.
- When each contract is weighted once, the book is calibrated to within 0.01 across the entire central range ($p \in [0.40, 0.70]$).

#### 7. Hedged Digital Option VRP Simulation (15-Minute Crypto Binaries)

Testing short Kalshi 15-minute crypto binaries delta-hedged on Binance spot across 924 contracts:
- Realized Volatility Stale-Bar Artifact: At 1-second sampling, stale zero-return bars artificially depress realized volatility, creating apparent IV/RV of 1.085 (55.8% IV > RV). At 15-second sampling, median IV/RV drops to **1.009** (50.5% IV > RV — exact coin flip).
- Execution & Hedging Friction:
  - All symbols, 30s rebalancing: Spot turnover per \$1 contract = **\$1,408**; Gross P&L = −2.22¢; Binance taker fees = 140.77¢; **Net P&L = −142.99¢**.
  - All symbols, 180s rebalancing: Spot turnover = \$751; Gross P&L = −6.36¢; Binance fees = 75.14¢; **Net P&L = −81.50¢**.
  - BTC only, 30s rebalancing: Spot turnover = \$1,738; Gross P&L = −0.94¢; Binance fees = 173.84¢; **Net P&L = −174.79¢**.
  - Decisive Falsification: Even with hedging fees set to **zero**, the strategy loses −2.22¢ gross due to gamma concentration and discrete replication tracking error near the strike at expiration.

### Independently reproduced

Not independently reproduced. All metrics and findings reflect third-party empirical audits, MLE fits, and market simulations committed by `elraffaello123-art` in repository `elraffaello123-art/quant-research` (commit `511fab83791a81a96ff64b3e5dadc1636cc5b698`).

### Negative evidence

- The academic pricing wedge ($\lambda \approx 0.178$) is completely annihilated once orders are executed at the bid: net alpha is negative across all price bands (−7.44¢ to −19.23¢ per contract).
- The positive midpoint wedge is an artifact of empty, wide books (> 10¢); in active, liquid books ($\le 2¢$), $\lambda$ is zero or slightly negative.
- Buying favourites is structurally unprofitable: realized win rates fail to exceed the ask price plus exchange fee rounding across every probability decile.
- Delta-hedging short digital options in crypto prediction markets is unexecutable: spot turnover of \$1,400+ per \$1 contract incurs catastrophic fee drag, while discrete delta hedging produces negative gross P&L even under zero-fee assumptions.

## Falsification plan

To falsify the negative finding (i.e. to identify conditions where a taker prediction market anomaly survives execution friction):

1. **Sub-Cent Fee or Maker Rebate Protocol:**
   - *Test:* Re-estimate net taker profitability on prediction venues with zero maker/taker fees or negative maker rebates (e.g., fee-free promotional campaigns on Polymarket or zero-fee limit orders).
   - *Data:* Full tick-level order book and execution logs across 5,000 resolved contracts.
   - *Research-defined falsification threshold:* Net realized profit factor $> 1.15$ with Sharpe ratio $> 1.0$ after all execution and gas costs.
   - *Action:* If unreached, maintain absolute rejection of directional prediction market taker models.
2. **True Two-Sided Liquidity Screen:**
   - *Test:* Evaluate longshot-fade alpha strictly on contracts where resting bid depth $\ge \$5,000$ within 1¢ of the best quote.
   - *Research-defined falsification threshold:* Executable $\lambda_{\text{exec}} > 0$ with $t > 3.0$ and positive net P&L after fees.
   - *Action:* Rejection confirms the wedge is purely an illiquidity premium.
3. **Continuous Delta-Hedging Barrier Options:**
   - *Test:* Evaluate whether dynamic delta hedging can achieve non-negative gross returns by replacing digital binary options with smooth barrier or vanilla European option structures where gamma does not diverge at expiry.
   - *Research-defined falsification threshold:* Gross hedging tracking error $< 0.5\%$ of contract notional.

## Crypto portability

- **Portability Status:** `adapted` (and `unproven`).
- **Venue Mechanics (Kalshi vs. Decentralized Crypto Prediction Markets):**
  - Kalshi is a centralized, CFTC-regulated exchange using US dollars, bank wires/ACH, and integer-cent fee rounding rules (`source-reported`).
  - Decentralized prediction markets (Polymarket on Polygon, Limitless on Base, Azuro) operate on-chain using USDC collateral (`research-proposed`).
- **Fee and Execution Differences:**
  - Polymarket utilizes a hybrid CLOB (off-chain order matching with on-chain settlement via CTF exchange contracts). Taker fees vary by market type (historically zero on general event contracts, with specialized fees introduced on 15-minute crypto markets) (`research-proposed`).
  - Because decentralized venues avoid the integer-penny fee rounding of Kalshi, micro-price distortions near 99¢ may differ in magnitude, but wide bid-ask spreads on thin longshot tokens remain endemic across on-chain order books (`research-proposed`).
- **Structural Risks in Crypto Porting:**
  - On-chain gas costs, RPC latency, and reorg risks during high-volatility resolution windows.
  - Oracle resolution risk: Kalshi resolves through official government or institutional data feeds; Polymarket resolves via UMA optimistic oracle voting, introducing subjective arbitration risk and token-holder consensus delays (`research-proposed`).
  - Liquidity concentration: Similar to Kalshi, Polymarket liquidity is heavily concentrated in headline political and macro events, while long-tail informational markets feature wide, unexecutable spreads (`research-proposed`).

## Limitations

- **delisted Series Censorship:** The empirical Kalshi sample was harvested by enumerating active and settled series available via public endpoints; contracts delisted prior to the scrape window were unavailable, introducing potential survivorship selection in series enumeration (`source-reported`).
- **Unreconciled Academic Level Gap:** The audit achieved complement-invariant midpoint $\lambda_{\text{mid}} = +0.0356$, whereas Yang (2026) reported $\lambda = 0.172$ for 2026 (`source-reported`). While the directional mid-to-executable collapse holds decisively across both specifications, the exact reason for the 4× to 5× level difference in raw midpoint $\lambda$ remains an unresolved provenance gap (`source-reported`).
- **Taker Execution Only:** The study does not falsify market-making profitability; market makers quoting wide books may indeed capture the spread premium, provided their inventory is not adversely selected by informed traders (`source-reported`).

## Implementation status

`not-implemented`. No implementation of Wang transform pricing, prediction market taking, or digital option delta-hedging exists in our research stack. This document represents a formal negative empirical research record.

## Adoption boundary

- Status: `research-only`.
- Adoption: `not-approved`.
- Approval Scope: `research-only`.
- This record provides definitive negative evidence regarding published academic prediction-market anomalies. It does not authorize strategy implementation, backtesting promotion, or live deployment.

## Related Wiki records

- `prediction-market-optimal-market-making-latent-belief-hjb-2026-09-01.md`
- `prediction-market-proper-betting-accuracy-profit-conversion-2026-09-02.md`
- `prediction-market-structural-volatility-wright-fisher-glosten-milgrom-2026-09-02.md`
- `polymarket-15m-crypto-tri-transformer-market-making-2026-09-13.md`
- `polymarket-negrisk-executable-arbitrage-token-conversion-2026-09-03.md`
- `[[quant/prediction-market-microstructure-and-fee-frictions]]`

## Sources

- **Primary Audit Repository:** `elraffaello123-art/quant-research`, commit `511fab83791a81a96ff64b3e5dadc1636cc5b698`, pushed 2026-09-07T18:45:19Z. https://github.com/elraffaello123-art/quant-research
- **Primary Research Document:** `docs/KALSHI_WEDGE_RESULT.md` (commit `511fab83791a81a96ff64b3e5dadc1636cc5b698`). https://github.com/elraffaello123-art/quant-research/blob/511fab83791a81a96ff64b3e5dadc1636cc5b698/docs/KALSHI_WEDGE_RESULT.md
- **Primary Code Implementations:**
  - `pm/wedge.py`: Maximum likelihood estimation of Wang transform on Kalshi order books.
  - `pm/favourites.py`: Empirical test of favourite buying and fee-rounding arithmetic.
  - `pm/calibration.py`: Reliability diagram contract-weighting vs observation-weighting audit.
  - `pm/vrp.py`: Simulation of delta-hedged 15-minute crypto binary options against Binance spot.
  - `pm/kalshi_fetch.py`: Historical market and candlestick collector for Kalshi API v2.
  - `pm/wedge_report.txt`: Full console output of the 17,671 contract empirical panel.
- **Academic Target 1:** Fan Yang, "Pricing Prediction Markets: Incomplete Markets, Selection Rules, and Risk Premia", SSRN Working Paper 6468338, 2026. https://ssrn.com/abstract=6468338
- **Academic Target 2:** Charles Lee, Joseph Lee, & Suji Lee, "Systematic Underconfidence in Prediction Markets: Evidence from Digital Options and Cryptocurrencies", SSRN Working Paper 6748186, 2026. https://ssrn.com/abstract=6748186
