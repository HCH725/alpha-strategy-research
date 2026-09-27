---
schema: strategy-research-record-v1
title: "Crypto Dated-Futures Basis ARP with Default-Aversion Rebalancing and One-Touch-Insured Near-Arbitrage (SSRN 7226353)"
created: 2026-09-27
updated: 2026-09-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - futures
  - basis-carry
  - convenience-yield
  - default-aversion
  - portfolio-insurance
  - one-touch-options
  - near-arbitrage
  - preprint
status: research-only
confidence: medium
source_as_of: 2026-08-03
sources:
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7226353"
  - "https://doi.org/10.2139/ssrn.7226353"
  - "SSRN Open PDF in Browser delivery link for abstract_id=7226353 (download.ssrn.com presigned object), pinned locally 2026-09-27"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Dated-Futures Basis ARP with Default-Aversion Rebalancing and One-Touch-Insured Near-Arbitrage (SSRN 7226353)

## Provenance

Page numbers in this record are physical pages of the pinned PDF (the PDF's own printed folio runs one lower from printed page 2 onward).

- **Primary source:** SSRN preprint, `abstract_id=7226353`, DOI [`10.2139/ssrn.7226353`](https://doi.org/10.2139/ssrn.7226353). Landing page: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7226353>.
- **Exact title (PDF p.1 and landing page, identical):** `Crypto Futures Risk Mitigation: Dynamic Rebalancing, Carry and ARP Strategies`.
- **Authors, recorded exactly as each surface prints them; the two surfaces disagree on order and on one affiliation, and are not reconciled here.**
  - PDF p.1 title block, in printed order: **Ifigenia Georgiou\*** (`*Corresponding author`, `Associate Professor, Department of Accounting, Economics and Finance, School of Business, University of Nicosia, 46 Makedonitissas Avenue, CY-2417, Nicosia, Cyprus`, `georgiou.i@unic.ac.cy`); **Marc Eigenheer** (`DM Innovations GmbH, Tannbergstrasse 4, 6214 Schenkon, Switzerland`, `me@dm-innovations.ch`); **Svetlana Sapuric** (`Associate Professor`, same department, `sapuric.s@unic.ac.cy`).
  - Landing-page `Suggested Citation` and author headings, in printed order: **Georgiou, Ifigenia** (`University of Nicosia`), **Sapuric, Svetlana** (`University of Nicosia, Department Accounting, Economics and Finance`), **Eigenheer, Marc** (`University of Nicosia`).
  - Two discrepancies: the author order differs (PDF `Georgiou, Eigenheer, Sapuric` vs landing `Georgiou, Sapuric, Eigenheer`), and Eigenheer's affiliation differs (`DM Innovations GmbH` in the PDF vs `University of Nicosia` on the landing page).
  - PDF metadata `/Author` is `Svetlana Sapuric` alone.
- **Dates (both printed; not reconciled).** Landing page: `Posted: 3 Aug 2026`, `24 Pages`. PDF metadata: `/CreationDate D:20260516100400Z` (2026-05-16), `/ModDate D:20260803154225+00'00'` (2026-08-03), `/Producer Aspose.Pdf for Java 17.12`. The paper prints no `Date Written` field.
- **Publication / peer-review status.** Every page of the PDF carries the footer `This preprint research paper has not been peer reviewed.` plus `Preprint not peer reviewed`; the landing page banner states `This is a preprint article, it offers immediate access but has not been peer reviewed.` No journal, volume, issue or conference appears on the landing page. Status: **preprint, not peer reviewed**.
- **Rights (recorded, not interpreted).** The landing page prints `The copyright holder has granted SSRN a license` and `All rights reserved. No reuse allowed without permission.` This record therefore normalises only the source's own claims, printed values, section references and table identifiers, and does not reproduce the source's prose at length.
- **Reference / citation metadata discrepancy (recorded, not repaired).** The landing page prints `0 References` (with an unfetched `Fetch References` button) and `0 Citations`, while a separate `Paper statistics` block on the same page links `49 References`; the PDF's own reference list (pp.19-22) contains **49** entries counted entry-by-entry.
- **Landing-page statistics at read time (2026-09-27):** 125 downloads, 213 abstract views, 0 citations.
- **Pinned primary source.** PDF obtained 2026-09-27 through the SSRN `Open PDF in Browser` delivery link (a `download.ssrn.com` presigned object), **528,297 bytes, 24 pages**, SHA-256 `614218f8bfa1a278a32b80b1197c45c304ea5ed6ba1e61e360da61d8b1437176`. Text was extracted page by page with `pypdf` 6.16.2 (character counts per page: 774, 225, 2030, 4389, 3933, 3659, 3778, 2992, 3617, 2659, 3047, 2438, 2397, 2922, 2990, 2475, 3600, 3150, 3020, 2467, 2473, 2463, 374, 420); all 24 pages carry a text layer and every page was read in full before this record was written. Raster figure pixels on pp.23-24 were not inspected, so any claim about plotted figure content is `data gap`.
- **Sample window - four mutually inconsistent statements in one source (all recorded, none reconciled).** Abstract p.3: `March 2021 to March 2024`. Section 4.1 p.12: `June 2021 to March 2024`. Conclusion p.18: `between April 2021 and March 2024`. Appendix A p.22: `February 2021 to March 2024`. The Table 2 / Table 3 quarter headers run `2021-06` through `2024-03`, which is consistent with the section 4.1 wording. The exact sample window is therefore `data gap`.
- **Code / data availability.** No data-availability statement, code-availability statement, replication package, repository URL or `github` string appears anywhere in the pinned text (word scan). Every availability field is `not stated in source`.
- **Pre-write source-identity dedup (hidden-inclusive, executed 2026-09-27).** `rg -uuu` over all `*.md` / `*.csv` / `*.json` / `*.txt` in the repository, including `.mimo-worktrees`, `.agents` and `.hermes`, for `7226353`, `Crypto Futures Risk Mitigation`, `Ifigenia`, `Georgiou`, `Sapuric`, `Eigenheer`, `one-touch digital` and `default-aversion`: **zero hits**. `coverage_manifest.csv` (1,088,787 bytes) for `7226353|Georgiou|Sapuric|Eigenheer|one-touch`: **zero hits**. `git log --oneline -20` was inspected as a convenience glance only and does not by itself satisfy dedup.
- **Four-axis distinction against the nearest existing records (source identity and mechanism differ in every pair).**
  1. Repo record `crypto-futures-term-structure-roll-yield-carry-2026-08-31.md` (Schmeling, Schrimpf & Todorov, `Crypto Carry`, DOI `10.1287/mnsc.2024.01524`): different source identity; that record is a **cross-sectional curve-carry rank** across coins and maturities, this record is a **single-asset (BTC/ETH only) portfolio-construction and default-insurance experiment**; signal construction (carry rank vs ex-ante-Sharpe-gated inception plus probability-of-default trigger), universe (multi-coin multi-maturity vs two assets on one venue's quarterly contracts), horizon (weekly/monthly rebalance vs multi-day portfolio runtimes monitored every 5 minutes or hourly), and material data dependency (curve basis only vs Deribit DVOL + Monte-Carlo default probabilities + a simulated one-touch premium) all differ.
  2. Wiki `[[quant/btc-perp-single-venue-funding-carry-taker-fee-falsification-2026-09-14]]`: perpetual **funding-rate** carry versus **dated quarterly futures basis**; rate predictability versus a risk-overlay claim.
  3. Wiki `[[quant/bitcoin-ibit-options-cme-futures-implied-carry-wedge-2026-09-01]]`: options-versus-futures implied-carry **wedge arbitrage** versus a **purchased protective digital option** that is an insurance leg, not an arbitrage leg.
  4. Repo record `kalshi-btc-event-contract-spot-hedge-2026-09-15.md`: one-touch appears there as a **prediction-market event contract** priced against a vanilla Black-Scholes mispricing signal; here it is a **protective digital call inside a levered basis position**, different market type, different signal role.
  5. Repo record `crypto-funding-rate-arbitrage-event-driven-mvo-adaptive-interval-2026-09-23.md`: funding-rate arbitrage with mean-variance allocation versus probability-of-default-driven exposure reduction.
- **Scope of this record.** The paper contributes no new predictive alpha; its contribution is an implementation-and-risk-overlay construction on an already-documented carry anomaly. Nothing here is independently reproduced.

## Economic mechanism

### Source-reported

The source frames three nested hypotheses on the `Crypto Carry Puzzle` (pp.4-8): crypto futures carry unusually large **convenience yields**, which under cost-of-carry pricing (`F = S * e^(r + s - c) * t`, eq.1, p.6; convergence form eq.3, p.6) mean futures price below spot, so a long-spot / short-futures position captures the convergence payoff.

- **H1 (p.7):** `A strategy combining long spot and short futures positions will earn a positive ARP, driven by high convenience yields and inefficiencies.`
- **H2 (p.7):** `Default-aversion strategies using high-frequency rebalancing outperform an unprotected approach, lowering forced liquidations and improving Sharpe ratios.` The source defines default-aversion as investors' dislike of the possibility of the borrower defaulting even when compensated by high expected returns (p.5).
- **H3 (p.8):** `Including protective one-touch options in a long-spot, short-futures portfolio can create near-arbitrage opportunities by insulating positions from market volatility.`

The stated contribution over Schmeling, Schrimpf & Todorov (2023) is portfolio-level implementability under margin, liquidation and funding constraints, plus a `dynamic risk management method akin to CPPI-based default-aversion techniques` on **dated (quarterly)** rather than perpetual futures (p.8). The arbitrage portfolio combines a 5x leveraged spot-futures position with a one-touch digital call that pays out on default-triggering price moves, purchased once as `insurance` with no rebalancing (pp.10-11).

### Research interpretation

Component roles, normalised so each can be ablated independently:

```text
Carry base (H1):     long Binance spot + short Binance quarterly future, fully funded
                     at 1x, or 5x-levered with 20% collateral
Regime / entry gate: ex-ante Sharpe >= 1.0 at inception, Sharpe denominator built
                     from Deribit DVOL and a spot-futures correlation borrowed from
                     the prior literature; no new entries within 6 days of expiry
Overlay A (H2):      probability-of-default trigger - Monte-Carlo PoD over the next
                     2 hours, reduce exposure when PoD > 25%, target PoD 5%
Overlay B (H3):      one-time purchase of a one-touch digital call sized to neutralise
                     loss-given-default, expiry matched to the future
Exit:                convenience yield <= 0, or upper margin threshold reached,
                     or contract expiration
```

The hypothesised frictions are limits-to-arbitrage (custody risk, fragmented liquidity, exchange-level automatic liquidation) sustaining the basis, plus a **risk-engineering** channel: PoD-triggered de-risking should remove forced-liquidation outcomes without destroying carry, and a correctly priced digital option should convert residual default loss into a flat payoff. Research interpretation: H1 is a carry/convergence thesis, H2 and H3 are **not alpha claims** - they are claims that risk overlays improve the Sharpe of a carry book. Under this reading, if H1 fails, H2 and H3 have nothing to protect, so the falsification plan tests H1 first. Do not treat the three hypotheses as independent evidence.

## Signal

All parameters below are `source-reported` unless tagged. Where the source prints nothing, the gap is marked; no operational value has been invented.

**Data formation / tradability.** Five-minute closing spot and futures prices from Binance (p.9); positions are established `at inception` of each candidate portfolio and conditions are checked every 5 minutes post-trade (p.9). Signal-formation timestamp, bar close convention, timezone of the 5-minute bars, and the timezone of the `end-of-day revaluation at 23:55 (or upon closing)` (p.9) are `not stated in source` -> `data gap`.

**Entry (H1, unprotected ARP; p.9).**
- Direction: long spot, short the corresponding quarterly future, market-neutral at notional level.
- Gate: `At inception, the portfolio must meet a minimum expected Sharpe ratio of 1.0` (p.9). Expected return and risk come from observable convenience yield and risk-free return; volatility denominator = variance of the spot-minus-futures difference built from the **highest hourly Deribit DVOL value** and a spot-futures correlation `estimated in Schmeling et al. (2023) and confirmed in this paper to exceed 0.9` (eq.5, p.9).
- Exclusion: `New positions are not initiated within six days prior to expiration` (p.9).
- Size: `The position size range is set between USD 375,000 and USD 2,000,000` (p.9). The rule that selects a specific size inside that band is `underspecified`.
- Funding: `This strategy employs no leverage - both spot and futures positions are fully funded` (p.9).

**Exit (all three strategies; p.9).** Close if any of: convenience yield `<= 0`; `upper margin threshold is reached` (defined as a maintenance margin of `5.0%`); contract expiration. Precedence among simultaneous exit conditions, order type, and execution reference price are `not stated in source`.

**Overlay A - protected ARP (pp.9-10, 14-16).**
- Leverage up to 5x (20% collateral); initial margin lower than the 1x case (Table 1, p.10).
- Probability of default estimated by Monte Carlo with `1,000 iterations` (p.10) / `1,000 Monte Carlo iterations` (p.15).
- Triggers: `PoDmax = 25%` and `PoDtarget = 5%` (p.10); `maximum probability of default (PoD,max) of 25%, a target probability of default (PoD,target) of 5%` (p.15).
- Binary search for the transaction notional matching the 5% target: `step size of 6`, accuracy `+/- 1.625%` concerning the transaction notional (pp.15-16); elsewhere the same accuracy is given as `binary search accuracy of 1.625%` (p.15).
- Monitoring frequency is **contradicted inside the source**: question (b) p.5 says `high-frequency (5-minute) default-aversion rebalancing`; section 3.2.2 p.10 says `rebalancing steps at 5-minute intervals`; section 4.2.1 p.15 says `hourly monitoring and estimating the probability of default (PoD) over the next two hours ... observations conducted hourly`. All three are recorded, none reconciled.
- Execution direction: exposure is **only reduced**, never re-established (`we dynamically reduce exposure without re-establishing it`, p.9). Rebalance execution price, order type and fill assumption are `not stated in source`.

**Overlay B - arbitrage / insured near-arbitrage (pp.10-11, 17-18).**
- Long spot + short futures at 5x leverage plus a `binary (digital) call option that pays out upon default-triggering price moves`; `The option expires with the futures contract. No rebalancing is needed; it is a one-time purchase of insurance` (p.10).
- Only BTC and ETH contracts with ex-ante Sharpe > 1.0 are considered (p.10).
- Premium: `the option's premium ... priced by Monte Carlo (1,000 simulations). We search for the option cost that neutralizes default losses - if that cost still permits a net positive return ... we have achieved a form of insured arbitrage` (pp.10-11).
- The **barrier definition** (what price constitutes a `default-triggering price move`), the volatility surface and strike input to the Monte Carlo, the quoting venue, whether the option is exchange-listed or OTC, and how it is marked after purchase are all `not stated in source` -> `underspecified`. The paper's own figures for this leg are captioned `Simulation of prices for one-touch options` (p.24), i.e. simulated rather than quoted.

**Holding period.** Not a fixed horizon: portfolios run until one of the exit conditions fires. Source-reported runtimes are listed under Evidence.

**Parameter provenance.** `Sharpe >= 1.0`, `5.0%` maintenance margin, `USD 375,000-2,000,000`, `5x`, `PoDmax 25%`, `PoDtarget 5%`, `1,000` Monte Carlo draws, `1.625%` search accuracy, `6 days` pre-expiry exclusion, `23:55` revaluation are all **source-reported**. The source states of the PoD parameters: `These parameters were set arbitrarily to allow for various scenarios and have not been optimized` (p.16). Any threshold not printed above is `research-proposed` and appears only in the falsification plan, where each cutoff is `research-defined`.

## Required data

- **Instrument:** BTC and ETH quarterly (dated) futures plus the same-asset spot leg; `here we maintain USDT-based futures data`, and COIN-M futures are explicitly not used (p.9). Quote currency USD/USDT. Roll treatment: positions are not opened within 6 days of expiry and close at expiry; the roll rule into the next quarter is `not stated in source` -> `data gap`.
- **Universe:** BTC and ETH only. Inclusion rule = ex-ante Sharpe >= 1.0 at a 5-minute inception grid. No liquidity, volume, listing-age or open-interest filter is printed -> `data gap`.
- **Venue / vendor:** Binance for 5-minute spot and futures closes (p.9, Appendix A p.22); Deribit for the hourly DVOL index (p.9); USD 1M/3M/6M LIBOR, interpolated daily, as the risk-free rate (p.9, p.22). Single price venue for the traded legs.
- **Timeframe:** five-minute bars; end-of-day revaluation at `23:55` (timezone `not stated in source`); hourly DVOL (highest hourly value used); daily LIBOR. The 24/7 session convention and bar-boundary alignment are `not stated in source` -> `data gap`.
- **Fields:** spot close, futures close, contract expiry timestamp, implied-volatility index level (DVOL), spot-futures correlation (borrowed from prior literature, not re-estimated per period), risk-free rate, maintenance margin, convenience yield (derived from cost-of-carry deviation, Appendix A.1), option premium (simulated).
- **Not required by the source but required for an honest re-run:** order-book depth / bid-ask, funding, open interest, liquidation price ladder, venue fee schedules by tier, option market quotes.
- **Point-in-time:** the source does not describe publication lags or availability conventions for DVOL or LIBOR beyond `hourly` and `daily` -> `data gap`. Whether LIBOR inputs were available through the stated end-2024 sample is `not stated in source` -> `data gap`.
- **Missing data:** no null/stale/suspended/bad-print handling rule appears anywhere -> `data gap`. Imputation, if any, is `not stated in source`.
- **Funding / fee / spread needs:** taker fees are modelled (see Execution assumptions); bid-ask spread, slippage, market impact, participation, capacity, latency, partial fills, collateral financing beyond LIBOR, and liquidation execution are **not modelled** -> `data gap`, never zero.

## Execution assumptions

- **Order type / timing:** the source states that trades are `executed` and that conditions are then checked every 5 minutes (p.9), but never states market vs limit, the reference price used for entry or for PoD-driven reductions, or the signal-to-order delay -> `underspecified`. Fill model: `not stated in source`.
- **Transaction costs (source-reported, section 3.3.3, p.11):** `Our transaction cost estimates for Taker Fees were 0.10% of transaction volume for spot, 0.05% of transaction volume for futures and 12.5% of option premium for options.`
  - Unprotected: `total opening and closing costs being 0.15% respectively` (i.e. 0.15% to open both legs and 0.15% to close them).
  - Protected: opening `0.15%`; `BTC portfolios total rebalancing costs, given 1.6x rebalancing on average equalled 0.09%`; `ETH portfolios total rebalancing costs, given 3.7x rebalancing on average equalled 0.185%`; closing `0.15%`.
  - Arbitrage: opening `0.15%`; `BTC portfolios option transaction costs equalling 0.11%`; `ETH portfolios option transaction costs equalling 0.06%`; the closing sentence repeats the `0.15%` opening figure verbatim, so the closing-cost statement for this leg is internally garbled -> `underspecified`.
- **Costs the same source explicitly does not model (both quoted, not inferred):** section 3.2.2 p.10: the protective rebalancing `may incur extra transaction costs (not modeled here)`. Section 4.2.2 p.16: `significant reductions in position sizes may lead to higher transaction costs, which were not considered in this analysis`. These two statements contradict the transaction-cost-adjusted results reported in section 3.3.3.2 and Tables 7 and 11.
- **Spread / slippage / impact / capacity:** word scan of the pinned text shows `slippage` twice (p.17 named as a risk when defaults occur; p.18 listed as future work alongside `staking returns ... partial funding constraints`), `bid/ask` once (p.17, `the risk of increased bid/ask spreads at lower levels of option delta`), and **zero** occurrences of `capacity`, `latency`, `fill`, `maker`, or any market-impact model. No cost rate is attached to any of them -> `data gap`, never zero.
- **Funding:** `funding` appears twice in the whole document - once in the introduction as `margining ... funding constraints` (p.4) and once in the conclusion as `partial funding constraints` deferred to future work (p.18). The study uses dated futures (no perpetual funding mechanism), and the financing return on the residual cash / the cost of the collateral is `not stated in source` -> `data gap`.
- **Leverage / margin:** 1x (fully funded) for the unprotected book; up to 5x with 20% collateral for the protected and arbitrage books; maintenance margin `5.0%`; Table 1 (p.10) prints the initial forced-liquidation futures price for a worked BTC 09/21 example: `99,834 / 74,236 / 65,703 / 61,436 / 58,876` at leverage `1.0 / 2.0 / 3.0 / 4.0 / 5.0`, alongside `E(return) 8.99% 11.98% 13.47% 14.37% 14.97%`, `E(risk) 8.98% 11.97% 13.46% 14.36% 14.96%` and `E(Sharpe ratio) 1.00102998` for every leverage level (the annualisation convention for those percentages is `not stated in source`).
- **Borrow / shorting:** the short leg is a futures short, so no securities borrow is modelled; the word `borrow` appears once, inside the definition of default-aversion (p.5).
- **Liquidation:** forced liquidation is the object of study, but the liquidation price rule, insurance-fund / auto-deleveraging interaction, and the cost of being liquidated are `not stated in source` -> `data gap`.
- **Latency / partial fills / failures:** `not stated in source` -> `data gap`.

## Evidence

### Source-reported

Every figure below is `source-reported`, traced to the pinned PDF (SHA-256 `614218f8...37176`). None has been independently reproduced, and the source itself reports **no** t-statistic, p-value, confidence interval or significance test anywhere in the 24 pages (word scan for `t-stat`, `p-value`, `statistically significant`, `confidence interval`: zero hits).

**Convenience yield (the precondition, section 3 `Initial Findings`, p.12; Appendix A.2, p.22)**
- Average annualised convenience yield: **BTC 7.23%**, **ETH 6.63%**; described as `averaging 10%, consistent with Schmeling et al. (2023)`.
- Near-dated futures exceed far-dated by `1.76% and 1.77% average spread for BTC and ETH` (p.22).
- Regression of yield changes against spot-price changes: slopes `0.21 (BTC, one month)`, `0.30 (BTC, one week)`, `0.11 (ETH, one month)`, `0.22 (ETH, one week)` (p.12).

**H1 - unprotected ARP (Table 2 p.12, Table 3 p.13, section 4.1.4 p.14)**
- `30,358 portfolios with a Sharpe ratio exceeding 1.0` = **16,254 BTC** (Table 2) + **14,104 ETH** (Table 3), drawn from `a total of 348,765 five-minute intervals`, i.e. **4.7%** of BTC intervals and **4.0%** of ETH intervals (section 4.1.4).
- `portfolios achieving 111% of the estimated Sharpe ratios` (p.12).
- `the median realized portfolio Sharpe ratio across all portfolios being 1.52, compared to an overall average estimate of 1.37` (section 4.1.4).
- Table 7 `All Portfolios / 1X` column: expected SR >= 1 `30358`; `Average Expected` Sharpe `1.55`; `Average Realised` `2.05`; `Median Realised` `1.35`; runtime `Average Expected 38` days vs `Average Realised 14` days; `Transaction Cost Adjusted Returns / Average Realised` `1.89` (**units are not printed in the table** -> `not stated in source`).
- Table 7 BTC / ETH 1X columns: expected SR `1.53` / `1.56`; realised average `2.11` / `1.99`; realised median `1.53` / `1.29`; runtime expected `39` / `38` days, realised `14` / `15` days; transaction-cost-adjusted realised `1.94` / `1.82` (units `not stated in source`).
- Transaction-cost-adjusted average realised return by quarter is **negative in six cells**: BTC Table 2 `-6.54`, `-1.01`, `-0.34`; ETH Table 3 `-14.05`, `-0.84`, `-0.82` (column identity: the `Transaction Cost Adjusted Returns / Average Realised` row under the quarter headers `2021-06 ... 2024-03`; units `not stated in source`). Section 4.1.2 concedes the unprotected portfolio `suffer[s] from transaction costs where the opportunity set (i.e. number of portfolios) is small`.
- Defaulting: `none of the portfolios experienced default` at 1x (section 4.1.2, p.13) because `the futures price would need to increase by 95%`.
- **No default probabilities (Table 4, p.14), Monte-Carlo 1,000 samples at 80% volatility, collateral 22-day / 8-day columns:** `100%` -> `0.2% / 0.0%`; `50%` -> `5.4% / 0.1%`; `33%` -> `14.7% / 2.1%`; `25%` -> `23.4% / 6.5%`; `20%` -> `34.5% / 13.2%`.

**H2 - protected ARP (Table 7 p.15, Table 8 p.16, sections 4.2.1-4.2.2)**
- At 5x, `5,539 (18.2%) defaulted under the 5X leverage strategy` of the 30,358 (p.14); broken down as BTC `1,104` = `6.8%` and ETH `4,435` = `31.4%` (p.17).
- Protection applied to `a random sample of 200 portfolios` per asset (400 total, `1.3`% of the dataset per Table 7).
- Table 7 `5XP` columns: expected SR `1.32` (all) / `1.14` (BTC) / `1.31` (ETH); realised average `1.11` / `0.70` / `1.51`; realised median `1.49` / `1.22` / `1.61`; runtime expected `71` / `61` / `71` days, realised `13` / `14` / `13` days; transaction-cost-adjusted realised `1.03` / `0.66` / `1.42` (units `not stated in source`).
- Table 7 `5XU` (defaulted, unprotected at 5x) columns: expected SR `1.31` / `1.16` / `1.34`; realised average `-0.80` / `-1.54` / `-0.61`; realised median `-0.85` / `-1.33` / `-0.69`; transaction-cost-adjusted realised `-0.99` / `-1.76` / `-0.84`.
- Section 4.2.1: `the returns of the unlevered portfolios were fully retained with comparable Sharpe ratios`, and `the protected portfolios had a lifespan 50-60% longer than their unprotected counterparts`.
- Table 8 (`Effects of rebalancing`, 400 portfolios): `# Defaulted 78` = `20%` overall (`42` BTC = `21%`, `36` ETH = `18%`); defaulted `Before 1st REBAL` `50 / 40 / 10`; `# REBALs on Average` `2.7 / 1.6 / 3.7`; `Average first REBAL at day` `6.9 / 7.0 / 6.8`; `Minimum first REBAL at day` `1 / 3 / 1`; `Average reduction (%)` of futures exposure `58 / 45 / 68`; `Minimum reduction (%)` `25 / 25 / 34`; a second row also captioned `Minimum reduction (%)` prints `100 / 67 / 100` (duplicate caption, likely intended as maximum -> recorded as a source label defect); `Average PoD triggering REBAL` `34` with `Maximum 59` and `Minimum 25`; `Average PoD after REBAL` `6` with `Maximum 13` and `Minimum 1`.
- Section 4.2.2 narrative: `Despite setting the PoD threshold at 25% within a 2-hour interval, defaults persisted in 20% of portfolios. However, the average PoD triggering rebalancing occurred at 34% ... the PoD after rebalancing slightly exceeded the 5% target, with portfolios sometimes exiting rebalancing events with a PoD of up to 13%`.
- Section 4.2.2 on parameters: `These parameters were set arbitrarily to allow for various scenarios and have not been optimized.`

**H3 - one-touch-insured `arbitrage` (Table 11, pp.17-18; narrative section 4.3.1, p.17)**
Table caption: `Results of Arbitrage portfolios for BTC and ETH 06/21` - i.e. **June 2021 contracts only**.

| Row (Table 11) | BTC | ETH |
|---|---|---|
| `# Portfolios` | 8473 | 6606 |
| `Default rate %` | 8.47 | 60.46 |
| `Expected Average Runtime` | 77 | 76 |
| `Expected Average Return %` | 3.97 | 4.64 |
| `Loss given default %` | -3.72 | -1.41 |
| `Required portfolio protection %` | 4.58 | 1.98 |
| `Average option price in % of notional` | 18.83 | 20.04 |
| `Cost of portfolio protection %` | -0.86 | -0.51 |
| `Non-default case return %` | 3.11 | 4.13 |
| `Default rate adjusted total arbitrage return %` | 2.84 | 1.63 |
| TC-adjusted `Expected Average Return %` | 3.56% | 4.27% |
| TC-adjusted `Non-default case return %` | 2.70% | 3.76% |
| TC-adjusted `Default rate adjusted total arbitrage return %` | 2.47% | 1.49% |

- Narrative (p.17): `In the non-default scenario, the expected return of 3.97% is reduced by the option cost of -0.86%, yielding an expected profit of 3.11%. Conversely, in the default scenario, the portfolio achieves a neutral return (0.00%), comprised of a -3.72% loss from the base strategy, the option cost of -0.86%, and a compensating payout of 4.58% from the one-touch option.`
- Scout arithmetic (labelled `research interpretation`, not a source claim): `3.11 * (1 - 0.0847) = 2.846` reproduces the printed BTC `2.84`, and `4.13 * (1 - 0.6046) = 1.633` reproduces the printed ETH `1.63`; the two reported headline rows are therefore internally consistent arithmetic on the printed inputs.
- The source itself lists the reasons the apparent arbitrage may not be capturable (p.17): `transaction costs; the risk that option prices deviate significantly from their theoretical value (TV); the risk of increased bid/ask spreads at lower levels of option delta; and the risk of slippage when defaults occur due to potentially high market volatility`.
- Conclusion (p.18): option-based protection `can approximate an arbitrage condition by neutralizing losses in default scenarios, although high implied volatility and illiquid option markets are limiting factors`.
- **The relationship between `Average option price in % of notional` (18.83 / 20.04) and `Cost of portfolio protection %` (-0.86 / -0.51) is never defined in the source** -> `underspecified`; the record does not attempt to reconcile them.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Selection and evaluation use the same statistic: only 5-minute intervals with ex-ante Sharpe `>= 1.0` are retained (4.7% BTC / 4.0% ETH), and realised performance is then reported on that selected subset (pp.9, 14).
2. Transaction-cost-adjusted average realised returns are negative in six quarter cells of the unprotected book (Table 2 `-6.54`, `-1.01`, `-0.34`; Table 3 `-14.05`, `-0.84`, `-0.82`; units `not stated in source`).
3. The source itself concedes the unprotected book fails after costs where the opportunity set is small (section 4.1.2).
4. The sample window is stated four different ways inside one document (`March 2021`, `June 2021`, `April 2021`, `February 2021` start), never reconciled.
5. The monitoring cadence of the headline overlay is self-contradictory: 5-minute (p.5, p.10) versus hourly (p.15).
6. Protection failed outright on 78 of 400 protected portfolios - `20%` still defaulted (Table 8).
7. The PoD control overshot both ways: average trigger at `34%` against a `25%` cap, and post-rebalance PoD up to `13%` against a `5%` target (Table 8).
8. The overlay parameters were `set arbitrarily ... not been optimized` by the source's own admission (p.16), so the reported results are not a tuned-or-registered configuration either way.
9. Rebalancing costs from the ~58% exposure reduction are explicitly `not modeled here` (p.10) and `not considered in this analysis` (p.16), directly contradicting the transaction-cost-adjusted columns in Tables 7 and 11.
10. No bid-ask spread, slippage, market-impact, participation, capacity, latency, fill or partial-fill model exists anywhere; `capacity`, `latency`, `fill` and `maker` return zero hits in the pinned text, and `slippage` / `bid/ask` appear only as named risks and future work.
11. No funding or collateral-financing cost is modelled; `partial funding constraints` is deferred to future work (p.18).
12. Zero statistical inference: no t-statistic, p-value, confidence interval, standard error or hypothesis test appears in the document, for any of the three hypotheses.
13. No out-of-sample, hold-out or walk-forward separation exists; gate construction and evaluation share the 2021-2024 sample.
14. The entire H3 result rests on `06/21` contracts (Table 11 caption) - one contract month inside the sample, in a bull regime.
15. ETH `Default rate 60.46%` under the `near-arbitrage` construction (Table 11): the hedge pays out in a majority of ETH portfolios, which is an insurance outcome, not an arbitrage.
16. `Average option price in % of notional` of 18.83 / 20.04 sits an order of magnitude away from `Cost of portfolio protection` of -0.86 / -0.51 with no definition bridging them -> `underspecified`.
17. The one-touch option's venue, quoting convention, pricing model, volatility input and post-purchase mark are all `not stated in source`; the premium is Monte-Carlo simulated rather than quoted (pp.10-11, p.24).
18. The ex-ante Sharpe denominator borrows the spot-futures correlation from Schmeling et al. (2023) rather than estimating it per period (eq.5, p.9), so the entry gate partly encodes a prior paper's parameter.
19. Runtime figures disagree inside the source: `Average Realised 14` days (Table 7) versus `averaging 8.2 days compared to the estimated 22.0 days` (section 4.1.2) versus `Average Expected 38` days (Table 7).
20. Sharpe figures disagree inside the source: section 4.1.4 prints median realised `1.52` and average estimate `1.37`, while Table 7 `All / 1X` prints median realised `1.35` and average expected `1.55`.
21. Document integrity defects: `Exhibit 2`, `Exhibit 3` and `Exhibit 7` are cited (pp.13, 14) but no exhibit exists in the pinned PDF; table numbering skips 5, 6, 9 and 10; section 4.1.4 cites non-existent `Tables 4.1.1 and 4.1.2`; subsection `4.1.2` is used twice; Table 3 is captioned `Tabel 3`; Table 8 has two rows captioned `Minimum reduction (%)`.
22. The cited magnitude of the underlying anomaly is inconsistent in the source itself: `as high as 40%, with an average around 10%` (p.4) versus `as high as 60% per annum` (p.7), both attributed to Schmeling et al. (2023).
23. The opportunity set is regime-clustered: the selected-portfolio count rows print `0` in several 2022 and 2023 quarters, and section 4.1 states opportunities existed in 2021 and 2024 with only limited opportunities in 2022 and up to Q3 2023 - the headline results therefore lean on two sub-periods.
24. Forced-liquidation execution is never modelled: liquidation is the risk the whole paper is built around, yet the liquidation price rule and its cost are `not stated in source`.
25. Provenance-level defects: author order and one affiliation differ between the SSRN landing page and the PDF title block; the landing page's `0 References` conflicts with its own `49 References` link and with the 49-entry PDF list.
26. No code, no data-availability statement and no replication package exist, so none of Tables 2, 3, 4, 7, 8 or 11 can be regenerated from the source alone.

## Falsification plan

All thresholds below are `research-defined falsification thresholds` chosen by the Scout; all reconstruction parameters not printed by the source are `research-proposed`. Failure action for every test is: **do not advance the hypothesis past research-only, and record the failure in this record.**

1. **F1 - Frozen forward replication.** Freeze the three constructions as printed (no re-tuning) and run them forward from `2026-10-01` for 24 months on BTC/ETH quarterly futures. Fail if the protected book's median realised Sharpe is `< 1.0` after all-in costs. (`research-defined`: 1.0, 24 months.)
2. **F2 - Sample-window recovery gate.** Rebuild Tables 7 and 11 from raw 5-minute Binance data before any forward test. Fail if All/1X average expected Sharpe is outside `1.55 +/- 0.05`, realised median outside `1.35 +/- 0.05`, or BTC/ETH default rates outside `8.47 +/- 0.30` and `60.46 +/- 1.50` percentage points. (`research-defined` tolerances; failure means the source's own numbers cannot be recovered, so stop.)
3. **F3 - All-in cost ladder.** Add per-leg costs of `0 / 1 / 2 / 5 / 10 / 20 bp`, plus an option-premium haircut of `0 / 5 / 10 / 20%`, plus collateral financing at the prevailing T-bill rate. Fail if the default-rate-adjusted arbitrage return (printed 2.47% BTC / 1.49% ETH, Table 11) turns negative at `10 bp` or loses `> 50%` of its gross value at `5 bp`. (`research-defined`.)
4. **F4 - Reinclude the omitted rebalancing costs.** Charge the PoD-driven reductions (average exposure cut `58%`, Table 8) at the source's own taker schedule. Fail if the protected transaction-cost-adjusted return (Table 7 `5XP`: `1.03` all / `0.66` BTC / `1.42` ETH, units as printed) falls by more than `50%`. (`research-defined`.)
5. **F5 - Selection-inflation control.** Evaluate the ex-ante-Sharpe-gated subset against the unconditional interval population on a disjoint hold-out window, with a block-bootstrap interval on the difference. Fail if the interval **includes zero**. (`research-defined`: inclusion of zero = no gate value.)
6. **F6 - Decisive overlay ablation.** Compare (a) protection as specified, (b) a sham overlay that rebalances on a random schedule at matched trade count, (c) a sign-shuffled PoD trigger, all at 5x on identical inception dates. Fail if protection does not beat both shams by `>= 0.20` Sharpe. (`research-defined`: 0.20.)
7. **F7 - PoD calibration.** Compare realised default frequency with the stated cap: for the protected book, fail if the 95% binomial interval of the realised default rate excludes the `25%` cap. (`research-defined`.) This directly targets the source's own observed `34%` average trigger.
8. **F8 - Option-price realism.** Replace the Monte-Carlo premium with executable quotes on a named venue for a contract with matched barrier semantics. Fail if the required protection cost exceeds the printed `-0.86%` (BTC) / `-0.51%` (ETH) by more than `2x`, or if the payout no longer neutralises loss-given-default. (`research-defined`: 2x.)
9. **F9 - Instrument availability gate.** Verify that a tradeable one-touch / digital BTC or ETH option with the required barrier semantics exists on a named, liquid venue at the required dates and notional (`USD 375,000-2,000,000` source-reported band). Fail if no such venue quotes it, or if displayed depth at the required delta is `<= 10%` of the position. (`research-defined`.)
10. **F10 - Liquidation-aware replay.** Re-simulate with an explicit liquidation price rule and liquidation cost. Fail if any protected-portfolio headline sign flips (default rate, protected realised Sharpe, or adjusted arbitrage return). (`research-defined`.)
11. **F11 - Placebo on the carry input.** Circular-shift the convenience-yield series `1,000` times, rebuilding portfolios each time. Fail if the observed net return is below the `95th` percentile of the null. (`research-defined`: 1,000 draws, 95th percentile.)
12. **F12 - Subperiod and venue stability.** Require non-negative net-of-cost Sharpe in each of 2021 / 2022 / 2023 / 2024 and on a second venue's quarterly contracts. Fail if any sub-period or the second venue is `<= 0`. (`research-defined`.)
13. **F13 - Multiplicity control.** Apply Benjamini-Hochberg over the full tested family (3 constructions x 2 assets x reported quarters x the reported Sharpe/return/Sharpe-percentage cells). Fail if any surviving claim has `q >= 0.10`. (`research-defined`.)
14. **F14 - Independent reproduction gate.** A clean-room implementation must reproduce Table 8 rebalance counts (`2.7 / 1.6 / 3.7` average events, `78` defaults) and Table 11 default rates within `+/- 10%` relative error. Fail otherwise. (`research-defined`: 10% relative.)

## Crypto portability

**direct.**

The evidence is itself crypto: BTC and ETH futures and spot on Binance, 5-minute bars, March 2021 - March 2024 (window statement `data gap` per Provenance), with Deribit DVOL as the volatility input. No porting step is required to place the mechanism in crypto, and no traditional-asset result is being re-labelled as crypto evidence.

`direct` is not a tradability or adoption statement. Residual crypto-specific gaps inside this direct setting remain `data gap`: the one-touch option venue, quoting and liquidity are `not stated in source` (H3 may be unimplementable, F9); collateral financing / funding of the cash leg is unmodelled; the 24/7 session has no reconciliation with the `23:55` revaluation or the daily LIBOR grid (timezone `not stated in source`); single-venue dependence with no venue-fragmentation analysis; mark/index price and contract specification (tick size, notional multiplier, settlement) `not stated in source`; forced-liquidation price rule, insurance fund and auto-deleveraging `not stated in source`; custody of the long spot leg across the multi-day runtime is unmodelled.

## Limitations

- `data gap`: exact sample window (four inconsistent statements); timezone and bar-boundary conventions; missing-data handling; roll rule; funding / collateral financing; spread, slippage, impact, participation, capacity, latency, partial fills; liquidation price and cost; option venue, model and quotes; units of the transaction-cost-adjusted return rows; code and data availability.
- `underspecified`: position size selection inside the printed `USD 375,000-2,000,000` band; entry/exit order type and reference price; closing-cost statement for the arbitrage leg; the bridge between `Average option price in % of notional` and `Cost of portfolio protection %`; the barrier definition of the one-touch option; monitoring cadence of the protected overlay.
- `not stated in source`: any statistical significance test; any hold-out or walk-forward evaluation; any capacity analysis; peer-review status is affirmative (`preprint, not peer reviewed`), journal status is `not stated in source`.
- Source-quality: preprint, not peer reviewed, `All rights reserved`, no replication package, and multiple internal contradictions (items 4, 5, 19, 20, 21 of Negative evidence) - so even the `source-reported` figures should be treated as unverified third-party claims.
- Identification: H1 is a carry/convergence thesis whose precondition (positive convenience yield) is measured from the same prices used to trade it; H2 and H3 are risk-overlay claims conditional on H1 and are not independent evidence.
- Publication-bias / selection: the gate retains only 4.7% / 4.0% of intervals and results concentrate in 2021 and 2024.
- Reproducibility: `not independently reproduced`; nothing in our stack has regenerated any number in this record.
- Incremental-write check: this record was written only after a hidden-inclusive repo-wide source-identity search returned zero hits for the DOI, title and all three author names; the nearest existing records differ in source identity and in mechanism (see Provenance, four-axis distinction).

## Implementation status

`not-implemented`. No part of this construction exists in our research stack: no data pipeline for Binance quarterly futures with DVOL, no convenience-yield estimator, no Monte-Carlo probability-of-default engine, no one-touch pricing, no portfolio simulator, no backtest, no Paper, no Testnet, no Live. Nothing in this record implies Qlib full-backtest validation or any survivor status.

## Adoption boundary

This record is research material only. Its presence in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading.

`status: research-only`, `implementation_status: not-implemented`, `adoption: not-approved`, `approval_scope: research-only`. No wording, evidence count, confidence value or schedule behaviour in this record promotes it.

## Related Wiki records

Verified Wiki Brain pages (paths returned by `kb_search` on 2026-09-27; a fourth query on `one-touch digital option protection portfolio insurance default probability rebalancing` and one on `crypto futures basis carry convenience yield long spot short futures margin liquidation` both returned zero pages, so no page for this exact mechanism is claimed):

- [[quant/crypto-funding-carry-fade-turnover-cost-dissipation-falsification-2026-09-12]]
- [[quant/crypto-cross-venue-funding-carry-negative-results-cost-decay-2026-09-13]]
- [[quant/btc-perp-single-venue-funding-carry-taker-fee-falsification-2026-09-14]]
- [[quant/crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11]]
- [[quant/cross-venue-funding-carry-patient-rebalance-vs-active-harvesting-2026-09-12]]
- [[quant/bitcoin-ibit-options-cme-futures-implied-carry-wedge-2026-09-01]]

Adjacent records in **this repository** (not Wiki links, listed for dedup transparency): `crypto-futures-term-structure-roll-yield-carry-2026-08-31.md` (Schmeling et al., `Crypto Carry`), `btc-perp-single-venue-funding-carry-taker-fee-falsification-2026-09-14.md`, `crypto-funding-rate-arbitrage-event-driven-mvo-adaptive-interval-2026-09-23.md`, `kalshi-btc-event-contract-spot-hedge-2026-09-15.md`, `defi-on-chain-options-mispricing-hegic-arbitrum-2026-09-01.md`.

## Sources

1. Ifigenia Georgiou, Marc Eigenheer, and Svetlana Sapuric, `Crypto Futures Risk Mitigation: Dynamic Rebalancing, Carry and ARP Strategies`, SSRN preprint, `abstract_id=7226353`, DOI [`10.2139/ssrn.7226353`](https://doi.org/10.2139/ssrn.7226353), posted `3 Aug 2026`, 24 pages, `preprint ... has not been peer reviewed`. Landing page: <https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7226353>. Author order and one affiliation differ between the landing page and the PDF title block and are recorded unreconciled in Provenance.
2. Pinned PDF (same work, retrieved 2026-09-27 through the SSRN `Open PDF in Browser` delivery link): 528,297 bytes, 24 pages, SHA-256 `614218f8bfa1a278a32b80b1197c45c304ea5ed6ba1e61e360da61d8b1437176`; text extracted page by page with `pypdf` 6.16.2 and every page read. All table/figure/section provenance in this record refers to this file.
3. Cited inside the primary source and named here only as the source's own dependency, **not** used as independent evidence by this record: Schmeling, Schrimpf & Todorov, `Crypto Carry` (referenced by the primary source as Goethe University / BIS working paper, 2023); Alexander, Deng & Zou, `Optimal hedging with margin constraints and default aversion and its application to Bitcoin perpetual futures`, *Quantitative Finance* (2021); Makarov & Schoar, `Trading in cryptocurrency markets`, *JFE* 135 (2020).
