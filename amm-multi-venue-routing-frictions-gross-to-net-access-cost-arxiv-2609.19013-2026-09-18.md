---
schema: strategy-research-record-v1
title: "AMM Multi-Venue Routing Frictions: Gross-to-Net Executable Liquidity Compression"
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - defi
  - amm
  - routing
  - execution-cost
  - fragmentation
  - ethereum
  - base
  - negative-evidence
  - falsification
  - market-structure
status: research-only
confidence: medium
source_as_of: 2026-09-18
sources:
  - "Wen-Ting Wang, 'Routing Frictions and Executable Liquidity in Fragmented Markets', arXiv:2609.19013v2 [stat.CO; q-fin.ST], submitted 2026-07-18, last revised 2026-09-17. https://arxiv.org/abs/2609.19013"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# AMM Multi-Venue Routing Frictions: Gross-to-Net Executable Liquidity Compression

## Provenance

Academic preprint: Wen-Ting Wang, **Routing Frictions and Executable Liquidity in Fragmented Markets**, arXiv:2609.19013v2 [stat.CO; cross-list q-fin.ST]. v1 submitted 2026-07-18; v2 revised 2026-09-17 (title/manuscript revision). DOI: https://doi.org/10.48550/arXiv.2609.19013. Canonical URL: https://arxiv.org/abs/2609.19013. Source reviewed as of 2026-09-18.

Repository deduplication on current `main` found no record with arXiv id `2609.19013` or the same normalized claim (transaction-level AMM access costs eliminate the large majority of gross multi-venue execution gains on Ethereum/Base). Adjacent records include `defi-amm-routing-suboptimality-bisection-split-loss-2026-09-02.md` (algorithmic routing suboptimality/split-loss — different question), CEX–DEX latency arb families, and general LVR/AMM LP records. This capture adds **execution-cost / negative evidence** for multi-pool routing alpha, not a new entry/exit trading signal.

## Economic mechanism

### Source-reported

The paper argues that public blockchains make many venues simultaneously visible and mechanically reachable, yet activating each additional venue has a cost: connectivity ≠ economically integrated execution. AMM pools make the gross-to-net gap measurable because pre-trade venue states, transaction-level routing costs, and realized venue use can be reconstructed from public chain records.

Sample and headline measurements (source-reported abstract figures):

- 13,768 sampled family-transactions from 29 Ethereum and Base token-pair families and 71 sibling pools.
- Equal-chain **lower bound on gross multi-venue gains: 34.85%**.
- Corresponding **upper bound after measured access costs: 6.89%**.
- Access costs **eliminate 80.45%** of point-identified states with positive gross gains.
- Actual multi-pool activation occurs in only **1.203%** of the opportunity population.
- Among 170 eligible realized integrated routes, observed allocation captures **94.8%** of aggregate feasible gain.
- Counterfactual: holding recipient orders and exact venue states fixed, replacing Ethereum’s routing-cost regime with Base’s lower-cost regime materially expands executable integration.

Source implication: blockchain scaling, cross-venue connectivity, and displayed liquidity do not by themselves establish economically integrated execution; integration is an **order-specific property** that depends on transaction-level access costs.

### Research interpretation

For alpha research this is primarily **falsification / cost evidence**, not a long/short signal. The reconstructable research hypothesis is:

> Multi-venue AMM routing or cross-pool arbitrage strategies that size opportunities on **gross** price/liquidity differences will systematically overstate net edge once transaction-level access costs (gas, priority fees, approval/route activation, latency-related costs) are applied; on the studied Ethereum/Base population, most gross-positive states are not net-positive.

Scout interpretation only: the 80.45% elimination rate is population- and cost-regime-specific (Ethereum vs Base gas conditions, sample period, pair families). It is not a universal constant for all DEX routing strategies. The high 94.8% capture among rare realized integrated routes suggests that when integration is actually attempted on eligible orders, allocation quality may be less binding than **whether the order pays to integrate at all**.

This record does **not** promote a new trading rule. Its incremental value is a source-backed cost constraint that any future multi-venue AMM alpha hypothesis must clear.

## Signal

Not a directional trading signal. Research-normalized evaluation construct implied by the paper:

- Formation: for a candidate order/pair family, observe pre-trade states across sibling AMM pools at decision time (public chain reconstructable states).
- Gross opportunity: lower-bound measure of multi-venue gains absent access costs (source reports 34.85% equal-chain lower bound on the studied population — not a per-trade signal threshold).
- Net opportunity: same states after measured transaction-level access costs (source upper bound 6.89%).
- Decision rule for future research (research-proposed, not source-trading-rule): treat a multi-venue route as research-plausible only if **net** (post measured access costs) gain remains positive under the cost regime of the target chain; do not size on gross spreads.
- Source-reported activation statistic: multi-pool activation only 1.203% of opportunity population — rare conditional on gross opportunity set.

Underspecified for mechanical trading reconstruction: exact gas/priority fee series used in the paper’s cost measure; exact definition of “family-transaction” and sampling frame; full algorithm for the equal-chain lower bound; code/data snapshot path beyond arXiv materials.

## Required data

- Instrument: Ethereum and Base AMM pools for sampled token-pair families (29 families, 71 sibling pools per source).
- Universe: public on-chain AMM pool states and transactions — not CEX books.
- Venue: Ethereum L1 and Base (source comparative cost regimes).
- Timeframe: paper sample period not stated in the abstract; treat as unknown without full PDF read — do not invent dates.
- Fields: pre-trade pool reserves/prices, routing path, transaction-level access costs (gas/priority/related), realized venue use, recipient order sizes.
- Point-in-time: paper emphasizes reconstructability from public blockchain records; Scout did not independently rebuild the dataset.
- Timestamp: block timestamps.
- Missing-data / costs: access costs are the paper’s central variable; exact fee taxonomy beyond “transaction-level access costs” is abstract-level only.

## Execution assumptions

Source-reported focus is measurement of gross vs net multi-venue opportunity and realized routing frequency, not a fill simulator for a retail bot. No Scout fill model is asserted. For any future crypto routing hypothesis, execution assumptions must include gas, priority fees, route activation, failed-tx risk, and latency — the paper’s qualitative point.

## Evidence

### Source-reported

arXiv:2609.19013v2 abstract reports the 34.85% gross lower bound, 6.89% post-cost upper bound, 80.45% elimination of gross-positive states by access costs, 1.203% multi-pool activation rate, 94.8% gain capture among 170 eligible realized integrated routes, and the Ethereum→Base lower-cost counterfactual. Comments note a revised title/manuscript at v2. Full tables/figures and methodology details live in the PDF/HTML full text; this Scout cycle used the public abstract page.

### Independently reproduced

not independently reproduced

### Negative evidence

The paper **is** negative/execution-cost evidence against naive gross multi-venue AMM routing alpha on the studied Ethereum/Base population. Related repository CEX–DEX and AMM records already treat latency, gas, and LVR as cost channels; this record strengthens that family with a specific measured gross-to-net compression statistic. No contrary public study claiming high net multi-venue AMM routing edge on the same cost-regime sample was identified in this cycle’s abstract-level review. Absence of other studies is not evidence that net edge is always negative on other chains or periods.

## Falsification

Research-proposed falsification tests for any multi-venue AMM routing hypothesis that claims net edge (not executed here):

1. Cost-regime replication: recompute gross vs net multi-venue gains on an independent Ethereum/Base period; research-defined falsification threshold: if post-access-cost net gains remain positive on ≥50% of gross-positive states under measured costs, the paper’s strong compression claim does not transfer to that period — record must be updated rather than reused as universal negative.
2. Chain transfer: same measurement on a low-cost L2 or alt-L1; if net opportunity is large there, portability of routing alpha is chain-specific — do not generalize Ethereum compression to all venues.
3. Fee decomposition ablation: remove priority fees vs base gas vs approval costs one at a time; fail a “gas-only” narrative if a single non-gas component drives most elimination.
4. Capacity stress: scale recipient order size; fail small-order edge claims if net gain dies at realistic size.
5. Placebo pools: permute pool labels within families; fail if gross-to-net gap is an artifact of pool identity coding.
6. Realized-route audit: among integrated routes, test whether 94.8% capture holds out-of-sample; fail allocation-quality claims if later samples show systematic under-capture.
7. Competing explanation: if net multi-venue edge appears only when one pool is stale/oracle-lagged, attribute to oracle lag rather than routing skill.

Each test needs a pre-declared failure rule; unconstrained retuning counts as falsification.

## Crypto portability

Mark: **direct for the measurement claim; unproven for trading portability**.

- Spot AMM pools on Ethereum/Base — not perpetuals, options, or CEX order books.
- 24/7 chain timestamps; gas markets are continuous but regime-dependent.
- No funding rate on AMM pools; cost is gas/priority/opportunity.
- Fragmentation is the paper’s subject: multiple sibling pools per pair family.
- On-chain dependency: public pool states and transaction traces.
- Portability of the **cost lesson** to other DeFi routing is qualitative; portability of the **34.85%/6.89%/80.45% numbers** is not established outside the sample.
- Crypto portability is not authorization to trade.

## Limitations

- Abstract-level capture this cycle; full PDF methodology, sample dates, and robustness checks not independently audited here.
- `not independently reproduced`.
- Cost regimes (especially Ethereum gas) change; 80.45% is not a physical constant.
- Measurement paper — does not provide a complete retail entry/exit strategy.
- Adjacent routing-suboptimality record answers a different question (split loss vs access-cost compression).
- Do not use this record to reject all DEX arb research; use it to demand net-of-access-cost evidence.

Incremental-write threshold: met as new execution/cost and negative-evidence capture for multi-venue AMM routing, with distinct mechanism (gross-to-net access-cost compression) vs algorithmic routing-suboptimality records.

## Implementation status

`not-implemented`. Research capture only; no runtime change; no Paper/Testnet/Live authorization; no Hermes Wiki Brain write.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. This record is a cost/falsification constraint for future hypotheses, not an adopted strategy.

## Related Wiki records

- `defi-amm-routing-suboptimality-bisection-split-loss-2026-09-02.md` — different mechanism (routing path suboptimality).
- `crypto-cex-dex-arbitrage-subsecond-latency-risk-compression-2026-09-01.md` and related CEX–DEX cost records — adjacent latency/cost context.
- `defi-amm-impermanent-gain-zone-fee-floor-lp-arbitrageur-symbiosis-2026-09-18.md` — LP fee-floor symbiosis, not multi-venue access-cost measurement.
- `crypto-amm-loss-versus-rebalancing-lvr-toxic-arbitrage-2026-08-31.md` — LVR toxic flow, complementary but different cost channel.

No Hermes Wiki Brain write was performed.

## Sources

- Wang, W.-T., arXiv:2609.19013v2, https://arxiv.org/abs/2609.19013 (abstract and metadata; captured 2026-09-18).
