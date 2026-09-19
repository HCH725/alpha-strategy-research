---
schema: strategy-research-record-v1
title: "Robinhood Chain Uniswap V3/V4 Active-Pool LP Fee-Cost Coverage Screen"
created: 2026-09-19
updated: 2026-09-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - defi
  - amm
  - liquidity-provision
  - uniswap
  - robinhood-chain
  - fee-carry
  - concentrated-liquidity
status: research-only
confidence: low
source_as_of: 2026-09-13
sources:
  - "FMZ strategy page: 'Robinhood V3/V4 Active-Pool LP Strategy', created 2026-09-13, author ianzeng123. https://www.fmz.com/strategy/549380"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Robinhood Chain Uniswap V3/V4 Active-Pool LP Fee-Cost Coverage Screen

## Provenance

- **Source URL**: https://www.fmz.com/strategy/549380
- **Source type**: Public FMZ strategy page (Common strategy). Full JavaScript source is login-gated; this capture uses only the publicly visible strategy description, parameters, and validation notes.
- **Author**: ianzeng123 (FMZ community author)
- **Platform**: FMZ / 发明者量化
- **Created**: 2026-09-13 21:02:07 UTC (source-reported on the strategy page)
- **Venue**: Robinhood Chain Uniswap V3 / V4 concentrated-liquidity pools
- **Source reviewed as of**: 2026-09-19
- **Deduplication audit (2026-09-19)**: Repository-wide search found **zero** prior records citing FMZ id `549380`, "Active-Pool LP", or this exact fee-cost coverage rule. Adjacent records are materially different:
  - `defi-amm-impermanent-gain-zone-fee-floor-lp-arbitrageur-symbiosis-2026-09-18.md` — academic arXiv theory on IL vs fee profitability zones; not an operational FMZ screening rule on Robinhood Chain.
  - `amm-multi-venue-routing-frictions-gross-to-net-access-cost-arxiv-2609.19013-2026-09-18.md` — multi-venue AMM routing access costs; different question (router alpha vs LP fee carry).
  - FMZ strategy `548663` / digest-topic `11037` (Uniswap V4 New Pool Radar on Robinhood Chain) — **new-pool discovery / Initialize-event radar**, not a fee-vs-cost LP entry gate on already-active pools. Not captured in this repository as of this cycle; not treated as a duplicate of this record.
  - Existing pairs/stat-arb, funding, grid, Polymarket, and TradFi-perp records — different mechanisms.

## Economic mechanism

### Source-reported

The strategy provides liquidity to Uniswap V3/V4 pools that show sustained trading activity and sufficient liquidity on Robinhood Chain. Before entry it compares expected fee income against swap costs, slippage, gas, and an inventory-risk allowance. By default the author discounts estimated hourly fee income by 50% and requires the discounted figure to cover at least 1.5 times the estimated round-trip cost.

Pool candidates are periodically retrieved through paginated V3/V4 pool-directory APIs. The source reports screening ETH/WETH pairs by pool age, liquidity, trading volume, buy/sell activity, and price movement. Eligible pools then undergo on-chain identity, liquidity, and two-way quote checks. Capital starts in ETH, converts to WETH when necessary, and enters a concentrated liquidity position around the entry price.

Source-reported production configuration excludes new positions targeting USDG and accepts only hook-free pools with static fees.

Positions are monitored for net losses, price deviations, liquidity changes, and accumulated fees. There is no fixed holding deadline. Fee-income progress checks begin after 10 minutes; materially weaker-than-expected fee income can also trigger exit.

Source-reported validation status: small live tests completed full entry-to-exit cycles for both V3 and V4, verifying execution and fee accounting. The source explicitly states that long-term profitability remains unverified, that price movements and transaction costs may outweigh fee income, and that exit thresholds do not guarantee the final realized loss.

### Research interpretation

This is an **activity-premium concentrated-liquidity fee-carry hypothesis** on a new L2/app-chain DEX venue (Robinhood Chain Uniswap V3/V4), gated by an explicit **cost-coverage rule** rather than by directional price views.

Hypothesized mechanism (research interpretation, not source-proven alpha):

1. **Fee premium from sustained two-way flow**: Pools with continuous swap volume generate LP fee income that can dominate inventory loss over short holding windows, if entry is restricted to high-turnover pools.
2. **Conservative cost haircut as adverse-selection buffer**: Discounting estimated hourly fees by 50% before requiring ≥1.5× round-trip cost is a research-visible attempt to leave headroom for estimation error, IL, and inventory risk.
3. **Hard inventory and path risk caps**: Default 3% max net loss and 3% price-deviation exit bound markout/inventory damage; fee-progress checks after 10 minutes attempt to abandon pools that do not monetize flow quickly.
4. **Venue novelty**: Robinhood Chain activity surge (context also discussed in FMZ digest-topic 11037) may temporarily supply higher fee APY relative to mature Uniswap deployments on Ethereum/L2s; that premium is regime-dependent and not established by this page.

This is **not** a claim that concentrated LP is profitable. The source itself frames the work as execution/accounting verification plus a cost-coverage screen, not a validated yield strategy.

Component roles (normalized):

```text
Venue/universe: Robinhood Chain Uniswap V3/V4; ETH/WETH-focused activity screen
Regime/filter: pool age, liquidity, volume, buy/sell activity, price movement; hook-free + static fees; exclude USDG targets
Primary entry rule: discounted hourly fee income ≥ 1.5 × estimated round-trip cost (default haircut 50%)
Execution: convert ETH→WETH if needed; concentrated LP around entry price; budget 3 USD/position; max 1 concurrent position
Risk/exit: max net loss 3%; price deviation ±3% from entry; fee-progress check after ~10 min; liquidity-change / fee monitoring; no fixed holding deadline
```

## Signal

### Formation timestamp

Source does not publish an exact clock convention. Research interpretation: pool screens and cost/fee estimates are formed from live public pool/quote APIs and on-chain checks immediately before entry; the position is tradable after the LP mint transaction confirms. Timezone and publication lag are not specified on the public page.

### Lookback

Source-reported screening dimensions (pool age, liquidity, trading volume, buy/sell activity, price movement) are listed but **exact lookback windows and threshold values are not published** on the public strategy page. Hourly fee-income estimation window is also unspecified beyond the phrase "estimated hourly fee income".

**Signal is partially underspecified** for independent reconstruction of numeric thresholds.

### Entry

Source-reported entry logic:

1. Discover pools via paginated V3/V4 pool-directory APIs.
2. Screen ETH/WETH-related candidates on age, liquidity, volume, buy/sell activity, price movement.
3. Run on-chain identity, liquidity, and two-way quote checks.
4. Apply production filters: no new USDG-target positions; hook-free pools only; static fees only.
5. Compute estimated hourly fee income; apply default **50% discount**; require result **≥ 1.5 × estimated round-trip cost** (swap + slippage + gas + inventory-risk allowance).
6. If eligible and budget allows: convert capital ETH→WETH if needed; mint concentrated liquidity around the current entry price.
7. Default sizing: **3 USD total budget per position** (includes entry gas and execution allowance); **max 1 concurrent position**; new entries enabled by default.

### Exit

Source-reported exit triggers (any may fire; precedence not fully ordered on the public page):

- **Max net loss 3%** (source-reported default parameter)
- **Price deviation 3%** from entry, either direction
- Liquidity change in the pool
- Accumulated-fee / inventory monitoring
- Fee-income progress check starting after **~10 minutes**; materially weaker-than-expected fee income can trigger exit
- No fixed holding deadline

On exit: remove liquidity, collect fees, convert proceeds back to ETH (source-reported flow).

### Holding period

Variable. Source reports no fixed deadline; typical intended horizon is short (minutes to hours) implied by the 10-minute fee-progress check and tight 3% deviation/loss caps. Exact expected holding period is not source-reported.

### Parameters (source-reported defaults)

| Parameter | Default | Role |
|-----------|---------|------|
| Fee income haircut | 50% | Discount on estimated hourly fee income |
| Cost coverage multiple | 1.5× | Discounted fees must cover ≥1.5× estimated round-trip cost |
| Budget per position | 3 USD | Includes entry gas and execution allowance |
| Max concurrent positions | 1 | Capacity cap |
| Allow new entries | Enabled | Can freeze new entries while managing existing |
| Max net loss | 3% | Exit trigger |
| Price deviation exit | 3% | Exit trigger, either direction |
| Fee-progress check start | ~10 minutes | Early underperformance exit |
| Pool filters | hook-free, static fees; exclude USDG targets | Production config |

Exact numeric pool-screen cutoffs (age, liquidity, volume, activity) and the inventory-risk allowance amount are **not published** on the public page and are marked **underspecified**.

### Position sizing

Fixed small notional (3 USD default) rather than volatility- or fee-scaled sizing. Research interpretation: this is pilot/experimental sizing, not a capacity claim.

### Multi-timeframe dependencies

None explicitly reported beyond live pool statistics and hourly fee estimates.

### Specification completeness

**Partially specified.** Core cost-coverage inequality, default exits, and production pool filters are public. Numeric activity/liquidity thresholds, fee estimator formula, concentrated-range width, and full source are not public without FMZ login. Do not treat this record as a complete executable blueprint.

## Required data

- **Instrument / universe**: Uniswap V3/V4 LP positions on Robinhood Chain; source emphasizes ETH/WETH-related active pools; production excludes USDG-target new positions and non-static-fee / hooked pools.
- **Venue**: Robinhood Chain (DEX); FMZ as automation host.
- **Market type**: Spot AMM concentrated liquidity (LP inventory), not perpetual directional futures.
- **Fields**: pool directory (paginated), pool age, reserves/liquidity, swap volume, buy/sell activity, price/path movement, live two-way quotes, gas estimates, fee tier (static), hook status, on-chain pool identity.
- **Point-in-time**: live public chain/API state at decision time; no published historical dataset on the strategy page.
- **Timestamp**: not specified on public page (research gap).
- **Missing-data**: not specified; source requires identity/liquidity/two-way quote checks to pass before entry (fail-closed on check failure is implied but not spelled out as a null-handling policy).
- **Costs**: swap fees, slippage, gas, inventory-risk allowance must be estimated for the coverage test; source treats them as scenario estimates, not realized ledger truth.

## Execution assumptions

Source-reported / implied:

- Entry after screen + cost-coverage pass; mint concentrated LP around entry price.
- Exit via remove-liquidity + collect fees + convert to ETH.
- Small pilot budget; max one position.
- Live tests verified mechanical entry/exit and fee accounting on V3 and V4.

Not established by source (must not be upgraded to facts):

- Exact fill/gas model under congestion
- MEV/sandwich exposure on mint/burn
- Range width and rebalancing policy
- Capacity beyond 3 USD pilot size
- Whether 3% exit bounds are hit before fee accrual in adverse regimes
- Long-horizon net yield

Research-proposed operationalization notes (not source-reported):

- Any use of this rule outside the published defaults (different haircut, coverage multiple, universe beyond ETH/WETH active pools, larger size) is **research-proposed** and would require separate evidence.
- Reconstructing numeric pool-screen thresholds from the login-gated source would be required before any faithful independent implementation; this Scout cycle did not log in and did not recover the full source.

## Evidence

### Source-reported

- Small live tests completed full entry-to-exit cycles for both V3 and V4 on Robinhood Chain, verifying execution and fee accounting (source-reported on https://www.fmz.com/strategy/549380 as of 2026-09-19).
- Source explicitly states: long-term profitability remains unverified; price movements and transaction costs may outweigh fee income; exit thresholds do not guarantee final realized loss.
- No Sharpe, APY, win rate, or sample-size performance series is published on the public strategy page. **No quantitative profitability figure is claimed in this record.**

### Independently reproduced

`not independently reproduced`

### Negative evidence

- Source-reported caveat: profitability unverified; costs/IL may exceed fees; exit thresholds do not cap final loss.
- Full source is login-gated; independent reconstruction of numeric thresholds is blocked this cycle (data/provenance gap).
- Adjacent academic work (`defi-amm-impermanent-gain-zone-fee-floor-lp-arbitrageur-symbiosis-2026-09-18.md`, arXiv:2604.28014) argues LP profitability depends on fee vs IL zones — mechanism-aligned caution, not a replication of this FMZ rule.
- Adjacent routing-cost work (`amm-multi-venue-routing-frictions-gross-to-net-access-cost-arxiv-2609.19013-2026-09-18.md`) shows gross AMM gains can be largely eliminated by access costs — relevant to whether fee screens survive real costs on any venue.
- No independent Robinhood Chain fee-yield study was found in this cycle's public search.
- None of the above constitutes a failed replication of FMZ 549380 specifically; absence of a long public track record is not evidence of either profit or loss.

## Falsification plan

Research-proposed tests (not executed; not authorized):

1. **Cost-coverage realized test** (research-defined falsification threshold): On ≥30 completed LP cycles that passed the source-default screen (50% haircut, 1.5× coverage), if median realized fee income ÷ realized all-in costs (swap + gas + measured inventory/markout loss) is **< 1.0**, reject the hypothesis that the published coverage screen identifies fee-positive inventory in this venue/regime.
2. **Haircut stress**: Re-run entry decisions with haircuts of 0%, 50%, 75%. If realized net edge appears only at 0% haircut, the 50% default is not doing protective work (or the fee estimator is miscalibrated).
3. **Exit ablation**: Compare default exits (3% loss / 3% deviation / 10-min fee progress) vs fee-progress-only vs deviation-only. If 3% deviation exits dominate losses, inventory path risk — not fee carry — drives outcomes.
4. **Universe ablation**: ETH/WETH-only vs broader active pools; hook-free static-fee vs unrestricted. If unrestricted pools dominate reported fees but not net-of-IL returns, production filters are material.
5. **Placebo pool sample**: Enter randomly selected active pools without the fee-cost screen, same size/exits. If screened pools do not outperform placebo on net fee-minus-cost, the screen has no discriminative power.
6. **Venue control**: Same rule on a mature Uniswap v3 deployment (e.g., Ethereum or a deep L2) with matched pool activity. If Robinhood Chain advantage disappears after gas normalization, venue novelty rather than rule quality drives any observed edge.
7. **Action on failure**: Mark hypothesis rejected for the tested regime; do not retune thresholds to rescue without a new pre-declared rule.

## Crypto portability

**Portability label: `direct` for the venue family (already crypto-native), `unproven` for portability to other chains or pool types.**

- Mechanism and instruments are crypto-native (DEX LP on Robinhood Chain Uniswap V3/V4). This is not a TradFi→crypto port.
- Portability risks if copied elsewhere:
  - **Venue activity regime**: fee APY on a newer chain can collapse as incentives rotate; screen may only work in a temporary activity surge.
  - **Gas and finality**: Robinhood Chain gas/latency profile differs from Ethereum mainnet; 3 USD pilot budgets may be gas-dominated on expensive venues.
  - **Hook / fee-tier heterogeneity**: production filter (hook-free, static fees) may not map cleanly to other DEX versions or dynamic-fee pools.
  - **Inventory vs perpetual funding**: this is spot inventory LP, not funding-carry perps; do not conflate with perpetual funding strategies in this repository.
  - **MEV / sandwich**: concentrated mints and burns around public quotes are exposed to adverse selection not modeled on the public page.
  - **USDG and quote-currency effects**: source excludes USDG targets; other stablecoin pools may have different volume quality.

Crypto portability is not authorization to trade.

## Limitations

- **underspecified**: numeric pool-screen thresholds, fee estimator formula, range width, gas model, timestamp convention.
- **not independently reproduced**
- **data gap**: full source login-gated; no public backtest series or long live track record on the strategy page.
- **capacity**: default 3 USD / 1 position is pilot-scale; no capacity claim.
- **source quality**: FMZ community strategy page, not peer-reviewed research; author self-reports unverified profitability.
- **venue novelty bias**: Robinhood Chain fee premia may be temporary; results may not generalize.
- **selection on activity**: screening for volume/liquidity may select pools where inventory loss is also elevated (adverse selection), which the 50% haircut only partially addresses.
- Ordinary generic LP/grid content without this cost-coverage rule would not clear the incremental-write bar; this record exists because the published fee-cost inequality + Robinhood Chain V3/V4 venue + explicit unverified-profit caveat are specific and traceable.

## Implementation status

No implementation in our research stack has been completed. This capture does not modify NautilusTrader, PyBroker, or any quantitative runtime; it does not create a strategy family; it does not authorize Paper, Testnet, or Live execution.

`implementation_status: not-implemented`

Source-side status (for clarity only): FMZ author reports small live execution tests on V3/V4; that is **source-reported third-party activity**, not our implementation or verification.

## Adoption boundary

This record is **research-only**. Presence in this repository does **not** mean the strategy is profitable, validated alpha, approved for implementation, paper trading, testnet, or live trading.

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

Any later adoption decision must be explicit, separately reviewed, and based on this record plus current live sources.

## Related Wiki records

No stable Hermes Wiki Brain path is known for this FMZ capture at write time. Do not fabricate Wiki links.

In-repository related records (for future intake/dedup):

- `defi-amm-impermanent-gain-zone-fee-floor-lp-arbitrageur-symbiosis-2026-09-18.md`
- `amm-multi-venue-routing-frictions-gross-to-net-access-cost-arxiv-2609.19013-2026-09-18.md`
- `defi-amm-routing-suboptimality-bisection-split-loss-2026-09-02.md` (if present on main; routing suboptimality family)

## Sources

1. FMZ Quant strategy page. "Robinhood V3/V4 Active-Pool LP Strategy." Author ianzeng123. Created 2026-09-13. https://www.fmz.com/strategy/549380 (public description, parameters, and validation notes reviewed 2026-09-19; full source not accessed).
2. Related public context (not used for strategy rules): FMZ digest-topic 11037, "FMZ Web3 in Practice — Riding the Robinhood Chain Wave: Build a Uniswap V4 New Pool Radar Step by Step" (different mechanism: new-pool radar).
