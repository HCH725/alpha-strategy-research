---
schema: strategy-research-record-v1
title: "Cross-Platform Semantic Non-Fungibility and Law-of-One-Price Arbitrage in Prediction Markets (arXiv:2601.01706)"
created: 2026-09-25
updated: 2026-09-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - prediction-markets
  - cross-platform-arbitrage
  - law-of-one-price
  - semantic-alignment
  - market-fragmentation
  - polymarket
  - kalshi
  - relative-value
status: research-only
confidence: medium
source_as_of: "2026-01-05 (arXiv v1 submission date, sole version as of 2026-09-25); market data through 2025-08-15/22"
sources:
  - https://arxiv.org/abs/2601.01706
  - https://arxiv.org/html/2601.01706v1
  - https://arxiv.org/pdf/2601.01706v1
  - https://doi.org/10.48550/arXiv.2601.01706
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Platform Semantic Non-Fungibility and Law-of-One-Price Arbitrage in Prediction Markets (arXiv:2601.01706)

## Provenance

- **Paper:** Jonas Gebele and Florian Matthes, "Semantic Non-Fungibility and Violations of the Law of One Price in Prediction Markets."
- **Authors exactly as source:** Jonas Gebele; Florian Matthes. Both listed under a single affiliation block: *Technical University of Munich, Munich, Germany*; contact `{jonas.gebele, matthes}@tum.de`. Per-author affiliation mapping beyond that single block is not stated in source.
- **Identifier / version:** `arXiv:2601.01706v1 [cs.CE]`. Submission history on the landing page shows only `[v1] Mon, 5 Jan 2026 01:01:52 UTC (3,126 KB)` — **no v2 exists as of 2026-09-25**, so v1 is the pinned version. Primary category `cs.CE` ("Computational Engineering, Finance, and Science"); no `q-fin` cross-list is printed on the landing page.
- **Publication / peer-review status:** the landing-page `Comments`, `Journal ref` and `DOI` cells are all empty and the body contains no peer-review statement → **preprint / working paper only**, not a published or refereed article. arXiv-issued DataCite DOI `10.48550/arXiv.2601.01706` resolved with redirect to the abs page, HTTP 200, checked 2026-09-25.
- **Licence:** the landing-page licence cell links `licenses/nonexclusive-distrib/1.0/` → **arXiv non-exclusive distribution licence**, not a Creative Commons licence. The text is therefore cited and normalized here rather than reproduced.
- **Primary-source checksum (pinned, read this run):**
  - HTML v1 `https://arxiv.org/html/2601.01706v1` — **291,445 bytes**, SHA-256 `22b8180777772515e3b6b4bec94d72fe00a3fc769959bf93615cee273da49890`; stripped to **82,742 characters / 1,730 lines**. Sections 1–8, the Discussion/Related-Work/Conclusion, Appendix 0.A (platform overview), Appendix 0.G (data acquisition) and Appendix 0.I (execution-cost assumptions) were read line by line; Appendix 0.B–0.F (LLM prompt templates and retrieval-recall validation) were sampled by heading only and not transcribed; the References list was skimmed, not transcribed. arXiv HTML build boilerplate after "Instructions for reporting errors" was excluded from all word-boundary scans below.
  - PDF v1 `https://arxiv.org/pdf/2601.01706v1` — **3,538,362 bytes**, SHA-256 `4f982f3b7958f697ce2656c62ebcd02e2260fff23f185bbaa4e8fa8a523c8214` (downloaded and hashed; text extraction used the HTML layer above).
- **Sample / universe:** all available historical market data per platform **through August 15–22, 2025** (Appendix 0.G / §4.1), within an overall ecosystem window the abstract states as **2018 to 2025**. Ten platforms: **Polymarket, Omen/Presagio, Augur v1, Limitless, Myriad, Seer, Truemarkets, Kalshi, Futuur, PredictIt** (§4.1 "Dataset summary"). Platform inclusion rule: a platform must list **at least 50 markets with individual lifetime trading volume above $500**; play-money systems (Metaculus, Manifold) and odds-replicating venues (Azuro, SX.bet, Betfair) are excluded; analysis is restricted to **non-sports** markets (§4.1).
- **Data/code availability:** the source states "The dataset will be made publicly available upon publication" (§4.1). **No code repository, no public dataset URL, and no data-availability statement exists in the pinned text** → these are `data gap`, not zero.
- **Duplicate-source note:** this record shares its first author and senior author with `polymarket-negrisk-executable-arbitrage-token-conversion-2026-09-03.md`, which cites a *different* manuscript (Gebele, Mutzel & Matthes, `arXiv:2608.00666`, Aug 2026). Source identities differ; see `## Related Wiki records` for the four-axis distinction.

## Economic mechanism

### Source-reported

Prediction-market venues independently describe the same real-world event in platform-specific natural language, with platform-specific oracles, cutoff times and dispute rules, and with no shared machine-verifiable event identifier. The authors call this **semantic non-fungibility**: economically identical claims cannot be netted or offset across venues, so arbitrage capital must be committed until resolution (§1, §6). The stated consequences are (i) liquidity fragments instead of pooling, (ii) prices reflect platform-local beliefs rather than a single global probability, and (iii) equivalent claims trade at persistent deviations from the Law of One Price (§1). The authors are explicit that the observed divergences **do not reflect disagreement about the underlying event** but a "structural failure of enforceability" (§1); §5.5 reinforces this using the 2024 U.S. presidential election, where information was effectively common knowledge and prices still failed to converge.

The paper formalizes four executable constructions over binary claims (§3): **single-platform YES/NO parity** (§3.2), **cross-platform conditional arbitrage** — buy YES on one venue and the corresponding NO on the other, yielding a unit payoff regardless of outcome (§3.3), **single-platform negative-risk arbitrage** over a mutually-exclusive-and-collective set (§3.4), and **cross-platform negative-risk / subset-superset arbitrage** over a shared atomic outcome space (§3.5, §3.6). A **subset relation** gives the same guarantee: YES on the superset market plus NO on the subset market spans the whole outcome space (§3.6).

### Research interpretation

Hypothesized mechanism, in falsifiable terms: **structural market fragmentation, not information, produces a persistent cross-venue relative-value signal on economically identical binary payoffs.** The tradable object is not a forecast of the event but a **capital-locked long/short (multi-leg) bundle whose unit payoff is deterministic at settlement**, with expected return equal to the execution-adjusted entry discount versus 1.0 annualized by the remaining time to resolution.

Component roles (source-reported roles; none is assumed to add alpha without ablation):

```text
Identity layer: cross-platform semantic equivalence / subset / negative-risk alignment
                (structural filter → top-20 embedding retrieval → two LLM verification passes)
Signal:         execution-adjusted parity violation, i.e. min{pY(mi)+pN(mj), pY(mj)+pN(mi)}
                outside [1 - Δij, 1 + Δij], with Δij = δ(mi) + δ(mj)
Confirmation:   deviation must persist ≥ 1 hour (Figures 6 and 8) / ≥ 30 min (Figure 9 case study)
Execution/risk: hold every bundle until resolution; no mark-to-market exit, no switching
```

Because the payoff is deterministic *conditional on venue/oracle/settlement integrity*, the residual risks the source leaves unpriced are **counterparty, oracle, dispute, regulatory and capital-lockup risks** — these are the falsifiable weak points of the thesis (see `## Evidence → Negative evidence`).

## Signal

- **Formation timestamp:** price observations are synchronized cross-platform snapshots in UTC (§4.1 "All timestamps are standardized to UTC"); assumption (ii) of §3 requires offsetting trades to be feasible "within a bounded latency window (accounted for empirically in §5)". **The numeric latency bound itself is not printed anywhere in the pinned text → `data gap`.**
- **Lookback:** none. The signal is a contemporaneous parity violation between two aligned markets; there is no historical window, warm-up or smoothing. The one temporal filter is a **persistence requirement** (below).
- **Long entry / short entry:** for an aligned pair `(mi, mj)`, buy the underpriced side of `min{pY(mi)+pN(mj), pY(mj)+pN(mi)}` — i.e. buy YES on the cheaper venue and NO on the more expensive venue (or the reverse), so that exactly one leg pays 1.0 at resolution (§3.3). For a subset pair, **YES on the superset + NO on the subset** (§3.6). For a negative-risk construction, buy the underpriced bundle: `π_YES = 1 − Σ(pY + δ)` (§3.5).
- **Exit:** **hold to resolution only.** Assumption (iv): "Arbitrage positions are held until market resolution." There is no stop, no take-profit, no time-based unwind and no partial close anywhere in the source.
- **Holding period:** from entry to the later (worst-case) resolution date. Reported as **days to weeks** in practice: the source notes semantically linked events "typically remain active for several weeks" against a median market life of "just over one day" (§5.1), and Figure 7 left is explicitly colored by "median time to resolution".
- **Re-entry:** the naive backtest (§5.4) "at each point in time … enters the single highest-yield equivalent-market arbitrage available and holds the position until resolution, **without switching or timing optimization**." Whether positions may overlap concurrently is **not stated → underspecified**.
- **Parameters (source-reported):**
  - Execution-friction parameter `δ(m) ≥ 0`, applied uniformly to YES and NO legs in every no-arbitrage bound (§3); in the empirical work it takes **platform-specific conservative values** from Appendix 0.I Table 3 (fee and spread columns listed under `## Execution assumptions`).
  - Structural filters: cross-platform only; one of **20 LLM-assigned semantic categories**; non-empty temporal overlap (§4.3).
  - Embedding retrieval: `text-embedding-3-large`, 3072 dimensions, **k = 20** nearest neighbours by cosine similarity (§4.3).
  - Negative-risk search: substitutions limited to **2–4 outcomes per partition**, at most the **top 1,000 substitution permutations** ranked by total trading volume per baseline event (§4.3).
  - Persistence screens: **≥ 1 hour** for Figures 6 and 8; **≥ 30 minutes** for Figure 9; Figure 6 uses the **top 1,000 relations by total trading volume**.
  - Yield definition: **"maximum guaranteed (worst-case) annualized arbitrage return", computed under worst-case (latest) resolution assumptions** (Figure 7 caption and §5.4).
- **Not specified by the source (→ `data gap` / `underspecified`):** position size or capital allocation per trade; whether the reported cumulative return compounds or is additive; concurrent-position netting; maximum simultaneous capital deployed; any ranking/tie-break rule when several constructions qualify at the same timestamp; any signal-strength threshold beyond the parity bound itself.
- The signal is therefore **reconstructable at the level of leg construction and cost bounds, but underspecified at the level of sizing and portfolio assembly.**

## Required data

- **Instrument / universe:** binary prediction-market claims (YES/NO) on non-sports events, across ten venues; categorical markets are represented as sets of binary claims; **scalar markets (temperatures, inflation) are explicitly excluded** (§3.1).
- **Venue:** Polymarket (Polygon), Omen/Presagio (Gnosis), Augur v1 (Ethereum), Limitless (Base), Myriad (Abstract/Linea/Celo), Seer (Gnosis/Ethereum), Truemarkets (Base), Kalshi (off-chain), Futuur (off-chain), PredictIt (off-chain) — Table 2 / Appendix 0.A, §4.1.
- **Market type:** fully collateralized binary contingent claims (prediction markets). **Not** spot, perpetual, futures or options; no funding, no margin, no leverage, no borrow in the source.
- **Timeframe:** event-level life-cycle data with UTC timestamps; price series at platform-native resolution (mid-quotes for CLOB venues; transaction-level on-chain reserve reconstruction for AMM venues).
- **Fields actually used (§4.1, Table 0.G):** market title, description, outcome labels, resolution metadata (oracle identity, cutoff time, dispute rules, scope qualifiers), category, validity window, mid-quote or reconstructed AMM price, daily trading volume, fee schedule, tick size, chain/block timestamps.
- **Data sources named in source (Table 0.G):** Polymarket Gamma API + the-graph subgraph (ID `81Dm16JjuFSrqz813HysXoUPvzTwE7fsfPk2RTf66nyC`) + Polygonscan; Etherscan RPC for Augur v1; Basescan + Limitless API; the-graph subgraph for Omen (ID `9fUVQpFwzpdWS9bq5WkAnmKbNNcoBwatMR4yZq81pbbz`); Polkamarkets API for Myriad; the-graph subgraph for Seer (ID `BMQD869m8LnGJJfqMRjcQ16RTyUw6EUx5jkh3qWhSn3M`) + Gnosisscan; Truemarkets API + Basescan; **Kalshi Trade API v2**; **Futuur API**; **PredictIt API (price data on request only)**.
- **Point-in-time:** market descriptions, oracles and resolution rules are read from the listing as captured; the paper makes no look-ahead claim for its descriptive statistics, but the **lifetime-maximum yield statistics in Figures 6–8 are ex-post maxima over the joint lifetime** (see `## Evidence → Source-reported`).
- **Timestamp / timezone:** UTC standardization stated; precision, clock source and out-of-order handling are **not stated → `data gap`**.
- **Missing data:** deterministic filters drop markets with missing temporal information, zero trading volume, or internally inconsistent records (§4.1); Omen markets open < 30 days are discarded (Table 0.G). **Imputation is not described.**
- **Cost fields:** observed/reconstructed fee schedules and bid–ask spreads per platform (Appendix 0.I); gas is inside `δ(m)` (§3); volume is used as the liquidity proxy ("geometric mean of normalized daily trading volume", Figures 6–7).
- **Currently unavailable:** the aligned dataset itself ("will be made publicly available upon publication") and any analysis code → **`data gap`.**

## Execution assumptions

**This source does model execution frictions — this is not an unmodelled-cost paper.** The cost determination below comes from a Methods-level read of §2.4 (Market Microstructure), §3 (formal model and assumptions (i)–(v)), §3.2–§3.6 (no-arbitrage bounds), §5.4 (execution-aware statistics), §5.5 (election case study) and Appendix 0.I (Table 3), plus a word-boundary scan of the pinned v1 text.

- **Cost model:** a single one-sided non-negative parameter `δ(m)` summarizing "bid–ask spreads, platform fees, gas costs, tick-size constraints, and slippage" (§3), applied to both YES and NO positions and summed across legs as `Δij = δ(mi) + δ(mj)`.
- **Appendix 0.I Table 3 — platform-specific fee and spread assumptions (source-reported, "conservative, standardized"):**

| Platform | Structure | Fee assumption | Spread assumption | Note |
|---|---|---|---|---|
| Kalshi | CLOB | 1.5% | $0.01 | dynamic fee schedule; conservatively fixed at 1.5% |
| Polymarket | CLOB | 0% | $0.01 (0.01–0.99) | $0.001 spread assumed near bounds |
| Polymarket | CPMM | 2% | 0 | — |
| Futuur | CLOB + LMSR | 6% | $0.01 | — |
| Omen | CPMM | 2% | 0 | — |
| Myriad | CPMM | 0–2% | 0 | market-specific fees considered |
| Truemarkets | AMM (Uni v3) | 0.8% | 0 | — |
| Limitless | CPMM | 1.5% | 0 | fees range 0.03–3%; conservatively fixed at 1.5% |

  Note: Table 3 covers the **7 of 10 platforms** used in the price-divergence analysis (§5.4); PredictIt and the remaining two venues are outside that analysis for want of reconstructable price/fee data → **`data gap`, never zero.**
- **Latency:** assumption (ii) requires synchronized snapshots with offsetting trades feasible "within a bounded latency window (accounted for empirically in §5)"; **the bound is not printed → `data gap`.**
- **Slippage:** in the 2024-election case study, footnote 7 states "Given the substantial depth observed on both venues, slippage is assumed negligible over the relevant horizons." **That assumption is scoped to the case study only**; no slippage model exists for the ecosystem-wide statistics beyond being folded into `δ(m)` without a numeric value → partly `underspecified`.
- **Market impact / participation / capacity:** word scan of the pinned body gives `market impact` in prose only, `participation`/`ADV` in prose only, and **no participation cap, no depth model, no capacity analysis** → `data gap`, never zero.
- **Order type / fill model:** not stated; the model presumes both legs can be entered on synchronized snapshots. Partial fills, failed legs and legging risk are **not modelled** → `data gap`.
- **Fees / funding / borrow / leverage / margin:** fees modelled as above; **`funding` 0 relevant hits, `leverage` 0, `margin` 0, `borrow` 0** — consistent with fully collateralized, long-only, hold-to-resolution bundles (no shorting of a single instrument; the "NO" leg is a purchased claim).
- **Capital:** "arbitrage positions require capital to be committed until resolution" (§8); the source calls such positions "capital-intensive and ill-suited to short-horizon price alignment" (§6). **No sizing rule, no capital utilization metric and no financing cost is given → `data gap`.**
- **Regulatory / access:** assumption (iii) requires the representative arbitrageur to "legally and operationally hold all required positions, including both YES and NO claims"; §5.5 discusses Kalshi serving primarily U.S. participants while Polymarket operates under different regulatory constraints. **Whether a single account/identity can hold both legs on both venues in practice is not demonstrated → `underspecified`.**
- **Settlement:** each market resolves under its own stated rules and "dispute and appeal processes are assumed to terminate" (assumption (v)). Oracle failure, dispute non-termination and platform default are **not modelled** → `data gap`.

## Evidence

### Source-reported

All figures below are third-party, source-reported, **not independently reproduced**, and trace to the pinned `arXiv:2601.01706v1`.

- **Dataset scale (§4.1, §5.1):** "over 100,000 unique events"; §5.1 gives the working denominator **102,275 events**; Table 0.G gives per-platform event counts Polymarket 29,651; Kalshi 59,176; Futuur 43,910; Omen 12,846; Limitless 5,560; PredictIt 4,381; Myriad 3,198; Augur v1 2,569; Seer 878; Truemarkets 562.
- **Overlap (§5.1):** "approximately **6%** of events" are involved in at least one cross-platform semantic relation, representing "nearly **10% of total event-days**"; median market life "just over one day" vs linked events "several weeks"; most linked events appear on 1–2 platforms, "a handful of events listed on up to eight platforms."
- **Relation inventory (§5.1):** **1,501 equivalence classes / 6,709 relations**; **1,645 subset-related event sets / 6,421 relations**; **1,123 negative-risk constructions / 2,771 markets**; mean internal connectivity 4.5 relations per equivalence class, 3.9 for subsets, 2.5 markets per negative-risk construction.
- **Venue concentration (§5.2):** approximately **8% of Polymarket's markets** have an equivalent counterpart elsewhere vs about **2% for Kalshi**; Kalshi and Polymarket dominate the equivalence network; directionality between them "nearly balanced."
- **Time trend (§5.3):** in 42-day windows, matched pairs rarely exceed **100** per window from 2018 through late 2022 and are almost entirely political; from early 2024 overlap rises sharply; "By 2025, windows routinely exceed **1,200–1,500** matched pairs."
- **Price divergence (§5.4, Figures 6–7):** using the **top 1,000 relations by total trading volume** and requiring deviations to persist **≥ 1 hour**, "even among the most liquid constructions, prices typically remain **2–4% away from execution-adjusted parity**" (right panel, median deviation); maximum deviations "decline only gradually with volume."
- **Yield distribution (§5.4, Figure 8):** execution-aware annualized return after platform fees and typical bid–ask spreads, requiring ≥ 1 hour persistence — "a substantial mass exceeds **200% APY**, and a non-trivial fraction exceeds **1,000%**." The source itself warns these large APYs "are driven primarily by short market horizonts until resolution rather than substantial mispricing" (§5.4, Figure 7 discussion).
- **Naive strategy backtest (§5.4):** "we simulate a naive, fully mechanical strategy starting in **2022**. At each point in time, the trader enters the single highest-yield equivalent-market arbitrage available and holds the position until resolution, without switching or timing optimization. Even under this restrictive policy and after accounting for all execution frictions, the strategy yields a **cumulative return of 1,218.66% over 800 days, across 15 completed trades**."
- **2024 U.S. election case study (§5.5, Figure 9):** Polymarket **$3.3B** cumulative volume, Kalshi **>$1B**; Polymarket ran a **zero-fee CLOB with $0.001 tick**, Kalshi **$0.01 ticks with no transaction fees on that market**; rolling three-hour min–max execution-adjusted spread, retaining deviations persisting **≥ 30 min**, **averages approximately $0.03 and reaches up to $0.07** for sustained intervals before the election-night call; depending on whether capital is released at Polymarket's call-based closure or Kalshi's inauguration-based resolution, these gaps correspond to "deterministic annualized returns ranging from **single-digit percentages to several hundred percent**."
- **Matching-quality evidence (§4.4):** structural filtering preserves **100%** of validated true relations; top-20 embedding retrieval captures **99.9%** of verified equivalence/subset relations (Appendix 0.C); two-stage LLM verification reduces the **false-positive rate below 2%**; human validation on **1,000 verification-stage instances** with **κ = 0.94** (one annotator); a second **1,000-pair** stratified end-to-end sample had "effectively perfect" agreement but is "heavily skewed toward true negatives." Full pipeline cost "on the order of **200 million tokens**" (§4.4).
- **Matching-quality caveat in source (§4.4):** residual errors are "primarily false negatives"; the one ex-post consistency check failure is the New York weather-station case (Kalshi resolves on NOAA Central Park, Polymarket on LaGuardia), "which reflects genuinely distinct semantics and was not correctly classified by both the human annotator and the framework" (§2.3, §4.4).
- **No Sharpe, no drawdown, no win rate, no turnover and no P&L distribution are reported anywhere in the pinned body** (word scan: `sharpe` 0, `drawdown` 0, `win rate` 0, `profit factor` 0, `turnover` 0). The only return statistic in the paper is the single 1,218.66% / 800-day / 15-trade cumulative figure above.

### Independently reproduced

Not independently reproduced. No code, no dataset and no replication package are published as of 2026-09-25 (`data gap`).

### Negative evidence

1. **The source's own framing limits the strategy's capacity:** divergence persists *because* arbitrage cannot be netted across venues and capital is locked until resolution (§6, §8). The mechanism that creates the signal is the same mechanism that blocks the trade — the paper offers no evidence that a real, single-identity trader can hold both legs on both venues legally and operationally (assumption (iii) is asserted, not demonstrated).
2. **Sample size of the only traded result is 15.** The 1,218.66% cumulative return rests on **15 completed trades over 800 days** — no distribution, no drawdown, no variance, no baseline and no significance test. Concentration in one or two events (2024 election, Figure 9) is plausible but not disclosed per trade → `underspecified`.
3. **Fees alone destroy a visible share of opportunities:** Figure 7 (right) shows a group of pairs at "fraction of time with an arbitrage" near zero because "execution costs — most notably platform fees on venues such as Futuur — fully absorb nominal price differences and eliminate arbitrage despite visible mid-quote deviations." Futuur's assumed fee is **6%** (Table 3).
4. **The headline APYs are horizon artefacts by the source's own admission:** "large APYs are driven primarily by short market horizonts until resolution rather than substantial mispricing" (§5.4).
5. **Lifetime-maximum statistics are ex-post:** Figures 6, 7 and 8 all use the **maximum** deviation/return over the joint lifetime of the aligned pair. A live trader cannot observe that maximum in advance; only the naive point-in-time strategy in §5.4 is described as contemporaneous, and its yield rule ("highest-yield available") is not formally defined relative to the ex-post maximum → `underspecified`.
6. **Residual false-positive rate < 2% on verified relations** (§4.4) means a small share of "aligned" pairs are not payoff-equivalent; one such misclassification is documented (NY weather stations). A single false equivalence converts a "risk-free" bundle into an unhedged directional position.
7. **Coverage gap:** the execution-aware analysis runs on **7 of 10 platforms** (§5.4); PredictIt price data is "on request only" (Table 0.G); Limitless CLOB markets were "ignored as they lacked on-chain tracability" (Table 0.G).
8. **No statistical inference anywhere:** no confidence intervals, no standard errors, no placebo, no multiple-testing control over the thousands of tested relations.
9. **No denominator reconciliation:** our count on Appendix 0.G sums the ten per-platform event counts to **162,731**, against §5.1's working denominator of **102,275 events** (difference **60,456**) and §4.1's "over 100,000 unique events". The paper does not reconcile platform instantiations with unique filtered events → `underspecified` (our count, arithmetic on printed Table 0.G cells).
10. **Unpublished data and code** make every printed number currently unverifiable outside the authors' pipeline.
11. **Related negative evidence in this repository** (different sources, same execution-honesty theme): `[[kalshi-prediction-market-pricing-wedge-executable-spread-falsification-2026-09-13]]` finds a headline prediction-market pricing wedge collapses to the spread under honest execution costs; `[[crypto-prediction-market-high-frequency-combinatorial-arbitrage-2026-09-01]]` documents combinatorial-arbitrage frictions on decentralized venues; `[[polymarket-binance-high-frequency-binary-lead-lag-2026-09-02]]` is a lead–lag signal, not a parity signal.
12. **None of the reviewed sources reports a failed independent replication of this specific paper**; absence is not evidence of no negative result.

## Falsification plan

Every threshold below is **research-defined (falsification threshold)** or **research-proposed (operationalization)** — none is stated by the source. Action on failure for all tests: **do not promote beyond `research-only`; record the failure in this file's Negative evidence section.**

- **F1 — Point-in-time reconstruction (leakage).** Rebuild the paired book using only quotes, resolution metadata and oracle rules available at each timestamp, with the match made from the listing text as of that timestamp (no hindsight re-listing or post-hoc rule edits). *Fail if:* the number of executable, ≥1-hour-persistent parity violations falls below **50%** of the source-reported count for the same window, **research-defined**.
- **F2 — Honest all-in cost ladder.** Re-price every leg with observed queue-position-aware spread, actual per-venue fee schedule, gas, and a **0 / 1 / 5 / 10 / 20 bp-equivalent (of notional) plus venue-fee** ladder, alongside a **30 bps per round trip** slippage stress. *Fail if:* fewer than **20%** of the source's ≥200% APY opportunities remain strictly positive after costs at the median rung, **research-defined**.
- **F3 — Capacity / depth screen.** Cap each entry at **10% of the lesser leg's displayed depth** at the touch. *Fail if:* realized executable notional is below **10%** of the notional implied by the printed mid-quote statistics, or median achieved gap is below **50%** of the printed gap, **research-defined**.
- **F4 — Fifteen-trade statistical honesty.** Recompute the naive strategy with per-trade capital weights printed, plus a bootstrap over the 15 trades (1,000 draws). *Fail if:* the 95% interval of cumulative return includes **0**, or the single largest trade contributes **>50%** of total P&L, **research-defined**.
- **F5 — Baseline comparison.** Compare against (a) doing nothing with the same capital locked, and (b) a same-duration risk-free/short-term T-bill proxy, over the identical calendar. *Fail if:* the strategy's excess over (b) is non-positive on a capital-weighted basis, **research-defined**.
- **F6 — Event-identity placebo.** Repeat the whole pipeline with **20% of matched pairs randomly re-paired** across venues within the same category and time window (1,000 draws). *Fail if:* the observed median execution-adjusted deviation does not exceed the **95th percentile** of the placebo distribution, **research-defined**.
- **F7 — Matching-error stress.** Inject the source's own **<2% false-positive rate** (and a 2× stress at 4%) by randomly flipping that share of equivalence labels to independent. *Fail if:* expected loss from mislabelled bundles erases **>25%** of gross strategy P&L, **research-defined**.
- **F8 — Single-identity feasibility audit.** Prove that one legal identity can open and hold both legs on both venues for at least **20** randomly sampled aligned pairs, with documented account, KYC/geo, withdrawal and collateral constraints. *Fail if:* fewer than **80%** of sampled pairs are jointly feasible, **research-defined**.
- **F9 — Resolution/oracle risk accounting.** Track dispute, oracle-failure, platform-delay and default events across the sample. *Fail if:* any loss event exceeds **10%** of realized strategy P&L, or if assumption (v) (disputes terminate) is violated in the sample, **research-defined**.
- **F10 — Ex-post vs live yield gap.** Compare the live point-in-time "highest-yield available" rule against the printed lifetime-maximum distribution (Figures 6–8). *Fail if:* live entry yields are below **30%** of the printed maximum-APY levels at the median, **research-defined**.
- **F11 — Regime / category breakdown.** Split by 2022–2023 vs 2024–2025, by political vs non-political, and by venue pair. *Fail if:* the effect is absent (median execution-adjusted deviation ≤ the venue-fee floor) in **≥2 of 3** splits, **research-defined**.
- **F12 — Forward frozen window.** Freeze at **2025-09-01** and evaluate only data produced afterwards, with the same cost table and the same ≥1-hour persistence rule. *Fail if:* fewer than **10** executable constructions appear over **6 months** or their median net annualized return is non-positive, **research-defined**.
- **F13 — Multiple-testing audit.** Apply Benjamini–Hochberg at **q < 0.10** across the full set of tested relations. *Fail if:* the surviving set does not retain at least **50%** of the constructions used for the headline statistics, **research-defined**.

## Crypto portability

**Verdict: `adapted`.**

- Seven of the ten analysed venues are on-chain and crypto-denominated (Polymarket/Polygon, Augur/Ethereum, Omen & Seer/Gnosis, Limitless & Truemarkets/Base, Myriad/Abstract-Linea-Celo), collateralised in USD/stablecoin terms, so a **crypto-venue implementation of the same mechanism sits inside the source's own evidence base**. The mechanism — identity fragmentation sustaining cross-venue price gaps — is exactly what the source measures on those venues.
- However, the source contains **no crypto spot or perpetual evidence**: it does not analyse BTC/ETH spot books, perpetual funding, mark/index basis, liquidation, or cross-exchange crypto arbitrage. Porting the *parity-bundle* logic to crypto spot/perpetual pairs (e.g. Polymarket vs CEX threshold options) is a **ported hypothesis, not crypto empirical evidence** — cf. `[[crypto-cross-platform-binary-threshold-mispricing-polymarket-binance-2026-09-01]]` for a distinct source that does test a crypto/threshold pairing.
- Crypto-specific risks absent from the source: **funding** (not applicable to these collateralized claims, but central to any perp adaptation), **mark/index price and liquidation**, **venue fragmentation beyond the ten listed venues**, **24/7 session structure and candle-boundary conventions** (the source is event-lifecycle based, UTC-stamped, and does not rely on session boundaries), **custody/withdrawal and bridge risk for multi-leg bundles**, **stablecoin de-peg and collateral conversion** (PredictIt/Kalshi are fiat, Polymarket/Omen are USDC-style collateral → an FX/collateral wedge is unmodelled), and **smart-contract/oracle risk** (UMA optimistic oracle 2 h challenge window, Reality.eth + Kleros, Pyth, REP disputes — Appendix 0.A).
- "Crypto portability" is not authorization to trade.

## Limitations

- `underspecified` — position sizing, capital allocation, compounding convention, concurrency of open bundles and the exact definition of the point-in-time "highest-yield" rule.
- `underspecified` — the numeric latency window required by assumption (ii), though §5 claims it is "accounted for empirically."
- `data gap` — no published dataset, no code, no data-availability statement as of 2026-09-25.
- `data gap` — no market-impact, participation, capacity, fill or partial-legging model; slippage given a numeric value only in the election case-study footnote.
- `data gap` — clock precision, out-of-order record handling, and per-trade venue-level P&L are never printed.
- `not independently reproduced` — every number in this record is source-reported.
- `unproven` — the single traded result is 15 trades over 800 days with no variance, no drawdown, no baseline and no significance test.
- `underspecified` — denominator reconciliation: our count of Appendix 0.G per-platform event cells is **162,731** vs §5.1's **102,275** (Δ **60,456**), unexplained in source.
- Sample-period concentration: cross-platform duplication is "negligible" before 2024 (§5.3), so the economically meaningful window is essentially **2024–2025** — a short, favourable regime that includes one exceptional event (2024 U.S. election).
- Survivorship/selection: platform inclusion requires ≥50 markets with lifetime volume >$500 and excludes play-money and sports venues; zero-volume and temporally incomplete markets are dropped (§4.1) → an ex-post liquidity/survival filter.
- Legal/operational feasibility of holding both legs on both venues is an **assumption, not a demonstration** (assumption (iii) vs §5.5).
- Preprint status: single manuscript, no peer review, no published venue, no citation context.
- **Incremental-write check:** no existing record in this repository shares this source identity (`2601.01706`, its DataCite DOI, either exact title variant, or the phrase "Semantic Non-Fungibility") — repo-wide hidden-inclusive search across all 2,546 `.md` files including `.mimo-worktrees`, `.agents`, `.hermes`, plus `coverage_manifest.csv`, returned **0 hits before this write**. The only same-author hit is the *different* manuscript `2608.00666`.

## Implementation status

`not-implemented`. Nothing in this record has been implemented in our research stack. No venue adapter, no semantic matcher, no parity scanner, no backtest, no Qlib run, and no Paper/Testnet/Live workflow exists for this hypothesis. This file is a research capture only.

## Adoption boundary

Presence in this repository means only that a normalized research capture was pushed to the public staging pool. It does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. `status: research-only`, `implementation_status: not-implemented`, `adoption: not-approved`, `approval_scope: research-only`.

## Related Wiki records

Verified via Wiki Brain `kb_search` this run (only pages returned by the vault are linked; nothing is fabricated). Query `prediction market` returned 8 pages and query `negative risk arbitrage executable arbitrage Polymarket Kalshi` returned 3 pages; query `prediction market cross-platform arbitrage price divergence` returned **0 pages** (no dedicated prior record for this exact mechanism).

- `[[quant/kalshi-prediction-market-pricing-wedge-executable-spread-falsification-2026-09-13]]` — adjacent on execution-friction falsification, but single-venue (Kalshi) and a pricing-wedge hypothesis rather than cross-venue parity.
- `[[quant/crypto-prediction-market-high-frequency-combinatorial-arbitrage-2026-09-01]]` — adjacent on arbitrage mechanics, but high-frequency combinatorial/within-venue and retail-liquidity focused.
- `[[quant/polymarket-binance-high-frequency-binary-lead-lag-2026-09-02]]` — adjacent venue family; the signal is lead–lag timing, not a parity bound.

**Four-axis distinction (source identity × mechanism × signal construction × data dependency):**
1. vs `polymarket-negrisk-executable-arbitrage-token-conversion-2026-09-03` (Gebele, Mutzel & Matthes, `arXiv:2608.00666`) — same first/senior author, **different manuscript**; that record is within-platform NegRisk token conversion on Polymarket, this record is an ecosystem-scale **cross-platform** identity/parity study across ten venues with its own dataset, its own formal model (§3.3/§3.5/§3.6) and its own cost table (Appendix 0.I).
2. vs `crypto-cross-platform-binary-threshold-mispricing-polymarket-binance-2026-09-01` (`arXiv:2606.19517`) — different source; that pairs a prediction market with a **crypto derivative** (Binance threshold options) and delta-hedging, this pairs **venue-to-venue same-event claims** with a hold-to-resolution bundle.
3. vs `kalshi-prediction-market-pricing-wedge-executable-spread-falsification-2026-09-13` (GitHub `elraffaello123-art/quant-research` @ `511fab8`, SSRN 6468338) — different source and different hypothesis class (Wang-transform wedge / FLB / digital VRP on one venue, falsified).
4. vs `prediction-market-lead-lag-llm-semantic-risk-filtering-2026-09-03` (`arXiv:2602.07048`) — different source; time-series lead–lag signal with an LLM risk filter, not an identity/parity construction.

## Sources

1. Jonas Gebele, Florian Matthes, "Semantic Non-Fungibility and Violations of the Law of One Price in Prediction Markets," arXiv preprint `arXiv:2601.01706v1 [cs.CE]`, submitted 5 January 2026 01:01:52 UTC (sole version as of 2026-09-25). https://arxiv.org/abs/2601.01706
2. Pinned full text (arXiv HTML v1, 291,445 bytes, SHA-256 `22b8180777772515e3b6b4bec94d72fe00a3fc769959bf93615cee273da49890`): https://arxiv.org/html/2601.01706v1
3. Pinned PDF v1 (3,538,362 bytes, SHA-256 `4f982f3b7958f697ce2656c62ebcd02e2260fff23f185bbaa4e8fa8a523c8214`): https://arxiv.org/pdf/2601.01706v1
4. arXiv-issued DataCite DOI `10.48550/arXiv.2601.01706`, resolving to the abs page (HTTP 200, checked 2026-09-25): https://doi.org/10.48550/arXiv.2601.01706
