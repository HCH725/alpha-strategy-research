---
schema: strategy-research-record-v1
title: "Binance Perpetual Delisting Event Short Base + Dynamic Short Grid (FMZ 535836)"
created: 2026-09-15
updated: 2026-09-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - binance
  - perpetual
  - delisting-event
  - event-driven
  - short-grid
  - liquidity-withdrawal
  - fmz
status: research-only
confidence: low
source_as_of: 2026-04-07
sources:
  - "FMZ strategy page and full Python source: '下架合约网格策略' (Binance delisting perpetual short-grid), created 2026-04-07, last modified ~2026-06. https://www.fmz.com/strategy/535836"
  - "Companion FMZ digest article: https://www.fmz.com/digest-topic/10945"
  - "Author FMZ user page (ianzeng123): https://www.fmz.com/user/5b5af9ca45caa814184d2e80e1b1cf66"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Binance Perpetual Delisting Event Short Base + Dynamic Short Grid (FMZ 535836)

## Provenance

- **Source URL**: https://www.fmz.com/strategy/535836
- **Companion article**: https://www.fmz.com/digest-topic/10945
- **Title (source)**: 币安下架合约空头网格策略 (Binance delisting-contract short grid)
- **Author**: FMZ community user `ianzeng123` (https://www.fmz.com/user/5b5af9ca45caa814184d2e80e1b1cf66)
- **Platform**: FMZ Quant; full Python source visible on the strategy page
- **Created / as-of**: 2026-04-07; last modified ~3 months before capture (2026-09-15). Capture date 2026-09-15.
- **Identity**: FMZ strategy URL + page as-of; no immutable Git commit SHA (FMZ artifact).
- **Related same-author family (not this record)**: TradFi matrix null-space (`gateio-tradfi-matrix-null-space-stat-arb-q-score-fshock-2026-09-15.md`) and EWY three-leg pairs are different mechanisms/venues.

## Economic mechanism

### Source-reported

The source claims that when Binance announces delisting of a USDT-margined perpetual, the market often shows a short-term crash followed by oscillating decline as holders exit and liquidity thins. The strategy aims to capture:

1. **Trend PnL** from a short base position opened after the delist signal is detected.
2. **Oscillation PnL** from a dynamic short grid that sells rebounds and covers on dips.

Detection is mechanical: poll Binance `fapi/v1/exchangeInfo` for `contractType=PERPETUAL` symbols ending in `USDT` whose `deliveryDate` is less than the perpetual default far-future sentinel `4133404800000` (and still in the future). That field flip is treated as the delist signal.

### Scout interpretation

The structural story is **forced exit + liquidity withdrawal**: longs/shorts who cannot or will not hold into a delisted/closed instrument create order-flow imbalance; market makers widen or step away; price path dependency is one-way toward closure. This is a **crypto-native event structure** (exchange delivery-date change), not a factor model.

The missing link (not proven by the source): not every delist coin dumps monotonically; some bounce hard. The source itself flags this. Without a published event-study of post-delist return paths, the short bias is a **research hypothesis**, not established evidence.

## Signal

### Formation / availability

- **Monitor**: every `MONITOR_INTERVAL = 15s`, HTTP GET `https://fapi.binance.com/fapi/v1/exchangeInfo`.
- **Trigger**: a USDT PERPETUAL with `deliveryDate < 4133404800000` and `deliveryDate > now_ms` that was not in the previous known set.
- On new symbols: **close all existing tasks first** (flatten), then re-allocate capital equally across the current delist set and initialize each task independently.
- No bar-close convention; continuous poll.

### Entry (per delist contract)

1. **Base short (market)**: `usdt = fund_per_task * BASE_SHORT_RATIO * LEVERAGE` (defaults: ratio 0.5, leverage 10). Market sell open; if position amount ≤ 0 after fill check, **skip that symbol**.
2. **Dynamic short grid**: range initially `[price * (1 - GRID_WIDTH_PCT), price]` (default width 10%). `GRID_COUNT = 10` equal-width cells. Grid capital: `fund_per_task * (1 - BASE_SHORT_RATIO) * 0.8 * LEVERAGE / GRID_COUNT` per cell.
3. For each cell with sell price ≥ current price: place limit short at upper grid level; on fill, place limit cover at the lower grid level of that cell.

### Exit

1. **Primary forced exit**: when remaining time to `deliveryDate` ≤ `FORCE_CLOSE_MINS` (default 60), cancel all orders and market-close all shorts (up to 10 attempts).
2. **Grid cell cover**: limit cover at cell lower bound after short fill (oscillation harvest).
3. **Range shift**: if price breaks below range low, shift the whole window down in steps of `SHIFT_STEP_PCT * price` (default 5%) while keeping width; if price breaks above high, shift up. Re-place remaining held contracts' cover at the new lowest cell as protection.
4. Manual/reset path: new delist batch flattens everything first.

### Holding period

Bounded by time-to-delist (hours to days after announcement). Force-close 60 min before `deliveryDate` is the hard time stop. Overlapping multi-symbol tasks allowed until a new batch forces flatten.

### Parameters (source defaults; fixed, not paper-tuned)

| Param | Default |
|---|---|
| LEVERAGE | 10 |
| GRID_WIDTH_PCT | 0.10 |
| SHIFT_STEP_PCT | 0.05 |
| GRID_COUNT | 10 |
| BASE_SHORT_RATIO | 0.5 |
| FORCE_CLOSE_MINS | 60 |
| MONITOR_INTERVAL | 15 s |
| POLL_INTERVAL | 1 s |
| FEE_RATE (declared) | 0.0003 one-way |
| PERPETUAL_END sentinel | 4133404800000 |

## Required data

- **Instrument**: Binance USDT-M perpetual futures only (`contractType=PERPETUAL`, symbol suffix `USDT`).
- **Venue**: Binance USDⓈ-M futures (`fapi.binance.com` exchangeInfo + FMZ exchange adapter).
- **Fields**: `deliveryDate`, contract metadata (precision, MinQty, CtVal), ticker Last, account equity/balance, short position amount/price/PnL, open orders.
- **Timeframe**: event timestamp (deliveryDate flip) + tick/1s grid polling.
- **Point-in-time**: deliveryDate change is observable in exchangeInfo with poll lag up to `MONITOR_INTERVAL`; no historical point-in-time deliveryDate archive is provided by the source.
- **Missing data**: failed HTTP → skip that monitor cycle; failed base short → skip symbol.
- **Funding / fees / spread**: FEE_RATE declared 3 bps; funding and slippage not modeled in source; near-delist liquidity collapse is acknowledged but not quantified.

## Execution assumptions

### Source-reported

- Market open for base short; limit for grid legs.
- Poll 1s for grid state machine; 15s for delist monitor.
- Multi-task: independent symbols; capital split equally among current delist set (80% of free balance).
- Force-close market buy-cover with 0.5% price buffer, up to 10 retries; residual after 10 retries is a manual warning.

### Scout interpretation

- Detection lag (up to 15s + HTTP) means the first dump may already be underway — entry is **chase**, not front-run.
- Near-delist, books thin; market covers and grid fills can slip hard; the 60-min force-close is a necessary but not sufficient liquidity guard.
- Default 10x leverage on event shorts is aggressive; research-proposed risk control would reduce leverage and size by pre-event volume/OI.

## Evidence

### Source-reported

- Page presents design + full source; **no published backtest equity curve, hit rate, or event-study table** on the strategy page.
- Author-stated risks: low event frequency; poll lag; not all delist names dump (rebound risk); extreme vol + high leverage → liquidation risk; worsening liquidity toward close; recommends profit targets / rebound stops beyond the force-close clock.
- Page metrics as of capture: ~303 hits, 13 copies, created 2026-04-07.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- None identified in the FMZ page; absence is not evidence of no negative result.
- **Research-proposed negative checks** (not source-reported): event study of post-announcement 1h/4h/24h returns across a historical Binance delist sample would likely show a non-trivial share of bounce/rally cases — the short-only bias must survive that split before any operational use.

## Falsification

Research-defined tests (not source-reported):

1. **Event-study short bias (primary)**  
   - Data: historical Binance USDT-M perpetual delist announcements with `deliveryDate` change timestamps; mark price path T0→T0+1h/4h/24h/until force-close.  
   - Metric: fraction of events with negative close-to-close return over the holding window; median and mean return; conditional on pre-event 24h vol and OI.  
   - **Research-defined falsification threshold**: if P(return < 0) ≤ 0.55 over the intended holding window after fees, reject the short-base premise. Action: do not run short-only; at most research a two-sided or filter-only design.

2. **Detection-lag stress**  
   - Delay entry by 15s/60s/5min after the deliveryDate flip in a walk-forward replay.  
   - If most of the dump is gone within the lag, the strategy is not implementable as written.

3. **Liquidity / fill stress**  
   - Impose taker fees + 5–20 bps slippage and partial-fill caps near delist.  
   - If net PnL of base+grid is non-positive under those costs, reject.

4. **Bounce regime placebo**  
   - Split events by whether price mean-reverted ≥ 3% after the first dump.  
   - Grid should contribute positively in bounce cases; if it only adds losses, the oscillation leg is not load-bearing.

5. **DeliveryDate integrity**  
   - Manually audit that `deliveryDate` flips are true delists (not data glitches); false positives would open shorts on live contracts.

## Crypto portability

**Direct** — the mechanism is already crypto-native (Binance USDT-M perpetual `deliveryDate`). Portability caveats:

- Other venues (OKX, Bybit, Gate) use different delist metadata; the poll predicate must be rewritten.
- Spot delists, futures-settlement-only delists, and “trading suspended” states are not the same event.
- 24/7 clock: force-close uses wall-clock minutes to `deliveryDate` (exchange local UTC convention assumed by Binance API).

Crypto portability is not authorization to trade.

## Limitations

- **No published performance or event-study evidence** — confidence **low**.
- **Poll-lag chase entry** after announcement.
- **Short-only bias unvalidated**; bounce risk acknowledged by author.
- **Liquidity death spiral** near close not modeled; force-close is a blunt instrument.
- **Leverage 10x default** is research-unsafe without sizing redesign.
- **Rare events** → low sample, high path variance; multi-symbol simultaneous delists may concentrate risk.
- FMZ community artifact; no immutable commit SHA; not peer-reviewed.

## Implementation status

- Published as FMZ automation source; **not implemented** in any production system reviewed here.
- **Not authorized** for Paper/Testnet/Live in nautilus-quant-system. This record does not modify NautilusTrader, create a strategy family, or authorize execution.

## Adoption boundary

`status = research-only`. `adoption = not-approved`. `approval_scope = research-only`.

Presence of this record means only that a public FMZ event-driven design was normalized with reconstructable trigger, entry/exit, data, and falsification tests. It is not adoption, implementation authorization, or permission for Paper/Testnet/Live.

## Related Wiki / repo records

- `crypto-perpetual-liquidation-cascade-*` records: liquidation-driven paths, not exchange-delist `deliveryDate` events.
- `crypto-dynamic-grid-trading-adaptive-boundary-resets-2026-09-02.md`: generic adaptive grid, not delist-event conditioned.
- No existing record in this repository uses Binance perpetual `deliveryDate` as the primary signal (searched 2026-09-15).

## Sources

1. FMZ strategy + source: https://www.fmz.com/strategy/535836 (captured 2026-09-15).
2. FMZ digest: https://www.fmz.com/digest-topic/10945
3. Author: https://www.fmz.com/user/5b5af9ca45caa814184d2e80e1b1cf66
4. Binance Futures API (referenced by source): `https://fapi.binance.com/fapi/v1/exchangeInfo`
