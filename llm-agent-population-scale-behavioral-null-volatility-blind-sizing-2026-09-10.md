---
schema: strategy-research-record-v1
title: "LLM Agent Population-Scale Behavioral Null: Volatility-Blind Sizing, Render-Driven Selection, and Uncaptured Excursion"
created: 2026-09-10
updated: 2026-09-10
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - llm-agent
  - behavioral-alpha
  - contrarian
  - market-microstructure
  - operating-layer
  - volatility-blind
  - negative-result
status: research-only
confidence: high
source_as_of: 2026-09-04
sources:
  - "T.J. Barton, Chris Constantakis, Patti Hauseman, Annie Mous, Alaska Hoffman, Brian Bergeron, Hunter Goodreau, 'What LLM Trading Agents Actually Do in Production: A Six-Month, Population-Scale Record from Two Fleets', arXiv:2609.05663v1 [cs.AI], September 4, 2026. https://arxiv.org/abs/2609.05663"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# LLM Agent Population-Scale Behavioral Null: Volatility-Blind Sizing, Render-Driven Selection, and Uncaptured Excursion

## Provenance

- **Paper:** Barton et al. (2026), "What LLM Trading Agents Actually Do in Production: A Six-Month, Population-Scale Record from Two Fleets"
- **arXiv:** 2609.05663v1 [cs.AI]
- **Authors:** T.J. Barton (poof), Chris Constantakis, Patti Hauseman, Annie Mous, Alaska Hoffman, Brian Bergeron, Hunter Goodreau — DX Research Group (DXRG)
- **Published:** September 4, 2026
- **PDF:** https://arxiv.org/pdf/2609.05663
- **Data availability:** Aggregate statistics at https://dxrg.ai/research; DX Terminal Pro public dashboard at https://dune.com/dxrg/dx-terminal-pro

## Economic mechanism

### Source-reported

The paper measures how thousands of autonomous LLM trading agents behave in production across two systems:

1. **DX Terminal Pro** (Feb–Mar 2026): 3,505 user-funded vaults trading real ETH in Base memecoin markets (12 tokens, Uniswap V4 pools), 21 days, 7.5M invocations, ~300K onchain actions, ~$20M volume.
2. **DXAP live alpha fleet** (Jun–Aug 2026): 500–599 user-created agents trading Hyperliquid perpetuals (~99–100 perps), 69 days, 231,638 finalized turns, 14,596 fills.

The paper documents four FIRM findings:

1. **Operating layer determines behavior:** A risk slider explains leverage (+0.425× per level, p = 3.8 × 10⁻²⁷⁹); agent fixed effects absorb 60% of variance; a leaderboard render boundary causally routes selection (regression discontinuity 1.75× at the top-3 cut). Strategy text is overridden by configuration surfaces.
2. **Sizing is volatility-blind:** Median leverage is 5.0× in every volatility sextile across a 5.7× volatility spread (Spearman(volatility, leverage) = −0.001, p = 0.92). Notional goes the wrong way: agents size up in wilder names (Spearman = +0.165, p = 2.7 × 10⁻⁴⁰).
3. **Agents capture almost none of the upside:** 43.2% of positions saw at least +300 bps of favorable excursion within 24h, yet 49.3% of those closed with a negative trade return. A mechanical bracket recovers +39.0 bps per position.
4. **Neither fleet shows a directional edge:** The DXAP fleet trails a matched Hyperliquid retail benchmark (41% vs. 50% roundtrip win rate). Cumulative realized P&L is −$217K at common 5.5 bps fee rate.

### Research interpretation

The paper's findings suggest that LLM agent behavior is predictable based on their operating-layer configuration, not their strategy text. This predictability creates potential contrarian alpha opportunities:

- **Volatility-blind sizing** creates predictable liquidation patterns in high-volatility regimes. LLM agents use the same leverage regardless of volatility, leading to concentrated liquidations in volatile names.
- **Render-driven selection** creates predictable flow patterns around leaderboard changes. Agents disproportionately select symbols shown on the movers leaderboard, creating predictable buying pressure.
- **Uncaptured excursion** suggests that mechanical exit rules (brackets) outperform discretionary exits, implying that predictable exit behavior of LLM agents could be exploited.
- **Momentum posture at high frequency** concentrates liquidations: 62% of liquidations occur in one posture-slider cell (momentum × frequency 5), representing ~11% of the book.

The core hypothesis is that LLM agent behavioral patterns are sufficiently predictable to construct a contrarian strategy that trades against their systematic biases.

## Signal

The paper does not propose a specific trading signal. However, the documented behavioral patterns suggest the following research-proposed contrarian signals:

### Signal 1: Volatility-Adjusted Contrarian (research-proposed)

- **Formation timestamp:** End of each hourly bar.
- **Lookback:** 24-hour rolling window for realized volatility estimation.
- **Entry trigger:** When LLM agent concentration (measured by leaderboards or on-chain flow patterns) is high in a high-volatility name, take the opposite side.
- **Direction:** Short when LLM agents are structurally long (~78% of entries) in high-vol names.
- **Exit:** Mechanical bracket at +39 bps (research-proposed, based on the paper's bracket result).
- **Parameters:** Volatility sextile threshold (research-defined), LLM agent concentration threshold (research-defined).
- **Falsification threshold:** If contrarian positions do not show positive risk-adjusted returns net of 5.5 bps/side fees over a 6-month out-of-sample period, the hypothesis is falsified.

### Signal 2: Render Boundary Flow (research-proposed)

- **Formation timestamp:** When leaderboard composition changes (top-3 cutoff shifts).
- **Lookback:** Real-time leaderboard monitoring.
- **Entry trigger:** When a new symbol enters the top-3 gainers/losers/volume leaderboard, anticipate LLM agent buying pressure.
- **Direction:** Front-run the expected LLM agent flow by buying before the render boundary effect materializes.
- **Exit:** Mechanical bracket or time-based exit after flow subsides.
- **Parameters:** Render boundary cutoff (3rd position), holding period (research-defined).
- **Falsification threshold:** If front-running leaderboard changes does not generate positive returns net of fees and slippage, the hypothesis is falsified.

### Signal 3: Liquidation Cascade Anticipation (research-proposed)

- **Formation timestamp:** When volatility enters the upper sextile for names with high LLM agent concentration.
- **Lookback:** 24-hour rolling volatility, LLM agent positioning data.
- **Entry trigger:** Anticipate liquidations in the momentum × frequency 5 posture cell.
- **Direction:** Short high-vol names with high LLM agent momentum positioning.
- **Exit:** After liquidation cascade completes or mechanical bracket.
- **Parameters:** Volatility sextile threshold, LLM agent concentration threshold (research-defined).
- **Falsification threshold:** If liquidation cascade anticipation does not generate positive returns, the hypothesis is falsified.

**Note:** All three signals are research-proposed, not source-reported. The paper does not propose specific trading signals; it measures how LLM agents behave. The contrarian signals above are Scout-generated operationalizations based on the paper's findings.

## Required data

- **Instrument:** Crypto perpetual futures (Hyperliquid, Binance, or similar venues with LLM agent activity).
- **Universe:** Top ~100 perpetual contracts by volume, filtered for LLM agent activity (if measurable via on-chain data or leaderboard monitoring).
- **Venue:** Hyperliquid (primary, as studied in the paper), Binance (secondary).
- **Market type:** Perpetual futures.
- **Timeframe:** Hourly bars for volatility estimation; real-time for leaderboard monitoring.
- **Fields:** OHLCV, funding rate, open interest, leaderboard composition (if available), on-chain flow data (if available).
- **Point-in-time:** Leaderboard data must be observed in real-time to avoid look-ahead bias.
- **Missing-data:** LLM agent positioning data may not be directly observable; proxy measures (on-chain flow, leaderboard ranking) must be used.

## Execution assumptions

- **Signal-to-order timing:** End-of-hour for Signal 1; real-time for Signals 2 and 3.
- **Execution:** Next-bar market order (research-proposed).
- **Fill model:** Assume fill at mid-price plus half spread (research-proposed).
- **Fees:** 5.5 bps/side (common fee rate from the paper).
- **Slippage:** Not specified by the source; assume 1–2 bps per side (research-proposed).
- **Funding:** Observed funding rates (not modeled by the source).
- **Leverage:** 1–3× (research-proposed, conservative relative to LLM agents' 5× median).
- **Position sizing:** Equal-weight or volatility-adjusted (research-proposed).

## Evidence

### Source-reported

- **DXAP fleet win rate:** 41% roundtrip win rate vs. 50% for matched Hyperliquid retail benchmark (4-day trailing window ending Aug 15, 2026; n = 353 for DXAP, n = 16,009 for retail).
- **DXAP fleet P&L:** Cumulative realized P&L of −$217K at common 5.5 bps fee rate (Jun 8 to Jul 26 window).
- **Volatility-blind sizing:** Median leverage 5.0× in every volatility sextile; Spearman(volatility, leverage) = −0.001 (p = 0.92).
- **Liquidation concentration:** 128 of 205 liquidations (62%) in one posture-slider cell (momentum × frequency 5), representing ~11% of the book; Mantel-Haenszel odds ratio 22.37 [12.59, 37.45].
- **Capture gap:** 43.2% of positions saw ≥+300 bps favorable excursion within 24h; 49.3% of those closed negative. Mechanical bracket recovers +39.0 bps per position.
- **Render boundary effect:** 46.5% [43.4, 49.7] of entries in rendered symbols vs. 8.9% random-availability baseline (5.2× over-selection); RDD at rank-3/4 boundary: 1.75× [1.49, 2.06].
- **DX Terminal Pro:** 3,505 funded vaults, median true return 0.492×, 16.2% profitable, 92% ETH withdrawn.

All figures are from Barton et al. (arXiv:2609.05663v1, September 2026).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Neither fleet shows directional edge:** The DXAP fleet is not profitable and trails retail benchmark. This is the paper's central null result.
- **Decision quality indistinguishable across models:** Paired-replay league of frontier models on 416 captured production scenarios finds decision quality statistically indistinguishable at this horizon.
- **Forced numeric restatement fails:** Agents state liquidation distance in 45.0% of entry turns and size identically anyway; staters liquidate more often (5.8% vs. 1.2%).
- **Text-control conflict varies by system:** In DX Terminal Pro, sliders override text; in DXAP, text overrides sliders. Same lineage, opposite outcomes.

## Falsification plan

1. **Out-of-sample contrarian test:** Trade against documented LLM agent behavioral patterns on a 6-month out-of-sample period. If contrarian positions do not show positive risk-adjusted returns net of fees and slippage, the hypothesis is falsified.
2. **Ablation of behavioral signals:** Test each behavioral signal (volatility-blind sizing, render-driven selection, liquidation concentration) independently. If individual signals do not generate positive returns, the composite strategy may be driven by luck.
3. **Fee sensitivity:** Restate all P&L at varying fee levels (0, 5.5, 10, 15 bps/side). If strategy profits disappear at realistic fee levels, the alpha is not real.
4. **Regime breakdown:** Test across different volatility regimes (calm, normal, stressed). If contrarian strategy only works in one regime, it is not robust.
5. **Capacity test:** Estimate strategy capacity by varying position sizes. If strategy profits decay rapidly with size, it is not scalable.
6. **Control for market regime:** Test whether documented LLM agent behavioral patterns persist across different market regimes (bull, bear, sideways). If patterns are regime-dependent, the strategy must be regime-aware.

## Crypto portability

**Direct.** The paper studies crypto perpetual futures (Hyperliquid) and crypto spot markets (Base memecoins). The findings are directly applicable to crypto markets.

**Crypto-specific considerations:**
- **24/7 trading:** LLM agents operate continuously, creating persistent behavioral patterns.
- **Leverage availability:** High leverage (5×+) is standard on crypto perpetual platforms, amplifying the volatility-blind sizing effect.
- **Leaderboard visibility:** Public leaderboards on platforms like Hyperliquid create the render boundary effect documented in the paper.
- **Liquidation mechanics:** Crypto perpetual liquidation cascades are well-documented and align with the paper's findings about concentrated liquidations.

## Limitations

- **Paper-engine mechanics:** Most DXAP fills are paper (zero slippage, zero funding, 0.4% maintenance-margin placeholder liquidating ~2× later than real margining). Real-money results may differ.
- **Single venue per era:** Base memecoins in one window, Hyperliquid perps in another; cross-venue generality is asserted only where findings cross systems.
- **Model mix concentration:** DX Terminal Pro is one frozen model; DXAP is 86/91 qwen3.7-plus among active agents. Results may not generalize to other model families.
- **Observability of LLM agent behavior:** Contrarian strategies require observing LLM agent positioning, which may not be directly available. Proxy measures (leaderboard ranking, on-chain flow) may be noisy.
- **Regime dependency:** The paper studies a specific time period (Feb–Aug 2026). Behavioral patterns may change as LLM agent technology evolves.
- **Small liquidation sample:** 205 liquidations underpin the tail results; the concentration finding is robust to stratification but cell counts are small.
- **No independent reproduction:** The paper's findings have not been independently reproduced.
- **Data gaps:** The paper does not provide specific data on LLM agent positioning across all symbols, making it difficult to construct exact contrarian signals.

## Implementation status

No implementation in our research stack. The paper is an empirical measurement study, not a strategy implementation.

## Adoption boundary

This record is research material only. The paper's findings document how LLM agents behave in production, not a profitable trading strategy. The contrarian signals proposed above are Scout-generated operationalizations based on the paper's findings, not source-reported strategies.

A record being present in this repository does not mean:
- Profitable
- Validated alpha
- Approved for implementation
- Approved for paper trading
- Approved for testnet
- Approved for live trading

## Related Wiki records

- [[crypto-llm-agent-liquidity-scarcity-range-attention-factor-2026-09-01]] (different paper: LLM agents discovering factors, not measuring behavior)
- [[crypto-public-wallet-identity-trader-informativeness-adverse-selection-2026-09-02]] (related: public trader identity and adverse selection in crypto)

## Sources

1. T.J. Barton, Chris Constantakis, Patti Hauseman, Annie Mous, Alaska Hoffman, Brian Bergeron, Hunter Goodreau. "What LLM Trading Agents Actually Do in Production: A Six-Month, Population-Scale Record from Two Fleets." arXiv:2609.05663v1 [cs.AI], September 4, 2026. https://arxiv.org/abs/2609.05663
