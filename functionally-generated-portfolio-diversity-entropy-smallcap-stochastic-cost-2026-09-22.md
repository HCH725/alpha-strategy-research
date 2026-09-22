---
schema: strategy-research-record-v1
title: "Cost-Adjusted SPT Functionally Generated Portfolios: Diversity- and Entropy-Weighted Small-Cap Rotation Under Stochastic Transaction Costs (arXiv:2507.09196)"
created: 2026-09-22
updated: 2026-09-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-07-12
sources:
  - https://arxiv.org/abs/2507.09196
  - https://arxiv.org/html/2507.09196v1
  - https://arxiv.org/pdf/2507.09196v1
  - https://doi.org/10.48550/arXiv.2507.09196
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cost-Adjusted SPT Functionally Generated Portfolios: Diversity- and Entropy-Weighted Small-Cap Rotation Under Stochastic Transaction Costs

## Provenance

- **Primary source:** Nader Karimi, Erfan Salavati (Department of Mathematics and Computer Science, Amirkabir University of Technology, Tehran, Iran), *"Functionally Generated Portfolios Under Stochastic Transaction Costs: Theory and Empirical Evidence"*, arXiv preprint `arXiv:2507.09196v1 [q-fin.PM]`, submitted **12 Jul 2025 08:29:29 UTC** (single version; arXiv API entry `published = updated = 2025-07-12T08:29:29Z`).
- Abstract / landing: https://arxiv.org/abs/2507.09196
- Full text HTML (v1, used for all section/table extraction): https://arxiv.org/html/2507.09196v1
- PDF: https://arxiv.org/pdf/2507.09196v1
- arXiv-issued DOI: `10.48550/arXiv.2507.09196`
- **arXiv metadata (verified via abs page + export.arxiv.org API, 2026-09-22):** authors exactly `Nader Karimi`, `Erfan Salavati`; Comments field `15 pages, 6 figures`; primary category `q-fin.PM` (sole category); **no `journal-ref`, no publisher DOI, no statement of peer review** → publication status = **preprint v1, peer-review status `not stated in source`**; license shown on HTML as **CC Zero**.
- **Provenance discrepancy (marked, not repaired):** the v1 HTML body renders a date line `August 24, 2026` beneath the author block, which is inconsistent with the v1 submission timestamp of 12 Jul 2025. Research interpretation: this is most likely a LaTeX `\date{\today}` evaluated at HTML-conversion time; the arXiv submission history is treated as authoritative for the version date. The paper does not explain the line → `underspecified`.
- **Verification integrity:** this record was written after direct reading of the v1 HTML full text (Sections 1–6, Tables 3–4, Figures 5–6, footnotes) plus the abs page and the arXiv API record. No secondary summary or aggregator page supplied any strategy rule or empirical figure.
- **Pre-write dedup (2026-09-22, ripgrep across all `*.md` in this repository):** `2507.09196`, exact title fragments (`Functionally Generated`), `Karimi`, `Salavati`, `diversity-weighted`, `entropy-weighted`, `functionally generated`, `relative arbitrage`, `Fernholz`, `stochastic portfolio theory` → **0 source-identity hits**. The only `Fernholz`/SPT matches are two records that cite SPT only as background for materially different mechanisms (`path-portfolio-optimization-signature-defect-lift-2026-09-02.md`: path-signature portfolio theory; `statistical-arbitrage-rank-space-cnn-transformer-hybrid-atlas-2026-09-02.md`: learned rank-space cross-sectional stat-arb). This record's mechanism — mechanical long-only rotation to a functional generator's target weights with an explicit stochastic-cost bound — is materially distinct in mechanism and signal construction. This repository has no `coverage_manifest`.
- Near-neighbor scans this round that were **already present** and therefore not written: nuclear/energy short-put VRP (`nuclear-energy-equity-options-short-put-variance-risk-premium-2026-09-02.md`), simple stock/bond/gold volatility control (`simple-dynamic-stock-bond-gold-markowitz-volatility-control-2026-09-11.md`, arXiv:2609.07946), Alpha191 cross-market DS-LASSO (`cross-market-alpha191-short-term-trading-factors-double-selection-lasso-2026-09-03.md`), agentic nowcasting (`agentic-ai-nowcasting-stock-returns-llm-web-search-2026-09-04.md`), BTQ (`beta-times-quantity-noise-trader-flow-factor-pricing-2026-09-07.md`), GoAnt, STRATA, centering/RevIN, crypto anomaly interactions, 0DTE VRP learning-to-rank — all matched by exact source identity.

## Economic mechanism

### Source-reported

The paper argues that classical Stochastic Portfolio Theory (SPT) extracts **structural alpha from pathwise market features** — specifically market diversity and capitalization-distribution curvature — via Fernholz's master formula, which decomposes log-relative wealth of a functionally generated portfolio (FGP) into (i) a local growth term driven by the chosen generator `G` and (ii) a non-negative drift proportional to the market's excess-growth rate `γ*`. Prior empirical work the paper cites validated p-variation, diversity- and entropy-weighted FGPs, but assumed frictionless trading. The paper's stated contribution is extending SPT to a continuous-time market with **proportional, stochastic transaction costs**, deriving closed-form lower bounds on cost-adjusted relative wealth (sufficient conditions for relative arbitrage to survive random costs), and showing empirically that diversity- and entropy-weighted FGPs still beat a value-weighted benchmark after cost deduction on 1994–2024 CRSP small caps. The paper explicitly notes higher turnover amplifies drawdowns during liquidity events (1998 LTCM, 2008 GFC, 2020 Covid), in line with its cost-adjusted master inequality.

### Research interpretation

Falsifiable mechanism statement: **cross-sectional capitalization dispersion is a persistent, partially mean-reverting feature of equity markets; a mechanical portfolio that over-weights mid-small names relative to the market's own concentration harvests the resulting excess-growth drift as long-only relative outperformance**, provided (a) Fernholz diversity stays elevated and (b) turnover costs (modeled as stochastic half-spreads) do not exceed the drift. Component roles:

```text
Mechanism / drift source: market excess-growth (Fernholz diversity) via functional generator
Signal & sizing: entropy generator G(mu)=prod(mu_i^mu_i); diversity weights with exponent p=0.7
Execution / cost control: monthly rebalance, single end-of-day trade, proportional half-spread cost
No separate timing filter, stop, or regime gate exists in the source
```

This is a **cost-adjusted portfolio-construction hypothesis, not a return-forecast hypothesis**: the source claims relative (not absolute) performance, and the edge is claimed to be erosion-resistant rather than eliminated by costs. Whether the drift source is behavioral (under-diversification / non-indexed small-cap ownership), structural (slow capital reallocation), or a survivorship/selection artifact is **not identified by the source** → identification of the causal channel is `data gap`.

## Signal

All rules below are source-reported unless marked `research-proposed`.

- **Formation timestamp:** at the **first trading day of every month**, compute (i) the value-weighted (VW) market benchmark, (ii) the entropy-weighted FGP target weights, (iii) the diversity-weighted FGP target weights (Section 5, "Portfolio construction"). Whether weights use that day's close or the prior close is `not stated in source`. Timezone/calendar: US equity regular session; intraday NBBO quotes are daily-frequency matched to CRSP permnos.
- **Lookback:** the FGP target weights are functions of the **current capitalization vector only** (no multi-day return lookback): entropy generator `G(μ)=∏ᵢ μᵢ^μᵢ`; diversity weights for `p ∈ (0,1)` with `p = 0.7` fixed (Section 3.1 / Section 5). Warm-up: `not stated in source`. Endpoints: not a windowed statistic.
- **Long entry / sizing:** hold the generator's target weights, long-only, fully invested (weights normalized over the 1,000-name cross-section; the paper's construction implies investable fraction `not explicitly stated` → `underspecified` for any cash convention).
- **Short entry:** none. The strategy is long-only; no short leg, hedge, or leverage appears anywhere in Section 5.
- **Execution:** target weights are implemented via a **single end-of-day trade** on the rebalance day; proportional cost `κᵢ,ₜ = ½·(ask−bid)/mid` is charged on absolute dollar turnover per stock.
- **Exit / holding period:** continuous monthly holding; positions are re-targeted monthly, so effective holding period = 1 month per rebalance cycle. No stop-loss, take-profit, or time exit exists in the source.
- **Re-entry / overlap:** N/A (always invested).
- **Parameters:** `p = 0.7` for the diversity generator — the paper does not report a tuning procedure or sensitivity grid for `p` → fixed-value provenance `underspecified` (treat as **source-fixed, tuning history not stated**). Universe size 1,000; spread filter `>500 bps` and zero-spread exclusion; rebalance mesh = monthly (theory section derives a mesh constraint `Δ̂` but the empirical mesh is simply monthly).
- **Reproducibility judgment:** the weight formulas, universe, cadence, and cost formula are reconstructible; the execution-price convention, cash rule, `p`-selection history, and warm-up are **not** → the signal is **partially reproducible, explicitly underspecified** in those fields rather than fully specified.

## Required data

All fields below are source-reported except where marked.

- **Instrument:** US common equities, CRSP share codes 10 and 11 (ordinary common shares), dividends reinvested; delisted shares replaced by the next-smallest stock to keep the cross-section at 1,000.
- **Universe:** the **one thousand smallest** US common stocks listed on NYSE/AMEX/NASDAQ, 2 Jan 1994 – 31 Dec 2024 (7,541 trading days). Inclusion/exclusion: panel filtered for zero spreads, spreads `> 500 bps`, and days with missing quotes, "leaving a balanced sample of **981 permnos**." Whether "balanced" means quote coverage across the full 31-year span or per-day eligibility is `underspecified` — and it materially interacts with survivorship (see Limitations).
- **Venue / data vendor:** CRSP daily database (prices, shares, share codes, delisting) + **TAQ daily NBBO bid/ask quotes** matched to CRSP permnos; mid-price `= ½(bid+ask)`.
- **Market type:** cash equities (no futures/perps/options/funding involved).
- **Timeframe:** daily data, **monthly** rebalance, single end-of-day trade.
- **Fields used:** market capitalization (for weights), bid, ask, shares outstanding (implied), delisting flags, dividends.
- **Point-in-time:** capitalization vector at rebalance date; NBBO quotes same-day. Publication-lag issues do not apply to price data; index-membership look-ahead is N/A (universe is bottom-size, not an index).
- **Timestamp / timezone:** US equity session; specific clock/precision `not stated in source` → `data gap`.
- **Missing data:** zero/extreme-spread and missing-quote days excluded; delisted names replaced by next-smallest. Imputation: none stated.
- **Funding/fee/spread needs:** spread is **observed** (NBBO half-spread) and charged; maker/taker fees, commissions, borrow, financing: **not modeled and not mentioned in the backtest** → `not stated in source`. Market impact: **explicitly excluded** — quadratic impact is listed in Section 6 as *future research*, so the backtest is spread-only.

## Execution assumptions

- **Source assumptions:** monthly single end-of-day trade; proportional cost = per-stock daily half-spread applied to absolute dollar turnover; dividends reinvested; long-only; no leverage, no shorting, no borrow, no latency model, no partial-fill/failure handling. Fill price for the trade itself (close vs mid vs next open) is `not stated in source` → `underspecified`.
- **Costs covered vs omitted (read from Sections 2, 5, 6, not inferred from the abstract):** spread **modeled**; slippage beyond half-spread, market impact, commissions/fees, borrow, latency: **not stated in source** (impact explicitly deferred to future work). Therefore all "net" figures are **net of proportional half-spread only** — they are not fully-loaded net-of-everything figures.
- **Scout assumptions (label: research-proposed):** any replication should charge an additional flat fee grid (e.g. 0/5/10/20 bps one-way) and a square-root participation-impact term on top of the source's half-spread, execute at next-bar open to remove fill ambiguity, and treat capacity as bounded by bottom-decile small-cap dollar volume. None of these appear in the source.

## Evidence

### Source-reported

All figures below are from `arXiv:2507.09196v1`, Section 5, Tables 3–4 and Figures 5–6, sample Jan 1994 – Dec 2024, CRSP 1,000-smallest universe, **net = after proportional half-spread cost only**; third-party result, not reproduced by us.

- **Table 3 (Cost-adjusted performance, Jan 1994–Dec 2024):** Market (VW) gross CAGR 7.1%, net CAGR 7.1%, avg. turnover 0.4%/mo, max DD −57%; **Entropy FGP** gross 11.0%, net **10.0%**, turnover 3.7%/mo, max DD **−63%**; **Diversity (p=0.7)** gross 12.2%, net **10.7%**, turnover 4.1%/mo, max DD **−65%**.
- **Abstract headline:** diversity- and entropy-weighted portfolios beat the VW benchmark by **3.6** and **2.9** percentage points annually, respectively, after cost deduction (equals Table 3 net CAGR gaps: 10.7−7.1=3.6; 10.0−7.1=2.9).
- **Table 4 (sub-period net outperformance vs VW, %/yr):** Entropy `+2.7 / +3.4 / +2.9 / +1.1`; Diversity(p=0.7) `+3.1 / +4.6 / +3.2 / +0.6` for `1994–1999 / 2000–2009 / 2010–2019 / 2020–2024`.
- **Section 5.1 footnote:** annual cost burden averages **97 bps/yr** (entropy) and **150 bps/yr** (diversity).
- **Section 5.3 / Figures 5–6:** diversity FGP cumulative net wealth ends **+220% above VW**; monthly turnover stable at **30–45 %/yr** while spreads spike in crises.
- **Section 5.4 take-aways:** "**280–360 bp** net edge" over three decades; average annual cost ≈ **25% of the gross excess-growth rate**; edge largest 2000–2009 (elevated dispersion) and decays post-2020.
- **Section 4 (simulation, not market data):** 5,000 Monte Carlo paths, 50-stock Itô market, T=1,000 trading days, DWP p=0.7, stochastic price-correlated cost process — validates `O(√T)` cost growth, **not** a market backtest.
- **Statistical inference:** no t-statistics, confidence intervals, significance tests, or Sharpe ratios are reported for Tables 3–4 → `not stated in source`.

### Independently reproduced

Not independently reproduced.

### Negative evidence

Source-acknowledged (all from v1):

- **Drawdowns are worse than the passive benchmark:** max DD −63%/−65% for the two FGPs vs −57% for VW (Table 3) — the strategy does not derisk; higher turnover amplifies losses in 1998/2008/2020 liquidity events (Section 5.1).
- **Edge is decaying in the most recent regime:** 2020–2024 net excess falls to **+1.1%** (entropy) and **+0.6%** (diversity) — the source attributes this to widening spreads and concentration in a few small-cap "winners" diluting `γ*` (Section 5.2). A regime where market concentration is high structurally weakens the stated mechanism.
- **Cost drag is material:** ~25% of gross excess-growth is consumed by costs; the diversity FGP pays 150 bps/yr before earning its edge (Section 5.1 footnote, 5.4).
- **Single-model, single-universe, single-cost-model evidence:** one 31-year US small-cap sample, one proportional-cost specification, no fee/impact/borrow model, no significance testing, no out-of-sample or walk-forward split, `p = 0.7` tuning history unstated.
- No independent replication attempts or contrary external studies were found in this round's sources; absence is not evidence of no negative result.

## Falsification plan

Items are tests we would run; **thresholds not given by the source are labeled research-defined falsification thresholds**.

1. **Spread-only → fully-loaded cost audit (research-proposed):** re-run the net backtest adding flat fee grids of 5/10/20 bps one-way plus a square-root impact term sized on bottom-decile dollar volume. **Fail rule (research-defined):** diversity FGP full-sample net excess vs VW `< 100 bp/yr` under the 10 bps + impact spec → mechanism not tradable as stated; action: do not advance to implementation.
2. **Survivorship / panel-construction audit (research-proposed):** rebuild the universe with per-day eligibility (no balanced-panel restriction) and CRSP delisting returns applied before replacement. **Fail rule (research-defined):** full-sample net edge drops `> 50%` vs the paper's 3.6 pp → original result treated as panel artifact; action: reject.
3. **Placebo / shuffled-weight test (research-proposed):** apply the same generator to a cross-section with permuted capitalization labels each month (preserves turnover, destroys the diversity drift link). **Fail rule (research-defined):** placebo net excess within `±100 bp/yr` of the real strategy → claimed excess-growth channel falsified (edge would be generic small-cap tilt, not the generator); action: reclassify as unnamed small-cap exposure and reject the mechanism.
4. **Mesh sensitivity (theory-linked):** the cost-adjusted master inequality predicts a too-fine rebalancing mesh erodes the bound. Run monthly vs weekly vs quarterly. **Fail rule (research-defined):** if finer meshes *systematically improve* net results, the paper's cost-scaling story is contradicted; action: revisit mechanism.
5. **Post-sample out-of-sample extension (research-proposed):** extend CRSP/TAQ through 2025–2026. **Fail rule (research-defined):** 24-month rolling net excess `≤ 0` → treat post-2020 decay as regime death; action: reject for adoption consideration.
6. **Regime breakdown:** recompute Table 4-style sub-periods conditioned on market-concentration measures (top-10 market-weight share). **Fail rule (research-defined):** net edge `≤ 0` in every high-concentration sub-period → mechanism is regime-conditional; any forward use requires a pre-declared concentration filter (`research-proposed` if built).
7. **Benchmark robustness:** compare against a small-cap value-weighted index of the same universe (and equal-weight as a control). **Fail rule (research-defined):** edge vs VW disappears once controlling for size-momentum or illiquidity factors in a spanning regression (`|t| < 2`) → mechanism is a priced-factor loading, not structural alpha; action: reclassify.
8. **Data/version pinning:** any replication must pin CRSP/TAQ vintage; failure to reproduce Table 3 within `±50 bp/yr` (research-defined) on the same vintage → record marked non-reproducible.

## Crypto portability

**`unproven`.**

The source's empirical evidence is exclusively US small-cap cash equities; it contains **no crypto experiment** (it cites, but does not itself perform, prior frictionless FGP work said to include cryptocurrency markets). Porting risks:

- **No month-end EOD session convention:** crypto trades 24/7; "first trading day of the month, single end-of-day trade" must be re-defined (`research-proposed`: UTC month boundary on a named venue) — candle boundaries and venue clocks differ.
- **Universe analog is hostile:** the "1,000 smallest liquid names" analog in crypto is the long-tail altcoin cross-section, where spreads routinely exceed the paper's 500 bps filter, delistings/rugs are frequent, and the balanced-panel rule would select survivors.
- **No consolidated NBBO:** venue fragmentation means there is no single mid-price; half-spread must be measured per venue, and cross-venue arbitrage bounds differ.
- **Spot vs perpetual:** a spot-only rotation has no funding, but implementing on perps introduces funding payments and liquidation/ADL mechanics absent from the source; mark/index basis and contract specification would change the cost term.
- **Mechanism precondition may not hold:** the edge is claimed to be largest when capitalization dispersion (Fernholz diversity) is high and to decay under concentration — crypto market concentration in BTC/ETH is high and dynamic, so the drift source is unverified there.
- **Custody/withdrawal and venue risk** are additional frictions with no counterpart in the CRSP/TAQ setup.

Crypto portability is not authorization to trade.

## Limitations

- `underspecified`: execution fill price for the monthly trade; cash/investable-weight convention; warm-up; `p = 0.7` selection history; timezone/clock precision; meaning of "balanced sample of 981 permnos" (full-span vs per-day).
- `data gap`: causal channel linking capitalization concentration to subsequent relative returns is asserted via Fernholz drift, not identified econometrically; no significance tests or confidence intervals anywhere in the empirical section.
- `not stated in source`: commissions, fees, slippage beyond half-spread, market impact (explicitly future work), borrow/shorting (N/A), latency, capacity/liquidity limits.
- Peer-review status `not stated in source` (preprint v1, no journal-ref); single version, no revision history.
- Internal date line (`August 24, 2026`) conflicts with the v1 submission date — see Provenance; not repaired here.
- Single universe (US small-cap bottom-decile), single 31-year window, no out-of-sample split, no parameter sensitivity for `p`.
- Theoretical `O(√T)` cost bound is asymptotic and sufficient-condition only; it does not guarantee the empirical edge persists.
- `not independently reproduced`; source-reported figures remain third-party claims.
- Provenance discrepancy between the v1 HTML date line and the arXiv submission history is preserved rather than silently resolved.

## Implementation status

`implementation_status: not-implemented`. Nothing from this record has been implemented in our research stack: no portfolio-construction code, no CRSP/TAQ pipeline, no backtest, no Qlib run, no prototype. The theory (cost-adjusted master inequality) and the 1994–2024 CRSP backtest exist only inside the source paper. This record does not modify any engine and does not authorize Paper, Testnet, or Live execution.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this record in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet, or live trading. Any adoption or implementation decision is a separate, explicit, reviewed step based on this record plus current sources.

## Related Wiki records

No stable Hermes Wiki Brain page was identified for this mechanism, and none is fabricated here. Adjacent captures in **this repository** (provenance pointers only, not Wiki links, not dedup substitutes):

- `path-portfolio-optimization-signature-defect-lift-2026-09-02.md` — cites Fernholz SPT as background but studies path-signature portfolio lifts (different mechanism).
- `statistical-arbitrage-rank-space-cnn-transformer-hybrid-atlas-2026-09-02.md` — uses SPT rank-stationarity as motivation for a learned cross-sectional stat-arb model (different signal construction).
- `entropic-value-at-risk-parity-tempered-stable-returns-2026-09-11.md` / `entropic-value-at-risk-tempered-stable-levy-portfolio-optimization-2026-09-02.md` — "entropic" here is Entropic VaR risk budgeting, unrelated to the entropy generator in this record.

Future Scout runs should re-check these adjacencies before materially updating this record rather than creating a duplicate.

## Sources

1. Nader Karimi, Erfan Salavati, *"Functionally Generated Portfolios Under Stochastic Transaction Costs: Theory and Empirical Evidence"*, `arXiv:2507.09196v1 [q-fin.PM]`, submitted 12 Jul 2025; Comments: 15 pages, 6 figures; license CC Zero.
   - Abstract: https://arxiv.org/abs/2507.09196
   - Full text HTML v1 (all tables/sections extracted from here): https://arxiv.org/html/2507.09196v1
   - PDF v1: https://arxiv.org/pdf/2507.09196v1
   - DOI: https://doi.org/10.48550/arXiv.2507.09196
2. arXiv API metadata record for `2507.09196` (authors, version timestamps, categories, absence of journal-ref/DOI), queried via `https://export.arxiv.org/api/query?id_list=2507.09196` on 2026-09-22 — used only for bibliographic verification, no empirical claim taken from it.

All performance figures in this record trace to Source 1, Section 5, Tables 3–4 / Figures 5–6 / Section 5.1 footnote, as noted inline. Equities (US small-cap cash equities) sample — **not** crypto evidence.
