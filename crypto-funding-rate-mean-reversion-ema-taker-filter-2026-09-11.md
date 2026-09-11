---
schema: strategy-research-record-v1
title: "Crypto Perpetual Funding Rate Mean-Reversion with EMA Trend Filter and Taker-Volume Confirmation"
created: 2026-09-11
updated: 2026-09-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - funding-rate
  - mean-reversion
  - walk-forward
  - execution-cost-aware
status: research-only
confidence: medium
source_as_of: 2026-06-09
sources:
  - "https://github.com/Gotodataru/binance-futures-backtest"
  - "https://github.com/Gotodataru/binance-futures-backtest/blob/5ed0d6e39d8a3e951bea40c66e2638c213012e1b/strategy_1_funding_mr/signals.py"
  - "https://github.com/Gotodataru/binance-futures-backtest/blob/5ed0d6e39d8a3e951bea40c66e2638c213012e1b/shared/backtest_engine.py"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Perpetual Funding Rate Mean-Reversion with EMA Trend Filter and Taker-Volume Confirmation

## Provenance

- **Repository:** https://github.com/Gotodataru/binance-futures-backtest
- **Full Commit SHA:** `5ed0d6e39d8a3e951bea40c66e2638c213012e1b` (single-commit repo, "Initial release")
- **Relevant Files:**
  - `strategy_1_funding_mr/signals.py` — signal generation logic
  - `shared/backtest_engine.py` — walk-forward engine, execution model
  - `shared/data_loader.py` — data pipeline
  - `README.md` — strategy descriptions and OOS results
- **Data Source:** Local database ("BIGdatabaseBinance") of Binance USDⓈ-M perpetual futures data; 1-minute candles, 8-hour funding rates, 5-minute market metrics (open interest, taker buy/sell ratio, top trader long/short ratio). Not publicly distributed.
- **Data Period:** 2023–2026 (3 years), walk-forward validated.
- **Source Quality:** Public GitHub repository, 0 stars, 0 forks. Single author. Code-only source (no paper or blog post). The strategy and execution model are fully transparent in code.

## Economic mechanism

### Source-reported

The author states: "When funding rate is deeply negative (shorts overpaying) and price is below EMA — market is oversold → LONG. When funding rate is extremely high (longs overpaying) with price above EMA — market is overheated → SHORT." The economic rationale is that extreme funding rates indicate crowded positioning: when longs pay high funding, the crowd is leveraged long and vulnerable to a correction; when shorts pay negative funding, the crowd is leveraged short and vulnerable to a squeeze.

### Research interpretation

The hypothesis is that funding-rate extremes on crypto perpetual futures reflect crowded positioning that tends to mean-revert. The mechanism is:

- **Primary signal:** Funding-rate extreme → crowding indicator → contrarian entry.
- **Trend filter (EMA):** Avoids entering against strong trends; longs only when price is below EMA (pullback entry), shorts only when price is above EMA (rally entry).
- **Confirmation filter (taker buy ratio):** Taker buy volume ratio provides flow-based confirmation of directional pressure.

This is a mean-reversion hypothesis: extreme funding → crowded positioning → reversal. The EMA filter makes it a pullback/rally mean-reversion rather than pure contrarian.

## Signal

**Formation timestamp:** Signal forms at the close of bar t. Execution occurs at the open of bar t+1 (next-bar entry, no same-bar look-ahead).

**Lookback:**
- EMA period: configurable, grid-searched over [20, 50, 100]. EMA is computed on close with `ewm(span=period, adjust=False).shift(1)` (lagged by one bar).
- Funding rate: shifted by 1 bar (`funding.shift(1)`) to ensure the signal uses only already-settled funding.
- Taker buy ratio: shifted by 1 bar.

**Long entry (signal = +1):**
- `funding_rate.shift(1) < -threshold_low` (funding rate negative; shorts overpaying)
- `close < EMA` (price below trend filter)
- `buy_ratio.shift(1) > 0.45` (taker buy flow confirmation)

**Short entry (signal = -1):**
- `funding_rate.shift(1) > threshold_high` (funding rate high; longs overpaying)
- `close > EMA` (price above trend filter)
- `buy_ratio.shift(1) < 0.55` (taker sell flow confirmation)

**Parameters (grid-searched):**
- `threshold_high`: [0.0003, 0.0005, 0.0007] — 0.03%, 0.05%, 0.07%
- `threshold_low`: [0.00005, 0.0001, 0.0002] — 0.005%, 0.01%, 0.02%
- `ema_period`: [20, 50, 100]
- `hold_bars`: [8, 16, 32]

**Exit:** Fixed holding period (`hold_bars` × 15 minutes). No stop-loss or take-profit in the base signal; the engine also checks high/low for SL/TP if configured (research-defined).

**Holding period:** `hold_bars` bars × 15 min = 2h to 8h (research-proposed range).

**Position sizing:** One position at a time per symbol. No portfolio-level sizing specified.

**Re-entry rules:** New signals are ignored while a position is open.

## Required data

- **Instrument:** Binance USDⓈ-M perpetual futures (USDT-settled).
- **Universe:** Top 10–30 liquid perps by volume (top-10 default, top-30 with `--full`).
- **Venue:** Binance.
- **Market type:** Perpetual futures.
- **Timeframe:** 15-minute candles (resampled from 1-minute source data).
- **Fields:** OHLCV (open, high, low, close, volume), taker_buy_volume, funding_rate (8h), open_interest, top_trader_ls_ratio, taker_ls_vol_ratio (5m).
- **Timestamp:** UTC.
- **Point-in-time:** Funding rates are settled at 00:00, 08:00, 16:00 UTC; the signal uses `shift(1)` to ensure no look-ahead.
- **Missing data:** Symbols with >50% missing funding data are excluded.

## Execution assumptions

- **Signal-to-order timing:** Signal forms at bar close, order placed at next bar open (15-minute delay).
- **Order type:** Market order.
- **Fill model:** Next-bar open with slippage.
- **Fees:** 0.04% taker per side (0.08% round-trip) — source-specified.
- **Slippage:** 0.01% per side (0.02% round-trip) — source-specified.
- **Total round-trip cost:** ~0.10% — source-specified.
- **Leverage:** Not specified; code does not model leverage or margin.
- **Funding carry:** NOT modeled during position holding. The backtest does not account for the funding payments that accrue while the position is open. This is a material omission for a funding-rate-based strategy — source-acknowledged in README ("Costs model taker fees but not funding carry").
- **Impact / capacity:** Not modeled. Universe is limited to top-10 or top-30 liquid perps.
- **Liquidation:** Not modeled.
- **Walk-forward:** 6-month train, 2-month test, 2-month step. Optimization metric: Sharpe. Minimum 10 trades per window.

## Evidence

### Source-reported

From the README and walk-forward backtest results on Binance perpetual futures (2023–2026):

**Strategy 1 — Funding Rate Mean Reversion OOS results (top symbols):**

| Symbol | Sharpe | Return | Win Rate | Trades |
|--------|--------|--------|----------|--------|
| XRPUSDT | +1.58 | +0.19% | 61.4% | 44 |
| DOGEUSDT | +0.27 | +0.22% | 54.0% | 202 |

Source reports these as out-of-sample walk-forward results. The Sharpe is annualized from 15-minute bars (periods_per_year = 252 × 24 × 4 = 24,192).

Portfolio-level equal-weight results are described in the README but specific portfolio metrics (aggregate Sharpe, MDD) are not enumerated in the text. The source shows a strategies_comparison.png image but its contents are not extractable as text.

**Source also reports 3 strategies total:**
- Strategy 1: Funding Rate Mean Reversion (this record)
- Strategy 2: Taker Momentum (not specified in detail in README)
- Strategy 3: OI Divergence (not specified in detail in README)

The README states the framework was "built on 3 years of tick-level Binance data (2023–2026)" with "walk-forward validation" and "realistic execution model."

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The source explicitly acknowledges: "The backtest universe is survivorship-biased (only currently-listed perps), which flatters historical returns."
- The source acknowledges: "Costs model taker fees but not funding carry or slippage on thinner alts, so live net will run below the paper number." (Note: the code does model 0.01% slippage per side; the README note about "not slippage" may refer to venue-specific slippage beyond the fixed 0.01%.)
- Funding carry during position holding is not modeled. For a funding-rate mean-reversion strategy, the funding payments received or paid during the holding period are economically material and could significantly alter net performance.
- XRPUSDT result is based on only 44 OOS trades — limited statistical power.
- The strategy was not tested on a truly independent out-of-sample period separate from the walk-forward procedure.
- No portfolio-level aggregate performance metrics are provided.

## Falsification plan

1. **Walk-forward replication:** Re-run the exact signal logic with the same parameter grid on the same data. Verify Sharpe, return, and trade count match reported figures. (Requires access to the BIGdatabaseBinance dataset, which is not publicly available — data gap for independent replication.)
2. **Funding-carry sensitivity:** Add funding-rate payments during the holding period. If the strategy's edge depends on funding received while holding (which is economically likely for mean-reversion around funding extremes), net performance after funding carry is the critical test. Threshold: strategy is falsified if Sharpe drops below 0.5 after including funding payments. (Research-defined threshold.)
3. **Survivorship-bias stress test:** Extend the universe to include delisted or migrated perpetual contracts. If the edge concentrates in currently-surviving names, the result is survivorship-driven.
4. **Cost sensitivity:** Double taker fees to 0.08% per side and triple slippage to 0.03% per side. Check if Sharpe remains above 1.0. (Research-defined thresholds.)
5. **Parameter stability:** Hold-out the final 6 months of data entirely (outside walk-forward). If OOS Sharpe on the held-out period is < 0, the walk-forward procedure may be overfitting through window selection.
6. **Cross-venue replication:** Test the same signal logic on Hyperliquid, Bybit, or OKX perpetuals with different funding rate schedules and market microstructure.

## Crypto portability

**Direct** — the strategy is natively designed for crypto perpetual futures. No adaptation needed.

Crypto-specific considerations:
- Funding rate schedules vary by venue (Binance: 00:00/08:00/16:00 UTC; Hyperliquid: every hour). The signal timing must be adjusted for non-Binance venues.
- Funding rate magnitudes differ across venues and across market regimes. The thresholds (0.03%–0.07%) are calibrated to Binance 2023–2026 levels and may not generalize.
- 24/7 trading means funding events occur at fixed calendar times, not end-of-day. The 15-minute candle resolution means the signal can only react at candle boundaries, not at exact funding settlement times.
- Venue fragmentation: different venues may show different funding rates for the same underlying, creating cross-venue arbitrage opportunities that are not captured.
- Liquidation dynamics: extreme funding events often coincide with liquidation cascades, which can amplify the mean-reversion. This is not modeled.

## Limitations

- **Funding carry not modeled:** The strategy trades around funding-rate extremes but does not account for the funding payments that accrue during the holding period. This is a material omission — the strategy's economic thesis depends on funding-rate behavior, yet the backtest ignores the actual cash flow of funding during position holding. (Underspecified / data gap.)
- **Survivorship bias:** Only currently-listed perpetuals are included. Delisted or migrated contracts are excluded, which flatters historical returns.
- **Limited trade count:** Best result (XRPUSDT) has only 44 OOS trades — insufficient for robust statistical inference.
- **No portfolio-level metrics:** Aggregate performance across the multi-symbol portfolio is not reported with specific numbers.
- **Data availability:** The backtest depends on a private local dataset (BIGdatabaseBinance) that is not publicly available, preventing independent replication.
- **Single-source, no peer review:** Code-only source with no external validation or published results.
- **Parameter grid is coarse:** Only 81 combinations (3^4) were tested. Finer grids or alternative parameters could yield different results.
- **Taker buy ratio thresholds are very permissive:** Long entries require buy_ratio > 0.45 and short entries require buy_ratio < 0.55 — these thresholds are so close to 0.5 (neutral) that they may provide minimal filtering power. (Research observation, not source-stated.)
- **Walk-forward window selection:** 6-month train / 2-month test windows may not be robust across different market regimes.

## Implementation status

No implementation exists in our research stack (PyBroker, NautilusTrader, or any paper/testnet/live environment). This is a research capture from an external GitHub repository.

## Adoption boundary

This record is research material only. The source-reported results have not been independently reproduced. A record being present in this repository does not mean the strategy is profitable, validated, approved for implementation, approved for paper trading, approved for testnet, or approved for live trading.

## Related Wiki records

No directly related records identified in the repository at this time. Adjacent research on crypto funding rates and perpetual futures microstructure exists in the repository (e.g., records on DeFi AMM dynamics, oracle pricing, and cross-venue basis) but none shares the same mechanism or signal construction.

## Sources

1. Gotodataru. "Walk-forward backtesting framework for crypto perpetual futures — 3 years of data, explicit no-lookahead guarantees, realistic execution model." GitHub repository: https://github.com/Gotodataru/binance-futures-backtest. Commit: `5ed0d6e39d8a3e951bea40c66e2638c213012e1b`. Created 2026-06-09. Accessed 2026-09-11.
2. Signal logic: `strategy_1_funding_mr/signals.py` (same commit). Full signal construction verified against source code.
3. Execution model: `shared/backtest_engine.py` (same commit). Commission 0.04% per side, slippage 0.01% per side, next-bar open entry verified against source code.
4. OOS results: `README.md` (same commit). XRPUSDT Sharpe +1.58, DOGEUSDT Sharpe +0.27 reported as walk-forward out-of-sample results.
