---
schema: strategy-research-record-v1
title: "MarketSenseAI Multi-Agent LLM Adaptive Equity Selection with Regime-Rotating Agent Attribution"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - LLM
  - multi-agent
  - equity
  - cross-sectional
status: research-only
confidence: medium
source_as_of: 2026-04-19
sources:
  - "George Fatouros and Kostas Metaxas, 'Signal or Noise in Multi-Agent LLM-based Stock Recommendations?', arXiv preprint arXiv:2604.17327v1 [q-fin.PM, cs.AI, q-fin.ST], submitted April 19, 2026. DOI: 10.48550/arXiv.2604.17327. https://arxiv.org/abs/2604.17327"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# MarketSenseAI Multi-Agent LLM Adaptive Equity Selection with Regime-Rotating Agent Attribution

## Provenance

- **Primary Source:** George Fatouros and Kostas Metaxas, *"Signal or Noise in Multi-Agent LLM-based Stock Recommendations?"*, arXiv preprint `arXiv:2604.17327v1 [q-fin.PM, cs.AI, q-fin.ST]`, submitted April 19, 2026.
- **DOI:** https://doi.org/10.48550/arXiv.2604.17327
- **Stable URL:** https://arxiv.org/abs/2604.17327
- **Full text HTML:** https://arxiv.org/html/2604.17327v1
- **Length:** 22 pages, 10 figures
- **System website:** https://marketsense-ai.com
- **Developer:** Alpha Tensor Technologies (https://www.alpha-tensor.ai)

## Economic mechanism

### Source-reported

MarketSenseAI is a deployed multi-agent LLM equity-research platform that routes four specialist agents—News, Fundamentals, Dynamics, and Macro—through a synthesis agent. Each specialist independently produces a text analysis for a given stock and date. The synthesis agent reads all four expert analyses and generates a free-text equity thesis together with a five-point ordinal recommendation (strong sell, sell, hold, buy, strong buy). The system operates on a monthly cadence (first Friday of each month).

The authors hypothesise that the multi-agent architecture captures complementary information channels—company-level news developments, fundamental financials, price-action/technical signals, and macroeconomic context—and that the synthesis agent adaptively integrates these channels, weighting each specialist according to prevailing market regime and sector conditions. The resulting strong-buy signal is proposed as a universe-filter that improves the ex-ante properties of any downstream portfolio-construction process.

### Research interpretation

The hypothesised alpha mechanism is **adaptive multi-source information integration with regime-conditioned agent weighting**. The core falsifiable claim is that an ensemble of LLM specialists, each processing a distinct information modality (news, fundamentals, price dynamics, macro), can produce cross-sectional stock-selection signals with genuine predictive content that persists after controlling for market beta and passive exposure.

The regime-rotation component adds a second testable layer: agent contribution weights (extracted via NNLS attribution of thesis embeddings onto agent embeddings) rotate with market regime, with Fundamentals dominating during stock-specific quality-driven periods, Macro dominating during macro-driven episodes (e.g., Fed rate cuts, elections, tariff shocks), and Dynamics acting as an episodic momentum signal. This rotation is the proposed mechanism for why no single agent dominates and why the ensemble outperforms any individual component.

**Component roles:**
- News agent: ticker-specific progressive news analysis (company-level developments)
- Fundamentals agent: quantitative financials, filings, earnings transcripts
- Dynamics agent: price-action and technical signals
- Macro agent: sector-level and macroeconomic context
- Synthesis agent: integrates all four, produces thesis + ordinal recommendation

## Signal

- **Formation timestamp:** First Friday of each month; signals are generated live at each observation date (not retroactively).
- **Lookback:** Each specialist agent analyses its respective data modality up to the observation date. No explicit lookback window is specified in the paper; each agent processes the most recent available data for its modality.
- **Universe:** S&P 500 cohort (467 stocks present from post-expansion date onward); S&P 100 cohort (94 stocks).
- **Long entry:** Strong-buy recommendations only (7.5% of S&P 500 observations, 10.5% of S&P 100 observations). Within the actionable buy+strong-buy universe, ordinal score maps buy→1, strong buy→2.
- **Exit:** Monthly rebalancing on first-Friday cadence; one-month buy-and-hold forward returns.
- **Position sizing:** Equal-weight across all strong-buy picks each month.
- **Holding period:** One month (monthly rebalance).
- **Parameters:** No tunable parameters reported; the system is a deployed production platform, not a backtested strategy with optimised parameters.
- **Signal class distribution (S&P 500):** Strong sell 2.0%, Sell 3.2%, Hold 78.8%, Buy 8.4%, Strong buy 7.5%.
- **Signal class distribution (S&P 100):** Strong sell 1.5%, Sell 2.3%, Hold 76.2%, Buy 9.4%, Strong buy 10.5%.

**Falsification-relevant operational choices (research-defined):**
- The strong-buy threshold is the system's own output, not a researcher-defined cutoff.
- Equal-weight sizing is the paper's evaluation convention; the paper explicitly notes that the strong-buy signal can sit upstream of any portfolio-construction method (risk-parity, mean-variance, factor overlay).

## Required data

- **Instrument:** US large-cap equities (S&P 500 and S&P 100 constituents).
- **Universe:** Fixed cohorts (467 S&P 500 stocks from Sep 2024 onward; 94 S&P 100 stocks from May 2023 onward). No survivorship adjustment beyond the fixed-cohort design.
- **Venue:** US equity exchanges (specific venue not stated).
- **Timeframe:** Monthly observation dates (first Friday); one-month forward returns.
- **Fields:** Financial news, fundamental data (financials, filings, earnings transcripts), price-action/technical signals, macroeconomic/sector data. Specific data vendors or field definitions not stated in the paper.
- **Embedding:** All text outputs encoded with OpenAI's text-embedding-3-small (D=1536).
- **Point-in-time:** All agent outputs produced through live execution at each observation date; for dates beyond LLM training cut-off, data is necessarily absent from pre-training corpus (eliminating knowledge leakage).
- **Timestamp:** Monthly cadence; specific timezone not stated (implied US market timezone).
- **Missing data:** Not explicitly addressed in the paper.

## Execution assumptions

- **Signal-to-order timing:** Monthly rebalance on first Friday; forward returns measured as one-month buy-and-hold.
- **Order type:** Not specified (assumed market order for equal-weight evaluation).
- **Fill model:** Not specified.
- **Fees/spread/slippage:** The paper states: *"typical implementation drag (bid-ask spread, market impact) would be well below 30 bps/month, leaving substantial headroom before the signal becomes unprofitable net of costs"* (Section 5.1). No formal transaction cost model is applied. This is a data gap — the cost assumption is qualitative, not quantified.
- **Capacity:** ~35 large-cap equal-weight positions per month on S&P 500; ~10 on S&P 100. Large-cap US equities with monthly rebalancing implies high liquidity and low market impact.
- **Leverage/margin:** Not specified (assumed no leverage).
- **Shorting:** Sell-side signals are reported but not tested for actionability. The paper notes: *"Effective implementation of short positions depends on short interest and short ratios, borrow availability, and liquidity metrics... The absence of these inputs means the sell-side results reported here should be read as a data-scope limitation."*
- **Latency:** Not relevant for monthly-frequency signals.

## Evidence

### Source-reported

All figures trace to Fatouros & Metaxas (arXiv:2604.17327v1); section/table/figure anchors per group below.

**Monte Carlo portfolio test (primary result — Section 5.1, Table 3; Figures 4–5; per-date detail Appendix A Table 8):**
- S&P 500 (19 months, Sep 2024–Mar 2026):
  - Strong-buy mean monthly return: +2.18%
  - EW universe benchmark (approximating RSP): +1.15%
  - Excess vs EW benchmark: +1.02%/month
  - Compound return (full period): +46.8% (strong-buy) vs +21.6% (EW benchmark)
  - Excess compound: +25.2 percentage points
  - Percentile rank in 10,000 MC null: 99.7th
  - pp-value: 0.003
  - Win rate: 11/19 months (57.9%)
  - Average strong-buy picks per month: 35.1

- S&P 100 (35 months, May 2023–Mar 2026):
  - Strong-buy mean monthly return: +2.02%
  - EW universe benchmark (approximating EQWL): +1.47%
  - Excess vs EW benchmark: +0.55%/month
  - Compound return: +93.2% (strong-buy) vs +62.7% (EW benchmark)
  - Excess compound: +30.5 percentage points
  - Percentile rank in MC null: 83.4th
  - pp-value: 0.163 (not significant, driven by small ~10-stock average selection; Table 3 reports 0.166 mean-monthly / 0.163 compound, Abstract rounds to p=0.17)

**IC/ICIR analysis (within buy+strong-buy universe — Section 5.4, Table 6 Panels A/B; score result text; Figure 8):**
- S&P 500 ordinal score: mean IC = +0.051, ICIR = +0.489, t = +2.13, p = 0.024
- S&P 100 ordinal score: mean IC = +0.018, ICIR = +0.080, p = 0.319 (underpowered)
- Fundamentals pooled IC on S&P 500: +0.052 (p = 0.049)
- Macro pooled IC on S&P 100: +0.079 (p = 0.042)

**NNLS attribution (methods Sections 3.2–3.3; results Section 5.2; Figure 2; Table 4):**
- Thesis reconstruction cosine: mean C^TR = 0.944 (S&P 500), 0.936 (S&P 100)
- Agent contributions rotate with regime; no single agent dominates across all dates/sectors

**Beta analysis (Section 6 "Market beta and downside protection"; Figure 10a–b):**
- Portfolio beta vs EW proxy: β̂ = 0.865 (below unity)
- Jensen's α̂ = +1.18%/month (annualised +14.2%, t = 1.45, p = 0.17, R² = 0.60)
- Down-market months: strong-buy -2.00% vs EW -3.32% (+1.31% excess)
- Up-market months: strong-buy +5.22% vs EW +4.39% (+0.82% excess)

**Downside behaviour (S&P 500 — Section 5.3, Table 5; Figure 6):**
- Strong-buy: upside +6.39%, downside -5.95%, hit rate 58.4%, UpDn ratio 1.07
- Hold: upside +5.27%, downside -6.71%, hit rate 53.4%, UpDn ratio 0.79
- Bootstrap Δ(UpDn) = +0.17, 95% CI [-0.03, +0.37], one-tailed p = 0.050

These results have not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- S&P 100 Monte Carlo result is directional but does not reach formal significance (p = 0.163–0.17), attributed to small average selection (~10 stocks) producing high variance.
- Sell and strong-sell stocks earn positive average returns over the sample period (+1.65% and +2.98% respectively for S&P 500), indicating contrarian bearish calls underperformed in this generally risk-on environment. The paper flags this but notes the sample is too small (n < 470 total sell-side observations) for formal testing.
- Agent date-level ICs are small and insignificant for all four agents in both cohorts (all p > 0.08), meaning agent weights carry pooled cross-sectional information but not consistent month-by-month timing.
- The paper acknowledges that the S&P 500 period (Sep 2024–Mar 2026) was characterised by generally positive equity returns; whether outperformance persists in a sustained bear market is unknown.
- Dynamics agent has significantly negative pooled IC on S&P 500 (−0.069, p = 0.009), consistent with momentum being episodic rather than persistent.

## Falsification plan

1. **Extended out-of-sample period:** The primary result rests on 19 monthly observations. Extend to ≥60 months across multiple market regimes (bull, bear, sideways, high-volatility). **Failure rule:** If MC pp-value degrades to > 0.05 with T ≥ 48, the S&P 500 result is not robust.
2. **Broader universe test:** Replicate on Russell 1000, mid-cap, or international equiverses. **Failure rule:** If strong-buy excess compound return < +10pp over 24+ months in any broad universe, the signal may be specific to S&P 500/100 large-caps.
3. **Regime breakdown:** Split the sample into up-market and down-market months. **Failure rule:** If down-market alpha is negative (strong-buy underperforms EW in down months), the downside protection claim is falsified.
4. **Agent ablation:** Remove one specialist agent at a time and re-evaluate. **Failure rule:** If removing any single agent does not degrade MC pp-value, the multi-agent integration adds no incremental value over the best single agent.
5. **Cost sensitivity:** Apply 30–50 bps/month implementation drag (spread + impact + fees). **Failure rule:** If net-of-cost excess compound return drops below +15pp on S&P 500, the signal's economic significance is materially reduced.
6. **Parameter perturbation:** Vary the recommendation threshold (e.g., include buy+strong-buy vs strong-buy only). **Failure rule:** If including buy signals dilutes the MC pp-value below 0.05, the strong-buy concentration is essential and the signal is fragile.
7. **LLM version sensitivity:** Re-run with different LLM backends (as tested in the AlphaSchema paper for a related framework). **Failure rule:** If signal quality degrades substantially with a different LLM version, the alpha is model-dependent rather than mechanism-driven.

## Crypto portability

**Unproven.**

The paper studies US large-cap equities only. The multi-agent LLM architecture is modality-agnostic in principle (news, fundamentals, price dynamics, macro could all be adapted to crypto), but:

- Crypto markets lack the structured fundamental data (financials, filings, earnings transcripts) that the Fundamentals agent relies on.
- The monthly cadence may be too slow for crypto's higher-frequency regime dynamics.
- Crypto-specific data (on-chain flows, funding rates, open interest, DEX volume) would require entirely new specialist agents.
- The regime-rotation mechanism (Fundamentals leading in quality-driven periods, Macro in macro-driven episodes) may map differently in crypto, where macro and sentiment dominate more consistently.
- No crypto-specific evidence exists; this is a ported hypothesis.

## Limitations

- **Short sample:** 19 monthly observations for the primary S&P 500 result; formal significance rests on a narrow window.
- **No formal cost model:** Transaction costs are assumed to be "well below 30 bps/month" but not modelled.
- **Single system case study:** Results are specific to MarketSenseAI; not generalisable to all multi-agent LLM systems.
- **Pooled IC is directional only:** Within-date cross-sectional dependence makes pooled IC unsuitable for conventional significance testing.
- **Sell-side signals untested:** Bearish signals show positive returns but the sample is too small and short-selling implementation is not modelled.
- **Market regime:** The S&P 500 period was generally positive; sustained bear market performance unknown.
- **LLM dependency:** The system uses specific LLM backends (not disclosed which models); results may not replicate with different models.
- **Data availability:** Specific data vendors, field definitions, and preprocessing steps are not disclosed.
- **Not independently reproduced.**

## Implementation status

Not implemented in our research stack. This is a source-captured research record of a deployed external system. No PyBroker, Nautilus, paper, testnet, or live verification has been performed.

## Adoption boundary

This record is research material only. Its presence in this repository does not mean:
- profitable
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

The strong-buy signal is source-reported as a deployed production system with live-generated signals, but this is an external system's claim, not our own verification.

## Related Wiki records

- [[quant/alphacrafter-harness-driven-multi-agent-llm-alpha-discovery-2026-09-03]] — AlphaCrafter is a multi-agent LLM framework for cross-sectional factor generation; MarketSenseAI is a deployed multi-agent LLM system for equity selection with portfolio-level validation. Different mechanisms: AlphaCrafter generates factor formulas; MarketSenseAI synthesises specialist analyses into stock recommendations.
- [[quant/finsmart-market-aligned-reinforcement-learning-sentiment-alpha-2026-09-02]] — FinSMART optimises sentiment signals via RL; MarketSenseAI uses multi-agent LLM synthesis. Both involve LLM-based financial signals but different architectures and evaluation frameworks.
- [[quant/aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03]] — AEAP/SEADS focuses on LLM-agentic formulaic alpha mining; MarketSenseAI operates at the recommendation/portfolio level rather than formula discovery.

## Sources

1. George Fatouros and Kostas Metaxas, *"Signal or Noise in Multi-Agent LLM-based Stock Recommendations?"*, arXiv preprint `arXiv:2604.17327v1 [q-fin.PM, cs.AI, q-fin.ST]`, submitted April 19, 2026. DOI: 10.48550/arXiv.2604.17327. https://arxiv.org/abs/2604.17327. Full text HTML: https://arxiv.org/html/2604.17327v1.
