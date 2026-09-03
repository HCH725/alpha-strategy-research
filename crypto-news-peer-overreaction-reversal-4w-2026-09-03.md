---
schema: strategy-research-record-v1
title: Crypto News-Identified Smaller-Peer Overreaction Reversal
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - cross-sectional
  - event-driven
  - news
  - reversal
status: research-only
confidence: medium
source_as_of: 2025-07
sources:
  - "Gustavo Schwenkler and H. Zheng, 'News-driven peer co-movement in crypto markets', Journal of Corporate Finance 93 (2025), 102772, DOI: 10.1016/j.jcorpfin.2025.102772"
  - "Open-access article page: https://www.sciencedirect.com/science/article/pii/S0929119925000409"
  - "Author-hosted/academic working-paper version: https://cdar.berkeley.edu/sites/default/files/cryptopeers_latestversion.pdf"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The final journal article weights eligible short positions in proportion to each peer's positive event-week return, while an accessible earlier working-paper version describes equal weighting. The final journal version is treated as authoritative for signal normalization; older-version fee assumptions must not be silently imported without confirming they survived into the final specification."
---

# Crypto News-Identified Smaller-Peer Overreaction Reversal

## Provenance

Primary source: Gustavo Schwenkler and H. Zheng, *News-driven peer co-movement in crypto markets*, *Journal of Corporate Finance* 93 (July 2025), article 102772, DOI `10.1016/j.jcorpfin.2025.102772`. The publisher marks the article open access under a Creative Commons license.

The empirical sample covers weekly cryptocurrency data from 2017-10-01 through 2020-11-30. Market and return data are assembled from CoinGecko, CoinAPI and CryptoCompare. The peer-link layer is constructed from more than 200,000 online crypto-news articles collected from CryptoCompare. The final paper reports 207 cryptocurrencies in the news/market overlap, 3,403 identified peer-link observations, and 1,071 unique peer connections among 266 cryptocurrencies in the wider peer-network sample.

Repository-wide source-identity checks on 2026-09-03 found no existing pool record for DOI `10.1016/j.jcorpfin.2025.102772`, the exact paper title, authors Schwenkler/Zheng, or the distinctive mechanism of a negative idiosyncratic crypto shock causing a contemporaneous positive overreaction in news-identified smaller peers followed by multi-week reversal. Existing pool records involving generic news, sentiment, momentum, reversal, or cross-sectional relationships are not source-identical and do not normalize this event/peer-network construction.

An earlier open working-paper PDF is retained only as supplementary provenance. It differs from the final journal article in at least one material strategy detail: the working paper describes equal weighting of short positions, while the final journal article states that eligible shorts are weighted in proportion to their positive event-week returns. This record therefore uses the final journal version as the canonical source for the normalized rule.

## Economic mechanism

### Source-reported

The authors argue that financial news helps investors identify competitive peer relationships among cryptocurrencies. When a cryptocurrency suffers a large idiosyncratic negative shock, investors appear to rotate toward smaller peers that are linked to the shocked cryptocurrency in news reporting. Those peers experience unusually positive abnormal returns during the event week even though the originating shock is designed to be idiosyncratic rather than a common fundamental shock.

The paper interprets this contemporaneous opposite-sign peer move as an investor-overreaction / competition effect. The effect is strongest among smaller peers, which the authors associate with slower information processing and lower investor attention. The resulting peer mispricing then reverses over the following weeks. The authors report that the reversal takes more than three weeks to dissipate and build an event-driven strategy that shorts the positively performing smaller peers while holding an equal long notional in Bitcoin.

### Research interpretation

The falsifiable mechanism is a **news-conditioned peer overreaction followed by slow reversal**:

1. a large negative idiosyncratic shock hits crypto `j`;
2. news reporting supplies a competitive-peer mapping from `j` to peer `i`;
3. if `i` is smaller than `j`, investor reallocation/attention causes `i` to rise abnormally during the event week;
4. because the shock to `j` does not contain pricing-relevant information for `i`, the positive peer move is temporary;
5. `i` subsequently underperforms while the overreaction unwinds.

The economic claim is more specific than generic sentiment or mean reversion because the signal requires the conjunction of an idiosyncratic negative shock, a news-derived competitive peer link, a relative-size relation, and a positive event-week return in the peer.

The original peer model is trained using a manually labeled sample and then applied to historical news. A live implementation would face model drift, entity-resolution changes, source-coverage changes, and point-in-time news availability. Those are not minor implementation details; they are part of the alpha identification and must be falsified separately.

## Signal

The source provides a relatively complete weekly event-driven trading construction, but several live-timing conventions remain underspecified.

### Source-reported event and peer construction

- **Frequency:** weekly.
- **Abnormal return:** the authors estimate crypto abnormal returns relative to crypto common risk factors. For event detection in the predictive strategy, each coin's abnormal return is standardized using information available up to that week.
- **Shock condition:** at the end of week `t`, crypto `j` is shocked if its standardized abnormal return is in the bottom decile of the historically observed distribution available at that time across cryptos/time.
- **Non-informational filter:** the shocked coin's standardized log news mentions must lie in the bottom half of its historically observed distribution available at that time.
- **Peer definition:** two cryptocurrencies are peers when they are co-mentioned in a sentence and a trained NLP classifier labels the sentence as describing a competitive relationship. Peer links are re-established at the beginning of each week from news information.
- **Smaller-peer filter:** eligible peer `i` must have smaller market capitalization than shocked crypto `j` during the event week.
- **Return filter:** eligible peer `i` must have a positive total return during the event week.

### Source-reported portfolio rule

- **Formation timestamp:** end of the event week after the shock, mention, size, peer-link, and positive peer-return conditions are observed.
- **Short entry:** short all eligible smaller peers of shocked cryptos.
- **Short weights:** proportional to each eligible peer's positive event-week return in the final journal article.
- **Long hedge:** long Bitcoin in an equal aggregate notional amount to keep the strategy approximately market neutral.
- **Leverage/margin:** the final article states that shorting occurs on margin at 1x leverage with Bitcoin as collateral.
- **Holding period:** the paper evaluates multiple weekly holding periods. The four-week version is the focal high-performing rule discussed in the text.
- **Capital allocation with overlapping cohorts:** for holding period `H`, only `1/(H+1)` of available wealth is allocated to new short positions each week; the equivalent long Bitcoin amount is opened alongside the short cohort.
- **Exit:** close each cohort after its fixed `H`-week holding period.
- **Weekly return accounting:** P&L from positions closed in a week is divided by terminal wealth from the prior week.

### Underspecified / version-sensitive items

- Exact exchange-close timestamp defining the weekly boundary is **underspecified** in the reviewed final-source text; do not assume a UTC weekday/hour without direct verification.
- Exact executable entry price and order type at the event-week boundary are **underspecified**.
- Ties, duplicate peer membership across multiple shocked cryptos, and exact handling of multiple simultaneous shocks are **underspecified** in the reviewed source text.
- The final journal version's complete fee/spread/borrow schedule was not independently resolved in this Scout cycle. An older working-paper version reports explicit costs, but because that version also differs in portfolio weighting, those cost parameters are version-sensitive and are not imported as final-source facts.
- Any use of perpetual futures instead of spot/margin borrowing is **research-proposed** and requires an independent funding/liquidation model.

## Required data

- **Instrument/universe:** a point-in-time cross-section of tradable cryptocurrencies with weekly returns, market capitalization, and sufficient historical coverage; the source focuses on the largest cryptocurrencies available through its vendors rather than a fixed modern exchange universe.
- **Venue/data vendors:** CoinGecko, CoinAPI, CryptoCompare for the historical source study; live replication may use other vendors only after demonstrating point-in-time equivalence.
- **Market type:** source return data are cryptocurrency market data; the short strategy assumes margin shorting. A perpetual-futures port is not source-equivalent.
- **Timeframe:** daily returns for factor/abnormal-return estimation and weekly aggregation for signal/event construction and portfolio rebalancing.
- **Fields:** daily/weekly price returns, market capitalization, trading availability/listing history, crypto market/size/momentum factor inputs, news article text, article timestamps, coin/entity mentions, peer sentence labels, and news-mention counts.
- **News corpus:** point-in-time crypto-news articles with publication timestamps and sufficient text to reconstruct sentence-level co-mentions and competitive-peer classification.
- **NLP model inputs:** entity-resolved sentences, a sentence-transformer representation, and the trained peer/non-peer classifier. The source uses the open-source `all-mpnet-base-v2` sentence transformer plus a neural-network classifier trained on 460 manually selected sentences; the reported OOS peer-classification accuracy is 88%.
- **Point-in-time requirement:** no article published after the portfolio formation boundary may influence peer links, mention filters, or event classification. Historical-distribution quantiles must use only information known by the formation date.
- **Survivorship/listing:** delisted/dead coins must remain represented when historically eligible. Modern replication must not construct the universe from current listings only.
- **Timestamp:** article publication time and market-data week boundaries must be aligned explicitly; timezone convention is a required replication choice because it was not fully resolved in the reviewed final-source text.
- **Missing data:** do not impute absent news relationships, returns, market caps, or factor exposures unless a pre-declared rule is justified. A missing peer link is not equivalent to a verified non-peer relationship when news coverage is sparse.
- **Funding/fee/spread needs:** observed or modeled margin borrow, spread, fee, slippage, market impact and borrow availability are required for a modern trading test. Perpetual portability additionally requires funding, mark/index and liquidation data.

## Execution assumptions

### Source-reported

- event-driven weekly portfolio formation after the event week closes;
- short eligible smaller peers and hold an equal notional Bitcoin long;
- 1x short leverage with Bitcoin collateral;
- fixed holding cohorts of `H` weeks;
- allocate `1/(H+1)` of available wealth to each new weekly cohort;
- final journal version weights shorts in proportion to positive event-week returns.

### Research-proposed for modern falsification

- Execute at the first causally available executable price after the weekly formation boundary rather than at a same-week closing price. **research-proposed**.
- Use next-quote or next-bar bid/ask execution with explicit spread/slippage rather than frictionless closes. **research-proposed**.
- Cap each short by a fixed fraction of observable ADV/open interest and available borrow. **research-proposed**.
- Treat missing borrow, delisting, suspension, forced buy-in, collateral impairment, exchange outage, and liquidation as explicit failure states rather than silently dropping positions. **research-proposed**.
- For perpetual adaptation, use delta-equivalent short perps and BTC long only after funding/mark/index/liquidation are included. **research-proposed**.

Because the source sample predates modern perpetual dominance, exchange failures, and the 2024-2026 institutional/ETF regime, a modern test cannot assume the historical margin-short implementation is still operationally equivalent.

## Evidence

### Source-reported

- Publication: *Journal of Corporate Finance* 93 (2025), article 102772, DOI `10.1016/j.jcorpfin.2025.102772`.
- Sample: weekly crypto data from 2017-10-01 through 2020-11-30, with market data from CoinGecko, CoinAPI and CryptoCompare and a CryptoCompare news corpus exceeding 200,000 articles.
- Peer identification: sentence-level co-mentions plus a competitive-relation classifier; the paper reports 88% out-of-sample classification accuracy for the peer model.
- Event-week co-movement: the final paper reports that a shocked cryptocurrency records an excess abnormal return of about `-23.5%` in the event week while its peers contemporaneously record about `+6.5%` excess abnormal return.
- Predictability: the authors report that the peer mispricing takes more than three weeks to disappear and that smaller peers subsequently reverse.
- Table 11 / main text: the four-week holding strategy reports roughly `43.61%` cumulative return, `0.23%` average weekly return, `1.01%` weekly volatility and annualized Sharpe about `1.398` (described in the text as `1.40`). The reported weekly alpha for the four-week version is `0.0018` with t-statistic `2.392`; the text summarizes the significant alpha as more than 13 bp per week.
- The paper reports statistically insignificant market and momentum betas for the focal four-week strategy and states that its annualized Sharpe exceeds the sample-period crypto market and Bitcoin Sharpe ratios of `0.53` and `0.73`, respectively.
- Placebo tests using random peer links, size-matched random links, or prior-return-matched random links do not reproduce the post-event predictability. The authors also report stronger co-movement for exogenous than endogenous shocks and weaker evidence under positive rather than negative shocks.

These are source-reported results. They are not ChatGPT-verified returns and are based on the source's historical 2017-2020 environment.

### Independently reproduced

not independently reproduced

### Negative evidence

1. **Old market regime:** the source sample ends in November 2020, before the 2021-2022 leverage cycle, major exchange failures, modern perpetual market structure, spot ETFs, and the 2024-2026 institutional regime.
2. **NLP/data dependency:** the signal depends on a specific historical news corpus and a trained classifier. Peer links may change materially with news-provider coverage, entity aliases, LLM/embedding changes, and current crypto narratives.
3. **Publication/version drift:** an accessible working-paper version differs materially from the final journal version on short weighting. This confirms that implementation details changed through publication and must be pinned to the final source before reproduction.
4. **Cost-model uncertainty in this Scout capture:** the final article's complete fee/spread/borrow assumptions were not independently resolved from the reviewed text. An older working-paper version reports substantial assumed bid-ask and short-maintenance costs, but those parameters cannot be silently treated as final-version facts because the same version uses a different weighting rule.
5. **Borrow and shortability:** many small cryptocurrencies may not be borrowable at all, or may only be shortable through derivatives with funding/liquidation risk unlike the source's margin assumption.
6. **Event rarity / concentration:** the strategy is event-driven and may derive much of its P&L from relatively few shock weeks, making regime and cluster dependence important.
7. **Positive-shock asymmetry:** the source reports weaker co-movement and predictability for positive shocks, so the mechanism is not symmetric.
8. **News causality is not absolute identification:** the authors run extensive controls and placebos, but the peer network and news exposure remain observational and may proxy for omitted attention/liquidity structure.

## Falsification plan

1. **Frozen modern OOS replication** — Reconstruct the final-source rule on a strictly point-in-time 2021-2026 sample with frozen code/model/data snapshots. **research-defined falsification threshold:** reject the modern-alpha hypothesis if the four-week market-neutral portfolio has non-positive net mean return or HAC/cluster-robust alpha `p >= 0.05` after pre-declared multiple-testing adjustment.
2. **Peer-model time-causality audit** — Rebuild peer links using only articles available before each weekly formation boundary. **research-defined falsification threshold:** fail the signal if any material share of links requires future articles, retrospective entity dictionaries, or labels unavailable at formation time.
3. **Peer-classifier robustness** — Compare the source-style classifier with a frozen modern sentence classifier while holding the news corpus fixed. **research-defined falsification threshold:** if strategy sign/performance disappears when only reasonable peer-classification perturbations are made, downgrade the mechanism to model-specific/unproven.
4. **Random-link placebo** — Repeat the source's random, size-matched, and prior-return-matched peer-placebo designs. **research-defined falsification threshold:** reject incremental news-peer alpha if placebo portfolios produce statistically indistinguishable or stronger post-event reversal after multiplicity control.
5. **Component ablation** — Remove one condition at a time: non-informational-news filter, smaller-peer filter, positive event-week peer-return filter, news-derived peer link, Bitcoin hedge. **research-defined falsification threshold:** if the news-derived peer condition adds no incremental OOS information over simpler size/reversal baselines, treat the NLP layer as non-essential rather than alpha-bearing.
6. **Shock-threshold perturbation** — Perturb the bottom-decile shock threshold and bottom-half mention threshold around the source values without retuning on the test set. **research-defined falsification threshold:** reject robustness if effect sign or alpha survives only at the exact published cutoff and fails at adjacent reasonable quantiles.
7. **Holding-horizon robustness** — Pre-register 1-7 week holds, with four weeks as the source focal horizon. **research-defined falsification threshold:** reject the slow-reversal mechanism if adjacent 3-5 week horizons do not preserve the predicted negative peer drift net of costs.
8. **Realistic shortability/cost stress** — Require actual historical borrow or perpetual availability, observed fees/spread, funding, slippage, forced exits and impact. **research-defined falsification threshold:** reject implementation viability if net expectancy is non-positive after venue-realistic costs or if more than 25% of intended short notional is untradeable/borrow-unavailable in the held-out sample.
9. **Liquidity/capacity stress** — Cap positions by observable liquidity and exclude signals where the planned short exceeds a pre-declared participation limit. **research-defined falsification threshold:** reject scalability if performance vanishes under a 1% of weekly traded-notional cap or if P&L is dominated by assets below the minimum tradability threshold.
10. **Regime split** — Evaluate 2021 bull, 2022 deleveraging, 2023 recovery, 2024 ETF transition, and 2025-2026 market structure separately. **research-defined falsification threshold:** reject generality if alpha is positive only in one regime or flips sign in two or more major regimes.
11. **Competing explanation controls** — Add contemporaneous liquidity, size, volatility, listing age, exchange coverage, general attention and ordinary short-term reversal controls. **research-defined falsification threshold:** if the news-peer event interaction loses incremental predictive power after these controls, reclassify the strategy as a proxy for a simpler effect.

Any Scout-defined cutoffs above are **research-defined falsification thresholds**, not source-reported acceptance criteria.

## Crypto portability

**Direct, with substantial modern adaptation risk.** The source itself studies cryptocurrency returns and a crypto-specific news/peer network, so the underlying domain is directly crypto. However, the exact historical execution model is not automatically portable to current spot/perpetual venues.

Key portability risks:

- 24/7 weekly boundaries must be standardized; small timestamp changes can alter event-week returns and news availability.
- Small-peer shorting may require perpetual futures rather than margin borrow, changing funding, mark/index, liquidation and counterparty exposures.
- Current exchange listing concentration differs from 2017-2020, and many historical coins are delisted or economically obsolete.
- Modern news diffusion through X, Telegram, Discord, exchange announcements, project feeds and LLM-driven aggregation may be materially faster than the source's web-news environment.
- Competitive relationships can change quickly as protocols pivot, merge ecosystems, move chains, or become inactive.
- Stablecoin quote and venue fragmentation can contaminate return and market-cap comparisons.
- BTC as the sole long hedge may not neutralize beta for altcoin peer baskets in all modern regimes; changing the hedge, however, is **research-proposed** and must be treated as a separate branch rather than silently modifying the source rule.

## Limitations

- **not independently reproduced:** no source backtest has been rerun by ChatGPT in this cycle.
- **data gap:** exact source-vendor snapshots and the complete historical news corpus were not independently downloaded/rebuilt in this cycle.
- **version gap:** working-paper and final journal strategy details differ on weighting; the final journal version is canonical here, but all implementation details should be re-verified against the final article/online appendix before reproduction.
- **timestamp gap:** the exact week-closing timezone/hour is underspecified in the reviewed final-source text.
- **execution gap:** exact final-version order type, fill price, full cost model, borrow failures and partial fills were not fully resolved in this Scout cycle.
- **shortability limitation:** small-peer assets are precisely where borrow/liquidity constraints are likely most severe.
- **sample limitation:** 2017-10 to 2020-11 is structurally distant from the current market.
- **model-risk limitation:** peer identification depends on NLP training labels, entity extraction and news-source coverage.
- **selection/multiplicity risk:** many event, peer and horizon choices can create researcher degrees of freedom; modern replication must pre-register branches and apply multiplicity control.
- **causal limitation:** extensive placebos and controls strengthen the news-overreaction interpretation but do not prove that news alone causally creates the reversal.

## Implementation status

No PyBroker, NautilusTrader, strategy-registry, data-pipeline, Kanban, Paper, Testnet or Live implementation has been created or modified by this Scout cycle.

`implementation_status: not-implemented`

## Adoption boundary

This record is Alpha Strategy Pool research material only. It is not evidence that the strategy remains profitable, is implementable on current venues, or is approved for any trading workflow.

`status: research-only`

`adoption: not-approved`

`approval_scope: research-only`

## Related Wiki records

No Hermes Wiki Brain record was written or modified in this Scout cycle. No stable related Wiki path was used as evidence for this record; the canonical Wiki Brain strategy-research specification was read only to resolve the required schema.

## Sources

1. Schwenkler, G. and Zheng, H. *News-driven peer co-movement in crypto markets*. Journal of Corporate Finance 93 (2025), 102772. DOI: https://doi.org/10.1016/j.jcorpfin.2025.102772
2. ScienceDirect open-access article page for the final journal version: https://www.sciencedirect.com/science/article/pii/S0929119925000409
3. Santa Clara University Scholar Commons record: https://scholarcommons.scu.edu/finance/10/
4. Author/academic working-paper version used only as version-history provenance: https://cdar.berkeley.edu/sites/default/files/cryptopeers_latestversion.pdf
