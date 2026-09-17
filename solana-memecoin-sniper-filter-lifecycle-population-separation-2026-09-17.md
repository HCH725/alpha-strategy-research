---
schema: strategy-research-record-v1
title: "Solana Memecoin Sniper vs Filter-Rejection Population Separation: Two-Window Lifecycle-Stage Replication"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - solana
  - memecoin
  - sniper-cohort
  - filter-rejection
  - lifecycle-stage
  - population-separation
  - negative-evidence
  - replication
status: research-only
confidence: medium
source_as_of: 2026-09-17
sources:
  - "Arati Uday Kamat, 'Sniper Cohorts and Algorithmic Filter Rejections in Solana Memecoin Markets: Two-Window Replication of Lifecycle-Stage Population Separation', arXiv:2609.18975 [q-fin.TR, q-fin.CP, q-fin.ST], 2026-09-17. https://arxiv.org/abs/2609.18975"
  - "Zenodo companion dataset DOI: https://doi.org/10.5281/zenodo.21399918 (CC-BY-4.0)"
  - "Also SSRN 7128818; GitHub scripts referenced on arXiv page (http URL in listing)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Solana Memecoin Sniper vs Filter-Rejection Population Separation: Two-Window Lifecycle-Stage Replication

## Provenance

- **Primary source**: arXiv:2609.18975 (2026-09-17), Kamat.
- **Data**: Zenodo DOI 10.5281/zenodo.21399918, CC-BY-4.0; SSRN 7128818.
- **Windows**: 2026-06-11 to 2026-06-25 and 2026-06-29 to 2026-07-16 (non-overlapping).
- **Pipelines**: cohort detector v1 (20,162 mints) and v2 (623 mints); rejection-stream 83 and 1,743 mints per window.

## Economic mechanism

### Source-reported

Prior work often conflates **pre-graduation (bonding-curve)** and **post-graduation (open-market)** Solana memecoin populations. This paper tests whether sniper-cohort detection and algorithmic filter-rejection streams identify the **same** tokens.

**Result**: set overlap remains **<1% of the cohort population** in both windows; cross-window cohort overlap is **zero**. Separation is **structural**: cohort detection operates at bonding-curve stage; rejection filtering on PumpSwap and other post-graduation venues. Four alternative explanations systematically ruled out (time-window artifact, data-source mismatch, DEX venue asymmetry, pipeline-version artifact).

### Scout interpretation

This is **negative / structural evidence for research design**, not a trading alpha. It implies: (1) sniper and filter metrics must not be pooled across lifecycle stages; (2) any “memecoin alpha” paper that mixes stages may be measuring different populations; (3) cross-stage token surveillance needs explicit stage labels. Incremental vs in-repo `solana-bonding-curve-sniper-cohort-contamination-adjusted-flow-2026-09-02.md` (flow contamination) — this record is **population-overlap / stage separation**, with public replication data.

## Signal

Not a trading signal. Reconstructable **research pipeline claim**:

- Cohort-detected mints vs rejection-stream mints; set overlap fraction per window.
- Overlap <1% of cohort population; cross-window cohort overlap 0.

## Required data

- On-chain Solana mint/cohort and rejection-stream logs for the two windows (Zenodo CC-BY-4.0).
- Venue tags distinguishing bonding-curve vs PumpSwap/post-grad.

## Execution assumptions

N/A (measurement study).

## Evidence

### Source-reported

- Two independent windows; two detector versions; four alternative explanations ruled out.
- Datasets released for replication.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- Core result **is** negative evidence against treating sniper and filter populations as interchangeable.
- Does **not** claim no sniper edge or no filter edge separately.

## Falsification

Research-defined (not source-reported):

1. **Third-window replication**  
   - New non-overlapping window; recompute overlap.  
   - **Research-defined falsification threshold**: if overlap ≥ 10% of cohort population under the same stage definitions, structural-separation claim weakens.

2. **Stage-label ablation**  
   - If pooling stages produces materially different sniper/filter statistics than stage-split analysis, supports the paper’s warning.

3. **Detector swap**  
   - Independent sniper implementation; if overlap jumps, v1/v2 pipelines are idiosyncratic rather than stage-bound.

## Crypto portability

**Direct** for Solana memecoin research methodology. Not portable as a trading signal. Implications apply to any multi-venue memecoin study that mixes bonding-curve and open-market samples.

## Limitations

- June–July 2026 windows only; detector versions are author-specific.
- Measurement, not alpha; confidence **medium** for the separation claim, **N/A** for profitability.
- Related but distinct from in-repo contamination-flow record.

## Implementation status

- Research measurement only; **not implemented**.
- **Not authorized** for Paper/Testnet/Live.

## Adoption boundary

`status = research-only`. `adoption = not-approved`. `approval_scope = research-only`.

## Related Wiki / repo records

- `solana-bonding-curve-sniper-cohort-contamination-adjusted-flow-2026-09-02.md` — flow contamination within cohort detection.
- `solana-memecoin-hour-aware-deployment-fragility-2026-09-14.md` — deployment fragility.
- No prior record cites arXiv:2609.18975 (searched 2026-09-17).

## Sources

1. https://arxiv.org/abs/2609.18975  
2. https://doi.org/10.5281/zenodo.21399918  
3. SSRN 7128818 (as cited on arXiv page).
