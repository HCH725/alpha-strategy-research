---
schema: strategy-research-record-v1
title: Bitcoin On-Chain Cumulative Value-Days Destroyed (CVDD) Macro Floor Model
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - bitcoin
  - on-chain
  - valuation
  - coin-days-destroyed
  - macro-cycle
status: research-only
confidence: medium
source_as_of: 2019-2026
sources:
  - "https://woocharts.com/bitcoin-cvdd/"
  - "https://academy.glassnode.com/market/pricing-models/cvdd"
  - "https://bitbo.io/cvdd/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin On-Chain Cumulative Value-Days Destroyed (CVDD) Macro Floor Model

## Provenance

- **Primary Industry Source:** Willy Woo (April 2019), "Cumulative Value-Days Destroyed (CVDD) Floor Model", published on WooCharts / Twitter (`@woonomic`). Reference: [WooCharts CVDD Model](https://woocharts.com/bitcoin-cvdd/).
- **Platform Ingestion & Validation:** Glassnode Research & Academy, "CVDD (Cumulative Value-Days Destroyed) Metric Specification". Reference: [Glassnode Academy CVDD Documentation](https://academy.glassnode.com/market/pricing-models/cvdd).
- **Secondary Analytics:** Bitbo Bitcoin Metrics Framework. Reference: [Bitbo CVDD Chart & Methodology](https://bitbo.io/cvdd/).

The model builds upon the concept of Coin Days Destroyed (CDD), first introduced on the Bitcointalk forum in 2011 by user `ByteCoin`, extending it into a cumulative time-and-value-weighted macro floor pricing metric for Bitcoin.

## Economic mechanism

### Source-reported

Willy Woo posits that when Bitcoin moves from long-term, seasoned holders ("old hands") to newer market participants, two economic events occur simultaneously:
1. Accumulated holding time ("coin-days") is destroyed (reset to zero);
2. Capital is exchanged at the prevailing spot market price ($P_t$), establishing a new acquisition cost basis.

By accumulating the USD value of destroyed coin-days throughout Bitcoin's operational lifetime and dividing by the total age of the network (in days), the model computes the cumulative time-weighted capital turnover of seasoned market participants. Woo introduced an empirical calibration divisor ($6{,}000{,}000$) to map this cumulative value metric directly into the Bitcoin price domain. The resulting curve has historically traced the absolute price bottoms of major multi-year bear market cycles (2012, 2015, 2018–2019, March 2020, and November–December 2022).

### Research interpretation

The economic thesis rests on **cumulative irreversible capital absorption and long-term holder capitulation exhaustion**:

1. **Volume vs Time-Weighted Capital Flow:** Standard volume indicators treat intraday churn between short-term traders identically to the transfer of UTXOs held dormant for 5+ years. Coin Days Destroyed weights transfers by dormancy ($\text{CDD} = \text{UTXO Volume} \times \text{Holding Period}$), isolating genuine divestment by smart-money and early network accumulators.
2. **USD Value Weighting:** Multiplying daily CDD by daily spot price ($\text{CDD}_t \times P_t$) weights UTXO liquidation events by the fiat capital required to absorb them.
3. **Monotonically Ascending Macro Floor:** Because $\text{CVDD}$ is a cumulative integral of non-negative on-chain value destruction normalized by time, $\text{CVDD}_t$ is strictly monotonic non-decreasing (or grows whenever dormant coins are spent). This creates a structural upward-trending "lower bound" that reflects the expanding monetary base and historical capital retention of the Bitcoin network.
4. **Capitulation Floor Hypothesis:** When spot price falls to or touches the CVDD curve, marginal selling from long-term holders has already been fully absorbed, speculative premium is compressed to zero, and the asset trades at the cumulative replacement cost of historical holder conviction.

## Signal

1. **Daily Coin Days Destroyed (CDD):**
   For day $t$, sum across all spent Unspent Transaction Outputs (UTXOs) $i \in \mathcal{U}_t$:
   $$\text{CDD}_t = \sum_{i \in \mathcal{U}_t} v_i \times d_i$$
   where $v_i$ is the Bitcoin volume of UTXO $i$ and $d_i$ is the duration (in days) that UTXO $i$ remained unspent prior to transaction $t$.

2. **Daily Value-Days Destroyed ($VDD_t$):**
   $$VDD_t = \text{CDD}_t \times P_t$$
   where $P_t$ is the daily BTC/USD closing price.

3. **Cumulative Value-Days Destroyed (CVDD):**
   Let $\text{Age}_t$ be the total elapsed time in days from Bitcoin Genesis (2009-01-03) to day $t$:
   $$\text{CVDD}_t = \frac{\sum_{\tau=1}^{t} VDD_\tau}{\text{Age}_t \times 6{,}000{,}000}$$
   where $6{,}000{,}000$ is the constant empirical calibration parameter.

4. **CVDD Multiple / Proximity Ratio:**
   $$R_t = \frac{P_t}{\text{CVDD}_t}$$

5. **Trading & Allocation Rules:**
   - **Deep Value Macro Accumulation (Long Entry / DCA Escalation):** If $R_t \le 1.05$ (spot price within 5% of CVDD or $P_t \le \text{CVDD}_t$), trigger maximum macro long allocation / spot accumulation.
   - **Neutral Hold:** If $1.05 < R_t < 2.50$, maintain baseline strategic holding.
   - **Macro De-Risking / Distribution:** When $R_t > 4.00$ (overextended relative to cumulative floor value) combined with secondary top indicators (such as MVRV Z-Score $> 5.0$ or Puell Multiple $> 2.0$), systematically take profit or delta-hedge spot reserves.

6. **Specification Status:**
   - **Fully specified:** The mathematical formula, calibration constant ($6{,}000{,}000$), and boundary ratio rules.
   - **Underspecified:** Intraday UTXO indexing latency and whether internal miner pool restructuring or exchange cold storage rebalances are filtered out via entity clustering.

## Required data

- **UTXO Ledger History:** Full Bitcoin on-chain transaction history with exact UTXO creation timestamps, spent timestamps, and coin values.
- **Reference Price Series:** Daily BTC/USD spot OHLCV with UTC 00:00 boundary standardization across primary fiat exchanges (Coinbase, Bitstamp, Kraken, Binance).
- **Network Age Clock:** Exact calendar day count since Genesis Block (2009-01-03).

## Execution assumptions

- **Rebalancing Frequency:** Macro weekly or daily rebalancing at UTC 00:00 daily candle boundary.
- **Order Execution:** Spot accumulation via TWAP or limit orders on deep spot venues (Coinbase, Binance, Kraken).
- **Transaction Costs:** 3–10 bps spot maker/taker fee; zero funding cost for unleveraged spot holdings.
- **Holding Horizon:** Multi-month to multi-year macro cycle horizon (typically 12 to 36 months following a CVDD touch).

## Evidence

### Source-reported

- Willy Woo (2019) and Glassnode Academy report that the CVDD model accurately framed the absolute bottom of every historical Bitcoin bear market:
  - 2011/2012 bottom (~$2.00);
  - January 2015 capitulation (~$170);
  - December 2018 bear market trough (~$3,150);
  - March 2020 COVID-19 liquidity shock (~$3,850);
  - November–December 2022 FTX collapse trough (~$15,600).
- Across these macro cycles, spot price touched or wicked into the $\pm 5\%$ band of $\text{CVDD}_t$ before initiating multi-year parabolic upward expansions.
- This result is source-reported and based on historical chart fitting; it has not been independently verified in an institutional backtesting engine.

### Independently reproduced

Not independently reproduced in our research backtesting stack.

### Negative evidence

- **Empirical Calibration Risk ($6{,}000{,}000$ Divisor):** The $6{,}000{,}000$ constant is an in-sample curve-fitting parameter chosen ex-post to align with historical cycle bottoms. There is no first-principles economic derivation guaranteeing that future cycle bottoms will not bottom higher (e.g. at $R_t = 1.3$) or plunge deeper (e.g. $R_t = 0.70$) during severe macro liquidity crunches.
- **Low Signal Frequency:** The entry trigger ($R_t \le 1.05$) fires on average only once every 3 to 4 years, rendering statistical sample size small ($N \approx 5$ historical macro events).
- **Internal Exchange Shuffling Noise:** Large centralized exchange cold-wallet consolidations (e.g., Binance, Coinbase moving hundreds of thousands of dormant BTC) create massive artificial CDD spikes that permanently push CVDD upward without reflecting organic economic change of hands.

## Falsification plan

1. **Structural Floor Breach Test:** Evaluate whether Bitcoin spot price can spend more than 30 consecutive daily closes $> 15\%$ below $\text{CVDD}_t$. A sustained breakdown would falsify the hypothesis that CVDD represents an inviolable capital floor.
2. **Entity-Filtered vs Raw CDD Ablation:** Test whether replacing raw CDD with Glassnode's entity-adjusted CDD (which filters out internal exchange wallet migrations) materially alters the trajectory or predictive precision of the floor.
3. **Divisor Sensitivity Stability:** Perform walk-forward cross-validation testing varying divisors in the range $[4{,}000{,}000, 8{,}000{,}000]$ to evaluate whether parameter estimation degrades out-of-sample.
4. **Opportunity Cost / Cash Drag Benchmark:** Compare a CVDD-gated DCA strategy against a uniform daily DCA benchmark over rolling 4-year windows to verify whether waiting for CVDD touches outperforms passive systematic accumulation after accounting for cash drag.

## Crypto portability

- **Applicability:** `direct` for Bitcoin (UTXO-based blockchain with permanent transaction history).
- **Account-Based Blockchains (Ethereum, Solana):** `adapted` / `unproven`. Ethereum and account-based architectures do not natively maintain individual UTXO coin ages. Constructing CDD on Ethereum requires reconstructing virtual token-age or gas-weighted balance dormancy matrices, introducing significant architectural and heuristic variance.

## Limitations

- **Heuristic Parameterization:** Relies on an unproven $6{,}000{,}000$ scaling scalar.
- **Small Sample Size:** Only 4–5 full cycle observations since 2009.
- **UTXO Data Processing Overhead:** Requires parsing and indexing tens of gigabytes of raw Bitcoin UTXO data.
- **Research Only:** Not a complete standalone intraday strategy; serves primarily as a macro regime boundary.

## Implementation status

No implementation in our PyBroker or NautilusTrader research stack has been completed.

## Adoption boundary

Research material only. A record being present in this repository does not mean:
- Profitable;
- Validated alpha;
- Approved for implementation;
- Approved for paper trading;
- Approved for testnet;
- Approved for live trading.

## Related Wiki records

- `bitcoin-onchain-mvrv-zscore-cycle-reversal-2026-08-31.md`
- `bitcoin-onchain-puell-multiple-miner-capitulation-2026-09-01.md`
- `bitcoin-onchain-reserve-risk-hodl-conviction-2026-09-01.md`
- `bitcoin-onchain-market-cap-to-thermocap-ratio-2026-09-01.md`

## Sources

- Willy Woo (2019), "Bitcoin CVDD Model", WooCharts: https://woocharts.com/bitcoin-cvdd/
- Glassnode Academy (2020), "Cumulative Value-Days Destroyed (CVDD)": https://academy.glassnode.com/market/pricing-models/cvdd
- Bitbo (2024), "Bitcoin CVDD Interactive Chart and Documentation": https://bitbo.io/cvdd/
