---
schema: strategy-research-record-v1
title: "Binance Crypto Perpetual Order-Flow and Sign Entropy Microstructure Direction and Taker Cost Falsification"
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - market-microstructure
  - order-flow-imbalance
  - shannon-entropy
  - taker-fee-wall
  - falsification
  - negative-evidence
  - pre-registered
status: research-only
confidence: high
source_as_of: 2026-08-31
sources:
  - "https://github.com/yushingtoncity/market-entropy/tree/06db3d1c6d5eb2d29d4bea94b0af704a80c8f557"
  - "https://github.com/yushingtoncity/market-entropy/blob/06db3d1c6d5eb2d29d4bea94b0af704a80c8f557/report/v3_research_note.md"
  - "https://github.com/yushingtoncity/market-entropy/blob/06db3d1c6d5eb2d29d4bea94b0af704a80c8f557/report/v2b_predictive_study.md"
  - "https://github.com/yushingtoncity/market-entropy/blob/06db3d1c6d5eb2d29d4bea94b0af704a80c8f557/report/v2b_design.md"
  - "https://github.com/yushingtoncity/market-entropy/blob/06db3d1c6d5eb2d29d4bea94b0af704a80c8f557/report/v2a_tardis_dataset.md"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Binance Crypto Perpetual Order-Flow and Sign Entropy Microstructure Direction and Taker Cost Falsification

## Provenance

- **Primary Source Repository:** `yushingtoncity/market-entropy` (*Pre-registered market microstructure study: order-flow features predict short-horizon crypto returns out of sample, nothing survives taker costs, and entropy adds nothing beyond flow*), authored by `yushingtoncity` (`source-reported`).
- **Canonical Source Identity:** GitHub repository `https://github.com/yushingtoncity/market-entropy` at immutable head commit `06db3d1c6d5eb2d29d4bea94b0af704a80c8f557` (authored 2026-08-31T03:51:51Z), with pre-registration frozen at commit `6e65063ad9d2816819cc01812137b7f89a116ea6` (dated 2026-08-22).
- **Core Research Artifacts in Repository:**
  - `report/v3_research_note.md`: Synthesized research memo summarizing findings, data validation, and economic interpretation.
  - `report/v2b_predictive_study.md`: Complete 1,020-configuration report documenting return predictability, volatility forecasting, entropy ablation, and cost survival.
  - `report/v2b_design.md`: Pre-registered study specification committed before any model fitting.
  - `report/v2a_tardis_dataset.md`: Tick-level data provenance, quote/trade schemas, and cleaning/validation protocols.
  - `run_v2b.py`: Deterministic study runner executing all configurations with fixed seeds (`random_state=42`).
  - `src/signals/generator.py`: Initial v0 rule-based regime-shift signal generator.
- **Dataset and Coverage:** Tick-level Binance USDT-margined perpetual futures (`BTCUSDT` and `ETHUSDT`) from Tardis.dev open archive covering the 1st calendar day of each month from 2023-01 to 2026-08 (44 candidate months; 87 valid day-symbols, 1 excluded due to a 60.2 s quote gap). Aggregated to 1-second bars with microseconds precision (`source-reported`).
- **Repository Deduplication Audit:** Pre-write search across all records in `alpha-strategy-research` confirmed zero existing records citing `yushingtoncity`, `market-entropy`, commit `06db3d1`, or commit `6e65063`. Adjacent microstructure and order-flow records evaluate fundamentally different datasets, mechanisms, or venues:
  - `crypto-order-flow-online-sgd-microstructure-horizon-cost-falsification-2026-09-13.md` (Patil 2026, `jarvisss007/crypto-microstructure`) evaluates continuous 1-minute to 15-minute online SGD learning on Coinbase spot `BTC-USD` over 38 continuous days in July–August 2026.
  - `order-flow-imbalance-predictive-decoupling-cost-falsification-2026-09-12.md` (Mungale 2026, `Tejas356/limit_order_book_engine`) evaluates C++ NASDAQ equity LOBSTER data (INTC/GOOG) on single-day Level-10 book reconstruction.
  - `retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11.md` evaluates retail CVD divergences and funding extremes rather than sub-minute tick-level OFI and Shannon entropy.
  - `hyperliquid-perpetual-order-flow-imbalance-depth-elasticity-nonlinearity-2026-09-13.md` tests nonlinear depth elasticity on Hyperliquid L2 books rather than pre-registered multi-horizon tick OFI and entropy ablation on Binance.

## Economic mechanism

### Source-reported

1. **Order-Flow Price Impact:** Microstructure theory (Cont, Kukanov & Stoikov 2014) posits that contemporaneous order-flow imbalance (OFI) drives price revisions through queue depletion and adverse selection. In high-frequency perpetual crypto markets, aggressive buyer/seller arrival imbalance creates short-term price momentum as market makers adjust quotes.
2. **Shannon Entropy as Directional Regime Filter:** The author originally hypothesized that the Shannon entropy of recent trade signs (buyer vs seller aggressor flow) measures the degree of directional coordination or information asymmetry among market participants. Low entropy (high concentration of one-sided trade signs) was hypothesized to signal informed, persistent directional runs, whereas high entropy (near 1.0) reflects balanced two-sided noise trading.
3. **The Microstructure Taker Cost Wall:** While order-flow features display statistically consistent out-of-sample directional correlation over 1–60 second horizons, the absolute magnitude of the expected price move is mechanically bounded by the tick size and book depth of ultra-liquid perpetuals. Because aggressive directional traders must cross the spread and pay exchange taker fees, the cost to extract this edge exceeds the gross informational value by an order of magnitude.

### Research interpretation

This study serves as a clean, pre-registered empirical falsification of two widely held quantitative trading hypotheses:
- **Hypothesis 1 (Entropy Alpha — Refuted):** Rolling Shannon entropy of trade signs does *not* carry independent predictive information beyond standard linear and nonlinear order-flow variables (OFI, queue imbalance, signed volume). In walk-forward testing, adding 60-second sign entropy changes out-of-sample $R^2$ by $-0.0002$ percentage points (OLS), proving to be an economically redundant non-linear transformation.
- **Hypothesis 2 (Taker Order-Flow Predictability — Falsified for Alpha Extraction):** Out-of-sample directional predictability is statistically real ($R^2 \approx 2.6\% - 3.6\%$ at 1 second, sign accuracy $\approx 69\% - 76\%$ on non-zero bars), but economically untradeable via taker orders. The breakeven transaction cost is $0.17 - 0.33$ bps per turn, whereas the lowest Binance retail taker fee tier is $4.0 - 5.0$ bps (and institutional maker/taker crossing costs exceed $2.0$ bps). Therefore, gross order-flow predictability represents a structural property of market-maker quoting rather than an extractable directional taker alpha.

## Signal

### Signal Features and Construction

Features are computed on 1-second uniform bar aggregations from tick-by-tick quote and trade records:
- `ofi_1s`: Best-level order-flow imbalance summed over the 1-second bar following Cont, Kukanov & Stoikov (2014) (`source-reported`):
  $$e_n = I_{\{p_n^b \ge p_{n-1}^b\}} q_n^b - I_{\{p_n^b \le p_{n-1}^b\}} q_{n-1}^b - I_{\{p_n^a \le p_{n-1}^a\}} q_n^a + I_{\{p_n^a \ge p_{n-1}^a\}} q_{n-1}^a$$
- `ofi_5s`, `ofi_30s`: Trailing rolling sums of `ofi_1s` over 5 and 30 seconds (`source-reported`).
- `qi`: Time-weighted Level-1 queue imbalance $(q^b - q^a) / (q^b + q^a)$ sampled on a 100 ms forward-filled grid (`source-reported`).
- `dqi_1s`: First difference in queue imbalance $qi_t - qi_{t-1}$ (`source-reported`).
- `sv_1s`: Signed trade volume in the bar, signed by verified aggressor side (buy $= +1$, sell $= -1$) (`source-reported`).
- `sv_30s`: Trailing 30-second rolling sum of signed volume (`source-reported`).
- `tc_1s`: Trade count in the 1-second bar (`source-reported`).
- `spread_bps`: Time-weighted bid-ask spread in basis points of midprice (`source-reported`).
- `entropy_60s`: Shannon entropy of aggressor trade signs over trailing 60 seconds, computed from bar-level $\text{sign}(sv_{1s})$, normalized by $\log_2(2)$ to lie in $[0, 1]$ (`source-reported`):
  $$H = -\sum_{s \in \{+1, -1\}} p_s \log_2(p_s) / \log_2(2)$$
  If fewer than 10 of the trailing 60 bars have non-zero signed volume, $H$ defaults to $1.0$ (`source-reported`).

### Ablation Grouping

- **Group 1 (G1 - OFI only):** `ofi_1s`, `ofi_5s`, `ofi_30s` (`source-reported`).
- **Group 2 (G2 - Order Flow & Book):** G1 + `qi`, `dqi_1s`, `sv_1s`, `sv_30s`, `tc_1s`, `spread_bps` (`source-reported`).
- **Group 3 (G3 - Full Feature Set + Entropy):** G2 + `entropy_60s` (`source-reported`).

### Predictive Models and Horizons

- **Horizons ($h$):** $h \in \{1, 5, 10, 30, 60\}$ seconds forward log midprice return:
  $$r_{t \to t+h} = \ln(p^{\text{mid}}_{t+h}) - \ln(p^{\text{mid}}_t)$$
- **Model Architectures:**
  1. Ordinary Least Squares (OLS) via `numpy.linalg.lstsq` (`source-reported`).
  2. Logistic Regression on return sign via `sklearn.linear_model.LogisticRegression(C=1.0, solver='lbfgs')` (`source-reported`).
  3. HistGradientBoostingRegressor (HGB) with fixed, untuned parameters (`max_iter=100`, `learning_rate=0.1`, `max_leaf_nodes=31`, `min_samples_leaf=200`, `l2_regularization=1.0`) (`source-reported`).

### Trading Rule and Decision Policy

- **Decision Cadence:** Non-overlapping $h$-bar steps within each test day (`source-reported`).
- **Execution Timing:** One-bar delay — signal formed at end of bar $t$ fills at the first midprice of bar $t+1$ (`source-reported`).
- **Threshold Policy:** Position $p_t \in \{-1, 0, +1\}$ assigned as:
  $$p_t = \begin{cases} +1 & \text{if } \hat{r}_{t \to t+h} > c \cdot (\text{half\_spread}_t + \text{fee}) \\ -1 & \text{if } \hat{r}_{t \to t+h} < -c \cdot (\text{half\_spread}_t + \text{fee}) \\ 0 & \text{otherwise} \end{cases}$$
  where $c \in \{0.5, 1.0, 2.0\}$, $\text{half\_spread}_t = \text{multiplier} \cdot (\text{spread\_bps}_t / 2)$ with multiplier $\in \{0.5, 1.0, 2.0\}$, and fee $\in \{0.0, 2.5, 5.0\}$ bps (`source-reported`).
- **Position Sizing:** Unit fixed position $p \in \{-1, 0, +1\}$ (`source-reported`). Sizing scaling by predicted return or volatility: `research-proposed`.
- **EOD Exit:** Positions closed at the final bar of the day with turnover fee applied (`source-reported`).

## Required data

- **Instruments:** `BTCUSDT` and `ETHUSDT` perpetual futures (`source-reported`).
- **Venue:** Binance USDT-margined perpetual contract market (`source-reported`).
- **Raw Data Feed:** Tardis.dev public downloadable CSV files (`quotes` and `trades` channels) (`source-reported`).
- **Fields Required:**
  - Quotes: `timestamp` ($\mu s$ UTC), `bid_price`, `bid_amount`, `ask_price`, `ask_amount` (`source-reported`).
  - Trades: `timestamp` ($\mu s$ UTC), `price`, `amount`, `side` (`buy` or `sell`, validated as taker aggressor side) (`source-reported`).
- **Sampling Convention:** 1-second uniform epoch-second bars with time-weighted book features and volume-weighted trade aggregations (`source-reported`).
- **Warm-up and Truncation:** First 300 bars (5 minutes) dropped per day for rolling window warm-up; last $h$ bars dropped to prevent overnight day-boundary overlap (`source-reported`).
- **Data Quality Filter:** Days with $>60$ seconds total quote gaps excluded (`source-reported`).

## Execution assumptions

- **Execution Mode:** Taker market orders crossing the prevailing bid-ask spread (`source-reported`).
- **Execution Delay:** Exactly 1-bar ($1$ second) delay between feature computation and trade entry (`source-reported`).
- **Fill Price:** Filled at the first midprice of bar $t+1$ (`source-reported`). Real execution bid/ask crossing slip: modeled via half-spread and spread multipliers (`source-reported`).
- **Fee Structure:** Evaluated across a $3 \times 3 \times 3$ grid:
  - Taker fee parameter: $0.0$, $2.5$, and $5.0$ bps one-way (`source-reported`).
  - Spread multiplier: $0.5\times$, $1.0\times$, and $2.0\times$ observed time-weighted spread (`source-reported`).
  - Hurdle multiplier $c$: $0.5$, $1.0$, and $2.0$ (`source-reported`).
- **Borrow / Margin:** Fully collateralized USDT perpetual margin assumed; funding payments ignored due to sub-minute holding periods (`source-reported`).
- **Market Maker / Passive Limit Fills:** Not modeled in primary study (`source-reported`). Post-only passive queue simulation: `research-proposed`.

## Evidence

### Source-reported

All metrics below trace directly to `yushingtoncity/market-entropy`, commits `6e65063` and `06db3d1`, evaluated on 38 held-out test days for `BTCUSDT` and 37 held-out test days for `ETHUSDT` (monthly walk-forward expanding window from 2023-07 to 2026-08):

#### 1. Out-of-Sample Return Predictability ($R^2$ against Zero-Return Benchmark)

| Target Horizon | Model & Group | BTCUSDT Med OOS $R^2$ | BTCUSDT Days $R^2 > 0$ | ETHUSDT Med OOS $R^2$ | ETHUSDT Days $R^2 > 0$ | Binomial $p$-value |
|---|---|---|---|---|---|---|
| $h = 1$ s | OLS Group 1 (OFI only) | 2.263% | 37 / 38 | 1.622% | 34 / 37 | $p < 0.001$ |
| $h = 1$ s | OLS Group 2 (+ flow/book) | 3.649% | 37 / 38 | 2.619% | 36 / 37 | $p < 0.001$ |
| $h = 1$ s | OLS Group 3 (+ entropy) | 3.649% | 37 / 38 | 2.619% | 36 / 37 | $p < 0.001$ |
| $h = 1$ s | HGB Group 2 (nonlinear) | 4.234% | 36 / 38 | 3.049% | 36 / 37 | $p < 0.001$ |
| $h = 5$ s | OLS Group 2 | 2.878% | 38 / 38 | 1.511% | 37 / 37 | $p < 0.001$ |
| $h = 10$ s | OLS Group 2 | 1.834% | 38 / 38 | 0.932% | 37 / 37 | $p < 0.001$ |
| $h = 30$ s | OLS Group 2 | 0.688% | 36 / 38 | 0.389% | 36 / 37 | $p < 0.001$ |
| $h = 60$ s | OLS Group 2 | 0.286% | 33 / 38 | 0.236% | 31 / 37 | $p < 0.001$ |

- **Directional Sign Accuracy (on non-zero price moves):** At $h = 1$ s, median sign accuracy reaches $74.91\%$ (BTCUSDT OLS G2) and $69.58\%$ (ETHUSDT OLS G2), significantly exceeding the $50.16\%$ and $50.40\%$ majority baselines on $38/38$ and $37/37$ days ($p < 0.001$).
- **Decay Profile:** Predictability decays monotonically with horizon: at $h = 60$ s, median OOS $R^2$ drops to $0.286\%$ (BTCUSDT) and $0.236\%$ (ETHUSDT), with sign accuracy compressing to $53.40\%$ and $52.28\%$.

#### 2. The Entropy Null Result (Pre-registered Ablation)

Pre-registered hypothesis test comparing G2 (OFI + queue + volume) against G3 (G2 + Shannon sign entropy):
- BTCUSDT OLS: $\Delta(G3 - G2)$ median OOS $R^2 = -0.0000$ pp at $h=1$ s (14/38 days $G3 > G2$, $p = 0.143$), $-0.010$ pp at $h=5$ s ($p = 0.034$), $-0.016$ pp at $h=10$ s ($p = 0.073$).
- ETHUSDT OLS: $\Delta(G3 - G2)$ median OOS $R^2 = -0.0000$ pp at $h=1$ s (14/37 days $G3 > G2$, $p = 0.188$), $+0.001$ pp at $h=5$ s ($p = 1.000$), $-0.040$ pp at $h=30$ s ($p = 0.188$).
- Binomial sign tests confirm that adding 60-second Shannon entropy fails to outperform the flow-only model on day-level splits across all horizons.

#### 3. Breakeven Transaction Costs vs Exchange Taker Fees

Breakeven one-way cost (bps per turn) across models and horizons at the permissive baseline grid ($c = 0.5$, fee $= 0$, spread $\times 0.5$):

| Asset | Model | $h = 1$ s | $h = 5$ s | $h = 10$ s | $h = 30$ s | $h = 60$ s |
|---|---|---|---|---|---|---|
| BTCUSDT | OLS | 0.18 bps | 0.27 bps | 0.26 bps | 0.28 bps | 0.33 bps |
| BTCUSDT | Logit | — | 0.24 bps | 0.24 bps | 0.26 bps | 0.29 bps |
| BTCUSDT | HGB | 0.19 bps | 0.29 bps | 0.29 bps | 0.24 bps | 0.21 bps |
| ETHUSDT | OLS | 0.19 bps | 0.25 bps | 0.24 bps | 0.25 bps | 0.27 bps |
| ETHUSDT | Logit | — | 0.23 bps | 0.23 bps | 0.23 bps | 0.23 bps |
| ETHUSDT | HGB | 0.17 bps | 0.25 bps | 0.26 bps | 0.21 bps | 0.22 bps |

Across all models and horizons, the gross edge generated by order-flow imbalance breaks even at **$0.17$ to $0.33$ bps per turn**.
Under the central realistic grid point (fee $= 2.5$ bps, spread multiplier $= 1.0\times$, $c = 1.0$), the hurdle rule trades 0 times on every single test day for linear models (turnover $= 0$, median net PnL $= 0.0$ bps). Under configurations where trades execute at non-zero fees, median net daily returns are severely negative (e.g. HGB BTCUSDT loses $-11.6$ to $-240.5$ bps/day across horizons).

### Independently reproduced

Not independently reproduced. All metrics, tables, and empirical figures reflect third-party findings reported by `yushingtoncity` (`market-entropy`, commit `06db3d1c6d5eb2d29d4bea94b0af704a80c8f557`). No execution has taken place within NautilusTrader, PyBroker, or internal execution environments.

### Negative evidence

- **Complete Destruction by Taker Fees:** Taker trading against order-flow predictability is economically unviable. The breakeven threshold ($0.17 - 0.33$ bps) is an order of magnitude smaller than Binance's base VIP 0 taker fee ($5.0$ bps) and well below top-tier VIP 9 taker fees ($1.5 - 2.0$ bps).
- **Entropy Irrelevance:** Trade sign entropy contains zero distinct alpha or regime-filtering power beyond raw order-flow and queue imbalance metrics.
- **Overfitting of Complex Non-linear Models at Longer Horizons:** While HistGradientBoosting (HGB) achieves slightly higher $R^2$ at $h = 1$ s ($4.23\%$ vs $3.65\%$), its out-of-sample performance degrades rapidly at $h = 60$ s, producing negative median $R^2$ ($-0.142\%$ for BTCUSDT, $-1.042\%$ for ETHUSDT) due to leaf-splitting on microstructure noise.

## Falsification plan

To falsify the author's negative findings and demonstrate an extractable alpha mechanism, future research must establish:
1. **Passive Maker Execution Survival:** Replace the aggressive taker fill assumption with a queue-position-aware limit order fill model (e.g., Avellaneda-Stoikov or Cont-de Larrard). If an order-flow-conditioned quoting policy achieves positive net PnL after adverse selection and maker rebates ($-0.5$ to $0.0$ bps), the taker cost wall is bypassed (`research-proposed`).
   - *Falsification criteria:* If maker PnL net of adverse selection remains negative across $\ge 20$ out-of-sample test days, confirm that order-flow predictability is unextractable on both maker and taker sides (`research-defined falsification threshold`).
2. **Alternative Venue / Fee Subsidy Regimes:** Test whether zero-fee or maker-rebate venues (such as Hyperliquid or dYdX under promotional liquidity incentive epochs) permit net profitability (`research-proposed`).
   - *Falsification criteria:* Reject alpha validity if net PnL after gas/settlement costs does not exceed $+2.0$ bps daily median (`research-defined falsification threshold`).
3. **Cross-Exchange Lead-Lag Transfer:** Test whether Binance 1-second order-flow imbalance predicts price movements on slower secondary exchanges (e.g., Bybit, OKX, Coinbase) with sufficient latency buffer ($>200$ ms) and larger mispricing spreads (`research-proposed`).
   - *Falsification criteria:* If cross-venue spread plus taker fees exceed the directional lead-lag return, reject the cross-venue transmission hypothesis (`research-defined falsification threshold`).

## Crypto portability

- **Classification:** `direct` (`source-reported`).
- **Portability Mechanics:** The primary study was conducted natively on cryptocurrency perpetual futures (`BTCUSDT` and `ETHUSDT` on Binance) using raw tick-level order book and trade feeds.
- **Crypto-Specific Structural Factors:**
  - *Perpetual Funding Neutrality:* The short holding periods ($1$ to $60$ seconds) render 8-hour perpetual funding payments completely negligible (`source-reported`).
  - *24/7 Continuous Trading:* Unlike traditional equity markets (which exhibit heavy opening/closing auction dislocations and overnight jump risks), crypto order-flow dynamics operate continuously. However, turn-of-month and UTC midnight volatility shifts may introduce intraday seasonality (`source-reported`).
  - *Aggressor Side Transparency:* Unlike traditional equity feeds that require the Lee-Ready (1991) tick-rule heuristic to infer trade direction, Binance trade websocket feeds provide explicit `isBuyerMaker` boolean flags, allowing 100% exact classification of aggressor trade flow (`source-reported`).

## Limitations

- **Coarse Sampling Calendar:** The study utilizes the 1st calendar day of each month (44 days) rather than continuous multi-year tick recordings, potentially introducing turn-of-month calendar seasonality (`source-reported`).
- **Taker-Only Execution Architecture:** The backtest simulator tests only aggressive crossing orders; it does not simulate passive limit order placement, queue queueing dynamics, or cancellation latency (`source-reported`).
- **Single-Venue Data Wall:** Cross-exchange arbitrage and lead-lag dynamics between Binance, Bybit, and Hyperliquid were not evaluated (`source-reported`).
- **Underspecified Queue Depth Below BBO:** Only Level-1 (best bid/ask) sizes and time-weighted queue imbalances were computed; full L2/L3 order book depth profiles were omitted (`source-reported`).

## Implementation status

`not-implemented`. This document captures external quantitative research from public GitHub repository `yushingtoncity/market-entropy`. No implementation or execution has been carried out in PyBroker, NautilusTrader, paper trading, testnet, or live environments.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption Scope:** `not-approved`.
- **Approval Boundary:** This research record is strictly for evidence capture and strategy falsification taxonomy. It is not approved for production implementation, paper trading, testnet execution, or live capital allocation.

## Related Wiki records

- `crypto-order-flow-online-sgd-microstructure-horizon-cost-falsification-2026-09-13.md` (Patil 2026, `jarvisss007/crypto-microstructure`: Minute-level online SGD order-flow direction and retail taker fee drag on Coinbase spot).
- `order-flow-imbalance-predictive-decoupling-cost-falsification-2026-09-12.md` (Mungale 2026, `Tejas356/limit_order_book_engine`: Microstructure taker cost wall and contemporaneous vs predictive decoupling on NASDAQ equities).
- `retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11.md` (Mykola-Quant 2026: Retail cumulative volume delta and funding rate microstructure signal falsification).
- `hyperliquid-perpetual-order-flow-imbalance-depth-elasticity-nonlinearity-2026-09-13.md` (Hyperliquid L2 order flow imbalance and depth elasticity).
- `crypto-noise-perturbed-order-flow-privacy-subsidy-kyle-market-making-2026-09-01.md` (Nakamura 2026: Closed-form Kyle equilibrium and privacy subsidy under noise-perturbed order flow).

## Sources

1. **Primary Research Repository:** `yushingtoncity/market-entropy`, public GitHub repository, commit `06db3d1c6d5eb2d29d4bea94b0af704a80c8f557` (August 31, 2026). URL: [https://github.com/yushingtoncity/market-entropy](https://github.com/yushingtoncity/market-entropy).
2. **Pre-registration Specification:** `report/v2b_design.md` at immutable commit `6e65063ad9d2816819cc01812137b7f89a116ea6` (August 22, 2026). URL: [https://github.com/yushingtoncity/market-entropy/blob/6e65063ad9d2816819cc01812137b7f89a116ea6/report/v2b_design.md](https://github.com/yushingtoncity/market-entropy/blob/6e65063ad9d2816819cc01812137b7f89a116ea6/report/v2b_design.md).
3. **Comprehensive Results Report:** `report/v2b_predictive_study.md` at commit `06db3d1c6d5eb2d29d4bea94b0af704a80c8f557`. URL: [https://github.com/yushingtoncity/market-entropy/blob/06db3d1c6d5eb2d29d4bea94b0af704a80c8f557/report/v2b_predictive_study.md](https://github.com/yushingtoncity/market-entropy/blob/06db3d1c6d5eb2d29d4bea94b0af704a80c8f557/report/v2b_predictive_study.md).
4. **Research Synthesis Memo:** `report/v3_research_note.md` at commit `06db3d1c6d5eb2d29d4bea94b0af704a80c8f557`. URL: [https://github.com/yushingtoncity/market-entropy/blob/06db3d1c6d5eb2d29d4bea94b0af704a80c8f557/report/v3_research_note.md](https://github.com/yushingtoncity/market-entropy/blob/06db3d1c6d5eb2d29d4bea94b0af704a80c8f557/report/v3_research_note.md).
5. **Dataset Specification & Manifest:** `report/v2a_tardis_dataset.md` and `report/tardis_manifest.json` at commit `06db3d1c6d5eb2d29d4bea94b0af704a80c8f557`.
6. Cont, R., Kukanov, A., Stoikov, S. (2014). *The Price Impact of Order Book Events*. Journal of Financial Econometrics, 12(1), 47–88. DOI: [10.1093/jjfinec/nbt003](https://doi.org/10.1093/jjfinec/nbt003).
