---
schema: strategy-research-record-v1
title: "Kalshi First and Stable Decidability Observability Negative Evidence (arXiv 2609.16642)"
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - prediction-markets
  - kalshi
  - observability
  - settlement
  - rule-version
  - negative-evidence
  - methodology
status: research-only
confidence: medium
source_as_of: 2026-09-15
sources:
  - "Maksym Nechepurenko, 'From Public Evidence to Contractual Outcome: First and Stable Decidability on Kalshi', arXiv:2609.16642v1 [q-fin.TR], September 15, 2026. https://arxiv.org/abs/2609.16642"
  - "SSRN abstract mirror (source-reported): https://ssrn.com/abstract=7421261"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Kalshi First and Stable Decidability Observability Negative Evidence (arXiv 2609.16642)

## Provenance

- **Source**: arXiv:2609.16642v1 [q-fin.TR]
- **Author**: Maksym Nechepurenko
- **Submitted**: 2026-09-15
- **DOI**: https://doi.org/10.48550/arXiv.2609.16642
- **URL**: https://arxiv.org/abs/2609.16642
- **SSRN (source-reported)**: https://ssrn.com/abstract=7421261
- **HTML/PDF reviewed 2026-09-20**: abstract page (full experimental tables not fully re-audited beyond abstract-level claims this cycle)
- **Comments (source)**: 13 pages, 2 figures
- **Deduplication audit (2026-09-20; origin/main)**: No prior record cites `arXiv:2609.16642`, “first decidability,” or “stable decidability” on Kalshi. Adjacent records are different:
  - `kalshi-prediction-market-pricing-wedge-executable-spread-falsification-2026-09-13.md` — pricing wedge / fee / calibration **execution falsification**; not rule–evidence settlement clocks.
  - `kalshi-btc-event-contract-spot-hedge-2026-09-15.md` — BTC event-contract hedge construction; not observability of contractual outcome timing.
  - Other prediction-market / Polymarket records — market-making, arb, or bias mechanisms; not Kalshi rule-version decidability.

## Economic mechanism

### Source-reported

Source-reported problem: public evidence can become sufficient to settle a prediction-market contract **before** the venue records its first determination, but the boundary depends on rule version, exact release object, source hierarchy, correction history, and unfinished contract conditions.

Source-reported definitions:

- **First decidability:** earliest contemporaneous singleton in the rule–evidence mapping.
- **Stable decidability:** retrospective earliest time after which the same singleton remains unchanged through finalization.

Source-reported completed tests (abstract):

1. **Frozen blind pilot:** 25 identities and blinding checks passed; current rule text recovered for all 25; **no** exact or bounded historical rule version and **no** exact or bounded official source-release object recovered.
2. **Full historical recovery:** 152,694 ordinary tickers; 11,530 exact event identities; 6,540 read-only official requests; **zero** historically eligible events and **zero** historically eligible tickers.
3. **Prospective infrastructure shakedown:** observation capability for three source programmes across 25 markets; integrity revalidation of 781,266 lifecycle frames; 22 closed lower-bounded reconnect receipts; no unresolved reconnect gap; no due-but-missed official release; inactive price layer.
4. Production evidence enrollment active; prospective sample frozen only at enrollment close; frozen target size selected mechanically under registered full/reduced/exploratory/no-go disposition.

Source-reported scope limits (critical):

- Result is an **observability result**, **not** a claim that no market was decidable or that public evidence never existed.
- **No** contractual-decidability clock, human-adjudication, price, or cross-venue result is reported in this paper.

### Research interpretation

This is **family-level methodology / observability negative evidence** for strategies that assume historical public evidence can be timestamped into a clean “decidable before venue X” edge on Kalshi — not a trading entry/exit rule.

Hypothesized research relevance:

1. **Historical edge samples may be unconstructible:** Zero historically eligible events/tickers under the paper’s recovery protocol means many backtests that invent “evidence became sufficient at time T” cannot be grounded in recovered rule-version + release-object pairs.
2. **Current rule text ≠ historical rule:** Blind pilot recovered current rules for 25/25 but failed exact/bounded historical rule versions and source-release objects — PIT rule audits are first-order for settlement-edge claims.
3. **Boundary for early-settlement / information-arb records:** Any Scout record claiming public evidence settles Kalshi contracts earlier than the venue must pre-declare rule-version provenance and release-object identity; this paper **strengthens** that boundary.
4. **Not proof of no edge:** Explicitly not “markets were never decidable”; only that this recovery found zero historically eligible units and reports no price/clock result.

Component roles (normalized):

```text
Not a trading signal.
Evidence class: observability / methodology negative evidence for Kalshi decidability clocks.
Required practice (research-proposed): recover exact historical rule version + official source-release object before claiming first/stable decidability; report eligibility counts; do not substitute current rule text for PIT rules.
```

## Signal

Not applicable as a trading signal. No long/short entry, holding period, or position sizing in this source for alpha reconstruction.

Research evaluation sketch only (research-proposed):

- **Formation timestamp:** first/stable decidability times as defined by the paper’s rule–evidence mapping (not reported as tradable clocks in this paper).
- **Lookback:** full historical recovery over stated ticker/event identity sets; prospective enrollment freeze at close.
- **Entry / Exit / Holding:** N/A.
- **Parameters:** pilot N=25; historical 152,694 / 11,530 / 6,540; prospective shakedown 25 markets, 781,266 frames, 22 reconnect receipts; three source programmes.

## Required data

- **Instrument / universe (source-reported):** Kalshi ordinary tickers and exact event identities; three source programmes in prospective shakedown.
- **Venue:** Kalshi official rule text and official source-release objects (read-only official requests).
- **Market type:** prediction-market event contracts / rule–evidence mapping — not perpetual futures alpha.
- **Fields:** rule version identity, release object identity, source hierarchy, correction history, unfinished contract conditions, lifecycle frames, reconnect receipts.
- **Point-in-time:** central to the design — historical rule version and release object must be exact/bounded, not current-text substitutes.
- **Timestamps:** first vs stable decidability clocks as defined in the paper; **no tradable price clock reported**.
- **Costs:** not a trading fee model; official request budget appears in recovery counts (6,540 read-only requests).

## Execution assumptions

No trading execution proposed. “Execution” in the paper is evidence enrollment, rule recovery, and lifecycle integrity observation — not order placement.

## Evidence

### Source-reported

All counts in this record trace to arXiv:2609.16642v1 abstract (2026-09-15 / reviewed 2026-09-20): blind pilot 25/25 current-rule recovery with zero exact/bounded historical rule versions and zero exact/bounded official source-release objects; full historical recovery 152,694 tickers / 11,530 event identities / 6,540 official requests with **zero** historically eligible events and tickers; prospective shakedown three programmes, 25 markets, 781,266 lifecycle frames, 22 closed lower-bounded reconnect receipts, no unresolved gap, no missed official release, inactive price layer; explicit non-claims (not “never decidable”; no price/cross-venue result).

### Independently reproduced

`not independently reproduced`

### Negative evidence

- Source-reported **zero historically eligible** events/tickers under the recovery protocol (core incremental observability negative).
- Source-reported failure to recover exact/bounded historical rule versions and source-release objects even when current rule text recovered (PIT rule audit gap).
- Explicit paper boundary: observability only — absence of eligible units is **not** evidence that no market was ever decidable.
- No independent re-run of the recovery pipeline in our stack this cycle.
- Absence of our replication is not evidence against the paper’s counts.

## Falsification plan

Research-proposed evaluation standards for future Kalshi early-settlement / public-evidence-edge records (not a source trading rule):

1. **Rule-version gate (research-defined falsification threshold):** Any claimed first/stable decidability time must cite an **exact or bounded historical rule version** and **official source-release object**. Fail any backtest that substitutes current rule text for PIT rules.
2. **Eligibility accounting:** Report counts of events/tickers that pass recovery; if eligibility is zero under a documented protocol, reject historical edge samples built on unrecovered identities.
3. **Blind identity integrity:** Require identity + blinding checks analogous to the pilot; fail claims that cannot re-identify the contract under study.
4. **Lifecycle continuity:** Pre-declare reconnect/gap policy; fail if unresolved gaps or missed official releases could move the alleged decidability time.
5. **No price smuggled in:** Keep observability clocks separate from tradable PnL; fail records that present this paper’s counts as a price edge (paper reports none).
6. **Competing explanation:** If venue determination lag alone explains “early” fills without rule–evidence mapping, the decidability mechanism is non-load-bearing.
7. **Action on failure:** Keep related Kalshi early-settlement records `research-only`; do not promote historical decidability clocks without recovered rule/release provenance.

## Crypto portability

**Portability: `unproven` / `adapted` for crypto prediction markets (Polymarket etc.); `not applicable` as a perp/spot trading port.**

- Mechanism is Kalshi-specific rule text, official release objects, and CFTC-style contract finalization.
- Crypto venues differ in resolution sources, oracle timing, and rule mutability — clocks would need re-derivation.
- Risks if misused: treating zero historical eligibility as “no edge exists,” or treating current rules as historical.
- Crypto portability is not authorization to trade.

## Limitations

- **Review depth:** abstract-level claims this cycle; full PDF tables / recovery code not fully audited.
- **not independently reproduced**
- **Not a strategy record:** no reconstructable entry/exit; incremental value is **Kalshi decidability observability negative evidence** (settlement-edge family boundary).
- Do not overclaim: paper explicitly denies “never decidable” and reports **no** price or cross-venue result.
- Zero eligibility is protocol-conditional — a different recovery protocol might differ; that does not license unrecovered PIT claims.
- SSRN mirror identity preserved; primary is arXiv.

## Implementation status

No implementation in our research stack. Does not modify NautilusTrader/PyBroker; does not authorize Paper/Testnet/Live.

`implementation_status: not-implemented`

Source-side: paper reports infrastructure shakedown and active enrollment; **not** treated as our validation or as a trading system.

## Adoption boundary

Research-only. Presence here does **not** mean any Kalshi strategy or decidability clock is profitable, validated, or approved.

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

## Related Wiki records

No stable Hermes Wiki Brain path known for this arXiv capture at write time. Do not fabricate Wiki links.

In-repo related: `kalshi-prediction-market-pricing-wedge-executable-spread-falsification-2026-09-13.md`; `kalshi-btc-event-contract-spot-hedge-2026-09-15.md`; other prediction-market mechanism records (different questions).

## Sources

1. Maksym Nechepurenko. "From Public Evidence to Contractual Outcome: First and Stable Decidability on Kalshi." arXiv:2609.16642v1 [q-fin.TR], September 15, 2026. https://arxiv.org/abs/2609.16642
2. SSRN abstract (source-reported): https://ssrn.com/abstract=7421261
