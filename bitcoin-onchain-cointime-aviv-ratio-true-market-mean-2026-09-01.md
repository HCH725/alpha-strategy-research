---
schema: strategy-research-record-v1
title: Bitcoin On-Chain Cointime Active-to-Investor Value (AVIV Ratio) and True Market Mean Macro Cycle Reversal
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bitcoin
  - on-chain
  - utxo
  - cointime-economics
  - aviv-ratio
  - true-market-mean
  - macro-cycle
status: research-only
confidence: high
source_as_of: 2023-08-24
sources:
  - "David Puell and James Check, 'Cointime Economics: A New Framework For Analyzing Bitcoin', ARK Invest and Glassnode Research (August 24, 2023). https://ark-invest.com/articles/analyst-research/cointime-economics"
  - "Glassnode Insights, 'The Cointime Economics Framework: Active Cap, Investor Cap, and the AVIV Ratio' (2023). https://insights.glassnode.com/the-cointime-economics-framework/"
  - "Checkmate, 'Cointime Economics: A Mathematically Symmetrical Approach to Bitcoin On-Chain Economics', Checkonchain (2023). https://checkonchain.com"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin On-Chain Cointime Active-to-Investor Value (AVIV Ratio) and True Market Mean Macro Cycle Reversal

## Provenance

- **Primary Source:** David Puell (ARK Invest) and James Check (Checkmate / Glassnode), *"Cointime Economics: A New Framework For Analyzing Bitcoin"*, published August 24, 2023. Joint research by ARK Investment Management LLC and Glassnode.
  - ARK Invest Whitepaper: https://ark-invest.com/articles/analyst-research/cointime-economics
  - Glassnode Technical Framework: https://insights.glassnode.com/the-cointime-economics-framework/
  - Checkonchain Reference Suite: https://checkonchain.com
- **Core Ledger Framework:** Time-weighted UTXO economic model based on "coinblocks" (multiplying the volume of Bitcoin transacted by the duration in blocks for which those coins remained dormant).
- **Source Data Sample:** Full Bitcoin ledger history from Genesis Block (2009-01-03) through publication as-of date (2023-08-24).

## Economic mechanism

### Source-reported

Traditional Bitcoin on-chain metrics, such as Realized Cap and the standard MVRV ratio, evaluate all UTXOs equally regardless of coin lifespan. This introduces structural distortions because millions of Bitcoins mined during the network's infancy (including Satoshi Nakamoto's estimated ~1.1 million BTC and early lost private keys) have remained unmoved for over a decade. These static coins artificially inflate unspent supply metrics and distort cost-basis estimates downward.

Cointime Economics solves this by introducing **coinblocks** ($1\text{ coinblock} = 1\text{ BTC} \times 1\text{ block}$). As new blocks are produced, Coinblocks Created ($CBC$) accumulate across circulating supply. When an unspent transaction output is spent, its accumulated coinblocks are destroyed, generating Coinblocks Destroyed ($CBD$). The ratio of cumulative coinblocks destroyed to cumulative coinblocks created defines **Cointime Liveliness**:

$$\text{Liveliness} = \frac{\sum \text{Coinblocks Destroyed}}{\sum \text{Coinblocks Created}}$$

Liveliness partitions circulating Bitcoin supply into **Active Supply** (coins actively participating in economic turnover) and **Vaulted Supply** (dormant/lost coins):

$$\text{Active Supply} = \text{Circulating Supply} \times \text{Liveliness}$$

$$\text{Vaulted Supply} = \text{Circulating Supply} \times (1 - \text{Liveliness})$$

By valuing the Active Supply at the current spot price, the framework derives **Active Cap**:

$$\text{Active Cap} = \text{Spot Price} \times \text{Active Supply}$$

To measure the actual cost basis deployed by active secondary market participants, the framework subtracts cumulative miner revenue (**Thermocap**, representing virgin coin production subsidy and transaction fees) from aggregate Realized Cap to yield **Investor Cap**:

$$\text{Investor Cap} = \text{Realized Cap} - \text{Thermocap}$$

The **Active-Value-to-Investor-Value (AVIV) Ratio** compares Active Cap to Investor Cap:

$$AVIV = \frac{\text{Active Cap}}{\text{Investor Cap}}$$

Dividing Investor Cap by Active Supply yields the **True Market Mean (TMM)** (or Active-Investor Price), representing the volume-weighted average acquisition price paid by active secondary market investors:

$$\text{True Market Mean} = \frac{\text{Investor Cap}}{\text{Active Supply}}$$

### Research interpretation

The economic thesis is **macro-scale capital accumulation, active investor cost-basis equilibrium, and cyclical mean reversion**:

1. **Filtering Lost Supply Distortions:** Unadjusted Realized Cap and MVRV drift over time as lost early coins dilute the denominator. Cointime weighting dynamically discounts dormant supply in proportion to coinblock destruction, providing an invariant metric of active investor capital turnover across multiple 4-year halving cycles.
2. **AVIV as an Equilibrium Valuation Multiplier:** 
   - When $AVIV = 1.0$, the active market capitalization exactly equals the net capital invested by secondary investors (aggregate break-even equilibrium).
   - In cyclical macro bottoms, extreme capitulation drives $AVIV < 0.55$, where the market discounts active coins below the active investor cost basis. This represents generational exhaustion of seller liquidity.
   - In cyclical bull market tops, speculative frenzy inflates $AVIV > 2.50$, indicating that active coins are priced at an unsustainable multiple of deployed active capital.
3. **True Market Mean as a Structural Regime Boundary:** The True Market Mean price ($TMM$) represents the empirical center of gravity for active Bitcoin capital. In secular bull markets, pullbacks to $TMM$ find robust institutional demand as underwater holders return to cost basis; sustained breaks below $TMM$ define transitions into macro bear regimes.

## Signal

- **On-Chain Ledger State Estimation (Daily at 00:00 UTC):**
  1. For each block $b$, calculate incremental coinblocks created: $\Delta CBC_b = \text{Supply}_b \times 1$.
  2. For each spent transaction output $j$ in block $b$, calculate coinblocks destroyed: $\Delta CBD_{j} = \text{Amount}_j \times (b - \text{BirthBlock}_j)$.
  3. Aggregate cumulative totals: $CBC_t = \sum_{b=1}^{B_t} \Delta CBC_b$ and $CBD_t = \sum_{j \in \text{Spents}(t)} \Delta CBD_j$.
  4. Compute daily Liveliness: $L_t = \frac{CBD_t}{CBC_t}$.
  5. Compute Active Supply: $S_{\text{active}, t} = S_t \times L_t$.
  6. Compute Active Cap: $Cap_{\text{active}, t} = P_t \times S_{\text{active}, t}$.
  7. Compute Investor Cap: $Cap_{\text{investor}, t} = \text{RealizedCap}_t - \text{Thermocap}_t$.
  8. Compute the AVIV Ratio: $AVIV_t = \frac{Cap_{\text{active}, t}}{Cap_{\text{investor}, t}}$.
  9. Compute True Market Mean Price: $TMM_t = \frac{Cap_{\text{investor}, t}}{S_{\text{active}, t}}$.

- **Regime Identification:**
  $$Regime_t = \begin{cases} \text{BULL} & \text{if } P_t > TMM_t \text{ and } EMA(AVIV_t, 14) > 1.00 \\ \text{BEAR} & \text{if } P_t \le TMM_t \text{ or } EMA(AVIV_t, 14) \le 1.00 \end{cases}$$

- **Operational Trading Rules:**
  - **Macro Accumulation / Long Entry (Cycle Bottom Capitulation):**
    - Condition 1 (Deep Capitulation Zone): $AVIV_t < 0.55$.
    - Trigger: $AVIV_t$ crosses back above $0.55$ (or crosses above its 14-day EMA) with daily price momentum confirmation ($P_t > EMA(P, 20\text{d})_t$).
    - Alternative Re-entry (Mid-Cycle Bull Dip): In $Regime_t == \text{BULL}$, when price pulls back to test $TMM_t$ ($P_t \in [0.97 \cdot TMM_t, 1.03 \cdot TMM_t]$) and bounces ($P_t > P_{t-1}$), enter/add to Long BTC.
  - **Macro Distribution / Long Exit (Cycle Top Euphoria):**
    - Condition: $AVIV_t > 2.50$.
    - Exit Trigger: $AVIV_t$ crosses below $2.50$ (or crosses below its 14-day EMA from overbought levels $> 2.30$), rotate 100% of portfolio to USD/stablecoins or initiate structural hedge.
  - **Bear Regime Risk Management:**
    - If $P_t$ breaks below $TMM_t$ by more than 3% and $AVIV_t < 1.00$, close all long spot/derivative exposures.

## Required data

- **Universe:** Bitcoin (BTC/USD, BTC/USDT).
- **Timeframe:** Daily on-chain aggregated block ledger state (00:00 UTC finalization).
- **Fields:**
  - Full UTXO transaction spend data (amount, block height created, block height spent).
  - Circulating coin supply series.
  - Daily Bitcoin closing price ($P_t$).
  - Historical block subsidy and transaction fee revenue (Thermocap).
  - Aggregate Realized Cap (sum of all UTXO values at creation price).
- **Availability:** Point-in-time on-chain data with minimum 2-hour finalization lag buffer to ensure network reorganization immunity.

## Execution assumptions

- **Execution Timing:** Daily rebalancing at 00:00 UTC plus 2-hour block settlement buffer (execution at 02:00 UTC).
- **Order Types:** Limit orders or 30-minute TWAP on spot/perpetual exchanges (Coinbase, Binance, Kraken, CME Bitcoin Futures).
- **Fee Model:** Standard taker fee tier (2–5 bps) and maker fee tier (1–2 bps).
- **Slippage & Impact:** 1–3 bps for BTC execution on institutional-depth order books.
- **Shorting Mechanism:** CME Bitcoin futures or perpetual swap contracts for hedging during bear regimes.

## Evidence

### Source-reported

- David Puell and James Check (ARK Invest / Glassnode, 2023) demonstrate that the AVIV ratio accurately identified all four historical Bitcoin macro cycle bottoms ($AVIV < 0.55$ in 2011, 2015, 2018–2019, March 2020, and November–December 2022) with zero false-positive bottom signals.
- Across historical cycles, euphoric macro cycle tops coincided with $AVIV > 2.50$ (June 2011, November 2013, December 2017, and March–April 2021).
- The True Market Mean price provided strict dynamic support during structural bull market retracements (e.g., 2016–2017 bull run pullbacks, late 2020 retest), whereas breaches below True Market Mean marked the onset of multi-month bear market winters (early 2018, May 2022).
- The authors show that Cointime Economics eliminates the multi-year secular downward drift observed in traditional MVRV caused by unspent Satoshi coins.

All claims above are source-reported and have not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Prolonged Submersion in Bear Markets:** During deep bear market phases (e.g., Q4 2018 to Q1 2019, Q2 to Q4 2022), the AVIV ratio remained below $0.55$ for multiple consecutive months. Unconditioned dollar-cost-averaging immediately upon first touching $0.55$ incurs substantial mark-to-market drawdown without momentum confirmation.
- **Macro Low-Frequency Regime:** Because Bitcoin macro cycles span 3–4 years, the total sample of historical cycles is small ($N \approx 4$). Statistical power for cycle-top and cycle-bottom thresholds is inherently limited.
- **ETF Structural Regime Shift:** The introduction of spot Bitcoin ETFs in 2024 introduces off-chain custodial aggregation (custodian cold wallets holding tens of thousands of BTC for multiple ETF share creators/redeemers), which may alter the velocity and coinblock destruction patterns of newly acquired institutional supply.

## Falsification plan

1. **Ablation vs. Traditional MVRV and MVRV-ZScore:** Backtest the AVIV strategy alongside classic MVRV and MVRV-ZScore over the 2011–2026 period. If AVIV does not achieve a higher Calmar ratio or lower drawdown duration, reject the Cointime active-supply adjustment hypothesis.
2. **Post-2023 Out-of-Sample Validation:** Test the $AVIV > 2.50$ and $P > TMM$ signals strictly out-of-sample across the 2024–2026 ETF cycle. If True Market Mean fails to act as support or if AVIV exceeds $2.50$ without cycle overvaluation, adjust or reject the static threshold model.
3. **Custody & Exchange Internal Rebalancing Placebo:** Simulate large exchange-wallet migrations (which destroy millions of coinblocks without economic change of ownership). If simulated internal migrations shift AVIV by $> 15\%$, invalidate the raw coinblock destruction metric without entity-adjusted filtering.

## Crypto portability

**Direct**: Cointime Economics is natively derived from the unspent transaction output (UTXO) architecture of the Bitcoin blockchain. It is directly applicable to Bitcoin and can be ported with appropriate adaptation to other UTXO blockchains (e.g., Litecoin, Dogecoin). It is not directly applicable to account-based smart contract networks (Ethereum, Solana) without simulating virtual UTXO lifespans.

## Limitations

- **not independently reproduced**: Empirical backtesting inside our NautilusTrader/PyBroker environment is pending.
- **low sample size of macro cycles**: Bitcoin has experienced only 4 major halving cycles; macro threshold overfitting is a material risk.
- **data indexing dependency**: Requires comprehensive full-node block-by-block UTXO tracking infrastructure (e.g. Glassnode, Checkonchain, or custom Bitcoin Core UTXO parser).
- **regime latency**: On-chain daily settlement requires daily candle close finalization, precluding high-frequency trading.

## Implementation status

No internal implementation in PyBroker, NautilusTrader, or live execution engines has been performed.

`implementation_status: not-implemented`

## Adoption boundary

Research material only. Does not constitute trading advice, production validation, or authorization for Paper, Testnet, or Live deployment.

`status: research-only`
`adoption: not-approved`
`approval_scope: research-only`

## Related Wiki records

- `[[bitcoin-onchain-mvrv-zscore-cycle-reversal-2026-08-31]]`
- `[[bitcoin-onchain-sopr-spent-output-profit-ratio-2026-08-31]]`
- `[[bitcoin-onchain-nvt-signal-macro-cycle-2026-08-31]]`
- `[[bitcoin-onchain-entity-adjusted-dormancy-flow-macro-bottom-2026-09-01.md]]`

## Sources

1. David Puell and James Check, "Cointime Economics: A New Framework For Analyzing Bitcoin", *ARK Invest and Glassnode Research*, August 24, 2023. URL: https://ark-invest.com/articles/analyst-research/cointime-economics
2. Glassnode Insights, "The Cointime Economics Framework: Active Cap, Investor Cap, and the AVIV Ratio", *Glassnode Research*, August 2023. URL: https://insights.glassnode.com/the-cointime-economics-framework/
3. Checkmate, "Cointime Economics: A Mathematically Symmetrical Approach to Bitcoin On-Chain Economics", *Checkonchain*, 2023. URL: https://checkonchain.com
