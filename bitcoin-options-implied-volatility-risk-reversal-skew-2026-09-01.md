---
schema: strategy-research-record-v1
title: Bitcoin Options Implied Volatility Risk-Reversal Skew Predictor
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - options
  - implied-volatility
  - risk-reversal
  - volatility-smile
  - bitcoin
  - deribit
status: research-only
confidence: high
source_as_of: 2026-05
sources:
  - https://ink.library.smu.edu.sg/etd_coll/597/
  - https://doi.org/10.2139/ssrn.4820114
  - https://www.deribit.com
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin Options Implied Volatility Risk-Reversal Skew Predictor

## Provenance

- **Primary Academic Source:** Meng Hwee Neo, “Bitcoin options risk-reversal predictability,” PhD Dissertation in Business (General Management), Singapore Management University (SMU), May 2026. Supervised by Prof. Jianfeng Hu. Institutional repository: InK@SMU, https://ink.library.smu.edu.sg/etd_coll/597/.
- **Data Source:** Daily Bitcoin options implied volatility smiles, delta-tenor grids, and trades from Deribit (representing >90% of global crypto options open interest and volume), covering April 2021 through December 2025 (1,723 daily observations).
- **Core Signal Concept:** Directional skewness of the implied volatility smile measured via the Risk-Reversal (RR) spread across fixed-delta strikes and maturity tenors.

## Economic mechanism

### Source-reported

In options pricing theory, the volatility smile reflects non-normality, jump expectations, and market participant sentiment. The **risk-reversal (RR)** spread—defined as the difference between out-of-the-money (OTM) call implied volatility and out-of-the-money (OTM) put implied volatility at matching delta—measures directional asymmetry in the pricing of upside versus downside volatility.

Neo (2026) investigates whether the Bitcoin options risk-reversal spread possesses predictive power for subsequent Bitcoin spot returns. The author reports that:
1. When options market participants pay a premium for right-tail upside convexity relative to downside protection (positive RR spread), subsequent Bitcoin spot returns are statistically significantly positive.
2. The predictive power is concentrated in the 30-day to 180-day maturity band and extends to deep out-of-the-money (10-delta) strikes.
3. The return persistence pattern (strongest on Day 1 and extending through Day 6) supports an **information-transmission mechanism** where informed institutional order flow in options markets leads spot price discovery, rather than transitory liquidity-driven price pressure.

### Research interpretation

The strategy is a **derivatives-to-underlying information transmission alpha**:
1. **Informed Capital Allocation in Convexity:** In cryptocurrency markets, sophisticated directional traders and institutional market participants utilize options to obtain asymmetric upside exposure with defined downside risk, particularly around macro events, regulatory decisions, or halving cycles.
2. **Implied Volatility Asymmetry as Sentiment / Demand Proxy:** Unlike traditional equity markets where index options exhibit persistent negative skew (expensive puts due to crash hedging demand), Bitcoin options exhibit episodic shifts between steep positive skew (call premium / retail & institutional FOMO) and negative skew (put premium / capitulation hedging).
3. **Price Discovery Lead-Lag:** Implied volatility shifts on Deribit incorporate informed market expectations faster than fragmented spot and perpetual markets, allowing the risk-reversal spread to serve as a predictive leading indicator for underlying Bitcoin returns over multi-day holding horizons (1 to 6 days).

## Signal

The normalized quantitative signal is constructed from the Deribit daily implied volatility surface:

1. **Risk-Reversal Spread Calculation:**
   At daily snapshot timestamp $t$ (standardized at 08:00 UTC Deribit settlement cutoff), extract the implied volatilities for standardized delta ($\Delta$) and tenor ($\tau$):
   $$RR_{\Delta, \tau, t} = IV_{\text{Call}}(\Delta, \tau, t) - IV_{\text{Put}}(\Delta, \tau, t)$$
   - Primary benchmark specification: $\Delta = 0.25$ (25-delta), $\tau = 90$ days.
   - Robustness tenor set: $\tau \in \{30, 60, 90, 180\}$ days; delta set: $\Delta \in \{0.10, 0.25\}$.

2. **Butterfly Spread (Curvature / Jump Risk Component):**
   $$BF_{\Delta, \tau, t} = \frac{IV_{\text{Call}}(\Delta, \tau, t) + IV_{\text{Put}}(\Delta, \tau, t)}{2} - IV_{\text{ATM}}(\tau, t)$$

3. **Trading Rule / Alpha Formation:**
   - **Directional State:** Form a z-score or quantile rank of $RR_{25\Delta, 90d, t}$ over a trailing lookback window (e.g., 30–90 days) or evaluate the raw sign / threshold.
   - **Long Position:** Enter / maintain long exposure in BTC spot or perpetual futures when $RR_{25\Delta, 90d, t} > 0$ (or upper quintile), indicating call IV pricing exceeds put IV pricing.
   - **Short / Neutral Position:** Reduce exposure, exit to cash, or establish a short position when $RR_{25\Delta, 90d, t} < 0$ (or lower quintile), indicating put IV pricing exceeds call IV pricing.
   - **Holding Horizon:** $K = 1$ to $6$ days, re-evaluated daily at the 08:00 UTC observation boundary.

## Required data

- **Venue:** Deribit options market.
- **Instrument Set:** BTC European cash-settled options across the full expiration schedule.
- **Data Granularity:** Daily implied volatility surface snapshots at 08:00 UTC, including 10-delta, 25-delta, and 50-delta (ATM) implied volatilities interpolated across standard tenors (30d, 60d, 90d, 180d).
- **Underlying Price:** Bitcoin spot index (Deribit BTC index / composite spot reference).
- **Derived Metrics:** ATM implied volatility, 25-delta Risk-Reversal, 10-delta Risk-Reversal, 25-delta Butterfly Spread, BTC-DVOL index.
- **Data Availability / Point-in-Time:** Strict point-in-time calculation at 08:00 UTC ensuring no lookahead bias into the subsequent daily return window.

## Execution assumptions

- **Execution Timing:** Next-interval execution (e.g., 08:05 UTC) immediately following daily IV snapshot and settle.
- **Execution Instrument:** BTC spot or BTC-USDT / BTC-USD perpetual futures contracts.
- **Friction Model:** Academic baseline reports gross econometric significance; live implementation must incorporate:
  - Taker exchange fees: 2 to 5 bps.
  - Bid-ask spread on BTC perpetuals: ~1 bp.
  - 8-hour funding rate payments on perpetual futures when maintaining directional exposure.
- **Slippage / Capacity:** BTC spot and perpetual futures have high liquidity ($>\$10\text{B}$ daily volume), providing substantial capacity for this macro-directional signal.

## Evidence

### Source-reported

- **Statistical Significance of Risk-Reversal:** In the primary specification (25-delta, 90-day maturity), the risk-reversal coefficient is statistically significant at the **1% level** ($p < 0.01$) in a 13-variable baseline regression incorporating Newey–West standard errors across the full April 2021 – December 2025 sample (1,723 daily observations).
- **Maturity Band Robustness:** Predictive significance is concentrated in the **30-day to 180-day maturity band**.
- **Deep OTM Strikes:** The effect remains statistically significant at **10-delta strikes**, demonstrating that asymmetric tail-risk expectations also carry directional predictive power.
- **Persistence Horizon:** The return predictability is highest on **Day 1** following the signal and remains statistically significant through **Day 6**, indicating persistent information incorporation rather than instantaneous noise.
- **Butterfly Spread (BF):** Butterfly spreads also exhibit statistically significant predictive power for returns in the pre-2024 sample period.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Structural Attenuation Post-January 2024:** The study documents a notable structural break coinciding with the approval and launch of US Spot Bitcoin ETFs in January 2024:
  - In the pre-2024 subperiod, both RR and BF coefficients were significant at the **1% level**.
  - In the post-January 2024 subperiod, the RR signal weakened to the **5% significance level**, and the BF signal lost statistical significance entirely.
  - This degradation supports the **Adaptive Markets Hypothesis**: increased institutional participation, arbitrage efficiency, and liquidity deepening in spot/ETF markets reduce the lead-time and profitability of options smile signals.
- **Single-Asset Constraint:** The empirical evidence is demonstrated primarily on Bitcoin; applicability to Ethereum or smaller altcoins with less liquid options markets is unproven.

## Falsification plan

The hypothesis should be considered rejected or materially compromised if:
1. Out-of-sample testing on 2026+ data demonstrates that the Newey–West $t$-statistic for the 25-delta 90-day RR spread falls below $1.96$.
2. Incorporating realistic trading frictions (5 bps round-trip transaction costs and 8-hour perpetual funding costs) reduces the strategy's net annualized Sharpe ratio below $0.4$.
3. A randomized placebo test (permuting the date alignment of the Deribit IV surface relative to spot returns) yields comparable predictive $t$-statistics, indicating spurious econometric fit.
4. Conditioning on contemporaneous spot momentum subsumes the entire explanatory power of the risk-reversal spread in multi-factor spanning regressions.

## Crypto portability

- **Direct:** The strategy is developed natively on Bitcoin options from Deribit, the primary institutional cryptocurrency options venue.
- **Cross-Crypto Portability (Adapted / Unproven):** Porting the strategy from BTC to ETH or SOL options is unproven and subject to thinner liquidity in non-BTC options strikes and wider bid-ask spreads on altcoin volatility surfaces.

## Limitations

- **Not independently reproduced.**
- **Structural Alpha Decay:** Post-2024 attenuation indicates that institutional ETF inflows have compressed the predictive edge of options skew.
- **Options Data Dependency:** Requires continuous, clean implied volatility surface interpolation from Deribit; outages or illiquidity at specific tenors can cause missing signal values.
- **Funding Drag in Perpetual Implementation:** Long positions held during overheated bull markets may incur significant funding rate costs if executed via perpetual futures rather than spot.

## Implementation status

Not implemented in the research stack. No PyBroker, NautilusTrader, Paper, Testnet, or Live verification has been performed.

`implementation_status: not-implemented`

## Adoption boundary

This record is `research-only`, `not-implemented`, and `not-approved`. Presence in the repository does not constitute approval for live capital allocation, paper trading, or testnet deployment.

`status: research-only`
`adoption: not-approved`
`approval_scope: research-only`

## Related Wiki records

- `crypto-options-volatility-risk-premium-zscore-2026-08-31.md` — options variance risk premium harvesting.
- `crypto-options-implied-correlation-dispersion-2026-08-31.md` — crypto options correlation dispersion.
- `crypto-perpetual-funding-rate-carry-spot-perp-2026-08-31.md` — perpetual funding rate dynamics and carry.

## Sources

1. Meng Hwee Neo, “Bitcoin options risk-reversal predictability,” PhD Dissertation, Singapore Management University (SMU), May 2026. Institutional Knowledge at Singapore Management University (InK@SMU): https://ink.library.smu.edu.sg/etd_coll/597/.
2. Deribit Institutional Exchange Specifications and Historical Volatility Surface Archives: https://www.deribit.com.
3. Relevant SSRN working paper series on cryptocurrency option surface dynamics: https://doi.org/10.2139/ssrn.4820114.
