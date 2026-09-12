---
schema: strategy-research-record-v1
title: Polymarket 15-Minute Crypto Binary Tri-Transformer Market Making and Latency Adverse Selection
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - prediction-market
  - polymarket
  - market-making
  - transformer
  - order-flow
  - microstructure
  - high-frequency
  - adverse-selection
  - falsification
status: research-only
confidence: high
source_as_of: 2026-09-10
sources:
  - "QuantumSlayer, 'poly-15min: A quantitative market-making engine for Polymarket 15-minute crypto up/down binary contracts using three Transformer models', GitHub repository, commit 8e5a8cc51955c9c52af26a51e74d4244af1f6756, September 2026. URL: https://github.com/QuantumSlayer/poly-15min"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Polymarket 15-Minute Crypto Binary Tri-Transformer Market Making and Latency Adverse Selection

## Provenance

- **Repository:** QuantumSlayer / `poly-15min`
- **Canonical GitHub URL:** https://github.com/QuantumSlayer/poly-15min
- **Immutable Commit SHA:** `8e5a8cc51955c9c52af26a51e74d4244af1f6756`
- **Primary Source Files Examined:**
  - `README.md` (overview, model architectures, timeline, failure analysis)
  - `docs/technical-reference.md` (detailed technical manual covering Chapters 01–09)
  - `quote_seq.py` (Model B quantile inference and directional quote policy)
  - `quote_iv.py` (Model C event replay, inference, and book mid reconstruction)
  - `market_lib.py` (feed handlers, microprice computation, Kalman volatility calibrator)
  - `trade.py` (fair center synthesis, Student-t spot inversion, quote width, inventory tilt, GTC execution)
  - `trade_lib.py` (CLOB authentication, order I/O, position monitoring)
  - `utils.py` (Model A architecture, Student-t loss, feature extraction)
- **Source As-Of Date:** 2026-09-10 (repository push date).
- **License:** Sustainable Use License 1.0 (source-available for noncommercial and internal research purposes).
- **Target Venue & Instrument:** Polymarket Central Limit Order Book (CLOB) on Polygon, trading rolling 15-minute crypto Up/Down binary contracts (binary cash-or-nothing options settling to $1.00 or $0.00).

## Economic mechanism

### Source-reported

In rolling 15-minute binary prediction markets (such as Polymarket `btc-updown-15m-<timestamp>`), contract payoff is binary: $1.00 if the ending reference price equals or exceeds the opening reference price ($S_{\text{close}} \ge S_{\text{open}}$), and $0.00$ otherwise. Passive liquidity provision aims to capture the bid-ask spread on both YES and NO outcome tokens by maintaining continuous resting limit orders around an estimate of the fair binary probability.

The source structures market making around three distinct predictive estimation channels:
1. **Underlying return distribution scale (Model A):** Uses 300 seconds of Binance perpetual futures order flow to estimate a zero-location Student-t distribution with scale $\text{iv}$ and degrees of freedom $\text{df}$. As remaining contract duration $\tau \in [1, 900]$ decays, scale scales as $\sigma_{\text{eff}} = \text{iv} \cdot \sqrt{\tau / 900}$. The cumulative distribution function gives an objective probability that spot terminates above the opening barrier.
2. **High-frequency directional drift (Model B):** Uses 32 contiguous Coinbase order-book ticks to predict return quantiles ($q \in \{0.10, 0.25, 0.50, 0.75, 0.90\}$) across ultra-short horizons (2s, 5s, 10s). A directional score shifts the quote center by up to $\pm 0.02$ ($0.02 per share) or withdraws passive quotes on the adverse side to avoid being picked off.
3. **Endogenous Polymarket book dynamics (Model C):** Uses an event sequence of up to 64 mixed Coinbase and Polymarket events to estimate the contemporaneous book mid-price residual $\Delta_{\text{mid}}$ and half-spread $\text{hs}_{\text{pred}}$.
4. **Kalman volatility calibration:** Solves for the implied volatility consistent with Polymarket's size-weighted book mid-price, and runs a 1D log-space Kalman filter to track the ratio $\text{pm\_iv\_mult} = \exp(k_t)$ between Polymarket implied volatility and Model A underlying volatility. This ratio scales inventory limits dynamically.

**Failure Mechanism (Source-reported post-mortem):** The system operated profitably in live trading on BTC 15-minute contracts until late December 2025. It permanently lost profitability because it relied on public WebSocket feeds and public internet infrastructure, leaving its quote cancellation requests $\ge 100\text{ ms}$ behind participants with direct low-latency exchange access. When underlying spot prices jumped on centralized exchanges, informed takers crossed the resting GTC orders on Polymarket before the cancellation requests could be matched, generating severe toxic adverse selection that erased all earned spread capture.

### Research interpretation

The primary economic edge in high-frequency binary market making is structural: earning the 1-tick to 2-tick spread ($0.01–$0.02) across complementary outcome tokens while neutralizing directional inventory risk. However, binary cash-or-nothing options have discontinuous delta and infinite gamma at expiration when spot is near the strike. 

As expiration approaches ($\tau \to 0$):
- If spot is far from the barrier, the outcome is near certainty (0 or 1), spread compresses, and volume collapses.
- If spot is close to the barrier, small spot jumps create massive instantaneous revaluations in the binary contract.
- A market maker with passive resting limit orders writes a free latency option to informed high-frequency takers. A $\ge 100\text{ ms}$ lag in canceling stale resting quotes guarantees that every incoming fill during a spot move is toxic adverse selection. The strategy's survival strictly depends on whether the cancel-to-execution latency envelope is faster than the cross-venue lead-lag diffusion time between Binance/Coinbase and the Polymarket matching engine.

## Signal

### Model Architecture and Signal Specifications (Source-reported)

```text
Binance Futures Trades/Bars (300s x 14) ──> [Model A: 4L, 4H, d=96]  ──> Student-t iv, df ──> P(Up) via CDF
                                                                              │
                                                                   Kalman Volatility Calibrator
                                                                              │ (pm_iv_implied_900, pm_iv_mult)
                                                                              ▼
Mixed Events: CB + Polymarket (64 x 22) ──> [Model C: 4L, 8H, d=192] ──> Book pred_mid, hs_pred
                                                                              │
Coinbase L2 Ticks (32 x 75)             ──> [Model B: 4L, 8H, d=256] ──> Directional seq_skew (±0.02)
                                                                              │
                                                                              ▼
                                                                  [Synthesized Fair Center]
                                                                  [Spread Realized Prob Addon]
                                                                  [Crossing & Inventory Gates]
                                                                              │
                                                                              ▼
                                                                Passive GTC Bids/Asks (YES/NO)
```

1. **Model A (Return Distribution Scale):**
   - *Inputs:* Sequence of 300 rows $\times$ 14 features from Binance BTC perpetual futures trades (close, VWAP, quantities, trade counts, buy/sell volumes, log returns, volume imbalance) + 19 static features (minute returns, basis, time-of-day sin/cos, time-to-expiration $\tau$).
   - *Architecture:* 4-layer Transformer encoder, 4 attention heads, hidden dimension 96, attention pooling readout, static MLP fusion. Parameter count: 420,995 trainable parameters per asset.
   - *Outputs:* Zero-location Student-t distribution scale $\text{iv}_{900}$ and degrees of freedom $\text{df}$.
   - *Effective Volatility:* $\sigma_{\text{eff}} = \text{iv}_{900} \cdot \sqrt{\tau / 900}$, floored at $\tau \ge 1.0\text{ s}$.
   - *Binary Probability Formulation:*
     $$z = \frac{\ln(K_{\text{barrier}}) - \ln(S_{\text{now}})}{\max(\sigma_{\text{eff}}, 10^{-12})}$$
     $$P(\text{YES}) = 1.0 - F_{\text{Student-t}}(z, \text{df})$$
     where $K_{\text{barrier}}$ is the opening reference price proxy (`prev_close`), evaluated at floored/ceiled bounds $[K_{\text{low\_floor}}, K_{\text{high\_ceil}}]$, giving $t_{\text{fair\_mid}} = 0.5 \cdot (P(K_{\text{low\_floor}}) + P(K_{\text{high\_ceil}}))$.

2. **Model B (Short-Term Directional Quantiles):**
   - *Inputs:* Sequence of 32 contiguous Coinbase L2 ticks $\times$ 75 features (L2 depth, imbalance, microprice, trade flow) + 229 static features. Gaps $> 1\text{ s}$ reset the window.
   - *Architecture:* 4-layer Transformer encoder, 8 attention heads, hidden dimension 256, last-token readout routed to asset-specific heads. Parameter count: 2,596,156 trainable parameters.
   - *Outputs:* 15 quantile forecasts: $q \in \{0.10, 0.25, 0.50, 0.75, 0.90\}$ across three horizons $h \in \{2\text{s}, 5\text{s}, 10\text{s}\}$.
   - *Policy Mapping:*
     - Linear interpolation of quantiles to estimate $P(Y > 0)$.
     - Effect size: $z = \frac{q_{0.50}}{\max(q_{0.75} - q_{0.25}, 10^{-18})}$.
     - Horizon score: $\text{score}_h = \tanh(|z| / 2.0) \cdot \text{sign}(q_{0.50})$.
     - Aggregate score: $\text{seq\_score} = 0.50 \cdot \text{score}_{2\text{s}} + 0.35 \cdot \text{score}_{5\text{s}} + 0.15 \cdot \text{score}_{10\text{s}} \in [-1.0, +1.0]$.
     - Skew: $\text{seq\_skew} = \text{seq\_score} \cdot 0.02 \in [-0.02, +0.02]$.
     - One-sided gate: Activated if $|\text{seq\_score}| > 0.80$ (or tail-strong condition: $|z| \ge 0.60$ with $q_{0.10} > 0$ or $q_{0.90} < 0$). In the live trader, an aggressive one-sided cancel is triggered at $|\text{seq\_score}| > 0.10$.

3. **Model C (Book Mid Residual & Half-Spread):**
   - *Inputs:* Up to 64 events $\times$ 22 features (moneyness, flow, Polymarket CLOB book prices, calibrated IV scale `pm_iv_implied_900`, $\tau$). Minimum 16 events required.
   - *Architecture:* 4-layer Transformer encoder, 8 attention heads, hidden dimension 192. Parameter count: 1,492,808 trainable parameters.
   - *Outputs:* Book mid residual $\Delta_{\text{mid}}$ and predicted half-spread $\text{hs}_{\text{pred}} \ge 0$. Reconstructed mid: $\text{pred\_mid} = \text{ref\_mid} + \Delta_{\text{mid}}$.

4. **Kalman Volatility Calibration:**
   - *Polymarket Observed Mid:* $p_{\text{obs}} = \frac{P_b Q_b + P_a Q_a}{Q_b + Q_a}$.
   - *Student-t Implied Volatility:* Inverts $p_{\text{obs}}$ for $\text{iv}_{\text{obs}}$ over $[10^{-5}, 5 \cdot 10^{-3}]$ via bisection (50 iterations, tolerance $10^{-6}$).
   - *Observation in Log Space:* $y = \ln(\text{clip}(\text{iv}_{\text{obs}} / \text{model\_iv}, 0.2, 5.0))$.
   - *Quality Weighting:* $Q = \frac{1}{1 + (\text{spread} / 0.02)^2} \cdot \text{clip}(2 |p_{\text{obs}} - 0.5|, 0, 1)$.
   - *Measurement Noise:* $R_t = 0.04 / \max(Q, 10^{-12})$.
   - *State Update:*
     $$K_t = \frac{P_{t-1}}{P_{t-1} + R_t}, \quad k_t = k_{t-1} + K_t(y - k_{t-1}), \quad P_t = (1 - K_t)P_{t-1} + 10^{-5}$$
     $$\text{pm\_iv\_mult} = \exp(k_t), \quad \text{pm\_iv\_implied\_900} = \text{pm\_iv\_mult} \cdot \text{model\_iv}$$

5. **Quote Center & Half-Spread Synthesis:**
   - $\text{center}_0 = \text{clip}(\text{pred\_mid} + \text{seq\_skew}, 0.0, 1.0)$
   - $\text{iv\_skew} = \text{clip}(0.15 \cdot (t_{\text{fair\_mid}} - \text{center}_0), -0.01, 0.01)$
   - $\text{fair\_center} = \text{clip}(\text{center}_0 + \text{iv\_skew}, 0.0, 1.0)$
   - *Realized Volatility Add-on:* Spot is inverted from $\text{fair\_center} \to S_{\text{center}}$ via Student-t bisection. Shifting by 1-second realized volatility $\sigma_{1\text{s}} = \max(\sigma_{\text{EWMA}}, \text{RV}_{3\text{s}} / \sqrt{3}, 0.0)$ produces:
     $$S_{\text{up}} = S_{\text{center}} e^{+\sigma_{1\text{s}}}, \quad S_{\text{dn}} = S_{\text{center}} e^{-\sigma_{1\text{s}}}$$
     $$\text{hs}_{\text{realized\_prob}} = 0.5 \cdot \max(0.0, P(S_{\text{up}}) - P(S_{\text{dn}}))$$
   - *Total Quote Half-Spread:* $\text{quote\_half} = \max(\text{hs}_{\text{pred}} + \text{hs}_{\text{realized\_prob}}, \text{tick\_sz})$.
   - *Raw Quotes:* $p_{\text{bid}} = \text{fair\_center} - \text{quote\_half}$, $p_{\text{ask}} = \text{fair\_center} + \text{quote\_half}$.
   - *Crossing Guard:* If $|\text{seq\_score}| \le 0.50$, clamps $p_{\text{bid}} \le \text{pred\_book\_ask} - 0.01$ and $p_{\text{ask}} \ge \text{pred\_book\_bid} + 0.01$.
   - *Tick Rounding:* $P_{\text{YES\_bid}} = \lfloor p_{\text{bid}} / 0.01 \rfloor \cdot 0.01$, $P_{\text{YES\_ask}} = \lceil p_{\text{ask}} / 0.01 \rceil \cdot 0.01$.
   - *Complementary NO:* $P_{\text{NO\_bid}} = 1.0 - P_{\text{YES\_ask}}$, $P_{\text{NO\_ask}} = 1.0 - P_{\text{YES\_bid}}$.

6. **Order Placement and Cancellation Logic:**
   - Orders placed as passive GTC orders on both YES and NO order books.
   - *Cancellation Band:* Open orders canceled if price falls outside fair band $[\text{fair\_center} - 0.5 \cdot \text{hs}_{\text{pred}}, \text{fair\_center} + 0.5 \cdot \text{hs}_{\text{pred}}]$.
   - *One-sided Flush:* If $|\text{seq\_score}| > 0.10$, cancels all resting orders on the adverse side.
   - *Timing Guards:*
     - Head guard: $S$ to $S + 8\text{ s}$ (no quoting during initial contract opening).
     - Tail guard: $S + 885\text{ s}$ to $S + 900\text{ s}$ (cancels all resting orders; nominal quoting interval = 877 seconds).

7. **Inventory Management & Dynamic Tilting:**
   - *Default Quote Size:* 5 shares per quote.
   - *Inventory Cap:* 20 shares (`inv_cap`).
   - *Cumulative Fill Cap:* 20,000 shares per slug (`vol_cap`).
   - *Dynamic Time-Decay Tilt:* As contract progresses ($p_{\text{prog}} = 1.0 - \tau / 900$):
     - If spot diverges from opening price in the same direction as IV multiplicity ($\text{sign}(\Delta_{\text{px}} \cdot (\text{pm\_iv\_mult} - 1)) > 0$): $\text{lower\_cap} = \text{inv\_cap} \cdot (1.2 p_{\text{prog}} - 1.0)$, restricting further accumulation on the winning/expensive side.
     - Else: $\text{upper\_cap} = \text{inv\_cap} \cdot (1.0 - 1.2 p_{\text{prog}})$.
   - *Balance Rebalancing Switch:* If YES balance $> 25$ shares, replaces NO BUY with YES SELL; if NO balance $> 25$ shares, replaces YES BUY with NO SELL.

## Required data

- **Instruments:** Rolling 15-minute BTC binary contracts (`btc-updown-15m-<start_ts>`), settling on Polymarket CTF Exchange on Polygon.
- **Reference Underlyings:** BTC/USDT perpetual futures (Binance), BTC/USD spot (Coinbase), and Chainlink RTDS reference feeds.
- **Venue Feeds:**
  - Polymarket CLOB WebSocket: L2 order book (bids/asks/sizes), user WebSocket (fills, order status, position balances).
  - Coinbase WebSocket: Ticker (microprice), L2 depth updates (level sizes, spread, imbalance), trade prints.
  - Binance Futures WebSocket: Trade stream, 1-second ticks, 1-minute Kline bars (VWAP, taker volumes, trade counts).
- **Timeframe & Alignment:** Continuous event stream aggregated into 1-second grids for Model A (300 steps), tick-level buffer for Model B (32 ticks), and mixed event stream for Model C (64 events).
- **Point-in-time Integrity:** All inferences use strictly trailing causal data. However, WebSocket transport delays introduce variable arrival latency ($> 100\text{ ms}$).

## Execution assumptions

- **Order Type:** Good 'Til Cancelled (GTC) limit orders submitted via Polymarket CLOB API without an exchange-enforced post-only flag (source-reported). Marketable limit orders execute as taker (source-reported).
- **Fees:** Polymarket CLOB charges 0.00% maker / taker fee on standard binary markets (source-reported); however, crossing wide spreads incurs heavy economic penalty. Any fee stress model assuming non-zero fees (0.05% to 1.00%) is labeled `research-proposed`.
- **Fill Model:** Passive limit order queue priority based on price-time priority on Polymarket's off-chain relayer matching engine (source-reported). Fills are asynchronous and report back via user WebSocket (source-reported). For offline simulation, an order-book queue fill simulation with cancellation latency delay is `research-proposed`.
- **Concurrency & I/O:** Asyncio event loop with a dedicated thread pool (8 workers, semaphore = 8) for blocking cryptographic order signing and HTTP/WebSocket I/O (source-reported).
- **Latency Assumption:** Source empirically observed $\ge 100\text{ ms}$ latency between underlying CEX spot price movements and Polymarket order book updates/cancellations over public internet (source-reported). A benchmark cancellation latency threshold of 50 ms for adverse-selection cutoff is `research-proposed`.

## Evidence

### Source-reported

1. **Live Production Track Record:** The system operated live on BTC 15-minute contracts on Polymarket. The author reports that the strategy was profitable on BTC for a sustained period until late December 2025.
2. **Relative Profitability:** The author explicitly discloses that total profits were "only a tiny fraction of those earned by the top accounts" on Polymarket, indicating that highly optimized collocated market makers extracted the vast majority of available economic rent.
3. **Decay and Termination:** The strategy ceased being profitable in late December 2025 due to latency disadvantage. Secondhand WebSocket feeds left the engine at least 100 ms behind participants with direct exchange connectivity, causing adverse selection that completely erased the strategy's trading advantage.
4. **Codebase Artifacts:** The repository preserves 6 trained model checkpoints totaling 5,772,944 parameters: 4 independent Model A checkpoints (BTC, ETH, SOL, XRP; 420,995 params each), 1 shared Model B checkpoint (2,596,156 params), and 1 shared Model C checkpoint (1,492,808 params).

### Independently reproduced

Not independently reproduced. Training datasets and raw historical fill logs were permanently lost upon decommissioning, as explicitly documented by the repository author.

### Negative evidence

1. **Severe Adverse Selection Under Public Latency:** The primary failure mode is toxic flow. A market maker relying on public WebSocket feeds is exposed to latency arbitrage: when Binance/Coinbase spot prices jump, external HFT participants cross resting Polymarket limit orders before the engine's cancellation request reaches the matching engine.
2. **Defect & Risk Catalog (Confirmed via Technical Reference):**
   - *Plaintext Key Logging:* WebSocket subscription payload dumped private keys, API secrets, and passphrases into local log files in plaintext (`logs/ws_user/sent/`).
   - *Hard-Exit Safety Gap:* Safety checks and position threshold breaches terminate the Python process without issuing cancellation requests, leaving active GTC orders orphaned on the live venue.
   - *Cross-Asset Config Defect:* The engine evaluated `MM_BTC_QSIZE`, `MM_BTC_INVCAP`, and `MM_BTC_VOLCAP` for all traded assets (ETH, SOL, XRP), meaning non-BTC assets erroneously inherited BTC-specific share quantities.
   - *Idempotency Defect:* Submission retries lacked unique client order IDs, creating potential duplicate exposure upon transient network timeouts.
   - *Feature Omission in Live Ingestion:* Live Model C ingestion omitted `model_df` and passed raw zeros into z-score scalers.

## Falsification plan

To falsify the viability of passive Tri-Transformer market making on binary prediction markets:

1. **Latency Sensitivity Stress Test:**
   - *Method:* Simulate artificial network latency delays in quote cancellation ($\Delta t \in \{10\text{ ms}, 50\text{ ms}, 100\text{ ms}, 250\text{ ms}, 500\text{ ms}\}$) on synchronized historical tick data (pairing Binance spot jumps with Polymarket L2 book state).
   - *Research-defined falsification threshold:* If net market making PnL turns negative at cancellation latency $\ge 50\text{ ms}$, reject the hypothesis that model predictive precision can compensate for latency disadvantage.
   - *Action:* Classify the strategy as strictly latency-dominated rather than alpha-dominated; disqualify execution without direct cross-connects.

2. **Model Ablation Falsification Test:**
   - *Method:* Test the contribution of each model component:
     - Configuration 1: Pure Model C (mid/spread) without Model A or Model B.
     - Configuration 2: Model C + Model A (Student-t pull) without Model B.
     - Configuration 3: Model C + Model B (directional skew) without Model A.
     - Configuration 4: Naive heuristic market making (quoting Polymarket mid $\pm 1$ tick).
   - *Research-defined falsification threshold:* If Configuration 4 matches or outperforms Configurations 1–3 after accounting for model inference compute latency ($15–35\text{ ms}$ on CPU/GPU), reject the hypothesis that multi-Transformer sequence modeling provides incremental net alpha over naive book-following heuristics.

3. **Adverse Selection Ratio Test:**
   - *Method:* Measure the markout return of filled orders at horizons $t \in \{1\text{s}, 5\text{s}, 15\text{s}, 60\text{s}, \text{expiry}\}$ post-fill.
   - *Research-defined falsification threshold:* If average markout return across all passive fills is negative at $t = 15\text{s}$ (i.e., filled bids are immediately followed by downward price moves, and filled asks by upward price moves), the passive quoting strategy is dominated by toxic adverse selection.

4. **Fee and Rebate Dependency Test:**
   - *Method:* Evaluate strategy profitability under non-zero maker/taker fee regimes (e.g., 0.10% to 1.00% maker fees or withdrawal of Polymarket liquidity reward incentives).
   - *Research-defined falsification threshold:* If net Sharpe drops below 0.0 under any fee $\ge 5\text{ bps}$, the edge is entirely an artifact of zero-fee prediction-market subsidies.

## Crypto portability

- **Portability status:** `direct` for Polymarket crypto binary contracts (BTC, ETH, SOL, XRP); `adapted` for other prediction market venues (e.g., Kalshi, SX Bet, Azuro); `not applicable` to standard crypto perpetuals or spot without binary cash-or-nothing terminal settlement.
- **Porting Adaptation (`research-proposed`):** Porting this Tri-Transformer market making framework to CFTC-regulated prediction markets (such as Kalshi) or other on-chain prediction protocols (such as SX Bet) is `research-proposed` and `unproven`. It requires replacing Polygon CLOB RPC interfaces with venue-specific order types, adapting for discrete batch auctions, and substituting venue-compliant settlement oracles.
- **Venue Microstructure Differences:**
  - Polymarket uses an off-chain centralized relayer matching engine with on-chain settlement on Polygon. Order submission/cancellation is subject to relayer rate limits, WebSocket disconnects, and gas-free meta-transactions.
  - Unlike perpetual futures with continuous funding rates, binary options feature non-linear delta and gamma that explode near expiration, making quote management in the final 60 seconds toxic. The source-implemented 15-second tail guard is mandatory.
  - Reference price oracle resolution (Chainlink RTDS / UMA Optimistic Oracle) can diverge from centralized exchange spot prices during flash crashes, introducing oracle basis risk.

## Limitations

- **Latency Domination (`underspecified / unproven`):** The primary source demonstrates that without sub-50ms co-located execution infrastructure, algorithmic market making on prediction markets is structurally unviable due to toxic picking-off.
- **Model Checkpoint Reproducibility Gap (`data gap`):** Training data and data pipeline code were lost; existing models cannot be retrained on new market regimes without engineering an entirely new dataset builder.
- **Single-Asset Empirical History:** Although 4 assets were modeled, only BTC was live-traded; multi-asset portfolio diversification and correlated inventory risk remain completely unproven.
- **Security & Concurrency Deficiencies:** Plaintext credential logging and lack of process shutdown cancellation guards make the public code unsuitable for direct deployment without a complete architectural rewrite.

## Implementation status

`not-implemented`. No implementation of the Tri-Transformer market making framework or Polymarket CLOB integration exists in the internal quantitative research stack.

## Adoption boundary

`research-only`. This record is captured strictly for quantitative research, microstructure modeling, and adverse-selection falsification analysis. It does **not** constitute an approved trading strategy, an implementation authorization, or permission to deploy capital on Polymarket or any live trading venue.

## Related Wiki records

- `polymarket-binance-high-frequency-binary-lead-lag-2026-09-02.md` (Young 2026, arXiv:2607.26245: OpenMarket high-frequency cross-venue lead-lag showing aggressive taker crossing failure)
- `crypto-prediction-market-onchain-trade-misattribution-longshot-spread-2026-09-02.md` (Dubach 2026, arXiv:2604.24366: Polymarket order book microstructure and maker concentration)
- `polymarket-negrisk-executable-arbitrage-token-conversion-2026-09-03.md` (Polymarket combinatorial multi-outcome token conversion arbitrage)
- `prediction-market-optimal-market-making-latent-belief-hjb-2026-09-01.md` (Stochastic control and HJB equations for binary prediction market making)
- `deep-rl-market-making-regime-switching-bocpd-scenario-bandit-2026-09-11.md` (Moret & Lillo 2026, arXiv:2609.11614: Distributional RL market making under regime-switching order flow)

## Sources

1. **Primary Implementation & Documentation Source:**
   - Author: QuantumSlayer
   - Repository: `QuantumSlayer/poly-15min`
   - Description: "Code for Polymarket 15-minute crypto market making using three Transformer models. Profitable on BTC until late December 2025. Discontinued and unmaintained."
   - Stable URL: https://github.com/QuantumSlayer/poly-15min
   - Immutable Commit SHA: `8e5a8cc51955c9c52af26a51e74d4244af1f6756`
   - Exact Paths:
     - `README.md`
     - `docs/technical-reference.md`
     - `quote_seq.py`
     - `quote_iv.py`
     - `market_lib.py`
     - `trade.py`
     - `trade_lib.py`
     - `live_prediction.py`
     - `utils.py`
   - As-of Date: 2026-09-10
   - License: Sustainable Use License 1.0
