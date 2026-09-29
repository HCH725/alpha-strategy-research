---
schema: strategy-research-record-v1
title: "Shadow Before Swap (SBS): Forward-Gated Model Replacement for Binance Perpetual-Futures Forecast Serving"
created: 2026-09-29
updated: 2026-09-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-07-30
sources:
  - https://arxiv.org/abs/2607.28577
  - https://arxiv.org/html/2607.28577v1
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Section 5.1 prints a simultaneous 95% lower endpoint of 0.1160% for the 48-week calendar contrast, while Table 1 prints a pointwise 95% lower endpoint of 0.1139% for that same contrast; the simultaneous band is narrower than the pointwise band at the lower end for one of three contrasts while being wider for the other two, and all three simultaneous lower endpoints sit exactly 0.0312 below their point estimate. The source does not reconcile the two interval constructions."
  - "Section 4.2 states without qualification that 'Two weeks has the lowest observed NLL', but the Figure 2c values printed in the same paragraph give the blind comparator its best cell at one week (0.1036% against 0.0751% at two weeks and 0.0899% at three weeks), so the statement holds only for the calendar and maintenance comparators."
  - "Section 4.4 prints cadence-axis calendar contrasts of 0.1195%, 0.0997% and 0.0580% at two, four and eight weeks, while Section 4.2 prints a two-week trial-duration calendar contrast of 0.1760% for the 26-week episode; the source never states which configuration differs between the two two-week cells, never identifies the episode or weighting behind the cadence-axis numbers, and prints no intervals for them."
---

# Shadow Before Swap (SBS): Forward-Gated Model Replacement for Binance Perpetual-Futures Forecast Serving

## Provenance

Primary source identity. Title as printed: "Train Often, Deploy Selectively: Forward-Gated Model Replacement in Crypto Markets". arXiv identifier arXiv:2607.28577. Complete author list exactly as the source: one author, Aditya Dutta; affiliation printed as "Emory University, Atlanta, Georgia, USA"; printed email aditya.dutta@emory.edu; no co-authors on the abstract page or in the rendered HTML author block; no ORCID printed, so identifiers stay `data gap`.

Pinned landing page. `https://arxiv.org/abs/2607.28577` fetched 2026-09-29, HTTP 200, 41,398 bytes, SHA-256 `3270caa8c841a8a948b16b8bcf2b8aa0695f865c0921d68cf4d2269c3dbc66eb`. Dateline `[Submitted on 30 Jul 2026]`. Submission history `[v1] Thu, 30 Jul 2026 17:38:45 UTC (291 KB)` and no later version, so the version/date is v1, 30 July 2026. Subject cells read `Computational Engineering, Finance, and Science (cs.CE) ; Trading and Market Microstructure (q-fin.TR)` with cs.CE primary as printed in the HTML dateline `arXiv:2607.28577v1 [cs.CE] 30 Jul 2026`; this is a two-cell listing, not a single subject, and there is no separate cross-list line. No Comments cell, no journal-ref cell and no DOI cell are present on the landing page, so publication status beyond arXiv preprint is `not stated in source`. Licence cell reads `License: arXiv.org perpetual non-exclusive license`, therefore only short printed values, table cells and section references are normalised here.

Pinned full text. `https://arxiv.org/html/2607.28577v1` fetched 2026-09-29, HTTP 200, 185,795 bytes, SHA-256 `647261a3ddd6028adbdcd0be36c5b9eaf0abbf8d2f85d9d3251d3bfb7d5d4b31`, converted to 51,746 characters over 941 lines with a local tag stripper and read end to end on 2026-09-29, covering the Abstract, Sections 1 through 7, Tables 1 to 4, the captions of Figures 1 to 5, and the 34-entry reference list. The PDF was not downloaded, so PDF bytes and checksum stay `data gap`.

Artifact provenance. The paper refers to a "versioned repository" in Section 3.1 and to "Repository configuration and run manifests" that "make the lock reproducible", but no repository URL, owner, commit SHA or path is printed anywhere in the pinned text; `data availability` occurs 0 times and every `github` occurrence is either arXiv interface chrome or the third-party Binance Public Data reference. Public code, commit, and runnable artifact therefore stay `data gap`, and no immutable commit can be cited. The only external data artefact named is Binance Public Data (reference entry "Binance (n.d)", noted as a GitHub repository, "Accessed July 19, 2026").

Deduplication. Deterministic source-identity search was run with `rg -uuu` across the entire checkout including hidden directories, `.git`, worktrees, skill directories and `coverage_manifest.csv` (1,088,787 bytes) before writing, for each of `2607.28577`, `Shadow Before Swap`, `Aditya Dutta`, `emory.edu`, `forward-gated`, `warm-refit`, `delayed-label`, `paired negative-log-likelihood`, `champion-challenger` and `champion-challenger` with an en dash: every one returned 0 files, and `coverage_manifest.csv` returned 0 matches for both `2607.28577` and `Shadow Before Swap`. Positive control `novy-marx` run as `rg -uuu -l -i --glob '!.git/**' -e novy-marx` returned 34 files before writing and 35 after, the sole increment being this record's own dedup sentence (the same probe with `.git` included and case-sensitivity on returns 38 and 29 respectively, which is why the command form is pinned here). `git log --oneline -20` was used only as a convenience glance and does not by itself satisfy dedup. The same source identity therefore did not previously exist in the repository, so no same-source material-distinction argument is required.

Schema resolution. `quant/strategy-research-record-spec-v2.md` was requested from Wiki Brain first and returned file not found, so this run failed closed onto `quant/strategy-research-record-spec-v1.md`, canonical at 10,289 bytes, SHA-256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`. README.md (575 lines) was read in full on this run.

## Economic mechanism

### Source-reported

The source frames its contribution as a deployment policy, not a forecasting architecture and not a return premium. Its stated question is whether a newly trained model state has earned authority to replace a state that has kept adapting during fitting, because "the selected state becomes the parent of the next refit" and "model replacement is therefore a sequential control problem, even when the underlying learner and release cadence are fixed". Shadow Before Swap (SBS) deep-copies the complete incumbent (representation, prediction head, causal normalizer, delayed-label queue and online optimizer), warm-fits the clone on history mature at the scheduled boundary, advances challenger and incumbent independently over the same next week on the same market tape, and promotes only if the mean paired loss differential on the matured trial labels is at least a fixed deadband tau = 1e-4. The continuously maintained incumbent is the deployment null; a schedule-matched "blind" policy trains and shadows the same challengers but always promotes, isolating the value of trial evidence from the value of waiting. The source is explicit that "the contribution is a deployment policy rather than a forecasting architecture" and that its estimand is "deployment quality measured by probabilistic forecasting performance and state turnover".

### Research interpretation

Hypothesis in falsifiable terms: under nonstationary limit-order-book inputs, scheduled refits of a served forecaster contain a materially damaging tail; requiring one forward week of paired, delayed-label evidence before authorising a state swap removes enough of that tail to lower the served probabilistic loss while cutting deployed-state churn, and the surviving accepted refits still add value over a never-refitting incumbent. The word `alpha` occurs 0 times in the pinned text, and the source prints no return, Sharpe, CAGR, drawdown or PnL figure anywhere, so this record must be read as a forecast-quality and release-governance hypothesis, not as an excess-return hypothesis.

Component roles, as the source defines them:

- Regime / baseline state: the continuously maintained incumbent, updated online with matured labels and refreshed causal normalizer moments.
- Candidate generator: a warm refit on the preceding 28 calendar days with a function-preserving reparameterisation, trained off the serving path.
- Confirmation gate: a one-week off-path paired trial scored on delayed labels, promoting only when the paired NLL advantage clears tau = 1e-4.
- Risk / exit: rejection discards the challenger in full; the serving path, latency and retraining cadence are unchanged; the accepted state becomes the parent of all later challengers.
- Comparators that decompose the claim: maintenance isolates "never refit", blind isolates "wait but always swap", calendar isolates "swap immediately on schedule".

Do not assume every component contributes alpha-like value; the paper itself reports that the Temporal-CNN candidate generator supplies almost no deployable refits, so the gate there is pure downside protection, and the delay axis is separately identified by the calendar-versus-blind gap.

## Signal

Formation timestamp and tradability. Decisions are taken on a 30-second UTC cadence. Each input is the most recent 60 snapshots (a 30-minute lookback at 30-second spacing) of ten-band depth. The label is the 300-second future transaction-price return, classified down / neutral / up against a fixed five-basis-point neutral band; it matures 300 seconds after the prediction. Reference prices use only the latest completed official one-minute futures close available at prediction time. Prediction precedes use of the current label, following prequential and delayed-online-learning conventions.

Forecaster. Each snapshot is projected to 24 channels, temporal mean / final / maximum features are pooled, a second 24-unit layer follows, then a linear three-class head. Layer-local Forward-Forward training fits the representation; matured labels supervise the head. All policies refresh causal normalizer moments from current unlabeled inputs at rate 0.01; head updates use plain SGD at 3e-4.

Warm refit. Preceding 28 calendar days, 21 for training and 7 for validation, with at least 14 source days. Fresh normalizer; function-preserving reparameterisation W' = W diag(sigma'/sigma) and b' = b + W((mu' - mu)/sigma); fresh Adam at 1e-3, batch size 128, at most 50 epochs, validation-NLL patience 3.

Gate rule as printed. Challenger C_b is cloned from incumbent I_b at action block b and fitted only on history mature at the training boundary; both states then advance on the same trial stream; at decision time d_b the paired mean differential v_hat = mean over matured trial examples of [loss(incumbent) - loss(challenger)]; promote when 1{v_hat >= tau} with tau = 1e-4. Positive v_hat means lower challenger NLL. The threshold is applied to the paired trial mean of one contract-underlying-seed state before any cross-asset or cross-contract aggregation.

Causal ordering that must be preserved. At each scheduled boundary the incumbent first processes every label whose availability time has passed; only then is the challenger cloned and fitted on examples mature at that boundary; neither branch may use a trial label before its 300-second delay expires; the gate is evaluated only after all eligible trial labels have matured. Branches share the exogenous tape but not mutable state; a rejected challenger is discarded in full; an accepted challenger contributes fitted parameters, normalizer and accumulated trial updates and becomes the parent of later challengers.

Comparators. Maintenance applies the maintenance operator but never full-refits. Calendar warm-refits and serves immediately at each boundary. Blind follows the SBS training and trial schedule but always promotes. SBS promotes only under the gate.

Parameters and their source status. Source-reported and frozen: one-week trial, tau = 1e-4 ("development-selected and frozen", described as an operational deadband equal to about 0.009% of baseline weekly NLL, explicitly "a conservative release tolerance, not an estimate of a universal market constant"), policy family, aggregation order, matured-label scoring and temporal-block analysis. Source-reported sensitivity grid: tau in {0, 1e-4, 2.5e-4, 5e-4} and trial durations of one, two and three weeks. Source-reported fixed design values: 30-second grid, 60 snapshots, 40 depth-band features, 300-second horizon, five-basis-point band, 300-second label delay, 24 channels, 28-day refit window, 1e-3 / 128 / 50 / patience-3 refit hyperparameters, normalizer rate 0.01, head SGD 3e-4. No Scout-invented entry, exit, stop, sizing or threshold rule is added anywhere in this record.

Underspecified in the source. The exact four per-band depth fields behind "40 depth-band features" are not fully enumerated (only three economic features are named: log base quantity, log USD notional, within-side depth shares); depth-band edges are not printed; the scheduled-boundary cadence of the canonical replay is not printed as a number (the paper states SBS "does not change the existing retraining cadence" and tests two, four and eight week cadences only as a secondary axis); the exact start and end dates of the March-June 2024 twenty-asset panel are not printed, only "14-week"; the three evaluation seed identities are not printed (only development "seed 0" is named); how missing registered days enter the equal-weight aggregation is described but not formulas; the episode and weighting behind the Section 4.4 cadence-axis numbers are not printed; mean local hindsight regret in Figure 3b has no printed numeric value. The rule is therefore reproducible in structure but `underspecified` for byte-identical reconstruction from text alone.

## Required data

- Instrument: Binance USD-margined and coin-margined perpetual futures contracts for BTC, ETH, BNB, XRP, SOL, DOGE, ADA and BCH (eight underlyings), two contract types on one exchange, explicitly "not independent venues".
- Venue and market type: Binance futures, perpetual, USD-M and COIN-M; secondary one-action screen on Coinbase with different preprocessing.
- Timeframe and fields: aggregate depth observations complete across ten bands, snapped to a 30-second UTC grid and deduplicated; contract sizes from hashed exchange metadata; official one-minute futures closes; transaction price for labelling. Input shape 60 snapshots x 40 depth-band features.
- Point-in-time: label availability time with a fixed 300-second delay; training uses only examples mature at the boundary; no 60-snapshot input or 300-second target window may cross a data gap.
- Missing data: a day must contain at least 95% of its 2,880 scheduled observations; one isolated missing grid step may be causally forward-filled; longer gaps remain discontinuities; missing registered days are omitted consistently from every policy state. No imputation beyond that single forward-fill is specified.
- Scale actually used: 6,319,220 scored examples in the 22-week episode (class shares 34.75 / 30.88 / 34.37 down / neutral / up), 6,789,702 in the 26-week episode (33.29 / 33.97 / 32.74), 5,536,506 in the twenty-asset panel (35.97 / 27.98 / 36.05), and 55,367 in the Coinbase screen (41.17 / 16.84 / 41.98).
- Not required by the source for its own estimand: funding, open interest, trades and aggressor side, borrow, options surface, on-chain data. A word-boundary census of the pinned HTML returns funding-rate 0, open-interest 0 occurrences in the body, and the single `funding` hit is arXiv page furniture ("Major funding support"), not paper content.

## Execution assumptions

The source's "execution" is model-state deployment, not order execution. Deployment-side costs are the ones it prints, in Table 3: challenger inference costs one bounded shadow pass; storage costs one versioned challenger state; decision latency costs one forward-trial week; online serving leaves the incumbent path unchanged; the principal operational charge is the deliberate one-week decision delay. The paper states SBS "does not increase online inference latency or change the existing retraining cadence".

Trading-side assumptions are absent by declaration rather than by omission. A word-boundary census over the pinned HTML text returns 0 occurrences for transaction cost, fee, fees, commission, slippage, spread, bid-ask, maker, taker, fill model, market order, borrow, leverage, margin call, liquidation, participation, position sizing, Sharpe, Sharpe ratio, CAGR, drawdown, PnL, backtest, win rate, execution, cost of trading and `alpha`; the three `transaction` hits are "transaction-price return" in Section 3.2 and two "IEEE Transactions" reference titles; `limit order` and `order book` appear only in reference titles and Section 6 literature discussion; `turnover` (4) and `capacity` (1) and `latency` (3) all refer to model-state turnover, a capacity-matched network and serving latency respectively. The only market-impact sentence is Section 4.4's own scope statement: "Converting them into executable profit is a separate strategy-level estimand requiring prespecified trading costs, fills, and market impact." Accordingly, order type, fill model, signal-to-order delay, in-market latency, bid-ask spread, slippage, market impact, participation, capacity, funding, leverage, margin, liquidation, borrow and partial fills are `not modelled and explicitly declared out of scope by the source`; any monetary figure derived from this record would be `data gap`, never zero, and any choice of order type, fill model or cost ladder added later must be labelled research-proposed.

## Evidence

### Source-reported

All figures below are third-party claims from the pinned arXiv v1 text, `not independently reproduced`, with Table or Section provenance. They are forecast-score and operational figures, never returns.

Table 1, canonical SBS effects, relative NLL reduction in percent with pointwise 95% four-week circular moving-block intervals: 22-week episode calendar 0.1157 [0.0676, 0.1573], blind 0.0423 [0.0146, 0.0689], maintenance 0.0379 [0.0242, 0.0533]; 26-week episode calendar 0.1738 [0.1265, 0.2103], blind 0.1036 [0.0673, 0.1380], maintenance 0.0470 [0.0263, 0.0671]; 48-week pooled calendar 0.1472 [0.1139, 0.1754], blind 0.0755 [0.0521, 0.0980], maintenance 0.0428 [0.0301, 0.0554]. Section 4.1 adds absolute NLL reductions per forecast of 0.001567, 0.000803 and 0.000455 for the same three contrasts.

Table 2, full promotion-margin sensitivity, promotions/rejections and calendar / blind / maintenance relative NLL reduction with pointwise four-week intervals: 22 weeks at tau 0 gives 56/184 and 0.1174 [0.0693, 0.1591], 0.0441 [0.0165, 0.0704], 0.0397 [0.0258, 0.0548]; at tau 1e-4 gives 50/190 and 0.1157 [0.0676, 0.1573], 0.0423 [0.0146, 0.0689], 0.0379 [0.0242, 0.0533]; at tau 2.5e-4 gives 47/193 and 0.1155 [0.0662, 0.1589], 0.0421 [0.0110, 0.0712], 0.0377 [0.0224, 0.0553]; at tau 5e-4 gives 42/198 and 0.1135 [0.0650, 0.1562], 0.0401 [0.0093, 0.0685], 0.0357 [0.0213, 0.0520]. 26 weeks at tau 0 gives 66/222 and 0.1742 [0.1266, 0.2113], 0.1039 [0.0671, 0.1388], 0.0473 [0.0266, 0.0680]; at tau 1e-4 gives 64/224 and 0.1738 [0.1265, 0.2103], 0.1036 [0.0673, 0.1380], 0.0470 [0.0263, 0.0671]; at tau 2.5e-4 gives 59/229 and 0.1701 [0.1235, 0.2064], 0.0998 [0.0641, 0.1342], 0.0432 [0.0233, 0.0624]; at tau 5e-4 gives 55/233 and 0.1705 [0.1241, 0.2069], 0.1002 [0.0645, 0.1351], 0.0436 [0.0242, 0.0623].

Section 4.1 operational and distributional claims: 114 promotions among 528 proposals (21.6% acceptance), 414 avoided state changes, deployed-state turnover reduced by 78.4%; all 18 episode-seed-comparator effects positive; worst weekly relative differences (22-week / 26-week) of -0.0232 / 0.0000 versus calendar, -0.0354 / -0.0593 versus blind, -0.0080 / -0.0184 versus maintenance; favourable weeks 17/22 and 22/26 versus calendar, 13/22 and 21/26 versus blind, 17/22 and 21/26 versus maintenance; positive weekly medians for every comparator in both episodes; about 455 total log-loss units per million predictions versus maintenance; roughly 200 additional correct high-confidence decisions per million opportunities at matched 5% coverage in the 22-week episode versus calendar.

Section 4.2 duration axis for the 26-week episode, one / two / three-week trials: calendar 0.1738 / 0.1760 / 0.1683, blind 0.1036 / 0.0751 / 0.0899, maintenance 0.0470 / 0.0491 / 0.0414, with all corresponding pointwise four-week intervals printed only inside Figure 2c.

Section 4.3 mechanism diagnostics on the canonical 26-week episode's 288 mature challenger decisions: Spearman association 0.524 between paired trial gain and value over the next three mature weeks, 74.0% sign agreement, and mean local hindsight regret reported only graphically.

Section 4.4 breadth, transfer and safety: the earlier 14-week twenty-asset USD-M panel gives 0.0821 [0.0427, 0.1170] versus calendar, 0.0458 [0.0121, 0.0940] versus blind, 0.0270 [0.0044, 0.0515] versus maintenance; a topology-matched cross-entropy challenger gives 0.0757 / 0.0508 / 0.0195 with no intervals printed; the cadence axis gives 0.1195 / 0.0997 / 0.0580 versus automatic calendar replacement at two, four and eight weeks with no intervals printed; the Temporal-CNN stress case gives NLL 12.6506 for calendar, 15.8667 for blind, 1.07117 for maintenance and 1.07141 for SBS with 236 of 240 proposals rejected and a -0.0221% maintenance contrast; a matched-coverage Brier comparison in the 22-week episode gives reductions of 0.000678 versus calendar, 0.000370 versus blind and 0.000274 versus maintenance.

Section 5.1 inference: simultaneous 95% lower endpoints for the three pooled contrasts of 0.1160%, 0.0443% and 0.0116%; the inferential sample is 48 aggregate UTC weeks; 10,000 deterministic circular moving-block resamples with four-week blocks, with two-, six- and eight-week blocks, stationary bootstrap, Newey-West lag-four intervals, contract exclusions and leave-one-asset-out as sensitivities; equal decision-budget aggregation (seeds averaged within stream-week, underlyings equally within contract type, contract types equally within UTC week, weeks equally over time); fixed 22/48 and 26/48 pooling weights that reproduce the printed pooled cells (0.1157 x 22/48 + 0.1738 x 26/48 = 0.1472, and likewise 0.0755 and 0.0428).

Section 3.1 evidence chronology: rule development on 26 UTC weeks from 3 February through 3 August 2025 with seed 0; first out-of-time episode 4 August 2025 through 4 January 2026 (22 weeks); second nonoverlapping episode 5 January through 5 July 2026 (26 weeks), classified by the source as a "retrospective historical robustness episode"; earlier March-June 2024 twenty-asset panel; objective, cadence, Temporal-CNN and Coinbase analyses labelled secondary stress tests; the source states it uses the term "development-selected and frozen" and does "not claim[] independent preregistration".

Table 3 deployment footprint and Table 4 positioning versus test-time adaptation, continual learning, model selection and canary release are operational statements, not performance claims.

### Independently reproduced

not independently reproduced

No backtest, replay, forecast recomputation or market-data retrieval was performed in this run. The only independent work is arithmetic and provenance checking of the printed values against the pinned text.

### Negative evidence

1. No trading economics exist in the source: Sharpe, Sharpe ratio, CAGR, drawdown, PnL, win rate and backtest each occur 0 times, and `alpha` occurs 0 times, so nothing in the record is evidence of tradable excess return.
2. The source itself declares trading costs, fills and market impact a separate future estimand, so the headline forecast gains are gross of every friction by construction.
3. Absolute effect size against the strongest baseline is 0.000455 NLL per forecast (0.0428% relative), which the paper translates into 455 log-loss units per million predictions, a service-scale rather than economic magnitude.
4. In the Temporal-CNN failure-containment stress case SBS is worse than maintenance (-0.0221%), i.e. the gate does not improve a healthy serving trajectory there and only prevents catastrophe (NLL 1.07141 against 1.07117).
5. Weekly reversals are real: worst weekly differences of -0.0354% and -0.0593% versus blind, -0.0080% and -0.0184% versus maintenance, and only 13 of 22 weeks favour SBS over blind in the first episode (59.1%).
6. The gate is an imperfect predictor: paired trial gain has Spearman 0.524 and 74.0% sign agreement with next-three-week value, and hindsight regret has no printed number.
7. Breadth is thin: two nonoverlapping episodes on one exchange, two contract types explicitly "not independent venues", 48 inferential weeks, three seeds, one incumbent maintenance mechanism.
8. The source concedes that its block intervals "target temporal robustness of the realized recursive trajectories" only and that "Counterfactual-history uncertainty requires independent episodes or a validated market simulator".
9. Selection was development-driven on 26 weeks with seed 0 and frozen, not independently preregistered, and the second episode is described as a retrospective robustness episode whose recursive outcomes had previously been "unopened".
10. No hypothesis-test infrastructure: p-value, t-statistic, Benjamini, FDR, false discovery, multiple testing, placebo, walk-forward and out-of-sample each occur 0 times; only block-bootstrap intervals are reported.
11. The headline threshold is not identified by the data: effects are near-flat across tau from 0 to 5e-4 (calendar 0.1174 to 0.1135 in the 22-week episode), so the 1e-4 choice is a convention rather than an estimate.
12. Effect magnitude depends on comparator: 0.1472% versus calendar bundles waiting plus authorisation, 0.0755% versus blind is the clean authorisation contrast, and only 0.0428% remains versus maintenance.
13. The cadence axis decays with longer cadences (0.1195 / 0.0997 / 0.0580) and is printed without intervals, episode identification or a stated baseline cadence.
14. The two-week cell differs between the trial-duration axis (0.1760%) and the cadence axis (0.1195%) with no printed reconciliation, so one of the two two-week configurations is not recoverable.
15. No public artefact: the versioned repository is unnamed, no commit exists to pin, `data availability` occurs 0 times, and every outcome depends on replaying code the reader cannot see.
16. No prospective live deployment: Section 5.4 lists "prospective live deployment with frozen economic weights and explicit release costs" as future work.
17. The Coinbase transport screen is small (55,367 examples), one-action, and uses a different label construction (midpoint returns instead of minute-close returns), so it does not transport the recursive policy result.
18. Coinbase class shares sum to 99.99% rather than 100.00%, a rounding-scale discrepancy the source does not comment on.
19. The three comparator contrasts are not independent of one another because they share the same SBS trajectory, so the three intervals cannot be read as three separate discoveries.
20. Section 5.1's simultaneous lower endpoint for the calendar contrast (0.1160%) exceeds Table 1's pointwise lower endpoint (0.1139%) for that same contrast, an interval construction the source does not reconcile.

## Falsification plan

Everything numeric below is a `research-defined falsification threshold` chosen by this Scout, not by the source. Failure action in every case is the same: record the mechanism as unproven for our purposes, keep `adoption: not-approved`, and do not retune tau, trial length, panel composition, episode weighting or aggregation order after seeing the outcome.

- F1 (printed-value reproduction, tolerance research-defined): reconstruct Table 1 and Table 2 from a replay of the frozen configuration; fail if any relative NLL cell differs from the printed value by more than 0.0001 percentage points.
- F2 (artifact gate, currently failing): a public repository with a full commit SHA, run manifests and per-week sufficient statistics must exist and be re-executable; fail while no URL is printed.
- F3 (independent-venue gate): repeat the complete recursive replay on a genuinely separate exchange and data vendor; fail if the 48-week pooled maintenance contrast is not strictly positive there.
- F4 (prospective gate): freeze the rule and run forward on live data for 26 weeks; fail if the four-week block 95% lower endpoint of the maintenance contrast is <= 0.
- F5 (trading-economics gate): attach a pre-specified decision rule from the three-class forecast to positions plus a cost ladder of fees, spread, slippage at 0 / 1 / 2 / 5 / 10 bps and funding; fail if the SBS-served signal's net performance is not strictly better than the calendar-served signal over the same window; any position rule added here is research-proposed.
- F6 (ablation for attribution): compare full SBS against gate-only-always-refit, refit-only-always-promote and maintenance; fail if the authorisation contrast (full SBS minus always-promote under the same schedule) is <= 0, because that is the only cell that isolates the gate from the waiting.
- F7 (placebo): sign-flip the paired differentials for 10,000 draws under the same aggregation; fail if the observed authorisation contrast does not exceed the 95th percentile of the placebo distribution.
- F8 (multiplicity): form the family of 3 comparators x 4 margins x 3 durations x 2 episodes = 72 cells, run a paired weekly loss-differential test per cell, apply Benjamini-Hochberg at q < 0.10 across the whole family, and fail if the maintenance contrast does not survive.
- F9 (gate-activity check): require that the promotion rate moves by at least 20% relative across tau in [0, 5e-4]; fail if the rate is essentially invariant, which would mean the deadband axis is inert and cannot support any threshold claim.
- F10 (venue-independence check): treat USD-M and COIN-M as one venue as the source itself instructs; fail any breadth claim that still rests on a single exchange.
- F11 (capacity, research-proposed, only if F5 passes): cap positions at 20% of 20-day median traded volume and fail if the effect vanishes under that cap.
- F12 (live serving gate): 26 weeks of prospective production serving with frozen weights and frozen tau; fail if the served NLL advantage over maintenance is non-positive in at least 2 of 3 months.

## Crypto portability

`direct` for the mechanism as evaluated: the source runs natively on Binance USD-M and COIN-M perpetual futures over a 24/7 thirty-second UTC grid, so no porting step is required to state the forecast-quality claim inside crypto markets.

Portability risks that remain open:

- Spot versus perpetual: irrelevant to the printed estimand (no position is ever taken) but decisive for any F5 extension, because a position on a perpetual carries funding that this paper never models (funding-rate 0 occurrences).
- Funding, mark and index price: labels use transaction price and reference prices use the official one-minute close; neither is mark or index price, so a trading port must restate the label against the venue's mark convention used for funding and liquidation, which is `underspecified` here.
- Venue fragmentation: USD-M and COIN-M on one exchange are explicitly "not independent venues"; a cross-venue claim is `unproven`.
- Leverage, margin and liquidation: 0 occurrences, so any leveraged port is `data gap`.
- Custody, withdrawal, stablecoin and quote-currency effects: not addressed by the source, `data gap`.
- Candle and timestamp boundaries: 30-second UTC grid, 300-second label horizon, 30-minute input window; all boundaries are causal as printed, which is the main reason the mechanism is portable as stated.
- Port to non-crypto markets: `unproven`. The release-authorisation logic is venue-agnostic in principle, but every empirical number here comes from crypto perpetual futures, and no non-crypto result is printed.
- Port from forecast quality to trading profit: `unproven` and explicitly disclaimed by the source.

## Limitations

- `underspecified`: byte-identical reconstruction from text alone; per-band feature list; depth-band edges; canonical retraining cadence; twenty-asset panel dates; evaluation seed identities; episode and weighting behind the cadence-axis numbers; hindsight-regret values.
- `data gap`: PDF bytes and checksum; public code, commit SHA, run manifests and per-week sufficient statistics; any ORCID; journal, issue or peer-review status; monetary value of avoided promotions ("their monetary value remains organization specific" is the source's own wording); any statement about returns.
- `not independently reproduced`: every quantitative claim in this record is third-party, source-reported and was not recomputed by us.
- `unproven`: prospective live serving, cross-venue transport, non-crypto transport, and any translation of NLL gains into net trading performance.
- Epistemic boundary: tau = 1e-4, the one-week trial, the five-basis-point band, the 300-second horizon and every falsification cutoff above are source-reported design choices or, where marked, `research-defined` / `research-proposed`; none of them is a Scout-invented operational rule presented as source fact.
- Publication and selection risk: development on 26 weeks with a frozen rule is weaker than preregistration, and the source says so explicitly.
- The incremental-write threshold is met because no existing record in this repository covers model-lifecycle release authorisation, delayed-label champion-challenger gating, or forecast-serving churn as a mechanism; the three nearest evaluation-validity records study different objects (tuning protocols, execution semantics, or factor-mining referees), not deployment gating.

## Implementation status

`implementation_status: not-implemented`. Nothing from this record has been implemented in our research stack. No forecaster was built, no Binance or Coinbase data was downloaded, no replay was run, no dependency was installed and no third-party code was executed in this run. This research capture does not modify any engine, does not create a strategy family, and does not authorize Paper, Testnet or Live execution.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. The presence of this record means only that normalised, source-traceable research material was pushed to the public staging pool. It does not mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed any full backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. No record may promote itself by wording, evidence count, confidence or schedule behaviour.

## Related Wiki records

Read-only Wiki Brain search on this run. A query for `model retraining deployment gate champion challenger` returned 0 pages, so no page on this mechanism exists to link. A query for `crypto perpetual probabilistic forecast evaluation` returned 5 pages; the two closest adjacent pages are linked below, both verified to exist in the vault, and neither shares this record's mechanism:

- [[quant/crypto-short-horizon-predictability-purged-walk-forward-audit-2026-09-11]] - adjacent because it audits short-horizon crypto forecast evaluation; it tests predictive validity under purged walk-forward and multiple-testing control, whereas this record measures a release-authorisation policy on a served model and prints no predictive-accuracy statistic of its own.
- [[quant/cryptol-scale-balanced-multivariate-ohlc-physics-loss-2026-09-12]] - adjacent because it concerns a crypto short-horizon forecaster; it changes the architecture and loss, whereas this record holds the architecture fixed and changes only whether a refit is allowed to replace the incumbent.

The remaining three search results (probability-sorted perpetual long-short, Huesler-Reiss extremes, and foundation-transformer factor residuals) share no mechanism with this record and are deliberately not linked. No Wiki Brain page was written, and no other link was fabricated.

## Sources

- arXiv abstract page, arXiv:2607.28577v1, https://arxiv.org/abs/2607.28577 - pinned 2026-09-29 at 41,398 bytes, SHA-256 3270caa8c841a8a948b16b8bcf2b8aa0695f865c0921d68cf4d2269c3dbc66eb; source of author list, affiliation, email, dateline, submission history, subject cells, licence and the absence of Comments, journal-ref and DOI cells.
- arXiv full text (HTML), https://arxiv.org/html/2607.28577v1 - pinned 2026-09-29 at 185,795 bytes, SHA-256 647261a3ddd6028adbdcd0be36c5b9eaf0abbf8d2f85d9d3251d3bfb7d5d4b31; source of every table, section reference, parameter and quantitative claim normalised above.
- Primary data source named by the paper (not opened by this Scout): Binance Public Data, GitHub repository, noted in the reference list as accessed 19 July 2026.
