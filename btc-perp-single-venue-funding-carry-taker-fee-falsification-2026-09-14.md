---
schema: strategy-research-record-v1
title: "BTC Perpetual Single-Venue Funding Carry: Stationary but Non-Predictive Rate and Taker-Fee Falsification"
created: 2026-09-14
updated: 2026-09-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-08-05
sources:
  - "https://github.com/santzmr/funding-rate-arbitrage (commit b0cfb3aa4075bdecab2bab4a70313491366c2227, README.md; src/backtest.py; src/fetch_data.py)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# BTC Perpetual Single-Venue Funding Carry: Stationary but Non-Predictive Rate and Taker-Fee Falsification

## Provenance

- **Source:** Public GitHub repository `santzmr/funding-rate-arbitrage`
- **Repository URL:** https://github.com/santzmr/funding-rate-arbitrage
- **Full commit SHA:** `b0cfb3aa4075bdecab2bab4a70313491366c2227`
- **Primary paths read:** `README.md`, `src/backtest.py`, `src/fetch_data.py` (structure and data notes)
- **Author:** Santiago Zamora (Economics, Universidad de Costa Rica); self-described student practice project
- **Source as-of:** commit date 2026-08-05; sample January 2023 – July 2026
- **Source type:** Public open-source research repo with data pull scripts, statistical tests, backtest, and sensitivity grid

## Economic mechanism

### Source-reported

Crypto perpetual funding is an exchange mechanism that periodically transfers cash between longs and shorts to keep the perpetual anchored near spot. The naive hypothesis: when funding is abnormally high (longs pay shorts), a **delta-neutral** package — long spot + short perpetual — earns the funding stream with no directional BTC exposure. The author reports that Binance BTCUSDT funding is **stationary** (ADF −5.13, p ≈ 1.2e−5) and mean-reverting (AR(1) φ ≈ 0.81, half-life ≈ 3.32 periods ≈ 1.11 days), but that the funding rate **does not predict forward perpetual returns** at 8h, 1d, or 7d horizons under Newey–West HAC inference (all |t| < 1, R² ≈ 0). Under Binance standard **taker** fees the cash-and-carry backtest **loses money** (−1.52% over ~3.5 years, 33 trades, 21.2% win rate); the same trades gross **+5.20%** without fees, so fee drag ≈ **6.7 pp**. Swapping to **maker** fees flips most of the sensitivity grid positive (best cell +3.57%). Source conclusion: whether this works depends almost entirely on **execution cost**, not on the entry threshold.

### Research interpretation

This capture is **negative / cost-binding evidence** for the single-venue spot–perp funding-carry family. The reconstructable lesson is threefold: (1) mean-reversion of the funding *series* is not the same as *tradeable* carry after costs and capital accounting; (2) taker execution on reactive threshold entries can fully consume thin carry; (3) funding level alone is a weak directional predictor of forward returns, so any edge is carry-collection + cost structure, not a return-forecast factor. The author also documents two subtle implementation traps that inflate naive backtests: crediting funding on the entry bar (should be first collection at t+1) and dividing PnL by spot notional alone while capital includes margin on the short leg. This interpretation framing is **research-proposed**; numeric results below are source-reported.

## Signal

- **Formation timestamp / availability:** 8-hour Binance funding settlements. Historical series from public `/fapi/v1/fundingRate` (paginated). Price series from `/fapi/v1/klines` (perp) and `/api/v3/klines` (spot), indexed on **close_time** so the price at a funding timestamp is the close of the candle that ends there (author notes open_time indexing would shift prices 8h early).
- **Lookback / thresholds:** Entry when funding crosses the **sample 95th percentile** (`entry_q=0.95`); exit when funding falls below the **median** (`exit_q=0.50`) or after `MAX_HOLD=9` periods (~3 days ≈ 3× half-life). Percentiles are computed on the full sample in the default backtest (**in-sample**; author flags this).
- **Entry (long-carry package):** When `funding[t] > hi`: long spot notional 1, short equal-notional perpetual; first funding collection is **t+1** (not t). Entry fee charged at open.
- **Exit:** Funding `< lo` or `held >= max_hold`; exit fee charged; equal-notional legs closed simultaneously.
- **Holding period:** Mean source-reported hold ≈ (not stated as average in README for the 33-trade taker run); max 9 periods. Time deployed ≈ 8.4% of sample.
- **Parameters (source):** `SPOT_FEE=0.0010`, `FUT_FEE=0.0005` (Binance standard-tier taker), `MARGIN_FRAC=0.5` (short-leg margin as fraction of notional; author labels this a **guess**), `MAX_HOLD=9`, `PER_YEAR=365*3` (8h grid annualization). Maker-fee scenario explored in sensitivity only.
- **Capital accounting:** `cap = 1 + MARGIN_FRAC`; period return divided by capital, not spot notional alone.

## Required data

- **Instrument:** BTCUSDT perpetual + BTCUSDT spot (Binance USDⓈ-M style pairing; cash-and-carry).
- **Venue:** Binance (single exchange).
- **Sample:** January 2023 – July 2026; **3,912** 8-hour funding observations after cleaning (no missing values, no duplicate timestamps, no gaps > 9 hours).
- **Fields:** funding rate history; perp klines; spot klines (OHLC close used).
- **Point-in-time / look-ahead:** Percentile thresholds in default backtest use full-sample quantiles (**in-sample**; not point-in-time). Author states sensitivity grid is in-sample and “nothing here is validated out-of-sample.”
- **Basis caveat:** Author used **close-to-close** spot–perp basis, not Binance `/fapi/v1/premiumIndexKlines`. Mean funding +0.0066%/period vs mean basis −0.028% looks contradictory because Binance funding ≈ premium + clamped interest (default 0.01%/8h); 28% of observations sit at exactly 0.01%. A production version would pull the premium index.
- **Missing-data:** None remaining after cleaning; fetch script paginates 1000-row API caps.

## Execution assumptions

- **Order style (source):** Taker by default — “entries are triggered by funding crossing a level, which is a reactive order, not a passive one sitting on the book.” Fees: spot 0.10% + futures 0.05% = **0.15% per side**, **0.30% round trip**.
- **Maker alternative:** Sensitivity with maker fees flips almost the entire grid positive (every taker cell except one loses; every maker cell except one makes money). Longer holds beat shorter holds (more collections per fixed round-trip fee).
- **Slippage / impact:** Flat fee assumption; not modeled from book depth. Liquidity/capacity not assessed.
- **Margin / liquidation:** `MARGIN_FRAC=0.5` is explicit guess; real margin varies with vol/size; **short-leg liquidation not modeled**.
- **Funding collection timing:** Corrected in code comments — funding at t is paid to positions already open at t; entry bar does not receive funding[t].

## Evidence

### Source-reported

- **Stationarity / dynamics:** ADF funding −5.13 (p=0.000012); basis −4.15 (p=0.0008); AR(1) φ=0.81; half-life 3.32 periods (1.11 days).
- **Predictive regression (HAC Newey–West):** funding → forward perp returns at 8h/1d/7d: β = −2.31 / −1.76 / +15.43; t = −0.78 / −0.23 / +0.36; p = 0.44 / 0.82 / 0.72; R² ≈ 0.000. Bucket sorts non-monotonic; author attributes dual-tail elevation to bull-market artifact (BTC ~$16.5k→$65k).
- **Backtest (entry p95, exit median/9, taker):** strategy −1.52%, Sharpe −0.90, max DD −1.56%, time deployed 8.4%, 33 trades, **21.2% win rate**. Buy-and-hold +285.79%, Sharpe 1.07, max DD −53.29% (author warns Sharpe series are **not comparable** due to cash-heavy strategy path).
- **Fee decomposition:** Gross (no fees) **+5.20%**; net **−1.52%**; fee drag **~6.7 pp**.
- **Sensitivity:** Longer holds dominate; taker vs maker is the dominant sign flip.
- **Author caveats:** In-sample grid; 100% win-rate cells are 11–42 trade artifacts at near-zero fees; single venue/symbol; premium index not used; margin guessed.

### Independently reproduced

`not independently reproduced`.

### Negative evidence

This record **is** the negative-evidence capture for naive single-venue BTCUSDT cash-and-carry on high funding:
1. Stationary funding ≠ profitable carry after Binance taker costs.
2. Funding does not linearly predict forward returns at tested horizons.
3. Thin gross edge (+5.2%) is erased by 0.30% round-trip taker fees over 33 trades.
4. Default thresholds are in-sample; no OOS validation claimed.
Related repository captures already document cross-venue funding spreads, cost decay, and binding-cost negatives; this adds **single-venue spot–perp** mechanics, HAC non-prediction, and an explicit **entry-bar funding timing bug** that would otherwise manufacture ~most of gross edge on a 33-trade sample.

## Falsification plan

Tests the source already runs or that follow directly (research-defined thresholds marked):

1. **Fee stress (primary falsifier):** If net total return ≤ 0 under venue-standard **taker** fees while gross > 0, classify as **cost-killed** rather than alpha. Source result: −1.52% net vs +5.20% gross.
2. **Execution-structure test:** Re-run identical signals with **maker**/post-only assumption; if sign flips purely on fee class, edge is execution-conditioned, not signal-stable. Source: maker grid mostly positive.
3. **Predictive-null check:** HAC regressions of funding on forward returns; if |t| < 2 and R² ≈ 0 at all tested horizons, reject “funding as return forecast” (**research-defined falsification threshold**). Source: rejected.
4. **In-sample audit:** Refit thresholds on rolling/expanding windows; if p95 entry chosen on full sample degrades OOS, treat grid cells as descriptive only. Source does **not** complete this; remains open.
5. **Timing audit:** Confirm first funding credit is t+1; if t is credited, gross edge is overstated (author measured ~1.1 pp / most of gross on 33 trades when buggy).
6. **Capital audit:** Divide PnL by spot+margin capital, not spot notional alone.
7. **Premium-index substitution:** Recompute with `/fapi/v1/premiumIndexKlines` vs close-to-close basis; large differences would change entry occupancy at 0.01% piles.

## Crypto portability

- **Status:** **Direct** (already a crypto-native BTCUSDT strategy), but **implementation-quality limited**.
- **What ports cleanly:** 8h funding cadence; long-spot/short-perp construction; percentile entry; fee-class dominance.
- **What does not automatically port:**
  - Cross-venue or Hyperliquid/Bybit fee schedules and maker rebates.
  - Funding formula variants (premium index, clamps, interest terms).
  - Capital/margin and liquidation on the short leg.
  - Stablecoin collateral and venue risk.
- **Relation to other captures:** Cross-venue funding-differential arb and extreme-reversion/fade family records already exist in-repo; this record does **not** authorize porting and does not replace those. Incremental crypto-specific value is **negative single-venue evidence + cost/timing traps**, not a new live edge claim.

## Limitations

- Student practice project; 0 stars; single author; not peer-reviewed.
- 33 trades; 8.4% deployment; statistical power for strategy performance is low even though funding-series tests use ~3.9k points.
- No OOS / walk-forward on thresholds; in-sample quantiles and in-sample sensitivity.
- Taker fee assumptions may overstate retail cost if maker/post-only is achievable; understate if slippage/impact added.
- Margin fraction guessed; liquidation risk ignored.
- Close-to-close basis ≠ exchange premium index.
- Buy-and-hold comparison is context only, not a fair risk-matched benchmark.
- Independent reproduction not performed for this Scout run.

## Implementation status

`not-implemented` in our systems. Source provides fetch/stats/backtest Python scripts. This research capture does not modify NautilusTrader/PyBroker, does not run backtests here, and does not create implementation/backtest/Paper/Testnet/Live tasks.

## Adoption boundary

`research-only` / `not-implemented` / `not-approved` / `approval_scope: research-only`. Presence of this record means only that a reconstructable single-venue funding-carry hypothesis and its **negative cost/predictability evidence** were normalized for intake review. It is not strategy adoption, implementation authorization, or permission to run Paper/Testnet/Live.

## Related Wiki records

Repository-local neighbors (mechanism family; not identical rules):

- `crypto-perpetual-funding-rate-carry-spot-perp-2026-08-31.md`
- `crypto-funding-rate-mean-reversion-ema-taker-filter-2026-09-11.md`
- `crypto-funding-carry-fade-turnover-cost-dissipation-falsification-2026-09-12.md`
- `crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11.md`
- `crypto-cross-venue-funding-carry-negative-results-cost-decay-2026-09-13.md`
- `cross-venue-funding-carry-patient-rebalance-vs-active-harvesting-2026-09-12.md`

No pre-existing record in this repository implements this exact Binance BTCUSDT **p95 funding entry / median-or-9 exit** cash-and-carry with HAC non-prediction tests, taker-vs-maker fee flip, entry-bar funding timing correction, and full-sample-quantile in-sample caveat as one package; this is not a paraphrase of the above.

## Sources

- https://github.com/santzmr/funding-rate-arbitrage
- https://github.com/santzmr/funding-rate-arbitrage/blob/b0cfb3aa4075bdecab2bab4a70313491366c2227/README.md
- https://github.com/santzmr/funding-rate-arbitrage/blob/b0cfb3aa4075bdecab2bab4a70313491366c2227/src/backtest.py
- https://github.com/santzmr/funding-rate-arbitrage/commit/b0cfb3aa4075bdecab2bab4a70313491366c2227
