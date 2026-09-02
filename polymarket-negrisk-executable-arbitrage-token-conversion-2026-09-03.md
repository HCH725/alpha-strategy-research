---
schema: strategy-research-record-v1
title: "Polymarket NegRisk Executable Arbitrage: Pre-Settlement Token Conversion and Complete-Basket Settlement Dynamics"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - prediction-markets
  - polymarket
  - negrisk
  - arbitrage
  - token-conversion
  - market-microstructure
  - execution-analysis
  - smart-contracts
status: research-only
confidence: high
source_as_of: 2026-08-01
sources:
  - "Jonas Gebele, Timm Mutzel, and Florian Matthes, 'Executable Arbitrage and Market Efficiency in Prediction Markets', arXiv preprint arXiv:2608.00666v1 [cs.CE], August 1, 2026. https://arxiv.org/abs/2608.00666"
  - "Polymarket NegRisk CTF Adapter: https://github.com/Polymarket/neg-risk-ctf-adapter"
  - "Gnosis Conditional Tokens Framework: https://conditional-tokens.readthedocs.io/en/latest/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Polymarket NegRisk Executable Arbitrage: Pre-Settlement Token Conversion and Complete-Basket Settlement Dynamics

## Provenance

- **Primary Source:** Jonas Gebele, Timm Mutzel, and Florian Matthes (Technical University of Munich, TUM; Chair of Software Engineering for Business Information Systems), *"Executable Arbitrage and Market Efficiency in Prediction Markets"*, arXiv preprint `arXiv:2608.00666v1 [cs.CE]`, submitted August 1, 2026. Available at: [https://arxiv.org/abs/2608.00666](https://arxiv.org/abs/2608.00666); full HTML at [https://arxiv.org/html/2608.00666v1](https://arxiv.org/html/2608.00666v1).
- **Core Smart Contract Systems Studied:**
  - Polymarket NegRisk CTF Adapter: Open-source smart contract repository at [https://github.com/Polymarket/neg-risk-ctf-adapter](https://github.com/Polymarket/neg-risk-ctf-adapter) (deployed on Polygon PoS on November 28, 2023).
  - Gnosis Conditional Tokens Framework (CTF): ERC-1155 tokenized state-contingent claims specification and contracts at [https://conditional-tokens.readthedocs.io/en/latest/](https://conditional-tokens.readthedocs.io/en/latest/).
- **Primary Data Sources:**
  - Polygon RPC transaction logs and goldsky subgraphs for on-chain NegRisk adapter conversions and CTF split/merge traces cross-checked against PolygonScan.
  - Historical CLOB transaction panel covering 32,702 Polymarket events and 259 million trades through December 31, 2025 (sourced via HuggingFace dataset `SII-WANGZJ/Polymarket_data`).
  - High-frequency Level 2 CLOB market-state panel from pmxt (`archive.pmxt.dev/docs/v2-data-overview`) covering hour-stratified event-time order book replays from April 14, 2026, to May 19, 2026.
  - WebSocket market replication panel consisting of 308,416,666 messages recorded between May 8, 2026, and May 15, 2026, verifying order book synchronization properties.
- **Verification Note:** This record was produced through direct examination of the unabridged primary paper (arXiv:2608.00666v1 full text), its mathematical derivations, empirical tables, and appendix diagnostics. No search-engine snippets, LLM generated summaries, or secondary aggregators were used to supply strategy rules, equations, or empirical statistics.

## Economic mechanism

### Source-reported

In winner-takes-all prediction markets where events comprise $n \ge 3$ mutually exclusive and collectively exhaustive outcomes $Q$, terminal payoff identities theoretically constrain cross-market prices:
1. **Within-market complementarity:** In any individual binary market $i \in Q$, a unit YES claim $Y_i$ pays $1.00$ collateral if outcome $i$ occurs and $0$ otherwise; a unit NO claim $N_i$ pays $1.00$ collateral if outcome $i$ does not occur. Collateral backing enforces:
   $$Y_i + N_i \equiv \mathbf{1}$$
   where $\mathbf{1}$ denotes one unit of collateral (USDC).
2. **Event-level exclusivity:** Because exactly one outcome can occur:
   $$\sum_{i \in Q} Y_i \equiv \mathbf{1}$$
3. **Negative-risk subset identity:** Combining within-market complementarity and event-level exclusivity reveals that for any subset $S \subseteq Q$, holding a NO basket over $S$ is state-wise payoff-equivalent to holding $(|S|-1)$ units of collateral plus complementary YES exposure on the unselected outcomes $\bar{S} = Q \setminus S$:
   $$\sum_{i \in S} N_i \equiv (|S| - 1)\mathbf{1} + \sum_{j \in Q \setminus S} Y_j$$

The authors demonstrate a critical divergence between **payoff-space no-arbitrage** (which follows from terminal payoffs at expiration $T$) and **protocol-executable no-arbitrage** (which depends on whether the protocol provides pre-settlement position transformation primitives):
- **Settlement-based arbitrage:** Traders purchase an underpriced complete YES basket ($\sum_{i \in Q} Y_i$) for less than $1.00$ collateral, or an underpriced complete NO basket ($\sum_{i \in Q} N_i$) for less than $(|Q|-1)$ collateral, and hold the basket until oracle resolution. This locks up capital for days, weeks, or months, subjecting the trader to opportunity cost of capital, duration risk, and platform counterparty/oracle risk.
- **Converter-enabled arbitrage:** Polymarket's `NegRisk Adapter` operationalizes the subset identity before settlement in one specific direction:
   $$\text{convertPositions}: \sum_{i \in S} N_i \longrightarrow (|S| - 1)\mathbf{1} + \sum_{j \in Q \setminus S} Y_j$$
   Traders acquire NO-side tokens, execute the adapter call on-chain, immediately recover $(|S|-1)$ units of collateral plus the complementary YES tokens, and sell the returned YES tokens back into the CLOB. This realizes the arbitrage profit immediately while the market remains open, releasing collateral for continuous inventory recycling.
- **Asymmetric protocol enforcement:** Polymarket provides the NO-to-YES conversion primitive, but provides no native primitive for the reverse YES-to-NO direction:
   $$\sum_{j \in Q \setminus S} Y_j + (|S| - 1)\mathbf{1} \centernot\longrightarrow \sum_{i \in S} N_i$$
   Consequently, YES-side mispricings cannot be converted pre-settlement and must be enforced via capital-intensive complete basket holding to settlement. This structural asymmetry leads directly to observable market efficiency disparities: positive YES-side violations are far more frequent and persist significantly longer than adapter-supported NO-side violations.

### Research interpretation

This strategy captures a **structural, mechanism-driven execution alpha** arising from market-microstructure frictions and asymmetric smart contract primitives. Rather than forecasting event probabilities or macro outcomes, the trading agent exploits transient violations of deterministic combinatorial payoff bounds across mutually exclusive CLOB order books.

The economic edge is governed by the velocity of capital:
1. **Capital velocity / Inventory turn advantage:** In converter-enabled arbitrage, capital turnover is measured in seconds (median 10-second acquisition to 5-minute liquidation) rather than event duration (weeks to months). Even a microscopic net spread ($0.1\%$ to $0.5\%$) yields an annualized Sharpe ratio orders of magnitude higher than settlement-locked trades because the same capital base can be deployed hundreds of times per week.
2. **Maker-assisted latency tolerance:** Contrary to the common belief that crypto CLOB arbitrage requires ultra-subsecond taker execution, the empirical record reveals that $\approx 80\%$ of successful conversion bundles utilize passive resting limit orders to accumulate the input NO legs, converting and disposing only after legs are filled. This insulates the strategy from taker-fee drag and gas auction races on public mempools.

## Signal

### Formation timestamp

The observation signal is formed in event-time upon every Level-2 order book tick update across all component books in a mutually exclusive event set $Q$. Calculations run continuously off-chain via low-latency WebSocket market feeds, with executable bounds evaluated against resting bid and ask depth.

### Lookback and state evaluation

- **Sampling window:** Zero historical lookback required; evaluation is purely cross-sectional across depth snapshots at instantaneous time $t$.
- **Depth-aware portfolio valuation:** For any portfolio $P$ and quantity $q$:
  - $a_t(P, q)$: Executable cost to buy $q$ units of portfolio $P$ by walking the ask depth across all constituent books.
  - $b_t(P, q)$: Executable proceeds from selling $q$ units of portfolio $P$ by walking the bid depth across all constituent books.

### Entry triggers

At market update $t$, evaluate the fee-adjusted edge across all valid subsets $S \subseteq Q$ (focusing on $2 \le |S| \le |Q|$):

1. **Converter-Enabled NO-to-YES Arbitrage Signal:**
   $$\Delta_t^{N \to Y}(S, q) = (|S| - 1)q + b_t\left(\sum_{j \in Q \setminus S} Y_j, q\right) - a_t\left(\sum_{i \in S} N_i, q\right) - f(q)$$
   - Trigger Long NO / Convert when $\Delta_t^{N \to Y}(S, q) > \theta_{\text{conv}}$, where $\theta_{\text{conv}}$ is a positive minimum profit threshold (e.g., $\$0.01$ per share or $\$0.20$ total profit per bundle) and $f(q)$ accounts for trading fees and on-chain conversion gas/relayer costs.
   - For complete NO baskets ($S = Q$), the returned YES set is empty ($\bar{S} = \emptyset$), yielding direct collateral redemption:
     $$\Delta_t^{N \to \text{collateral}}(Q, q) = (|Q| - 1)q - a_t\left(\sum_{i \in Q} N_i, q\right) - f(q)$$

2. **Settlement-Based Complete Basket Arbitrage Signal:**
   - Complete YES Basket:
     $$\Delta_t^{\text{settle}, Y}(q) = q\mathbf{1} - a_t\left(\sum_{i \in Q} Y_i, q\right) - f(q)$$
   - Complete NO Basket:
     $$\Delta_t^{\text{settle}, N}(q) = (|Q| - 1)q\mathbf{1} - a_t\left(\sum_{i \in Q} N_i, q\right) - f(q)$$
   - Trigger Settlement Formation when $\Delta_t^{\text{settle}} > \theta_{\text{settle}} + r_{\text{hurdle}}(T - t)$, where $r_{\text{hurdle}}$ is the annualized cost of capital lock-up through expiration $T$.

3. **Reverse YES-to-NO Arbitrage Signal (Under Proposed Bidirectional Primitive):**
   $$\Delta_t^{Y \to N}(S, q) = b_t\left(\sum_{i \in S} N_i, q\right) - \left[(|S| - 1)q + a_t\left(\sum_{j \in Q \setminus S} Y_j, q\right)\right] - f(q)$$
   - Trigger when positive and executable on platforms supporting reverse composition (e.g., Hyperliquid) or if Polymarket deploys `convertYESPositions`.

### Exit and execution cadence

- **Converter Execution Pipeline:**
  1. *Leg Acquisition:* Acquire input NO positions on subset $S$. In maker-assisted mode, place limit buy orders on thin legs and sweep remaining depth once threshold fills occur. The empirical acquisition window is bounded within 5 Polygon blocks ($\approx 10.5$ seconds).
  2. *On-Chain Conversion:* Submit atomic transaction calling `convertPositions(bytes32 conditionId, uint256 indexSet, uint256 amount)` on the NegRisk Adapter contract.
  3. *Leg Disposition:* Liquidate the returned complementary YES positions on the CLOB. Empirically, completed dispositions occur within 150 Polygon blocks ($\approx 5.25$ minutes). If intermediate inventory cannot be immediately sold at the target price, resting limit asks are posted at the current spread midpoint.
- **Settlement Execution Pipeline:**
  1. *Basket Completion:* Accumulate complete lots spanning all active outcomes $i \in Q$ within a strict 10-minute formation window ($t_{\text{formation}} \le 10$ min).
  2. *Holding:* Transfer complete tokens to cold or custody vault; hold through oracle resolution.
  3. *Redemption:* Call CTF `redeemPositions` once UMA Optimistic Oracle finalizes resolution.

### Parameters

- **Subsets evaluated:** All singletons and pairs/triples up to $|Q| \le 10$; for large outcome sets ($|Q| > 10$), heuristic pruning restricts evaluation to full set $S=Q$ and high-volume subsets.
- **Spread adjustment model (for midpoint quote estimation):**
  - Midpoints between $\$0.03$ and $\$0.97$: 1.0-cent spread at half-cent midpoints ($0.5$¢); 2.0-cent spread at integer-cent midpoints ($1.0$¢).
  - Extreme tails (midpoint $< \$0.03$ or $> \$0.97$): 0.1-cent adjustment.
- **Gas / Cost parameters:**
  - Standard `convertPositions`: Base gas consumption $\approx 700,000$ to $2,500,000$ gas units depending on outcome vector length.
  - Reverse `convertYESPositions` overhead: Incremental $+63,095$ gas units relative to standard conversion.
- **Relayer routing:** Polymarket gasless relayer sponsored meta-transactions (zero user gas cost in standard CLOB API execution; priority gas required only during congested mempool races).

## Required data

- **Instrument:** ERC-1155 tokenized state-contingent claims (YES and NO outcome tokens) issued under the Gnosis Conditional Tokens Framework, backed 1:1 by collateral token USDC (`0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174` on Polygon PoS).
- **Universe:** Multi-outcome winner-takes-all event markets on Polymarket configured as negative-risk markets ($|Q| \ge 3$ mutually exclusive outcomes, e.g., election winners, sports tournament champions, pop-culture awards).
- **Venue:** Polymarket Central Limit Order Book (off-chain matching engine, on-chain Polygon PoS settlement). Comparison venues: Hyperliquid native outcome contracts, Kalshi CFTC-regulated binary event contracts.
- **Timeframe:** Continuous tick-level L2 order book updates (WebSocket level 2 diffs and snapshots) paired with on-chain Polygon block headers ($\approx 2.1$ seconds block time).
- **Fields:**
  - Off-chain CLOB: `market_id`, `token_id`, `side` (bid/ask), `price`, `size`, `timestamp`.
  - On-chain Contract Logs:
    - NegRisk Adapter: `PositionsConverted(address indexed actor, bytes32 indexed conditionId, uint256 indexSet, uint256 amount)`
    - CTF: `PositionSplit`, `PositionsMerge`, `PayoutRedemption`
    - Exchange: `OrderFilled` events
- **Point-in-time / Synchronization requirements:** Order book snapshots must be replayed in strict event-time sequence. Due to WebSocket multiplexing, independent verification is necessary to confirm that YES and NO order books for the same condition do not desynchronize (the primary source proved identical synchronization across $308.4$ million messages, with only 20 isolated API inconsistencies).
- **Missing-data handling:** If an outcome book has zero bid or ask depth, executable cost $a_t$ or proceeds $b_t$ is set to $\infty$ or $0$, respectively, preventing phantom signals. Imputation of liquidity is strictly prohibited.

## Execution assumptions

- **Execution Mode (Maker vs. Taker):**
  - The source's theoretical order-book model conservatively assumes **100% taker execution** (paying the full spread and crossing the book).
  - Empirical actor-level reconstruction reveals that in practice, **$\approx 80\%$ of successful conversion bundles are maker-assisted** (accumulating legs passively at the bid, or placing resting asks for disposition), while all-taker bundles account for $\le 40\%$ of weekly volume.
- **Fill model:** Deterministic depth-walking fill model. Order size $q$ is capped by the minimum cumulative depth available at or below the calculated threshold price across all constituent legs.
- **Execution Latency:**
  - Leg accumulation: Bounded within 5 Polygon blocks ($\approx 10.5$ seconds).
  - Disposal of converted tokens: Bounded within 150 Polygon blocks ($\approx 5.25$ minutes).
- **Relayer and Transaction Fees:** Standard Polymarket transactions are relayed through gasless meta-transactions. For private, un-relayed execution, Polygon gas price (typically 30–100 Gwei) applies. Maker fee is $0.00$ bps; taker fee is $0.00$ bps on standard Polymarket order books (platform fees are zero, making execution purely spread- and gas-limited).
- **Collateral / Leverage:** Unlevered, fully collateralized. Every token pair is backed 1:1 by USDC.

## Evidence

### Source-reported

The primary source (arXiv:2608.00666v1) provides an extensive empirical evaluation across three distinct panels:

1. **Total Realized Mechanism-Linked Profit:**
   - Reconstructed total across the historical panel: **$1,118,283 USDC** ($1.12 million).
   - **Converter-enabled arbitrage accounts for $1,085,999.68 USDC ($\approx 97.1\%$)** of total realized profit.
   - **Settlement-based complete basket formation accounts for $32,283.32 USDC ($\approx 2.9\%$)**.
2. **Actor-Level Exploitation and Concentration:**
   - Following deployment of the NegRisk Adapter on November 28, 2023, converter profits first manifested in January 2024.
   - The top 10 most profitable addresses captured **75%** of all converter-enabled profits.
   - Full-set NO-to-collateral conversions ($S = Q$) accounted for **$205,531 USDC (18.9%)** of the $1.086M total; partial conversions followed by inventory recycling accounted for the remaining **81.1%**.
   - An anomalous cluster of 75 conversions executed within 7 minutes on December 12, 2025, by three addresses produced an artificial $381,748 USDC profit on manipulated midpoint prices and was excluded as non-representative coordinated activity.
3. **Market-State Violation Incidence and Persistence Asymmetry (CLOB L2 Panel, April–May 2026):**
   - In the CLOB sample (624 observed episodes across the hour-stratified window), positive episodes were overwhelmingly concentrated on the **unsupported YES side: 2,098 positive episodes vs. only 36 positive episodes on the adapter-supported NO side**.
   - For non-window-spanning episodes with observed lifecycles, **median episode duration was 16.15 seconds on the unsupported YES side vs. 7.99 seconds on the adapter-supported NO side**.
   - $58.7\%$ (366 of 624) of CLOB episodes were window-spanning (lasting $> 50$ minutes), indicating severe, persistent mispricings when traders cannot convert tokens pre-settlement.
4. **Historical Fixed-Product Market Maker (FPMM) Benchmark:**
   - In the legacy FPMM regime (where no NegRisk Adapter existed), positive and negative episodes were symmetric across YES and NO sides, and $\approx 40\%$ of episodes persisted beyond 50 minutes (some lasting $> 24$ hours).
   - FPMM settlement baskets generated only $3,639 USDC in realized profit across 67 baskets, with a single actor capturing $76\%$.
5. **Profit Margin Decay Over Time:**
   - Median profit per conversion trade was $\approx 1.00$ USDC through July 2024.
   - Compressed to $\approx 0.20$ USDC across late 2024 and 2025.
   - Compressed further to $\approx 0.08$ USDC by early 2026 as automated competition escalated.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Intense Margin Compression and Bot Competition:** The rapid decline of median conversion profits from $\$1.00$ in 2024 to $\$0.08$ in 2026 demonstrates severe alpha decay. Competing on purely taker-driven sweeps against public order books is no longer viable without maker-assisted execution or co-located latency advantages.
2. **Execution Risk in Multi-Leg Acquisition:** In partial conversions ($S \subset Q$), an actor must fill multiple NO legs before calling `convertPositions`. If one leg fills while another slips or moves, the trader is left with unhedged directional exposure.
3. **Liquidation Frictions on Returned YES Tokens:** 81.1% of converter profit relies on disposing returned YES tokens within 150 blocks. In illiquid or breaking-news markets, bid liquidity on the returned YES tokens can evaporate, turning an apparent conversion edge into an inventory loss.
4. **Capital Lockup Penalty in Settlement Baskets:** While 5,923 profitable complete baskets were identified in the CLOB sample, their aggregate profit was only $28,644 USDC ($\approx \$4.83$ per basket). Holding capital for weeks to harvest $\$4.83$ carries severe negative risk-adjusted returns relative to baseline treasury/money-market yields.

## Falsification plan

The strategy hypothesis asserts that **pre-settlement smart contract conversion enables positive-expectancy executable arbitrage by eliminating capital lockup and facilitating maker-assisted inventory recycling**. This hypothesis will be falsified if:

1. **Maker-Taker Fee Sensitivity Test:** If Polymarket introduces standard CLOB trading fees (e.g., $\ge 5$ bps taker fee or removes maker fee rebates), and the net realized profit $\Pi^{\text{conv}}$ across all converted bundles drops below zero on out-of-sample data.
2. **Capital Lockup Opportunity Cost Hurdle:** If the internal rate of return (IRR) on settlement-based complete baskets, adjusted for holding time to resolution $T - t$, fails to exceed the risk-free SOFR rate plus a $200$ bps smart contract risk premium on $> 80\%$ of formed baskets.
3. **Bidirectional Adapter Impact Experiment:** If the deployment of a bidirectional conversion primitive (`convertYESPositions`) on a test environment or production market fails to compress YES-side violation frequency and duration by at least $70\%$ toward NO-side levels.
4. **Adverse Execution / Stale Fill Test:** If the slippage incurred when liquidating returned YES tokens over the 150-block post-conversion window exceeds the initial conversion spread on $> 35\%$ of trials under random order flow conditions.

## Crypto portability

- **Portability status:** `direct` for EVM-based decentralized prediction markets; `adapted` for next-generation L1 prediction architectures; `not applicable` for traditional finance.
- **EVM Prediction Markets (Polymarket):** Direct native application. The mechanism is built directly on the Gnosis Conditional Tokens Framework (ERC-1155) and the Polygon `NegRiskAdapter` smart contract.
- **High-Performance L1s (Hyperliquid):** Adapted. As detailed in the primary paper (Section 6 and Appendix 0.B.1), Hyperliquid natively supports outcome operations (`negateOutcome`, `splitOutcome`, and `mergeQuestion`). Pre-settlement NO-to-YES is direct via `negateOutcome`, while reverse YES-to-NO can be composed natively by contributing temporary collateral, splitting into all outcomes of $S$, and merging the complete YES set.
- **Centralized / Regulated Venues (Kalshi):** Adapted / Constrained. Kalshi implements "Collateral Return" at the clearinghouse ledger level, which automatically nets out redundant margin on mutually exclusive contracts, but does not mint transferable ERC-1155 token pairs, preventing secondary DEX arbitrage or multi-venue inventory routing.
- **Traditional Financial Markets:** Not applicable. Traditional binary options, sportbooks, and prediction exchanges do not expose open smart contract primitives for atomic token minting, splitting, merging, or pre-settlement subset transmutation.

## Limitations

- **Historical Order Book Sample Window:** Full Level-2 CLOB order book depth was available to the authors only for the April–May 2026 period (hour-stratified). Consequently, market-state violation persistence could not be matched 1:1 with the entire 2023–2025 actor transaction panel.
- **Actor Intent Ambiguity:** In the 1,909 complete NO baskets held to settlement in the CLOB sample (earning $14,445 USDC), the data cannot definitively establish whether traders held positions intentionally (e.g., formation occurred seconds before oracle resolution) or whether they suffered execution failures during attempted adapter conversions.
- **Smart Contract and Oracle Risk:** The strategy relies entirely on the solvency, correctness, and dispute resolution of the Gnosis CTF, Polymarket NegRisk Adapter, and UMA Optimistic Oracle. A disputed or delayed oracle outcome freezes collateral and destroys capital velocity.
- **Platform Relayer Centralization:** While matching occurs off-chain, reliance on Polymarket's gasless relayer exposes the strategy to potential rate-limiting or MEV front-running by privileged operator infrastructure.

## Implementation status

- `not-implemented`: This strategy record represents an external research capture and market-microstructure analysis.
- No code or algorithmic execution pipelines have been implemented in PyBroker, NautilusTrader, paper-trading engines, testnet environments, or live execution accounts.

## Adoption boundary

- Status: `research-only`
- Adoption: `not-approved`
- Approval scope: `research-only`
- Presence of this record in the repository serves purely to document the empirical properties of smart-contract-enabled prediction market arbitrage and does not authorize capital allocation, paper trading, testnet verification, or live trading.

## Related Wiki records

- `[[crypto-prediction-market-high-frequency-combinatorial-arbitrage-2026-09-01]]` (Analysis of NBA cross-market logical subset constraints; contrasts with NegRisk event-level conversion studied here)
- `[[crypto-prediction-market-layered-informed-trading-skill-score-2026-09-01]]` (Informed wallet tracking and adverse selection in Polymarket CLOBs)
- `[[defi-prediction-market-uniform-loss-amm-lvr-dynamic-liquidity-2026-09-02]]` (Theoretical AMM design mitigating adverse selection in binary prediction claims)
- `[[prediction-market-structural-volatility-wright-fisher-glosten-milgrom-2026-09-02]]` (Structural volatility modeling and quoting spreads in binary prediction markets)
- `[[polymarket-binance-high-frequency-binary-lead-lag-2026-09-02]]` (High-frequency lead-lag arbitrage between Binance spot and Polymarket binary contracts)

## Sources

1. Jonas Gebele, Timm Mutzel, and Florian Matthes, *"Executable Arbitrage and Market Efficiency in Prediction Markets"*, arXiv preprint `arXiv:2608.00666v1 [cs.CE]`, August 1, 2026. DOI: [10.48550/arXiv.2608.00666](https://doi.org/10.48550/arXiv.2608.00666). Full text URL: [https://arxiv.org/abs/2608.00666](https://arxiv.org/abs/2608.00666); HTML: [https://arxiv.org/html/2608.00666v1](https://arxiv.org/html/2608.00666v1).
2. Polymarket NegRisk CTF Adapter Smart Contract Repository, [https://github.com/Polymarket/neg-risk-ctf-adapter](https://github.com/Polymarket/neg-risk-ctf-adapter).
3. Gnosis Conditional Tokens Framework Documentation, [https://conditional-tokens.readthedocs.io/en/latest/](https://conditional-tokens.readthedocs.io/en/latest/).
4. Polymarket Official Developer Documentation, [https://docs.polymarket.com/](https://docs.polymarket.com/).
5. Z. Wang, L. Chao, Y. Bao, L. Cheng, J. Liao, and Y. Li, *"Polymarket data: complete data infrastructure for polymarket"*, Hugging Face Dataset: [https://huggingface.co/datasets/SII-WANGZJ/Polymarket_data](https://huggingface.co/datasets/SII-WANGZJ/Polymarket_data), 2026.
6. pmxt, *"Polymarket Orderbook Archive (v2): Data Overview"*, [https://archive.pmxt.dev/docs/v2-data-overview](https://archive.pmxt.dev/docs/v2-data-overview), 2026.
7. Hyperliquid Systems, *"Hyperliquid Documentation: Native Outcome Operations"*, [https://hyperliquid.gitbook.io/hyperliquid-docs/](https://hyperliquid.gitbook.io/hyperliquid-docs/), 2026.
8. Kalshi Inc., *"Collateral Return Documentation"*, [https://help.kalshi.com/en/articles/13823816-collateral-return](https://help.kalshi.com/en/articles/13823816-collateral-return), 2026.
