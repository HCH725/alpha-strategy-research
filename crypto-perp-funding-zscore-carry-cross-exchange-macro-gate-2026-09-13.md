---
schema: strategy-research-record-v1
title: "Cross-Exchange Delta-Neutral Perpetual Funding Z-Score Carry with Macro Gate and OBI Confirmation"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - funding-rate
  - carry
  - delta-neutral
  - cross-exchange
status: research-only
confidence: medium
source_as_of: 2026-03-11
sources:
  - "https://github.com/PietroC21/Crypto-PerpetualFutures (commit a07294730ca656b14771ecd46701b2dc69e8df30, 2026-03-11)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Exchange Delta-Neutral Perpetual Funding Z-Score Carry with Macro Gate and OBI Confirmation

## Provenance

- **Repository:** https://github.com/PietroC21/Crypto-PerpetualFutures
- **Full commit SHA:** `a07294730ca656b14771ecd46701b2dc69e8df30` (latest, "OKX pipeline", 2026-03-11)
- **Strategy file:** `strategy.py` (single-exchange backtest engine with `funding_zscore`, `oi_filter`, `macro_gate`, `obi_filter`)
- **Cross-exchange engine:** `strategy_cross.py` (`run_backtest_cross`, `compute_best_fr`)
- **Notebook:** `FINAL_Notebook_V2.ipynb` (QTS Final Project, March 2026)
- **Authors:** Cesare Bavaresco, Pietro Candiani, Thibaut Desauty, Alan Donnelly, Khanh Nguyen
- **Institutional context:** QTS (Quantitative Trading & Strategies) program project
- **Source data as-of:** Binance/Gate/OKX hourly funding rates and OHLCV; Bybit OI; VIX/SPY/FRED macro data; coverage 2020-01-01 to 2026-03

## Economic mechanism

### Source-reported

Perpetual futures contracts periodically pay or receive a funding rate to keep the perp price anchored to spot. When the funding rate is anomalously high (positive), shorting the perp and holding spot collects the funding payment (cash-and-carry). Conversely, when funding is anomalously negative, going long the perp and shorting spot collects the negative funding payment. Cross-exchange routing selects, for each asset at each 8-hour rebalance, the exchange offering the highest funding rate for the short leg while maintaining the spot leg on Binance. The authors note that Hyperliquid's 1-hour funding settlement (vs. 8-hour on other venues) generates more frequent carry opportunities and often the highest effective rate.

### Research interpretation

The hypothesis is that funding rates exhibit mean-reverting behavior relative to each asset's own history, and that cross-exchange routing captures dispersion in funding rate levels across venues. The signal is a time-series z-score of each asset's own funding rate, not a cross-sectional ranking. When the z-score exceeds a threshold, the position is taken on the exchange offering the most favorable funding for that direction. The mechanism combines:

- **Time-series mean reversion of funding rates:** Elevated (depressed) funding rates tend to revert, allowing carry collection during the reversion window.
- **Cross-exchange funding dispersion:** Different venues price funding differently due to differing participant composition, settlement frequency, and liquidity conditions. Routing to the best venue captures additional spread.
- **Settlement frequency arbitrage:** Hyperliquid's 1-hour settlement creates more frequent carry collection events than 8-hour settlement on Binance/OKX/Gate.

This is a carry/trade-finance mechanism, not a directional alpha. The edge depends on funding rate persistence and mean reversion, venue-level dispersion, and the ability to execute the delta-neutral leg efficiently.

## Signal

### Formation timestamp

Funding rate observed at each 8-hour settlement timestamp (00:00, 08:00, 16:00 UTC). Signal computed at settlement; position entered for the next funding period.

### Lookback

Rolling z-score window: 270 periods (270 × 8h ≈ 90 days). Minimum observations: 135 (half the lookback).

### Entry

- **Short perp + long spot** (collect positive funding): when z-score > +1.5 (default `z_entry`)
- **Long perp + short spot** (collect negative funding): when z-score < −1.5

### Exit

Position exits when the z-score crosses back below/above the entry threshold (i.e., the z-score reverts toward zero). Research-proposed: no explicit time exit or stop-loss is specified in the strategy code beyond the z-score reversal.

### Holding period

Variable, driven by funding rate reversion speed. Expected holding is multiple 8-hour funding periods (days to weeks).

### Cross-exchange routing

At each rebalance, for each asset, the exchange with the highest absolute funding rate for the desired direction is selected. Source-reported routing split: Binance ~45%, Hyperliquid ~55% of position-periods.

### Filters

1. **Open interest liquidity gate:** OI must be ≥ 50% of 270-period rolling mean (default `oi_min_ratio = 0.5`). Fallback: if OI is NaN, the filter defaults to True.
2. **Macro risk gate:** Go flat when VIX > 30.0 OR SPY 5-day (15-period) drawdown > 5%.
3. **Order book imbalance (OBI) confirmation (optional):** For a SHORT candidate (z > +z_entry), require OBI > +threshold (bid-heavy book confirms longs are dominant and will keep paying positive funding). For a LONG candidate (z < −z_entry), require OBI < −threshold. Default `obi_threshold = 0.0` (any directional match). OBI data loaded from Binance order book snapshots if available.

### Sizing

Equal weight across active positions (1/N per period where N = number of active positions).

### Parameters

| Parameter | Default | Source |
|-----------|---------|--------|
| `z_lookback` | 270 (≈90 days) | Source-reported |
| `z_entry` | 1.5 | Source-reported |
| `oi_lookback` | 270 | Source-reported |
| `oi_min_ratio` | 0.5 | Source-reported |
| `vix_gate` | 30.0 | Source-reported |
| `spy_dd_window` | 15 (≈5 days) | Source-reported |
| `spy_dd_gate` | 0.05 (5%) | Source-reported |
| `taker_fee` | 0.0004 (4 bps per side) | Source-reported |
| `obi_threshold` | 0.0 | Source-reported |
| `use_obi` | True | Source-reported |

### Position-sizing logic

Research-proposed: equal weight across active positions. No Kelly sizing, volatility targeting, or dynamic allocation described.

## Required data

- **Instruments:** BTC, ETH, SOL, BNB, XRP, DOGE, AVAX perpetual futures (top 7 by Binance perp liquidity)
- **Universe:** 15 symbols in full panel; strategy.py defaults to top 7
- **Venues:** Binance (primary), Gate, OKX (cross-exchange); Hyperliquid (secondary, via `data_extra/`); Bybit (OI data)
- **Market type:** Perpetual futures (USDT-margined) + spot
- **Timeframe:** 8-hour settlement grid (00:00, 08:00, 16:00 UTC); hourly data resampled
- **Fields:** Funding rate, perp OHLCV (mark price), spot OHLCV (index), open interest (base currency), VIX daily close, SPY daily close, FRED 3-month T-bill rate
- **Timestamp:** UTC, rounded to nearest second
- **Missing data:** Funding rate coverage ~87.5% (ARB/POL only from 2023); OI coverage ~73.5% (Bybit OI starts Dec 2020); VIX ~97.7% (null on US market holidays)

## Execution assumptions

- **Signal-to-order timing:** Position entered at the next funding settlement after signal generation.
- **Execution price:** Not explicitly specified in `strategy.py`. The backtest appears to use funding rate received/paid directly, without modeling perp entry/exit price impact.
- **Fill model:** research-proposed assumption of full fill at settlement.
- **Fees:** Taker fee of 4 bps per side (Binance default). Round-trip cost: ~8 bps for single-exchange; source-reported net CAGR assumes 14.5 bps round-trip for cross-exchange (including additional venue fees).
- **Spread:** Not explicitly modeled. For delta-neutral carry, the spot-perp basis at entry/exit is material but not addressed in the backtest.
- **Slippage:** Not explicitly modeled.
- **Impact:** Not explicitly modeled. Position sizes are equal-weighted across active positions; capacity constraints not analyzed.
- **Funding:** The core revenue source; funding rates are observed and received/paid at settlement.
- **Leverage:** Not explicitly stated; delta-neutral construction implies roughly 1:1 long spot / short perp.
- **Borrow/shorting:** Spot leg assumes ability to hold spot; perp leg assumes ability to short perpetual.
- **Latency:** Not modeled; execution assumed at settlement.

## Evidence

### Source-reported

From the `FINAL_Notebook_V2.ipynb` executive summary (cross-exchange backtest, net of 14.5 bps round-trip costs):

| Metric | Value |
|--------|-------|
| Zero-cost CAGR | +9.5% p.a. |
| Net CAGR (after fees) | +5.76% p.a. |
| Fee drag | ~3.7% p.a. |
| Annualised volatility | 0.71% |
| Max drawdown (cross-exchange, net) | 1.22% |
| Max drawdown (Binance-only, net) | 25.6% |
| Hit rate (net positive 8h periods) | 34.0% |
| Profit factor | 4.06 |
| Benchmark Sharpe (daily) | +3.95 |
| BTC buy-and-hold Sharpe | 0.87 |

Source-reported comparison: Binance-only strategy net CAGR is −10.0% (unprofitable). Cross-exchange routing (particularly including Hyperliquid) transforms the strategy from unprofitable to profitable.

Exchange selection: Binance ~45%, Hyperliquid ~55% of position-periods.

Sample period: 2020-01-01 to 2026-03 (per panel construction; exact backtest window not explicitly stated but panel covers this range).

Source-reported limitation: The backtest uses Binance taker fees at 4 bps per side; the 14.5 bps round-trip for cross-exchange includes additional venue fees. The backtest does not model perp entry/exit price impact, spread, or slippage.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Binance-only strategy is unprofitable (net CAGR −10.0%), demonstrating that the cross-exchange routing is essential, not optional.
- Hit rate of 34.0% indicates the strategy relies on large winning periods offsetting frequent small losses (profit factor 4.06).
- Source does not report performance broken down by market regime (bull/bear/sideways).
- The VIX gate (>30) and SPY drawdown gate (>5%) are active filters; their contribution to performance is not ablated.
- The OBI confirmation filter contribution is not ablated (default `obi_threshold = 0.0` means any directional match passes).
- Source does not analyze the impact of Hyperliquid's 1-hour settlement frequency advantage in isolation.

## Falsification plan

1. **Single-exchange replication:** Run the z-score carry strategy on each venue independently (Binance, OKX, Gate, Hyperliquid) and verify that cross-exchange routing is necessary for positive net returns. Source-reported: Binance-only is unprofitable. **Failure rule:** If any single venue achieves net CAGR > 3% with Sharpe > 1.5, the cross-exchange routing hypothesis is weakened.
2. **Funding rate mean-reversion decay test:** Compute the half-life of funding rate z-score mean reversion across the sample. If half-life < 8 hours (one settlement period), the carry window is too short to capture after fees. **Failure rule:** If the half-life of z-score autocorrelation drops below 0.3 at lag 1 for any major asset, the time-series mean reversion hypothesis is weakened.
3. **Fee sensitivity stress:** Recompute net CAGR at 20 bps, 30 bps, and 50 bps round-trip costs. **Failure rule:** If net CAGR turns negative at any realistic institutional cost level (e.g., 20 bps), the strategy is not robust to execution costs.
4. **Regime decomposition:** Break backtest into bull (BTC up >20% annualized), bear (BTC down >20%), and sideways regimes. **Failure rule:** If the strategy is unprofitable in any single regime for >12 consecutive months, regime dependence is a material risk.
5. **Hyperliquid settlement frequency ablation:** Remove Hyperliquid from the venue universe and re-run. **Failure rule:** If removing Hyperliquid causes net CAGR to drop below zero, the strategy's viability depends on a single venue's microstructure.
6. **Parameter perturbation:** Vary `z_entry` from 1.0 to 2.5 in 0.5 increments and `z_lookback` from 180 to 360. **Failure rule:** If net CAGR is negative for more than 2 of the 10 parameter combinations, the strategy lacks a stable parameter plateau.
7. **VIX/SPY gate ablation:** Remove the macro risk gate entirely. **Failure rule:** If removing the gate increases max drawdown by more than 5x without proportionally increasing CAGR, the gate is load-bearing and its removal falsifies the strategy's standalone viability.

## Crypto portability

direct

The strategy is native to crypto perpetual futures markets. The funding rate mechanism is specific to perpetual contracts and does not exist in traditional futures. Cross-exchange routing relies on the fragmented nature of crypto derivatives venues (Binance, OKX, Gate, Hyperliquid, etc.) with differing settlement frequencies and participant compositions.

Crypto-specific portability considerations:
- Funding rate dynamics are non-stationary and regime-dependent; periods of persistent positive or negative funding can erode carry.
- Hyperliquid's 1-hour settlement is a structural advantage not available on most venues; if Hyperliquid changes its settlement mechanism, the strategy's edge may diminish.
- Cross-exchange execution requires maintaining accounts and margin on multiple venues, introducing operational complexity and counterparty risk.
- Spot-perp basis at entry/exit is not modeled; in practice, the delta-neutral leg requires simultaneous spot purchase and perp short, which introduces basis risk.
- Funding rate data quality varies across venues; some newly listed assets have incomplete history.

## Limitations

- **Backtest does not model perp entry/exit price impact, spread, or slippage.** The funding PnL is computed directly from observed funding rates without accounting for the cost of establishing and unwinding the delta-neutral position. This is a material data gap for live deployment.
- **Sample period ends March 2026.** Performance in subsequent regimes is unknown.
- **Hyperliquid dependency.** ~55% of position-periods are routed to Hyperliquid; the strategy's viability depends on this venue's continued operation, liquidity, and 1-hour settlement mechanism.
- **Hit rate of 34.0%.** The strategy relies on a small number of large winning periods; tail risk and path dependency are material.
- **No out-of-sample forward test.** The backtest covers 2020-2026 but is not reported as walk-forward or rolling-window validated.
- **Parameter sensitivity not fully reported.** Only default parameters are shown; robustness to parameter variation is not demonstrated.
- **OBI filter not ablated.** The contribution of the order book imbalance confirmation filter to performance is unknown.
- **Macro gate not ablated.** The contribution of the VIX/SPY risk-off gate to performance is unknown.
- **Not independently reproduced.**
- **Source is a student project (QTS program).** While the methodology is reasonable, the source quality is academic-project level, not peer-reviewed.

## Implementation status

not-implemented

No implementation in our research stack (PyBroker, NautilusTrader, or live) has been completed. The source provides a complete backtest framework (`strategy.py`, `strategy_cross.py`) that could serve as a reference implementation.

## Adoption boundary

research-only

This record represents normalized research material only. Presence in this repository does not mean:
- profitable (source-reported results are unverified)
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

The source-reported net CAGR of +5.76% and Sharpe of +3.95 are source-reported claims that have not been independently reproduced. The strategy requires independent validation before any implementation consideration.

## Related Wiki records

- `[[crypto-cex-dex-cross-venue-funding-spread-carry-2026-08-31]]` — Cross-exchange funding rate spread carry between CEX and DEX; different mechanism (spread harvesting vs. per-asset z-score carry).
- `[[ethena-optimal-execution-delta-neutral-steth-perp-carry-2026-09-02]]` — Optimal execution for delta-neutral stETH-perp carry; different mechanism (execution optimization vs. signal generation).
- `[[crypto-hyperliquid-momentum-funding-carry-combo-2026-09-12]]` — Hyperliquid momentum + funding carry combo; different mechanism (momentum overlay vs. pure funding z-score).
- `[[funding-rate-cross-sectional-factor-survivorship-free-regime-flip-2026-09-13]]` — Cross-sectional funding factor with regime flip; different mechanism (cross-sectional ranking vs. time-series z-score per asset).
- `[[rl-market-making-funding-rate-capture-crypto-perpetual-2026-09-12]]` — RL market making for funding rate capture; different mechanism (liquidity provision vs. carry harvesting).

## Sources

1. Cesare Bavaresco, Pietro Candiani, Thibaut Desauty, Alan Donnelly, Khanh Nguyen. "Cross-Exchange Delta-Neutral Spot-vs-Perp Cash-and-Carry." QTS Final Project, March 2026. Repository: https://github.com/PietroC21/Crypto-PerpetualFutures, commit `a07294730ca656b14771ecd46701b2dc69e8df30` (2026-03-11).
2. Strategy code: `strategy.py` (single-exchange backtest), `strategy_cross.py` (cross-exchange backtest).
3. Backtest results: `FINAL_Notebook_V2.ipynb`, executive summary section.
