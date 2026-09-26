---
schema: strategy-research-record-v1
title: "EvolveTrade: Experience-Driven Policy Refinement for Self-Evolving LLM Trading Agents — online rewrite of an LLM agent's tool-use policy on 15 US blue chips (arXiv:2609.17632v1)"
created: 2026-09-26
updated: 2026-09-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - llm-agent
  - self-evolving-policy
  - prompt-as-policy
  - tool-use
  - us-equities
  - large-cap
  - daily-rebalance
  - long-only
  - portfolio-allocation
status: research-only
confidence: medium
source_as_of: 2026-09-15
sources:
  - "https://arxiv.org/abs/2609.17632 (landing, checked 2026-09-26: arXiv:2609.17632v1 [cs.AI] 15 Sep 2026, primary category cs.AI with cs.CL cross-list, citation_date 2026/09/15, no Comments field, no journal-ref, license CC BY 4.0)"
  - "https://arxiv.org/pdf/2609.17632v1 (pinned PDF downloaded 2026-09-26: 823,098 bytes, 23 pages, SHA-256 0457b5268526fff9fed2d91e958bd977324aed7b33a31ab66cefea5d8c3fdae8; text extracted with pypdf 6.16.2 to 111,017 characters / 111,434 bytes; Sections 1-7, Tables 1-7, Appendices A-H and the Limitations block read, appendix prompt figures spot-read)"
  - "https://arxiv.org/html/2609.17632v1 (pinned LaTeXML HTML downloaded 2026-09-26: 1,461,496 bytes, SHA-256 4d6c22007b82676841096ad7b8bbc0e27b2d03e52a45b93ce599010e5ceffeb1; all seven tables re-extracted cell-by-cell from the raw HTML and cross-checked against the PDF text extraction — the EvolveTrade Table 1 row, the EvolveTrade Table 6 row, the 15-ticker asset list and the 10 bps sentence match in both renderings)"
  - "https://api.datacite.org/dois/10.48550/arxiv.2609.17632 (retrieved 2026-09-26: state 'findable', registered 2026-09-17T02:04:31Z, submitted 2026-09-15T10:35:18Z with dateInformation 'v1', creators Kim Sehee / Choi Yumin / Kang Minki / Hwang Sung Ju, rights CC BY 4.0, url https://arxiv.org/abs/2609.17632)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# EvolveTrade: Experience-Driven Policy Refinement for Self-Evolving LLM Trading Agents — online rewrite of an LLM agent's tool-use policy on 15 US blue chips (arXiv:2609.17632v1)

## Provenance

- **Paper**: Sehee Kim*, Yumin Choi*, Minki Kang, Sung Ju Hwang, *EvolveTrade: Experience-Driven Policy Refinement for Self-Evolving LLM Trading Agents*, arXiv preprint `arXiv:2609.17632v1 [cs.AI]`.
- **Author list and affiliations (verbatim from the pinned PDF title block)**: `Sehee Kim∗1 Yumin Choi∗1 Minki Kang1 Sung Ju Hwang1,2`; `1 KAIST`, `2 DeepAuto.ai`; `{sehee.kim, yuminchoi, sungju.hwang}@kaist.ac.kr`; `∗ Equal contribution.` No e-mail is printed for Minki Kang. (The arXiv HTML rendering separates names, affiliations and e-mails into blocks that do not line up one-to-one, so the PDF title block is the authoritative reading; the HTML-only artefact of Minki Kang carrying Sung Ju Hwang's address is a rendering artefact, not a second authorship claim.)
- **Version / date**: sole version **v1**, submitted **Tue, 15 Sep 2026 10:35:18 UTC** (arXiv submission history and DataCite `Submitted` date agree); DataCite records a later `Updated 2026-09-17T00:01:42Z` still labelled `v1`, i.e. no v2 exists — `arxiv.org/abs/2609.17632v2` and the API entry for the id both resolve to `v1`, checked **2026-09-26**. The HTML title page prints `arXiv:2609.17632v1 [cs.AI] 15 Sep 2026`.
- **Publication status**: **preprint only, not peer reviewed**. The arXiv landing has **no Comments field and no journal-ref** (arXiv API returns no `arxiv:comment`, no `arxiv:journal_ref`, no `arxiv:doi` element); no venue, no "under review" line, no acknowledgement, no funding statement and no conflict-of-interest statement appear in the pinned 23 pages. DOI `10.48550/arXiv.2609.17632` is registered through DataCite (state `findable`), which is an arXiv registration DOI and not evidence of peer review.
- **Licence**: CC BY 4.0 (printed on the PDF title page, `License: CC BY 4.0`; confirmed on the landing page and in the DataCite `rightsList`). Claims and printed figures are normalised and attributed; no source text is reproduced wholesale.
- **Code / data / AI-use**: word scan of the pinned PDF and HTML for `github`, `code availability`, `data availability`, `upon request`, `supplementary`, `repository` → the only `Data Availability` hits are **inside the appendix prompt templates** (they describe the agent's price/news availability, not an artefact statement), and the only absolute links in the PDF text are `https://openai.` and `https://storage.googleapis.` fragments from citation strings. **No code repository, no dataset link, no artefact or data-availability statement anywhere** → every availability field is `not stated in source`.
- **Source / data as-of**: six one-month post-cutoff evaluation windows — **January 2025, April 2025, September 2025 (GPT-5-mini)** and **November 2025, February 2026, April 2026 (Gemini-2.5-Flash)** — plus one 50-trading-day window **2025-09-02 – 2025-11-10** (Table 2 caption). Exact start/end dates of the six one-month windows are **never printed** (`data gap`). Manuscript as-of 2026-09-15; captured 2026-09-26.
- **Pre-write source-identity dedup (whole repository, hidden trees and manifest included)**: `2609.17632`, `10.48550/arXiv.2609.17632`, `EvolveTrade`, `Experience-Driven Policy Refinement`, `Sehee Kim`, `Sung Ju Hwang`, `Minki Kang`, `LiveTradeBench`, `Live-Trade-Bench`, `text-parameterized`, `EvolveStrategy`, `15 major US blue-chip` → **0 hits** across all `*.md`, `*.csv`, `*.json`, `*.txt` including `.mimo-worktrees/`, `.agents/`, `.hermes/` and `coverage_manifest.csv` (1,088,787 bytes), case-insensitive, before the write. `GPT-5-mini` → 10 files and `Policy Agent` → 0 files; the GPT-5-mini hits belong to other LLM-agent records with different source identities and are not EvolveTrade captures.
- **Four-axis material-distinction statement vs the nearest existing repository records**: (1) `factorminer-self-evolving-experience-memory-formulaic-alpha-2026-09-20.md` — also "self-evolving", but the mechanism is an experience *memory* that accumulates formulaic-alpha formulas for Chinese high-frequency mining, i.e. offline factor discovery, not an online rewrite of a deployed agent's operating prompt; different source, different universe, different horizon; (2) `llm-verifier-guided-strategy-genome-evolution-evoquant-2026-09-04.md` (arXiv:2607.12455v1) — evolves *typed strategy-genome code* under a verifier, offline, whereas EvolveTrade never touches code or weights and only edits the system prompt of a running agent; (3) `sok-farsight-llm-trading-agents-robustness-security-negative-evidence-arxiv-2609.19705-2026-09-19.md` — a negative-evidence survey of LLM trading schemes, no strategy, no policy-evolution mechanism; (4) `llm-agent-population-scale-behavioral-null-volatility-blind-sizing-2026-09-10.md` — an audit of agent sizing bias, no adaptation mechanism at all; (5) `retail-agent-structured-adverse-timing-contrarian-alpha-2026-09-02.md` — behavioural order-flow alpha inferred from retail agent flow, a different signal construction and data dependency. Source identity differs in every pair, and the mechanism differs in every pair: *online, feedback-conditioned rewriting of the tool-use procedure* versus experience-memory factor mining / genome evolution of strategy code / robustness survey / bias audit / retail-flow contrarian signal.

## Economic mechanism

### Source-reported

The paper's stated problem is that a tool-using LLM trading agent's behaviour is governed by a hand-written system prompt fixed before deployment, so the *procedure* by which it gathers evidence never revisits what its earlier trades revealed.

Three stated channels carry the argument:

1. **The policy is the trainable object, and it is text.** Section 3 defines the day-`t` state as `S_t = (π_t, t, P_{t-1}, 𝒯)`, where `π_t` is "the natural-language system prompt that guides the agent's tool use, evidence verification, risk control, and output requirements", `P_{t-1}` the previous portfolio state and `𝒯 = {t_price, t_news, t_code}` the toolset (a price tool, a news tool and a Python code interpreter, the first two "from recent autonomous trading frameworks (Fan et al., 2025)"). The frozen backbone `p_θ`, the context, the tools and the policy text jointly induce the action; LLM parameters and tool interfaces are fixed throughout.
2. **Static policy locks the analytic vocabulary (Section 4, Figure 2).** With a fixed policy under GPT-5-mini, the same five metrics (Sharpe, 20d return, 60d return, annualised volatility, drawdown) appear on **90–100% of days in all three regimes**, while regime-relevant computations (RSI, EMA, VaR, signal normalisation) "never appear at all"; news queries collapse to per-asset boilerplate and the price lookback stays "roughly six months on every call across all three regimes". The stated diagnosis: the subset of the LLM's analytic capability that gets invoked is decided at development time and never revisited, so the agent applies the same analytical scope to a −9.8% drawdown month as to a steady uptrend.
3. **Experience becomes a rewrite (Section 5).** After the allocation is submitted, the environment returns post-trade feedback `g_t` (daily portfolio return, per-asset returns, resulting allocations and portfolio state). Because `g_t` alone is ambiguous ("a loss may reflect flawed evidence gathering or an unavoidable market shock"), it is paired with the decision trace `h_t = (w_t, d_t^dec)` into a refinement record `ℛ_t = (h_t, g_t)`. The horizon is cut into batches of `N` days (policy held fixed inside a batch), and a separate Policy Agent performs `π_{kN+1} = f_update(π_kN, 𝓑_k) = LLM(I_update, π_kN, 𝓑_k)`, where `I_update` "asks the Policy Agent to analyze the records … identify which aspects of the current prompt most contributed to good or poor performance, and rewrite the full policy text accordingly", preferring "grounded edits over generic rewrites". A refinement step may revise tool selection, query formulation, signal interpretation, evidence verification, risk control or output structure.

The paper's two empirical claims (Section 1): online policy self-evolution "often improves LLM trading agents over fixed-policy baselines" — best SR and CR among LLM methods in three model-regime pairs — and the improvement is accompanied by measurable tool-use change (more code-mediated analysis, activation of regime-relevant metrics).

### Research interpretation

Stated as a falsifiable hypothesis rather than a finding: **if the mismatch between an agent's fixed analytic coverage and the current regime is real, then rewriting the *procedure* from realised feedback — with model, tools, universe and data held constant — should improve risk-adjusted performance over the identical agent with a frozen prompt, and the gain should survive a sham-update control that rewrites the prompt from shuffled feedback.** Component roles as printed: *regime* = **no explicit regime detector** — regime matching is claimed to emerge implicitly from feedback-conditioned rewriting (Figure 3 shows tail-risk metrics activated in the April drawdown window and trend-following indicators in the September uptrend window); *primary signal* = the frozen LLM's daily long-only target allocation over 15 equities plus cash, produced under the current policy text after mandatory `get_price` → `code_interpreter` → `news_searcher` calls; *confirmation* = the policy-required cross-checks (e.g. the initial prompt demands at minimum 20d return, annualised volatility and Sharpe per asset, and Figure 7's evolved policy converts metric tables into deterministic target weights with validation guardrails); *risk / exit* = **daily full rebalance to target weights with cash as the only sink** — no stop, no take-profit and no short book is specified, and the single-asset caps that do appear (e.g. 15% per name, 40% top-3, minimum 6 holdings, 3% daily micro-adjustment budget) are visible only in the **evolved** policy examples (Figures 12–16), not in the initial prompt (Figure 8). We do not assume any component contributes alpha; F4 and F8 below decide whether feedback *content* matters rather than prompt perturbation per se.

## Signal

**Source-reported construction (all from the pinned v1 PDF and its HTML rendering):**

- **Universe**: "15 major US blue-chip stocks (e.g., AAPL, MSFT, NVDA, JPM) and a cash component" (Section 6.1); the full list appears in the prompt templates: **AAPL, MSFT, NVDA, JPM, V, JNJ, UNH, PG, KO, XOM, CAT, WMT, META, TSLA, AMZN, CASH**. Static membership rule, no point-in-time reconstitution, no delisting handling discussed (`data gap`).
- **Environment**: "a daily-close simulation environment based on the LiveTradeBench (Yu et al., 2025a) framework"; on each trading day the system tracks the current portfolio, receives target percentage weights and "rebalances the portfolio at the daily closing price".
- **Formation timestamp / tradability**: one decision per trading day at the daily close; the agent "can access only information available before the allocation is submitted", and "all retrieval tools enforce the same temporal cutoff to prevent look-ahead leakage" — price data up to and including the close of day `t`, news only up to day `t-1` (Figures 8–11 prompt constraints, stated verbatim: *do NOT use any news from the trading date or later*).
- **Lookback**: the initial policy requires `get_price` for all tickers at once with a **3–12 month** lookback and mandates at minimum `20d return`, `annualised volatility` and `Sharpe ratio` per asset (Figure 8); Section 4 reports the *static* policy actually used a fixed ~six-month lookback on every call.
- **Entry / exit / holding**: the action is a feasible allocation `w_t ∈ 𝒲`, with `𝒲` "a long-only allocation simplex over the tradable assets and cash"; weights must sum to 1.0; **CASH is treated as a zero-volatility risk-free asset at a constant $1.0 that earns zero return**. The allocation "is executed after the decision time and evaluated over the next holding interval" (Section 3); Appendix E's worked example applies the September 10 allocation to September 11 prices. Holding period is therefore **one day**, with a full rebalance each close; no re-entry rule beyond the next day's decision; no shorts, no leverage.
- **Policy update**: `N = 5` trading days in all main experiments (Section 6.1); Trading Agent and Policy Agent **share the same backbone within each run**; initial policy templates and update prompts are Figures 8–11. Sensitivity over `N ∈ {1, 3, 5, 7}` is Table 3.
- **Rule-based baselines (Appendix A)**: SPY buy-and-hold of the SPY ETF; B&H equal-weight portfolio initialised at the window start; MACD (bullish/bearish signal-line crossovers), KDJ&RSI (oversold-reversal buys, overbought/weakening sells), ZMR (buy deviations below a recent reference, sell after reversion), SMA (short-above-long risk-on). All active strategies are capped at **1/N with N = 15 (≈6.7% per name)**, a sell signal exits the position to zero, and unallocated capital sits in cash earning zero return. **The numeric parameters of MACD / KDJ / RSI / ZMR / SMA (windows, thresholds, references) are never printed** (`underspecified`) — the rules are described only qualitatively.
- **Metrics (Appendix B)**: `R_t = (V_t − V_{t-1})/V_{t-1}`; `SR = √252 · R̄/σ_R` with sample daily σ (risk-free rate deliberately omitted "because the evaluation windows are one month long"); `CR = (V_T/V_0 − 1) × 100`; `MDD`; `WR` = share of days with positive return; `Vol` = daily σ in percentage points.
- **What is not reconstructible from the source (`data gap`, never invented)**: the exact date range of each of the six one-month windows; the turnover definition and units behind Table 6's `TO` column; baseline indicator parameters; the data provider behind `news_searcher`; any binding position constraint in the *initial* policy beyond "sums to 1.0"; whether hard constraints are enforced outside the prompt; LLM sampling temperature, seed and retry policy; the number of trading days per window.
- **Scout-labelled operationalisation (`research-proposed`, not from the source)**: pin the six window dates before looking at results; run ≥10 seeds per cell; enforce the 15% single-name cap in code rather than in prompt text; net a US-equity commission-plus-spread ladder; treat any threshold in the Falsification plan as `research-defined`.

## Required data

- **Instrument / universe**: daily closes for the 15 named US common stocks plus the SPY ETF (benchmark) over each evaluation window; CASH as a constant $1.0 zero-return asset. The list is static; a reproducer wanting survivorship safety should still document that the universe was chosen as persistent mega-caps (`data gap` on the selection rule).
- **Venue / market type**: US equity cash market, single-venue close auction implied by "daily closing price"; no derivatives, no shorts.
- **Timeframe / fields**: daily bars (OHLCV at least close and volume if turnover is to be recomputed); the agent additionally receives per-asset news up to `t-1` through `news_searcher`.
- **News**: provider, corpus and cutoff mechanics beyond "only available up to the day before the trading date" are `not stated in source`.
- **Point-in-time**: price and news cutoffs are enforced in the source's environment (stated); model knowledge-cutoff alignment is handled by choosing post-cutoff windows (stated) — but the *window selection rule itself* is `not stated in source`.
- **Timestamp / timezone**: no timezone is printed anywhere; "daily close" plus a US equity universe implies the US regular-session close, but this is `underspecified`, and the 24/7 or non-US analogue is undefined.
- **Cost inputs**: none are requested by the source's main pipeline — no fee schedule, commission, spread, borrow or impact model appears; the single robustness rung is a flat 10 bps proportional charge (Appendix D).
- **Missing data**: halted days, missing closes, corporate actions, dividends and the treatment of the ex-dividend gap are never discussed (`data gap`).

## Execution assumptions

**Cost determination from a Methods-level read** of Section 3 (Problem Setup), Section 6.1 (Trading Environment, Baselines, Implementation Details, Evaluation), Section 6.3, Section 7 Limitations, Appendix A (baseline definitions), Appendix B (metric definitions), Appendix D (trading friction), Appendix G (operational prompts) and Appendix H (evolved-policy examples), plus a word scan of the pinned 111,017-character text for `fee, commission, spread, bid-ask, slippage, market impact, liquidity, turnover, leverage, margin, borrow, financing, latency, fill, partial fill, capacity, participation, gross, net of`:

- **Gross-versus-net status is explicit.** Main Tables 1–3, 4 and 5 carry **no cost at all** (gross). Appendix D recomputes SR and CR "after applying a proportional transaction cost of **10 bps** to traded portfolio value" and reports turnover alongside.
- **The Limitations block states the boundary verbatim in substance**: these turnover/cost estimates "do not capture slippage, market impact, or liquidity constraints", and "future evaluation could incorporate these factors through more realistic execution models."
- Therefore `fees` (beyond the single 10 bp rung), `commission`, `spread`, `bid-ask`, `impact`, `participation`, `ADV`, `capacity`, `borrow`, `financing`, `leverage`, `margin`, `latency`, `fill / partial fill / failure handling`, and `funding` are **`data gap`, never zero**. `Turnover` is *reported* (Table 6 `TO` column) but **never defined** — no formula, no units, no whether it is one-way or two-way, daily or window-cumulative → `underspecified`.
- **Order / fill**: "rebalances the portfolio at the daily closing price" implies a market-on-close fill at the reference price with complete execution; order type, queue position, partial fills and latency are `not stated in source`, and the operational prompt declares "Latency is IRRELEVANT: Do NOT optimize for speed or execution timing. All decisions are made once daily."
- **Execution-timing ambiguity**: Section 3 says the allocation "is executed **after** the decision time and evaluated over the next holding interval", while the Appendix G prompt states "Decision, execution, and evaluation all happen at the **same closing price (t)**". Appendix E's worked example (Sept 10 decision → Sept 11 return) supports "set weights at close `t`, earn `t → t+1`", but the two sentences are not identical and are recorded as-is (`underspecified`).
- **Leverage / shorting / financing**: long-only simplex summing to 1.0 → no leverage and no short book are specified; cash earns **zero** return by construction (explicit in Appendix A and in the prompt). Margin, borrow and financing are therefore not applicable to the printed design rather than modelled.
- **Non-trading costs**: LLM inference/API cost is never reported (calls per day are material — three mandated tool calls plus a policy rewrite every `N` days) → `data gap`. API rate limits, tool failures and retry handling are `not stated in source`.
- Because the reported advantage is a *Sharpe difference between two agents over one-month windows* with gross returns, an unmodelled cost difference of even a few basis points per day could plausibly reorder the methods; the source bounds this only with one flat 10 bp rung and an undefined turnover column.

## Evidence

### Source-reported

All figures below are read from the pinned v1 PDF/HTML (SHA-256 `0457b526…`) and are third-party, source-reported; **none has been independently reproduced**. Metric order is `SR | CR % | MDD % | WR % | Vol %`; annualised SR per Appendix B (`√252`, no risk-free rate). LLM rows are averages over **three runs** (Tables 4–5 give the standard deviations).

**Table 1, GPT-5-mini panel — one-month windows Jan / Apr / Sep 2025 (`SR | CR%`):**

| Method | Jan 2025 | Apr 2025 | Sep 2025 |
|---|---|---|---|
| SPY (benchmark) | 2.77 \| 2.94 | −0.02 \| −1.15 | 8.22 \| 4.34 |
| B&H | 4.21 \| 4.11 | −0.44 \| −2.48 | 8.35 \| 5.79 |
| MACD | 3.16 \| 1.05 | −1.45 \| −1.37 | 5.72 \| 2.29 |
| KDJ&RSI | 4.98 \| 1.34 | 2.22 \| 5.13 | 3.54 \| 0.38 |
| ZMR | 5.62 \| 3.70 | 1.23 \| 3.49 | 5.82 \| 1.13 |
| SMA | 5.14 \| 3.27 | −3.99 \| −2.43 | 9.58 \| 5.31 |
| Static Base Agent | 1.55 \| 1.89 | −1.66 \| −5.06 | 5.88 \| 4.15 |
| Static TC Agent | 2.87 \| 3.30 | −1.54 \| −4.71 | 6.45 \| 4.86 |
| EvolveBase | 1.41 \| 1.82 | −2.87 \| −7.58 | 5.29 \| 3.80 |
| EvolveStrategy | 3.86 \| 4.70 | −3.09 \| −6.85 | 7.76 \| 4.78 |
| **EvolveTrade (Ours)** | **5.12 \| 5.10** | −2.53 \| −6.60 | **8.43 \| 6.84** |

**Table 1, Gemini-2.5-Flash panel — Nov 2025 / Feb 2026 / Apr 2026 (`SR | CR%`):**

| Method | Nov 2025 | Feb 2026 | Apr 2026 |
|---|---|---|---|
| SPY (benchmark) | 0.08 \| 0.01 | −1.34 \| −1.35 | 9.80 \| 9.68 |
| B&H | 0.16 \| 0.09 | 0.33 \| 0.23 | 11.30 \| 9.23 |
| MACD | 3.99 \| 0.92 | −5.82 \| −1.80 | 10.63 \| 7.39 |
| KDJ&RSI | 3.63 \| 1.39 | 0.68 \| 0.23 | 5.10 \| 0.98 |
| ZMR | 2.80 \| 1.15 | −1.49 \| −0.96 | 11.35 \| 4.10 |
| SMA | −1.04 \| −0.70 | 2.26 \| 1.09 | 5.72 \| 1.37 |
| Static Base Agent | −1.89 \| −1.73 | −2.04 \| −1.83 | 9.07 \| 11.64 |
| Static TC Agent | −1.99 \| −2.24 | 2.70 \| 2.29 | 6.62 \| 4.73 |
| EvolveBase | −2.28 \| −2.16 | −1.70 \| −1.38 | 7.98 \| 10.50 |
| EvolveStrategy | −1.04 \| −1.16 | 3.92 \| 3.52 | 3.66 \| 2.23 |
| **EvolveTrade (Ours)** | **−1.03 \| −1.07** | 2.75 \| 2.92 | 4.73 \| 3.69 |

**EvolveTrade full metric row (Table 1)**: Jan 2025 `5.12 / 5.10 / 2.39 / 57.0 / 0.84`; Apr 2025 `−2.53 / −6.60 / 9.13 / 46.7 / 2.01`; Sep 2025 `8.43 / 6.84 / 1.26 / 81.3 / 0.65`; Nov 2025 `−1.03 / −1.07 / 4.49 / 53.7 / 0.86`; Feb 2026 `2.75 / 2.92 / 2.66 / 51.9 / 0.95`; Apr 2026 `4.73 / 3.69 / 0.94 / 55.0 / 0.59`.

**Table 2 — 50 trading days, GPT-5-mini, 2025-09-02 – 2025-11-10 (`SR | CR% | MDD% | WR% | Vol%`)**: Static Base `1.82 / 4.51 / 4.70 / 68.0 / 0.82`; Static TC `2.94 / 8.88 / 4.40 / 63.3 / 0.95`; EvolveBase `2.41 / 4.79 / 3.00 / 65.3 / 0.65`; EvolveStrategy `3.27 / 6.94 / 2.82 / 65.3 / 0.68`; **EvolveTrade `4.00 / 10.56 / 2.96 / 67.3 / 0.81`**. No rule-based baselines appear in Table 2.

**Table 3 — update-interval sensitivity, averaged over the Jan / Apr / Sep 2025 GPT-5-mini windows (`SR | CR% | MDD% | WR% | Vol%`)**: `1 day 1.92 / 0.16 / 4.58 / 61.5 / 1.13`; `3 days 3.25 / 0.97 / 4.46 / 62.7 / 1.13`; `5 days 3.67 / 1.78 / 4.26 / 61.7 / 1.17`; `7 days 3.50 / 1.54 / 4.55 / 60.6 / 1.21`. Source's reading: non-monotonic, daily updates are worst ("overly frequent revision overfits short-horizon feedback").

**Tables 4–5 — standard deviations across three runs (`SR ± sd | CR% ± sd`)**: EvolveTrade Jan `5.12±0.51 | 5.10±0.72`, Apr 2025 `−2.53±0.47 | −6.60±1.19`, Sep `8.43±1.68 | 6.84±0.70`, Nov `−1.03±0.39 | −1.07±0.40`, Feb `2.75±0.29 | 2.92±0.25`, Apr 2026 `4.73±1.48 | 3.69±1.83`. Comparators: EvolveStrategy Jan `3.86±1.51`, Sep `7.76±0.47`, Feb `3.92±1.03`; Static TC Apr 2025 `−1.54±0.11`, Apr 2026 `6.62±0.78`; Static Base Apr 2026 `9.07±0.60`.

**Table 6 — turnover and performance after 10 bps proportional transaction cost (`TO | SR | CR%`, columns in order Jan / Apr / Sep 2025 GPT-5-mini, Nov 2025 / Feb 2026 / Apr 2026 Gemini-2.5-Flash)**: **EvolveTrade `1.05 | 5.01 | 4.99`, `1.20 | −2.58 | −6.71`, `1.68 | 8.21 | 6.67`, `1.93 | −1.23 | −1.26`, `1.44 | 2.62 | 2.77`, `1.90 | 4.48 | 3.49`**. For contrast, Static TC prints `2.25 / 2.53 / 1.90 / 2.32 / 2.27 / 3.21` TO and EvolveStrategy `2.22 / 3.32 / 2.98 / 3.27 / 3.04 / 4.39` TO. Source's reading: EvolveTrade keeps lower turnover than Static TC and EvolveStrategy in all six windows and retains the lead in the same three settings where it leads the main results.

**Table 7 — average cash weight, EvolveTrade minus the selected static baseline (Appendix F)**: Jan 2025 `12.9 vs 9.0 (+4.0pp)`, Apr 2025 `27.1 vs 17.1 (+10.1pp)`, Sep 2025 `8.0 vs 8.7 (−0.7pp)`, Nov 2025 `16.1 vs 9.7 (+6.4pp)`, Feb 2026 `10.7 vs 5.1 (+5.6pp)`, Apr 2026 `40.1 vs 4.3 (+35.9pp)`.

**Behavioural / case evidence**: Figure 2 — the static policy's five metrics appear on 90–100% of days in all three 2025 GPT windows while RSI/EMA/VaR/signal normalisation never appear; Figure 3 — after evolution, EvolveTrade invokes VaR and signal normalisation in the April drawdown and SMA/EMA/RSI in the September uptrend, which the Static TC baseline never calls; Figure 4 — mean daily `code_interpreter` calls rise from ~1.0 to **2.6–4.5** per day while price calls stay ~1 and news calls do not increase overall; Figure 5 — on 2025-01-24 the Static TC agent holds 10.7% NVDA versus EvolveTrade's 2.9% "under a refined sizing policy", NVDA falls 17.0% the next day, and the two agents post −0.03% versus −1.11% that day; Appendix E — a matched 2025-09-10 → 2025-09-11 comparison in which EvolveTrade's code-derived target weights produce `+1.1753%` versus the Static TC agent's `+0.6686%`, a **+0.5067pp** portfolio gap.

### Independently reproduced

not independently reproduced

We verified only the artefact and the reading: PDF byte count, page count and SHA-256 recorded above; full text extraction to 111,017 characters; the same seven tables re-extracted cell-by-cell from the pinned HTML and cross-checked against the PDF text (EvolveTrade's Table 1 row, Table 6 row, the 15-ticker list and the 10 bps sentence agree); DataCite DOI resolution and version history; and every quoted number located in its named table or section. No agent was re-run, no policy was re-evolved, no portfolio was re-balanced, and the source ships no code and no data.

### Negative evidence

1. **It is the best LLM method in only 3 of 6 windows.** The paper's own Section 1 tally: best SR and CR among LLM-based methods "in three model-regime pairs, while fixed-policy agents remain stronger in the other two". Table 1 shows the fixed-policy Static TC agent beating EvolveTrade in **both April windows** (Apr 2025: −1.54 vs −2.53 SR; Apr 2026: 6.62 vs 4.73 SR), and Appendix F explains it as a cash overweight of **+10.1pp and +35.9pp** — an unforced conservative tilt the method never corrects inside the window.
2. **The six-window tally is arithmetically incomplete.** `3 best + 2 fixed-better = 5`, yet six windows were run; the sixth (Feb 2026) is lost to **EvolveStrategy**, the policy-evolving baseline (`3.92 vs 2.75` SR). The sentence does not conceal a number, but it does leave the one window lost to another *evolving* method outside the count.
3. **Rule-based baselines usually beat it.** By SR, EvolveTrade is the top row in only **1 of 6** windows (Feb 2026, 2.75): Jan 2025 has ZMR 5.62 and SMA 5.14 above its 5.12; Sep 2025 has SMA 9.58 above 8.43; Nov 2025 puts EvolveTrade at **−1.03** while MACD 3.99, KDJ&RSI 3.63 and ZMR 2.80 are positive; Apr 2026 puts it 4.73 against SPY 9.80, B&H 11.30, MACD 10.63, ZMR 11.35, SMA 5.72 and KDJ&RSI 5.10. By CR it is the top row in 3 of 6 (Jan, Sep, Feb 2026), which is what Section 6.2's narrower "exceeds all rule-based baselines on return-side metrics in some regimes" claim rests on.
4. **No statistical test exists anywhere.** A word scan for `significan` (outside prompt prose), `p-value`, `confidence interval` and `statistical test` returns no inferential content: three runs per cell, standard deviations only, no test of EvolveTrade-minus-baseline. In Table 4 the January comparison is `5.12±0.51` (EvolveTrade) vs `3.86±1.51` (EvolveStrategy) — the intervals overlap.
5. **Sharpe is annualised from one month of daily returns.** `SR = √252 · mean/σ` on roughly 21 observations, with the risk-free rate deliberately omitted (Appendix B) — SR values of 8.43 or 9.07 are annualisation artefacts of tiny samples, not comparable to any monthly-frequency Sharpe.
6. **`N = 5` may be selected in-sample.** Table 3 reports that `N = 5` is the best of {1,3,5,7} *on the same three GPT-5-mini windows used for the main results*, and `N = 5` is then the main setting; no held-out interval selection or pre-registration is stated (`underspecified`).
7. **Window selection is not specified.** Windows are chosen as "regimes after each model's knowledge cutoff" (sideways / drawdown-recovery / uptrend / bearish / sideways / bullish) with exact dates never printed; regime labels are applied ex post, so selection-on-outcome cannot be ruled out from the document.
8. **Cost evidence is one flat rung with an undefined turnover column.** 10 bps proportional, explicitly excluding slippage, market impact and liquidity constraints; `TO` is printed for every method with no formula or units, so neither break-even cost nor cost-per-unit-turnover can be derived.
9. **Turnover is still material for a "low turnover" claim.** EvolveTrade's `TO` runs 1.05–1.93 across windows on a portfolio that is fully re-targeted every trading day over 15 names; the comparison that matters (does the 10 bp charge preserve the *ranking* against the best fixed baseline, not against other LLM agents?) is reported only against LLM rows.
10. **Main tables are gross.** Tables 1–3, 4 and 5 contain no cost of any kind; commissions, spread and borrow for US equities are never modelled.
11. **Rule-based baseline parameters are not printed.** MACD / KDJ / RSI / ZMR / SMA are described qualitatively in Appendix A, so the headline "beats traditional rules" comparison cannot be re-implemented faithfully (`underspecified`).
12. **Sample identity is only partially pinned**: one 50-day window has dates (Table 2); the six headline one-month windows do not.
13. **Execution-timing wording conflicts** between Section 3 ("executed after the decision time and evaluated over the next holding interval") and the Appendix G prompt ("decision, execution, and evaluation all happen at the same closing price (t)").
14. **A source-internal numeric mismatch**: Section 1 attributes a **+1.33 percentage-point** relative daily return difference to the NVDA case, while Section 6.3 / Figure 5 for the same case prints −0.03% versus −1.11%, i.e. **+1.08pp**. The record does not reconcile them (`underspecified`); Appendix E's +0.5067pp belongs to a different, September, case.
15. **Risk limits are endogenous to the prompt.** The 15% single-name cap, 40% top-3 cap, minimum-6-holdings rule, ≥2% rebalance trigger and 3% daily micro-adjustment budget appear in the *evolved* policies (Figures 12–16), not in the initial prompt (Figure 8), and the source never states that any constraint is enforced outside the prompt text — so a rewritten policy could in principle loosen its own risk rules (`underspecified`).
16. **Which edit helps is not isolated.** EvolveStrategy (strategy text only) vs EvolveTrade (whole policy incl. tool protocols) is reported as two systems, with no breakdown of which class of edit — tool orchestration, signal interpretation, risk text, output format — carries the gain, and no sham-update control.
17. **Environment and tooling are proprietary/undocumented**: LiveTradeBench-based simulation, `news_searcher` provider unstated, no fill model, no partial fills, latency declared irrelevant; LLM inference cost per trading day is never reported.
18. **Scope**: one universe (15 persistent US mega-caps), long-only, daily close, two backbones, three runs, six one-month windows, no subperiod analysis, no multiplicity control across 6 windows × 11 methods × 2 backbones, no capacity or ADV analysis, no crypto evidence.
19. **Status**: arXiv v1 preprint with no venue, no peer review, no code and no data; all performance claims are third-party, source-reported and (for the main tables) gross.

## Falsification plan

Every threshold below is `research-defined` (Scout-chosen) and every operational rule not printed by the source is `research-proposed`. Data: the same 15-ticker US universe on daily closes plus SPY, with the source's six windows re-run and ≥3 later calendar-month windows added that were not used in the paper. Action on failure: record the hypothesis as disproved for this deployment and drop the candidate — no retuning of thresholds after seeing results.

- **F1 — frozen forward replication.** Fix the policy templates, `N = 5` and all prompt text; run ≥10 seeds on ≥3 pre-registered later one-month windows. **Pass** only if EvolveTrade beats the Static Tool-Calling Agent by ≥ 0.50 annualised SR with a seed-level bootstrap 95% CI on the difference excluding zero in at least 2 of 3 windows. **Fail** otherwise.
- **F2 — cost ladder (decisive for tradability).** Net the identical book at 0/5/10/20/30 bp per side plus a US-equity commission schedule, and recompute the ranking against Static TC *and* against the best rule-based baseline. **Fail** if the EvolveTrade-minus-Static-TC advantage at the source's own 10 bp rung shrinks by more than 50% of its gross value, or if the ranking flips at 20 bp.
- **F3 — turnover and capacity audit.** Publish an explicit one-way turnover definition (`research-proposed`: `0.5 · Σ|w_t − w_{t-1}|`, daily, averaged) and recompute Table 6; measure participation versus 10% of 20-day ADV on the 15 names. **Fail** if daily one-way turnover exceeds 25% on average or the book cannot be filled inside the participation cap.
- **F4 — decisive policy-evolution ablation (with a sham control).** Compare (a) EvolveTrade, (b) Static TC (same tools, frozen prompt), (c) EvolveStrategy, (d) **sham evolution**: the Policy Agent rewrites the prompt on the same cadence but with `g_t` replaced by shuffled feedback from another seed/window, keeping rewrite length and token budget matched. **Pass** only if (a) beats (b) and (d) by ≥ 0.30 SR — otherwise the gain is prompt perturbation or extra compute, not experience.
- **F5 — update-interval pre-registration.** Fix `N = 5` before any new window is scored and re-run `N ∈ {1,3,5,7}` only on a held-out set. **Fail** if the chosen `N` is not in the top-2 of the held-out ranking, or if the reported Table 3 ordering fails to replicate.
- **F6 — window-selection audit.** Pre-register exact window dates by calendar rule (e.g. every third calendar month) before looking at data. **Fail** if EvolveTrade's advantage exists only in the hand-described "regimes" and disappears on the calendar rule.
- **F7 — baseline-parameter audit.** Re-implement MACD / KDJ&RSI / ZMR / SMA with published, citable default parameters (documented as `research-proposed`) and re-run Table 1. **Fail** if the rule-based ranking changes materially versus the source's unparameterised description.
- **F8 — feedback-permutation null (decisive for the mechanism).** Circularly shift the feedback record `g_t` fed to the Policy Agent relative to the decision traces (1000 draws, matched rewrite budget). **Pass** only if the observed EvolveTrade SR exceeds the 95th percentile of the null distribution.
- **F9 — multiplicity.** Apply Benjamini–Hochberg over the full family of EvolveTrade-vs-baseline comparisons (6 windows × 10 comparators × 2 backbones). **Fail** if nothing survives `q < 0.10`.
- **F10 — seed and subperiod stability.** ≥10 seeds per cell, and split the 50-day Table 2 window into two contiguous halves. **Fail** if the seed-level CI on EvolveTrade-minus-Static-TC includes zero in ≥ 4 of the 6 windows, or if the two halves disagree in sign.
- **F11 — reproducibility gate.** If no code and no data become public within 12 months of 2026-09-15, mark the result permanently `unverifiable` and drop it regardless of printed numbers; if they do, a third party must reproduce Table 1's EvolveTrade row within ±0.30 SR and ±2pp CR across the six windows.
- **F12 — crypto port.** Re-run the identical framework (same prompts, `N`, tool roles) on a crypto universe with 24/7 candles and a funding-aware, liquidation-aware cost ladder. **Fail** if the EvolveTrade-minus-static advantage is below 0.30 SR after 10 bp plus funding, or if it exists only when funding is ignored.

## Crypto portability

**`unproven`.**

The source contains **zero crypto evidence**: all results are US large-cap equities traded at the daily close in a LiveTradeBench-style simulation, long-only, with SPY as the market benchmark. The *mechanism* — rewriting a frozen LLM agent's tool-use policy from realised feedback — is venue-agnostic in principle, but that is a porting hypothesis, not crypto empirical evidence, and this record marks it as such.

What would have to be re-specified before any crypto claim: the 24/7 session versus a single daily close decision; the definition of "close" and of the candle boundary (timezone is never printed even for equities); funding and mark/index price for perpetuals (entirely absent, as is any leverage or liquidation logic); the long-only simplex versus a two-sided book; the news cutoff at `t-1` under continuous trading; venue fragmentation and per-venue liquidity; and the flat 10 bp rung, which is not a crypto fee schedule. Long-only cash-as-sink also has no crypto analogue beyond a stablecoin leg with its own de-peg and yield assumptions.

Crypto portability is not authorisation to trade; F1, F2, F4 and F12 must pass before any deployment consideration.

## Limitations

- **`data gap`**: exact dates of the six one-month windows; news provider and corpus; timezone/session convention; all cost fields except the single 10 bp rung (commission, spread, slippage, impact, participation, capacity, borrow, financing, leverage, margin, latency, fill/failure handling); LLM inference cost; missing-data, dividend and corporate-action handling; universe selection rule; code and data availability.
- **`underspecified`**: turnover definition and units; rule-based baseline parameters; execution-timing wording (Section 3 vs Appendix G); whether risk caps are enforced outside the prompt; the source's own +1.33pp vs +1.08pp NVDA mismatch; the update-interval selection rule; seed/temperature/retry settings.
- **`not stated in source`**: any significance test, confidence interval or p-value; any pre-registration of `N`, windows or prompts; any ablation isolating which class of policy edit matters.
- **`not independently reproduced`**: every number in this record; we hashed and read the pinned PDF and re-extracted the tables from the pinned HTML, but re-ran nothing, and the source provides no code and no data.
- **`unproven`**: out-of-sample stability beyond six hand-described one-month windows; net-of-cost profitability; any capacity claim; multiplicity-adjusted significance; the claim that feedback *content* (rather than prompt perturbation) drives the gain; portability to crypto or to any non-US, non-daily-close market.
- **Design limitations**: annualised Sharpe from ~21 daily observations, three seeds, no statistics, rule-based baselines outperforming in most windows, both April losses explained by an uncorrected cash overweight, in-sample-looking interval selection, ex-post regime labelling, prompt-level risk limits, preprint status with no venue and no peer review.
- **Scope**: this is a record of *research material*. Presence in this repository does not imply the strategy works, was validated, or may be traded.

## Implementation status

`implementation_status: not-implemented`. No implementation exists in our research stack: no trading agent was instantiated, no policy was evolved, no portfolio was constructed, and no backtest, Paper, Testnet or Live run has occurred. The source itself ships no code and no data. Nothing here implies Qlib full-backtest validation or any downstream approval.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. This record did **not** pass Research Intake Review, did **not** enter Hermes Wiki Brain as an adopted record, did **not** enter the production candidate pool, did **not** complete Qlib validation, and did **not** become a frozen survivor or leaderboard entry. It is not evidence of profitability, not validated alpha, and not approval to implement, paper-trade, testnet-trade or trade.

## Related Wiki records

Mechanism-adjacent pages returned and verified by Wiki Brain `kb_search` for this run (`large language model trading agent` → 10 hits, of which the five linked below were used; `LLM trading agent self-evolving prompt policy` → 0 hits; `prompt optimization self-evolving agent portfolio` → 0 hits):

- [[quant/trading-r1-curricular-reinforcement-learning-llm-reasoning-2026-09-05]]
- [[quant/retail-agent-structured-adverse-timing-contrarian-alpha-2026-09-02]]
- [[quant/webcryptoagent-web-informatics-two-tier-agentic-crypto-2026-09-05]]
- [[quant/moira-language-driven-hierarchical-reinforcement-learning-pair-trading-2026-09-05]]
- [[quant/alphaschema-trading-semantic-plan-space-surrogate-guided-factor-mining-2026-09-05]]

No other Wiki Brain pages were verified for this record; no page is linked beyond the ten returned by the single productive query, and no Wiki Brain page exists for arXiv:2609.17632.

## Sources

1. Kim, S., Choi, Y., Kang, M., & Hwang, S. J. (2026). *EvolveTrade: Experience-Driven Policy Refinement for Self-Evolving LLM Trading Agents* (arXiv:2609.17632v1 [cs.AI], submitted 15 September 2026 10:35:18 UTC). arXiv. https://arxiv.org/abs/2609.17632 — DOI https://doi.org/10.48550/arXiv.2609.17632. KAIST (Sung Ju Hwang also DeepAuto.ai); Sehee Kim and Yumin Choi marked equal contribution; licence CC BY 4.0; no Comments field and no journal-ref on the landing page (checked 2026-09-26).
2. Pinned full text (PDF): https://arxiv.org/pdf/2609.17632v1 — 823,098 bytes, 23 pages, SHA-256 `0457b5268526fff9fed2d91e958bd977324aed7b33a31ab66cefea5d8c3fdae8`, downloaded 2026-09-26, text extracted to 111,017 characters (pypdf 6.16.2).
3. Pinned HTML rendering: https://arxiv.org/html/2609.17632v1 — 1,461,496 bytes, SHA-256 `4d6c22007b82676841096ad7b8bbc0e27b2d03e52a45b93ce599010e5ceffeb1`, downloaded 2026-09-26; Tables 1–7 re-extracted cell-by-cell from the raw HTML and cross-checked against source 2.
4. DataCite DOI record `10.48550/arXiv.2609.17632` (https://api.datacite.org/dois/10.48550/arxiv.2609.17632), retrieved 2026-09-26 — state `findable`, registered 2026-09-17, `Submitted 2026-09-15T10:35:18Z (v1)`, creators and CC BY 4.0 rights confirmed.
5. arXiv export API record for `2609.17632` (https://export.arxiv.org/api/query?id_list=2609.17632), retrieved 2026-09-26 — single entry `v1`, no `arxiv:comment`, no `arxiv:journal_ref`, no `arxiv:doi`.

All quantitative claims above are labelled source-reported and trace to Table 1 (both panels), Table 2, Table 3, Table 4, Table 5, Table 6, Table 7, Figure 2, Figure 3, Figure 4, Figure 5, Figure 6, Figure 7, Figures 8–16, Sections 1, 3, 4, 5, 6.1, 6.2, 6.3, 7 (Limitations), Appendix A, Appendix B, Appendix D, Appendix E, Appendix F, Appendix G and Appendix H of source 1 as rendered in sources 2 and 3. The main tables are gross of trading costs; Tables 1–5, 7 and the figures carry no cost model, and only Appendix D's Table 6 applies any cost (10 bps proportional). None of these results has been independently reproduced.
