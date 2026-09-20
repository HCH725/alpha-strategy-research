---
schema: strategy-research-record-v1
title: "PCA Factor-Model Estimation Error Decomposition: Out-of-Subspace vs In-Subspace Negative Methodology (arXiv 2609.20550)"
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - methodology
  - factor-models
  - pca
  - estimation-error
  - portfolio-construction
  - negative-evidence
  - high-dimensional
status: research-only
confidence: medium
source_as_of: 2026-09-17
sources:
  - "Alex Bernstein, Lisa R. Goldberg, Nicholas Gunther, Alec N. Kercheval, Tian Lan, Yian Lin, Dayi Yao, 'Principal component error in high-dimensional factor models', arXiv:2609.20550v1 [math.ST], September 17, 2026. https://arxiv.org/abs/2609.20550"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# PCA Factor-Model Estimation Error Decomposition: Out-of-Subspace vs In-Subspace Negative Methodology (arXiv 2609.20550)

## Provenance

- **Source**: arXiv:2609.20550v1 [math.ST]
- **Authors**: Alex Bernstein, Lisa R. Goldberg, Nicholas Gunther, Alec N. Kercheval, Tian Lan, Yian Lin, Dayi Yao
- **Submitted**: 2026-09-17
- **DOI**: https://doi.org/10.48550/arXiv.2609.20550
- **URL**: https://arxiv.org/abs/2609.20550
- **Review scope this cycle**: arXiv abstract + metadata only (35-page PDF body not re-audited this cycle). Exact simulation tables beyond abstract-level statements are **not restated** as source-reported facts.
- **Deduplication audit (2026-09-20; origin/main)**: No prior record cites `arXiv:2609.20550` or this PCA error decomposition. Adjacent records are different sources/mechanisms:
  - `special-markowitz-thermodynamic-joint-regularisation-returns-covariance-2026-09-17.md` — thermodynamic regularisation of Markowitz; different paper (2609.14029 family).
  - `separated-signal-libraries-packing-saturation-joint-spectral-limits-2026-09-17.md` — signal-library packing/spectral limits (2609.17609); different construction.
  - EVaR / HRP / risk-parity FMZ records — allocation engines; this paper is **PCA estimation-error methodology**, not an allocation rule.
  - Look-ahead PIT-vintage record (2609.20554) — foundation-model **training-vintage** leakage; different failure mode.
  - Matrix/stat-arb FMZ and academic pairs records — use covariances/PCA-like constructs but do not cite this error decomposition.

## Economic mechanism

### Source-reported

Source-reported setting: in a **statistical factor model**, principal components (eigenvectors of a sample covariance matrix) estimate the **principal directions** — the true drivers of co-movement of observed variables. The paper writes the **often substantial error** in these estimates as a **sum of two interpretable terms** with almost sure asymptotic limits as the number of variables grows with sample size bounded (high-dimensional regime common in financial economics).

Source-reported decomposition:

1. **Out-of-subspace error:** distance from an estimate to the subspace spanned by **population factor exposures**. Expressible **in terms of data**, providing an **estimable floor** for error.
2. **In-subspace error:** arises from the **fixed sample size of latent factor returns**; **cannot be estimated from data alone**.

Source-reported illustration: a **three-factor simulation of the US public equity market**, showing how error magnitude and its components depend on **dimension and sample size**. In that simulation, **out-of-subspace error dominates**.

Source-reported use case: researchers who rely on PCA to estimate factor models can use these results to **quantify errors in model-based predictions and attributions**.

### Research interpretation

This is **methodological / negative-evidence** material for the family of strategies and portfolio constructions that treat **sample PCA / eigenvector factor directions as if they were true population factors** — not a trading entry/exit strategy.

Research interpretation:

1. **PCA factors are estimates, not truth:** High-dimensional sample PCs can be substantially misaligned with population factor exposures; any strategy that ranks, hedges, or risk-budgets on sample PCs inherits this error.
2. **Partial identifiability:** Only out-of-subspace error has a **data-estimable floor**; in-subspace error is **not recoverable from data alone** under the paper’s regime — a structural limit on how “validated” a PCA-based construction can be.
3. **Boundary for in-repo PCA/factor records:** Matrix null-space stat-arb, risk parity on EWMA covariances, HRP, and other PCA-adjacent captures remain `research-only`; any evaluation should report dimension/sample sensitivity and not treat sample PCs as known exposures (research-proposed operationalization).
4. **Not crypto-empirical:** Illustration is a **US equity** three-factor simulation; crypto portability of the **error framework** is research-proposed, not source-proven on crypto universes.

Component roles (normalized):

```text
Not a trading signal.
Evidence class: methodological caution / error decomposition for sample-PCA factor models.
Required practice (research-proposed): report dimension vs sample size; estimate out-of-subspace error floor where possible; treat in-subspace error as unidentifiable from data alone; avoid presenting sample PCs as true factor exposures.
```

## Signal

Not applicable as a trading signal. No entry/exit, holding period, or position sizing.

Research evaluation sketch only (research-proposed):

- **Formation timestamp:** sample covariance estimated on data up to \(t\); PCA at \(t\) is an estimate, not a trading timestamp rule.
- **Lookback / parameters:** abstract does not publish numeric error tables for specific markets beyond the qualitative simulation claim (`data gap` for this cycle).

## Required data

- **Source-reported illustration:** US public equity three-factor **simulation** (not a live trading universe claim).
- **Fields:** cross-sectional variables / returns used to form sample covariance; population factor structure for error measurement in theory/simulation.
- **Point-in-time:** estimation window vs evaluation dimension/sample-size regime is the paper’s focus; no crypto dataset in the abstract.
- **Trading costs:** not applicable (methodology paper).

## Execution assumptions

None. No order routing, fills, or fees in the source-reported abstract.

## Evidence

### Source-reported

All qualitative claims in this record trace to arXiv:2609.20550v1 **abstract** (2026-09-17): PCA/eigenvectors as estimates of principal directions; error split into out-of-subspace (estimable floor) vs in-subspace (not estimable from data alone); asymptotic limits under growing dimension with bounded sample size; three-factor US equity simulation with out-of-subspace error dominating; intended use for quantifying errors in model-based predictions and attributions.

**No crypto results, no trading PnL, and no specific numeric error magnitudes are restated here** beyond the abstract-level dominance statement.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- The paper is itself **negative/methodological evidence** against treating sample PCA factor directions as error-free inputs to strategies or attributions.
- In-subspace error is reported as **not estimable from data alone** — a structural limit, not merely a small-sample inconvenience.
- Full PDF body not re-read this cycle; exact theorems/tables unread (`data gap`).

## Falsification plan

Research-proposed standards for PCA-based factor/stat-arb/risk constructions (not a source trading rule):

1. **Dimension–sample sensitivity (research-defined falsification threshold):** For any claimed PCA- or PC-risk-budget strategy, if OOS performance or risk attribution **materially degrades** when \(N/T\) increases within a pre-declared grid, and the source does not report an out-of-subspace error floor, treat the construction as **estimation-fragile** until shown otherwise.
2. **Out-of-subspace audit:** Where population factors are known (simulation) or proxied, measure PC subspace distance; fail “validated factor model” claims that ignore this floor.
3. **In-subspace honesty check:** Reject reports that estimate in-subspace PC error from the same sample without acknowledging non-identifiability claimed in this paper.
4. **Shrinkage / alternative backbone control:** Compare sample PCA vs Ledoit–Wolf / diagonal / HRP-style backbones; if PCA is not better after error-aware evaluation, sample PCs are non-load-bearing.
5. **Crypto portability test (research-proposed):** Repeat dimension/sample analysis on crypto cross-sections; do not import the US equity simulation numbers as crypto evidence.
6. **Action on failure:** Keep dependent PCA/factor records `research-only`; do not promote on in-sample PC fit alone.

## Crypto portability

**Portability: `unproven` for crypto data; methodology caution is general.**

- Source illustration: US equity factor **simulation**.
- Research interpretation: the **estimation-error decomposition** applies to any crypto cross-sectional PCA/factor construction (perp baskets, token sector PCA, EWMA cov risk parity) because sample-PC error is a statistical property — but **crypto-specific magnitudes are not source-reported**.
- Risks if ignored in crypto: thin \(T\) relative to large \(N\) token universes; regime-shifting loadings; treating EWMA sample PCs as stable exposures.

Crypto portability is not authorization to trade.

## Limitations

- **Abstract-level review** this cycle; full math/tables not restated.
- **not independently reproduced**
- **Not a strategy record** — incremental value is methodological evidence for the PCA/factor-model family adjacent to risk-parity, matrix stat-arb, and spectral library records already on main.
- Do not overclaim: paper provides a **decomposition and simulation illustration**, not a crypto backtest nor a universal rejection of PCA.
- Equity simulation ≠ crypto evidence.

## Implementation status

No implementation in our research stack. Does not modify NautilusTrader/PyBroker; does not authorize Paper/Testnet/Live.

`implementation_status: not-implemented`

## Adoption boundary

Research-only. Presence here does **not** mean any PCA/factor strategy is validated or approved.

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

## Related Wiki records

No stable Hermes Wiki Brain path known at write time. Do not fabricate Wiki links.

In-repo related: Special Markowitz regularisation record; Separated Signal Libraries record; FMZ risk parity 535843; EWY/TradFi matrix stat-arb; HRP/BL vol-target records; look-ahead PIT-vintage record.

## Sources

1. Alex Bernstein, Lisa R. Goldberg, Nicholas Gunther, Alec N. Kercheval, Tian Lan, Yian Lin, Dayi Yao. "Principal component error in high-dimensional factor models." arXiv:2609.20550v1 [math.ST], September 17, 2026. https://arxiv.org/abs/2609.20550
2. arXiv abstract/metadata reviewed 2026-09-20; full PDF body not re-read this cycle.
