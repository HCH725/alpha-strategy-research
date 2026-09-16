---
schema: strategy-research-record-v1
title: "Polymarket Protocol Finality, Observed Redemption Latency, and Known-Payout Carry Arbitrage Falsification (Nechepurenko 2026)"
created: 2026-09-16
updated: 2026-09-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - prediction-markets
  - polymarket
  - conditional-tokens-framework
  - market-microstructure
  - settlement-latency
  - protocol-finality
  - carry-arbitrage
  - empirical-falsification
  - kaplan-meier
status: research-only
confidence: high
source_as_of: 2026-07-12
sources:
  - "Maksym Nechepurenko, 'Resolution Is Not Settlement, Part II: Protocol Finality and Observed Redemption on Polymarket', arXiv:2609.15373v1 [q-fin.TR, cs.CR, q-fin.CP], September 14, 2026. https://arxiv.org/abs/2609.15373"
  - "Maksym Nechepurenko, 'Resolution Is Not Settlement, Part I: Oracle Adjudication and Semantic Governance on Polymarket', arXiv:2609.15368v1 [q-fin.TR, cs.CR, q-fin.CP], September 14, 2026. https://arxiv.org/abs/2609.15368"
  - "Gnosis, 'Conditional Tokens Contracts', Gnosis Conditional Tokens Framework (CTF) open-source smart contract repository on GitHub. https://github.com/gnosis/conditional-tokens-contracts"
  - "Polymarket, 'UMA CTF Adapter', commit 8b76cc9e0d46c6f7450a0adb0ddc0f5b0568c9cc, Polymarket repository. https://github.com/Polymarket/uma-ctf-adapter"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Polymarket Protocol Finality, Observed Redemption Latency, and Known-Payout Carry Arbitrage Falsification (Nechepurenko 2026)

## Provenance

- **Primary Academic Sources:**
  - **Author:** Maksym Nechepurenko (Research Department, Devnull FZCO; Lead Researcher, ForesightFlow programme) (`source-reported`).
  - **Part II Primary Paper:** Maksym Nechepurenko, *"Resolution Is Not Settlement, Part II: Protocol Finality and Observed Redemption on Polymarket"*, arXiv preprint `arXiv:2609.15373v1 [q-fin.TR, cs.CR, q-fin.CP]`, submitted September 14, 2026 (`source-reported`).
    - Stable arXiv URL: https://arxiv.org/abs/2609.15373
    - Full-text HTML: https://arxiv.org/html/2609.15373v1
    - Full-text PDF: https://arxiv.org/pdf/2609.15373v1
    - SSRN Working Paper: `SSRN 7344081` (`source-reported`).
  - **Part I Companion Paper:** Maksym Nechepurenko, *"Resolution Is Not Settlement, Part I: Oracle Adjudication and Semantic Governance on Polymarket"*, arXiv preprint `arXiv:2609.15368v1 [q-fin.TR, cs.CR, q-fin.CP]`, submitted September 14, 2026 (`source-reported`).
    - Stable arXiv URL: https://arxiv.org/abs/2609.15368
    - Full-text HTML: https://arxiv.org/html/2609.15368v1
    - SSRN Working Paper: `SSRN 7344079` (`source-reported`).
- **Core Smart Contract Systems & ABIs Audited:**
  - **Gnosis Conditional Tokens Framework (CTF):** Deployed on Polygon PoS at `0x4D97DCd97eC945f40cF65F87097ACe5EA0476045` (`source-reported`).
    - ABI Event Signatures:
      - `ConditionPreparation(bytes32 indexed conditionId, address indexed oracle, bytes32 indexed questionId, uint outcomeSlotCount)` (`source-reported`).
      - `ConditionResolution(bytes32 indexed conditionId, address indexed oracle, bytes32 indexed questionId, uint outcomeSlotCount, uint[] payoutNumerators)` (`source-reported`).
      - `PayoutRedemption(address indexed redeemer, address indexed collateralToken, bytes32 indexed parentCollectionId, bytes32 conditionId, uint[] indexSets, uint payout)` (`source-reported`).
  - **Polymarket UMA CTF Adapter:** Commit `8b76cc9e0d46c6f7450a0adb0ddc0f5b0568c9cc`, `src/UmaCtfAdapter.sol` (`source-reported`).
- **Target Population & Censoring Snapshots:**
  - Upstream question population frozen at Polygon block `79,721,080` (185,550 initialized adapter-question instances, 350,703 decoded adapter logs) (`source-reported`).
  - Downstream follow-up snapshot frozen at Polygon block `90,114,204` at canonical timestamp `2026-07-12T17:11:41Z` (`source-reported`).
  - Exact bridge cohort: 108,638 linked conditions; 99,283 observed protocol-resolution events; 92,158 observed redemptions of any amount; 91,817 observed positive-payout redemptions (`source-reported`).
- **Repository Deduplication Audit:**
  - Audited all existing `.md` strategy records in `alpha-strategy-research` on 2026-09-16:
    - Zero prior records cite `arXiv:2609.15373`, `arXiv:2609.15368`, SSRN 7344081, SSRN 7344079, or Maksym Nechepurenko's September 2026 "Resolution Is Not Settlement" series.
    - Adjacent prediction market records (`crypto-short-horizon-prediction-market-settlement-push-reversal-2026-09-01.md`, `polymarket-negrisk-executable-arbitrage-token-conversion-2026-09-03.md`, `kalshi-prediction-market-pricing-wedge-executable-spread-falsification-2026-09-13.md`, `crypto-prediction-market-layered-informed-trading-skill-score-2026-09-01.md`) address different phenomena: spot order-flow manipulation, static combinatorial NegRisk basket conversion, Kalshi bid-ask spread fee falsification, and wallet information leakage scores. None model or empirically evaluate the multi-stage gap between oracle adjudication, protocol finality, and holder redemption realization.
  - This record represents an independent, source-complete research capture of protocol finality latency and the empirical falsification of post-outcome carry arbitrage.

## Economic mechanism

### Source-reported

1. **The Multi-Stage Lifecycle Fallacy in Prediction Markets:**
   - In quantitative prediction market research, contract resolution is frequently treated as an instantaneous, scalar event at a single timestamp where winning tokens instantaneously convert to cash (`source-reported`).
   - Nechepurenko (2026, Parts I & II) demonstrates that on decentralized infrastructure (Polymarket on Polygon PoS), resolution consists of four distinct, non-equivalent lifecycle states controlled by different actors and governed by separate protocol clocks (`source-reported`):
     1. **Oracle Adjudication ($T_c^O$):** UMA Optimistic Oracle receives a data assertion, observes a dispute window, and finalizes an outcome proposal (`source-reported`).
     2. **Adapter Terminality ($T_c^A$):** The Polymarket adapter contract transitions to a terminal state after oracle finality (`source-reported`).
     3. **Protocol Finality ($T_c^P$):** The adapter executes `reportPayouts(questionId, payouts)` on the Gnosis Conditional Tokens Framework (CTF) contract, emitting a canonical `ConditionResolution` event that permanently locks the integer payout vector $\bm{\pi}_c$ and creates legal claim redeemability (`source-reported`).
     4. **Holder Realization ($T_c^R$):** The token holder (or smart contract proxy) executes an explicit on-chain transaction calling `redeemPositions()`, emitting a `PayoutRedemption` event that burns ERC-1155 tokens and transfers collateral (USDC) to the wallet (`source-reported`).

2. **The Known-Payout Carry Benchmark and Cash-Equivalent Wedge:**
   - When an outcome becomes known or oracle-finalized, winning tokens frequently trade at a persistent discount to parity on secondary order books (`source-reported`):
     $$\omega_c(t) = \pi_c^{\mathrm{win}} - V_c(t)$$
     where $V_c(t)$ is the executable secondary market price in collateral units and $\pi_c^{\mathrm{win}}$ is the final winning payout per unit (`source-reported`).
   - The author formalizes the "Known-Payout Carry Benchmark": assuming fixed final payout $\pi_c$, random realization delay $\Delta_c$, collateral carry rate $r$, and transaction cost $k_c$ with zero default risk, the present value is (`source-reported`):
     $$PV = \frac{\pi_c}{1 + r \Delta_c} - k_c$$
   - The total delay decomposes into mechanism delay $L_c^{OP} = T_c^P - T_c^O$ (controlled by the adapter/protocol relay) and holder delay $\Delta_c^{PH} = T_c^R - T_c^P$ (controlled by holder behavior and custody infrastructure) (`source-reported`).
   - The total state-conditioned carrying cost is (`source-reported`):
     $$K_c = \int_0^{\Delta_c} k_{s(t)}(t) \, dt$$
   - State-occupation and capital-time are defined by combining occupation intervals with a capital-service rate $\kappa_c^{\mathrm{cap}}(t)$ (`source-reported`):
     $$\Omega_c^{\mathrm{cap}} = \int_{T_c^P}^{T_c^R} \kappa_c^{\mathrm{cap}}(t) \, dt$$

3. **Asynchronous Finality in Multi-Leg Combinatorial Spreads:**
   - In combinatorial and NegRisk event structures (e.g. multi-candidate elections), an event spread comprises multiple condition legs (`source-reported`).
   - When leg $A$ reaches protocol finality while leg $B$ remains unresolved, the spread's hedged delta collapses: the position turns into a deterministic claim plus an unhedged directional single-leg exposure, freezing capital and generating asymmetric carry drag (`source-reported`).

4. **Theorem 6 (The Value Denominator Gate):**
   - Nechepurenko formally proves that redemption events alone identify realized holder actions and paid collateral, but mathematically cannot identify the fraction of winning entitlement redeemed without an independent, balance-consistent ERC-1155 ledger reconstruction ($G\text{-}\mathrm{VALUE}$ blocked) (`source-reported`).

### Research interpretation

1. **Falsification of the Naive "Post-Outcome Carry Arbitrage" Edge:**
   - Retail algorithmic traders frequently deploy bots targeting "post-outcome carry": purchasing winning binary shares at $0.985$–$0.992$ immediately after media confirmation or initial oracle proposal, expecting an annualized return $> 100\%$ on what appears to be a "riskless" convergence to $1.00$.
   - This research establishes that the secondary discount $\omega_c(t)$ is not an unexploited behavioral inefficiency or free alpha. It is the competitive equilibrium compensation for:
     1. Unresolved mechanism latency $L_c^{OP}$ (which can extend from hours to days if disputes or route resets occur, as demonstrated in Part I where modern routes have median request-to-proposal times of 2 to 8.6 days) (`source-reported`);
     2. Capital-time opportunity costs ($\Omega_c^{\mathrm{cap}}$) while funds remain locked in illiquid ERC-1155 token states;
     3. Execution friction and Polygon network gas fees ($k_c$) required to trigger redemption transactions;
     4. Protocol-resolution failure tail risk: 9,355 conditions (8.61% of the exact-linked cohort) never reached protocol resolution during the observation window (`source-reported`).

2. **Leverage Amplification & Margin Engine Fragility:**
   - In synthetic or leveraged prediction market protocols (such as perpetual binary futures), marking an asset to $1.00$ upon oracle proposal introduces phantom equity, because protocol finality has not occurred.
   - Conversely, marking to market ($V_c(t)$) during the post-finality redemption lag penalizes traders with the cash-equivalent wedge $\omega_c(t)$, triggering spurious liquidations due to protocol-induced latency rather than economic loss.

## Signal

### 1. Underlying Strategy Concept (Naive Post-Outcome Carry)

The target trading strategy evaluated and falsified by this empirical capture is the systematic capture of the post-outcome secondary discount on Polymarket:
- **Observation:** Outcome $c$ has occurred or oracle proposal is submitted, but secondary market CLOB best ask satisfies $V_c(t) < 1.00$ (`source-reported`).
- **Hypothesized Signal:** Buy winning outcome token at $V_c(t)$; hold until settlement; redeem via CTF for $1.00$ cash, capturing gross return $(1.00 - V_c(t)) / V_c(t)$ (`source-reported`).

### 2. Normalized Falsification & Feasibility Filter (`research-proposed`)

To evaluate whether this strategy generates genuine risk-adjusted alpha or net loss after capital-time and execution drag, we specify the exact normalized operational rules:

- **Signal Formation Timestamp:** Formed on the arrival of an official oracle assertion or `ConditionResolution` block timestamp on Polygon PoS (`research-proposed`).
- **Universe Filter:** Active Polymarket binary conditions with verifiable UMA CTF Adapter linkage and observable order book depth on the winning outcome token (`research-proposed`).
- **Secondary Discount Screen:**
  $$V_c(t) \le 1.00 - \omega_{\mathrm{min}}$$
  where $\omega_{\mathrm{min}} = 0.008$ ($0.80$ cents) is a `research-proposed` minimum gross margin filter.
- **Capital-Time Cost Gate:** A candidate trade is accepted if and only if the projected net carry exceeds the opportunity cost of capital:
  $$\frac{1.00 - V_c(t) - k_c}{V_c(t)} > \kappa_{\mathrm{ref}}^{\mathrm{cap}} \cdot \mathbb{E}[\Delta_c]$$
  where:
  - $k_c$ is the transaction cost model incorporating secondary taker fee ($0$ bps on Polymarket CLOB) + Polygon gas for buy order + Polygon gas for `redeemPositions` ($~120,000$ gas units $\times$ gas price) (`research-proposed`).
  - $\kappa_{\mathrm{ref}}^{\mathrm{cap}}$ is the reference capital hurdle rate (Polygon USDC Aave borrow rate or $8.0\%$ annualized) (`research-proposed`).
  - $\mathbb{E}[\Delta_c]$ is the expected duration to redemption, parameterized by route: $200$ seconds if protocol-final, or $176,388$ seconds (~$49$ hours) if pre-protocol modern adapter (`source-reported`).
- **Execution Logic:**
  - Enter via passive limit buy order at best bid or aggressive marketable limit order at best ask (`research-proposed`).
  - Upon CTF `ConditionResolution` confirmation, trigger an automated `redeemPositions` transaction if positive payout exists (`research-proposed`).
- **Exit & Holding Period:**
  - Normal exit: Collateral redemption via `PayoutRedemption` event (`source-reported`).
  - Emergency timeout exit: If condition remains unresolved after $T_{\mathrm{timeout}} = 14$ days, dump claim on secondary book at market bid to mitigate permanent capital freeze (`research-proposed`).

## Required data

- **On-Chain Event Logs (Polygon PoS):**
  - Contract: Gnosis CTF `0x4D97DCd97eC945f40cF65F87097ACe5EA0476045` (`source-reported`).
  - Events: `ConditionPreparation`, `ConditionResolution`, `PayoutRedemption` (`source-reported`).
  - Envelope Fields: `block_number`, `block_hash`, `block_timestamp`, `tx_hash`, `log_index`, `topics`, `data` (`source-reported`).
- **Adapter & Oracle State Data:**
  - Polymarket UMA CTF Adapter logs and DVM dispute notifications (`source-reported`).
  - UMA Optimistic Oracle request and proposal timestamps (`source-reported`).
- **Market Data:**
  - Tick-by-tick or Level 2 order book snapshots of Polymarket CLOB token prices $V_c(t)$ and bid-ask spreads (`source-reported`).
  - Polygon gas prices (base fee + priority fee in Gwei) for execution cost accounting (`research-proposed`).
- **Point-in-Time Discipline:**
  - Only block headers and confirmed transaction logs with finalized receipts may be used to identify state transitions (`source-reported`).
  - Secondary order book prices must be sampled strictly after block confirmation timestamps to eliminate look-ahead bias (`research-proposed`).

## Execution assumptions

- **Execution Venue:** Polygon PoS blockchain for settlement and Polymarket CLOB (off-chain matching, on-chain settlement) for secondary token acquisition (`source-reported`).
- **Execution Fees & Gas Costs:**
  - Secondary CLOB trading fee: $0.00\%$ (`source-reported`).
  - On-chain redemption execution: ~120,000 gas units per `redeemPositions` call. At 50 Gwei and POL = $0.40, cost is ~$0.0024 per redemption (`research-proposed`).
  - Polygon reorg safety: Minimum 128 block confirmations (~256 seconds) for economic finality (`research-proposed`).
- **Capital Cost & Slippage:**
  - Cost of capital: 8.0% APR continuously compounded (`research-proposed`).
  - Secondary order book slippage: Evaluated against top-of-book depth; market orders capped at available quantity at best ask (`research-proposed`).
- **Fill Model:** Immediate fill against standing limit orders; no partial fill queue priority assumed (`research-proposed`).

## Evidence

### Source-reported

All empirical figures below are directly reported by Maksym Nechepurenko (arXiv:2609.15373v1 and arXiv:2609.15368v1, September 2026):

1. **Bridge Population & Lifecycle Accounting (arXiv:2609.15373v1, Section 9.1, Table 7 & 8):**
   - Exact bridge cohort: **108,638 linked conditions** (`source-reported`).
   - Observed protocol-resolution events by block 90,114,204: **99,283 conditions** (91.39% of linked cohort) (`source-reported`).
   - Unresolved conditions at follow-up snapshot: **9,355 conditions** (8.61%) (`source-reported`).
   - Contract-wide CTF resolution events in total target union: **1,857,116 resolved conditions** (`source-reported`).

2. **Payout-Vector Taxonomy (arXiv:2609.15373v1, Section 9.2, Table 9):**
   Across the 99,283 resolved exact-linked conditions:
   - Canonical `(0, 1)` vectors (NO wins): **53,847 conditions** (54.24%) (`source-reported`).
   - Canonical `(1, 0)` vectors (YES wins): **45,024 conditions** (45.35%) (`source-reported`).
   - Fifty-fifty split `(0.5, 0.5)` vectors: **410 conditions** (0.41%) (`source-reported`).
   - Other valid vectors: **2 conditions** (0.002%) (`source-reported`).

3. **Observed Redemption Latency & Survival Accounting (arXiv:2609.15373v1, Section 9.4, Table 11):**
   Within the resolved exact-linked risk set of 99,283 conditions:
   - Conditions with observed redemption of any amount: **92,158 conditions** (92.82%) (`source-reported`).
   - Conditions with observed positive-payout redemption: **91,817 conditions** (92.48%) (`source-reported`).
   - **Kaplan-Meier Median time from protocol resolution to any redemption:** **182 seconds** (`source-reported`).
   - **Kaplan-Meier Median time from protocol resolution to positive redemption:** **200 seconds** (`source-reported`).
   - Heterogeneous follow-up exposure: 25th, 50th, and 75th percentiles of available observation follow-up are **21,074,649 seconds** (~243.9 days), **25,254,353 seconds** (~292.3 days), and **33,617,219 seconds** (~389.1 days), with maximum follow-up of **142,006,845 seconds** (~4.5 years) (`source-reported`).

4. **Oracle & Cross-Contract Finality Latency (arXiv:2609.15368v1, Section 8; arXiv:2609.15373v1, Section 9.3, Table 10):**
   - Upstream oracle requests in Part I: 184,148 creations, 159,447 proposals, 1,604 disputes, 159,133 settlements (`source-reported`).
   - Request-to-first-proposal median delay: **182 seconds** on legacy route, but **176,388 to 744,151 seconds** (2.04 to 8.61 days) on modern routes (`source-reported`).
   - Post-reset successor proposals: median **300 to 2,909 seconds** (`source-reported`).
   - Downstream cross-contract linkage: only **823 conditions** have an interval-qualified terminal generation; **48** have multiple candidate generations; **91,638 conditions** have no compatible terminal generation in frozen evidence; and **16,129** are right-censored or unevaluable (`source-reported`).

### Independently reproduced

`Not independently reproduced.` All empirical metrics, lifecycle counts, Kaplan-Meier medians, and payout-vector frequencies reflect direct extraction from Nechepurenko (arXiv:2609.15373v1 and arXiv:2609.15368v1). No independent execution on raw Polygon RPC archives has been completed in this research stack.

### Negative evidence

- **Pervasive Resolution Unavailability:** 9,355 conditions (8.61% of all linked conditions) failed to resolve over months of follow-up, causing indefinite capital lockup for any trader holding tokens awaiting redemption (`source-reported`).
- **Dispute & Route Extension Drag:** On modern adapter routes, median oracle adjudication requires 2 to 8.6 days before protocol resolution can even begin. Under an 8% cost of capital, an 8-day lockup consumes ~17.5 bps of return, eroding over 20% of an 80 bps discount (`source-reported`).
- **Asymmetric Multi-Leg Spread Breakdown:** In combinatorial markets, cross-leg finality is non-atomic. When one leg settles days ahead of another, the spread hedge collapses, exposing traders to directional delta and severe collateral friction (`source-reported`).
- **Missing Value Denominator ($G\text{-}\mathrm{VALUE}$ Blocked):** Token redemption records do not equal total entitlement completion; a significant tail of winning tokens remains unredeemed indefinitely due to gas cost vs. dust value (`source-reported`).

## Falsification plan

To test and definitively falsify the hypothesis that secondary-market post-resolution discounts represent an exploitable alpha edge, the following pre-registered empirical tests are defined:

1. **Net Realized Carry vs. Capital Hurdle Test:**
   - **Sample:** All resolved Polymarket binary conditions from 2024 to 2026 where $V_c(t)$ is observed on the CLOB between oracle proposal and protocol resolution (`research-proposed`).
   - **Methodology:** Simulate purchasing winning tokens at $V_c(t)$, paying on-chain gas costs for acquisition and redemption, and applying an 8% APR capital-service rate across actual observed holding time $\Delta_c = T_c^R - t_{\mathrm{entry}}$ (`research-proposed`).
   - **Decision Rule (`research-defined falsification threshold`):** The carry alpha hypothesis is falsified if the net annualized Sharpe ratio across the strategy is $\le 0.0$ or if the net cumulative return is lower than holding passive Polygon USDC on Aave.

2. **Asynchronous Leg-Variance Stress Test:**
   - **Sample:** Multi-candidate NegRisk election markets with $n \ge 3$ outcomes (`research-proposed`).
   - **Methodology:** Hold complete synthetic NO baskets and record portfolio variance during the window between the first leg's resolution and the final leg's resolution (`research-proposed`).
   - **Decision Rule (`research-defined falsification threshold`):** The market-neutral carry hypothesis is falsified if unhedged residual variance exceeds $25\%$ of total position notional during the asynchronous resolution window.

3. **Margin Engine Spurious Liquidation Audit:**
   - **Sample:** Simulated 5x leveraged event-linked perpetual contracts evaluated against historical Polymarket price paths (`research-proposed`).
   - **Methodology:** Compare liquidation rates under mark-to-par ($1.00$) vs mark-to-market ($V_c(t)$) during the post-finality interval $[T_c^P, T_c^R]$ (`research-proposed`).
   - **Decision Rule (`research-defined falsification threshold`):** If mark-to-market triggers $> 0.5\%$ spurious liquidations of economically winning positions due solely to the cash-equivalent wedge $\omega_c(t)$, mark-to-market is falsified as an implementable margin rule for prediction market derivatives.

## Crypto portability

`direct`

The mechanism and empirical phenomena documented in this record are 100% native to cryptocurrency and smart contract market microstructure. Polymarket is an on-chain prediction market deployed on Polygon PoS, utilizing the Gnosis Conditional Tokens Framework (ERC-1155 tokens) and UMA Optimistic Oracle adapters.

Key crypto-native structural dependencies include:
- **Blockchain Execution Clocks:** Block numbers, block timestamps, and log indices determine exact state precedence, distinct from off-chain wall-clock time (`source-reported`).
- **Gas & Network Congestion:** Transaction fees on Polygon PoS dictate the economic threshold below which small winning claims are abandoned (unredeemed dust) (`source-reported`).
- **Smart Contract Composability & Adapter Routes:** Discrepancies between legacy direct adapters and modern multi-step routes govern oracle resolution latency (`source-reported`).
- **Collateral Settlement Currency:** All payoffs settle in bridged USDC (`0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174` / Native USDC), subjecting holders to quote-currency opportunity costs and bridge risk (`source-reported`).

## Limitations

- **Not Independently Reproduced:** All lifecycle, redemption, and payout statistics represent third-party empirical findings reported by Nechepurenko (2026).
- **Frozen Cohort Boundaries:** Findings are based on historical Polygon data ending at block 90,114,204 (July 12, 2026). Protocol updates, gas adjustments, or adapter redesigns post-snapshot may alter latency distributions (`source-reported`).
- **Entitlement Denominator Gap ($G\text{-}\mathrm{VALUE}$ Blocked):** The exact total dollar value of unredeemed winning claims cannot be proven from event logs alone without a full ERC-1155 token balance archive (`source-reported`).
- **Address Anonymity:** Public redemption addresses do not map one-to-one to unique human traders or institutional entities (`source-reported`).
- **Off-Chain CLOB vs. On-Chain State:** Secondary market prices $V_c(t)$ reflect off-chain CLOB dynamics, which may experience temporary disconnection or order-cancellation freezes during oracle dispute events (`research-proposed`).

## Implementation status

No automated execution or backtest script in our research stack (`nautilus-quant-system` or PyBroker) has been implemented. This record captures empirical market microstructure evidence and theoretical falsification principles from external research.

## Adoption boundary

Research material only. This record documents an empirical microstructure study and the falsification of a naive retail carry strategy. It does not constitute profitable alpha, a validated production strategy, or authorization for paper trading, testnet deployment, or live capital allocation.

## Related Wiki records

- `[[crypto-short-horizon-prediction-market-settlement-push-reversal-2026-09-01]]` — Spot order-flow manipulation during short-horizon binary contract settlement.
- `[[polymarket-negrisk-executable-arbitrage-token-conversion-2026-09-03]]` — Static combinatorial complete-basket token conversion on NegRisk CTF adapter.
- `[[kalshi-prediction-market-pricing-wedge-executable-spread-falsification-2026-09-13]]` — Execution costs, bid-ask spread, and fee falsification of prediction market pricing wedges.
- `[[crypto-prediction-market-layered-informed-trading-skill-score-2026-09-01]]` — Layered informed trading and information leakage scores on Polymarket.
- `[[fifo-queue-partial-identification-l2-execution-sensitivity-2026-09-16]]` — Queue execution sensitivity and partial identification in order-book backtesting.

## Sources

1. **Maksym Nechepurenko**, *"Resolution Is Not Settlement, Part II: Protocol Finality and Observed Redemption on Polymarket"*, arXiv preprint `arXiv:2609.15373v1 [q-fin.TR, cs.CR, q-fin.CP]`, submitted September 14, 2026.
   - Stable URL: https://arxiv.org/abs/2609.15373
   - HTML Full Text: https://arxiv.org/html/2609.15373v1
   - PDF: https://arxiv.org/pdf/2609.15373v1
   - SSRN Working Paper: https://ssrn.com/abstract=7344081
2. **Maksym Nechepurenko**, *"Resolution Is Not Settlement, Part I: Oracle Adjudication and Semantic Governance on Polymarket"*, arXiv preprint `arXiv:2609.15368v1 [q-fin.TR, cs.CR, q-fin.CP]`, submitted September 14, 2026.
   - Stable URL: https://arxiv.org/abs/2609.15368
   - HTML Full Text: https://arxiv.org/html/2609.15368v1
   - SSRN Working Paper: https://ssrn.com/abstract=7344079
3. **Gnosis**, *Conditional Tokens Framework (CTF)* smart contracts repository, GitHub: https://github.com/gnosis/conditional-tokens-contracts
4. **Polymarket**, *UMA CTF Adapter* smart contracts repository, commit `8b76cc9e0d46c6f7450a0adb0ddc0f5b0568c9cc`, GitHub: https://github.com/Polymarket/uma-ctf-adapter
