---
schema: strategy-research-record-v1
title: "Pre-Game Paired-Comparison Win Model for Professional League of Legends Maps Benchmarked Against Polymarket Per-Map Contracts"
created: 2026-09-22
updated: 2026-09-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - esports
  - prediction-markets
  - polymarket
  - paired-comparison
  - bradley-terry
  - forecasting
  - market-efficiency
status: research-only
confidence: medium
source_as_of: 2026-07-21
sources:
  - "https://arxiv.org/abs/2609.08060"
  - "https://arxiv.org/html/2609.08060v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Pre-Game Paired-Comparison Win Model for Professional League of Legends Maps Benchmarked Against Polymarket Per-Map Contracts

## Provenance

- **Paper:** Min-Ren Guan (Teahouse Finance, Taipei 105803, Taiwan; `john@teahouse.finance`) and Shen-Ning Tung (corresponding author, Department of Mathematics, National Tsing Hua University, Hsinchu, Taiwan; ORCID 0000-0002-4646-3575), "Pre-game paired-comparison modeling of professional League of Legends map outcomes."
- **Preprint:** arXiv:2609.08060v1 [stat.AP] (cross-listed q-fin.ST), submitted Mon, 7 Sep 2026 23:51:43 UTC; manuscript front-matter dated September 8, 2026; comments "26 pages, 2 figures"; license CC BY 4.0 (v1 is the only version as of capture).
- **Stable URLs:** https://arxiv.org/abs/2609.08060 ; full text https://arxiv.org/html/2609.08060v1 ; PDF https://arxiv.org/pdf/2609.08060v1
- **Publication status:** preprint. The arXiv landing page carries no journal reference and no DOI beyond the arXiv-issued identifier (DataCite registration pending; checked 2026-09-22). Peer-review status is `data gap`: Section 1 of the manuscript describes itself in one passage as "the first peer-reviewed application" of the continuous-response two-stage paired-comparison design to esports, but no journal, acceptance, or DOI is stated anywhere on the landing page — treat as unverified self-description, not as confirmed publication.
- **Funding / disclosures (source-reported):** Tung acknowledges Taiwan NSTC grant 114-2115-M-007-012-MY3, "Mathematical Foundation of Automated Market Makers"; Guan thanks Teahouse Finance for Claude credits and compute (Acknowledgements). Section 3.4 discloses that implementation code was drafted/refactored with Anthropic's Claude, reviewed and tested by the authors, who take responsibility; no modeling decision or reported result was delegated to it.
- **Data as-of:** modeling-corpus counts as of July 2026 (5,135 first-pick-complete games of 5,893 collected, Section 3.2); market comparison backtest dated **2026-07-21** (Table 7 caption) — this is the `source_as_of` value. Figure 1 and Appendix B.1 use the later August-2026 corpus (5,233 / 4,703 games) and are explicitly illustrative, not reported results.
- **Primary-source checksum (2026-09-22):** opened the arXiv landing page and the complete full-text HTML of v1 and verified there: exact author list/order and affiliations (Guan, Tung); version/date (v1, 7 Sep 2026); sample period (2024–2026, counts as of July 2026) and universe (six regional leagues + three international events, ~80 teams, ~80 patches); transaction-cost treatment — read Methods-equivalent sections directly (Section 3 Data, Section 3.3–3.4 evaluation/training workflow, Section 4 scoring, Section 5.5 market backtest including 5.5.1–5.5.4, Section 6); publication/preprint status; and every performance number below with its Table/Section location. Fields that cannot be verified from the primary text are marked `data gap` / `not stated in source`.
- **Deduplication audit (2026-09-22):** ripgrep across **all** `*.md` records in this repository (not `git log`) for `2609.08060`, `10.48550/arXiv.2609.08060`, the exact title phrase "Pre-game paired-comparison modeling", author names (Min-Ren Guan, Shen-Ning Tung), affiliation/email (Teahouse, teahouse.finance), and mechanism terms (`League of Legends`, `esports`, `paired-comparison`, LoL/`Polymarket` combinations) → **zero source-identity hits**; only two unrelated records match `paired-comparison`/`Bradley-Terry` as a method term (electoral betting-exchange pairs; DeFi CFMM). No `coverage_manifest` exists in the repository. Full-tree search of `~/.hermes/wiki` for the same identities → zero hits.

## Economic mechanism

### Source-reported

The paper builds a **pre-game win-probability forecaster for individual professional League of Legends maps** and evaluates it against three things: two classical paired-comparison benchmarks, a stronger two-stage rival model built by the same authors, and **Polymarket's own per-map "Game N winner" contract prices** as an external forecasting benchmark (Sections 1, 2, 5.5). The proposed model is a minimal one-stage logistic regression, fit end-to-end on the win/loss log-loss, combining (i) each team's exponentially-weighted moving average (EWMA) of its own past *same-side* results, (ii) a ridge-shrunk stable team strength that the paper proves is exactly the maximum-a-posterior estimate of a logistic mixed model, and (iii) a schedule-assigned first-pick draft indicator (Section 2.2, Eqs. 6–8). Source-reported conclusions: the minimal model ties the strongest two-stage rival on every protocol ("parity and parsimony", Sections 5.3, 6); both beat the purely dynamic Bradley–Terry benchmark; and against Polymarket the forecasts are **statistically indistinguishable on the market's own per-game contracts, with the market holding a modest edge on cross-region Worlds and series-decider maps** (Abstract, Section 5.5.2).

### Research interpretation

Falsifiable hypothesis, stated in our terms: **prediction-market prices on scheduled binary esports contests are, at best, matchable — not beaten — by a transparent public statistical forecaster using only pre-game information, and any residual exploitable mispricing is confined to thin, pre-declared slices.** The competing hypothesis is that pre-start model-minus-market probability gaps carry positive expectancy once frictions are paid. Component roles (hybrid structure preserved; note the source supplies no trading layer at all):

```text
Regime: none required by the source (no regime filter anywhere in the paper)
Primary signal: pre-game win probability p̂ from Eq. (7) — EWMA same-side form (λ) + ridge-shrunk team strength (τ) + first-pick indicator
Decision reference (source-reported): last Polymarket quote strictly before map start, anchored to the first telemetry frame, quotes >6 h stale rejected (Section 5.5.3)
Decision rule (bet/no-bet, threshold, side): NOT in source — research-proposed layer required (see Falsification plan)
Risk / exit / sizing: NOT in source — the paper defines no position, exit, holding period, or sizing rule (Section 5.5.4 explicitly scopes this out)
```

Candidate mechanisms if any edge exists (our interpretation, not the source's): day-of information (roster/patch news) not consumed by the model; liquidity/attention asymmetries across six regional leagues; behavioral favorite/longshot or home-region biases in thinly covered esports contracts. The source's own evidence points the other way — the market is *ahead* where uncertainty is highest — so this record's primary value is a clean, reproducible **market-efficiency / negative-evidence** benchmark for prediction-market timing, not a demonstrated alpha.

## Signal

All operational items below are **source-reported** unless explicitly marked research-proposed / research-defined.

- **Formation timestamp:** prediction is produced strictly before the map begins. Under the walk-forward protocol the model is refit at each scored game on all games strictly prior in calendar time, minimum 500 prior games (Sections 3.3, 5.5.1); the market quote is the **last price strictly before game start, anchored to the first telemetry frame's own timestamp** (Section 3.2), because for some leagues the provider's recorded timestamp marks game *end* rather than start (undocumented, provider-side). `data gap`: the timezone/DST convention for those timestamps is not stated in source.
- **Lookback:** each team's form state is accumulated from its own debut (zero-initialized) over its own same-side games only — a team's red-side results never update its blue-side form (Section 2.2, Eq. 5). End-of-training feature scaling only; no game's own outcome ever enters its own feature (Section 3.4).
- **Signal construction (Eq. 7, proposed model):** `p̂ = expit(β₀ + γ_FP·1[blue is first-pick] + β_B·E^B − β_R·E^R + θ_blue − θ_red)` with `E` the EWMA of the signed result `x = 2O−1 ∈ {±1}`, i.e. four unpenalized coefficients plus the ridge-penalized per-team block `θ` (Section 2.2, Table 1).
- **Estimation:** single convex L-BFGS pass minimizing penalized log-loss + (τ/2)‖θ‖² (Eq. 8); the paper proves this equals the MAP of a logistic GLMM with τ ↔ 1/σ²_θ (Section 2.2).
- **Evaluation protocols (both reported):** (a) global time split — oldest 80% train / newest 20% test, cross-region `n_te = 912` after the seen-side filter (115 of 1,027 cross-region test rows removed); (b) per-game walk-forward — refit at every scored game on all strictly prior games, min 500, `4,605` games scored (Section 3.3). Random cross-validation is explicitly rejected as leaky for path-dependent EWMA features.
- **Hyper-parameters (source-reported):** λ selected on training data alone from grid {0.1, 0.2, 0.3, 0.5, 0.7, 0.9} (Appendix B), τ from grid 0.25–16 (Section 5.4); inner chronological split = first 75% of the training window scored on the remaining 25% (Section 3.4). Holdout selects λ = 0.1; the walk-forward's frozen pair on its first-500-game window is (λ, τ) = (0.9, 4). Second candidate model fixes λ₁ = λ₂ = 0.3 a priori and Platt-calibrates in-sample (Sections 2.3, 3.4).
- **Ablation dimensions (source-reported):** latent-update dimension d ∈ {1, 4, 10} (Table 5); composite-response re-weightings (Section 5.4); λ sweep (Appendix B, Table B.1).
- **Long entry / short entry / exit / holding period / re-entry:** **not specified by the source.** The paper predicts probabilities and scores them with the Brier score (identical to the ranked probability score for this two-outcome market, Section 4.1); it never converts a probability gap into a position. Any entry threshold, side rule, stop, or holding rule used downstream is `research-proposed` (see Falsification plan item 3) and must not be attributed to the source.
- **Position sizing:** `not stated in source` (no Kelly, no stake, no bankroll).
- **Benchmarks:** re-implemented Cattelan–Varin–Firth dynamic Bradley–Terry, static Stefani least squares, static boundary of Eq. (9) with BLUP shrinkage, two-stage candidate, and Polymarket market prices (Sections 5.2, 5.5).
- **Reconstruction status:** the *forecasting* layer is reproducible from Sections 2–4 (equations, grids, protocols all given); the *trading* layer is `underspecified` because it does not exist in the source.

## Required data

- **Instrument / universe:** professional League of Legends maps (individual games, mostly best-of-three series) — six regional leagues LCK, LPL, LEC, LCS, LCP, CBLOL plus three international events (First Stand, Mid-Season Invitational, Worlds); ~80 teams, ~80 patches, 2024–2026 (Table 2: LPL 1,822; LCK 1,276; LEC 697; LCP 432; CBLOL 277; LCS 216; Worlds 190; MSI 157; First Stand 68 — sums to 5,135).
- **Venue / market type:** Polymarket per-map binary "Game N winner" prediction-market contracts, plus the series-winner contract used as a price fallback on decider maps (Sections 3.1, 5.5.3). Settlement chain, token standard, and venue fee schedule: `not stated in source`.
- **Timeframe:** per-map pre-game forecasts for scheduled events; market window restricted to Polymarket's listing history for LoL, which began in **October 2025** (Section 5.1).
- **Fields:** binary map outcome `O_i` (blue win); side-specific form states; first-pick assignment; patch ID; rosters; end-of-game margins (gold, kills, towers, inhibitors, barons, dragons), 15-minute differentials, and game duration (used by the second candidate / d-ablation only); Polymarket pre-start quotes with timestamps.
- **Data providers (source-reported, Section 3.1):** (1) lolesports broadcast telemetry via **unofficial** endpoints — community API documentation at `github.com/jpteixeira99/lol-esports-api`, last accessed 24 August 2026; (2) **Leaguepedia** MediaWiki Cargo database (patch IDs, rosters, first-pick — the sole first-pick source); (3) **Polymarket prediction-market API** (benchmark only, never used in fitting).
- **Point-in-time / leakage controls:** features built strictly from games prior to each game (Section 3.4); games lacking a first-pick assignment excluded outright, not imputed (758 of 5,893, mostly pre-season 2026 slots, <13% of corpus); market quotes must be strictly pre-start with a 6-hour staleness cutoff (47 rejected stale + 1 unsettled = 48 exclusions; median accepted staleness 0.5 min, max 106 min) (Sections 3.2, 5.5.3); market backtest excludes the predicted game from its own training window by game identifier (Section 5.5.1).
- **Timestamp / timezone:** anchored to the first telemetry frame timestamp (10-second cadence); for some leagues the recorded schedule timestamp marks game end rather than start — an undocumented provider convention (Section 3.2). Timezone/DST convention: `data gap` (not stated in source).
- **Missing data / exclusions:** no imputation for missing first-pick; seen-side filter removes 115 of 1,027 cross-region test rows so every model can predict (Section 5); unseen-team fallback sets θ̂ = 0 (near 0.27 Brier on those 115 games vs ~0.23 elsewhere).
- **Funding / fee / spread needs:** maker/taker fees, bid-ask spread, slippage, gas/network cost, borrow, and funding are **`not stated in source`** — no trading layer exists in the paper; do not read this as "zero".

## Execution assumptions

- **Signal-to-order timing:** `not applicable / not stated in source` — the paper never issues an order. Forecasts are pre-map; quotes are read strictly pre-start.
- **Order type / fill model / latency / partial fills / failures:** all `not stated in source`.
- **Fees / spread / slippage / impact / capacity:** all `not stated in source`. Section 5.5.4 states the scope explicitly: "The market comparison reported here is a forecasting-quality result only, model RPS against market-implied RPS: Polymarket functions throughout this paper strictly as an external forecasting benchmark, and nothing built on top of these probabilities is discussed further here." Quote semantics (mid vs bid vs last trade) are also `data gap` — the paper says "last pre-start price" without defining the quote type.
- **Leverage / margin / borrow:** not discussed (binary contracts, no leverage layer modeled).
- **What the source does assume for evaluation:** the score comparison is paired per-game Brier with Diebold–Mariano-style standard errors under squared-error loss and independent games (Section 4.2); model–market score correlation ≈ 0.7; models-vs-models ≈ 0.944.
- Any claim that this forecasts *returns* rather than *probabilities* would be a misreading: no P&L, ROI, or expectancy figure appears anywhere in the source.

## Evidence

### Source-reported

All figures below are source-reported from arXiv:2609.08060v1 and have **not** been independently reproduced; each is tied to its table/section. Sign convention for the market comparison: Δ = RPS_model − RPS_market, so **negative = model ahead, positive = market ahead** (Table 7).

1. **Classical benchmarks, global 0.2 holdout (Table 4, n_te = 912):** proposed (7) λ=0.1 RPS **0.2230**; two-stage candidate (9) **0.2257**; Cattelan dynamic Bradley–Terry **0.2351** (λ=0.1; 0.2391 at λ=0.3; 0.2462 at λ=0.9); Stefani static least squares **0.2301**; static boundary of (9), BLUP-shrunk **0.2268**. Proposed beats the best Cattelan configuration by 0.0121 RPS, two-stage by 0.0094 (Section 5.2). Paired two-stage vs Cattelan: Δ = −0.0094, paired SE 0.0052, t = −1.82, p = 0.07.
2. **Walk-forward corroboration (Section 5.2.2, 4,605 games):** proposed **0.2207** vs best Cattelan **0.2319** (λ=0.1) → gap 0.0112; two-stage **0.2215** → gap 0.0104.
3. **Architecture parity + native calibration (Table 5, Section 5.3):** d=1 proposed 0.2230 / LogLoss 0.6371 / Δ vs two-stage +0.0027 (p = 0.22) / holdout calibration slope 0.88; core4 d=4 0.2242 (slope 0.77); all-features d=10 0.2258 (slope 0.74, Δ = −0.0001, p = 0.97); two-stage 0.2257 / 0.6492 (slope 0.67). Walk-forward: proposed 0.2207 vs two-stage 0.2215, paired Δ = +0.0008, p = 0.40, score correlation 0.944; full one-stage family member 0.2227. Walk-forward calibration of the proposed model: intercept −0.009, **slope 0.995** (the abstract's headline calibration figure).
4. **Market comparison (Table 7, backtest of 2026-07-21):** Overall — proposed n = 924 Δ = **+0.009** (t = +2.24), two-stage n = 928 Δ = **+0.010** (t = +2.24); Section 5.5.2 text gives +0.0093 and +0.0097 with p = 0.025 for both. Per-game-contract-only row (excludes the 136 fallback-priced deciders) — proposed n = 788 Δ = +0.006 (t = +1.41), two-stage n = 792 Δ = +0.005 (t = +1.08); with confidence intervals (Section 5.5.2): proposed Δ = +0.006 (95% CI −0.002 to +0.015), two-stage Δ = +0.005 (95% CI −0.004 to +0.014) — intervals spanning zero while bounding any market edge below 0.015 Brier and any model edge below 0.004.
5. **League-level rows (Table 7):** LPL n=316 −0.003 / −0.008; First Stand n=33 −0.008 / −0.031; LCK n=244 +0.002 / +0.001; LCP +0.015 / +0.032; LEC +0.020 / +0.032; LCS +0.037 (t = +2.28) / +0.026; **Worlds n=50 +0.069 (t = +4.61) / +0.050 (t = +3.52)**; CBLOL n=14 +0.077 / +0.094 (too sparse to read). Read against a Bonferroni ×8 threshold: **Worlds is the only slice that survives** for either architecture (Section 5.5.2).
6. **Market sample construction (Sections 5.1, 5.5.3):** 928 matched maps of 973 corpus games inside the Polymarket listing window (≈95% coverage); 136 of 928 (15%) priced from the series-winner contract at the decider point (138 recovered, 2 later rejected by price filters); exclusions 47 stale + 1 unsettled; median quote staleness 0.5 minutes (max 106).
7. **Self-training guard / coherence check (Section 5.5.1):** backtest model Brier on the market window **0.2260** vs independent walk-forward on the identical window **0.2263** — two pipelines sharing no code path.
8. **Per-league robustness (Table 3):** the proposed model converges in every single-league fit (no singular fits); LCP 0.2648 vs two-stage 0.3055; LCK identical at 0.2137; LPL 0.2281 vs 0.2216; LEC 0.2529 vs 0.2593; LCS 0.2383 vs 0.2366.
9. **Feature-count ablation (Section 5.3):** held-out RPS worsens monotonically in d (0.2230 → 0.2242 → 0.2258); the win indicator even receives a large *negative* learned weight (−0.81 at d=4, −0.88 at d=10) — richer end-game telemetry learns noise at this corpus size.
10. **λ robustness (Section 5.4, Appendix B Table B.1):** walk-forward score identical at 0.2207 for λ = 0.1 and λ = 0.9; total Brier spread across the six-point grid = 0.0002 (n = 4,703, August-2026 corpus).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **The market, not the model, is ahead overall.** With decider-fallback maps included, Polymarket beats both architectures: Δ = +0.0093 (proposed), t = +2.24, p = 0.025 (Section 5.5.2) — the deficit concentrates on cross-region Worlds (Δ = +0.069, t = +4.61, the only slice surviving Bonferroni ×8) and on series-decider maps, i.e. exactly the maximal-uncertainty games where day-of information matters most.
- **Parity is not alpha.** On the market's own per-game contracts the model–market CIs bound any model edge below 0.004 Brier and any market edge below 0.015 (Section 5.5.2) — no exploitable gap is demonstrated, and the paper explicitly declines to build any trading claim on the probabilities (Section 5.5.4).
- **No league-level model advantage reaches significance, let alone multiplicity-corrected significance.** The best nominal model slices are small and statistically insignificant (LPL Δ = −0.003, t = −0.45; First Stand Δ = −0.008 at n = 33, t = −0.22); only the *market*-ahead slice (Worlds) survives Bonferroni ×8 (Section 5.5.2, Table 7).
- **Richer features hurt monotonically** (d-ablation, Section 5.3) — a negative result for the "more telemetry ⇒ more signal" story in this domain.
- **The stronger architecture buys nothing:** the deliberately strongest two-stage rival is statistically indistinguishable from the minimal model on every protocol and window (Section 5.3) — accuracy headroom is not the binding constraint.
- **Calibration caveat:** the two-stage model's absolute scores are mildly inflated by in-sample Platt scaling; an out-of-fold refit moves 0.2257 → 0.2248 (Appendix A).
- **Unseen-team fallback degrades accuracy:** near 0.27 Brier on the 115 fallback games vs ~0.23 elsewhere (Section 5).
- **Sample comparability:** market scores (928 maps, Oct 2025 – Jul 2026) and model holdout scores are computed on different samples and are explicitly "not directly comparable" in level (Section 5.1).
- **Pipeline fragility:** unofficial lolesports endpoints with silent pagination truncation, undocumented per-league start-vs-end timestamp conventions, and three sources sharing no join key — the authors flag standing exposure to provider-side convention changes (Sections 3.2, 6).
- **Zero execution evidence:** no spread, fee, gas, fill, sizing, or P&L treatment exists anywhere in the source; Brier parity therefore says nothing about post-friction expectancy.
- **Classical fits go singular** on thin single-league designs (LCP) (Sections 2.3, 6).
- No independent replication or contrary published study on this specific source was found in this run; absence is not evidence of no negative result.

## Falsification plan

Every threshold below is **research-defined** (not from the source) unless explicitly noted; the operational trading rules are **research-proposed**.

1. **Out-of-sample replication on fresh seasons (source's own design):** rebuild the corpus post-July-2026 and rerun both protocols. Failure rule (research-defined): proposed model fails to beat a re-implemented Cattelan dynamic Bradley–Terry by ≥ 0.005 walk-forward Brier, **or** walk-forward calibration slope falls outside [0.9, 1.1] → the "stable shrunk strength carries recoverable signal" claim is materially weakened.
2. **Market-edge test, pre-registered:** paired Δ (model − market) on ≥ 300 fresh matched maps within each pre-declared slice (research-defined n). Failure rule (research-defined): 95% CI includes 0 → no exploitable-edge claim survives; record as parity.
3. **Trading-layer test (entirely research-proposed; the source supplies none):** convert pre-start probability gaps into Polymarket bets only when |p̂ − p_market| ≥ 5 cents (research-proposed threshold), with a fixed fractional-Kelly cap of 0.25 (research-proposed), explicitly modeling bid-ask spread, taker fees, chain gas, partial fills, and resolution timing (all `not stated in source`). Failure rule (research-defined): net ROI ≤ 0 after costs over ≥ 200 bets → not tradable, regardless of Brier results.
4. **Multiplicity discipline:** repeat all league-level comparisons under Bonferroni/BH across pre-declared slices. Failure rule (research-defined): any slice-level "edge" that does not replicate out-of-sample is discarded as noise rather than retuned.
5. **Placebo market (research-proposed):** shuffle market quotes across maps within league-week and recompute Δ. If the model's gap vs the placebo market is indistinguishable from its gap vs the real market, the comparison is measuring forecaster quality, not market inefficiency.
6. **Ablation of the ridge stable-strength block (mechanism test):** remove θ and re-score. Failure rule (research-defined): Brier does not degrade toward the 0.2351 dynamic benchmark (tolerance ±0.003) → the mechanism claim is falsified.
7. **Data-source audit:** rebuild the corpus from an independent schedule/roster source. Failure rule (research-defined): > 10% join loss or first-pick missingness > 5% → the corpus is not reproducible as specified.

Action on failure: retain this record as research-only, append the negative evidence here, and do not advance to implementation candidacy; do not rescue a failed threshold by unconstrained retuning.

## Crypto portability

**adapted** — the source's subject matter is professional esports; it contains **zero** crypto price/volume/funding evidence, so this is a ported evaluation hypothesis, not crypto empirical evidence.

- **What ports:** the *protocol* — a public pre-event statistical forecaster scored against a prediction market's own pre-start quote with a paired proper-score test, staleness filtering, and leakage-guarded walk-forward — transfers directly to crypto-subject prediction markets (e.g., Polymarket/Kalshi contracts on BTC/ETH price thresholds). Polymarket itself is a crypto-settled venue, so venue mechanics are already crypto-native.
- **What does not port:** every covariate (teardown telemetry, first-pick draft, team EWMA, patch IDs) is esports-specific; there is no analog to these in crypto markets, so a crypto implementation would need an entirely different signal layer while reusing only the evaluation harness.
- **Crypto-specific risks:** 24/7 markets remove the clean "pre-game vs post-game" event boundary; contract/oracle resolution and settlement timing (chain gas, redemption latency) are `not stated in source` but are material costs; venue fragmentation across prediction venues creates quote-arbitrage and staleness issues; thin books and wide spreads on crypto-subject contracts can swamp the ≤0.004-Brier-scale edges the source bounds; spot/perpetual/funding mechanics are entirely absent from the source.
- No crypto backtest of this protocol exists in our research stack; portability remains unproven.

## Limitations

- **Source status:** unpublished arXiv preprint (v1, 2026-09-07); peer-review status is `data gap` despite the Section 1 self-description; no journal reference or external DOI on the landing page (checked 2026-09-22).
- **Not a strategy backtest:** forecasting-quality comparison only — no P&L, no expectancy, no transaction-cost, spread, fee, gas, fill, or sizing treatment anywhere (Section 5.5.4 states this scope explicitly); execution fields are `not stated in source`, not zero.
- **Short, single-venue market window:** 928 maps, October 2025 – July 2026, Polymarket only, one title (LoL), one contract style (binary per-map + series fallback).
- **`data gap`:** timezone/DST convention for event timestamps; whether Polymarket quotes are mid/bid/ask/last; venue chain and fee schedule; series-level (best-of-three) market modeling is deferred to future work by the authors (Section 4.3).
- **Known small-sample inflation:** in-sample Platt calibration inflates the two-stage model's absolute scores (0.2257 → 0.2248 out-of-fold, Appendix A); the CBLOL row (n=14) is explicitly too sparse to read.
- **LLM-assisted implementation** (Claude) disclosed by the authors (Section 3.4); pipeline not independently audited by us.
- **Not independently reproduced**; corpus depends on unofficial endpoints with undocumented conventions (Sections 3.2, 6).
- **Self-comparison concern:** the authors built both competing architectures and the benchmark pipeline; the market is the only external opponent, and it wins where it matters.
- **Incremental scope:** the captured claim is about *forecast parity with a prediction market*, not about esports or prediction markets being profitable.
- **Crypto porting is `adapted`, not `direct`.**

## Implementation status

`not-implemented`. No implementation, backtest, prototype, paper trading, or validation exists in our research stack; nothing in Qlib, Paper, Testnet, or Live has been touched by this record.

## Adoption boundary

This record is research material only. Its presence in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading.

## Related Wiki records

- Full-tree search of `~/.hermes/wiki` for `League of Legends`, `esports`, `paired-comparison`, and `2609.08060` (2026-09-22) found **no** matching record; no Wiki link is asserted for those identities rather than fabricate one.
- `[[quant/prediction-market-llm-confidence-weighted-value-bet-2026-09-04]]` — adjacent family: prediction-market value-betting construction; different source, different mechanism (LLM confidence weighting vs paired-comparison forecasting parity), different universe.
- Repo-adjacent records (same repository, different source identities): `electoral-betting-ou-pairs-bootstrap-signal-bradley-terry-selection-2026-09-22` (Bradley–Terry used inside an electoral betting-exchange pairs design — different source, universe, and mechanism); `polymarket-favorite-longshot-bias-crypto-politics-2026-09-14`; `prediction-market-proper-betting-accuracy-profit-conversion-2026-09-02`; `kalshi-prediction-market-pricing-wedge-executable-spread-falsification-2026-09-13`; `polymarket-binance-high-frequency-binary-lead-lag-2026-09-02`. None shares this source identity (arXiv:2609.08060) or this mechanism (esports pre-game paired-comparison forecast vs market price, paired-Brier parity test).

## Sources

1. Guan, M.-R., & Tung, S.-N. (2026). "Pre-game paired-comparison modeling of professional League of Legends map outcomes." arXiv:2609.08060v1 [stat.AP] (cross-list q-fin.ST), submitted 7 September 2026. https://arxiv.org/abs/2609.08060 (full text: https://arxiv.org/html/2609.08060v1 ; PDF: https://arxiv.org/pdf/2609.08060v1 ; DOI: https://doi.org/10.48550/arXiv.2609.08060). All quantitative claims above trace to Sections 1–6, Tables 1–7, and Appendices A–B of that preprint; all are labeled source-reported.
2. Data providers used by the primary paper (used by it, not directly by us), for provenance only: lolesports community API documentation `https://github.com/jpteixeira99/lol-esports-api` (last accessed 24 August 2026 per Section 3.1); Leaguepedia (MediaWiki Cargo database); Polymarket prediction-market API.
