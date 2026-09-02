---
schema: strategy-research-record-v1
title: "DEX-Only Point-in-Time Cross-Sectional ML Crash-Avoidance Filter"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - dex
  - cross-sectional
  - machine-learning
  - crash-risk
status: research-only
confidence: medium
source_as_of: 2026-07-26
sources:
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6858778"
  - "https://doi.org/10.2139/ssrn.6858778"
  - "https://github.com/DaruFinance/dex-tradeability-study"
  - "https://github.com/DaruFinance/dex-tradeability-study/blob/d848735e7995c7c155e14ae3a28a84227d01d656/gap-studies/ml_xsec_ranker/ml_ranker_pit.py"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The source reports statistically detectable 7- and 14-day cross-sectional ranking skill, but explicitly states that it does not generate long-only alpha: every predicted decile has negative median forward return and the apparent top-K edge is attributed to winsorization and survivorship artifacts."
---

# DEX-Only Point-in-Time Cross-Sectional ML Crash-Avoidance Filter

## Provenance

- **Primary paper:** Daniel V. Gatto, *No Edge Without Information: An Empirical Study of Tradeability in Decentralized-Exchange-Only Cryptocurrencies*, SSRN Working Paper 6858778, 43 pages, posted and last revised 2026-06-10; date written 2026-05-31. DOI: `10.2139/ssrn.6858778`.
- **Primary public implementation:** `https://github.com/DaruFinance/dex-tradeability-study` at full commit `d848735e7995c7c155e14ae3a28a84227d01d656` (2026-07-26 snapshot).
- **Exact relevant path:** `gap-studies/ml_xsec_ranker/ml_ranker_pit.py` at that commit. This is the source-designated leakage-free re-run; the repository states that the earlier `ml_ranker.py` used end-of-sample snapshot features and is superseded for this claim.
- **Supporting implementation path:** `gap-studies/ml_xsec_ranker/ml_ranker.py` at the same commit contains the shared point-in-time OHLCV feature construction, model definitions, sample assembly, walk-forward logic, costs, ranking target, and top-K evaluation used by the leakage-free wrapper.
- **Source/data as-of:** code snapshot 2026-07-26. The public paper/repository identifies a survivorship-aware corpus of 4,990 DEX-only trading pairs across 27 blockchains, but the exact first/last market-data dates used for the reported PIT-ranker cells are not stated in the inspected public README/code excerpts: **data gap**.
- **Source-identity deduplication:** repository-wide and Wiki Brain searches found no existing record matching SSRN `6858778`, DOI `10.2139/ssrn.6858778`, the exact paper title, `DaruFinance/dex-tradeability-study`, or `ml_ranker_pit.py`. Related cross-sectional ML records use materially different universes, labels, architectures, and economic questions.

## Economic mechanism

### Source-reported

The source's broad conclusion is negative: for small DEX-only cryptocurrencies, a long-only trader using price information does not obtain detectable edge after realistic execution costs and null controls. The one qualified exception is a leakage-free cross-sectional machine-learning ranker using point-in-time features. The source reports positive out-of-sample rank information coefficient at 7- and 14-day horizons, while the 30-day horizon is insignificant.

Crucially, the source does **not** call this profitable alpha. It characterizes the surviving structure as **crash-avoidance skill**: the model ranks which coins are likely to fall more severely, but every predicted decile has negative median forward return. The source further states that the long-only top-K edge is a winsorization-and-survivorship artifact and that a long-only AMM trader cannot directly monetize the left tail.

### Research interpretation

The falsifiable hypothesis is narrower than a generic ML-return forecast: **within a contemporaneously alive cross-section of DEX-only tokens, lagged price/volume/liquidity-state features may contain incremental information about relative 7- to 14-day downside severity even when they do not identify positive-return winners.**

A plausible mechanism is heterogeneous deterioration rather than upside selection. Tokens displaying adverse combinations of recent returns, drawdown, volatility, illiquidity, volume velocity, range expansion, and weak trend state may be closer to liquidity withdrawal, abandonment, or crash dynamics. The model may therefore function as a **cross-sectional risk veto / crash-risk ranker**, not as evidence that price timing creates a standalone long-only trading edge.

Any use of this ranker to exclude high-crash-risk assets from another portfolio is **research-proposed**. The source itself reports the ranker as a lead, not an investable strategy.

## Signal

### Source-specified predictive construction

The leakage-free wrapper `ml_ranker_pit.py` uses the shared `ml_ranker.py` pipeline with the end-of-sample snapshot features removed.

1. **Universe eligibility:** load the DEX-only OHLCV panel and require at least 120 daily bars per pair; discard pairs whose close-to-close return standard deviation is `<= 0.01` in the loaded history as a near-stable/illiquid-history filter. The underlying corpus is sourced from currently live GeckoTerminal pools, so it is survivor tilted.
2. **Formation clock:** daily bars. All time-varying features used at rebalance day `t` are shifted by one day, so feature values are computed from data no later than `t-1`.
3. **Point-in-time age:** `log_age_pit = log1p(cumulative non-null bar count).shift(1)`. The leakage-free re-run drops end-of-sample reserve, age, 24-hour volume, and snapshot flow features.
4. **Lagged feature set:**
   - returns over 5, 10, 20, and 60 days;
   - 20- and 60-day standard deviation of log returns;
   - 20-day Amihud-style `log1p(mean(abs(log return) / volume))` proxy;
   - `log1p` of 20-day mean volume as a turnover proxy;
   - 10-day / 40-day mean-volume ratio as volume velocity;
   - 10-day return minus 40-day return as momentum acceleration;
   - 20-day close / rolling-maximum minus 1 as maximum-drawdown state;
   - 20-day rolling max/min close range minus 1;
   - indicator for close above its 20-day moving average;
   - point-in-time log age described above.
5. **Prediction horizons:** `R in {7, 14, 30}` days.
6. **Rebalance grid:** after a 60-day index offset, source code uses `range(60, len(days) - R, R)`, giving non-overlapping R-day rebalance spacing.
7. **Label:** forward `R`-day return is computed for each alive coin, then transformed into its cross-sectional percentile rank within each training rebalance date.
8. **Models:** LightGBM regressor and sklearn `HistGradientBoostingRegressor`. The inspected source fixes the principal tree parameters in code; model fitting is repeated under strict expanding walk-forward splits.
9. **Walk-forward:** the first out-of-sample boundary begins after roughly 40% of available rebalance dates; subsequent folds expand the in-sample set and predict later disjoint blocks. Feature missing values are imputed using the in-sample column median only.
10. **Evaluation:** cross-sectional Spearman rank-IC between predicted score and realized forward return. The source also ranks scores and evaluates top `K=20`, but explicitly warns that the apparent long-only top-K edge is not reliable alpha evidence.
11. **Null:** within each in-sample rebalance date, training rank labels are permuted across coins and the otherwise identical walk-forward procedure is re-run. The PIT wrapper defaults to 200 label permutations and reports a permutation p-value.

### Research-proposed operationalization

Because the source does not establish a profitable long-only strategy, the only proposed trading use in this record is a **risk filter**, not a source-reported entry rule:

- At an eligible 7- or 14-day rebalance, compute the PIT ranker score using only information available through the prior completed daily bar.
- **research-proposed:** if another independently justified long-only strategy selects a token that falls in the bottom predicted-return tail, veto or down-weight that position; do not create a new long merely because a token is highly ranked.
- The exact veto fraction/quantile is **underspecified by the source** and must be predeclared before testing. No default percentile is asserted here.
- Shorting the predicted crash tail is **unproven** because the source universe consists of DEX-only spot tokens for which borrow/perpetual availability is not assured.

## Required data

- **Instrument/universe:** DEX-only cryptocurrency spot pairs that have never been CEX-listed under the source's universe-construction process.
- **Scale:** source reports 4,990 trading pairs across 27 blockchains.
- **Provider:** source repository identifies GeckoTerminal/CoinGecko-derived OHLCV plus chain/universe metadata. Bitquery data supports other study components, but the leakage-free ranker explicitly drops snapshot flow features.
- **Timeframe:** daily OHLCV.
- **Fields used by PIT ranker:** close, volume, timestamps/pair identity; high/low/open are required by the source loader's quality filter even though the listed PIT rank features are derived primarily from close and volume.
- **Point-in-time:** historical bars must be available before signal formation; age is cumulative and lagged; end-of-sample reserve/age/volume snapshots are forbidden for this hypothesis.
- **Universe reconstruction:** a true validation requires point-in-time pool discovery including dead/rugged/delisted pools. The source itself states that its currently-live-pool universe creates survivorship bias.
- **Costs:** the source code estimates a per-coin round-trip cost using chain-specific gas assumptions plus a constant-product AMM cost function dependent on reserve and order size. The precise reserve input used in the historical cost map comes from universe metadata and is itself not a point-in-time historical reserve series: **data gap / survivorship-cost caveat**.
- **Missing data:** source drops pairs that lack sufficient history and requires at least 30 alive coins when assembling a rebalance cross-section; later top-K evaluation requires at least `3*K` coins.
- **Timestamp:** Unix-day aggregation is used in code (`ts // 86400`), implying UTC-day buckets; a replication must verify provider timestamp semantics and late/corrected bars.

## Execution assumptions

### Source-reported / source-coded

- Market type is long-only DEX spot/AMM.
- Source top-K evaluation uses equal weights across the 20 highest predicted scores.
- Forward returns are evaluated over 7, 14, or 30 days on disjoint rebalance spacing.
- Per-fill AMM cost incorporates swap/constant-product slippage and gas through the source cost model.
- The study does not provide a live-routing, latency, MEV, failed-transaction, partial-fill, or block-inclusion model for the PIT-ranker hypothesis.
- For top-K comparison, source code clips realized individual forward returns to `[-95%, +300%]`; the paper/README explicitly warns that top-K edge is sensitive to this winsorization and survivorship.

### Research interpretation

No same-bar executable price should be assumed. A future test must form the signal only after the prior daily data are final and apply a predeclared next-observable execution rule including gas, AMM price impact, slippage, MEV/adverse selection, failed transaction risk, and pool liquidity at that actual timestamp.

No leverage, borrow, perpetual funding, or short availability is assumed by this record.

## Evidence

### Source-reported

- The paper/repository reports a survivorship-aware corpus of **4,990 DEX-only pairs across 27 blockchains**.
- For the leakage-free point-in-time cross-sectional ranker, the source reports out-of-sample **rank-IC approximately 0.06-0.08 at 7- and 14-day horizons**, with **label-permutation p approximately 0.005**; the 30-day horizon is reported as insignificant.
- The source explicitly limits the interpretation: predictive skill is concentrated in the lower tail, **every predicted decile's median forward return is negative**, and the apparent long-only top-K edge is described as a winsorization-and-survivorship artifact.
- The source says the result rests on only roughly **15-30 disjoint rebalances**, depending on horizon/cell, and treats it as a research lead rather than an established edge.
- The broader study reports that price-based timing and several practitioner-style alternatives fail to beat their appropriate nulls after costs in this DEX-only universe; this contextual negative result is important because the PIT ranker is an exception in predictive structure, not evidence of general DEX inefficiency.

### Independently reproduced

not independently reproduced

### Negative evidence

- The source itself says the PIT ranker **does not generate alpha** for its long-only AMM setting.
- Every predicted decile has negative median forward return in the reported sample; the model distinguishes degrees of loss rather than reliably selecting positive-return tokens.
- The apparent long-only top-K edge is attributed by the source to winsorization and survivorship artifacts.
- The cross-sectional corpus is constructed from currently live pools, making survivorship the source's stated dominant uncontrolled threat.
- The effective number of disjoint OOS rebalances is small, increasing uncertainty around rank-IC and permutation inference.
- The superseded earlier ranker used end-of-sample snapshot features; only the explicitly leakage-free `ml_ranker_pit.py` variant should be considered for this record.

## Falsification plan

1. **Dead-pool-inclusive point-in-time universe test.** Reconstruct all historically observable DEX pairs, including subsequent failures/rugs, with eligibility determined only from information available at each rebalance. Metric: 7- and 14-day OOS Spearman rank-IC. **research-defined falsification threshold:** if either horizon's rank-IC is `<= 0` or fails to exceed its within-date label-permutation null at `p < 0.05`, reject the corresponding horizon as persistent predictive structure.
2. **Lower-tail localization test.** Measure forward returns by predicted decile and tail-loss classification quality. **research-defined falsification threshold:** if the bottom predicted decile does not exhibit worse median/quantile forward return than the cross-section in both 7- and 14-day OOS tests, reject the crash-avoidance interpretation even if aggregate rank-IC remains positive.
3. **Incremental filter test.** Apply the score only as a predeclared veto to an independently specified long strategy, with the base strategy frozen. Compare net return, downside deviation, max drawdown, and left-tail loss against the identical strategy without the veto. **research-defined falsification threshold:** if the veto does not reduce downside loss after incremental turnover and AMM costs, reject the actionable risk-filter hypothesis.
4. **Feature ablation.** Remove recent-return/momentum features, then liquidity/volume features, then volatility/drawdown features in separately predeclared models. Reject any claimed economic channel whose ablation does not materially reduce OOS rank-IC relative to its uncertainty.
5. **Horizon placebo.** Treat the source-reported insignificant 30-day cell as a negative control and test adjacent horizons without tuning on the test sample. If apparent significance appears broadly across shuffled or arbitrarily selected horizons, treat the 7/14-day finding as multiple-testing contamination.
6. **Venue/chain stability.** Re-estimate by chain and liquidity bucket. Reject broad portability if the signal is driven by one chain, one launch cohort, or the least executable liquidity tail.
7. **Execution/cost stress.** For any proposed veto or tradable portfolio, use point-in-time pool reserves, gas, swap fees, MEV/slippage stress, and transaction failures. If net benefit disappears under realistic execution, retain the statistical ranking finding but reject tradeability.
8. **Competing explanation.** Control explicitly for token age, liquidity, recent crash, and simple drawdown/volatility ranks. If the ML score adds no OOS rank information beyond a simple transparent baseline, reject the claim that the multivariate model contributes incremental information.

## Crypto portability

- **Portability:** `direct` for the source's DEX-only crypto cross-sectional prediction setting.
- This hypothesis is natively about cryptocurrency AMM/DEX spot markets, not an adaptation from traditional assets.
- It is **not directly portable to Binance perpetuals** without changing the universe, microstructure, available features, shortability, funding, liquidity, and listing-survivorship process.
- DEX execution is fragmented across chains and pools; gas, MEV, routing, token taxes/honeypots, liquidity migration, contract risk, and stale/irregular bars can dominate a nominal ranking signal.
- A future CEX/perpetual version would constitute a distinct empirical hypothesis unless the same PIT score is validated on that market with appropriate funding and execution treatment.

## Limitations

- **survivorship:** the source's current-live-pool corpus under-represents dead/rugged assets and is explicitly treated as an upper bound.
- **small effective OOS sample:** only approximately 15-30 disjoint rebalances support the reported lead.
- **data gap:** exact first/last dates of the PIT-ranker market panel were not established from the inspected public implementation/README.
- **cost-model point-in-time gap:** the leakage-free prediction features remove snapshot statics, but historical trading-cost reconstruction still depends on universe reserve metadata rather than a fully verified point-in-time reserve series.
- **model-selection risk:** two boosting model families and three horizons are evaluated; inference must preserve the six-cell search and any further experimentation.
- **not an upside selector:** positive rank-IC does not imply positive expected return or implementable long-only alpha.
- **short-side unproven:** many DEX-only tokens have no reliable borrow/perpetual market, so monetizing predicted crashes may be infeasible.
- **not independently reproduced.**

## Implementation status

No implementation has been made in PyBroker, Nautilus, the strategy registry, Paper, Testnet, Live, or any production data pipeline. This record only captures the source-backed research hypothesis and its negative evidence.

## Adoption boundary

- `status: research-only`
- `implementation_status: not-implemented`
- `adoption: not-approved`
- `approval_scope: research-only`

This staging record is not evidence of validated alpha and does not authorize implementation, paper trading, testnet, live trading, shorting, leverage, or capital allocation.

## Related Wiki records

- `[[quant/phase10-universe-lifecycle-survivorship-2026-08-28]]` — directly relevant to the source's dominant survivorship threat.
- `[[quant/phase8-financial-ml-sample-leakage-contract-2026-08-28]]` — relevant to the superseded snapshot-feature leakage and future walk-forward validation.
- `[[quant/signal-to-executable-pnl-costs-2026-08-28]]` — relevant to the gap between rank predictability and executable AMM PnL.

No materially equivalent Wiki Brain strategy-research record was found for SSRN 6858778 or this DEX-only PIT crash-ranker construction.

## Sources

1. Daniel V. Gatto (2026), *No Edge Without Information: An Empirical Study of Tradeability in Decentralized-Exchange-Only Cryptocurrencies*, SSRN Working Paper 6858778, posted/revised 2026-06-10, date written 2026-05-31. DOI: `10.2139/ssrn.6858778`. Stable abstract: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6858778
2. DaruFinance, `dex-tradeability-study`, public GitHub repository, immutable snapshot commit `d848735e7995c7c155e14ae3a28a84227d01d656`: https://github.com/DaruFinance/dex-tradeability-study/tree/d848735e7995c7c155e14ae3a28a84227d01d656
3. Leakage-free PIT ranker implementation, exact path `gap-studies/ml_xsec_ranker/ml_ranker_pit.py` at commit `d848735e7995c7c155e14ae3a28a84227d01d656`: https://github.com/DaruFinance/dex-tradeability-study/blob/d848735e7995c7c155e14ae3a28a84227d01d656/gap-studies/ml_xsec_ranker/ml_ranker_pit.py
4. Shared ranker pipeline, exact path `gap-studies/ml_xsec_ranker/ml_ranker.py` at the same immutable commit: https://github.com/DaruFinance/dex-tradeability-study/blob/d848735e7995c7c155e14ae3a28a84227d01d656/gap-studies/ml_xsec_ranker/ml_ranker.py
5. Public companion research page: https://daru.finance/research/dex-only
