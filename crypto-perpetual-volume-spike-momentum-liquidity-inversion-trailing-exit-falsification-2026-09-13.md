---
schema: strategy-research-record-v1
title: "Crypto Perpetual Volume-Spike Momentum: Liquidity-Tier Drift Inversion, Trailing-Stop Pathology, and Intrabar Resolution Bias Falsification"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - momentum
  - volume-spike
  - market-microstructure
  - liquidity-tiers
  - drift-inversion
  - trailing-stop
  - execution-costs
  - falsification
  - negative-evidence
status: research-only
confidence: high
source_as_of: 2026-08-23
sources:
  - "https://github.com/AlexSilka/spike_bot/tree/397ed221a6e7accb92641b8b7a7d674ec950c127"
  - "https://github.com/AlexSilka/spike_bot/blob/397ed221a6e7accb92641b8b7a7d674ec950c127/docs/WHAT_WORKS.md"
  - "https://github.com/AlexSilka/spike_bot/blob/397ed221a6e7accb92641b8b7a7d674ec950c127/docs/ROBUSTNESS_PLAN.md"
  - "https://github.com/AlexSilka/spike_bot/blob/397ed221a6e7accb92641b8b7a7d674ec950c127/research/reports/tick_layer.md"
  - "https://github.com/AlexSilka/spike_bot/blob/397ed221a6e7accb92641b8b7a7d674ec950c127/research/reports/cost_model.md"
  - "https://github.com/AlexSilka/spike_bot/blob/397ed221a6e7accb92641b8b7a7d674ec950c127/research/reports/event_study_15m.md"
  - "https://github.com/AlexSilka/spike_bot/blob/397ed221a6e7accb92641b8b7a7d674ec950c127/research/reports/exit_search.md"
  - "https://github.com/AlexSilka/spike_bot/blob/397ed221a6e7accb92641b8b7a7d674ec950c127/research/reports/tf_search.md"
  - "https://github.com/AlexSilka/spike_bot/blob/397ed221a6e7accb92641b8b7a7d674ec950c127/research/reports/sweep_1m_calibration.md"
  - "https://github.com/AlexSilka/spike_bot/blob/397ed221a6e7accb92641b8b7a7d674ec950c127/docs/FEE_REDUCTION.md"
  - "https://github.com/AlexSilka/spike_bot/blob/397ed221a6e7accb92641b8b7a7d674ec950c127/lib/strategy/src/signal.rs"
  - "https://github.com/AlexSilka/spike_bot/blob/397ed221a6e7accb92641b8b7a7d674ec950c127/research/all_years.py"
  - "https://github.com/AlexSilka/spike_bot/blob/397ed221a6e7accb92641b8b7a7d674ec950c127/research/trend_book.py"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Perpetual Volume-Spike Momentum: Liquidity-Tier Drift Inversion, Trailing-Stop Pathology, and Intrabar Resolution Bias Falsification

## Provenance

- **Primary Source Codebase & Research Repository:** `AlexSilka/spike_bot` (*Rust trading system for crypto perpetual futures: live executor, tick-accurate backtester, memoised grid optimizer, and empirical robustness study*), authored by Alex Silka (`AlexSilka`) (`source-reported`).
- **Canonical Source Identity:** GitHub repository `https://github.com/AlexSilka/spike_bot` at immutable commit SHA `397ed221a6e7accb92641b8b7a7d674ec950c127` (as of 2026-08-23) (`source-reported`).
- **Primary Source Files Directly Inspected:**
  - `docs/WHAT_WORKS.md`: Research synthesis and empirical verdict across 17.3 billion evaluated parameter combinations, contrasting short-horizon failures with daily breakout survival (`source-reported`).
  - `docs/ROBUSTNESS_PLAN.md`: Seven-phase pre-registered study design establishing multi-tiered panels, clustered bootstrap inference, and walk-forward gating (`source-reported`).
  - `research/reports/tick_layer.md`: Tick-level backtest report across 40 coins and 214,184 trades documenting the decomposition of the edge, commission drag, and trailing stop failure (`source-reported`).
  - `research/reports/cost_model.md`: Live order execution measurement across 3,295 closed trades ($65,906 turnover) calibrating commission, taker share, and slippage (`source-reported`).
  - `research/reports/event_study_15m.md`: Event study across 668 perpetuals (154 delisted) and 85,455 events comparing coin-clustered vs pooled inference across 4 liquidity tiers (`source-reported`).
  - `research/reports/exit_search.md`: Comparison of seven exit architectures on 79 coins over 6 years in bps per day held (`source-reported`).
  - `research/reports/tf_search.md`: Multi-timeframe cross-evaluation across 8 entry families (15m, 1h, 4h, 1d) on 79 coins (`source-reported`).
  - `research/reports/sweep_1m_calibration.md`: Intrabar resolution calibration measuring trailing-stop overstatement on 15m bars vs tick engine (`source-reported`).
  - `docs/FEE_REDUCTION.md`: Microstructural fee analysis of Binance USDⓈ-M VIP 0 taker/maker orders on 1,340 live trades (`source-reported`).
  - `lib/strategy/src/signal.rs`: Production Rust implementation of the `VolumeSpike` signal evaluator (`source-reported`).
  - `research/all_years.py`: Multi-year symmetric breakout vs volume spike comparison script (`source-reported`).
  - `research/trend_book.py`: Account-level capital-constrained portfolio simulation script (`source-reported`).

## Economic mechanism

### Source-reported

1. **Volume Spike Entry Hypothesis:** The source initially hypothesized that a sudden surge in quote volume ($volume \ge k \cdot \overline{volume}_{SMA}$) accompanied by a sharp close-to-close directional price jump ($close_t / close_{t-1} - 1 \ge pcp$) indicates aggressive institutional liquidity-taking or metaorder execution that creates persistent post-event directional drift over intraday horizons (1h to 24h) (`source-reported`).
2. **Empirical Liquidity Drift Inversion:** Rigorous event-study measurement across a 668-perpetual panel disproved universal momentum. While liquid top-30 contracts exhibit positive drift (+15.8 bps over 8h in 2025–2026), micro-cap perpetuals (rank 300+) exhibit **statistically significant negative drift** (−11.2 bps over 8h, $t = -3.3$; −1.4 bps at 1h, $t = -2.7$). The source attributes this inversion to structural differences: in illiquid names, volume spikes represent retail FOMO exhaustion, aggressive pump-and-dump market orders, or forced liquidations that quickly reverse rather than continue (`source-reported`).
3. **Execution Fee Wall:** On liquid names where positive drift exists (+15.8 bps over 8h), the physical execution engine captures only +0.9 bps gross due to execution latency, quote displacement, and the single-position restriction. Round-trip taker commissions (−10.0 bps) and funding (−0.5 bps) convert this gross drift into a net loss of −9.5 bps per trade (`source-reported`).
4. **Trailing-Stop Exit Pathology:** The source tested seven exit architectures. A trailing stop activated after reaching a profit threshold performed **worst of all seven exits** (−5.6 bps/day). By removing a hard time-based exit horizon, the trailing stop allows losing trades to drift unchecked until hitting the catastrophic disaster stop. This lifts the stop-loss rate from 1.9% (under a time exit) to 29.4%, degrading net returns from −9.5 bps to −32.4 bps per trade (`source-reported`).
5. **Intrabar Resolution Bias:** Simulating a 1% trailing stop on 15-minute bars overstates net returns by +93 bps against tick-level replay. The discrete 15-minute bar cannot observe intrabar high/low traversal sequences, falsely assuming favorable exits before stops are triggered (`source-reported`).

### Research interpretation

The findings provide an important quantitative autopsy of short-horizon momentum on cryptocurrency derivatives:
- **Regime & Liquidity Segmentation:** The signal conflates two economically opposite phenomena: (a) institutional informed flow in deep order books (which produces transient continuation), and (b) retail liquidity exhaustion or liquidation cascades in shallow order books (which produces immediate mean-reversion). Applying a uniform volume-spike threshold across an unsegmented crypto universe guarantees negative drift in the tails.
- **Statistical Hallucination of Naive Pooling:** When overlapping event windows are pooled naively, $t$-statistics explode into false precision ($t = 37.7$ on liquid 24h, $t = 447.0$ on micro 24h). Clustering standard errors by coin reveals the true sampling uncertainty ($t = 2.6$ and $t = 0.2$), exposing how naive statistical backtests manufacture spurious confidence.
- **Structural Primacy of the Time-Exit Barrier:** Trailing stops are structurally mismatched to intraday crypto momentum. Because crypto perpetuals exhibit heavy-tailed noise and mean-reverting microstructure, a trade that does not materialize its drift within an 8–24 hour informational window has decayed into pure adverse selection. A hard time cap acts as an essential information purge; removing it creates severe left-tail bleeding.
- **Contrast with Daily Breakout:** The source demonstrates that trend-following alpha in crypto survives on daily bars (20-day breakout with 50-day moving average cross exit, yielding 5 profitable years and 1 flat year across 2021–2026), but only when:
  1. Horizon is long enough that ~11.6 bps round-trip friction becomes negligible relative to holding returns.
  2. Long and short sleeves operate symmetrically to cover each other's regime drawdowns (long lost −76 bps/day in 2022 while short gained +26 bps/day; long lost −48 bps/day in 2026 while short gained +26 bps/day).

## Signal

### VolumeSpike Signal Construction (Falsified Intraday Specification)

- **Formation Timestamp:** Evaluated strictly at the close timestamp of bar $t$ (`trigger_bar_close_ts_ns`) (`source-reported`).
- **Execution Timestamp:** Order placed at `open[t+1]` (the open of the next bar); same-bar execution is explicitly forbidden and rejected (`source-reported`).
- **Lookback Window:** Rolling simple moving average over the $N$ closed bars strictly preceding bar $t$ (`volume_avg_window`), excluding bar $t$ itself (`source-reported`). Tested grid: $N \in \{20, 96\}$ bars (`source-reported`).
- **Price Change Trigger:**
  $$\Delta P_t = \left(\frac{Close_t}{Close_{t-1}} - 1\right) \times 100 \ge pcp$$
  where $pcp \in \{0.0, 1.0, 3.0, 6.0\}\%$ (`source-reported`). Computed strictly close-to-close to avoid intrabar wick contamination (`source-reported`).
- **Volume Spike Trigger:**
  $$Volume_t \ge k \times \frac{1}{N} \sum_{i=1}^{N} Volume_{t-i}$$
  where $k \in \{2.0, 4.0, 8.0\}$ (`volume_multiplier`) (`source-reported`). Volume is measured in USDT quote volume to ensure price invariance over multi-year regimes (`source-reported`).
- **Direction:** Long when $\Delta P_t \ge +pcp$; Short when $\Delta P_t \le -pcp$ (`source-reported`).
- **Exit Logic (Evaluated Variants):**
  1. `time_only`: Exit at `open[t + 1 + h]` where $h \in \{1, 2, 4, 8, 24\}$ hours (`source-reported`).
  2. `stop_only`: Exit when intrabar adverse move hits $sl \in \{2.0, 4.0, 8.0\} \times ATR$ (`source-reported`).
  3. `ma_cross`: Exit when bar close crosses the rolling $MA \in \{10, 20, 50\}$ against the position (`source-reported`).
  4. `fixed_atr` (Trailing after profit): Fixed stop-loss at $-sl \times ATR$; once profit reaches $+tp \times ATR$, activate trailing stop trailing $trD \times ATR$ below highest watermark (`source-reported`).
  5. `chandelier`: Trailing stop pegged continuously to trailing highest high minus ATR multiple (`source-reported`).
  6. `breakeven`: Move stop to entry price once profit reaches trigger threshold (`source-reported`).
- **Concurrency & Sizing:** Single position per coin; new signals firing while a position is open are dropped (`source-reported`). Position sizing fixed at ~1% of capital (`research-proposed` portfolio rule, `source-reported` sizing sweep).

### Daily Breakout Benchmark Construction (Surviving Multi-Year Specification)

- **Formation Timestamp:** Daily bar close ($00:00$ UTC) (`source-reported`).
- **Execution Timestamp:** Daily bar open ($00:00$ UTC next day) (`source-reported`).
- **Lookback Window:** $LB = 20$ days (`source-reported`).
- **Entry Rules:**
  - Long: $Close_t > \max(High_{t-20..t-1})$ (`source-reported`).
  - Short: $Close_t < \min(Low_{t-20..t-1})$ (`source-reported`).
- **Exit Rules:**
  - Long Exit: $Close_{t+k} < SMA_{50}(Close)$ (`source-reported`).
  - Short Exit: $Close_{t+k} > SMA_{50}(Close)$ (`source-reported`).
  - Emergency Disaster Stop: $8.0 \times ATR_{14}$ (`source-reported`).
  - Maximum Hold: 200 days (`source-reported`).

## Required data

- **Instrument:** USDⓈ-M perpetual futures contracts listed on Binance (`source-reported`).
- **Universe:**
  - 672 perpetual contracts in frozen full panel, including 154 delisted contracts (e.g., Ake, FTT, LUNA) to eliminate survivorship bias (`source-reported`).
  - 79 liquid perpetual contracts with continuous history from 2021 through 2026 for the 6-year multi-coin benchmark (`source-reported`).
  - 40 coins for high-frequency tick backtesting (10 liquid, 12 mid, 12 small, 12 micro) (`source-reported`).
- **Venue:** Binance USDⓈ-M Futures (`source-reported`).
- **Timeframe:** 15-minute bars (primary signal timeframe), aggregated 1h, 4h, 1d bars; tick-by-tick trade records (`trade_ts_ns`, `price`, `qty`, `is_buyer_maker`) (`source-reported`).
- **Fields:**
  - `open`, `high`, `low`, `close` prices.
  - `quote_volume` (denominated in USDT).
  - `taker_buy_quote_volume` (for aggressor flow comparison).
  - `funding_rate` (8-hour settlement).
  - High-resolution tick parquet store running at 226M ticks/s (`source-reported`).
- **Point-in-Time Integrity:** Bars closed and timestamped prior to order generation; tick-level fills calibrated against exchange order book timestamps; delisted coins frozen at historical delisting timestamps (`source-reported`).
- **Missing-Data Assumptions:** Delisted coins retain historical trades until delisting date then cease; zero forward imputation permitted (`source-reported`).

## Execution assumptions

- **Order Types & Routing:**
  - Entries: Limit orders and Market orders (live telemetry: 75% taker share; ~50% of intended limit orders cross the spread due to momentum displacement) (`source-reported`).
  - Exits: 100% taker orders (`STOP_MARKET` and `SELL_MARKET` / `BUY_MARKET`) (`source-reported`).
- **Fees & Frictions:**
  - Binance VIP 0 base schedule: 0.020% maker fee, 0.050% taker fee (`source-reported`).
  - Live empirical fee measurement: 4.25 bps average commission per side (8.5 bps round trip) (`source-reported`).
  - Entry slippage: +0.96 bps average (`source-reported`).
  - Stop-loss execution slippage: +10.96 bps average (`source-reported`).
  - Backtest composite round-trip friction: **11.6 bps** ($2 \times 4.25 + 0.96 + 0.199 \times 10.96$) (`source-reported`).
  - Funding drag: −0.5 bps per trade on 8h holds (`source-reported`).
- **Fill Engine Parity:**
  - Limit orders execute on `open[t+1]`, never on signal bar `t` (`source-reported`).
  - Intrabar stop execution: Adverse extreme taken first in 15m bar evaluation (`source-reported`).
  - Latency model: Execution delay modeled with half-spread penalty (`source-reported`).
  - Market impact: Modeled as $0.1 \cdot \sigma_{bar} \cdot \sqrt{\text{notional}/\text{volume}}$; live notional at $10–$500 exhibits negligible market impact (`source-reported`).
  - Leverage: 1.0x (unleveraged cash account constraint; leverage multiplies drawdown and return proportionally without altering risk-to-drawdown ratio) (`source-reported`).

## Evidence

### Source-reported

#### 1. Event Study: Forward Drift Across Liquidity Tiers (Gate G1)

Evaluated across 668 perpetuals (154 delisted) and 85,455 events over 2020–2026. Forward excess drift (bps) over coin random baseline; errors clustered by coin:

| Tier | Universe Definition | 1h Drift | 2h Drift | 4h Drift | 8h Drift | 24h Drift | Active Coins |
|---|---|---|---|---|---|---|---|
| **Liquid** | Top 30 by turnover | **+23.9 bps** ($t = +5.0$) | **+23.6 bps** ($t = +3.7$) | **+22.8 bps** ($t = +2.4$) | **+46.3 bps** ($t = +3.9$) | **+87.8 bps** ($t = +2.6$) | 30 |
| **Mid** | Rank 30–120 | **+4.0 bps** ($t = +2.8$) | **+5.1 bps** ($t = +2.5$) | **+7.8 bps** ($t = +2.4$) | **+11.6 bps** ($t = +2.1$) | **+29.0 bps** ($t = +2.4$) | 90 |
| **Small** | Rank 120–300 | +1.2 bps ($t = +0.3$) | +3.1 bps ($t = +0.6$) | +4.0 bps ($t = +0.9$) | +5.1 bps ($t = +1.6$) | +15.9 bps ($t = +1.3$) | 180 |
| **Micro** | Rank 300+ | **−1.4 bps** ($t = -2.7$) | −1.1 bps ($t = -1.4$) | −0.6 bps ($t = -0.6$) | −0.0 bps ($t = -0.0$) | +0.4 bps ($t = +0.2$) | 368 |

*Statistical artifact of pooled vs clustered standard errors on Liquid 24h:*
- Clustered by coin: **+87.8 bps** ($t = +2.6$, 4,841 events across 30 coins)
- Naively pooled: **+135.0 bps** ($t = +37.7$)
- Micro 24h naively pooled: **+5.2 bps** ($t = +447.0$) vs clustered **+0.4 bps** ($t = +0.2$)

*Temporal decay of 8h drift across market regimes:*
- Liquid tier: decayed from **+26.9 bps** ($t = 4.4$, 2020–2024) to **+15.8 bps** ($t = 4.3$, 2025–2026).
- Micro tier: shifted from **+0.3 bps** ($t = 0.1$, 2020–2024) to **−11.2 bps** ($t = -3.3$, 2025–2026).

#### 2. Tick-Level Execution Decomposition (Liquid Tier, 2025–2026)

Evaluated across 40 coins and 214,184 tick-executed trades (`research/reports/tick_layer.md`):

| Decomposition Step | Realized bps / Trade | Cumulative bps |
|---|---|---|
| Theoretical 8h forward drift after spike (excess over random) | **+15.8 bps** ($t = 4.3$) | +15.8 bps |
| What tick engine captures gross (time exit, 10–15% stop) | **+0.9 bps** | +0.9 bps |
| Execution slippage and queue latency drag | −14.9 bps | +0.9 bps |
| Round-trip taker commission | **−10.0 bps** | −9.1 bps |
| 8-hour funding settlement drag | −0.5 bps | **−9.5 bps** |
| Net result with time exit | **−9.5 bps** | **−9.5 bps** |
| Additional penalty when using trailing stop instead of time exit | **−22.9 bps** | **−32.4 bps** |
| Net result with trailing stop | **−32.4 bps** | **−32.4 bps** |

#### 3. Trailing Stop Failure Mechanism (Liquid Tier)

| Exit Architecture | Total Exits | Mean Trade Return | Stopped Trade Share | Break-Even Stop Rate |
|---|---|---|---|---|
| **Stop + Time Exit** | 17,552 time / 338 stop | +0.22% (time) / −10.70% (stop) | **1.9%** | 2.0% |
| **Stop + Trailing** | 17,929 trail / 7,499 stop | +3.07% (trail) / −8.02% (stop) | **29.4%** | 27.7% |

*The trailing stop lifts average winning trade return from +0.22% to +3.07%, but removing the time horizon cap causes the stop-out rate to jump fifteen-fold from 1.9% to 29.4%, pushing it beyond the 27.7% break-even boundary.*

#### 4. Intrabar Resolution Bias Calibration

| Strategy Configuration | 15-Minute Bar Model | 1-Minute Bar Model | Tick Engine Ground Truth | Model Overstatement |
|---|---|---|---|---|
| Long, Trailing Distance = 1.0% | +92 bps | −7 bps (335 trades) | **+6 bps** (332 trades) | **+93 bps overstatement** on 15m |
| Short, Trailing Distance = 2.5% | +19 bps | +57 bps (588 trades) | **+67 bps** (582 trades) | **+10 bps divergence** on 1m |

#### 5. Walk-Forward Stability (Gate G2)

Grid refit across anchored and rolling folds on 15m ticks:
- Whole Panel: Anchored 12m = +6.0 bps ($t = 0.7$); Anchored 6m = **−22.1 bps** ($t = -2.6$); Spread = 28.1 bps.
- Liquid + Mid: Anchored 12m = +4.1 bps ($t = 0.7$); Anchored 6m = **−37.7 bps** ($t = -3.4$); Spread = 41.8 bps.
- **Verdict: Gate G2 FAILED.** Result unstable across walk-forward partitions; multiple testing gate G3 halted.

#### 6. Live Order Validation (`docs/cost_model.md`)

Measured on 3,295 closed trades, 6,637 fills, $65,906 turnover:
- Realized gross PnL before commission: **+1.6 bps per trade**
- Round-trip commission: **−8.5 bps per trade**
- **Actual realized net PnL: −6.9 bps per trade**

#### 7. Benchmark: Multi-Year Daily Breakout with MA Cross Exit (Surviving System)

Evaluated across 79 coins with 6-year history (2021–2026, 7,744 total trades, 20-day high/low breakout, 50-day MA cross exit, 8 ATR emergency stop):

| Calendar Year | bps / Day Held | Profitable Coin Ratio | Total Trades | Long Sleeve (bps/day) | Short Sleeve (bps/day) |
|---|---|---|---|---|---|
| **2021** | **+45.6** | 46 / 79 | 1,151 | +91 | −28 |
| **2022** | **+6.0** | 48 / 78 | 1,421 | −76 | **+26** |
| **2023** | **+7.8** | 50 / 75 | 1,479 | +26 | −3 |
| **2024** | **+12.1** | 47 / 73 | 1,656 | +36 | −17 |
| **2025** | **+0.4** | 23 / 70 | 1,174 | +7 | −3 |
| **2026** | **+13.3** | 51 / 63 | 863 | −48 | **+26** |
| **Summary** | **5 profitable, 1 flat** | **Stable across bear/bull** | 7,744 | Net +36 bps | Net +1 bps |

### Independently reproduced

Not independently reproduced (`research-proposed`). This record captures the source-reported empirical findings and codebase telemetry from `AlexSilka/spike_bot`.

### Negative evidence

- The primary finding of the source is a comprehensive negative result: rule-based volume-spike momentum on intraday crypto perpetuals (15m, 1h, 4h) is non-viable net of trading costs.
- Intraday drift has decayed by ~41% on liquid coins between 2020–2024 (+26.9 bps) and 2025–2026 (+15.8 bps).
- Micro-cap perpetuals exhibit negative momentum drift (−11.2 bps over 8h), causing adverse selection for uninformed spike-following bots.
- Intrabar bar-backtest paths overstate trailing-stop returns by ~93 bps, misleading researchers who do not use tick-level simulation.

## Falsification plan

1. **Out-of-Sample Forward Window Test:** Evaluate the `VolumeSpike` signal on Binance USDT perpetuals post-August 2026.
   - *Falsification Condition:* If net return on liquid top-30 coins remains $\le 0.0$ bps per trade after accounting for Binance VIP 0 taker fees (10 bps round trip), the intraday volume spike thesis remains falsified (`research-defined falsification threshold`).
2. **Aggressor Imbalance vs Raw Volume Test:** Replace raw quote volume with signed aggressor flow (`taker_buy_quote_volume` / total volume) on 1h and 4h bars.
   - *Falsification Condition:* If net 8h drift fails to exceed $2 \times$ the round-trip commission (i.e., $< 20$ bps net), the order-flow refinement fails to salvage intraday momentum (`research-defined falsification threshold`).
3. **Liquidity Inversion Boundary Test:** Measure forward drift across 10 deciles of perpetual turnover.
   - *Falsification Condition:* If the drift slope across turnover deciles is flat or positive in the bottom 50% of names, the liquidity exhaustion hypothesis is disproven (`research-defined falsification threshold`).
4. **Intrabar Resolution Discrepancy Test:** Compare simulated trailing stops on 15m bars vs 1s tick bars across 1,000 synthetic random-walk price paths.
   - *Falsification Condition:* If the 15m bar model diverges from tick simulation by $> 50$ bps, bar-level trailing stops are certified structurally invalid for backtesting (`research-defined falsification threshold`).
5. **Symmetric Daily Breakout Regime Inversion Test:** Run the 20-day breakout system without the short sleeve during a bear regime ($BTC$ drawdown $> 30\%$).
   - *Falsification Condition:* If long-only annual return is negative while symmetric long/short return is positive, the requirement for dual-sleeve regime coverage is verified (`research-defined falsification threshold`).

## Crypto portability

- **Direct:** The strategy, fee models, tick store, and event studies are natively engineered for Binance USDⓈ-M perpetual futures.
- **Microstructural Portability Considerations:**
  - *Funding Rate Settling:* 8-hour funding settlements create discrete carry costs (−0.5 bps average) that must be integrated into intraday holding horizons.
  - *Taker Fee Dominance:* Retail crypto perpetual fees (5 bps per taker side) dwarf the available 15–20 bps statistical drift. Maker-only execution is mandatory for survival.
  - *Liquidation Spikes:* High leverage in altcoins induces sharp, short-lived volume spikes that represent forced liquidations rather than informed drift.

## Limitations

- **Single Exchange Venue:** Empirical measurements are derived exclusively from Binance Futures. Cross-venue dynamics (Bybit, OKX, Hyperliquid) were not evaluated (`data gap`).
- **Single-Position Concurrency Cap:** Backtest models assumed only one active trade per instrument; concurrent signals were dropped, potentially truncating cluster returns (`source-reported limitation`).
- **Low Notional Live Sample:** Live order data was collected with small trade sizes ($10 notional), leaving market impact at institutional scale uncalibrated (`data gap`).
- **Survivorship Panel Truncation:** While 154 delisted coins were included, historical tick data was available for only 40 coins due to storage constraints (`source-reported limitation`).

## Implementation status

`not-implemented`. No implementation in our research stack (`nautilus-quant-system` / PyBroker / NautilusTrader) has been performed. This is a research-only capture of an external empirical study.

## Adoption boundary

Research material only. A record being present in this repository does not mean:
- Profitable
- Validated alpha
- Approved for implementation
- Approved for paper trading
- Approved for testnet
- Approved for live trading

## Related Wiki records

- `[[quant/binance-perpetual-cross-sectional-momentum-taker-cost-falsification-2026-09-13]]` — Arefev (2026) multi-year panel falsification of weekly cross-sectional crypto momentum at taker fees; demonstrates the same retail fee wall across longer horizons.
- `[[quant/crypto-cross-sectional-reversal-momentum-equal-vol-mix-2026-09-13]]` — ccollins80 (2025) study combining low-turnover momentum with short-term reversal on liquid perpetuals.
- `[[quant/crypto-perpetual-order-flow-entropy-microstructure-taker-cost-falsification-2026-09-13]]` — yushingtoncity (2026) order-flow entropy study showing taker cost destruction on Binance perpetuals.
- `[[quant/hyperliquid-perpetual-order-flow-imbalance-depth-elasticity-nonlinearity-2026-09-13]]` — Tejas356 / Rattandeep0500 high-frequency OFI nonlinear depth elasticity.
- `[[quant/crypto-smc-fvg-bpr-liquidity-retracement-random-walk-falsification-2026-09-12]]` — haoyueOuo (2026) empirical falsification of retail ICT / smart-money concepts on crypto.

## Sources

1. Alex Silka (`AlexSilka`), *"spike_bot: Rust trading system for crypto perpetual futures — tick-accurate backtester, memoised grid optimizer, and empirical robustness study,"* GitHub repository, commit `397ed221a6e7accb92641b8b7a7d674ec950c127`, https://github.com/AlexSilka/spike_bot, published August 2026.
2. Alex Silka, *"What works: the study that killed its own strategy,"* `AlexSilka/spike_bot/docs/WHAT_WORKS.md`, commit `397ed221a6e7accb92641b8b7a7d674ec950c127`.
3. Alex Silka, *"Robustness study plan: pre-registered gating, panel optimization, and multiple testing,"* `AlexSilka/spike_bot/docs/ROBUSTNESS_PLAN.md`, commit `397ed221a6e7accb92641b8b7a7d674ec950c127`.
4. Alex Silka, *"The tick-level exit layer — G2 and the decomposition of the edge,"* `AlexSilka/spike_bot/research/reports/tick_layer.md`, commit `397ed221a6e7accb92641b8b7a7d674ec950c127`.
5. Alex Silka, *"The cost model, measured on live orders,"* `AlexSilka/spike_bot/research/reports/cost_model.md`, commit `397ed221a6e7accb92641b8b7a7d674ec950c127`.
6. Alex Silka, *"G1 — event study: is there drift after a spike,"* `AlexSilka/spike_bot/research/reports/event_study_15m.md`, commit `397ed221a6e7accb92641b8b7a7d674ec950c127`.
7. Alex Silka, *"Which exit to trade a daily breakout with,"* `AlexSilka/spike_bot/research/reports/exit_search.md`, commit `397ed221a6e7accb92641b8b7a7d674ec950c127`.
8. Alex Silka, *"Higher timeframes: 1h / 4h / 1d, with stops in ATR units,"* `AlexSilka/spike_bot/research/reports/tf_search.md`, commit `397ed221a6e7accb92641b8b7a7d674ec950c127`.
9. Alex Silka, *"The 1m bar model against the tick engine,"* `AlexSilka/spike_bot/research/reports/sweep_1m_calibration.md`, commit `397ed221a6e7accb92641b8b7a7d674ec950c127`.
10. Alex Silka, *"Cutting Binance USDⓈ-M futures fees: measured against live telemetry,"* `AlexSilka/spike_bot/docs/FEE_REDUCTION.md`, commit `397ed221a6e7accb92641b8b7a7d674ec950c127`.
