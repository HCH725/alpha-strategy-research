---
schema: strategy-research-record-v1
title: "Retail Crypto Microstructure Signal Falsification: Order Flow, CVD Divergence, Funding Fade, and Pattern-Based Edge Null After Costs"
created: 2026-09-11
updated: 2026-09-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - null-result
  - negative-evidence
  - microstructure
  - order-flow
  - funding-rate
  - cvd-divergence
  - retail
  - perpetual-futures
status: research-only
confidence: high
source_as_of: 2026-06-26
sources:
  - "https://github.com/Mykola-Quant/retail-crypto-alpha (commit 417490bb6bd2d61a987dd11ac30eea1bcb0f6b97, 2026-06-26)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Retail Crypto Microstructure Signal Falsification: Order Flow, CVD Divergence, Funding Fade, and Pattern-Based Edge Null After Costs

## Provenance

- Repository: https://github.com/Mykola-Quant/retail-crypto-alpha
- Full commit SHA: 417490bb6bd2d61a987dd11ac30eea1bcb0f6b97
- Research report: https://github.com/Mykola-Quant/retail-crypto-alpha/blob/main/research_report.md
- Author: Mykola (Mykola-Quant)
- Date: 2026-06-26 (latest commit to research report)
- Study period: 2023–2026 (funding rate); March–June 2026 (tick data); 2018–2026 (risk overlays)
- This is a GitHub-hosted negative-results study with full code, data collectors, and reproducible backtesting framework. It is not peer-reviewed but provides complete methodology and independently runnable scripts.

## Economic mechanism

### Source-reported

This is a **negative-results study** — it does not propose an alpha strategy but systematically falsifies several retail-accessible microstructure signal families in crypto. The author built a complete research pipeline (live WebSocket collectors, tick-data ingestion, backtesting framework) and tested the following signal families under strict pre-specified hypotheses, train/test splits, realistic costs (~0.13% round-trip), and multiple-testing controls:

1. **Intraday order-flow momentum and absorption** (one-minute CVD on ~18.8M trades)
2. **Liquidation cascades conditioned on open interest** (34 cascade events)
3. **OHLCV patterns**: liquidity sweeps, session-open bias, CME gap fills (BTC, ETH, SOL)
4. **Spot–perpetual CVD divergence** (~111M spot + ~181M perpetual trades, hourly)
5. **Funding-rate z-score mean reversion** (3.5 years, ~3,800 funding intervals)
6. **Absorption as context filter** (drift-aware permutation test)
7. **Opening FVGs and calendar effects** (five assets: BTC, ETH, SOL, gold, oil)

Headline finding: **no signal produced a tradeable edge after costs at intraday-to-daily horizons**. The gross predictable price move was roughly an order of magnitude smaller than the round-trip cost of capturing it.

### Research interpretation

The null finding is structural, not a tuning failure. At intraday-to-daily horizons, the predictable component of crypto returns available to retail traders using public data is dominated by transaction costs. This constrains the feasible alpha frontier for retail-accessible microstructure signals and provides a calibration baseline: any proposed signal must demonstrate predictive power substantially larger than ~0.13% per round-trip to be economically meaningful.

The study also found that **risk-management overlays (volatility targeting + trend filter) do not create alpha but reliably reshape risk**: on Bitcoin, they cut maximum drawdown from ~−83% to ~−29% at roughly unchanged Sharpe ratio (~0.66 to ~0.69). On Ethereum, the overlay genuinely improved risk-adjusted return (Sharpe ~0.55 to ~0.77).

## Signal

No actionable signal is proposed. This is a null-result record documenting the failure of the following signal families to produce edge after costs:

### 4.1 Order-flow momentum and absorption
- **Hypothesis**: One-minute CVD imbalance predicts next few minutes (momentum or absorption reversal)
- **Method**: ~18.8M trades → one-minute bars → CVD → aggressive-buy/sell momentum + absorption signals → net returns after 0.13% cost at 1/3/5/10 bar horizons; 70/30 train/test split
- **Result**: Median absolute move at +1 bar ≈ 0.024%; cost ≈ 0.13%. Every signal direction lost decisively. Training: −0.13% to −0.15% net, win rates 1–16%, t ≈ −7 to −19. Test: −0.10% to −0.13% net, t ≈ −3 to −6
- **Verdict**: No tradeable edge. Gross move 7–10× smaller than cost

### 4.2 Liquidation cascades + open interest
- **Hypothesis**: Forced liquidations clear one side; conditioning on OI change sharpens signal
- **Method**: 34 cascade events in live window; excess move + net return after costs at 1/5/15/30/60 min
- **Result**: Almost every cell |t| < 2. One cell (buy-cascade + rising OI at +1 min): +0.16% excess, 100% up-rate, t = +2.76, but n = 8 (below n ≥ 30 gate), did not persist at longer horizons
- **Verdict**: No robust edge. Single suggestive cell is a small-sample, regime-locked artifact consistent with multiple testing

### 4.3 OHLCV patterns (sweeps, session bias, gap fills)
- **Hypothesis**: Three popular retail setups predict short-timeframe returns
- **Method**: Mechanized rules on 1- and 3-min bars across BTC, ETH, SOL futures
- **Result**: None produced positive net expectancy after costs
- **Verdict**: No edge

### 4.4 Spot–perpetual CVD divergence
- **Hypothesis**: Cross-market CVD disagreement predicts resolution direction
- **Method**: Hourly CVD on spot (~111M trades) and perpetual (~181M trades), March–June 2026
- **Result**: Weakly positive on training split (not significant); significantly negative on test split. Sign reversed OOS.
- **Verdict**: No edge. Sign flip = noise fitted in-sample

### 4.5 Funding-rate z-score mean reversion
- **Hypothesis**: Extreme funding rates signal crowded positioning; fading earns mean-reversion premium
- **Method**: 3.5 years of funding history (2023–2026, ~3,800 intervals); z-score thresholds 1.7σ and 2.3σ; train/test split
- **Result**: Null over full sample. Training returns flat; test split weakly negative. No significant positive edge at either threshold.
- **Verdict**: No edge

### 4.6 Absorption as context filter
- **Hypothesis**: Absorption may add value as a conditional filter (not standalone signal)
- **Method**: Drift-aware permutation test on both perpetual and spot tapes
- **Result**: Null on both venues. Absorption-flagged bars indistinguishable from random bars after drift removal.
- **Verdict**: No edge

### 4.7 Opening FVGs and calendar effects
- **Hypothesis**: Unmitigated opening gaps set day direction; intraday momentum; day-of-week effects
- **Method**: Five assets (BTC, ETH, SOL, gold, oil), 5-min bars; opening-gap unmitigated rate vs. midday control; calendar effects on 2025–2026 extended sample
- **Result**: Unmitigated rates 20–36% (not ~80% as claimed). Every tradable version lost after costs. Day-of-week effect vanished on extended sample (n = 76 Mondays, all t-tests p > 0.4).
- **Verdict**: No edge. Apparent cross-asset consistency on small sample was shared regime, not repeatable edge

## Required data

- **Universe**: BTC, ETH, SOL (perpetual futures, Binance USD-M); gold (PAXG); oil
- **Venue**: Binance (primary)
- **Market type**: USD-M perpetual futures; spot (for CVD divergence)
- **Timeframe**: One-minute and five-minute bars (signal tests); daily bars (risk overlays)
- **Fields**: Aggressive trades (tick tape), cumulative volume delta, liquidation events, open interest, funding rate, OHLCV
- **Period**: March–June 2026 (tick data); 2023–2026 (funding rate); 2018–2026 (risk overlays)
- **Data source**: Binance WebSocket streams (live); Binance public archives (data.binance.vision)

## Execution assumptions

- **Round-trip cost**: ~0.13% (taker fees + slippage) applied to every position change
- **Fill model**: Not explicitly modeled beyond cost; no slippage model beyond the flat 0.13% assumption
- **Execution timing**: Next-bar execution (causal features, shifted signals)
- **Minimum sample gate**: n ≥ 30 per cell before interpretation
- **Multiple-testing control**: Tracked configuration count; single significant cells among many treated as noise
- **Cost sensitivity**: The central finding is that gross moves are 7–10× smaller than costs — a decisive gap, not marginal

## Evidence

### Source-reported

- Across 13+ configurations on 5 assets, no signal produced tradeable edge after realistic costs
- Order-flow momentum: gross move ~0.024% vs. cost ~0.13% (7–10× gap)
- Liquidation cascades: 34 events, no cell cleared both n ≥ 30 and |t| > 2 robustly
- CVD divergence: sign flip between train and test
- Funding-rate fade: null over 3.5 years at both 1.7σ and 2.3σ thresholds
- Calendar effects: day-of-week anomaly vanished on extended sample (p > 0.4 on all assets)
- Risk overlays: VT + trend filter cut BTC MDD from ~−83% to ~−29% at similar Sharpe; ETH Sharpe improved from ~0.55 to ~0.77

### Independently reproduced

Not independently reproduced.

### Negative evidence

This entire record IS negative evidence. The study's core contribution is systematically falsifying retail-accessible microstructure signal families in crypto. The null finding is reinforced by:
- Consistency across independent data sources (spot and perpetual tapes agree on absorption null)
- Consistency across five assets (BTC, ETH, SOL, gold, oil)
- Strict methodology: pre-specified hypotheses, train/test splits, cost modeling, multiple-testing controls
- Structural explanation: predictable moves are an order of magnitude smaller than costs at retail horizons

## Falsification plan

This record itself is a falsification of the hypothesis that retail-accessible microstructure signals produce reliable alpha in crypto. To falsify this null:

1. A signal must demonstrate gross predictive power substantially exceeding ~0.13% per round-trip (research-proposed threshold)
2. Must survive train/test split with parameters fit only on training data
3. Must hold across at least two independent data sources or assets
4. Must survive multiple-testing correction for the number of configurations examined
5. Must be tested on sample sizes ≥ 30 per cell
6. The Castellanos Macias (2026, SSRN 7085378) adversarial audit framework provides a complementary falsification standard

## Crypto portability

direct — this study is already conducted on crypto perpetual futures and spot markets.

## Limitations

- **GitHub-hosted, not peer-reviewed**: the study is rigorous but has not undergone formal peer review
- **Retail-level execution**: institutional strategies with better execution, lower fees, or proprietary data may achieve different results
- **Specific venue**: primarily Binance; results may differ on venues with different fee structures or market microstructure
- **Cost model**: flat 0.13% round-trip does not model impact, partial fills, or regime-dependent slippage
- **Horizon-specific**: null finding is for intraday-to-daily horizons; longer-horizon or cross-sectional signals are not tested
- **Sample period**: tick data covers March–June 2026 (short); funding rate covers 2023–2026 (longer)
- The null result does not prove alpha is impossible — only that the specific signals tested under the specific conditions tested did not survive

## Implementation status

Not implemented. This is a null-result record — no strategy to implement.

## Adoption boundary

This record is research material only. Its presence in this repository does not mean:

- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

The finding is that the tested strategies were NOT profitable after costs.

## Related Wiki records

- [[crypto-retail-systematic-trading-null-result-adversarial-audit-2026-09-01]] (complementary null result: Castellanos Macias 2026, SSRN 7085378, 18 experiment families over 2018–2026)
- [[crypto-public-wallet-identity-trader-informativeness-adverse-selection-2026-09-02]] (related: wallet-level identity as alpha source on Hyperliquid)
- [[crypto-l2-liquidity-state-transitions-order-flow-2026-09-01]] (related: L2 state as first-order predictor; order flow as conditional overlay)

## Sources

1. Mykola-Quant. "Retail Crypto Alpha: A Negative-Results Study." GitHub repository, commit 417490bb6bd2d61a987dd11ac30eea1bcb0f6b97, 2026-06-26. https://github.com/Mykola-Quant/retail-crypto-alpha
2. Research report: https://github.com/Mykola-Quant/retail-crypto-alpha/blob/main/research_report.md
