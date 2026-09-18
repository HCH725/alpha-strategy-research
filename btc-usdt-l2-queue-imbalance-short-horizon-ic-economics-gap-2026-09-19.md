---
schema: strategy-research-record-v1
title: "BTC-USDT L2 Queue Imbalance Short-Horizon Alpha: Strong Predictive IC but Thin Execution Economics"
created: 2026-09-19
updated: 2026-09-19
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - microstructure
  - order-book
  - queue-imbalance
  - BTC-USDT
  - walk-forward
  - execution-cost
  - LightGBM
status: research-only
confidence: high
source_as_of: 2026-08-15
sources:
  - "https://github.com/H2nryHe/Microstructure_Alpha_Execution_Lab (commit 50497ff0a6ed54e2f9af078de895e6a0162b1112, 2026-08-15)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# BTC-USDT L2 Queue Imbalance Short-Horizon Alpha: Strong Predictive IC but Thin Execution Economics

## Provenance

- **Primary source:** GitHub repository `H2nryHe/Microstructure_Alpha_Execution_Lab` — an end-to-end market-microstructure research system built around incremental L2 order-book data and trades for BTC-USDT on Binance.
- **Author:** Henry (H2nryHe on GitHub).
- **Repository URL:** https://github.com/H2nryHe/Microstructure_Alpha_Execution_Lab
- **Immutable commit SHA:** `50497ff0a6ed54e2f9af078de895e6a0162b1112` (2026-08-15).
- **Source as-of:** 2026-08-15 (commit date); repository claims research-complete status with 2026 reserved as untouched temporal holdout.
- **Public-use status:** Repository is public. This record normalizes the public description and findings; no source code is reproduced.
- **Primary research artifacts in repository:** `reports/final/MICROSTRUCTURE_ALPHA_EXECUTION_LAB_REPORT.md`, `reports/final/FINAL_METRICS.json`, `reports/final/FINAL_ARTIFACT_INDEX.md`.
- **Deduplication:** No repository record was found for H2nryHe, `Microstructure_Alpha_Execution_Lab`, commit `50497ff0a6ed`, or the specific finding that queue imbalance reaches ~0.43 Spearman IC at 1s but breakeven fee is only ~0.687 bps. Materially related records include `order-flow-imbalance-predictive-decoupling-cost-falsification-2026-09-12.md` (Tejas356 OFI study, different source, different methodology) and `binance-perpetual-order-flow-imbalance-horizon-decay-queue-imbalance-falsification-2026-09-13.md`. Those address OFI predictive decay and cost falsification from different angles; the present source provides the specific IC-to-economics gap quantification and the LightGBM-vs-QI comparative finding.

## Economic mechanism

### Source-reported

The source investigates whether BTC-USDT order-book and order-flow signals can forecast short-horizon price moves, and whether that signal survives the mechanics and costs required to trade it. The central hypothesis is that queue imbalance (QI) — the difference between bid and ask queue sizes at the top of the book — contains short-horizon predictive information about the direction of the next price move.

The mechanism: when the bid queue is significantly larger than the ask queue (positive QI), the next price move is more likely to be upward because aggressive sellers will exhaust the thinner ask side first. The converse holds for negative QI. This is a standard microstructure prediction grounded in the Kyle (1985) and Glosten-Milgrom (1985) framework.

### Research interpretation

The hypothesized mechanism is **order-flow pressure asymmetry**: the relative size of resting limit orders at the best bid and ask creates an asymmetric vulnerability to aggressive market orders. When one side is thinner, it exhausts first, pushing the price toward the thicker side. This is a well-established microstructure effect, but the source's contribution is quantifying how much of this effect survives after realistic execution costs.

The source's key insight is that **predictive power (IC) and executable economics are decoupled**: a signal can have strong statistical predictive power but fail to generate net-of-cost returns because of turnover, spread consumption, latency, queue uncertainty, and adverse selection. This is the central finding.

## Signal

### Queue imbalance (QI) baseline

- **Signal formation:** At each 100ms observation point, compute QI = (bid_queue_size - ask_queue_size) / (bid_queue_size + ask_queue_size) at the top of the book.
- **Prediction horizon:** 1-second forward mid-price return.
- **Signal rule (research-defined):** q10/q90 threshold — go long when QI exceeds the 90th percentile, go short when QI falls below the 10th percentile (research-defined threshold).
- **Active coverage:** ~21.7% of observations.
- **Formation timestamp:** Observation-time causality enforced — exchange timestamps preserved, local observation time plus source order governs replay.
- **Lookback:** Feature windows strictly backward-looking; labels strictly forward-looking.

### Extended LightGBM model

- **Features:** 91 leakage-controlled microstructure features including QI, OFI (order flow imbalance), microprice, and deeper imbalance features.
- **Training:** Chronological walk-forward with 18 expanding folds; no cross-day leakage.
- **Active coverage:** ~17.3% of observations (q10/q90 rule on model output).
- **Model:** Extended LightGBM with default hyperparameters; the source treats this as a representative nonlinear model, not an optimized production system.

### QI + OFI combination

- **Signal:** QI augmented with OFI (order flow imbalance — the net aggressive order flow over a short window).
- **Active coverage:** ~20.2% of observations.

## Required data

- **Instrument:** BTC-USDT perpetual futures (Binance).
- **Venue:** Binance.
- **Market type:** USDT-margined perpetual futures.
- **Timeframe:** Incremental L2 order-book updates (tick-level); observation grid at 100ms intervals; 1-second prediction horizon.
- **Fields:** L2 order-book depth (top 20 levels), trade data (aggressor side, size, price), best bid/ask prices and sizes.
- **Data source:** Tardis.dev L2 reconstruction.
- **Observation count:** ~20.7M state-observation rows across the research dataset; 6.49M L2 rows on the engineering validation day; 816K completed event states; 864K fixed 100ms observations per day.
- **Point-in-time:** Causal order-book replay enforced; no look-ahead in feature construction.
- **Timestamp requirements:** Exchange timestamps preserved; local observation time governs replay order.
- **Missing-data handling:** Causal replay naturally handles out-of-order records by replaying in source order.

## Execution assumptions

### Market orders (source-reported)

- High fill certainty.
- Immediate spread / displayed-depth cost through the actual fill price.
- Latency changes the market state seen at arrival.
- Higher turnover quickly consumes sub-basis-point predictive edge.

### Passive orders (source-reported)

- Conservative queue-position approximation from visible L2 depth.
- Partial fills, TTL, cancel handling, and taker-on-arrival behavior.
- Low fill participation in the reference diagnostics.
- Residual inventory and post-fill adverse-selection risk remain visible.
- The source deliberately does **not** claim exact FIFO queue reconstruction from L2 data.

### Cost model

- Fee stress is separated from fill mechanics so spread/slippage is not double-counted.
- The source does not assume a specific fee tier; instead it computes the **breakeven fee** — the fee level at which the strategy breaks even — to characterize cost headroom.

### Key cost findings (source-reported)

- QI six-date mean breakeven fee at 0ms latency: **~0.687 bps**.
- QI six-date median breakeven fee at 0ms latency: **~0.440 bps**.
- QI net-positive days at 0.25 bps taker fee: **3/6 dates**.
- QI net-positive days at 0.50 bps taker fee: **2/6 dates**.
- Extended / QI+OFI did not robustly improve net economics versus QI.

## Evidence

### Source-reported

1. **QI predictive power:** Queue imbalance reached ~0.426 mean daily Spearman IC at 1-second horizon, with 24/24 pre-registered development dates positive across ~20.7M observations. This survived targeted audits: changed-state-only IC ~0.447; non-overlap IC ~0.425; five-minute temporal-mismatch control ~0.004. Source reports this as the dominant simple microstructure signal.

2. **ML marginal contribution:** Extended LightGBM improved mean IC by approximately +0.0107 versus direct QI across 18 expanding walk-forward folds, positive in 18/18 folds. QI+OFI added approximately +0.0067. The source emphasizes that "a simple, interpretable microstructure variable captured most of the ranking structure, while nonlinear modeling added a small but repeatable adjustment."

3. **IC-economics decoupling:** Stronger predictive IC from Extended/LightGBM did not robustly dominate the simpler QI baseline economically. The source states: "Predictive alpha ≠ executable gross edge ≠ cost-adjusted net edge."

4. **Thin cost headroom:** At 0ms latency, the mean breakeven fee was only ~0.687 bps. At realistic fee levels (0.25–0.50 bps), only a minority of dates remained net-positive. This means the strategy's edge is real but extremely fragile under realistic cost assumptions.

5. **Passive execution limitation:** Passive fills remained low, queue-sensitive, adverse-selection-prone, and inventory-constrained. The source does not claim passive execution solves the spread problem.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The central negative finding is that **better predictive IC does not automatically produce better net trading economics**. This is a structural limitation, not a bug — it reflects the fundamental gap between statistical prediction and implementable alpha.
- At realistic fee levels (0.25–0.50 bps), the majority of dates were net-negative. Only at zero or near-zero fees does the strategy show consistent profitability.
- Passive execution did not cleanly solve the spread problem — fills were low and adverse-selection-prone.
- The source reserves 2026 as an untouched temporal holdout, so out-of-sample validation on the most recent data has not yet been performed.

## Falsification plan

1. **Out-of-sample validation on 2026 data:** The source reserves 2026 as a holdout. If the QI IC degrades materially on unseen data, the hypothesis is weakened. (research-defined falsification threshold: IC drops below 0.30 Spearman on the holdout period.)

2. **Fee sensitivity:** If the strategy is net-negative at any realistic fee level (≥0.25 bps) on a sustained basis, it is not tradeable. (research-defined: net-negative on >4/6 dates at 0.25 bps.)

3. **Venue generalization:** If the QI signal does not replicate on other high-volume perpetual venues (e.g., OKX, Bybit), the finding may be Binance-specific. (research-defined: IC < 0.25 Spearman on alternative venue.)

4. **Latency sensitivity:** If adding realistic latency (≥50ms) destroys the breakeven fee margin, the strategy is not implementable without co-location. (research-defined: breakeven fee drops below 0.25 bps at 50ms latency.)

5. **Ablation of ML contribution:** If the LightGBM model's +0.0107 IC advantage does not survive parameter perturbation or alternative model specifications, the ML marginal contribution is not robust.

## Crypto portability

**Adapted.** The QI mechanism (order-book asymmetry driving short-horizon price direction) is a universal microstructure phenomenon that should transfer to any venue with a central limit order book. However:

- The specific IC magnitudes (~0.43 Spearman at 1s) are calibrated to BTC-USDT on Binance and may differ on other venues or assets.
- Fee structures vary significantly across venues and tiers; the breakeven fee analysis is venue-specific.
- BTC-USDT perpetuals on Binance are among the most liquid crypto markets; thinner markets may show different dynamics (higher IC but lower fill rates, or vice versa).
- The 24/7 crypto session structure means the signal operates continuously, unlike equity markets with defined trading hours.
- Funding rate mechanics on perpetuals create additional costs not modeled in the source.

## Limitations

- **Single-asset, single-venue:** Results are for BTC-USDT on Binance only. Generalization to other assets and venues is unproven.
- **No live execution:** The source is a historical research system; no live trading has been performed.
- **Simplified passive queue model:** The source explicitly does not claim exact FIFO queue reconstruction from L2 data. Queue position is approximated, not observed.
- **No hidden liquidity modeling:** Only displayed L2 depth is observed; hidden orders and iceberg orders are not modeled.
- **Fee model is generic:** Fee stress tests use generic research fee levels, not actual venue-specific tier pricing.
- **2026 holdout not yet evaluated:** The source reserves 2026 as an untouched temporal holdout; the most recent data has not been tested.
- **Thin cost headroom:** At realistic fee levels, the majority of dates are net-negative. The strategy's edge is real but extremely fragile.
- **ML marginal contribution is small:** LightGBM adds only +0.0107 IC over QI; this may not justify the additional complexity and overfitting risk.
- **Not independently reproduced:** All findings are from a single researcher's pipeline.

## Implementation status

No implementation in our research stack. The source repository provides a complete, reproducible pipeline (Python 3.11+, CI-verified) but is a research artifact, not a trading system. The source explicitly states it "does not claim production trading performance or executable profit."

## Adoption boundary

This record is research material only. A record being present in this repository does **not** mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

The central finding — that strong predictive IC does not guarantee executable edge — is itself a valuable research result for calibrating expectations about microstructure alpha strategies.

## Related Wiki records

- `[[order-flow-imbalance-predictive-decoupling-cost-falsification-2026-09-12]]` — Related OFI predictive-decoupling study from a different source (Tejas356/limit_order_book_engine), covering contemporaneous-to-predictive decoupling from a different methodological angle.
- `[[binance-perpetual-order-flow-imbalance-horizon-decay-queue-imbalance-falsification-2026-09-13]]` — Related OFI horizon-decay study.
- `[[quant/strategy-research-record-spec-v1]]` — Schema specification.

## Sources

1. Henry (H2nryHe), *Microstructure Alpha & Execution Lab*, GitHub repository `H2nryHe/Microstructure_Alpha_Execution_Lab`, commit `50497ff0a6ed54e2f9af078de895e6a0162b1112` (2026-08-15). https://github.com/H2nryHe/Microstructure_Alpha_Execution_Lab. Source as-of: 2026-08-15.
