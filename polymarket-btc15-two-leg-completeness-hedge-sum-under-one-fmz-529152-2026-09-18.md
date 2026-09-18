---
schema: strategy-research-record-v1
title: "Polymarket BTC 15-Minute Two-Leg Completeness Hedge (Up+Down Sum < 1)"
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - bitcoin
  - polymarket
  - prediction-market
  - binary-arbitrage
  - completeness
  - two-leg-hedge
  - event-contract
  - negative-evidence
  - fmz
status: research-only
confidence: medium
source_as_of: 2026-09-18
sources:
  - "FMZ Quant strategy platform, Polymarket BTC 15分钟 两腿对冲套利机器人 (双向对冲版), strategy id 529152, author ianzeng123, created 2026-02-25, page last modified approx. 6 months before capture; inspiration credited to @the_smart_ape. https://www.fmz.com/strategy/529152"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Polymarket BTC 15-Minute Two-Leg Completeness Hedge (Up+Down Sum < 1)

## Provenance

Public FMZ strategy page: **Polymarket BTC 15分钟 两腿对冲套利机器人 (双向对冲版)**, strategy id `529152`, author ianzeng123. Canonical URL: https://www.fmz.com/strategy/529152. Created 2026-02-25; page last modified about six months before capture. Source credits inspiration to @the_smart_ape and requires FMZ hosted runtime ≥ 3.8.8. Source reviewed as of 2026-09-18 (public description, parameter table, state-machine snippet, and public comments).

Repository deduplication on current `main` found no record with FMZ id `529152` or the same normalized rule (buy both Polymarket BTC 15-minute Up and Down Yes contracts when combined ask cost < 1 USDC after a one-side dump trigger). Adjacent Polymarket records cover NegRisk token conversion, protocol-finality redemption carry, binary mean-reversion cost sensitivity, ETH LateAsk Chainlink displacement, HF lead-lag, and tri-transformer market-making — all different mechanisms.

## Economic mechanism

### Source-reported

Polymarket BTC 15-minute up/down contracts satisfy the **binary completeness identity** at settlement: exactly one side redeems 1 USDC, the other 0, so `Up + Down = 1` in payoff space. The strategy states that when one side is temporarily oversold on a short-horizon shock, the **sum of two asks** can print below 1 USDC:

```text
arb profit = 1 - leg1 fill price - leg2 fill price
```

Flow (source): monitor both asks → detect one-side dump beyond `MOVE_PCT` within `DUMP_WINDOW_S` → concurrently submit two limit orders targeting combined cost ≤ `SUM_TARGET` (< 1) → if both fill, wait for expiry Redeem (~840s after cycle in source notes; `INTERVAL` default 900s for 15-minute contracts) → if only one leg fills, cancel the other and enter single-leg risk controls.

Single-leg risk (source): absolute floor (`FLOOR_PRICE`) exit if bid ≤ floor; early take-profit (`EARLY_TAKE_PROFIT`) before the last N seconds; last-phase stop-loss (`LAST_MIN_STOP_LOSS`) in the final `LAST_MIN_S` (suggest 60s). If the cancelled leg unexpectedly fills during cancel confirmation, state upgrades to both-leg lock and skips flatten.

### Research interpretation

The economic channel is **transient binary mispricing under one-sided stress**, not directional BTC alpha. The hypothesis is that retail/order-flow shocks on one Polymarket leg can push `ask_up + ask_down` below 1 before arbitrageurs restore the completeness bound. Execution risk is **legging risk**: partial fills leave naked directional binary exposure into a 15-minute settlement.

Scout interpretation: public comments on the page are material negative context (see Evidence). This capture does not claim the opportunity is currently live.

## Signal

Source-specified reconstruction:

- Instrument: Polymarket BTC 15-minute Up/Down binary event contracts (paired market for one cycle).
- Formation/entry: within each ~15-minute cycle monitoring window (`WINDOW_MIN`); dump detection uses sliding `DUMP_WINDOW_S` and threshold `MOVE_PCT` (source example 0.15 = 15% one-side move).
- Entry: concurrent two-leg limits when dump trigger fires and target combined cost `SUM_TARGET` < 1 is achievable; first-leg slippage tolerance `SLIPPAGE`; order wait `ORDER_TIMEOUT_S`.
- Exit:
  - Both filled: hold to settlement Redeem (source auto-redeem ~840s after cycle start notes; poll redeemable positions).
  - One filled: cancel other; apply floor / early TP / last-phase SL; optional upgrade to both-leg if second fills during cancel.
- Holding period: minutes to settlement (target ~one 15-minute cycle).
- Parameters (source table): `SHARES` (min 5), `SUM_TARGET`, `MOVE_PCT`, `WINDOW_MIN`, `DUMP_WINDOW_S`, `SLIPPAGE`, `FLOOR_PRICE`, `EARLY_TAKE_PROFIT`, `LAST_MIN_STOP_LOSS`, `LAST_MIN_S`, `ORDER_TIMEOUT_S`, `SLEEP_MS`, `INTERVAL` (900).
- Market-neutral claim: source describes the both-filled path as not depending on BTC direction.

Underspecified: exact numeric defaults for several risk parameters beyond examples; fill model for concurrent limits; Polymarket fee schedule impact on net of `1 - sum_asks`.

## Required data

- Instrument: Polymarket BTC 15m Up/Down Yes contracts.
- Venue: Polymarket via FMZ exchange adapter.
- Timeframe: ~15-minute contract cycles; dump window in seconds.
- Fields: both-leg ask/bid/depth; order status; redeemable positions.
- Point-in-time: live book only; no historical reconstruction claimed.
- Costs: USDC balance ≥ `SUM_TARGET × SHARES`; fees not fully parameterized on the public page.

## Execution assumptions

Source-reported: concurrent limit submissions; blocking cancel-confirm polling; state machine `WATCHING / BOTH_PENDING / LEG1_ONLY / LEG2_ONLY / BOTH_DONE`; simulation recommended before live. FMZ hosted ≥ 3.8.8.

## Evidence

### Source-reported

FMZ page 529152 discloses the completeness identity, dump-triggered concurrent two-leg entry, single-leg risk stack, auto-redeem path, parameter surface, and a partial JavaScript state-machine header. The page positions the both-filled path as market-neutral.

Public comments on the same page (captured 2026-09-18) include:
- A user asking whether the strategy still works (~4 months before capture).
- A user reporting observed quotes such as Up 52 + Down 49 = 101 (~6 months before capture).
- Author reply (~6 months before capture): bid and ask prices generally sum above 1, **no arbitrage space**.

These comments are source-page community statements, not independently verified market snapshots.

### Independently reproduced

not independently reproduced

### Negative evidence

Author-stated and commenter-stated **current absence of sum<1 opportunities** is recorded as negative evidence against treating this as a standing live edge. Adjacent repository records already document cost sensitivity and finality friction on Polymarket binaries; those raise the prior that naive completeness arb is rare or cost-eroded. Absence of opportunities in comments is not a formal statistical study.

## Falsification

Research-proposed falsification tests (not executed):

1. Opportunity census: reconstruct full ask_up+ask_down time series over a held-out month of BTC 15m cycles; research-defined falsification threshold: fail as a standing alpha if the fraction of cycles with executable sum < 1 after fees is ~0, or net expected value ≤ 0 after single-leg unwind costs.
2. Legging stress: simulate one-leg fill rates under dump windows; fail if single-leg loss expectancy exceeds both-leg locked profit frequency × profit.
3. Fee/slippage stress: add Polymarket fees + adverse selection on the dumped leg; fail if net arb ≤ 0 whenever sum < 1 gross.
4. Latency stress: delay second leg by realistic RTT; fail if second-leg miss rate dominates.
5. Settlement integrity: confirm Up/Down always partition BTC 15m outcome under platform rules; fail if rule changes break completeness.
6. Placebo dumps: randomize trigger times; fail if real dump triggers show higher sum<1 incidence than placebo.
7. Capacity: scale `SHARES`; fail if book depth cannot support claimed size at sum < 1.

## Crypto portability

Mark: **direct for crypto event contracts; unproven beyond Polymarket BTC 15m**.

- Already on Polymarket BTC 15-minute crypto binaries.
- Completeness identity is venue/rule-specific, not portable to non-partition markets.
- No funding rate; capital locked until Redeem.
- Crypto portability is not authorization to trade.

## Limitations

- Public description + comments only; full source gated.
- `not independently reproduced`.
- Opportunity may be structurally absent in current books (author comment).
- Single-leg risk can dominate rare both-leg locks.
- Fees, latency, and depth can erase theoretical 1−sum.
- Related NegRisk/finality records answer different questions — not duplicate updates.
- Incremental-write threshold: met via distinct binary completeness mechanism + author/comment negative evidence on live opportunity scarcity.

## Implementation status

`not-implemented`. No runtime change; no Wiki Brain write; third-party FMZ code not endorsed.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

## Related Wiki records

- `polymarket-negrisk-executable-arbitrage-token-conversion-2026-09-03.md`
- `polymarket-protocol-finality-redemption-latency-carry-arbitrage-falsification-2026-09-16.md`
- `polymarket-binary-mean-reversion-cost-sensitivity-2026-09-14.md`
- `polymarket-eth15-lateask-chainlink-displacement-fmz-545782-2026-09-18.md`
- `crypto-cross-platform-binary-threshold-mispricing-polymarket-binance-2026-09-01.md`

## Sources

- FMZ Quant, Polymarket BTC 15-minute two-leg hedge, https://www.fmz.com/strategy/529152 (description, parameters, public comments; captured 2026-09-18).
