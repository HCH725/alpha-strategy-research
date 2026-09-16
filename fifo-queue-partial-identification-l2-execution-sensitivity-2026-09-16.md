---
schema: strategy-research-record-v1
title: "FIFO Queue Partial Identification and Passive Execution Sensitivity in Aggregate Order Books (Danait, Zamora, & Boier 2026)"
created: 2026-09-16
updated: 2026-09-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - market-microstructure
  - order-book
  - fifo-queue
  - level-2-data
  - partial-identification
  - passive-execution
  - implementation-shortfall
  - jax-lob
  - falsification
status: research-only
confidence: medium
source_as_of: 2026-09-11
sources:
  - "Riya Danait, Yuliana Zamora, and Ioana Boier, 'Same Book, Different Fills: Partial Identification of FIFO Execution from Aggregate Order Books', arXiv:2609.13597v1 [q-fin.TR, cs.AI], September 11, 2026. https://arxiv.org/abs/2609.13597"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FIFO Queue Partial Identification and Passive Execution Sensitivity in Aggregate Order Books (Danait, Zamora, & Boier 2026)

## Provenance

- **Primary Source:**
  - Authors: Riya Danait (Mathematical Institute, University of Oxford, UK), Yuliana Zamora (NVIDIA Corporation, USA), Ioana Boier (NVIDIA Corporation, USA).
  - Title: *Same Book, Different Fills: Partial Identification of FIFO Execution from Aggregate Order Books*
  - Publication: arXiv preprint `arXiv:2609.13597v1 [q-fin.TR, cs.AI]`, submitted September 11, 2026.
  - Stable arXiv URL: https://arxiv.org/abs/2609.13597
  - Full-text HTML: https://arxiv.org/html/2609.13597v1
  - Full-text PDF: https://arxiv.org/pdf/2609.13597v1
  - Canonical DOI: [10.48550/arXiv.2609.13597](https://doi.org/10.48550/arXiv.2609.13597)
  - Research Sponsorship: Riya Danait supported by Qube Research & Technologies (QRT) through EPSRC Grant EP/S023925/1; research completed during an internship at NVIDIA (`source-reported`).
- **Data & Experimental Infrastructure:**
  - Primary Venue: Tokyo Stock Exchange (TSE).
  - Primary Feeds: London Stock Exchange Group (LSEG) Tick History Level-2 (10-level snapshots) and Level-1 (trades) data covering January 6 through July 25, 2025 (7 months) (`source-reported`).
  - Compute Platform: Single compute node with 8 CPU cores and 4 NVIDIA GB200 GPUs (`source-reported`).
  - Matching Engine Verifier: JAX-LOB GPU-accelerated limit order book matching engine executed within an NVIDIA PyTorch 25.01 NGC container (`source-reported`).
- **Repository Deduplication Audit:**
  - Audited all existing `.md` strategy records in `alpha-strategy-research`. Zero prior records cite `arXiv:2609.13597`, Riya Danait, Yuliana Zamora, or Ioana Boier.
  - Related execution and microstructure records in the repository:
    - `binance-perpetual-dollar-bar-monotonic-lightgbm-queue-fill-falsification-2026-09-13.md` (empirically demonstrates passive maker fill rate collapse under top-of-book tick queue tracking on Binance crypto perps).
    - `china-ashare-l3-eaten-order-age-imbalance-execution-timing-falsification-2026-09-13.md` (investigates Level-3 eaten order queue age on China A-shares).
    - `order-flow-imbalance-predictive-decoupling-cost-falsification-2026-09-12.md` (examines predictive decoupling of OFI under realistic transaction costs).
    - `deep-rl-market-making-regime-switching-bocpd-scenario-bandit-2026-09-11.md` (Moret & Lillo 2026: deep RL market making under regime-switching order flow).
  - Distinctiveness: Unlike prior records that evaluate directional signals or assume a fixed queue simulator, this work introduces the first mathematically proven conditional partial-identification framework for Level-2 order books. Holding the exact aggregate book path, reconciled trades, and additions fixed, it isolates the unobserved within-queue cancellation placement (Front vs. Random vs. Back) and rigorously quantifies how queue ambiguity alone shifts passive fill rates, implementation shortfall, and optimal policy selection on TSE equities.

## Economic mechanism

### Source-reported

1. **Price–Time Priority (FIFO) Value and Aggregate L2 Information Loss:**
   - Under price-time priority matching rules, orders placed earlier at a price level hold strictly superior economic value because they must be filled before subsequent orders (`source-reported`).
   - Standard Level-2 (L2) market data report aggregate quantity at each price rank but omit individual order IDs, arrival sequence, and the specific order targeted by a subsequent cancellation (`source-reported`).
   - Consequently, when an aggregate cancellation occurs, L2 data cannot distinguish whether the canceled volume was located ahead of a resting passive order (accelerating its fill) or behind it (leaving its fill probability unchanged) (`source-reported`).
2. **Conditional Partial Identification of Order-Level Histories:**
   - Instead of adopting an arbitrary cancellation convention (e.g., front, back, or uniform) and treating resulting backtest metrics as ground truth, the recovery of Market-by-Order (MBO) histories from aggregate L2 snapshots is formulated as a conditional partial-identification problem (`source-reported`).
   - Given an observed aggregate path $A_b = \{(t_k, Q_k, T_k, Z_k)\}_{k=0}^{K_b}$, multiple distinct order-level realizations $R \in \mathcal{R}(A_b)$ reproduce the identical aggregate depth and trade history (`source-reported`).
   - A controlled compiler class $\mathcal{G} = \{\text{front}, \text{random}, \text{back}\}$ is defined, holding timestamps, prices, reconciled market removals, partition seeds, and additions identical while varying only the placement of residual within-queue cancellations (`source-reported`).
3. **Analytical Fill Ordering for Passive Markers (Proposition 3.1):**
   - For a virtual tagged passive limit order joining the best quote during an unchanged touch-price spell, Proposition 3.1 establishes that cumulative fills strictly obey:
     $$F_{\text{front}}(t) \ge F_{\text{random}}(t) \ge F_{\text{back}}(t)$$
     for every timestamp $t$ before the touch price changes (`source-reported`).
4. **Execution Policy Sensitivity and Misallocation Risk:**
   - Algorithmic execution policies (Passive-at-Touch vs. TWAP Hybrid vs. Aggressive immediate execution) produce divergent implementation shortfall outcomes across compatible FIFO queue realizations (`source-reported`).
   - If an algorithmic trading system selects its execution policy based on an unverified queue convention, it faces material regret (added cost) when market reality deviates from that convention (`source-reported`).

### Research interpretation

- **Microstructure Identification Boundary:**
  - Backtests of market-making, stat-arb, or directional alpha strategies that rely on passive limit orders to avoid taker fees are fundamentally unidentifiable on L2 data alone.
  - Assuming that a limit order fills as soon as cumulative trading volume equals pre-existing queue depth implicitly assumes a favorable front-of-queue cancellation allocation, artificially boosting backtest Sharpe ratios and underestimating execution friction.
- **Friction-Driven Strategy Inversion:**
  - In liquid instruments with tight spreads, queue position uncertainty alters the tradeoff between earning the spread and incurring terminal adverse selection.
  - In less active instruments with wider tick sizes, failing to fill passively forces aggressive liquidity crossing at the horizon, converting an apparent passive execution edge into an severe execution loss.

## Signal

### Signal Formation and Timeline
- **Observation Frequency:** Continuous limit order book snapshots and trade prints during TSE continuous trading sessions (`source-reported`).
- **Data Availability Lag:** L2 snapshots and L1 trades causally synchronized via exchange matching-engine timestamp; capture lag diagnostic verified with 99th percentile $< 20$ ms (`source-reported`).
- **Evaluation Horizons:** 300-second ($5$-minute) non-overlapping execution episodes (`source-reported`).
- **Tagged Probe Frequency:** Virtual $100$-share probe placed every $5$ seconds with a $15$-second maximum horizon (`source-reported`).

### Policy Logic and Order Routing
The source evaluates three deterministic price-taking execution policies:
1. **Aggressive Benchmark ($\pi_{\text{agg}}$):**
   - Immediate execution at episode start against a copy of the contemporaneous order book using aggressive market orders (`source-reported`).
   - Outcome is invariant across all FIFO queue realizations because it only queries displayed aggregate depth (`source-reported`).
2. **TWAP Hybrid ($\pi_{\text{hyb}}$):**
   - Tracks a cumulative schedule target across $10$ equally spaced checkpoints ($30$-second intervals over the $300$-second episode) (`source-reported`).
   - Targets are rounded half-up to $100$-share lots (`source-reported`).
   - Places passive limit orders at the same-side best quote; crosses any accumulated schedule deficit aggressively at each checkpoint (`source-reported`).
3. **Passive-at-Touch ($\pi_{\text{pas}}$):**
   - Places a passive limit order at the same-side best quote using a virtual queue marker (`source-reported`).
   - Retains marker priority while the price remains the best quote (`source-reported`).
   - When the best quote changes, cancels the marker and rejoins at the new best quote (`source-reported`).
   - At terminal horizon $T = 300$ seconds, any remaining unfilled inventory $q_T > 0$ is crossed aggressively against a copy of the terminal book at VWAP price $P_T$ (`source-reported`).

### Queue Compilation and Virtual Fill Rules
- **Reconciliation Equations:**
  - Observed quantity transition: $Q_{s,p,k} - Q_{s,p,k-1} = L_{s,p,k} - D_{s,p,k} - M_{s,p,k}$ (`source-reported`).
  - Residual cancellation: $D_{s,p,k} = [- (Q_{s,p,k} - Q_{s,p,k-1} + M_{s,p,k})]_+$ (`source-reported`).
  - Residual addition: $L_{s,p,k} = [Q_{s,p,k} - Q_{s,p,k-1} + M_{s,p,k}]_+$ (`source-reported`).
  - Reconstructed event processing sequence: Reconciled market removals ($M$), then residual cancellations ($D$), then residual additions ($L$) (`source-reported`).
- **Cancellation Rules:**
  - `front`: Removes the oldest eligible resting background quantity (`source-reported`).
  - `random`: Iteratively samples eligible resting background orders with probability proportional to remaining quantity until $D_{s,p,k}$ is satisfied (`source-reported`).
  - `back`: Removes the newest eligible resting background quantity (`source-reported`).
- **Virtual Fill Mechanics:**
  - Virtual queue marker records remaining order size $x_{g,k^-}$ and background quantity ahead $H_{g,k^-}$ (`source-reported`).
  - Trade execution of size $m_k$ fills: $\Delta F_{g,k} = \min(x_{g,k^-}, [m_k - H_{g,k^-}]_+)$ (`source-reported`).
  - Cumulative fill: $F_g(t) = X - x_g(t)$ (`source-reported`).

### Parameters
- **Episode Duration ($T$):** $300$ seconds (`source-reported`).
- **Checkpoints ($K$):** $10$ checkpoints ($30$-second step) for hybrid policy (`source-reported`).
- **Parent Order Size ($X$):**
  - RIC `1301.T`: $100$ shares ($5\%$ of development-period median positive same-side aggressive volume, rounded to $100$-share lots) (`source-reported`).
  - RIC `7911.T`: $200$ shares ($5\%$ of development-period median positive same-side aggressive volume, rounded to $100$-share lots) (`source-reported`).
- **Tick Sizes:**
  - RIC `1301.T`: $55$ yen minimum tick increment (`source-reported`).
  - RIC `7911.T`: $11$ yen minimum tick increment (`source-reported`).
- **Trading Unit:** $100$ shares for both instruments (`source-reported`).
- **Policy Selection Tolerance:** $10^{-6}$ bps tie-breaking threshold (`source-reported`).

## Required data

- **Universe:**
  - RIC `1301.T` (Kyokuyo Co., Ltd.): TOPIX Small 2 constituent, "Other Issues" tick schedule, lower turnover (`source-reported`).
  - RIC `7911.T` (TOPPAN Holdings Inc.): TOPIX Mid400 / TOPIX500 constituent, TOPIX500 tick schedule, actively traded (`source-reported`).
- **Data Venue & Vendor:**
  - Tokyo Stock Exchange (TSE), LSEG Tick History (`source-reported`).
- **Data Feeds & Fields:**
  - Level-2 (L2): 10 occupied price levels (bid price, bid size, ask price, ask size) with exchange matching-engine timestamp (`source-reported`).
  - Level-1 (L1): Regular trades reporting exchange timestamp, execution price, and share quantity (`source-reported`).
- **Feed Quality & Inclusion Filters:**
  - Instrument must appear in both feeds with complete scans (`source-reported`).
  - $\ge 98\%$ of regular trades fall within L2 coverage with an exact exchange-time match (`source-reported`).
  - Daily 99th-percentile absolute capture lag $< 20$ ms (`source-reported`).
  - $\ge 99\%$ of continuous rows are two-sided and uncrossed, with all 10 ranks present in $\ge 95\%$ of rows (`source-reported`).
- **Chronological Data Partition:**
  - January 6, 2025 – May 31, 2025: $97$ feed-eligible dates for estimation of latent partition inputs and parent scale (`source-reported`).
  - June 1, 2025 – June 30, 2025: $21$ dates for tuning/selection of block, probe, and policy settings (`source-reported`).
  - July 1, 2025 – July 25, 2025: $18$ held-out dates for final out-of-sample evaluation (`source-reported`).
- **Missing Data Handling:**
  - Pre-open, lunch break (11:30–12:30 JST), closing auction, and non-continuous phases strictly excluded (`source-reported`).
  - Replay blocks terminate upon encountering un-reconciled compound updates or session boundaries (`source-reported`).
  - Imputation of liquidity outside the observed 10 price levels is strictly prohibited (`source-reported`).

## Execution assumptions

- **Signal-to-Order Latency:** Zero latency assumed in price-taking shadow evaluations (`source-reported`).
- **Fill Mechanics:** Virtual queue marker tracking resting depth ahead; fills occur strictly via price-time priority from L1-attributed trade removals (`source-reported`).
- **Market Impact:** Zero endogenous price impact assumed; virtual orders do not divert historical executions or alter subsequent L2 transitions (`source-reported`).
- **Terminal Liquidity & Crossing:** Unfilled inventory at $T = 300$s is crossed aggressively against a copied terminal book at VWAP price $P_T$ (`source-reported`). Episodes without sufficient terminal depth are flagged under pre-declared eligibility rules rather than priced via imputation (`source-reported`).
- **Fees & Commissions:** Zero broker commission or exchange transaction fee assumed in the baseline academic evaluation (`source-reported`).
- **Slippage & Spread Accounting:** Explicitly evaluated via implementation shortfall:
  $$\text{IS}(\pi, R) = \sigma \left( \frac{\sum_i q_i P_i + q_T P_T}{X} - P_0 \right) / P_0 \times 10^4 \text{ bps}$$
  where $\sigma = 1$ for buys and $-1$ for sells, and $P_0$ is the arrival midprice (`source-reported`).

## Evidence

### Source-reported

All empirical results below are directly reported by Danait, Zamora, & Boier (arXiv:2609.13597v1, September 2026) across the held-out sample of 18 trading days in July 2025 ($1,080$ distinct 300-second episode windows per instrument, evaluated across two sides and three random seeds = $6,480$ matched episode-side-seed units per instrument):

1. **Aggressive Benchmark Invariance:**
   - RIC `1301.T`: Invariant at $10.010$ bps implementation shortfall across all FIFO cancellation realizations (`source-reported`).
   - RIC `7911.T`: Invariant at $2.400$ bps implementation shortfall across all FIFO cancellation realizations (`source-reported`).
2. **Passive-at-Touch Preterminal Completion Rate:**
   - RIC `1301.T`: Front cancellation raises preterminal completion by $8.01$ percentage points compared to Back cancellation (`source-reported`).
   - RIC `7911.T`: Front cancellation raises preterminal completion by $7.39$ percentage points compared to Back cancellation (`source-reported`).
3. **Implementation Shortfall (IS) Sensitivity (Front minus Back, $\Delta \text{IS}_{\text{front} - \text{back}}$):**
   - RIC `1301.T` (Passive-at-Touch): $-1.010$ bps difference ($95\%$ bootstrap confidence interval: $[-1.253, -0.788]$ bps) (`source-reported`).
   - RIC `1301.T` (TWAP Hybrid): $-0.398$ bps difference (`source-reported`).
   - RIC `7911.T` (Passive-at-Touch): $-0.384$ bps difference ($95\%$ bootstrap confidence interval: $[-0.493, -0.284]$ bps) (`source-reported`).
   - RIC `7911.T` (TWAP Hybrid): $-0.414$ bps difference (`source-reported`).
4. **Policy Choice Switching and Associated Regret:**
   - Date-average shortfall ranking: Passive-at-Touch has lowest cost under all cancellation rules, followed by Hybrid and Aggressive (`source-reported`).
   - RIC `1301.T`: The lowest-cost policy changes in $0.83\%$ to $4.49\%$ of directed cross-rule comparisons (`source-reported`). Conditional on a policy change, the regret (added execution cost) is $14.277$ to $17.354$ bps (`source-reported`).
   - RIC `7911.T`: The lowest-cost policy changes in $3.63\%$ to $14.26\%$ of directed cross-rule comparisons (`source-reported`). Conditional on a policy change, the regret is $2.366$ to $3.723$ bps (`source-reported`).
5. **Tagged-Order Proposition 3.1 Verification:**
   - Evaluated across $3,209$ blocks ($354,774$ matched triplets) for `1301.T` and $21,309$ blocks ($370,992$ matched triplets) for `7911.T` (`source-reported`).
   - $100\%$ of matched triplets satisfy Proposition 3.1: $F_{\text{front}}(t) \ge F_{\text{random}}(t) \ge F_{\text{back}}(t)$ (`source-reported`).
6. **Independent JAX-LOB Replay Verification:**
   - Replayed $648$ reconstructed streams ($54$ background paths) for `1301.T` ($232,800$ shares) and $456$ streams ($38$ paths) for `7911.T` ($4,119,600$ shares) through the JAX GPU matching engine (`source-reported`).
   - $100\%$ of requested market-message quantities executed without immediate trade triggers on adds or sentinel price artifacts (`source-reported`).
7. **Robustness & Strict Block Checks:**
   - Deterministic 100-share partition chunks leave primary front-minus-back estimates unchanged for both instruments (`source-reported`).
   - Strict replay-block analysis yields front-minus-back passive shortfall difference of $-0.397$ bps (95% CI: $[-0.576, -0.229]$) for `1301.T`, and $-0.325$ bps (95% CI: $[-0.649, 0.000]$) for `7911.T` (`source-reported`).

### Independently reproduced

`not independently reproduced`.

### Negative evidence

- **Falsification of Deterministic L2 Backtest Realism:**
  - Demonstrates that evaluating passive execution strategies on Level-2 order book snapshots without testing across compatible FIFO cancellation realizations produces spurious precision.
  - Naive L2 backtests overstate passive fill rates by $7.4$ to $8.0$ percentage points and underestimate execution shortfall by $0.38$ to $1.01$ bps compared to worst-case back-of-queue cancellation allocation.
  - In less active instruments (`1301.T`), misidentifying queue position alters optimal policy selection and exposes the execution engine to severe conditional regret exceeding $14$ to $17$ bps.

## Falsification plan

- **Cross-Market Replication:** Replay Level-2 order books across US equities (Nasdaq/NYSE) and European equities (Euronext/LSE) to test whether FIFO sensitivity envelopes scale inversely with tick-to-price ratio and order flow turnover (`research-proposed`).
- **Crypto Order Book Falsification:** Construct matched Front, Random, and Back queue compilers on high-frequency crypto perpetual order book snapshots (e.g. Binance or Hyperliquid top-of-book depth) (`research-proposed`).
- **Research-Defined Falsification Thresholds:**
  - *Envelope Insignificance Cutoff:* If the implementation shortfall sensitivity envelope width $|\text{IS}_{\text{front}} - \text{IS}_{\text{back}}| < 0.05$ bps across $\ge 90\%$ of continuous execution episodes, the hypothesis that L2 queue ambiguity induces material economic distortion is falsified (`research-defined falsification threshold`).
  - *Policy Invariance Cutoff:* If the optimal execution policy choice switches in $< 0.1\%$ of episodes across varying liquidity tiers, queue ambiguity is considered economically negligible for high-level policy routing (`research-defined falsification threshold`).

## Crypto portability

- **Portability Status:** `adapted/unproven`.
- **Mechanism Origin:** The paper's empirical evidence is derived exclusively from Tokyo Stock Exchange (TSE) cash equities. Porting the framework to cryptocurrency markets represents a research adaptation.
- **Crypto-Specific Market Microstructure Differences:**
  1. **Feed Aggregation & Granularity:** Major crypto exchanges (Binance, OKX, Bybit) distribute aggregated Level-2 order book feeds (e.g., $100$ms diff snapshots or top-20 levels) rather than raw Market-by-Order (MBO/L3) feeds. The partial-identification problem is therefore structurally pervasive across centralized crypto exchanges.
  2. **High Cancellation Ratios:** Centralized crypto perpetual markets experience order cancellation rates exceeding $90\%$, driven by HFT quoting and inventory rebalancing. The sensitivity of a resting order to whether cancellations remove volume from the front versus the back of the queue is significantly heightened compared to traditional equities.
  3. **Maker Fee Rebates vs. Taker Penalties:** Crypto perpetual exchanges charge significant taker fees (typically $2$ to $5$ bps) while providing maker rebates (typically $-0.5$ to $+1$ bps). When a passive limit order fails to execute due to unfavorable queue positioning, the required terminal crossing incurs a severe fee cliff ($4$ to $6$ bps spread-plus-fee penalty), making FIFO sensitivity envelopes a primary determinant of strategy net PnL.
  4. **24/7 Continuous Trading:** Eliminates opening/closing auction boundary splits, but introduces recurrent 8-hour funding rate settlement spikes where order book depth temporarily collapses.

## Limitations

- **Instrument Scope:** Primary empirical evidence is limited to two Tokyo Stock Exchange equities (`1301.T` and `7911.T`) over $18$ held-out trading days in July 2025 ($36$ instrument-day observations) (`source-reported`).
- **Proprietary Data Dependency:** Requires synchronized Level-2 order book snapshots and Level-1 trade feeds (sourced from LSEG Tick History); cannot be verified using standard bar-level OHLCV data (`source-reported`).
- **Price-Taking Shadow Assumption:** Shadow policies assume zero endogenous market impact and zero latency, evaluating fills against unperturbed historical background book transitions (`source-reported`).
- **Single-Spell Endpoint Bounds:** Analytical fill ordering (Proposition 3.1) is mathematically proven only for a single virtual marker during an unchanged touch-price spell; Front and Back are conditional compiler conventions and do not represent sharp bounds over all conceivable order-level queue configurations (`source-reported`).

## Implementation status

`not-implemented`.

## Adoption boundary

- Status: `research-only`.
- Adoption: `not-approved`.
- Scope: `research-only`.
- This record captures external market microstructure and execution research for upstream knowledge intake. It does not authorize strategy implementation in NautilusTrader, PyBroker, Paper, Testnet, or Live trading environments.

## Related Wiki records

- `[[quant/binance-perpetual-dollar-bar-monotonic-lightgbm-queue-fill-falsification-2026-09-13]]` — Empirical queue simulation and maker fill rate collapse on crypto perpetuals.
- `[[quant/china-ashare-l3-eaten-order-age-imbalance-execution-timing-falsification-2026-09-13]]` — Level-3 order queue age imbalance and execution timing.
- `[[quant/order-flow-imbalance-predictive-decoupling-cost-falsification-2026-09-12]]` — Order flow imbalance predictive decay under execution friction.
- `[[quant/sp500-avellaneda-lee-residual-reversion-implementability-falsification-2026-09-13]]` — Execution friction falsification in statistical arbitrage.
- `[[quant/deep-rl-market-making-regime-switching-bocpd-scenario-bandit-2026-09-11]]` — Reinforcement learning market making under regime-switching order flow.

## Sources

- Riya Danait, Yuliana Zamora, and Ioana Boier, *"Same Book, Different Fills: Partial Identification of FIFO Execution from Aggregate Order Books"*, arXiv preprint `arXiv:2609.13597v1 [q-fin.TR, cs.AI]`, submitted September 11, 2026.
  - Stable arXiv URL: https://arxiv.org/abs/2609.13597
  - Full-text HTML: https://arxiv.org/html/2609.13597v1
  - Full-text PDF: https://arxiv.org/pdf/2609.13597v1
  - Canonical DOI: [10.48550/arXiv.2609.13597](https://doi.org/10.48550/arXiv.2609.13597)
  - Key Citations:
    - Frey, S. Y., Li, K., Nagy, P., Sapora, S., Lu, C., Zohren, S., Foerster, J. N., & Calinescu, A. (2023). *JAX-LOB: a GPU-accelerated limit order book simulator to unlock large scale reinforcement learning for trading*. In Proceedings of the Fourth ACM International Conference on AI in Finance (pp. 583–591). DOI: [10.1145/3604237.3626880](https://doi.org/10.1145/3604237.3626880).
    - Manski, C. F. (2003). *Partial identification of probability distributions*. Springer, New York. DOI: [10.1007/b97478](https://doi.org/10.1007/b97478).
    - Manski, C. F. (2007). *Identification for prediction and decision*. Harvard University Press. ISBN: 9780674026537.
    - Perold, A. F. (1988). *The implementation shortfall: paper versus reality*. The Journal of Portfolio Management, 14(3), 4–9. DOI: [10.3905/jpm.1988.409150](https://doi.org/10.3905/jpm.1988.409150).
    - Almgren, R., & Chriss, N. (2001). *Optimal execution of portfolio transactions*. The Journal of Risk, 3(2), 5–39. DOI: [10.21314/JOR.2001.041](https://doi.org/10.21314/JOR.2001.041).
