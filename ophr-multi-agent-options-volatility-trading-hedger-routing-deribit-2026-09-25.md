---
schema: strategy-research-record-v1
title: "OPHR: Multi-Agent RL Crypto-Options Volatility Trading with Learned Hedger Routing (Deribit BTC/ETH, NeurIPS 2025)"
created: 2026-09-25
updated: 2026-09-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - options
  - volatility-trading
  - delta-hedging
  - multi-agent-reinforcement-learning
  - hedger-routing
  - crypto-options
  - deribit
  - peer-reviewed
status: research-only
confidence: medium
source_as_of: "2025-10-22"
sources:
  - "Zeting Chen, Xinyu Cai, Molei Qin, Bo An, \"OPHR: Mastering Volatility Trading with Multi-Agent Deep Reinforcement Learning\", Advances in Neural Information Processing Systems 38 (NeurIPS 2025) Main Conference Track. Proceedings page https://proceedings.neurips.cc/paper_files/paper/2025/hash/4c7dbef8023a15c4b81dc95a6ea08bf3-Abstract-Conference.html (prints authors, volume, track and DOI 10.52202/085713-1764)."
  - "Pinned primary source read end to end: https://proceedings.neurips.cc/paper_files/paper/2025/file/4c7dbef8023a15c4b81dc95a6ea08bf3-Paper-Conference.pdf fetched 2026-09-25 — 1,352,171 bytes, SHA-256 e61e4794adb82c98fe32f7d6b8ba3719742174ba92e0055058ce73d58ac68b57, 31 pages, covering Sections 1-6, Tables 1-14 (main + appendix), Figures 1-5 captions, References, Appendices A-D, NeurIPS Impact Statement and Reproducibility Checklist. Every performance number below is anchored to a Table in this PDF."
  - "NeurIPS OpenReview forum https://openreview.net/forum?id=2p4AtivyZz (NeurIPS 2025 Poster, submission 7551) — read 2026-09-25 for review status; the OpenReview PDF endpoint returned HTTP 403 / bot challenge on 2026-09-25, so the NeurIPS proceedings PDF above is the pinned checksum."
  - "Code release used only to verify signal/execution mechanics (every statement from it is labelled code-derived): https://github.com/Edwicn/OPHR-MasteringVolatilityTradingwithMultiAgentDeepReinforcementLearning at full commit SHA 8c3aeadef62bc16ab92dc3594b21183b56ec1342 (sole commit \"init\", author date 2025-10-22T11:39:34Z, default branch main, 68 files). Files read: README.md (0 bytes), requirements.txt, config.py, configs/env_config.yaml, configs/evaluation_config.yaml, env/rl_env.py, env/base/perpetual.py, env/base/volatility_tickers.py, backtest/backtest.py, plus the recursive tree listing."
  - "Negative provenance check run 2026-09-25: arXiv API queries ti:\"Mastering Volatility Trading\" and all:\"OPHR\" AND all:\"volatility\" both returned zero entries — no arXiv preprint of this paper exists as of 2026-09-25 (data gap for an arXiv ID is therefore \"no such record\", not a fetch failure)."
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions:
  - "Abstract says \"cryptocurrency options data from 2021-2024\" while Table 1 starts the train split at 19/04/01 and the prose names 2019 and 2020 as in-sample periods (source-internal period mismatch)."
  - "NeurIPS checklist answers itself both ways on code release: reproducibility question = [Yes] \"We open-source the code and example data\", while the new-assets documentation question = [NA] \"We do not open-source our code\"; the abstract and the live GitHub repository show a release does exist."
  - "Paper Section 5.3 models a 0.05% Deribit fee on perpetual futures, but the released configs/env_config.yaml sets fee_config.futures_perpetual = 0.0000 (0.00%) — released config therefore cannot reproduce the paper's own cost statement (code-derived)."
  - "Paper Table 1 test split is 23/07/01 - 24/07/01, while the released configs/env_config.yaml sample comments use test_start 2024-01-01 / test_end 2024-04-01 with \"Sample data: 2024-01-01 to 2024-04-01\" (code-derived mismatch between paper experiment and released sample config)."
  - "Table 2 Mean-Reversion row is cell-for-cell identical for BTC and BTC/ETH blocks (TR -19.80, ASR -1.32, ACR -0.74, ASoR -1.54, AVOL 15.40, MDD 27.45, WR 41.94, PLR 1.18) — impossible-looking duplication left unexplained by the source."
---

# OPHR: Multi-Agent Reinforcement-Learning Crypto-Options Volatility Trading with Learned Hedger Routing

## Provenance

- **Primary source (sole source for every empirical claim below).** Zeting Chen, Xinyu Cai, Molei Qin, Bo An, *"OPHR: Mastering Volatility Trading with Multi-Agent Deep Reinforcement Learning"*, **Advances in Neural Information Processing Systems 38 (NeurIPS 2025), Main Conference Track** (peer-reviewed conference proceedings, not a preprint), DOI **10.52202/085713-1764**. Stable proceedings URL: https://proceedings.neurips.cc/paper_files/paper/2025/hash/4c7dbef8023a15c4b81dc95a6ea08bf3-Abstract-Conference.html (`source-reported`).
- **Author list exactly as printed on the proceedings page and on the PDF first page (4 authors, in order):** `Zeting Chen, Xinyu Cai, Molei Qin, Bo An`. The PDF footnote marks Zeting Chen and Xinyu Cai as equal contributors (correspondence: Xinyu Cai). Affiliations printed on the PDF first page: Zeting Chen, Xinyu Cai and Molei Qin — Nanyang Technological University, Singapore; Bo An — Nanyang Technological University and Skywork AI, Singapore (`source-reported`). Funding acknowledgment: National Research Foundation Singapore / DSO National Laboratories under the AI Singapore Programme, AISG Award No. AISG2-GC-2023-009.
- **Pinned checksum / extent:** the Conference PDF fetched 2026-09-25, **1,352,171 bytes, SHA-256 `e61e4794adb82c98fe32f7d6b8ba3719742174ba92e0055058ce73d58ac68b57`, 31 pages**, read end to end (Sections 1-6, Tables 1-14, Figure captions 1-5, References, Appendices A-D, Impact Statement, NeurIPS Reproducibility Checklist). The proceedings.com catalog entry for this DOI lists 31 pages, consistent with the pinned PDF.
- **Publication / preprint status:** peer-reviewed NeurIPS 2025 Main Conference paper (Advances in NIPS 38). **No arXiv version** (two arXiv API queries returned zero results on 2026-09-25). **No journal / SSRN version** claimed by the source (`data gap`: none found). OpenReview forum `2p4AtivyZz` shows the item as a NeurIPS 2025 Poster (submission 7551) (`source-reported`); note that `dblp`-style mirrors list a second OpenReview forum handle for the same paper — the proceedings hash URL above is the identity anchor used here.
- **Code:** https://github.com/Edwicn/OPHR-MasteringVolatilityTradingwithMultiAgentDeepReinforcementLearning pinned at **full commit SHA `8c3aeadef62bc16ab92dc3594b21183b56ec1342`** (sole commit "init", 2025-10-22T11:39:34Z). Repository hygiene (`code-derived`): `README.md` is **0 bytes**, there is **no LICENSE file**, the tree commits `__pycache__/*.pyc` bytecode, and `requirements.txt` pins only lower bounds (`numpy>=1.21.0`, `torch>=1.9.0`, `polars>=0.15.0`, …) with **no exact lock and no version pins**.
- **Dedup (deterministic, whole-repository, run 2026-09-25 before writing):** 2,538 `*.md` files (including `.mimo-worktrees` / `.agents` / `.hermes`) plus `coverage_manifest.csv` (5,808 rows) searched for `OPHR`, `2p4AtivyZz`, `4c7dbef8023a15c4b81dc95a6ea08bf3`, `085713-1764`, `Edwicn`, `Mastering Volatility Trading`, `Zeting`, `8c3aeadef62bc16ab92dc3594b21183b56ec1342`, `e61e4794` → **all 0 hits in `*.md` and 0 hits in the manifest.** Author near-hits were opened and confirmed unrelated: `Bo An`, `Xinyu Cai` and `Molei Qin` appear only in `fineft-risk-aware-ensemble-rl-vae-routing-crypto-futures-2026-09-03.md` and `archetype-trader-vq-rl-hierarchical-crypto-perpetual-2026-09-13.md`, which cite different papers (KDD'26 arXiv:2512.23773 and Zong/Xia et al.) from the same NTU lab. **No exact source identity exists in the repository → new record is legitimate.**

## Economic mechanism

### Source-reported

- The claimed mechanism is a **volatility-risk-premium / IV-vs-RV wedge**: long volatility via options when implied volatility is cheap relative to expected realized volatility, short volatility when implied is rich, and delta-hedged over the holding window so the payoff isolates the IV−RV difference rather than direction (Sections 1-2; the paper frames the target explicitly as "delta-hedged straddle PnL as the optimization target").
- **Two cooperating agents (Sections 3-4):** an **OP-Agent** maps market features `Ft` to an option position target `a_op ∈ {+1, −1, 0}` (long / short / neutral) at each step and is rewarded by the change in portfolio net value `r_op = V_(t+1) − V_t`; an **HR-Agent** maps `(Ft, Pt, Gt)` (market features, positions, Greeks Δ/Γ/Θ/Vega) to **a selection from a pool of hedging policies** every `n_hr` steps and is rewarded by the counterfactual advantage of the selected hedger over a rule-based baseline hedger run in a twin environment, `r_hr = V_(t+n) − V̂_(t+n)` (Eq. reward paragraph in Section 3, Section 4.2).
- **Training (Section 4.3):** Phase 1 offline initialization from a **sub-optimal Oracle policy** that places long volatility if `future RV ≥ σ(1+β)`, short if `future RV ≤ σ(1−β)`, otherwise neutral (β grid and RV horizon grid in Table 5); Phase 2 alternating HR-Agent / OP-Agent online training. GNN-style hedger pool and hedger parameter grids are in Table 6 (delta-based, price-based and risk-aversion `λ` grids, pool size 30).
- Paper's stated claim (Section 5): OPHR "consistently outperforms traditional approaches across key metrics" on BTC and ETH crypto options.

### Research interpretation

- The falsifiable hypothesis we record is: **a learned hedger-routing layer is the marginal contributor** — i.e. holding OP timing fixed, swapping a fixed rule-based delta/threshold hedger for a periodically re-selected hedger from a risk-graded pool should raise risk-adjusted return. This is an ablation claim the paper does make internally (row `OP` vs row `OPHR`), but it is tested on a single venue, a single 12-month test window and a single run (`unproven`).
- Second, weaker channel: **trade-frequency control** — the paper attributes its low cost ratio to average holding periods of 9-51 hours (Table 3), i.e. the strategy's economics may come partly from *trading less*, not from a better volatility forecast. Neither channel is separated by any significance test in the source.
- Missing link the source does not supply: no evidence that the IV−RV wedge on Deribit is stable, transferable or capacity-bearing; no comparison to a simple static "sell rich IV / buy cheap IV with a fixed hedge-ratio band" control, so the RL layer is not isolated from the underlying vol-premium effect.

## Signal

- **Formation timestamp / cadence:** hourly data (`source-reported`, Section 5.1 "We utilize hourly-level data"). The OP-Agent decides at each step; the HR-Agent re-selects a hedger every `n_hr = 24` steps (Table 7) — with hourly bars that is **24 hours** (`research interpretation` of the source's step unit; the paper does not restate the step→wall-clock mapping in Section 3). `code-derived` config in `configs/env_config.yaml`: `option_interval: 180` (minutes), `hedge_interval: 60` (minutes), `episode_length: 14` — i.e. the released sample config implies option decisions every 3 hours and hedges hourly, which does **not** match an hourly OP step reading of the paper (`underspecified`).
- **Position target:** `a_op ∈ {+1, −1, 0}` sets the target long / short / neutral option position for the step; the HR-Agent's chosen hedger then trades the underlying (Deribit perpetual, per Section 3 "the underlying asset … primarily includes the perpetual future of the underlying asset") to realize the hedge.
- **Instrument selection:** the paper states the family of positions as **delta-hedged straddles** (Sections 1-2) and, for the *baseline* strategies only, "selects the nearest-to-the-money (ATM) straddle within a predefined maturity range" with roll-on-expiry rules (Appendix C.3). **For OPHR's own positions the exact strike / expiry selection and roll rule is not stated anywhere in Sections 3-5 → `underspecified`.** No independent reconstruction is possible without that rule.
- **State features:** "features derived from options and underlying market data to analyze price trends and volatility" (Section 3) — **the feature vector is never enumerated → `underspecified`**. `code-derived`: `env/rl_env.py` sets `state['features'] = tick.perpetual.features` and `state['volatility_tickers'] = tick.volatility_tickers.features`; `env/base/perpetual.py` carries bid/ask arrays, `mark_price`, `funding_rate` and `future_information` alongside `features`, and `env/base/volatility_tickers.py` carries `min_mark_iv`, `min_mark_iv_delta`.
- **Oracle (training only, not tradable):** long if `future RV ≥ σ(1+β)`, short if `future RV ≤ σ(1−β)`, else neutral (Section 4.3) — uses **future realized volatility by construction**, i.e. deliberate look-ahead confined to offline initialization. `research-defined` note: any re-run must confirm the teacher never enters the test-period policy.
- **Parameters (source-reported, Tables 5 and 7):** training window size 10 (days); oracle future-RV horizons `(3, 6, 9, 12, 24)`; oracle thresholds `β ∈ (0.1, 0.2, 0.4, 0.6, 0.8)`; oracle exploration rate 0.1; episodes per training window 20,000; updates per episode 20; batch size 512; hidden layer size 1,024; learning rate `1 × 10^-4`; n-step TD 12; discount `γ = 0.99`; HR-Agent learning rate `1 × 10^-4`, `γ = 0.99`, batch 512, hidden 1,024, `ε: 0.9 → 0.01` linear over 10,000 steps, 10 updates per routing step, `n_hr = 24`. Hedger pool size 30 with delta-threshold grid `0 … 0.9` and price-threshold grid `0.5% … 100%`, `λ ∈ 0.1 … 800` (Table 6).
- **Position sizing / stop / take-profit / deadband:** **not stated in source → `data gap`** (the source specifies position *targets* and a portfolio-margin constraint, not a sizing or exit rule). This record therefore does **not** claim a reconstructable entry/exit spec; any sizing or stop would be `research-proposed`, and none is proposed here.
- **Signal status:** `underspecified` for full independent reconstruction (missing contract-selection rule, missing feature list, missing sizing rule).

## Required data

- **Instrument:** Deribit **inverse options** on BTC and ETH — European-style, cash-settled in the base cryptocurrency, priced off the Black-Scholes forward (Appendix A.2), across "a wide range of strikes and expirations (weekly to quarterly)" with an IV surface, open interest and volume (Section 5.1). **Hedge instrument:** the Deribit **perpetual future** of the same underlying (Section 3).
- **Universe:** BTCUSD and ETHUSD option chains only (2 underlyings, 1 venue). Inclusion/exclusion rules, strike/expiry filters, minimum-liquidity filters, and survivorship treatment of expired/expiring contracts: **not stated in source → `data gap`** (the dataset is described only as "complete options chains").
- **Venue / vendor:** Deribit (named in Section 5.1 "BTC and ETH options data obtained from Deribit"). No data-vendor/API provenance, snapshot convention or back-fill statement → `data gap`.
- **Timeframe:** hourly bars, aggregated from order-book / option-chain observations; session convention is 24/7 crypto (Appendix A.2 states "Trading is generally conducted on a continuous 24/7 basis"). Timezone / clock source / out-of-order handling: **not stated → `data gap`**.
- **Fields:** option chain (bid/ask, IV, mark IV, strikes, expiries), underlying price, implied-vol surface, open interest, volume, Greeks computed from BSM (Δ, Γ, Θ, Vega), perpetual mark price and **funding rate** (`code-derived` — the field exists in `env/base/perpetual.py`, even though the word "funding" never appears in the paper).
- **Splits (source-reported, Table 1, both BTCUSD and ETHUSD):** train **19/04/01 – 22/12/31**, validation **23/01/01 – 23/06/30**, test **23/07/01 – 24/07/01**. Note the abstract's "2021-2024" does not match this table (frontmatter contradiction).
- **Point-in-time / look-ahead:** no publication-lag or snapshot-timestamp discussion in the source → `data gap`; the only look-ahead explicitly acknowledged is the future-RV Oracle used for training initialization.
- **Missing data:** no stale/missing/stale-quote handling stated → `data gap`.
- **Funding / fee / spread needs:** fee schedule modeled (Section 5.3); funding on the perpetual hedge leg, borrow/assignment on short options, and any index/mark-price lag are **neither observed nor modeled nor explicitly omitted → `data gap`** (the word "funding" appears 0 times in the pinned PDF).

## Execution assumptions

- **Order type / fill model:** `code-derived` and `source-reported`-adjacent — Section 5.3 states that "bid-ask spread costs [are] implicitly captured through market order execution prices in backtesting", i.e. **market orders at the chain's quoted bid/ask**, not a limit-order fill model. No queue / partial-fill / maker-order model is described.
- **Fees (source-reported, Section 5.3 + Table 4):** Deribit commission **0.05% on perpetual futures**, **0.03% on options, capped at 12.5% of option price**. Reported transaction cost as a share of P&L: **BTC 4.15% (options) + 5.21% (underlying) = 9.36%; ETH 2.97% + 2.78% = 5.75%** (Table 4). The paper states profitability "remains robust after accounting for transaction costs"; it does **not** print a separate gross series, so the **gross/net split of Table 2 is `underspecified`** (implied cost-inclusive, not explicitly labelled).
  - `code-derived` conflict: released `configs/env_config.yaml` sets `futures_perpetual: 0.0000` — zero perp fee — and `combo_fees.second_leg_reduction: 1` (second leg free), contradicting Section 5.3.
- **Slippage:** no slippage model anywhere in the pinned PDF; the only mention of slippage is inside the definition of "Residual PnL" (a term-by-term accounting identity) → **not a modeled cost → `data gap`** (do not read this as "slippage = 0").
- **Spread:** only the implicit claim above; no explicit spread series, no half-spread stress → `underspecified`.
- **Funding:** perpetual hedge leg implies periodic funding payments in reality, but the source never mentions funding → `data gap`.
- **Market impact / capacity / latency:** the terms "market impact", "capacity" and "latency" appear **0 times** in the pinned PDF → `data gap`. No participation/ADV cap, no position limit, no order-size limit stated.
- **Leverage / margin:** Portfolio Margin (Appendix A.3) — stress grid of price shifts `−15% … +15%` and IV adjustments `+45% / 0% / −30%`, margin required from the maximum projected loss, with required margin kept **below 50% of cash** (Appendix A.3). Liquidation / maintenance-margin breach handling: **not stated → `data gap`**.
- **Shorting / borrow:** short volatility is expressed as short option positions (and unhedged short-vol baselines); no borrow/locate/assignment discussion → `data gap`.
- **Initial capital:** `code-derived` `initial_capital: 10.0` in `configs/env_config.yaml`, denominated in **BTC** (`print(f"Initial capital: {initial_capital} BTC")` in `config.py`); the paper itself does not state the account base → `underspecified`.
- **Runs / seeds / error bars:** one run per configuration is implied; **no seed count, no repeated runs, no error bars** — NeurIPS checklist answer `[NA]`, justification *"The statistical significance is not applicable for quantitative trading research, because we only experienced one history and cannot access to other parallel universe."* (`source-reported`).

## Evidence

### Source-reported

All figures below are `source-reported`, from the **pinned 31-page NeurIPS 2025 PDF, Table 2** ("Performance comparison on 2 Crypto markets with 8 baselines"), rows read individually with column identity `TR(%)↑ / ASR↑ / ACR↑ / ASoR↑ / AVOL(%)↓ / MDD(%)↓ / WR(%)↑ / PLR↑`, test window **23/07/01 – 24/07/01**, Deribit BTC and ETH options, hourly, daily-aggregated returns, annualization factor 365, zero risk-free rate (`code-derived` `risk_free_rate: 0.0`, matching the ASR formula `E[ret]/σ[ret]×√365` in Appendix C.1). All rows are from the same table, the same version, the same universe — no cross-table, cross-version or cross-market splicing.

| Row (Table 2) | TR(%) | ASR | ACR | ASoR | AVOL(%) | MDD(%) | WR(%) | PLR |
|---|---|---|---|---|---|---|---|---|
| BTC — OPHR (full method) | 33.10 | 1.87 | 3.35 | 3.27 | 16.83 | 9.41 | 45.93 | 2.05 |
| BTC — OP (OP-Agent + rule-based hedger) | 21.43 | 1.19 | 1.46 | 2.03 | 17.01 | 13.84 | 44.50 | 1.86 |
| BTC — DLOT-style end-to-end baseline | 4.91 | 0.52 | 0.55 | 0.66 | 21.40 | 8.92 | 47.97 | 1.11 |
| BTC — Long Volatility | −33.05 | −1.32 | −0.77 | −2.13 | 24.90 | 42.70 | 21.74 | 1.82 |
| BTC — Short Volatility | 2.90 | 0.09 | 0.10 | 0.09 | 24.55 | 21.10 | 73.91 | 0.37 |
| ETH — OPHR (full method) | 44.89 | 1.76 | 1.58 | 1.67 | 24.42 | 27.25 | 55.61 | 1.43 |
| ETH — OP (OP-Agent + rule-based hedger) | 23.49 | 0.85 | 0.77 | 0.79 | 26.85 | 29.45 | 52.74 | 1.29 |
| ETH — DLOT-style end-to-end baseline | 1.19 | 0.07 | 0.09 | 0.09 | 17.14 | 13.53 | 42.80 | 1.34 |
| ETH — Long Volatility | −28.25 | −0.72 | −0.53 | −0.83 | 37.55 | 50.95 | 34.78 | 0.71 |
| ETH — Short Volatility | −34.75 | −1.12 | −0.69 | −1.25 | 33.00 | 53.05 | 56.52 | 0.48 |

(Every cell above was read from the pinned PDF's Table 2 by coordinate-level extraction, so row identity (BTC/ETH block × model) and column identity (`TR/ASR/ACR/ASoR/AVOL/MDD/WR/PLR`) are both confirmed — no cell was transcribed from a summary, and no cell from another table, version or market was mixed in. The two Mean-Reversion rows are cell-for-cell identical in the source; see the frontmatter contradiction.)

Additional `source-reported` items:

- **Table 3 (long/short behaviour):** BTC OP long HP 20.94h / WR 31.96% / PLR 2.21, short HP 52.94h / WR 55.86% / PLR 1.60; BTC OPHR long HP 21.29h / WR 33.68% / PLR 2.28, short HP 51.12h / WR 56.64% / PLR 1.87; ETH OP long HP 8.91h / WR 44.25% / PLR 1.51, short HP 47.56h / WR 60.98% / PLR 1.08; ETH OPHR long HP 9.16h / WR 47.17% / PLR 1.71, short HP 50.59h / WR 63.79% / PLR 1.18. Prose: "approximately 9-21 hours for long versus 50-51 hours for short".
- **Table 4 (costs as % of P&L):** BTC 4.15% / 5.21% / 9.36%; ETH 2.97% / 2.78% / 5.75%; Section 5.3 attributes the modest ratios to "measured trading frequency, with average holding periods of 9-51 hours (Table 3)".
- **Table 1 (splits)** and **Tables 5-7 (hyperparameters)** as quoted in `## Signal` above.
- **Training / test basis:** single 12-month test window on 2 underlyings at 1 venue; returns aggregated daily; 8 metrics defined in Appendix C.1.
- **Claim of significance:** none. There is no t-statistic, p-value, confidence interval, block bootstrap, seed count or error bar anywhere in the pinned PDF (term scan: `significan*` 0 hits, `t-stat` 0, `p-value` 0, `seed` 0; `error bar` appears only inside the checklist prompt text and the `[NA]` answer).

`our count` (arithmetic we performed on Table 2 / Table 4, explicitly not a source claim):

- OPHR − OP ablation gap: **BTC TR +11.67pp (33.10 − 21.43), ETH TR +21.40pp (44.89 − 23.49)**; ASR gap **+0.68 (BTC)** and **+0.91 (ETH)** — the entire measured benefit of the hedger-routing layer in TR terms.
- OPHR − best non-RL baseline (DLOT row): **BTC +28.19pp, ETH +43.70pp** in TR.
- ETH OPHR **MDD 27.25% with AVOL 24.42%** — a double-digit drawdown is present in the flagship row.
- Table 4 total cost is only **9.36% / 5.75% of P&L**, i.e. the strategy's edge, as reported, is an order of magnitude larger than its modeled fees — but the fees are the *only* modeled cost class.

### Independently reproduced

Not independently reproduced. No Qlib, NautilusTrader, or any local backtest has been run on this record; no figure above has been recomputed by us.

### Negative evidence

1. **Zero statistical inference:** no significance tests, seeds, error bars or repeated runs; the checklist answer explicitly declines statistical significance (`[NA]`, "one history … no parallel universe"). A single 12-month test path therefore carries the whole claim.
2. **Single window, single regime:** test = 23/07/01 – 24/07/01 only; no subperiod, no walk-forward, no second crypto-vol regime (e.g. the 2025 cycle) — regime robustness `unproven`.
3. **Look-ahead teacher by construction:** the Oracle initialization uses `future RV` (Section 4.3). The source does not demonstrate that the deployed OP-Agent no longer inherits that advantage beyond its offline use; no placebo/shuffled-label test exists.
4. **The ablation is confounded with cost:** Section 5.3 attributes the low cost ratio to 9-51h holding periods; the `OP → OPHR` gain could equally come from trading less rather than from better hedger selection. No frequency-matched control is reported.
5. **Baseline weakness is visible in Table 2:** e.g. BTC Short Volatility shows **WR 73.91% with TR 2.90** (our observation: win rate alone is not an edge signal here), and BTC Long Volatility **TR −33.05**; the mean-reversion row is byte-identical across BTC and ETH (frontmatter contradiction), which undermines confidence in the baseline table's transcription.
6. **Cost model is a single class:** only Deribit commission + an implicit market-order spread. **Funding on the perpetual hedge leg, slippage, market impact, capacity, latency, borrow/assignment are all `data gap`** — none are set to zero, none are modeled.
7. **Released code cannot reproduce the paper as shipped:** empty README, no LICENSE, lower-bound-only dependencies, zeroed perp fee vs the paper's 0.05%, sample test window differing from Table 1, `__pycache__` committed, **ETH sample data absent** (only `sample_data/BTC/option_chain/*.parquet` for 2024-01-01..2024-03-31 plus `perp.parquet` / `volticker.parquet`).
8. **Self-contradiction on code release** in the same checklist (Yes vs NA) — frontmatter contradiction.
9. **Metric-definition oddity:** Appendix C.1 defines Calmar as `ACR = E[ret]/MDD × m` while MDD is a cumulative drawdown and returns are daily-aggregated; TR is defined on "margin balance" (`TR = (V_t − V_1)/V_1`) without stating the currency/unit of that balance (`code-derived` base = BTC). Ratios may not be comparable to our own metric stack.
10. **No cross-record contradiction is claimed here; conversely, no independent corroboration exists in this repository.** Absence of a negative replication is not evidence of absence: `none identified in the reviewed sources; absence is not evidence of no negative result`.

## Falsification plan

Every item below is `research-defined` (our failure thresholds) or `research-proposed` (our operationalization); none is source-reported.

- **F1 — Held-out regime extension (`research-defined`).** Re-run OP timing + fixed hedger vs OP timing + learned hedger routing on **≥ 3 non-overlapping 12-month Deribit BTC/ETH test windows** spanning at least one high-vol and one low-vol regime. **Failure rule:** if the routing layer's annualized Sharpe improvement over the fixed hedger is ≤ 0 in ≥ 2 of 3 windows, the "hedger routing is the mechanism" claim is rejected.
- **F2 — Seed sensitivity (`research-defined`).** ≥ 5 training seeds per arm. **Failure rule:** if the 90% bootstrap interval of the OPHR−OP TR gap contains 0 for either underlying, reject.
- **F3 — Block bootstrap on daily returns (`research-defined`).** 20-day circular block bootstrap on the OPHR daily-return series; **failure rule:** lower 95% bound of annualized Sharpe ≤ 0 → reject tradability claim (the source provides no such interval at all).
- **F4 — Full cost ladder (`research-defined`).** Re-price with 0/1×/2× Deribit commission **plus** explicit half-spread on both legs **plus** **observed 8h funding on the perpetual hedge leg** (currently `data gap`) **plus** a 5–20 bp one-way impact buffer. **Failure rule:** if net TR or Sharpe turns negative at 1× fees + observed funding, the strategy is `not-tradeable-as-described`.
- **F5 — Instrument-selection placebo (`research-proposed`).** Because the contract-selection rule for OPHR is `underspecified`, pre-register one rule (nearest-ATM straddle, maturity 60-90 days, same as Appendix C.3) and a random-contract control. **Failure rule:** if random-strike/expiry selection matches the pre-registered rule within ±20% of TR, the reported edge is not in the stated mechanism.
- **F6 — Oracle look-ahead audit (`research-defined`).** Verify by unit test that `future_information` (present in `env/base/perpetual.py`) is only reachable in Phase-1 training and never in evaluation. **Failure rule:** any test-period path that reads `future RV` → invalidates all results.
- **F7 — Cost/frequency-matched control (`research-proposed`).** Compare against a static IV−RV rule (long if IV < RV−β, short if IV > RV+β, β ∈ {0.1, 0.2}) with the *same* hold-time distribution. **Failure rule:** if the static rule matches OPHR's ASR within 10%, the RL layer adds no demonstrated value.
- **F8 — Data/vendor cross-check (`research-defined`).** Rebuild the hourly chain from a second vendor or from Deribit's own API and require **≥ 99% timestamp agreement**; **failure rule:** below 99% → treat Table 2 as unreproducible.
- **F9 — Point-in-time / survivorship audit (`research-defined`).** Confirm the chain includes only quotes observable at the decision timestamp and that expired contracts are handled without removal-before-expiry. **Failure rule:** any look-ahead in chain assembly → reject.
- **F10 — Venue / underlying transfer (`research-defined`).** Port to a second options venue (e.g. Binance/OKX/Bybit options) and to ETH-only and BTC-only sub-portfolios; **failure rule:** ASR < 0 on either sub-portfolio → the BTC/ETH aggregate is not robust.
- **F11 — Capacity (`research-proposed`).** Scale notional against Deribit recorded volume until realized shortfall exceeds 10% of the backtest's modeled fill; **failure rule:** capacity below the proposed 5 BTC-equivalent order size → mark `capacity-limited`.
- **F12 — Baseline-table integrity (`research-defined`).** Recompute all Table 2 baseline rows from the released code; **failure rule:** any row that cannot be reproduced (starting with the identical BTC/ETH Mean-Reversion row) → downgrade the entire baseline comparison to `unverified`.

## Crypto portability

**Portability: `direct` — with an important scope caveat.** The source is itself crypto evidence: Deribit BTC and ETH inverse options hedged with Deribit perpetuals, 24/7, with funding-rate fields present in the data layer. Nothing has to be ported from TradFi.

Scope caveat and crypto-specific risks (all `source-reported` gaps unless noted):

- **Spot vs perpetual:** hedge is the perpetual future, so **8-hour funding on the hedge leg is economically material and is not in the paper's cost model** (`data gap`) — F4 must add it before any adoption decision.
- **24/7 sessions / candle boundaries:** hourly bars with no stated exchange-timezone convention; candle boundary treatment for Deribit's settlement and funding times is `underspecified`.
- **Venue fragmentation / custody:** single-venue result (Deribit); no withdrawal, custody, or venue-default discussion → `data gap`.
- **Liquidity / impact:** no capacity, participation or impact model for either the option legs or the hedge leg → `data gap`.
- **Contract specification:** inverse (crypto-denominated) options with portfolio margin; porting to **linear** options or to a perp-only stack changes the P&L unit, margin math and the TR definition → `adapted` for those destinations, `unproven` for any venue the source did not test.
- **Mark/index price and liquidation:** PM stress grid is described, but liquidation/maintenance-breach behavior is not → `data gap`.

Crypto portability is not authorization to trade.

## Limitations

- **Source quality:** peer-reviewed NeurIPS 2025 paper (high provenance quality) but **weak empirical hygiene for a trading claim**: one run, no seeds, no error bars, one 12-month test window, 2 underlyings, 1 venue.
- **`underspecified`:** contract/strike/expiry selection and roll rule for OPHR's own positions; state feature vector; position sizing; stop/exit rules; step→wall-clock cadence (paper vs released config conflict); TR's balance unit; gross/net labeling of Table 2; timezone/snapshot convention; capacity.
- **`data gap`:** funding, slippage, spread series, market impact, latency, borrow/assignment, liquidation handling, vendor provenance, missing/stale data handling, survivorship of the option-chain universe, seed count, and any statistical inference.
- **Reproducibility:** released code (single commit `8c3aeadef62bc16ab92dc3594b21183b56ec1342`) has an empty README, no LICENSE, unpinned dependencies, committed bytecode, zeroed perp fee vs the paper's 0.05%, a sample test window that differs from Table 1, and BTC-only sample data (no ETH).
- **Internal contradictions** (5 recorded in frontmatter): abstract period vs Table 1; checklist code-release Yes vs NA; perp fee paper vs config; test window paper vs config; identical BTC/ETH Mean-Reversion row.
- **Publication-bias / arena concern:** NeurIPS-accepted "we beat all baselines" trading papers are subject to selection on novelty; baselines are reimplemented by the authors, and 14-baseline style comparisons elsewhere in this repository routinely show large degrade-out-of-sample. No independent group has reproduced this result as of 2026-09-25 (`not independently reproduced`).
- **Mechanism is not isolated:** no static IV−RV control and no frequency-matched control, so the delta-hedged vol-premium effect cannot be separated from the RL machinery.
- **Ordinary-content rule:** this record is written because it clears the incremental threshold — new family (multi-agent OP/HR with **learned hedger routing**), new signal construction (counterfactual-advantage hedger selection), new crypto-options execution evidence, and new falsification items — not because it reports a high return.

## Implementation status

`implementation_status: not-implemented`. Nothing in this record has been implemented in our stack: no Qlib backtest, no NautilusTrader strategy, no Paper/Testnet/Live run, no dataset acquisition, no reproduction of the paper's code. The only work performed here is source capture, primary-source checksum verification, and repository dedup. Implementation authorization is a separate decision.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

Presence of this record does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. Research capture is not adoption.

## Related Wiki records

Read-only Wiki Brain search performed before writing (`options volatility trading gamma delta hedging` → 10 pages; `reinforcement learning trading agent crypto perpetual hedging` → 4 pages). Verified existing adjacent pages:

- [[quant/transformer-ddqn-straddle-option-volatility-trading-2026-09-05]] — nearest neighbour: also RL on option-volatility, but a *different source* (single-agent DDQN, resistance-aware straddle timing) with no hedger-routing component; the mechanism here (cooperative OP/HR MDP with counterfactual-advantage hedger selection) is materially distinct.
- [[quant/spy-options-svi-surface-rv-falsification-adverse-selection-2026-09-12]] — same IV/RV-versus-friction theme, equity options and a falsification-first design; useful contrast for F4/F8.
- [[quant/bitcoin-option-rnd-low-volatility-high-vrp-regime-2026-09-01]] — crypto option-implied regime evidence; relevant to whether the VRP/vol regime needed by this strategy is present.
- [[quant/exploratory-reinforcement-learning-sequential-optimal-stopping-pairs-trading-2026-09-05]] — RL methodology neighbour in a different signal family.

Sibling records in this staging pool (same lab, different papers, confirmed unrelated to this source): `fineft-risk-aware-ensemble-rl-vae-routing-crypto-futures-2026-09-03.md`, `archetype-trader-vq-rl-hierarchical-crypto-perpetual-2026-09-13.md`. No Wiki page was written or modified by this Scout run.

## Sources

1. Zeting Chen, Xinyu Cai, Molei Qin, Bo An, *"OPHR: Mastering Volatility Trading with Multi-Agent Deep Reinforcement Learning"*, **Advances in Neural Information Processing Systems 38 (NeurIPS 2025) Main Conference Track**, DOI **10.52202/085713-1764**. https://proceedings.neurips.cc/paper_files/paper/2025/hash/4c7dbef8023a15c4b81dc95a6ea08bf3-Abstract-Conference.html (abstract page + author/volume/track/DOI metadata; read 2026-09-25).
2. Same paper, pinned PDF: https://proceedings.neurips.cc/paper_files/paper/2025/file/4c7dbef8023a15c4b81dc95a6ea08bf3-Paper-Conference.pdf — fetched 2026-09-25, **1,352,171 bytes, SHA-256 `e61e4794adb82c98fe32f7d6b8ba3719742174ba92e0055058ce73d58ac68b57`, 31 pages**. Provenance for every table reference used here: **Table 1** (splits), **Table 2** (all performance rows), **Table 3** (long/short behaviour, holding periods), **Table 4** (transaction costs), **Table 5** (OP-Agent hyperparameters), **Table 6** (hedger parameters), **Table 7** (HR-Agent hyperparameters), **Appendix C.1** (metric definitions), **Appendix A.2** (inverse options), **Appendix A.3** (portfolio margin), **Appendix C.3** (baseline instrument selection), **Section 5.1** (datasets/setup), **Section 5.3** (Transaction Cost Analysis), **Section 4.3** (Oracle initialization rule), **NeurIPS Reproducibility Checklist** (error-bar `[NA]`, code-release answers).
3. OpenReview forum: https://openreview.net/forum?id=2p4AtivyZz (NeurIPS 2025 Poster, submission 7551; read 2026-09-25; PDF endpoint returned HTTP 403 / bot challenge on that date).
4. Code release: https://github.com/Edwicn/OPHR-MasteringVolatilityTradingwithMultiAgentDeepReinforcementLearning at **full commit SHA `8c3aeadef62bc16ab92dc3594b21183b56ec1342`** — paths read: `README.md`, `requirements.txt`, `config.py`, `configs/env_config.yaml`, `configs/evaluation_config.yaml`, `env/rl_env.py`, `env/base/perpetual.py`, `env/base/volatility_tickers.py`, `backtest/backtest.py`, plus the recursive file tree (read 2026-09-25). All statements sourced from here are labelled `code-derived`.
5. arXiv API negative check (2026-09-25): `ti:"Mastering Volatility Trading"` and `all:"OPHR" AND all:"volatility"` both returned 0 entries — no arXiv version of this paper exists as of that date.
