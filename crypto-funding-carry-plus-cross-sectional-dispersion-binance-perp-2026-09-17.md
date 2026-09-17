---
schema: strategy-research-record-v1
title: "Funding-Rate Carry plus Cross-Sectional Funding Dispersion: Delta-Neutral Perpetual Arbitrage on Binance"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - funding-rate
  - carry
  - dispersion
  - delta-neutral
  - perpetual-futures
  - binance
status: research-only
confidence: medium
source_as_of: 2026-05-09
sources:
  - "https://github.com/KaranChavan21/crypto-funding-rate-arbitrage (commit 507d0f5815c8c7339b4ee6c4a13a2ed422466f27, 2026-05-09)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Funding-Rate Carry plus Cross-Sectional Funding Dispersion: Delta-Neutral Perpetual Arbitrage on Binance

## Provenance

- **Repository:** KaranChavan21/crypto-funding-rate-arbitrage
- **Repository URL:** https://github.com/KaranChavan21/crypto-funding-rate-arbitrage
- **Commit SHA:** `507d0f5815c8c7339b4ee6c4a13a2ed422466f27` (single initial commit, 2026-05-09)
- **Author:** KaranChavan21 (GitHub handle; no real name disclosed)
- **Core signal logic, parameter values, and live execution code are withheld** from the repository; only documentation and result artifacts are public.
- **Deduplication audit:** Searched all existing `*.md` records for `KaranChavan21`, `funding-rate-arbitrage`, `carry plus dispersion`, and `cross-sectional funding dispersion`. No exact source identity match found. Adjacent records in this repo cover:
  - `crypto-hyperliquid-momentum-funding-carry-combo-2026-09-12.md` — Keel Research momentum + funding on Hyperliquid (different venue, different mechanism: momentum + carry vs carry + dispersion)
  - `crypto-perp-funding-zscore-carry-cross-exchange-macro-gate-2026-09-13.md` — cross-exchange funding z-score carry with macro gate (cross-exchange, not intra-venue dispersion)
  - `crypto-cex-dex-cross-venue-funding-spread-carry-2026-08-31.md` — CEX-DEX funding spread carry (cross-venue, not cross-asset dispersion)
  - `funding-rate-carry-falsification` (Mykola-Quant) — single-leg funding carry falsified on BTC/ETH/SOL (different mechanism; this record combines carry + dispersion)
  - `crypto-two-tiered-cex-dominant-funding-discovery-structural-arbitrage-2026-09-12.md` — two-tiered funding market structure analysis (different study)
  The combination of **intra-Binance carry + cross-asset funding dispersion** with walk-forward embargo validation is materially distinct from all captured records.

## Economic mechanism

### Source-reported

The strategy exploits a structurally persistent inefficiency in perpetual-futures markets: funding-rate payments. Two complementary sub-strategies are combined:

- **Strategy A (Funding-rate carry):** Classic crypto basis trade — long spot, short perpetual — capturing the absolute level of 8-hour funding payments when rates are persistently positive.
- **Strategy C (Funding-rate dispersion):** Cross-sectional trade — long basis (long spot, short perp) on high-funding coins and short basis (short spot, long perp) on low/negative-funding coins — capturing the spread between the highest and lowest funding-rate coins rather than the absolute level.

The author states that Strategy A profits when funding levels are absolutely high, while Strategy C profits when funding dispersion across coins is wide. The two regimes are claimed to be imperfectly correlated (source-reported daily correlation between A and C: +0.18), providing regime-orthogonality: when one compresses, the other typically still earns.

### Research interpretation

The hypothesis is that the cross-sectional funding-rate distribution across crypto perpetuals carries exploitable dispersion even when the unconditional mean funding level is low. The carry component captures the unconditional positive drift in funding rates (longs paying shorts in a structurally bullish market), while the dispersion component captures a cross-sectional arbitrage: the spread between the richest and cheapest funding rates across coins is wider than the cost of harvesting it. This is a combined time-series carry + cross-sectional relative-value trade within a single asset class.

The mechanism depends on:
1. Funding rates being sufficiently volatile across coins to sustain a cross-sectional spread.
2. The spread being wider than the round-trip execution costs (perp taker fees + spot taker fees + borrow + funding accrual timing).
3. The two sub-strategies having low enough correlation to provide diversification benefit.

## Signal

### Strategy A — Funding-rate carry (source-reported, detail withheld)

- **Entry:** Long spot + short perpetual on coins with persistently positive funding rates.
- **Exit:** Position unwinding or rebalancing per walk-forward-validated rules (exact parameters withheld).
- **Parameters:** Withheld.
- **Rebalance:** Walk-forward-validated rules (exact frequency withheld).

### Strategy C — Funding-rate dispersion (source-reported, detail withheld)

- **Entry:** Long basis on highest-funding coins + short basis on lowest/negative-funding coins simultaneously.
- **Exit:** Rebalancing per walk-forward-validated rules.
- **Parameters:** Withheld.
- **Universe:** Liquid USDT-margined Binance perpetual futures. Cross-sectional liquidity filtering to exclude stale-spot artifacts on illiquid altcoins.

### Combined portfolio

- Both strategies run continuously, blended (exact weighting withheld).
- **Holding period:** Continuous/overlapping positions, rebalanced per walk-forward-validated rules.
- **Position sizing:** Inverse-volatility weighting and per-strategy risk budgeting (research-proposed: the author mentions this as the intended allocation method but exact implementation is withheld).

**Note:** The core signal logic, parameter values, threshold values, lookback windows, and position sizing rules are explicitly withheld from the repository. This record describes the strategy at the conceptual level only. Reproduction is not possible from the public documentation alone.

## Required data

- **Instrument:** USDT-margined perpetual futures on Binance (130 symbols at time of backtest).
- **Universe:** Liquid Binance perpetual futures. Cross-sectional liquidity filtering applied to exclude illiquid altcoins with stale spot prices.
- **Venue:** Binance Futures (both spot and perpetual legs).
- **Market type:** Perpetual futures + spot.
- **Timeframe:** 8-hour funding settlement periods; hourly bars used for backtesting.
- **Fields:** OHLCV (hourly), funding rates (8-hour), open interest, long/short ratios, taker buy/sell volume.
- **Data source (backtest):** Binance Vision (klines, funding rates, open interest, long/short ratios).
- **Point-in-time:** Walk-forward validation with non-overlapping OOS windows and time-aware embargo.
- **Missing-data:** Stale-spot artifacts on illiquid coins explicitly filtered (the author notes this is a "common but rarely-discussed source of fake backtest profits").

## Execution assumptions

- **Signal-to-order timing:** Not specified (withheld).
- **Fill model:** Not specified (withheld).
- **Order type:** Not specified (withheld).
- **Fees:** Perpetual taker fees + spot taker fees included in cost model (exact rate withheld but described as realistic Binance taker fees).
- **Slippage:** Not explicitly stated as a separate line item; the cost model includes "perpetual taker fees" and "spot taker fees" but does not separately enumerate slippage.
- **Funding payments:** Explicitly modeled at every 8-hour mark.
- **Spot borrow rate:** Worst-case stressed borrow rate for short-basis legs included.
- **Capital opportunity cost:** USDT lending rate proxy included.
- **Leverage:** Not specified (withheld). Delta-neutral implies 1:1 long/short dollar amounts.
- **Capacity:** Not discussed. The author mentions "low-latency to Binance" VPS infrastructure for production, suggesting the strategy may have capacity constraints.

## Evidence

### Source-reported

All performance metrics below are from the repository's documentation, covering the out-of-sample period 2023-05 to 2026-04 (36 months):

| Metric | Value |
|---|---|
| Sharpe Ratio (OOS) | 3.37 |
| Annual Return | +12.55% |
| Max Drawdown | −1.35% |
| Calmar Ratio | 9.30 |
| Positive Months | 36 / 36 |

- Source reports Sharpe 3.37, annual return +12.55%, max drawdown −1.35%, and 36/36 positive months over the stated OOS window. This result has not been independently reproduced.
- Source reports daily correlation between Strategy A and Strategy C of +0.18.
- Source reports annualized funding yields ranging from −10% to +30% depending on conditions, with sustained positive funding of 8–15% annualized common during bull markets.
- Source reports the cross-sectional funding spread between top and bottom coins remained 8–15% even when average funding collapsed to 2–4% annualized in 2025.
- **Research funnel:** Of 10 strategy candidates tested, 6 were declared dead (failed walk-forward), 2 were marginal, and 2 were deployed. Rejected strategies include cross-sectional price momentum, BTC/ETH cointegration, open interest × funding combo, long/short ratio contrarian, top-trader positioning follow, and trend-following with adaptive stops.
- **ML ablation:** A LightGBM regressor trained on smoothed funding history, realized volatility, OI dynamics, long/short positioning, taker imbalance, and BTC regime to predict forward per-coin carry edge **failed to beat simple cross-sectional rank** out-of-sample. The author interprets this as evidence that smoothed funding rate is the sufficient statistic for cross-coin basis dispersion.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The author explicitly documents 6 of 10 candidate strategies that failed walk-forward validation. This is a form of publication of null/negative results within the repository.
- The ML model (LightGBM) failed to improve over simple cross-sectional rank, suggesting limited room for ML augmentation of the core signal.
- Source notes that funding levels compressed to 2–4% annualized in 2024–2025 after ETF approval and institutional arbitrage desk entry, making standalone carry (Strategy A) insufficient — motivating the dispersion component.
- Source states that the combination strategy continues to profit in the low-funding 2025 regime, but the absolute return is modest (+12.55% annual) and the strategy bears counterparty, execution, and funding-reversal risks.

## Falsification plan

1. **Walk-forward OOS replication:** Reproduce the 36-month walk-forward with non-overlapping OOS windows and time-aware embargo on the same Binance perpetual universe. Required sample: 2023-05 to 2026-04 minimum. Failure: OOS Sharpe below 1.5 or more than 3 negative months.
2. **Cost sensitivity:** Stress test with 2× and 3× taker fees, 5 bps slippage per leg, and realistic borrow rates. Failure: Strategy C (dispersion) becomes unprofitable at 2× costs.
3. **Regime decomposition:** Separate 2023 (high-funding), 2024 (mixed), and 2025–2026 (low-funding) regimes. Failure: Strategy A shows negative returns in the low-funding regime and Strategy C does not compensate.
4. **Per-symbol attribution:** Verify no single coin dominates returns. Failure: removing the top-3 contributors causes Sharpe to drop below 1.0.
5. **Funding-rate mean reversion test:** The dispersion component assumes funding spreads are transient and mean-revert. Falsification: if top-bottom funding spread persists in one direction for >48 hours without mean-reverting, the short-basis leg may face sustained losses.
6. **Capacity test:** Increase position sizes to determine at what AUM the strategy's edge degrades due to market impact on spot legs.
7. **Withheld-parameter sensitivity:** Since core parameters are withheld, any independent implementation must re-tune. Falsification: if the re-tuned version underperforms the simple cross-sectional rank baseline, the strategy's edge may be parameter-specific rather than structural.

## Crypto portability

**Adapted.** The strategy is designed specifically for crypto perpetual futures on Binance. Key portability considerations:

- **Spot-perp structure:** Requires both spot and perpetual contracts for the same asset on the same venue (or cross-venue with basis risk). Not all venues offer both.
- **Funding mechanism:** The 8-hour funding settlement is specific to crypto perpetuals. Traditional futures use different roll/convergence mechanisms.
- **Venue fragmentation:** The strategy is intra-venue (Binance). Cross-exchange variants face additional basis risk, execution risk, and capital fragmentation.
- **Liquidity:** The strategy depends on liquid perp books for the short-basis leg. Illiquid altcoins may have stale spot prices (the author explicitly filters these).
- **24/7 trading:** Funding settles every 8 hours around the clock, requiring continuous monitoring.
- **Counterparty risk:** Both legs are on the same venue; an exchange failure would affect both simultaneously.

## Limitations

- **Withheld signal logic:** Core signal logic, parameters, thresholds, lookback windows, and position sizing rules are explicitly withheld. The strategy cannot be independently reproduced from public documentation alone.
- **Single-author, single-repo:** Results are from a single author with no independent verification. The repository contains documentation and result artifacts only; no executable code is public.
- **Survivorship/selection bias risk:** The author tested 10 candidates and selected 2. Without pre-registration, the reported OOS results may reflect selection over the strategy design space.
- **Cost model gaps:** Slippage is not separately itemized from taker fees. Spot borrow rates are described as "worst-case stressed" but exact values are withheld. Capital opportunity cost is included but its exact calibration is withheld.
- **Capacity unaddressed:** No discussion of maximum deployable AUM, market impact on spot legs, or fill quality at scale.
- **Regime dependence:** The strategy's profitability depends on funding-rate dispersion across coins. If cross-exchange institutional arbitrage compresses funding spreads universally, the dispersion component may lose its edge.
- **Not independently reproduced.**
- **Core code withheld:** Reproduction requires re-derivation of all parameters from scratch.
- **data gap:** Exact fee rates, borrow rates, capital opportunity cost calibration, and rebalance frequency are not disclosed.
- **underspecified:** The walk-forward window size, embargo length, and number of OOS folds are described conceptually but not numerically specified.

## Implementation status

No implementation in our research stack. The repository itself describes a production stack as "frozen" and "ready for capital deployment" but does not provide executable code.

## Adoption boundary

This record is research material only. A record being present in this repository does not mean the strategy is profitable, validated alpha, approved for implementation, approved for paper trading, approved for testnet, or approved for live trading.

The source-reported Sharpe of 3.37 and 36/36 positive months are impressive but come from a single unverifiable backtest with withheld parameters. The strategy has not been independently reproduced or validated by any third party.

## Related Wiki records

- `[[crypto-cex-dex-cross-venue-funding-spread-carry-2026-08-31]]` — CEX-DEX funding spread carry (cross-venue, not intra-venue dispersion)
- `[[crypto-two-tiered-cex-dominant-funding-discovery-structural-arbitrage-2026-09-12]]` — Two-tiered funding market structure analysis
- `[[crypto-hyperliquid-momentum-funding-carry-combo-2026-09-12]]` — Momentum + funding on Hyperliquid (different mechanism)
- `[[crypto-perp-funding-zscore-carry-cross-exchange-macro-gate-2026-09-13]]` — Cross-exchange funding z-score carry (cross-exchange, not intra-venue dispersion)
- `[[crypto-futures-term-structure-roll-yield-carry-2026-08-31]]` — Futures term-structure roll yield carry (traditional futures carry, not funding-rate specific)

## Sources

1. KaranChavan21, "Crypto Funding-Anchored Quantitative Strategy," GitHub repository `KaranChavan21/crypto-funding-rate-arbitrage`, commit `507d0f5815c8c7339b4ee6c4a13a2ed422466f27`, created 2026-05-09. URL: https://github.com/KaranChavan21/crypto-funding-rate-arbitrage
