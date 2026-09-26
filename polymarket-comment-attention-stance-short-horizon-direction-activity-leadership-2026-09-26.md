---
schema: strategy-research-record-v1
title: "Polymarket Comment-Feature Short-Horizon Signals: Attention/Toxicity/Stance vs. Trading-Activity, Buying-Direction and Leadership-Change Targets"
created: 2026-09-26
updated: 2026-09-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-24
sources:
  - "https://arxiv.org/abs/2609.28965"
  - "https://doi.org/10.48550/arXiv.2609.28965"
  - "https://arxiv.org/html/2609.28965v1"
  - "https://arxiv.org/pdf/2609.28965v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Polymarket Comment-Feature Short-Horizon Signals: Attention/Toxicity/Stance vs. Trading-Activity, Buying-Direction and Leadership-Change Targets

## Provenance

- **Primary source (pinned, checksummed, text-extracted and read across the sections listed below):** Sultan, Omneya; Morstatter, Fred, *The Conversation Turns First: Crowd Discussion and Price Reversals in Prediction Markets*, **arXiv:2609.28965v1 [cs.SI]**, dated **24 Sep 2026**. Both authors are at the **Information Sciences Institute, University of Southern California, Marina del Rey, California 90292, USA** (emails as printed: `osultan@usc.edu`, `fredmors@isi.edu`). Author block verified on both the HTML and the PDF title page.
- **Version identity (arXiv API entry fetched 2026-09-26):** `id = 2609.28965v1`, `published = updated = 2026-09-24T03:26:44Z`, `arxiv:comment = "8 pages, 1 figure"`, **primary category `cs.SI` only** (no q-fin cross-list), **no `journal-ref`**, no publisher DOI beyond the arXiv-issued DataCite identifier. The submission history shows **v1 only** as of 2026-09-26 (no v2).
- **DOI:** `10.48550/arXiv.2609.28965` — `https://doi.org/10.48550/arXiv.2609.28965` returned HTTP **302** (resolver redirect) and `https://arxiv.org/abs/2609.28965` returned HTTP **200**, both checked **2026-09-26**.
- **Pinned artifacts (both downloaded 2026-09-26):**
  - HTML: `https://arxiv.org/html/2609.28965v1` — **138,032 bytes**, **SHA-256 `d4705a193efe4af2aa8fc2ab470c5f20c97ffd509108afdb2f0ebdfb0041d028`**, stripped to 46,718 characters of text.
  - PDF: `https://arxiv.org/pdf/2609.28965v1` — **135,894 bytes**, **SHA-256 `13902c8dd5516d24ceb4dd036e2ffb9f0440a3e7aef8e28781bc3817fe17bf63`**, 8 pages (per the arXiv comment field); the PDF text layer was re-read against the HTML and the numbers below agree across both renderings.
- **Sections read line-by-line for this record:** Abstract; §1 Introduction; §2 Related Work; §3 Data Selection; §4 Correlation Sweep; §5.1 Temporal Construction and Features (comment features, trading and market-state features); §5.2 Tasks and Evaluation; §6 Results incl. §6.1–§6.4; §7 Discussion and Conclusion; Acknowledgements (Generative AI disclosure); **Table 1, Table 2, Table 3, Table 4 read as printed**; References sampled for the cited works used in framing (Wolfers–Zitzewitz 2004, Tetlock 2007, Lee–Ready 1991, Chordia et al. 2002, Detoxify, TweetEval/TimeLMs, Kim et al. 2026 = arXiv:2602.07048, Mbrice 2026 = arXiv:2605.28745).
- **License:** CC BY 4.0 (printed on the HTML infobox).
- **Publication / peer-review status:** **arXiv preprint only, not peer reviewed** — no journal-ref, no publisher DOI, primary category cs.SI only. The paper carries a **Generative AI disclosure**: Claude (Anthropic) assisted with analysis code, experimental reports, drafting and generated the comment-level stance labels; ChatGPT (OpenAI) assisted with manuscript drafting/revision and tables.
- **Code / data / replication:** a targeted scan of the pinned HTML for `data availability`, `code will`, `available at`, `upon request` and `github` returned **no hits except arXiv's own "Report GitHub Issue" page chrome** → **no code repository, no replication package, no data-availability statement**; every availability field is `not stated in source`.
- **Sample period:** **`data gap` / `not stated in source`.** The paper never prints a collection window, a date range for the markets, or an as-of date for the trade/comment history. The only temporal anchors in the pinned text are (i) the arXiv v1 date 2026-09-24, (ii) Polymarket documentation references "Accessed September 16, 2026", and (iii) library/software citations accessed the same day. **No collection dates are inferred in this record.**
- **Transaction-cost treatment (Methods-level read of §3, §4, §5.1, §5.2, §6, §7 plus a full-text scan of both pinned renderings):** the words `fee`, `cost`, `spread`, `slippage`, `profit`, `backtest` and `strategy` appear in the paper only in (a) the §1 platform description — "On fee-enabled markets, taker fees provide platform revenue and partly fund maker rebates, with the documented schedule varying by category and price" (citing Polymarket 2026a, a documentation link) — (b) literature-review sentences about other papers, and (c) §7's explicit scope statement "The study does not identify causal effects, private information, **or trading profitability**." There is **no cost model, no fill model, no spread/impact/participation assumption, no turnover, no capacity and no traded-strategy backtest anywhere in the source.** Therefore fees / spread / slippage / impact / participation / capacity / borrow / funding / financing / leverage / margin / latency / fill / failure handling / turnover are **all `data gap`, never zero**, and no result in this record may be read as net-of-cost.
- **Dedup (pre-write, whole repository, hidden-inclusive):** deterministic source-identity search across **all `.md` files plus `coverage_manifest.csv`, `.csv`, `.json`, `.txt` in the checkout including `.mimo-worktrees/`, `.agents/`, `.hermes/`** for `2609.28965`, `arxiv.org/abs/2609.28965`, `10.48550/arXiv.2609.28965`, `The Conversation Turns First`, `Omneya`, `Morstatter`, `Detoxify`, `63,720`, `non-political Polymarket`, `buy-flow imbalance`, `comment thread`, `distinct commenters`, `stance detection in prediction markets`, `2605.28745` → **all zero hits** before this write (the single `63,720` hit is an unrelated MSE figure inside `price-systematic-llm-adaptation-bitcoin-forecasting-2026-09-16.md`, cleared by inspection). Mechanism-level sweeps (`polymarket` within 100 chars of `comment|discussion|attention|stance|toxicity`, and `attention|comment|discussion|social` near `prediction market|Polymarket|Kalshi`) returned only incidental matches — FMZ page "public comments", source-code comments, and cross-reference lines — all cleared. `git log --oneline -20` was inspected as a convenience glance only and does not by itself satisfy dedup.
- **Four-axis distinction from the closest existing records:** `prediction-market-lead-lag-llm-semantic-risk-filtering-2026-09-03` (arXiv 2602.07048) links **market-to-market probability series** with LLM semantic filtering — mechanism, signal construction and data dependency (price series, no text side-channel) all differ here; `polymarket-favorite-longshot-bias-crypto-politics-2026-09-14` and `kalshi-prediction-market-pricing-wedge-executable-spread-falsification-2026-09-13` are **price-level calibration/inefficiency** records with no discussion data; `kalshi-temperature-ladder-market-implied-forecast-public-nwp-lead-2026-09-22` uses **meteorological** leading data; `polymarket-clob-maker-screening-rent-tail-demand-regime-arxiv-2609.20017-2026-09-19` is a **market-structure/rent** record. None of them uses comment-thread text (attention / toxicity / sentiment / stance) as the independent variable.

## Economic mechanism

### Source-reported

The paper's own framing (§1, §7): on Polymarket, "trading takes place alongside public comment threads. The two records reveal different aspects of collective behavior: trades allocate money, while comments reveal attention, emotional tone, and expressed support for an outcome." The authors ask "whether discussion helps predict what a market will do next" and deliberately separate three targets — **trading activity**, **buying direction**, and **changes in leadership** — "evaluating each against information already present in the trading record."

The source reports three qualitatively different roles for discussion (Abstract, §6, §7):

1. **Attention ≈ participation.** Comment counts, distinct commenters and reactions nearly match trade history in predicting heavy subsequent trading (PR-AUC 0.786 vs 0.790 against prevalence 0.606), with the relative advantage concentrated in **short** markets (≤21 days).
2. **Content ≈ direction.** Toxicity/hostility and stance (LLM-labelled bullish/bearish support) rank **future buying direction** above chance in 43 of 53 and 34 of 53 scored markets respectively, and adding attention + sentiment + stance to flow history raises ROC-AUC from 0.780 to 0.788.
3. **Price state ≈ leadership change.** Reversals of the leading outcome are predicted primarily by market state (distance from even odds, `p(1−p)`, liveness, recent movement); discussion **shifts against the leader before reversals** (23 of 27 evaluable markets away from even odds, exact binomial p ≈ 0.0003) but adds no clear incremental forecasting power at the block level.

The source explicitly refuses a causal reading: "We interpret these as predictive associations. Shared developments may affect both discussion and trading; our observational design does not identify the direction or presence of causal effects between them" (§1), and "These results … establish predictive associations consistent with discussion and trading responding to shared information, without identifying a causal effect of comments on markets" (Abstract).

### Research interpretation

Normalised, falsifiable statement of the mechanism as we read it: **in an on-chain event market with a public comment thread, the thread is a low-latency side-channel of the same latent information shock that later shows up in order flow; aggregating comment features (attention, hostility, stance) at fixed time bins should therefore carry incremental short-horizon information about the next bins' trade intensity and net buying direction beyond what the recent trade/price history alone contains, while the sign of the *price-level* state (proximity to $0.50) dominates any leadership-change prediction.**

Component roles as we normalise them (the source itself does not present a strategy):

```text
Data channel    : public Polymarket comment threads + trade history (6-hour UTC bins)
Primary signals : attention (comment/author counts, 24h trailing, count ratios),
                  hostility (Detoxify threat/insult/obscenity/identity-attack,
                  market-standardised, max = overall hostility),
                  sentiment (RoBERTa compound + polarity shares),
                  stance (LLM bullish/bearish/neutral labels vs. resolution criteria,
                  net and confidence-weighted net stance)
Baseline /      : trade count, 48h surge ratio, buy-flow imbalance, aggressor
controls          imbalance, log-odds, distance from $0.50, p(1-p), liveness
Targets         : heavy trading in next 3 bins (18h), next-bin burst,
                  sign of mean buy-flow imbalance next 3 bins,
                  activity increase next 3 bins, leader change next 4 bins
Trading layer   : NOT specified by the source — any entry/exit/sizing rule below
                  is research-proposed, and no traded result exists
```

Falsifiable predictions of this normalisation: (a) comment features add measurable out-of-market ranking power over a trading-history baseline for **direction** (the source reports +0.008 ROC-AUC, 0.780 → 0.788); (b) attention is a *participation* signal, not a *direction* signal (attention alone ROC-AUC 0.571 for direction but PR-AUC 0.786 for activity); (c) stance is anti-leader on average before reversals but too noisy at the block level to add clear forecast value (source: 0.394 → 0.414 PR-AUC, "smaller than fold variation"); (d) collapsing each market to a single whole-life summary destroys the signal (source: market-level stance classifiers ROC-AUC 0.512 / 0.485) — i.e. the information is **temporal and within-market**, not a cross-market "optimistic markets win" effect.

The strategy layer (any rule that turns these scores into a position) is entirely **research-proposed**: the source publishes no trading rule, no portfolio, no return series and explicitly excludes profitability from scope (§7).

## Signal

All parameters in this section are **source-reported** unless explicitly marked `research-proposed`.

### 1. Corpus and temporal construction (§3, §4, §5.1)

- **Universe:** non-political Polymarket markets; only **single-market events** (one thread → one price series); recurring series and autogenerated fixture markets excluded; candidates required **more than 100 platform-reported comments**. **79 markets** entered the sweep; **76 markets / 18,399 six-hour blocks** after truncation and warm-up; Experiment 6 used **18,323 labelled blocks across 74 markets** (two panel markets lacked stance labels). **63,720 retrieved and scored comments** are covered identically by the sentiment, toxicity and stance annotation files (four files per market: complete trade history + three annotation sets).
- **Contestedness (descriptive, not an exclusion):** each market lifetime normalised to 200 bins; contested if the winning-side price has binary entropy ≥ 0.5 in ≥ 20% of bins **or** total log-odds variance ≥ 40. Four uncontested markets were retained; the criterion "did not exclude markets from the reported analyses" (§3).
- **Clock:** trades and comments aligned to a **fixed UTC clock**; blocks start at **00:00, 06:00, 12:00, 18:00 UTC** (6-hour bins); the **first four blocks** are dropped for rolling-feature warm-up (§5.1).
- **Resolution/terminal handling:** a winning token required a **final trade price ≥ $0.95** (one extreme-longshot market failed and could not be processed); histories truncated when the winning token's **daily close first reached $0.99** (§4).
- **Liveness (feature-side, source-reported):** a block is *live* if, over the preceding week, price **crossed $0.50** or **spanned ≥ $0.10** (§5.1). **Short market:** lasting **≤ 21 days** before cutoff (§5.1).

### 2. Comment features (§5.1, all source-reported)

- **Attention (5):** comment presence; log comment count; log distinct-author count; log trailing 24-hour comment count; current count ÷ trailing 48-hour mean.
- **Sentiment:** RoBERTa compound score plus positive/negative/neutral shares.
- **Toxicity:** Detoxify threat, insult, obscenity and identity-attack scores, their four market-standardised counterparts, and **overall hostility = max of the four standardised scores**. Standardisation uses each market's **strictly preceding expanding history with ≥ 6 periods**; missing standardised scores filled with **0**; missing raw toxicity values **0**; undefined count/trade ratios filled with **1** (§5.1).
- **Stance (7 block-level features):** Claude Sonnet 5 labels each comment **bullish / bearish / neutral** with a confidence score, using the market's **verbatim resolution criteria** and market-specific prompts frozen across batches; features are the three label shares, **net stance (bullish − bearish share)**, **confidence-weighted net stance** (confidence × {+1, −1, 0}), log labelled-comment count, and the **trailing four-block mean net stance**. Stance is oriented to the **first-listed outcome**, independent of eventual resolution (§5.1).

### 3. Trading / market-state features (§5.1)

- **Burst:** log trade count; trailing 48-hour surge ratio; *bursting-now* indicator from the **expanding 80th percentile** of preceding counts.
- **Activity change:** adds trailing 24-hour mean absolute price movement.
- **Flow:** current **buy-flow imbalance** (dollars buying the two outcomes ÷ their sum), its four-block average, log trade count; **tick-based aggressor imbalance** as a distinct directional measure (Lee–Ready 1991; Chordia et al. 2002).
- **Leadership model (36 features):** 19 comment + 17 market-state signals — including distance from $0.50, `p(1−p)`, liveness, trailing log-odds movement, current/trailing buy-flow and aggressor imbalance, current movement sign / signed magnitude / trailing signed magnitude; burst and large-movement indicators use **preceding 80th and 85th percentimes over eight historical blocks**; leader orientation multiplies reference-token features by ±1 according to the current side of $0.50. **Stance is tested separately, not among the 36 features.**

### 4. Targets, models and evaluation (§5.2)

| Exp | Target (source-reported) | Sample | Model / evaluation |
|---|---|---|---|
| 1 | any of the **next three blocks** exceeds the market's **whole-life trade-count 80th percentile** | live + commented filter: 7,133 → **2,462 blocks / 65 markets**, **51 scored** | L2 logistic `C = 0.5` + 300 shallow boosted trees; leave-one-market-out |
| 2 | same as Exp 1, split by market duration | 19 live short / 32 live long (and 24 / 37 without live filter) | grouping after prediction |
| 3 | **burst in the next block**, no live filter | **3,801 commented blocks / 74 markets**, **62 scored** | logistic; random-score reference over **200 seeds** |
| 4 | **sign of mean buy-flow imbalance in the next three blocks** | **3,699 commented blocks / 74 markets**, **53 scored**; plus 20 random splits of 58 train / 16 test markets | logistic `C = 0.5` |
| 5 | mean trade count next three blocks **> current count** | **3,691 commented blocks / 74 markets**; 20 splits of 56/18 markets and 20 splits of 2,953/738 blocks | 300 boosted trees, depth 3, lr 0.05, 80% row/column sampling |
| 6 | **change of leader within the next four blocks** (prevalence **0.078**), no comment filter | **18,323 labelled blocks / 74 markets**; five market-grouped folds; fixed seed-0 holdout of **20 markets = 2,391 blocks (668 commented)** | boosted trees + feature ablations |

- **Metrics:** PR-AUC vs mean prevalence, ROC-AUC vs 0.5; decision comparisons at probability 0.5 and in the **top-scoring decile**; baselines = training-majority, held-out-market majority (hindsight), current-burst persistence (§5.2).
- **Warm-up / exclusions:** first four blocks dropped; markets failing "≥10 qualifying blocks and both target classes" are not scored (but may still contribute training rows) (§5.2).

### 5. Trading rule — **research-proposed, not source-reported**

The source specifies **no** trading rule. Any of the following would be *our* operationalisation and is labelled `research-proposed` in full: taking a directional position in the first-listed vs second-listed outcome token at a 6-hour boundary when net stance or toxicity exceeds a threshold; a trade-activity burst pre-emptive liquidity-provision rule; a leader-reversal trade triggered by market-state scores; any sizing, entry price, order type, exit, stop, holding period, take-profit, fee treatment or capital allocation. **Nothing in this record may be treated as a source-reported strategy.**

## Required data

- **Instrument / venue:** Polymarket binary outcome tokens on **Polygon** (off-chain CLOB matching, on-chain smart-contract settlement, $1 redemption for the winning token), non-political single-market events (§1, §3).
- **Market type:** event/claim tokens (binary digital), quoted in USDC-collared cents; **not** spot, perpetual or futures.
- **Timeframe:** **6-hour UTC bins** (00/06/12/18) as the analysis grid; raw inputs are tick-level trade history plus timestamped comment threads.
- **Fields required:** full trade history (price, size, aggressor side for buy-flow and aggressor imbalance); complete comment threads with comment identifiers, authors, timestamps, reactions; platform-reported comment counts; resolution criteria text per market (verbatim, for stance prompts).
- **Derived fields:** log-odds, `p(1−p)`, distance from $0.50, liveness (52-week… i.e. **preceding-week** cross/spread rule above), expanding quantiles, trailing 24h/48h ratios, market-standardised toxicity.
- **Annotation pipeline (source-reported):** RoBERTa sentiment model, **Detoxify** toxicity model, **Claude Sonnet 5** stance labeller with market-specific frozen prompts. These are model-derived labels — the source states "Language annotations are model-derived, and neither the source-domain benchmarks nor the forecasting comparisons establish their accuracy for every comment" (§7).
- **Point-in-time / availability:** comment and trade timestamps are assumed aligned to a fixed UTC clock (§4); **the source states no publication-lag or look-ahead audit for comment availability** → `underspecified`. Feature standardisation is explicitly **strictly preceding expanding** (look-ahead-safe within the source's design).
- **Sample window / collection dates:** **`data gap` — not stated in source.**
- **Missing-data rules (source-reported):** missing standardised toxicity → 0; missing raw toxicity → 0; undefined count/trade ratios → 1; markets lacking ≥15 comment bins excluded from the sweep (22 of 79).
- **Cost/fee fields needed for any live use:** Polymarket taker-fee schedule (varies by category and price), maker rebates, book depth/spread, tick size, latency to CLOB — **all `data gap` in the source** (only a prose reference to the documentation exists).

## Execution assumptions

**The source makes no execution assumptions of any kind**, because it runs no trading simulation. Everything below is therefore a gap, never an implied zero:

- Signal-to-order timing: **`underspecified`** (the source forms features on the completed 6-hour block and predicts *subsequent* blocks, but never states when a trader could act, whether fills happen inside the block, or at which price).
- Order type, fill model, same-bar/next-bar, market vs limit: **`data gap`**.
- Fees, spread, slippage, market impact, participation/ADV caps, capacity, turnover: **`data gap`** (the only fee mention is the §1 platform description of taker fees funding maker rebates, with a schedule "varying by category and price").
- Funding, borrow, leverage, margin: **`data gap`** (binary outcome tokens have no funding/leverage concept in the source; collateral mechanics are not analysed).
- Latency, partial fills, failed/partial resolution, dispute windows: **`data gap`**.
- Any cost ladder, position cap or risk rule used downstream of this record is **`research-proposed`**.

Because the source reports discrimination metrics (PR-AUC / ROC-AUC) rather than returns, **no gross-vs-net distinction can even be formed** for its results; reading any number below as P&L-related would be a misreading.

## Evidence

### Source-reported

All figures are third-party, **source-reported**, **gross-of-nothing** (no cost model exists), and **not independently reproduced**. Provenance is pinned to the section/table of arXiv:2609.28965v1.

**A. Correlation sweep (§4, Table 1):** grid of **34,938,540 cells**, **2,388,347 computable**, **246,739 eligible** across **57 markets** (22 markets lacked 15 comment bins). Clearing rates (%) by feature family — **Attention 33.0 / 14.7 / 7.2** (activity / price / direction), **Hostility 8.8 / 5.0 / 2.7**, **Tone 2.6 / 2.1 / 1.8** (Table 1 caption: "Rates describe eligible configurations, not predictive accuracy or calibrated discovery rates"). At the representative 6-hour / 1-comment / 1-bin-lead setting, distinct-commenter counts predicted subsequent trade count in **32 of 57** markets (all positive, **median r = 0.58**); insult scores cleared in **15** markets (all positive, **median r = 0.41**). Of **415** clearing hostility–direction cells: **257 live (58% positive), 66 settled (15% positive), 92 both (42% positive)**. Mean sentiment vs buy-flow imbalance cleared in **0 of 57** markets. Six-hour bins produced **7,775** clearing cells vs **6,334** (12h) and **4,503** (24h). Attention–activity cleared **33% live vs 24.2% settled**.

**B. Activity targets (Table 2, PR-AUC, all rows require comments):**

| Setting | Chance | Attention | Trading | Both |
|---|---|---|---|---|
| E1: live, 18h | .606 | **.786** | **.790** | **.793** |
| E3: all, 6h | .387 | .637 | .692 | .673 |
| E5: markets | .484 | .530 | .734 | .734 |
| E5: blocks | .483 | .534 | .745 | .750 |

- E1 under boosting: trading .767 → both **.781**, beating trading in **29** markets; toxicity alone **.663**, sentiment alone **.626**; adding toxicity did not improve on trading alone (§6.1).
- E1 decisions: accuracy attention **.612** vs trading **.685** vs both **.684** vs training-majority **.606**; on 2,393 scored blocks attention flagged 1,971 (recall **.875**, precision **.660**); top-decile precision attention **.745**, both **.833** (199 of 239 flags, recall **.134**).
- Without the comment filter: trading **.745** vs attention **.685**; at daily resolution **.811** vs **.775**; raising the comment threshold improves attention by only **+0.012** (5 comments) and **+0.045** (10 comments) (§6.1).
- E2 duration split: markets favouring attention had median duration **15.0 vs 76.5 days** and **15.1 vs 4.2** comments/day (Mann–Whitney p < 0.001 and < 0.020). Live short (n=19): attention **.766** vs trading **.718**; live long (n=32): **.833 vs .798**; without the live filter, short (n=24) **.739 vs .715**, long (n=37) **.846 vs .790**. Top decile on short markets: combined **.825** (33/40), trading .775, attention .625; on long markets trading **.975** (195/200). Attention's short-market recall at 0.5 was **.990** with precision **.524** against pooled prevalence **.520** (§6.1, Figure 1).
- E3: attention **.637**, trading **.692**, both **.673** against prevalence .387; **empirical random-score reference .447 ± .012 over 200 seeds (min .407)**; accuracy trading **.710** vs training majority .613 and held-out-market majority .689; attention accuracy **.594**; trading top-decile precision **.695** (260/374) vs attention **.529** (§6.1).

**C. Direction of buying (Experiment 4, Table 3, mean held-out-market ROC-AUC over 53 scored markets):**

| Features | ROC-AUC | Above .5 | Accuracy |
|---|---|---|---|
| Toxicity | **.586** | **43/53** | .496 |
| Stance | **.580** | 34/53 | .546 |
| Attention | .571 | 34/53 | .554 |
| Sentiment | .540 | 33/53 | .496 |
| Flow history | **.780** | 49/53 | .805 |
| Flow + stance | .779 | 51/53 | .803 |
| Flow + attention + sentiment + stance | **.788** | 51/53 | **.812** |

- Top decile: strongest combined precision **.965 (329/341)**, recall **.207**, vs flow-only **.962**; at probability 0.5 precision **.816**, recall **.824** (§6.2).
- 20 random market splits: stance **0.600 ± 0.065**, flow history **0.908 ± 0.024**, flow + stance **0.909 ± 0.033**. Live-block restriction: stance **.584** (44 markets). Daily aggregation: stance **.547** (34 markets) vs flow **.805** and flow+stance **.802** (§6.2).
- Market-collapsed control: whole-life net stance vs whole-life flow direction **ρ = 0.15 (p = 0.202)**; market-level stance classifiers **ROC-AUC .512** (flow direction) and **.485** (winning outcome) — the signal disappears when markets are reduced to one observation (§6.2).

**D. Activity increase (Experiment 5, §6.3):** on unseen markets trading **PR-AUC .734 ± .027**, **ROC .737 ± .024**, accuracy **.677 ± .019** (majority .516); attention **PR .530 ± .024**; trading + attention PR .734, **ROC .740**. Under block splits trading **.745 ± .014 → .750 ± .015**. Top-decile precision: pooled market-split trading **.871 (1,575/1,808)**, combined **.865**; block splits **.885 (1,306/1,476)** and **.888 (1,311/1,476)** — lifts ≈ **1.8×** prevalence (attention alone ≈ **1.2×**). Paired-block stricter construction: sample 3,637 → 1,822, trading PR **.652 → .661**, trading+stance **.671**. Adding liveness and contestedness as features changed ROC-AUC by **less than 0.001** (§6.3).

**E. Leadership change (Experiment 6, Table 4, §6.4):** five market-grouped folds — mean PR-AUC **.420**, pooled **.403** vs prevalence **.078**, pooled ROC-AUC **.868**; ROC exceeded each fold's chance reference in all five folds; "predicting no change" would give **92.2% accuracy**. Fixed 20-market holdout (2,391 blocks / 668 commented):

| Features | All, 6h | All, 24h | Comments, 24h |
|---|---|---|---|
| Full | .242 | **.517** | .386 |
| Market state | **.260** | .515 | .407 |
| Comment signals | **.057** | .158 | .233 |
| Price distance | .259 | .511 | **.428** |
| Prevalence | .042 | .120 | .162 |

- Operating points on all 18,323 blocks: market-state model at 0.5 flagged **745** and captured **408** reversals → precision **.548**, recall **.287**, lift **7.1**; top decile **736/1,832** → precision **.402**, recall **.518**, lift **5.2**; combined top decile **.398**; comments alone **.092** (§6.4).
- **Stance before reversal:** mean stance toward the current leader **−0.080** within a day before a reversal vs **+0.025** otherwise (3,801 commented blocks); among **27** markets with sufficient observations **more than $0.20 from even odds** in both groups, **23** showed more negative stance before reversals (two-sided exact binomial **p ≈ 0.0003**); typical within-market gap **0.235**. Individual-block evaluation: stance alone PR-AUC **.121 ± .043** vs prevalence **.101**, ROC-AUC **.486**; market state **.394 ± .109** (ROC .852) → adding stance **.414 ± .107** (ROC .853), an increase "smaller than fold variation"; top decile **178 vs 172** of 380 flags (precision **.453 → .468**).

### Independently reproduced

not independently reproduced

### Negative evidence

1. **No traded result exists.** The source runs classification experiments, not a strategy: no returns, no Sharpe, no drawdown, no win rate, no turnover, no capacity, no cost model. §7 states outright: "The study does not identify causal effects, private information, **or trading profitability**." Any alpha reading of these AUCs is an extrapolation, not a source claim.
2. **`data gap` on every execution field** (fees, spread, slippage, impact, participation, capacity, latency, fill, borrow, funding, turnover). Polymarket's own taker-fee schedule is referenced only in prose and "varies by category and price"; the source does not evaluate whether its 0.788-vs-0.780 direction gain survives any fee.
3. **The incremental value of comment content is very small.** Flow history alone already gives ROC-AUC **.780**; attention + sentiment + stance raise it to **.788** (**+0.008**), accuracy .805 → .812. Toxicity, the strongest single comment family (`.586`), **did not improve** the combined model at all (§6.2).
4. **Leadership-reversal signal fails its own event-level test.** Stance-alone PR-AUC .121 vs prevalence .101 and ROC-AUC **.486 (below chance)**; adding stance to market state moves PR-AUC .394 → .414, which the source says is "smaller than fold variation, so improvement was not established with confidence" (§6.4). The attractive aggregate pattern (23/27 markets, p ≈ 0.0003) **does not yield a usable block-level predictor** — the paper says so explicitly: "An aggregate behavioral pattern and an effective event-level predictor are different findings."
5. **Price state, not discussion, dominates reversal prediction.** Comment signals alone give PR-AUC **.057** at 6h against prevalence .042 (Table 4); distance-from-even-odds alone (.259/.511/.428) matches or beats the full model. The paper's own headline is that "leadership changes are predicted primarily by market state."
6. **Selection/snooping is acknowledged and uncorrected.** The exploratory sweep searched a grid of **34,938,540 cells** with **analytic p < 0.01** and **no permutation null**: "No permutation null was computed, so neither the nominal p-values nor the clearing frequencies estimate a calibrated number of discoveries" (§4). The evaluated markets also informed setting selection — there is no independent replication cohort (§2, §7).
7. **Corpus selection is severe and ex-post:** non-political, single-market, **>100 comments**, discussion-rich, with a $0.95/$0.99 terminal-price screen. ~**70% of all blocks have no comments at all** (§6.1), so the signal applies only to a small, selected slice of markets and time.
8. **Comment-filter dependence:** without the comment filter, trading beats attention **.745 vs .685**; at daily resolution **.811 vs .775**. The attention "parity" is a property of the live+commented subset (§6.1).
9. **Signal is fragile to temporal aggregation and unit of analysis:** daily aggregation drops stance-direction ROC-AUC from .600 to **.547** (20-split) and .580 → .547 (held-out-market); collapsing each market to one observation removes it entirely (ρ = 0.15, p = 0.202; classifier ROC .512/.485) (§6.2).
10. **Activity prediction at the next-block horizon is weaker than the baseline:** E3 attention .637 vs trading .692, and the combined model (.673) is *below* trading alone; the empirical random reference (.447) is itself above prevalence (.387) because of finite-sample effects (§6.1).
11. **No out-of-sample protocol beyond market holdouts inside the same corpus.** "Whole-market holdouts assess transfer within that design rather than independent discovery replication" (§7). No frozen forward window, no later-time test, no second platform.
12. **Labels are model-derived** (RoBERTa sentiment, Detoxify toxicity, Claude Sonnet 5 stance) with **no human accuracy audit on this corpus**: "neither the source-domain benchmarks nor the forecasting comparisons establish their accuracy for every comment" (§7). The strongest single directional family (toxicity, .586) is a model score whose construct validity for "hostility" in prediction-market threads is unverified here.
13. **No causality.** The design cannot distinguish "comments cause/anticipate flow" from "a common shock moves both"; the source states this in the Abstract, §1 and §7.
14. **Rare-event economics of the reversal target:** prevalence 0.078, and even the best model flags ~10% of observations for ~half the reversals (precision .548 at 0.5, .402 top decile). A trading rule built on it would trade rarely, in markets with uncertain depth.
15. **`data gap` — no collection window at all.** The sample period is never stated, so the corpus cannot be dated, re-drawn, or checked for regime dependence (e.g. whether it spans a single market phase).
16. **`data gap` — no code, no data, no availability statement.** Polymarket comment history, the annotation files and the analysis code are not released; the corpus (63,720 comments, 79 markets) cannot be rebuilt from the paper alone, and Polymarket's comment API is not documented in the source.
17. **Multiplicity across six experiments × several feature families × two evaluation protocols × duration/liveness/aggregation slices** with no multiple-testing correction; the source cites Benjamini–Hochberg (1995) only as background and applies no correction to the reported results.
18. **Preprint status:** arXiv v1, **not peer reviewed**, cs.SI only, with a substantial share of the analysis pipeline and drafting performed by LLMs (disclosed).

## Falsification plan

Every threshold below is a **research-defined falsification threshold** and every construction choice is **research-proposed**; none of them is specified by the source. Each test has a pre-declared failure rule that cannot be rescued by retuning.

- **F1 — Point-in-time, forward replication.** Rebuild the 6-hour panel from a freshly collected, independently drawn Polymarket corpus (markets **not** in the original 79; collection window frozen and documented — closing the `data gap`), with strictly-preceding expanding standardisation. **Pass:** flow + comment features beat flow-only by **≥ 0.010 ROC-AUC** for the direction target with a market-clustered 95% interval excluding zero. **Fail:** increment ≤ 0.000 or interval includes zero → the +0.008 headline is not reproducible.
- **F2 — Genuine temporal holdout.** Train on markets whose first block is before a frozen cutoff, test only on later-formed markets (no market overlap, no re-selection of settings). **Fail** if the direction increment disappears (≤ 0) or if attention's activity PR-AUC falls below its prevalence baseline.
- **F3 — Permutation null for the sweep.** Re-run the 6-hour/1-comment/1-bin-lead screen with **1,000 circular time-shifts of the comment series per market**, rebuilding the clearing-rate distribution. **Fail** if the observed clearing rates (33.0% attention→activity) do not exceed the **95th percentile** of the null, or if the analytic-p<.01 clearing counts are not ≥ 3× the null mean.
- **F4 — Multiplicity control.** Apply Benjamini–Hochberg at **q < 0.10** across the printed grid (6 experiments × 4 comment families × 3 feature-combination arms × 2 evaluation protocols). **Fail** if the headline direction result (0.788) does not survive.
- **F5 — Cost ladder on any operationalised rule (research-proposed).** Any rule derived from this record must clear **0 / 1 / 5 / 10 / 20 bp** per side plus platform taker fees at 10% book-depth participation. **Fail** if net expectancy at 5 bp is ≤ 0, or if **>50%** of gross edge is erased at 10 bp.
- **F6 — Label-ablation test.** Replace model annotations with (a) a second independent stance model and (b) a **hand-labelled 500-comment audit set**. **Fail** if direction increment vanishes when labels change, or if human-audit agreement with the Claude labels is **< 0.70 Cohen's κ**.
- **F7 — Baseline horse race.** Jointly control for trade count, buy-flow imbalance, aggressor imbalance, log-odds level and change, distance from $0.50, liveness and market age. **Fail** if comment features' incremental contribution is absorbed (market-clustered t < 1.96).
- **F8 — Reversal-signal test (decisive for the title claim).** On an independent sample, test the anti-leader stance gap (pre-reversal vs otherwise) restricted to markets **> $0.20 from even odds**, and require block-level PR-AUC lift over market state. **Fail** if fewer than **60%** of evaluable markets show the negative gap, or if the block-level increment stays below fold variation (as in the source).
- **F9 — Horizon/aggregation stress.** Re-run at 1h, 12h and 24h bins and with market-collapsed features. **Fail** if the direction increment exists only at the 6-hour resolution that the sweep selected, or if the market-collapsed version (which the source shows to be null, ρ = 0.15) starts working — indicating the original was a binning artefact.
- **F10 — Universe transport.** Repeat on **Kalshi** (and, separately, on political markets, which the source excludes). **Fail** if the direction increment reverses sign or drops below 0 outside non-political Polymarket.
- **F11 — Capacity and liquidity audit.** For any operationalised rule, measure book depth at the 6-hour decision instant, realised spread, fill rate and turnover. **Fail** if the rule cannot deploy **≥ $10k** at ≤ 10% of top-of-book depth, or if turnover exceeds **500%/yr** without compensating edge.
- **F12 — Freeze-and-wait.** Freeze the full pipeline (features, models, thresholds) and evaluate on **≥ 6 months** of forward Polymarket markets. **Fail** if net-of-ladder (F5) expectancy ≤ 0 or if PR-AUC for the activity target falls below prevalence.

Action on failure: mark the failing axis `falsified-in-our-tests` in this record, keep `status: research-only`, and do not promote to the candidate pool.

## Crypto portability

**adapted.**

- The source's evidence is already produced on a **crypto-rail venue** — Polymarket matches off-chain on a CLOB and settles on **Polygon** with dollar-denominated outcome tokens — so the mechanism *as demonstrated* lives inside an on-chain prediction-market venue. Re-running the same comment-feature study on Polymarket/Kalshi-class event markets is therefore an **adaptation of the same design**, not a port to a new asset class.
- **What does not port:** nothing in the source speaks to **crypto spot or perpetual markets**. There are no comment threads attached to BTC/USDT candles; no funding rate, mark/index price, basis, liquidation, borrow or 24/7 candle-boundary treatment appears anywhere; the target variables (buy-flow imbalance of a binary token, leader change of an event) have no spot/perp analogue. Mapping attention/hostility/stance onto Telegram/Discord/X chatter around a coin is a **different signal with a different data dependency**, untested here (`unproven`).
- Crypto-specific risks that the source never addresses: venue fragmentation across event markets, stablecoin/de-peg and USDC collateral risk, oracle/dispute outcomes that change the payoff independently of price, deposit/withdrawal and resolution-timing effects, and the fee schedule that "varies by category and price" — all `data gap`.
- Any crypto-spot transport claim must therefore be labelled a **ported hypothesis (`research-proposed`, `unproven`)**, not crypto empirical evidence.

## Limitations

Markers used: `underspecified`, `data gap`, `not stated in source`, `not independently reproduced`, `unproven`, `ex-post selection`.

- **No strategy exists in the source.** The record captures a falsifiable *hypothesis* (comment features carry short-horizon incremental information), not a backtested rule. The entire trading layer is `research-proposed`.
- **`data gap` — sample period / collection dates** never stated anywhere in the pinned text.
- **`data gap` — execution and cost**: fees, spread, slippage, impact, participation, capacity, turnover, latency, fill model, borrow, funding, leverage — none present, none implied zero.
- **`data gap` — reproducibility**: no code, no data, no availability statement; model-derived labels unreleased.
- **`underspecified` — tradability timing**: block boundaries are UTC-aligned, but the source never states when a participant could act on a completed block's features, nor the price/queue position at that instant.
- **`underspecified` — label semantics**: Claude-generated stance labels are oriented to the "first-listed outcome" and frozen prompts; the prompt text, model version pinning and confidence calibration procedure are not reproduced in the paper.
- **`ex-post selection` — corpus**: discussion-rich, non-political, single-market, >100-comment markets selected after the fact; ~70% of blocks are comment-free.
- **Snooping**: a 34.9M-cell sweep with analytic p < 0.01 and no permutation null, then experiments on the same corpus.
- **Modest effect sizes**: +0.008 ROC-AUC from comment content; stance alone at chance for leadership change (ROC .486).
- **No causality**, no profitability, no independent replication, no out-of-platform test.
- **`not independently reproduced`** for every number in the Evidence section.
- **`unproven`** for crypto spot/perpetual portability and for any period after the paper's undated corpus.
- **Preprint only**, not peer reviewed; substantial LLM involvement in analysis and writing (disclosed).

## Implementation status

`implementation_status: not-implemented`.

No implementation exists in our research stack. No Polymarket comment/trade pipeline has been built, no annotation model has been run, no classifier has been trained, no portfolio has been simulated, and no Paper, Testnet or Live verification of any kind has occurred. This record is a normalised research capture of a third-party arXiv preprint only.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

The presence of this record in this repository does **not** mean it passed Research Intake Review, entered Hermes Wiki Brain, entered the production candidate pool, completed Qlib full-backtest validation, became a frozen survivor or leaderboard entry, is profitable, is validated alpha, or is approved for implementation, paper trading, testnet, or live trading. None of those steps has happened.

## Related Wiki records

Pre-write `kb_search` in Hermes Wiki Brain: **zero** results for `prediction market Polymarket comments discussion attention stance` and **zero** for `social media comment sentiment stance toxicity attention signal returns`; `prediction market trading signal` returned **8 pages**, of which the following are verified and mechanism-adjacent (price/exec/valuation records for prediction markets, none using comment text as the input):

- [[quant/prediction-market-llm-confidence-weighted-value-bet-2026-09-04]] (LLM value-bet sizing — text-derived, but from resolution/news text, not crowd comments)
- [[quant/polymarket-binance-high-frequency-binary-lead-lag-2026-09-02]] (cross-venue lead-lag price signals, no discussion channel)
- [[quant/kalshi-prediction-market-pricing-wedge-executable-spread-falsification-2026-09-13]] (pricing anomalies vs. execution friction)
- [[quant/prediction-market-proper-betting-accuracy-profit-conversion-2026-09-02]] (accuracy → profit conversion, relevant to F5/F11)
- [[quant/crypto-prediction-market-layered-informed-trading-skill-score-2026-09-01]] (informed-flow decomposition)

No other Wiki link is asserted; none was fabricated.

## Sources

- Sultan, O., & Morstatter, F. (2026). *The Conversation Turns First: Crowd Discussion and Price Reversals in Prediction Markets*. arXiv:2609.28965v1 [cs.SI], 24 Sep 2026. DOI: https://doi.org/10.48550/arXiv.2609.28965 — landing page https://arxiv.org/abs/2609.28965 (HTTP 200, checked 2026-09-26; `arxiv:comment = 8 pages, 1 figure`; no journal-ref; v1 only).
- Pinned full text: https://arxiv.org/html/2609.28965v1 — 138,032 bytes, SHA-256 `d4705a193efe4af2aa8fc2ab470c5f20c97ffd509108afdb2f0ebdfb0041d028`, fetched 2026-09-26. Pinned PDF: https://arxiv.org/pdf/2609.28965v1 — 135,894 bytes, SHA-256 `13902c8dd5516d24ceb4dd036e2ffb9f0440a3e7aef8e28781bc3817fe17bf63`, fetched 2026-09-26. All quantitative claims above trace to this file: Abstract; §1; §2; §3; §4 (Table 1); §5.1; §5.2; §6.1 (Table 2, Figure 1); §6.2 (Table 3); §6.3; §6.4 (Table 4); §7; Acknowledgements.
- Cited-by-the-source references used only for framing (not as independent evidence here): Wolfers & Zitzewitz (2004); Tetlock (2007); Mao, Counts & Bollen (2011); Keskin & Aste (2020); Lee & Ready (1991); Chordia, Roll & Subrahmanyam (2002); Harvey, Liu & Zhu (2016); Jensen, Kelly & Pedersen (2023); White (2000); Benjamini & Hochberg (1995); Sethi et al. (2025); Dahlke et al. (2026); Kim et al. (2026, arXiv:2602.07048); Mbrice (2026, arXiv:2605.28745); Detoxify (Hanu & Unitary team, 2020); TweetEval (Barbieri et al., 2020).
- Polymarket platform documentation cited by the source as `Polymarket (2026a) Fees`, "Accessed September 16, 2026" — used only to record that a fee schedule exists; **no fee value is adopted in this record** (`data gap`).
