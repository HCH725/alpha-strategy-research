---
schema: strategy-research-record-v1
title: Bitcoin Stablecoin Supply Ratio (SSR) Oscillator and Purchasing Power Mean-Reversion
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - on-chain
  - bitcoin
  - stablecoins
  - liquidity
  - mean-reversion
  - oscillator
status: research-only
confidence: high
source_as_of: 2024-06
sources:
  - https://medium.com/glassnode-insights/quantifying-bitcoins-risk-reward-stablecoin-supply-ratio-ssr-738927914f6b
  - https://studio.glassnode.com/metrics?a=BTC&metric=indicators.ssr_oscillator
  - https://doi.org/10.2139/ssrn.3601831
  - https://doi.org/10.1111/jofi.12903
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Stablecoin Supply Ratio (SSR) Oscillator and Purchasing Power Mean-Reversion

## Provenance

- **Original Concept & Formulation:** Renato Shirakashi (2019), quantitative on-chain researcher who conceptualized the Stablecoin Supply Ratio (SSR) to quantify the aggregate buying power of fiat-pegged tokens relative to Bitcoin's market size.
- **Platform Implementations:** 
  - Glassnode Insights (Rafael Schultze-Kraft, 2020), “Quantifying Bitcoin's Risk/Reward with the Stablecoin Supply Ratio (SSR),” and Glassnode Studio metrics `stablecoin_supply_ratio` and `indicators.ssr_oscillator`.
  - CryptoQuant On-Chain Analytics (Ki Young Ju), stablecoin reserve and purchasing power tracking.
- **Academic Context:**
  - Daniele Bianchi, Luca Rossini, and Matteo Iacopini (2020), “Stablecoins and Cryptocurrency Returns: What is the Role of Tether?,” SSRN Working Paper Series, doi:10.2139/ssrn.3601831 (evaluating stablecoin liquidity shocks and crypto return predictability using Large Bayesian VARs).
  - John M. Griffin and Amin Shams (2020), “Is Bitcoin Really Untethered?,” *The Journal of Finance*, 75(4), 1913–1964, doi:10.1111/jofi.12903.

## Economic mechanism

### Source-reported

In cryptocurrency market microstructure, USD-pegged stablecoins (e.g., USDT, USDC, BUSD, DAI, USDD) serve as the primary quote currency, settlement medium, and collateral asset across centralized and decentralized exchanges. Fiat capital entering the crypto ecosystem predominantly mints into stablecoins before deploying into volatile assets.

The **Stablecoin Supply Ratio (SSR)** is defined as:
$$\text{SSR}_t = \frac{\text{MarketCap}_{\text{BTC}, t}}{\text{MarketCap}_{\text{Stablecoins}, t}} = \frac{P_{\text{BTC}, t} \times S_{\text{BTC}, t}}{\sum_{i \in \text{Stablecoin Pool}} P_{i, t} \times S_{i, t}}$$

Where the stablecoin pool aggregates all major circulating USD stablecoins. 

The economic thesis posits:
1. **High Purchasing Power (Low SSR):** When the aggregate market cap of stablecoins is large relative to Bitcoin’s market cap (low SSR), there is significant "dry powder" sitting on the sidelines or parked in exchange reserves capable of absorbing sell-side liquidity and driving price appreciation.
2. **Exhausted Purchasing Power (High SSR):** When Bitcoin’s market cap outpaces stablecoin supply expansion (high SSR), marginal buying power is thin, making the market vulnerable to liquidity withdrawal and downside corrections.
3. **SSR Oscillator:** Applying statistical normalization (200-day Bollinger Bands or rolling Z-scores) to SSR converts the raw secularly trending ratio into a stationary cyclical oscillator that flags macro overbought and oversold liquidity regimes.

### Research interpretation

The SSR Oscillator is a **structural liquidity-to-asset valuation mean-reversion alpha**:
1. **Quote-Currency Inventory Dynamics:** Unlike traditional equity markets where the broad money supply ($M_2$) is vast relative to any single equity ticker, crypto markets operate with a closed, transparent, on-chain pool of native quote money. The aggregate stablecoin market capitalization represents the active liquidity pool directly available to trade digital assets.
2. **Lagged Liquidity Deployment:** Stablecoin minting and redemption cycles reflect institutional fiat inflows and outflows. When institutional capital deposits fiat to mint stablecoins during a price consolidation, the stablecoin market cap expands before spot deployment occurs, driving SSR down into statistical oversold bands. Subsequent deployment of this dry powder into BTC spot and perp margin drives mean-reverting upward returns.
3. **Structural Stationarity via Bands:** Because stablecoin aggregate supply has grown exponentially from $<\$1\text{B}$ in 2017 to $>\$150\text{B}$ in 2024+, the raw SSR exhibits secular downward trend drift. The rolling 200-day Bollinger Band standardization removes secular supply expansion trend and isolates local cyclical deviations.

## Signal

The quantitative strategy is structured as a daily-sampled oscillator-driven mean-reversion trading model:

1. **Daily Data Aggregation:**
   At daily snapshot timestamp $t$ (standardized at 00:00 UTC):
   - Extract Bitcoin market capitalization $\text{MarketCap}_{\text{BTC}, t}$.
   - Extract aggregate market capitalization of the top tracked stablecoins:
     $$\text{StableCap}_t = \sum_{k \in \{\text{USDT, USDC, DAI, BUSD, USDD, TUSD, FDUSD}\}} \text{Supply}_{k, t} \times 1.0$$
   - Calculate raw $\text{SSR}_t = \frac{\text{MarketCap}_{\text{BTC}, t}}{\text{StableCap}_t}$.

2. **Oscillator Construction (Rolling 200-Day Bollinger Band Transformation):**
   $$\mu_{200, t} = \frac{1}{200} \sum_{i=0}^{199} \text{SSR}_{t-i}$$
   $$\sigma_{200, t} = \sqrt{\frac{1}{199} \sum_{i=0}^{199} (\text{SSR}_{t-i} - \mu_{200, t})^2}$$
   $$\text{UpperBand}_t = \mu_{200, t} + 2.0 \times \sigma_{200, t}$$
   $$\text{LowerBand}_t = \mu_{200, t} - 2.0 \times \sigma_{200, t}$$
   $$\text{SSR\_Oscillator}_t = \frac{\text{SSR}_t - \mu_{200, t}}{\sigma_{200, t}}$$

3. **Trading Rules:**
   - **Long Entry (Oversold Liquidity / High Stablecoin Dry Powder):**
     - Condition: $\text{SSR\_Oscillator}_t \le -2.0$ (or raw $\text{SSR}_t$ touches/breaches $\text{LowerBand}_t$) AND crosses back above $-2.0$.
     - Action: Enter 100% Long BTC exposure on the next daily bar open ($t+1$).
   - **Exit / De-risk (Overbought / Exhausted Purchasing Power):**
     - Condition: $\text{SSR\_Oscillator}_t \ge +2.0$ (or raw $\text{SSR}_t$ touches/breaches $\text{UpperBand}_t$) OR crosses below $+2.0$ after hitting the overbought zone.
     - Action: Exit long position to stablecoins / cash (0% exposure) or enter delta hedge.
   - **Neutral Zone ($ -1.5 < \text{SSR\_Oscillator} < +1.5$):** Maintain prevailing trend position or default to neutral allocation.

## Required data

- **Underlying Asset:** Bitcoin (BTC/USD spot).
- **On-Chain Stablecoin Supply Feeds:** Daily total circulating supply for major USD-pegged stablecoins (USDT on Ethereum/Tron/Solana, USDC, DAI, FDUSD, etc.).
- **Price Reference:** Daily BTC/USD closing price index.
- **Derived Metrics:** Aggregate Stablecoin Market Cap, Raw SSR, 200-day rolling mean ($\mu_{200}$), 200-day rolling standard deviation ($\sigma_{200}$), SSR Oscillator.
- **Point-in-Time Constraint:** Daily snapshot fixed at 00:00 UTC with all on-chain mint/burn events finalized prior to signal calculation.

## Execution assumptions

- **Execution Timing:** Daily rebalance at 00:05 UTC.
- **Instrument:** BTC spot or BTC perpetual futures.
- **Friction Model:**
  - Spot taker fee: 5 bps to 10 bps.
  - Perpetual taker fee: 2 bps to 5 bps.
  - Perpetual 8-hour funding rate impact when holding long positions during extended bull regimes.
  - Slippage on BTC at daily bar open: $< 2$ bps.
- **Turnover:** Low to medium frequency (typically 4 to 8 cyclical swing signals per calendar year).

## Evidence

### Source-reported

- **Historical Cyclical Inflection Points:** Glassnode (2020, 2024) reports that lower Bollinger Band breaches ($\text{SSR Oscillator} \le -2.0$) coincided with major local and macro bottom accumulation opportunities throughout 2019–2024:
  - December 2018 / January 2019 bottom ($\text{SSR Oscillator} < -2.5$).
  - March 2020 liquidity shock ($\text{SSR Oscillator} < -3.0$, followed by multi-hundred-percent rally).
  - May–July 2021 consolidation bottom ($\text{SSR Oscillator} \approx -2.2$).
  - November 2022 FTX crash trough ($\text{SSR Oscillator} < -2.0$).
  - October 2023 pre-ETF breakout base ($\text{SSR Oscillator} < -2.0$).
- **Academic Findings on Stablecoin Liquidity:** Bianchi, Rossini, and Iacopini (2020) find in a Large Bayesian VAR framework that positive shocks to stablecoin issuance and aggregate market cap are followed by statistically significant positive cryptocurrency price responses over multi-week horizons.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Multi-Chain Fragmentation and Supply Double-Counting:** As stablecoins proliferate across Layer 1s and Layer 2s via cross-chain bridges and wrapped tokens, simple sum of circulating supplies risks double-counting bridged/wrapped tokens unless strict entity and contract deduplication is enforced.
- **Non-Crypto Stablecoin Use Cases:** In emerging markets and global trade, substantial stablecoin volume is utilized for cross-border remittances, business payroll, and non-trading currency substitution, weakening the pure "exchange dry powder" assumption.
- **Persistent Downward Trend in Regime Shifts:** During intense bear markets (e.g., 2022 stablecoin redemptions following Terra/Luna collapse), stablecoin supply contractions can create false oscillator spikes or distorted band widths.

## Falsification plan

The SSR Oscillator alpha hypothesis will be rejected if:
1. In an out-of-sample test across 2025–2028, entering long upon lower band breaches ($\text{SSR Oscillator} < -2.0$) yields a negative 90-day forward return across $\ge 3$ consecutive signals.
2. Replacing the stablecoin denominator with a simple 200-day price moving average yields equivalent or superior Sharpe and Sortino ratios, demonstrating that SSR adds no independent information beyond raw price trend/momentum.
3. Spanning regressions of SSR Oscillator signals against standard MVRV and SOPR on-chain factors show zero statistically significant residual alpha ($t\text{-stat} < 1.96$).

## Crypto portability

- **Direct:** The strategy is built entirely on cryptocurrency market-native quote currency dynamics (Bitcoin and USD stablecoins).
- **Adapted (Ethereum / Major Layer 1s):** The ratio can be adapted to Ethereum ($\text{ETH-SSR} = \text{MarketCap}_{\text{ETH}} / \text{StableCap}$) or Solana, though altcoin market caps are more heavily influenced by individual token unlock schedules and rotational flow.

## Limitations

- **Not independently reproduced.**
- **Stablecoin Universe Definition Risk:** Exclusion of fast-growing new stablecoins (e.g., USDe, PYUSD) or failure to remove deprecated/depegged stablecoins (e.g., UST in May 2022) introduces metric distortion.
- **Structural Break from Spot ETFs:** Post-2024 spot Bitcoin ETFs allow institutional capital to enter BTC directly through traditional fiat brokerages without minting on-chain stablecoins, potentially diluting the explanatory power of purely on-chain stablecoin metrics over time.

## Implementation status

Not implemented in the research stack. No PyBroker, NautilusTrader, Paper, Testnet, or Live verification has been performed.

`implementation_status: not-implemented`

## Adoption boundary

This record is `research-only`, `not-implemented`, and `not-approved`. Presence in the repository does not constitute authorization for live trading, testnet, or capital allocation.

`status: research-only`
`adoption: not-approved`
`approval_scope: research-only`

## Related Wiki records

- `bitcoin-onchain-mvrv-zscore-cycle-reversal-2026-08-31.md` — MVRV Z-Score cycle valuation.
- `bitcoin-onchain-net-unrealized-profit-loss-nupl-macro-cycle-2026-09-01.md` — Net Unrealized Profit/Loss on-chain cycle oscillator.
- `bitcoin-onchain-nvt-signal-macro-cycle-2026-08-31.md` — NVT Signal macro mean reversion.
- `crypto-perpetual-funding-rate-carry-spot-perp-2026-08-31.md` — Perpetual funding rate carry.

## Sources

1. Renato Shirakashi, Original Stablecoin Supply Ratio formulation and analytics research (2019).
2. Rafael Schultze-Kraft, “Quantifying Bitcoin's Risk/Reward with the Stablecoin Supply Ratio (SSR),” Glassnode Insights, 2020: https://medium.com/glassnode-insights/quantifying-bitcoins-risk-reward-stablecoin-supply-ratio-ssr-738927914f6b.
3. Glassnode Studio On-Chain Metric Documentation for SSR and SSR Oscillator: https://studio.glassnode.com/metrics?a=BTC&metric=indicators.ssr_oscillator.
4. Daniele Bianchi, Luca Rossini, Matteo Iacopini (2020), “Stablecoins and Cryptocurrency Returns: What is the Role of Tether?,” SSRN Electronic Journal, doi:10.2139/ssrn.3601831.
5. John M. Griffin and Amin Shams (2020), “Is Bitcoin Really Untethered?,” *The Journal of Finance*, 75(4), pp. 1913–1964, doi:10.1111/jofi.12903.
