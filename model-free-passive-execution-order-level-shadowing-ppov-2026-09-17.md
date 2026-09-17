---
schema: strategy-research-record-v1
title: "Model-Free Passive Execution via Order-Level Shadowing (Shadow-PPOV)"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - optimal-execution
  - passive-execution
  - percentage-of-volume
  - market-microstructure
  - limit-order-book
  - cancel-mirroring
  - model-free-benchmark
status: research-only
confidence: medium
source_as_of: 2026-09-16
sources:
  - "Vincent Maciejewski, 'Model-Free Passive Execution via Order-Level Shadowing', arXiv:2609.18019v1 [q-fin.TR], September 16, 2026. https://arxiv.org/abs/2609.18019"
  - "Vincent Mayeski / M2 Technologies, 'kaspar-hft', GitHub repository commit 77a1f9d5ec1eb317cf909e2275c6eb4742ce2eae, September 2026. https://github.com/vincent212/kaspar-hft"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Model-Free Passive Execution via Order-Level Shadowing (Shadow-PPOV)

## Provenance

- **Primary Source:** Vincent Maciejewski (M2 Technologies / 16425640 Canada Inc., `mayeski@gmail.com`), *"Model-Free Passive Execution via Order-Level Shadowing"*, arXiv preprint `arXiv:2609.18019v1 [q-fin.TR]`, submitted September 16, 2026.
- **Canonical Identifier / Stable URL:** https://arxiv.org/abs/2609.18019
- **Canonical DOI:** [10.48550/arXiv.2609.18019](https://doi.org/10.48550/arXiv.2609.18019)
- **Full-Text HTML Source:** https://arxiv.org/html/2609.18019v1
- **Full-Text PDF Source:** https://arxiv.org/pdf/2609.18019v1
- **Reference Implementation / Codebase:** Public open-source C++ system `vincent212/kaspar-hft` at immutable commit SHA `77a1f9d5ec1eb317cf909e2275c6eb4742ce2eae` (MIT License). Exact documentation files audited: `STRATEGY_SIMULATOR_GUIDE.md`, `ACTORS_INVENTORY.md`, `FILE_STRUCTURE.md`.
- **Source Verification:** The primary preprint full-text HTML, analytical derivations, Algorithm 1, Tables 1–7, Figures 1–6, and the reference GitHub implementation were directly retrieved and audited. All equations, parameters, empirical slippage tables, and latency degradation figures cited in this record trace directly to Sections 1–12 and Tables 1–7 of `arXiv:2609.18019v1`.
- **Repository Deduplication Audit:** Pre-write search across all records in `alpha-strategy-research` confirmed zero existing records citing `arXiv:2609.18019`, Vincent Maciejewski, `kaspar-hft`, `Shadow-PPOV`, or `cancel mirroring`. Adjacent optimal execution captures (`passive-market-impact-optimal-execution-mlofi-2026-09-02.md`, `stochastic-tracking-optimal-execution-obizhaeva-wang-regularization-2026-09-02.md`, `signature-optimal-execution-statistical-arbitrage-quadratic-reduction-2026-09-02.md`) investigate ML-driven order-flow imbalance kernels, transient impact Obizhaeva-Wang tracking, or path signatures; none formulate model-free order-level shadowing or identifier-keyed lifecycle mirroring.

## Economic mechanism

### Source-reported

Conventional automated execution algorithms are divided into schedule-based (TWAP, VWAP, POV, Implementation Shortfall) and liquidity-seeking families. All existing schedule-based methods are **model-based**: each derives child order decisions from an explicit model, volume forecast, schedule, or control rule. Placing passive limit orders efficiently conventionally requires an order-book model, fill-probability prediction, and queue-position valuation to balance fill probability against adverse selection (Glosten & Milgrom 1985; Moallemi & Yuan 2016). Posting blindly at the touch courts adverse selection, filling when the level thins ahead of an adverse price move.

Shadow-PPOV introduces **model-free passive execution via order-level shadowing**:
1. **Model-free placement:** A resting limit order represents an external participant's conclusion that a price is worth standing at. On observing a third-party `add` on an order-by-order (MBO) feed, Shadow-PPOV transmits its own limit order at the exact price and venue of that add, joining behind the followed order in the price-time-priority (FIFO) queue. A market sweep must consume the followed participant order and any pre-existing depth before reaching the shadow.
2. **Identifier-driven cancel mirroring:** State-dependent cancellation (continuously evaluating book depth, spread, or queue decay) is eliminated. Instead, Shadow-PPOV stores a single mapping from the followed order's venue-scoped exchange identifier to its own shadow identifier:
   - If the followed order is pulled (`delete`), the liquidity has fled without aggression; remaining exposed would be pure adverse selection, so Shadow-PPOV cancels the shadow immediately and removes the association.
   - If the followed order is hit (`trade`), an aggressive market sweep is actively in flight. Cancelling immediately would pull the shadow before the sweep arrives. Shadow-PPOV arms a delayed cancellation for a short **grace window** of $B$ burst events to give the incoming sweep an opportunity to fill the shadow.
   - If the followed order is amended (`modify`), it is treated as lifecycle termination; the shadow is cancelled immediately.
3. **Flow-inherited venue selection:** Transmitting each shadow to the originating venue of the observed add ensures that the execution venue distribution matches the observed resting add distribution in expectation, eliminating smart order routing (SOR) optimization.
4. **Glosten-Milgrom equilibrium constraint:** Because Shadow-PPOV carries no directional forecast, it cannot separate toxic from benign flow. Under the Glosten-Milgrom account of the spread, the half-spread captured by resting is returned in expectation through adverse selection. At zero latency, passive Shadow-PPOV and aggressive POV exhibit identical relative slippage ($+0.0955$ vs $+0.0952$ ticks/contract on ES), demonstrating that a model-free method without directional alpha executes slightly worse than the arrival mid-price and cannot beat it.

### Research interpretation

The proposed economic mechanism is **liquidity-flow tracking with structural queue insulation**:
- By anchoring passive orders strictly to freshly committed participant liquidity, the algorithm avoids posting in stale or desert price levels.
- Resting behind an observable participant order in FIFO queue priority provides transient queue protection against marginal adverse sweeps, while allowing block sweeps to execute the child order.
- The asymmetric response to deletes versus trades exploits the temporal clustering of aggressive marketable bursts: incoming market sweeps often consume multiple orders in a burst, creating a window where resting behind a freshly hit order yields passive fills at the bid/ask without taking on enduring inventory risk.
- Shadow-PPOV serves as an empirical lower bound and benchmark for passive execution: any predictive placement model must beat Shadow-PPOV's baseline slippage on the same parent order, corpus, and participation rate to justify its modeling complexity.

## Signal

The execution strategy operates on message-level order-by-order market data (Algorithm 1):

### 1. State Variables (`source-reported`)
- Association mapping $M: k \mapsto \text{shadow\_id}$ with venue-scoped key $k = (\text{venue}, \text{ex\_id})$.
- Target side $\sigma \in \{\text{buy}, \text{sell}\}$.
- Order-placement rate $\rho \in (0, 1]$ (probabilistic coin flip per qualifying add) or deterministic every-$N$-th add.
- Grace window parameter $B \in \mathbb{N}$ (burst count).
- Own identifier set $O = \{(\text{venue}, \text{shadow\_id})\}$.

### 2. Message Processing Logic (Algorithm 1) (`source-reported`)
On receipt of order-book message $m$ with type $m.\tau \in \{\text{add}, \text{delete}, \text{trade}, \text{modify}\}$, exchange order identifier $m.\text{id}$, venue $m.v$, side $m.s$, and price $m.p$, let key $k = (m.v, m.\text{id})$:

```text
switch m.τ do:
  case add:
    if k ∈ O or m.s ≠ σ then return              // ignore own orders and opposite side
    if selection criterion not met then return    // probabilistic coin-flip with probability ρ
    shadow_id ← transmit limit order at price m.p to venue m.v
    O ← O ∪ {(m.v, shadow_id)}
    M[k] ← shadow_id

  case delete:                                    // followed order pulled
    if k ∈ M then:
      cancel M[k] immediately
      remove k from M

  case trade:                                     // followed order hit by marketable sweep
    if k ∈ M and not already armed then:
      arm delayed cancel of M[k] in B burst events // grace window for sweep to reach shadow

  case modify:                                    // followed order amended
    if k ∈ M then:
      cancel M[k] immediately
      remove k from M
```

- **Grace-window expiry or safety guard:** Triggers immediate cancellation of armed shadow (`source-reported`).
- **Own fill event:** Removes association from $M$ and clears shadow from $O$ (`source-reported`).
- **Parent order completion:** Cancels all outstanding shadows in $M$ and clears $M$ (`source-reported`).

### 3. State-Based Safety Guards in Reference Implementation (`source-reported`)
While the core placement and cancellation logic is model-free, the reference implementation in `kaspar-hft` layers operational safety guards:
1. **Two-band place/cancel hysteresis:**
   - A shadow is placed only when its price is within a tight placement band $\delta_{\text{place}}$ ticks of the inside (e.g. for a buy, $p \ge b_0 - \delta_{\text{place}}$ against best bid $b_0$).
   - A resting shadow is cancelled for distance only when the market drifts beyond a looser cancel band $\delta_{\text{cancel}}$, with $\delta_{\text{place}} < \delta_{\text{cancel}}$. The gap prevents one-tick book oscillations from causing place/cancel churn.
2. **Completion and over-hedge guards:**
   - Working shadows are pulled immediately when target quantity is reached or position goes flat.
   - Working shadows are pulled if resting size at that level would overshoot remaining unexecuted parent quantity.
3. **Child order size clamping:**
   - Placed child order size is clamped to $\min(\text{per\_level\_cap}, \text{per\_order\_cap}, \text{remaining\_parent\_qty}, \text{followed\_order\_size})$.

### 4. Operational Parameters
- Order placement rate: $\rho = 0.05$ (shadows 5% of qualifying adds) (`source-reported`).
- Grace window burst count: $B = 2$ burst events (`research-proposed`).
- Placement hysteresis band: $\delta_{\text{place}} = 1$ tick (`research-proposed`).
- Cancel hysteresis band: $\delta_{\text{cancel}} = 3$ ticks (`research-proposed`).
- Child order clip ceiling: 1 contract per child, 25-contract aggregate price-level cap (`source-reported`).
- Time-to-live for aggressive benchmark arm: 11 ms (`source-reported`).

## Required data

- **Instrument / Universe:** CME E-mini S&P 500 futures (`ES`), contract multiplier $50 ($12.50 per 0.25 index tick) (`source-reported`).
- **Venue / Market Type:** Chicago Mercantile Exchange (CME Globex), centralized limit order book (CLOB), quarterly outright futures (`source-reported`).
- **Market Data Feed:** CME MDP 3.0 Market-by-Order (MBO) binary feed on channels 310, 318, and 344 (`source-reported` in `STRATEGY_SIMULATOR_GUIDE.md`). Requires full packet captures (PCAP) with nanosecond hardware timestamps.
- **Message Fields Required (`source-reported`):**
  - Message type ($m.\tau \in \{\text{add}, \text{modify}, \text{delete}, \text{trade}\}$).
  - Exchange order identifier ($m.\text{id}$, 64-bit integer, unique per venue).
  - Originating venue ($m.v$).
  - Side ($m.s \in \{\text{buy}, \text{sell}\}$).
  - Price ($m.p$, integer tick format).
  - Order quantity / trade size.
  - End-of-burst flag (to count burst events for grace window).
- **Point-in-Time Availability (`source-reported`):** Real-time, event-by-event processing. Zero look-ahead bias; messages processed strictly in sequence of receipt.
- **Missing-Data & Desynchronization Handling (`research-proposed`):** Any packet gap or channel reset requires dropping all pending state $M$, issuing immediate bulk cancels for all working shadows, and waiting for book reconstitution.

## Execution assumptions

- **Order Types (`source-reported`):** Standard displayed limit orders sent via CME iLink3 binary protocol or simulated order manager.
- **Execution Venue Selection (`source-reported`):** Transmitted directly to the originating venue of the followed add (pass-through).
- **Queue Priority Model (`source-reported`):** Strict price-time priority (FIFO). Shadow joins the queue immediately behind the followed order.
- **Fill Inference (`source-reported`):** A shadow fills when recorded subsequent market executions indicate aggression has penetrated through its position in the queue.
- **Market Impact Assumption (`source-reported`):** Zero endogenous market impact modeled in the baseline replay simulator; orders fill against recorded historical feeds without displacing other participant quotes.
- **Latency Modeling (`source-reported`):** Three independent configurable delay components: inbound market data, outbound order submission, and outbound order cancellation.
- **Transaction Costs & Fees (`research-proposed`):** Primary source reports gross slippage in ticks/contract without deducting exchange or clearing fees. In production live execution, CME member/non-member all-in exchange and clearing fees (~$0.25 to $1.25 per contract round-turn) must be added (`research-proposed`).
- **Margin & Capital Requirements (`research-proposed`):** Standard CME initial margin (~$12,000 to $15,000 per ES contract); unleveraged cash buffer to support 100-contract inventory swing during execution window (`research-proposed`).

## Evidence

### Source-reported

All empirical results below are directly reported by Vincent Maciejewski (`arXiv:2609.18019v1`, Section 8, Tables 1–7, Figures 1–6):

1. **Experimental Setup (Section 8.1):**
   - Corpus: E-mini S&P 500 futures (`ES`), CME channel 310 MBO data, covering all regular trading sessions (09:29 to 16:00 ET) for the entire calendar year 2025.
   - Task: Two-sided execution over rolling 10-minute measurement windows (up to 39 windows per session). In each window, the algorithm is tasked with completing 100 contracts to buy and 100 contracts to sell simultaneously using separate books.
   - ES book characteristics: ES is a 1-tick wide book at 96.3% of window openings, with mean spread of 1.038 ticks ($+0.519$ ticks slippage for immediate execution).

2. **Passive Shadow-PPOV vs. Aggressive POV at Matched Participation (Table 3 / Table 8 in source):**
   - Parameter settings: Passive shadowed rate $\rho = 5\%$ of adds; Aggressive shadowed rate $= 2\%$ of prints.
   - Completed windows: 9,592 (Passive) vs. 9,581 (Aggressive).
   - Realized participation rate: **4.46%** (Passive) vs. **4.86%** (Aggressive).
   - Time to fill 100 contracts: **72.7 seconds** (Passive) vs. **62.4 seconds** (Aggressive).
   - Child executions per leg: **85.5** (Passive) vs. **85.6** (Aggressive), averaging 1.18 contracts per fill.
   - Share filled by crossing (marketable): **1.04%** (Passive) vs. **51.86%** (Aggressive).
   - Relative slippage against arrival mid ($m_0$):
     - **Passive Shadow-PPOV:** $+0.0955 \pm 0.0130$ ticks/contract (Buy leg: $+0.0704 \pm 0.0532$; Sell leg: $+0.1205 \pm 0.0517$).
     - **Aggressive POV:** $+0.0952 \pm 0.0135$ ticks/contract (Buy leg: $+0.0292 \pm 0.0830$; Sell leg: $+0.1613 \pm 0.0836$).
     - *Finding:* Passive and aggressive relative slippage match to the fourth decimal place ($+0.0955$ vs $+0.0952$, under 0.1 tick or $1.19/contract on ES).
   - Cost relative to immediate execution (crossing spread at open):
     - Passive Shadow-PPOV: **$-0.4236 \pm 0.0117$ ticks/contract** (saves $5.30 per contract vs crossing).
     - Aggressive POV: **$-0.4239 \pm 0.0105$ ticks/contract**.
   - Cost relative to working-interval VWAP:
     - Passive Shadow-PPOV: $-0.6208 \pm 0.0204$ ticks/contract.
     - Aggressive POV: $-0.4036 \pm 0.0275$ ticks/contract.
     - *(Caveat: working intervals differ in duration; longer passive interval averages broader session slice).*

3. **Post-Fill Mark-Outs (Table 4 / Table 9 in source):**
   - Evaluated 1s, 5s, and 30s after fill signed as adverse movement against fill:
     - Passive Shadow-PPOV: 1s: $+0.0825 \pm 0.0076$; 5s: $+0.0743 \pm 0.0110$; 30s: $+0.0993 \pm 0.0200$ ticks.
     - Aggressive POV: 1s: $+0.0826 \pm 0.0072$; 5s: $+0.0874 \pm 0.0118$; 30s: $+0.0913 \pm 0.0190$ ticks.
   - *Finding:* Mark-out profile is flat in time between 1s and 30s, reflecting structural adverse selection rather than transient market impact.

4. **Latency Degradation Across Round-Trip Delays (Table 5 / Table 10 in source):**
   - Delays applied simultaneously to outbound order, outbound cancel, and inbound feed:
     - **$0\,\mu\text{s}$:** Passive $+0.097 \pm 0.013$ ticks (4.51% part, 72s); Aggressive $+0.087 \pm 0.017$ ticks (3.18% part, 92s).
     - **$500\,\mu\text{s}$:** Passive $+0.121 \pm 0.014$ ticks (6.00% part, 55s); Aggressive $+0.176 \pm 0.017$ ticks (2.43% part, 121s).
     - **$1,000\,\mu\text{s}$ ($1\,\text{ms}$):** Passive $+0.132 \pm 0.015$ ticks (6.12% part, 54s); Aggressive $+0.211 \pm 0.018$ ticks (2.24% part, 131s).
     - **$2,500\,\mu\text{s}$ ($2.5\,\text{ms}$):** Passive $+0.141 \pm 0.015$ ticks (6.40% part, 52s); Aggressive $+0.240 \pm 0.018$ ticks (2.09% part, 138s).
     - **$5,000\,\mu\text{s}$ ($5\,\text{ms}$):** Passive $+0.150 \pm 0.015$ ticks (6.87% part, 48s); Aggressive $+0.296 \pm 0.022$ ticks (2.02% part, 141s).
   - *Key findings:*
     - Cost rises monotonically in both styles.
     - Passive Shadow-PPOV loses **0.011 ticks/ms**; Aggressive POV loses **0.042 ticks/ms** (degrades ~4x faster).
     - Aggressive is cheaper only at $0\,\mu\text{s}$ (by 0.010 ticks); by $500\,\mu\text{s}$, Passive is cheaper by 0.055 ticks, and by $5\,\text{ms}$, Aggressive costs nearly double Passive.
     - Passive participation *increases* with delay (4.51% to 6.87%) as quotes arrive late and cross on contact (share filling on arrival jumps from 1.1% to 27.3%), whereas Aggressive participation collapses (3.18% to 2.02%) as marketable limits miss moving levels.

5. **Stale Information Control (Section 8.5, Table 6 / Table 11 in source):**
   - Delaying market data by 30 seconds while holding everything else fixed causes relative slippage to jump 3.9x from $+0.0953 \pm 0.0130$ to $+0.3673 \pm 0.0989$ ticks/contract.
   - Proves that the inherited information from the followed order is real and perishable.

6. **Parent-Order Size & Participation Dispersion Scaling Law (Section 9, Table 7 / Table 13 in source):**
   - Under a stylized exponential fill gap model, realized participation ratio $\hat{p}/\rho = Q/\text{Gamma}(Q, 1)$ has coefficient of variation $CV = 1/\sqrt{Q-2}$.
   - At $Q=1$: 10th–90th percentile band is $[0.44, 9.48]$ (participation is random).
   - At $Q=10$: $[0.70, 1.61]$, $CV = 0.35$.
   - At $Q=100$: $[0.89, 1.14]$, $CV = 0.10$.
   - At $Q=1,000$: $[0.96, 1.04]$, $CV = 0.03$.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- **Inability to Beat Mid-Price:** Without a directional alpha forecast, Shadow-PPOV consistently pays $+0.0955$ ticks in relative slippage against the arrival mid. The half-spread captured by passive resting is entirely erased by adverse selection.
- **Participation Instability on Small Orders:** For orders comprising few child fills ($Q < 20$), realized participation rate exhibits severe variance ($CV \ge 0.24$), making completion timing unpredictable unless constrained to a narrow inside band.
- **Zero-Impact Simulator Bias:** The underlying simulation engine does not model market impact or queue displacement. As participation rate rises above 5%, actual market execution costs in live markets will exceed the simulator's reported figures.

## Falsification plan

1. **Glosten-Milgrom Invariance & Slippage Floor Falsification (`research-proposed`):**
   - Deploy Shadow-PPOV and Aggressive POV across out-of-sample regular sessions of CME ES futures (2026 data) in an identical replay harness with $0\,\mu\text{s}$ simulated latency.
   - *Failure Rule (`research-defined falsification threshold`):* If the difference between passive and aggressive relative slippage exceeds $0.03$ ticks/contract ($p < 0.01$), or if passive slippage against arrival mid is strictly negative (beats mid-price), the model-free adverse selection balance thesis is falsified.

2. **Latency Degradation Slope Asymmetry Falsification (`research-proposed`):**
   - Measure relative slippage across simulated round-trip delays $\tau \in [0, 5000]\,\mu\text{s}$ in increments of $500\,\mu\text{s}$.
   - *Failure Rule (`research-defined falsification threshold`):* If the linear regression degradation slope of Passive Shadow-PPOV exceeds $0.025$ ticks/ms, or if the degradation slope of Aggressive POV is less than $0.025$ ticks/ms, the claim that passive shadowing is ~4x less sensitive to latency than aggressive taking is falsified.

3. **Identifier Mirroring vs. Shuffled Placebo Control (`research-proposed`):**
   - Compare Shadow-PPOV against two synthetic controls: (a) random-cancel placebo (cancelling after a Poisson lifetime matched to observed order durations), and (b) decoupled identifier placebo (cancelling on deletes/trades of unrelated orders).
   - *Failure Rule (`research-defined falsification threshold`):* If Shadow-PPOV fails to achieve at least a 20% reduction in relative slippage compared to the random-cancel placebo ($p < 0.01$), the hypothesis that identifier-keyed cancel mirroring extracts structural queue protection is falsified.

4. **Endogenous Queue Displacement Stress (`research-proposed`):**
   - Introduce an endogenous queue displacement model where placing a shadow order pushes subsequent participant orders further back in the queue and tests participation rates $\rho \in [0.01, 0.20]$.
   - *Failure Rule (`research-defined falsification threshold`):* If simulated slippage increases by $>0.10$ ticks when accounting for queue displacement at $\rho = 0.05$, the zero-impact evaluation is falsified as an accurate guide for institutional deployment.

## Crypto portability

**Label: adapted / unproven**

The primary paper evaluates Shadow-PPOV exclusively on CME ES futures using proprietary CME MDP3 binary feeds. Application to cryptocurrency markets requires substantial structural adaptations and remains completely unproven:

1. **Identifier Tracking Feed Availability (`research-proposed`):**
   - CME Globex broadcasts unique 64-bit exchange order IDs in MDP3 binary packets. Most cryptocurrency exchanges (Binance, OKX, Bybit, Coinbase) only publish aggregate Level 2 depth updates (e.g. Binance `@depth` diff streams) without unique order identifiers.
   - On standard L2 crypto venues, direct identifier-driven cancel mirroring is technically impossible. A ported version must substitute price-level volume subtraction heuristics (`adapted`).
   - Only select venues (e.g. Coinbase L3 Market Data, Hyperliquid L2/L3 book feeds) broadcast individual order IDs, but WebSocket delivery introduces millisecond-level network jitter.
2. **Fee Inversion Opportunity (`research-proposed`):**
   - In traditional futures (CME), trading fees are typically symmetric or volume-tiered taker/maker fees.
   - In crypto perpetual contracts (Binance, Bybit), maker fees are frequently negative (maker rebates of $-0.005\%$ to $0.000\%$) while taker fees are positive ($0.020\%$ to $0.050\%$).
   - A passive execution method that captures the spread without suffering elevated adverse selection would harvest substantial maker rebates, making the net economic advantage of passive shadowing significantly higher in crypto than in equities (`adapted`).
3. **24/7 Session & Cloud Latency Jitter (`research-proposed`):**
   - Traditional CME colocation in Aurora, IL offers sub-microsecond determinism. Crypto execution runs over public internet or cloud cross-connects (AWS Tokyo/Dublin) where round-trip latency fluctuates from 5 ms to 80 ms.
   - At latencies $>5\,\text{ms}$, the source data shows passive quotes convert into crosses on 27.3% of fills; in crypto, this would cause unexpected taker fee penalties unless strict post-only flags are enforced (`unproven`).

## Limitations

- **Benchmark Role, Not Standalone Alpha:** Shadow-PPOV is an execution benchmark designed to minimize execution drag; it generates no directional returns and loses money relative to arrival mid ($+0.0955$ ticks/contract).
- **Zero-Impact Simulator Bias:** The empirical findings rely on a replay harness without endogenous price impact or order displacement.
- **Single-Asset Empirical Evidence:** The empirical verification is conducted exclusively on CME ES futures over calendar year 2025; multi-venue equity routing (flow-inherited venue selection) remains an untested analytical proposal.
- **Strict Order-Level Data Dependency:** Requires granular MBO data feeds with order-level identifiers, which are expensive or unavailable in many retail and cryptocurrency venues.

## Implementation status

- `not-implemented`.
- This research record represents a pure literature capture and analytical benchmark specification. No implementation exists within NautilusTrader or PyBroker.
- Not authorized for Paper, Testnet, or Live execution.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- Research capture does not authorize deployment. Any subsequent integration into execution routing or algorithmic child order placement requires independent simulation with realistic fee and impact models.

## Related Wiki records

- `passive-market-impact-optimal-execution-mlofi-2026-09-02.md`
- `stochastic-tracking-optimal-execution-obizhaeva-wang-regularization-2026-09-02.md`
- `signature-optimal-execution-statistical-arbitrage-quadratic-reduction-2026-09-02.md`
- `order-flow-filtration-trade-grounded-imbalance-hawkes-2026-09-17.md`
- `crypto-perpetual-optimal-liquidation-funding-rate-hjb-2026-09-02.md`
- `duration-aware-bocpd-lognormal-order-flow-regime-2026-09-11.md`

## Sources

1. Vincent Maciejewski, *"Model-Free Passive Execution via Order-Level Shadowing"*, arXiv preprint `arXiv:2609.18019v1 [q-fin.TR]`, submitted September 16, 2026.
   - Abstract URL: https://arxiv.org/abs/2609.18019
   - HTML Full Text: https://arxiv.org/html/2609.18019v1
   - PDF: https://arxiv.org/pdf/2609.18019v1
   - DOI: https://doi.org/10.48550/arXiv.2609.18019
2. Vincent Mayeski / M2 Technologies (16425640 Canada Inc.), `kaspar-hft` GitHub repository:
   - Repository URL: https://github.com/vincent212/kaspar-hft
   - Commit SHA: `77a1f9d5ec1eb317cf909e2275c6eb4742ce2eae`
   - Key Files: `STRATEGY_SIMULATOR_GUIDE.md`, `ACTORS_INVENTORY.md`, `FILE_STRUCTURE.md`, `actors/cpp/Actor.cpp`
3. Supporting Literature Cited in Primary Source:
   - R. Almgren and N. Chriss, "Optimal Execution of Portfolio Transactions", *Journal of Risk*, 3(2):5–40, 2001.
   - L. R. Glosten and P. R. Milgrom, "Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders", *Journal of Financial Economics*, 14(1):71–100, 1985.
   - C. C. Moallemi and K. Yuan, "A Model for Queue Position Valuation in a Limit Order Book", Columbia University Working Paper, SSRN 2996221, 2016.
   - T. Foucault and A. J. Menkveld, "Competition for Order Flow and Smart Order Routing Systems", *Journal of Finance*, 63(1):119–158, 2008.
   - R. Kissell, *The Science of Algorithmic Trading and Portfolio Management*, Academic Press, 2013.
   - O. Guéant, C.-A. Lehalle, and J. Fernández-Tapia, "Optimal Portfolio Liquidation with Limit Orders", *SIAM Journal on Financial Mathematics*, 3(1):740–764, 2012.
