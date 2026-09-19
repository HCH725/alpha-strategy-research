---
schema: strategy-research-record-v1
title: "Information Fidelity in LLM-Compressed Financial Analysis: Decision-Distortion Negative Evidence (arXiv 2606.29251)"
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - methodology
  - llm
  - context-compression
  - information-fidelity
  - negative-evidence
  - agentic-ai
  - financial-nlp
status: research-only
confidence: medium
source_as_of: 2026-09-17
sources:
  - "Hoyoung Lee et al., 'When Summaries Distort Decisions: Information Fidelity in LLM-Compressed Financial Analysis', arXiv:2606.29251v3 [cs.AI], last revised September 17, 2026 (v1 June 28, 2026). EMNLP 2026 Industry Track. https://arxiv.org/abs/2606.29251"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Information Fidelity in LLM-Compressed Financial Analysis: Decision-Distortion Negative Evidence (arXiv 2606.29251)

## Provenance

- **Source**: arXiv:2606.29251v3 [cs.AI]
- **Authors**: Hoyoung Lee, Suhwan Park, Seunghan Lee, Jun Seo, Jaehoon Lee, Sungdong Yoo, Minjae Kim, CheolWon Na, Zhangyang Wang, Zach Golkhou, Minkyu Kim, Sotirios Sabanis, Alejandro Lopez-Lira, Dhagash Mehta, Soonyoung Lee, Chanyeol Choi, Wonbin Ahn, Yongjae Lee (18 authors listed on abstract page)
- **Versions**: v1 2026-06-28; v2 2026-07-08; **v3 2026-09-17**
- **Venue (source-reported comments)**: EMNLP 2026 Industry Track
- **DOI**: https://doi.org/10.48550/arXiv.2606.29251
- **URL**: https://arxiv.org/abs/2606.29251
- **HTML**: https://arxiv.org/html/2606.29251v3 (available; body not fully re-audited this cycle — abstract-level claims only)
- **Review scope this cycle**: arXiv abstract + metadata (v3). Per-dataset numeric metrics not restated beyond abstract-level findings.
- **Deduplication audit (2026-09-20)**: Repository-wide search found **zero** prior records citing `arXiv:2606.29251`, this title, or “Agentic Context Compression” / decision-fidelity compression. Adjacent records are different:
  - `sok-farsight-llm-trading-agents-robustness-security-negative-evidence-arxiv-2609.19705-2026-09-19.md` — security/robustness SoK of LLM **trading schemes**; not context-compression decision fidelity.
  - `stableeval-arena-agentic-stablecoin-peg-risk-negative-evidence-arxiv-2609.18949-2026-09-20.md` — peg-risk **benchmark** of agents; different task.
  - `look-ahead-bias-pretrained-financial-forecasting-pit-vintage-arxiv-2609.20554-2026-09-19.md` — foundation-model **training-vintage** look-ahead; different failure mode.
  - `llm-strategy-discovery-leakage-safe-search-deflated-eval-2026-09-04.md` — strategy-search leakage; not compression-induced decision change.
  - LLM news/sentiment strategy captures — individual hypotheses; this is **cross-cutting negative evidence** about compressing financial source material before decisions.

## Economic mechanism

### Source-reported

Source-reported problem: financial decision-makers face more information than they can inspect, so **context compression** is necessary. When LLMs compress financial source material, they can **alter the investment judgment supported by the original source**.

Source-reported framing — **information fidelity**: compression loses fidelity when it **changes the decision induced by the source**. In agentic systems, such losses may **recur across intermediate steps and amplify**.

Source-reported empirical domain: **financial filings** and **earnings-call transcripts**.

Source-reported findings (abstract-level):

- LLM-based compression can produce **fluent and factually plausible** compressed contexts that nevertheless **alter downstream decisions**.
- Two diagnostic patterns associated with fidelity loss:
  1. **Decontextualization** — salient evidence retained but **separated from caveats and contextual qualifiers** needed for correct interpretation.
  2. **Model dependency** — different compressors expose **different views** of the same source.
- Proposed mitigation: **Agentic Context Compression** — generate **multiple candidate compressions** and **audit disagreements against the original source**.
- Source conclusion: financial compression should be evaluated not only by efficiency or factuality, but also by ability to **preserve decision-relevant context**.

### Research interpretation

This is **family-level negative / evaluation evidence** for LLM pipelines that compress filings, transcripts, research PDFs, or digests **before** trading or risk decisions — not a trading entry/exit strategy.

Research interpretation:

1. **Factuality ≠ decision safety:** A summary can pass “looks right / no hallucinated numbers” checks yet change the investment decision the full source supports.
2. **Agentic amplification risk:** Multi-step research agents (scout → compress → decide) can compound fidelity loss at each hop — directly relevant to AI-assisted research intake in this pipeline’s broader ecosystem.
3. **Boundary for in-repo LLM-finance records:** Any capture that relies on LLM summaries of primary sources remains `research-only`; primary-source verification and decision-fidelity checks are required (research-proposed operationalization).
4. **Not crypto-empirical:** Sample is filings/transcripts (equity-style corporate disclosure); crypto portability of the **evaluation standard** is research-proposed.

Component roles (normalized):

```text
Not a trading signal.
Evidence class: methodological negative evidence — LLM financial context compression can alter decisions.
Required practice (research-proposed): evaluate compression by decision fidelity vs full source; audit decontextualization and model-dependency; multi-candidate disagreement audit against originals.
```

## Signal

Not applicable as a trading signal. No entry/exit, holding period, or sizing.

Research evaluation sketch (research-proposed):

- **Formation timestamp:** source document publication time; compression must not use post-decision information beyond the document.
- **Lookback:** full source vs compressed context comparison at decision time.
- **Parameters:** abstract does not publish numeric fidelity-loss rates this cycle (`data gap` for tables).

## Required data

- **Source-reported domain:** financial filings; earnings-call transcripts.
- **Fields:** full source text; LLM-compressed context; induced investment decision labels/judgments.
- **Point-in-time:** decision induced by original source is the reference; compression is the treatment.
- **Crypto:** not in source sample; any crypto memo/news compression study would be a **new** source.

## Execution assumptions

No trading execution. “Agentic” in the paper refers to multi-step LLM workflows, not order routing.

## Evidence

### Source-reported

All qualitative claims in this record trace to arXiv:2606.29251v3 **abstract** (revised 2026-09-17; EMNLP 2026 Industry Track): necessity of compression; fidelity defined as decision preservation; fluent/plausible compressions that alter downstream decisions; decontextualization and model-dependency patterns; Agentic Context Compression (multi-candidate + disagreement audit); evaluation should include decision-relevant context preservation. Domains: filings and earnings-call transcripts.

**No numeric effect sizes are restated here** without full-table access this cycle.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- The paper is itself **negative evidence** against treating LLM summaries as decision-safe financial context.
- No independent replication of their fidelity experiments in our stack this cycle.
- Full PDF/HTML body not fully audited; numeric tables unread (`data gap`).

## Falsification plan

Research-proposed standards for LLM-compressed financial decision systems (not a source trading rule):

1. **Decision-fidelity gate (research-defined falsification threshold):** For any claimed LLM research/compression pipeline used in investment judgment, if the compressed-context decision **disagrees with the full-source decision** at a rate **above a pre-declared tolerance** on a held-out filing/transcript set, reject “lossless research assistant” claims.
2. **Decontextualization audit:** Blind raters or rule checks on whether caveats/qualifiers survive compression; fail if decision-critical caveats drop out while entities/numbers remain.
3. **Model-dependency test:** Same source, ≥2 compressors; if induced decisions diverge without resolution against the original, mark pipeline unstable.
4. **Efficiency vs fidelity frontier:** Pre-declare token budget; reject compressions that save tokens only by changing decisions.
5. **Agentic hop stress:** Compare single-pass vs multi-hop agent compression; if fidelity decays with hops, require original-source re-audit before final action.
6. **Action on failure:** Keep dependent LLM-finance records `research-only`; do not promote on factuality metrics alone.

## Crypto portability

**Portability: `unproven` for crypto corpora; methodology caution is general.**

- Source sample: equity-style filings and earnings calls, not on-chain or crypto news corpora.
- Research interpretation (research-proposed): the **decision-fidelity evaluation standard** applies to any crypto research agent that summarizes papers, FMZ pages, or on-chain reports before signals — but crypto-specific evidence would require a new study.
- Risks if ignored in crypto: compressed funding/OI narratives, protocol risk caveats stripped from “bullish” digests, multi-hop agent echo chambers.

Crypto portability is not authorization to trade.

## Limitations

- **Abstract-level review** this cycle; numeric tables not restated.
- **not independently reproduced**
- **Not a strategy record** — incremental value is methodological negative evidence for LLM financial compression (adjacent to FARSIGHT/StableEval/look-ahead family, different failure mode).
- Do not overclaim: paper proposes a mitigation (Agentic Context Compression); it does not say all LLM finance tools fail.
- Author list is long (industry track); exact affiliations beyond abstract not re-audited this cycle.

## Implementation status

No implementation in our research stack. Does not modify NautilusTrader/PyBroker; does not authorize Paper/Testnet/Live.

`implementation_status: not-implemented`

## Adoption boundary

Research-only. Presence here does **not** mean any LLM pipeline is validated or approved.

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

## Related Wiki records

No stable Hermes Wiki Brain path known at write time. Do not fabricate Wiki links.

In-repo related: FARSIGHT SoK; StableEval Arena; look-ahead PIT-vintage record; LLM strategy-discovery leakage record; LLM news/sentiment captures.

## Sources

1. Hoyoung Lee et al. "When Summaries Distort Decisions: Information Fidelity in LLM-Compressed Financial Analysis." arXiv:2606.29251v3 [cs.AI], last revised September 17, 2026. EMNLP 2026 Industry Track. https://arxiv.org/abs/2606.29251
2. arXiv abstract/metadata reviewed 2026-09-20; full body not fully re-read this cycle.
