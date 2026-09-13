---
schema: strategy-research-record-v1
title: "Positioning-Based Directional Trading on BTC Perpetual Futures: Crowd Long/Short Ratio Cascade Mechanism"
created: 2026-09-14
updated: 2026-09-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-04-05
sources:
  - "https://github.com/MG-Trading-Terminal/trading-strategy (commit e6d26a6d41693ea74024cf699942f72f224e296c, strategies/positioning-based-btc.md)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Positioning-Based Directional Trading on BTC Perpetual Futures: Crowd Long/Short Ratio Cascade Mechanism

## Provenance

- **Source:** GitHub repository `MG-Trading-Terminal/trading-strategy`
- **Full commit SHA:** `e6d26a6d41693ea74024cf699942f72f224e296c`
- **File path:** `strategies/positioning-based-btc.md`
- **Author:** D. Chystiakov
- **Date:** April 5, 2026 (version 1.0)
- **Source type:** Public GitHub repository with backtest code and full methodology documentation
- **Source URL:** https://github.com/MG-Trading-Terminal/trading-strategy

## Economic mechanism

### Source-reported

The author identifies five participant classes in BTC perpetual futures: smart money (top traders), slow money (institutions/ETFs), market makers, small money, and retail. The core mechanism is the liquidation cascade: when one side of the market becomes overloaded (avgLong < 48% or > 65%), their aggregate stop-losses and liquidation levels create a pool of potential forced orders ("fuel"). A relatively small exogenous trigger causes the first wave of stops to fire, pushing price further and triggering more closures in a self-reinforcing cascade. The cascade exhausts when positioning rebalances — empirically after avgLong shifts approximately 13 percentage points from the entry level.

The author claims that participant positioning (who is long and who is short) predicts direction more reliably than price action, volume, technical indicators, or funding rates. The top trader long/short account ratio reportedly leads crossing events in 67% of cases, while retail positioning is described as the single most reliable contrarian indicator.

### Research interpretation

The hypothesis is that Binance Futures' published long/short account ratios — particularly the divergence between top trader and retail positioning — contain mechanically useful information about the distribution of liquidation levels in the market. When positioning is extreme, the "path of least resistance" for price is toward the heavier cluster of liquidations. The regime classification (BULL avgLong < 48%, DEAD 48–65%, BEAR > 65%) partitions the market into states where the fuel-cascade mechanism is armed (extremes) versus disarmed (dead zone). This is a **research-proposed** interpretation; the source reports it as observed but does not provide independent microstructural identification beyond the statistical backtest.

The eight models operate at different regime boundaries:
- Regime filter: avgLong-based regime classification (3-day EMA)
- Primary signal: positioning extremes (avgLong levels, top-retail divergence, velocity metrics)
- Confirmation: price range stability, velocity thresholds
- Risk / exit: fuel-based exit (13pp avgLong shift), signal inversion, fixed stop-loss 5%

## Signal

- **Formation timestamp:** Binance Futures reports top trader and global long/short account ratios every 5 minutes. The signal uses a 3-day EMA of avgLong for regime classification and raw/velocity-derived positioning metrics for entry.
- **Lookback:** Various per model — topVel24 (24-hour top trader velocity), retVel12 (12-hour retail velocity), 12-hour price range. Regime classification uses 3-day EMA of avgLong.
- **Long entry (PB14-L):** avgLong < 48%, |topVel24| < 1.5pp, |retVel12| < 2.5pp, range12h < 2.5%, OI_USD ≤ $10B.
- **Short entry (PB12):** avgLong > 65%, div < -5%, topVel24 > -2pp, ΔP4h < -0.3%, ΔOI12h > -3%, topLong > 60%.
- **Additional models:** PB2 (adaptive failed-pump short), PB14-S (dead-zone top-sells-while-retail-buys short), DIST (3-day distribution divergence short), FLIQ-L (OI flush long), PEND-S (pendulum spike short, removed from entry, used for exit detection).
- **Exit:** Primary exit is fuel consumption — avgLong shifts ~13pp from entry level ("fuel-based exit"). Secondary exit: signal inversion (exit LONG when any SHORT signal fires, vice versa — 100% WR on inverse exits per source). Fixed stop-loss at 5% of entry price. 72-hour cooldown after stop-loss hit (V3 refinement).
- **Holding period:** 1–7 days (model-dependent). Average hold time 1–7 days.
- **Parameters:** All thresholds are research-proposed based on 733-day bar-by-bar study. The author reports parameter sensitivity: 21/21 variations profitable (+691% to +848% PnL).
- **Position sizing:** research-proposed; practical leverage limit stated as x2 maximum due to irreducible drawdown at higher leverage.
- **Re-entry:** Allowed after 72h cooldown post-stop-loss. No explicit re-entry prohibition otherwise.

## Required data

- **Instrument:** BTCUSDT perpetual futures (Binance USDⓈ-M)
- **Venue:** Binance Futures
- **Market type:** Perpetual futures (USDT-margined)
- **Timeframe:** 5-minute bars (~210,000 bars over 733 days)
- **Fields:**
  - Top trader long/short account ratio (5-min, `topLongShortAccountRatio`)
  - Global (retail) long/short account ratio (5-min, `globalLongShortAccountRatio`)
  - Open interest in USD and BTC (5-min, `openInterestHist`)
  - Klines with taker buy volume (5-min, `klines`)
  - Funding rate history (8-hour, `fundingRate`)
- **Timestamp:** UTC, 5-minute granularity
- **Point-in-time:** Binance reports positioning ratios with 5-minute granularity; no stated lag. Historical data beyond 30-day API window obtained from Binance S3 public data archive.
- **Missing-data:** Not explicitly addressed in source. Binance S3 archive coverage for the full 733-day period is assumed complete.

## Execution assumptions

- **Signal-to-order timing:** Next 5-minute bar execution (signal known at bar close, entry at next bar open).
- **Order type:** Research-proposed as taker execution for entries; exit mechanism unspecified beyond "signal inversion" and fuel-based exit.
- **Fill model:** Research-proposed mid-price execution assumed.
- **Fees:** Source reports round-trip cost of 0.105% (maker 0.02% + taker 0.055% + slippage 0.03%). All reported PnL figures are net of these costs. The taker fee assumption (0.055%) exceeds Binance VIP0 taker rate (0.04%), suggesting conservative fee modeling.
- **Slippage:** 0.03% (3 bps) per side, included in the 0.105% round-trip cost.
- **Spread:** Not explicitly modeled; subsumed into the slippage assumption.
- **Funding:** Source notes average hold time of 1–7 days spans 3–21 funding settlements; at typical rates, funding cost is 0–0.5% of PnL — characterized as "noise."
- **Leverage:** Practical limit stated as x2 maximum. Source reports irreducible maximum drawdown at higher leverage.
- **Impact / capacity:** Not explicitly addressed. BTCUSDT perpetual has multi-billion-dollar open interest, so capacity constraints are likely negligible for the stated trade sizes.
- **Latency:** 5-minute signal resolution; not latency-sensitive.

## Evidence

### Source-reported

- **V1 results (full system, 733 days, April 2024–April 2026):**
  - 290 trades, 72% win rate, +828% cumulative PnL (net of 0.105% round-trip costs), profit factor 3.53, maximum drawdown -40%
  - Walk-forward efficiency: 0.97 (out-of-sample retains 97% of in-sample quality)
  - Monte Carlo p-value < 0.01% (100,000 random permutations, zero matched or exceeded actual performance)
  - Profitable quarters: 8/8 (100%)
  - Parameter sensitivity: 21/21 variations profitable (+691% to +848%)
  - Average trade PnL: +2.85%
  - Average hold time: 1–7 days

- **V3 results (refined with 72h cooldown and signal inversion exit, 547-day subset):**
  - BTC: 109 trades, 80% WR, +1,021% PnL, PF 13.94, max DD -27%
  - ETH: 98 trades, 73% WR, +2,972% PnL, PF 27.36, max DD -21%
  - SOL: 90 trades, 62% WR, +1,015% PnL, PF 7.61, max DD -25%

- **Cross-asset validation (V3, 547-day kline period):**
  - BTC: 109 trades, 80% WR, +1,021% PnL, PF 13.94
  - ETH: 98 trades, 73% WR, +2,972% PnL, PF 27.36
  - SOL: 90 trades, 62% WR, +1,015% PnL, PF 7.61

- **Key mechanical rules (source-reported from bar-by-bar study):**
  - avgLong < 48% = squeeze fuel: 76% accuracy (111 events)
  - avgLong > 65% = crash fuel: 74% accuracy (89 events)
  - Pendulum: avgLShift24 > 6pp → price follows opposite direction: 97% direction accuracy (67 events), but only 50% exceed 2% minimum threshold
  - Fuel consumed: ΔavgLong ≈ 13pp: consistent across 150 moves
  - OI flush + price < -2%: 78% bounce (23 events)

These are source-reported backtest figures. They have not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

Source identifies several structural limitations:
1. **Irreducible 9% direction error rate:** Of 290 trades, 27 (9.3%) are fundamentally wrong about direction and are indistinguishable from winners at entry on all measured metrics.
2. **"Bear-no-divergence" problem:** Type B crashes (externally driven, e.g., February 2026 BTC crash $89K→$63K) show no positioning divergence — avgLong remains stable while price drops. Positioning-based models are structurally blind to these events.
3. **Dead zone is uninformative:** In the 48–65% avgLong range, seven independent signal approaches all yield win rates near 50% and PF near 1.0. The normal zone is structurally uninformative.
4. **Altcoin positioning is noise:** After removing BTC correlation, zero informational signal survives on any of the seven altcoins studied. The "top trader" category on altcoins correlates 95–98% with retail.
5. **Speed of the research:** The entire study was conducted in a compressed timeframe (190+ tests across 141 iterations), raising potential for data-snooping bias despite the author's attempt at walk-forward validation.

## Falsification plan

- **Out-of-sample extension:** The study covers 733 days (April 2024–April 2026). The author reports V3 results on a 547-day subset. A genuine forward-test on data after April 2026 would be the most direct falsification test.
- **Cost sensitivity:** The 0.105% round-trip cost model is research-proposed. Testing at higher costs (e.g., 0.15–0.20% for retail execution with wider slippage) would stress-test profitability.
- **Regime breakdown:** The author reports 8/8 profitable quarters. A prolonged dead-zone regime (avgLong 48–65% for extended periods) would starve the system of signals. Testing on historical periods dominated by the dead zone would be informative.
- **Positioning data availability:** The strategy depends on Binance publishing top trader and global long/short ratios at 5-minute granularity. Any change to data availability, granularity, or delay would invalidate the signal.
- **Comparison to simple baselines:** The source reports mechanical rules (e.g., avgLong < 48% = 76% accuracy) but does not compare the full system to a simple rule-based baseline using the same positioning data without the eight-model framework.
- **Leverage sensitivity:** The source notes a practical x2 leverage limit. Testing at higher leverage levels would reveal whether the reported drawdowns are truly irreducible or artifacts of the chosen sizing.

## Crypto portability

direct

The strategy is natively designed for crypto perpetual futures (Binance USDT-M). The liquidation cascade mechanism is specific to leveraged perpetual futures markets with continuous funding and forced liquidation. The author tested cross-asset extension on ETH and SOL with varying success (ETH showed strong results, SOL weaker). The author's negative finding that altcoin positioning is noise after removing BTC correlation limits portability beyond BTC and ETH.

Crypto-specific considerations:
- **Funding:** Source reports funding cost is "noise" (0–0.5% of PnL) at the 1–7 day hold horizon. This may change in extreme funding environments.
- **Venue dependency:** The signal requires Binance-specific positioning data (top trader and global long/short account ratios). Other exchanges may not provide equivalent data.
- **24/7 sessions:** The strategy operates continuously; no session-dependent effects noted.
- **Liquidity:** The strategy depends on sufficient open interest for cascade mechanics to propagate. The source notes altcoins with $100–500M OI lack sufficient depth.

## Limitations

- **Single-author, single-repository:** No independent peer review or replication.
- **Compressed research timeline:** 190+ tests across 141 iterations raises data-snooping concerns despite walk-forward validation.
- **733-day sample:** Relatively short for a strategy targeting 7–14 day holds; approximately 290 trades in V1. Statistical power for regime-specific claims is limited.
- **Walk-forward efficiency of 0.97:** The author reports near-perfect out-of-sample retention, which is unusual for most trading strategies and may indicate overfitting to the specific sample or insufficient out-of-sample degradation testing.
- **V1 vs V3 discrepancy:** V1 reports 290 trades / 72% WR / +828% / PF 3.53; V3 reports 109 trades / 80% WR / +1,021% / PF 13.94 on a shorter subset. The V3 refinement (72h cooldown + signal inversion exit) appears to dramatically improve metrics, but the relationship between V1 and V3 is not fully transparent.
- **Cost model:** The 0.105% round-trip cost is research-proposed and may be optimistic for retail execution at higher leverage or during volatile periods.
- **Not independently reproduced**
- **data gap:** Maximum drawdown context — the -40% max DD in V1 occurred during December 2025–January 2026 (PB12 serial losses). The source notes this but does not provide detailed drawdown attribution.
- **underspecified:** The exact mapping from the 290-trade V1 system to the 8 individual model contributions is not fully transparent in the source; per-model performance is partially reported.

## Implementation status

No implementation in our research stack. This is a source-reported backtest only. No PyBroker, Nautilus, paper, testnet, or live execution has been conducted by our team.

## Adoption boundary

This record represents normalized research material only. Presence in this repository does not mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

The source reports strong backtest results but they have not been independently reproduced. The strategy's dependence on Binance-specific positioning data and the compressed research timeline warrant caution.

## Related Wiki records

- No directly related strategy research records were identified in the repository that share the same source identity or materially identical mechanism. Related records in the general domain of crypto perpetual microstructure and positioning exist but use different data sources and mechanisms.

## Sources

1. D. Chystiakov, "Positioning-Based Directional Trading on BTC Perpetual Futures: A 733-Day Empirical Study," GitHub repository `MG-Trading-Terminal/trading-strategy`, commit `e6d26a6d41693ea74024cf699942f72f224e296c`, file `strategies/positioning-based-btc.md`, April 5, 2026. https://github.com/MG-Trading-Terminal/trading-strategy
