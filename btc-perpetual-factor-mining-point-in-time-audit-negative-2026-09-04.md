---
schema: strategy-research-record-v1
title: "Point-in-Time Audit Before Alpha: Negative Matched-Budget Factor-Mining Study on BTC Perpetual Futures"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - negative-result
  - btc-perpetual
  - factor-mining
  - point-in-time
status: research-only
confidence: high
source_as_of: 2026-08-26
sources:
  - "https://arxiv.org/abs/2608.25348"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Point-in-Time Audit Before Alpha: Negative Matched-Budget Factor-Mining Study on BTC Perpetual Futures

## Provenance

- **Authors:** Baocheng Zeng, Jinhao Yang, Peilin Han, Kangnan He
- **arXiv:** 2608.25348v1 [cs.SE]
- **Published:** 2026-08-26
- **DOI:** 10.48550/arXiv.2608.25348
- **Stable URL:** https://arxiv.org/abs/2608.25348
- **Full text HTML:** https://arxiv.org/html/2608.25348v1
- **Reproducibility materials included:** Yes (per abstract: "scoped negative-result preprint; reproducibility materials included")
- **Comments:** 11 pages, 4 figures

**Primary Source Verification:** Authors, title, date, and abstract confirmed via arXiv API (id_list=2608.25348). Full paper text read and all quantitative claims below are extracted directly from arXiv:2608.25348v1 Sections 5.1–5.5.

## Economic mechanism

### Source-reported

The authors investigate whether public cryptocurrency data archives can support rigorous factor research on BTC perpetual futures. The core mechanism tested is whether formulaic factor mining — using a DSL with moving-average, momentum, and volume-based operators — can produce economically viable trading signals on Binance BTCUSDT USD-M perpetual futures after enforcing strict point-in-time availability constraints. The paper's central question is not whether alpha exists, but whether public-archive timing semantics and deterministic auditing change false-discovery rates and whether an adaptive search agent outperforms baselines.

### Research interpretation

This is a **negative-result study**: the paper demonstrates that:

1. Public Binance perpetual futures data has significant point-in-time availability gaps that invalidate naive factor research.
2. A deterministic auditor reduces false passes (78.5% reduction) but does not independently establish masking effects.
3. An adaptive audited agent does not outperform random search on qualified candidates.
4. All factor candidates — despite positive holdout IC — yield negative net Sharpe under every tested cost combination.

The falsifiable hypothesis under test was: "Point-in-time auditing changes the false-discovery landscape in crypto perpetual factor mining." The paper supports this for the auditor component but rejects profitability, agent superiority, and independent masking effects.

## Signal

The paper does **not propose a single trading signal**. Instead, it benchmarks factor-mining search methods (adaptive audited agent, random search, tree GP) against a deterministic auditor on BTC perpetual futures.

**Search DSL:** Maximum AST depth 4, at most 5 operator nodes, lookbacks of 3/6/12/24/48/96/288 five-minute bars.

**Candidate qualification:** Valid candidates must pass audit, be unique, have ≥0.95 finite coverage, and have finite train/validation IC. Further qualification requires BH-FDR q<0.10, dependence-aware interval excluding zero, performance above random-search 90th percentile, and |correlation|<0.8 deduplication.

**Composite signal:** At most 5 qualified factors per run, direction-corrected on validation data, z-scored, equally weighted. Position = sign of composite, delayed by one completed decision bar, sampled non-overlapping at target horizon (15 or 60 minutes).

**Parameters:** 5 seeds (11, 23, 37, 53, 71) × 2 horizons (15min, 60min) × 100 valid candidates = 1,000 valid candidates per method.

**Signal is underspecified for standalone reconstruction** — this is a meta-study of search methods, not a single reproducible signal. The DSL, selection pipeline, and composite construction are documented but the specific discovered factors are not the paper's contribution; the negative economic result is.

## Required data

- **Instrument:** Binance BTCUSDT USD-M perpetual futures
- **Venue:** Binance (public archive: data.binance.vision)
- **Market type:** USD-M perpetual futures
- **Timeframe:** 5-minute bars (primary), with 15-minute and 60-minute evaluation horizons
- **Fields:** Trade OHLCV, mark price, index price, realized funding rate (core); open interest (optional, excluded due to unverified publication time)
- **Point-in-time:** Availability time = close_time + 1 ms; funding uses event time + 5 min assumption (tested at 0/5/10/15 min lag)
- **Sample period:** 2024-08-01 to 2026-08-01 (727 complete UTC days after availability masking)
- **Split:** 436 train / 145 validation / 146 holdout days (60/20/20, timestamp-only)
- **Missing-data:** Interpolation, backward fill, cross-gap forward fill, timestamp snapping, deletion of conflicting duplicates, and venue mixing are all prohibited. Missing observations removed via explicit mask.

## Execution assumptions

- **Signal-to-order timing:** One completed decision bar delay (non-overlapping)
- **Order type:** Market order assumption
- **Fill model:** Assumed full fill at bar close
- **Fees:** Primary model: 6 bp taker fee per side + 2 bp slippage per side
- **Fee sensitivity grid:** 4/5/6/8/10 bp fee × 1/2/5/10 bp slippage = 20 combinations per evaluated run (460 total cells across all methods)
- **Realized funding:** Charged only when position crosses a settlement event
- **Slippage:** Assumed per-side; aggregated bars do not support capacity or live-tradability claims
- **Impact / capacity:** Not modeled; the paper explicitly states aggregated bars and assumed slippage do not support capacity claims
- **Leverage / margin:** Not specified
- **Latency:** Not specified (5-minute bar granularity)
- **Partial fills / failures:** Not modeled

## Evidence

### Source-reported

**Data audit results (Section 5.1):**
- Original exact-grid requirement (trade+mark+index+OI, continuous 5-min): **304.57 days** — FAILED the 365-day requirement
- Revised core (trade+mark+index+funding, OI optional): **727 complete UTC days**
- Trade: 210,240 rows, 730 dates, no exact-grid gap
- Mark: 209,952 rows, 729 dates, 288 missing bars on 2026-06-29
- Index: 209,952 rows, 729 dates, 288 missing bars on 2026-06-29
- Funding: 2,190 events, 730 dates, no separate publication-time field
- OI: 210,235 rows, 730 dates — excluded (9 missing, 3 off-grid, 1 conflicting duplicate, 501 archive-order reversals)

**Auditor benchmark (Section 5.2):**
- Illegal templates detected: **40/40** (Wilson 95% CI: [0.9124, 1.0000])
- Legal templates falsely rejected: **0/40** (Wilson 95% CI: [0.0000, 0.0876])
- All 40 rejection reasons matched the injected violation class

**Null controls (Section 5.3):**
- At 5% missingness with availability masking:
  - No audit: mean false passes = **0.2910**
  - Full audit: mean false passes = **0.0625**
  - Relative reduction: **78.5%** (paired path-bootstrap 95% CI [-0.2595, -0.2012], sign-test p=0.001953)

**Search comparison (Section 5.4):**
- Audited agent: 39 qualified candidates (yield 3.9/100 valid)
- Random search: 39 qualified candidates (yield 3.9/100 valid)
- Tree GP: 29 qualified candidates (yield 2.9/100 valid)
- Audited agent **tied** random search; agent superiority rejected

**Historical holdout (Section 5.5):**
- Audited agent: mean test IC = **0.2352** [0.1551, 0.3552], RankIC = 0.2136
- Random: mean test IC = **0.1907** [0.1164, 0.2681], RankIC = 0.1826
- Tree GP: mean test IC = **0.1550** [0.1262, 0.1765], RankIC = 0.1375
- **All evaluated runs: 0/N positive net Sharpe** (audited 0/8, random 0/8, tree GP 0/7)
- **All 460 fee-slippage cells: 0 positive Sharpe**
- Best observed Sharpe values: -6.3148, -5.5009, -5.4938 (all deeply negative)
- Mean drawdown: -0.9291 (audited), -0.9460 (random), -0.9008 (GP)
- Turnover: 5,158–6,653 (very high)

**Economic summary:** Positive IC did not imply economically usable strategy. The combination of high turnover, transaction costs, and signal decay destroyed all predictive value.

### Independently reproduced

Not independently reproduced.

### Negative evidence

This IS a negative-result paper. The primary findings are:
1. Public Binance perpetual data has significant availability gaps invalidating naive factor research
2. The deterministic auditor reduces false passes but does not independently establish masking effects
3. The adaptive audited agent ties random search (no agent superiority)
4. All factor candidates yield negative net Sharpe under every tested cost combination (0/460 positive Sharpe cells)
5. Positive IC did not translate to economic viability — the signal is overwhelmed by trading costs

Additional negative evidence from the paper:
- One-bar delay (conservative): 0/23 positive Sharpe
- Extreme-observation deletion: no run remained economically positive
- The simulation did not distinguish exact-grid deletion from availability masking
- PBO improvement was negligible (Δ = -0.001429)

## Falsification plan

This paper is itself a falsification study. The authors explicitly designed it as a one-time historical holdout with frozen rules. Key falsification elements:

1. **Template auditor validity:** 40 illegal + 40 legal templates; acceptance required ≥38/40 illegal detected, ≤2/40 legal falsely rejected. Result: 40/40 detected, 0/40 false rejection.
2. **Null-signal controls:** 10 null paths × 100 candidates each; full audit reduced false passes by 78.5%.
3. **Economic viability:** 460 fee-slippage combinations × 23 evaluated runs = 0 positive Sharpe.
4. **Agent superiority:** Audited agent tied random search (39 vs 39 qualified candidates).

**Falsification thresholds (research-defined):**
- Agent superiority: If audited agent produces >10% more qualified candidates than random, claim is supported. Result: 0% difference → rejected.
- Profitability: If any of the 460 cost cells produces positive Sharpe, profitability claim is supported. Result: 0/460 → rejected.
- Independent masking effect: If PBO improvement >0.01, masking is supported. Result: Δ=-0.0014 → rejected.

## Crypto portability

**Not applicable** — this study is inherently crypto-specific (Binance BTCUSDT USD-M perpetual futures). The data audit and point-in-time methodology could be adapted to other perpetual futures venues, but the specific negative result (0/460 positive Sharpe cells) is conditional on this single asset, venue, and cost model.

**Crypto-specific risks the paper identifies:**
- Public archive data may have unverified publication times (funding, OI)
- Perpetual-specific mechanics (realized funding, mark/index price) require special handling
- 24/7 markets compound timestamp alignment issues
- Venue fragmentation and data quality issues (archive-order reversals, conflicting duplicates)

## Limitations

- **Single asset and venue:** Limited to Binance BTCUSDT USD-M; cannot establish cross-market validity.
- **Retrospective lock:** Holdout interval ended before protocol lock; one-time access is not prospective validation.
- **Funding-time assumption:** 5-minute lag assumed without a distinct publication timestamp.
- **OI excluded:** Publication time unverified; archive contains gaps, off-grid records, conflicting duplicate, and 501 ordering reversals.
- **Template scope:** Audit benchmark covers known injected rules, not unknown or adversarial leakage.
- **Incomplete search curves:** Budgets 30 and 300, first-discovery counts, and resource-normalized comparison were not executed.
- **Missing baseline:** LightGBM and broader nonlinear baselines were not completed.
- **Execution approximation:** Aggregated bars and assumed slippage do not support capacity or live-tradability claims.
- **No external validation:** No second asset, exchange, or genuinely future interval.
- **Not independently reproduced**
- **cs.SE classification:** Paper is classified under Software Engineering, not quantitative finance categories; the finance-specific contribution is the negative economic result, not the auditor framework per se.

## Implementation status

No implementation in our research stack. The paper is a negative-result study; the specific DSL factors and search pipelines are not proposed for adoption.

## Adoption boundary

This record is research material only. A record being present in this repository does **not** mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

The paper's explicit conclusion: "The evidence supports an audit-focused negative-result paper, not a profitability or general agent-superiority claim."

## Related Wiki records

- [[quant/crypto-intraday-sign-mean-reversion-15m-walk-forward-2026-09-01]] — Studies short-horizon mean reversion on the same Binance perpetual data; uses different methodology (sign-based reversal, not formulaic factor mining) and arrives at a different (marginal gross) conclusion.
- [[quant/crypto-short-horizon-15min-mean-reversion-taker-flow-2026-09-01]] — Companion to the above; provides taker-flow conditioning evidence.
- [[quant/aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03]] — Studies LLM-driven factor discovery (SEADS); the negative result here suggests public-archive timing is a critical prerequisite that SEADS does not address.
- [[quant/crypto-open-interest-crash-rebound-flow-gap-2026-09-03]] — Uses AQuA's crypto factor discovery results; this paper's exclusion of OI due to unverified publication time is directly relevant.

## Sources

1. Baocheng Zeng, Jinhao Yang, Peilin Han, Kangnan He, "Point-in-Time Audit Before Alpha: Public-Archive Availability and a Negative Matched-Budget Study on BTC Perpetual Futures," arXiv preprint `arXiv:2608.25348v1 [cs.SE]`, submitted August 26, 2026. DOI: [10.48550/arXiv.2608.25348](https://doi.org/10.48550/arXiv.2608.25348). Full text: https://arxiv.org/html/2608.25348v1.
