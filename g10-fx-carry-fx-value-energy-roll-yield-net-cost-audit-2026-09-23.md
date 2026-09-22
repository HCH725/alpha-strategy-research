---
schema: strategy-research-record-v1
title: "G10 FX Carry / FX Value and Energy Futures Roll-Yield Audit: Net-of-Cost Premia, Decay and Roll-Construction Fragility (Alpha Research Paper 6)"
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - fx
  - carry
  - fx-value
  - commodity
  - term-structure
  - roll-yield
  - basis-momentum
  - cross-sectional
  - monthly-rebalance
status: research-only
confidence: medium
source_as_of: 2026-06-17
sources:
  - "Bryan Vine, 'FX Carry & Commodity Roll Yield — and What Six Papers of Honest Search Found', Alpha Research Paper 6, byline June 17, 2026, https://bryanvine.github.io/alpha-research/paper6.html"
  - "https://github.com/bryanvine/alpha-research — file docs/paper6.html at full commit SHA c823c2d09acbb188728b5aadf725bf765912d999 (2026-06-17T01:03:35Z); byte-identical to repo head 17b8b5e1c79af194f733544517d82e3cf12c2259 (2026-08-23); SHA-256 98f3edbddb15afe073877305004e9642e394d9d899edb6d9bc1e342782bcd1eb, 19102 bytes (verified 2026-09-23)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# G10 FX Carry / FX Value and Energy Futures Roll-Yield Audit: Net-of-Cost Premia, Decay and Roll-Construction Fragility (Alpha Research Paper 6)

## Provenance

- **Source:** Bryan Vine, *"FX Carry & Commodity Roll Yield — and What Six Papers of Honest Search Found"* — Alpha Research, Paper 6 (self-described "finale" of a six-paper program).
- **Author list (complete, as printed on the source):** Bryan Vine (sole author; page byline `Bryan Vine · June 17, 2026`).
- **Published URL (stable):** https://bryanvine.github.io/alpha-research/paper6.html
- **Repository URL:** https://github.com/bryanvine/alpha-research
- **Immutable provenance:** file path `docs/paper6.html` at **full commit SHA `c823c2d09acbb188728b5aadf725bf765912d999`** (2026-06-17T01:03:35Z, commit message *"Paper 6 (finale): FX Carry & Commodity Roll Yield + program capstone"*) — the commit that introduced the paper.
- **Primary-source checksum (performed 2026-09-23):** three copies were fetched and hashed — (a) the live GitHub Pages file, (b) `docs/paper6.html` at creation commit `c823c2d…`, (c) `docs/paper6.html` at repository head `17b8b5e1c79af194f733544517d82e3cf12c2259` (head as of 2026-09-23, last commit 2026-08-23). All three are **byte-identical**: SHA-256 `98f3edbddb15afe073877305004e9642e394d9d899edb6d9bc1e342782bcd1eb`, 19,102 bytes. The published page therefore equals the pinned artifact.
- **Sections read directly from that pinned HTML full text:** header/byline; Abstract; §1 Introduction (pre-registered H1–H4); §2 *Data & leakage control*; §3 *Method*; §4 *Experiments & results* (§4.1–§4.3); §5 *What six papers of honest search found*; §6 *Limitations & future work*; References.
- **Version/date:** single public version, byline **June 17, 2026**; no version history, DOI, or revision statement on the page → versioning beyond the commit chain is `not stated in source`.
- **Publication status:** self-published research-series page hosted on GitHub Pages plus an open-source GitHub repository; **no journal, no peer-review statement, no DOI** → `not stated in source`.
- **Supporting code paths present at pinned head `17b8b5e…`:** `scripts/45_paper6_figures.py` (naming explicitly ties it to paper 6 figures), `scripts/10_fetch_fx_commodity.py`, `scripts/20_fetch_eia.py`, `scripts/21_macro_carry_core.py`, `configs/data_sources.yaml`. The paper links to the repository root ("code & full research log") but **does not map paper sections/numbers to specific files** → section-to-script mapping `underspecified`.
- **Repository-wide deduplication audit (2026-09-23, whole repository, not `git log`):** ripgrep across **all 361 `*.md` records** for `Alpha Research Paper 6`, `paper6`, `FX Carry & Commodity`, `macro_carry`, `energy roll`, `10_fetch_fx_commodity`, `21_macro_carry`, `G10` produced **zero records for this source identity**. Four existing records cite the same *author/series* but different papers with non-overlapping mechanisms: Paper 1 (crypto/equity volatility risk premium), Paper 2 (crypto perpetual funding carry), Paper 3 (crypto statistical arbitrage), Paper 8 (on-chain liquidity premia). No existing record covers G10 FX carry, FX value (REER), or energy-futures roll yield as a strategy source. Adjacent curve/basis records use different sources and different markets (see *Related Wiki records*).
- **Sample period, universe, cost treatment and every performance figure below were read from the primary source's §2–§4 and §6 (Methods / Data / Results / Limitations), not from any summary.**

## Economic mechanism

### Source-reported

Vine frames FX carry and commodity roll yield as "the most-documented anomalies in finance" and tests them on newly-sourced free data, with two named failure modes: **crash risk** (carry's fat left tail) and **post-financialization decay**. The paper pre-registers four hypotheses (§1) and reports their outcomes:

- **H1:** diversified FX carry nets ~0.2–0.4 Sharpe with negative skew and has decayed post-2008 — *Confirmed*.
- **H2:** FX value (real-exchange-rate reversion) is comparable and roughly uncorrelated with carry — *Confirmed* (0.46, steadier, stronger post-2008).
- **H3:** commodity roll yield / basis-momentum survive in the curve — *Refuted for energy* (≈0 net).
- **H4:** the premia decayed with financialization (post-2010) — *Confirmed in direction*.

Mechanism statements in the source: carry earns the **yield differential** plus currency appreciation (§3), but pays with the carry-crash left tail (§4.1); FX value is **real-exchange-rate reversion** (§2–§3); energy **roll yield** is the curve slope `log(C1/C2)` (backwardation vs contango) and **basis-momentum** is the front-minus-back 12-month return difference (§3). A construction channel is elevated to a result: a futures "return" naively computed from a spliced front-contract series `log(C1_t/C1_{t-1})` "injects the monthly roll with the wrong sign" and produced a spurious Sharpe of −1.57, whereas the correct roll-adjusted return tracks the held contract, `log(C1_t/C2_{t-1})` (§2, §4.2) — i.e. **"the roll method *is* the signal."**

### Research interpretation

Falsifiable normalization of the four components and their roles (component roles, not an assumption that each contributes alpha):

```text
FX carry (primary):  cross-sectional financing premium — long high 3-month rate
                     differential vs USD, short low; dollar-neutral, monthly.
                     Channel: compensation for providing funding + unhedged
                     crash-exposed FX exposure. Expected: positive mean,
                     negative skew, decaying mean.
FX value (diversifier): REER-deviation mean reversion — valuation/purchasing-power
                     correction, expected to be weakly correlated with carry.
Energy roll yield (tested, refuted): hedging-pressure / curve-slope premium;
                     expected to die after financialization.
Basis momentum (tested, refuted): term-structure slope-change signal;
                     expected to survive, does not, net of costs, in 4 curves.
```

The honest reading of §4.2–§4.3 is that **two of four tested signals are dead net of costs in this sample**, and the two survivors are *modest risk premia* (0.44 and 0.46 full-sample net Sharpe), not standalone edges — "diversified-book ingredients at small weight" (§4.1, §5).

## Signal

All four signals are monthly, cross-sectional, long-short, and formed on month-*t* data **lagged one month** before being applied to month *t+1* return (§2). The paper's only stated timing convention is that one-month lag.

**S1 — FX carry (§3)**
- **Formation timestamp:** monthly rate differential vs USD, observed in month *t*, shifted by the source's one-month lag; applied to the next month's return (§2–§3). Exact calendar/observation convention and timezone → `not stated in source`.
- **Lookback:** the 3-month rate differential itself (§2: "G10 spot and 3-month rate differentials vs USD"); averaging/endpoint convention for the differential → `underspecified`.
- **Long entry:** the **top three** currencies by rate differential. **Short entry:** the **bottom three** (§3).
- **Direction/netting:** dollar-neutral (§3).
- **Rebalance / holding:** monthly (§3); positions reset at each monthly rebalance. Exit rule other than rebalance (stop, partial de-risk, drawdown cut) → `not stated in source`.
- **Sizing:** per-name weights within the top-3/bottom-3 (equal weight vs any other rule) → `not stated in source`.
- **Parameters:** group size 3 (source-reported, fixed); sample 1971–2026 (§2).

**S2 — FX value (§3)**
- **Signal:** sort currencies on **real effective exchange rate (REER) deviation** (BIS REER, §2), i.e. real-exchange-rate reversion.
- **Formation/lag:** same one-month lag (§2).
- **Underspecified:** REER reference index, lookback/horizon of the deviation, deviation threshold, number of long/short legs, weighting, rebalance cadence and net cost for this leg are **not stated in source**. S2 is therefore **not independently reconstructible** from the paper alone; the source only reports its aggregate Sharpe (0.46 full sample, 0.61 post-2008).

**S3 — Energy roll-yield carry (§2–§3)**
- **Signal:** sort the four energy futures on `log(C1/C2)` (backwardation vs contango) at the lagged month.
- **Execution reference:** long-short **on the roll-adjusted front return** `log(C1_t/C2_{t-1})` (§2); cost **net 10 bp** (§3).
- **Rebalance:** monthly (signals lagged one month, §2). Sizing, tie handling, leg counts → `not stated in source`.

**S4 — Energy basis-momentum (§3)**
- **Signal:** front-minus-back **12-month** return (12-month lookback, source-reported); same long-short execution on the roll-adjusted front return, **net 10 bp**.
- All other operational detail → `not stated in source`.

**Shared construction rule (§2, source-reported):** never use the spliced front series return `log(C1_t/C1_{t-1})`; use `log(C1_t/C2_{t-1})` (the second-nearest contract last month is the front this month). Source calls this a "second-to-first approximation" and notes a true contract-level roll calendar would refine it (§6).

**Stop / take-profit / liquidation logic:** none stated for any of the four signals → `not stated in source` (no stop, no drawdown control, no leverage rule appears in the source; do not read that as "modeled").

## Required data

- **S1/S2 universe:** G10 currencies vs USD (§2). **The exact G10 membership used is not enumerated** → `underspecified`.
- **FX fields:** G10 spot rates and 3-month interest-rate differentials vs USD (**FRED**), real effective exchange rates (**BIS**), CFTC positioning — **monthly, 1971–2026** (§2). CFTC positioning is listed as sourced data but its role in any of S1–S4 is not described → `underspecified`.
- **S3/S4 universe:** four energy futures curves — **WTI crude, Henry Hub natural gas, NY Harbor heating oil, RBOB gasoline** (§2).
- **Commodity fields:** **EIA daily settlement prices for the front-through-fourth contract**, 2004–2024 (§2) — a genuine multi-contract curve rather than a spliced continuous series.
- **Venue / market type:** OTC FX (spot + rate differential proxy) and NYMEX/energy futures settlements via EIA; specific execution venue, contract month selection, and roll calendar → `not stated in source`.
- **Timeframe:** monthly signals/returns for S1/S2; daily settlement inputs aggregated to monthly lagged signals for S3/S4 (§2).
- **Point-in-time / availability:** signals lagged one month (§2). Publication lags and revision handling for FRED/BIS/EIA series, and any vintage control → `data gap`.
- **Timestamp / timezone / alignment:** `not stated in source`.
- **Missing-data handling:** `not stated in source` (no null/stale/suspension policy given).
- **Cost data:** flat bp assumptions only (below); observed bid-ask, roll costs, forward points, borrow → not supplied (`not stated in source`).

## Execution assumptions

- **Signal-to-order timing:** one-month lag between observation and application (§2) — the only explicit timing assumption.
- **Costs (source-stated):** S1 FX carry **net 5 bp** per rebalance; S3/S4 commodity **net 10 bp** per rebalance (§3). S2 FX value cost basis → `not stated in source`.
- **Gross vs net:** all reported Sharpes are described as **net** of those flat bp assumptions; gross-of-cost figures → `not stated in source`.
- **Order type, fill model, fills-at-open vs settlement, latency, partial fills, market impact, participation/capacity, borrow/short availability, leverage/margin, liquidation** → `not stated in source`. The paper reports no fill model at all; per contract this is recorded as *not stated*, **not** as "assumed zero".
- **Carry proxy (source-stated limitation, §6):** carry is proxied by the **rate differential**, not traded forward points, because free forward data are scarce and covered-interest parity broke down after 2008. EM currencies are excluded (G10 only) — "the higher-carry, higher-crash EM currencies would sharpen both the premium and its tail" (§6).
- **Roll implementation (source-stated, §2/§6):** second-to-first approximation `log(C1_t/C2_{t-1})`; a true contract-level roll calendar would refine it.
- **Program-wide cost language (§5):** the source's own general lesson names "half-spreads, turnover, queue position, the roll method, options execution" as decisive; for **this** paper only the flat 5/10 bp assumptions are specified → per-strategy impact/queue treatment `not stated in source`.

## Evidence

### Source-reported

All figures below are read directly from the pinned `docs/paper6.html` (SHA-256 `98f3edbd…c1eb`) and are **source-reported, not independently reproduced**. All are Sharpe ratios unless noted; market/universe as marked. The page reports **no t-statistics, p-values, confidence intervals, turnover, capacity, or maximum drawdown for any of S1–S4** → `data gap`.

- **§2 (construction result):** naive spliced front-contract return `log(C1_t/C1_{t-1})` produced a **spurious Sharpe of −1.57**; the roll-adjusted construction is the correct one. Reproduced by the author within the same study as a construction check (not our reproduction).
- **§4.1 — S1 FX carry, G10, 1971–2026 monthly, net 5 bp:**
  - Full-sample Sharpe **0.44**.
  - Sub-periods (Figure 1): **0.64** before 2008 → **0.09** (2008–15) → **0.22** "since" (the source prints "0.22 since" with **no endpoint year** → sub-period boundary `underspecified`).
  - Skew **−0.16** (negative, "the carry trade's signature").
- **§4.1 — S2 FX value, G10, net basis `not stated`:** full-sample Sharpe **0.46**, **positive** skew, **post-2008 Sharpe 0.61** (i.e. stronger after 2008).
- **§4.1 (benchmark comparison, third-party, source-reported):** both FX signals "sit at or below the **~0.41** a live multi-style fund delivers" — §3 names it as AQR's QSPIX live multi-style net Sharpe, used as a "realistic professional ceiling"; we did not open any AQR source → **benchmark claim attributed to Vine, unverified**.
- **§4.2 — S3 energy roll-yield carry, four energy curves, 2004–2024, net 10 bp:** Sharpe **−0.22** (does not clear zero); mildly positive pre-2010, negative post-2010 (Figure 2).
- **§4.2 — S4 energy basis-momentum, same universe/net:** Sharpe **−0.06**; same pre-2010 positive / post-2010 negative pattern (Figure 2).
- **§1 — pre-registered hypotheses:** H1 Confirmed; H2 Confirmed; H3 **Refuted** (energy); H4 Confirmed in direction.
- **§4.3 — six-program tally (Figure 3):** surviving edges (crypto trend, FX value, FX carry, liquidity provision, crypto funding carry, equity quality) cluster at net Sharpe **≈0.39–0.53**, "just above our **+0.3 floor**" (the +0.3 mean-reversion floor is defined in §3); the edges that die sit "at or well below zero". These are cross-paper aggregates reported by this source, not measurements from S1–S4 alone.
- **§5 — program summary (source-reported):** Paper 4 (factor zoo) "anomalies decay ~half post-publication; only low-turnover quality survives"; Paper 5 "no standalone microstructure alpha… but a real execution edge and a vol-conditional liquidity-provision premium".

### Independently reproduced

Not independently reproduced. No backtest was run by us; no Qlib, Paper, Testnet, or Live verification exists for this record.

### Negative evidence

- **H3 refuted by the source itself:** neither energy roll yield (−0.22) nor basis-momentum (−0.06) clears zero net of 10 bp in the four-curve energy cross-section (§4.2).
- **Carry decay and crash profile:** 0.64 pre-2008 → 0.09 (2008–15) → 0.22 "since", skew −0.16 (§4.1). The most recent sub-period boundary is not stated → decay magnitude into the present is `underspecified`.
- **Construction fragility as a live failure mode:** the same factor flips from a spurious −1.57 Sharpe to ≈0 purely from roll-handling (§2, §4.2) — a replication trap for anyone rebuilding it from a continuous-futures feed.
- **Financialization decay confirmed in direction** (H4, §1): both curve signals were mildly positive pre-2010 and negative after (§4.2).
- **Thin cross-section:** only four energy curves; EIA series end in 2024; metals/agriculture/softs (where basis-momentum is reported to survive in the literature) require a paid multi-contract feed and were not tested (§6).
- **Carry proxy weakness:** rate differential instead of traded forward points; CIP broke down post-2008; EM excluded (§6).
- **No significance apparatus for S1–S4:** no t-stats, CIs, deflated Sharpe, PBO, turnover or drawdown reported for these four signals (§4) → the 0.44/0.46 numbers cannot be distinguished from noise from the paper alone (`data gap`).
- **Source quality:** self-published, non-peer-reviewed, single-author research series whose own thesis is that most backtest alphas are artifacts (§5) — a credibility caution on both directions of its claims.
- **None of the above was independently reproduced.**

## Falsification plan

Thresholds below that are not in the source are explicitly labeled `research-defined` (acceptance/failure cutoffs chosen by this Scout) or `research-proposed` (operational choices the source does not specify).

1. **Independent rebuild of S1 (sample, data):** reconstruct G10 spot, 3-month rate differentials (FRED), BIS REER on a point-in-time monthly panel 1971–2026; run long top-3 / short bottom-3, dollar-neutral, one-month lag, 5 bp. **Failure rule** (`research-defined`): full-sample net Sharpe < **0.30** (the source's own +0.3 floor, §3), or post-2015 sub-period net Sharpe ≤ 0 → treat the carry claim as not surviving; action: mark hypothesis rejected in this repo, no downstream candidate entry.
2. **Cost sweep:** 0 / 5 / 10 / 20 bp per rebalance. **Failure rule** (`research-defined`): net Sharpe ≤ 0 at **10 bp** → effect is cost-fragile; escalate turnover estimate before any further use.
3. **Roll-construction placebo:** compute S3/S4 twice — spliced-front return vs roll-adjusted `log(C1_t/C2_{t-1})`. **Failure rule** (`research-defined`): if the naive construction again produces |Sharpe| ≥ 1.0 while the adjusted one does not, the pipeline's roll handling is wrong (or the effect is an artifact) → halt and audit; action: no result may be reported until the two constructions reconcile.
4. **Tail/skew check:** monthly-return skew of S1. **Failure rule** (`research-defined`): out-of-sample skew < **−0.5** with a left-tail contribution exceeding the source-reported −0.16 → the carry premium is dominated by crash months; action: reject as a standalone leg, allow only as a small diversified weight.
5. **Leave-one-currency-out jackknife** (`research-proposed`; the source names no currencies): drop each G10 member in turn. **Failure rule** (`research-defined`): sign of full-sample Sharpe flips under any single deletion → concentrated, not a cross-sectional premium.
6. **S2 reconstruction gate:** because REER-deviation details are `underspecified`, first declare the exact reference index, horizon, and leg construction *before* looking at results (`research-proposed`). **Failure rule** (`research-defined`): if the declared variant does not reproduce a net Sharpe within ±0.15 of the source's 0.46 on the same sample, treat 0.46 as unreproducible rather than retuning.
7. **S3/S4 confirmation beyond energy** (`research-proposed`): extend to metals/ag softs via a paid multi-contract curve feed and test the pre/post-2010 split with an interaction term. **Failure rule** (`research-defined`): post-2010 net Sharpe 95% CI containing 0 → confirm the source's own refutation of H3 and drop the curve signals.
8. **Regime/decade breakdown:** rolling 10-year net Sharpe for S1. **Failure rule** (`research-defined`): two or more consecutive decades ≤ 0 → decay thesis confirmed as fatal; action: reject.
9. **Competing-explanation control** (`research-proposed`): regress S1 returns on USD index and global risk-aversion proxies; **failure rule** (`research-defined`): |t| < 2.0 on the carry premium after those controls, or a placebo sort on a shuffled differential retaining |t| ≥ 2.0 in ≥10% of 1,000 draws → premium is not differential-driven; reject.
10. **Out-of-sample extension:** extend FX data past 2026 and EIA past 2024 as they publish; **failure rule** (`research-defined`): OOS net Sharpe ≤ 0 over ≥ 36 new monthly observations → reject.

## Crypto portability

**Unproven.** The source contains **no crypto evidence** for any of S1–S4 (its crypto findings come from separate papers in the same series). Nothing here may be cited as crypto validation.

- **Carry analogue:** perp funding is often called crypto "carry", but it is an exchange-determined periodic payment, not a rate differential against a funding currency; the same author's Paper 2 (already captured separately) is the crypto-side source. Any perp-funding port of S1 would be a `research-proposed` new hypothesis.
- **FX value analogue:** no REER exists for crypto assets; stablecoin-peg or BTC-dominance proxies would be `research-proposed` substitutes with different economics.
- **Curve analogue:** crypto has calendar futures on a handful of coins plus perpetual basis — a much thinner cross-section than four energy curves, with no official settlement/roll data equivalent to EIA; roll handling is venue-specific.
- **Structural gaps:** 24/7 sessions vs monthly FX/FUT settlement, venue fragmentation, no central REER/rate statistics, funding/borrow asymmetry on short legs, liquidation paths invisible to daily bars, and index/Mark price mechanics.
- Verdict: mechanism origin is traditional-asset research with zero crypto demonstration → `unproven`, and any crypto version is a ported hypothesis, not empirical crypto evidence.

## Limitations

- **Source-reported gaps:** G10 membership not enumerated (`underspecified`); REER-deviation construction for S2 `underspecified`; sub-period endpoint for "0.22 since" `underspecified`; S2 cost basis `not stated in source`; sizing/weighting for all legs `not stated in source`.
- **Execution/cost:** order type, fill model, slippage, spread, impact, latency, borrow, leverage, capacity all `not stated in source`; results are net only of flat 5/10 bp assumptions.
- **Statistical:** no t-stats, CIs, deflated Sharpe, PBO, turnover, or drawdown for S1–S4 → `data gap`; multiple-testing correction across the four signals not reported for this paper → `data gap`.
- **Data:** EIA panel ends 2024; carry proxied by rate differential rather than forward points; EM excluded; CFTC positioning sourced but unused/unexplained in S1–S4 (`underspecified`).
- **Sample/identification:** single 55-year FX sample with one regime shift (2008) and one hypothesized financialization shift (2010); four-commodity cross-section is thin; free-data constraint bounded the universe (§6).
- **Provenance:** self-published, non-peer-reviewed; all numbers `not independently reproduced`.
- **Scope:** this record captures a source-reported audit of four monthly cross-sectional signals; it is not a claim that any of them works.

## Implementation status

`implementation_status: not-implemented`. Nothing from this record has been implemented in our research stack: no backtest harness, no data pipeline, no strategy module, no Qlib full backtest, and no Paper/Testnet/Live stage. Only the research capture above exists.

## Adoption boundary

This record being present in this repository means only normalized research material in the public staging pool. It does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading.

`status: research-only` · `adoption: not-approved` · `approval_scope: research-only`.

## Related Wiki records

- **Wiki Brain search (read-only, 2026-09-23):** `kb_search` for "FX carry commodity roll yield energy futures term structure" returned only `quant/forecast-to-fill-gold-futures-friction-adjusted-kelly-alpha-2026-09-02` and `quant/commodity-futures-network-momentum-lead-lag-graph-learning-2026-09-02`; a second query for "Bryan Vine alpha research carry" was also run. **No Hermes Wiki Brain page exists for this source identity** (and this Scout does not write one). The two hits are different mechanisms (gold trend-momentum; commodity network momentum), listed only as future retrieval hooks.
- Adjacent records in this repository (different source identities, non-overlapping mechanisms):
  - `crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11` — same author/series, **Paper 2**: cross-sectional perpetual funding carry (crypto), not G10 FX carry.
  - `crypto-volatility-risk-premium-variance-swap-estimator-fragility-decay-2026-09-12` — Paper 1 (VRP); `crypto-statistical-arbitrage-pca-residual-cointegration-falsification-2026-09-12` — Paper 3 (stat-arb audit); `autonomous-llm-research-stablecoin-flow-carry-trend-death-2026-09-19` — Paper 8 (on-chain premia).
  - `crypto-futures-cross-sectional-basis-momentum-slope-2026-08-31` — Boons & Prado *Basis-Momentum* (JF 2019) ported to crypto futures; this record's S4 is the same-named signal but a **different source, different market (energy futures), and a refuted net result**.
  - `crypto-futures-term-structure-roll-yield-carry-2026-08-31` — crypto curve carry; here the analogous signal is energy-futures roll yield, refuted net.
  - `foreign-exchange-spatiotemporal-graph-statistical-arbitrage-2026-09-02`, `anchored-currency-arbitrage-qubo-gauge-fixed-annealing-2026-09-04` — FX-adjacent but different mechanisms (graph stat-arb; QUBO arbitrage construction).

## Sources

1. Bryan Vine. *"FX Carry & Commodity Roll Yield — and What Six Papers of Honest Search Found."* Alpha Research, Paper 6, byline June 17, 2026. https://bryanvine.github.io/alpha-research/paper6.html — read in full (Abstract, §1–§6, References) on 2026-09-23. Every quantitative claim in this record traces to §2, §3, §4.1, §4.2, §4.3 or §5 of that page.
2. Bryan Vine. `alpha-research` repository. https://github.com/bryanvine/alpha-research — file `docs/paper6.html` at full commit `c823c2d09acbb188728b5aadf725bf765912d999` (2026-06-17) and at head `17b8b5e1c79af194f733544517d82e3cf12c2259` (2026-08-23); both byte-identical to the published page (SHA-256 `98f3edbddb15afe073877305004e9642e394d9d899edb6d9bc1e342782bcd1eb`, 19102 bytes, verified 2026-09-23). Related paths at head: `scripts/45_paper6_figures.py`, `scripts/10_fetch_fx_commodity.py`, `scripts/20_fetch_eia.py`, `scripts/21_macro_carry_core.py`, `configs/data_sources.yaml`.
3. Third-party works **cited by** source 1 (listed for provenance only; **not opened, no claim taken from them**): Koijen, Moskowitz, Pedersen & Vrugt (2018) "Carry", *JFE* 127(2); Lustig, Roussanov & Verdelhan (2011) "Common Risk Factors in Currency Markets", *RFS* 24(11); Boons & Prado (2019) "Basis-Momentum", *JF* 74(1); Gorton & Rouwenhorst (2006) "Facts and Fantasies about Commodity Futures", *FAJ*; Asness, Moskowitz & Pedersen (2013) "Value and Momentum Everywhere", *JF* 68(3); AQR QSPIX live net Sharpe ~0.41 (attributed to source 1, unverified by us).
