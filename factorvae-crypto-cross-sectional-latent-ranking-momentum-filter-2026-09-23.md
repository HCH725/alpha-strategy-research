---
schema: strategy-research-record-v1
title: "FactorVAE cross-sectional latent ranking of 50 Binance cryptocurrencies (Alpha158 features, one-day-ahead RankIC signal) → seven portfolio constructions incl. BTC-momentum-filtered Top-5 (SSRN 6860920)"
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - deep-learning
  - factor-model
  - variational-autoencoder
  - market-timing
status: research-only
confidence: medium
source_as_of: 2024-12-31
sources:
  - "Sacha Boyer, 'Cross-Sectional Return Prediction in Cryptocurrency Markets Using Variational Latent Factor Models', SSRN abstract 6860920, DOI 10.2139/ssrn.6860920; Posted 11 Jun 2026, Date Written June 01, 2026, 19 pages. Stable URL: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6860920"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-sectional crypto return prediction with a FactorVAE latent-factor model: seven portfolio constructions over a daily one-day-ahead ranking signal, with a BTC 20-day-momentum cash filter as the best reported variant (SSRN 6860920)

## Provenance

- **Primary source (complete author list, exactly as printed on the PDF cover and the SSRN abstract page):** **Sacha Boyer**, University of California, Berkeley (`sacha.boyer@berkeley.edu`). **Single-author paper** — no co-authors on cover, abstract page, or anywhere in the document.
- **Title:** *Cross-Sectional Return Prediction in Cryptocurrency Markets Using Variational Latent Factor Models*.
- **Version / date (primary-source checksum, performed 2026-09-23):** pinned version = SSRN delivery PDF `https://papers.ssrn.com/sol3/Delivery.cfm/6860920.pdf?abstractid=6860920&mirid=1`, retrieved inside a Cloudflare-cleared browser session on 2026-09-23. Local file: **1,778,056 bytes, SHA-256 `7278f652e7ce69f6dee95cca38052378c55904d14ea16af71173570846c5d876`**, `%PDF-1.5`, **19 pages**. SSRN abstract page (read 2026-09-23): `19 Pages · Posted: 11 Jun 2026 · Date Written: June 01, 2026 · Downloads 127 · Abstract Views 261`. Suggested citation on SSRN: `Boyer, Sacha, Cross-Sectional Return Prediction in Cryptocurrency Markets Using Variational Latent Factor Models (June 01, 2026). Available at SSRN: https://ssrn.com/abstract=6860920 or http://dx.doi.org/10.2139/ssrn.6860920`. SSRN license line: "The copyright holder has granted SSRN a license. All rights reserved. No reuse allowed without permission." → this record normalizes the idea and cites figures; it does not reproduce the document.
- **What was read for this record (complete document, not abstract/summary):** Abstract, Table of Contents, §1 Introduction, §2 Model Architecture (§2.1 latent factor representation Eqs. 1–2, §2.2 variational inference Eqs. 3–5, §2.3 network components Eqs. 6–9), §3 Data and Implementation (§3.1 Universe Selection, §3.2 Feature Engineering, §3.3 Sample Periods, §3.4 Model Configuration), §4 Empirical Results (§4.1 Prediction Quality, §4.2.1–§4.2.7 all seven strategy definitions, §4.3 Performance Comparison + **Table 1**, §4.4 Analysis of Results, Figure captions 1–6), §5 Latent Factor Analysis (§5.1–§5.4, Eq. 12, Figure captions 7–11), §6 Conclusion, and the full 29-item References list. All pages of the 19-page PDF were extracted and read.
- **Sample period (§3.3):** **January 2019 through December 2024**, split **train 2019-01-01–2022-12-31 (4y), validation 2023 (1y), test 2024 (1y)**. OOS evaluation reported in this record is the single 2024 test year. This is the `source_as_of: 2024-12-31` value (end of data sample, not the paper date).
- **Universe (§3.1):** **50 cryptocurrencies traded on Binance**, "selected based on market capitalization and trading volume", includes BTC/ETH/BNB/SOL plus mid-cap alternatives; **all prices denominated in USDT**. Spot vs. perpetual instrument is **not stated** (`underspecified`); the per-asset selection list, the selection date rule, and any reconstitution schedule are **not stated** (`underspecified`).
- **Transaction-cost / slippage / spread / funding / fill treatment (read across §2, §3, §4 and all of Table 1):** the **only** cost statement in the pinned version is §3.4: **"Transaction costs of 1 basis point per trade are applied in all strategy backtests."** No bid-ask spread, slippage, market impact, maker/taker fee schedule, **funding rate**, **borrow/short fee**, order type, fill model, latency, leverage/margin assumption, or partial-fill treatment appears anywhere in the document, and the paper does not state whether Table 1 returns are gross or net beyond that flat 1 bp. Recorded as **`data gap` / `not stated in source`** — an observation about the pinned 19-page document (whole document read), not an inference from an unavailable section.
- **Core performance numbers (all `source-reported`, every figure table-pinned to Table 1 of the 2026-06-01 / 11 Jun 2026 SSRN version, 2024 test period, starting capital $1,000,000; see Evidence for full provenance):** Momentum Filter **269.8% return, Sharpe 2.12, Max DD −36.2%**; Top-10 Long **133.9%, 1.42, −51.7%**; Vol-Weighted **123.8%, 1.37, −52.7%**; Top-5 Long **106.9%, 1.24, −53.9%**; Score-Weighted **84.5%, 1.07, −41.6%**; Quintile L/S **47.6%, 1.16, −33.4%**; Decile L/S **−0.6%, −0.07, −26.3%**. Prediction quality is reported only qualitatively: RankIC "positive throughout the test period" (§4.1) with **no numeric value** → `data gap`.
- **Publication / preprint status:** SSRN preprint / working paper only (SSRN Electronic Journal, DOI `10.2139/ssrn.6860920`). The SSRN page shows no journal reference, no "last revised" date, and 0 SSRN-listed references/citations as of 2026-09-23; no peer-reviewed publication of this work was found. Recorded as **SSRN preprint, not peer reviewed, publication status not independently confirmed beyond SSRN**.
- **Pre-write deduplication (2026-09-23, full repository, not `git log -20`):** ripgrep (fixed-string and regex) across **all 878 `*.md` records plus `coverage_manifest.csv`** for `6860920`, `10.2139/ssrn.6860920`, the exact title `Cross-Sectional Return Prediction in Cryptocurrency Markets Using Variational`, `FactorVAE`, `Sacha Boyer` → **0 hits for this source identity**. `git log --oneline -20` was inspected separately as a convenience glance only and does not substitute for the repository-wide search.
- **Material distinction from adjacent mechanism neighbors (dedup statement):** the repository already holds three neighbors, none of which shares this source identity or this signal construction: (a) `crypto-cross-sectional-instrumented-latent-mispricing-ipca-2026-09-01.md` — crypto cross-sectional latent model but **IPCA characteristics-based** identification from a peer-reviewed JFQA paper (DOI `10.1017/S0022109025102329`), not a deep generative VAE, different source, different sample; (b) `prism-vq-vector-quantized-discrete-latent-factor-stock-ranking-2026-09-04.md` — discrete **vector-quantized** latent factors for **stock** ranking, different source, different universe; (c) `crypto-convolutional-vae-volatility-surface-completion-anomaly-2026-09-01.md` — a VAE but used for **options volatility-surface completion/arbitrage**, not cross-sectional return ranking, different mechanism and market segment. This record is independent under the dedup contract on at least: **signal construction** (conditional FactorVAE prior-posterior latent ranking over Alpha158 technical features), **universe/market type** (50 Binance USDT crypto pairs), and **horizon** (one-day-ahead cross-sectional forecast, daily portfolio formation).

## Economic mechanism

### Source-reported

The author's thesis (§1, §6) is that cross-sectional return predictability observed in equities transfers to cryptocurrency markets, and that a deep generative latent-factor model can extract it. The stated rationale: crypto assets trade continuously, are extremely volatile, and lack fundamental valuation anchors (§1), so technical price/volume characteristics cross-sectionally standardized per date should carry ranking information; the FactorVAE architecture (Duan, Wang, Zhang & Li, AAAI 2022, the paper's ref [9]) combines probabilistic factor structure with neural non-linearity, letting the model "explicitly model uncertainty in predictions — a crucial consideration given the low signal-to-noise ratio" of returns (§1). Interpretability is claimed as the middle ground of VAE latent factors (§1, §5). The seven strategy variants are presented as four economic channels: directional selection (Strategies 1, 3), market-neutral arbitrage of the ranking (Strategies 2, 4), risk-adjusted sizing (Strategies 5, 7), and **market timing via BTC's own trend as a regime filter** (Strategy 6). The author reports the timing overlay as the dominant contributor (§4.4: "By conditioning trades on Bitcoin's trend direction, this strategy avoids exposure during adverse market conditions").

### Research interpretation

- **Hypothesis in falsifiable form:** a conditional-VAE latent ranking built only from lagged price/volume characteristics has positive one-day-ahead cross-sectional RankIC in a 50-coin Binance universe, and long-short or long-only portfolios formed on that ranking earn positive returns after realistic crypto costs; the reported edge is (a) the VAE ranking and (b) a BTC-momentum cash filter, and these two contributions must be separable by ablation.
- **Component roles (hybrid structure as normalized):**
  - **Regime / timing filter:** hold cash (Strategy 6) when **BTC 20-day momentum is negative** (§4.2.6); `research-proposed` if applied to any other strategy — the source applies it only to Top-5.
  - **Primary signal:** one-day-ahead predicted return `μ̂` per asset from the FactorVAE **prior** `p(z|x)` (inference-time distribution; the author states only the prior is used at inference "ensuring no forward-looking information leakage", §2.2), produced by GRU asset encoder (Eq. 6) → attention portfolio aggregation (Eq. 7) → decoder mean/variance (Eqs. 8–9).
  - **Signal inputs:** 158 Qlib **Alpha158** technical features from OHLCV (momentum at 5/10/20/30/60 days, volatility/range, volume patterns and price-volume correlation, mean reversion/trend), **cross-sectionally standardized within each date** (§3.2); sequence length **20 days** (§3.4).
  - **Long entry / short entry / sizing:** per §4.2.1–§4.2.7 (Top-5 EW; quintile top-20%/bottom-20% L/S; Top-10 EW; decile top-10%/bottom-10% L/S; Top-5 weighted `w_i ∝ 1/σ_i^(20)`; Top-5 with BTC-momentum cash filter; Top-5 weighted `w_i ∝ μ_i − min_j μ_j + ε`).
  - **Exit / holding period:** **"Each day, we form…"** (§4.2.1) implies daily formation / ≈1-day holding for Strategy 1; explicit holding-period, rebalance-price and exit statements for the other six strategies are **not given** → `underspecified`.
  - **Risk management:** no stop-loss, position limit, vol target or leverage cap is specified by the source; the only risk controls present are the inverse-vol weighting (Strategy 5) and the BTC cash filter (Strategy 6). This absence is recorded, not repaired.
  - **Model configuration (§3.4):** 32 latent factors, hidden dimension 64, sequence length 20 days, 64 dynamically constructed training portfolios, 20 epochs with early stopping on validation loss; temporal stabilization regularizer `L_stab = L + λ1·KL(q_t‖q_{t−1}) + λ2·‖β_t − β_{t−1}‖²` (Eq. 12, §5.1) — **λ1, λ2 values not stated** → `underspecified`.
- **Do not assume every component is alpha:** the source's own Table 1 shows the extreme-quantile market-neutral variant (Decile L/S) **loses** money (−0.6%, Sharpe −0.07), i.e. the ranking's tails add noise once portfolio construction is aggressive; and the largest single reported improvement comes from a **non-model** overlay (BTC 20-day momentum), which is a well-known public signal — whether the VAE ranking adds anything on top of that overlay is **not ablated in the source** and is the central falsification item below.

## Signal

- **Formation timestamp:** daily formation ("Each day…", §4.2.1). The exact observation cut-off, candle timezone/boundary convention (24/7 market → which daily close), and the tradable timestamp are **not stated** → `underspecified`; `research-proposed` operationalization (for testing only): form the signal on the Binance daily close in UTC and trade at the next day's open.
- **Lookback:** 20-day feature sequence (§3.4) over Alpha158 features whose own momentum windows are 5/10/20/30/60 days (§3.2); warm-up period not stated → `underspecified`. Cross-sectional standardization is within-date across the 50 assets (§3.2).
- **Model:** FactorVAE adaptation — conditional VAE with posterior `q(z|x,y)` (conditions on realized future returns during training) and prior `p(z|x)`; loss `L = −E_q[log p(y|z,x)] + γ·KL(q‖p)` (Eq. 5); **γ not stated** → `underspecified`. K = 32 latent factors (§3.4).
- **Long entry (source-specified):** Strategy 1 = equal weight on the 5 highest-`μ̂` coins; Strategy 3 = equal weight on top 10; Strategy 5 = Top-5 with `w_i ∝ 1/σ_i^(20)` (20-day rolling std); Strategy 7 = Top-5 with `w_i ∝ μ_i − min_j μ_j + ε`; Strategy 6 = Strategy 1 but **cash when BTC 20-day momentum < 0** (§4.2.6; the momentum reference price for the BTC 20-day window is not stated → `underspecified`).
- **Short entry (source-specified):** Strategy 2 = short the bottom 20% of the ranking; Strategy 4 = short the bottom 10% (with 50 coins, ≈5 coins per decile leg). Leg gross notional, whether the book is dollar-neutral, and whether shorts are spot-margin or perpetual are **not stated** → `underspecified`.
- **Exit / re-entry:** not explicitly stated; daily re-formation implies daily exit for Strategy 1. No stop, no take-profit, no max-holding rule is given.
- **Parameters:** all seven strategy definitions, Top-5/Top-10/quintile/decile cuts, `σ(20)`, BTC 20-day momentum, 32/64/64/20/20-epoch model config, 1 bp cost — all source-specified (§3.4, §4.2). Everything else (execution price, rebalance price, L/S sizing, γ, λ1/λ2, universe list) is absent from the source → marked above rather than filled in.
- **Reproducibility verdict:** the signal is **partially reconstructable** — strategy construction is clear, model hyperparameters are mostly given, but the exact universe constituents, execution convention, and several training constants are missing → **not fully reproducible as stated** (`underspecified`).

## Required data

- **Instrument / universe:** 50 cryptocurrencies on **Binance**, USDT-quoted (§3.1); constituents and selection/reconstitution rule not stated → `underspecified`; `research-proposed` for testing: build the list point-in-time from trailing 30-day average quote volume and market cap to remove survivorship risk.
- **Venue / market type:** Binance; **spot vs. perpetual not stated** → `underspecified` (matters materially for short legs, funding and borrow).
- **Timeframe:** daily bars over 2019-01 → 2024-12 (§3.3), 20-day sequence context (§3.4); 24/7 session, daily boundary convention not stated → `data gap`.
- **Fields:** OHLCV only (§3.2) → Open, High, Low, Close, Volume, transformed into 158 Alpha158 indicators. **No funding rate, open interest, order book, trades/aggressor, on-chain, sentiment or borrow data is used** (§3.2) — the paper explicitly lists funding rates and on-chain/sentiment data as *future* work (§6).
- **Point-in-time:** the author asserts prior-only inference avoids forward-looking leakage (§2.2); the cross-sectional standardization uses same-day cross-section (fine for ranking, but the tradability of the daily cut-off is unstated → `underspecified`). Train/validation/test boundaries are explicit (§3.3).
- **Missing-data:** handling of delisted/hard-failed coins, stale prices, or assets entering/leaving the 50 is **not stated** → `data gap`.
- **Cost fields:** flat 1 bp/trade is modeled (§3.4); spread, slippage, impact, funding, borrow are **not observed, not modeled, not stated** → `data gap`.

## Execution assumptions

- **Source assumptions:** daily portfolio formation (§4.2.1); flat **1 bp per trade** cost (§3.4) applied in all strategy backtests. Order type, fill price, same-bar vs next-bar execution, latency, participation/capacity limits, leverage/margin, shorting mechanics, funding, borrow availability, partial fills and failure handling are **not stated anywhere in the pinned version** → `data gap` / `not stated in source`.
- **Scout assumptions (`research-proposed`, for testing only, not source-reported):** signal on UTC daily close → trade next daily open; taker fills; universe rebuilt point-in-time; L/S books run 1× gross each side; capacity treated as unbounded only as a null to be broken by a participation cap.
- **Tradability caveat:** because gross, net, spread, funding and borrow treatment are unstated beyond the 1 bp line, **no Table 1 figure in this record may be read as net-of-realistic-cost performance**.

## Evidence

### Source-reported

All figures below are `source-reported` from the pinned SSRN 19-page PDF (SHA-256 `7278f652…846c5d876`), **Table 1: "Strategy Performance Summary (2024 Test Period, starting capital $1,000,000)"**, costs = 1 bp/trade (§3.4). None has been independently reproduced.

| # | Strategy (§4.2) | Final equity | Return | Sharpe | Max DD | Approach |
|---|---|---|---|---|---|---|
| 1 | Top-5 Long (EW) | $2,069,122 | 106.9% | 1.24 | −53.9% | Directional |
| 2 | Quintile Long-Short | $1,475,707 | 47.6% | 1.16 | −33.4% | Market-neutral |
| 3 | Top-10 Long (EW) | $2,338,648 | 133.9% | 1.42 | −51.7% | Diversified |
| 4 | Decile Long-Short | $993,957 | −0.6% | −0.07 | −26.3% | Aggressive L/S |
| 5 | Volatility-Weighted (Top-5, `1/σ20`) | $2,237,733 | 123.8% | 1.37 | −52.7% | Risk-adjusted |
| 6 | **Momentum Filter** (Top-5 + BTC 20d cash) | $3,697,680 | **269.8%** | **2.12** | −36.2% | Market-timing |
| 7 | Score-Weighted (Top-5) | $1,844,908 | 84.5% | 1.07 | −41.6% | Confidence-based |

- Prediction quality (§4.1): RankIC (Spearman of predicted vs. realized cross-sectional returns) is stated to be **positive throughout the test period**, but **no mean/median value, standard error or t-statistic is given** → `data gap`.
- Abstract-level claim: "six out of seven strategies achieving positive Sharpe ratios exceeding 1.0" — consistent with Table 1 (rows 1, 2, 3, 5, 6, 7 ≥ 1.07; row 4 = −0.07).
- Author's reading (§4.4): momentum filter dominates and reduces drawdown; Top-10 beats Top-5 on both return and Sharpe (diversification > concentration); Quintile L/S has best directional-side drawdown protection (−33.4%); Decile L/S fails because "extreme quantile selection introduces noise".
- Latent-factor stabilization (§5): temporal regularization yields smooth factor trajectories, persistent common factors with fast-adjusting loadings; **stability metrics (adjacent-day factor correlation, L2 distance) are described qualitatively with no numeric table** → `data gap`.
- Sharpe computation convention (annualization factor, risk-free rate, daily-return basis) **not stated** → `underspecified`.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Source-reported, inside Table 1:** the **Decile Long-Short construction loses money** (−0.6%, Sharpe −0.07) — the ranking's extreme tails do not survive aggressive market-neutral construction (§4.4).
- **Source-reported, inside Table 1:** maximum drawdowns of **−53.9% / −51.7% / −52.7%** for Top-5 / Top-10 / Vol-Weighted despite Sharpe > 1.2 — the long-only variants carry near-halving drawdowns in the 2024 test year.
- **Single-year out-of-sample, seven strategies plus multiple design choices, no multiple-testing control:** test = calendar 2024 only (§3.3); no deflated Sharpe / probability-of-backtest-overfitting / walk-forward evidence anywhere in the document → `data gap`; a 1-year window cannot distinguish skill from the 2024 crypto regime (BTC-trend filter specifically benefits from trend-shaped years).
- **Cost realism (`research interpretation`, not a source claim):** 1 bp/trade flat (§3.4) is far below a plausible all-in Binance taker round-trip (commission + spread) for a daily-rebalanced 5-coin book; turnover and realized cost curves are not reported → cost sensitivity is **untested in the source**; the falsification ladder below is `research-defined`.
- **Funding and borrow absent (`data gap`):** the two short-selling strategies (2, 4) are evaluated with no funding-rate or borrow-cost line even though perpetual funding (if perps were used) or margin borrow (if spot) is a first-order cost for daily-held shorts; instrument type is itself unstated.
- **Universe survivorship / look-ahead risk (`underspecified`):** "50 cryptocurrencies … selected based on market capitalization and trading volume" (§3.1) gives no as-of rule; if constituents were chosen ex-post over 2019–2024, every figure in Table 1 inherits survivorship bias. Not provable from the document either way — recorded as a gap, not asserted as an error.
- **The headline improvement may not require the VAE (`research interpretation`):** Strategy 6 = Strategy 1 + a public BTC 20-day-momentum cash filter, and it raises Sharpe from 1.24 → 2.12. The source performs **no ablation** of the overlay on a non-model portfolio, so the marginal contribution of the FactorVAE ranking inside the headline number is undetermined.
- **External contrary context (separate source, abstract-level only in this run):** Cakici, Shahzad, Będowska-Sójka & Zaremba (2024), "Machine learning and the cross-section of cryptocurrency returns", *International Review of Financial Analysis* 94 (RePEc `ideas.repec.org/a/eee/finana/v94y2024ics1057521924001765.html`), report that ML models produce economic gains in crypto but that **"the benefits from model complexity are limited"** — i.e. incremental value from deep architectures over simple models is contested in the adjacent literature. Full text not read in this run (`data gap`); cited as context only, its numbers are not merged with SSRN 6860920.
- **Source quality:** single-author, unrefereed SSRN preprint, 19 pages, 0 SSRN citations as of 2026-09-23; no independent replication or press coverage identified.

## Falsification plan

All thresholds below are Scout operationalizations, labeled `research-defined`; all rebuild/execution choices are `research-proposed`. Failure action for every item: record fails to advance beyond research-only and is not submitted to the candidate pool.

1. **Point-in-time universe rebuild (`research-proposed`):** reconstruct the 50-coin panel with trailing 30-day volume/market-cap membership at each month-end, dropping coins before listing and after delisting/failure. **Fail rule (`research-defined`):** Momentum-Filter 2024 Sharpe falls by >50% vs. the paper's 2.12 → survivorship was material.
2. **True holdout (`research-defined`):** retrain per the source split and evaluate unchanged rules on 2025-01-01 → 2026-12-31. **Fail:** Momentum-Filter Sharpe < 1.0 in either calendar year, or RankIC ≤ 0 for two consecutive quarters.
3. **Cost ladder (`research-defined`):** rerun all seven strategies at 1/5/10/20 bps one-way plus a spread proxy (top-of-book distance on the daily close). **Fail:** the headline variant (Strategy 6) Sharpe < 1.0 at 10 bps one-way.
4. **Funding/borrow stress (`research-defined`):** for Strategies 2 and 4 on perps, add realized funding and a borrow/fee proxy. **Fail:** Quintile L/S net Sharpe ≤ 0 at median funding.
5. **Execution timing (`research-proposed`):** close-formed signal executed next-day open vs. same-day close. **Fail (`research-defined`):** Strategy-6 Sharpe halves under next-day-open execution → look-ahead in the daily cut-off.
6. **Shuffled-rank placebo (`research-proposed` / `research-defined`):** 1,000 daily cross-sectional shuffles of `μ̂`, same portfolio code. **Fail:** actual RankIC does not exceed the 95th percentile of the placebo distribution, or actual strategy Sharpe ≤ placebo median.
7. **Overlay-only ablation (`research-defined`):** run BTC 20-day momentum cash filter on (a) buy-and-hold BTC and (b) Top-10 without the model. **Fail:** the overlay alone delivers ≥ 80% of Strategy 6's excess Sharpe over the unfiltered Top-5 → the VAE ranking is not the alpha.
8. **Complexity baseline (`research-defined`):** replace FactorVAE with a linear cross-sectional rank of the same 158 features and with the Cakici-et-al.-style simple-ML baseline. **Fail:** FactorVAE RankIC ≤ simple-baseline RankIC → deep generative structure adds nothing (matches the external contrary context).
9. **Multiple-testing discipline (`research-defined`):** deflated Sharpe ratio ≥ 0.95 across all seven strategies plus any retuning of γ, λ1/λ2, K, sequence length. **Fail:** DSR < 0.95 → headline is selection-biased.
10. **Instrument/venue portability (`research-defined`):** repeat on (a) Binance spot and (b) a second venue's perpetuals with the identical signal. **Fail:** sign of Strategy-6 excess return flips across venue/instrument → microstructure artifact, not cross-sectional alpha.

## Crypto portability

**direct** — the source is itself a crypto study (50 Binance USDT pairs, 2019–2024, §3.1), so no porting step is required for crypto. Caveats that still apply inside crypto: **spot vs. perpetual is unstated** (short-leg mechanics, funding and borrow differ fundamentally between them → `data gap`); **24/7 session** daily-boundary convention is unstated (candle close timezone, weekend/holiday effects); **single-venue** universe ignores exchange fragmentation, listing/delisting churn and index-price vs. last-price basis; **funding and borrow are unmodeled** (§3.4 models only 1 bp); **24/7 liquidation/leverage** risk does not appear because leverage is unstated; survivorship in the 50-coin list is unresolved (§3.1). Not applicable to equities/commodities claims — none are made. Crypto portability is not authorization to trade.

## Limitations

- `underspecified`: spot vs. perpetual instrument; universe constituent list and as-of/reconstitution rule; signal tradability timestamp and daily boundary; execution price and next-bar/same-bar convention; holding/rebalance rules for Strategies 2–7; L/S gross and neutralization; loss weight γ; stabilization weights λ1/λ2; BTC-momentum reference price; Sharpe annualization convention.
- `data gap`: numeric RankIC (and any t-stat); factor-stability metrics; funding/borrow/slippage/spread/impact/latency models; gross-vs-net wording beyond the 1 bp line; missing-data/delisting handling; turnover and capacity; multiple-testing controls; ablation of the VAE ranking vs. the BTC-momentum overlay.
- `not stated in source`: order type, fill model, leverage/margin, position limits, stops, partial fills.
- `not independently reproduced`: every figure in Table 1 and all qualitative RankIC/stability claims.
- `unproven`: generalization beyond the single 2024 test year; superiority of the deep generative model over simple cross-sectional baselines.
- Source-quality / publication-bias: single-author SSRN preprint without peer review; seven strategy variants reported from one model with no pre-registration or holdout discipline visible in the document; adjacent literature (`data gap`, abstract-level) suggests limited gains from model complexity in crypto cross-sections.
- Incremental threshold check: this record is written because it is a **new family for this repository** — deep generative (conditional-VAE) cross-sectional ranking on a Binance 50-coin panel with a regime-filter ablation gap — distinct from the existing IPCA crypto-latent and equity VQ-latent records named in Provenance.

## Implementation status

`implementation_status: not-implemented`. Nothing in this record has been implemented in our research stack: no FactorVAE training run, no Alpha158 crypto panel build, no backtest, no Qlib full-backtest validation, and no Paper / Testnet / Live activity has occurred. This document is a normalized research capture of an external preprint only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this record does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; or approved for implementation, paper trading, testnet, or live trading. Confidence `medium` describes confidence in the *research interpretation* of the pinned source — not confidence that the strategy is profitable.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` — canonical schema contract, read directly from Wiki Brain this run (sha256 `4561578a…ff6ff2fcaa7`).
- Repository neighbors referenced by **file name only** (repo staging files, **not** Wiki links, and **not** written to Wiki Brain by this run): `crypto-cross-sectional-instrumented-latent-mispricing-ipca-2026-09-01.md`, `prism-vq-vector-quantized-discrete-latent-factor-stock-ranking-2026-09-04.md`, `crypto-convolutional-vae-volatility-surface-completion-anomaly-2026-09-01.md`. A repository-wide search found no existing record for this source identity; no other related Wiki page was confirmed to exist, so none is linked.

## Sources

- **Primary (pinned):** Boyer, Sacha. *Cross-Sectional Return Prediction in Cryptocurrency Markets Using Variational Latent Factor Models*. SSRN abstract 6860920, DOI `10.2139/ssrn.6860920`; Date Written June 01, 2026; Posted 11 Jun 2026; 19 pages. Landing: `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6860920`. Delivery PDF: `https://papers.ssrn.com/sol3/Delivery.cfm/6860920.pdf?abstractid=6860920&mirid=1` (retrieved 2026-09-23, 1,778,056 bytes, SHA-256 `7278f652e7ce69f6dee95cca38052378c55904d14ea16af71173570846c5d876`). All performance figures trace to Table 1; all strategy definitions to §4.2.1–§4.2.7; the 1 bp cost line to §3.4; universe/sample to §3.1/§3.3.
- **Method origin (as cited by the primary source, ref [9]):** Duan, Y., Wang, L., Zhang, Q., & Li, J. (2022). *FactorVAE: A Probabilistic Dynamic Factor Model Based on VAE for Predicting Cross-Sectional Stock Returns*. Proceedings of the AAAI Conference on Artificial Intelligence, 36(4), 4468–4476 (AAAI DOI `10.1609/aaai.v36i4.20369`, verified via the AAAI OJS page on 2026-09-23). Cited as architecture provenance only; **no number from the AAAI paper is imported into this record**.
- **Feature library (as cited by the primary source, §3.2):** Qlib **Alpha158** feature set (Microsoft Qlib), used to generate the 158 technical indicators.
- **External contrary context (abstract-level, this run):** Cakici, N., Shahzad, S. J. H., Będowska-Sójka, B., & Zaremba, A. (2024). *Machine learning and the cross-section of cryptocurrency returns*. International Review of Financial Analysis, 94. RePEc: `https://ideas.repec.org/a/eee/finana/v94y2024ics1057521924001765.html` — quoted only for the "benefits from model complexity are limited" finding; full text not read (`data gap`).
- **Discovery surfaces used (not evidence):** arXiv API q-fin/cs.CE recent listing scan and public web search on 2026-09-23; every empirical claim above comes from the pinned SSRN PDF or the SSRN landing page, both read directly.
