---
schema: strategy-research-record-v1
title: "ArchetypeTrader: VQ-Distilled Hierarchical RL Archetype Selection and Regret-Aware Refinement for Crypto Perpetuals"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - reinforcement-learning
  - hierarchical-rl
  - vector-quantization
  - crypto-perpetual
  - cryptocurrency
  - archetype-discovery
  - regret-aware
status: research-only
confidence: medium
source_as_of: 2026-03-14
sources:
  - "DOI: 10.1609/aaai.v40i34.40166 (AAAI 2026, Vol. 40, No. 34, pp. 29269–29276)"
  - "https://personal.ntu.edu.sg/boan/papers/AAAI26_ArchetypeTrader.pdf"
  - "https://ojs.aaai.org/index.php/AAAI/article/view/40166"
  - "https://github.com/yfcck/ArchetypeTrader (public fork, commit 02183806eea6530d062b1f016ade68190f3bc22b, 2026-04-06)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# ArchetypeTrader: VQ-Distilled Hierarchical RL Archetype Selection and Regret-Aware Refinement for Crypto Perpetuals

## Provenance

- **Paper:** "ArchetypeTrader: Reinforcement Learning for Selecting and Refining Learnable Strategic Archetypes in Quantitative Trading"
- **Authors:** Chuqiao Zong, Molei Qin, Haochong Xia, Bo An — Nanyang Technological University, Singapore
- **Venue:** AAAI 2026, Vol. 40, No. 34, pp. 29269–29276
- **Published:** 2026-03-14
- **DOI:** https://doi.org/10.1609/aaai.v40i34.40166
- **PDF:** https://personal.ntu.edu.sg/boan/papers/AAAI26_ArchetypeTrader.pdf
- **GitHub (public fork):** https://github.com/yfcck/ArchetypeTrader (commit `02183806eea6530d062b1f016ade68190f3bc22b`, 2026-04-06). Note: the original repo (liupion9/ArchetypeTrader) appears to be private. The public fork implements the paper with documented deviations (see Execution assumptions).

## Economic mechanism

### Source-reported

The authors identify two shortcomings in existing RL for crypto trading: (1) human-engineered regime labels (e.g., trend/volatility bins) oversimplify market dynamics, biasing sub-policies toward superficial trend-following and neglecting nuanced profitable opportunities; (2) demonstration data is either ignored or used in overly granular "optimal" trajectories that overwhelm learning and introduce bias, causing high variance and large drawdowns.

ArchetypeTrader addresses this by discovering discrete, reusable trading archetypes from demonstration trajectories via vector quantization (VQ), then training a hierarchical RL system to select and refine archetypes based on market context and intra-horizon performance.

### Research interpretation

The core hypothesis is that cryptocurrency price dynamics at 10-minute horizons contain a finite set of recurring behavioral patterns (archetypes) that can be distilled from DP-generated optimal demonstrations into a compact codebook. An RL agent can then learn to match current market state to the appropriate archetype and perform at most one refinement step per horizon, constrained by a regret-aware reward that penalizes both underperformance vs. the base archetype and deviation from the hindsight-optimal adaptation.

This is a meta-learning / skill-discovery mechanism: the VQ codebook acts as a learned library of trading behaviors, and the hierarchical controller selects + adapts from this library. The information bottleneck (archetype dimension 16 < network dimension 128) forces abstraction beyond raw features.

**Component roles:**
- **Phase I (Archetype Discovery):** DP planner generates 30k demonstration trajectories; VQ encoder-decoder compresses into K=10 discrete archetypes.
- **Phase II (Archetype Selection):** Horizon-level PPO-style RL agent selects best archetype per 72-step horizon; frozen decoder generates step-by-step micro-actions.
- **Phase III (Archetype Refinement):** Step-level RL agent fine-tunes selected archetype's actions via regret-aware reward, at most one adjustment per horizon; AdaLN conditions on archetype context.

## Signal

### Formation timestamp
- Formed at each 10-minute bar close (standard candle boundary on Binance).
- Market observations include M=25 level LOB, OHLCV bar, and technical indicators over backward window w.

### Lookback
- VQ encoder-decoder processes a full horizon of h=72 steps (720 minutes = 12 hours) of historical trajectories during Phase I training.
- At inference, the horizon-level selector observes market state at the first bar of each 72-step horizon.
- The step-level adapter observes real-time state including the selected archetype embedding, current base action, cumulative archetype reward, and remaining horizon steps.

### Entry / Exit / Position
- Action space: {0 (short, position = −m), 1 (flat, position = 0), 2 (long, position = +m)}.
- The horizon-level selector picks an archetype code; the frozen decoder generates a sequence of 72 step-level base actions.
- The refinement adapter may override the base action at most once per horizon: when it acts, the final action is set to 0 (flat) or 2 (long), overriding the base archetype's action at that step.
- Position size m varies by asset: BTC=8, ETH=100, DOT=2500, BNB=200 (units of perpetual contract).

### Parameters (source-reported)
- VQ codebook: K=10 archetypes, archetype vector dimension=16, network hidden dim=128, commitment loss β0=0.25.
- VQ training: 100 epochs, 30k DP trajectories, horizon h=72.
- Selector training: 3M PPO steps, KL penalty α=1.
- Adapter training: 1M steps, β2=1, β1 ∈ {0.3, 0.5, 0.7} (0.5 for BTC/DOT, 0.7 for ETH/BNB, tuned via validation).
- Commission rate: δ = 0.02% per trade.
- DP modules are training-only; disabled during inference to prevent future information leakage.

### Holding period
- Horizon length h=72 bars (720 minutes). The agent makes one archetype selection per horizon and at most one refinement action within the horizon.
- Positions persist until the next archetype selection or refinement override.

### Position-sizing logic
- Fixed maximum position m per asset. No dynamic sizing, Kelly, or vol-targeting described in the paper.

## Required data

- **Universe:** BTC/USDT, ETH/USDT, DOT/USDT, BNB/USDT perpetual contracts on Binance.
- **Venue:** Binance (perpetual futures).
- **Timeframe:** 10-minute bars with 25-level limit order book (LOB) depth.
- **Fields:** OHLCV (open, high, low, close, volume), LOB bid/ask price and quantity for M=25 levels, technical indicators computed over backward window w.
- **Sample period:** Training: 2021-06-01 to 2023-05-31; Validation: 2023-06-01 to 2023-12-31; Testing: 2024-01-01 to 2024-09-01.
- **Point-in-time:** Standard candle boundary alignment assumed; no explicit look-ahead protection beyond chronological train/val/test split described.
- **Missing data:** Not explicitly addressed in the paper.
- **Funding rates:** Not included in the MDP formulation; funding costs are not modeled.

## Execution assumptions

- **Commission:** 0.02% per trade (δ = 0.02%), applied to |ΔP| × pmark.
- **LOB fill cost:** C(|ΔP|) models the cost of executing against the limit order book. The paper includes LOB fill cost in the execution loss formula but does not specify the exact fill model beyond this general form.
- **Slippage:** Not explicitly modeled beyond LOB fill cost. The paper does not discuss slippage or spread separately.
- **Funding:** Not modeled. The MDP reward is net value difference without funding accrual.
- **Mark price:** Position PnL calculated against mark price.
- **Order type:** Implicitly market/limit orders via LOB fill cost model.
- **Latency:** Not discussed; 10-minute bar frequency implies low latency sensitivity.
- **Leverage / margin:** Not explicitly specified; position limits are defined by max position m per asset.
- **Fill model:** Not specified beyond LOB cost function C(·). The exact relationship between order size and fill price within the LOB is not detailed.

**Key assumption gap:** The paper models execution cost via C(|ΔP|) + δ|ΔP|pmark but does not specify the functional form of C(·) or whether it accounts for partial fills, queue position, or order book impact beyond the top-of-book level.

## Evidence

### Source-reported

Source: Table 1 of Zong et al. (AAAI 2026), test period 2024-01-01 to 2024-09-01.

| Market | Model | TR (%) | ASR | ACR | ASoR | AVOL (%) | MDD (%) |
|--------|-------|--------|-----|-----|------|----------|---------|
| BTC | ArchetypeTrader | 76.25 | 2.66 | 3.76 | 4.48 | 33.57 | 23.75 |
| BTC | EarnHFT (best baseline) | 24.56 | 1.00 | 1.52 | 1.58 | 39.28 | 25.72 |
| ETH | ArchetypeTrader | 41.93 | 1.37 | 1.86 | 2.26 | 43.61 | 32.13 |
| DOT | ArchetypeTrader | 147.48 | 3.19 | 8.72 | 6.08 | 44.41 | 16.26 |
| BNB | ArchetypeTrader | 39.24 | 1.34 | 3.53 | 2.41 | 42.31 | 16.03 |

Note: The table in the paper appears to have a two-column layout (BTC/ETH on left, DOT/BNB on right). The exact attribution of ETH vs DOT vs BNB rows was parsed from the paper's table structure. Source-reported results have not been independently reproduced.

The paper reports ArchetypeTrader significantly outperforms 8 baselines (DQN, PPO, CDQNRP, CLSTM-PPO, EarnHFT, MacroHFT, MACD, IV) across all 4 assets on both profit and risk metrics. The strongest baseline is typically EarnHFT (ASR 1.00 on BTC) or MACD/IV depending on the asset.

### Independently reproduced

Not independently reproduced.

### Negative evidence

None identified in the reviewed sources; absence is not evidence of no negative result. However, the following concerns apply:

1. **Short test window:** The test period is only 9 months (2024-01 to 2024-09), which covers a specific market regime. Generalization to bear markets, high-volatility crashes, or different market microstructure regimes is unverified.
2. **Survivorship in universe:** Only 4 major assets are tested (BTC/ETH/DOT/BNB). Performance on the broader crypto perpetual universe is unknown.
3. **Funding cost omission:** The MDP does not include funding rate accrual. In crypto perpetuals, funding costs can be material (sometimes >100% annualized for crowded positions), and the absence of this cost in training and evaluation means live performance would be lower.
4. **No out-of-sample beyond test set:** No walk-forward or rolling retraining protocol is described. The model is trained once on 2021-2023 data and tested on a single 9-month window.
5. **Commission rate (0.02%) is low:** Real taker fees on major perpetual exchanges are typically 0.04–0.06%. Even at 0.02% maker rate, the paper's cost assumption is optimistic for many venues and order sizes.

## Falsification plan

1. **Walk-forward retraining:** Retrain on rolling windows (e.g., 12-month train, 3-month validation, 3-month test) across the full 2021-2024 period and check whether ASR and MDD remain stable across different market regimes.
2. **Funding cost stress:** Add realistic funding rate accrual to the reward function and re-evaluate. If ASR drops below 1.0 or MDD exceeds 40% under 8-hour funding at 0.01% per period, the cost-free assumption materially inflates results.
3. **Commission sensitivity:** Re-run with 0.04% and 0.06% commission to test robustness. The paper's 0.02% is research-defined falsification threshold for fee tolerance.
4. **Universe expansion:** Test on top-20 or top-50 crypto perpetual pairs to check whether archetype discovery generalizes beyond 4 large-cap assets.
5. **Ablation of refinement adapter:** Disable Phase III and compare. If the refinement contributes <10% of total Sharpe improvement, the additional training complexity may not be justified.
6. **Ablation of KL penalty:** Remove the KL term from the selector objective (α=0) to test whether demonstration guidance is necessary or if pure RL can discover comparable archetypes.
7. **Parameter perturbation:** Vary K ∈ {5, 10, 20, 50}, h ∈ {24, 48, 72, 144}, and archetype dimension ∈ {8, 16, 32} to assess sensitivity. The paper uses fixed K=10 without sensitivity analysis.
8. **Capacity / slippage stress:** Model order-book impact for position sizes > paper's max position to test whether the LOB cost function C(·) adequately captures real market impact.

## Crypto portability

**Direct** — the strategy is designed for and evaluated on crypto perpetual contracts (BTC/ETH/DOT/BNB vs USDT on Binance).

**Crypto-specific considerations:**
- The 24/7 market structure is naturally handled by the 10-minute bar framework.
- Exchange fragmentation is a risk: the model is trained on Binance LOB data; transferability to other venues (Bybit, OKX, Hyperliquid) with different LOB depth, fee structures, and liquidity profiles is unverified.
- The absence of funding cost modeling is a significant gap for live deployment on perpetual contracts.
- Liquidation mechanics are not modeled; the position is bounded by m but there is no liquidation price or margin check in the MDP.
- Mark price vs. last price divergence is assumed negligible (mark price used for PnL calculation), which may not hold during high-volatility events.

## Limitations

- **Underspecified LOB fill cost function:** The paper defines execution loss with C(|ΔP|) but does not specify the functional form, making it difficult to assess whether the cost model is realistic for the tested position sizes and LOB depths.
- **Short test period:** 9 months of test data on 4 assets is a limited evaluation window.
- **No funding cost modeling:** Critical omission for perpetual contract strategies.
- **No walk-forward validation:** Single train/val/test split; no rolling retraining.
- **Low commission assumption:** 0.02% is below typical retail taker fees and at or below maker fees on most exchanges.
- **No capacity analysis:** Position sizes are fixed; no discussion of market impact or capacity limits.
- **Limited baseline comparison:** Compared to 8 baselines, all from the same RL-for-trading literature. No comparison to traditional systematic strategies (e.g., momentum, mean-reversion, funding carry).
- **Implementation deviations:** The public fork (yfcck/ArchetypeTrader) documents several deviations from the paper: two-stage VQ pretraining, PPO-style objectives replacing paper's formulation, τ_remain normalization fix, commission rate consistency fix, and ETH max position correction. These deviations may affect reproducibility of the paper's reported numbers.
- **Not independently reproduced.**

## Implementation status

Not implemented. No implementation exists in our research stack.

## Adoption boundary

This is a research-only capture. The paper's source-reported results have not been independently reproduced. The strategy is not approved for implementation, paper trading, testnet, or live trading.

## Related Wiki records

- [[quant/earnhft-hierarchical-rl-high-frequency-crypto-trading-2026-09-04]] (if exists) — EarnHFT is a direct predecessor baseline; both use hierarchical RL for crypto trading but differ in regime labeling (handcrafted vs. VQ-discovered archetypes).
- [[quant/prism-vq-vector-quantized-discrete-latent-factor-stock-ranking-2026-09-04]] — Uses vector quantization for factor representation, but applies to cross-sectional stock ranking rather than temporal archetype discovery for crypto.

## Sources

1. Zong, C., Qin, M., Xia, H., & An, B. (2026). ArchetypeTrader: Reinforcement Learning for Selecting and Refining Learnable Strategic Archetypes in Quantitative Trading. *Proceedings of the AAAI Conference on Artificial Intelligence*, 40(34), 29269–29276. DOI: 10.1609/aaai.v40i34.40166. Published 2026-03-14.
2. PDF: https://personal.ntu.edu.sg/boan/papers/AAAI26_ArchetypeTrader.pdf
3. AAAI proceedings: https://ojs.aaai.org/index.php/AAAI/article/view/40166
4. GitHub (public fork): https://github.com/yfcck/ArchetypeTrader, commit `02183806eea6530d062b1f016ade68190f3bc22b` (2026-04-06).
