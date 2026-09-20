---
schema: strategy-research-record-v1
title: "Cross-Venue Four-Dimensional Crypto Options Contract Selector (FMZ 547584)"
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - options
  - contract-selection
  - cross-venue
  - iv-surface
  - liquidity
  - fmz
status: research-only
confidence: low
source_as_of: 2026-08-13
sources:
  - "FMZ digest article: 'You Got the Direction Right—Why Can Options Still Lose Money? A Four-Dimensional Crypto Options Selector Based on Deribit, Binance, and OKX', digest topic 11012, created 2026-08-13. https://www.fmz.com/digest-topic/11012"
  - "FMZ strategy page: 'Crypto Options Four-Dimensional Selector — Practical Monitoring Version v1.3.1', strategy id 547584. https://www.fmz.com/strategy/547584"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Venue Four-Dimensional Crypto Options Contract Selector (FMZ 547584)

## Provenance

- **Source URL (article):** https://www.fmz.com/digest-topic/11012
- **Source URL (strategy):** https://www.fmz.com/strategy/547584
- **Source type:** Public FMZ digest article with methodology narrative, formulas, and pseudocode; companion public strategy page (monitoring version v1.3.1). Full strategy source not fully audited this cycle (`data gap`).
- **Platform:** FMZ / 发明者量化
- **Created (source-reported):** digest 2026-08-13; strategy version label v1.3.1
- **Source reviewed as of:** 2026-09-20 (full digest body + strategy URL identity)
- **Deduplication audit (2026-09-20; origin/main):** No prior record cites FMZ id `547584`, digest topic `11012`, or this four-dimensional cross-venue options **contract-selection** construction. Adjacent records are different:
  - `fmz-synthetic-bs-gamma-scalping-btc-futures-hviv-delta-band-523268-2026-09-18.md` — synthetic BS straddle **overlay on BTC futures**; not listed-option contract selection.
  - `bitcoin-short-strangle-strike-distance-spa-decomposition-2026-09-18.md` — short-strangle strike SPA; different instrument construction.
  - Listed-option VRP / skew / GEX / RND records — trade or measure **vol risk**, not post-view contract selection across Deribit/Binance/OKX.
  - Gamma-scalping / hedging-band records — execution of Greeks, not selector ranking.

## Economic mechanism

### Source-reported

Source-reported problem: a correct directional view on BTC/ETH can still lose money on options because the buyer is long a bundle of Delta, Gamma, Vega, Theta, and liquidity exposure. Direction only determines part of the first-order term:

\[
\Delta V \approx \Delta\cdot\Delta S + \tfrac{1}{2}\Gamma(\Delta S)^2 + \mathrm{Vega}\cdot\Delta IV + \Theta\cdot\Delta t - \text{Trading Costs}
\]

Source-reported architecture: split trading into (1) a directional model that outputs where/how long/how far, and (2) an **option selector** that translates that view into a contract. The article focuses only on layer 2.

Four selection dimensions (source-reported):

1. **Convexity (strike):** Delta filter band, then Gamma, Speed (finite-difference bump of Gamma vs forward), and convexity efficiency \(\Gamma F^2 / \mathrm{Premium}\).
2. **Timing (expiry):** DTE must cover forecast horizon; ATM IV term structure; perpetual funding and futures basis as **crowding/maturity filters**, not standalone directional signals; liquidity of the expiry.
3. **Valuation (surface):** log-moneyness \(k=\ln(K/F)\); total variance \(w(k)=IV(k)^2 T\); skew-capable fit (SVI or simpler asymmetric smoother); **AskResidual** = AskIV − fair IV (buyer pays ask, not mark); 25-delta risk reversal and butterfly; local residual vs **cross-venue consensus fair IV** after projecting Deribit/Binance/OKX surfaces into common \((k,T)\).
4. **Execution (liquidity):** hard filters on relative spread, book-walk slippage for target notional, OI **and** 24h volume, quote age (`quote_age_ms`); stale quotes discarded before surface fit and ranking.

Source-reported process: hard filters first, layered ranking second (not one magic total score); then scenario repricing under direction-realized × IV-down/flat/up before order; final Top-3 contracts; risk budget sets size.

Source-reported cross-venue stance: three venues as **one candidate pool** and mutual validation; cross-venue IV residual is selection information, **not** automatic arbitrage (margin, fees, multipliers, settlement, transfer, leg risk remain).

Source-reported risk: limited premium loss ≠ low risk; repeated low-Delta short-DTE buys can be persistently negative after theta and spread; selector does not create directional edge.

### Research interpretation

This is **instrument selection / execution design** after an upstream view — not a standalone alpha signal and not vol-risk premium capture.

Research interpretation:

1. **Selection-as-cost-control hypothesis:** Most option PnL dispersion for a fixed view comes from strike/expiry/surface/liquidity choice; a reconstructable four-layer filter should reduce avoidable theta/vega/spread losses versus naive ATM-or-cheapest picks.
2. **Ask vs mark residual:** Ranking on mark IV systematically overstates “cheap” when spreads are wide — buyer-executable residual is the load-bearing valuation field.
3. **Cross-venue consensus:** Same risk cheaper on one venue may be structural (specs/margin/participants) rather than arb; selector should surface residual, not claim riskless edge.
4. **Boundary:** Without a directional edge upstream, the selector only chooses how to lose or win less/more on an already-made bet.

Component roles (normalized from digest):

```text
Input: underlying, direction, forecast horizon (from upstream model)
Universe: Deribit + Binance Options + OKX Options call/put chains
Normalize: USD premium, forward, DTE, Greeks (recompute with one model)
L1 filter: delta band (e.g. 0.10–0.30 long call illustrative), non-stale, max slippage
Convexity rank: speed bump, GammaEfficiency = Γ F² / premium
L2 timing: DTE vs horizon, ATM IV term structure, basis/funding crowding, expiry liquidity → keep 2–3 expiries
L3 surface: per-venue surface fit; AskResidual local + vs 3-venue consensus; RR25/BF25
L4 liquidity hard filter: spread rank, book walk, OI+volume, quote_age_ms
Scenario reprice: F_scenario × IV_scenario net of entry ask + exit cost + fee
Output: Top 3 contracts → risk budget sizes position
```

## Signal

Not a directional entry/exit signal. The “signal” is a **contract ranking** conditional on an external view.

### Formation timestamp

Source-reported: public REST/ticker endpoints on each venue; quotes carry age; stale quotes discarded. Exact snapshot alignment across three venues is implementation-defined (`underspecified` beyond `quote_age_ms`).

### Lookback

- Surface fit / term structure: all currently tradable expiries for the underlying at scan time (no multi-day lookback specified for the selector itself).
- OI/volume: 24h volume field; OI current.
- Illustrative delta band and thresholds in the article are **methodology examples**, not proven optima.

### Entry (contract selection)

Conditional on upstream `Underlying / Direction / Horizon`:

1. Filter option type (call for long view).
2. Delta band (illustrative long: `0.10 ≤ Δ ≤ 0.30`; short mirror).
3. Drop stale / excessive slippage candidates.
4. Rank convexity efficiency; keep candidate set.
5. Rank expiries by horizon coverage + term structure + crowding + liquidity; keep 2–3.
6. Fit surfaces; rank by AskResidual (local and cross-venue).
7. Hard liquidity filter; scenario reprice; Top 3.

### Exit

Source discusses exit **scenario pricing** (reprice at horizon with IV paths) and notes buyer max loss = premium but sequence risk remains. No mechanical stop/take-profit ladder is specified in the digest (`underspecified` for live exit rules).

### Holding period

Matched to upstream forecast horizon (example: 7-day view → DTE covering ~7 days plus timing buffer). Not a fixed holding rule in the selector alone.

### Parameters (source-reported illustrative defaults / formulas)

| Item | Source-reported value | Role |
|------|----------------------|------|
| Long delta band | 0.10–0.30 (illustrative) | Stage-1 strike filter |
| Short delta band | −0.30–−0.10 (illustrative) | Mirror |
| Speed | bump \(\varepsilon\) on forward, recompute Gamma | Cross-venue Speed without native field |
| GammaEfficiency | \(\Gamma F^2 / \mathrm{Premium}\) | Convexity per dollar premium |
| Moneyness | \(k=\ln(K/F)\) | Common strike coordinate |
| Total variance | \(w(k)=IV(k)^2 T\) | Surface coordinate |
| SVI form | \(w(k)=a+b[\rho(k-m)+\sqrt{(k-m)^2+\sigma^2}]\) | Skew-capable fit (or simpler smoother) |
| AskResidual | AskIV − IV_fair | Buyer-executable cheapness |
| Cross-venue residual | AskIV − consensus fair IV | Relative value across venues |
| RR25 / BF25 | standard 25Δ risk reversal / butterfly | Wing pricing |
| Spread / slippage / OI / volume / age | hard filters (thresholds adaptive/percentile preferred) | Execution gate |
| Strategy page | FMZ 547584 v1.3.1 | Monitoring implementation identity |

**Underspecified:** exact numeric hard-filter thresholds as production defaults; exit ladder; full source of 547584; capital allocation across Top-3; fee schedule per venue.

### Position sizing

Source: risk budget after Top-3 determines final size; premium budget and daily/weekly max-loss are **outside** the selector. No fixed notional in the digest.

### Specification completeness

**Medium-high for ranking pipeline and formulas** from the public digest; **medium** for live exit/sizing; strategy source not fully read this cycle.

## Required data

- **Instrument:** BTC/ETH listed options (calls/puts) on Deribit, Binance Options (`/eapi`), OKX Options (`/api/v5` option endpoints).
- **Universe:** all tradable contracts for underlying after type/delta/staleness filters.
- **Venue:** three named crypto option venues; one candidate pool after surface projection.
- **Timeframe:** real-time REST/ticker; no bar aggregation required for selector core.
- **Fields:** strike, expiry, option type, forward, bid/ask premium (USD-normalized), bid/ask/mark IV, Delta/Gamma/Theta/Vega (recomputed preferred), Speed (bumped), OI, 24h volume, book depth for slippage walk, quote timestamp/age; perpetual funding and futures basis for crowding filter; upstream direction + horizon.
- **Point-in-time:** only contemporaneous quotes; no historical surface required for the scan; upstream view must be formed without look-ahead into option path.
- **Timestamp:** per-venue quote age; cross-venue clock skew not fully specified (`underspecified`).
- **Missing-data:** drop stale quotes; insufficient quotes → simpler surface smoother or drop expiry.
- **Costs:** spread (hard), book-walk slippage, fees in scenario net PnL; funding/basis as filters not PnL legs in the selector itself.

## Execution assumptions

Source-reported: public APIs only; buyer pays **ask**; scenario net subtracts entry ask, expected exit spread, fees. Not established: queue/partial fills on options, cross-venue capital mobility, margin for multi-venue books, transfer latency.

Scout: treat cross-venue residual as selection signal only; do not assume simultaneous hedgeable legs without separate arb analysis.

## Evidence

### Source-reported

- Public digest methodology (four dimensions, formulas, pipeline diagram, scenario repricing).
- Strategy identity: FMZ `547584` “Practical Monitoring Version v1.3.1”.
- Source explicitly frames thresholds as **explanation of methodology**, not fixed parameters or investment advice; information checked August 2026.
- **No** published Sharpe/CE/hit-rate series for the selector in the digest.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- Source-reported: direction-correct option trades still lose via theta/vega/spread; “cheap” mark IV can be unexecutable at wide ask; limited max loss can still produce negative expectancy sequences.
- Research interpretation: without upstream edge, selector cannot create alpha; cross-venue residual may be structural not arb.
- No independent re-run of 547584 this cycle.
- Absence of our replication is not evidence the framework is useless — only that net edge is unproven here.

## Falsification plan

Research-proposed (not executed; not authorized):

1. **Selector vs naive baseline (research-defined falsification threshold):** Same upstream direction+horizon events; compare four-dimensional Top-1/Top-3 vs ATM-or-highest-liquidity pick on net premium PnL after ask, exit spread, fees. Fail if selector does **not** improve mean net PnL or tail loss per view.
2. **AskResidual vs MarkResidual ablation:** Rank by mark residual only; if mark-based “cheap” names underperform ask-based after costs by a pre-declared margin, mark ranking fails for buyers.
3. **Cross-venue value:** Restrict to single venue vs three-venue pool; fail cross-venue claim if consensus residual adds no net improvement after transfer/margin frictions are charged.
4. **Liquidity hard-filter stress:** Relax spread/slippage/age gates; fail if theoretical edge exists only when stale/wide quotes are allowed.
5. **Scenario honesty:** Require IV-down path still meets min net return; fail contracts that only win if IV rises with direction (two-factor bet mislabeled as directional).
6. **Horizon–DTE mismatch:** Force DTE < horizon; fail if theta dominates despite correct direction (supports dimension-2 necessity).
7. **Action on failure:** Keep `research-only`; do not treat 547584 as validated execution alpha.

## Crypto portability

**Portability: `direct` for crypto listed options venues (already the design domain); `not applicable` as a perp/spot trading port.**

- Native to Deribit/Binance/OKX option chains; depends on public option APIs and USD-normalized premiums.
- Risks: IV surface regime shifts, venue listing gaps, USDT/coin margin differences, option liquidity evaporation near events, upstream view quality.
- Crypto portability is not authorization to trade.

## Limitations

- **Not a strategy edge by itself** — selection layer only.
- **not independently reproduced**
- **No public performance series** in the digest.
- **underspecified:** production hard-filter thresholds, exit ladder, full 547584 source, multi-venue capital model.
- Thresholds in the article are explicitly illustrative.
- Incremental value: **public reconstructable cross-venue four-dimension options contract selector** with formulas and strategy URL, distinct from futures gamma overlays and single-venue VRP records.

## Implementation status

No implementation in our research stack. Does not modify NautilusTrader/PyBroker; does not authorize Paper/Testnet/Live.

`implementation_status: not-implemented`

Source-side: FMZ hosts strategy 547584; **not** treated as our validation.

## Adoption boundary

Research-only. Presence here does **not** mean profitable, validated, or approved for implementation, paper, testnet, or live trading.

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

## Related Wiki records

No stable Hermes Wiki Brain path known at write time. Do not fabricate Wiki links.

In-repo related: synthetic BS gamma scalping FMZ 523268; short-strangle SPA; listed-option VRP/skew/GEX/RND records; Polymarket/Kalshi binary records (different instruments).

## Sources

1. FMZ Quant. 「You Got the Direction Right—Why Can Options Still Lose Money? A Four-Dimensional Crypto Options Selector Based on Deribit, Binance, and OKX.」 Digest topic 11012, created 2026-08-13. https://www.fmz.com/digest-topic/11012 (full article body reviewed 2026-09-20).
2. FMZ Quant strategy page. 「Crypto Options Four-Dimensional Selector — Practical Monitoring Version v1.3.1.」 Strategy id 547584. https://www.fmz.com/strategy/547584 (identity preserved; full source not audited this cycle).
