---
schema: strategy-research-record-v1
title: "Cross-Sectional Intraday Alpha in Crypto Perpetual Futures: Leakage-Safe Factor Mining with Cost Rejection"
created: 2026-09-14
updated: 2026-09-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - cross-sectional
  - intraday
  - microstructure
  - factor-mining
  - leakage-safe
  - negative-result
status: research-only
confidence: high
source_as_of: 2026-07-16
sources:
  - "Luqman Akasyah, 'Intraday Alpha Research Lab: Leakage-safe cross-sectional intraday futures alpha research with walk-forward testing and explicit cost rejection', GitHub repository, commit a140e9f9da25a34af4932f3083343625bb14adb5, July 16 2026. https://github.com/luqmanakasyah/intraday-alpha-research-lab"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - Source reports statistically detectable out-of-sample rank IC (0.047 pooled, 0.0496 for strongest factor), but the gross edge does not survive baseline transaction costs. The study explicitly rejects executable alpha.
---

# Cross-Sectional Intraday Alpha in Crypto Perpetual Futures: Leakage-Safe Factor Mining with Cost Rejection

## Provenance

Primary source: Luqman Akasyah, "Intraday Alpha Research Lab," GitHub repository, commit `a140e9f9da25a34af4932f3083343625bb14adb5` (July 16, 2026). The repository is a research demonstrator with a complete, reproducible pipeline: data collection, factor construction, leakage-controlled inference, walk-forward modelling, portfolio construction, turnover analysis, and explicit cost sensitivity.

The study covers 12 USD-M perpetual-futures contracts on Binance (ADA, AVAX, BCH, BNB, BTC, DOGE, DOT, ETH, LINK, LTC, SOL, XRP) over 2026-03-18 to 2026-07-16 (120 days, 138,240 complete 15-minute bars, 11,520 bars per symbol).

Source-reported data: Binance USD-M perpetual-futures public klines (15-minute OHLCV + volume). The study uses the close of each 15-minute bar as the decision timestamp and the next bar's open as the execution proxy.

## Economic mechanism

### Source-reported

The study tests whether cross-sectional factor signals—reversal, momentum, realized volatility, volume shock, range, and taker-buy imbalance—can predict next-period returns across a universe of crypto perpetual futures after proper leakage controls and cost accounting. The economic hypothesis is that cross-sectional ranking by these factors captures persistent return predictability arising from heterogeneous trader behavior, liquidity provision, and information asymmetry in 24/7 crypto markets.

### Research interpretation

The strongest signal is short-horizon reversal: the rank reversal factor (previous 1-bar return rank) has positive IC at 1-, 4-, and 12-bar horizons (mean rank IC of 0.0496 at 1-bar, 0.0377 at 4-bar, 0.0333 at 12-bar). Momentum factors are correspondingly negatively correlated with forward returns (rank IC of -0.0408 to -0.0480). This is consistent with compensated liquidity provision at the 15-minute frequency: assets that experienced strong recent moves tend to partially reverse, and this reversal is cross-sectionally predictable.

The mechanism is hypothesized to be liquidity provision compensating short-horizon overreaction, similar to the single-coin mean reversion documented by Kitron & Wengrowicz (2026, arXiv:2608.21888). However, the critical finding is that the cross-sectional signal, while statistically detectable, does not survive realistic transaction costs.

## Signal

### Formation timestamp

Decision time: after each 15-minute bar closes. Execution proxy: immediate next 15-minute bar open.

### Lookback

- rank_reversal_1: 1-bar (15-minute) return rank
- rank_momentum_4: 4-bar (1-hour) return rank
- rank_momentum_16: 16-bar (4-hour) return rank
- rank_realized_vol: realized volatility over rolling window (underspecified in source; exact window not stated in the JSON)
- rank_volume_shock: volume deviation from recent average (underspecified)
- rank_range: high-low range rank (underspecified)
- rank_taker_buy_imbalance: taker-buy volume share rank (underspecified)

All factors are converted to cross-sectional ranks within each 15-minute bar.

### Entry

Top-2 long / bottom-2 short, dollar-neutral portfolio (0.5 long + 0.5 short), one-hour rebalance cadence.

### Exit

One-hour rebalance (4-bar holding period). Rank-4 retention buffer prevents unnecessary turnover.

### Parameters

- Model: pooled Ridge regression with alpha=1.0 (fixed, not tuned)
- Validation: purged expanding-window walk-forward, 9 folds, 1,434 out-of-sample decisions, 1-decision purge
- Inference: moving-block bootstrap (block size not specified in excerpt) + Benjamini-Hochberg FDR correction across 21 factor-horizon tests

### Source-reported performance

- Out-of-sample Ridge rank IC (pooled across factors): **0.0471** (95% moving-block CI [0.0314, 0.0620])
- Strongest single factor (rank_reversal_1 at 1-bar): mean rank IC **0.0496** (95% CI [0.0422, 0.0584], q-value 0.0028)
- Gross portfolio return: **15.4%** over the sample
- Break-even one-way cost: **0.97 bps**
- Net return at 2.0 bps one-way cost: **-14.6%**

Source reports: "The model identifies a positive out-of-sample association within this sample, but the portfolio turns over too quickly."

### Independence

Not independently reproduced.

## Required data

- Instrument: 12 Binance USD-M perpetual-futures contracts (ADA, AVAX, BCH, BNB, BTC, DOGE, DOT, ETH, LINK, LTC, SOL, XRP)
- Venue: Binance (spot klines, not order-book data)
- Market type: USDT-margined perpetual futures
- Timeframe: 15-minute bars
- Fields: OHLCV + volume (taker-buy volume implied by taker_buy_imbalance factor, but exact construction underspecified)
- Point-in-time: public Binance klines, no look-ahead concerns
- Timestamp: UTC (implied by Binance API conventions)
- Missing-data: complete bars only (11,520 bars per symbol); no imputation stated

## Execution assumptions

- Signal-to-order timing: decision at bar close, execution at next bar open (1-bar delay)
- Fill model: next-bar open (immediate)
- Fees: variable (tested at 0, 0.5, 1.0, 2.0, 5.0 bps one-way)
- Slippage: not explicitly modeled beyond the next-bar-open proxy
- Spread: not modeled
- Impact: not modeled
- Funding: not modeled
- Leverage: not stated
- Capacity: not assessed; the study uses a 12-asset universe with daily volume sufficient for the tested notional

Source states: "Queue position, spread, market impact, funding or order-book execution" are not included.

## Evidence

### Source-reported

The study is a negative-result research demonstrator. Source-reported headline findings:

| One-way cost (bps) | Net return | Annualised Sharpe | Max drawdown |
|---|---|---|---|
| 0.0 | 15.4% | 4.46 | -4.5% |
| 0.5 | 7.1% | 2.17 | -5.7% |
| 1.0 | -0.7% | -0.12 | -6.9% |
| 2.0 | -14.6% | -4.70 | -16.1% |
| 5.0 | -45.7% | -18.33 | -46.4% |

Sharpe is mechanically annualised from hourly research returns and is not presented as live-performance evidence.

Factor evidence: the strongest pattern is short-horizon reversal (`rank_reversal_1` has positive IC at 1-, 4-, and 12-bar horizons). Momentum coefficients are correspondingly negative. Volume shock does not survive FDR.

Source conclusion: "Statistically detectable, but not executable after baseline costs."

### Independently reproduced

Not independently reproduced.

### Negative evidence

The study IS the negative evidence. Key negative findings:

1. The break-even one-way cost (0.97 bps) is below realistic taker fees on most perpetual-futures venues (typically 2-5 bps taker, 0-2 bps maker).
2. The signal does not survive even at 1.0 bps one-way cost (-0.7% net return).
3. The study explicitly rejects executable alpha at baseline cost.
4. The sample is 120 days on 12 assets—a short window that limits regime coverage.

## Falsification plan

1. **Extended sample**: Replicate on a later untouched period (source recommends this as the next step).
2. **Cost sensitivity**: The study already performs cost sensitivity; the break-even at 0.97 bps is the falsification threshold for any cost-aware implementation.
3. **Universe expansion**: Test on a larger universe (50+ perpetuals) to assess whether the signal concentrates in less liquid names where costs are higher.
4. **Execution model upgrade**: Replace next-bar-open proxy with a more realistic fill model incorporating spread, queue position, and market impact.
5. **Regime breakdown**: Assess whether the reversal signal persists across bull, bear, and range-bound regimes within the 120-day window.
6. **Turnover reduction**: Test whether the signal survives with longer rebalance cadences (e.g., 2-hour, 4-hour) that reduce turnover at the cost of signal decay.

Research-defined falsification threshold: net Sharpe > 0 at 2.0 bps one-way cost (research-defined, not source-specified).

## Crypto portability

direct

The study is natively conducted on crypto perpetual futures. The universe, venue, and instrument type are crypto-native.

## Limitations

- **Short sample**: 120 days (March-July 2026) on a single market phase. Not representative of bear or high-volatility regimes.
- **Small universe**: 12 assets only. Cross-sectional power is limited.
- **Retail cost assumptions**: The break-even at 0.97 bps assumes no maker rebate. Maker-level execution could potentially change the conclusion.
- **No order-book data**: The study uses klines, not order-book depth or trade-level data. Richer microstructure features might improve the signal.
- **Not independently reproduced**: The study is a single research demonstrator.
- **Source is a GitHub repo, not a peer-reviewed paper**: The methodology is rigorous but not peer-reviewed.
- **Signal decay not assessed**: The 120-day window is too short to assess whether the reversal signal decays over time.
- **data gap**: Exact factor construction details for volatility, volume shock, range, and taker-buy imbalance factors are underspecified in the published JSON; the code repository may contain full specifications.

## Implementation status

Not implemented. The source is a research demonstrator that explicitly rejects executable alpha.

## Adoption boundary

This record represents research material only. The source explicitly states: "This is a research demonstrator, not investment advice, a live-trading record or a claim of profitable alpha."

A record being present in this repository does NOT mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet trading
- approved for live trading

## Related Wiki records

- [[quant/strategy-research-record-spec-v1]] (schema specification)
- [[quant/crypto-short-horizon-15min-mean-reversion-taker-flow-2026-09-01]] (related study on single-coin 15-minute mean reversion with taker flow conditioning; different mechanism and scope but overlapping signal family)
- [[quant/crypto-intraday-sign-mean-reversion-15m-walk-forward-2026-09-01]] (related study on sign-based mean reversion at 15-minute horizon; same signal family, different approach)

## Sources

1. Luqman Akasyah, "Intraday Alpha Research Lab: Leakage-safe cross-sectional intraday futures alpha research with walk-forward testing and explicit cost rejection," GitHub repository, commit `a140e9f9da25a34af4932f3083343625bb14adb5` (July 16, 2026). https://github.com/luqmanakasyah/intraday-alpha-research-lab
2. Source-reported factor-level results: `artifacts/research-results.json` in the repository.
