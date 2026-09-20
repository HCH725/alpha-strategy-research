---
schema: strategy-research-record-v1
title: "Large Signal Libraries: Equal-Weight Limits and Divergent Signal vs PnL Spectra (arXiv 2609.12477)"
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - methodology
  - formulaic-alpha
  - signal-libraries
  - equal-weight
  - pca
  - portfolio-construction
  - negative-evidence
status: research-only
confidence: medium
source_as_of: 2026-09-11
sources:
  - "Marc da Costa Nunes, 'Large Signal Libraries: Equal-Weight Limits and the Divergent Spectra of Signals and PnL', arXiv:2609.12477v1 [q-fin.PM], September 11, 2026. https://arxiv.org/abs/2609.12477"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Large Signal Libraries: Equal-Weight Limits and Divergent Signal vs PnL Spectra (arXiv 2609.12477)

## Provenance

- **Source**: arXiv:2609.12477v1 [q-fin.PM]
- **Author**: Marc da Costa Nunes
- **Submitted**: 2026-09-11
- **DOI**: https://doi.org/10.48550/arXiv.2609.12477
- **URL**: https://arxiv.org/abs/2609.12477
- **Review scope this cycle**: arXiv abstract + metadata (PDF body not fully re-audited). Ancillary simulation scripts listed on the abstract page were not executed this cycle.
- **Deduplication audit (2026-09-20; origin/main)**: No prior record cites `arXiv:2609.12477` or this equal-weight / signal-vs-PnL spectral construction. Adjacent same-author paper **is already on main and is different**:
  - `separated-signal-libraries-packing-saturation-joint-spectral-limits-2026-09-17.md` — **arXiv:2609.17609**, packing under correlation caps, saturation, Gilbert–Varshamov-style separation. Distinct paper identity and distinct technical claims (admission geometry vs equal-weight limits / signal–PnL spectrum divergence).
  - `pca-factor-model-error-decomposition-out-of-subspace-arxiv-2609.20550-2026-09-20.md` — sample-PC estimation error; different object (factor PCs vs signal-library EWS).
  - Formulaic-alpha mining records (Alpha-Foundry, FactorMiner, AlphaCFG, etc.) — discovery systems; this record is **population/geometry theory** about large equal-weighted libraries, not a mining algorithm.
  - `special-markowitz-thermodynamic-joint-regularisation-returns-covariance-2026-09-17.md` — different regularisation object.

## Economic mechanism

### Source-reported

Source-reported motivating observation: an ensemble of roughly **3,000 signals** over **20 assets** was reported to have approximately **90% correlation** with the leading component of the asset-space return structure. The paper asks whether having ~**158 signals per available linear dimension** explains that alignment.

Source-reported population answer: crowding alone imposes **neither a nonzero mean nor agreement with a principal component**; the answer depends on the research process’s **design distribution** and its relation to returns.

Source-reported theory distinguishes **four objects**:

1. Equal-weight signal  
2. Signal principal components  
3. Equal-weight **PnL**  
4. **PnL** principal components  

The **return operator** in the motivating observation is a **separate object** again.

Source-reported library-type results: **Independent** libraries converge to their **design mean**; **exchangeable** libraries can retain a **random conditional mean**.

Source-reported geometry (cross-sectional signals over \(d\) assets, demeaned and normalized on \(S^{q-1}\), \(q=d-1\)): under **axial symmetry**, nonzero mean equals **signal-cloud PC1 exactly when** longitudinal second moment exceeds \(1/q\) (isotropic energy share). Residual-and-gap bounds quantify approximate alignment.

Source-reported combining bound: design weights into signals contract the tangent of angle to PC1 to at most \(\sqrt{\lambda_2/\lambda_1}\) times its value (\(\lambda_1>\lambda_2\) leading signal-kernel eigenvalues); factor is sharp.

Source-reported frame distinction: **transverse signal geometry** (which PnL discards) vs **dispersion weighting and temporal centering** (which also change the spectrum).

Source-reported validation framing: reproducible **synthetic** example of the geometric threshold; proposed empirical program separating library growth from limited-history estimation. **No market-data empirical results are presented.**

### Research interpretation

This is **methodological / theory evidence** for large **equal-weighted formulaic-alpha / signal libraries** — not a trading entry/exit rule.

Research interpretation:

1. **Library size ≠ PC1 alpha:** Hundreds of signals per asset dimension do not automatically make EWS align with return PC1; design distribution and return linkage matter.
2. **Signal spectrum ≠ PnL spectrum:** Large libraries can look coherent in signal space while PnL spectra diverge — a warning against treating “many agreeing signals” as evidence of tradeable ensemble edge.
3. **Boundary for in-repo mining records:** Alpha-Foundry / FactorMiner / AlphaCFG-class captures that produce large formulaic libraries remain `research-only`; intake should not treat EWS–PC1 alignment as proof of alpha without an explicit design/return model (research-proposed).
4. **Companion to 2609.17609:** Separation/cap geometry (already on main) and equal-weight spectral limits (this record) are **different theorems**; both argue that naive “more separated signals → better ensemble” is incomplete.

Component roles (normalized):

```text
Not a trading signal.
Evidence class: population/geometry theory for large equal-weight signal libraries.
Key objects: EWS, signal PCs, EWS-PnL, PnL PCs, return operator — keep separate.
Claim: crowding/design alone does not force mean or PC1 alignment; signal vs PnL spectra can diverge.
```

## Signal

Not applicable as a trading signal. No entry/exit, holding period, or sizing.

Research evaluation sketch (research-proposed):

- **Formation:** library of cross-sectional signal vectors at each date; demean/unit-normalize.
- **Lookback / sample:** theory is population/asymptotic + synthetic illustration; no market sample claimed this cycle.

## Required data

- **Source-reported:** synthetic example; ancillary validation files listed on arXiv (not run here).
- **Universe:** abstract uses \(d\) assets / \(q=d-1\) sphere; motivating anecdote ~20 assets / ~3000 signals — **not** treated as our empirical universe.
- **Market data:** source states **none** presented.

## Execution assumptions

None (theory/methodology).

## Evidence

### Source-reported

Qualitative abstract claims only (2026-09-11): ~3000 signals / 20 assets / ~90% PC1 correlation anecdote; crowding ≠ mean/PC1; four-object distinction; independent vs exchangeable library limits; sphere geometric threshold \(\lambda\)-energy share \(1/q\); \(\sqrt{\lambda_2/\lambda_1}\) angle bound; synthetic illustration; **no market-data empirical results**.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- Source-reported: crowding alone does not explain EWS–PC1 alignment; signal and PnL spectra can diverge.
- Same-author companion on main (2609.17609) already documents separation ≠ guaranteed good EWS behavior — this paper adds **equal-weight / spectral** negative structure.
- No independent theorem proof or synthetic rerun in our stack this cycle.

## Falsification plan

Research-proposed standards for large signal-library systems (not a source trading rule):

1. **Four-object audit (research-defined falsification threshold):** For any claimed large-library ensemble, report EWS, signal-PC, EWS-PnL, and PnL-PC spectra separately. If a source reports only signal-space “coherence” or PC1 alignment **without** PnL-space evidence, reject tradeable-edge claims until PnL spectra are shown.
2. **Design-mean control:** Compare independent vs exchangeable/adaptive library construction under the same return operator; if results are identical regardless of design distribution, the theory’s design channel is non-load-bearing for that sample (or the implementation ignored design).
3. **Dimension crowding test:** Vary signals-per-dimension; if EWS–PC1 correlation rises solely with library size under a null return operator, treat alignment as geometry artifact, not alpha.
4. **Transverse discard check:** Show how much signal geometry PnL weighting discards; fail “diversified library” narratives that ignore this loss.
5. **Synthetic threshold replication:** Reproduce the \(1/q\) longitudinal-moment threshold on held-out synthetic setups; if not reproducible, mark theory as unverified.
6. **Action on failure:** Keep formulaic-alpha mining records `research-only`; do not promote large EWS libraries on signal-PC alignment alone.

## Crypto portability

**Portability: `unproven` for crypto libraries; methodology is asset-class general.**

- Source presents theory + synthetic geometry, not crypto data.
- Research interpretation: crypto formulaic libraries (perp cross-sections, large N tokens) face the **same** signal-vs-PnL and crowding-vs-PC1 confusions; crypto-specific \(N/T\), funding, and non-stationarity are **not** source-proven here.
- Do not import the 3000/20/90% anecdote as crypto evidence.

Crypto portability is not authorization to trade.

## Limitations

- **Abstract-level review**; full proofs/tables not restated.
- **not independently reproduced**
- **No market-data empirical results** in source — theory/methodology only.
- **Not a strategy record** — incremental value is a **distinct paper identity** (2609.12477) and **equal-weight / signal–PnL spectral** evidence complementary to packing/saturation (2609.17609) already on main.
- Do not overclaim: theory does not say all large libraries fail; it separates objects and states when PC1 alignment can/cannot occur under stated symmetry assumptions.

## Implementation status

No implementation in our research stack. Does not modify NautilusTrader/PyBroker; does not authorize Paper/Testnet/Live.

`implementation_status: not-implemented`

## Adoption boundary

Research-only. Presence here does **not** mean any signal library is validated or approved.

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

## Related Wiki records

No stable Hermes Wiki Brain path known at write time. Do not fabricate Wiki links.

In-repo related: `separated-signal-libraries-packing-saturation-joint-spectral-limits-2026-09-17.md`; PCA error decomposition record; Alpha-Foundry / FactorMiner / formulaic-alpha discovery family; Special Markowitz record.

## Sources

1. Marc da Costa Nunes. "Large Signal Libraries: Equal-Weight Limits and the Divergent Spectra of Signals and PnL." arXiv:2609.12477v1 [q-fin.PM], September 11, 2026. https://arxiv.org/abs/2609.12477
2. arXiv abstract/metadata reviewed 2026-09-20; ancillary simulation not executed this cycle.
