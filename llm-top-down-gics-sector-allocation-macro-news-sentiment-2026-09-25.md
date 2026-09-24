---
schema: strategy-research-record-v1
title: LLM Top-Down Macro → GICS Sector Allocation with News Aspect-Sentiment Stock Selection (S&P 500 Long-Short)
created: 2026-09-25
updated: 2026-09-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - llm
  - sector-allocation
  - macro-regime
  - news-sentiment
  - long-short
status: research-only
confidence: medium
source_as_of: 2025-04-10
sources:
  - "Ryan Quek Wei Heng, Edoardo Vittori, Keane Ong, Rui Mao, Erik Cambria, Gianmarco Mengaldo, 'Leveraging LLMS for Top-Down Sector Allocation In Automated Trading' (abs-page title casing), arXiv:2503.09647v5 [cs.CE primary, q-fin.PM cross-list], v5 Thu 10 Apr 2025 02:53:25 UTC, CC BY 4.0. https://arxiv.org/abs/2503.09647"
  - "Pinned full text read this run: https://arxiv.org/html/2503.09647v5"
  - "DataCite DOI: https://doi.org/10.48550/arXiv.2503.09647 (HTTP 302 → abs page, checked 2026-09-25)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions:
  - "Source-internal unreconciled backtest window (checked against pinned arXiv:2503.09647v5 HTML, 2026-09-25): Section 3 Data Source states 'The backtesting period was limited to January 2019 through June 2019 due to constraints on computational resources and cost', Section 3 later restates 'backtesting window of 6 months, 2019-Jan to 2019-Jun', and the Table 1 caption prints 'Backtesting results from Jan-2019 to Jun-2019', while Section 7 Limitations calls it 'the relatively short backtesting period from 2019 to 2024'. Both window definitions are printed in the same pinned version and never reconciled; the headline 8.79% / Sharpe 2.51 are attached to the 6-month caption, so the record uses the 6-month window and flags the 2019–2024 claim as unverified."
---

# LLM Top-Down Macro → GICS Sector Allocation with News Aspect-Sentiment Stock Selection (S&P 500 Long-Short)

## Provenance

- **Primary source:** arXiv:2503.09647, *"Leveraging LLMS for Top-Down Sector Allocation In Automated Trading"* (abs-page title; the v5 body title prints the same paper as *"Leveraging LLMs for Top-Down Sector Allocation in Automated Trading"* — casing/wording variant of one document, recorded, not treated as two sources).
- **Authors (exactly six, per abs-page `citation_author` metadata and the v5 HTML author block, checked 2026-09-25):** Ryan Quek Wei Heng (College of Design and Engineering, National University of Singapore; ryanquekweiheng@u.nus.edu); Edoardo Vittori (CVA Management and A.I. Investments, IMI Corporate and Investment Banking, Intesa Sanpaolo); Keane Ong (College of Design and Engineering, NUS; Asian Institute of Digital Finance, NUS; keane.ongweiyang@u.nus.edu); Rui Mao (College of Computing and Data Science, Nanyang Technological University; rui.mao@ntu.edu.sg); Erik Cambria (College of Computing and Data Science, NTU; cambria@ntu.edu.sg); Gianmarco Mengaldo (College of Design and Engineering, NUS; Asian Institute of Digital Finance, NUS; Sustainable and Green Finance Institute, NUS; Honorary Research Fellow, Imperial College London; mpegim@nus.edu.sg). `citation_author` order prints `Heng, Ryan Quek Wei` first (submitter "Ryan Wei Heng Quek").
- **Version/date:** five versions — `[v1] Wed, 12 Mar 2025 08:41:36 UTC (217 KB)`, `[v2] Tue, 18 Mar 2025 14:37:14 UTC (218 KB)`, `[v3] Tue, 1 Apr 2025 17:54:27 UTC (218 KB)`, `[v4] Sat, 5 Apr 2025 17:44:25 UTC (191 KB)`, `[v5] Thu, 10 Apr 2025 02:53:25 UTC (192 KB)`; `citation_date` 2025/03/12, `citation_online_date` 2025/04/10; HTML header prints `arXiv:2503.09647v5 [cs.CE] 10 Apr 2025`. **v5 pinned**; no cross-version number splicing (v1–v4 full texts not diffed → any pre-v5 difference is `data gap`, but no figure in this record is taken from anything but v5).
- **Subjects:** primary *Computational Engineering, Finance, and Science (cs.CE)*; cross-list *Portfolio Management (q-fin.PM)* (abs page, checked 2026-09-25).
- **Publication status:** abs-page `Comments`, `Journal-ref` and publisher `DOI` fields all empty → no journal version; the v5 body prints *"Preprint accepted to ICLR Workshop Advances in Financial AI: Opportunities, Innovations, and Responsible AI on March 5, 2025"* → **workshop acceptance only**; any peer review beyond that workshop is `not stated in source`. DataCite DOI `10.48550/arXiv.2503.09647` → HTTP 302 → abs page (verified 2026-09-25). License: **CC BY 4.0** (v5 HTML header line "License: CC BY 4.0").
- **Full text read this run:** `https://arxiv.org/html/2503.09647v5` (188,022 bytes fetched 2026-09-25; tag-stripped text 50,491 chars), containing Sections 1–8, References, and Appendix 9.1 (sentiment prompt) / 9.2 (FOMC minutes prompt) / 9.3 (top-down Ranking-Agent prompt) / 9.4 (cross-sectional Ranking-Agent prompt). Document contains exactly **Figure 1** (agentic-flow diagram) and **Table 1** (the only results table); the "Table 2.8.7" string in the text is a U.S. BEA PCE data-table caption, not a results table.
- **Funding / support (source-reported, Acknowledgments):** MOE Tier 1 Startup project `#22-3565-A0001-1`; MOE Academic Research Fund Tier 2 (STEM RIE2025 Award `MOE-T2EP20123-0005`); RIE2025 Industry Alignment Fund – Industry Collaboration Projects (IAF-ICP) Award `I2301E0026`, administered by A*STAR; also "supported by Alibaba Group and NTU Singapore". Conflicts-of-interest statement: none printed → `data gap`.
- **Code / data availability:** no code, repository, GitHub, replication-package or data-availability statement anywhere in v5 (keyword scan this run) → **not reproducible from the source**; news corpus (300,000 NewsAPI articles) and agent outputs are not released → `data gap`.
- **Cost-treatment determination (mandatory Methods-level read + pinned-v5 word-boundary scan, 2026-09-25):** the single cost sentence sits in Section 5 Methodology — *"A commission rate of 10 basis points per trade was applied to reflect standard institutional brokerage fees, while market impact costs of 10 basis points were included to account for price slippage during execution"*, with initial capital USD 100M. Whole-document word-boundary counts: `slippage` 1, `commission` 1, `market impact` 1, `fees` 1 (all four inside that one sentence), `bid-ask` 0, `spread` 0, `latency` 0, `borrow` 0, `shorting` 0, `short sale` 0, `short-sell` 0, `margin` 0, `fill` 0, `dividend` 0, `risk-free` 0, `annualized`/`annualised` 0, `temperature` 0, `seed` 0, `confidence interval` 0, `t-stat` 0, `p value` 0, `bootstrap` 0, `multiple testing` 0, `deflated` 0, `drawdown` 0, `win rate` 0, `leverage` hits are the verb "leveraged/leverages" (not a margin rule), `turnover` 2 (both inside printed prompt text, never a measured quantity), `funding` 1 (arXiv footer "Major funding support"). → **only** a flat 10bp commission + 10bp market-impact/slippage per trade exists; no spread, borrow/stock-loan, short-side, dividend, fill, latency, participation, capacity or risk-free-rate model exists, and everything missing is recorded as `data gap`, **never as zero cost**. Whether "per trade" is per side or round-trip is `underspecified`.
- **Repo-wide source-identity dedup (2026-09-25):** ripgrep across **all 2,521 `*.md` files including hidden trees** (`.mimo-worktrees/`, `.agents/`, `.hermes/`) plus `coverage_manifest.csv` (5,808 lines) for `2503.09647`, the DataCite DOI, both exact title variants (`Leveraging LLMs for Top-Down Sector Allocation` / `Leveraging LLMS for Top-Down Sector Allocation In Automated Trading`), `Quek`, `Vittori`, `Mengaldo`, `Keane Ong`, `top-down sector allocation`, `cross-momentum strategy` → **zero hits**. Fresh-candidate screen this run also confirmed already-captured neighbours (arXiv 2608.21888, 2609.12227, 2609.05485, 2608.14014, 2607.09426, 2608.04373, 2606.29591, 2607.01550, 2607.26188 all exist as records) and were skipped.
- **Four-axis distinction from nearest existing captures (different source identity in every case):** `llm-persona-ensemble-stock-bond-portfolio-cpi-regime-timing-2026-09-22.md` (persona-ensemble 40/60 stock–bond timing → different asset mix, different mechanism); `mfast-market-friction-aware-llm-news-sentiment-quintile-2026-09-22.md` (news-sentiment quintile factor → cross-sectional text factor, no macro→sector hierarchy); `commodity-etf-macro-interpretation-multi-agent-llm-debate-2026-09-04.md` (commodity ETFs → different universe); `llm-macro-analog-cpi-nowcast-factor-ranking-walkforward-2026-09-22.md` (CPI nowcast factor ranking → forecasting task, no portfolio); `small-cap-alpha-beta-separation-uncertainty-aware-llm-portfolio-2026-09-02.md` (Russell 2000 small-cap uncertainty-aware covariance → different universe and allocation problem); `retrieval-augmented-llm-expert-switching-portfolio-management-2026-09-03.md` (expert-switching RAG → different mechanism). This record's mechanism (hierarchical three-phase macro analysis → 11-GICS sector target allocation → within-sector news-aspect long/short stock selection), signal construction (DeepSeek-7B ABSA aspect sentiments + Llama-3.3-70B sector phase), universe (S&P 500 constituents, long **and** short) and horizon (daily agent loop over a 6-month window) are distinct in all four axes.
- **Schema provenance:** structure and frontmatter follow the canonical Wiki Brain contract resolved this run — `kb_read` `quant/strategy-research-record-spec-v1.md` (10,289 bytes, sha256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`); `kb_read` v2 → file not found → **v1 remains canonical**. `README.md` (575 lines) re-read this run.

## Economic mechanism

### Source-reported

The authors argue macroeconomic forces propagate heterogeneously across the 11 GICS sectors (inflation constrains manufacturing but helps services/agriculture; hawkish Fed communication raises borrowing costs and amplifies negative sentiment in vulnerable firms — Sections 1–2.2), and that this cross-sector heterogeneity is exploitable top-down. Their agent stack therefore (i) converts CPI/PPI/PCE/NFP/PMI month-over-month changes plus an LLM summary of FOMC minutes into a macro view, (ii) maps that view onto overweight/underweight targets across the 11 GICS sectors, and (iii) inside each favoured sector ranks constituent stocks using aspect-level sentiment extracted from news, taking long positions in favoured names and short positions in disfavoured ones (Section 4). Claimed outcome (abstract, Section 1, Section 6, Section 8): the sector-allocation strategy returns **+8.79% with Sharpe 2.51** versus the paper's own cross-momentum baseline at **−1.39% and −0.61** over the printed window, which the source calls "significant" outperformance (no statistical test is reported for that word).

### Research interpretation

Falsifiable hypothesis: **macro-regime-conditioned sector rotation, combined with news aspect-level sentiment for within-sector long/short selection, produces US-large-cap cross-sectional alpha beyond a momentum baseline after realistic costs.** Component roles: *Regime* = Llama-3.3-70B macro phase over CPI/PPI/PCE/NFP/PMI + FOMC summaries; *Primary signal* = the phase-2 sector target allocation; *Selection* = phase-3 within-sector ranking from DeepSeek-7B ABSA sentiment pairs (aspect ∈ 14-item taxonomy, score ∈ {−1,0,1}); *Decision/confirmation* = Llama-3.2-3B conversion to JSON orders; *Risk/exit* = full liquidation when the daily ranking flips a stock's sentiment outlook, automatic liquidation of names leaving the S&P 500, 90% maximum capital utilization. Nothing in the source isolates each component's contribution (no ablation), so it is an open question whether the edge — if real — comes from the macro phase, the sentiment phase, the long/short construction, or the single six-month sample. Competing explanations that must be eliminated before believing the mechanism: (a) Jan–Jun 2019 was a benign, mildly rising equity tape, so a long-biased tilt alone could explain +8.79%; (b) the baseline is a deliberately weakened LLM variant that *lost* money, so the contrast may measure baseline quality rather than macro skill; (c) LLM sampling randomness (temperature/seed unstated) could have produced one lucky run; (d) unmodelled borrow/dividend/spread effects on the short and long legs.

## Signal

Source-reported elements (all from pinned v5):

- **Formation timestamp:** one ranking per trading day. Temporal guard printed in Section 4: the Ranking Agent "only processes news memories published on the previous trading day and macro memories based on their official release dates, using the latest available data points for each economic indicator" — i.e. signal for day *t* uses news with `published_date` ≤ previous trading day and macro values by release date (point-in-time handling is asserted, timezone/venue of the news timestamp not stated → `data gap`). The PCE series for 2018-12/2019-01/2019-02 was released off-schedule during the federal government shutdown, and the source states the latest previously available data was used instead (explicit point-in-time accommodation, source-reported).
- **Lookback / memory:** a "Sentiment Memory Module" stores historical (ticker, aspect, score) pairs and a "Macro Memory Module" stores FOMC summaries with memory/reflection circles in Figure 1; **no retention window, decay or retrieval depth is printed** → `underspecified`.
- **Inputs:** macro trend readings `CPI {value}, PPI {value}, PCE {value}, NFP {value}, PMI {value}` (month-over-month percentage changes computed by the Macro Agent), an LLM FOMC-minutes summary (prompt 9.2: rate decisions, forward guidance, dissent, GDP/labor/inflation/financial conditions, upside/downside risks), the S&P 500 universe with `date|ticker|aspect_sentiment_pairs`, and the current long/short book with weights (prompt 9.3).
- **Sentiment construction:** NewsAPI articles retrieved by keyword search over company names and "global market identifiers", 300,000 articles spanning the 6-month window (Section 3); Sentiment Agent = **DeepSeek-7B-Chat** doing NER + ABSA (prompt 9.1: only explicitly discussed information, only aspects from the fixed taxonomy, content-only evidence, consistent aspect naming, no duplicates, **3–5 most significant aspects per article**, most common ticker; taxonomy = revenue/sales, earnings/profit, market_share, product_performance, management, growth, competition, regulatory, innovation, customer_demand, operational_efficiency, partnerships, risk, strategy; scores illustrated as 1/−1 and described in prompt 9.4 as −1/0/1).
- **Long entry:** Ranking Agent phase 3 prioritizes stocks in macro-favoured sectors, ranks them by sentiment within sector, and emits `Positions to Long: [TICKER] (Sector) — macro alignment / sector view / supporting sentiment / position size recommendation [X%]` (prompt 9.3 output format). Decision Agent (Llama-3.2-3B) converts the reflection to JSON orders; Portfolio Management Agent executes.
- **Short entry:** same format under `Positions to Short`; prompt 9.3 explicitly carries `Short positions: [(TICKER, weight)]` in the state, and Section 4 says the phase "enabl[es] the selection of stocks best positioned for both long and short positions within their respective sectors". **No borrow, locate, uptick, hard-to-borrow or short-sale-settlement rule is printed** → `data gap`.
- **Exit:** "positions are fully liquidated when new rankings indicate a shift in stock sentiment outlook"; positions in names removed from the S&P 500 during the window are "automatically liquidated" (Section 4, source-reported). No stop-loss, take-profit, maximum-holding or time-based exit exists → `not stated in source`.
- **Holding period / re-ranking:** daily re-ranking with turnover discouraged ("avoid unnecessary turnover", "Consider existing positions", "Rationale for maintaining existing positions" in prompt 9.3) but **no explicit holding period, minimum-hold or re-entry rule** → `underspecified`.
- **Position sizing:** Portfolio Management Agent enforces a **90% maximum capital utilization**; new positions are only initiated "when they do not create conflicts with existing holdings" (Section 4). The per-trade size inside the top-down strategy is whatever `Position size recommendation: [X%]` the LLM emits — **no numeric sizing rule is printed** → `underspecified`; any reconstruction's sizing rule is `research-proposed`. (The baseline cross-momentum arm fixes 1% of portfolio per trade, Section 5.)
- **Baseline (for comparison only):** cross-momentum arm runs only prompt 9.4 — composite score = sentiment scores reweighted by macro context, stocks ranked, long candidates = positive scores, short candidates = negative scores, duplicate long/short resolved toward the higher composite score, fixed 1% position size; the source describes it as building "a portfolio purely on momentum factors" while the printed prompt is sentiment+macro composite — an internal description mismatch worth flagging (`underspecified`).
- **Parameters:** 11 GICS sectors; models `deepseek-llm-7b-chat`, `Llama-3.3-70B-Instruct` (Ranking), `Llama-3.2-3B` (Decision); 90% utilization cap; 1%/trade (baseline); 10bp commission + 10bp impact; USD 100M initial capital; 6-month window. **Sampling temperature, seed, number of runs, and inference framework are not stated** → `data gap`.
- **Not specified by source → research-proposed for any reconstruction:** execution timestamp/price (same-bar vs next-bar, open vs close vs VWAP), order type, tie/simultaneous-signal precedence, per-side vs round-trip cost convention, sector-mapping vendor and as-of rule, memory retention window, position-sizing formula, short-borrow model, and all acceptance/failure thresholds below.

## Required data

- **Universe:** S&P 500 constituents **point-in-time** (the source says the set was dynamically updated as composition changed, giving the FRC-in/SCG-out example dated 2019-01-02; the membership source and as-of convention are not named → `underspecified`), with automatic removal of leavers.
- **Prices:** daily OHLC + volume from the **Alpha Vantage API** (accessed 2025-02-06 per References). Whether the series is split/dividend-adjusted is `not stated in source` → material `data gap` for an 8.79%-over-6-months claim (Section 6 defines portfolio change as final value including unrealized P&L minus trading costs; no dividend treatment appears anywhere — `dividend` count 0).
- **Sector labels:** GICS classification of each constituent across the 11 sectors; vendor and vintage `not stated in source` → `data gap`.
- **Macro:** CPI, PPI (U.S. Bureau of Labor Statistics), PCE (Bureau of Economic Analysis), NFP (BLS), ISM PMI (Investing.com economic calendar), FOMC meeting minutes/calendars (Board of Governors) — each with its **official release date** (the point-in-time key), plus month-over-month percentage changes as the LLM-facing representation.
- **Text:** NewsAPI articles (title, description, content, published date) for the 6-month window, ~300,000 items, keyword-matched to company names/identifiers. Corpus not released; historical availability/revisability of NewsAPI content for 2019 articles is `not stated in source` → point-in-time `data gap`.
- **Timestamp/timezone:** `not stated in source` (news timezone, daily decision cut-off, market close alignment) → `data gap`.
- **Missing data:** only the PCE shutdown substitution is described; all other stale/missing/suspension handling `not stated in source`.
- **Not required by source but required for a real long-short implementation:** borrow availability and cost, margin/financing, dividend entitlements on longs and payment obligations on shorts, spread/impact curves — all `data gap`.

## Execution assumptions

- Signal-to-order timing, order type, fill model, partial-fill/failure handling, latency, participation caps and capacity: **all `not stated in source`** (word-boundary counts above).
- Costs (source-reported, Section 5): **10bp commission per trade + 10bp market impact "to account for price slippage"**, applied to a USD 100M starting book; Section 6 states portfolio percentage change is net of these trading costs. Per-side vs round-trip convention `underspecified`.
- Spread, borrow/stock-loan for the short leg, margin/financing, dividends, and risk-free rate (needed to interpret "daily excess returns") are **absent from the source** → `data gap`, not zero.
- Leverage/margin limit: `not stated in source` (the only `leverage*` hits are the verb). Utilization is capped at 90% gross-style usage but gross-vs-net convention is `underspecified`.
- The source assumes a backtest fill environment; no live-execution claim is made or implied here.

## Evidence

### Source-reported

All figures below are third-party claims from pinned `arXiv:2503.09647v5` and have **not** been independently reproduced.

- **Table 1 (the only results table), caption: "Backtesting results from Jan-2019 to Jun-2019", Section 5:** Cross-Momentum → portfolio PCT change **−1.39%**, Sharpe **−0.61**; Sector-Allocation → portfolio PCT change **+8.79%**, Sharpe **2.51**. Same four numbers are repeated in the abstract, Section 1 and Section 8 (identical values in all four places — checked).
- **Metric definitions (Section 6):** portfolio percentage change = final portfolio value (including unrealized profit) minus trading costs; Sharpe ratio = daily excess returns ÷ standard deviation of portfolio returns. The **risk-free rate used, the annualization convention (6-month Sharpe 2.51 would be ~3.5 annualized from ~2.5 half-yearly), the number of trades, volatility, drawdown, hit rate, turnover and any per-period series are all `not stated in source`.**
- **Design claims:** dynamic S&P 500 membership updates to mitigate survivorship bias (Section 3); strict temporal filtering to prevent look-ahead (Section 4); dual-stream (news ∥ macro) pipeline with memory/reflection modules (Section 4, Figure 1); costs as in Execution assumptions.
- **Publication/venue claims:** workshop acceptance (ICLR WAF-AI, 2025-03-05) as printed in v5.

### Independently reproduced

not independently reproduced.

### Negative evidence

1. **Sample is six months (2019-01 → 2019-06), one regime, one country, one index** — and the paper's own Limitations contradicts this by calling the window "2019 to 2024" (frontmatter contradiction). No walk-forward, no hold-out, no second period, no second market.
2. **Zero statistical inference:** word-boundary counts over the pinned full text give `t-stat` 0, `p value` 0, `confidence interval` 0, `bootstrap` 0, `multiple testing` 0, `deflated` 0 — yet the abstract/Sections 1/6/8 use "significantly outperforms". The headline difference is untested.
3. **Single weak baseline.** The only comparator is the paper's own cross-momentum arm, which lost money (−1.39%, Sharpe −0.61). No S&P 500 buy-and-hold, no equal-weight 11-sector rotation, no buy-and-hold-per-sector, no published macro-timing rule, no FinMem/FinAgent-style peer. The comparison therefore cannot separate "top-down macro skill" from "any long tilt in H1 2019" or from "baseline implementation quality".
4. **Baseline description mismatch:** Section 5 says the baseline builds a portfolio "purely on momentum factors", but the printed prompt 9.4 ranks by macro-reweighted *sentiment* composite scores with no momentum term → the baseline is `underspecified`/mis-described.
5. **Sharpe definition incomplete:** "daily excess returns" with no stated risk-free rate and no annualization → 2.51 is not interpretable or comparable (`underspecified`).
6. **Short leg economics entirely unmodelled:** no borrow/locate/stock-loan cost, no settlement or recall rule, no uptick constraint (`borrow`/`shorting`/`short sale` cost-context hits = 0) while the strategy explicitly shorts S&P 500 names.
7. **Cost model is a flat 20bp-per-trade fiction:** no spread, no size/participation-dependent impact, no latency, no capacity analysis, and turnover is never reported even though the strategy re-ranks daily (`turnover` only appears inside prompts).
8. **Dividends ignored/undefined** (`dividend` 0): over a 6-month equity window, long-leg dividend treatment materially changes an 8.79% total-return claim; adjusted-vs-unadjusted Alpha Vantage series not specified.
9. **LLM stochasticity unaddressed:** temperature, seed, number of runs and inference stack not stated; a single run of a non-deterministic agent stack cannot support a "significant" claim.
10. **No component ablation:** macro phase, sector phase, sentiment phase and long/short construction are never separated, so the mechanism is unattributed.
11. **No released artifacts:** no code, no prompts-to-run harness beyond printed templates, no news corpus, no per-day positions → independent reproduction impossible from the source.
12. **Point-in-time text risk unexamined:** a retrospective NewsAPI crawl's 2019 availability (article edits, paywall truncation, removed content) is not discussed, so the "no look-ahead" claim covers timestamps only, not corpus reconstruction.
13. **Precedent of unstable LLM-allocation results** in the adjacent literature and the fact that a 6-month, single-benchmark, no-inference design is far below standard backtest practice → prior probability of the headline surviving honest evaluation is low (our assessment, `research interpretation`).
14. **Reporting gaps that block verification:** no drawdown, volatility, trade count, turnover, per-month returns, or portfolio composition printed anywhere (Sections 5–6 contain only Table 1).

## Falsification plan

All thresholds below are **`research-defined` / `research-proposed`** — none are in the source. Action on failure is stated for each; a failed gate keeps the hypothesis `research-only` and blocks implementation.

- **F1 — Point-in-time replication gate (`research-defined`).** Rebuild the pipeline on ≥ 3 years of unseen data (2023-01 → 2026-06 minimum, spanning rising, falling and high-vol regimes) with release-date-accurate macro and timestamped news. Fail if Newey–West t-stat of daily active return vs the S&P 500 is < 2.0, or if out-of-sample Sharpe (net of the cost ladder in F4) < 0.5. One-shot: no re-tuning after seeing the hold-out.
- **F2 — Baseline horse race (`research-defined`).** The same execution engine must beat, net of identical costs, all four of: S&P 500 buy-and-hold, monthly equal-weight 11-sector rotation, a non-LLM macro rule (fixed CPI/PMI sign rules), and a pure-momentum cross-section. Fail if any single comparator matches or exceeds the strategy's Sharpe (difference < 0.10 counts as a match).
- **F3 — Macro-phase ablation (`research-defined`).** Replace the Llama-3.3-70B macro/sector phase with a fixed, non-LLM sector rule while keeping sentiment and execution identical. Fail the *macro-LLM mechanism* if the Sharpe gap is < 0.30 — the claimed edge would then belong to sentiment or construction, not to LLM macro reasoning.
- **F4 — Cost ladder (`research-proposed`).** Re-run at 0/5/10/20/30 bp per side plus a 50 bp/yr stock-loan fee on the short leg. Fail if net Sharpe < 0.5 at 20 bp per side, or if the sign of total P&L flips versus the gross run.
- **F5 — Long-only ablation / short-side dependence (`research-defined`).** Run the identical stack with the short leg disabled, and separately with a 50 bp/yr stock-loan fee charged on shorts. Fail the *short-side* claim if the short leg contributes < 40% of gross P&L after borrow; fail the *whole-strategy* claim if the long-only variant drops below the F1 thresholds (NW t < 2.0 or net Sharpe < 0.5), which would indicate the reported edge rests on an unpriced short leg rather than on sector selection.
- **F6 — Determinism/repeatability (`research-defined`).** Run ≥ 5 independent seeds/temperature settings of the frozen agent stack. Fail if the monthly P&L sign disagrees across runs in more than 1 of 5 runs, or if the Sharpe range across runs exceeds 0.5.
- **F7 — Placebo (`research-defined`).** 1,000 circular-shift placebo of the macro/news input timeline (preserving autocorrelation and the cost/turnover profile). Fail if the true configuration does not exceed the placebo 95th percentile (`|z| ≥ 2.0`).
- **F8 — Multiplicity control (`research-defined`).** Over the printed evaluation grid (metric × baseline × window × ablation), apply Benjamini–Hochberg at q < 0.10 and require a deflated Sharpe ratio ≥ 0.95 against the number of configurations actually attempted (which the source does not disclose → must be self-declared). Fail if fewer than half the claimed effects survive.
- **F9 — Text point-in-time audit (`research-defined`).** Reconstruct the news feed from timestamped, immutable archives; fail if > 5% of cited articles were unavailable or materially different at signal time, or if re-running on the audited corpus moves Sharpe by > 0.5.
- **F10 — Price/universe consistency (`research-defined`).** Re-run on total-return (dividend-adjusted) prices with an as-of point-in-time index-membership table. Fail if the edge shrinks by more than 50% or if membership as-of errors exceed 1% of the constituent-days.

## Crypto portability

**unproven.** The source tests only US large-cap equities (S&P 500, 11 GICS sectors, long–short, daily, 6 months) and demonstrates nothing in crypto. GICS sectors have no crypto equivalent, so the sector phase cannot be ported directly; the only speculative analogue is *macro-liquidity regime + asset-level news/aspect sentiment → rotation among large-cap majors versus the long-tail*, which is an invented mapping (`research-proposed`, not source-supported). Porting risks: no index membership or GICS map (the universe/selection rule must be redesigned); 24/7 sessions remove the "previous trading day news" convention and the macro-release clock alignment; shorting requires perps (funding, liquidation, isolated margin) or borrow on spot — none modelled by the source; venue fragmentation breaks single-vendor adjusted closes; NewsAPI-equivalent crypto text is noisier, faster and heavily bot-generated; and the flat 10bp-per-trade cost assumption is unrealistic versus typical perp taker fees plus spread. Crypto portability is not authorization to trade.

## Limitations

- Six-month single-regime backtest with an internally contradictory window definition (frontmatter contradiction) — `not independently reproduced`, `underspecified`.
- No statistical inference anywhere despite "significantly" language; no drawdown/volatility/turnover/trade counts — `data gap`.
- Only one weak internal baseline; no external or passive benchmark — `underspecified` experimental design.
- Short-side, dividend, spread, fill, latency, capacity, risk-free-rate and leverage treatment all `data gap` (never assume zero).
- LLM sampling parameters and run counts not stated; agent outputs and news corpus not released; no code or replication package — `not reproducible from source`.
- Sector-mapping vendor/as-of, index-membership source/as-of, news timezone and daily cut-off, memory retention, and top-down position-sizing formula all `underspecified`.
- Publication status: arXiv preprint with a single workshop acceptance (ICLR WAF-AI 2025); no journal version, no peer-review statement beyond that; industry support disclosed (Alibaba Group; A*STAR-administered RIE2025 award; MOE grants) with no COI section — source-quality caveat.
- Cost numbers (10bp + 10bp per trade) are asserted institutional averages, not measured; per-side vs round-trip ambiguous — `underspecified`.
- Incremental-write check: this capture is the repository's first macro→GICS-sector→long/short LLM allocation record; no existing record shares its source identity or its three-phase signal construction (dedup evidence in Provenance).

## Implementation status

`implementation_status: not-implemented`. No implementation in our research stack exists: nothing has been coded, no agent stack assembled, no data pipeline built, no backtest run, and **no Qlib validation, Paper, Testnet or Live activity of any kind has occurred**. This record is a normalized research capture only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this file means only that a source-traceable research capture entered the public staging pool. It does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; or approved for implementation, paper trading, testnet or live trading. No record may promote itself by wording, evidence count, confidence or schedule.

## Related Wiki records

Wiki Brain `kb_search` this run: `"LLM sector allocation macro top-down portfolio"` → **0 results**; `"large language model trading agent equity"` → 10 adjacent pages (`quant/trading-r1-curricular-reinforcement-learning-llm-reasoning-2026-09-05.md`, `quant/moira-language-driven-hierarchical-reinforcement-learning-pair-trading-2026-09-05.md`, `quant/retail-agent-structured-adverse-timing-contrarian-alpha-2026-09-02.md`, `quant/alphalogics-market-logic-multi-agent-factor-generation-2026-09-05.md`, `quant/llm-news-sentiment-direct-rl-crypto-trading-ddqn-grpo-2026-09-06.md` and others) — all different mechanisms (RL trading agents, factor mining, crypto news-RL). **No Wiki page corresponds to this macro→sector-allocation mechanism, and none is asserted** (do not fabricate Wiki links).

## Sources

1. Ryan Quek Wei Heng, Edoardo Vittori, Keane Ong, Rui Mao, Erik Cambria, Gianmarco Mengaldo, *"Leveraging LLMS for Top-Down Sector Allocation In Automated Trading"*, `arXiv:2503.09647v5 [cs.CE; q-fin.PM]`, submitted 12 Mar 2025, v5 10 Apr 2025, CC BY 4.0 — https://arxiv.org/abs/2503.09647
2. Pinned full text (Sections 1–8, References, Appendix 9.1–9.4 prompts; Figure 1, Table 1) — https://arxiv.org/html/2503.09647v5
3. DataCite DOI — https://doi.org/10.48550/arXiv.2503.09647 (302 → abs page, checked 2026-09-25)
4. Workshop-acceptance line printed in v5: "Preprint accepted to ICLR Workshop Advances in Financial AI: Opportunities, Innovations, and Responsible AI on March 5, 2025".
5. Source-reported data dependencies (not evidence): Alpha Vantage API (https://www.alphavantage.co/), NewsAPI (https://newsapi.org), U.S. Bureau of Labor Statistics (CPI/PPI/NFP), Bureau of Economic Analysis (PCE), Investing.com ISM PMI calendar, Board of Governors of the Federal Reserve System FOMC minutes/calendars (https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm).
