---
schema: strategy-research-record-v1
title: "Commodity Soybean Crush Spread Statistical Arbitrage: Cointegration Fair-Value Deviations, Look-Ahead Bias, and Out-of-Sample Decay"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - commodities
  - futures
  - crush-spread
  - statistical-arbitrage
  - cointegration
  - mean-reversion
  - look-ahead-bias
status: research-only
confidence: medium
source_as_of: 2026-09-12
sources:
  - "https://github.com/rolling-panda-san/notebooks/blob/2bf0457d2b6d46dcfd43dd2c46696505d980ee62/commodity_crush_spread_stat_arb.ipynb"
  - "David P. Simon, 'The soybean crush spread: Empirical evidence and trading strategies', Journal of Futures Markets, 19(3), pp. 271–289 (1999), DOI: 10.1002/(SICI)1096-9934(199905)19:3<271::AID-FUT1>3.0.CO;2-9"
  - "John B. Mitchell, 'Soybean futures crush spread arbitrage: Trading strategies and market efficiency', Journal of Risk and Financial Management, 3(1), pp. 63–96 (2010), DOI: 10.3390/jrfm3010063"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Commodity Soybean Crush Spread Statistical Arbitrage: Cointegration Fair-Value Deviations, Look-Ahead Bias, and Out-of-Sample Decay

## Provenance

- **Primary Source Code & Empirical Notebook:** `commodity_crush_spread_stat_arb.ipynb`
- **Canonical Repository:** `https://github.com/rolling-panda-san/notebooks`
- **Immutable Commit SHA:** `2bf0457d2b6d46dcfd43dd2c46696505d980ee62`
- **Repository Author / Maintainer:** `rolling-panda-san` (Nekopuni)
- **License:** MIT License
- **Notebook Timestamp:** Executed `11-Sep-2026 23:53 UTC`, pushed `2026-09-12T00:51:10Z`
- **Underlying Academic Foundation:**
  1. David P. Simon (Bentley College), *"The soybean crush spread: Empirical evidence and trading strategies"*, *Journal of Futures Markets: Futures, Options, and Other Derivative Products*, Vol. 19, No. 3 (May 1999), pp. 271–289. DOI: `10.1002/(SICI)1096-9934(199905)19:3<271::AID-FUT1>3.0.CO;2-9`.
  2. John B. Mitchell (Central Michigan University), *"Soybean futures crush spread arbitrage: Trading strategies and market efficiency"*, *Journal of Risk and Financial Management*, Vol. 3, No. 1 (2010), pp. 63–96. DOI: `10.3390/jrfm3010063`.
- **Deduplication Audit:** A full audit of all strategy records in `alpha-strategy-research` confirms zero existing records referencing the soybean crush spread, Simon (1999), Mitchell (2010), or `rolling-panda-san/notebooks`. Related commodity records (`bbce5f7` Reddy & Chakri 2026 on crude oil crack spreads, and `31bcd9d` Son 2026 on coffee weather stress) examine unrelated energy and soft commodity markets without agricultural processing cointegration or crush margin dynamics.

## Economic mechanism

### Source-reported

In agricultural commodity processing, soybean crushing is the physical extraction process by which raw soybeans ($S$) are processed into two joint co-products: soybean meal ($SM$, approximately 79–80% by weight, primarily consumed as animal feed protein) and soybean oil ($BO$, approximately 18–19% by weight, consumed as edible vegetable oil and industrial biofuel feedstock). 

The Gross Crush Margin (GCM) represents the gross dollar return per bushel of soybeans processed:
$$\text{GCM}_t = \left(\frac{SM_t}{2000} \times 48\right) + \left(\frac{BO_t}{100} \times 11\right) - \left(\frac{S_t}{100}\right)$$
based on standard USDA conversion estimates where 1 bushel of soybeans (60 lbs) yields approximately 48 lbs of meal and 11 lbs of oil, with approximately 1 lb of waste/shrinkage.

Economic equilibrium operates via commercial processor capacity adjustments:
1. **Compressed Crush Margin:** When the spread between product values ($SM$, $BO$) and raw input cost ($S$) collapses below variable processing costs, commercial processors curtail crushing operations, idling processing plants. This reduces immediate market demand for raw soybeans while restricting incoming supply of meal and oil, forcing the crush spread to expand back toward its cost-of-production equilibrium.
2. **Elevated Crush Margin:** Conversely, when crush margins are abnormally wide, processors operate at full capacity and pre-hedge future output margins by buying soybean futures and selling meal and oil futures (a commercial crush hedge), which bids up soybean prices and depresses meal and oil prices, compressing the margin back toward long-run equilibrium.
3. **Seasonality:** Simon (1999) documents distinct seasonal patterns: crush spreads tend to be lower during the growing season (February to June) due to relative scarcity of available old-crop soybeans prior to harvest, and higher during post-harvest delivery periods (September to November).

### Research interpretation

The hypothesized alpha mechanism is **processing-chain cointegration mean-reversion with seasonal adjustment**. Because soybeans and their meal/oil derivative products are bound by physical input-output constraints, their prices cannot drift indefinitely apart. The spread represents an economic margin bounded by the physical marginal cost of crushing and processor storage/capacity constraints.

However, as demonstrated by `rolling-panda-san`'s empirical audit, the original Simon (1999) publication suffers from severe **in-sample look-ahead conditioning**: the long-run cointegrating fair-value model was estimated across the full 10-year sample period (1985–1995), implicitly baking future price relationships into historical trading decisions. When the static cointegrating vector from 1985–1995 is carried forward into true out-of-sample trading (1995–2026), the strategy collapses entirely. Structural changes in the crushing industry—including the introduction of the US Renewable Fuel Standard (RFS/biodiesel mandates altering soybean oil demand), expansion of South American production (Brazil/Argentina), and shifting processing efficiencies—mean that the physical fair-value cointegration vector is inherently time-varying.

## Signal

### Signal Construction & Formulas

The strategy trades the commercial 1-1-1 contract crush spread on CME/CBOT:
- 1 contract Soybean Meal ($SM$): 100 short tons ($200,000\text{ lbs}$)
- 1 contract Soybean Oil ($BO$): 60,000 lbs
- 1 contract Soybeans ($S$): 5,000 bushels ($300,000\text{ lbs}$)

The nominal dollar spread for a 1-1-1 basket is defined as (`source-reported`):
$$\text{Crush Spread}_t = (SM_t \times 100) + (BO_t \times 600) - (S_t \times 50)$$
where $SM_t$ is priced in $\$ / \text{ton}$, $BO_t$ is priced in $\text{cents} / \text{lb}$, and $S_t$ is priced in $\text{cents} / \text{bushel}$.

### Long-Run Econometric Fair-Value Model

Simon (1999) and the replicating notebook estimate the long-run fair value using ordinary least squares (OLS) regression (`source-reported`):
$$S_t = \alpha + \beta_1 SM_t + \beta_2 BO_t + \gamma \cdot \text{trend}_t + \sum_{m=1}^{11} \delta_m D_{m,t} + \epsilon_t$$
where:
- $S_t$ is the front-month soybean futures settlement price in $\$ / \text{bushel}$ ($S_t / 100$);
- $SM_t$ is the front-month soybean meal settlement price in $\$ / \text{ton}$;
- $BO_t$ is the front-month soybean oil settlement price in $\text{cents} / \text{lb}$;
- $\text{trend}_t$ is an integer daily time trend index;
- $D_{m,t}$ are monthly seasonal dummy variables for January through November (December is the benchmark omitted month);
- The fair-value price deviation is defined as the residual: $e_t = S_t - \hat{S}_t$.

### Trading Rules

Two distinct strategy variants are evaluated in the primary source (`source-reported`):

#### 1. Simple Moving-Average Mean Reversion (Without Fair-Value Model)
- **Lookback window:** 5-day simple moving average $\text{SMA}_5(\text{Crush Spread}_t)$.
- **Long Crush Entry:** Enter when $\text{Crush Spread}_t < \text{SMA}_5(\text{Crush Spread}_t) - \Delta$, where threshold $\Delta \in \{\$100, \$300\}$.
  - Position: Long 1 contract $SM$, Long 1 contract $BO$, Short 1 contract $S$.
- **Long Crush Exit:** Exit when $\text{Crush Spread}_t \ge \text{SMA}_5(\text{Crush Spread}_t)$.
- **Short Crush (Reverse Crush) Entry:** Enter when $\text{Crush Spread}_t > \text{SMA}_5(\text{Crush Spread}_t) + \Delta$, where threshold $\Delta \in \{\$100, \$300\}$.
  - Position: Short 1 contract $SM$, Short 1 contract $BO$, Long 1 contract $S$.
- **Short Crush Exit:** Exit when $\text{Crush Spread}_t \le \text{SMA}_5(\text{Crush Spread}_t)$.

#### 2. Hybrid Moving-Average + Fair-Value Conditioned Model
- **Long Crush Entry:** Enter Long Crush only when **both** conditions hold:
  $$\text{Crush Spread}_t < \text{SMA}_5(\text{Crush Spread}_t) - \$100 \quad \text{AND} \quad (S_t - \hat{S}_t) \ge \theta$$
  where $\theta \in \{0.0, 0.1, 0.2\}$ is the fair-value deviation hurdle (meaning raw soybeans are overpriced relative to econometric fair value, so crush margins are cyclically depressed).
- **Long Crush Exit:** Exit when the moving-average deviation closes ($\text{Crush Spread}_t \ge \text{SMA}_5$) or when fair-value deviation reverts.
- **Short Crush (Reverse Crush) Entry:** Enter Short Crush only when:
  $$\text{Crush Spread}_t > \text{SMA}_5(\text{Crush Spread}_t) + \$100 \quad \text{AND} \quad (S_t - \hat{S}_t) \le -\theta$$
  where $\theta \in \{0.0, 0.1\}$ (meaning raw soybeans are underpriced relative to econometric fair value, so crush margins are cyclically inflated).
- **Short Crush Exit:** Exit when spread reverts back to moving average or fair value.

#### 3. Pure Calendar Seasonality Variant
- **Unconditional Long:** Continuously long 1-1-1 crush spread.
- **Short Growing Season:** Short 1-1-1 crush spread during February through June (months 2 to 6); cash/flat elsewhere.
- **Long Winter:** Long 1-1-1 crush spread during September through November (months 9 to 11); cash/flat elsewhere.
- **Combined Seasonality:** Short growing season + Long winter.

### Operational Parameters Classification

- `source-reported` MA lookback: 5 days.
- `source-reported` MA entry thresholds: $\$100$ and $\$300$ per 1-1-1 spread basket.
- `source-reported` Fair-value deviation thresholds ($\theta$): $0.0$, $0.1$, and $0.2$.
- `source-reported` Seasonal active calendar windows: growing season (February–June), post-harvest winter (September–November).
- `research-proposed` Rebalance timestamp: Daily market-on-close (MOC) after official settlement calculation.
- `research-proposed` Order type: Simultaneous limit orders pegged to previous-day settlement or market-on-open (MOO) on $T+1$.

## Required data

- **Instruments:**
  - CME/CBOT Soybean Futures (Ticker: `S`, contract unit 5,000 bushels, quote unit cents/bushel).
  - CME/CBOT Soybean Meal Futures (Ticker: `SM`, contract unit 100 short tons, quote unit $/ton).
  - CME/CBOT Soybean Oil Futures (Ticker: `BO`, contract unit 60,000 lbs, quote unit cents/lb).
- **Contract Maturity / Roll Rule:** First active (front-month) generic contract. Futures are rolled prior to delivery notice period (`source-reported` roll schedule: rolled 21 days prior to first notice date).
- **Data Frequency:** Daily settlement prices (OHLCV).
- **Timeframe & Sample Periods:**
  - In-Sample Period (Simon 1999 replication): 1985-01-01 to 1995-02-28 (2,565 trading days).
  - Recent/Full Sample Period: 2010-01-01 to 2026-09-11 (4,203 trading days).
  - Post-Publication Out-of-Sample Period: 1999-04-27 to 2026-09-11.
- **Missing Data Handling:** Forward-fill (`ffill().dropna()`) aligned across the three contracts.

## Execution assumptions

- **Return Calculation Convention:** In the source implementation (`vivace`), returns are lot-based rather than fully-collateralized percent returns:
  $$r_t = \frac{F_t - F_{t-1}}{c}$$
  where collateral $c = \$10,000$ per leg (`source-reported`). Total basket return is the sum of lot returns:
  $$r_{\text{basket}, t} = 100 \cdot r_{SM, t} + 600 \cdot r_{BO, t} - 50 \cdot r_{S, t}$$
- **Execution Timing:** `research-proposed`: Orders execute on the next day's open ($T+1$ MOO) following signal generation at $T$ close, preventing same-bar look-ahead execution.
- **Transaction Costs & Slippage:** The primary source calculates **gross returns** (`calculate_net=False`).
- `research-proposed` Cost Model: Crossing fees and exchange clearing on CME agricultural futures typically run approximately $\$2.50$–$\$4.00$ per contract per side. For a 3-legged spread (1 SM + 1 BO + 1 S), round-trip execution cost is approximately $\$15$–$\$24$ per basket. On a $\$100$ deviation target, friction absorbs 15% to 24% of the nominal gross target.
- **Margin & Leverage:** Exchange cross-margining / inter-commodity spread margin credits on CME significantly reduce initial margin for 1-1-1 crush spreads compared to individual legs.

## Evidence

### Source-reported

#### 1. Cointegration OLS Regression Estimates
- **In-Sample Period (1985–1995, 2,565 observations):**
  - $R^2 = 0.975$, Adjusted $R^2 = 0.975$, $F(14, 2550) = 7,218$ ($p < 0.0001$), $\text{Log-Likelihood} = 1,414.4$.
  - Intercept: $+1.6342$ ($t = 51.199, p = 0.000$).
  - $SM$ Coefficient: $+0.0237$ ($t = 253.360, p = 0.000$).
  - $BO$ Coefficient: $+0.0880$ ($t = 115.074, p = 0.000$).
  - Time trend: $-0.0002$ ($t = -60.761, p = 0.000$).
  - Monthly dummy coefficients ($\text{month}_1$ to $\text{month}_{11}$ vs December):
    - Jan ($\text{month}_1$): $+0.0669$ ($t = 5.027$)
    - Feb ($\text{month}_2$): $+0.1375$ ($t = 10.067$)
    - Mar ($\text{month}_3$): $+0.1551$ ($t = 11.457$)
    - Apr ($\text{month}_4$): $+0.1762$ ($t = 12.806$)
    - May ($\text{month}_5$): $+0.1766$ ($t = 12.911$)
    - Jun ($\text{month}_6$): $+0.2092$ ($t = 15.363$) [peak growing season soybean premium]
    - Jul ($\text{month}_7$): $+0.1252$ ($t = 9.194$)
    - Aug ($\text{month}_8$): $+0.0224$ ($t = 1.668, p = 0.096$)
    - Sep ($\text{month}_9$): $-0.0155$ ($t = -1.132, p = 0.258$)
    - Oct ($\text{month}_{10}$): $-0.0753$ ($t = -5.570$) [harvest low]
    - Nov ($\text{month}_{11}$): $-0.0603$ ($t = -4.390$).
- **Modern Sample Period (2010–2026, 4,203 observations):**
  - $R^2 = 0.969$, Adjusted $R^2 = 0.969$, $F(14, 4188) = 9,435$ ($p < 0.0001$).
  - Intercept: $+3.5919$ ($t = 38.739$), $SM: +0.0229$ ($t = 187.814$), $BO: +0.0970$ ($t = 171.998$).
  - Monthly seasonal dummy significance collapsed across February–June ($p > 0.10$ except April $p = 0.051$), demonstrating severe structural attenuation of the historical seasonal crush pattern.

#### 2. In-Sample Backtest Results (1985–1995, Simon 1999 Replication)
- **Long-Only Without Fair-Value Model:**
  - Threshold $\$100$: CAGR $7.20\%$, Annualized Vol $15.64\%$, Sharpe $0.460$, Max Drawdown $26.76\%$, Calmar $0.269$.
  - Threshold $\$300$: CAGR $5.16\%$, Annualized Vol $15.93\%$, Sharpe $0.324$, Max Drawdown $24.34\%$, Calmar $0.212$.
- **Long-Only With Fair-Value Conditioning:**
  - MA $\$100$, FV $0.0$: CAGR $7.57\%$, Annualized Vol $12.21\%$, Sharpe **$0.620$**, Max Drawdown $17.08\%$, Calmar $0.443$.
  - MA $\$100$, FV $0.1$: CAGR $5.52\%$, Annualized Vol $12.98\%$, Sharpe $0.425$, Max Drawdown $16.73\%$, Calmar $0.330$.
  - MA $\$100$, FV $0.2$: CAGR $3.86\%$, Annualized Vol $12.27\%$, Sharpe $0.314$, Max Drawdown $15.41\%$, Calmar $0.250$.
- **Short-Only (Reverse Crush) Without Fair-Value Model:**
  - Threshold $\$100$: CAGR $5.43\%$, Annualized Vol $12.17\%$, Sharpe $0.446$, Max Drawdown $22.87\%$, Calmar $0.237$.
  - Threshold $\$300$: CAGR $5.10\%$, Annualized Vol $6.63\%$, Sharpe **$0.769$**, Max Drawdown **$4.57\%$**, Calmar $1.117$.
- **Short-Only With Fair-Value Conditioning:**
  - MA $\$100$, FV $0.0$: CAGR $2.55\%$, Annualized Vol $7.47\%$, Sharpe $0.342$, Max Drawdown $23.94\%$, Calmar $0.107$.
  - MA $\$100$, FV $0.1$: CAGR $1.86\%$, Annualized Vol $5.12\%$, Sharpe $0.364$, Max Drawdown $15.61\%$, Calmar $0.119$.

### Independently reproduced

`Not independently reproduced.` All statistical and simulation outputs cited above represent verified extractions from `rolling-panda-san/notebooks/commodity_crush_spread_stat_arb.ipynb` (commit `2bf0457d2b6d46dcfd43dd2c46696505d980ee62`), which replicates and independently evaluates Simon (1999) and Mitchell (2010).

### Negative evidence

The notebook exposes severe empirical failures and structural vulnerabilities:

1. **Catastrophic Out-of-Sample Decay (1995–2026):**
   When the static fair-value model calibrated on 1985–1995 data is applied to the subsequent 30-year out-of-sample period, performance collapses across all specifications:
   - Long-Only Without FV ($\$100$): CAGR collapses from $7.20\%$ to **$0.02\%$**, Sharpe from $0.460$ to **$0.001$**, Max Drawdown expands to **$70.70\%$**.
   - Long-Only Without FV ($\$300$): CAGR collapses to **$-3.73\%$**, Sharpe to **$-0.066$**, Max Drawdown expands to **$98.53\%$**.
   - Long-Only With FV ($\$100$, FV $0.0$): CAGR collapses from $7.57\%$ to **$0.68\%$**, Sharpe from $0.620$ to **$0.042$**, Max Drawdown expands to **$63.73\%$**.
   - Short-Only Without FV ($\$100$): CAGR collapses to **$1.48\%$**, Sharpe to **$0.161$**, Max Drawdown expands to **$72.51\%$**.
   - Short-Only Without FV ($\$300$): Suffers complete portfolio failure (CAGR `NaN`, Max Drawdown **$114.40\%$**).
   - Short-Only With FV ($\$100$, FV $0.0$): CAGR collapses to **$0.25\%$**, Sharpe to **$0.048$**, Max Drawdown expands to **$38.17\%$**.
2. **Identification of In-Sample Look-Ahead Bias in the Literature:**
   Simon (1999) published positive trading results based on an in-sample econometric model that estimated cointegration parameters over the entire sample. The notebook explicitly identifies: *"In Simon 1999, the author mentions that the trading strategy is performed in-sample, which suggests that the long-run fair value model was fit with the entire data sample. Because of this, the strategy contains a look-ahead bias and not a valid trading strategy."*
3. **Severe Parameter Sensitivity:**
   Strategy returns vary drastically between small shifts in entry hurdles (e.g., $\$100$ vs $\$300$, or FV $0.0$ vs $0.2$), characteristic of unregularized data snooping.
4. **Structural Regime Instability:**
   The relationship between soybeans, meal, and oil shifted dramatically after 2005 due to federal biofuel mandates (US RFS), which structurally elevated soybean oil value independently of animal feed protein demand. A static cointegrating vector cannot accommodate shifts in input-output economic shadow prices.
5. **Pure Seasonality Failure:**
   The standalone seasonal trading strategy exhibits deeply negative or unviable long-term risk-adjusted returns:
   - Unconditional Long: CAGR $-4.93\%$, Sharpe $-0.140$, Max Drawdown $99.55\%$.
   - Short Growing Season: CAGR $-0.83\%$, Sharpe $-0.036$, Max Drawdown $92.89\%$.
   - Short Growing + Long Winter: CAGR $+1.52\%$, Sharpe $+0.054$, Max Drawdown $95.01\%$.

## Falsification plan

To determine whether an adaptive, rolling-cointegration variant of the soybean crush spread possesses any genuine residual alpha, the following operational tests must be executed:

1. **Strict Walk-Forward Rolling Cointegration Audit:**
   - **Protocol:** Calibrate the OLS cointegrating vector on a rolling 3-year or 5-year window with 1-year purging. Re-estimate monthly dummy coefficients and time trends dynamically without future data access.
   - `research-defined falsification threshold`: If the rolling walk-forward strategy fails to achieve an out-of-sample Sharpe ratio $\ge 0.50$ net of $\$20$ round-trip friction, the crush spread cointegration hypothesis is rejected as economically unviable.
2. **Execution Lag & Slippage Sensitivity:**
   - **Protocol:** Apply a 1-day execution lag (enter on $T+1$ close or $T+2$ open after observing signal at $T$ close).
   - `research-defined falsification threshold`: If adding a 1-day execution delay reduces net annualized return by $\ge 50\%$, the apparent edge is an artifact of same-day settlement execution assumptions.
3. **Transaction Cost Floor Test:**
   - **Protocol:** Sweep round-trip multi-leg execution costs from $\$0$ to $\$40$ per 1-1-1 spread contract in $\$5$ increments.
   - `research-defined falsification threshold`: If net Sharpe ratio drops below zero at round-trip costs $\le \$15$ per basket, the strategy cannot survive real-world CME exchange and broker clearing fees.
4. **Biofuel Regime Shift Chow Test:**
   - **Protocol:** Split out-of-sample data at the enactment of the Energy Policy Act of 2005 (RFS1) and Energy Independence and Security Act of 2007 (RFS2). Test whether cointegrating residuals remain stationary using augmented Dickey-Fuller (ADF) and Johansen trace tests.
   - `research-defined falsification threshold`: If cointegration is rejected ($p > 0.05$) in the post-2005 regime, the physical input-output price relationship does not form a stationary trading band.

## Crypto portability

- **Portability Status:** `unproven` / `adapted`.
- **Traditional-Asset Origin:** The soybean crush spread is an agricultural processing arbitrage based on physical extraction yields of agricultural commodities. It does not exist natively in crypto spot or perpetual markets.
- **Ported Conceptual Analogues (`research-interpretation`):**
  1. **PoW Mining Hashrate / Energy Spread:** The closest structural crypto analogue is the Bitcoin mining gross margin: input cost (electricity, kWh priced in USD) versus output product (BTC block rewards + transaction fees). When hash price falls below energy break-even, miner capitulation curtails hashrate.
  2. **Liquid Staking Token (LST) Redemption Arbitrage:** Input (ETH) versus staked derivative outputs (stETH, rETH) plus staking yields. Deviations are bounded by the staking exit queue latency and execution costs.
  3. **Synthetic Perps on Decentralized Perps (HIP-1 / Synthetix):** If decentralized perpetual venues list synthetic agricultural commodity perps ($S$, $SM$, $BO$), the 1-1-1 spread could theoretically be executed on-chain. However:
     - Synthetic funding rate divergence across three synthetic perps would likely exceed the small physical cointegration margin;
     - Asymmetric liquidity and oracle update latencies between $S$, $SM$, and $BO$ would expose the multi-leg position to oracle front-running and execution slippage.

## Limitations

- **Source Code Availability:** The underlying backtesting engine (`vivace`) used by `rolling-panda-san` is proprietary and not open-sourced, though the complete Jupyter notebook, mathematical formulas, regression inputs, and executed cell outputs are fully public under MIT license.
- **Gross Returns Assumption:** All reported backtest figures exclude transaction commissions, exchange fees, bid-ask spread crossing, and roll slippage.
- **Look-Ahead Bias in Foundational Paper:** The classic paper on this anomaly (Simon 1999) used an in-sample cointegration model, invalidating its original reported Sharpe ratios as tradable alphas.
- **Static vs. Rolling Cointegration:** The notebook test demonstrates that holding a 1985–1995 static vector fixed causes total out-of-sample strategy failure. It does not prove whether a rolling Kalman-filter or Johansen cointegration vector could recover tradability.
- **Capital Intensity & Margin Requirements:** Trading three simultaneous futures contracts with daily mark-to-market introduces cash-drag and margin call risk during extended spread widening events.

## Implementation status

- `not-implemented`: This strategy record captures external research from `rolling-panda-san/notebooks` (commit `2bf0457d2b6d46dcfd43dd2c46696505d980ee62`), Simon (1999), and Mitchell (2010).
- No implementation has been created or executed in `nautilus-quant-system`, PyBroker, or NautilusTrader.
- No strategy family or operational pipeline has been authorized.

## Adoption boundary

- `research-only`: This record represents normalized research and negative empirical evidence for intake review.
- `not-approved`: This strategy is not approved for live trading, testnet, paper trading, or production deployment.
- A recording here serves primarily as a vital negative-evidence reference and cautionary case study on **in-sample cointegration look-ahead bias and structural multi-decade parameter decay in physical commodity processing spreads**.

## Related Wiki records

- `[[quant/sp500-statistical-arbitrage-johansen-ou-ablation-multiple-testing-2026-09-12]]` — Cointegration vector instability and multiple-testing ablation in equity statistical arbitrage baskets.
- `[[quant/convex-cross-impact-transient-execution-relative-value-2026-09-08]]` — Convex cross-impact and execution friction in multi-leg commodity relative-value calendar spreads.
- `[[quant/path-signature-decomposition-segmented-levy-area-futures-pair-trading-2026-09-03]]` — Path signature non-linear cointegration in agricultural commodity futures pairs (including ZC, ZS, ZL).
- `[[quant/crypto-adjacent-futures-weekly-basis-return-reversal-2026-09-03]]` — Short-term term-structure reversal across adjacent futures contract maturities.
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` — Methodological standards for detecting in-sample conditioning and look-ahead contamination.

## Sources

1. **Rolling Panda San (Nekopuni)**, *"Commodity crush spread statistical arbitrage"*, Jupyter Notebook `commodity_crush_spread_stat_arb.ipynb`, GitHub repository `rolling-panda-san/notebooks`, commit `2bf0457d2b6d46dcfd43dd2c46696505d980ee62`, executed `11-Sep-2026 23:53 UTC`, pushed `2026-09-12T00:51:10Z`. Available at: [https://github.com/rolling-panda-san/notebooks/blob/2bf0457d2b6d46dcfd43dd2c46696505d980ee62/commodity_crush_spread_stat_arb.ipynb](https://github.com/rolling-panda-san/notebooks/blob/2bf0457d2b6d46dcfd43dd2c46696505d980ee62/commodity_crush_spread_stat_arb.ipynb). Raw notebook source: [https://raw.githubusercontent.com/rolling-panda-san/notebooks/2bf0457d2b6d46dcfd43dd2c46696505d980ee62/commodity_crush_spread_stat_arb.ipynb](https://raw.githubusercontent.com/rolling-panda-san/notebooks/2bf0457d2b6d46dcfd43dd2c46696505d980ee62/commodity_crush_spread_stat_arb.ipynb).
2. **David P. Simon**, *"The soybean crush spread: Empirical evidence and trading strategies"*, *Journal of Futures Markets: Futures, Options, and Other Derivative Products*, Vol. 19, No. 3, May 1999, pp. 271–289. DOI: [10.1002/(SICI)1096-9934(199905)19:3<271::AID-FUT1>3.0.CO;2-9](https://doi.org/10.1002/(SICI)1096-9934(199905)19:3%3C271::AID-FUT1%3E3.0.CO;2-9).
3. **John B. Mitchell**, *"Soybean futures crush spread arbitrage: Trading strategies and market efficiency"*, *Journal of Risk and Financial Management*, Vol. 3, No. 1, 2010, pp. 63–96. DOI: [10.3390/jrfm3010063](https://doi.org/10.3390/jrfm3010063).
