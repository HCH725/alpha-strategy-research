---
schema: strategy-research-record-v1
title: "Stablecoin De-Peg Primary-Arb Recovery: Mean-Field Game Threshold Model"
created: 2026-09-21
updated: 2026-09-21
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - stablecoin
  - depeg
  - mean-field-game
  - arbitrage
  - defi
status: research-only
confidence: medium
source_as_of: "2026-05-07 (arXiv v2)"
sources:
  - "https://arxiv.org/abs/2601.18991"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Stablecoin De-Peg Primary-Arb Recovery: Mean-Field Game Threshold Model

## Provenance

- **Primary Source:** Hardhik Mohanty and Bhaskar Krishnamachari (University of Southern California, Viterbi School of Engineering), "Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics", arXiv preprint `arXiv:2601.18991v2 [q-fin.TR]`, revised May 7, 2026. Accepted at IEEE International Conference on Blockchain and Cryptocurrency (ICBC) 2026.
- **Abstract URL:** https://arxiv.org/abs/2601.18991
- **Full-Text HTML:** https://arxiv.org/html/2601.18991v2
- **DOI:** https://doi.org/10.48550/arXiv.2601.18991
- **Code:** Publicly available (referenced as [27] in paper, link not resolved from text alone; code repository not directly verified).
- **Verification:** Full paper HTML retrieved and inspected. Author list, title, abstract, methodology, calibration data, experimental results (Tables I–III, Figures 3–9), and key claims verified against primary source text.

## Economic mechanism

### Source-reported

The paper develops a dynamic mean-field game (MFG) framework for fiat-collateralized stablecoins (USDC, USDT) in which two populations — arbitrageurs (15% of agents) and retail traders (85%) — strategically interact across primary markets (mint/redeem at $1 peg via treasury) and secondary markets (CEX/DEX exchanges) during de-peg episodes. The MFG endogenously maps market frictions into a market-clearing price path and implied net order flows.

Key source-reported findings:
1. **Primary-market arbitrage is the dominant peg-restoring mechanism** when redemption rails are functional. In the May 2022 USDT de-peg (Terra collapse), stabilization was overwhelmingly driven by primary-market redemptions.
2. **Event-specific channel decomposition:** In the March 2023 USDC de-peg (SVB), the primary channel initially contributed negatively due to impaired minting/redemption, and recovery reflected a joint role of primary and secondary forces once rails were restored. In the July 2023 USDT venue-level failure, both channels contributed little.
3. **Non-linear breakdown threshold in primary-rail friction (κ_P):** When κ_P ≤ ~10 (model units), de-peg half-life remains short (~2–4 model steps) across a wide range of secondary frictions. Once κ_P rises past ~15–18, half-life increases sharply — a breakdown of mint/redeem arbitrage capacity. Secondary-market liquidity acts mainly as a complement in the impaired-primary region.
4. **Calibration to three historical events** reproduces observed recovery half-lives: May 2022 USDT (sub-3-hour recovery, both data and model agree), March 2023 USDC (model estimates ~half-day recovery), July 2023 USDT (model predicts 45.9-hour half-life vs. 30.7-hour empirical).

### Research interpretation

The falsifiable alpha hypothesis: **during stablecoin de-peg events, the speed and completeness of peg recovery are primarily determined by the operational state of primary-market mint/redeem rails, not by secondary-market liquidity depth.** A de-peg whose primary rails are impaired (high κ_P) will persist longer and reverse more slowly, creating a harvestable window for traders who can assess primary-rail status in real-time.

Operationalizable signals (research-proposed):
- **Primary-rail friction estimation:** Monitor on-chain mint/redeem activity, treasury reserve attestation status, banking partner health, and chain-level congestion as proxies for κ_P.
- **De-peg severity prediction:** When κ_P is estimated to be rising (e.g., banking partner distress, reserve transparency concerns), predict longer recovery half-lives and larger mispricing.
- **Channel-aware entry:** Enter positions only when primary rails are estimated to be functional (low κ_P), avoiding "falling knife" scenarios where primary arbitrage is impaired.
- **Secondary-market depth as confirmation:** Use secondary-market order book depth and retail trader share as a secondary filter — thinner books in the impaired-primary region amplify mispricing.

## Signal

**Signal formation:** Continuous monitoring of stablecoin primary-rail status (on-chain mint/redeem flows, reserve attestations, banking partner health indicators) and secondary-market microstructure (order book depth, bid-ask spread, trading volume on major CEX/DEX venues).

**Entry logic (research-proposed):**
1. Detect de-peg event: stablecoin price deviates from $1 by more than a threshold (research-proposed threshold: 0.5% for monitoring, 1% for active consideration).
2. Assess primary-rail status: if on-chain mint/redeem activity is normal and reserve attestations are current → primary rails functional → enter long on discounted stablecoin (expect rapid recovery).
3. If primary rails appear impaired (reduced on-chain flow, reserve concerns, banking partner issues) → do NOT enter or reduce position size → de-peg may persist.
4. Secondary confirmation: order book depth on major venues, retail trader flow composition.

**Exit logic (research-proposed):** Close position when stablecoin price returns within 0.1% of $1 peg, or when primary-rail impairment is detected post-entry (stop-loss on extended de-peg).

**Holding period:** Variable — from hours (May 2022 USDT: sub-3-hour recovery) to days (July 2023 USDT: ~46-hour half-life). No fixed holding period; exit driven by peg recovery or rail-status deterioration.

**Position sizing (research-proposed):** Scale by estimated κ_P — larger positions when primary rails are assessed as functional (lower risk of prolonged de-peg), smaller or no position when rails are impaired.

**Parameters:** Not fully specified by source. Thresholds for "functional" vs. "impaired" primary rails, entry/exit thresholds, and position sizing rules are all research-proposed.

## Required data

- **Instrument:** Fiat-collateralized stablecoins (USDC, USDT, and potentially DAI/FRAX).
- **Venue:** Binance spot (used in paper for calibration), plus on-chain data for primary-market mint/redeem flows.
- **Market type:** Spot stablecoin pairs (USDC/USD, USDT/USD).
- **Timeframe:** 1-minute to hourly candlestick data for de-peg event analysis; continuous monitoring for real-time detection.
- **Data fields:** OHLCV for stablecoin/USD pairs, on-chain mint/redeem transaction volumes, treasury reserve attestation data, banking partner status indicators, order book depth on major venues.
- **Timestamp requirements:** High-frequency (1-minute or finer) during de-peg events for calibration; hourly or finer for real-time monitoring.
- **Point-in-time requirements:** On-chain mint/redeem data must be point-in-time (confirmed blocks only); reserve attestation data must reflect the attestation date, not publication date.
- **Missing data:** Primary-rail friction (κ_P) is not directly observable; must be proxied from on-chain flow, reserve status, and banking partner indicators. The paper does not specify how to measure κ_P in real-time.

## Execution assumptions

- **Signal-to-order timing:** Source does not specify. Research-proposed: enter within minutes of de-peg detection if primary rails are assessed as functional.
- **Execution:** Market orders on CEX spot for stablecoin/USD pairs. Source uses Binance spot data for calibration but does not model execution explicitly.
- **Fill model:** Not specified by source.
- **Fees:** Not specified by source. Binance spot taker fees (typically 10 bps) would apply.
- **Slippage:** Not specified by source. During de-peg events, spreads widen and slippage increases; the model captures this via venue-impact parameters (λ_s) but does not provide execution-level slippage estimates.
- **Spread:** Widens during de-peg events; not quantified by source for execution purposes.
- **Funding:** Not applicable for spot positions. For perpetual futures positions (research-proposed extension), funding rate dynamics during de-peg events would need to be modeled.
- **Capacity:** Not specified by source. Stablecoin de-peg events are infrequent and short-lived; capacity is likely limited by available liquidity during stress.
- **Leverage:** Not specified by source. Research-proposed: avoid leverage given tail-risk of extended de-peg.
- **Latency:** Not specified by source. Primary-rail assessment requires on-chain data processing latency.

## Evidence

### Source-reported

All figures below trace directly to Mohanty & Krishnamachari (arXiv:2601.18991v2, Section V, Tables II–III, Figures 3–9):

**Model calibration performance (Table II, averaged across 3 de-peg events):**
- Dynamic MFG: Avg. RMSE = 0.0128, Avg. half-life error = 0.41 model steps
- AR(1) baseline: Avg. RMSE = 0.0158, Avg. half-life error = 0.36
- ARMA-GARCH baseline: Avg. RMSE = 0.0162, Avg. half-life error = 0.24
- ARX baseline: Avg. RMSE = 0.0217, Avg. half-life error = 1.15

**Half-life estimates (Figure 5):**
- May 2022 USDT: sub-3-hour recovery (both data and model agree)
- March 2023 USDC: model estimates ~12-hour recovery
- July 2023 USDT: model predicts 45.9-hour half-life vs. 30.7-hour empirical (AR(1) estimate)

**Out-of-sample performance on March 2023 USDC (Table III):**
- 70/30 split: Train RMSE 0.0028, Test RMSE 0.0072
- 80/20 split: Train RMSE 0.0023, Test RMSE 0.0070
- 90/10 split: Train RMSE 0.0020, Test RMSE 0.0073

**Sensitivity analysis (Figures 7–8):**
- Primary-rail friction κ_P ≤ ~10: half-life ~2–4 model steps (short recovery)
- κ_P > ~15–18: half-life increases sharply (breakdown threshold)
- At intermediate retail shares (π_R ∈ [0.4, 0.7]) with shallow secondary books, half-life exceeds 30 model steps

Source reports that the dynamic MFG achieves the lowest average RMSE among compared models and enables counterfactual experiments on market structure that reduced-form models cannot perform. This result has not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The paper acknowledges that the model is calibrated on only 3 historical de-peg events, which is a small sample.
- Out-of-sample test RMSE (~0.007) is substantially higher than in-sample train RMSE (~0.002), indicating some overfitting or regime sensitivity.
- The July 2023 USDT model half-life (45.9 hours) overestimates the empirical value (30.7 hours) by ~50%.
- The model does not account for counterparty risk, smart contract risk, or regulatory intervention — all of which have historically played roles in de-peg dynamics.
- None identified in the reviewed sources beyond the above; absence is not evidence of no negative result.

## Falsification plan

1. **Primary-rail dependency test:** If a de-peg event occurs with fully functional primary rails but the recovery half-life is long (>24 hours), the primary-rail dominance hypothesis is weakened.
2. **Threshold validation:** Collect a larger sample of de-peg events (including minor de-pegs < 1% deviation) and test whether the κ_P ≈ 15–18 breakdown threshold is stable across events.
3. **Out-of-sample prediction:** Apply the calibrated model to a new de-peg event not used in training and evaluate whether the predicted half-life is within 50% of the observed half-life.
4. **Counterfactual robustness:** Test whether the model's counterfactual predictions (e.g., "if primary rails were faster, recovery would be X hours shorter") are consistent with natural experiments where primary-rail accessibility changed during an event.
5. **Secondary-market irrelevance test:** If a de-peg occurs with deep secondary-market liquidity but impaired primary rails and recovery is still slow, the model's claim that secondary liquidity is only a complement is supported; if recovery is fast despite impaired rails, the model is weakened.
6. **Actionable threshold (research-defined):** A de-peg harvesting strategy that enters only when κ_P proxy indicators are "green" should achieve positive returns on a sample of ≥5 de-peg events with a Sharpe > 0.5 after costs. Failure to achieve this on the available historical sample would weaken the alpha hypothesis.

## Crypto portability

**direct**

The paper is inherently crypto-native: it models fiat-collateralized stablecoins (USDC, USDT) on crypto exchanges (Binance) and on-chain primary markets. The mechanism — primary-market arbitrage restoring the peg — is specific to the stablecoin market structure and does not require porting from traditional assets.

**Crypto-specific considerations:**
- **Spot vs. perpetual:** The paper models spot stablecoin pairs. A perpetual-futures extension (e.g., USDC/USD perp) would introduce funding-rate dynamics during de-peg events, which the model does not capture.
- **Venue fragmentation:** De-peg events often involve venue-specific dislocations (e.g., July 2023 USDT was localized to Binance). The model uses a single secondary-market price; multi-venue arbitrage across fragmented liquidity is not modeled.
- **On-chain latency:** Primary-market mint/redeem operations have chain-dependent confirmation times (seconds to minutes on Ethereum, faster on L2s). The model uses discrete time steps without explicit chain-latency modeling.
- **Regulatory intervention:** Historical de-pegs have been influenced by regulatory actions (e.g., Circle's SVB exposure disclosure). The model does not incorporate regulatory shock dynamics.
- **Counterparty risk:** Banking partner failures (SVB) can impair primary rails; this is captured implicitly via κ_P but not modeled as an endogenous risk.

## Limitations

- **Small calibration sample:** Only 3 historical de-peg events used for calibration (May 2022 USDT, March 2023 USDC, July 2023 USDT). Generalizability is untested.
- **κ_P not directly observable:** Primary-rail friction is a model-internal parameter estimated by fitting price paths; real-time measurement requires proxy indicators that are not specified by the source.
- **No transaction cost modeling:** The paper does not model fees, slippage, or spread for executing the de-peg harvesting strategy. During de-peg events, spreads can widen dramatically, eroding or eliminating the mispricing opportunity.
- **Out-of-sample overfitting risk:** Test RMSE is ~3.5× train RMSE on the March 2023 USDC event, suggesting the model may not generalize well to unseen de-peg dynamics.
- **Half-life estimation error:** The July 2023 USDT model overestimates recovery half-life by ~50% (45.9 vs. 30.7 hours).
- **No capacity analysis:** The paper does not address how much capital can be deployed in a de-peg harvesting strategy before market impact eliminates the edge.
- **Not independently reproduced:** All results are source-reported only.
- **Research-proposed operationalization:** The entry/exit rules, position sizing, κ_P proxy indicators, and thresholds described in this record are research-proposed, not source-reported. The paper is a modeling framework, not a trading strategy.

## Implementation status

Not implemented. The paper is a theoretical modeling framework calibrated on historical data. No trading strategy has been implemented or backtested using this model's predictions. Code is stated to be publicly available but the repository URL was not resolved from the paper text.

## Adoption boundary

A record being present in this repository does **not** mean:
- Passed Research Intake Review;
- Entered Hermes Wiki Brain;
- Entered the production candidate pool;
- Completed Qlib full-backtest validation;
- Became a frozen survivor or leaderboard entry;
- Profitable;
- Validated alpha;
- Approved for implementation;
- Approved for paper trading;
- Approved for testnet;
- Approved for live trading.

## Related Wiki records

- `[[quant/stableswap-amplification-pool-sizing-institutional-fx-2026-09-09]]` — Related to stablecoin mechanics but focuses on StableSwap pool design, not de-peg recovery dynamics.
- `[[quant/stableeval-arena-agentic-stablecoin-peg-risk-negative-evidence-arxiv-2609.18949-2026-09-20]]` — Negative evidence on LLM-based stablecoin peg-risk detection; complementary to this paper's equilibrium-based approach.
- `[[quant/tradingview-stablecoin-dominance-volatility-adjusted-risk-regime-2026-09-21]]` — Stablecoin dominance as a regime indicator; different mechanism but shares the stablecoin-systemic-risk theme.
- `[[quant/ethena-optimal-execution-delta-neutral-steth-perp-carry-2026-09-02]]` — Ethena yield-bearing stablecoin optimal execution; related to stablecoin carry mechanics but different mechanism (delta-neutral perp carry vs. de-peg arbitrage).

## Sources

1. Hardhik Mohanty and Bhaskar Krishnamachari. "Who Restores the Peg? A Mean-Field Game Approach to Model Stablecoin Market Dynamics." arXiv preprint arXiv:2601.18991v2 [q-fin.TR], revised May 7, 2026. Accepted at IEEE ICBC 2026. URL: https://arxiv.org/abs/2601.18991. DOI: https://doi.org/10.48550/arXiv.2601.18991.
