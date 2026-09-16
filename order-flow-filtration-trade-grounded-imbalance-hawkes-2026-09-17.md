---
schema: strategy-research-record-v1
title: "Structural Order-Flow Filtration and Trade-Grounded Imbalance Directional Signal Extraction"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-07-31
sources:
  - https://arxiv.org/abs/2507.22712
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Structural Order-Flow Filtration and Trade-Grounded Imbalance Directional Signal Extraction

## Provenance

- **Primary Source:** Aditya Nittur Anantha (Indian Institute of Science / Indian Institute of Technology Kharagpur), Shashi Jain (Indian Institute of Science, Bangalore), and Prithwish Maiti, *"Order-Flow Filtration and Directional Association with Short-Horizon Returns"* (also titled in manuscript build *"Order Book Filtration and Directional Signal Extraction at High Frequency"*), arXiv preprint `arXiv:2507.22712v1 [q-fin.TR]`, submitted July 2025.
- **Canonical arXiv URL:** https://arxiv.org/abs/2507.22712
- **Full Text HTML:** https://arxiv.org/html/2507.22712v1
- **DOI:** https://doi.org/10.48550/arXiv.2507.22712
- **Licence:** Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0).
- **Deduplication Audit:** A full audit of existing repository strategy records confirms zero prior citations of `2507.22712`, Anantha, Jain, or Maiti. Existing repository records covering high-frequency microstructure or order flow (`contrarian-market-making-fill-probability-order-flow-2026-09-01.md`, `crypto-order-flow-online-sgd-microstructure-horizon-cost-falsification-2026-09-13.md`, `crypto-volume-synchronized-probability-of-toxicity-vpin-microstructure-2026-08-31.md`, `dealer-toxic-flow-infinite-horizon-internalisation-externalisation-2026-09-17.md`) focus on fill probabilities, toxic flow internalisation, or online parameter adaptation. None implement observable structural filtration rules (order lifetime, update frequency, or inter-modification delay) or contrast associative versus causal Hawkes excitation norms between book-derived and trade-grounded order flow imbalance.

## Economic mechanism

### Source-reported

In modern electronic limit order book (LOB) markets, algorithmic participants and latency-sensitive market makers submit dense event streams containing vast numbers of transient or fleeting quotes. Empirical studies indicate that a large fraction of quotes are canceled within milliseconds without trading intent, often functioning as latency-arbitrage probes, quote-stuffing buffers, or deceptive liquidity displays.

Standard Order Book Imbalance (OBI)—defined as the signed volume or count difference between bid and ask sides—is commonly used as a short-horizon directional indicator. However, naive OBI computed on raw event streams is heavily contaminated by fleeting liquidity, degrading the informational fidelity of the signal.

The authors propose a systematic filtration framework that applies real-time observable structural filters to the event stream before reconstructing the order book:
1. **Lifetime-based filtering:** discards orders that survive less than a threshold duration $\bar{\mathcal{T}}$, removing ephemeral orders.
2. **Modification-count filtering:** removes orders subject to frequent updates exceeding $\bar{M}$, targeting non-committal strategic probing.
3. **Modification-time filtering:** requires the time lag between successive order updates $\mathcal{M}_j$ to exceed a threshold $\bar{\mathcal{M}}$, filtering out tightly clustered modification bursts (associated with spoofing or high-frequency quote flickering).

To evaluate signal quality, the paper establishes a three-layer diagnostic ladder:
- **Layer 1: Contemporaneous Pearson correlation** between raw OBI and traded returns.
- **Layer 2: Discretized regime-count modeling** using cross-correlation and autoregression-adjusted $R^2$.
- **Layer 3: Multivariate Hawkes point process excitation**, measuring causal cross-excitation from OBI regimes to return regimes.

Furthermore, the paper contrasts book-derived OBI against an alternative benchmark: **Trade-based OBI ($OBI^{(T)}$)**, constructed strictly from executed transactions (buyer-initiated minus seller-initiated trade volume).

### Research interpretation

The economic thesis is that **raw book-derived order book imbalance reflects primarily associative, self-exciting microstructural feedback (quote replenishment and cancellations) rather than an exogenous causal driver of short-term returns. In contrast, trade-grounded order flow captures true capital commitment and terminal execution pressure, which possesses genuine causal predictive power over short-horizon returns that is amplified when fleeting order modifications are filtered out.**

In high-frequency alpha design, relying on raw book imbalance subjects strategies to adverse selection from phantom liquidity that cancels before an execution can take place. Structural modification-time filtering purges this non-committal noise, but book-level OBI remains structurally dominated by internal self-excitation. To achieve causal alpha, the signal must be anchored on terminal execution events (trade-based OBI) conditioned on a structurally filtered order environment.

## Signal

### Event Stream and Structural Filtration Rules (Source-Reported)

The market event stream $\epsilon_t \in \mathcal{E}$ consists of discrete events uniquely tracked by an Order ID (OID):
- Event types: `NEW`, `MODIFY`, `CANCEL`, `TRADE`.
- Event attributes: timestamp $t_i$, Order ID $j$, side $Y_i \in \{b, s\}$, price $p_i$, and size $q_i$.

Three observable real-time filtration schemes are defined:
1. **Lifetime Filter ($\mathscr{F}^\mathcal{T}$):** Retains order events only if the total survival time $\mathcal{T}_j \ge \bar{\mathcal{T}}$. Evaluated thresholds: $\bar{\mathcal{T}} \in \{100, 500, 1000\}\text{ ms}$.
2. **Modification Count Filter ($\mathscr{F}^M$):** Retains order events only if the total number of modifications $M_j \le \bar{M}$. Evaluated thresholds: $\bar{M} \in \{1, 3, 5\}$.
3. **Modification Time Filter ($\mathscr{F}^\mathcal{M}$):** Retains order events only if the lag between successive modifications $\mathcal{M}_j \ge \bar{\mathcal{M}}$. Evaluated thresholds: $\bar{\mathcal{M}} \in \{50, 100, 200\}\text{ ms}$.

**Execution Consistency Protocol (Source-Reported):**
When reconstructing the filtered limit order book, any new order or modification matching an excluded Order ID is ignored. However, if a filtered Order ID executes against a resting order, its trade tick is strictly retained to preserve execution consistency and prevent structural book imbalance.

### Imbalance Signal Construction (Source-Reported)

1. **Filtered Book-Derived Order Book Imbalance ($OBI^{(f)}$):**
   Over an evaluation lookback window $(\tau - h, \tau]$ of length $h = 10\text{ seconds}$:
   $$OBI^{(f)}(\tau, h) = \frac{N_b^{(f)}(\tau, h) - N_s^{(f)}(\tau, h)}{N_b^{(f)}(\tau, h) + N_s^{(f)}(\tau, h)}$$
   where $N_b^{(f)}, N_s^{(f)}$ denote the counts (or volume) of bid and ask events in the filtered reconstructed book.
2. **Trade-Based Order Imbalance ($OBI^{(T)}$):**
   Derived exclusively from signed executed trades over $(\tau - h, \tau]$:
   $$OBI^{(T)}(\tau, h) = \frac{V_{buy}(\tau, h) - V_{sell}(\tau, h)}{V_{buy}(\tau, h) + V_{sell}(\tau, h)}$$
   where trades are signed via the standard tick rule (buyer-initiated vs. seller-initiated).
3. **Realized Traded Return ($\tilde{r}$):**
   Measured over the contiguous forecast window $(\tau, \tau + \xi]$ of length $\xi = 1\text{ second}$:
   $$\tilde{r}_{(\tau, \tau + \xi]} = \frac{S_{\tau + \xi} - S_\tau}{S_\tau}$$

### Diagnostic Scoring Functionals (Source-Reported)

- **Pearson Correlation ($\mathcal{S}^\rho$):** Contemporaneous correlation between $OBI(\tau, h)$ and $\tilde{r}_{(\tau, \tau + \xi]}$.
- **Discretized Regime Score ($\mathcal{S}^{\rho, \Lambda}$ and $\mathcal{S}^\mathcal{R}$):** Discretizes OBI into 9 regimes and returns into 4 regimes. Computes the masked $\ell_1$-norm of the regime correlation matrix $\rho_\tau \in \mathbb{R}^{9 \times 4}$ under a diagonality mask $\Lambda$, and the autoregression-adjusted $R^2$ from regressing return regime counts on OBI regime counts.
- **Hawkes Excitation Norm ($\mathcal{S}^\phi$):** Fits a 13-dimensional multivariate Hawkes process (9 OBI regimes + 4 return regimes) with sum-of-exponentials kernel $\phi_{ij}(t) = \sum_k \alpha_{ij,k} e^{-\beta_k t}$. Extracts the forward cross-excitation submatrix $\Phi_{OBI \to Ret} \in \mathbb{R}^{4 \times 9}$ and computes the Frobenius norm under a diagonality-weighted mask $M$:
  $$\mathcal{S}^\phi = \| M \odot \Phi_{OBI \to Ret} \|_F$$

### Operational Strategy Implementation (`research-proposed`)

Because the primary paper is an empirical econometric investigation of signal informativeness rather than an algorithmic execution system, the following operational trading rules are `research-proposed`:
- **Signal Frequency & Cadence:** Evaluated every $10\text{ seconds}$ on closed event windows ($h = 10\text{ s}$, `research-proposed`).
- **Composite Entry Rule:**
  - **Long Entry:** Enter long at market if Trade-based Imbalance $OBI^{(T)}(\tau, 10\text{s}) > +0.60$ (`research-proposed`) AND filtered book imbalance under Modification-Time Filtering ($\bar{\mathcal{M}} = 100\text{ ms}$) confirms direction: $OBI^{(MTF)}(\tau, 10\text{s}) > +0.10$ (`research-proposed`).
  - **Short Entry:** Enter short at market if $OBI^{(T)}(\tau, 10\text{s}) < -0.60$ (`research-proposed`) AND $OBI^{(MTF)}(\tau, 10\text{s}) < -0.10$ (`research-proposed`).
- **Exit & Holding Period:** Fixed horizon exit at $\tau + 2\text{ seconds}$ (`research-proposed`), or early exit if $OBI^{(T)}$ crosses zero in the opposite direction (`research-proposed`).
- **Risk / Stop Loss:** Hard stop loss at $1.5 \times \text{spread}$ (`research-proposed`).
- **Position Sizing:** Fixed risk budget of $0.25\%$ portfolio equity per event (`research-proposed`).

## Required data

- **L3 / Tick-Level Event Stream:** Millisecond-stamped event feed with Order ID, event type (`NEW`, `MODIFY`, `CANCEL`, `TRADE`), side (`BID`/`ASK`), price, and quantity.
- **Venue / Asset in Source:** Indian National Stock Exchange (NSE) BANKNIFTY index futures.
- **Top-of-Book Snapshots:** Top-5 price levels and standing volumes, updated on every tick that modifies top-5 book depth.
- **Trade Aggressor Tags:** Explicit trade prints with buyer/seller initiator flags (or tick-rule signing data).
- **Point-in-Time Availability:** Windows are strictly backward-looking $(\tau - 10\text{s}, \tau]$. Orders are filtered in real-time as modification timestamps arrive. No future information is utilized.
- **Crypto-Specific Data Equivalent:** Requires exchange Level 3 (order-by-order) feeds (e.g. Coinbase Prime FIX / ITCH) or centralized exchange Level 2 depth diffs paired with raw trade execution tick feeds.

## Execution assumptions

- **Source-Reported Settings:**
  - Evaluation window $h = 10\text{ seconds}$, anchored every $15\text{ seconds}$.
  - Forecast window $\xi = 1\text{ second}$.
  - Market session: Main trading hours 09:20–15:25 IST.
  - Zero transaction cost or fee subtraction is applied in the source paper; the paper evaluates diagnostic informational content rather than net trading PnL.
- **Research-Proposed Operational Settings:**
  - **Order Type:** Aggressive Immediate-or-Cancel (IOC) taker market orders to capture the 1–2 second return window (`research-proposed`).
  - **Fee Model:** Crypto perpetual exchange taker fee tier of $2.0\text{ bps}$ ($0.02\%$) or traditional equity index futures exchange fee of $0.5\text{ bps}$ (`research-proposed`).
  - **Slippage Model:** 0.5 minimum price tick ($0.5\text{ tick}$) crossing half-spread (`research-proposed`).
  - **Signal-to-Order Latency:** Modeled at $10\text{ ms}$ for co-located execution or $50\text{ ms}$ for cloud execution (`research-proposed`).

## Evidence

### Source-reported

All numerical findings below are directly reported by Aditya Nittur Anantha, Shashi Jain, and Prithwish Maiti in arXiv:2507.22712v1 (Section 6, Section 6.1, Section 6.2, and Section 6.3):
- **Dataset Sample:** Tick-by-tick NSE BANKNIFTY index futures across three distinct trading days: January 2, January 13, and January 23, 2021.
- **Linear Pearson Correlation ($\mathcal{S}^\rho$):**
  - Unfiltered OBI (UF): $0.01018$
  - Modification-Time Filter (MTF): $0.01133$ (**+11.3% improvement** over unfiltered baseline)
  - Lifetime Filter (LF): $0.01011$ (near parity with unfiltered)
  - Modification-Count Filter (MF): $0.00826$ (**-18.9% degradation**)
- **Discretized Regime Scoring (Cross-Correlation Error):**
  - Unfiltered OBI (UF): $-4.00$
  - Modification-Time Filter (MTF): $-3.39$ (**strongest error reduction**, improving regime alignment)
  - Lifetime Filter (LF): $-3.41$
  - Modification-Count Filter (MF): $-4.44$ (worsened regime alignment)
- **Discretized Regime Scoring ($R^2$):**
  - Unfiltered OBI (UF): $8.43$
  - Lifetime Filter (LF): $8.39$
  - Modification-Count Filter (MF): $8.42$
  - Modification-Time Filter (MTF): $8.37$
  - Finding: Explanatory power under $R^2$ is flat across all filtration schemes, indicating no material gain in linear variance explanation.
- **Hawkes Excitation Norm Score ($\mathcal{S}^\phi$ - Standard Book OBI):**
  - Unfiltered OBI (UF): $8.9292$
  - Modification-Time Filter (MTF): $9.1745$ (modest gain of $+2.7\%$)
  - Modification-Count Filter (MF): $9.0048$
  - Lifetime Filter (LF): $8.9287$
  - Finding: Book-derived OBI shows weak cross-excitation to returns ($\Phi_{OBI \to Ret}$); internal self-excitation ($\Phi_{OBI \to OBI}$ and $\Phi_{Ret \to Ret}$) strongly dominates.
- **Trade-Based OBI ($OBI^{(T)}$) Hawkes Excitation Results:**
  - On the high-activity trading day (January 23, 2021), the Hawkes excitation norm for trade-based OBI under Modification-Time Filtering (MTF) surges to **$24.7352$**, compared to **$9.6726$** for standard book OBI on the same day (**+155.7% increase**).
  - On January 13, 2021, the excitation norm under Lifetime Filtering (LF) reaches **$15.8630$**.
  - Finding: Deriving OBI from executed trades rather than book volume unlocks strong, identifiable causal excitation to subsequent returns, which is substantially magnified under structural filtration.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Modification-Count Filter Degradation:** Restricting orders by modification count ($M_j \le \bar{M}$) consistently degrades performance (Pearson correlation falls from $0.01018$ to $0.00826$; regime error worsens from $-4.00$ to $-4.44$). This provides clear negative evidence that simply penalizing active orders strips out informative market-making adjustments along with noise.
- **Absence of Causal Power in Book OBI:** For standard limit order book imbalance, filtration fails to create substantial causal excitation to returns (norm rises only from $8.9292$ to $9.1745$). Cross-excitation is drowned out by self-excitation, confirming that book imbalance behaves primarily as an endogenous feedback loop rather than an exogenous return driver.
- **Flat Regime $R^2$:** Across all filters, autoregression-adjusted $R^2$ remains unchanged ($8.37$ to $8.43$), demonstrating that structural filtering does not improve simple linear regime predictability.

## Falsification plan

1. **Trade vs. Book Hawkes Cross-Excitation Dominance Test:**
   - Fit 13-dimensional Hawkes processes to trade-based OBI ($OBI^{(T)}$) versus book OBI ($OBI^{(f)}$) across 10 out-of-sample trading days.
   - *Research-defined falsification threshold:* If the cross-excitation norm $\mathcal{S}^\phi(OBI^{(T)})$ fails to exceed $\mathcal{S}^\phi(OBI^{(f)})$ by at least $30\%$ ($\text{Ratio} < 1.30$), the thesis that executed trades possess superior causal transmission over book depth is falsified.
2. **Order ID Scrambling Placebo Test:**
   - Permute Order IDs randomly across events prior to applying the modification-time filter ($\bar{\mathcal{M}} = 100\text{ ms}$).
   - *Research-defined falsification threshold:* If the scrambled-OID stream produces a Pearson correlation within $5\%$ of the true MTF correlation ($0.01133$), the hypothesis that structural filtration captures real order-level intent rather than random sampling is falsified.
3. **Transaction Fee and Slippage Hurdle:**
   - Backtest the `research-proposed` operational strategy under realistic taker exchange fees ($2.0\text{ bps}$) and $0.5\text{ tick}$ slippage.
   - *Research-defined falsification threshold:* If gross return per trade is less than $3.5\text{ bps}$ (yielding negative net PnL after friction), the operational trading viability is falsified.
4. **Sub-Second Execution Latency Degradation Test:**
   - Introduce synthetic execution delays $\tau_{delay} \in \{10\text{ ms}, 50\text{ ms}, 100\text{ ms}, 250\text{ ms}, 500\text{ ms}\}$.
   - *Research-defined falsification threshold:* If net Sharpe ratio drops below $0.0$ at a delay of $\tau_{delay} \le 50\text{ ms}$, the strategy is falsified for non-co-located retail and institutional environments.

## Crypto portability

**adapted / unproven**

- **Traditional Asset Origin:** The primary source derives all empirical findings exclusively from Indian equity index futures (BANKNIFTY on the NSE). It does not analyze cryptocurrency markets.
- **Applicability to Crypto:**
  - Suitable for institutional market makers or proprietary trading desks on centralized crypto exchanges (Binance, Bybit, OKX, Coinbase) with direct access to private WebSocket order feeds or raw ITCH/FIX streams.
  - Useful for designing high-frequency toxicity filters on decentralized liquidity pools and RFQ networks (e.g. Paradigm).
- **Portability Obstacles and Friction:**
  - **Lack of Level 3 Order IDs:** Most retail CEX APIs (Binance, Bybit) provide only Level 2 aggregated depth snapshots and deltas, which do not expose discrete Order IDs. Implementing lifetime or modification-time filtering requires either institutional Level 3 feeds (e.g. Coinbase Prime) or synthetic heuristic queue tracking.
  - **24/7 Continuous Trading:** Crypto markets do not have daily opening/closing auctions or fixed 6-hour sessions. Parameters must adapt continuously to diurnal liquidity cycles.
  - **Venue Fragmentation & Latency Arbitrage:** Crypto price discovery is fragmented across multiple global venues. An imbalance on one exchange may be immediately sniped by cross-venue latency arbitrageurs reacting to another exchange's trade, reducing the holding window from $1\text{ s}$ to microseconds.
  - **Fee Hurdle:** Crypto taker fees ($2$ to $4\text{ bps}$) are significantly higher than the gross return of typical sub-second high-frequency book imbalances, requiring maker-only execution or extreme threshold filtering.

## Limitations

- **Small Sample Period:** Empirical findings are based on three trading days in January 2021. Long-term stability across differing macro volatility regimes (e.g. 2022–2025 bear/bull markets) is unverified.
- **Underspecified PnL Strategy in Source:** The primary paper is an econometric market microstructure study of signal quality and Hawkes dynamics. It does not specify concrete entry/exit thresholds, sizing, stops, or transaction costs; these rules are necessarily `research-proposed`.
- **Infrastructure Overhead:** Computing per-order modification intervals and maintaining reconstructed filtered books requires sub-millisecond event processing infrastructure.
- **Not Independently Reproduced:** Empirical results rely strictly on the primary authors' published statistics.

## Implementation status

`not-implemented`

No code or strategy pipeline has been implemented in our research stack (`nautilus-quant-system`, PyBroker, or NautilusTrader). This record serves strictly as an upstream research capture.

## Adoption boundary

`research-only` | `adoption: not-approved` | `approval_scope: research-only`

This research capture does not constitute trading authorization, does not establish a verified production alpha, and does not approve implementation for paper, testnet, or live trading.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted from this GitHub-only Scout run.

## Sources

- **Primary Source:** Aditya Nittur Anantha, Shashi Jain, and Prithwish Maiti, *"Order-Flow Filtration and Directional Association with Short-Horizon Returns"*, arXiv preprint `arXiv:2507.22712v1 [q-fin.TR]`, submitted July 2025.
  - Canonical URL: https://arxiv.org/abs/2507.22712
  - Full Text HTML: https://arxiv.org/html/2507.22712v1
  - DOI: https://doi.org/10.48550/arXiv.2507.22712
- **Related Prior Literature Cited in Primary Source:**
  - Michael Hanke and Markus Weigerding (2015), *"Order flow imbalance effects on the german stock market"*, *Business Research*, 8(2):213–238.
  - Petter N. Kolm, Jorge Turiel, and Nicholas Westray (2023), *"Deep order flow imbalance: Extracting alpha at multiple horizons from the limit order book"*, *Mathematical Finance*, 33(4):1044–1081.
  - Rama Cont, Arseniy Kukanov, and Sasha Stoikov (2014), *"The price impact of order book events"*, *Journal of Financial Econometrics*, 12(1):47–88.
  - Joel Hasbrouck and Gideon Saar (2013), *"Low-latency trading"*, *Journal of Financial Markets*, 16(4):646–679.
  - A. Nittur Anantha and S. Jain (2025), *"Forecasting high frequency order flow imbalance using hawkes processes"*, *Computational Economics*.
  - Alan G. Hawkes (1971), *"Spectra of some self-exciting and mutually exciting point processes"*, *Biometrika*, 58(1):83–90.
