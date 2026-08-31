---
schema: strategy-research-record-v1
title: Bitcoin On-Chain Market-Cap-to-Thermocap Ratio Macro Valuation Cycle
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - bitcoin
  - on-chain
  - thermocap
  - miner-economics
  - valuation
  - macro-regime
status: research-only
confidence: medium
source_as_of: 2024-03-01
sources:
  - "https://academy.glassnode.com/market/thermocap"
  - "https://academy.glassnode.com/market/market-cap-to-thermocap-ratio"
  - "https://coinmetrics.io/community-network-data/"
  - "https://medium.com/@nic__carter/a-new-cryptoasset-fundamental-introducing-thermocap-562725359489"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin On-Chain Market-Cap-to-Thermocap Ratio Macro Valuation Cycle

## Provenance

Primary on-chain conceptual source: Nic Carter and Antoine Le Calvez (Coin Metrics), *A new cryptoasset fundamental: introducing Thermocap*, published October 2018 (Medium / Coin Metrics Research: https://medium.com/@nic__carter/a-new-cryptoasset-fundamental-introducing-thermocap-562725359489).

Canonical metric definition and historical multiple framework documented by Glassnode Academy:
- *Thermocap*: https://academy.glassnode.com/market/thermocap
- *Market Cap to Thermocap Ratio*: https://academy.glassnode.com/market/market-cap-to-thermocap-ratio

Thermocap aggregates the cumulative USD value of all block rewards (newly minted block subsidies plus transaction fees) distributed to Proof-of-Work miners since network genesis. The Market Cap to Thermocap Ratio compares the prevailing spot market capitalization to this cumulative capital expenditure.

Exact block-level transaction fee timestamp alignment and daily pricing aggregation nuances across independent data vendors remain **underspecified** in public documentation.

## Economic mechanism

### Source-reported

In Proof-of-Work blockchain networks, Thermocap represents the total aggregate capital expenditure paid out to miners to secure the ledger from inception to date. Unlike Market Capitalization (which applies the latest marginal trade price to all outstanding coins regardless of whether they are active or lost) and Realized Capitalization (which values coins at their last on-chain movement), Thermocap captures the cumulative thermodynamic production cost basis of the asset.

The Market Cap to Thermocap (MC/TC) ratio measures the monetary premium that the market currently assigns to Bitcoin over and above its cumulative security production cost. Source documentation reports that during historical bull market peaks, market capitalization expanded to between 32x and 64x of Thermocap, reflecting extreme speculative enthusiasm. Conversely, during macro bear market bottoms, the multiple contracted into the 2x to 6x range, where market capitalization closely approached cumulative miner investment and flushed out speculative excess.

### Research interpretation

The falsifiable hypothesis is that **Bitcoin's market price exhibits bounded cyclical valuation multiples relative to its cumulative aggregate production expenditure (Thermocap)**:

1. **Speculative Overextension Regimes ($MCTR > 32\text{x}$)**: When market capitalization trades at extreme multiples of cumulative miner spend, the network's market price is heavily driven by speculative momentum rather than fundamental network security costs. Forward medium-term (6 to 24 month) risk-adjusted returns deteriorate, and severe tail-drawdown probability rises.
2. **Cost-Floor Accumulation Regimes ($MCTR < 6\text{x}$)**: When the multiple compresses near historical production expenditure floors, the asset is deeply undervalued relative to historical capital investment, signaling macro accumulation zones with asymmetric positive forward returns.
3. **Macro Risk Management Overlay**: The metric serves as a low-turnover macro exposure filter rather than a high-frequency directional trading signal.

## Signal

1. **Daily Miner Revenue ($R_d$):** For each calendar day $d$ from Bitcoin genesis (2009-01-03) to $t$:
   $$R_d = \left(\text{BlockSubsidy}_d + \text{TxFees}_d\right) \times P_d$$
   where $\text{BlockSubsidy}_d$ is total newly minted BTC on day $d$, $\text{TxFees}_d$ is total transaction fees paid in BTC, and $P_d$ is the daily volume-weighted spot reference price in USD.

2. **Cumulative Thermocap ($\text{TC}_t$):**
   $$\text{TC}_t = \sum_{d=1}^t R_d$$

3. **Market Cap to Thermocap Ratio ($\text{MCTR}_t$):**
   $$\text{MCTR}_t = \frac{\text{MarketCap}_t}{\text{TC}_t} = \frac{P_t \times S_t}{\text{TC}_t}$$
   where $S_t$ is the circulating Bitcoin supply at day $t$.

4. **Macro State Classification & Exposure Rules:**
   - **Deep Value / Accumulation ($MCTR_t < 6.0$ or $MCTR_t \le \text{Quantile}_{0.15}(MCTR_{1..t})$):** Allocate 100% target spot exposure (Long).
   - **Neutral Trend ($6.0 \le MCTR_t < 32.0$):** Maintain standard trend-following baseline allocation.
   - **Elevated Overvaluation ($32.0 \le MCTR_t < 48.0$):** Reduce gross exposure to 50% (Derisking).
   - **Extreme Overheating / Macro Top ($MCTR_t \ge 48.0$ or $MCTR_t \ge \text{Quantile}_{0.95}(MCTR_{1..t})$):** Defensive allocation (0% exposure or delta-neutral hedging).

5. **Timing:** Computed daily at UTC 00:00 close. State transitions trigger execution on day $t+1$ open.

## Required data

- Complete historical daily on-chain block subsidies and transaction fees from Bitcoin Genesis block (2009-01-03) to present.
- Point-in-time daily USD reference price series for BTC.
- Daily circulating coin supply $S_t$.
- Continuous on-chain data ingestion pipeline to prevent lookahead or revised block accounting.

## Execution assumptions

- Execution occurs at daily UTC boundary on liquid spot or linear perpetual venues (e.g. Binance BTC/USDT, Coinbase BTC/USD).
- Market order or VWAP execution on large cap Bitcoin markets; slippage and fee impact are minimal due to low annual turnover (< 2–4 rebalances per cycle).
- Funding costs apply if linear perpetual contracts are used for delta-neutral hedging during bubble regimes.

## Evidence

### Source-reported

- Glassnode Academy and Coin Metrics empirical studies report that Bitcoin's major macro cycle tops in 2011, 2013, 2017, and early 2021 coincided with MCTR crossing into the 32x–64x multiple band.
- Bear market cycle lows in 2011, 2015, 2018–2019, and late 2022 consistently bottomed in the 2x–6x Thermocap multiple band, aligning with the Investor Capitalization floor ($\text{Realized Cap} - \text{Thermocap}$).
- The metric demonstrates strong long-term cyclical co-movement with Bitcoin price on a non-logarithmic linear scale, providing an anchor for fundamental valuation.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Denominator Monotonicity & Downward Multiple Drift:** Because Thermocap is a cumulative sum of all historical revenues, it increases monotonically over time. As Bitcoin's annual supply inflation rate halves every 4 years, newly added daily miner revenue becomes a smaller percentage of existing Thermocap. This causes static multiple bands (e.g. 32x, 64x) to experience structural drift over successive halving cycles.
- **Low Sample Size / Small-N Hazard:** Bitcoin has completed only 4 major halving/halving-adjacent macro cycles since 2009. Statistical inference on 4 cycle peaks is prone to overfitting and small-sample bias.
- **Fee Dominance Transition:** If transaction fees grow to dominate miner revenue in future epochs, Thermocap dynamics may alter substantially compared to the historical block-subsidy era.

## Falsification plan

1. **Rolling vs Static Multiple Ablation:**
   - Test static threshold rules ($MCTR < 6$, $MCTR > 32$) against expanding-window percentile rules (10th percentile, 90th percentile) and detrended Z-score transformations.
   - If static bands fail to trigger in post-2024 cycles due to denominator expansion drift, reject fixed threshold rules in favor of dynamic percentile models.
2. **Orthogonal Information Test:**
   - Benchmark MCTR against MVRV Z-Score, Realized Price, Cointime AVIV Ratio, and Puell Multiple.
   - Run logistic regression forecasting 12-month forward drawdowns. If MCTR has no incremental explanatory power over MVRV, reject MCTR as a redundant collinear indicator.
3. **Out-of-Sample Cycle Testing:**
   - Calibrate thresholds strictly on data prior to 2020; test out-of-sample performance over the 2020–2026 cycle.
4. **Execution & Cash Drag Net Return:**
   - Evaluate whether an MCTR-filtered holding strategy outperforms simple Buy-and-Hold BTC on a risk-adjusted basis (Sharpe, Sortino, Calmar) net of inflation and cash yield drag during de-risked periods.

## Crypto portability

**direct** for Bitcoin.

For other digital assets:
- **Proof-of-Work Assets (e.g. LTC, DOGE, BCH):** Directly applicable, provided full genesis block reward and fee data are accessible.
- **Proof-of-Stake Assets (e.g. ETH post-Merge, SOL):** **adapted / unproven**. PoS security expenditure consists of validator issuance and staking yield rather than physical thermodynamic hardware/electricity expenditures; cumulative issuance metrics must be reformulated for staking economics.

## Limitations

- **not independently reproduced**.
- **small sample size:** Historical evidence rests on only 4 completed Bitcoin market cycles.
- **structural multiple drift:** Diminishing block subsidy inflation causes the multiple to behave non-stationarily over decades without detrending.
- **macro-horizon latency:** Ineffective for short-term or intraday trading; useful only as a multi-month/multi-year macro allocation overlay.

## Implementation status

No implementation or validation in PyBroker, NautilusTrader, strategy registry, Paper, Testnet, or Live has been performed in this Scout cycle.

`implementation_status: not-implemented`

## Adoption boundary

This record is Alpha Strategy Pool research material only. Presence in this repository does not imply profitability, validated alpha, implementation approval, paper-trading approval, testnet approval, or live-trading approval.

`status: research-only`
`adoption: not-approved`
`approval_scope: research-only`

## Related Wiki records

No stable Hermes Wiki Brain link was verified in this Scout cycle. Do not fabricate one.

Related strategy families in this repository include:
- `bitcoin-onchain-mvrv-zscore-cycle-reversal-2026-08-31.md` (MVRV Z-Score)
- `bitcoin-onchain-cointime-aviv-ratio-true-market-mean-2026-09-01.md` (Cointime AVIV Ratio)
- `bitcoin-onchain-puell-multiple-miner-capitulation-2026-08-31.md` (Puell Multiple)

## Sources

1. Nic Carter and Antoine Le Calvez, *A new cryptoasset fundamental: introducing Thermocap*, Coin Metrics Research (October 2018): https://medium.com/@nic__carter/a-new-cryptoasset-fundamental-introducing-thermocap-562725359489
2. Glassnode Academy, *Thermocap Metric Specification*: https://academy.glassnode.com/market/thermocap
3. Glassnode Academy, *Market Cap to Thermocap Ratio*: https://academy.glassnode.com/market/market-cap-to-thermocap-ratio
4. Coin Metrics Community Network Data & Research Documentation: https://coinmetrics.io/community-network-data/
