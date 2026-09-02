---
schema: strategy-research-record-v1
title: "Crypto Open-Interest Crash Weak-Rebound Flow-Gap Falsifiable Alpha"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - market-microstructure
  - open-interest
  - order-flow
  - deleveraging
status: research-only
confidence: medium
source_as_of: 2026-08-13
sources:
  - "Jiacheng Guo, Suozhi Huang, Yunlong Gao, Zihao Li, Jian Ge, Xu Kuang, and Mengdi Wang, 'AQuA: Recursively Self-Improving Quantitative Trading Research Agents', arXiv:2608.12841v1 [cs.CL], August 13, 2026. https://arxiv.org/abs/2608.12841"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Open-Interest Crash Weak-Rebound Flow-Gap Falsifiable Alpha

## Provenance

Primary source: Jiacheng Guo (Princeton University), Suozhi Huang (Princeton University), Yunlong Gao (Ant Group), Zihao Li (Princeton University), Jian Ge, Xu Kuang (Stanford University), and Mengdi Wang (Princeton University), **"AQuA: Recursively Self-Improving Quantitative Trading Research Agents"**, *arXiv preprint* `arXiv:2608.12841v1 [cs.CL]`, published August 13, 2026.
- Canonical stable abstract URL: https://arxiv.org/abs/2608.12841
- Full text HTML: https://arxiv.org/html/2608.12841v1
- Full text PDF: https://arxiv.org/pdf/2608.12841v1
- DOI: `10.48550/arXiv.2608.12841`

The paper studies recursive self-improvement in quantitative-investment research using sealed evaluation sandboxes that prevent look-ahead bias and data leakage. Part I specifically develops an autonomous formulaic alpha factor discovery system evaluated on a cryptocurrency 5-minute perpetual universe (`BTCUSDT_5m`).

A repository-wide and Hermes Wiki Brain source-identity pre-write audit confirmed zero existing records containing `arXiv:2608.12841`, the paper title, or the specific "open-interest crash weak-rebound flow-gap" mechanism. Related records in the repository examine general perpetual basis or aggressor flows, but none address the structural interaction between sudden open-interest deleveraging unwinds, subsequent price bounce quality, and aggressive taker-flow / basis-rate confirmation gaps.

**Provenance gap notice:** In Section 4 and Appendix A (Listing 1 and Listing 3), the authors fully publish the event trigger definition, context fields, factor blueprint components, evaluation contract, and empirical information coefficients. However, the authors explicitly state: `"The deployed expressions are withheld throughout"` and `"expression: withheld"`. Therefore, while the economic mechanism, event profile, structural variable dependencies, and empirical performance ranges are source-reported, the exact closed-form symbolic expression tree is **underspecified** by the authors and requires normalized research operationalization.

## Economic mechanism

### Source-reported

In cryptocurrency perpetual derivatives markets, sharp declines in open interest and open-interest value under elevated trading volume indicate forced deleveraging episodes (e.g., cascading long liquidations or margin stop-outs). Once the acute liquidation wave dissipates, mechanical selling pressure ceases, and market prices frequently stage a short-horizon rebound as order books refill or short-sellers buy back contracts to lock in profits.

However, the authors' visual analysis and factor evaluation identify a critical structural bifurcation in rebound quality:
1. **Healthy demand reset:** Following the unwind, prices recover in tandem with surging aggressive taker buy volume (`taker_buy_sell_ratio > 1`) and a normalization/expansion of the futures basis rate (`basis_rate` recovery), signaling genuine organic accumulation by unconstrained capital.
2. **Hollow / unconfirmed rebound:** The price bounces upward solely due to passive liquidity depletion or brief short-covering, while aggressive taker buy flow remains absent (`flow_gap`) and the futures basis remains depressed/compressed.

The source reports that price rebounds that are left unconfirmed by aggressive taker flow exhibit insufficient fundamental demand and have a high propensity to fail and reverse over medium intraday horizons (`ret_open_open_h10` and `ret_open_open_h30`, corresponding to 50 to 150 minutes).

### Research interpretation

The falsifiable alpha hypothesis is **Liquidation Exhaustion vs. Organic Demand Deficit**.

Forced liquidation flows temporarily dislocate market prices below local equilibrium through aggressive market-order execution. When the liquidation run terminates, the bid side of the limit order book naturally reconstitutes, producing a mechanical bounce. This mechanical price rebound presents an adverse-selection trap:
- If institutional market participants actively step in to accumulate the discounted inventory, aggressive taker flow surges and basis compresses back toward positive carry, confirming the bottom.
- If aggressive taker flow remains anemic while price drifts upward on thin passive liquidity, the bounce represents a liquidity-hollow reflex. As soon as passive bids are met by remaining overhead inventory from distressed market participants, the rebound collapses.

Thus, a composite signal quantifying the divergence between price rebound magnitude and aggressive taker flow following a deleveraging event provides a directional short alpha signal targeting the failure of the bounce.

## Signal

**Status:** Partially specified by the primary source; variable dependencies and blueprint are source-reported; explicit formulaic tree expressions are withheld by the authors (`expression: withheld`), so executable operational rules are `research-proposed`.

### Event trigger definition (Source-reported)

- **Instrument / Universe:** `BTCUSDT_5m` perpetual futures contract.
- **Evaluation Cadence:** 5-minute bar close / boundary.
- **Deleveraging Event Trigger:**
  - Sharp drop in open interest: $\Delta OI_t = OI_t - OI_{t-k} \ll 0$ or $\Delta (\text{OI Value})_t \ll 0$ over a short lookback window $k \in [3, 12]$ bars (15 to 60 minutes).
  - Elevated trading volume: $\text{Volume}_t > 1.5 \times \text{SMA}(\text{Volume}, 20)$.

### Factor blueprint (Source-reported)

The source decomposes the signal into four structural components:
1. **Deleveraging Intensity:** Ranked negative change in open interest (`ranked negative change in open interest`).
2. **Rebound Strength:** Short-horizon price recovery following the deleveraging shock (`short-horizon price recovery after the event`).
3. **Flow Gap:** Lack of aggressive taker-flow confirmation during the rebound (`lack of taker-flow confirmation during the rebound`).
4. **Basis Filter:** Weak or compressed basis-rate recovery (`weak or compressed basis-rate recovery`).

- **Expected Direction:** Higher signal value predicts lower future return (`expected_direction: higher_signal_predicts_lower_future_return`).
- **Target Forward Labels:** 
  - `ret_open_open_h10`: Forward return over 10 bars (50 minutes).
  - `ret_open_open_h30`: Forward return over 30 bars (150 minutes).

### Research-proposed operationalization

To transform the author's blueprint into a deterministic, reproducible quantitative rule:

1. **Deleveraging Shock Indicator:**
   $$\text{OI\_Drop}_t = \frac{OI_{t} - \max_{s \in [t-k, t]} OI_s}{\text{std}(OI, 288)}$$
   $$\text{Event}_t = \mathbb{I}\left(\text{OI\_Drop}_t < -2.0 \quad \text{AND} \quad \text{Volume}_t > 1.5 \times \text{SMA}(\text{Volume}_t, 20)\right)$$

2. **Rebound Strength ($M = 3$ bars = 15 minutes post-shock):**
   $$\text{Rebound}_t = \frac{P_t - \min_{s \in [t-M, t]} P_s}{\text{ATR}(14)_t}$$

3. **Taker Flow Gap:**
   $$\text{TakerRatio}_t = \frac{\text{TakerBuyVolume}_t}{\text{TakerBuyVolume}_t + \text{TakerSellVolume}_t + \epsilon}$$
   $$\text{FlowGap}_t = \max\left(0, 0.50 - \text{SMA}(\text{TakerRatio}_t, M)\right)$$

4. **Basis Compression Filter:**
   $$\text{BasisRate}_t = \frac{P_{\text{perp}, t} - P_{\text{index}, t}}{P_{\text{index}, t}}$$
   $$\text{BasisFilter}_t = \mathbb{I}\left(\text{BasisRate}_t < \text{SMA}(\text{BasisRate}, 288)_t\right)$$

5. **Composite Signal:**
   $$S_t = \text{Rebound}_t \times \text{FlowGap}_t \times \text{BasisFilter}_t$$
   conditioned on $\sum_{i=0}^{M} \text{Event}_{t-i} \ge 1$.

6. **Execution Rules:**
   - **Short Entry:** If $S_t > \theta_{\text{short}}$ at the close of bar $t$, enter short at the open of bar $t+1$.
   - **Exit:** Exit after 10 bars (primary horizon) or 30 bars (secondary horizon), or when price rises $\ge 1.5 \times \text{ATR}(14)$ above the post-shock swing high (invalidation stop).
   - **Long Leg:** Remained flat during deleveraging events; the source focuses on the directional failure of unconfirmed bounces.

## Required data

- **Instrument / Universe:** Bitcoin perpetual futures (`BTCUSDT`).
- **Venue:** Centralized derivatives exchange publishing tick-level or bar-aggregated trade and derivatives metrics (e.g., Binance Futures, Bybit, OKX).
- **Market Type:** USDT-margined linear perpetual contract.
- **Timeframe:** 5-minute bars.
- **Data Fields:**
  - Core OHLCV: `open`, `high`, `low`, `close`, `volume`.
  - Derivatives open interest: `open_interest` (contracts) and `open_interest_value` (USD/quote notional).
  - Taker aggressor volume: `taker_buy_volume`, `taker_sell_volume` (or `taker_buy_sell_ratio`).
  - Index / Mark Price: `index_price` (required to compute `basis_rate` = $\frac{P_{\text{perp}} - P_{\text{index}}}{P_{\text{index}}}$).
  - Optional market-context fields (source-reported in Listing 3): `long_short_account_ratio`, `top_trader_position_ratio`.
- **Point-in-Time / Timestamping:** All metrics must be stamped with strict exchange closing timestamps. Execution is evaluated at the open of bar $t+1$ to ensure zero look-ahead bias from bar $t$ closing statistics.
- **Missing Data Handling:** If open interest or taker volume feeds experience gaps or delayed delivery from the exchange API, signal generation is suppressed for that bar; forward-filling open interest across structural outages is prohibited.
- **Friction Data:** Observed bid-ask spread at bar open, taker fee schedule (e.g., 2–4 bps), maker fee schedule, and perpetual funding rate payments over the holding period.

## Execution assumptions

### Source-reported

- Evaluated against forward open-to-open returns (`ret_open_open_h10` and `ret_open_open_h30`), enforcing strict causal next-open execution.
- Evaluated inside a sealed sandbox where the data pipeline, feature definitions, and evaluator are frozen prior to model iteration.

### Research-proposed

- **Order Type:** Taker market order at the open of bar $t+1$ following a bar $t$ signal confirmation.
- **Trading Costs:** Conservative taker fee baseline of 3.0 bps per leg (6.0 bps round-trip) plus 0.5–1.0 bp estimated half-spread slippage, totaling 7.0–8.0 bps round-trip.
- **Margin / Funding:** Requires perpetual short margin availability; short positions collect or pay the prevailing 8-hour funding rate prorated over the 50–150 minute holding window.
- **Latency:** Bar boundary execution requires an automated execution engine capable of sub-second order placement after bar close.

## Evidence

### Source-reported

All empirical figures below trace directly to Guo et al. (*arXiv:2608.12841v1*, Section 4.4, Section 4.5, Section 5.6, Table 3, Table 4, and Appendix A):

- **Target Universe:** `BTCUSDT_5m` perpetual data.
- **Single-Factor Performance:** In the open-interest crash family of runs, the "OI crash rebound flow gap" factor achieved single-factor information coefficients (IC) ranging between approximately **0.026 and 0.037** depending on the specific forward return label (`ret_open_open_h10`, `ret_open_open_h30`) and event context.
- **Event Concentration:** Controlled comparisons against price, open-interest, taker-flow, and basis baselines confirmed that factor predictive skill was concentrated inside the deleveraging event window rather than in control periods outside the event.
- **Combined Factor Signal:** The manager-mediated multi-agent loop accumulated and combined surviving factors (integrating open-interest shocks, flow gaps, basis recovery, and crowding divergence), achieving a combined validation information coefficient of approximately **0.190** across iterations on the crypto 5-minute universe.
- **Companion Benchmark Evidence (Part II - US Equities, 30m):** The companion model system evaluated on US equities (30-minute interval, 2010–2019 train, 2020 embargo, 2021–2025 held-out test) achieved a per-stock raw IC of **+0.0843** (vs. Linear +0.0251, LightGBM +0.0397, xLSTM +0.0434, LSTM +0.0535, GRU +0.0613), per-stock $R^2 = 1.20\%$, and a held-out Sharpe ratio at 2 bps two-leg cost of **+2.15** (sector-neutral), **+2.50** (with causal volatility targeting), and **+2.00** under a fully causal walk-forward schedule. The strategy Sharpe was positive in every calendar year: +1.7 (2021), +3.5 (2022), +1.9 (2023), +1.8 (2024), and +2.7 (2025).

### Independently reproduced

not independently reproduced

### Negative evidence

- **Closed-form Expression Withheld:** The primary authors explicitly withheld the symbolic expression trees (`expression: withheld`), preventing direct bit-for-bit numerical replication of the exact production factor.
- **Lack of Net Portfolio Metrics for Standalone Factor:** The paper reports information coefficients and validation combination ICs for Part I, but does not publish standalone net-of-cost dollar PnL, annualized Sharpe ratio, or maximum drawdown for the single `oi_crash_weak_rebound_flow_gap` factor.
- **Modest Single-Factor Effect Size:** A single-factor IC of 0.026–0.037 on 5-minute bars represents a modest statistical edge that is highly sensitive to transaction fees and slippage; trading unconfirmed rebounds indiscriminately without strict threshold gating will result in negative net returns.
- **Event Scarcity in Low-Volatility Regimes:** Open-interest liquidation shocks occur sporadically during trending or volatile deleveraging events; during extended low-volatility consolidation regimes, the factor generates zero signals.

## Falsification plan

1. **Primary Out-of-Sample Event-Window Test:**
   - *Sample:* BTCUSDT perpetual data from 2025-01-01 to 2026-08-31 (or strictly post-August 2026 out-of-sample data).
   - *Metric:* Mean Pearson and Spearman rank IC of the normalized flow-gap signal against 10-bar and 30-bar forward returns specifically inside identified OI-crash windows.
   - *Falsification Threshold:* Fail the hypothesis if event-window IC is not statistically greater than zero ($t\text{-stat} < 2.0$) or if the event-window IC fails to exceed the non-event control window IC by at least 0.015.

2. **Ablation Against Short-Horizon Price Momentum:**
   - *Test:* Multi-variable regression of forward returns on both the flow-gap composite factor and simple 15-minute price return ($\Delta P_{t-3}$).
   - *Falsification Threshold:* Reject the flow-gap mechanism if the incremental $t$-statistic on the flow-gap term is $< 1.96$, indicating that rebound failure is merely a generic momentum continuation of the crash rather than a flow-confirmed information phenomenon.

3. **Transaction Cost Sensitivity Stress Test:**
   - *Test:* Simulate the operationalized short strategy with realistic round-trip costs of 6 bps (taker fee) + 2 bps (slippage/spread).
   - *Falsification Threshold:* Reject practical viability if the annualized net Sharpe ratio drops below 0.50 or if net cumulative return across 12 rolling months is negative.

4. **Direction Calibration / Inversion Audit:**
   - *Test:* Compare the primary short strategy against a reversed long strategy entering on the same triggers.
   - *Falsification Threshold:* If the reversed long strategy outperforms the short strategy on risk-adjusted net return, the economic thesis that unconfirmed bounces fail is falsified.

5. **Cross-Asset Perpetual Generalization:**
   - *Test:* Evaluate the identical formulation on ETHUSDT and SOLUSDT perpetuals without re-tuning parameters.
   - *Falsification Threshold:* Fail cross-asset universality if the average event-window IC across the altcoin universe is negative or statistically indistinguishable from zero.

## Crypto portability

**direct** for cryptocurrency perpetual futures contracts. The source hypothesis and empirical tests were developed specifically on cryptocurrency derivatives (`BTCUSDT_5m`) using exchange-native open interest, taker flow, and basis metrics.

Portability nuances and constraints across market segments:
- **Crypto Spot:** **not applicable** or heavily degraded. Spot markets lack native open interest, funding rate mechanics, and liquidation engine telemetry. Furthermore, shorting spot assets requires borrow inventory and margin interest, altering the cost structure.
- **Crypto Altcoin Perpetuals:** **adapted**. Highly applicable to liquid altcoin perpetuals (ETH, SOL, DOGE) where liquidation cascades frequently trigger mechanical bounces. However, altcoins have higher bid-ask spreads and lower order-book depth, making execution friction a steeper hurdle.
- **Traditional Equities / Futures:** **unproven / adapted**. Traditional equity index futures (e.g., CME E-mini S&P 500) publish open interest on a daily clearing basis rather than in real-time 5-minute feeds, rendering the high-frequency intraday OI-shock trigger inoperable without proprietary intraday trade/quote order-flow proxies.

## Limitations

- `not independently reproduced`
- `underspecified`: The exact symbolic operator expression tree is explicitly withheld by the authors (`expression: withheld`), requiring research-proposed formulaic reconstruction.
- `data gap`: The paper reports information coefficients (0.026–0.037 single-factor, ~0.190 combined validation IC) but omits dollar PnL, maximum drawdown, capacity bounds, and annualized net Sharpe ratios for the standalone factor.
- **Exchange Telemetry Latency:** Real-time 5-minute open interest and taker volume feeds from cryptocurrency exchange public WebSocket/REST endpoints are subject to delivery delays, rate limits, and periodic historical restatements.
- **Regime Fragility:** In persistent strong bull runs, aggressive short liquidations can lead to sustained price continuation where even "unconfirmed" bounces continue upward due to spot buying that is not captured by perpetual taker flow.

## Implementation status

Not implemented. No PyBroker strategy, NautilusTrader strategy, data ingestion pipeline, backtesting campaign, or Paper/Testnet/Live trading configuration was created in this Scout cycle.

## Adoption boundary

This record is research material only. It represents a source-traceable capture of an external academic paper and does not constitute validated alpha, proof of trading profitability, or authorization for implementation, paper trading, testnet deployment, or live capital allocation.

## Related Wiki records

- `[[quant/crypto-quarter-hour-opening-order-imbalance-medium-horizon-2026-08-31]]` — Intraday order flow imbalance and periodic algorithmic trading in crypto perpetuals.
- `[[quant/crypto-short-horizon-15min-mean-reversion-taker-flow-2026-09-01]]` — 15-minute taker flow, liquidity provision, and directional mean reversion across Binance pairs.
- `[[quant/crypto-perpetual-futures-self-benchmarked-factor-alpha-2026-09-01]]` — Market-neutral factor investing and aggressor flow alpha in perpetual futures.

## Sources

1. Guo, J., Huang, S., Gao, Y., Li, Z., Ge, J., Kuang, X., & Wang, M. (2026). "AQuA: Recursively Self-Improving Quantitative Trading Research Agents." *arXiv preprint* `arXiv:2608.12841v1 [cs.CL]`, submitted August 13, 2026.
   - Stable arXiv URL: https://arxiv.org/abs/2608.12841
   - Full HTML version: https://arxiv.org/html/2608.12841v1
   - Full PDF version: https://arxiv.org/pdf/2608.12841v1
   - DOI: https://doi.org/10.48550/arXiv.2608.12841
