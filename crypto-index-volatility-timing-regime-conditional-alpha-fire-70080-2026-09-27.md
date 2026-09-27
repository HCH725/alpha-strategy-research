---
schema: strategy-research-record-v1
title: "Crypto Index Volatility Timing with Regime-Conditional Alpha (S&P BDMI/BDMLCI/BDMXLCI, FFR and Sentiment Partitions)"
created: 2026-09-27
updated: 2026-09-27
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - volatility-timing
  - regime-conditional
  - index-level
  - journal-article
  - wiley
status: research-only
confidence: medium
source_as_of: 2026-09-16
sources:
  - "Arben Kita and Yue Zhang, 'Volatility != Risk: When Timing Alpha in Crypto Markets Reflects Mispricing', Financial Review (Wiley), First published 16 September 2026, DOI: 10.1111/fire.70080, open access CC BY 4.0, https://onlinelibrary.wiley.com/doi/10.1111/fire.70080"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Section 5 Conclusions claims volatility timing yields 'economically significant and state-dependent alphas-up to 18% annually for small-cap tokens', but no published article-HTML table cell supports an 18% small-cap annualized alpha: the largest BDMXLCI (ex-large-cap / small-cap proxy) monthly spanning alpha located anywhere in Tables 5, 7, 9 and 10 is 1.0636% (Table 5, Panel C, second Max quartile) and the text-reported COVID/low-FFR BDMXLCI alpha is 0.72% per month (Section 4.5). Unreconciled: the figure may live in the unread Online Appendix or in a non-table derivation, but as printed in the article HTML it is not traceable."
  - "Section 4.4 states 'CFGI regressions show no significant alphas, while SGI does', yet in Table 9 Panel A the SGI Growth-column alpha is insignificant for exactly the two indices the paper headlines (BDMXLCI 0.4960, PSI 0.2104, neither marked significant) while the only significantly negative SGI alpha in the panel is PSI Shrinking -0.7949. The blanket 'SGI does' prose and the 'strongest for small-cap coins' abstract claim are therefore not jointly supported by Table 9. Unreconciled."
---

# Crypto Index Volatility Timing with Regime-Conditional Alpha (S&P BDMI/BDMLCI/BDMXLCI, FFR and Sentiment Partitions)

## Provenance

- **Primary source:** Arben Kita and Yue Zhang, "Volatility != Risk: When Timing Alpha in Crypto Markets Reflects Mispricing."
  - **Title transcription note:** the source title uses the mathematical "not equal to" glyph (`U+2260`) between the words "Volatility" and "Risk". This record writes it as `!=` so that the file stays pure ASCII; the DOI, the URL and the exact rendering are preserved here for traceability.
  - **Complete author list (exactly as source):** two authors - **Arben Kita**, Crossref affiliation "University of Liverpool, Liverpool, UK", and **Yue Zhang**, Crossref affiliation "University of Southampton, Southampton, UK". No other author appears on the article page or in the Crossref record.
  - **Status / dates:** Crossref `type = journal-article`, container **Financial Review**, publisher **Wiley**, ISSN **0732-8516** (print) and **1540-6288** (online), article number `fire.70080`, no volume/issue/page assigned yet (Early View). Crossref assertions: **received 2025-11-13**, **accepted 2026-08-17**, **published 2026-09-16**. The Wiley page labels the item "**ORIGINAL ARTICLE**" and "**Open Access**", shows "**First published: 16 September 2026**", and carries a Creative Commons licence link; Crossref records the version-of-record licence as **CC BY 4.0** starting 2026-09-16. `reference-count = 33`, `is-referenced-by-count = 0` at read time. A received/accepted/published trail is present, but no explicit sentence "this article was peer reviewed" was captured from the page text, so peer-review wording is `not stated in source` beyond the editorial dates.
  - **Stable URL / DOI:** `https://doi.org/10.1111/fire.70080`, `https://onlinelibrary.wiley.com/doi/10.1111/fire.70080`.
  - **Public-use rights:** open access CC BY 4.0 for the version of record (Crossref licence field). This record still only normalises claims, rules and printed values; no source prose is reproduced wholesale.
- **How the full text was read:** a direct `curl` to `onlinelibrary.wiley.com` returned HTTP 403 (Cloudflare); the article was therefore read in a **browser session on 2026-09-27** after the Cloudflare interstitial cleared. Read in that session: Abstract, Sections **1, 2, 2.1, 2.2, 2.3, 3, 3.1, 3.2, 3.3, 4, 4.1, 4.2, 4.3, 4.4, 4.5, 4.5.1, 4.6, 4.6.1, 4.6.2, 5**, all **18 Endnotes**, **Tables 1-10** (all cells transcribed where cited below), the captions of **Figures 1, 2, 3**, and the collapsed-section headers for **Supporting Information**. **Not read:** the pixel content of Figures 1-3 (captions only), the **Online Appendix Table OA.1** (GARCH robustness, referenced in Endnote 2 and 16), and the collapsed Supporting Information item.
- **Data / code provenance as stated by the source:** data vendors are named (S&P Global for the three crypto indices, Bloomberg for the penny-stock index, Federal Reserve Bank of New York for the FFR, `sg-global-sentiment.com` for the SG Sentiment Indicator, `alternative.me` for the Crypto Fear & Greed Index). **No Data Availability statement, no repository, no commit and no code path appears anywhere in the published article HTML read on 2026-09-27** (`data gap`).
- **Pre-write dedup (repo-wide, hidden-inclusive, deterministic):** `rg -uuu -i "fire\.70080|Arben Kita|When Timing Alpha in Crypto|Volatility .? Risk" .` over the whole repository (all files including `.mimo-worktrees/`, `.agents/`, `.hermes/`, `.git`) returned only two hits, both journal-name strings unrelated to this source (`Volatility & Risk` in `equity-cross-sectional-homological-neural-network-mfcf-ranking-2026-09-02.md`, `Volatility / Risk` in `options-physical-crash-frontier-socp-finite-quotes-2026-09-02.md`); `rg -uuu -i -c "10\.1111/fire\.70080" .` returned **zero**; `rg -uuu -i -l "BDMXLCI|BDMLCI|Broad Digital Market|S&P Cryptocurrency|spglobal.*digital-assets" .` returned **zero**; `rg -uuu -i -o "10.1111/fire"` produced no occurrence of this DOI. `git log --oneline -20` was used only as a convenience glance. `git pull origin main` before researching: `Already up to date`.
- **Four-axis distinction against the nearest existing records** (source identity differs in every pair; mechanism or universe differs too):
  - `crypto-cross-sectional-volatility-managed-momentum-2026-08-31` - cross-sectional **momentum** portfolio risk-managed by total volatility; this record is **single-name-free index-level time-series exposure scaling with no momentum leg and a macro/sentiment regime partition**.
  - `bitcoin-semivolatility-upside-downside-exposure-timing-2026-09-27` - BTC exposure timed by an **upside/downside semivolatility ratio**; this record scales by **total realized variance**, on **multi-asset S&P crypto indices**, conditioned on **FFR and sentiment regimes**.
  - `stablecoin-dry-powder-volatility-targeting-copula-2026-09-01` - stablecoin dry-powder routing via a copula; different instrument set, different signal.
  - `crypto-macro-sentiment-contrarian-fear-greed-ema-2026-09-03` and `crypto-fear-greed-weekly-ar1-innovation-risk-premium-2026-09-04` - the Fear & Greed index is used there **as the trading signal**; here sentiment is only a **partition variable** (SGI phases, CFGI buckets) while the exposure driver is realized volatility.
  - `crypto-volatility-risk-premium-variance-swap-estimator-fragility-decay-2026-09-12` - harvests the variance risk premium with an estimator; this record has no variance-selling instrument at all, only scaled long exposure.
- **Wiki Brain (read-only) pre-write search:** `kb_search "S&P cryptocurrency index realized volatility timing federal funds regime alpha Kita Zhang"` -> **0 pages**; `kb_search "volatility management timing realized volatility scaling strategy"` -> 8 pages and `kb_search "cryptocurrency volatility risk premium regime monetary policy liquidity"` -> 2 pages, of which only verified adjacent pages are linked in `## Related Wiki records`. **No Wiki Brain write was performed.**

## Economic mechanism

### Source-reported

- The paper re-purposes a classic equity **volatility timing (VT)** strategy as a *diagnostic*: "we remodel a classic dynamic strategy, volatility timing (VT), not as a prescriptive tool for investors, but as a diagnostic to uncover the specific market conditions under which prices become inefficient."
- Stated mechanism: in crypto, realized volatility (RV) can proxy **noise-trader-driven flow imbalance** rather than a compensated risk premium, because there is no fundamental anchor, retail lottery demand is high, and arbitrage is capital- and short-sale-constrained. Elevated RV then flags periods when prices are temporarily distorted.
- The two stated conditions under which RV becomes a forward-looking mispricing proxy are: (1) noise-trader activity is high, and (2) arbitrage constraints are **sufficiently relaxed** (explicitly "during periods of loose monetary policy") so sophisticated capital can correct the dislocation. The paper's own counter-condition: when arbitrage is fully constrained - "such as during periods of 'extreme greed' where funding liquidity evaporates" - high volatility reflects market chaos and the timing strategy fails.
- Implementation story printed in Figure 1's caption (regime flowchart, source-reported): when high RV coincides with elevated sentiment and loose monetary policy (**FFR below 0.5%**) the rule "scale[s] down exposure to avoid mispricing during noise-driven 'Turmoil'" but **bypasses scaling during "Extreme Greed"** (sentiment above the **75th percentile with low FFR**) where arbitrage fails; low RV with stable sentiment scales up ("Orderly Bull"); neutral conditions keep baseline exposure.
- Proxies named by the source: **Max** (maximum daily return over a rolling one-month window, Bali et al. 2011) for lottery preference; the **federal funds rate** for funding liquidity (assumed exogenous to crypto, following Dong et al. 2022); **SG Global Sentiment Index** (three phases: shrinking / intermediate / growth) and the **Crypto Fear & Greed Index** (five buckets) for speculative participation. The source states: "the regime partitions (FFR, SGI, CFGI, volume) are defined ex-ante using observable data available at t-1."
- The source explicitly frames the contribution as conceptual: "Our primary contribution is diagnostic rather than prescriptive."

### Research interpretation

- Falsifiable hypothesis: **inverse-realized-volatility scaling of a long-only crypto index exposure earns a positive alpha relative to unscaled exposure only in sub-samples where monetary policy is loose and speculative participation is elevated**, i.e. the alpha is a *state-dependent* effect, not a stable risk-premium or generic risk-management gain.
- Component roles (hybrid structure):
  - **Signal:** monthly realized variance of the index, computed from daily log excess returns on a rolling basis (source Equation 2), used to form a scaling coefficient (source Equation 3).
  - **Regime gate (source-reported partitions, not part of the exposure rule itself):** FFR median split, COVID window January 2020 - December 2021, SGI three phases, CFGI five buckets; plus the Figure 1 illustration thresholds FFR 0.5% and sentiment 75th percentile.
  - **Portfolio construction:** scaled monthly index return; the coefficient on the unscaled return *is* the position weight, calibrated so that the unconditional variance of the scaled series equals that of the unscaled series.
  - **Evaluation:** spanning regression of scaled on unscaled returns (source Equation 4) with HAC standard errors; alpha and appraisal ratio (alpha / regression residual scale) are reported **monthly**.
- Why the mechanism could work: if RV spikes are transient, flow-driven and correctable, cutting exposure during high-RV states and adding it during calm states converts an inefficiency into return. Why it could be nothing: the same pattern is exactly what a variance-managed long book produces when the asset's mean-variance tradeoff is time-varying, i.e. **risk management indistinguishable from alpha**. The paper itself concedes the diagnostic framing and does not claim a standalone trading rule.
- Research reading of the causal channel: the *regime* conditions (low FFR, high sentiment) are doing the identification work, not the volatility rule per se; a strategy implementation would therefore need an observable, ex-ante, stable definition of those regimes, which the source provides only through in-sample partitions.

## Signal

- **Formation timestamp:** daily index observations are aggregated into a **monthly realized variance computed on a rolling basis from daily data** (Equation 2); the source's Endnote 11 states that "monthly index returns are computed on a rolling basis using daily data to enhance measurement stability ... all returns employed for scaling are derived as monthly returns from daily observations on a rolling basis. This ensures ex-ante implementability of the risk scaling and avoids look-ahead bias." **Timezone, index closing convention and the exact availability lag are `not stated in source`.**
- **Lookback:** the RV window is described as the current month's **"daily logarithm excess return of the index i"** (the source's own variable definition in Section 3.1) aggregated to a monthly realized variance; **the exact day count / calendar convention behind "monthly" (21 trading days vs calendar month vs trailing 30 days) is `not stated in source`** -> `underspecified`. Max uses a **rolling one-month** window (Bali et al. 2011 style, source-described).
- **Long entry / exposure:** always long. The scaling coefficient of Equation 3 multiplies the unscaled index return; "the coefficient of unscaled return represents the required leverage to invest in index i on the day d" (Section 3.2). There is **no threshold trigger, no entry signal and no exit signal** in the printed rule - exposure is continuously re-scaled.
- **Short entry:** none. No short leg is defined anywhere in the source; the scaled coefficient is positive by construction (variance matching), so the rule never goes net short (`not stated in source` whether negative weights are even permitted).
- **Exit:** none other than the next monthly re-scaling; no stop, no take-profit, no drawdown rule.
- **Holding period / rebalance cadence:** monthly re-scaling, measured from rolling daily data; positions persist between re-scales.
- **Regime partitions (source-reported, diagnostic rather than executable):** FFR split into **two equal subsamples** (median split of the FFR series); COVID window **January 2020 - December 2021**; SGI **three phases**; CFGI **five buckets**; Figure 1 illustration thresholds **FFR 0.5%** and **sentiment 75th percentile**.
- **Parameters:** variance-matching calibration constant set so that Var(scaled) = Var(unscaled) (value not printed); RV quartile sorts for diagnostics; spanning regression with **HAC / Newey-West standard errors (12 lags, per the Figure 3 caption)**; significance markers at **1%, 5%, 10%** (Table notes), unadjusted for multiplicity.
- **Reconstructability:** the *direction* of the rule (inverse RV, long only, monthly) is reconstructable; the *exact* numeric transformation, the exact RV window and the variance-matching constant are **not printed as numbers** -> the signal is **partially `underspecified`**, not fully reproducible from the article text alone.
- Anything a implementer would still have to choose (weight caps, financing, execution price, index replication method) is **`research-proposed`**, never source-reported.

## Required data

- **Instruments / universe:** three **S&P Global** daily crypto indices - **S&P Cryptocurrency Broad Digital Market Index (BDMI)**, **S&P Cryptocurrency LargeCap Index (BDMLCI)**, **S&P Cryptocurrency BDM Ex-LargeCap Index (BDMXLCI)**. BDMI is built from digital assets traded on **Lukka Prime-covered exchanges**, excluding stablecoins or other pegged assets (Endnote 6, S&P methodology accessed January 2024). BDMLCI constituents need **market capitalization of at least USD 1 billion** and a **three-month median daily trading value of over USD 1 million** (Endnote 7; the source renders this as "of over USD 1million"); BDMXLCI is the complement of BDMLCI inside BDMI.
- **Comparison universe:** **Penny Stock Index (PSI)** from **Bloomberg**, same sample period and daily frequency, used only as a speculative-asset benchmark.
- **Market type:** spot-index daily levels (crypto), not perpetuals, not futures. No venue other than the index construction is named.
- **Fields:** daily index prices/levels (to build log excess returns), realized variance, Max (rolling monthly maximum daily return), **federal funds rate** (Federal Reserve Bank of New York), **SG Global Sentiment Index**, **Crypto Fear & Greed Index (alternative.me)**, **trading volume / market cap** proxies used in Section 4.5.1.
- **Timeframe:** daily observations aggregated monthly; sample **March 2017 - December 2023** (abstract says "2017-2023", Section 3.1 says the sample spans March 2017 to December 2023 - consistent at year granularity).
- **Point-in-time:** the source states the regime partitions use data available at `t-1` and that the scaling is constructed to avoid look-ahead (Endnote 11). Index **constituent changes, reconstitution dates and point-in-time membership are `not stated in source`** -> `data gap`; the source itself warns in Endnote 8 that RV at index level "aggregates heterogeneous liquidity conditions, investor bases, volatility processes, and cross-sectional rebalancing effects."
- **Missing-data / timezone / candle boundary:** `not stated in source`.
- **The risk-free rate used to turn index levels into "excess" returns:** `not stated in source` -> `data gap` (the excess-return definition is asserted in Section 3.1 but the rate series is not identified in the article text read).
- **Funding / fee / spread needs:** none observed or modeled - see Execution assumptions.

## Execution assumptions

- **Transaction costs: explicitly not modeled.** Section 4.3 states verbatim that "We do not adjust for transaction costs or implementation frictions, because the VT exercise is not proposed as a tradable rule." Every reported figure in this record is therefore **gross of any friction**; costs are `data gap`, **never zero**.
- **Turnover:** `not stated in source` (`data gap`) - no turnover figure, no trade count, no rebalance-size distribution appears in Tables 1-10 or in the text read.
- **Signal-to-order timing / execution price:** `not stated in source` - no next-open, next-close, VWAP or auction convention is given for the monthly re-scale.
- **Order type / fill model / partial fills / latency:** `not stated in source`.
- **Spread / slippage / market impact / capacity:** `not stated in source`. The Roll (1984) illiquidity measure appears only as a **regression control** (Table 10), not as a cost model; Endnote 17 concedes Roll is "an imperfect proxy in cryptocurrency markets."
- **Leverage / margin / financing:** the scaling coefficient "represents the required leverage" and can exceed 1, but **no leverage cap, no margin requirement, no financing cost on the borrowed portion and no liquidation rule are stated** (`data gap`). The source's own narrative is built on leveraged scaling in a market where it also documents exchange outages and widened spreads.
- **Borrow / shorting:** no short leg; not applicable.
- **Funding (perpetuals):** not applicable inside the source - indices are spot composites; if implemented on perpetuals, funding and mark-price dynamics would be an **added** cost that the reported numbers never see.
- **Investability:** the three S&P indices are **licensed index products, not directly tradable instruments**; replication basket, license fee and tracking cost are `not stated in source`.

## Evidence

### Source-reported

All figures below are third-party claims from the pinned source, read in the browser on 2026-09-27, and **none has been independently reproduced**. Column identities were fixed by cross-checking full-sample columns across tables (see provenance note after this list).

- **Table 2 (RV sorts, time-series average *daily* excess returns; BDMI / BDMLCI / BDMXLCI / PSI):**
  - Panel A, March 2017 - December 2023: Low-RV quartile `0.0046 / 0.0049 / 0.0022 / -0.0004`; High-RV quartile `0.0004 / 0.0004 / -0.0005 / -0.0001`; **H-L `-0.0041 / -0.0045 / -0.0027 / 0.0003`**.
  - Panel B (excluding January 2020 - December 2021): H-L `-0.0015 / -0.0036 / -0.0009 / 0.0001`.
  - Panel C (January 2020 - December 2021): Low-RV `0.0089 / 0.0086 / 0.0083 / -0.0007`; High-RV `0.0010 / 0.0022 / -0.0017 / 0.0004`; **H-L `-0.0079 / -0.0064 / -0.0100 / 0.0011`**.
  - Source reading: "returns are highest in the lowest RV quartile ... the small-cap index (BDMXLCI) has limited overlap with Bitcoin and Ethereum."
- **Table 3 (direct comparison, average *daily* excess return / daily Sharpe / daily Sortino, unscaled -> RV-managed):**
  - Panel A (full sample): excess `0.0019 -> 0.0022` (BDMI), `0.0017 -> 0.0018` (BDMLCI), **`0.0018 -> 0.0013` (BDMXLCI)**, `-0.0003 -> -0.0007` (PSI); Sharpe `0.0408 -> 0.0473`, `0.0367 -> 0.0400`, **`0.0327 -> 0.0232`**, `-0.0127 -> -0.0253`; Sortino `0.0514 -> 0.0510`, `0.0470 -> 0.0432`, `0.0406 -> 0.0250`, `-0.0147 -> -0.0280`.
  - Panel B (excluding COVID): excess `0.0009 -> 0.0012`, `0.0006 -> 0.0007`, `0.0005 -> -0.0006`, `-0.0007 -> -0.0012`; Sharpe `0.0197 -> 0.0239`, `0.0141 -> 0.0140`, `0.0092 -> -0.0109`, `-0.0275 -> -0.0429`.
  - Panel C (COVID): excess `0.0042 -> 0.0046`, `0.0041 -> 0.0046`, `0.0048 -> 0.0057`, `0.0004 -> 0.0006`; Sharpe `0.0916 -> 0.1209`, `0.0910 -> 0.1180`, `0.0872 -> 0.1250`, `0.0148 -> 0.0307`; Sortino `0.1134 -> 0.1821`, `0.1138 -> 0.1840`, `0.1047 -> 0.1769`, `0.0196 -> 0.0371`.
  - Table note: "key performance ratios are highlighted in bold with superscripts denoting economic significance at the 1%, 5%, and 10% levels."
- **Table 7 (spanning regressions partitioned by FFR; alphas are MONTHLY, HAC standard errors in parentheses; Low = lower FFR half):**
  - Panel A (March 2017 - December 2023): BDMI `0.4467 (0.1944)` marked significant (Low) / `0.0577 (0.3533)` (High) / `0.2251 (0.2018)` (Full); BDMLCI `0.3259 (0.1846)` significant (Low) / `0.0606 (0.3566)` / `0.1717 (0.2009)`; BDMXLCI `0.3286 (0.2292)` / `-0.0911 (0.4004)` / `0.0101 (0.2374)`; PSI `-0.1092 (0.1650)` / `-0.1090 (0.1996)` / `-0.1262 (0.1373)`.
  - Panel B (excluding COVID): BDMI `0.2496 (0.3054)` / `0.1001 (0.3156)` / `0.1337 (0.2640)`; BDMLCI `0.1374 (0.2930)` / `0.1058 (0.3186)` / `0.0575 (0.2604)`; BDMXLCI `-0.3038 (0.4002)` / `-0.0009 (0.3609)` / `-0.2463 (0.3077)`; PSI **`-0.3289 (0.1605)` marked significant** / `-0.0961 (0.1775)` / `-0.2110 (0.1764)`.
  - Panel C (January 2020 - December 2021): BDMI `0.5089 (0.2743)` significant / `0.2487 (0.5810)` / `0.4786 (0.2664)` significant; BDMLCI `0.5068 (0.2873)` significant / `0.2234 (0.5536)` / `0.4760 (0.2786)` significant; **BDMXLCI `0.7201 (0.3355)` significant** / `0.1100 (1.0086)` / `0.6733 (0.3269)` significant; PSI `0.1813 (0.1981)` / `-0.0513 (0.1695)` / `0.1184 (0.1927)`.
  - Section 4.5 states the same headline as: "Our strategy delivered **0.72% monthly alpha (t = 2.14)** for BDMXLCI during COVID but not in regular times."
  - Source reading: "Over the full sample period, the RV-scaling strategy is effective only for BDMI and BDMLCI during periods of relatively high market funding liquidity ... when the highly volatile COVID period is excluded, the strategy fails to generate statistically significant alphas across all indices."
- **Table 9 (spanning regressions partitioned by sentiment; alphas MONTHLY, HAC SE):**
  - Panel A (SG Global Sentiment): BDMI Shrinking `-0.5003 (0.6102)`, Intermediate `-0.0150 (0.2058)`, **Growth `1.0159 (0.3763)` significant**, Full `0.2251 (0.2018)`; BDMLCI `-0.5311 (0.6142)`, `-0.0006 (0.2099)`, **Growth `0.8672 (0.3621)` significant**, Full `0.1717 (0.2009)`; BDMXLCI `-0.5644 (0.6491)`, `-0.3053 (0.2778)`, `0.4960 (0.4632)`, Full `0.0101 (0.2374)`; PSI **`-0.7949 (0.1347)` significant (negative)**, `-0.2195 (0.2635)`, `0.2104 (0.1975)`, Full `-0.1262 (0.1373)`.
  - Panel B (Crypto Fear & Greed): BDMI `0.3433 (0.3095)`, `0.1776 (0.3195)`, `-1.0504 (0.8966)`, `0.5888 (0.4396)`, `0.0265 (0.4032)`, Full `0.2251 (0.2018)`; BDMLCI `0.3341 (0.3074)`, `0.1955 (0.3171)`, `-1.0495 (0.9097)`, `0.5927 (0.4683)`, `0.0087 (0.4071)`, Full `0.1717 (0.2009)`; BDMXLCI `0.2558 (0.4086)`, `-0.1502 (0.4105)`, `-1.2272 (0.9440)`, `0.5865 (0.3719)`, `0.3283 (0.9948)`, Full `0.0101 (0.2374)`; PSI **`-0.3790 (0.1212)` significant**, `-0.2710 (0.2879)`, **`-0.5521 (0.2576)` significant**, `0.5833 (0.4225)`, `0.2320 (0.2227)`, Full `-0.1262 (0.1373)`.
  - Source reading: "the lack of alpha from RV timing during extreme greed sentiment phases (Table 9 B) suggests that when noise traders dominate, and frictions remain high, the strategy loses efficacy" and "CFGI regressions show no significant alphas, while SGI does."
- **Table 5 (spanning regressions partitioned by rolling one-month Max quartiles):** Panel C (January 2020 - December 2021) BDMXLCI columns print `0.5398 / 1.0636 (marked significant) / 0.8984 / 0.5962 / 0.6733 (full sample)`; PSI columns print `0.0248 / 0.5197 / 0.1415 (significant) / 0.6469 (significant) / 0.1184`. The panel's full-sample column equals `0.4786 / 0.4760 / 0.6733 / 0.1184` for BDMI / BDMLCI / BDMXLCI / PSI, which is **identical to Table 7 Panel C's full-sample column** - this cross-check is how column identity for Tables 5, 7, 9 and 10 was fixed for this record. Section 4.2 reading: significant alphas appear "without a clear pattern across Max-based subsamples."
- **Table 10 (spanning regressions with Roll (1984) liquidity control; alphas MONTHLY):** Panel A (full sample) `0.4996 (0.4523)` / `0.5963 (0.4621)` / `-0.0689 (0.5598)` / `0.3571 (0.3764)` for BDMI / BDMLCI / BDMXLCI / PSI - **none significant**. Panel C (COVID) **`1.3241 (0.6497)` significant (BDMI)**, **`1.3781 (0.6823)` significant (BDMLCI)**, `0.9322 (0.8460)` (BDMXLCI), `-0.1741 (0.4892)` (PSI). Section 4.5.1 reading: alphas rise "from 0.51% to 1.32% (BDMI) and from 0.51% to 1.38% (BDMLCI), with statistical significance improving from 10% to 5%", while "the BDMXLCI alpha becomes insignificant, likely due to high collinearity between RV and Roll for small-cap cryptocurrencies during COVID."
- **Expanding-window / real-time check (Section 4.5 and Figure 3 caption):** initialization March 2017 - March 2018 (12 months), then the spanning regression is re-estimated **monthly** on an expanding sample for **BDMXLCI**, with **Newey-West HAC standard errors (12 lags)**; alpha becomes statistically distinguishable from zero **in March 2020** when COVID enters the sample and FFR drops below 0.5%; pre-COVID results show economically small and insignificant alphas (**mean = 0.13%, t = 0.54**); alpha **peaks at 0.65% in December 2021**; **Chow test across pre-COVID / COVID / post-COVID: F = 6.42, p = 0.002**; alpha reverts to insignificance after **June 2022** when FFR exceeds **2.5%**. (Units of the 0.13% / 0.65% figures are printed as alpha percentages against a caption describing "annualized monthly alpha estimates" -> **unit `underspecified`**.)
- **Placebo (Endnote 15):** randomly shuffled returns preserving annual structure, **1,000 block-bootstrap replications** under the null preserving autocorrelation, **mean t-statistic 0.19**, **zero windows significant at 5%**; effects for BDMI/BDMLCI "qualitatively similar but attenuated."
- **Volatility-estimator robustness (Section 4.5, Endnote 2 and 16):** replacing RV with **GARCH(1,1)** volatility in the scaling makes **all spanning-regression alphas insignificant** (results printed in **Online Appendix Table OA.1**, which was **not read** for this record).
- **Abstract / conclusion headline claims:** "Volatility timing in cryptocurrency markets generates significant alpha, but only during periods of loose monetary policy and high uncertainty"; Section 5: "VT strategies yield economically significant and state-dependent alphas-**up to 18% annually for small-cap tokens**-only during periods of loose monetary policy, high sentiment, or elevated uncertainty."
- **Column-identity verification used above:** Table 7 Panel A full-sample alphas `0.2251 / 0.1717 / 0.0101 / -0.1262` reappear as the Full-sample column of Table 9 Panels A and B for the same four indices, and Table 5 / Table 7 Panel C full-sample alphas `0.4786 / 0.4760 / 0.6733 / 0.1184` coincide exactly. Every number above was transcribed from the read page, not recomputed.

### Independently reproduced

**`not independently reproduced`.** No backtest, no simulation, no data download and no code execution was performed for this record. The only actions taken were: reading the primary source in a browser, reading Crossref metadata, running read-only repository dedup searches, and running read-only Wiki Brain searches.

### Negative evidence

1. **Full-sample alphas are all insignificant.** Table 7 Panel A full-sample column: `0.2251 / 0.1717 / 0.0101 / -0.1262`, none marked significant; Table 10 Panel A (Roll control): `0.4996 / 0.5963 / -0.0689 / 0.3571`, none significant. The baseline claim is a conditional claim, not a full-sample one.
2. **Outside the COVID window nothing works.** Table 7 Panel B (excluding January 2020 - December 2021): every crypto alpha is insignificant and **PSI's low-FFR alpha is significantly negative (-0.3289)**; the source says so itself: "the strategy fails to generate statistically significant alphas across all indices."
3. **The rule hurts the small-cap index over the full sample.** Table 3 Panel A: BDMXLCI daily excess `0.0018 -> 0.0013`, daily Sharpe `0.0327 -> 0.0232`, Sortino `0.0406 -> 0.0250`.
4. **Sortino degrades even where Sharpe improves.** Table 3 Panel A: BDMI `0.0514 -> 0.0510`, BDMLCI `0.0470 -> 0.0432`; Panel B (ex-COVID) BDMLCI `0.0182 -> 0.0144`.
5. **The penny-stock control shows the effect is not generic speculation beta.** PSI has no significantly positive alpha in any spanning cell; its significant alphas are negative (Table 9 Panel A Shrinking `-0.7949`, Table 9 Panel B Extreme fear `-0.3790`, Neutral `-0.5521`, Table 7 Panel B Low FFR `-0.3289`).
6. **Explicitly not tradable and explicitly costless.** Section 4.3: "We do not adjust for transaction costs or implementation frictions, because the VT exercise is not proposed as a tradable rule." Every number is gross; costs are `data gap`, never zero.
7. **Turnover is never reported** (`data gap`), so the cost drag of a monthly leverage-varying long book is unquantified.
8. **Leverage is unpriced.** The coefficient "represents the required leverage" but no cap, financing rate, margin rule or liquidation rule is printed (`data gap`).
9. **The result depends on the volatility estimator.** GARCH(1,1) scaling makes **all** alphas insignificant (Section 4.5) - the effect lives specifically in realized variance's jump/order-flow component, and the supporting table (Online Appendix OA.1) was not read, so its magnitudes are `underspecified`.
10. **The crypto-specific sentiment proxy produces nothing.** Table 9 Panel B: no CFGI cell is significant for any of the three crypto indices, which the source explains away as CFGI being "more reactive and prone to noise."
11. **The global sentiment proxy does not support the small-cap headline.** Table 9 Panel A Growth column: BDMXLCI `0.4960` insignificant and PSI `0.2104` insignificant, while only BDMI `1.0159` and BDMLCI `0.8672` are significant - recorded as a frontmatter contradiction against the blanket prose and the abstract's "strongest for small-cap coins."
12. **The small-cap alpha disappears once liquidity is controlled.** Table 10 Panel C: BDMXLCI `0.9322` with SE `0.8460`, insignificant, while BDMI and BDMLCI *strengthen* - the source attributes this to collinearity between RV and Roll in small caps, which is itself an admission that small-cap RV is largely an illiquidity proxy.
13. **Short sample with one decisive episode.** Just over six years (March 2017 - December 2023, 82 months), of which the effect is carried by a **24-month** COVID window; the source concedes "one caveat of our results remains the relatively short sample length" and that regime sub-windows shrink to "two- to three-year windows, reducing statistical power."
14. **Chow test means one episode drives everything.** `F = 6.42, p = 0.002` across pre-COVID / COVID / post-COVID is evidence *against* a stationary alpha, i.e. the strategy's profitability is a single-episode result as printed.
15. **No alpha after June 2022.** Expanding-window alpha reverts to insignificance once FFR exceeds 2.5%; the final 18 months of the sample contribute no effect, and nothing after December 2023 exists at all.
16. **No multiplicity control anywhere.** Dozens of alpha cells are printed (3 partition schemes x 4 indices x 3-6 buckets x 3 panels, plus 4-quartile Max and RV sorts) with unadjusted 10/5/1% markers and no Benjamini-Hochberg, Bonferroni or Newey-West-adjusted family (`data gap`).
17. **Placebo design is narrow.** Endnote 15 shuffles returns; it does not test the *selection* of the COVID window, the FFR split or the sentiment thresholds - the degrees of freedom that actually generate the conditional claim.
18. **The regime gates are in-sample descriptive.** The COVID window is chosen with hindsight; the FFR median split and SGI/CFGI buckets are defined on the full sample; only the `t-1` availability of the underlying series is asserted (Section 3.1).
19. **The headline "up to 18% annually for small-cap tokens" is not traceable to a published table cell** (see frontmatter `contradictions`): largest BDMXLCI monthly alpha located = `1.0636` (Table 5 Panel C) and the text-reported COVID/low-FFR value = `0.72` (Section 4.5).
20. **Index-level, not asset-level.** Endnote 8: RV "aggregates heterogeneous liquidity conditions, investor bases, volatility processes, and cross-sectional rebalancing effects" and "should not be interpreted as implying that the same flow-driven dynamics operate uniformly or on an asset-by-asset basis."
21. **Composition effects are acknowledged but not removed.** Section 4.1 concedes the results are "portfolio-level evidence given the index's heterogeneous and time-varying composition"; the source argues rebalancing would "attenuate, rather than generate," the pattern but does not show a constituent-level test.
22. **Indices are not tradable instruments** and no replication basket, license fee, tracking error or investable proxy is discussed (`data gap`); a proxy implementation would have to absorb spreads and impact the paper never models.
23. **No data/code availability statement, no repository, no commit** in the published HTML; only a collapsed "Supporting Information" item and an unread Online Appendix (reproducibility `data gap`).
24. **Scout-labelled: no independent third-party replication identified.** Crossref `is-referenced-by-count = 0` at read time; absence of a replication is not evidence that replication would fail or succeed. Additionally the sample ends **December 2023**, so there is no evidence for the 2024-2026 regime (ETF-era crypto, subsequent tightening/easing cycles); forward performance is `unproven`.

## Falsification plan

All thresholds below are **`research-defined falsification thresholds`** and all operational choices not printed by the source are **`research-proposed`**. Base data = daily levels of BDMI / BDMLCI / BDMXLCI (S&P Global) plus an independent aggregate crypto index from a second vendor; partitions follow the source (FFR median split, sentiment buckets) and are recomputed strictly at `t-1`.

- **F1 - Frozen forward replication.** Pre-register the rule (inverse monthly RV, long only, variance-matched weights, monthly re-scale) and run it from **2026-10-01** for **>= 24 months**. **Fail** if the RV-managed book's annualized Sharpe <= the unscaled index Sharpe over that window (`research-defined`).
- **F2 - Reproduction gate.** Rebuild Tables 3, 7 and 10 from public index levels. **Fail** if any Full-sample alpha, or any Panel C alpha quoted above, cannot be reproduced within **+/- 0.05 percentage points per month**, or if Table 3's daily excess returns cannot be reproduced within **+/- 0.0002** (`research-defined`). Unreproducible numbers invalidate the record's evidence base.
- **F3 - All-in cost ladder.** Apply **0 / 5 / 10 / 20 / 50 bps per side** to measured turnover. **Fail** if the low-FFR/COVID alpha advantage is erased at or below **20 bps per side** (`research-defined`) - because turnover is `data gap`, this is the single most likely kill switch.
- **F4 - Turnover and capacity audit.** Report annual one-way turnover of the scaled book and the implied trade sizes at each re-scale. **Fail** if annual turnover exceeds **200%** with no documented sub-5-bps execution path, or if a 10% participation cap makes the re-scale infeasible (`research-defined`).
- **F5 - Decisive mechanism ablation (four-way).** Run (a) **month-shuffled RV series**, (b) **sign-inverted scaling** (scale *up* in high RV), (c) **GARCH(1,1) scaling** as the source does, (d) constant exposure. **Fail the mechanism** if (a) or (b) lands within **0.05 monthly alpha** of the published rule, or if the direction of the scaling carries no information (`research-defined`).
- **F6 - Regime-conditionality test.** Pre-register the low-FFR gate as the expanding median of FFR through `t-1`, and test `alpha_lowFFR - alpha_highFFR` over **>= 60 months** with Newey-West lags 12. **Fail** if the 95% CI includes **0** (`research-defined`) - this is the paper's actual claim, not the volatility rule itself.
- **F7 - Leave-one-episode-out.** Recompute alphas with the COVID window removed (the source already does this and finds nothing) and then require **>= 2 independent** low-FFR/uncertainty episodes with positive alpha out of sample. **Fail** if alpha exists in only **one** episode (`research-defined`) - as printed, it does.
- **F8 - Vendor / index replication.** Rebuild the same rule on an independent aggregate crypto basket (second index vendor or a point-in-time top-N basket). **Fail** if the sign flips or the alpha falls by more than **50%** (`research-defined`).
- **F9 - Point-in-time universe rebuild.** Reconstruct a BDMI-like basket with listing-date and delisting handling and explicit stablecoin exclusion. **Fail** if the conditional alpha disappears (`research-defined`) - composition drift is an acknowledged confound.
- **F10 - Multiplicity control.** Apply Benjamini-Hochberg at `q < 0.10` across the full grid of partition x index x bucket cells actually reported. **Fail** if no cell survives (`research-defined`).
- **F11 - Significance gate.** Monthly alpha differential vs unscaled with Newey-West/HAC lags = 12: **fail** if `|t| < 1.96`, and require a 95% stationary-block-bootstrap CI excluding 0 (`research-defined`).
- **F12 - Placebo null.** **1,000 circular shifts** of the exposure series *and* of the regime labels (the source only shuffled returns). **Fail** if the observed differential does not exceed the **95th percentile** of either null (`research-defined`).
- **F13 - Investable-proxy net test.** Implement on a tradable broad crypto basket (spot or perps) including spread, financing on any weight above 1.0x, and index-tracking differences. **Fail** if net alpha <= 0 at **20 bps** per side (`research-defined`).
- **F14 - Reproducibility gate.** A second independent implementation must match the Table 3 ratios and the Table 7 / Table 10 alpha cells quoted above within **+/- 10%** (`research-defined`).
- **Action on failure:** F1, F6, F11 failing => reject the conditional-alpha claim; F3, F4, F13 failing => reject implementability as stated (cost- and leverage-dependent); F5, F9 failing => reject the noise-trader/limited-arbitrage mechanism (composition or artefact); F8, F10, F14 failing => reject the evidence base; F7 failing => keep only as a single-episode historical observation, never as a tradeable regime rule.

## Crypto portability

**direct.**

The evidence base is itself cryptocurrency: three S&P crypto index series, crypto prices, a rule applied at crypto market frequency. No asset-class porting assumption is required. Residual gaps even inside this `direct` setting:

- **Index vs tradable instrument:** `data gap` - the source trades *indices* (licensed S&P products) rather than spot or perpetual books; a replication basket, license fee and tracking cost are never discussed.
- **Spot vs perpetual / funding / mark price / liquidation:** not applicable to the source's own design; `data gap` the moment the >1x scaling weights are implemented on perps or on margin, since financing on the borrowed portion is unpriced.
- **24/7 session structure:** `data gap` - no timezone, index-closing convention, candle boundary or month-boundary rule is stated for a market that never closes, yet the rule is monthly.
- **Venue fragmentation:** `data gap` - BDMI spans "Lukka Prime-covered exchanges" only; the source itself cites exchange outages and widened spreads during extreme greed, i.e. execution in exactly the states the rule reacts to is documented as degraded.
- **Stablecoin / pegged-asset exclusion:** stated for BDMI (Endnote 6), so the index is already filtered; a naive "all coins" port would differ.
- **Liquidity / impact:** `data gap` - Roll illiquidity is used only as a regression control, never as a cost model.
- **Custody / withdrawal / venue risk:** `not stated in source`.

`direct` describes the evidence domain only. It is **not** authorization to trade, and not a claim that the numbers survive costs.

## Limitations

- **`underspecified`** - the exact RV window ("monthly ... rolling" with no day count), the variance-matching constant, the risk-free series behind "excess" returns, and the units of the Figure 3 alpha percentages (0.13% / 0.65%).
- **`underspecified` / unreconciled** - the Section 5 "up to 18% annually for small-cap tokens" claim has no matching published table cell (frontmatter `contradictions`).
- **`data gap`** - every friction field: transaction costs, spread, slippage, market impact, participation, turnover, financing, margin, liquidation, order type, fill model, latency. **Nothing may be inferred as zero.**
- **`data gap`** - leverage cap, cash handling, position limits, shorting permission, rebalance execution price, missing-data treatment, timezone.
- **`data gap`** - no data/code availability statement, no repository, no commit; the Online Appendix (Table OA.1) and the collapsed Supporting Information were not read.
- **`data gap`** - no multiple-testing correction across the large reported cell grid; significance markers are unadjusted.
- **`not stated in source`** - peer-review wording beyond the Crossref received/accepted dates; a statement about index investability.
- **`not independently reproduced`** - no backtest, no code, no data was opened by this Scout.
- **`unproven`** - forward performance after December 2023, and any claim that the regime conditions identified in-sample recur in later cycles.
- **Single market design:** spot crypto indices only, one monthly frequency, one volatility estimator as the headline (RV), one macro partition (FFR) plus two sentiment series; the paper's own robustness shows the effect vanishes with GARCH volatility.
- **Source-quality:** journal article (Wiley, Financial Review) carrying received 2025-11-13 / accepted 2026-08-17 editorial dates, open access CC BY 4.0, 33 references, **0 citations at read time**; no explicit peer-review statement was captured from the page, so that wording is `not stated in source`. The empirical base is one 82-month sample with the result carried by a 24-month window.
- **Publication-bias / selection:** a positive-result conditional framing ("when it works") with the unconditional null printed in the same tables; the negative full-sample and ex-COVID results are reported but the abstract headline is conditional.

## Implementation status

`implementation_status: not-implemented`. **Nothing has been implemented in our research stack.** No signal code was written, no data was downloaded, no backtest was run, and no Qlib, Paper, Testnet or Live stage was touched by this record. The only actions taken were: reading the primary source in a browser, reading Crossref metadata, hashing nothing (the source is HTML, not a pinned PDF), and running read-only repository and Wiki Brain dedup searches.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. The presence of this record in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. No wording, evidence count or figure in this record promotes itself, and every Sharpe, alpha and ratio above is a third-party claim that has not been reproduced.

## Related Wiki records

Verified by `kb_search` in this run (read-only; no page was written):

- [[quant/csi300-regime-augmented-harq-xgboost-low-vol-gated-2026-09-05]] - adjacent family: regime-gated, volatility-scaled equity allocation.
- [[quant/market-regime-routed-specialist-gbt-asymmetric-hysteresis-2026-09-12]] - adjacent family: regime-conditional exposure routing with volatility targeting.
- [[quant/crypto-kalshi-prediction-market-macro-repricing-volatility-forecasting-2026-09-01]] - adjacent family: monetary-policy channels into crypto volatility.
- [[quant/around-the-clock-macro-jump-risk-premia-fama-macbeth-2026-09-04]] - adjacent family: macro-conditioned crypto risk premia.

A search for the exact mechanism (`S&P cryptocurrency index realized volatility timing federal funds regime alpha`) returned **0 pages**, so no identical or near-identical Wiki record exists.

## Sources

- Arben Kita and Yue Zhang, "Volatility != Risk: When Timing Alpha in Crypto Markets Reflects Mispricing," **Financial Review** (Wiley), First published **16 September 2026**, open access **CC BY 4.0**, Crossref type `journal-article`, ISSN 0732-8516 / 1540-6288, article number `fire.70080`, received 2025-11-13, accepted 2026-08-17, published 2026-09-16, 33 references, 0 citations at read time. DOI: `10.1111/fire.70080`. Landing/full text: https://onlinelibrary.wiley.com/doi/10.1111/fire.70080 (read in a browser session 2026-09-27 after a direct `curl` returned HTTP 403). Provenance for every number above: **Table 1** (regime schematic, pp. rendered in Section 2), **Table 2** and its note (RV sorts), **Table 3** and its note (direct comparison), **Table 4** note (Max sorts), **Table 5** and its note (Max spanning regressions), **Table 6** note (FFR sorts), **Table 7** and its note (FFR spanning regressions, alphas monthly with HAC SE), **Table 8** note (sentiment sorts), **Table 9** and its note (sentiment spanning regressions), **Table 10** and its note (Roll liquidity controls), **Figure 1** caption (VT regime flowchart with FFR 0.5% and sentiment 75th percentile), **Figure 2** caption (cumulative returns), **Figure 3** caption (expanding-window annualized alpha, Newey-West 12 lags), **Section 3.1-3.3** (data, return scaling, spanning regressions), **Section 4.1-4.6.2** (results, robustness, implementation), **Section 5** (conclusions incl. the 18% claim), **Endnotes 1-18** (incl. Endnote 6 index construction, Endnote 7 large-cap definition, Endnote 8 portfolio-level caveat, Endnote 11 ex-ante rolling construction, Endnote 15 placebo, Endnotes 16-17 GARCH and Roll caveats).
- Crossref REST record for `10.1111/fire.70080` (metadata, affiliations, editorial dates, licence, reference and citation counts) - read 2026-09-27.
- Works **cited by the source** for the rule families and proxies, **not read for this record** and carrying no imported numbers here: Moreira and Muir (2017), *Journal of Finance* 72, 1611-1644; Barroso and Santa-Clara (2015); Cederburg, O'Doherty, Wang and Yan (2020); Bali, Crain and Thrasher (2011); Glosten and Milgrom (1985); Amihud and Mendelson (1986/2013 framework as cited); Brunnermeier and Pedersen (2008); Barberis and Huang (2008); Makarov and Schoar (2020); Goyal and Welch (2008); Roll (1984); Dong et al. (2022); Leong and Kwok (2023, 2025); Zhao et al. (2024); Babiak and Bianchi (2025); Scaillet et al. (2020); Liu and Tsyvinski (2021); Liu et al. (2022); Cong et al. (2020); Baker et al. (2020); Kumar et al. (2022); Baltussen et al. (2021); Duarte et al. (2025).
