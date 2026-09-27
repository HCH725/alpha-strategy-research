---
schema: strategy-research-record-v1
title: "CryptoGAT Cross-Asset Graph-Attention Pure-Price Cryptocurrency Forecasting → Daily Top-5 Long-Only Rotation on 66 Binance USDT Pairs"
created: 2026-09-27
updated: 2026-09-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - cryptocurrency
  - graph-neural-network
  - graph-attention
  - cross-sectional
  - binance
  - pure-price
  - top-k-rotation
  - deep-learning
  - transaction-cost-sensitivity
status: research-only
confidence: medium
source_as_of: 2026-06-26
sources:
  - "arXiv:2606.27670v1 [cs.CE, q-fin.ST], 'CryptoGAT: Are Time Series Models Effective for Cryptocurrency Forecasting?', Yu Peng, Matloob Khushi, Josiah Poon, submitted Fri 26 Jun 2026 03:05:02 UTC. https://arxiv.org/abs/2606.27670 (DataCite DOI: https://doi.org/10.48550/arXiv.2606.27670)"
  - "Pinned primary PDF: https://arxiv.org/pdf/2606.27670v1 — 1,560,076 bytes, 10 pages, SHA-256 f377f86618c2d6a4a43380613905ce4b4847f04de71c39420f2039c9ecb1fa16, downloaded 2026-09-27"
  - "Pinned primary HTML: https://arxiv.org/html/2606.27670v1 — 216,567 bytes, SHA-256 5492b00b1ba0cb616312319afd6a93bb73de28ad9657036b2c3956485fde95c3, downloaded 2026-09-27"
  - "Official implementation: https://github.com/FanBroWell/CryptoGAT, full commit SHA 00292fdda64c3f50296103d01c74bfa937e08851 (2026-07-11T03:24:54Z), MIT, pinned README / training / evaluation / graph code read for this record"
  - "Dataset mirror referenced only by the repository README (not by the paper): https://huggingface.co/datasets/CharlieYPeng/cryptogat-crypto-1d — HTTP 200 checked 2026-09-27"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# CryptoGAT Cross-Asset Graph-Attention Pure-Price Cryptocurrency Forecasting → Daily Top-5 Long-Only Rotation on 66 Binance USDT Pairs

## Provenance

- **Primary source:** arXiv preprint **arXiv:2606.27670v1**, *"CryptoGAT: Are Time Series Models Effective for Cryptocurrency Forecasting?"*, categories `cs.CE` (primary) and `q-fin.ST` (cross-list).
- **Authors (exactly as printed on the PDF title block and in the arXiv author list):** Yu Peng (1st; School of Computer Science, University of Sydney, ypen0278@uni.sydney.edu.au); Matloob Khushi (2nd; Department of Computer Science, Brunel University London, Matloob.Khushi@brunel.ac.uk); Josiah Poon (3rd; School of Computer Science, University of Sydney, josiah.poon@sydney.edu.au). No equal-contribution, corresponding-author or funding footnote appears in the source → per-author role = **data gap**.
- **Version / date:** submission history shows a single version `[v1] Fri, 26 Jun 2026 03:05:02 UTC (1,479 KB)`; the `abs` page carries **Comments: "Under review"**, **no journal-ref field** and **no DOI field** → **preprint only, under review, not peer reviewed at capture time**. DataCite (`10.48550/arXiv.2606.27670`) returns `resourceTypeGeneral: Preprint`, `version: 1`, dates `Submitted 2026-06-26T03:05:02Z (v1)` / `Updated 2026-06-29T00:17:06Z (v1)`, registered 2026-06-29T01:41:45Z → **no v2 exists**. Rights: `arXiv.org perpetual, non-exclusive license` (abs + DataCite `rightsList` + PDF metadata `/License`) — **not** CC BY, so only claims, printed figures and code are normalised here; no source text is reproduced wholesale.
- **Pinned artefacts (both downloaded and read end to end on 2026-09-27):**
  - PDF: `https://arxiv.org/pdf/2606.27670v1` — 1,560,076 bytes, **10 pages**, SHA-256 `f377f86618c2d6a4a43380613905ce4b4847f04de71c39420f2039c9ecb1fa16`; pypdf metadata `/Author` = `Yu Peng; Matloob Khushi; Josiah Poon`, `/arXivID` = `https://arxiv.org/abs/2606.27670v1`, `/DOI` = `https://doi.org/10.48550/arXiv.2606.27670`.
  - HTML: `https://arxiv.org/html/2606.27670v1` — 216,567 bytes, SHA-256 `5492b00b1ba0cb616312319afd6a93bb73de28ad9657036b2c3956485fde95c3`.
  - Both renderings were cross-checked cell by cell for **Tables I–VI**; every number quoted below appears in **both** renderings (PDF page map: Fig. 1 p.3; Tables I–II p.5; Tables III–IV p.6; Figs. 2–4 p.7; Table V p.8; Table VI p.10).
  - Size quirk recorded, not reconciled: the submission history lists `(1,479 KB)` ≈ 1,514,496 bytes while the bytes served on 2026-09-27 are 1,560,076 (arXiv-side re-generation); the recorded SHA-256 is of the bytes served on 2026-09-27.
- **Primary-source checksum coverage (read directly, section level):** Abstract; §I Introduction; §II Related Work; §III-A Problem Definition (Eq. 1), §III-B Time Series Models (Eq. 2, StockMixer), §III-C CryptoGAT/FGAT (Eq. 3–5, Algorithm 1); §IV-A Experimental Setup (Datasets, Implementation Details, Metrics, Algorithm 2, Baselines), §IV-B Overall Comparison (Table I), §IV-C Comprehensive Portfolio Evaluation (Tables II–III); §V-A Ablation (Table IV), §V-B input-sequence analysis (Fig. 2), §V-C dataset analysis (Figs. 3–4, Table V); §VI Conclusion; References (incl. the cost reference [42]); Appendix A-A baselines and A-B hyper-parameter settings (Table VI); Tables I–VI; Figures 1–4; Algorithms 1–2.
- **Code provenance (read, not just linked):** `https://github.com/FanBroWell/CryptoGAT` at full commit SHA **`00292fdda64c3f50296103d01c74bfa937e08851`** (2026-07-11T03:24:54Z, "Move dataset link to README footer"; default branch `main`; MIT; repository created 2026-06-12, last push 2026-07-11, 7 stars when checked 2026-09-27). Tree = 89 blobs: `src/train_gat_crypto.py`, `src/train_gat_enhanced.py`, `src/evaluator.py`, `src/models/gat.py`, `src/process_crypto_ALL.py`, `src_Feature/feature_engineer.py`, `src_Feature/process_crypto_enhanced.py`, `requirements.txt`, `CITATION.cff`, `README.md`, `LICENSE`, `assets/cryptogat-overview-results.png`, plus `dataset/` (68 `*USDT_daily_1000days.csv` files and 8 pickles `eod/gt/mask/price_data.pkl`). README at that commit also links `https://huggingface.co/datasets/CharlieYPeng/cryptogat-crypto-1d` (HTTP 200 on 2026-09-27) and carries the badge `Status: Under Review`. The Hugging Face mirror is **repository-only provenance** — the paper never mentions it.
- **Repository deduplication audit (hidden-inclusive, pre-write, 2026-09-27):** ripgrep `--hidden -g '!.git'` over the whole checkout scanned **2,613 files** (all `*.md`, `coverage_manifest.csv`, `.agents/`, `.mimo-worktrees/`, `.hermes/`) for each of `2606.27670`, `10.48550/arXiv.2606.27670`, `CryptoGAT`, the exact title `Are Time Series Models Effective for Cryptocurrency`, `CharlieYPeng`, `cryptogat-crypto-1d` → **every pattern returned zero matches before this write**, and `coverage_manifest.csv` contains no row for this source. Secondary/adjacency scans: `Matloob|Josiah Poon|Yu Peng` → 3 files, **all the same-record CAST capture** (`cast-cross-asset-state-space-collaborative-kalman-mpc-drawdown-control-2026-09-16.md` plus its two `.mimo-worktrees` copies); `graph attention` → 12 files (4 distinct equity records × 3 checkouts); `cross-asset graph` → **0 hits**; loose `crypto + graph attention` scans returned only unrelated prose. `git log --oneline -20` was inspected separately as a convenience glance only, never as dedup.
- **Four-axis distinction (why this is not a duplicate):**
  1. *Source identity* — `arXiv:2606.27670` / `FanBroWell/CryptoGAT` / `CharlieYPeng/cryptogat-crypto-1d` appear nowhere in the repository. The only same-author record is `cast-cross-asset-state-space-collaborative-kalman-mpc-drawdown-control-2026-09-16` (`arXiv:2609.14205`, Peng/Khushi/Poon) — a **different paper**.
  2. *Mechanism* — a **static Pearson-correlation graph over crypto price levels + graph-attention pooling with no temporal backbone**, versus CAST's cross-asset **state-space collaborative Kalman filter with MPC drawdown control**, versus the repository's equity graph-attention records (analyst-coverage network spillover; STN-TGAT soft-threshold Top-K; THGNN/SPONGEsym correlation forecasting), none of which is a crypto pure-price forecaster.
  3. *Signal construction* — daily **long-only top-5 equal-weight rotation** on predicted 1-day returns of 66 Binance USDT pairs, versus long-short equity graph ranks, Kalman spread positions, or factor-model quintiles elsewhere.
  4. *Material data dependency* — **Binance USDT daily OHLCV only** (no on-chain, no sentiment, no order book, no macro) plus a graph adjacency derived from the same price history; no other record depends on that combination.

## Economic mechanism

### Source-reported

The authors' stated rationale (§I, §III-B/§III-C, §V-C): time-series models (LSTM/GRU/Transformers) work on equities because equity returns carry exploitable *temporal* structure, but cryptocurrency pure-price series are dominated by *cross-asset* co-movement, so the forecasting task is mis-specified as a temporal problem. The source supports this with three empirical claims (all `source-reported`, §V-C): (i) **predictability** — AR models on 1,026 Nasdaq stocks versus crypto give a standard deviation of R² more than **5×** higher for Nasdaq, and crypto R² "consistently below 0.1" (Fig. 3); (ii) **statistical coupling** — average pairwise Pearson correlation **0.528** for crypto vs **0.200** for stocks, with **65.78%** of crypto pairs at r > 0.5 vs **2.39%** of stock pairs (Fig. 4a); graph density at threshold τ = 0.5 stays **0.66** for crypto while Nasdaq falls from ~0.8 to ~0.2 (Fig. 4b); PC1 explains **55%** of crypto variance vs **16%** for Nasdaq and the top-20 PCs exceed 80% (Fig. 4c); (iii) **architecture ablation** — adding StockMixer's time-mixing module to the GAT *hurts* on crypto (IC 0.037 → 0.006) while it is the most important module on Nasdaq (Table IV), and a sixth "market-dominant factor" input does not let temporal baselines catch up (Table V). CryptoGAT therefore recasts the task as `y_t ≈ g(G, f(X_{t−1}))` (Eq. 3): build an undirected weighted graph from pairwise |Pearson correlation| of prices above threshold τ (Algorithm 1), then let a graph-attention layer (Eq. 4–5) aggregate neighbour representations into each asset's next-day score. FGAT adds StockMixer-style indicator mixing in front of the same GAT. The source reports that this "outperforms various state-of-the-art forecasting methods with a notable margin".

### Research interpretation

Stated as a falsifiable hypothesis, not as an established fact:

- **Signal component (the only alpha claim):** cross-sectional information flowing through a correlation graph — *which other coins' price paths move with this coin* — carries next-day predictive content for a crypto cross-section that each asset's own recent history does not. The decisive control is a **rewired/degree-preserving or identity graph**: if a random graph with the same degree distribution scores the same, the mechanism is generic cross-sectional pooling, not correlation structure.
- **Regime component:** **none** — the source has no regime filter, no volatility gate, no market-direction overlay.
- **Sizing / risk component (not alpha):** long-only, equal weight `w = 1/K` with `K = 5`, full daily re-strike, no vol targeting, no stop, no take-profit, no leverage, no shorts (nothing in the source describes a short book). Cash is implicitly the remainder (5 of 66 names held).
- Component roles: *(Graph construction: static |Pearson|>τ on prices) + (Signal: GAT/FGAT predicted next-day return) + (Sizing: equal-weight top-5, daily) + (Risk/exit: none printed)*. The source's own ablations are the tool for asking whether the graph component contributes; the source does **not** claim every component adds alpha.
- Everything not printed by the source (execution timing, graph-refresh policy, cost acceptance cutoffs, all thresholds below) is labelled **research-proposed** or **research-defined**.

## Signal

- **Target / formation timestamp (source-reported, §III-A Eq. 1):** predict the next day's close and form the 1-day return ratio `r_i^t = (p_i^t − p_i^{t−1}) / p_i^{t−1}`. Input is the historical OHLCV window; the model therefore scores asset *i* for the return that begins at the last observed close. **Timezone, daily candle boundary and publication convention are not stated in source** → `data gap` (this is a 24/7 market; the only session statement anywhere in the paper is `√365` in Algorithm 2).
- **Input/label alignment in the pinned code (source-reported from commit `00292fd`):** `get_batch` feeds `eod_data[:, offset : offset+30, :]` and labels `gt_data[:, offset+30]`, where `gt[i] = (close[i] − close[i−1]) / close[i−1]`. The input window therefore ends at close *t* and the label is the close *t* → close *t+1* return: **no same-row label leakage in the slicing**. Whether orders are struck at that same close *t* (the last input bar) or at a later price is **never stated in the source** → same-bar vs next-bar = `underspecified`.
- **Lookback:** **30 days** (Table VI; `lookback_length = 30` in both training scripts); sweep `L ∈ {5,10,15,30,60}` reported only in Fig. 2. Warm-up and endpoint inclusivity: not stated in source (first row is dropped by preprocessing, `mask[0]=0`).
- **Features (5, source-reported §IV-A + `src/process_crypto_ALL.py`):** `open/close_prev`, `high/close_prev`, `low/close_prev`, `close/close_prev`, `volume / 5-day-MA(volume)`; the code additionally clips features to `[0.5, 2.0]`, maps NaN→1.0 and runs `ffill().bfill()` (see Negative evidence 17).
- **Graph (source-reported, Algorithm 1):** Pearson correlation on the price matrix `P ∈ R^{N×T_train}`, keep `|C_ij| > τ`, store `|C_ij|` as a weighted undirected edge, self-loop 1.0. **The value of τ is never printed in the paper** (Table VI omits it) → the paper's algorithm is not reproducible from the paper alone. The pinned code supplies `correlation_threshold = 0.5` and `np.abs(corr)`, and computes it on the **entire** `price_data` tensor (see Negative evidence 2).
- **Model / training parameters (source-reported Table VI + §IV-A, plus pinned code):** lookback 30; learning rate 0.00025; dropout 0; 100 epochs; hidden size 64; split 60/20/20; MSE loss; code adds `num_layers = 2`, `num_graph_layer = 2`, Adam `weight_decay = 0`, `ReduceLROnPlateau(factor 0.5, patience 10)`, `RANDOM_SEED = 123456789`, split indices `valid_index = 599`, `test_index = 799`. FGAT hyperparameters are in `src_Feature/` and are **not printed in the paper** → `data gap`.
- **Trading rule (source-reported, Algorithm 2):** each trading day rank assets by predicted return descending, take the **top K = 5**, equal weight `1/5`, hold for one day, `r_{p,t}` = mean of those five assets' actual same-day returns; `Ann.SR = mean(r_p)/std(r_p) × √365`. Long-only; no shorts, no leverage, no cash yield, no re-entry rule beyond the daily re-strike.
- **Fully specified?** **Partially underspecified.** Reconstructible: target, features, lookback, graph recipe (with code-supplied τ), portfolio rule, K, annualisation. Missing from the source: execution price/order type/latency, graph refresh policy, τ, FGAT settings, exact test calendar, risk-free rate value, capacity/liquidity rules.

## Required data

- **Instrument / universe (source-reported §IV-A):** start from the top 1,000 cryptocurrencies by market capitalisation, then filter (1) market cap > **$200M**, (2) **USDT-denominated trading pairs only**, (3) continuous daily data with no missing values → **66 major cryptocurrencies**, daily, **15/04/2023 – 08/01/2026**, time-aligned to **999 trading days**. The source itself notes that fewer than 20 of the 1,000 had continuous records prior to 2019.
- **Venue / market type:** **Binance**. Market type = "USDT-denominated trading pairs" — **spot vs perpetual is never stated** → `data gap`; this determines whether funding, mark/index price and liquidation are even applicable.
- **Universe reproducibility from the pinned code:** `dataset/Binance_USDT/` ships **68** `*USDT_daily_1000days.csv` files; `process_crypto_ALL.py` excludes `USDCUSDT` and `TUSDUSDT` → **66 symbols exactly**, matching the paper's count. The *selection rule* (market-cap and continuity filters) is **not implemented anywhere in the released code** (no market-cap field exists in the repository) → the filter itself is `data gap`, only its output set is reproducible.
- **Timeframe / fields:** daily OHLCV only. **No** funding, open interest, order book, trades/aggressor, borrow, options surface or on-chain field is used (§III-C is explicit that this is a pure-price setting).
- **Point-in-time / availability:** the market-cap and "no missing values" filters carry **no as-of date** and no delisting handling → survivorship/point-in-time = `data gap` (research interpretation flags this as a look-ahead risk; the source does not address it).
- **Timestamp:** not stated in source (`data gap`); 24/7 venue with daily bars, boundary convention unstated.
- **Missing data:** source claims "no missing values" after filtering; the released preprocessing nevertheless applies `ffill().bfill()`, NaN→1.0 and clipping (Negative evidence 17).
- **Compute (source-reported §IV-A):** PyTorch, RTX 4090 24GB and A100 40GB, "each experiment was repeated 3 times, and the average performance was reported" (contradicted by the released scripts — Negative evidence 8).

## Execution assumptions

- **Signal-to-order:** **not stated in source** → `data gap`. The pinned code implies the book is struck at the close that provides the last input bar (label = close→next-close return); whether that close is actually fillable is not addressed. Order type (market/limit), fill model, latency, partial fills, failure handling → all `not stated in source`.
- **Fees / slippage / spread:** the only cost model is a **flat proportional per-side ladder**, applied post-hoc: Table II `10 bps/side`, Table III `0 / 0.050 / 0.075 / 0.100 / 0.200 / 0.300 %` per side, with §IV-C stating that the 30 bps rung is "including slippage and trading fees" and that the sensitivity analysis is "based on cost calculations [42]" — reference [42] is **Makarov & Schoar, "Trading and arbitrage in cryptocurrency markets", JFE 135(2), 293–319 (2020)**, a study of crypto arbitrage frictions, **not** a fitted fee/slippage schedule for these 66 pairs. No observed spread, no maker/taker schedule, no venue fee tier → `data gap`.
- **Turnover:** **35.5% per day** printed in Table II, identical in the no-cost and 10 bps columns. See Negative evidence 5 — this printed number is **inconsistent with the size of the cost drag implied by Tables II/III**.
- **Market impact / participation / ADV / capacity:** `not stated in source` → `data gap`, never zero. Leverage/margin → not stated (long-only, so not required). Borrow/shorting → not required by the printed rule. Funding/liquidation → `not stated in source`, and applicability depends on the unstated spot-vs-perpetual instrument type.
- **Released code contains no cost engine at all:** at pinned commit `00292fd`, grep over all nine code/config files (`train_gat_crypto.py`, `train_gat_enhanced.py`, `evaluator.py`, `models/gat.py`, `process_crypto_ALL.py`, `feature_engineer.py`, `process_crypto_enhanced.py`, `requirements.txt`, `CITATION.cff`) for `cost|turnover|slippage|bps|fee` returns **zero hits** → Tables II–III are not reproducible from the released repository (`data gap`).
- Any execution choice made by us rather than the source (next-open execution, a fitted fee/spread schedule, a participation cap) is **research-proposed**.

## Evidence

### Source-reported

All figures below are third-party claims from `arXiv:2606.27670v1`, **not independently reproduced**. Unless stated otherwise the market/universe is the 66-token Binance USDT panel, 15/04/2023–08/01/2026, chronological 60/20/20 split, 30-day lookback, daily long-only top-5 equal-weight portfolio with `√365` annualisation; **Table I metrics are the frictionless (no-cost) evaluation**; Tables II–III are the GAT variant.

**Table I (PDF p.5), overall comparison — IC / ICIR / Ann.SR / Prec@10 / inference ms (params):**

| Type | Method | Params | IC | ICIR | Ann.SR | Prec@10 | ms |
|---|---|---|---|---|---|---|---|
| RNN | LSTM | 51,521 | 0.011 | 0.046 | 2.299 | 0.496 | 0.252 |
| RNN | ALSTM | 55,746 | 0.009 | 0.043 | 1.162 | 0.503 | 0.276 |
| RNN | GRU | 38,657 | 0.017 | 0.072 | 1.529 | 0.495 | 0.245 |
| Transformer | PatchTST | 266,369 | −0.004 | −0.003 | −0.256 | 0.501 | 0.410 |
| Transformer | iTransformer | 13,764 | −0.007 | −0.052 | −0.370 | 0.506 | 0.494 |
| GNN | RSR | 76,481 | 0.015 | 0.079 | 1.544 | 0.499 | 0.449 |
| GNN | ESTIMATE | 332,259 | −0.002 | −0.025 | 1.018 | 0.496 | 7.899 |
| Spatio-Temp | TGN | 72,065 | 0.026 | 0.101 | 2.210 | 0.506 | 0.903 |
| Spatio-Temp | Graphormer | 109,929 | −0.007 | −0.058 | −0.129 | 0.494 | 0.992 |
| Spatio-Temp | MASTER | 142,593 | 0.027 | 0.114 | 2.227 | 0.513 | 1.382 |
| SOTA | StockMixer | 2,327 | 0.011 | 0.113 | 0.356 | 0.511 | 2.415 |
| **CryptoGAT** | **GAT †** | 47,105 | **0.037** | **0.138** | **3.128** | 0.504 | 0.627 |
| **CryptoGAT** | **FGAT †** | 52,865 | **0.047** | **0.168** | **3.892** | 0.507 | 0.792 |

§IV-B prose: "FGAT improves IC by 74% with only one-third of the parameters" relative to MASTER (0.027 → 0.047).

**Table II (PDF p.5), portfolio performance of the GAT, no cost vs 10 bps/side:**

| Metric | No Cost | Cost (10 bps/side) |
|---|---|---|
| IC | 0.037 | 0.037 |
| Cumulative Return | +229.12% | +185.66% |
| Annualized Return | +779.37% | +579.10% |
| Volatility/day | 4.25% | 4.25% |
| Sharpe (ann.) | 3.128 | 2.759 |
| Max Drawdown | −36.63% | −38.98% |
| Avg Turnover/day | 35.5% | 35.5% |

**Table III (PDF p.6), cost sensitivity of the GAT:** per-side cost → Ann.SR / Ann. Return: `0.000%` → 3.128 / +779%; `0.050%` → 2.920 / +673%; `0.075%` → 2.840 / +624%; `0.100%` → 2.759 / +579%; `0.200%` → 2.438 / +424%; `0.300%` → 2.117 / +305%. §IV-C: "Even at 30 bps per side (including slippage and trading fees), the model maintains a Sharpe Ratio above 2.0 and annualized returns exceeding 300%".

**Table IV (PDF p.6), component ablation — NASDAQ IC/ICIR | Cryptocurrency IC/ICIR:** StockMixer 0.043/0.501 | 0.011/0.113; `w.o. Indicator Mix` 0.040/0.465 | −0.008/−0.052; `w.o. Time Mix` 0.018/0.164 | −0.014/−0.071; `w.o. Stock Mix` 0.037/0.376 | 0.001/0.011; **GAT** 0.035/0.377 | **0.037/0.138**; **GAT + Time Mixing** −0.008/−0.117 | **0.006/0.023**.

**Table V (PDF p.8), market-dominant factor added as a sixth input — IC / ICIR / Sharpe:** MF-LSTM 0.009/0.048/0.669; MF-iTransformer −0.012/−0.091/−0.591; MF-StockMixer 0.015/0.094/0.963; MF-MASTER 0.008/0.027/0.926; **GAT 0.037/0.138/3.128**.

**Table VI (PDF p.10), defaults:** lookback 30; learning rate 0.00025; train/valid/test 60%/20%/20%; dropout 0; epochs 100; hidden size 64.

**Figures 2–4 (PDF p.7):** Fig. 2 — GAT IC/Sharpe improve with lookback and stabilise while most temporal models degrade; iTransformer stays negative. Fig. 3 — AR R² distributions for 1,026 Nasdaq stocks vs crypto (crypto below 0.1; Nasdaq std > 5×). Fig. 4 — correlation strength, graph density and PCA shares as quoted under Economic mechanism.

**Dataset empirical structure (§V-C, Fig. 4):** mean pairwise correlation crypto 0.528 vs stocks 0.200; 65.78% vs 2.39% of pairs above r = 0.5; density at τ = 0.5 crypto 0.66 vs Nasdaq ≈ 0.2 (from ~0.8 at low τ); PC1 share crypto 55% vs Nasdaq 16%; top-20 PCs crypto > 80%.

Provenance for every number above: `arXiv:2606.27670v1` Tables I–VI (PDF pp. 5, 6, 8, 10), §IV-B/§IV-C/§V-A/§V-C prose and Figs. 2–4 (p.7), each value re-extracted from the pinned HTML rendering as well.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. **Universe filters are full-sample.** "Market capitalization exceeding $200M" and "continuous daily data with no missing values" (§IV-A) carry no as-of date and no delisting handling, and the released code contains no market-cap field at all → the traded set is selected using information that would not have been available in real time (research interpretation: survivorship/point-in-time look-ahead risk). The source's own remark that fewer than 20 of the 1,000 tokens have records prior to 2019 shows how much the sample depends on that selection.
2. **Code contradicts the paper's graph-construction algorithm (look-ahead in the adjacency).** Paper Algorithm 1 takes `Price matrix P ∈ R^{N×T_train}` (train only). Pinned code (`build_correlation_matrix(price_data)` called from `train_gat_crypto.py` line 128 and `train_gat_enhanced.py` line 125, commit `00292fd`) passes the **entire** price history — `np.corrcoef` over train **and** validation **and** test rows — once, before training, and holds that adjacency fixed for every epoch and every inference. Test-period prices therefore decide which edges exist → a concrete, source-level leak that a frozen replication must remove.
3. **Correlation is taken on price levels, not returns, and τ is code-only.** `np.corrcoef(price_data)` on non-stationary price paths with `|ρ| > 0.5` (gat.py) makes much of the "cross-asset structure" a common-trend artefact; the threshold `0.5` never appears in the paper (Algorithm 1 leaves τ symbolic, Table VI omits it) → the published algorithm is not reproducible from the paper alone.
4. **The cost evidence covers only the weaker model.** Tables II–III are the plain **GAT** (the prose says "portfolio performance of GAT"; the Sharpe 3.128 matches Table I's GAT row). **FGAT — the paper's headline best model (IC 0.047, SR 3.892) — never receives a portfolio, drawdown, turnover or cost table.** The robustness claim therefore does not attach to the model the abstract promotes.
5. **Printed turnover is inconsistent with the printed cost drag (research interpretation, arithmetic from Tables II–III).** Table II's no-cost pair (229.12% cumulative, 779.37% annualised) implies an exactly **200-day** test window; over those 200 days the 10 bps/side deduction removes 229.12 − 185.66 = **43.46 pp = 21.73 bps/day**, which at 10 bps per unit traded implies **≈217% of NAV traded per day**, i.e. **≈6.1× the printed 35.5%/day**. The other rungs agree (189.9%–224.5% implied daily one-way traded value, 5.3–6.3× the printed figure). At the printed 35.5% the 10 bps ladder should have cost 3.55 bps/day = **7.10 pp** over the window, not 43.46 pp. Either the turnover print or the cost implementation is wrong; the source does not reconcile them.
6. **No spread, impact, participation or capacity model.** Costs are a flat proportional bps ladder anchored to a 2020 arbitrage paper, on a book that must trade ~35.5%–217% of NAV daily across 66 names; no ADV, no depth, no fill model, no venue fee tier. The source itself concedes elsewhere that crypto has "extremely unstable liquidity" and "irregular liquidity" (§I) without connecting that to the cost table.
7. **No cost code was released.** `grep cost|turnover|slippage|bps|fee` over all nine code/config files at the pinned commit → **0 hits**; `evaluator.py` computes only MSE, IC, ICIR, `sharpe5`, Prec@10. Tables II–III cannot be reproduced from the repository (`data gap`).
8. **Single fixed seed versus a claimed 3-run average.** §IV-A: "Each experiment was repeated 3 times, and the average performance was reported." Both released training scripts set `RANDOM_SEED = 123456789`, run once, and contain no loop over runs and no aggregation. No standard deviation, seed range or dispersion is printed anywhere → the reported point estimates may be single-run and no run-to-run stability is evidenced.
9. **Metric definition differs between paper and code.** The paper's Sharpe formula explicitly contains a risk-free rate `R_f`; `evaluator.py` computes `mean/std × √365` with **no risk-free subtraction**, and the value of `R_f` is never printed. The reported 3.128/3.892 are therefore gross excess-return-free arithmetic Sharpe ratios.
10. **Near-random classification metrics alongside Sharpe ≈ 3–4.** Prec@10 for **all 13 methods** lies in 0.494–0.513 (best FGAT 0.507, GAT 0.504) — essentially coin-flip top-10 hit rates — while reported annualised Sharpe reaches 3.128–3.892 on an IC of only 0.037–0.047. The source offers no reconciliation of that tension (e.g. return concentration in a few names), and Fig. 4's 55% PC1 share means much of any long-only top-5 book is common-factor exposure the source never subtracts.
11. **"Annualized Return +779%" is not a compounded strategy return.** `evaluator.py` accumulates the daily top-5 mean **arithmetically** (`bt_long5 += ...`), and the annualised figure geometricises that arithmetic sum over 200 days: `(1+2.2912)^(365/200) − 1 = 7.79`. A real compounded equity curve with 4.25%/day volatility and a −36.63% max drawdown cannot be read off Table II without a position-sizing rule the source never prints.
12. **Single split, single window, no regime table.** `valid_index = 599`, `test_index = 799` over 999 aligned days → the test set is the last ~200 days; exact calendar dates are never printed. No subperiod, crash, or bull/bear breakdown is given even though §IV-A says the sample spans "two consolidation-to-bull cycles, separated by the 2025 bear crash, subsequent recovery, and crash again".
13. **Execution timing unspecified.** The label is the return beginning at the last input close, but the source never states the execution price, order type, latency or whether the book is struck at that same close. Any realised version would need to trade inside the bar that produced the last feature (research interpretation).
14. **Baseline fairness.** "All baseline methods use uniform settings and the same optimization loss" (§IV-B) with no per-model tuning and no cited published defaults; four baselines print **negative** IC (PatchTST, iTransformer, Graphormer, ESTIMATE). Negative Sharpe for standard architectures on a 66-asset panel is at least as consistent with under-tuning as with a universal failure of temporal modelling, and there is no significance test, confidence interval or multiplicity control over 13 methods × 4 metrics.
15. **The ablation makes the claim architecture-conditional.** GAT + time mixing collapses to IC 0.006 (crypto) while helping on Nasdaq, and StockMixer's own IC falls 0.043 → 0.011 between markets (Table IV). The result is "these implementations on this panel", not an information-theoretic statement about temporal data; §VI's own framing ("problem-definition bias") is a hypothesis, not a tested exclusion of temporal signal.
16. **Static graph, no re-estimation.** The adjacency is computed once and never refreshed, no walk-forward refit exists, and graph staleness over a three-year deployment is not addressed. Combined with leak #2, the true causal version (train-only, refreshed, returns-based graph) is exactly the variant never tested.
17. **Preprocessing contradicts the "no missing values" claim.** `process_crypto_ALL.py` runs `replace([inf,-inf], nan).ffill().bfill()`, then maps NaN→1.0, +inf→2.0, −inf→0.5 and `clip(0.5, 2.0)`. `bfill` fills from the future, and the clipping silently truncates real returns beyond ±50% — neither is disclosed in the paper.
18. **Universe selection rule not reproducible.** Count reconciles (68 shipped CSVs − USDCUSDT − TUSDUSDT = 66 ✓), but the market-cap/continuity filters that supposedly produced those 68 files are not implemented anywhere in the repository, so the set cannot be re-derived from the stated rule.
19. **Instrument type and crypto economics unstated.** Spot vs perpetual, funding, mark/index price, leverage, liquidation, margin and borrow are never mentioned; there is no OI/book/trade data. For a perpetual implementation the cost model is therefore incomplete by construction (`data gap`), and for a spot implementation the funding leg of any real book is simply absent.
20. **No daily-bar convention for a 24/7 market.** The only session statement is the `√365` factor; timezone, candle boundary and cut-off for "daily" Binance bars are not printed, which matters directly for a same-close execution assumption.
21. **Publication/selection status.** Preprint, "Under review", 10 pages, no journal-ref, no peer review, no independent replication, a 7-star repository, one sample (2023–2026) and one split; all headline numbers are single-source claims.
22. **No passive benchmark.** Tables I–V never compare the long-only top-5 book against buy-and-hold BTC/ETH, a market-cap basket, or an equal-weight 66-coin book — on a sample the source describes as containing two bull cycles, a crash, a recovery and another crash. Long-only crypto exposure is the obvious untested competitor.
23. **None identified in the reviewed external sources** for direct refutations of this specific paper: it is June 2026 work and no citing replication, comment or failure report was found in the searches run on 2026-09-27; absence is not evidence of no negative result.

## Falsification plan

Every threshold in F1–F13 is a **research-defined falsification threshold** (not from the source); every construction choice is **research-proposed**. Failure action for all tests: mark the hypothesis falsified for this record and do not advance it to a production candidate.

- **F1 — Frozen forward replication (decisive).** Rebuild with the pinned commit `00292fd` + the shipped CSVs, then extend to an unseen window after 08/01/2026 with all hyperparameters frozen (lookback 30, hidden 64, τ = 0.5, K = 5). **Pass** requires top-5 net SR ≥ **1.00** at 10 bps/side **and** ≥ **+0.50** above a parameter-matched GRU/LSTM re-run on identical splits. **Fail** if either condition is missed.
- **F2 — Cost ladder with measured spread (decisive for tradability).** 0/1/2/5/10/20/30/50 bps per side plus observed bid–ask on the 66 pairs. **Fail** if net SR < **1.00** at 10 bps or if more than **50%** of gross SR erodes by 10 bps. (Pre-registered expectation: at the printed 35.5%/day turnover, 10 bps/side costs ≈3.55 bps/day ≈ 7.1 pp over 200 days — cheap; at the ≈217% turnover implied by Table II it costs ≈21.7 bps/day. The audit must first establish which turnover is real.)
- **F3 — Turnover / capacity audit (resolves Negative evidence 5).** Recompute one-way turnover from the actual rebalanced book and compare with 10%-ADV participation for each pair. **Fail** if realised daily one-way turnover is not within **±20%** of the printed 35.5%, or if any position needs >**10%** of daily volume at the tested scale.
- **F4 — Decisive mechanism ablation (four-way).** Full GAT vs (a) **degree-preserving rewired graph**, (b) **identity graph (no edges)**, (c) pure market/PC1 factor, (d) parameter-matched GRU — same seeds, same splits. **Pass** requires full − rewired SR gap ≥ **0.50** and full − identity ≥ **0.50**; otherwise the correlation-graph mechanism is not carrying the result (generic cross-sectional pooling or market beta is).
- **F5 — Point-in-time universe rebuild.** Rebuild the panel with the market-cap filter applied **at each date**, including tokens that later delisted or broke continuity. **Fail** if top-5 net SR drops by >**50%** versus the reported figure.
- **F6 — Graph-construction leak removal (fixes Negative evidence 2/3).** Rebuild adjacency from **training-window returns only** (not price levels, not full history), re-fit walk-forward each retraining. **Fail** if SR at 10 bps falls below **1.00**, or if the τ sweep `0.3/0.4/0.5/0.6/0.7` shows the headline result only at one τ (range across τ within **±30%** required).
- **F7 — Label-timing / fill audit.** Execute at (i) next bar open, (ii) next bar close, (iii) the same close as the last input bar with a 1-minute latency budget. **Fail** if net SR at 10 bps is < **0.50** under (i) or (ii) — i.e. the result exists only under same-close execution.
- **F8 — Seed and run dispersion.** 10 independent seeds (the released script fixes one), report median/IQR/min of SR, IC. **Fail** if the median SR is < **60%** of the reported 2.759 (10 bps), or if the source's claimed 3-run averaging cannot be reproduced.
- **F9 — Permutation null.** 1,000 draws of circularly shifted labels (and, separately, shuffled graph edges) re-running the headline metric. **Fail** if the real SR is not above the **95th percentile** of the null.
- **F10 — Multiplicity control.** Benjamini–Hochberg `q < 0.10` across 13 methods × 4 metrics × 2 cost settings. **Fail** if the GAT/FGAT contrast does not survive.
- **F11 — Subperiod stability.** Split the 999 days into three contiguous blocks aligned to the source's own bull/crash description, plus the 2025 crash window. **Fail** if the top-5 book underperforms the equal-weight 66-coin basket in any block, or if the full-sample result is driven by one block.
- **F12 — Passive-benchmark horse race.** Top-5 vs buy-and-hold BTC, buy-and-hold ETH, and an equal-weight 66-coin basket, cost-matched. **Fail** if the strategy's net information ratio vs the equal-weight basket is not positive with Newey–West `t ≥ 1.96`.
- **F13 — 12-month reproducibility gate.** With the pinned commit and shipped CSVs, IC and SR must land within **±20%** of 0.037/3.128 (GAT, no cost) and 0.047/3.892 (FGAT). **Fail** otherwise; a failure here also invalidates Negative evidence 8's "3-run average" reading.

## Crypto portability

**direct.**

The source's evidence **is** crypto: 66 Binance USDT pairs, 24/7 annualisation via `√365`, a crypto-native sample (15/04/2023–08/01/2026) and a mechanism (cross-asset correlation graph) built explicitly for this market's reported 0.528 mean pairwise correlation. Nothing is ported from another asset class, so `direct` is the correct label — but `direct` covers only the forecasting/cross-sectional mechanism, not execution economics, which remain open inside that setting: **spot vs perpetual is unstated**, so funding, mark/index price, leverage and liquidation may or may not apply; venue fragmentation (Binance-only), daily-candle boundary/timezone, 24/7 session, liquidity concentration in the top names, and any per-leg borrow (not needed for the printed long-only rule) are all `data gap`. `direct` is **not** authorization to trade, and F1–F7 must pass before this record is treated as anything more than research material.

## Limitations

- `underspecified`: execution price / order type / fill model / latency; graph refresh policy; τ (paper); FGAT hyper-parameters (paper); exact test calendar dates; risk-free rate value; capacity, participation and liquidity rules; spot-vs-perpetual instrument type; timezone and daily-bar boundary; missing-data policy in the published pipeline.
- `data gap`: market-cap and continuity filter as-of dates (point-in-time universe); the cost engine behind Tables II–III (absent from the released code); the printed 35.5% turnover vs the ≈190%–225% turnover implied by the cost ladder; the claimed 3-run averaging vs a single fixed seed in code; dispersion/significance for every reported number; ablation of the FGAT variant; passive-benchmark comparison; arXiv-listed 1,479 KB vs served 1,560,076 bytes.
- `not independently reproduced`: every performance, ablation, cost and dataset-structure figure in this record.
- `unproven`: the causal reading of "time series models are ineffective for cryptocurrency" (the source tests its own implementations under one shared recipe); the claim that the graph edge set — rather than common-factor exposure — produces the return (no rewired/identity-graph control exists in the source).
- Source-quality: preprint under review, not peer reviewed, single sample/single split, no multiplicity control, no released cost code, full-sample universe filters, and a code-level look-ahead in the graph construction.
- Incremental-write / dedup: this source identity and mechanism are recorded here for the first time (pre-write scans above); if a later run finds `2606.27670` already captured, this record should be updated rather than duplicated.

## Implementation status

`implementation_status: not-implemented`. Nothing in this record has been implemented in our research stack: no code was written, no data was acquired or downloaded into the repository, no backtest, walk-forward, paper, testnet or live run was performed, and no Wiki Brain record, candidate-pool entry, Qlib run, Kanban task or strategy family was created by this capture. The strategy exists only as source-reported research material. Reading the public repository files listed under Provenance is provenance verification, not implementation.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. The presence of this record does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, Paper, Testnet or Live. All third-party results above are `source-reported` and were **not independently reproduced**. Any operational rule not printed by the source (execution timing, graph refresh, cost acceptance cutoffs, falsification thresholds) is `research-proposed` / `research-defined` and carries no authority.

## Related Wiki records

Pre-write `kb_read` resolution of the canonical specification: `quant/strategy-research-record-spec-v1.md` → 10,289 bytes, SHA-256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`; `quant/strategy-research-record-spec-v2.md` → file not found, so **v1 remains canonical**. Read-only; no Wiki Brain write was performed.

Three read-only `kb_search` queries were run: `graph attention network cross-sectional stock prediction` → 3 pages, `cryptocurrency cross-sectional machine learning return prediction` → 10 pages, `graph neural network cryptocurrency trading correlation graph` → 8 pages. The verified mechanism-adjacent pages linked here:

- [[quant/nystrom-attention-cross-sectional-stock-transformer-low-rank-2026-09-11]] — mechanism-adjacent: attention decomposition inside MASTER (one of this paper's baselines), equity cross-section, no graph and no crypto.
- [[quant/equity-analyst-coverage-network-graph-attention-momentum-spillover-2026-09-02]] — graph attention but over an analyst-coverage network on equities, momentum-spillover mechanism, different universe and data dependency.
- [[quant/crypto-short-horizon-predictability-purged-walk-forward-audit-2026-09-11]] — crypto predictability under a leakage-safe audit protocol; the natural validation template for F1/F5/F6 here.
- [[quant/dynamic-johansen-deep-weighted-ensemble-cryptocurrency-pairs-2026-09-05]] — crypto ML but cointegration pairs trading, not cross-sectional ranking.
- [[quant/lstm-learnable-sector-embeddings-cross-sectional-reversal-2026-09-02]] — cross-sectional neural ranking with explicit structure embeddings, equity universe.

Repository-adjacent records (same repository, **not** Wiki links, different source identities and mechanisms): `cast-cross-asset-state-space-collaborative-kalman-mpc-drawdown-control-2026-09-16` (`arXiv:2609.14205` — **same three authors**, different paper, Kalman/MPC drawdown control instead of graph attention); `stn-tgat-nmi-soft-threshold-graph-attention-topk-ranking-2026-09-04` (equity graph-attention Top-K with learnable sparsification); `forward-looking-equity-correlation-thgnn-spongesym-statistical-arbitrage-2026-09-05` (S&P 500 correlation forecasting, signed-graph clustering); `equity-analyst-coverage-network-graph-attention-momentum-spillover-2026-09-02`; `crypto-cross-sectional-momentum-fused-encoder-2026-08-31` and `binance-perpetual-cross-sectional-momentum-taker-cost-falsification-2026-09-13` (crypto cross-sectional books built on momentum factors rather than a learned graph).

## Sources

1. Yu Peng, Matloob Khushi, Josiah Poon, *"CryptoGAT: Are Time Series Models Effective for Cryptocurrency Forecasting?"*, **arXiv:2606.27670v1 [cs.CE, q-fin.ST]**, submitted 26 Jun 2026 03:05:02 UTC, Comments "Under review", arXiv.org perpetual non-exclusive licence. Landing page: https://arxiv.org/abs/2606.27670 — DataCite DOI: https://doi.org/10.48550/arXiv.2606.27670.
2. Pinned full text (primary source for every field in this record), PDF: https://arxiv.org/pdf/2606.27670v1 — 1,560,076 bytes, 10 pages, SHA-256 `f377f86618c2d6a4a43380613905ce4b4847f04de71c39420f2039c9ecb1fa16`, downloaded 2026-09-27; Abstract, §I–§VI, Appendix A, Tables I–VI, Figures 1–4, Algorithms 1–2 read directly.
3. Pinned full text (HTML rendering used for cell-level cross-checking): https://arxiv.org/html/2606.27670v1 — 216,567 bytes, SHA-256 `5492b00b1ba0cb616312319afd6a93bb73de28ad9657036b2c3956485fde95c3`, downloaded 2026-09-27.
4. Official implementation at full commit `00292fdda64c3f50296103d01c74bfa937e08851` (2026-07-11), MIT: https://github.com/FanBroWell/CryptoGAT — files read: `README.md`, `src/train_gat_crypto.py`, `src/train_gat_enhanced.py`, `src/evaluator.py`, `src/models/gat.py`, `src/process_crypto_ALL.py`, `src_Feature/feature_engineer.py`, `src_Feature/process_crypto_enhanced.py`, `requirements.txt`, `CITATION.cff`, and the `dataset/` file listing (68 CSVs + 8 pickles).
5. Dataset mirror cited by the repository README only: https://huggingface.co/datasets/CharlieYPeng/cryptogat-crypto-1d — HTTP 200 checked 2026-09-27.
6. Reference *cited by the source* for its cost ladder (not read independently for this record): Makarov & Schoar, "Trading and arbitrage in cryptocurrency markets", *Journal of Financial Economics* 135(2), 293–319 (2020) — source reference [42].
