---
schema: strategy-research-record-v1
title: "Polymarket-Binance High-Frequency BTC 15-Minute Binary Lead-Lag Alpha (OpenMarket)"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - prediction-markets
  - polymarket
  - binance
  - high-frequency
  - order-flow-imbalance
  - lead-lag
  - bayesian-updating
  - student-t
  - cross-venue
  - latency-arbitrage
  - null-result
status: research-only
confidence: medium
source_as_of: 2026-07-01
sources:
  - "Gregory Young, 'OpenMarket: A Synchronized Polymarket-Binance Dataset for High-Frequency Prediction-Market Research', arXiv:2607.26245v1 [q-fin.TR, cs.CE], July 28, 2026. DOI: 10.48550/arXiv.2607.26245. Stable URL: https://arxiv.org/abs/2607.26245. GitHub: https://github.com/gregyoung14/openmarket, tag v0.5.2, commit 6e6cc240f32ab9fd2f8fa602bd0aba823b24bfee."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Polymarket-Binance High-Frequency BTC 15-Minute Binary Lead-Lag Alpha (OpenMarket)

## Provenance

- **Author:** Gregory Young (University of Colorado Boulder, Department of Computer Science; contact: `gryo8540@colorado.edu`).
- **Paper Title:** "OpenMarket: A Synchronized Polymarket–Binance Dataset for High-Frequency Prediction-Market Research"
- **Identifier:** arXiv preprint `arXiv:2607.26245v1 [q-fin.TR, cs.CE]`, submitted July 28, 2026.
- **DOI:** [10.48550/arXiv.2607.26245](https://doi.org/10.48550/arXiv.2607.26245)
- **Stable URL:** https://arxiv.org/abs/2607.26245
- **Full Text HTML:** https://arxiv.org/html/2607.26245v1
- **Code Repository:** https://github.com/gregyoung14/openmarket
- **Repository Anchor:** Release tag `v0.5.2`, immutable commit SHA `6e6cc240f32ab9fd2f8fa602bd0aba823b24bfee`.
- **License:** Apache License 2.0 (open-source software) / Creative Commons Attribution 4.0 International (paper).
- **Public Data Releases:**
  - Hugging Face Dataset: `gregyoung14/openmarket-btc-polymarket` (deduplicated analytic split `v0.4.3-unified`: 727,098,247 rows, 8.69 GiB Parquet; full archive `v0.2-full`; sample `v0.1-sample`).
  - Hugging Face Models: `gregyoung14/openmarket-models` (walk-forward logistic + Platt calibrator `v0.2.1/`; pilot `v0.1/`).
- **Sample/Data Period:**
  - Archive span: February 12, 2026 to May 15, 2026 (93 calendar days; 54 observed event days for Polymarket, 57 observed event days for Binance).
  - Snapshot publication window: March 14, 2026 to July 1, 2026 (202 CDN SQLite snapshots, 46.21 GB compressed).
- **Target Universe:** Rolling 15-minute Bitcoin binary outcome markets on Polymarket (UP/DOWN tokens settling to $1.00 or $0.00 depending on whether BTC price at expiry exceeds the strike/open price) paired synchronously against spot BTC/USDT trade and order book updates on Binance.

## Economic mechanism

### Source-reported

In decentralized prediction markets (DePM) operating central limit order books (CLOBs), such as Polymarket's 15-minute Bitcoin rolling markets, contracts represent short-horizon binary cash-or-nothing options that settle strictly to 1 or 0 based on reference crypto spot prices. The foundational premise of high-frequency cross-venue trading systems in this domain is that **centralized spot exchanges with deep liquidity and high tick frequency (specifically Binance BTC/USDT) lead price discovery relative to decentralized prediction market order books**.

Under this thesis:
1. When significant order flow imbalance or sharp price jumps occur on Binance, Polymarket's order book should exhibit a measurable latency before quotes adjust to the new implied terminal probability.
2. An automated trader collocated or listening to both WebSocket feeds could extract directional alpha by observing Binance taker order flow, computing the statistical log-return drift and order flow imbalance (OFI) acceleration, and aggressively crossing the Polymarket spread on UP or DOWN tokens before prediction-market market makers update their resting limit orders.

However, Young (2026) empirically investigates this thesis across 727 million events and concludes with a **definitive out-of-sample null result**:
- While Polymarket quotes take a median of 347 ms on the collector clock to adjust to large Binance spot moves ($\ge 5$ bps within 1 s), the top-of-book spread on Polymarket contracts concentrates at 1 tick wide (0.01 probability points).
- Once realistic maker/taker fees (1.0% per trade) and crossing slippage (0.5 cents / 0.5% per trade) are applied, and once models are evaluated strictly walk-forward out-of-sample, a 43-feature multivariate model fails to outperform the probability already implied by Polymarket's own resting mid-price, resulting in negative economic payoff.

### Research interpretation

The proposed system represents a **hybrid cross-venue latency and momentum-acceleration directional trading policy**:
- **Regime gate:** Uses path efficiency and return autocorrelation over a 60-second rolling window to filter out choppy / mean-reverting microstructure environments and engage only during directional trend or neutral regimes.
- **Bayesian Student-$t$ sequential log-odds updater:** Replaces Gaussian drift assumptions with a 3-degree-of-freedom Student-$t$ log-likelihood ratio to account for fat tails in high-frequency BTC log-returns, dynamically amplified by taker trading volume.
- **Order Flow Imbalance (OFI) acceleration:** Measures second-derivative shifts in aggressive buying vs selling volume across split halves of the observation window.
- **Scoreboard displacement:** Measures cumulative displacement from the 15-minute window open price.
- **Whipsaw quality regularizer:** Penalizes excessive logit extremity when the price path exhibits excessive direction reversals.
- **Logit-space LMSR/Softmax mapping:** Linearly aggregates component logits into a combined log-odds, maps to probability via a sigmoid link function, and executes when confidence and edge exceed calibrated hurdle thresholds across an adaptive confirmation window.

The empirical failure of this strategy demonstrates that **the Polymarket order-book mid price is remarkably informationally efficient**: it already incorporates continuous spot price discovery within the boundary of its 1-tick spread. Any apparent cross-venue latency edge (such as the 347 ms median response lag) is insufficient to overcome transaction frictions, exchange fees, and execution slippage.

## Signal

The normalized signal computation is executed once per second during the active market entry window (seconds 60 to 600 of each 900-second / 15-minute contract).

### 1. Market Window Timeline

- Total market duration: $T = 900\text{ s}$ (15 minutes).
- Earliest entry second: $t_{\mathrm{min}} = 60\text{ s}$ (allowing warm-up of price/volume history).
- Latest entry second: $t_{\mathrm{max}} = 600\text{ s}$ (10 minutes into the window; entries past 600s are blocked to allow the directional thesis time to mature before expiry).

### 2. Microstructure Regime Detector

Evaluated over the last $N_{\mathrm{regime}} = 60$ 1-second closing prices of BTC on Binance:
1. **Path Efficiency ($PE$):**
   $$PE = \frac{|P_{t} - P_{t-N}|}{\sum_{i=t-N+1}^{t} |P_i - P_{i-1}| + 10^{-12}}$$
2. **Lag-1 Autocorrelation ($\rho_1$):**
   Computed on 1-second log returns $r_i = \ln(P_i / P_{i-1})$:
   $$\rho_1 = \frac{\sum_{i=1}^{k-1} (r_i - \bar{r})(r_{i+1} - \bar{r})}{\sum_{i=1}^{k} (r_i - \bar{r})^2}$$
3. **Regime Classification:**
   - If $\rho_1 < -0.25$ (`REGIME_AUTOCORR_CHOP`) or $PE < 0.06$ (`REGIME_CHOP_THRESHOLD`): **`Chop`** $\rightarrow$ signal emission suppressed (`None`).
   - Else if $PE \ge 0.15$ (`REGIME_TREND_THRESHOLD`) and $\rho_1 > -0.10$: **`Trend`** $\rightarrow$ active.
   - Otherwise: **`Neutral`** $\rightarrow$ active, with confidence penalty $\Delta c = 0.02$ (`NEUTRAL_CONF_PENALTY`).

### 3. Sub-Signal Logit Formulations

#### Component 1: Bayesian Student-$t$ Drift ($\mathrm{logit}_{\mathrm{drift}}$)
- Evaluated on 1-second log returns $r_i$ from window start to current second.
- Assumed per-second parameters: local volatility $\sigma = 0.0002$, expected drift $\mu = 0.00004$, degrees of freedom $\nu = 3.0$ (`STUDENT_T_DF`), scaling factor $c_\nu = (\nu + 1) / 2 = 2.0$.
- Standardized deviations under UP ($z_{\mathrm{up}}$) and DOWN ($z_{\mathrm{down}}$) hypotheses:
  $$z_{\mathrm{up}} = \frac{r_i - \mu}{\sigma}, \quad z_{\mathrm{down}} = \frac{r_i + \mu}{\sigma}$$
- Log-likelihoods:
  $$\ell_{\mathrm{up}} = -c_\nu \ln\left(1 + \frac{z_{\mathrm{up}}^2}{\nu}\right), \quad \ell_{\mathrm{down}} = -c_\nu \ln\left(1 + \frac{z_{\mathrm{down}}^2}{\nu}\right)$$
- Step log-odds $\Delta \ell_i = \ell_{\mathrm{up}} - \ell_{\mathrm{down}}$, scaled by volume conviction relative to expanding-window mean volume $\bar{V}_i$:
  $$\Delta \ell_i^* = \begin{cases} 2.0 \cdot \Delta \ell_i, & \text{if } V_i > 1.5 \bar{V}_i \text{ (high conviction)} \\ 1.2 \cdot \Delta \ell_i, & \text{if } \bar{V}_i < V_i \le 1.5 \bar{V}_i \text{ (moderate conviction)} \\ 0.5 \cdot \Delta \ell_i, & \text{if } V_i \le \bar{V}_i \text{ (low conviction / noise)} \end{cases}$$
- Cumulative drift logit: $\mathrm{logit}_{\mathrm{drift}} = \sum \Delta \ell_i^*$.

#### Component 2: OFI Acceleration ($\mathrm{logit}_{\mathrm{ofi}}$)
- Splits volume history into earlier half ($[0, n/2]$) and recent half ($[n/2, n]$):
  $$\mathrm{OFI}_{\mathrm{recent}} = \frac{V_{\mathrm{buy}}^{\mathrm{recent}} - V_{\mathrm{sell}}^{\mathrm{recent}}}{V_{\mathrm{buy}}^{\mathrm{recent}} + V_{\mathrm{sell}}^{\mathrm{recent}} + 10^{-9}}, \quad \mathrm{OFI}_{\mathrm{earlier}} = \frac{V_{\mathrm{buy}}^{\mathrm{earlier}} - V_{\mathrm{sell}}^{\mathrm{earlier}}}{V_{\mathrm{buy}}^{\mathrm{earlier}} + V_{\mathrm{sell}}^{\mathrm{earlier}} + 10^{-9}}$$
  $$\mathrm{OFI}_{\mathrm{accel}} = \mathrm{OFI}_{\mathrm{recent}} - \mathrm{OFI}_{\mathrm{earlier}}$$
  $$\mathrm{logit}_{\mathrm{ofi}} = \mathrm{OFI}_{\mathrm{accel}} \cdot 5.0 \quad (\mathrm{OFI\_SCALE} = 5.0)$$

#### Component 3: Scoreboard Momentum ($\mathrm{logit}_{\mathrm{score}}$)
- Measures percentage move from market open price $P_{\mathrm{start}}$:
  $$\Delta_{\mathrm{open}} = \frac{P_t - P_{\mathrm{start}}}{P_{\mathrm{start}} + 10^{-9}}$$
  $$\mathrm{logit}_{\mathrm{score}} = \Delta_{\mathrm{open}} \cdot 500.0 \quad (\mathrm{SCOREBOARD\_SCALE} = 500.0)$$

#### Component 4: Whipsaw Regularization ($S_{\mathrm{whip}}$)
- Measures fraction of consecutive bars changing direction:
  $$W = \frac{\sum_{i=1}^{n-2} \mathbf{1}\{\operatorname{sgn}(P_{i+1} - P_i) \ne \operatorname{sgn}(P_{i+2} - P_{i+1})\}}{n - 2}$$
- Gaussian proximity to optimal whipsaw ratio $W^* = 0.40$ (`WHIPSAW_OPTIMAL`) with width $\sigma_w^2 = 0.08$ (`WHIPSAW_WIDTH`):
  $$S_{\mathrm{whip}} = \exp\left(-\frac{(W - 0.40)^2}{0.08}\right)$$

### 4. LMSR / Softmax Aggregation

Combined logit is formed via linear weighting:
$$\mathrm{logit}_{\mathrm{raw}} = W_{\mathrm{drift}} \cdot \mathrm{logit}_{\mathrm{drift}} + W_{\mathrm{ofi}} \cdot \mathrm{logit}_{\mathrm{ofi}} + W_{\mathrm{score}} \cdot \mathrm{logit}_{\mathrm{score}}$$
where default calibrated weights from `config.rs` are:
$$W_{\mathrm{drift}} = 1.0910, \quad W_{\mathrm{ofi}} = 1.4691, \quad W_{\mathrm{score}} = 4.0578$$
Whipsaw dampening pulls the logit toward zero to prevent overconfidence in choppy conditions:
$$\mathrm{logit}_{\mathrm{comb}} = \mathrm{logit}_{\mathrm{raw}} - \operatorname{sgn}(\mathrm{logit}_{\mathrm{raw}}) \cdot |W_{\mathrm{whip}}| \cdot S_{\mathrm{whip}}$$
where $W_{\mathrm{whip}} = -1.4707$.

The implied UP probability is:
$$p_{\mathrm{UP}} = \frac{1}{1 + e^{-\mathrm{logit}_{\mathrm{comb}}}}$$

### 5. Direction, Confidence, and Gating

- Direction:
  $$\text{Direction} = \begin{cases} \text{"UP"}, & \text{if } p_{\mathrm{UP}} > 0.50 \\ \text{"DOWN"}, & \text{if } p_{\mathrm{UP}} \le 0.50 \end{cases}$$
- Raw confidence: $c = \max(p_{\mathrm{UP}}, 1 - p_{\mathrm{UP}})$. If regime is Neutral, $c \leftarrow c - 0.02$.
- Adaptive confirmation window $K_{\mathrm{confirm}}$:
  $$K_{\mathrm{confirm}} = \operatorname{clamp}\left(\left\lfloor 30 \cdot \left(1.3 - 0.3 \cdot \min\left(2.0, \frac{\sigma_{\mathrm{recent}}}{0.0002}\right)\right)\right\rfloor, 15, 50\right)$$
- Entry gate criteria:
  1. Market hourly volume above median (`ENABLE_VOLUME_GATE`).
  2. $c \ge 0.60$ (`DEFAULT_MIN_CONFIDENCE`).
  3. $\text{Edge} = c - P_{\mathrm{entry}} \ge 0.08$ (`DEFAULT_MIN_EDGE`), where $P_{\mathrm{entry}} = P_{\mathrm{best\_ask}} + 0.005$ (`SLIPPAGE`).
  4. Best ask within valid quote range: $0.15 \le P_{\mathrm{best\_ask}} \le 0.55$.
  5. Peak-confidence selection: Rather than executing on the first qualifying second, the strategy tracks all qualifying signals across seconds 60–600 and selects the single timestamp with the highest confidence.

## Required data

- **Venues:**
  - Prediction Market: Polymarket CLOB (Polygon network).
  - Reference Spot Exchange: Binance (global centralized exchange).
- **Instruments:**
  - Polymarket: Rolling 15-minute BTC binary market contracts (`market_slug` format e.g., `btc-updown-15m-<timestamp>`), tracking both UP and DOWN outcome tokens.
  - Binance: BTC/USDT spot market.
- **Data Feeds and Fields:**
  - Polymarket: WebSocket stream capturing L2 book snapshots, top-of-book best bid/ask, market-order trades, tick timestamps, and market resolution metadata.
  - Binance: WebSocket trade stream (`tradeId`, `price`, `quantity`, `isBuyerMaker`, `tradeTime`) and 1-second aggregated OHLCV bars.
  - Paired Table (`lag_pairs_ms`): Nearest-neighbor paired events inside alignment window $W = 750\text{ ms}$, preserving source timestamps (`polymarket_source_ts_ms`, `binance_source_ts_ms`), collector ingest timestamps (`polymarket_ingest_ts_ms`, `binance_ingest_ts_ms`), realized lead-lag in milliseconds, and quality flag (`tight` for $|\Delta t| \le 100\text{ ms}$, `medium` for $\le 300\text{ ms}$, `wide` for $> 300\text{ ms}$).
- **Point-in-Time Integrity:**
  - Feature cutoffs are locked to observation timestamp $t$; labels are populated only upon official market resolution at expiry $T$.
  - Platt probability calibration and logistic regression models are fitted strictly on pre-cutoff historical market windows; scored out-of-sample windows are excluded from calibration fitting.

## Execution assumptions

- **Order Type:** Aggressive taker market order crossing the top-of-book ask on Polymarket.
- **Transaction Costs & Fees:**
  - Exchange fee: 1.0% per trade ($0.01$ fee rate, applied to both winning and losing trades).
  - Assumed slippage: 0.5 cents ($0.005$ probability points added to displayed best ask).
- **Fill Model:** Immediate execution at $P_{\mathrm{entry}} = P_{\mathrm{best\_ask}} + 0.005$. In the simulator, losing trades lose 1 staked unit plus fee ($1.0 + \text{fee}$), while winning trades receive the $1.00$ contract settlement payout net of entry price, fee, and slippage.
- **Position Sizing:** Fractional Kelly sizing (`KELLY_SCALE` = 0.25, quarter-Kelly), capped at 5.0% of bankroll (`MAX_BET_FRACTION` = 0.05) with minimum bet size of 1.0 unit.
- **Capital & Leverage:** 1.0x cash collateral (USDC on Polygon), no borrowing or margin leverage.

## Evidence

### Source-reported

All figures, metrics, and empirical findings below are directly reported by Gregory Young in *arXiv:2607.26245v1* and the accompanying release manifests (tag `v0.5.2`, commit `6e6cc240f32ab9fd2f8fa602bd0aba823b24bfee`):

#### 1. Dataset Scale and Architecture (Table 1, Section 9.1)
- Total deduplicated rows in unified split (`v0.4.3-unified`): **727,098,247 rows** (8.69 GiB on disk across 504 Parquet parts).
- Breakdown: Polymarket ticks (605,608,370), Binance trades (62,258,815), Binance millisecond ticks (55,792,056), explicit cross-venue lag pairs (2,936,031), derived candle tables (498,525 rows).
- Calendar coverage: 93 calendar days (February 12, 2026 to May 15, 2026); 54 observed Polymarket days and 57 observed Binance days across 202 SQLite snapshot checkpoints.
- Market coverage: 4,450 total market slugs recorded; 2,251 markets possess sufficient data density to support feature export and walk-forward training.

#### 2. Synchronization and Lead-Lag Dynamics (Section 5.2, 9.2, 10.2)
- Continuous flow lead-lag ($n = 2,936,031$ pairs):
  - Median apparent source-clock lead-lag: **16 ms** (positive indicates Polymarket following Binance).
  - 5th / 95th percentiles: **-186 ms / +316 ms**.
  - Quality flag split on 500k sample: 67.6% tight ($\le 100\text{ ms}$), 27.0% medium ($\le 300\text{ ms}$), 5.5% wide ($> 300\text{ ms}$).
- Clock drift and offset validation:
  - Relative venue clock drift bounded empirically to **$\le 6\text{ ms}$** over the entire 3-month archive based on minimum-delay transport envelopes (Binance 99 ms, Polymarket 7 ms).
  - Constant-offset ambiguity: Approximately $\pm 99\text{ ms}$ due to single collection vantage point.
- Synchronization-free causal response:
  - 15,148 large Binance moves ($\ge 5\text{ bps}$ within 1 s) matched to 4,272 directionally consistent Polymarket UP-token best-bid quote changes ($\ge 1\text{ tick}$) within 2 s.
  - Measured entirely on the collector's single ingest clock: **median quote response lag is 347 ms**.

#### 3. Out-of-Sample Model Benchmarks and Ablations (Section 10.4, Table 2)
Evaluated on 357,390 step3 feature rows across 2,251 markets:
- Strictly out-of-sample walk-forward evaluation (559 windows, 355,814 OOS rows):
  - **Walk-forward Logistic + Platt model (`v0.2.1`):** ROC AUC = **0.8377**, Brier score = **0.165**, Expected Calibration Error (ECE) = **0.026**.
  - **Naive Polymarket mid-price prior (zero parameters, identical feature cutoff timestamp):** ROC AUC = **0.8405**, Brier score = **0.163**, ECE = **0.014**.
  - **Statistical result:** The multivariate ML model slightly underperforms the market's own resting order-book mid price out of sample.
- Diagnostic full-timeline in-sample comparison ($n = 357,390$ rows):
  - In-sample ranking shows model AUC slightly above naive prior ($\Delta \mathrm{AUC} = +0.0014$, 95% CI $[0.0005, 0.0023]$, paired block bootstrap, $p = 0.001$).
  - However, this marginal lift is entirely in-sample and vanishes under walk-forward OOS validation.

#### 4. Simulated Trading Economics (Abstract, Section 6, 10.4)
- Top-of-book spreads on Polymarket UP/DOWN tokens concentrate at **1 tick wide** (median 0.01 probability points; 95th percentile 0.02).
- Under realistic fees (1.0%) and slippage (0.5 cents):
  - Simulated positive-EV trading nets **$-0.116$ normalized payoff units per attempted trade**.
  - No strategy iteration survived transaction fees and crossing spread.

### Independently reproduced

Not independently reproduced. All figures and empirical metrics cited above are source-reported by Gregory Young (*arXiv:2607.26245v1*, GitHub repository `gregyoung14/openmarket` tag `v0.5.2`).

### Negative evidence

1. **Failure to beat market-implied probability:** The 43-feature walk-forward model fails to surpass the naive mid-price prior out-of-sample (AUC 0.8377 vs 0.8405; Brier 0.165 vs 0.163; ECE 0.026 vs 0.014).
2. **Economic infeasibility under fees:** Despite an observable 347 ms causal response delay between venues, simulated execution yields $-0.116$ payoff units per trade under standard 1% taker fees and 0.5% crossing slippage.
3. **Spread barrier:** With Polymarket top-of-book spreads fixed at 1 tick ($0.01$), paying the half-spread immediately destroys the theoretical information advantage obtained from external CEX order flow.
4. **Heavy tails in event pairing:** Source-clock lead-lag exhibits wide tails (-186 ms to +316 ms), indicating substantial latency jitter and queue contention during high-volatility events.

## Falsification plan

To falsify the author's negative conclusion and demonstrate an exploitable alpha:
1. **Maker Quoting / Passive Limit Orders:**
   - Test whether resting passive limit orders on Polymarket (capturing the 1-tick spread rather than paying crossing fees and slippage) can earn positive expectancy when canceled or repriced using Binance spot signals.
   - *Falsification rule:* If passive limit order execution suffers adverse selection greater than the 1-tick spread (fill rate conditional on adverse moves $> 70\%$), the passive alpha hypothesis is disproven.
2. **Extreme Volatility Jump Threshold Stress:**
   - Filter entry signals strictly to extreme Binance price shocks ($\ge 25\text{ bps}$ within 500 ms) where the 347 ms response latency might provide a price delta substantially wider than the 1-tick spread.
   - *Falsification rule:* If net trade expectancy remains $\le 0.00$ after accounting for polygon transaction gas and latency race failures, the latency arbitrage hypothesis is completely refuted.
3. **Multi-Vantage Clock Synchronization Test:**
   - Deploy redundant collectors collocated in Frankfurt, Tokyo, and Virginia to resolve the $\pm 99\text{ ms}$ constant-offset ambiguity.
   - *Falsification rule:* If resolving clock ambiguity reveals that Polymarket quotes actually lead Binance or adjust concurrently at the matching engine level, cross-venue lead-lag alpha is definitively falsified.

## Crypto portability

- **Portability status:** `direct` for Binance spot and Polymarket BTC 15-minute binary contracts; `unproven` for non-crypto prediction markets.
- **Crypto-specific structural factors:**
  1. *Underlying asset characteristics:* High volatility and continuous 24/7 liquidity on Binance BTC/USDT provide dense millisecond order flow. In contrast, political, macro, or sports prediction markets lack a continuous high-frequency external reference stream, making cross-venue lead-lag pairing impossible.
  2. *Polygon blockchain vs CEX latency:* While Polymarket CLOB matching occurs off-chain on a centralized relayer, settlement and funding occur on the Polygon network. Network congestion or RPC delays can impede automated balance updates and order management.
  3. *Binary settlement boundary:* The contract value approaches a discontinuous step function ($0$ or $1$) as expiration approaches, causing gamma and vega to spike erratically within the final 60 seconds.

## Limitations

- `null-result`: The source explicitly demonstrates that directional lead-lag trading between Binance and Polymarket binary contracts is economically unprofitable under standard fees.
- `single-vantage clock ambiguity`: A single collection vantage point leaves an unresolved constant-offset uncertainty of approximately $\pm 99\text{ ms}$.
- `archive coverage gaps`: Data collection over the 93-calendar-day span contains multi-day WebSocket disconnections, covering 54 active Polymarket days out of 93.
- `not independently reproduced`: Findings reflect the source-reported experimental outputs from Young (2026).
- `niche contract scope`: Results are specific to short-duration (15-minute) BTC contracts and do not generalize to long-horizon political or economic event contracts.

## Implementation status

`not-implemented`. This strategy has not been implemented or evaluated within PyBroker, NautilusTrader, or any internal paper or live trading infrastructure.

## Adoption boundary

Research material only. A record being present in this repository does not constitute evidence of profitability, approval for implementation, or authorization for paper, testnet, or live trading.

## Related Wiki records

- `[[quant/crypto-cross-platform-binary-threshold-mispricing-polymarket-binance-2026-09-01]]`
- `[[quant/crypto-prediction-market-high-frequency-combinatorial-arbitrage-2026-09-01]]`
- `[[quant/crypto-short-horizon-prediction-market-settlement-push-reversal-2026-09-01]]`
- `[[quant/defi-prediction-market-uniform-loss-amm-lvr-dynamic-liquidity-2026-09-02]]`
- `[[quant/prediction-market-optimal-market-making-latent-belief-hjb-2026-09-01]]`

## Sources

- Gregory Young, "OpenMarket: A Synchronized Polymarket–Binance Dataset for High-Frequency Prediction-Market Research", arXiv preprint `arXiv:2607.26245v1 [q-fin.TR, cs.CE]`, submitted July 28, 2026. DOI: [10.48550/arXiv.2607.26245](https://doi.org/10.48550/arXiv.2607.26245). Stable URL: https://arxiv.org/abs/2607.26245. Full text HTML: https://arxiv.org/html/2607.26245v1.
- Gregory Young, OpenMarket Open-Source Platform Repository, GitHub: https://github.com/gregyoung14/openmarket, frozen release tag `v0.5.2`, immutable commit SHA `6e6cc240f32ab9fd2f8fa602bd0aba823b24bfee`.
- Gregory Young, OpenMarket Dataset and Model Releases, Hugging Face:
  - Dataset: `gregyoung14/openmarket-btc-polymarket` (split `v0.4.3-unified`). URL: https://huggingface.co/datasets/gregyoung14/openmarket-btc-polymarket.
  - Models: `gregyoung14/openmarket-models` (model `v0.2.1/`). URL: https://huggingface.co/gregyoung14/openmarket-models.
