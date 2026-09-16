---
schema: strategy-research-record-v1
title: "Crypto Sentiment Extremity and Estimated Spreads: Specification-Dependent Association (v4 Correction)"
created: 2026-09-01
updated: 2026-09-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - market-microstructure
  - sentiment-extremity
  - bid-ask-spread
  - fear-and-greed
  - negative-evidence
  - specification-sensitivity
  - retraction-correction
status: research-only
confidence: low
source_as_of: 2026-09-13
sources:
  - "Murad Farzulla, 'Does Crypto Sentiment Extremity Widen Estimated Spreads? Evidence Depends on the Specification', arXiv:2602.07018v4 [q-fin.ST, q-fin.CP], last revised 2026-09-13. https://arxiv.org/abs/2602.07018"
  - "https://doi.org/10.48550/arXiv.2602.07018"
  - "Prior capture of v3 lineage: this repository record originally written 2026-09-01 against arXiv:2602.07018v3 (July 2026) under title 'The Extremity Premium: Sentiment Regimes and Adverse Selection in Cryptocurrency Markets'"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Author-corrected v4 (2026-09-13) withdraws quote-validation and alternative-spread claims present in the v3 lineage; ABM and decomposition removed; momentum outcome and effect-size denominators corrected. v4 concludes only a descriptive, specification-dependent association and explicitly does not establish a stable or causal liquidity premium."
---

# Crypto Sentiment Extremity and Estimated Spreads: Specification-Dependent Association (v4 Correction)

## Provenance

- **Primary source (current canonical)**: Murad Farzulla, *"Does Crypto Sentiment Extremity Widen Estimated Spreads? Evidence Depends on the Specification"*, arXiv:2602.07018v4 [q-fin.ST, q-fin.CP], last revised **2026-09-13**. DOI: https://doi.org/10.48550/arXiv.2602.07018.
- **Correction notice (source-reported)**: v4 includes a correction notice. Comments state: empirical reconstruction with ABM and decomposition removed; prior alternative-spread row and quote-validation claims withdrawn; momentum outcome and effect-size denominators corrected. Code URL accompanies the preprint.
- **This record was first written 2026-09-01 against the v3 lineage** (title then: "The Extremity Premium: Sentiment Regimes and Adverse Selection in Cryptocurrency Markets"). That capture overstated stability and omitted author-side negative evidence that did not yet exist.
- **Update 2026-09-15**: material update for incremental negative/correction evidence under the strategy-research-record-v1 dedup rule (same mechanism/signal family → update in place rather than create a second artifact).
- Sample (v4): 2,896 BTC/USDT daily observations, February 2018 – January 2026. Sentiment: Alternative.me Crypto Fear & Greed Index. Spread proxy: daily high-low estimate (Corwin–Schultz lineage in prior versions; v4 centers the high-low spread estimate and specification ladder).

## Economic mechanism

### Source-reported (v4)

The question posed is whether extreme values of the Crypto Fear & Greed Index are associated with a daily high-low **estimated** spread for Bitcoin. v4 reports:

- Unconditional extreme-minus-neutral gap: **61.99 bps**.
- After close-to-close realized-volatility-quintile demeaning: **24.79 bps**, but **none of the five separate quintile contrasts survives Holm correction**.
- With quadratic realized-volatility and strictly lagged momentum controls, HAC estimate: **11.81 bps** (95% CI **[−2.31, 25.93]**, **p = .101**).
- Fixed non-parametric stratification: **20.44 bps** (**p = .0195** under circular shifts).
- Separate models for a zero-floored estimate's incidence and positive magnitude are **imprecise**.
- **Author conclusion**: results show only a **descriptive, specification-dependent association**. They **do not establish a stable or causal liquidity premium**.

### Scout interpretation

v3-era operationalizations in the prior capture of this record (extreme-regime quote widening, taker-deferral filters, adverse-selection premium as a durable structural feature) are **not supported as stable causal claims by the corrected source**. The residual signal is a fragile descriptive gap that appears or disappears with specification choice. Treat any market-making / execution overlay built on CFGI extremity as **hypothesis-only** and require pre-registered point-in-time spread data (quoted/effective L2), not daily high-low proxies, before any further use.

## Signal

### Source-faithful (descriptive only)

- Sentiment: daily CFGI ∈ [0, 100].
- Extremity: |CFGI − 50| / 50; extreme regimes typically CFGI < 25 or CFGI > 75.
- Outcome proxy: daily high-low spread estimate (not exchange-quoted bid-ask).
- **No reconstructable entry/exit alpha is claimed in v4.** Prior operational quote-offset rules from the v3 capture remain in this record only as **withdrawn / underspecified** research-proposed ideas and must not be treated as source-reported.

### Underspecified / withdrawn

Exact quoting multipliers, inventory penalties, and taker-deferral thresholds were never fully parameterized in the source; v4 further removes the evidentiary basis that made those overlays look motivated.

## Required data

- Daily Alternative.me CFGI (or equivalent) with publication timestamp.
- BTC/USDT daily OHLC (for high-low spread estimate) and, for any serious re-test, L1/L2 quoted and effective spreads at decision frequency.
- Realized volatility (close-to-close and preferably intraday) and lagged momentum controls as in v4.
- Point-in-time availability of CFGI (index publication lag).

## Execution assumptions

No executable strategy is asserted. Any prior "defer taker in extreme regimes" idea is research-proposed and **not authorized**. Cost/fill models were not the focus of v4.

## Evidence

### Source-reported (v4, 2026-09-13)

See mechanism section for the full specification ladder. Headline: association is specification-dependent; causal/liquidity-premium claim **withdrawn**. Quote-validation and alternative-spread claims from earlier versions are **withdrawn by the author**.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- **Author-side correction (primary)**: v4 is itself a negative-evidence document relative to the v3 "extremity premium" framing. Holm correction kills within-vol quintile contrasts; HAC + momentum CI includes zero; incidence/magnitude split is imprecise.
- Prior capture (2026-09-01) reported "none identified in the reviewed sources" for negative evidence; that statement is **superseded** by v4.
- Related in-repo sentiment records (e.g. weekly AR(1) innovation risk premium, contrarian Fear & Greed EMA) study **different** constructions and are not automatically invalidated; they must not be used to "rescue" a causal CFGI→spread premium.

## Falsification

Research-defined tests that would further disconfirm a **stable** CFGI-extremity → spread effect:

1. **Quoted-spread replication (primary gap)**  
   - Data: BTC/USDT L2 quoted/effective spreads, point-in-time CFGI, ≥ 2018–present.  
   - Test: extreme vs neutral days after realized-vol and lagged-momentum controls, HAC + Holm across multiple spread estimators.  
   - **Research-defined falsification threshold**: if the 95% CI on extreme-minus-neutral includes 0 under both high-low and quoted/effective spreads, reject any durable spread-premium claim. Action: mark family rejected for execution overlays.

2. **Specification multiverse**  
   - Report the full grid of demeaning/controls/estimators without selecting the favorable cell.  
   - If only non-parametric stratification clears p < 0.05 while parametric/HAC cells fail, treat as fragile descriptive artifact.

3. **Placebo sentiment**  
   - Shuffle CFGI series within volatility strata (circular shifts as in v4).  
   - Observed gap must exceed the placebo distribution; v4's circular-shift p = .0195 is a start but not decisive against Holm-adjusted multi-contrast failures.

4. **No rescue by adjacent records**  
   - Do not treat other CFGI-based records in this repo as independent confirmation of a **spread** premium unless they use the same outcome and controls.

## Crypto portability

**Direct** for the descriptive association (crypto-native CFGI + BTC/USDT). **Not** portable as an execution alpha without the falsification tests above. Perp funding, venue fragmentation, and 24/7 session effects are unaddressed in v4.

Crypto portability is not authorization to trade.

## Limitations

- Daily high-low spread is a **proxy**, not quoted bid-ask; v4's withdrawn quote-validation claims matter here.
- CFGI is a daily composite with publication lag; intraday regime shifts are invisible.
- Single asset (BTC) in the corrected empirical focus of the abstract; multi-asset generality not established in v4.
- Preprint with author retraction of prior claims; treat lineage carefully.
- Confidence **downgraded** from medium (v3 capture) to **low** after correction.
- `contested: true` because author-side corrections contradict the earlier "extremity premium" framing stored in this record.

## Implementation status

- Nothing implemented.
- Prior research-proposed market-making / taker-deferral overlays are **not implemented** and should not proceed on v3-era evidence.

## Adoption boundary

`status = research-only`. `adoption = not-approved`. `approval_scope = research-only`.

This update is a correction of research staging content only. It is not strategy adoption, implementation authorization, or permission for Paper/Testnet/Live.

## Related Wiki / repo records

- This file replaces the 2026-09-01 v3-era content in place (same path).
- `crypto-fear-greed-weekly-ar1-innovation-risk-premium-2026-09-04.md` and `crypto-macro-sentiment-contrarian-fear-greed-ema-2026-09-03.md` — different signal constructions (return/risk premium and contrarian timing), not the spread outcome.
- No Wiki Brain write performed.

## Sources

1. Murad Farzulla, arXiv:2602.07018v4 (2026-09-13): https://arxiv.org/abs/2602.07018  
2. DOI: https://doi.org/10.48550/arXiv.2602.07018  
3. Alternative.me CFGI: https://alternative.me/crypto/fear-and-greed-index/
