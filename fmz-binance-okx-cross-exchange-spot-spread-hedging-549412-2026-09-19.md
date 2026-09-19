---
schema: strategy-research-record-v1
title: "Binance / OKX Cross-Exchange Spot Spread Hedging (Inventory-Prepositioned Convergence)"
created: 2026-09-19
updated: 2026-09-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-exchange
  - spot-arbitrage
  - spread-convergence
  - binance
  - okx
  - inventory
status: research-only
confidence: low
source_as_of: 2026-09-14
sources:
  - "FMZ strategy page: 'Binance / OKX Cross-Exchange Spot Spread Hedging Strategy', created 2026-09-14, author ianzeng123. https://www.fmz.com/strategy/549412"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Binance / OKX Cross-Exchange Spot Spread Hedging (Inventory-Prepositioned Convergence)

## Provenance

- **Source URL**: https://www.fmz.com/strategy/549412
- **Source type**: Public FMZ strategy page (Common strategy). Full JavaScript source is login-gated; this capture uses only the publicly visible description, parameters, validation notes, and a short public code banner.
- **Author on page**: ianzeng123 (FMZ community author; same page-author neighborhood as FMZ 549380 Robinhood LP and 548617 meme rotation, but **different mechanism**)
- **Platform**: FMZ / 发明者量化
- **Created (source-reported)**: 2026-09-14 10:38:17
- **Venues**: Binance spot + OKX spot
- **Source reviewed as of**: 2026-09-19
- **Deduplication audit (2026-09-19)**: Repository-wide search found **zero** prior records citing FMZ id `549412` or this exact Binance/OKX inventory-prepositioned spot spread workflow. Adjacent records are related families, not duplicates:
  - Academic cross-exchange **spot** arbitrage (Makarov & Schoar lineage) — research paper on spatial price gaps; not this FMZ operational workflow.
  - `funding-adjusted-cross-exchange-perp-price-space-arb-ou-s-score-illiquidity-guards-2026-09-12.md` — **perpetual** price-space arb after funding normalization; different market type and signal.
  - FMZ 549380 Robinhood Chain V3/V4 LP fee-cost screen — DEX LP inventory, not CEX dual-leg spot spread.
  - FMZ 545792 EWY three-leg pairs / 546626 TradFi matrix — stock-perpetual relative value; different instruments.
  - CEX–DEX latency / MEV families — different mechanism (latency vs prepositioned inventory spread).

## Economic mechanism

### Source-reported

The strategy monitors Binance and OKX spot markets simultaneously. It buys the same asset on the lower-priced exchange and sells it on the higher-priced exchange, then reverses both legs when the two prices move closer together.

Source-reported notice: the strategy is provided only as a reference for design and code testing. A cross-exchange price gap does **not** guarantee realizable profit. Asset-transfer routes must be verified and the full workflow should be tested with small live positions before production use.

Source-reported entry prerequisites: (1) the asset can be bought on the lower-priced exchange, (2) inventory is available for sale on the higher-priced exchange, and (3) both legs can ultimately be exited. Identical asset names do not guarantee cross-exchange transferability; different supported networks or asset mappings can cause a spread to persist and prevent completing an arbitrage cycle via ad-hoc transfer.

Source-reported operational constraint: spot assets cannot be sold without available inventory. Before entry, the asset must be **pre-positioned** on the exchange that may become the higher-priced side, while quote currency must be available on the lower-priced side. The public code banner states the program does **not** transfer coins across chains and does **not** short spot out of thin air.

Source-reported validation status: JavaScript syntax checks and offline tests covering spread direction, top-ten ranking, interactive parameter parsing, and position-quantity calculations. Status tables, market APIs, and interactive buttons are implemented for a full FMZ live strategy. **A complete small-size live entry-to-exit cycle on Binance and OKX has not yet been completed** (source-reported as of the public page on 2026-09-19). Exchange-specific minimum order rules, account modes, API limits, partial-fill recovery, and final costs still require live validation. Displayed live notional exposure is not equivalent to net profit after all costs.

### Research interpretation

This is an **inventory-prepositioned two-venue spot basis-convergence** hypothesis, not a transfer-arbitrage bot and not a directional signal.

Hypothesized mechanism (research interpretation):

1. **Temporary quote dislocation:** Same asset quotes on Binance and OKX can diverge due to fragmented order flow, regional demand, listing/news timing, or inventory shocks on one venue.
2. **Convergence trade with dual inventory:** If both legs can be entered without relying on cross-exchange withdrawal latency, the position is short the expensive venue and long the cheap venue until the spread compresses toward the exit threshold.
3. **Transferability as a hard gate:** Persistent gaps may be **untradeable** rather than alpha when networks/mappings differ — the source correctly treats this as a prerequisite check, not an afterthought.
4. **Cost blindness of raw thresholds:** Default entry/exit spreads are user-set and the source states they do **not** automatically deduct fees; any research use must treat 3%/0.5% as gross thresholds requiring a research-proposed fee/slippage buffer.

This is **not** evidence that Binance–OKX spot spreads are systematically profitable after costs. Academic literature and the source's own incomplete live validation leave net profitability **unproven**.

Component roles (normalized):

```text
Universe: spot instruments listed on BOTH Binance and OKX, quote USDT (default)
Signal: executable bid/ask spread between venues (Binance higher vs OKX higher)
Entry gate: pre-positioned base inventory on potential high side + quote on low side + transferability/exit feasibility check
Entry trigger (source-reported default): entry spread ≥ 3%
Execution: batch market/limit orders both legs; limit-price buffer 0.2%; batch size default 20 USDT
Exit trigger (source-reported default): exit spread ≤ 0.5%; reverse both legs
Risk ops: prioritize lagging leg if one side fills; max 5 active plans; abnormal-spread and turnover warnings
```

## Signal

### Formation timestamp

Research interpretation from public description: quotes are refreshed on a scan cadence (source-reported default `scan_interval` **3000 ms**) via FMZ `GetTickers()` after `GetMarkets()` builds the intersection universe. Signal becomes actionable when the user-selected instrument's executable spread reaches the entry threshold **and** inventory/preconditions are satisfied. Exact clock source, timezone, and whether decisions use same-millisecond both-leg quotes are **not specified** (`underspecified`).

### Lookback

No historical lookback window is used for signal formation. The construction is **cross-sectional at a point in time** across the common-market list. Top-N ranking is by current executable spread (default display size **10**), not by historical z-scores.

### Entry

Source-reported workflow:

1. `GetMarkets()` on both exchanges; keep instruments supported on **both** sides and settled in the selected quote asset (default **USDT**).
2. `GetTickers()` best bid/ask in batches; compute executable spreads both directions ("Binance higher", "OKX higher").
3. Rank candidates largest → smallest; display top 10 with quotes, proposed direction, estimated turnover, and risk warnings.
4. Instruments above abnormal-spread warning or below turnover warning remain visible but are **not** automatic recommendations.
5. User selects instrument and sets: entry spread, exit spread, notional per leg, batch size.
6. When entry condition is reached: sell in batches on the higher-priced exchange and buy in batches on the lower-priced exchange.
7. Preconditions (source-reported): asset buyable on low side; inventory sellable on high side; both legs exitable; transferability not assumed from ticker equality.

### Exit

Source-reported:

- During holding, display entry spread, exit spread, filled quantity per leg, balances, matched position size, live notional.
- If one leg fills and the other does not, prioritize the lagging leg to reduce unhedged exposure.
- After both legs match, monitor; when exit spread falls to the configured threshold, sell on the original lower-priced exchange and buy back on the original higher-priced exchange.
- **No fixed holding deadline.** User can force exit, pause, or resume. Plans persist; restart during entry/exit pauses the plan until balances are reviewed.

### Holding period

Variable; source reports no fixed deadline. Expected horizon is the time for cross-venue quotes to converge — could be minutes to hours; not source-quantified.

### Parameters (source-reported defaults on public page)

| Parameter | Default | Purpose |
|-----------|---------|---------|
| Quote asset | USDT | Common spot settlement quote |
| Ranking size | 10 | Display largest executable spreads |
| Scan interval | 3000 ms | Refresh quotes/plans/positions |
| Default entry spread | 3% | Start entry when spread reaches this value |
| Default exit spread | 0.5% | Start exit when spread falls to this value |
| Default notional per leg | 100 USDT | Planned amount each exchange |
| Default batch size | 20 USDT | Each batch order size |
| Limit-price buffer | 0.2% | Improve limit-order fill probability |
| Maximum active plans | 5 | Concurrent instruments |
| Turnover warning level | 100,000 USDT | Flag low-turnover names |
| Abnormal-spread warning | 50% | Flag unusually large spreads |

Source-reported caveats on parameters: actual order size remains subject to balances, minimum quantity, minimum notional, and precision rules on both exchanges. **Entry and exit thresholds do not automatically deduct fees**; fee and execution allowances must be included when setting them (source-reported). Any specific fee buffer chosen by researchers is **research-proposed**, not source-reported.

Exact historical default for inventory warm-up size, quote-currency buffer, and whether the 3%/0.5% thresholds are mid, last, or bid-ask based are **underspecified** on the public page beyond "executable spreads" language.

### Position sizing

Fixed planned notional per leg (default 100 USDT) with batch child orders (default 20 USDT). Not volatility-scaled. Capacity not claimed.

### Multi-timeframe dependencies

None; single scan cadence.

### Specification completeness

**Partially specified.** Core dual-leg convergence rule, defaults, and inventory prerequisite are public. Full source, exact spread formula (mid vs touch), fee model, and live fill behavior are not public without login / not yet live-validated. Do not treat as a complete executable blueprint.

## Required data

- **Instrument / universe:** Spot pairs listed on **both** Binance and OKX, quote USDT (default). Intersection built via exchange market APIs.
- **Venue:** Binance spot + OKX spot simultaneously.
- **Market type:** Spot (not perpetual). No shorting without inventory.
- **Fields:** Best bid/ask both venues; market listing metadata; account balances on both sides; min qty/notional/precision; optional turnover estimate for warnings.
- **Point-in-time:** Live dual-venue quotes at scan time; no research panel dataset published with the strategy page.
- **Timestamp:** Not specified on public page (research gap).
- **Missing-data:** If one venue lacks the market, instrument is excluded from common list. Partial fills and restart handling described operationally but null-quote policy not detailed.
- **Funding/fee/spread:** Maker/taker fees, spread, and slippage **must be estimated by the user**; source explicitly does not auto-deduct fees from thresholds. Withdrawal/transfer costs are out of scope because the design is prepositioned inventory, not transfer arb.

## Execution assumptions

Source-reported / implied:

- Dual-leg batch execution; limit-price buffer 0.2% default; lagging-leg prioritization on partial hedge.
- Inventory prepositioned; no on-the-fly cross-exchange transfer.
- Max 5 concurrent plans; interactive user selection of instrument and thresholds.
- Offline tests only for logic; **live two-venue entry-exit cycle not completed**.

Not established (must not upgrade to facts):

- Realistic fill rates under latency and API limits
- Whether 3% entry spreads survive taker fees on both legs plus any rebalancing of inventory
- Cross-venue inventory drift management over multiple trades
- Capacity, MEV-like latency competition between faster bots, or adverse selection on the lagging leg
- Account mode / regional access constraints on OKX vs Binance

Research-proposed notes:

- Any fee-aware threshold (e.g., require spread ≥ fees_long + fees_short + buffer) is **research-proposed**.
- Any automated transfer-arbitrage extension contradicts the source design and would be a **different** strategy identity.

## Evidence

### Source-reported

- Offline/syntax tests for spread direction, top-10 ranking, parameter parsing, position math (source-reported on https://www.fmz.com/strategy/549412 as of 2026-09-19).
- Explicit source-reported negative/validation gap: complete small-size live entry-to-exit cycle on Binance and OKX **not yet completed**; costs and exchange microstructure rules still need live validation.
- Explicit source-reported caution: cross-exchange price gap does not guarantee realizable profit; transferability must be verified.
- **No Sharpe, win rate, or net-of-cost performance series is published.** This record claims no quantitative profitability figure.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- Source-reported: live cycle incomplete; displayed notional ≠ net profit; fee-unaware thresholds.
- Source-reported structural risk: same ticker ≠ transferable asset; spreads can persist for untradeable reasons.
- Related research in-repo: funding-adjusted **perp** cross-exchange records and academic spatial-arb captures document that cross-venue dislocations often shrink after costs/latency — mechanism caution, not a replication failure of FMZ 549412 specifically.
- Author ecosystem note (not this strategy's PnL): the same FMZ page author publicly commented on the separate meme-momentum strategy (548617) that hard stable profitability is regime-dependent; that comment is **not** evidence about 549412 outcomes.
- No independent live audit of 549412 was found this cycle. Absence of live proof is not evidence of profit or loss.

## Falsification plan

Research-proposed tests (not executed; not authorized):

1. **Cost-aware realizability (research-defined falsification threshold):** On ≥30 completed dual-leg round trips that entered when raw spread ≥ 3% (source default), if median realized spread compression minus both-leg fees, spread, and rebalance costs is **≤ 0**, reject the hypothesis that the published default entry gate selects cost-positive convergence trades on Binance–OKX USDT spot in the tested sample.
2. **Placebo unfiltered universe:** Trade top spreads without turnover/abnormal warnings vs with warnings. If warning filters do not improve net outcomes, they are cosmetic.
3. **Touch vs mid robustness:** Recompute signals on bid-ask touch vs mid. If edge exists only on mid but not on executable touch, the signal is not tradable as stated.
4. **Inventory asymmetry stress:** Intentionally start with one-sided inventory and measure unhedged path PnL vs prepositioned baseline.
5. **Venue swap control:** Same rule on Binance–Bybit or OKX–Bybit common USDT spot lists. If Binance–OKX is not special after costs, venue pair choice is not a durable mechanism claim.
6. **Latency stress:** Delay second-leg submission by 100–500 ms in simulation. If fill asymmetry dominates, capacity is latency-limited rather than spread-limited.
7. **Action on failure:** Mark rejected for the tested regime; do not retune entry/exit thresholds without a new pre-declared rule.

## Crypto portability

**Portability: `direct` for crypto CEX spot venues; `unproven` for net profitability and for non-USDT quotes / additional venues.**

- Mechanism is crypto-native (fragmented CEX spot quotes).
- Portability risks:
  - **Fee schedules and VIP tiers** differ across venues/users; 3%/0.5% defaults are especially fragile after fees.
  - **Listing intersection** changes; many alts are not on both venues.
  - **Network/mapping differences** (source-acknowledged) can freeze convergence.
  - **Account access / regional restrictions** may block one venue.
  - **24/7** trading removes session gaps but does not remove inventory risk.
  - **Not portable as perp funding arb** — different cost structure; do not conflate with funding-adjusted perp records.
  - **Stablecoin quote effects** (USDT depeg or venue-specific premium) can create persistent “spreads” that are quote-asset artifacts.

Crypto portability is not authorization to trade.

## Limitations

- **underspecified:** exact spread estimator; fee buffer; inventory warm-up rules; live fill model.
- **not independently reproduced**
- **data gap:** full source login-gated; no public live equity curve; live cycle incomplete per source.
- **capacity / latency:** competing bots may compress spreads before slower participants; untested.
- **source quality:** FMZ community strategy page, not peer-reviewed; author explicitly frames incomplete validation.
- **mechanism generality:** cross-exchange spot convergence is a well-known family; incremental value of this capture is the **public operational rule set + inventory prerequisite + explicit unvalidated-live caveat**, not a novel economic discovery.
- **selection risk:** ranking by largest spread preferentially surfaces broken/untradeable pairs unless transferability and turnover gates work as intended.

## Implementation status

No implementation in our research stack. This capture does not modify NautilusTrader, PyBroker, or any quantitative runtime; it does not create a strategy family; it does not authorize Paper, Testnet, or Live execution.

`implementation_status: not-implemented`

Source-side (third-party only): FMZ author reports offline/syntax tests and explicitly **no completed live two-venue cycle** — that is source-reported status, not our verification.

## Adoption boundary

Research-only staging material. Presence here does **not** mean profitable, validated alpha, or approved for implementation, paper, testnet, or live trading.

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

## Related Wiki records

No stable Hermes Wiki Brain path is known for this FMZ capture at write time. Do not fabricate Wiki links.

In-repository related records for intake/dedup:

- `funding-adjusted-cross-exchange-perp-price-space-arb-ou-s-score-illiquidity-guards-2026-09-12.md`
- Academic spatial cross-exchange spot arb family (Makarov & Schoar lineage), if present on main
- `fmz-robinhood-chain-v3v4-active-pool-lp-fee-cost-coverage-549380-2026-09-19.md` — same FMZ page-author neighborhood, different venue/mechanism
- `crypto-cross-sectional-meme-momentum-funding-dynamic-rotation-2026-09-14.md` — same FMZ ecosystem, different mechanism (cross-sectional momentum+funding)

## Sources

1. FMZ Quant strategy page. "Binance / OKX Cross-Exchange Spot Spread Hedging Strategy." Author ianzeng123. Created 2026-09-14. https://www.fmz.com/strategy/549412 (public description, parameters, validation notes reviewed 2026-09-19; full source not accessed).
