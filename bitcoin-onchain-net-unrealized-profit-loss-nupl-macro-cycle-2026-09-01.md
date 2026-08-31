---
schema: strategy-research-record-v1
title: Bitcoin On-Chain Net Unrealized Profit/Loss (NUPL) Macro Cycle and Sentiment Oscillator
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
  - valuation
  - sentiment
  - macro-cycle
status: research-only
confidence: high
source_as_of: 2024-05
sources:
  - https://medium.com/glassnode-insights/dissecting-bitcoins-unrealised-on-chain-profit-loss-73e735020c8d
  - https://studio.glassnode.com/metrics?a=BTC&metric=net_unrealized_profit_loss
  - https://adamantresearch.com/
  - https://doi.org/10.3390/electronics13050965
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin On-Chain Net Unrealized Profit/Loss (NUPL) Macro Cycle and Sentiment Oscillator

## Provenance

- **Original Conceptual Formulation:** Tuur Demeester, Tamás Blummer, and Michiel Lescrauwaet, “Bitcoin Market Sentiment: A Primer,” Adamant Capital / Adamant Research, 2019.
- **Quantitative Normalization and Publication:** Rafael Schultze-Kraft, “Dissecting Bitcoin's Unrealised On-Chain Profit/Loss,” Glassnode Insights, November 2019; Glassnode Studio implementation `net_unrealized_profit_loss`.
- **Academic Empirical Studies:** 
  - MDPI *Electronics* (2024), “A Descriptive-Predictive–Prescriptive Framework for the Social-Media–Cryptocurrencies Relationship,” doi:10.3390/electronics13050965 (evaluating NUPL on-chain correlation $r = 0.899$ with Bitcoin market cycles).
  - Academic literature on Bitcoin fundamental on-chain factors and market efficiency benchmarks (e.g., *International Review of Financial Analysis*).

## Economic mechanism

### Source-reported

In Bitcoin's unspent transaction output (UTXO) accounting model, the timestamp and price at which each coin was last transferred represent its realized cost basis. By comparing the current spot price of Bitcoin to the historical acquisition price of each UTXO:
1. **Unrealized Profit:** Coins with current price greater than their last moved price hold unrealized paper gains.
2. **Unrealized Loss:** Coins with current price less than their last moved price hold unrealized paper losses.

**Net Unrealized Profit/Loss (NUPL)** calculates the total aggregate net paper gain or loss across the entire circulating supply, normalized by the current total market capitalization:
$$\text{NUPL} = \frac{\text{Market Cap} - \text{Realized Cap}}{\text{Market Cap}} = 1 - \frac{\text{Realized Cap}}{\text{Market Cap}} = 1 - \frac{1}{\text{MVRV}}$$

The source authors hypothesize that aggregate unrealized profit/loss drives market-wide participant psychology through five distinct psychological regime phases:
- **Capitulation ($\text{NUPL} < 0$):** Aggregate network is in net loss; investors capitulate, selling at deep losses to long-term value accumulators, historically marking secular multi-year cycle bottoms.
- **Hope / Fear ($0 \le \text{NUPL} < 0.25$):** Early recovery phase where price recovers above aggregate realized cost basis.
- **Optimism / Anxiety ($0.25 \le \text{NUPL} < 0.50$):** Mid-cycle trend expansion with moderate unrealized gains.
- **Belief / Denial ($0.50 \le \text{NUPL} < 0.75$):** Strong bull market conviction where the majority of circulating supply sits in substantial unrealized profit.
- **Euphoria / Greed ($\text{NUPL} \ge 0.75$):** Extreme market-wide paper profits exceeding 75% of total market cap; extreme incentive for early holders and institutional miners to distribute into retail liquidity, historically preceding secular bull market cycle peaks.

### Research interpretation

NUPL functions as an **aggregate cost-basis mean-reversion and disposition-effect macro oscillator**:
1. **Capital Distribution Friction:** When NUPL exceeds $0.75$, the overwhelming proportion of circulating Bitcoin is held at multi-fold gains. Behavioral disposition effect and profit-taking incentives create mounting supply overhang that exhausts marginal buy-side spot liquidity.
2. **Capitulation Floor:** When NUPL dips below $0.00$, the average market participant is submerged below cost basis. Transaction volume dries up, marginal selling pressure attenuates as weak hands liquidate, and high-conviction long-term holders absorb remaining float, establishing an asymmetric risk-reward entry zone.
3. **Difference from MVRV:** While algebraically related ($NUPL = 1 - \text{MVRV}^{-1}$), NUPL maps network profitability onto a bounded interval $(-\infty, 1.0]$ with an intuitive percentage interpretation (e.g., $\text{NUPL} = 0.50$ means exactly 50% of the total network market cap consists of paper profits), enabling standardized regime-switching thresholds.

## Signal

The quantitative macro strategy is structured as a daily-sampled multi-regime asset allocation and rebalancing model:

1. **Daily On-Chain State Construction:**
   At daily snapshot timestamp $t$ (standardized at 00:00 UTC):
   $$\text{MarketCap}_t = P_t \times S_t$$
   $$\text{RealizedCap}_t = \sum_{u \in \text{UTXO}} P_{\text{creation}}(u) \times v(u)$$
   $$\text{NUPL}_t = \frac{\text{MarketCap}_t - \text{RealizedCap}_t}{\text{MarketCap}_t}$$
   where $P_t$ is the daily closing spot price, $S_t$ is the circulating supply, $P_{\text{creation}}(u)$ is the price when UTXO $u$ was spent/created, and $v(u)$ is the satoshi volume of UTXO $u$.

2. **Core Allocation Rules:**
   - **Regime 1: Secular Accumulation (Long Entry / Maximum Exposure):**
     - Condition: $\text{NUPL}_t < 0.00$ (Capitulation zone) OR crossing back above $0.00$ from below.
     - Action: Set target exposure to 100% Long (or allocate maximum target portfolio weight to BTC).
   - **Regime 2: Expansion Holding:**
     - Condition: $0.00 \le \text{NUPL}_t < 0.70$.
     - Action: Maintain 100% Long directional exposure.
   - **Regime 3: Secular Distribution (De-risking / Short / Hedge Entry):**
     - Condition: $\text{NUPL}_t \ge 0.75$ (Euphoria zone) OR crossing below $0.70$ after having reached $\ge 0.75$.
     - Action: Reduce exposure to 0% (exit to cash/stablecoins) or establish a delta-hedged / short position.
   - **Execution Frequency:** Evaluated on daily close; rebalanced once daily at 00:05 UTC.

3. **Hybrid Variant: LTH-NUPL vs. STH-NUPL Cohort Divergence:**
   - Long-Term Holder NUPL ($\text{LTH-NUPL}$, coins with UTXO lifespan $\ge 155$ days) vs. Short-Term Holder NUPL ($\text{STH-NUPL}$, coins $< 155$ days).
   - Early warning signal: When $\text{STH-NUPL} < 0$ while $\text{LTH-NUPL} > 0.50$ during a bull trend, it signals local mid-cycle pullbacks (re-accumulation buying opportunity).

## Required data

- **Underlying Instrument:** Bitcoin (BTC).
- **On-Chain Ledger Data:** Complete historical UTXO set and transaction history from the Bitcoin blockchain.
- **Price Reference:** Daily aggregated BTC/USD spot index (e.g., Coin Metrics / Glassnode / CryptoQuant composite feed).
- **Derived On-Chain Fields:** Daily Market Capitalization, Realized Capitalization, Relative Unrealized Profit, Relative Unrealized Loss, LTH-NUPL, STH-NUPL.
- **Point-in-Time Constraint:** On-chain block timestamps and realized cap data must be strictly lagged to 00:00 UTC cutoff without post-hoc ledger reorg lookahead.

## Execution assumptions

- **Execution Timing:** Daily rebalance at 00:05 UTC following daily candle and on-chain UTXO aggregation close.
- **Instrument:** BTC spot or BTC-USDT perpetual futures.
- **Friction Model:**
  - Spot trading fee: 5 bps to 10 bps.
  - Perpetual futures taker fee: 2 bps to 5 bps; funding rate carry incorporated when holding long/short perpetuals.
  - Slippage on BTC at daily bar opens: $< 2$ bps.
- **Turnover:** Exceptionally low frequency (averaging 2 to 4 major state transitions per 4-year halving cycle), rendering net returns relatively insensitive to high-frequency execution slippage.

## Evidence

### Source-reported

- **Historical Macro Bottom Timing:** Schultze-Kraft (2019) and Glassnode historical audits document that $\text{NUPL} < 0$ precisely identified every major multi-year secular bottom in Bitcoin history:
  - November 2011 – February 2012 ($\text{NUPL}$ reached $-0.40$).
  - January 2015 – October 2015 ($\text{NUPL}$ reached $-0.35$).
  - November 2018 – March 2019 ($\text{NUPL}$ reached $-0.48$).
  - March 2020 COVID crash ($\text{NUPL}$ briefly dipped to $-0.05$).
  - November 2022 – January 2023 FTX capitulation ($\text{NUPL}$ reached $-0.30$).
- **Historical Macro Top Timing:** $\text{NUPL} > 0.75$ coincided with macro distribution phases in June 2011, April 2013, November 2013, and December 2017 ($\text{NUPL} > 0.78$), and was approached in February–April 2021 ($\text{NUPL} \approx 0.74$).
- **Statistical Correlation:** Academic evaluation in MDPI *Electronics* (2024) reports a Pearson correlation of $r = 0.899$ between the NUPL series and Bitcoin price cyclicality.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Diminishing Peak Amplitude (Structural Maturation):** In the 2021–2022 cycle, NUPL peaked at $\approx 0.748$ in February/March 2021 and failed to cross $0.75$ during the November 2021 all-time high ($\approx 0.65$), indicating that institutional adoption and deeper liquid derivative markets may compress peak unrealized profit margins below historical $0.75$ thresholds.
- **Protracted Bear Market Drawdown:** $\text{NUPL}$ can remain below zero for several months (e.g., 9 months in 2015, 4 months in 2018–2019) during which prices may experience further drawdowns of $20\%$ to $40\%$ before final bottom formation, exposing unhedged spot buyers to severe intermediate drawdown.
- **Lost and Inactive Coins Distortion:** Early Satoshi-era coins that have never moved since 2009–2010 (estimated at $> 1.5\text{M}$ BTC) are recorded at zero or near-zero cost basis, introducing a permanent positive upward drift in unrealized profit that requires entity-adjusted filtering for long-term precision.

## Falsification plan

The NUPL macro hypothesis will be considered refuted or structurally broken if:
1. Bitcoin enters a multi-year secular bear market with $>60\%$ drawdown from ATH while $\text{NUPL}$ fails to drop below $0.10$, indicating a disconnect between UTXO cost basis and market dynamics.
2. An out-of-sample cycle experiences a secular top and $>70\%$ multi-year collapse following a peak NUPL below $0.50$.
3. An active NUPL regime-switching allocation strategy fails to outperform a naive buy-and-hold benchmark on a risk-adjusted basis (Sharpe and Calmar ratios) over two consecutive 4-year halving cycles.

## Crypto portability

- **Direct:** NUPL is natively derived from the UTXO architecture of Bitcoin.
- **Adapted (UTXO-based Altcoins):** Directly portable to other UTXO-based chains with public ledgers (e.g., Litecoin, Dogecoin, Bitcoin Cash).
- **Adapted / Unproven (Account-based Chains):** Account-based blockchains like Ethereum require balance-weighted virtual coin-age reconstruction (e.g., tracking entry prices per account/token transfer), which introduces accounting heuristics and higher data ambiguity.

## Limitations

- **Not independently reproduced.**
- **Low Sample Size of Secular Cycles:** Bitcoin has only completed four full 4-year halving cycles since 2009, limiting the sample of macro tops and bottoms ($N \le 5$).
- **Sensitivity to Inactive / Lost Supply:** Unadjusted NUPL overstates unrealized profit if millions of permanently lost early coins are treated as active holdings.
- **Execution Lag:** As a slow macro indicator, NUPL is unsuited for intraday, daily, or swing trading and must be treated as a multi-month to multi-year allocation tool.

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
- `bitcoin-onchain-sopr-spent-output-profit-ratio-2026-08-31.md` — Spent Output Profit Ratio (realized profit/loss flow).
- `bitcoin-onchain-rhodl-ratio-macro-cycle-2026-08-31.md` — Realized HODL ratio age band distribution.
- `bitcoin-onchain-entity-adjusted-dormancy-flow-macro-bottom-2026-09-01.md` — Entity-adjusted dormancy flow bottom timing.

## Sources

1. Tuur Demeester, Tamás Blummer, Michiel Lescrauwaet, “Bitcoin Market Sentiment: A Primer,” Adamant Capital / Adamant Research, 2019: https://adamantresearch.com/.
2. Rafael Schultze-Kraft, “Dissecting Bitcoin's Unrealised On-Chain Profit/Loss,” Glassnode Insights, November 2019: https://medium.com/glassnode-insights/dissecting-bitcoins-unrealised-on-chain-profit-loss-73e735020c8d.
3. Glassnode Studio Documentation and Historical Data Engine for Net Unrealized Profit/Loss: https://studio.glassnode.com/metrics?a=BTC&metric=net_unrealized_profit_loss.
4. MDPI *Electronics* (2024), “A Descriptive-Predictive–Prescriptive Framework for the Social-Media–Cryptocurrencies Relationship,” doi:10.3390/electronics13050965.
