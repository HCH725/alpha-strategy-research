---
schema: strategy-research-record-v1
title: "Daily-Rebalanced Vol-Targeted TSMOM on Crypto Perpetuals: Honest Refutation of Four Alternatives and ETH-Concentrated Edge"
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - tsmom
  - time-series-momentum
  - crypto
  - perpetual-futures
  - volatility-targeting
  - rebalance-cadence
  - honest-refutation
status: research-only
confidence: medium
source_as_of: 2026-06-01
sources:
  - "https://github.com/yongzhe2160cs/trading-engine (commit efa37deac60fb9d91abcb181440c94f2f0eac4b8, 2026-06-01)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Daily-Rebalanced Vol-Targeted TSMOM on Crypto Perpetuals: Honest Refutation of Four Alternatives and ETH-Concentrated Edge

## Provenance

- **Primary Source:** yongzhe2160cs/trading-engine — a research-grade quantitative trading system for crypto perpetual futures on Bybit (USDT-margined linear perps).
- **Repository URL:** https://github.com/yongzhe2160cs/trading-engine
- **Full Commit SHA:** `efa37deac60fb9d91abcb181440c94f2f0eac4b8` (2026-06-01)
- **Key Source Paths:**
  - Strategy specification: `STRATEGY.md`
  - Core backtester and signals: `strategy/tsmom.py`
  - TSMOM validation (walk-forward, fold-stability): `analysis/tsmom_gate.py`
  - Significance testing (Newey-West HAC, bootstrap Sharpe CI): `analysis/significance.py`
  - TSMOM findings: `results/TSMOM_FINDINGS.md`
  - TSMOM validation findings: `results/TSMOM_VALIDATION.md`
- **Source As-Of Date:** 2026-06-01 (latest commit timestamp)
- **Sample Period:** 2021-01-01 to 2026-05-29 (47,381 hourly bars, ~5.4 years)
- **Universe:** BTC, ETH, SOL USDT-margined perpetual futures on Bybit
- **Data Source:** Binance Vision keyless mirror (1h OHLCV)
- **Repository Deduplication Audit:** Searched entire alpha-strategy-research repo for `yongzhe2160cs`, `trading-engine`, `TSMOM_FINDINGS`, and related terms. Existing TSMOM records (`hyperliquid-vol-targeted-tsmom-drawdown-calibrated-ratchet-2026-09-12.md`) cover Silvestri's Hyperliquid implementation with Magdon-Ismail drawdown calibration and asymmetric trailing ratchet. The present source is materially distinct: different author/repo, different venue (Bybit vs Hyperliquid), different validation methodology (honest refutation of four alternatives vs drawdown-calibrated leverage), and different key finding (daily rebalance importance and ETH-concentrated edge vs trailing ratchet mechanics).

## Economic mechanism

### Source-reported

Time-Series Momentum (Moskowitz, Ooi & Pedersen, 2012) exploits the empirical persistence of price trends across assets. The strategy goes long assets with positive trailing returns and short those with negative trailing returns, sized by inverse realised volatility (vol-targeting) to equalize risk contribution. The source reports that crypto trends are unusually persistent due to retail-driven, narrative-driven reflexive leverage cycles, and that vol-targeting naturally de-risks the book when realised vol spikes.

### Research interpretation

The hypothesized alpha mechanism is trend persistence filtered through cost-aware execution:

- **Regime:** Trend-following (directional persistence over weeks-to-months)
- **Signal:** Sign of trailing N-bar return (lookback = 720 hours = 30 days)
- **Sizing:** Inverse realised volatility with 20% annualized vol target, leverage capped at 2.0×
- **Rebalance:** Once daily (every 24 hourly bars), forward-filled between rebalances
- **Cost control:** Daily rebalance reduces turnover ~5-10× vs hourly, which is the critical finding — high-turnover strategies on 1h crypto bars are cost-dominated

The economic rationale relies on: (1) under-reaction to information creating serial correlation in returns, (2) herding and reflexive leverage amplifying trends, and (3) vol-targeting providing a natural crash-protection mechanism (position shrinks as vol rises).

## Signal

- **Formation timestamp:** Position decided at close of bar *t*, applied to return *t → t+1* (leak-free)
- **Lookback:** 720 hourly bars (30 days) for direction; 336 hourly bars (14 days) for realised volatility window
- **Long entry:** Sign(trailing return over 720 bars) = +1 → long, sized to target_vol / realised_vol
- **Short entry:** Sign(trailing return over 720 bars) = −1 → short, sized to target_vol / realised_vol
- **Exit:** Signal reversal at next rebalance bar; no stop-loss or take-profit in the core signal
- **Holding period:** 24 hours (daily rebalance); position forward-filled between rebalances
- **Parameters:**
  - Lookback: `lb = 720` bars (research-defined optimal; lb=336 also tested)
  - Vol window: `vw = 336` bars
  - Vol target: 20% annualized
  - Max leverage: 2.0×
  - Rebalance cadence: 24 bars (daily) — research-proposed; the source demonstrates this is materially superior to hourly
- **Re-entry rules:** At each daily rebalance, re-evaluate direction and re-size
- **Position sizing:** Inverse realised vol with leverage cap; equal capital split across 3 legs

## Required data

- **Instrument:** BTC, ETH, SOL USDT-margined perpetual futures
- **Venue:** Bybit (execution); Binance Vision (historical data)
- **Market type:** Perpetual futures (linear, USDT-margined)
- **Timeframe:** 1-hour OHLCV bars
- **Fields:** Open, High, Low, Close, Volume
- **Funding:** 8-hour settlement at 00/00/08/16 UTC, charged on held notional
- **Missing-data assumptions:** Standard OHLCV bars; no tick or order-book data required

## Execution assumptions

- **Signal-to-order timing:** Position decided at bar close, executed at next bar open (leak-free design)
- **Fill model:** Next-bar execution (conservative; no same-bar fills)
- **Fees:** Taker 5.5 bps + 5.0 bps slippage per unit turnover (Bybit-realistic)
- **Funding:** Charged at each 8h settlement on held notional; approximately 1 bp/8h average (conservative two-sided drag)
- **Spread:** Not separately modeled (subsumed in slippage assumption)
- **Impact / capacity:** Not modeled; strategy operates on liquid major perps
- **Leverage / margin:** Maximum 2.0×; actual average exposure ~0.32× due to vol-targeting
- **Partial fills / failures:** Not modeled

## Evidence

### Source-reported

The source reports the following from a chronological 70/30 in-sample/out-of-sample split on BTC/ETH/SOL 1h data (2021-01-01 to 2026-05-29), net of 5.5bps taker fee + 5.0bps slippage + funding:

**Per-asset OOS results (lb=720, vw=336):**

| Asset | OOS Sharpe | OOS Return | OOS MaxDD | B&H OOS |
|-------|-----------|-----------|-----------|---------|
| BTC   | −0.86     | −26.5%    | −35.0%    | +13.1%  |
| ETH   | 1.05      | +35.4%    | −24.7%    | −21.7%  |
| SOL   | −0.56     | −19.2%    | −26.6%    | −46.5%  |

**Per-asset OOS results (lb=336, vw=336):**

| Asset | OOS Sharpe | OOS Return | OOS MaxDD | B&H OOS |
|-------|-----------|-----------|-----------|---------|
| BTC   | −0.21     | −9.7%     | −38.4%    | +13.1%  |
| ETH   | 1.22      | +44.7%    | −20.5%    | −21.7%  |
| SOL   | 0.02      | −2.8%     | −19.6%    | −46.5%  |

**Book-level results (3-major equal-weight, lb=720, daily rebalance):**
- Net annualized Sharpe: ~1.15 (from README)
- Max drawdown: −19%
- HAC p-value: 0.008 (Newey-West, statistically significant)
- Fold-stability t-test (12 folds): SOL t=2.18, BTC t=2.02 — PASS
- Bootstrap Sharpe CI excludes zero

**Key finding — rebalance cadence matters enormously:**
- At hourly rebalance (~66× turnover/yr): NO config passes the fold-stability test
- At daily rebalance (24h): Net Sharpe roughly doubles; the verdict flips from "borderline" to "significant on the whole book"

**Honest refutation of four alternatives:**
1. EMA crossover: ~Zero edge, under-participates, fails edge_gate
2. Cross-sectional momentum (XSMOM): Dollar-neutral insignificant (p=0.17); long-only is just beta, −86% DD
3. Funding-rate arbitrage: Mean funding ≪ round-trip cost
4. BTC–ETH Kalman stat-arb: Pair doesn't revert fast enough at 1h

**Walk-forward validation (from TSMOM_VALIDATION.md):**
- Under strict multi-fold validation (6 and 12 folds), the only config passing at BOTH fold counts is SOL lb=720 (t=2.21/2.18)
- ETH is fold-count-sensitive (passes at 6, fails at 12)
- BTC never passes
- The source treats the overall conclusion as "borderline — small size at most, no clean deploy"

This result has not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The source explicitly notes that the edge is concentrated in ETH and does not generalize cleanly to BTC or SOL under strict multi-fold validation
- Short lookbacks (lb=24, vw=72) are catastrophic on every symbol — turnover costs dominate
- The walk-forward validation finding supersedes the single-split 70/30 result, and the more robust story is "borderline"
- The source states: "The edge is real but concentrated in ETH — not BTC, not SOL. This is an honest, surprising result"
- No other strategy in the repo (EMA, XSMOM, funding arb, stat-arb) survived validation

## Falsification plan

1. **Out-of-sample extension:** Extend the OOS window beyond 2026-05-29 and verify ETH edge persists. Failure threshold: OOS Sharpe < 0.5 over any rolling 12-month window.
2. **Multi-fold walk-forward (12+ folds):** Verify fold-stability across all three assets. Failure: any asset fails fold-stability t-test at |t| < 2.0.
3. **Cost sensitivity:** Double fee + slippage assumptions (to ~21 bps round-trip). Failure: book Sharpe drops below 0.5.
4. **Regime breakdown:** Test edge in distinct regimes (2021 bull, 2022 bear, 2023-2024 recovery, 2025+). Failure: edge absent in any full-year sub-period.
5. **Alternative lookbacks:** Test lb ∈ {168, 336, 504, 720, 1008} with fixed vol window. Failure: no lookback produces Sharpe > 0.5 across all three assets simultaneously.
6. **Universe widening:** Test on 11+ coins (as in `run_tsmom_universe.py`). The source reports this refutes the "just add more assets" hypothesis — confirm.
7. **Funding rate stress:** Test under extreme funding regimes (e.g., 2022 bear market persistent negative funding). Failure: funding drag erases >50% of gross edge.
8. **Action on failure:** If ETH edge fails any of the above, the strategy is rejected for implementation. If BTC/SOL edge fails but ETH survives, consider ETH-only deployment with position-size cap.

## Crypto portability

This strategy is native to crypto perpetual futures. Key portability considerations:

- **Perpetual vs spot:** Strategy requires perpetual futures for both long and short directions; not applicable to spot-only
- **Funding:** 8-hour funding settlement is a material cost component; strategy's edge exists despite this cost but is sensitive to funding regime
- **24/7 session:** No session structure issues; strategy operates continuously
- **Venue fragmentation:** Tested on Bybit; performance may differ on Binance, OKX, or Hyperliquid due to fee structures and liquidity differences
- **Liquidity:** BTC/ETH/SOL are the most liquid perps; extension to altcoins introduces liquidity and slippage risk
- **Leverage and liquidation:** Vol-targeting naturally keeps leverage low (~0.32× average), reducing liquidation risk

Label: **adapted** (native to crypto perps; TSMOM is a general quantitative finance concept applied to crypto)

## Limitations

- **ETH-concentrated edge:** Under strict multi-fold validation, only ETH shows a robust edge; BTC and SOL are borderline or negative. This limits portfolio diversification benefits.
- **Single venue:** Tested on Bybit data only; cross-venue replication not verified.
- **No order-book or tick data:** Strategy uses 1h OHLCV only; higher-frequency execution effects not modeled.
- **Walk-forward supersedes single split:** The 70/30 split result (book Sharpe ~1.15) is less robust than the multi-fold walk-forward finding ("borderline — small size at most").
- **Source is a single-author research repo:** Not peer-reviewed; code quality and methodology are self-reported.
- **Sample period overlaps with specific market regimes:** 2021-2026 includes both strong bull and bear markets; edge may be regime-dependent.
- **Funding data gaps:** Source notes funding data has gaps depending on exchange API.
- **No live or paper trading results:** Strategy has not been deployed; all results are backtest-only.
- **Data gap:** Exact transaction cost model parameters (5.5 bps taker + 5.0 bps slippage) are source-reported assumptions, not live-observed costs.

## Implementation status

No implementation in our research stack has been completed. The source repository contains a full backtester and validation pipeline but has not been deployed to paper or live trading.

## Adoption boundary

This record is research material only. Its presence in this repository does not mean:
- Passed Research Intake Review
- Entered Hermes Wiki Brain
- Entered the production candidate pool
- Completed Qlib full-backtest validation
- Became a frozen survivor or leaderboard entry
- Profitable
- Validated alpha
- Approved for implementation, paper trading, testnet, or live trading

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` — Schema specification
- `hyperliquid-vol-targeted-tsmom-drawdown-calibrated-ratchet-2026-09-12.md` — Related TSMOM research (Silvestri's Hyperliquid implementation with drawdown calibration; different source, different mechanism focus)

## Sources

1. yongzhe2160cs/trading-engine, commit `efa37deac60fb9d91abcb181440c94f2f0eac4b8` (2026-06-01). Repository URL: https://github.com/yongzhe2160cs/trading-engine. Key files: `STRATEGY.md`, `results/TSMOM_FINDINGS.md`, `results/TSMOM_VALIDATION.md`, `strategy/tsmom.py`, `analysis/significance.py`, `analysis/tsmom_gate.py`.
2. Moskowitz, Tobias J., Yao H. Ooi, and Lasse H. Pedersen (2012). "Time Series Momentum." *Journal of Financial Economics*, 104(2), 228–250. (Referenced in source as theoretical foundation.)
