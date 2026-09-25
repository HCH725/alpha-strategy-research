---
schema: strategy-research-record-v1
title: "Topological Risk Parity (TRP): rooted-MST signed-signal topology allocator with non-conservative propagation (arXiv:2604.16773v1)"
created: 2026-09-26
updated: 2026-09-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - arxiv
  - portfolio-construction
  - hierarchical-allocation
  - risk-parity
  - minimum-spanning-tree
  - long-short
  - market-neutral
  - signal-overlay
  - falsification
  - negative-evidence
status: research-only
confidence: medium
source_as_of: 2026-09-26
sources:
  - "arXiv:2604.16773v1 [q-fin.PM], 'Topological Risk Parity', Revant Nayar, Dnyanesh Kulkarni, El Mehdi Ainasse (abs metadata author order); submitted Sat, 18 Apr 2026 01:35:40 UTC (15 KB); https://arxiv.org/abs/2604.16773 (abs read 2026-09-26)"
  - "https://arxiv.org/html/2604.16773v1 — pinned v1 HTML, 244,697 bytes, SHA-256 1859701253442551d4a774aa2907a53d5ef79a72c24311b0cd299403b230210d (retrieved and hashed 2026-09-26); stripped body 725 lines / 40,642 characters read end to end for this record"
  - "https://arxiv.org/pdf/2604.16773v1 — pinned v1 PDF, 381,082 bytes, SHA-256 2a199eef59482720bf9638b2ee812bb5741f4094477ef7bf3ef95570face1a45 (retrieved and hashed 2026-09-26; embedded /Title 'Topological Risk Parity', /Producer 'pikepdf 8.15.1', no CreationDate object found → PDF creation date is a data gap)"
  - "https://doi.org/10.48550/arXiv.2604.16773 — arXiv-issued DataCite DOI, HTTP 200 on resolution (checked 2026-09-26)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions:
  - "Source-internal (pinned v1): the HTML document date line reads 'August 24, 2026', but the arXiv submission history shows only '[v1] Sat, 18 Apr 2026 01:35:40 UTC (15 KB)' and the arXiv API reports published = updated = 2026-04-18; abs and html for v2 both return HTTP 404 (all checked 2026-09-26). A manuscript cannot be dated four months after its own v1 submission, so at least one of the two dates is wrong. The pinned text never explains the gap (a plausible but unstated cause is a `\\date{\\today}` resolved at HTML rendering time). This record keeps both dates and marks the discrepancy `underspecified` rather than picking one."
  - "Source-internal (pinned v1): author order differs between surfaces. The abs page / arXiv API print 'Revant Nayar, Dnyanesh Kulkarni, El Mehdi Ainasse', while the pinned HTML byline prints 'Revant Nayar, El Mehdi Ainasse, Dnyanesh Kulkarni'. The complete author list is the same three names in both surfaces (all three affiliated to FMI Technologies LLC in the HTML byline), so this is an ordering discrepancy, not a membership discrepancy."
  - "Source-internal (pinned v1): Appendix B 'Recommended terminology' states that 'topological risk parity' should be used 'only for conservative, risk-based variants, not for the generic TRP-MST construction when ρ < 1', yet the title, abstract and §5.1 use 'Topological Risk Parity' for the generic non-conservative allocator itself. The paper therefore names the headline method with a term its own appendix says is reserved for the ρ = 1 risk-parity limit; no risk budgeting, volatility target or risk measure appears anywhere in the pinned text. This record uses 'TRP' as the framework name and treats the 'risk parity' label as a naming claim, not a demonstrated property."
---

# Topological Risk Parity (TRP): rooted-MST signed-signal topology allocator with non-conservative propagation (arXiv:2604.16773v1)

## Provenance

**Primary source.** arXiv:2604.16773**v1**, category `q-fin.PM` (sole category, no cross-lists), title *Topological Risk Parity*. Complete author list exactly as printed: **Revant Nayar**, **Dnyanesh Kulkarni**, **El Mehdi Ainasse**, all three with the affiliation *FMI Technologies LLC* in the pinned HTML byline (abs metadata orders the same three names differently — see `contradictions`). The submission history shows a single version `[v1] Sat, 18 Apr 2026 01:35:40 UTC (15 KB)`. `https://arxiv.org/abs/2604.16773v2` and `https://arxiv.org/html/2604.16773v2` both return **HTTP 404** (checked 2026-09-26), so v1 is the sole and latest version as of 2026-09-26. The HTML document date line reads `August 24, 2026`, which conflicts with the April submission date (recorded in `contradictions`, `underspecified`).

**Metadata / status.** The abs page has **no Comments field**, **no journal-ref**, and **no publisher DOI** beyond the arXiv-issued DataCite DOI `10.48550/arXiv.2604.16773` (resolution HTTP 200, checked 2026-09-26). No peer-review, acceptance or journal-submission statement appears anywhere in the pinned body. License line in the pinned HTML: **CC BY-NC-SA 4.0** (non-commercial share-alike), so the text is cited and normalized here rather than reproduced at length. Publication status = **preprint only** (`not stated in source` for any journal). The paper carries a standard *informational purposes only / not investment advice* disclaimer and a limitation-of-liability disclaimer.

**Pinned snapshots.** Pinned HTML `https://arxiv.org/html/2604.16773v1` = **244,697 bytes, SHA-256 `1859701253442551d4a774aa2907a53d5ef79a72c24311b0cd299403b230210d`**; pinned PDF `https://arxiv.org/pdf/2604.16773v1` = **381,082 bytes, SHA-256 `2a199eef59482720bf9638b2ee812bb5741f4094477ef7bf3ef95570face1a45`**; both retrieved and hashed 2026-09-26. The stripped HTML text is **725 lines / 40,642 characters** and was read end to end: Abstract, §1 Introduction, §2 Related background, §3 MSTs and Passive/Factor Flows, §4 Setup and notation (§4.1 Activity filter, §4.2 Correlation distance and the MST), §5 TRP (§5.1 Variant I, §5.2 Variant II), §6 Theoretical properties (§6.1–§6.4), §7 Practical implications and benefits (§7.1–§7.3), §8 Conclusion, Appendix A–C (including C.1–C.3), Table 1, References [1]–[5], Disclaimer.

**Document structure and the cost judgment.** This is a **theory-only paper**: there is no Methods section, no Experimental Setup, no Results section, no dataset, no sample period, no simulation and no backtest — the nearest thing to an experimental statement is Remark 5's sentence that combinatorial changes in the MST, root and active set "should be handled empirically", i.e. future work. Because a Methods-level cost read is required, the entire pinned body was additionally word-scanned (case-insensitive counts over the 40,642-character stripped text): `transaction cost` **0**, `transaction` **0**, `slippage` **0**, `bid-ask` **0**, `spread` **0**, `commission` **0**, `turnover` **0**, `rebalanc` **0**, `backtest` **0**, `sharpe` **0**, `drawdown` **0**, `cagr` **0**, `annualized` **0**, `latency` **0**, `market impact` **0**, `capacity` **0**, `margin` **0**, `borrow` **0**, `liquidation` **0**, `fill` **0**, `win rate` **0**, `t-statistic` **0**, `p-value` **0**, `simulation` **0**, `dataset` **0**, `sample period` **0**, `data` **0**. Four superficial hits are arXiv page chrome or disclaimers, not body content: `feedback` (arXiv HTML "Report Issue" widget), `funding` ("Major funding support from"), `Experimental support` (LaTeXML build-log widget), and the single body hit of `empirical` (Remark 5, quoted above). **No cost, fill, spread, funding, leverage-of-execution, capacity or performance model exists in the source at all**; every such field below is a `data gap` and is never treated as zero-cost or frictionless-by-claim.

**Code and data.** §7.2.4 refers to "a genuine implementation feature of the current code", so an implementation exists, but the pinned text contains **no repository URL, no commit, no code-availability statement, no dataset, no data vendor and no data-availability statement** (the three `github` string hits are arXiv template widgets). Every reproducibility field is a `data gap` and this record cites no code SHA.

**Data as-of.** No market data is used or cited by the source, so there is no source data as-of date (`data gap`). `source_as_of: 2026-09-26` is the date the primary source was pinned and verified.

**Repo-wide dedup (run 2026-09-26, before writing).** `git pull origin main` fast-forwarded `6c1dfe7..51317da` (another scout had pushed `tradingview-rsi-filtered-jaws-vwap-mean-reversion-2026-09-26.md`); `git status --porcelain --untracked-files=no` was **clean** before research began, and `git log --oneline -20` was inspected as a convenience glance only. A hidden-inclusive `rg --hidden --no-ignore` scan then walked **all 2,551 `*.md` files** in the repository (including `.mimo-worktrees`, `.agents`, `.hermes`) plus `coverage_manifest.csv` (5,808 lines), testing 11 source-identity patterns: `2604.16773`, `10.48550/arXiv.2604.16773`, `Topological Risk Parity`, `topological risk parity`, `Revant Nayar`, `Dnyanesh Kulkarni`, `El Mehdi Ainasse`, `FMI Technologies`, `TRP-MST`, `Semi-Supervised TRP`, `split-replication`. **Both scans returned exit 1 = zero matches** in `*.md` and zero in `coverage_manifest.csv`. Mechanism probes were then cleared as unrelated: `minimum spanning tree` / `MST` / `Mantegna distance` resolve only to `stn-tgat-nmi-soft-threshold-graph-attention-topk-ranking-2026-09-04.md` (which criticises MST hard-thresholding as fragile — used below as cross-record negative evidence, different source) and to a Tumminello–Mantegna citation in `equity-cross-sectional-homological-neural-network-mfcf-ranking-2026-09-02.md`; `topological`/`topology` hits (40) are persistent-homology, spectral-network, semantic-network and supply-chain records, none of which shares this source identity or the rooted-MST signed-signal propagation mechanism. No existing record for this source identity exists, so no material-distinction argument against a same-source record is required; the four-axis distinction against the nearest *mechanism* neighbours is stated under **Related Wiki records**.

## Economic mechanism

### Source-reported

The source (abstract, §1, §3, §5, §7) argues:

- **Passive and factor flows create tree-like dependence.** With returns decomposed into nested market / sector / basket shocks (§3, eq. 2–6), correlations satisfy `ρ_same basket > ρ_same sector > ρ_different sector`, so Mantegna distances `D_ij = sqrt((1-ρ_ij)/2)` become tiered and a minimum spanning tree extracts a natural sparse backbone of `n_A - 1` edges (§3, §4.2). As λ → 1 in the §3 "dominance knob" parameterization the tiers separate cleanly and the MST backbone becomes more stable; as λ → 0 the MST becomes sample-noise-driven.
- **TRP is an allocator, not a signal.** Given an exogenous signed signal vector `s` and a rooted tree, each node `v` receives a topological factor `g_v = ∏_{u ∈ Path(root→v)} α_u(ρ)` with the propagation coefficient `α_u(ρ) = (1-ρ) + ρ/b(u)` (§5.1 eq. 10–12, Appendix A eq. 16), where `b(u)` is the branching number. Pre-normalization position is `x_v = s_v · g_v` (the original signal, explicitly *not* volatility-rescaled, §5.1 Step 5), then `w_v = L · x_v / ‖x‖₁` to target gross leverage `L` (eq. 13).
- **Non-conservation is deliberate.** The sum of child factors is `β_u(ρ) = b(u)(1-ρ) + ρ ≥ 1`, with equality only if `b(u) = 1` or `ρ = 1` (Proposition 4, Corollary 1), so branching expands aggregate descendant factor mass whenever `ρ < 1`. ρ interpolates continuously from raw-signal allocation at `ρ = 0` (Proposition 3a) to conservative equal-split allocation at `ρ = 1` (Proposition 3b).
- **Two variants.** *Variant I (TRP-MST)*: MST on the active universe, then a root chosen by hub mode (maximal degree), max-magnitude mode (max `|s_i|`) or fixed-index mode (§5.1 Step 2). *Variant II (TRP-SPY/XL, "Semi-Supervised TRP")*: a dummy SPY root with signal 0 and zero returns, sector ETFs identified by the ticker prefix `XL` (XLK, XLF, XLE named) connected directly to the root, DFS extracts a rooted spanning tree from the resulting cyclic graph, then post-processing `clip(w_i, ±c)` and `w_i ← 0 if |w_i| < η` (§5.2, eq. 14); if no `XL*` name is active, a fallback builds the MST on the augmented universe including the zero-return dummy node (Case B).
- **Stated benefits versus HRP (§7.1, Table 1, abstract).** Support for long/short market-neutral books because sign is preserved (Proposition 5), an explicit market/sector/industry ontology instead of an emergent binary dendrogram, sparsity and interpretability, the ρ control lever, no covariance inversion and no cluster-variance recursion, easy append of caps/thresholds/neutralization, and — as an unquantified claim — being "much more robust to macroeconomic shocks and crises, where within-cluster correlations might spike" (abstract; §7.1 benefit 8).
- **Stated caveats (§7.2).** Root choice can change the entire allocation; the MST is combinatorially unstable under small correlation changes; a single tree discards all but `n_A - 1` edges; the sector-anchored DFS is order-dependent for non-sector nodes (Remark 4); the zero-return dummy-root fallback is "pragmatic, not canonical".

### Research interpretation

The falsifiable hypothesis is **topology-conditioned exposure shaping**: for a *fixed* signed cross-sectional signal, attenuating each name's weight by the product of branching-dependent factors along its path in a dependence-derived rooted tree tilts the book away from crowded, highly connected clusters toward more idiosyncratic names, improving risk-adjusted (net) performance relative to (i) the same signal allocated raw (`ρ = 0`, the source's own baseline, §7.3.4) and (ii) hierarchical cluster-variance allocators such as HRP — while preserving signal sign, so it is usable on long/short market-neutral books.

Component roles (hybrid structure, per README):

```text
Regime / structure estimator: correlation matrix on the active return history → Mantegna distance → MST (or SPY + XL* sector-ETF anchored spanning tree)
Allocation layer: signed signal × path product of α_u(ρ) = (1-ρ) + ρ/b(u), then L1 normalization to gross leverage L
Post-processing (Variant II only): weight clip ±c, small-weight prune |w| < η
Risk / exit logic: none specified by the source
Alpha signal: none supplied by the source — entirely exogenous
```

Critically, this is a **portfolio-construction / risk-allocation overlay, not an alpha signal** (README rule 8): the paper contains no predictive claim of its own, so any "alpha" attributed to TRP must come from the interaction of the allocator with an external signal and must be established by ablation against `ρ = 0`. The paper's macro-shock robustness language is a qualitative claim with no supporting experiment. "Risk parity" in the name is, on the pinned text, a label: no risk budget, volatility target, variance share or risk measure enters the formulas (see `contradictions`, Appendix B).

## Signal

**Formation timestamp.** `data gap` / `underspecified`: the source defines no signal formation time, no tradable timestamp, no timezone and no publication/availability convention. The allocator consumes whatever signed vector `s` is current at rebalance time; the rebalance cadence itself is never specified.

**Lookback.** The correlation matrix `C = corr(R^(A))` is formed over a return history of `T` observations for the active assets (§4.2), with `T` never given a value or a unit (days? bars?). The activity filter uses `m_i = (1/k) Σ_{t=T-k+1}^{T} |r_it|` over a lookback `k ≤ T` (§4.1) with `k` never given a value. Endpoint inclusivity is written as `T-k+1 … T` (inclusive both ends). Warm-up period: `data gap`.

**Entry (activity filter).** Active set `A = { i : m_i > ε AND |s_i| > τ }` (eq. 8); **the only parameter value printed anywhere in the paper is the baseline `τ = 10⁻³`** (§4.1). `ε` is declared as "a minimum recent-magnitude threshold ε > 0" with no value. Inactive assets receive **zero** weight (§5.1 Step 6) — the filter is a hard universe cut, not a size scale.

**Signal itself.** `s_i ∈ ℝ` is an arbitrary signed cross-sectional signal; the source specifies **no** signal construction, no lookback for it, no sign convention beyond "signed", and no tie/simultaneous-signal handling → the alpha input is `underspecified` by construction (the paper is deliberately signal-agnostic).

**Long / short entry.** Sign of `s_i` is preserved into `w_i` whenever `g_v > 0` (always) and clipping does not zero the name (Proposition 5, §7.3.1). Long and short legs are therefore the positive and negative components of the exogenous signal; the paper gives no separate long/short entry rules.

**Exit.** `data gap`: no exit rule, no stop, no take-profit, no time-based exit. Positions persist until the next (unspecified) re-allocation.

**Holding period / re-entry / overlapping positions.** `data gap` / `underspecified` — no cadence, no overlap treatment.

**Parameters (complete inventory of what the source actually fixes).**

| Parameter | Source value | Status |
|---|---|---|
| Signal threshold `τ` | `10⁻³` (baseline) | source-reported |
| Activity threshold `ε` | declared, no value | `data gap` |
| Filter lookback `k` | declared, no value | `data gap` |
| Correlation history `T` | declared, no value | `data gap` |
| Propagation `ρ ∈ [0,1]` | range and limits given, **no default / no tuning rule** | `data gap` |
| Gross leverage `L > 0` | declared, no value | `data gap` |
| Clip cap `c`, prune threshold `η` (Variant II) | declared, no value | `data gap` |
| Root rule (Variant I) | three modes offered (hub / max-magnitude / fixed-index), **no default** | `data gap` |
| Sector identification (Variant II) | ticker prefix `XL` | source-reported |
| Correlation handling | clip `C` to [-1,1], NaN→0, symmetrize (§4.2) | source-reported |
| MST algorithm | Kruskal [3] / Prim [4] cited; tie-breaking rule `data gap` | partly source-reported |
| Neutrality at sector/industry/factor layer | described as possible via `Σ w_i = 0` at a layer (§5.2) | source-reported as capability, no algorithm |

Because ρ, `L`, `ε`, `k`, `T`, `c`, `η` and the root rule are unfixed, **the source does not define one reproducible trading rule**; it defines a parameterized family. Any concrete instantiation used later must be labeled `research-proposed`.

**Specification status:** allocator formulas fully specified (eq. 8–16, Props. 1–10, Thm. 1); executable end-to-end rule **underspecified** (signal, cadence and all numeric parameters except `τ` missing).

## Required data

- **Instrument / universe:** cross-sectional equity-like return panel for the active set. Variant II presumes an index-proxy root (SPY) plus `XL*` sector ETFs present in the universe; §5.2 mentions GICS labels and industry/sub-industry ETFs as alternative anchors. No concrete universe, no inclusion/exclusion rules, no liquidity or minimum-mcap filter, no reconstitution schedule (`data gap`).
- **Venue / market type:** not stated (`data gap`); the framing is US equities/ETFs (SPY, XLK, XLF, XLE named in §5.2).
- **Timeframe:** return history frequency never stated — daily is implied by ETF/sector framing but **not declared** (`data gap`, do not treat as source-reported).
- **Fields:** historical returns `R ∈ ℝ^{N×T}` (log-returns permitted, §4) for the correlation structure; the signed signal vector `s`; ticker strings for the `XL` prefix test; optional sector/industry/factor membership labels for the anchored variant and for neutrality constraints.
- **Not required by the source:** order book, depth, open interest, funding, mark/index/basis, options surface, borrow — the allocator never touches them (their absence is a property of the model, not a claim that they are irrelevant to execution).
- **Point-in-time:** not discussed at all — no look-ahead, availability-lag or revision treatment (`data gap`). Correlation and MST inputs must in practice be lagged to the decision time; that is a `research-proposed` repair, not a source rule.
- **Timestamp / timezone:** `data gap`.
- **Missing data:** only the entry-wise `NaN → 0` correlation substitution (§4.2). No stale/suspended/partial-bar handling (`data gap`).
- **Funding / fee / spread needs:** `data gap` — the source models none (see Execution assumptions).

## Execution assumptions

The paper contains **no execution model whatsoever** (Methods-level word scan in Provenance: every cost/fill term = 0 occurrences). Therefore, for every field the source is silent:

- **Signal-to-order timing / next-bar vs same-bar:** `data gap`.
- **Order type and fill model:** `data gap` (market vs limit, partial fills, failures: not stated).
- **Fees, commissions, spread, slippage:** `data gap` — never zero; no number appears in the source.
- **Market impact / participation / capacity / latency:** `data gap`.
- **Funding, borrow, shorting availability, leverage/margin:** `data gap` for *execution*; note `L > 0` is a *target gross leverage* normalization (§5.1 Step 6), not a margin or financing model, and long/short books implicitly require borrow the source never prices.
- **Position limits:** only the post-processing clip `|w_i| ≤ c` and prune `|w_i| < η` in Variant II (values `data gap`); Variant I has no cap.
- **Qualitative execution note (source-reported):** §7.1 says final weights "drop out in one pass as a vector that can be clipped, thresholded, sector-neutralized, and rescaled to the desk's risk limits" — a capability claim, not a fill or cost model.

Because costs are entirely unmodeled, **no number in this record may be read as gross or net of cost**; there are no numbers. Any future evaluation must add a cost model explicitly labeled `research-proposed`.

## Evidence

### Source-reported

**There are no performance results in the source.** No Sharpe, no return, no CAGR, no drawdown, no win rate, no turnover, no IC, no t-statistic, no p-value, no baseline comparison table, no sample period, no universe instance, no simulation — all confirmed by the body-wide scan in Provenance (`sharpe`/`drawdown`/`backtest`/`win rate`/`t-statistic`/`p-value` = 0 occurrences). The only table in the paper (Table 1) is an explicitly **conceptual** feature comparison of TRP-MST / TRP-SPY-XL / classical HRP (structure, L/S support, root, second layer, propagation object, local conservation, sign use, covariance inversion, cluster-variance recursion, economic priors).

What the source does report is **theory** (source-reported, unverified by us):

- Proposition 1: `0 ≤ D_ij ≤ 1`, with `D_ij = 0` iff `C_ij = 1` and `D_ij = 1` iff `C_ij = -1`.
- Proposition 2 (path formula) and Proposition 3 (limits: `ρ = 0` → normalized raw-signal allocation; `ρ = 1` → conservative equal-split).
- Proposition 4 / Corollaries 1–2: `Σ_{v ∈ Ch(u)} g_v = β_u(ρ)·g_u`, `β_u(ρ) = b(u)(1-ρ) + ρ ≥ 1`, and level-mass bound `Σ_{v ∈ L_ℓ} g_v ≤ Γ_B(ρ)^ℓ` with `Γ_B(ρ) = B(1-ρ) + ρ`.
- Proposition 5 (sign preservation absent clipping) and Proposition 6 (scale symmetry: `w(cs) = w(s)` for `c > 0`, `w(cs) = -w(s)` for `c < 0`).
- Propositions 7–8: sector ETFs land at depth one under the dummy root; the augmented graph is connected and DFS yields a spanning tree (both proofs assume the edge set that makes the claim true — see Negative evidence).
- Proposition 9: `(1-ρ+ρ/B)^{d_v} ≤ g_v ≤ 1`, hence `(1-ρ)^{d_v} ≤ g_v ≤ 1` — topology only attenuates along a path.
- Proposition 10: Variant I output is independent of the subtree-mass exponent `p`.
- Theorem 1: conditional `L¹` Lipschitz stability of `F(s) = L·D_g s / ‖D_g s‖₁` with constant `2L/γ`, explicitly **conditional on a fixed tree, active set and root** (Remark 5: it "does not claim global continuity across changes in the MST, root, or active set").

All abstract-level benefit claims (robustness to macro shocks, reduced unintended factor bets, "close in spirit to HRP but markedly different", well-suited to market-neutral/stat-arb books) are **qualitative and untested in the source**.

### Independently reproduced

not independently reproduced

### Negative evidence

1. **Zero empirical evidence of any kind.** The source reports no backtest, no simulation, no sample, no benchmark and no performance metric; the entire benefit case is analytical plus conceptual (Table 1). Nothing in the pinned text indicates the allocator has ever been measured.
2. **Zero cost / execution model.** No transaction cost, spread, slippage, fees, impact, capacity, latency, turnover, borrow or funding treatment exists (`data gap`, never zero) — so even a future replication has no source-side cost baseline to check against, and any claim that TRP is "practical" is unpriced.
3. **The allocator provides no alpha of its own.** It maps an exogenous signal to weights; §7.3.4 itself concedes `ρ = 0` "allows one to measure whether the topology is actually helping". Until that ablation is run, the paper's contribution could be pure re-weighting noise.
4. **Name/mechanism mismatch.** Appendix B reserves "topological risk parity" for conservative risk-based variants (`ρ = 1`), yet the paper's title and abstract apply it to the generic `ρ < 1` non-conservative allocator; no risk budgeting object (variance, risk contribution, volatility target) appears in any formula.
5. **Root discretion changes the whole book** (§7.2.1): three root rules, no default, no sensitivity analysis — an unconstrained degree of freedom that can be tuned after the fact.
6. **MST instability** (§7.2.2): "small changes in correlations can change the MST combinatorially"; no stability quantification, no ensemble/robustness mechanism, and Theorem 1 explicitly does not cover tree changes.
7. **DFS order dependence in Variant II** (Remark 4, §7.2.4): with `|𝒳| > 1` the augmented graph has cycles and non-sector parent assignments depend on traversal order — i.e. two correct implementations can produce different portfolios from identical inputs.
8. **Artificial fallback branch** (§7.2.5): when no `XL*` ETF is active, a zero-return dummy node is inserted into the correlation matrix, creating correlations the paper itself calls not theoretically clean.
9. **Information discarding by construction** (§7.2.3): the MST keeps `n_A - 1` of `n_A(n_A-1)/2` edges; no comparison against using the full graph is offered.
10. **No exposure/risk analysis of the output book.** Despite the framing (market-neutral, factor-aware, "reduces unintended factor bets"), the paper reports no factor exposures, no tracking error, no VaR, no concentration diagnostics for portfolios produced by the propagation rule; the `β_u ≥ 1` mass expansion (Prop. 4) is derived but its *portfolio-level* consequences are never analyzed.
11. **Proof-quality caveat:** Propositions 7–8 are proved under the assumption that the DFS spanning tree "includes all edges `(m,x)` as tree edges", i.e. the conclusion is partly assumed; the paper gives no argument that the implementation's DFS order satisfies it for arbitrary inputs.
12. **Under-specified executable rule.** Signal, rebalance cadence, `ρ`, `ε`, `k`, `T`, `L`, `c`, `η`, root default and tie-breaking are all unfixed; only `τ = 10⁻³` is printed. A replication would have to invent most operational choices (`research-proposed`).
13. **No code, no data, no availability statement.** "Current code" is referenced but unpublished (§7.2.4); no repository, commit, dataset or vendor appears in the pinned text.
14. **Preprint-only, conflicted-authorship context.** Non-peer-reviewed q-fin.PM preprint; all three authors share a single commercial affiliation (FMI Technologies LLC) with an explicit not-investment-advice disclaimer and no conflict-of-interest statement; license is CC BY-NC-SA 4.0 (non-commercial), constraining redistribution of the text itself.
15. **Cross-record contrary evidence (different sources in this repo, not this paper):**
    - `stn-tgat-nmi-soft-threshold-graph-attention-topk-ranking-2026-09-04.md` (different source) states that "static graphs or heuristic hard-thresholding techniques (such as arbitrary correlation cutoffs or minimum spanning trees) are fragile under market regime shifts and discard subtle yet informative relational channels" — a direct challenge to the MST-backbone premise of §3–§4.
    - `deep-portfolio-optimization-attention-lstm-omega-cvar-risk-parity-2026-09-03.md` reports (source-reported there: Fernandes & Desell, arXiv:2605.28853v1, Table I, 480-trading-day OOS 2022-01-03 → 2023-11-29, net of bid-ask spread) **HRP at −7.94% compounded return and −0.1776 annualized Sharpe**, i.e. the hierarchical-allocation family's own reference method underperforming in one independent sample. This is not evidence about TRP specifically (different source, different construction) but it is evidence against assuming hierarchical allocation is automatically beneficial.
    - `forecast-vol-targeting-student-t-hmm-hrp-regime-momentum-tilt-2026-09-13.md` (source `Olivesz/kronos-quant` @ `2e112e4e5f01a39d89121921df86ef2970e237a4`) reports that online Hedge / fixed-share aggregators failed to beat hand-crafted regime weights because sleeves were co-dependent through a shared HRP covariance backbone — a reminder that a shared hierarchical backbone can suppress, not create, diversification.

No source-side falsification or replication of TRP exists (`none identified in the reviewed sources; absence is not evidence of no negative result` — the paper has no citations beyond five classics and, being from April 2026, has had no visible replication in this repo).

## Falsification plan

All thresholds below are `research-defined falsification thresholds`; all operational choices not printed by the source are `research-proposed`. The control `ρ = 0` is `source-suggested` (§7.3.4); its failure margin is ours.

- **F1 — Topology ablation (`ρ = 0` control, source-suggested).** Fix one signed cross-sectional signal, one universe, one rebalance cadence; compare TRP at a `research-proposed` grid `ρ ∈ {0, 0.25, 0.5, 0.75, 1}` against `ρ = 0` (raw-signal L1) net of the F3 cost ladder. **Fail** if no `ρ > 0` value improves net Sharpe by ≥ 0.15 over `ρ = 0` on the primary out-of-sample window.
- **F2 — HRP / equal-weight / inverse-vol baselines.** Same signal, same costs, same universe: compare TRP-MST and TRP-SPY/XL against HRP, equal-weight and inverse-volatility allocation. **Fail** if TRP does not beat HRP net Sharpe by ≥ 0.10 and does not beat at least two of the four baselines.
- **F3 — Cost ladder.** Evaluate at 0 / 5 / 10 / 20 / 30 bp round-trip plus a `research-proposed` 20%-ADV participation cap. **Fail** if the TRP-vs-`ρ = 0` net Sharpe edge is ≤ 0 at 10 bp, or if break-even cost is < 5 bp.
- **F4 — Root sensitivity (Variant I).** Run hub / max-magnitude / fixed-index roots plus 50 random roots. **Fail** if the cross-root standard deviation of net Sharpe exceeds 0.30, or if the sign of the TRP-vs-`ρ = 0` edge flips in more than 20% of root choices.
- **F5 — MST stability.** Block-bootstrap the return window used for `C`; measure Jaccard overlap of MST edge sets and weight-vector L¹ distance. **Fail** if median edge-set Jaccard < 0.70 or median L¹ weight distance > 0.25 of gross.
- **F6 — DFS order dependence (Variant II).** Randomize vertex order for the DFS 100× on identical inputs. **Fail** if the resulting net Sharpe standard deviation > 0.10 or if weight L¹ dispersion > 0.10 of gross — this tests the source's own acknowledged Remark 4 feature.
- **F7 — Exposure audit.** Compare sector/factor exposures and tracking error of TRP vs `ρ = 0` and vs HRP. **Fail** if TRP *increases* absolute unintended sector/factor exposure relative to `ρ = 0` (the paper's §7.1 "reduces unintended factor bets" claim).
- **F8 — Macro-shock robustness (source claim, abstract §7.1.8).** On a `research-defined` stress subset (e.g. VIX ≥ 25 days and the 2020-03 / 2022 drawdown windows), compare worst-window drawdown and realized drawdown of TRP vs `ρ = 0`. **Fail** if TRP's worst-window drawdown is not strictly shallower in at least 2 of 3 stress windows.
- **F9 — Random-topology placebo.** Replace the MST with 500 random spanning trees matched on depth/branching distribution (and, separately, random rooted trees on the same node set). **Fail** if the real MST's net Sharpe does not exceed the 95th percentile of the placebo distribution — i.e. the *dependence structure* is not doing the work.
- **F10 — Turnover control.** TRP re-multiplies signals each rebalance; measure turnover vs `ρ = 0`. **Fail** if TRP turnover exceeds 1.5× the `ρ = 0` turnover at the same signal and cadence (the topology layer would be buying itself out through trading).
- **F11 — Walk-forward and holdout.** ≥ 5 rolling out-of-sample years (or ≥ 3 frozen forward quarters for a shorter universe), requiring the TRP-vs-`ρ = 0` net edge positive in ≥ 4 of 5 folds (research-defined); then a frozen forward window committed before evaluation.
- **F12 — Multiplicity control.** Benjamini–Hochberg `q < 0.10` across the full grid of {variant × ρ × root rule × universe × metric}. **Fail** the headline claim if no cell survives.
- **F13 — Specification repair audit.** Before any of the above, instantiate every `data gap` parameter (signal, cadence, `ε`, `k`, `T`, `L`, `c`, `η`, root rule) under a pre-declared, non-tuned rule; if the conclusion depends on the instantiation (edge flips across two reasonable `research-proposed` instantiations), record the hypothesis as **underspecified rather than supported**.

Action on failure: keep `research-only`, do not promote; either drop the allocator or restrict the claim to the exact regime/variant that survived, with the surviving scope documented as a new falsifiable statement.

## Crypto portability

**unproven.**

- The source contains **zero crypto evidence** — no crypto instrument, venue, funding, mark price, perpetual, spot or 24/7 discussion appears in the pinned text (`data gap` by absence; do not read as "portable").
- What could port structurally: the allocator only needs a cross-sectional return panel plus a signed signal, so a crypto-perpetual cross-section (e.g. top-N liquid perps) can in principle feed the same MST → propagation → L1 pipeline. That is a `research-proposed` adaptation, not source evidence.
- What does not port: Variant II's SPY root and `XL*` sector-ETF anchor are equity-specific (a crypto analogue would need a `research-proposed` anchor such as BTC/ETH as market/sector roots); equity session/timezone conventions, sector ontologies and index membership have no counterpart.
- Crypto-specific risks the source never addresses: funding charged every 8 hours on perpetual shorts (a long/short market-neutral book is funding-sensitive), mark/index price and liquidation mechanics, 24/7 candle boundaries for the correlation window, venue fragmentation and per-venue correlation contamination, wash-traded/painted volume corrupting co-movement estimates, borrow availability and cost for the short leg, and stablecoin/quote-currency effects.
- Verdict: portability is a hypothesis to be tested under F1–F13 on crypto data before any claim; crypto portability is not authorization to trade.

## Limitations

- `data gap`: no sample period, no universe instance, no timeframe, no signal, no cadence, no numeric parameters except `τ = 10⁻³`.
- `data gap`: no cost, fill, spread, impact, capacity, latency, borrow, funding or leverage-of-execution model; nothing is claimed gross or net.
- `underspecified`: parameterized family rather than a single reproducible rule (see Signal table); root rule and ρ have no defaults.
- `underspecified`: document date line (2026-08-24) vs v1 submission (2026-04-18); author order across surfaces; "risk parity" naming vs Appendix B.
- `not independently reproduced`: all propositions and the sole comparison table are taken as source-reported theory; we reproduced no proof and no backtest.
- Source-quality: preprint only, no peer review, single commercial affiliation for all authors, no code/data, license CC BY-NC-SA 4.0 (cite/normalize, do not copy).
- Identification: no baseline experiment, no placebo, no ablation, no statistical inference, no multiplicity control, no capacity analysis anywhere in the paper.
- Regime: the macro-shock robustness claim is asserted, not tested; MST fragility under regime shifts is a documented concern from other work (see Negative evidence 15).
- Publication-bias: a method paper with zero negative results is the expected shape of an unreviewed preprint; absence of failure evidence carries no weight.

## Implementation status

`implementation_status: not-implemented`. Nothing has been implemented in our research stack: no allocator prototype, no signal, no data pipeline, no backtest, no Qlib run, no Paper/Testnet/Live activity. The source's own implementation is referenced (§7.2.4) but not published, so it cannot be adopted or audited. This record is a research capture only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this record does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet or live trading. Any later adoption or implementation decision must be explicit, separately reviewed, and based on this record plus current primary sources.

## Related Wiki records

Wiki Brain was searched read-only for this run (no writes). `kb_search` for `hierarchical risk parity portfolio allocation` returned 4 pages, of which the two mechanism-adjacent pages below were verified and linked; `minimum spanning tree correlation network portfolio` returned only an unrelated time-series-foundation-model page (not linked), `risk parity signal attenuation clustering allocation` returned **0** results, and `long-short market neutral signal overlay portfolio weights` returned 3 adjacent-but-not-mechanism pages (not linked). **No Wiki page for Topological Risk Parity, this arXiv ID or these authors exists; none is fabricated.**

- [[quant/small-cap-alpha-beta-separation-uncertainty-aware-llm-portfolio-2026-09-02]] — uses HRP as the allocation backbone for LLM-signal long/short books; HRP is TRP's stated comparator, so this is the closest allocator-family neighbour (different source, different mechanism: cluster-variance recursion vs signed-signal path propagation).
- [[quant/aegis-momentum-gated-hierarchical-minimax-sortino-allocation-2026-09-12]] — hierarchical allocation with an explicit gating layer; adjacent allocation family, different source and different construction.

In-repo neighbours (repository files, four-axis distinction stated; **different source identity, and different mechanism / signal construction / data dependency**):

- `nested-clustered-optimization-schur-bridge-gateway-model-2026-09-25.md` (arXiv:2609.21271, Peter Cotton) — hierarchical *covariance* allocation (NCO + Schur coupling); TRP never allocates risk clusters, it attenuates an exogenous signed signal along MST paths.
- `forecast-vol-targeting-student-t-hmm-hrp-regime-momentum-tilt-2026-09-13.md` (`Olivesz/kronos-quant` @ `2e112e4e5f01a39d89121921df86ef2970e237a4`) — HRP cluster-variance backbone with regime sleeves; different source, and HRP's binary dendrogram + cluster-variance recursion is exactly what TRP claims to replace.
- `stn-tgat-nmi-soft-threshold-graph-attention-topk-ranking-2026-09-04.md` — graph/topology signal model that *criticises* MST hard-thresholding; different source, opposite stance toward the MST premise.
- `tda-persistent-homology-finbert-sentiment-portfolio-optimization-2026-09-02.md` — "topological" in the persistent-homology sense (Vietoris–Rips, Betti numbers); unrelated construction despite the shared word.

## Sources

- Revant Nayar, Dnyanesh Kulkarni, El Mehdi Ainasse, *"Topological Risk Parity"*, arXiv:2604.16773v1 [q-fin.PM], submitted 18 Apr 2026 01:35:40 UTC. abs: https://arxiv.org/abs/2604.16773 · pinned HTML: https://arxiv.org/html/2604.16773v1 (244,697 bytes, SHA-256 `1859701253442551d4a774aa2907a53d5ef79a72c24311b0cd299403b230210d`) · pinned PDF: https://arxiv.org/pdf/2604.16773v1 (381,082 bytes, SHA-256 `2a199eef59482720bf9638b2ee812bb5741f4094477ef7bf3ef95570face1a45`) · DOI: https://doi.org/10.48550/arXiv.2604.16773 (DataCite, HTTP 200). All accessed and verified 2026-09-26. License CC BY-NC-SA 4.0. **Every quantitative claim in this record traces to this single source; the source reports no performance numbers at all.**
- Cross-record negative evidence (listed in Negative evidence 15, each attributed to its own record and source): `stn-tgat-nmi-soft-threshold-graph-attention-topk-ranking-2026-09-04.md`; `deep-portfolio-optimization-attention-lstm-omega-cvar-risk-parity-2026-09-03.md` (underlying source Fernandes & Desell, arXiv:2605.28853v1, Table I); `forecast-vol-targeting-student-t-hmm-hrp-regime-momentum-tilt-2026-09-13.md` (underlying source `Olivesz/kronos-quant` @ `2e112e4e5f01a39d89121921df86ef2970e237a4`).
- Canonical schema used for this record: Wiki Brain `quant/strategy-research-record-spec-v1.md` (`kb_read`, 10,289 bytes, sha256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`); `quant/strategy-research-record-spec-v2.md` returns `No such file or directory`, so v1 remains canonical (checked 2026-09-26).
