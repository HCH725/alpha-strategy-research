---
schema: strategy-research-record-v1
title: "Agentic AI Nowcasting Stock Returns: Asymmetric Winner-Picking via LLM Web Search"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - llm
  - alpha-signal
  - stock-selection
status: research-only
confidence: medium
source_as_of: 2026-01-17
sources:
  - "https://arxiv.org/abs/2601.11958"
  - "https://github.com/mapledust0/AI-Stock-Nowcasting/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Agentic AI Nowcasting Stock Returns: Asymmetric Winner-Picking via LLM Web Search

## Provenance

- **Paper:** arXiv:2601.11958v1 (q-fin.GN; also q-fin.PM, q-fin.TR)
- **Authors:** Zefeng Chen, Darcy Pu (Peking University)
- **Submitted:** 17 January 2026
- **GitHub:** https://github.com/mapledust0/AI-Stock-Nowcasting/
- **Sample period:** April 2025 – January 2026 (~158 trading days, ~155,891 daily stock-level observations)
- **Universe:** Russell 1000 constituents (~1,000 largest US equities, ~93% of domestic equity market cap)
- **Data source:** LSEG DataStream for daily financial data; AI model web interface (latest version with live search enabled) for signal generation

## Economic mechanism

### Source-reported

The authors hypothesize that an LLM agent deployed in a fully agentic (autonomous web-searching) workflow can nowcast stock returns by synthesizing heterogeneous real-time information from the live web. The model autonomously generates search queries, browses financial news sites and social media (including X/Twitter), filters for relevant events, and synthesizes information into quantitative attractiveness scores (-5 to +5) for each stock daily. The mechanism is that genuinely positive news generates coherent, consensus-positive signals across sources, while negative news is contaminated by strategic corporate obfuscation and social media noise, creating an asymmetric information environment where AI excels at identifying top winners but cannot reliably distinguish losers from average stocks.

### Research interpretation

This is a **cross-sectional stock-selection alpha** driven by an LLM agent's autonomous information synthesis. The hypothesized mechanism is:

1. **Information aggregation advantage:** The LLM agent processes and synthesizes a broader, more heterogeneous information set than any single human analyst or traditional NLP pipeline, because it autonomously decides what to read and how to interpret it in real-time.
2. **Asymmetric information structure:** Positive news (earnings beats, contract wins, product launches) generates clear, consensus signals; negative news is structurally noisier due to corporate obfuscation, "buy the dip" social media sentiment, and speculative content proliferation. This asymmetry is hypothesized to be a feature of the online information environment, not the model architecture.
3. **Top-concentration effect:** The predictive power is highly concentrated in the very top-ranked stocks (Top-10 to Top-20); expanding beyond this tier rapidly dilutes alpha. Bottom-ranked stocks show no statistically significant negative alpha.

This is a ported hypothesis from equities to crypto. The mechanism (LLM autonomous information synthesis) could potentially apply to crypto markets, but the asymmetric information structure (corporate obfuscation of negative news) may be less relevant in crypto, where negative sentiment often amplifies rather than dampens.

## Signal

### Formation timestamp

Predictions are generated overnight (after 4:00 PM ET market close on day t-1, before market open on day t). The signal is the AI-generated "Attractiveness Score" for each stock.

### Lookback

The LLM agent has access to real-time web information at the time of query. No specific historical lookback window is defined — the model autonomously decides what information to retrieve based on its web search queries.

### Long entry

Rank all stocks by Attractiveness Score in descending order. Go long the Top-20 stocks (value-weighted). Ties at the N-th rank are resolved by prioritizing larger market capitalization for liquidity.

### Short entry

The signal is **asymmetric** — bottom-ranked stocks do not generate statistically significant negative alphas. A long-short implementation would suffer from noise and transaction costs on the uninformative short leg. The authors recommend a long-only concentrated strategy.

### Exit / holding period

Daily rebalancing. Positions entered at the opening auction of day t and liquidated at the opening auction of day t+1 (open-to-open returns). For longer signal horizons (weekly, monthly, quarterly), overlapping sub-portfolios are used with 1/K weighting.

### Parameters

- **Signal horizons tested:** 1 day, 1 week, 1 month, 3 months, 6 months, 1 year
- **Portfolio size:** Top-N where N ranges from 10 to 100; Top-20 is the primary specification
- **Rebalancing:** Daily (value-weighted)
- **Score scale:** -5 (Strong Sell) to +5 (Strong Buy)
- **Model:** Latest version of a leading US-based AI model with web search enabled (specific model not named in the paper)

### Position sizing

Value-weighted within the Top-20 portfolio.

### Fully specified vs underspecified

The signal construction is well-specified for the Top-20 long-only implementation. However:
- The specific LLM model version is not named (described as "a leading US-based AI model")
- The prompt template is described but not fully reproduced (Appendix A contains details)
- The web search queries are autonomously generated by the model, not pre-specified
- **Underspecified:** Exact prompt wording, model version, and search query generation details

## Required data

- **Instrument:** Russell 1000 constituents (US large-cap equities)
- **Venue:** US equity markets (NYSE, NASDAQ)
- **Market type:** Equities (spot)
- **Timeframe:** Daily (open-to-open returns)
- **Fields:** Daily OHLCV, market cap, bid-ask spreads, EPS, analyst consensus, social media sentiment
- **Point-in-time:** Predictions collected overnight before market open; strictly out-of-sample by construction
- **Timestamp:** 4:00 PM ET cutoff for signal generation; opening auction for execution
- **Missing data:** Not explicitly addressed in the reviewed sections

## Execution assumptions

- **Signal-to-order timing:** Overnight signal generation → opening auction execution on day t
- **Order type:** Market orders at the opening auction
- **Fill model:** Assumed full fill at opening auction price
- **Fees/spread:** Average portfolio spread 1.63 bps (daily signal); market benchmark 1.48 bps. Transaction costs represent <10% of gross alpha.
- **Slippage:** Not explicitly modeled beyond spread; authors note closing spreads average ~1.50 bps, confirming liquidity is not binding
- **Capacity:** Strategy trades Russell 1000 constituents with median market cap $15.2B and median daily dollar volume $365M — highly liquid universe
- **Leverage:** Not specified
- **Latency:** Overnight signal generation eliminates HFT latency concerns; execution at opening auction
- **Partial fills / failures:** Not addressed

## Evidence

### Source-reported

From Table 4 (Column 5, FF6 specification) and Table 5 of the paper:

- **Daily signal horizon Top-20 portfolio:** FF6 alpha = 0.334% per day (t = 2.96, significant at 1%), annualized Sharpe = 3.23
- **Weekly signal horizon Top-20:** FF6 alpha = 0.238% per day (t = 2.72), annualized Sharpe = 1.22
- **Monthly signal horizon Top-20:** FF6 alpha = 0.231% per day (t = 2.25), annualized Sharpe = 0.49 (annualized)
- **Quarterly signal horizon Top-20:** FF6 alpha = 0.181% per day (t = 1.41), not significant
- **Bottom-20 portfolios:** Alpha statistically indistinguishable from zero across all horizons
- **Long-Short daily alpha:** 0.463% per day (t = 2.69), Sharpe = 2.23

The paper also reports (from abstract): daily FF5+momentum alpha of 18.4 bps (t = 2.46) for the Top-20. The discrepancy with the FF6 table values may reflect different specifications or subsamples; the FF6 table (Table 4, Column 5) reports 0.334% daily alpha.

**Factor exposures of Top-20 (daily signal):** Low market beta (0.347, t = 1.82), strong negative HML loading (-0.883, t = -3.60), insignificant momentum (-0.194, t = -1.18). The portfolio tilts toward growth stocks with defensive characteristics.

**Transaction costs:** Average portfolio spread 1.63 bps for daily signal; closing spreads ~1.50 bps. Costs <10% of gross alpha.

**Consistency tests (Table 3):** Split-half reliability ρ = 0.942; rank stability ρ = 0.902; KS distribution test 100% rejection rate across 30 tested stocks.

This result has not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The alpha is highly concentrated in the Top-10 to Top-20; expanding to Top-100 dilutes alpha from ~0.18% to ~0.12% per day.
- Bottom-ranked stocks show no significant negative alpha — the signal is asymmetric.
- The quarterly signal horizon produces attenuated, statistically insignificant alpha (t = 1.41).
- The sample period is short (~9 months, ~158 trading days) and may not survive regime changes.
- The specific LLM model version is not named; results may be model-version-dependent.
- The paper notes this is a "preliminary" draft.
- The irreproducibility of the dataset (live web search at a specific point in time) makes independent replication structurally impossible.

## Falsification plan

- **Out-of-sample extension:** Extend the sample beyond January 2026; test whether alpha persists as the LLM model version updates and market participants adapt.
- **Model version sensitivity:** Replicate with different LLM versions (GPT-4, Claude, Gemini, open-source models) to test whether the result is model-specific.
- **Prompt sensitivity:** Vary the prompt template to test whether the alpha is robust to prompt engineering choices.
- **Portfolio size sensitivity:** Test Top-5, Top-10, Top-30, Top-50, Top-100 to map the alpha concentration curve.
- **Universe expansion:** Test on Russell 3000 or global equities to assess generalizability.
- **Cost stress test:** Model realistic slippage beyond spread (market impact, partial fills at opening auction).
- **Regime breakdown:** Test performance during market drawdowns (e.g., tariff escalation events) to assess whether the asymmetric "winner-picking" degrades in bear regimes.
- **Alternative base rates:** Compare against analyst consensus, news sentiment scores, and traditional factor models to isolate the marginal information content of agentic web search.
- **Failure metric:** If FF6 alpha drops below 0.10% per day (t < 1.5) in an out-of-sample window of equivalent length, the hypothesis is materially weakened.

## Crypto portability

**Unproven.**

The core mechanism — LLM autonomous information synthesis from web sources — could theoretically apply to crypto markets, where information is fragmented across Twitter/X, Discord, Telegram, on-chain data dashboards, and news sites. However, several portability risks apply:

1. **Asymmetric information structure:** The paper's key finding (AI excels at identifying winners, not losers) is attributed to corporate obfuscation of negative news. In crypto, negative sentiment often amplifies rather than dampens (e.g., FTX collapse, Terra/LUNA), so the asymmetry may reverse or disappear.
2. **Universe definition:** Crypto lacks a standardized "Russell 1000"-equivalent universe; top coins by market cap are far fewer and more volatile.
3. **Liquidity:** Crypto markets (especially mid/small-cap tokens) have wider spreads and thinner order books than Russell 1000 equities.
4. **24/7 markets:** The overnight → opening auction timing convention does not directly translate to 24/7 crypto markets.
5. **On-chain data:** Crypto-specific on-chain data (wallet flows, smart contract interactions, DEX volume) represents a distinct information channel not present in equities.
6. **Model dependency:** LLM training data may have different coverage and recency for crypto vs. equities information.
7. **Market structure:** Crypto markets are more fragmented across venues, with different market microstructure (e.g., perpetual futures, funding rates, MEV).

The hypothesis is that LLM agents could potentially generate alpha in crypto by synthesizing fragmented social/news/on-chain information, but the specific asymmetric winner-picking mechanism may not directly transfer.

## Limitations

- **Short sample period:** ~9 months (~158 trading days) — insufficient for robust regime-change testing.
- **Irreproducible dataset:** The live web search at a specific point in time cannot be recreated; future researchers cannot query today's AI about today's stocks.
- **Model version unspecified:** The paper does not name the specific LLM model; results may be version-dependent.
- **Preliminary draft:** The authors note this is a preliminary version.
- **Asymmetric signal:** Only long-only implementation is viable; no short leg.
- **Alpha concentration:** Predictive power is limited to Top-10 to Top-20 stocks; rapid dilution beyond this tier.
- **Equities-only evidence:** No crypto or other asset class evidence presented.
- **Data gap:** Exact prompt template details are in Appendix A (not fully reviewed in this record).
- **Data gap:** Detailed transaction cost model (beyond spread) is not specified.
- **Potential publication bias:** Single study with extraordinary claims (daily alpha of 18-33 bps in 2025-2026); independent replication needed.

## Implementation status

Not implemented. No implementation in our research stack (PyBroker, Nautilus) has been completed.

## Adoption boundary

This record is research material only. Its presence in this repository does **not** mean:
- Profitable
- Validated alpha
- Approved for implementation
- Approved for paper trading
- Approved for testnet
- Approved for live trading

## Related Wiki records

- [[quant/multimarket-senseai-multi-agent-llm-regime-adaptive-equity-selection-2026-09-04]] (related: LLM-based stock selection, but uses multi-agent architecture with curated data feeds rather than autonomous web search)

## Sources

- arXiv:2601.11958v1 — Chen, Z. and Pu, D. (2026). "Autonomous Market Intelligence: Agentic AI Nowcasting Predicts Stock Returns." Peking University.
- GitHub: https://github.com/mapledust0/AI-Stock-Nowcasting/
- Source as-of date: 17 January 2026 (paper submission date)
