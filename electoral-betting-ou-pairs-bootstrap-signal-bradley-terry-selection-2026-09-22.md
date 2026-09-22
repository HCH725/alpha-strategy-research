---
schema: strategy-research-record-v1
title: Electoral Betting-Exchange Pairs Trading on Combined Nominee Implied Probability (Trending OU + Bootstrap Prediction Bounds + Bradley-Terry Candidate Selection)
created: 2026-09-22
updated: 2026-09-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - prediction-markets
  - betting-exchange
  - pairs-trading
  - ornstein-uhlenbeck
  - mean-reversion
  - political-markets
  - statistical-arbitrage
status: research-only
confidence: medium
source_as_of: 2026-09-18
sources:
  - "arXiv:2609.22639v1, Haoyu Liu, Len Thomas, Benjamin Baer, Carl Donovan, 'Adapting Pairs Trading to Gambling Markets: A Case Study of the U.S. Presidential Election', submitted 18 Sep 2026, https://arxiv.org/abs/2609.22639"
  - "Paper full text (HTML v1), https://arxiv.org/html/2609.22639v1"
  - "Code and data repository, https://github.com/lhy199661/2024-US-Election"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Electoral Betting-Exchange Pairs Trading on Combined Nominee Implied Probability (Trending OU + Bootstrap Prediction Bounds + Bradley-Terry Candidate Selection)

## Provenance

- **Primary source:** arXiv preprint **arXiv:2609.22639v1** — "Adapting Pairs Trading to Gambling Markets: A Case Study of the U.S. Presidential Election".
- **Authors (exactly as source):** Haoyu Liu, Len Thomas, Benjamin Baer, Carl Donovan.
- **Version / date:** v1 only; submission history shows `[v1] Fri, 18 Sep 2026 23:11:16 UTC`. Comments field: "44 pages, 12 figures, 3 tables". Subjects: `stat.AP` (primary), `q-fin.ST`.
- **Publication / preprint status:** arXiv preprint; no journal, conference, or peer-review status is stated in the source — **data gap** (not stated in source).
- **Stable URLs:** https://arxiv.org/abs/2609.22639 and https://arxiv.org/html/2609.22639v1 (both opened and read directly for this record; primary-source checksum performed against the v1 HTML full text, including Methods §2, case study §3, appendices C–E).
- **Code / data:** https://github.com/lhy199661/2024-US-Election — source states the repository contains the Betfair 2020 and 2024 U.S. Election data "purchased from the company BetData", that redistribution is permitted under the purchase agreement, and that BetData collected all data from Betfair using an API (Data Availability statement, § after Conclusion). The repository was not executed for this record.
- **Universe:** Betfair peer-to-peer betting exchange political markets; exactly two candidates per election — 2020: Trump (Republican) vs Biden (Democratic); 2024: Trump (Republican) vs Harris (Democratic).
- **Sample period (source-reported):**
  - Training (2020): 23 August 2020 (immediately before the Republican National Convention / one day before Trump's formal renomination) to 4 November 2020; odds recorded at 5-minute intervals; cleaned dataset **21,181 observations** (§1.1, §3.1.1).
  - Out-of-sample (2024): 23 August 2024 (after both major-party nominees confirmed) to 6 November 2024; 5-minute recording grid; **21,689 observations after data cleaning** (§1.1). First out-of-sample signal generated after 11:15 a.m. on 26 August 2024; final bet placed before 6:15 a.m. on 6 November 2024 (§3.2.1).
- **Transaction-cost treatment (verified in Methods §2.2 and §4, not from abstract):** the source explicitly models **no** transaction fees, no bid-ask spreads, no commission, no queue priority, no partial execution, no lay liability, and no settlement cash flows; returns are proportional changes in a selected decimal-odds quote under a "simplified frictionless representation" (§2.2, §3.2.2, §4).
- **Deduplication search (2026-09-22, full repository, not just recent log):** ripgrep across all `*.md` records and `coverage_manifest.csv` for `2609.22639`, the exact paper title, the author names, `gambling market`, `electoral`, `Betfair`, `PredictIt`, `Bradley-Terry`, and `Ornstein-Uhlenbeck` produced **no existing record for this source identity**. Adjacent but distinct records are listed under *Related Wiki records*; none shares this mechanism + signal construction on betting-exchange electoral odds.

## Economic mechanism

### Source-reported

Pairs trading exploits temporary mean reversion in the relationship between related instruments. The authors adapt the idea to political betting markets: rather than trading two securities, they model the **combined implied probability of the two major-party nominees**, defined as `Z_t = Σ_{i∈I} 1/O_{i,t}` (sum of inverse decimal odds, eq. in §2.1.3), as a latent **Ornstein-Uhlenbeck process with a time-varying mean-reversion level μ(t) and additive white observation noise**. The time-varying equilibrium is motivated by (a) the market over-round, which can hold the inverse-odds sum above the fair benchmark of one, and (b) the gradual reallocation of probability mass from outcomes outside the two-candidate subset to the leading nominees as uncertainty declines (§2.1.1, §2.1.3). The source frames this explicitly as **statistical arbitrage** (risky, convergence may fail), not as cross-price/no-risk arbitrage across all outcomes (§1.2).

When `Z_t` overshoots a one-step upper prediction bound, the model expects the combined implied probability to fall, which mechanically implies the decimal odds of at least one candidate rise; the strategy then backs the candidate-specific quote selected by an antisymmetric Bradley-Terry-type model (§2.2.1).

### Research interpretation

Falsifiable mechanism: **short-horizon mean reversion of a two-outcome implied-probability sum on a P2P betting exchange**, produced by transient over-shooting of aggregate lean (attention/news-driven pressure on both nominee books) against a slowly moving equilibrium. Component roles (ablation required before assuming each contributes):

```text
Model / regime:  latent trending OU (time-varying mean μ(t)) + additive noise, state-space ML + Kalman filter, parametric-bootstrap one-step predictive bound
Entry signal:    Z_t > upper (1-α) one-step predictive bound for Z_{t+1}, α = 0.05 (source-specified)
Candidate selection: no-intercept Bradley-Terry on X_i,t = (Y_i,t, ΔY_i,t), Y = 1/O, trained on 2020, threshold π ≥ 0.5 (source-specified)
Exit:            event-driven — first subsequent observation at which the selected quote differs from the entry quote (source-specified)
Sizing:          unit-notional synthetic position; no sizing, leverage, or risk rules stated in source (data gap)
```

Note the source's construction is "pairs-inspired" but executes as a **single open position in one candidate's odds quote** at a time (one bet precludes the other; §2.2). It does not hold a simultaneous long-short basket.

## Signal

All items below are **source-reported** unless marked research-proposed/research-defined.

- **Formation timestamp / tradability:** odds are recorded on a regular **5-minute grid**; a forecast origin exists at each scheduled observation `t`. The signal uses information up to `Z_1..Z_t` and the entry value is the observed decimal odds `O_{i,t}` at that same observation (§2.2, §2.2.1). Timezone convention of the recording grid: **not stated in source (data gap)**. The source does not model signal-to-order latency; it explicitly warns that a newly submitted order may not be matched immediately and the odds observed at signal time may no longer be available by the time the order reaches the queue front (§4).
- **Lookback / warm-up:** parameters `(θ, σ², ω²)` and the smooth expectation function `M(·)` are refit by maximum likelihood on the full history `Z_1..Z_t` available at each forecast origin (rolling/expanding refit via parametric bootstrap, §2.2.1); consecutive repeated (flat-period) values are collapsed to a single retained observation with the elapsed number of sampling intervals preserved in the continuous-time transition (§2.1.4, §3.1). Endpoints: history is all observations up to `t` inclusive.
- **Combined-probability variable:** `Z_t := Σ_{i∈I} 1/O_{i,t}` over the two major-party nominees (§2.1.3).
- **Entry trigger:** `S_t = 1{ Z_t > Ũ^{1-α}_{t+1|t} }` — enter when the current combined implied probability exceeds the parametric-bootstrap upper one-step predictive bound for `Z_{t+1}` (§2.2.1, eq. for `S_t`). Nominal level **1−α = 95% (α = 0.05)**, specified in Appendix D and used for the reported analyses.
- **Bootstrap bound construction (source-specified):** at each forecast origin `t`: fit the model on `Z_1..Z_t` by MLE, run Kalman recursions for the one-step predictive distribution, generate `B` bootstrap series recursively with parameter refit per replicate, refit to the original history, and take the empirical `(1−α)` quantile of simulated `Ẑ*_{t+1}` as the bound (§2.2.1 steps 1–4, Appendix D.1). **The numeric value of `B` is not stated in the sections reviewed — data gap.**
- **Candidate selection (which leg):** `Y_{i,t} = 1/O_{i,t}`; feature vector `X_{i,t} = (Y_{i,t}, ΔY_{i,t})` with `ΔY_{i,t} = Y_{i,t} − Y_{i,t−1}`; comparison score `d(X_1,X_2) = βᵀ(X_1 − X_2)` with the intercept fixed at zero to preserve antisymmetry (Hunter 2004); `π_t = 1/(1+exp(−βᵀ(X_1−X_2)))`. **Candidate 1 (Republican nominee) is selected when `π_t ≥ 0.5`, Candidate 2 (Democratic nominee) when `π_t < 0.5`** (§2.2.2, Appendix D.2). `β` is estimated once on 2020 training data; ties in the training label `L_t` are excluded from fitting (§2.2.2).
- **Exit:** `k = inf{ h ∈ ℕ⁺ : O_{i,t+h} ≠ O_{i,t} }` — the position is closed at the **first subsequent observation at which the selected quote differs from the entry quote**, in either direction; a positive odds-price return requires `O_{i,t+k} > O_{i,t}` (§2.2). `k` is unknown at entry and determined sequentially (no future information used at entry).
- **Holding period:** event-driven and variable, bounded by market activity in the recording grid; no fixed horizon, no stop-loss, no take-profit is specified (§4 lists variable quote duration as a limitation). Maximum holding: until the quote changes (or the sample ends).
- **Re-entry / overlapping positions:** only **one open position at a time**; signals arriving while a position is open are ignored; a new position may open from the first forecast origin after the previous close (§2.2). In the 2024 evaluation, no signal occurred while a position was open (§3.2.1).
- **Incomplete trades:** if the selected odds never changes again before the end of the sample, the trade is classified incomplete and excluded from realized-return calculations (§2.2).
- **Parameters and their source:** sampling interval 5 minutes (source); α = 0.05 (source, Appendix D); Bradley-Terry threshold 0.5 (source); feature set `(Y, ΔY)` (source); unit notional (source). Position sizing, capital allocation, risk limits, Kelly fraction, and any liquidity/participation cap: **not stated in source (data gap)**. Any threshold introduced later for our own testing is labeled research-proposed/research-defined in *Falsification plan*.
- **Underspecified items:** numeric `B`; timezone; whether `ΔY` at `t` uses the immediately previous 5-minute grid point or the previous retained (de-flattened) observation is described in terms of "most recently observed change" (§2.2.2) — treat as partially underspecified; exact Betfair market selection/market-id rules (which specific Betfair market contract backs each nominee) — not stated beyond "the Democratic and Republican nominees".

## Required data

- **Instrument / universe:** decimal odds `O_{i,t}` for exactly the two major-party nominees of one U.S. presidential election; inclusion limited to the post-nomination window (23 Aug – early Nov of the election year); no reconstitution rules beyond nominee confirmation (source).
- **Venue / market type:** Betfair peer-to-peer betting exchange, accessed through the Betdata historical archive (independent platform recording Betfair political betting odds); market type = event/binary betting exchange, not spot/perpetual/futures/options.
- **Timeframe:** 5-minute sampled odds quotes; also needs the flat/unchanged-run structure (consecutive repeats) for the de-flattening rule.
- **Fields:** decimal odds per nominee (mid/last quote convention **not specified — data gap**; source treats observed decimal odds as price quotes); implied probability `Y = 1/O`; combined `Z`; implied-probability changes `ΔY`.
- **Point-in-time / availability:** historical archive used retrospectively; training uses 2020 data only for `β` and is evaluated on 2024 (clean train/test separation by election). No live-availability lag model beyond the 5-minute recording grid; the source assumes the quote observed at `t` is the tradable quote (acknowledged as an execution limitation in §4).
- **Timestamps:** 5-minute grid; timezone not stated (data gap); out-of-order-record handling not stated (data gap).
- **Missing data:** genuinely missing scheduled observations are treated as **missing completely at random (MCAR)** (stated and flagged as possibly restrictive in §4); flat periods are collapsed, not imputed. No other imputation is specified.
- **Fees / funding / spread data:** none used — commission, spread, and execution data are explicitly out of scope (§2.2). Betfair's revenue model is commission rather than over-round (source-reported context, §2.1.1).

## Execution assumptions

Source assumptions (verified in §2.2 / §4):

- Decimal odds are treated as tradable price quotes; the return is the proportional change of the selected quote between entry and exit.
- **No transaction fees, no bid-ask spread, no commission, no queue priority, no partial execution, no lay liability, no settlement-at-resolution cash flows** are modeled — the source states the representation "does not reproduce the complete cash flows of matched back and lay bets" (§2.2).
- Fill assumption: entry at the observed `O_{i,t}`, exit at the first observation where the quote differs; effectively same-observation fill at the recorded quote. The source explicitly notes the observed odds may no longer be available when an order reaches the front of the queue (§4).
- Order type, latency, partial fills/failures, borrowing/shorting mechanics of laying a candidate, leverage/margin, and capacity/participation limits: **not stated in source (data gap)** — the analysis is a quote-change abstraction, not an order-level simulation.
- Consequently the reported performance is **gross of all frictions by construction**, and the source labels it "frictionless descriptive quantities rather than executable betting-exchange profits" (abstract; §3.2.2; §4).

## Evidence

### Source-reported

All figures below trace to arXiv:2609.22639v1 and are **source-reported, not independently reproduced**. Market/universe for all of them: Betfair two-nominee U.S. presidential election odds; frictionless (no costs of any kind).

- **2024 out-of-sample, §3.2.1:** 130 points fall outside the upper one-sided prediction interval; **130 statistical signals**, none overlapping an open position, all selected quotes changed before sample end → **130 completed trades** used for performance evaluation; **empirical one-step coverage 95.1%** vs nominal 95% (slight over-coverage, i.e., slightly conservative intervals).
- **2024 out-of-sample, §3.2.2 (also stated in Abstract and §4 Conclusion):** sample mean realized **odds-price return +1.86%** per trade and **unannualized per-trade Sharpe-type ratio 1.12**, under the simplified frictionless representation. The paper is explicit that this statistic is descriptive (unequal holding periods, not annualized) and not a conventional portfolio Sharpe ratio, and that returns "measure changes in decimal odds rather than actual betting profits" (§4).
- **2020 training sample, §3.1.1:** with the full sample (including the Trump COVID-19 episode), **107 signal points**; excluding the COVID period (separately fitted analysis, explicitly not nested with the first), **201 trading signal points out of 4,135 non-flat time observations**, empirical coverage **95.2%** vs nominal 95% (Figure 3).
- **Simulation study, Appendix C.3:** 1000 replications of the data-generating process gave empirical coverage **94.8%** vs theoretical 95% (validates the filter/likelihood implementation, not trading profitability).
- **Candidate-selection model, Table 3 (2020 Bradley-Terry coefficients):** `Y_{1,t}−Y_{2,t}` estimate −0.150 (SE 0.789, z = −0.190, p = 0.849); `ΔY_{1,t}−ΔY_{2,t}` estimate 33.1 (SE 23.0, z = 1.44, p = 0.150); no intercept.
- **Parameter estimates for the two elections:** Tables 1 (2020) and 2 (2024); **diagnostics:** Appendix E / §3.2.3 (Q-Q and ACF, Figures 9–10).

### Independently reproduced

not independently reproduced

### Negative evidence

- **Frictionless by construction (source-admitted):** no fees, spreads, commission, queue priority, lay liability, or execution risk; the authors state the numbers are not executable betting-exchange profits and that transaction fees "should also be considered" in future work (Abstract, §2.2, §4). Expected direction: costs strictly reduce the +1.86% per-trade mean; magnitude not testable from the paper alone — **data gap**.
- **Selection leg statistically unsupported in-sample:** neither Bradley-Terry coefficient is significant at conventional levels (Table 3: p = 0.849 and p = 0.150) — the model that chooses which nominee's quote to back has no significant predictors in the 2020 fit (source-reported table, interpreted here as negative evidence).
- **Residual misspecification:** standardized residuals of the trending-OU model show systematic departure from normality and substantial negative autocorrelation at lag 1 / positive at lag 2 outside approximate 95% bounds (§3.2.3, Appendix E); the Gaussian assumption "does not fully describe" the residual distribution, so prediction-interval coverage and hence signal frequency may be miscalibrated in other samples.
- **Extreme-event sensitivity:** the 2–6 October 2020 Trump COVID-19 episode produced a visible flat regime and a sharp probability drop; signal counts change drastically (107 vs 201) between separately fitted analyses, and the paper offers two ad-hoc strategies for handling such events (§3.1.1) — the rule is not robustly specified for shocks.
- **Single out-of-sample event:** one election pair (2024) for out-of-sample evaluation; no cross-market, cross-country, or multi-cycle replication (§1.1, §3.2).
- **Exit-rule dependence:** results use an event-driven exit with variable holding periods; the paper itself calls for sensitivity analysis against fixed-horizon exits, and notes changing the interval from 95% to 99% would change betting decisions (§4).
- **Missing-data assumption:** MCAR may be restrictive if missingness coincides with high-activity or disruption periods (§4).
- None identified in the reviewed external literature for this specific construction; absence is not evidence of no negative result.

## Falsification plan

Items not marked source-specified are **research-proposed**; all acceptance/failure cutoffs are **research-defined falsification thresholds**.

1. **Point-in-time / leakage audit (source-specified inputs, research-defined check):** rebuild `Z_t`, the de-flattened history, and the bootstrap bound strictly from information available at `t`; fail if any retained observation or bound uses post-`t` data, or if nominee/market selection rules depend on post-nomination information beyond the source's stated 23 Aug start.
2. **Honest out-of-sample extension (research-proposed):** re-run the frozen 2020-trained `β` + rolling-bound procedure on the next two-candidate electoral market (e.g., 2028 U.S. or another two-dominant-outcome election) with α = 0.05 fixed. **Fail if** the mean per-trade odds-price return over ≥100 completed trades is ≤ 0 (research-defined), or if empirical one-step coverage falls outside 93–97% (research-defined), indicating the signal process itself is broken.
3. **Cost stress (research-proposed):** recompute returns net of (a) a half-spread measured from the best back/lay quotes at each signal time and (b) exchange commission scenarios of 0% / 2% / 5% of net winnings (source models none of these). **Fail if** net mean per-trade return ≤ 0 or net per-trade Sharpe-type ratio < 0.5 (research-defined) under the mid scenario.
4. **Selection ablation (research-proposed):** compare the Bradley-Terry selector against (i) random candidate, (ii) always back the higher-implied-probability nominee, (iii) always back the lower-implied-probability nominee. **Fail the selection leg if** BT is not better than the best simple rule on a paired per-trade basis (research-defined), consistent with the already-insignificant Table 3 coefficients.
5. **Placebo / timing test (research-proposed):** randomize signal timestamps within the sample (preserving trade count) and run the mirrored rule (enter when `Z_t` falls below the lower bound). **Fail if** the real signal's mean per-trade return does not exceed the placebo distribution's 95th percentile (research-defined).
6. **Parameter perturbation (research-proposed):** α ∈ {0.01, 0.05, 0.10}; exits ∈ {first quote change (source), 1h, 6h, 24h fixed horizon}; de-flatten on/off. Report return/coverage/turnover sensitivity; material sign flips across these perturbations count as failure of robustness (research-defined "material" = sign flip or >50% mean-return decay).
7. **Regime / event breakdown (research-proposed):** split results by high-news vs quiet windows (debates, nominations, late campaign) and exclude ad-hoc shock windows only as a reported sensitivity, never as the headline. **Fail** if the edge is entirely concentrated in one excluded-in/out shock episode (research-defined).
8. **Competing explanation / capacity (research-proposed):** check whether returns survive conditioning on book depth; if the strategy's profits require fills deeper than the top-of-book available at signal time, mark non-implementable (research-defined).
9. **Action on failure:** record the negative result against this artifact; do not promote to implementation or candidate pool; no retuning of α/thresholds to rescue the result without a new pre-registered record.

## Crypto portability

**adapted** — not `direct`. The source demonstrates the mechanism only in political betting-exchange markets (Betfair, two-candidate U.S. elections); it provides **no crypto evidence**. Porting hypotheses (all research-proposed):

- Closest crypto analogue: two-dominant-outcome crypto event contracts (e.g., Kalshi/Polymarket BTC price-threshold or "up/down this week" binaries where two outcomes dominate), where a combined implied-probability sum and a mean-reverting over-round can be constructed analogously.
- Mechanisms that do **not** port directly: spot/perpetual directional trading (no two-outcome sum), cross-sectional funding/basis strategies (different signal family).
- Crypto-specific risks: thinner two-sided books and wider spreads on event contracts; oracle/resolution risk and "resolution vs settlement" distinctions; back/lay versus CLOB long/short mechanics and short-side availability; 24/7 continuous markets remove the scheduled-session structure the 5-minute grid assumes; stablecoin collateral and venue/custody risk; payment-for-flow dynamics differ from Betfair commission.
- Verdict: mechanism is a **ported hypothesis** for crypto prediction markets and **unproven** for crypto spot/perpetual markets.

## Limitations

- **Frictionless performance:** all reported returns/Sharpe exclude every trading cost; not executable P&L (source-admitted).
- **underspecified:** numeric bootstrap replicate count `B`; timezone; quote/tick convention (mid vs last vs available back/lay); exact Betfair market identifiers; sizing/leverage/risk rules; capacity and liquidity at signal times.
- **data gap:** peer-review status; commission/spread magnitude in the sample; holding-period distribution of the 130 trades (per-trade results are aggregated; individual trade returns, win rate, max drawdown, and turnover are **not stated in source**).
- **not independently reproduced.**
- **unproven** outside one out-of-sample election; two-candidate limitation acknowledged by the source (multi-party settings need a basket formulation).
- MCAR missingness and residual non-normality/autocorrelation weaken interval calibration guarantees.
- Dependence on paid Betdata archive (mirrored in the authors' GitHub repository) is a reproducibility dependency on third-party data licensing.
- Publication-bias concern: a single positive out-of-sample case study is weak evidence for durability; the paper itself is framed as a proof of concept.

## Implementation status

`implementation_status: not-implemented`. No implementation, backtest, or paper run exists in our research stack for this record. The authors' R code and data repository (https://github.com/lhy199661/2024-US-Election) has been located but **not executed or verified** by us. No Qlib/Paper/Testnet/Live stage has occurred or is implied.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this record does not mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet, or live trading. Any adoption/implementation decision is a separate, explicit, later review.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` — canonical strategy-research schema used for this record.
- Adjacent **repository** records (distinct source identities and mechanisms; none duplicates this capture):
  - `polymarket-binary-mean-reversion-cost-sensitivity-2026-09-14.md` — mean reversion in crypto binary contracts, different venue, signal, and cost focus.
  - `polymarket-favorite-longshot-bias-crypto-politics-2026-09-14.md` — political prediction-market bias, pricing-bias mechanism rather than OU pairs timing.
  - `kalshi-btc-event-contract-spot-hedge-2026-09-15.md` — Kalshi BTC event contracts used as hedging options, not pairs signals.
  - `kalshi-prediction-market-pricing-wedge-executable-spread-falsification-2026-09-13.md` — executable-spread wedge testing, cross-price style rather than statistical-arb timing.
  - `ou-first-passage-time-bands-fdr-stability-portfolio-stat-arb-2026-09-12.md` — OU pairs-trading bands in securities markets (different universe and signal construction).
  - `tether-pairs-trading-fdr-kalman-half-life-net-beta-2026-09-12.md` — cointegration/FDR pairs framework for liquid crypto pairs (different universe and mechanism).
  - `exploratory-reinforcement-learning-sequential-optimal-stopping-pairs-trading-2026-09-05.md` — RL optimal-stopping pairs trading on simulated OU spreads.

## Sources

1. Haoyu Liu, Len Thomas, Benjamin Baer, Carl Donovan. "Adapting Pairs Trading to Gambling Markets: A Case Study of the U.S. Presidential Election." arXiv:2609.22639v1 [stat.AP, q-fin.ST], submitted 18 September 2026. https://arxiv.org/abs/2609.22639 — landing page (authors, version, subjects, comments) and v1 full text https://arxiv.org/html/2609.22639v1 (§1.1 Data and study design; §2.2 Betting strategy; §2.2.1 When to place a bet; §2.2.2 Which bet to place; §3.1–3.2 case study; §3.2.2 Model evaluation; §4 Conclusion and limitations; Tables 1–3; Figures 1–4, 8–10; Appendices C–E) read directly on 2026-09-22 for every field in this record.
2. Authors' code and data repository: https://github.com/lhy199661/2024-US-Election (cited in the paper's data-availability statement; contains Betfair 2020/2024 election data purchased from BetData). Not executed for this record.
