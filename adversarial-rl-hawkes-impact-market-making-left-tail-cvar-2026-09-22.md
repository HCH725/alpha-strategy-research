---
schema: strategy-research-record-v1
title: "Adversarial Reinforcement-Learning Market Making with Hawkes Self-Exciting Order Flow and Permanent Price Impact: LSTM Temporal State under a Left-Tail CVaR Robustness Protocol"
created: 2026-09-22
updated: 2026-09-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - market-making
  - adversarial-reinforcement-learning
  - hawkes-process
  - price-impact
  - left-tail-risk
  - cvar
  - inventory-risk
  - simulation-only
status: research-only
confidence: medium
source_as_of: 2026-09-19
sources:
  - "Hao Yang and Zhenguo Xu, 'Robust Market Making with Hawkes Order Flow and Price Impact via Adversarial Reinforcement Learning', arXiv:2609.22785v1 [cs.LG], submitted 19 Sep 2026 05:32:29 UTC. https://arxiv.org/abs/2609.22785 (DOI: https://doi.org/10.48550/arXiv.2609.22785)"
  - "Full-text HTML v1, reviewed 2026-09-22: https://arxiv.org/html/2609.22785v1 (Sections 2-5, Tables 1-2, Appendix E)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Adversarial Reinforcement-Learning Market Making with Hawkes Self-Exciting Order Flow and Permanent Price Impact: LSTM Temporal State under a Left-Tail CVaR Robustness Protocol

## Provenance

- **Primary Source:** Hao Yang (North China Institute of Computer System Engineering, Beijing, China; corresponding author) and Zhenguo Xu (University of Science and Technology of China, Hefei, China), *"Robust Market Making with Hawkes Order Flow and Price Impact via Adversarial Reinforcement Learning"*, arXiv preprint `arXiv:2609.22785v1 [cs.LG]`, submitted Saturday, 19 September 2026 05:32:29 UTC (577 KB), submitter of record Zhenguo Xu.
  - Stable URL: https://arxiv.org/abs/2609.22785
  - Full-text HTML (v1): https://arxiv.org/html/2609.22785v1 — read in full on 2026-09-22 (Sections 1-6, Appendices A-E, Tables 1-2).
  - Canonical DOI: https://doi.org/10.48550/arXiv.2609.22785
- **Primary subject area:** Machine Learning (`cs.LG`) only; no q-fin cross-list on the landing page (verified from the Subjects table, 2026-09-22).
- **Comments field (verbatim intent):** 18 pages, 2 figures; includes theoretical analysis, numerical experiments, and supplementary results in the appendix.
- **Publication status:** preprint only — **no journal-ref and no related DOI** on the landing page as of 2026-09-22; not peer-reviewed. License: arXiv.org perpetual non-exclusive license.
- **Code/data availability:** no public code repository, artifact link, or data-availability statement was found in the v1 full text (checked 2026-09-22). All experiments are self-contained simulations.
- **Pre-write repository dedup (2026-09-22):** ripgrep across all `*.md` records plus `coverage_manifest.csv` for `2609.22785`, `Robust Market Making with Hawkes`, `ARLMM`, `adversarial.*market mak`, `zero-sum.*adversar` → **0 hits**. Adjacent market-making records were read and are materially different sources/mechanisms:
  - `sinkhorn-robust-rl-high-frequency-market-making-2026-09-02.md` (arXiv:2607.08291) — Sinkhorn-divergence distributionally robust RL with two-dimensional robustness decomposition and 14-block real-HF feature state (microprice, OFI, Hawkes states); robustness device = ambiguity set, not a zero-sum adversary, and its data dependency is real order-book features.
  - `deep-rl-market-making-regime-switching-bocpd-scenario-bandit-2026-09-11.md` (arXiv:2609.11614) — distributional C51/Rainbow with Bayesian online changepoint filtering and scenario-bandit robust fine-tuning, calibrated on real LOBSTER AMZN L3 data with a Santa Fe LOB simulator; robustness device = changepoint detection + curriculum fine-tuning.
  - `hawkes-driven-otc-market-making-volterra-riccati-2026-09-01.md`, `multi-level-market-making-logistic-normal-deep-sets-2026-09-02.md` — closed-form/multi-level quoting frameworks, no adversarial training.
  - The present source's materially distinct core: an explicit **episode-level zero-sum environmental adversary that selects the Hawkes/impact regime vector** `(b, A, k, κ_H, γ_H, ξ)`, paired with a **one-layer LSTM temporal encoding of a K=40 observation window**, evaluated by a **left-tail CVaR robustness protocol with a terminal-inventory bootstrap neutrality test** — and, distinctively, a **purely synthetic regime-grid data dependency (no market data at all)**.

## Economic mechanism

### Source-reported

Market makers earn the bid-ask spread by continuously posting one-unit passive bid/ask quotes around the mid-price and are exposed to inventory, adverse-selection, and model-misspecification risk. Existing adversarial-RL (ARLMM) work formulates Avellaneda-Stoikov market making as a zero-sum game between the market maker and an environmental adversary, but relies on Poisson arrivals with no price impact. The authors extend that game to (i) **bilateral Hawkes self-exciting arrival intensities** and (ii) **trade-induced permanent price impact**, argue this creates stronger non-stationarity, and add an **LSTM module over a recent observation window** so the policy can tell whether an order-flow burst is beginning, expanding, or decaying (Sections 1, 2, 4). They further propose a robustness evaluation protocol aligned with the worst-case training objective: left-tail metrics (CVaR_10% primary, CVaR_30% secondary) plus a one-sided bootstrap test that improvement is not bought with stronger terminal directional inventory bias (Section 5.1). Theoretical contribution: single-stage pure-strategy Nash equilibrium with interior best-response quote depths `δ± = 1/k± ∓ b + ξ` (Theorems 1-2, Eq. 11).

### Research interpretation

Falsifiable hypothesis: **a minimax-trained quoting policy whose adversary chooses episode-level microstructure regimes (including Hawkes excitation `γ_H` and impact `ξ`) and whose temporal encoder is an LSTM improves the left tail of the market-maker return distribution (CVaR_10%) relative to (a) fixed-regime training, (b) independently random regime sampling, and (c) ARLMM restricted to drift/liquidity/depth, without increasing directional inventory exposure.** Causal channel: flow clustering makes inventory risk propagate across steps, so a policy that cannot represent temporal state mis-times spread widening; adversarial regime selection concentrates training on exactly those clustered-flow environments. Component roles (hybrid): regime/training device = zero-sum adversary over `(b, A, k, κ_H, γ_H, ξ)`; state construction = K=40 window + 32-unit single-layer LSTM (versus the same window used flat by baselines); risk/exit logic = quadratic inventory penalties `ζH²` in the reward plus terminal penalty, not a separate exit rule. Do not assume each component contributes equally — the paper's own ablation (RQ2/RQ4) already shows the adversary alone is not uniformly beneficial.

## Signal

All items below are source-reported from Sections 2, 4, 4.1 (v1) unless marked otherwise.

- **Formation timestamp / tradability:** decision epochs every `Δt = 0.005` model time units, `T = 1`, i.e. 200 discrete steps per trajectory; quotes are posted at the start of each step and fills arrive within the step per the execution intensity. Time units are simulation units, not wall-clock; no timezone or session convention (not applicable to the synthetic environment).
- **State/observation:** environment-internal state = mid-price `Z`, inventory `H`, cash `X`, bilateral conditional intensities `λ±`; **only the MM observes `(H_t, t)`**, rolled into a window `O_t = (o_{t-K+1}, …, o_t)` with `K = 40`. For "Ours" the window is encoded by a one-layer LSTM with 32 hidden units.
- **Action:** continuous quote offsets `a_t = (δ_t^b, δ_t^a)`, i.e. bid/ask depths around mid (one-unit quotes). Fill intensity `Λ± = λ± · e^{−k± δ±}` (Eq. 5), bilateral Hawkes dynamics `λ± ← λ± + κ_H(A − λ±)Δt + γ_H ΔN±` (Eq. 4).
- **Dynamics:** mid-price `Z_{n+1} = Z_n + bΔt + σW + ξ(ΔN⁻ − ΔN⁺)` (Eq. 1) — permanent impact per unit net execution; cash `X_{n+1} = X_n + δ⁻ΔN⁻ + δ⁺ΔN⁺ − ZΔH` (Eq. 7); mark-to-market value `Π = X + HZ` (Eq. 8).
- **Reward:** `r_t = ΔΠ_t − ζ H_t² − 1{t=T} η H_T²` with `ζ = 10⁻⁴`, `η = 10⁻²` (Eq. 13); adversary payoff is the negative of the MM episode return.
- **Training algorithm:** both agents trained with PPO (actor-critic, GAE); learning rate `3 × 10⁻⁴`, discount `0.999`, MLP actor/critic with one hidden layer of 64 units; 50 trajectories per episode as one training chunk, 10 optimization epochs, total budget 800,000 environment steps.
- **Four training environments (Section 4):** `Fixed` = `(b,A,k,κ_H,γ_H,ξ) = (0,140,1.5,60,0,0)` always; `Random` = per-episode independent truncated-normal draws around the standard environment with `b ∈ [−5,5]`, `A ∈ [105,175]`, `k ∈ [1.125,1.875]`, `κ_H ∈ [35,60]`, `γ_H ∈ [0,40]`, `ξ ∈ [0,1]`; `ARLMM` = learnable adversary over `(b,A,k)` only (same ranges), following prior ARLMM work; `Ours` = learnable adversary over the full six-vector, same ranges, with LSTM state encoding.
- **Holding/exit:** no discrete entry/exit or holding-period rule; continuous two-sided quoting for the full horizon with inventory bound `|H| ≤ 50` and terminal liquidation penalty encoded in the reward.
- **Parameters fixed by the source:** `σ = 2`, initial price `Z_0 = 100`, inventory bound 50, `K = 40`, LSTM 32 units, `ζ = 10⁻⁴`, `η = 10⁻²`, seeds `701, 30, 90, 45, 78` (results averaged over these five seeds).
- **Underspecified in source:** no policy action box (admissible range of `δ±`) is stated; no parameter-tuning protocol for `ζ`/`η` beyond the fixed values; the Table 2 "Sharpe" column is not given a precise definition in Section 5.1 (treated as source-reported, definition = data gap).

## Required data

- **Instrument/venue/universe:** none — the evaluation universe is a **synthetic single-asset market** defined by Eqs. (1)-(8). No exchange, no ticker, no point-in-time data.
- **Fields implied if one were to instantiate it:** mid-price path, per-side arrival counts/conditional intensities (Hawkes `λ±` with `A, κ_H, γ_H`), depth-decay `k±`, drift `b`, volatility `σ`, impact coefficient `ξ`, inventory, cash, fill events.
- **Real-data requirements:** **not stated in source**; the paper validates against 19 hand-constructed simulation environments covering standard, up/down drift, sparse/dense liquidity, Hawkes-only, impact-only, and extreme compound-stress regimes (Section 5, Table 2). Any real order-book calibration is future work and is a `research-proposed` extension here.
- **Point-in-time/missing data:** not applicable to the synthetic setup; no imputation questions arise.

## Execution assumptions

Source-reported (Sections 2, 4.1, 5):

- One-unit bid and ask quotes posted every step; fills occur stochastically at `Λ± = λ± e^{−k±δ±}` — a Poisson/Hawkes fill model at the MM's own quotes.
- **Spread:** the quoted half-spreads `δ±` are the strategy's own action; there is no external bid-ask cost channel in the model.
- **Price impact:** modeled explicitly and permanently, `ξ` per unit of net execution, `ξ ∈ [0,1]` in the regime grid (this is the paper's headline realism extension).
- **Fees/commission:** **not stated in source** — no fee, commission, or rebate term appears in the cash or reward equations (Eqs. 7, 13). Do not read this as "fees = 0 verified"; it is an unmodeled channel (explicit data gap).
- **Slippage:** not modeled beyond the self-quoted depth and the impact term; latency, partial fills/failure handling, leverage/margin, borrow, and capacity: **not stated in source**.
- Signal-to-order: same-step quoting (policy acts at the start of each `Δt` step); no next-bar convention needed in simulation.

## Evidence

### Source-reported

All figures below are source-reported from arXiv:2609.22785v1 and have **not** been independently reproduced. Units are simulation model units; these are not P&L in any currency and no real-market backtest exists.

- **Table 2 (Section 5.2), representative environments, 5 seeds:**
  - `G1_std (0,140,1.5,60,0,0)`: Ours terminal wealth `27.0037 ± 7.5168`, Sharpe `3.592460`, CVaR_10% `14.633210`, CVaR_30% `18.339891`, terminal inventory `−0.1490 ± 1.0526`; vs ARLMM `19.7519 ± 6.9503` / `2.841865` / `8.172405` / `11.832854` / `−0.5350 ± 0.7612`; Random `20.9421 ± 7.1667` / `2.922123` / `9.369169` / `12.935652` / `−1.4750 ± 0.7402`; Fixed `14.9841 ± 6.9313` / `2.161794` / `3.888963` / `7.313555` / `−1.2930 ± 0.7847`.
  - `G6_hawkes_only`: Ours `39.1673 ± 8.9248` / `4.388613` / CVaR_10% `24.492749` vs ARLMM `28.3563 ± 8.0409` / `3.526515` / `15.146983`; Random `29.9129 ± 8.7390` / `3.422921` / `15.247651`.
  - `G11_extreme_hawkes`: Ours `39.0256 ± 8.4942` / `4.594403` / CVaR_10% `24.291729` vs ARLMM `28.5050 ± 8.0734` / `3.530709` / `14.882185`.
  - `G13_extreme_combo_up`: Ours `20.0622 ± 5.4765` / `3.663299` / CVaR_10% `10.718706` vs ARLMM `13.1582 ± 5.1424` / `2.558757` / `4.465327`.
  - `G14_extreme_combo_down`: Ours `42.5229 ± 9.7747` / `4.350317` / CVaR_10% `26.418352` vs ARLMM `33.2700 ± 8.9068` / `3.735368` / `18.624493`.
  - `G18_ultra_dense_up_hawkes_only`: Ours `51.8173 ± 12.0118` / `4.313877` / CVaR_10% `31.800296` vs ARLMM `36.0455 ± 10.9279` / `3.298473` / `18.194456`.
  - `G19_ultra_sparse_down_hawkes_only`: Ours `31.6350 ± 7.5567` / `4.186356` / CVaR_10% `19.220036` vs ARLMM `24.7564 ± 6.9500` / `3.562071` / `13.496312`.
- **RQ2 (Section 5.2):** the original ARLMM beats `Random` on CVaR_10% in only **9 of 19** environments and is worse in the remaining 10; its losses cluster in Hawkes-dominated regimes, high-drift-plus-execution-pressure regimes, and liquidity-dominated regimes.
- **RQ4 (Section 5.2):** Ours has higher CVaR_10% than ARLMM in **19/19** environments and than Random in **18/19** (exception `G3_drift_down`, which has neither clustering nor impact). Pooled one-sided bootstrap (B = 20,000, α = 0.05) on terminal-inventory mean shift: Ours vs Random `D_obs = −1.29968`, `p = 0.504425`; Ours vs ARLMM `D_obs = −0.379579`, `p = 0.500925` — no evidence of stronger terminal directional inventory bias.
- **RQ5 (Section 5.2, Figure 2):** Ours exceeds ARLMM at all **25** grid points of the `(γ_H, ξ)` plane; largest gains near `(γ_H, ξ) = (20, 0)` and `(30, 0.25)`; smallest near `(20, 1.0)`.
- **RQ6 (Section 5.2):** approximate Nash equilibrium is explicitly **not** accepted as a sufficient robustness definition — low exploitability inside the training game does not guarantee left-tail performance in unseen environments.

### Independently reproduced

not independently reproduced

### Negative evidence

- **Source's own negative results:** (a) the prior ARLMM adversary is *not* uniformly better than naive random regime sampling (9/19); (b) the LSTM gain is regime-concentrated — it shrinks to near-zero at very high impact `ξ = 1` and disappears in `G3_drift_down` (no clustering, no impact); (c) approximate equilibrium does not imply robustness (RQ6); (d) tail risk is evaluated on terminal-wealth densities whose right tail expands for all methods in G19 (RQ1), i.e. the distributions are far from stable Gaussian summaries.
- **Evidence absent:** zero real-market data, zero fees/costs, zero latency, no capacity analysis, no code artifact, no peer review — every headline number is five-seed synthetic simulation output in model units.
- **Structural concern (research interpretation):** with `ζ = 10⁻⁴` inventory penalties and model-unit wealth, the reported Sharpe values (2-4.6 range) are artifacts of the simulation scaling and must not be compared to real-market Sharpe ratios.
- No additional contrary study was identified in the reviewed sources; absence is not evidence of no negative result.

## Falsification plan

Items labeled `research-defined` are Scout-chosen thresholds, not source claims; items labeled `research-proposed` are Scout-constructed tests absent from the source.

1. **Reimplementation gate (`research-proposed`):** with no public code, first reproduce the qualitative ordering Ours > ARLMM > Random/Fixed on CVaR_10% across the 19 environments within 5 seeds; failure to reproduce the 19/19 CVaR ordering under the paper's own parameters falsifies the computational claim.
2. **Real-data port (`research-proposed`):** fit arrival/impact/Hawkes parameters from real LOB data (e.g. crypto perp or equities L2) and re-run the trained policies; `research-defined` failure threshold: Ours fails to beat a fixed-regime PPO baseline on out-of-sample CVaR_10% over ≥ 3 disjoint market regimes → mechanism rejected as simulation-only.
3. **Cost stress (`research-proposed`):** add per-fill fees, a crossing-spread cost on inventory reduction, and stochastic latency; `research-defined` failure: the Ours-vs-ARLMM CVaR_10% gap in the Hawkes regimes (e.g. G6: 24.49 vs 15.15 model units) shrinks to ≤ 0 after costs → economic relevance rejected.
4. **Ablation of the two components (`research-proposed`):** adversary-without-LSTM (= ARLMM extended to six parameters) and LSTM-without-adversary (= Random-regime training with LSTM). The source only compares Ours vs ARLMM-vs-three-param adversary, so the marginal contribution of expanding the adversary's parameter space is not isolated; if LSTM-without-adversary captures all the gain, the adversarial-training thesis fails while the temporal-state thesis survives.
5. **Placebo (`research-proposed`):** shuffle the order of the K=40 observation window at test time; `research-defined`: if CVaR_10% is unchanged, the claimed temporal-encoding channel is falsified.
6. **Inventory-neutrality replication:** rerun the source's own bootstrap (B = 20,000, α = 0.05) on terminal inventory; `research-defined` failure: one-sided p < 0.05 → improvement is directional inventory exposure, not robustness.
7. **Competing explanation:** compare against a non-game robust baseline (e.g. distributionally robust PPO or scenario randomization with matched budget); if a non-adversarial baseline matches the left-tail gains, the zero-sum mechanism is unnecessary.

## Crypto portability

**adapted** (not `direct`: the source demonstrates nothing in crypto or in any real market).

- The mechanism (inventory-aware two-sided quoting under clustered flow with permanent impact) is portable in form to crypto perpetual/spot venues, where order flow is plausibly even more self-exciting.
- Porting gaps (`research-proposed` unless noted): crypto is 24/7 with no session close, so `T = 1` horizon and time-to-close conventions must be redefined; the model has **no funding-rate channel**, which is a first-order cash flow for perpetual market makers; venue fragmentation means impact/arrival intensity is per-venue and cross-venue toxic flow is unmodeled; fees/rebates (maker rebates are common on CEXs) are absent from the model yet determine real MM economics; tick-size discreteness, queue position, and partial fills are not modeled (one-unit fills at own quotes); mark/index price dislocations and liquidation mechanics for inventory are unmodeled.
- Therefore any crypto instantiation is a new ported hypothesis requiring its own falsification; portability is not authorization to trade.

## Limitations

- **Simulation-only:** 19 hand-built synthetic environments; no real market data, venue, or instrument anywhere in the paper (underspecified for deployment).
- **No transaction-cost model:** fees/commission/latency **not stated in source**; impact is the only friction channel, and it is stylized permanent impact.
- **Not peer-reviewed:** arXiv v1 preprint, no journal reference; single-shot submission, no code, no independent replication.
- **Model-unit metrics:** wealth/Sharpe/CVaR values are simulation-scaled; cross-paper comparison is invalid.
- **Underspecified:** policy action bounds for `δ±`; precise Sharpe definition; hyperparameter tuning protocol; compute budget beyond the 800k-step statement.
- **Incremental-write check:** this record is written because no existing record covers the source identity `arXiv:2609.22785` or the specific mechanism (zero-sum regime adversary over Hawkes/impact parameters + LSTM temporal state + left-tail CVaR protocol); existing robust-MM records use materially different robustness devices and data dependencies (see Provenance).
- Confidence is `medium` (not `high`) because the interpretation is fully grounded in the primary text but the underlying evidence base is unreviewed, unreplicated, and synthetic.

## Implementation status

`implementation_status: not-implemented`. Nothing from this record has been implemented in our research stack: no policy reimplementation, no simulator, no Qlib/backtest run, no Paper, Testnet, or Live verification. The paper's own experiments are simulation results only and are reported as source-reported claims.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this record does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; or approved for implementation, paper trading, testnet, or live trading. Crypto portability is stated as a hypothesis only.

## Related Wiki records

No stable Hermes Wiki Brain page for this mechanism could be confirmed, so no Wiki links are asserted (link fabrication prohibited). Adjacent records in this repository (other scouts' captures, different source identities and mechanisms):

- `sinkhorn-robust-rl-high-frequency-market-making-2026-09-02.md` (arXiv:2607.08291 — Sinkhorn distributionally robust RL)
- `deep-rl-market-making-regime-switching-bocpd-scenario-bandit-2026-09-11.md` (arXiv:2609.11614 — C51 + BOCPD + scenario-bandit fine-tuning)
- `hawkes-driven-otc-market-making-volterra-riccati-2026-09-01.md` (closed-form Hawkes OTC quoting)
- `multi-level-market-making-logistic-normal-deep-sets-2026-09-02.md`
- `hawkes-self-exciting-lob-return-sign-forecasting-coe-2026-09-02.md`, `hawkes-order-flow-imbalance-self-excitation-microstructure-2026-09-12.md` (Hawkes as a forecasting signal rather than a quoting environment)

## Sources

1. Hao Yang, Zhenguo Xu. "Robust Market Making with Hawkes Order Flow and Price Impact via Adversarial Reinforcement Learning." arXiv:2609.22785v1 [cs.LG], submitted 19 Sep 2026 05:32:29 UTC. https://arxiv.org/abs/2609.22785 — DOI: https://doi.org/10.48550/arXiv.2609.22785
2. Full-text HTML v1 (primary-source checksum performed 2026-09-22): https://arxiv.org/html/2609.22785v1 — Sections 2 (Trading Model, Eqs. 1-8), 3 (Game Formulation, Theorems 1-2), 4/4.1 (Adversarial Training, Learning Configuration, Eqs. 11, 13), 5/5.1/5.2 (Experiments, Robustness Metrics, Results, Tables 1-2, RQ1-RQ6), 6 (Conclusion), Appendices A-E.
