---
schema: strategy-research-record-v1
title: Bitcoin On-Chain Realized HODL (RHODL) Ratio Macro Cycle Timing and Distribution Oscillator
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bitcoin
  - on-chain
  - utxo
  - rhodl-ratio
  - hodl-waves
  - macro-cycle
status: research-only
confidence: medium
source_as_of: 2024-06
sources:
  - https://www.lookintobitcoin.com/charts/rhodl-ratio/
  - https://insights.glassnode.com/the-rhodl-ratio/
  - https://medium.com/@positivecrypto/the-rhodl-ratio-a-bitcoin-macro-indicator-6368dcf03d49
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin On-Chain Realized HODL (RHODL) Ratio Macro Cycle Timing and Distribution Oscillator

## Provenance

- **Primary Source:** Philip Swift, “The RHODL Ratio: A Bitcoin Market Cycle Indicator” (July 2020), LookIntoBitcoin / Glassnode Insights publication. Public article: https://medium.com/@positivecrypto/the-rhodl-ratio-a-bitcoin-macro-indicator-6368dcf03d49 and live chart specification at https://www.lookintobitcoin.com/charts/rhodl-ratio/.
- **Methodological Foundations:** 
  - Glassnode Research & Academy, “Realized Cap HODL Waves” (2020–2024), partitioning UTXO age bands by realized dollar value.
  - Antoine Le Calvez and Coin Metrics, “Realized Capitalization” (2018), evaluating UTXOs at last-moved acquisition price.
  - Dhruv Bansal (Unchained Capital), “Bitcoin Data Science: HODL Waves” (2018).
- **Underlying Ledger Data:** The full history of the Bitcoin blockchain UTXO set, evaluating coin age (lifespan since last transaction output creation) and dollar cost-basis at the time of movement.

## Economic mechanism

### Source-reported

The RHODL (Realized HODL) Ratio is an on-chain macro valuation indicator designed to identify multi-year Bitcoin market cycle tops and generational bottoms.

The metric builds on Realized Cap HODL Waves, which track the dollar value of UTXOs across different age bands. The RHODL ratio contrasts the realized value of short-term speculative capital (UTXOs aged between 1 day and 1 week) against the realized value of medium-to-long term conviction capital (UTXOs aged between 1 year and 2 years).

To account for the aging of the Bitcoin network—where long-term dormant and lost coins naturally accumulate over time—the raw ratio is multiplied by the network's age in days. The source reports that:
1. **Cycle Tops (Euphoric Distribution):** When the RHODL Ratio surges into the upper band (historically $> 10,000$ to $50,000$), recent 1-week speculative turnover heavily outweighs 1–2 year dormant capital. This signals that long-term smart money has completed its macro distribution to euphoric retail buyers, marking imminent cyclical tops (successfully identifying the 2011, 2013, 2017, and 2021 peaks).
2. **Cycle Bottoms (Capitulation Accumulation):** When the RHODL Ratio drops into the lower band (historically $< 300$ to $500$), short-term turnover collapses while long-term hodler capital dominates the realized value base. This indicates seller exhaustion and macro accumulation, marking multi-year cycle bottoms (e.g., 2011, 2015, 2018–2019, and 2022).

### Research interpretation

The economic thesis is **on-chain capital velocity divergence and cohort wealth transfer**:
1. **Cohort Asymmetry:** In Bitcoin's unspent output topology, market cycle extremes are characterized by stark differences in the holding duration of market participants. Long-term holders accumulate during protracted bear markets when prices are depressed and volatility is subdued, causing the 1y–2y realized value band to expand.
2. **Retail Euphoria Transmission:** During bull market parabolas, ancient coins are mobilized and sold into aggressive retail demand. These coins re-enter the ledger as ultra-young UTXOs (< 1 week) with a significantly higher cost basis, causing short-term realized capital to expand exponentially relative to dormant cohorts.
3. **Market-Age Adjustment:** Multiplying by market age ($T_{\text{market}}$) compensates for the structural upward drift in the denominator caused by permanently lost coins (e.g., Satoshi coins) and increasing structural hodling illiquidity across halving epochs.

## Signal

1. **Realized Value Calculation:**
   For each UTXO $u$ in the unspent transaction output set at daily timestamp $t$:
   $$\text{Realized Value}(u, t) = \text{Amount}(u) \times P_{\text{creation}}(u)$$
   where $P_{\text{creation}}(u)$ is the BTC/USD spot reference price on the day UTXO $u$ was minted on-chain.

2. **Realized Cap HODL Bands:**
   - **Short-Term Band ($RC_{1\text{w}, t}$):** Total realized value of UTXOs with age $\tau \in [1\text{ day}, 7\text{ days}]$:
     $$RC_{1\text{w}, t} = \sum_{u \in \text{UTXO}(t), 1\text{d} \le \text{age}(u) \le 7\text{d}} \text{Realized Value}(u, t)$$
   - **Long-Term Band ($RC_{1\text{y}-2\text{y}, t}$):** Total realized value of UTXOs with age $\tau \in [365\text{ days}, 730\text{ days}]$:
     $$RC_{1\text{y}-2\text{y}, t} = \sum_{u \in \text{UTXO}(t), 365\text{d} \le \text{age}(u) \le 730\text{d}} \text{Realized Value}(u, t)$$

3. **RHODL Ratio Formulation:**
   $$RHODL_t = \left( \frac{RC_{1\text{w}, t}}{RC_{1\text{y}-2\text{y}, t}} \right) \times \text{Market Age (days)}_t$$
   where $\text{Market Age (days)}_t = \text{Date}_t - \text{2009-01-03}$.

4. **Research-hypothesis thresholds (not source-prescribed trading rules):**
   The public source defines the RHODL construction and interprets historically low/high zones, but it does not prescribe a production trading contract. The numerical cutoffs below are predeclared research hypotheses derived from the published chart zones and must be independently tested rather than treated as source-authored execution rules.
   - **Macro Long Accumulation / Over-Sold Regime:**
     $$\text{if } RHODL_t \le 350 \implies \text{Regime} = \text{Macro Undervalued / Accumulate Long}$$
   - **Macro Distribution / Over-Bought Exit Regime:**
     $$\text{if } RHODL_t \ge 15,000 \implies \text{Regime} = \text{Macro Overheated / Scale Out / Hedge Spot}$$
   - **Neutral / Trend-Following State:**
     $$\text{if } 350 < RHODL_t < 15,000 \implies \text{Hold baseline macro allocation or follow secondary momentum}$$

## Required data

- **Universe:** Bitcoin (BTC) spot on-chain ledger.
- **Data Source:** Full archival Bitcoin node parsing UTXO creation dates, block heights, output values, and spend timestamps.
- **Price Reference:** Daily BTC/USD volume-weighted spot index (e.g., Coin Metrics / Kaiko / CoinMarketCap) aligned with daily 00:00 UTC block timestamps.
- **Derived Time Series:** Daily aggregate $RC_{1\text{w}}$, $RC_{1\text{y}-2\text{y}}$, and elapsed calendar days from Bitcoin Genesis block.
- **Point-in-Time Requirement:** Daily UTC closure snapshot of the confirmed UTXO set. Unconfirmed mempool transactions must be excluded.

## Execution assumptions

The source is an on-chain market-cycle indicator, not an execution specification. Exact order type, venue, leverage, hedging instrument, rebalance timing, holding period, transaction-cost model, and custody workflow are **underspecified** and must not be inferred from the indicator itself. Any later PyBroker/Nautilus hypothesis must predeclare these choices independently and test them as implementation assumptions rather than source-reported rules.

## Evidence

### Source-reported

- **Cycle Top Precision:** The primary source reports that the RHODL Ratio correctly identified the exact macro peak window for all major historical Bitcoin cycles:
  - June 2011 peak ($RHODL \approx 45,000$)
  - April 2013 and November/December 2013 double peaks ($RHODL \approx 50,000$)
  - December 2017 peak ($RHODL \approx 35,000$)
  - April 2021 cycle high ($RHODL \approx 18,000$)
- **False-Peak Avoidance:** Unlike MVRV, which generated a premature peak reading during the April 2013 run-up, the RHODL Ratio did not flash an early exit during the mid-2013 correction, maintaining its regime signal through the secondary November 2013 blow-off top.
- **Cycle Bottom Precision:** The indicator entered its lower green accumulation band ($< 350$) during every major historical bear market trough:
  - November 2011 ($RHODL \approx 180$)
  - January 2015 ($RHODL \approx 220$)
  - December 2018 – February 2019 ($RHODL \approx 260$)
  - November–December 2022 FTX collapse ($RHODL \approx 310$)

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Small Sample Size:** The entire empirical history of Bitcoin spans only 4 completed 4-year halving cycles ($N = 4$). High statistical confidence under standard asymptotic distributions is not achievable due to the low number of independent cycle observations.
- **Structural Institutional Drift:** The introduction of spot Bitcoin ETFs (2024), regulated custodians (e.g., Coinbase Custody), and corporate treasuries alters the velocity of on-chain UTXOs. Large off-chain trading volumes executed within centralized omnibus wallets do not generate on-chain UTXO age transitions, potentially dampening the 1-week HODL band amplitude in modern cycles.
- **Band Degradation / Peak Compression:** The peak RHODL reading has exhibited diminishing peak amplitudes over successive cycles (from $\approx 50,000$ in 2013 down to $\approx 35,000$ in 2017 and $\approx 18,000$ in 2021), requiring adaptive or quantile-based thresholds rather than fixed static nominal levels.

## Falsification plan

The macro hypothesis should be rejected or revised if:
1. Bitcoin enters a prolonged multi-year bear market (drawdown $> 50\%$) following an accumulation signal ($RHODL < 350$) without delivering positive multi-year forward returns relative to buy-and-hold.
2. A cyclical blow-off top occurs where the RHODL ratio fails to rise above its historical median, indicating that institutional custodial off-chain flow has completely decoupled on-chain age metrics from market tops.
3. Replacing the 1-week and 1-2 year bands with randomly selected age band ratios yields superior cycle timing, showing that the economic cohort mechanism (hot retail money vs. dormant conviction capital) is spurious.
4. An out-of-sample cycle fails to show the characteristic expanding divergence between $RC_{1\text{w}}$ and $RC_{1\text{y}-2\text{y}}$ during market cycle peaks.

## Crypto portability

- **Direct** for Bitcoin (UTXO model).
- **Adapted / Unproven** for UTXO-based forks (e.g., Litecoin, Bitcoin Cash, Dogecoin) where on-chain age distributions exist but participant conviction dynamics differ significantly.
- **Not Applicable** in native form for account-based blockchains (e.g., Ethereum, Solana) where token balances do not possess distinct unspent transaction output lifespans, requiring alternative balance-weighted coin-age approximations.

## Limitations

- **Not independently reproduced.**
- **Extreme Low Frequency:** Generates actionable rebalancing signals only once or twice per 4-year cycle; cannot be utilized as a standalone intraday, daily, or weekly trading signal.
- **Off-Chain Volume Blindness:** The metric only observes settlement on the base Bitcoin blockchain, missing internal exchange matching-engine turnover, derivative open interest, and ETF creation/redemption units.
- **Threshold Non-Stationarity:** Static historical band values (e.g., $350$ and $15,000$) may suffer from parameter drift as the asset class matures and coin turnover slows.

## Implementation status

Not implemented in the research stack. No PyBroker, NautilusTrader, Paper, Testnet, or Live validation has been performed.

## Adoption boundary

This record is `research-only`, `not-implemented`, and `not-approved`. Presence in the repository does not constitute approval for live capital allocation, paper trading, or testnet deployment.

## Related Wiki records

- `bitcoin-onchain-mvrv-zscore-cycle-reversal-2026-08-31.md` — on-chain market value to realized value cycle oscillator; complementary valuation metric.
- `bitcoin-onchain-sopr-spent-output-profit-ratio-2026-08-31.md` — spent output profit ratio tracking realized profit/loss on moving UTXOs.
- `bitcoin-hash-ribbon-miner-capitulation-2026-08-31.md` — miner difficulty and hashrate capitulation cycle recovery signal.

## Sources

1. Philip Swift, “The RHODL Ratio: A Bitcoin Market Cycle Indicator”, LookIntoBitcoin / Glassnode Insights (July 2020). Live chart and documentation: https://www.lookintobitcoin.com/charts/rhodl-ratio/
2. Glassnode Insights, “The RHODL Ratio: Realized Cap HODL Waves Methodology” (2020–2024). https://insights.glassnode.com/the-rhodl-ratio/
3. Original Medium research release: https://medium.com/@positivecrypto/the-rhodl-ratio-a-bitcoin-macro-indicator-6368dcf03d49
