---
schema: strategy-research-record-v1
title: "Dynamic Multi-Pair Statistical Arbitrage with PPO-LSTM Execution Overlay in Cryptocurrency Perpetual Futures"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - statistical-arbitrage
  - pair-trading
  - deep-reinforcement-learning
  - PPO
  - LSTM
  - cointegration
  - mean-reversion
  - perpetual-futures
status: research-only
confidence: medium
source_as_of: 2026-09-02
sources:
  - "arXiv:2606.04574v2 [cs.LG], 'Dynamic Multi-Pair Trading Strategy in Cryptocurrency Markets with Deep Reinforcement Learning', June 2026. DOI: 10.48550/arXiv.2606.04574. https://arxiv.org/abs/2606.04574"
  - "GitHub: https://github.com/damianlebiedz/pair-trading-with-rl (public replication repository)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Dynamic Multi-Pair Statistical Arbitrage with PPO-LSTM Execution Overlay in Cryptocurrency Perpetual Futures

## Provenance

- **Primary Source:** *"Dynamic Multi-Pair Trading Strategy in Cryptocurrency Markets with Deep Reinforcement Learning"*, arXiv preprint `arXiv:2606.04574v2 [cs.LG]`, June 2026. DOI: [10.48550/arXiv.2606.04574](https://doi.org/10.48550/arXiv.2606.04574). Full text: [https://arxiv.org/abs/2606.04574](https://arxiv.org/abs/2606.04574).
- **Code Repository:** [https://github.com/damianlebiedz/pair-trading-with-rl](https://github.com/damianlebiedz/pair-trading-with-rl) (public, Python 3.12, Poetry, Docker, Stable-Baselines3, W&B integration).
- **Primary Subject Areas:** Machine Learning (`cs.LG`), Neural and Evolutionary Computing (`cs.NE`), Statistical Finance (`q-fin.ST`), Trading and Market Microstructure (`q-fin.TR`).
- **Context:** 61 pages, 37 figures, 16 tables. The paper proposes a hybrid architecture combining hierarchical cointegration-based pair selection with a PPO-LSTM deep reinforcement learning execution agent operating within deterministic risk-shielding boundaries. Evaluated on Binance USD-M Futures 1-hour data, 2024 IS / 2025 OOS.

## Economic mechanism

### Source-reported

The strategy exploits temporary pricing anomalies between cointegrated cryptocurrency pairs. The core mechanism is:
1. **Cointegration-based pair selection:** Identify pairs of assets sharing a long-run equilibrium (cointegrated spread) with mean-reverting properties (Hurst exponent H < 0.5).
2. **"Fixed Risk, Adaptive Mean" execution:** Unlike classical static pair trading, the strategy trades a "snapshot equilibrium" where the hedge ratio (β) and volatility anchor (σ) are frozen at entry, but the spread mean (μ) remains adaptive to structural drift.
3. **DRL execution overlay:** A PPO-LSTM agent learns optimal timing and sizing decisions within deterministic risk-shielding boundaries, adapting to microstructural conditions that static z-score thresholds cannot capture.
4. **Safe RL via deterministic shielding:** Hard guardrails (stop-loss lock, take-profit, SL threshold) constrain the RL agent's policy, preventing divergence in extreme regimes.

### Research interpretation

The falsifiable thesis is that **DRL-based execution timing and sizing, constrained within statistically robust boundaries, adds value over classical z-score-based entry/exit rules in cryptocurrency pair trading**:

- Classical pair trading suffers from rigidity: fixed z-score thresholds cannot adapt to changing volatility regimes or microstructural conditions.
- PPO-LSTM can learn context-dependent execution policies that account for recent order flow, volatility clustering, and mean-reversion speed dynamics.
- However, unconstrained DRL is brittle in high-noise environments; deterministic shielding ensures the agent cannot deviate from statistically validated risk boundaries.
- The "snapshot equilibrium" approach (freezing β and σ at entry) avoids the continuous rebalancing friction that destroys alpha in volatile crypto markets.

## Signal

### Formation timestamp
- Signal computed at each hourly candle close using finalized close prices (Signal on Close, Execute on Open architecture).
- Pair selection: monthly reconstitution using preceding 2-month formation window.
- Timeframe: 1-hour bars.

### Lookback
- Cointegration: Engle-Granger two-step method on log-prices over 2-month formation window.
- Hedge ratio (β): OLS regression over 1-month rolling window.
- Z-Score mean (μ): Rolling window of 168 hours (1 week).
- Z-Score standard deviation (σ): Frozen at entry value during active position.
- Hurst exponent: computed over formation window.

### Long entry
- Spread z-score falls below entry threshold (parameter grid-searched).
- Entry at the next hourly candle open.
- Capital: 100% of pair allocation committed at entry.

### Short entry
- Spread z-score rises above entry threshold (mirror signal).
- Same capital commitment logic.

### Exit
- Take-profit: z-score returns to zero (mean-reversion target).
- Stop-loss: dynamically tightened over trade duration; "SL Lock" regime filter pauses trading during extreme volatility.
- Terminal liquidation: forced close at end of each monthly trading window.
- Position state: β and σ frozen at entry; μ remains live.

### Holding period
- Variable; depends on mean-reversion speed.
- Maximum: remainder of monthly trading window (forced liquidation at month end).
- Trade-to-trade compounding: capital updated immediately upon position closure.

### Parameters
- Z-Score entry/exit thresholds: grid-searched monthly.
- Z-Score window: 168 hours (1 week) default.
- Hedge ratio window: 1-month rolling.
- Pair selection: top n=20 pairs from N=100 most liquid assets by Final Score.
- Final Score: 0.5·(1-p_EG) + 0.5·R² if H < 0.5 and β > 0; else 0.
- Hurst exponent hard filter: H < 0.5 (anti-persistent/mean-reverting).
- Hedge feasibility: β > 0.
- Leverage: 10x default.
- Transaction fee: 0.05% default (taker); 0.10% stress test.
- Liquidation threshold: 100% of initial margin (conservative simplification).

### Position sizing
- Equal-weight across selected pairs: 1/n of available funds per pair.
- Within each pair: capital split by hedge ratio β (w_A = 1/(1+β), w_B = β/(1+β)).

## Required data

- **Instrument:** Binance USD-M Futures perpetual swap contracts.
- **Universe:** Top 100 most liquid assets by average daily quoted volume (USDT), dynamically revised monthly.
- **Venue:** Binance Futures.
- **Market type:** USD-M perpetual futures.
- **Timeframe:** 1-hour OHLCV bars.
- **Fields:** Open, High, Low, Close, Volume (hourly).
- **Point-in-time:** Strictly no look-ahead; formation window (t-2, t-1) completely isolated from trading window (t).
- **Timestamp:** UTC.
- **Missing-data:** Assets with data gaps during formation window excluded before ranking.
- **Funding/fee/spread:** 0.05% taker fee per execution; funding rate not explicitly modeled (only commission).

## Execution assumptions

- **Order type:** Market order at next hourly candle open (Signal on Close, Execute on Open).
- **Fill model:** Assumed full fill.
- **Latency:** 1-hour signal cadence; latency sensitivity not explicitly tested.
- **Fees:** 0.05% taker fee per trade (default); 0.10% stress test.
- **Slippage:** Not explicitly modeled beyond fee proxy.
- **Funding:** Perpetual swap funding rate costs not explicitly included in the default model; only commission modeled.
- **Impact / capacity:** Not quantified; 100-asset universe with dynamic liquidity filter suggests reasonable capacity for moderate AUM.
- **Leverage:** 10x default; liquidation engine enforces 100% margin exhaustion threshold.
- **Shorting:** Available via perpetual swap contracts.

## Evidence

### Source-reported

- **Baseline strategy OOS (2025):**
  - Optimized heuristic baseline (no RL): positive returns, statistically significant at 10% level via circular block bootstrap.
  - RL-enhanced Agent 2 (StepPnLReward, Autonomous Space, λ=1.2): substantially outperforms heuristic baseline OOS.
- **Statistical significance:** Stationary circular block bootstrap confirms Agent 2 risk-adjusted outperformance at 10% level. Falls marginally short of 5% threshold, attributed to extreme idiosyncratic variance in crypto.
- **Ablation results (Agent 2):**
  - Full Agent with shielding > Agent without shielding (shielding prevents divergence).
  - StepPnLReward > other reward formulations.
  - Autonomous observation space > restricted observation space.
  - Beta hedge (dynamic empirical) > fixed β=1.0 allocation.
  - Stop-Loss Lock regime filter improves stability.
  - Temporal tightening of stop-loss improves risk management.
- **Fee sensitivity:** Agent 2 remains profitable at 0.10% fee rate.
- **Multi-seed robustness:** 5 independent random seeds show consistent OOS performance direction.
- Source reports all results; this result has not been independently reproduced.

### Independently reproduced

Not independently reproduced. However, the full source code is available at [https://github.com/damianlebiedz/pair-trading-with-rl](https://github.com/damianlebiedz/pair-trading-with-rl) for independent replication.

### Negative evidence

- Statistical significance at 10% level, not 5% level, suggesting the signal may be weaker than headline numbers imply.
- The paper acknowledges "extreme idiosyncratic variance characteristic of digital assets" as a fundamental challenge.
- Unconstrained DRL (no shielding) shows severe divergence; the alpha depends on the deterministic shielding, not purely on the RL agent.
- Baseline heuristic strategy (no RL) already captures some of the edge; RL adds incremental but not transformative value.
- Funding rate costs are not modeled; on perpetual swaps, funding can be material for mean-reversion trades held overnight.

## Falsification plan

1. **Extend OOS period:** Run on 2026 data. If the RL agent fails to outperform the heuristic baseline, the OOS edge may be sample-specific.
2. **Remove shielding:** Test fully unconstrained PPO-LSTM. If performance collapses (as shown in ablation), the alpha is in the deterministic boundaries, not the RL policy.
3. **Alternative pair selection:** Use Johansen cointegration or dynamic time warping instead of Engle-Granger. If performance changes materially, the specific filter is load-bearing.
4. **Funding rate inclusion:** Add realistic perpetual swap funding costs. If net returns become negative, the strategy is not implementable on perpetuals.
5. **Venue transfer:** Re-run on OKX or Bybit perpetuals. If performance degrades, Binance-specific microstructure effects may dominate.
6. **Reduce leverage:** Test at 1x and 3x leverage. If the edge disappears without leverage, it may be driven by leverage amplification rather than true alpha.
7. **Hurst threshold sensitivity:** Vary the H < 0.5 threshold (e.g., H < 0.45, H < 0.48). If performance is sensitive, the structural filter may be overfit.
8. **Random pair selection:** Select pairs randomly (no cointegration filter). If performance is comparable, the cointegration selection adds no value.

## Crypto portability

**Direct.** The study is conducted entirely on Binance USD-M perpetual futures.

- **Perpetual vs spot:** Strategy uses perpetual swaps; shorting is natively available. Deployment on spot would require spot-margin or借券, changing cost structure.
- **24/7 session:** 1-hour candles; no session-specific adjustments described.
- **Venue:** Binance-specific; liquidity and microstructure may differ on other venues.
- **Funding rates:** Not modeled; a material gap for perpetual swap deployment.
- **Liquidation risk:** 10x leverage with 100% margin exhaustion threshold; extreme moves can force liquidation.

## Limitations

- **Binance-only:** All results from Binance USD-M Futures.
- **Funding rate omission:** Perpetual swap funding costs not included; this is a significant gap for mean-reversion strategies held overnight.
- **No slippage model:** Fee-only cost model does not capture market impact or spread dynamics.
- **10% statistical significance:** Not at conventional 5% level; results may be noise.
- **Short OOS period:** Only 1 year of OOS data (2025); insufficient for regime diversity.
- **RL complexity:** Training instability across seeds; performance seed-dependent.
- **Equal-weight pair allocation:** Does not optimize across pairs; diversification benefits are mechanical.
- **No cross-asset or cross-venue testing:** Results may not generalize beyond Binance perpetuals.
- **Complexity vs marginal edge:** The full pipeline (cointegration → Hurst filter → RL execution → shielding) is complex; the marginal value of RL over heuristic execution may not justify the complexity.

## Implementation status

Not implemented. No implementation in our research stack (PyBroker, Nautilus, or paper trading) has been completed. Public code available at [https://github.com/damianlebiedz/pair-trading-with-rl](https://github.com/damianlebiedz/pair-trading-with-rl).

## Adoption boundary

This record represents research material only. A record being present in this repository does not mean:
- Profitable;
- Validated alpha;
- Approved for implementation;
- Approved for paper trading;
- Approved for testnet;
- Approved for live trading.

## Related Wiki records

- [[quant/crypto-perpetual-optimal-liquidation-funding-rate-hjb-2026-09-02]] — related perpetual futures execution; different mechanism (optimal liquidation via HJB vs. pair-trading mean-reversion).
- [[quant/sequential-limit-order-execution-quoting-signal-adaptive-triangular-hjb-2026-09-02]] — related execution optimization; different context (market making vs. stat arb).

## Sources

- *"Dynamic Multi-Pair Trading Strategy in Cryptocurrency Markets with Deep Reinforcement Learning"*, arXiv:2606.04574v2 [cs.LG], June 2026. DOI: 10.48550/arXiv.2606.04574. https://arxiv.org/abs/2606.04574.
- Code: https://github.com/damianlebiedz/pair-trading-with-rl (accessed September 2, 2026).
