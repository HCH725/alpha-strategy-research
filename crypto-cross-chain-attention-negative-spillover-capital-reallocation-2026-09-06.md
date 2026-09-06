---
schema: strategy-research-record-v1
title: Cross-Chain Attention-Driven Negative Spillover Capital Reallocation
created: 2026-09-06
updated: 2026-09-06
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-chain
  - attention
  - spillover
  - capital-reallocation
status: research-only
confidence: medium
source_as_of: 2026-02-27
sources:
  - "arXiv:2602.23762v1 [q-fin.PR], submitted 2026-02-27. https://arxiv.org/abs/2602.23762"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Chain Attention-Driven Negative Spillover Capital Reallocation

## Provenance

- **Paper:** Mengzhong Ma, Te Bao, Yonggang Wen, *"One Rising Ship Sinks Other Ships: Cross-Chain Negative Spillovers in Crypto Markets"*, arXiv:2602.23762v1 [q-fin.PR], submitted February 27, 2026.
- **Authors:** Mengzhong Ma (Interdisciplinary Graduate School, NTU Singapore), Te Bao (School of Social Sciences, NTU Singapore; corresponding author), Yonggang Wen (College of Computing & Data Science, NTU Singapore).
- **Affiliations:** NTU Centre in Computational Technologies for Finance; Tier 1 Grant MOE Singapore (RG121/23); Alibaba Group; Alibaba-NTU Global e-Sustainability CorpLab (ANGEL).
- **Source URL:** https://arxiv.org/abs/2602.23762
- **Full text:** https://arxiv.org/pdf/2602.23762v1
- **Sample period:** April 28, 2022 to March 31, 2025 (most specifications); March 17, 2023 to March 31, 2025 (specifications requiring $ARB data, which launched March 2023).
- **Universe:** On-chain assets from five major blockchains — Ethereum, Solana, Binance Smart Chain (BSC), Arbitrum, Avalanche — sourced via Coingecko on-chain DEX API.
- **Data frequency:** Half-day (12-hour) intervals in UTC.

## Economic mechanism

### Source-reported

Blockchains compete for users and capital. When one chain surges (e.g., a new protocol launch, airdrop, or hype event), investors attracted to that chain sell assets on rival chains to fund purchases on the surging chain. This creates negative return correlations across blockchains — the opposite of the positive co-movement typically seen in traditional equity markets during crises. The mechanism is analogous to international capital flight but within a crypto-native context where blockchains act as competing "nations" with their own native tokens serving as "domestic currencies."

### Research interpretation

The hypothesis is that **attention-induced capital substitution** is a systematic cross-chain phenomenon: when a chain experiences an attention shock (proxied by extreme returns or unexpected staking reward increases), capital flows *out* of rival chains, generating negative cross-chain return correlations. This is falsifiable via:

1. Measuring cross-chain return correlations conditional on attention proxies.
2. Testing whether the negative correlations persist after controlling for global macro factors and Bitcoin.
3. Testing whether the effect is stronger during extreme return episodes.

The mechanism is distinct from information-driven contagion (positive co-movement) because it relies on *limited investor attention* and *capital reallocation* rather than shared fundamental information. The paper's nonlinear factor models decompose returns into unconditional (baseline) and conditional (attention-dependent) components, finding that attention shocks amplify the negative spillover.

## Signal

The signal is the **attention shock on a rival chain** predicting a negative return on the home chain:

- **Formation timestamp:** Half-day t (12:00 UTC or 00:00 UTC).
- **Lookback:** Lagged returns (t-1) and contemporaneous rival chain activity variables.
- **Entry (research-proposed):** Short the home-chain portfolio when a rival chain experiences an extreme positive return (top 5% of the return distribution) or an unexpected staking reward increase.
- **Exit (research-proposed):** Close when the attention shock dissipates (rival chain return normalizes or extreme dummy turns off).
- **Parameters (from source):** Extreme return thresholds at 5th and 95th percentiles of the return distribution. Staking reward innovations extracted via ARIMA(p,d,q) models.
- **Position sizing:** Underspecified in source.
- **Holding period:** Half-day to multi-day (the paper measures at half-day frequency but does not specify optimal holding).
- **Re-entry rules:** Underspecified.

The signal is **not a fully specified trading strategy**. It identifies a persistent cross-chain correlation pattern. Operationalization for trading requires additional assumptions about entry/exit timing, position sizing, and cost treatment.

## Required data

- **Universe:** All actively traded assets on Ethereum, Solana, BSC, Arbitrum, Avalanche (DEX-only, excluding stablecoins, liquid staking tokens, wrapped native tokens).
- **Venue:** On-chain DEXs (Uniswap V3 and equivalents across chains); prices from Coingecko on-chain DEX API.
- **Market type:** Spot DEX.
- **Timeframe:** Half-day (12-hour) bars.
- **Fields:** Asset prices (denominated in chain native tokens), market capitalization, native token prices ($ETH, $SOL, $BNB, $ARB, $AVAX), staking reward rates, Bitcoin returns.
- **External controls:** S&P 500, FTSE 100, Hang Seng Index (half-day returns); HIBOR, EURIBOR, US 1-month T-bill (unexpected components via ARIMA).
- **Timestamp:** UTC half-day boundaries (00:00, 12:00).
- **Missing data:** Assets with missing price data excluded from portfolio construction; stablecoins, LST tokens, wrapped native tokens excluded by design.

## Execution assumptions

- **Signal-to-order timing:** Underspecified. The paper is an econometric study, not a backtest with execution simulation.
- **Fill model:** Not modeled.
- **Fees/spread/slippage:** Not modeled. The paper acknowledges that DEX execution involves gas fees, slippage, and MEV but does not include them in the analysis.
- **Leverage/margin:** Not modeled.
- **Capacity/liquidity:** Not assessed. The paper uses market-cap-weighted portfolios of all on-chain assets, which may include illiquid tokens.
- **Execution latency:** Not modeled.
- **Critical caveat:** The paper's econometric results (cross-chain correlations) are **not backtested as a trading strategy**. Any trading implementation would need to address DEX execution costs, gas fees, MEV, and liquidity constraints that the paper explicitly does not model.

## Evidence

### Source-reported

- **Negative spillover prevalence:** In baseline linear models (Table 3, Panel C, full sample), significant negative β coefficients found for multiple chain pairs. E.g., Ethereum–Arbitrum: β₃ = −0.140; Arbitrum–BSC: β₃ = −0.176; Arbitrum–Avalanche: β₄ = −0.160.
- **Effect strengthens with controls:** After adding global equity/rate controls (Table 4), negative spillovers become more pronounced. After adding chain-level activity variables (Table 5), some negative correlations are absorbed but many persist.
- **Nonlinear attention channel:** In nonlinear models with extreme return dummies (Table 8, Panel A), significant negative coefficients on extreme return dummies. E.g., Ethereum β₁₃ = −0.464 (Solana extreme up), β₃₃ = −0.901 (Arbitrum extreme up); BSC β₂₃ = −0.152, β₂₄ = −0.171 (Solana extremes). All significant at 1% level.
- **Asymmetry:** The effect is asymmetric — Ethereum investors sell when Solana/Arbitrum surge, but Solana investors do not exhibit reciprocal behavior when Ethereum surges. Arbitrum assets are particularly susceptible to outflows from attention shocks on other chains.
- **Short-term reversal:** Chain portfolio returns exhibit short-term reversal (negative α₁ across most specifications), consistent with the attention-driven overreaction/mean-reversion pattern.
- **This result has not been independently reproduced.**

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The paper acknowledges that some chain pairs show positive correlations (e.g., Arbitrum–Solana: β₂ = 0.028 in Panel C, Table 3), consistent with traditional contagion/rebalancing rather than negative spillover.
- The paper does not assess whether the negative spillover pattern is exploitable after DEX execution costs (gas fees, MEV, slippage).
- The paper does not test out-of-sample predictive performance or walk-forward validation of the correlation pattern.
- The 5% extreme return threshold is arbitrary; sensitivity to this choice is not tested.

## Falsification plan

1. **Out-of-sample test:** Reserve the last 6 months (October 2024–March 2025) as an out-of-sample period and test whether the negative spillover coefficients hold.
2. **Alternative threshold sensitivity:** Test extreme return thresholds at 1%, 10%, and 20% instead of 5%.
3. **Walk-forward validation:** Split the sample into rolling windows and test whether the negative spillover is stable across sub-periods.
4. **Cost stress test:** Implement a simple trading strategy (short home-chain portfolio on rival-chain extreme up) with realistic DEX execution costs (gas, slippage, MEV) and test whether the gross edge survives.
5. **Alternative chain selection:** Test whether the pattern holds for additional chains (e.g., Base, Polygon, Optimism) not included in the original study.
6. **Regime breakdown:** Test whether the negative spillover persists across bull, bear, and sideways market regimes.
7. **Failure threshold:** If the negative spillover coefficient is insignificant or positive in >50% of out-of-sample half-days, the hypothesis is weakened.

## Crypto portability

**direct**

The paper is already crypto-native, studying on-chain DEX assets across five blockchains. The mechanism (attention-driven capital reallocation across competing blockchains) is inherently a crypto phenomenon with no traditional-finance analogue.

Crypto-specific portability considerations:
- **Spot DEX only:** The study uses on-chain spot prices. Perpetual futures and CEX spot are not studied.
- **24/7 markets:** The half-day frequency aligns with UTC session boundaries but does not capture intraday dynamics.
- **Gas fees:** Not modeled. A trading strategy would need to account for gas costs, which vary by chain and congestion.
- **MEV:** Not modeled. Adverse selection from MEV bots could erode any exploitable signal.
- **Liquidity fragmentation:** DEX liquidity is fragmented across pools; the paper uses the largest pool per asset but does not assess fill quality.
- **Chain-specific risks:** Bridging, smart contract risk, and oracle manipulation are not addressed.
- **Mark/index price:** Not applicable for DEX spot.

## Limitations

- **Not a backtest:** The paper is an econometric study of cross-chain return correlations. It does not implement, backtest, or simulate a trading strategy.
- **No transaction cost model:** DEX execution costs (gas, slippage, MEV) are explicitly not modeled.
- **Data limitations:** The paper relies on Coingecko on-chain DEX API data, which may have gaps or inconsistencies for less liquid tokens.
- **Sample period:** April 2022–March 2025 covers a specific market cycle; the pattern may not persist across regimes.
- **Asymmetric effects:** The negative spillover is asymmetric — not all chain pairs exhibit it, and the magnitude varies substantially.
- **Extreme return threshold:** The 5% threshold is arbitrary and not optimized.
- **No predictive test:** The paper documents correlation patterns but does not test whether rival-chain extreme returns *predict* future home-chain returns in a trading-relevant sense.
- **Portfolio construction:** Market-cap-weighted portfolios of all on-chain assets may include very illiquid tokens, potentially inflating measured correlations.
- **Latency of on-chain data:** The paper uses half-day frequency, which smooths intraday dynamics that may be critical for a trading strategy.

## Implementation status

Not implemented. The paper is a pure econometric study with no backtest, strategy simulation, or execution framework.

## Adoption boundary

This record is research material only. The cross-chain negative spillover pattern has been documented but not validated as a tradeable signal. Any implementation would require:
- A cost-aware backtest on realistic DEX execution data.
- Walk-forward out-of-sample validation.
- Assessment of capacity and liquidity constraints.
- MEV and gas cost modeling.

## Related Wiki records

- No directly related records identified. The cross-chain spillover mechanism is novel to this repository.

## Sources

1. Mengzhong Ma, Te Bao, Yonggang Wen, *"One Rising Ship Sinks Other Ships: Cross-Chain Negative Spillovers in Crypto Markets"*, arXiv:2602.23762v1 [q-fin.PR], February 27, 2026. https://arxiv.org/abs/2602.23762.
2. Full paper text including all tables and figures: https://arxiv.org/pdf/2602.23762v1.
