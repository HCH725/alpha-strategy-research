---
schema: strategy-research-record-v1
title: "DeFi Lending Aggregate System Risk Early Warning: Synthetic Borrower-Lender Fragility as a Stablecoin and Liquidation Stress Signal"
created: 2026-09-09
updated: 2026-09-09
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - defi
  - lending
  - systemic-risk
  - early-warning
  - stablecoin
  - liquidation
  - aggregate-risk-measure
status: research-only
confidence: medium
source_as_of: 2026-09-07
sources:
  - https://arxiv.org/abs/2609.07902v1
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# DeFi Lending Aggregate System Risk Early Warning

## Provenance

- **Source:** Jeremy Bertomeu, Xiumin Martin, Ibrahima Sall. "Measuring DeFi Risk." arXiv preprint `arXiv:2609.07902v1 [q-fin.GN]`, submitted 2026-09-07.
- **Authors:** Jeremy Bertomeu (Associate Professor), Xiumin Martin (Professor), Ibrahima Sall (PhD candidate) — Olin School of Business, Washington University in St Louis, 1 Snow Way Dr, St. Louis, MO 63130.
- **Paper type:** 15 pages, 3 figures, 1 table. Preprint (not peer-reviewed at time of recording).
- **Sample period:** April 1, 2021 to May 18, 2022 (27,804 daily token-level observations).
- **Protocols studied:** Aave and Compound.
- **Primary source verified:** Full PDF read; all performance figures and model specifications traced to Table 1 and Figures 2–3 in the paper.

## Economic mechanism

### Source-reported

DeFi lending pools match yield-seeking depositors (lending stablecoins) with speculative borrowers (depositing volatile crypto collateral and borrowing stablecoins). Depositors receive tokens (e.g., cUSDC, aUSDC) backed by a basket of collateral rather than audited dollar reserves — sharing structural similarities with algorithmic stablecoins. The authors develop two aggregate risk measures using only public deposit and borrowing data:

1. **RI** (liquidation risk threshold): The maximum proportional decline in all unpegged coin prices that would cause the synthetic borrower's health factor to fall below one, triggering mass liquidation. RI = Σ(B_j for j≤0) / Σ((D_j - B_j) × τ_j for j>0), where B_j = total borrowings in coin j, D_j = total deposits, τ_j = liquidation threshold.

2. **RII** (solvency/collateral loss threshold): The maximum proportional decline that would cause the synthetic borrower to be unable to fully repay loans even after liquidation, resulting in lender losses. RII = Σ(B_j × (1+π_j) for j≤0) / Σ((D_j - B_j) for j>0), where π_j = liquidation premium.

Key finding: When RI > 1, the system is critically fragile — even at current price levels, borrower health factors can fall below 1. A RII of 0.65 implies that a 35% additional decline in coin prices would cause collateral losses to depositors.

### Research interpretation

The RI and RII measures function as a systemic stress gauge for DeFi lending. The hypothesized alpha mechanism is:

1. **Early warning signal:** Elevated RI/RII across major protocols (Aave, Compound, and potentially others) predicts heightened probability of liquidation cascades, stablecoin de-peg risk, and DeFi contagion events.
2. **Regime detection:** Sharp increases in RI/RII indicate the system is moving from a healthy state toward fragility, potentially preceding forced selling pressure in volatile collateral (ETH, BTC) as liquidations cascade.
3. **Cross-venue spillover:** Aggregate fragility in one protocol (e.g., Aave) can propagate to others through shared collateral assets and correlated liquidation triggers.

The alpha hypothesis: monitoring RI/RII as a composite stress indicator allows pre-positioning — reducing DeFi lending exposure, hedging collateral assets, or taking contrarian positions when stress dissipates.

## Signal

- **Formation timestamp:** Daily, computed from on-chain aggregate deposit and borrowing data (D_j, B_j) per coin per protocol. Data available via public blockchain queries (e.g., Dune Analytics queries 462944, 462941, 463938, 462905).
- **Lookback window:** Point-in-time daily computation; no lookback required for RI/RII themselves. For signal generation (detecting regime changes), a rolling window of 7–30 days is research-proposed.
- **Long entry / risk-on:** When RI < 0.7 and RII < 0.5 (research-proposed thresholds), the system has sufficient collateral buffer; DeFi lending positions and collateral-linked assets are relatively safe. Increase DeFi yield exposure.
- **Short entry / risk-off:** When RI > 0.85 or RII > 0.6 (research-proposed thresholds), system fragility is elevated. Reduce DeFi lending deposits, avoid borrowing volatile collateral, hedge ETH/BTC exposure for potential liquidation-driven selling.
- **Critical threshold:** When RI > 1, the system is at or beyond the liquidation threshold at current prices — extreme fragility. Research-proposed action: exit DeFi lending positions entirely, consider hedging via short perpetuals on volatile collateral.
- **Exit:** When RI and RII decline back below research-proposed thresholds, or after a specified holding period (research-proposed: 14 days max for stress positions).
- **Parameters:** The thresholds 0.7/0.85/1.0 for RI and 0.5/0.6 for RII are research-proposed and require empirical calibration. The paper provides the framework but does not specify trading thresholds.
- **Position sizing:** Not specified in source. Research-proposed: scale position inversely with RI (higher RI = smaller DeFi exposure).
- **Multi-protocol aggregation:** RI/RII should be computed per-protocol and also as a weighted aggregate across protocols, weighted by TVL (research-proposed).
- **Fully specified:** Partially. The RI/RII formulas are fully specified. The trading signal construction (thresholds, timing, sizing) is research-proposed.

## Required data

- **Instrument / universe:** Major DeFi lending protocols with publicly available aggregate deposit/borrowing data per coin (e.g., Aave v2/v3, Compound v2/v3).
- **Venue:** Ethereum mainnet (Aave, Compound), potentially extending to L2 protocols (Arbitrum, Polygon deployments).
- **Market type:** DeFi lending pools; collateral assets include ETH, BTC, and other volatile cryptocurrencies; borrowed assets are stablecoins (USDC, USDT, DAI).
- **Timeframe:** Daily computation. Intraday computation possible if on-chain data is available with sufficient granularity.
- **Fields required:** Per-coin aggregate deposits (D_j) and borrowings (B_j), liquidation thresholds (τ_j), liquidation premiums (π_j), coin classifications (stablecoin vs. volatile).
- **Data source:** On-chain data via Dune Analytics queries (queries 462944, 462941, 463938, 462905 referenced in paper), or direct blockchain node queries.
- **Point-in-time:** On-chain data is inherently point-in-time (no revision). No look-ahead bias risk for on-chain data.
- **Missing-data assumption:** The paper excludes coins backed entirely by other volatile crypto (e.g., DAI, TerraUST) from the stablecoin category, consistent with proposed U.S. legislation S.3970. This classification choice affects RI/RII computation.

## Execution assumptions

- **Signal-to-order timing:** Daily signal, end-of-day or next-day execution (research-proposed).
- **Order type:** Not specified in source. Research-proposed: market orders for DeFi position adjustments (deposit/withdraw from lending pools); limit orders or perpetual short for hedging.
- **Fill model:** Not specified. DeFi deposits/withdrawals are smart contract executions (no traditional fill model); perpetual shorts on centralized exchanges have standard fill assumptions.
- **Fees:** DeFi protocol fees (deposit/withdrawal fees, which vary by protocol) + CEX trading fees for hedging. Not modeled in source.
- **Slippage:** DeFi: gas costs + potential MEV (sandwich attacks on large deposits/withdrawals). CEX: standard slippage model. Not modeled in source.
- **Impact / capacity:** Aggregate RI/RII are protocol-level measures; individual position impact depends on pool size. Large withdrawals during stress periods may face queue delays or oracle manipulation risk.
- **Funding:** Not applicable for the risk measure itself. If hedging via perpetuals, funding rate costs apply.
- **Leverage / margin:** The source studies the existing leverage in the system; the strategy itself research-proposed uses no additional leverage for risk-off positions.
- **Latency:** On-chain data has block-level latency (~12 seconds on Ethereum). For daily signals, this is negligible.
- **Execution assumptions are underspecified:** The source does not provide an execution framework; all trading rules are research-proposed.

## Evidence

### Source-reported

- **Sample:** Aave and Compound, April 1, 2021 to May 18, 2022.
- **Table 1 (OLS regressions):** RI coefficient on NCI (Nasdaq crypto index, in thousands) = -0.119*** to -0.152*** (with controls). RII coefficient = -0.056*** to -0.094***. A 1,000-point increase in NCI reduces RI by 0.12–0.15 and RII by 0.06–0.09. R-squared ranges 0.04–0.18.
- **Peak fragility (Figure 2):** RI exceeded 1 in June/July 2021, indicating the system was at critical fragility. RII at peak implied ~35% additional decline would cause collateral loss to depositors.
- **Liquidation validation (Figure 3):** Dollar liquidations scaled by lagged borrowings are increasing in RI and RII quintiles, confirming the measures capture real system stress.
- **Sample-specific:** These results are for Aave and Compound during 2021–2022 only. The source does not report out-of-sample performance or forward-looking predictive power for specific stress events.
- **No Sharpe/CAGR/return figures:** This is a risk measurement framework, not a backtested trading strategy. No profitability claims are made.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The paper does not test whether RI/RII signals would have been profitable as a trading strategy (no position-level backtest).
- The sample ends May 2022, just before the major Terra/UST collapse (May 2022) and subsequent contagion (Three Arrows Capital, Celsius, etc.). The paper does not assess whether RI/RII would have provided timely warning for these events.
- The NCI regression R-squared is relatively low (0.04–0.18), suggesting RI/RII variation is only partially explained by broad crypto market movements.
- The paper notes that Maker (another major DeFi protocol) is excluded because it operates with a different model (borrowers mint DAI rather than borrowing stablecoins), limiting protocol coverage.
- None identified in the reviewed sources beyond the above; absence is not evidence of no negative result.

## Falsification plan

- **Required sample:** Extend RI/RII computation to at least 2022–2026, covering multiple market cycles (May 2022 crash, 2023 recovery, 2024–2025 bull).
- **Forward-looking stress test:** Verify whether RI > 1 preceded the May 2022 Terra/UST contagion, FTX collapse (November 2022), or March 2023 SVB/USDC de-peg. If RI/RII did not rise before these events, the early-warning signal is materially weakened.
- **Baseline / control:** Compare signal timing against simpler indicators (e.g., ETH price drawdown, VIX, stablecoin market cap changes) to assess incremental predictive power.
- **Protocol expansion:** Compute RI/RII for additional protocols (Spark, Morpho, Venus, Euler) to test portability.
- **Cost sensitivity (research-defined):** If DeFi deposit/withdrawal fees + gas costs + MEV exceed the benefit of early exit during stress, the strategy has no net alpha.
- **Parameter perturbation (research-defined):** Test RI thresholds from 0.5 to 1.2 and RII thresholds from 0.3 to 0.8. If performance is highly sensitive to exact thresholds, the signal is not robust.
- **Failure metric (research-defined):** If RI/RII fail to rise at least 3 days before a major DeFi stress event (>10% drawdown in collateral assets or >5% stablecoin de-peg), the early-warning function is falsified.
- **Action on failure:** If falsified, relegate to risk-monitoring-only tool (not a trading signal).

## Crypto portability

**Adapted.**

The mechanism is inherently crypto-native (DeFi lending on Ethereum/EVM chains). However:

- **Direct portability to EVM DeFi:** Yes, for Aave, Compound, Spark, Morpho, and similar lending protocols on Ethereum and EVM-compatible chains.
- **Non-EVM chains:** Requires adapted data pipelines. Solana lending (Solend, MarginFi), Cosmos-based protocols, and others have different on-chain data structures.
- **CEX lending:** Not directly applicable; CEX lending (e.g., Binance Earn, Bybit) does not have transparent on-chain aggregate data.
- **Stablecoin classification:** The paper's stablecoin definition (fiat-backed only, excluding algorithmic stablecoins) is a material choice. Including DAI or other crypto-backed stablecoins would change RI/RII.
- **Multi-chain fragmentation:** As DeFi TVL fragments across L2s and alt-L1s, aggregate RI/RII must be computed across chains, which introduces data aggregation complexity.
- **Liquidity:** DeFi lending pool liquidity varies significantly; large position adjustments during stress may face execution challenges not captured by aggregate measures.

## Limitations

- **Sample period is narrow:** April 2021 to May 2022 only. Does not cover the 2022 contagion cascade or post-2022 market structure changes.
- **Two protocols only:** Aave and Compound. Does not include newer protocols (Spark, Morpho, Euler) or L2 deployments.
- **No trading backtest:** The source provides a risk measurement framework, not a trading strategy. All trading rules and thresholds are research-proposed.
- **Forward-looking predictive power untested:** Whether RI/RII reliably predict future stress events (rather than contemporaneously measuring current stress) is not established.
- **Aggregate data limitation:** RI/RII use aggregate data and do not capture distribution of individual positions. A few very large positions could dominate system risk without appearing in aggregate measures.
- **Static liquidation parameters:** The framework uses fixed τ_j and π_j, but protocols can change these parameters in response to governance votes or stress events.
- **Governance token dependency:** The paper notes that DeFi protocols' safety mechanisms (e.g., Compound governance coin) mirror those that failed in Terra/UST. This is flagged as a potential systemic risk not captured by RI/RII.
- **Data gap:** The paper does not specify how to handle protocol parameter changes (e.g., when Aave updates liquidation thresholds) in the time series.
- **Not independently reproduced** by our research system.

## Implementation status

Not implemented. No PyBroker, Nautilus, paper, testnet, or live implementation exists in our research stack.

## Adoption boundary

This record is research-only. Presence in this repository does not mean:
- The RI/RII measures are profitable as trading signals.
- The early-warning function has been validated out-of-sample.
- The framework has been tested against our canonical validation pipeline.
- Any DeFi lending, hedging, or risk-off action is authorized.

All thresholds and trading rules in this record are research-proposed unless explicitly attributed to the source.

## Related Wiki records

- `[[quant/defi-lending-operational-tail-risk-premium-mispricing-2026-09-02]]` — Different mechanism: EVT-based individual protocol tail risk vs. this record's aggregate system fragility measure.
- `[[quant/defi-lending-collateral-liquidation-discount-arbitrage-2026-09-01]]` — Different mechanism: individual liquidation bot arbitrage vs. this record's systemic stress indicator.
- `[[quant/defi-lending-capital-allocation-rate-impact-kink-asymmetry-2026-09-02]]` — Different mechanism: protocol-level rate optimization vs. this record's aggregate risk decomposition.

## Sources

1. Jeremy Bertomeu, Xiumin Martin, Ibrahima Sall. "Measuring DeFi Risk." arXiv preprint `arXiv:2609.07902v1 [q-fin.GN]`, submitted 2026-09-07. https://arxiv.org/abs/2609.07902v1
2. Dune Analytics queries referenced in paper: 462944, 462941, 463938, 462905 (aggregate deposit/borrowing data for Aave and Compound).
3. Dune Analytics query 463010 (liquidation data).
