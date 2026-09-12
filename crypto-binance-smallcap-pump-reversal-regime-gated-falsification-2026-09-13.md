---
schema: strategy-research-record-v1
title: "Binance Perpetual Small-Cap Pump Reversal: Regime-Gated 72-Hour Short Mean Reversion and 29-Experiment Falsification Audit"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - mean-reversion
  - small-cap
  - pump-and-dump
  - negative-results
  - falsification
  - regime-gating
status: research-only
confidence: high
source_as_of: 2026-08-16
sources:
  - "Chirag Agarwal, 'Small-cap pump reversal: deployed rule, causal backtest, and experiment audit trail', GitHub repository, commit 12e7227a0757ea855a995713be31c4c94b9c8d1f, published 2026-08-16, accessed 2026-09-13. https://github.com/agarwalchirag535-lab/smallcap-pump-reversal"
  - "Primary strategy specification: https://github.com/agarwalchirag535-lab/smallcap-pump-reversal/blob/main/docs/strategy_spec.md"
  - "Research journey & experiment audit trail: https://github.com/agarwalchirag535-lab/smallcap-pump-reversal/blob/main/experiments/README.md"
  - "Core strategy code: https://github.com/agarwalchirag535-lab/smallcap-pump-reversal/blob/main/src/strategy.py"
  - "Causal backtest engine: https://github.com/agarwalchirag535-lab/smallcap-pump-reversal/blob/main/src/backtest.py"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Binance Perpetual Small-Cap Pump Reversal: Regime-Gated 72-Hour Short Mean Reversion and 29-Experiment Falsification Audit

## Provenance

- **Repository:** https://github.com/agarwalchirag535-lab/smallcap-pump-reversal
- **Author:** Chirag Agarwal (`agarwalchirag535-lab`)
- **Full Commit SHA:** `12e7227a0757ea855a995713be31c4c94b9c8d1f` (`source-reported`)
- **Primary Source Files:**
  - `README.md` (overview, causal backtest summary, and forward-test protocol)
  - `docs/strategy_spec.md` (formal strategy parameters, execution, and universe criteria)
  - `docs/research_summary.md` (synthesis of research path E-003 through E-025)
  - `src/strategy.py` (`SignalEngine` class and live scanning implementation)
  - `src/backtest.py` (event-driven causal backtester with 1-minute stop auditing)
  - `data/universe_143.csv` (143 profile-screened tradeable Binance USDT-M perpetual contracts)
  - `data/bad_coins.csv` (58 excluded coins with specific structural rationales)
  - `experiments/README.md` and 29 individual experiment outcome dossiers (`experiments/E-*/OUTCOME.md`)
  - `results/backtest_2025_2026.csv` (complete 694-trade causal backtest log)
- **License:** MIT License (`source-reported`)
- **Commit Date:** 2026-08-16T06:29:33Z (`source-reported`)
- **Primary Sample Period:** January 1, 2025 to July 15, 2026 (19 months); 2024 post-election bull run used as hostile out-of-sample stress period (`source-reported`).
- **Venue & Market Type:** Binance USDT-Margined Perpetual Futures (FAPI public endpoints) (`source-reported`).
- **Repository Deduplication Check:** Comprehensive search across `alpha-strategy-research` confirmed zero prior records citing `agarwalchirag535-lab`, `smallcap-pump-reversal`, Chirag Agarwal, commit `12e7227a`, or this specific multi-gate short reversal rule. While adjacent records examine retail contrarian flows (`retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11.md`) or on-chain Telegram pump dumps (`telegram-coordinated-pump-dump-detection-contrarian-fade-2026-09-13.md`), this record is unique in providing an extensive empirical falsification audit across 29 pre-registered experiments that systematically disproves ML meta-labeling, order flow, 1-minute microstructure conditioning, and funding-rate gating in crypto small-cap reversals.

## Economic mechanism

### Source-reported

The primary author frames the strategy around retail FOMO-driven price overextension in low-liquidity crypto assets:
1. **Unwinding of Trapped Longs:** Small-cap altcoin perpetual contracts experiencing rapid +25% price surges over 24 hours driven by speculative momentum create fragile, levered long positioning. Once the initial buying frenzy exhausts and volume drops, trapped retail longs unwind or face cascading stop-outs, driving downward mean reversion over a 1–3 day horizon.
2. **Failure of Conditioning Signals:** The author demonstrates across 29 pre-registered experiments that the edge is **population-level** rather than predictable at the individual trade level. Microstructure, order flow, ML meta-labeling, and funding rates fail to forecast which specific pump will reverse versus squeeze. Instead, the edge survives only when applied systematically to a universe screened strictly on stable asset *character* (liquidity, realized volatility, listing age) rather than past returns.
3. **Macro Regime Dominance:** Altcoin reversals fail catastrophically during macro Bitcoin bull markets. When Bitcoin rallies aggressively (30-day return ≥ +30%) or enters an immediate post-correction recovery phase (BTC 30-day negative but 7-day > +3%), market-wide beta overwhelms idiosyncratic mean reversion, causing altcoin pumps to continue upward into massive short squeezes.

### Research interpretation

This strategy captures a structural **retail overreaction and liquidity exhaustion premium** subject to severe **macro regime conditioning**:
1. **Idiosyncratic Overextension vs. Market Beta:** Small-cap pumps represent idiosyncratic retail mania only when Bitcoin is sideways or consolidating. In strong market-wide bull regimes or sharp market-wide recoveries, capital rotates aggressively into high-beta altcoins, converting exhaustion points into momentum breakouts. The BTC 30-day and 7-day dual regime gates act as an essential macro liquidity filter.
2. **Negative Confirmation Cost:** The source's finding that technical confirmation filters (e.g., waiting for close < EMA9 and negative MACD histogram) destroy profitability—despite halving stop-out rates—is economically significant: mean reversion in crypto small-caps is heavily front-loaded in the first few hours post-climax. Waiting for lagging confirmation forfeits more alpha than it saves in tail-risk reduction.
3. **Overfitting Trap of ML Meta-Labeling:** The source's negative findings regarding LightGBM meta-labeling (OOF AUC 0.42–0.48) highlight a pervasive pitfall in quantitative crypto research: pre-signal features easily overfit in-sample to historical squeeze paths (IS AUC > 0.90) but exhibit zero out-of-fold generalization.

## Signal

### Source-reported

The production signal (`v6`) is an hourly event-driven rule executed across the screened 143-coin universe. All conditions must be satisfied simultaneously at the close of hourly bar $t$ (UTC):

1. **Universe Filter:** Coin must be present in `data/universe_143.csv` (`source-reported`):
   - Daily quote volume: $2M to $30M USD
   - Realized daily volatility (`rvol`): $\le 0.075$
   - Extreme-day fraction: $\le 0.003$
   - Listing history: $\ge 180$ days on Binance
   - Non-inclusion in `data/bad_coins.csv` (58 excluded zombie/manipulated or high-stop coins)
2. **Pump Magnitude Signal:**
   $$\text{ret\_24h} = \frac{\text{close}[t]}{\text{close}[t-24]} - 1 \ge +0.25 \quad (+25\%) \quad (\text{source-reported})$$
3. **Volume Confirmation:**
   $$\text{vol\_pct} = \text{percentile\_rank}(\text{qvol}[t], \text{trailing } 168\text{h}) \ge 0.50 \quad (\text{source-reported})$$
   (Current bar's quote volume must be in the top 50% of its trailing 7-day hourly volume distribution).
4. **Macro BTC Regime Gate:**
   $$\text{btc\_30d} = \frac{\text{BTC\_close}[t]}{\text{BTC\_close}[t-720]} - 1 < +0.30 \quad (+30\%) \quad (\text{source-reported})$$
   (Skip all signals if Bitcoin has appreciated $\ge +30\%$ over the trailing 30 days).
5. **Macro BTC Recovery Gate:**
   $$\text{SKIP if } (\text{btc\_30d} < 0.00 \text{ AND } \text{btc\_7d} > +0.03) \quad (\text{source-reported})$$
   where $\text{btc\_7d} = \frac{\text{BTC\_close}[t]}{\text{BTC\_close}[t-168]} - 1$.
   (Skip signals when BTC is down over 30 days but surging $> +3\%$ over 7 days).
6. **Per-Coin Cooldown:** Minimum 24 hours between successive signals on the same coin (`source-reported`).
7. **Execution Timing:** Enter **SHORT** at the **OPEN of bar $t+1$** (strictly causal next-bar execution) (`source-reported`).
8. **Protective Stop-Loss:**
   $$\text{stop\_price} = \text{entry\_price} \times 1.25 \quad (+25\% \text{ above entry}) \quad (\text{source-reported})$$
   Evaluated continuously at 1-minute resolution (or if bar `high` $\ge \text{stop\_price}$). Exit immediately at `stop_price`.
9. **Scheduled Time Exit:** Hold for exactly 72 hours (72 hourly bars). Exit at the **OPEN of bar $t+73$** (`source-reported`).

### Research interpretation

The signal combines:
- A cross-sectional character screen (calm, liquid, non-zombie small-caps),
- An extreme short-term impulse detector (+25% in 24h with volume expansion),
- A multi-scale macro trend and recovery filter (BTC 30d and 7d), and
- A wide stop / fixed-horizon holding period (72h).

The rule set is fully specified with zero discretionary parameters.

## Required data

### Source-reported

- **Instrument Universe:** 143 USDT-Margined perpetual contracts on Binance (`data/universe_143.csv`).
- **Benchmark / Context Instrument:** `BTCUSDT` perpetual futures.
- **Timeframe:** Hourly (`1h`) OHLCV bars for signal generation; 1-minute (`1m`) high/low bars for stop-loss monitoring (`source-reported`).
- **Fields:** Timestamp (`t`), Open (`open`), High (`high`), Low (`low`), Close (`close`), Volume (`volume`), Quote Volume (`qvol`).
- **Point-in-Time Availability:** Binance REST endpoint `/fapi/v1/klines`. Closes are stamped at bar close; entry is strictly on bar $t+1$ open. Volume percentile uses strictly trailing 168 bars ($t-168$ to $t-1$) (`source-reported`).
- **Missing Data Handling:** Coins with fewer than 170 bars of history or missing volume data are skipped (`source-reported`).

### Research interpretation

All required data can be acquired using public REST endpoints without authenticated private keys. Historical backtesting requires 1-minute resolution data across the 143 coins to evaluate intraday stop breaches accurately without intrabar interpolation bias.

## Execution assumptions

### Source-reported

- **Order Types:** Market order at bar $t+1$ open for entry; stop-market order at $1.25 \times \text{entry}$ for stop; market order at bar $t+73$ open for scheduled exit (`source-reported`).
- **Execution Fee & Slippage:** Modelled as a flat **30 bps per side (60 bps round-trip)** deducted directly from trade P&L (`source-reported`):
  $$\text{pnl\_bps} = -\left(\frac{\text{exit\_price}}{\text{entry\_price}} - 1\right) \times 10{,}000 - 60 \quad (\text{source-reported})$$
- **Fill Price:** Stop fills assume execution exactly at `stop_price` ($1.25 \times \text{entry}$). Scheduled exits fill at bar open (`source-reported`).
- **Funding Rates:** Omitted in the backtest engine (`source-reported`). Author notes this is conservative for shorts, as pumped coins typically trade at positive funding rates where shorts receive payments.
- **Position Sizing:** 1% of portfolio equity notional per position (`source-reported`).
- **Concurrency Cap:** Maximum 5 simultaneous open positions (`source-reported`). Gross book exposure capped at 5% of portfolio equity.
- **Circuit Breakers:**
  - Daily: Halt trading if portfolio experiences $-3\%$ drawdown in a single day (`source-reported`).
  - Monthly: Halve position sizes if portfolio experiences $-5\%$ drawdown in a calendar month (`source-reported`).

### Research interpretation

- The 60 bps round-trip cost model is realistic for Binance VIP 0 taker tiers (50 bps base taker) or VIP 1-2 with minor slippage.
- The assumption that stop orders fill exactly at $+25\%$ without slippage during a fast short squeeze represents an operational risk; in fast-moving small caps, gap-ups or illiquid order books could cause slippage beyond 25% (`research-proposed`).
- Funding cost omission is generally favorable to shorts in crypto bull/pump regimes, but during negative funding squeezes shorts can pay severe funding penalties; formal accounting must incorporate funding cash flows (`research-proposed`).

## Evidence

### Source-reported

The primary author reports the following backtest metrics across January 1, 2025 to July 15, 2026 (19 months, 143 coins, net of 60 bps fees) (`source-reported`):

| Metric | Source-Reported Value | Source Reference |
|---|---|---|
| Total Trades | 694 trades (across 134 distinct coins) | `README.md`, `results/backtest_2025_2026.csv` |
| Mean P&L per Trade | **+608 bps** (+6.08% net) | `README.md`, Table 1 |
| Median P&L per Trade | **+982 bps** (+9.82% net) | `README.md`, Table 1 |
| Win Rate | **72.9%** | `README.md`, Table 1 |
| Stop-Out Rate | **16.3%** | `README.md`, Table 1 |
| Positive Months | **17 / 19 months (89.5%)** | `README.md`, Table 1 |
| Cumulative Return | **+42.2%** (at 1% notional / trade, max 5 positions) | `README.md`, Table 1 |
| Unfiltered Baseline Mean | +170 bps (on 213 unscreened coins) | `experiments/README.md` (E-003–E-007) |
| Filtered Universe Mean | +495 bps (post zombie removal) | `experiments/README.md` (E-012–E-014) |
| Unified v6 with Recovery Gate | +608 bps (final deployed rule) | `docs/strategy_spec.md`, `results/` |

### Independently reproduced

Not independently reproduced. All metrics above represent primary author reported results from repository commit `12e7227a0757ea855a995713be31c4c94b9c8d1f`. Internal reproduction in PyBroker or NautilusTrader has not yet been conducted.

### Negative evidence & 29-experiment falsification audit

The primary contribution of this repository is its transparent documentation of **failed hypotheses and killed variants** across 29 pre-registered experiments (`source-reported`):

1. **Machine Learning Meta-Labeling Falsification (E-010):**
   - Hypothesis: A LightGBM / Logistic classifier trained on pre-signal OHLCV features can separate profitable reversals from squeezes.
   - Result: In-sample AUC was 0.918 (severe overfitting), while out-of-fold (OOF) AUC was **0.421** (worse than random chance). Falsified; ML meta-labeling caught catastrophic false positives.
2. **Hourly Order Flow Failure (E-011):**
   - Hypothesis: Adding taker buy/sell ratio and funding rates to the meta-labeling model distinguishes reversals from continuations.
   - Result: OOF AUC moved from 0.421 to **0.442** (pure noise). Both Logistic and LightGBM failed all pre-registered kill gates ($K_1$ through $K_7$). Falsified.
3. **1-Minute Microstructure Feature Engineering Failure (E-018):**
   - Hypothesis: 15 formal microstructure features (Order Flow Imbalance, Amihud illiquidity, Kyle's lambda, Roll effective spread, realized bipower jump variation, return-sign entropy) over pre-signal 6h windows can predict reversal success.
   - Result: In-sample AUC was 0.885; OOF AUC was **0.483** (random). Confirmed that failure to condition reversals is fundamental, not a feature-resolution artifact.
4. **Funding-Rate Gate Failure (E-2026-07-17-002):**
   - Hypothesis: Higher perpetual funding rates reflect crowded long positioning and predict stronger downward reversals.
   - Result: Across 695 signals, **Spearman correlation between funding and net return was $-0.050$ ($p = 0.186$, null)**. Signals with funding $\le 0$ yielded $+531$ bps (stop rate 10.2%), while signals with funding $> 0$ yielded $+368$ bps (stop rate 13.9%). Funding gate failed.
5. **Technical Confirmation Entry + Tight Stop Failure (E-2026-07-17-005):**
   - Hypothesis: Waiting for reversal confirmation (close < EMA9 and MACD histogram < 0) allows a tighter 10% stop, cutting tail losses.
   - Result: Maximum Adverse Excursion confirmed that 75% of trades stayed under $+10\%$ squeeze after confirmation, and stop rates dropped to 5.6%. However, waiting an average 7.5 hours sacrificed front-loaded reversal gains. Net return collapsed from **+442 bps (baseline)** to **+135 bps (confirmation + 10% stop)**.
6. **AI Foundation Model Directional Filter Failure (E-2026-07-17-007):**
   - Hypothesis: Kronos pretrained K-line foundation model predicting next 3 candles can filter losing shorts.
   - Result: Strong in-sample correlation ($\rho = +0.199$) and 2024 holdout correlation ($\rho = +0.228$) collapsed to **$\rho = +0.011$ ($p = 0.45$, pure null)** and directional accuracy of **50.3% (random)** on unseen coins. Diagnosed as pre-training data memorization / look-ahead leakage.
7. **Delayed Intraday Peak Catch Entry Failure (E-2026-07-17-001):**
   - Waiting for intraday peak formation deteriorated Sharpe and net returns compared to immediate entry at bar $t+1$ open.
8. **Unscreened Coin Generalization Failure (E-008, BLUR universe):**
   - Deploying the signal on arbitrary unseen coins without character screening failed completely, showing that the alpha does not generalize without liquidity/volatility gating.
9. **Macro Bull Market Hostile Failure (2024 Sample):**
   - During the post-US election crypto rally in late 2024, small-cap pumps continued upward in massive short squeezes, establishing that the strategy requires macro BTC trend gating.

## Falsification plan

### Source-reported forward test

The primary author established an active paper-forward test (`experiments/E-2026-07-18-001_deployed_forward_test/`) on Binance with fixed pre-registered criteria (`source-reported`):

- **PASS Condition:** $n \ge 30$ trades, mean P&L $\ge +150$ bps, 95% bootstrap CI lower bound $\ge 0$, stop-out rate $\le 25\%$.
- **KILL Condition:** Mean P&L $< 0$ bps OR stop-out rate $> 30\%$.
- **INCONCLUSIVE:** Any other result $\rightarrow$ extend evaluation window to $n = 100$ trades or 90 calendar days.

### Research-defined falsification protocol

To independently evaluate this hypothesis within our own research pipeline, the following stress tests are declared (`research-proposed`):

1. **Point-in-Time Universe & Survivorship Audit:** Test whether the 143-coin universe selected as of mid-2026 suffers from survivorship bias by reconstructing a rolling point-in-time quarterly universe based strictly on trailing 180-day volume and realized volatility (`research-proposed`).
   - *Falsification threshold:* Strategy Sharpe drops below 0.50 or mean net trade return falls below $+100$ bps under dynamic point-in-time universe reconstitution (`research-defined falsification threshold`).
2. **Severe Short-Squeeze Slippage Stress Test:** Model execution slippage of 200–500 bps on stop-loss triggers rather than assuming frictionless fills at exactly $+25\%$ (`research-proposed`).
   - *Falsification threshold:* Strategy cumulative return turns negative when stop orders incur $\ge 200$ bps slippage (`research-defined falsification threshold`).
3. **Cross-Exchange Porting Test:** Evaluate the exact same signal rules on Bybit and OKX USDT-M perpetual contracts (`research-proposed`).
   - *Falsification threshold:* Failure to achieve a statistically significant positive mean return ($t \ge 2.0$) across non-Binance venues (`research-defined falsification threshold`).
4. **Funding Rate Cost Realism:** Integrate exact historical 8-hour funding cash flows into all trade P&L calculations (`research-proposed`).
   - *Falsification threshold:* Net mean P&L degrades by more than 200 bps after deducting actual funding debits (`research-defined falsification threshold`).

## Crypto portability

- **Portability Status:** `direct` (`source-reported`).
- The mechanism is natively researched and implemented directly on crypto assets (Binance USDT-M perpetual contracts).
- **Perpetual Contract Mechanics:** Highly applicable. Crypto perpetuals feature continuous 24/7 trading, high retail leverage participation, and frequent short-term speculative pumps.
- **Cross-Venue Considerations:** While tested natively on Binance, porting to Bybit, OKX, or Hyperliquid requires verifying:
  1. Minimum tick size and contract multipliers,
  2. Venue-specific funding settlement schedules (Binance 8h vs. Hyperliquid 1h),
  3. Liquidity depth on small caps to avoid market impact upon entry/exit.

## Limitations

- **Hostile Regime Vulnerability:** The strategy is structurally vulnerable to strong crypto bull markets and altcoin seasons. Despite the BTC 30d and 7d filters, rapid market-wide rallies can trigger clustered $-25\%$ stop-outs across all concurrent positions (`source-reported`).
- **Static Universe Selection:** The primary backtest uses a fixed 143-coin list screened over the full sample, introducing potential look-ahead / conditioning bias in coin selection (`source-reported`).
- **Uncapped Tail Risk on Gapping:** While a $+25\%$ stop is placed, low-liquidity small-cap perps can gap up violently during coordinated manipulation or exchange listing news, potentially leading to catastrophic fill slippage beyond $+25\%$ (`research-proposed`).
- **Exchange Counterparty & De-Listing Risk:** Small-cap perpetuals on Binance are frequently subjected to sudden leverage reductions, margin tier changes, or de-listings (`research-proposed`).
- **Unmodelled Funding Rates:** Historical funding payments were omitted from the backtest engine (`source-reported`).

## Implementation status

- `not-implemented` (`source-reported`).
- This research capture represents an audited evaluation of external public research. No strategy logic has been implemented in PyBroker or NautilusTrader, and no live or paper capital has been deployed in our execution systems.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`
- This record serves as candidate research material for Hermes Research Loop A. It does not constitute approval for live trading, testnet, paper trading, or production deployment.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]`
- `[[quant/crypto-cross-sectional-last-day-return-reversal-liquidity-conditioned-2026-08-31]]`
- `[[quant/crypto-medium-term-cross-sectional-reversal-lmw-2026-09-11]]`
- `[[quant/crypto-perp-crowded-flush-reversal-microstructure-2026-09-12]]`
- `[[quant/crypto-perpetual-pairs-trading-kalman-cointegration-falsification-2026-09-11]]`
- `[[quant/crypto-cross-venue-funding-carry-negative-results-cost-decay-2026-09-13]]`
- `[[quant/telegram-coordinated-pump-dump-detection-contrarian-fade-2026-09-13]]`
- `[[quant/bitcoin-negative-funding-contrarian-reversal-2026-08-31]]`

## Sources

1. Chirag Agarwal, *"Small-cap pump reversal: deployed rule, causal backtest, and experiment audit trail"*, GitHub repository, commit `12e7227a0757ea855a995713be31c4c94b9c8d1f`, created and published 2026-08-16, accessed 2026-09-13. URL: [https://github.com/agarwalchirag535-lab/smallcap-pump-reversal](https://github.com/agarwalchirag535-lab/smallcap-pump-reversal).
2. Primary strategy specification: `docs/strategy_spec.md` in repository `agarwalchirag535-lab/smallcap-pump-reversal` at commit `12e7227a0757ea855a995713be31c4c94b9c8d1f`. URL: [https://github.com/agarwalchirag535-lab/smallcap-pump-reversal/blob/main/docs/strategy_spec.md](https://github.com/agarwalchirag535-lab/smallcap-pump-reversal/blob/main/docs/strategy_spec.md).
3. Research journey summary and experiment audit index: `docs/research_summary.md` and `experiments/README.md` at commit `12e7227a0757ea855a995713be31c4c94b9c8d1f`.
4. Core signal engine implementation: `src/strategy.py` at commit `12e7227a0757ea855a995713be31c4c94b9c8d1f`.
5. Causal event-driven backtesting engine: `src/backtest.py` at commit `12e7227a0757ea855a995713be31c4c94b9c8d1f`.
6. Empirical trade log (694 trades): `results/backtest_2025_2026.csv` at commit `12e7227a0757ea855a995713be31c4c94b9c8d1f`.
7. Pre-registered experiment outcome reports:
   - `experiments/E-2026-07-14-010_smallcap_meta_labeling/OUTCOME.md` (ML meta-labeling failure)
   - `experiments/E-2026-07-14-011_orderflow_meta_label/OUTCOME.md` (Hourly order flow failure)
   - `experiments/E-2026-07-14-018_onemin_microstructure/OUTCOME.md` (1-min microstructure failure)
   - `experiments/E-2026-07-17-002_smallcap_funding_gate/OUTCOME.md` (Funding-rate gate null)
   - `experiments/E-2026-07-17-005_confirm_entry_tight_stop/OUTCOME.md` (Confirmation entry & tight stop trade-off)
   - `experiments/E-2026-07-17-007_kronos_direction_filter/OUTCOME.md` (Kronos foundation model failure on clean holdout)
