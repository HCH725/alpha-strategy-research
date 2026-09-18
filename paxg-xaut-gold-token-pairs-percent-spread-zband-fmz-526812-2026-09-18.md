---
schema: strategy-research-record-v1
title: "PAXG–XAUT Gold-Token Pairs Stat-Arb: Percent-Spread Z-Band Mean Reversion"
created: 2026-09-18
updated: 2026-09-18
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - gold
  - paxg
  - xaut
  - pairs-trading
  - statistical-arbitrage
  - mean-reversion
  - market-neutral
  - tokenized-commodity
  - fmz
status: research-only
confidence: medium
source_as_of: 2026-09-18
sources:
  - "FMZ Quant strategy platform, 黄金代币统计套利策略框架 / Gold-token statistical arbitrage framework, strategy id 526812, author ianzeng123, created 2026-02-05, page last modified approx. 6 months before capture. https://www.fmz.com/strategy/526812"
  - "FMZ-linked demo video referenced on the strategy page: https://www.bilibili.com/video/BV1KzFmzwEZ6/ (provenance pointer only)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# PAXG–XAUT Gold-Token Pairs Stat-Arb: Percent-Spread Z-Band Mean Reversion

## Provenance

Public FMZ strategy page: **黄金代币统计套利策略框架**, strategy id `526812`, author ianzeng123. Canonical URL: https://www.fmz.com/strategy/526812. Created 2026-02-05; page last modified about six months before capture. Visible backtest header on page references Bybit `XAUT_USDT` futures-style market data for a short Jan–Feb 2026 window. Source reviewed as of 2026-09-18.

Repository deduplication on current `main` found no record with FMZ id `526812` or the same normalized rule (PAXG vs XAUT percent-spread mean±Nσ band entry, exit at entry-time mean). Adjacent record `crypto-volatility-aware-portfolio-drawdown-scaling-paxg-hedge-2026-09-04.md` uses PAXG as a **portfolio hedge sleeve**, not a two-token gold-pairs mean-reversion rule. Other crypto pairs/stat-arb records concern BTC/ETH, perp cointegration, or multi-asset residual families — different instrument pairs and not this gold-token construction.

## Economic mechanism

### Source-reported

The strategy targets the long-run co-movement of two **gold-pegged crypto tokens** — **PAXG** (Paxos Gold) and **XAUT** (Tether Gold). Both claim exposure to allocated gold, so the source assumes a stable relative pricing relationship and harvests temporary percent-spread dislocations.

Spread definition (source):

```text
spread = (price1 - price2) / price2 × 100%
```

Rolling window estimates mean μ and std σ of the percent spread; bands:

- Upper = μ + N×σ (default N=2)
- Lower = μ − N×σ

Entry (source table):
- spread > upper → short leg1 / long leg2
- spread < lower → long leg1 / short leg2
- Record current μ as **target reversion spread** at entry

Exit (source): close when spread reverts to the **entry-time mean** (not necessarily the rolling μ at exit).

Execution (source):
- Sequential two-leg market orders: fill leg1 first, confirm, then leg2
- If leg2 fails → flatten leg1 to avoid naked exposure
- Order timeout cancel

Risk/filters (source):
- Minimum volatility filter: skip if rolling σ too small
- Sample-size check: pause if window sample insufficient
- Manual commands: force flatten / clear data / refresh equity

Monitoring: live spread μ/σ/bands/z-score, position state, trade history, equity curve, spread distribution panel.

### Research interpretation

The economic channel is **tokenized-commodity basis dislocation**: two liabilities on the same underlying metal can diverge temporarily due to issuance/custody frictions, venue liquidity differences, redemption mechanics, or idiosyncratic flow — then mean-revert if both remain credible gold claims. The rule is classic residual/pairs mean-reversion on a **percent spread**, not a directional gold forecast.

Scout interpretation: incremental value is the **specific gold-token pair family** with a transparent z-band rule. Whether PAXG–XAUT spreads are stationary enough after fees is untested by this capture. Related falsification priors exist for crypto pairs cointegration overfit in the repository.

## Signal

Source-specified reconstruction (defaults from public page; some numerics underspecified):

- Instruments: PAXG and XAUT (page backtest header shows XAUT_USDT on a futures venue — spot vs perp venue mix should be treated as implementation detail to verify).
- Formation: rolling window on **minute-bar closes**; polling at second-scale per source text; statistic = percent spread as above.
- Lookback: rolling statistical window length **not stated as a numeric default on the public description** — mark underspecified; sample-size gate implies a minimum bar count.
- Entry: |z| band breach with N default 2; directional hedge as in table; both legs equal notionals not fully specified (pairs literature often equal-notional or beta-1 — page does not fully state).
- Exit: spread returns to **entry-recorded μ**.
- Holding period: open until reversion or manual/risk flatten; not a fixed clock.
- Parameters exposed conceptually: N (σ multiplier), window length, min σ filter, min samples, order timeout; exact defaults for window/min-σ not visible in the public blurb.

Underspecified for bit-exact replication: window length, equal-notional vs share hedge ratio, fee model, whether both legs are spot or mixed with perps, venue pair used live.

## Required data

- Instruments: PAXG, XAUT price series (crypto venues; gold-token claims).
- Universe: single pair.
- Venue: crypto exchange(s) listing both; page example Bybit XAUT_USDT-style market.
- Timeframe: minute closes for stats; second-scale quote polling.
- Fields: mid/close prices for both tokens; spread time series.
- Point-in-time: rolling window only; no alternative data.
- Funding/fees: not modeled as alpha input on the page; taker market orders on sequential legs — cost sensitivity material.
- Missing data: insufficient sample → pause; both venues must update.

## Execution assumptions

Source-reported: sequential market orders with timeout; flatten naked leg on second-leg failure; min-vol and min-sample gates; manual force-flat. No claim of maker fills or latency model. Fill risk between legs is acknowledged by the unwind path.

## Evidence

### Source-reported

FMZ page 526812 discloses the percent-spread z-band rule, entry/exit semantics, sequential execution and naked-leg unwind, min-σ/sample filters, monitoring panel, and a short platform backtest header (Bybit XAUT_USDT, 2026-01-28 to 2026-02-01, 1m period). A Bilibili demo video is linked from the page. No audited live PnL or academic study is claimed on the strategy page.

### Independently reproduced

not independently reproduced

### Negative evidence

No independent replication identified this cycle. Adjacent repository records document cointegration/pairs overfit and cost decay on other crypto pairs — relevant priors, not disproof of PAXG–XAUT specifically. Gold-token spreads can also **fail to mean-revert** if one token’s redemption/credibility regime shifts (structural break) — not quantified on the page. Absence of public live results is not evidence of profitability.

## Falsification

Research-proposed falsification tests (not executed):

1. Cointegration/stationarity audit on longer PAXG–XAUT history: research-defined falsification threshold: fail pairs premise if ADF/OU half-life is unstable across years or residual is near unit-root.
2. Walk-forward z-band vs buy-both-hold: fail if net-of-fees pairs edge ≤ 0 on held-out periods under N=2.
3. Fee/slippage stress: sequential taker both sides; fail if mean reversion profit < round-trip cost on typical |z| signals.
4. Window/N perturbation: fail if sign of net edge unstable across modest parameter moves.
5. Structural-break test: subperiod around major gold/redemption news; fail if a single break destroys all subsequent edge without re-fit (would imply non-stationary pair).
6. Hedge-ratio ablation: 1:1 price hedge vs beta-adjusted; fail if only one construction works and the other is advertised as general.
7. Venue stress: one leg on a thin book; fail if unwind-on-failure path dominates losses.
8. Placebo pairs: PAXG vs non-gold crypto; fail if gold-token pair is not more mean-reverting than random pairs.

## Crypto portability

Mark: **direct for gold-token pairs; unproven for other tokenized commodities**.

- Already crypto tokens on crypto venues; 24/7 continuous quotes.
- No perp funding required for spot-spot pairs; if one leg is a perp, funding enters.
- Mechanism depends on both tokens remaining credible claims on similar gold — not portable to arbitrary alts.
- Fragmentation: different exchanges may list only one token — transfer/settlement frictions can bind.
- Crypto portability is not authorization to trade.

## Limitations

- Public FMZ description only; full source gated; key numerics (window, hedge ratio) underspecified.
- `not independently reproduced`.
- Short illustrative backtest header is not research-grade evidence.
- Sequential taker execution likely cost-heavy vs theoretical spread.
- Structural break if one token depegs from gold claim quality.
- Adjacent PAXG hedge record is portfolio construction — not a duplicate update.
- Incremental-write threshold: met via new instrument family (PAXG–XAUT gold tokens) and explicit percent-spread band rule distinct from general crypto pairs records.

## Implementation status

`not-implemented`. No runtime change; no Wiki Brain write; third-party FMZ code not endorsed.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

## Related Wiki records

- `crypto-volatility-aware-portfolio-drawdown-scaling-paxg-hedge-2026-09-04.md` — PAXG as hedge sleeve, different mechanism.
- `crypto-pairs-trading-cointegration-overfitting-falsification-2026-09-13.md` and related pairs falsification records — methodological priors.
- `commodity-perpetual-oracle-roll-funding-arbitrage-2026-09-01.md` — different commodity-perp mechanism.

## Sources

- FMZ Quant, 黄金代币统计套利策略框架, https://www.fmz.com/strategy/526812 (public description; captured 2026-09-18).
