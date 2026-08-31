---
schema: strategy-research-record-v1
title: Bitcoin On-Chain Balanced Price and Terminal Price Valuation Bands
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
  - "https://academy.glassnode.com/market/pricing-models/balanced-price"
  - "https://academy.glassnode.com/market/pricing-models/terminal-price"
  - "https://www.lookintobitcoin.com/charts/terminal-price/"
  - "https://woocharts.com/bitcoin-balanced-price/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin On-Chain Balanced Price and Terminal Price Valuation Bands

## Provenance

- **Primary Industry Origin:** David Puell (April 2019), "The Bitcoin Valuation Suite: Transferred Price, Balanced Price, and Terminal Price".
- **Institutional Documentation & Analysis:** Glassnode Insights & Academy (2020–2024), authored by Checkmate (`@_checkmatey_`) and the Glassnode Research Team. References: [Glassnode Balanced Price Documentation](https://academy.glassnode.com/market/pricing-models/balanced-price) and [Glassnode Terminal Price Documentation](https://academy.glassnode.com/market/pricing-models/terminal-price).
- **Secondary Analytics Platform:** LookIntoBitcoin Chart Suite. Reference: [LookIntoBitcoin Terminal Price Chart](https://www.lookintobitcoin.com/charts/terminal-price/).

The pricing models synthesize aggregate realized acquisition value (**Realized Price**) and cumulative spending throughput (**Transferred Price**) to define macro cycle valuation boundaries for Bitcoin.

## Economic mechanism

### Source-reported

David Puell and Glassnode propose that Bitcoin's market valuation can be decomposed into structural economic states through three interconnected on-chain metrics:
1. **Transferred Price ($P_{\text{trans}})$:** Measures the lifetime cumulative spending velocity of Bitcoin. It takes cumulative Coin Days Destroyed (CDD), converts them into a per-coin velocity metric, and divides by the circulating supply and network lifespan (in years). It represents the historical average price at which coins have been transferred/spent.
2. **Balanced Price ($P_{\text{bal}})$:** Calculated as the difference between Realized Price and Transferred Price ($\text{Realized Price} - \text{Transferred Price}$). Realized Price represents the average acquisition cost basis of all existing coins, whereas Transferred Price represents the lifetime spending throughput. The difference represents the unspent, "fair value" economic equity retained in the network. Historically, market prices have dropped to or briefly touched Balanced Price during severe bear market capitulation bottoms (2015, 2018, and late 2022).
3. **Terminal Price ($P_{\text{term}})$:** Calculated by extrapolating the Transferred Price across the ultimate 21 million Bitcoin supply cap ($P_{\text{term}} = P_{\text{trans}} \times 21$). It acts as a dynamic "upper bound" ceiling representing the theoretical exhaustion price if historical spending velocity were fully monetized.

### Research interpretation

The hypothesis frames Bitcoin market cycles as an oscillation between **capitulation fair value** and **terminal velocity exhaustion**:

1. **Capital Realization vs Spending Throughput:** Realized Cap ($RC_t = \sum \text{UTXO}_i \times P_{\text{acquired}, i}$) measures aggregate investor cost basis. Transferred Cap measures cumulative destruction of holding duration. When market cap falls below Realized Cap ($P_t < \text{Realized Price}$), the aggregate market is underwater. When $P_t$ drops to Balanced Price ($P_t \le P_{\text{bal}}$), speculative markup has been stripped down to pure historical unspent energy.
2. **Asymmetric Cycle Boundaries:**
   - **Capitulation Floor Regime ($P_t \le P_{\text{bal}}$):** Maximum structural accumulation zone where long-term seller exhaustion is statistically near 100%.
   - **Mid-Cycle Transition ($P_{\text{bal}} < P_t < P_{\text{term}}$):** Organic momentum and trend-following regimes.
   - **Terminal Exhaustion Regime ($P_t \ge 0.85 \times P_{\text{term}}$):** Market cap approaches the theoretical monetization limit of lifetime coin velocity, marking high-probability cycle peaks.

## Signal

1. **Transferred Price Computation ($P_{\text{trans}, t}$):**
   Let $\text{CDD}_t$ be daily Coin Days Destroyed, $S_t$ be the total circulating supply, and $\text{Age}_{\text{years}, t} = \frac{\text{DayCount}_t}{365.25}$ be the age of Bitcoin in years:
   $$\text{Transferred Price}_t = \frac{\sum_{\tau=1}^{t} \text{CDD}_\tau}{S_t \times \text{Age}_{\text{years}, t} \times 365.25} = \frac{\sum_{\tau=1}^{t} \text{CDD}_\tau}{S_t \times \text{DayCount}_t}$$

2. **Balanced Price Computation ($P_{\text{bal}, t}$):**
   Let $\text{Realized Price}_t = \frac{\text{Realized Cap}_t}{S_t}$:
   $$P_{\text{bal}, t} = \text{Realized Price}_t - P_{\text{trans}, t}$$

3. **Terminal Price Computation ($P_{\text{term}, t}$):**
   Let $S_{\text{max}} = 21{,}000{,}000$ (in millions, scalar $21$ relative to supply baseline):
   $$P_{\text{term}, t} = P_{\text{trans}, t} \times \frac{21 \times 10^6}{S_t} \approx P_{\text{trans}, t} \times 21$$

4. **Regime and Valuation Multiples:**
   - **Balanced Price Ratio:** $M_{\text{bal}, t} = \frac{P_t}{P_{\text{bal}, t}}$
   - **Terminal Price Ratio:** $M_{\text{term}, t} = \frac{P_t}{P_{\text{term}, t}}$

5. **Trading & Dynamic Allocation Strategy:**
   - **Capitulation Long Entry:** If $M_{\text{bal}, t} \le 1.05$ (spot price within 5% of Balanced Price), initiate aggressive macro spot/perp long exposure.
   - **Bull Market Expansion:** If $P_{\text{bal}, t} < P_t < 0.80 \times P_{\text{term}, t}$, maintain systematic trend-following allocations.
   - **Terminal Overheating / Exit:** If $M_{\text{term}, t} \ge 0.90$ (spot price reaches or exceeds 90% of Terminal Price), scale down directional longs by 75% and initiate delta-hedging / short perpetual basis positions.

6. **Specification Status:**
   - **Fully specified:** Mathematical equations for Transferred Price, Balanced Price, and Terminal Price, alongside valuation ratios.
   - **Underspecified:** Intraday UTXO indexing latency and adjustment heuristics for lost/burned coins (e.g., Satoshi's untouched 1.1M coins).

## Required data

- **Full UTXO Ledger:** Point-in-time spent output data for exact CDD calculation from Genesis Block.
- **Realized Cap Series:** Daily aggregate Realized Capitalization from major on-chain analytics nodes.
- **Circulating Supply:** Total mined Bitcoin supply $S_t$ at daily resolution.
- **Price Series:** Daily BTC/USD spot OHLCV (UTC 00:00 close) from consolidated major exchange feeds.

## Execution assumptions

- **Execution Timing:** Daily rebalancing at UTC 00:00 bar close once UTXO spending for day $t$ has achieved finality.
- **Order Execution:** Spot allocation or perpetual futures positioning with 3–5 bps execution fee assumption and 1–2 bps slippage.
- **Holding Period:** Multi-month to multi-year holding duration per macro cycle phase.

## Evidence

### Source-reported

- Glassnode Research and David Puell report that:
  - **Balanced Price** marked the exact bottom ranges of the 2015 bear market (~$165–$180), the 2018 capitulation floor (~$3,200), and the 2022 FTX liquidity flush (~$15,700–$16,500).
  - **Terminal Price** framed the major multi-year cycle tops in 2013 ($1,150), December 2017 ($19,700), and April 2021 ($64,800), where spot prices expanded directly into the Terminal Price boundary before experiencing structural trend reversals.
- Source claims are based on historical retrospective modeling and have not been independently reproduced in an out-of-sample backtest.

### Independently reproduced

Not independently reproduced in our research backtesting stack.

### Negative evidence

- **Supply Cap Saturation Effect:** As circulating supply approaches 21 million ($S_t \to 21\text{M}$), the $\frac{21\text{M}}{S_t}$ scaling factor approaches 1.0, progressively compressing the distance between Terminal Price and Transferred Price unless daily CDD growth accelerates substantially.
- **Macro Cycle Top Deviation (November 2021):** The November 2021 peak ($69,000) fell short of reaching Terminal Price (which sat around $105,000 at the time), demonstrating that cycle tops do not deterministically reach Terminal Price in every cycle.
- **Low Signal Turnover:** Like all macro on-chain valuation bands, signals occur on multi-year intervals, giving very low statistical power ($N \approx 4$ tops and bottoms).

## Falsification plan

1. **Capitulation Floor Breakdown Test:** If BTC trades and closes below Balanced Price by $> 20\%$ for longer than 30 consecutive days, the hypothesis that Balanced Price represents a hard structural floor is falsified.
2. **Terminal Top Upper-Bound Violation Test:** If BTC sustains a price $> 25\%$ above Terminal Price for more than 14 consecutive daily closes without immediately retracing, the theoretical ceiling formulation is falsified.
3. **Lost Coin Sensitivity Analysis:** Test whether removing estimated lost coins (3–4 million permanently dormant BTC) alters Transferred Price denominator dynamics and improves cycle top/bottom fidelity.

## Crypto portability

- **Applicability:** `direct` for Bitcoin (UTXO chain with 21 million hard supply cap).
- **Other Cryptocurrencies:** `unproven` / `not applicable`. Account-based assets (ETH, SOL) lack native UTXO coin-days and have dynamic or inflationary/deflationary supply schedules without a fixed 21M scalar, requiring fundamentally different structural parameters.

## Limitations

- **Fixed Scalar Assumption ($21\text{M}$):** The multiplier 21 is hardcoded to Bitcoin's maximum supply and cannot be generalized across other digital assets.
- **Low Trade Frequency:** Designed for macro portfolio rebalancing rather than tactical short-term trading.
- **Data Dependency:** High computational reliance on full-node UTXO trace parsers.

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

- `bitcoin-onchain-cumulative-value-days-destroyed-cvdd-floor-2026-09-01.md`
- `bitcoin-onchain-mvrv-zscore-cycle-reversal-2026-08-31.md`
- `bitcoin-onchain-net-unrealized-profit-loss-nupl-macro-cycle-2026-09-01.md`
- `bitcoin-onchain-puell-multiple-miner-capitulation-2026-09-01.md`

## Sources

- David Puell (2019), "The Bitcoin Valuation Suite: Transferred Price, Balanced Price, and Terminal Price".
- Glassnode Academy (2020), "Balanced Price": https://academy.glassnode.com/market/pricing-models/balanced-price
- Glassnode Academy (2020), "Terminal Price": https://academy.glassnode.com/market/pricing-models/terminal-price
- LookIntoBitcoin (2024), "Bitcoin Terminal Price Indicator": https://www.lookintobitcoin.com/charts/terminal-price/
- WooCharts (2021), "Balanced Price Model Documentation": https://woocharts.com/bitcoin-balanced-price/
