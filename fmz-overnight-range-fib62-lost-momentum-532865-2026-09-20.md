---
schema: strategy-research-record-v1
title: "FMZ Overnight Range + Fibonacci 62% Contrarian Entry with Lost-Momentum Continuation (532865)"
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - session-structure
  - fibonacci
  - mean-reversion
  - breakout-fade
  - trend-continuation
  - fmz
  - fx-session
status: research-only
confidence: low
source_as_of: 2026-03-20
sources:
  - "FMZ strategy page: 'Overnight Range Fibonacci Retracement Strategy' / 'Trader Tom - Overnight Range + Fib 62% Strategy', strategy id 532865, author ianzeng123, created 2026-03-20. https://www.fmz.com/strategy/532865"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FMZ Overnight Range + Fibonacci 62% Contrarian Entry with Lost-Momentum Continuation (532865)

## Provenance

- **Source URL**: https://www.fmz.com/strategy/532865
- **Source type**: Public FMZ strategy page (Pine strategy banner + public description + parameter names). Full Pine source login-gated.
- **Author on page**: ianzeng123
- **Platform**: FMZ / 发明者量化
- **Source-reported title in code banner**: `Trader Tom - Overnight Range + Fib 62% Strategy` (shorttitle `TraderTom`)
- **Created (source-reported)**: 2026-03-20 09:18:08
- **Tags on page (source)**: EMA, FIBONACCI, RANGE BREAKOUT, MOMENTUM
- **Source reviewed as of**: 2026-09-20
- **Deduplication audit (2026-09-20)**: Repository-wide search found **zero** prior records citing FMZ id `532865`, overnight-range Fib 62% fade, or this Lost-Momentum + overnight-range hybrid. Adjacent records are different constructions:
  - Session/VWAP/Monday/roll-out and generic fib/EMA TV or FMZ records — not this overnight-range → London-break → **62% retracement fade** + Lost-Momentum pair.
  - FMZ median/MAD mean reversion (549579) — robust z-score reversion, not session-range fib fade.
  - FMZ flywheel (542065) — capital architecture; no session-range signal.
  - MNQ VVG / other session classifiers — different instruments and constructs.

## Economic mechanism

### Source-reported

Source-reported marketing frame: not average breakout chasing; **contrarian** logic — when price breaks the overnight range, wait for **62% Fibonacci retracement** before entry (“fake breakout, real pullback”). Source claims (unverified) this outperforms direct breakout chasing by **15–20% in volatile markets**.

Source-reported core logic:

1. Establish **overnight range** (default **0000–0800**, described as Asian session / lower liquidity).
2. Wait for **London session breakout** (page discusses 0800–1700 liquidity surge).
3. Enter at **62% retracement** of the breakout move / range:
   - After breaking overnight **high**, if price retraces to **62% below the high** (`high − range size × 0.62`), trigger **short**.
   - After breaking overnight **low**, retracement **62% above** triggers **long**.
4. Source rationale (attributed to “Trader Tom”): 62% is where “institutions re-enter”; avoid buy-high/sell-low; capitalize on corrective inertia.

Source-reported **Lost Momentum** module (trend continuation):

- Price runs **above rising 62-period EMA** (parameter default MA length **62**, type EMA).
- Briefly **breaks below an 8-period previous low**, then **closes back above** → long continuation (vice versa for shorts).
- Source claims (unverified) **~25% higher risk-adjusted returns** than pure trend following.

Source-reported risk management:

- **1% stop loss**, **2× risk-reward** target multiplier; **trailing stop** option instead of fixed target.
- Source acknowledges **underperformance in sideways/choppy** markets; best in medium-high volatility; avoid pre-holiday/illiquid conditions.
- Source claims optimal on **EUR/USD, GBP/USD** with **15–25% annual returns** and **max DD 8–12%** (unverified marketing/backtest language on the page).
- Explicit disclaimer: historical backtests ≠ future returns; regime changes matter.

Source-reported code banner (not performance proof): FMZ backtest comment header `2026-01-01`–`2026-03-19`, `1h`, `Futures_Binance`, `ETH_USDT`, `balance: 500000` — **inconsistent** with FX narrative (EURUSD/GBPUSD, London/Asian session) on the same page. Pine `strategy(...)` visible; full source login-gated.

### Research interpretation

This is a **session-structure + Fibonacci retracement fade** hypothesis with an optional **Lost Momentum** continuation filter — not a pure breakout and not a pure MA cross.

Research interpretation:

1. **Overnight range as liquidity/regime proxy:** Asian-session ranges may mark consolidation; London open may probe extremes that fade if not confirmed — behavioral/microstructure hypothesis, **session labels are FX-centric**.
2. **62% fib as operationalization:** Source uses a fixed retracement fraction of range size; “institutional re-entry” is **source narrative**, not independently evidenced here. Treat 0.62 as a **source-reported parameter**, not a proven microstructure constant.
3. **Hybrid thesis:** Range-fade (contrarian) + Lost-Momentum (continuation) are **two different mechanisms**; source presents both in one strategy page — do not assume they share one economic law.
4. **Venue mismatch risk:** Public narrative is FX session clock; FMZ backtest header is crypto perpetual (ETH_USDT). **Crypto portability of session logic is unproven** on 24/7 books without a session definition (`research-proposed`: UTC or exchange-local session mapping must be pre-declared).

Component roles (normalized):

```text
Session filter: overnight range window (default 0000-0800) vs trading/entry session (page discusses London 0800-1700)
Primary signal A (fade): breakout of overnight high/low → wait → 62% retracement of range from extreme → short/long
Primary signal B (continuation): EMA62 rising + brief break of 8-bar prior low/high + close reclaim → continuation entry
Risk: stop loss % (source default 1%); TP R:R multiplier (source default 2x); optional trailing stop
Regime caveat (source): weak in low-vol/chop; intended medium-high vol
```

## Signal

### Formation timestamp

Research interpretation: overnight range formed at end of 0000–0800 window; entry session after range is fixed; Lost Momentum uses closed bars. Exact timezone of “0000–0800” **not published** (`underspecified` — exchange local vs UTC vs FX session convention).

### Lookback

- Overnight range: session window (source default 0000–0800).
- Lost Momentum MA: **62** (source default; “per Tom” on parameter panel).
- Prior extreme lookback: parameter `Min bars back for previous low/high` — numeric default **not published** on public page (page shows 8-period language in narrative for Lost Momentum).

### Long entry

Source-reported:

- **Fade path:** price broke overnight **low**, then retraces to **62% above** that low / fib level (`low + range × 0.62` in the source’s “62% above” language — exact formula pairing should be re-verified in full Pine before any implementation; public text uses both “62% below the high” and “62% above” for the opposite side).
- **Lost Momentum path:** above rising EMA62; brief break of prior low (n-bar); close back above → long continuation.

### Short entry

Source-reported:

- **Fade path:** broke overnight **high**, retrace to fib 62% level below high (`high − range size × 0.62` explicitly stated for short trigger).
- **Lost Momentum:** mirror for shorts (run below falling MA context — exact mirror underspecified in public English summary).

### Exit

Source-reported:

- Stop loss **1%** (parameter `Stop Loss %`).
- Target **2× risk-reward** (`TP Multiplier (R:R)`), optional **trailing stop**.
- No separate time exit published.

### Holding period

Not published; implied intraday/session-scale (FX London narrative; FMZ 1h bars in banner).

### Parameters (source-reported where stated)

| Parameter | Source default / note |
|-----------|----------------------|
| Overnight session (range) | Default narrative **0000–0800** |
| Trading session (entry) | Narrative **0800–1700** (London); exact code default not public |
| Fib retracement | **62%** (0.62) of range from extreme |
| MA length (Lost Momentum) | **62** |
| MA type | EMA |
| Min bars back for prev low/high | Narrative ~**8**; panel default not numeric on page |
| Stop Loss % | **1%** |
| TP R:R multiplier | **2** |
| Use Trailing Stop | Optional (toggle) |

**Underspecified:** timezone; exact long-side fib formula; whether Lost Momentum and Fib-fade are OR/AND; instrument universe in code vs narrative; fees/slippage; numeric marketing performance methodology.

### Position sizing

Not published on public page (`underspecified`).

### Specification completeness

**Partially specified** — core fade formula and Lost Momentum sketch are public; timezone, combination logic, and size are not. Marketing performance figures are **not** reconstructable evidence.

## Required data

- **Instrument:** narrative FX majors (EURUSD, GBPUSD); FMZ banner shows **ETH_USDT** futures-style backtest header — **source inconsistency to flag**.
- **Venue:** FMZ; Pine strategy.
- **Timeframe:** banner `1h`; session windows in wall-clock hours.
- **Fields:** OHLC for overnight high/low, session times, EMA62, prior n-bar extremes.
- **Point-in-time:** closed bars implied; intrabar session boundary handling not specified.
- **Costs:** not modeled in public description.

## Execution assumptions

Source-reported: stop 1%, R:R 2×, optional trailing. Not established: slippage, spread (critical for FX), funding (if crypto perps), fill timing at fib touch.

## Evidence

### Source-reported

- Public narrative rules: overnight range, London breakout, 62% fade levels, Lost Momentum sketch, 1%/2×/trailing risk, regime caveats, FX performance **claims** (15–20% vs breakout chase; 15–25% annual on EURUSD/GBPUSD; 8–12% max DD; ~25% vs pure trend on Lost Momentum) — **marketing/backtest language on the page; not independently verified**.
- FMZ backtest comment header (dates, ETH_USDT, balance) — tooling metadata, **not** a published equity curve.
- Full Pine source login-gated.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- Source-reported: underperforms in **sideways/low-vol**; not a guaranteed edge; regime dependence; historical backtests ≠ future.
- Structural (research interpretation): 62% is a conventional fib choice without source-side statistical proof on this page; session logic may not transfer to 24/7 crypto; dual mechanisms (fade + continuation) can conflict; narrative FX vs ETH_USDT header inconsistency; unverified annual-return claims.
- Adjacent in-repo breakout/fib/session records document false-break and look-ahead risks in similar families — caution, not a replication of 532865.

## Falsification plan

Research-proposed (not executed; not authorized):

1. **Fade vs breakout control (research-defined falsification threshold):** On a pre-declared instrument/session definition, if net-of-cost expectancy of 62% fib-fade after overnight breakout is **≤ direct breakout chase** (or ≤ 0) over ≥100 signals, reject the source’s superiority claim for that sample.
2. **Fib level grid:** Pre-declare {0.5, 0.62, 0.786} on train; evaluate holdout. If only 0.62 works in-sample and fails OOS, mark overfit.
3. **Lost Momentum ablation:** Fib-fade only vs Lost Momentum only vs both. If the pair is not better than the better single rule, hybrid complexity is non-load-bearing.
4. **Session timezone audit:** Rebuild overnight range under UTC vs venue-local vs FX conventional sessions; if signals flip materially, timezone is load-bearing (`underspecified` until fixed).
5. **Crypto portability test:** ETH/BTC USDT perps with pre-declared UTC session windows vs FX majors; if edge does not transfer, keep portability `unproven`.
6. **Cost/spread stress:** Include bid-ask (FX) or taker fees+slippage (crypto); fail if source-style edge vanishes after costs.
7. **Action on failure:** Keep `research-only`; do not treat page marketing percentages as validated alpha.

## Crypto portability

**Portability: `unproven`.**

- Narrative mechanism is **FX session liquidity** (Asian range → London breakout).
- Crypto trades **24/7** without London/Asian exchange closures; “overnight” must be **research-proposed** (e.g. UTC 00:00–08:00) and re-validated.
- FMZ banner uses ETH_USDT but does not publish crypto-specific evidence on the public page.
- Risks: funding, always-on news flow, different vol regimes, fib touch non-fills.

Crypto portability is not authorization to trade.

## Limitations

- **Marketing performance claims** source-reported and unverified; this record does not endorse them.
- **underspecified:** timezone, AND/OR of dual signals, sizing, exact long fib formula wording.
- **not independently reproduced**
- **Source inconsistency:** FX session narrative vs ETH_USDT backtest header on same page.
- Full source login-gated.
- Ordinary fib/EMA content would not clear the bar; this write exists because the **public page publishes a specific overnight-range + 62% fade + Lost-Momentum construction** with explicit regime caveats — incremental as a traceable research capture, not as proven alpha.

## Implementation status

No implementation in our research stack. Does not modify NautilusTrader/PyBroker; does not authorize Paper/Testnet/Live.

`implementation_status: not-implemented`

Source-side: FMZ hosts Pine strategy + optional backtest UI; **not** treated as our validation.

## Adoption boundary

Research-only. Presence here does **not** mean profitable, validated, or approved for implementation, paper, testnet, or live trading.

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

## Related Wiki records

No stable Hermes Wiki Brain path known at write time. Do not fabricate Wiki links.

In-repo related: session/VWAP/roll-out TV records; median/MAD FMZ 549579; flywheel FMZ 542065; breakout/fib family records.

## Sources

1. FMZ Quant strategy page. "Overnight Range Fibonacci Retracement Strategy" (code title: Trader Tom - Overnight Range + Fib 62% Strategy). Author ianzeng123. Strategy id 532865. Created 2026-03-20. https://www.fmz.com/strategy/532865 (public description, parameter names, risk notes, and backtest comment header reviewed 2026-09-20; full Pine source not accessed).
