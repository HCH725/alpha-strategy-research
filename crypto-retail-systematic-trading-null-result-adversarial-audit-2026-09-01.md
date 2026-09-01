---
schema: strategy-research-record-v1
title: "Anatomy of a Null Result: Retail Systematic Trading in Crypto Perpetuals (2018-2026)"
created: 2026-09-01
updated: 2026-09-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - null-result
  - negative-evidence
  - overfitting
  - perpetual-futures
  - systematic-trading
  - adversarial-audit
status: research-only
confidence: high
source_as_of: 2026-07-27
sources:
  - "Ricardo Castellanos Macias, 'Anatomy of a Null Result: A Pre-registered, Adversarially Audited Case Study of Retail Systematic Trading in Crypto Perpetuals (2018-2026)', SSRN 7085378, 2026. DOI: https://doi.org/10.2139/ssrn.7085378"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Anatomy of a Null Result: Retail Systematic Trading in Crypto Perpetuals (2018-2026)

## Provenance

- Paper: Ricardo Castellanos Macias, "Anatomy of a Null Result: A Pre-registered, Adversarially Audited Case Study of Retail Systematic Trading in Crypto Perpetuals (2018-2026)", SSRN Electronic Journal, 2026.
- DOI: https://doi.org/10.2139/ssrn.7085378
- OpenAlex ID: https://openalex.org/W7171320422
- Author: Ricardo Castellanos Macias (Independent Researcher, Toledo, Spain)
- Date: 2026 (created 2026-07-27 per OpenAlex)
- Source URL: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7085378

## Economic mechanism

### Source-reported

This is a **null-result paper** — it does not propose an alpha strategy but rather documents the systematic failure to find one. The author conducted a pre-registered, adversarially audited investigation of retail systematic trading strategies in cryptocurrency perpetual futures over the period 2018–2026. Over 18 experiment families, the author evaluated a strategy space targeting crypto perpetual futures. The key finding is stated bluntly: "The engineering survived every audit thrown at it; the alpha did not survive the engineering." The paper notes that the academic literature on quantitative crypto strategies is subject to significant publication bias, and aims to contribute a more realistic picture of alpha discovery in cryptocurrency markets.

### Research interpretation

This record captures a methodologically rigorous **negative result** — the finding that retail-accessible systematic strategies in crypto perpetuals did not produce reliable alpha over an 8-year sample after adversarial auditing. The hypothesized mechanisms tested likely include trend-following, mean-reversion, momentum, factor-based, and other standard systematic approaches (the exact experiment families are not available from the abstract alone). The null finding suggests that whatever weak signals may exist in crypto perpetuals are either:

1. Insufficient to overcome transaction costs and funding at retail fee levels;
2. Subject to severe overfitting that survives standard backtesting but not adversarial audit;
3. Degraded by publication bias in the academic literature (positive results published, nulls discarded).

This is a critical calibration record for any quantitative research program: it provides evidence that the bar for genuine alpha in crypto perpetuals is higher than naive backtesting suggests.

## Signal

No actionable signal is proposed. This is a null-result record documenting the failure to find exploitable signals after adversarial auditing.

## Required data

- Universe: Crypto perpetual futures (specific pairs and venues not fully specified in available abstract)
- Period: 2018–2026
- Data type: Likely OHLCV and funding rate signals (inferred from title context; not confirmed from full text)
- Specific data requirements: Unknown from abstract alone

## Execution assumptions

Not applicable — no strategy is proposed. The paper documents the failure of strategies that were tested under realistic execution assumptions including transaction costs and adversarial auditing.

## Evidence

### Source-reported

- 18 experiment families evaluated over 2018–2026
- All experiment families produced null results after adversarial auditing
- "The engineering survived every audit thrown at it; the alpha did not survive the engineering"
- The paper identifies publication bias in the academic quantitative crypto strategy literature as a compounding problem

### Independently reproduced

Not independently reproduced.

### Negative evidence

This entire record IS negative evidence. The paper's core contribution is documenting that systematic retail trading strategies in crypto perpetuals did not produce reliable alpha over an 8-year period when subjected to adversarial auditing.

## Falsification plan

This record itself is a falsification of the hypothesis that retail-accessible systematic strategies produce reliable alpha in crypto perpetuals. To falsify this null finding:

- A sufficiently large, out-of-sample, adversarially audited sample showing consistent alpha would be required
- The audit must survive the same adversarial framework applied by Castellanos Macias
- Publication bias must be controlled for (pre-registration, adversarial audit)
- Transaction costs, funding, and slippage must be realistically modeled

## Crypto portability

direct — this study is already conducted on crypto perpetual futures.

## Limitations

- Full abstract text not available (SSRN behind Cloudflare); record is based on OpenAlex metadata and Google Scholar snippets
- Specific experiment families, parameters, and methodology details are not available from the abstract
- The paper is a working paper (SSRN) and may not have undergone peer review
- "Retail" systematic trading may not capture institutional-grade strategies with better execution, lower fees, or proprietary data
- The null result does not prove alpha is impossible — only that the specific strategies tested under the specific conditions tested did not survive auditing

## Implementation status

Not implemented. This is a null-result record — no strategy to implement.

## Adoption boundary

This record is research material only. Its presence in this repository does not mean:

- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

The finding is that the tested strategies were NOT profitable after adversarial auditing.

## Related Wiki records

- [[crypto-perpetual-futures-self-benchmarked-factor-alpha-2026-09-01]] (related: self-benchmarked factor approach to perpetual futures alpha)
- [[crypto-adaptive-trend-following-asymmetric-portfolio-2026-09-01]] (related: trend-following approach that may be among the strategies tested)

## Sources

1. Castellanos Macias, R. (2026). "Anatomy of a Null Result: A Pre-registered, Adversarially Audited Case Study of Retail Systematic Trading in Crypto Perpetuals (2018-2026)." SSRN Electronic Journal. DOI: https://doi.org/10.2139/ssrn.7085378. OpenAlex: https://openalex.org/W7171320422.
