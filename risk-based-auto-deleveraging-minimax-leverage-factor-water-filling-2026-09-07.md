---
schema: strategy-research-record-v1
title: "Risk-Based Auto-Deleveraging: Minimax Leverage Policy and Factor-Adjusted Water-Filling"
created: 2026-09-07
updated: 2026-09-07
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - autodeleveraging
  - adl
  - liquidation-cascade
  - loss-socialization
  - market-microstructure
  - risk-management
  - water-filling
status: research-only
confidence: medium
source_as_of: 2026-07-16
sources:
  - "Steven Campbell, Natascha Hey, Ciamac C. Moallemi, Marcel Nutz, 'Risk-Based Auto-Deleveraging', arXiv:2603.15963v2 [q-fin.RM], July 2026. https://arxiv.org/abs/2603.15963"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Risk-Based Auto-Deleveraging: Minimax Leverage Policy and Factor-Adjusted Water-Filling

## Provenance

- **Paper URL:** https://arxiv.org/abs/2603.15963
- **Full arXiv ID:** 2603.15963v2 [q-fin.RM]
- **Authors:** Steven Campbell†, Natascha Hey†, Ciamac C. Moallemi, Marcel Nutz (Columbia University; †equal contribution)
- **Published:** v1 March 15, 2026; v2 July 16, 2026
- **Primary Category:** Risk Management (q-fin.RM); also Mathematical Finance (q-fin.MF), Trading and Market Microstructure (q-fin.TR)
- **Support:** Briger Family Digital Finance Lab (CCM, NH), Columbia CDFT Research Grant (SC, MN), NSERC PDF-599675-2025 (SC), NSF DMS-2407074/DMS-2106056 (MN)

## Economic mechanism

### Source-reported

Auto-deleveraging (ADL) is the terminal loss-socialization mechanism on cryptocurrency perpetual futures exchanges when margin and insurance funds are exhausted following large price moves. Exchanges forcibly reduce positions of solvent participants to cover the shortfall. The paper formalizes ADL as a risk-minimization problem: given an equity shortfall across accounts, the exchange seeks a position-reduction policy that minimizes the risk of future loss.

**Single-asset, isolated-margin setting:** The unique optimal policy for all monotone risk measures (including CVaR) is the **minimax leverage policy** — positions are reduced in order of highest leverage first, with leverage progressively equalized via a water-filling (or "leverage-draining") rule. This policy is:
- Distribution-free (no distributional assumptions on returns)
- Wash-trade resistant
- Sybil resistant
- Path-independent

**Multi-asset, cross-margin setting:** Under expected loss, asset-level shadow prices separate the optimization across accounts. When prices are driven by a single risk factor, optimal deleveraging is water-filling on **factor-adjusted leverage** (not gross leverage), so better-hedged portfolios are deleveraged less. For general cases, a sample-average ADMM scheme provides scalable numerical solutions.

**Empirical application:** The framework is applied to the October 10, 2025 Hyperliquid ADL event. The risk-minimizing allocations achieve lower expected shortfall than the exchange's realized allocation. The realized policy tends to fully close out affected accounts with little regard to leverage, while the risk-based allocations reduce each account only partially and in order of leverage.

### Research interpretation

The mechanism reveals a structural feature of crypto perpetual futures microstructure: the current queue-based ADL policy (profit% × leverage ranking) used by most exchanges is a suboptimal heuristic. The minimax leverage policy is provably optimal and has superior security properties.

**Potential alpha implications (research-proposed):**

1. **Preemptive De-risking Before ADL:** Knowledge of the ADL mechanism structure allows traders with high-leverage profitable positions to anticipate forced closure. The minimax leverage policy reduces accounts starting from the highest leverage — traders near the top of the leverage distribution face the highest ADL priority. Monitoring exchange insurance fund drawdown rates, liquidation velocity, and leverage distribution estimates enables preemptive position reduction before ADL triggers.

2. **Post-ADL Cascade Reversal:** The paper confirms that the realized Hyperliquid ADL policy is suboptimal (overshoots relative to risk-optimal allocations). When the realized policy fully closes accounts rather than partially reducing leverage, it dumps excess non-informational order flow into the market, creating temporary price dislocations that a contrarian strategy can exploit.

3. **Factor-Adjusted Leverage Advantage:** In multi-asset cross-margin portfolios, hedged positions are deleveraged less under the optimal policy. Traders who maintain well-hedged cross-asset portfolios face lower ADL risk than naive gross-leverage ranking suggests. This creates a structural advantage for portfolio-aware risk management during liquidation cascades.

## Signal

### Signal A: Leverage-Distribution ADL Priority Estimation
- **Formation Timestamp:** Continuous monitoring of exchange-wide leverage distribution (estimated from liquidation feed telemetry and public position data where available).
- **Lookback:** Rolling 1-hour window for leverage distribution estimation; insurance fund drawdown rate over 15-minute window.
- **Trigger:** When insurance fund drawdown rate exceeds threshold AND estimated position is in top quartile of leverage distribution:
  - Reduce position or hedge via off-venue instruments.
- **Parameters:** Leverage distribution estimation method; insurance fund drawdown threshold (research-proposed; not specified by source).
- **Holding Period:** Until insurance fund stabilizes or leverage is reduced below critical threshold.

### Signal B: Post-ADL Forced-Closure Mean Reversion
- **Formation Timestamp:** Upon cessation of active ADL cascade (30+ seconds without new ADL events).
- **Lookback:** Cumulative ADL haircut volume during cascade window.
- **Entry:** Long (short) when cumulative long (short) ADL volume exceeds 99th percentile and L2 bid (ask) replenishment is observed.
- **Exit:** Mean reversion target at 50% recovery of ADL impulse or 5-minute time horizon.
- **Holding Period:** 1–15 minutes (short microstructure mean-reversion horizon).
- **Parameters:** Volume threshold, time horizon (research-proposed; not specified by source).

## Required data

- **Instrument:** Linear and inverse perpetual contracts (BTC, ETH, SOL, high-beta altcoins).
- **Universe:** Major perpetual futures venues with transparent ADL / liquidation feeds (Hyperliquid, Binance, Bybit, OKX).
- **Timeframe:** Sub-second trade/liquidation stream, 1-minute OHLCV, 1-second insurance fund balance updates.
- **Fields:**
  - Real-time trade prints with liquidation/ADL flag.
  - Exchange insurance fund balance time series.
  - Account-level leverage and margin ratio (where publicly available).
  - L2 bid/ask depth (top 20 levels).
  - Mark price vs. index price spread.
- **Point-in-time:** Real-time execution feeds; no look-ahead.

## Execution assumptions

- **Order Types:** Aggressive limit / IOC orders for defensive exits; passive maker limit orders for post-ADL reversal capture.
- **Fill Model:** Conservative 5–10 bps slippage during volatile cascade aftermath.
- **Fees:** Standard perpetual VIP maker (0.00%–0.02%) and taker (0.04%–0.05%) fees.
- **Latency:** Low-latency execution stack (< 100ms) required for queue sensing and reversal capture.
- **Theoretical framework only:** The paper does not model transaction costs, fill probability, or execution latency. These are data gaps.

## Evidence

### Source-reported

- The minimax leverage policy is proven optimal for all monotone risk measures in the single-asset isolated-margin setting (Theorem 2.4).
- For CVaR, the optimal policy is a leverage cutoff with water-filling above the cutoff (Theorem 2.9).
- In single-factor multi-asset setting, optimal deleveraging is water-filling on factor-adjusted leverage (Theorem 3.8).
- Applied to October 10, 2025 Hyperliquid ADL event: risk-minimizing allocations achieve lower expected shortfall than realized allocation (Section 4.3).
- The realized Hyperliquid policy fully closes out affected accounts, while risk-based allocations reduce partially and in order of leverage.

No quantitative backtest performance numbers (Sharpe, CAGR, MDD) are reported. The paper is a theoretical mechanism design contribution with empirical case study, not a strategy backtest.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The paper acknowledges that the minimax leverage policy assumes complete information about account leverage, which is not publicly available on most exchanges (data gap).
- The single-factor water-filling result may not hold when multiple independent risk factors drive prices simultaneously.
- Real-world ADL events are rare (1–3 major events per year), limiting the empirical sample size for validation.

## Falsification plan

1. **Historical ADL Event Replication:** On Hyperliquid and Binance historical liquidation datasets, compare risk-minimizing allocation vs. realized allocation in terms of total equity shortfall at multiple time horizons post-ADL. **Failure rule:** If risk-minimizing allocation does not achieve strictly lower expected shortfall in ≥ 70% of historical ADL waves, the optimality claim is empirically unsupported.
2. **Factor-Adjusted vs. Gross Leverage Ranking:** Compare predictive power of factor-adjusted leverage decile vs. gross leverage decile for predicting which accounts are ADL'd. **Failure factor-adjusted leverage does not outperform gross leverage in account-level ADL prediction, the factor structure result is empirically weak.
3. **Cross-Exchange Generalizability:** Evaluate whether the minimax leverage policy properties (Sybil resistance, path independence) hold under Binance's and OKX's distinct ADL implementations. **Failure rule:** If exchange-specific ADL rules violate path-independence, the canonical policy is not portable.

## Crypto portability

**direct**

The mechanism is native to cryptocurrency perpetual futures markets. ADL is a crypto-specific loss-socialization mechanism not found in traditional finance (though analogous to central clearinghouse default waterfalls). Key crypto-specific considerations:
- **Exchange fragmentation:** Different exchanges implement distinct ADL priority formulas, requiring venue-specific calibration.
- **Leverage distribution:** Crypto perpetual markets support 50x–100x leverage, creating extreme tail distributions that amplify ADL mechanics.
- **24/7 continuous trading:** ADL events can occur at any time, requiring always-on monitoring.

## Limitations

- **Information asymmetry:** The paper assumes complete knowledge of account-level leverage, which is not publicly available on most exchanges (data gap).
- **Rare events:** Major ADL cascades occur infrequently (1–3 times per year), limiting empirical validation.
- **Single-factor assumption:** The factor-adjusted leverage result assumes a single dominant risk factor, which may not hold in multi-factor regimes (underspecified).
- **No transaction cost modeling:** The paper does not account for execution costs, slippage, or fill probability during high-volatility cascade periods (data gap).
- **Theoretical framework:** The paper provides mechanism design and optimality proofs, not a backtested trading strategy. Alpha claims are research-proposed extrapolations from the theoretical framework.
- **Not independently reproduced.**

## Implementation status

No implementation in our research stack. The paper provides theoretical proofs, ADMM algorithms, and empirical case study analysis of Hyperliquid ADL event data; no live execution pipeline has been deployed.

## Adoption boundary

This record is research material only. Presence in this repository does not mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

## Related Wiki records

- [[quant/crypto-perpetual-autodeleveraging-trilemma-queue-haircut-2026-09-02]] — Complementary ADL record covering Chitra (2025) impossibility results, queue mechanics, and profit-haircut optimization; this record covers Campbell et al. (2026) constructive optimal policy, factor-adjusted multi-asset extension, and ADMM algorithm
- [[quant/hyperliquid-sunshine-trading-adverse-selection-liquidity-extraction-2026-09-01]] — Hyperliquid-specific market microstructure and execution dynamics

## Sources

1. Steven Campbell, Natascha Hey, Ciamac C. Moallemi, Marcel Nutz, "Risk-Based Auto-Deleveraging", arXiv:2603.15963v2 [q-fin.RM], July 2026. https://arxiv.org/abs/2603.15963
