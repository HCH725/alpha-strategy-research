---
schema: strategy-research-record-v1
title: "LLM Persona Ensemble for Institutional 40/60 Stock-Bond Portfolio Timing with CPI-Regime-Conditioned Performance"
created: 2026-09-22
updated: 2026-09-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - llm
  - persona-ensemble
  - portfolio-timing
  - stock-bond
  - macro-regime
status: research-only
confidence: medium
source_as_of: 2024-11-29
sources:
  - "Yoshia Abe, Shuhei Matsuo, Ryoma Kondo, and Ryohei Hisano, 'Leveraging Large Language Models for Institutional Portfolio Management: Persona-Based Ensembles', arXiv:2411.19515v1 [cs.CE, cs.MA], submitted 29 Nov 2024 07:18:50 UTC, CC BY 4.0. https://arxiv.org/abs/2411.19515"
  - "Full text HTML of the same paper (v1): https://arxiv.org/html/2411.19515v1"
  - "Prompt/experiment repository cited inside the paper: https://github.com/YoshiaAbe/llm_based_portfolio_management (reachable, HTTP 200 verified 2026-09-22; not used as the basis of any empirical claim in this record)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# LLM Persona Ensemble for Institutional 40/60 Stock-Bond Portfolio Timing with CPI-Regime-Conditioned Performance

## Provenance

- **Primary source:** Yoshia Abe (Graduate School of Information Science and Technology, The University of Tokyo), Shuhei Matsuo (same), Ryoma Kondo (The University of Tokyo; Canon Institute for Global Studies), and Ryohei Hisano (The University of Tokyo; Canon Institute for Global Studies), *"Leveraging Large Language Models for Institutional Portfolio Management: Persona-Based Ensembles"* (`source-reported` affiliations taken from the arXiv author block).
- **Version / date:** `arXiv:2411.19515v1`, submitted Friday, 29 November 2024 07:18:50 UTC (single version; submission history shows no v2 at capture time). Subjects on the abs page: Computational Engineering, Finance, and Science (cs.CE); cross-list Multiagent Systems (cs.MA). License CC BY 4.0 (`source-reported`).
- **Publication status:** no `Comments` field, no journal-ref, no non-arXiv DOI on the abs page → treated as an **arXiv preprint of unknown peer-review status** (`not stated in source`).
- **Stable URLs:** https://arxiv.org/abs/2411.19515 · full text https://arxiv.org/html/2411.19515v1 · DOI https://doi.org/10.48550/arXiv.2411.19515.
- **Primary-source checksum (performed 2026-09-22 against the abs page and the v1 full-text HTML):** author list matches the four names above; v1 date/time matches; sample period (Oct 2021–Jan 2024 predictions; Nov 2021–Dec 2023 evaluation), universe (40% US equities / 60% US bonds), transaction-cost treatment (**no mention anywhere in the paper** → `not stated in source`), and all performance numbers quoted below were read from Sections III–V and Tables II–VIII / Figs. 2–5 of the v1 HTML.
- **Deduplication audit:** repository-wide search across all existing `*.md` records for `2411.19515`, the exact title, `Hisano`, `Yoshia Abe`, `mode ensemble`, `gpt-4-0613`, `40% US equities`, `llm_based_portfolio_management`, and `CPI Trend` returned **zero matches** (2026-09-22). No `coverage_manifest` file exists in this repository. Nearest relatives and why this record is independent: `digital-twin-finfluencer-belief-elicitation-silent-region-cross-sectional-2026-09-06.md` elicits stock-level scores from LLM replicas of real finfluencers (different source, different signal construction, single-name cross-section); `llm-distilled-kol-consensus-capability-factor-aggregation-2026-09-18` distills crypto key-opinion-leader capability factors into an IC-weighted consensus (different source, crypto traders, different aggregation); `prediction-market-llm-confidence-weighted-value-bet-2026-09-04.md` (PolyBench, arXiv:2604.14199) is a point-in-time LLM posterior value-bet benchmark on prediction markets (different source, different venue, different signal); `adaptive-alpha-weighting-ppo-llm-generated-alphas-2026-09-05.md` weights LLM-generated factor formulas with PPO (different source, factor library vs portfolio-timing classifier). This record's source identity, signal construction (persona-conditioned three-class macro-indicator classification with a two-stage mode ensemble), universe (40/60 stock-bond portfolio timing), and horizon (5-day ±2% target, daily position steps) are all distinct.
- **Schema provenance:** structure and frontmatter follow the canonical Wiki Brain contract `quant/strategy-research-record-spec-v1` (`schema: strategy-research-record-v1`), re-read this run.

## Economic mechanism

### Source-reported

The authors frame the task as institutional-style portfolio management: an LLM is given the previous 10 days of seven numerical indicators and asked to predict whether a portfolio of 40% US equities and 60% US bonds will rise or fall by more than 2% over the next 5 days, outputting one of three classes (`0` hold, `1` fall, `2` rise). Because LLM outputs vary with the persona stated in the prompt, the paper instantiates three personas — short-term (individual investor, several-day horizon, limited investment knowledge, weak risk management), medium-term (institutional investor, months-to-years horizon, extensive knowledge, robust risk management), and long-term (both investor types, 20–30 year perspective) — repeats each prediction five times, and aggregates votes with a *mode* (majority, ties broken toward the smaller class number) or a *sensitive* (any rise/fall signal wins) ensemble, first across the five trials and then across the three personas. The paper's stated rationale for why LLM strategies can help is knowledge beyond the 10-day window: the model can recognize that recent moves belong to a larger inflation-driven downtrend, which naive 10-day baselines cannot (`source-reported`, Section VI).

### Research interpretation

The falsifiable mechanism is **persona-heterogeneous aggregation plus prior-knowledge regime reading**:

- *Regime:* not a separate filter in the source — the CPI split is an ex-post analysis device (see Signal). The hypothesized tradable regime condition is that a persona-ensemble LLM adds value over 10-day technical baselines specifically during rising-CPI (inflation-scare) periods, when medium-term macro knowledge discriminates the path of stocks and bonds.
- *Primary signal:* three-class direction/magnitude classification of a 40/60 stock-bond portfolio from seven macro/price indicators, stabilized by two-stage majority voting (trials, then personas).
- *Confirmation:* none specified by the source beyond the ensemble vote itself; any additional confirmation filter would be `research-proposed`.
- *Risk / exit:* the "exit" is purely mechanical position de-risking — the invested fraction is stepped down in 0.2 increments when the ensemble votes class 1, reaching 0.0 (full cash) at worst. There is no stop-loss, no volatility targeting, and no borrow/shorting.

Do not assume the persona ensemble is the alpha source: the paper's own accuracy ablation shows the *long-term persona alone* (0.378 mode accuracy) beats the *inter-persona* mode ensemble (0.366), and the inter-persona ensemble only wins on decline-detection F1 (0.484). The economic claim therefore separates into (i) a decline-detection/risk-off claim, which the ensemble supports, and (ii) a return claim, which is regime-conditional and partly contradicted inside the same paper.

## Signal

All items below are `source-reported` unless marked `research-proposed` or `data gap`.

- **Formation timestamp:** every weekday over 593 trading days (October 2021 – January 2024) the model receives the previous 10 days of indicator values and emits one class; each prediction is repeated five times and aggregated (mode across trials, then mode across the three personas) before it drives that day's position (`source-reported`). Clock time, timezone, and publication/availability lag of the seven indicators are **not stated in source** (`data gap`) — point-in-time tradability of the rate/VIX/DXY inputs therefore cannot be verified from the paper.
- **Task / target:** three-class classification of whether the 40/60 portfolio rises or falls by more than 2% within the next 5 days; classes `0` (hold), `1` (fall), `2` (rise) (`source-reported`, Section III-A).
- **Lookback:** previous 10 days of seven indicators (`source-reported`): A = 40% stock / 60% bond portfolio return; B = US stocks (futures) return; C = US 5-year interest rate; D = US 30-year interest rate; E = US 30–10 year interest-rate spread; F = VIX; G = US Dollar Index. Warm-up and endpoint conventions are not stated (`data gap`).
- **Model:** GPT-4, pinned snapshot `gpt-4-0613` (trained up to September 2021) for all experiments; five trials per day; prompting methods 1–9 of the paper's Table I (clear instructions, delimiters, output format, persona specification, rationale-before-conclusion, chain-of-thought, zero-shot CoT). Sampling temperature and other API parameters are **not stated in source** (`data gap`).
- **Personas (exact source wording, normalized):** short-term = individual investor trading over several days with limited investment knowledge and weak risk management; medium-term = institutional investor trading over months to a few years with extensive knowledge and robust risk management; long-term = individual and institutional investors with a 20–30 year perspective.
- **Ensembles:** *Mode* = most-voted class across five trials, tie → smaller class number; *Sensitive* = if class 1 or 2 appears in any trial take that class (both present → most votes, tie → class 0). Final deployed ensemble for the investment strategies = mode across the five trials **then** mode across the three personas (`source-reported`, Sections IV-B and V-B).
- **Position sizing / entry:** invested fraction takes values in {0.0, 0.2, 0.4, 0.6, 0.8, 1.0}, starting at 1.0 (`source-reported`, Section IV-C). Three action patterns:
  - *Pattern 1 (binary):* class 1 → decrease one step; class 0 or 2 → increase one step.
  - *Pattern 2 (ternary):* class 1 → decrease one step; class 2 → increase one step; class 0 → no change.
  - *Pattern 3 (ternary + drift-back):* as Pattern 2, but if the position has been flat for `d_flat = 5` days it is gradually increased back to 1.0 in 0.2 steps.
- **Exit:** no exit rule other than the position reaching 0.0 (all cash). No re-entry rule beyond the same stepping logic. Holding is continuous; there is no trade-settlement horizon because the "asset" is a stock-bond portfolio, not a contract (`source-reported`).
- **Baseline strategies (for comparison):** buy-and-hold at constant 1.0; *Continuous movement* CM(D2)/CM(D3) — raise/lower position when indicator A rose/fell for 2 or 3 consecutive days within a 10-day window; *Regression* RG(S10)/RG(S5) — 10-day linear-regression slope of indicator A, adjust when |slope| ≥ 0.001 (S10) or 0.0005 (S5), otherwise hold.
- **Evaluation metrics (unconventional — read carefully):** return = cumulative return of position-weighted daily returns **divided by the average position size**; volatility and max drawdown analogously divided by average position; Sharpe = (cumulative return) / (volatility), with **no risk-free rate** (`source-reported`, Section IV-C formulas).
- **Regime split (analysis device, not part of the strategy):** CPI Trend = direction of the 6-month moving average of the year-over-year change in US CPI Total versus the previous month; High = Nov 2021–Aug 2022 plus Dec 2023, Low = Sep 2022–Nov 2023 (`source-reported`, Section V-C). Using this split as a *tradable* gate would require publication-lag handling — the paper does not do so; any such gate is `research-proposed`.
- **Fully specified?** The classifier target, personas, ensemble rules, position lattice, action patterns, baselines, and metrics are reconstructible. Indicator vendors/instruments, signal time-of-day, API sampling parameters, and any cost model are **underspecified** (`data gap`).

## Required data

- **Instrument / universe:** a portfolio of 40% US equities and 60% US bonds; the exact proxies (index, futures, ETF) are **not stated in source** (`data gap`). Indicator B is described only as "US Stocks (Futures, Return)".
- **Venue / market type:** unspecified traditional brokerage/bond market; no crypto, no derivatives, no shorting (`source-reported` at the level of asset classes only).
- **Timeframe:** daily (593 weekdays), 5-day prediction horizon, monthly evaluation buckets.
- **Fields:** the seven indicators A–G listed above (daily, previous 10 days); US CPI Total (YoY, 6-month MA) for the ex-post regime labels; portfolio daily returns for evaluation; the GPT-4 class outputs (5 trials × 3 personas per day).
- **Point-in-time / availability:** model training cutoff September 2021 precedes the October 2021 – January 2024 sample (avoids direct label leakage from the model's training data, `source-reported`); indicator release lags and any look-ahead in constructing indicator A are **not stated in source** (`data gap`).
- **Timestamp / timezone:** not stated (`data gap`).
- **Missing data:** not discussed by the source (`data gap`); Table VI reports `nan` Sharpe for months with zero volatility (2023-05 CM(D3), 2023-06 CM(D3)).
- **Costs/fees/spread needs:** no fee, spread, slippage, bid-ask, turnover, or market-impact field appears anywhere in the paper → **`not stated in source`** (4 mentions of this gap tracked in Execution assumptions/Evidence). It must not be read as "zero cost".

## Execution assumptions

- **Signal-to-order timing:** daily adjustment immediately after the ensemble vote; same-day vs next-day execution is **not stated in source** (`data gap`).
- **Order type / fill model:** not stated (`data gap`); the backtest implicitly rebalances a stock-bond portfolio in 0.2 position increments each time the class demands a change.
- **Fees / spread / slippage / impact / capacity:** **`not stated in source`** — the paper contains no transaction-cost, commission, spread, slippage, turnover, liquidity, market-impact, or execution discussion (verified by full-text search of the v1 HTML). With a 0.2-step daily lattice the implied turnover is non-trivial, so net-of-cost performance is unknown and must not be inferred.
- **Funding / leverage / margin / borrow / shorting:** position is a 0–1 invested fraction; no leverage, no short leg, no borrow (`source-reported`).
- **Latency / partial fills / failures:** not discussed (`data gap`).
- **LLM operational assumptions:** five GPT-4 trial calls per day per persona set; model snapshot `gpt-4-0613` availability and API cost are not addressed by the source (`data gap`).

## Evidence

### Source-reported

All figures below are `source-reported` from arXiv:2411.19515v1 and have **not** been independently reproduced. Provenance (Table/Figure/Section, sample, gross/net status) is given for each. All results are **gross of any cost** (no cost model exists in the paper).

*Prediction accuracy (Experiment 1, 593 weekdays, Oct 2021 – Jan 2024; chance level 0.333 for a uniform three-class guess):*

- Fig. 2 — average accuracy across five trials: short 0.345, medium 0.333, long 0.352; with the mode ensemble across trials: 0.361 / 0.339 / 0.378; with the sensitive ensemble: 0.314 / 0.312 / 0.317 (mode helps, sensitive hurts).
- Table II — inter-persona × within-persona ensemble accuracy: mode×mode **0.366** (best), mode×sensitive 0.324, sensitive×mode 0.319, sensitive×sensitive 0.307.
- Table III — per-class precision/recall/F1 for the long-term persona with within-trial mode: class 0 = 0.551 / 0.327 / 0.411 (281 correct of 167 predicted), class 1 = 0.380 / 0.570 / 0.456 (172 / 258), class 2 = 0.202 / 0.243 / 0.221 (140 / 168).
- Fig. 3 — F1 for class 1 (decline detection): persona averages 0.449 / 0.451 / 0.423 (short/medium/long), mode-across-trials 0.474 / 0.479 / 0.456, sensitive 0.469 / 0.468 / 0.452.
- Table IV — inter-persona F1(class 1): mode×mode **0.484** (best), mode×sensitive 0.466, sensitive×mode 0.477, sensitive×sensitive 0.461.
- Table V — per-class metrics for mode-across-trials then mode-across-personas: class 0 = 0.556 / 0.263 / 0.357 (281 / 133), class 1 = 0.378 / 0.674 / 0.484 (172 / 307), class 2 = 0.176 / 0.193 / 0.184 (140 / 153).

*Investment strategies (Experiment 2, 26 months, Nov 2021 – Dec 2023; monthly Sharpe from Table VI, columns Buy-and-hold / Pattern 1 / Pattern 2 / Pattern 3 / CM(D2) / CM(D3) / RG(S10) / RG(S5); paper's Sharpe definition, gross):*

| Month | B&H | P1 | P2 | P3 | CM(D2) | CM(D3) | RG(S10) | RG(S5) |
|---|---|---|---|---|---|---|---|---|
| 2021-11 | 0.097 | 0.280 | 0.397 | 0.397 | 0.108 | 0.097 | 0.097 | 0.172 |
| 2021-12 | 1.003 | 0.559 | 0.424 | 0.353 | 0.574 | 0.736 | 1.003 | 0.709 |
| 2022-06 | −0.909 | −1.521 | −1.011 | −1.011 | −0.373 | −1.778 | −1.301 | 0.160 |
| 2022-09 | −1.657 | −0.846 | −0.846 | −0.846 | −1.730 | −2.628 | −1.847 | −1.269 |
| 2023-09 | −2.400 | −2.214 | −1.637 | −1.637 | −2.521 | −2.430 | −2.400 | −1.589 |
| 2023-12 | 1.890 | 1.781 | 1.767 | 1.767 | 1.890 | 1.890 | 1.890 | 0.886 |

(excerpt of the 26 rows in Table VI; full table is in the source).

- Table VII — best strategy per metric and CPI regime. Sharpe, High period: best-mean **Pattern 1**, win-ratio-vs-B&H **Pattern 1**; Sharpe, Low period: best-mean **buy-and-hold**, win-ratio **Pattern 1**. Return: High best-mean B&H (win-ratio CM(D2)), Low best-mean B&H (win-ratio Pattern 1). Volatility: High best-mean B&H (win-ratio RG(S10)), Low both RG(S10). Max drawdown: High both RG(S5), Low best-mean B&H (win-ratio Pattern 1).
- Figs. 4–5 (Section V-C narrative) — LLM patterns drove the position to 0.0 during the Sep–Oct 2022 and Sep–Oct 2023 declines (avoiding depreciation), matched baselines during Jan/Mar 2023, but were **slow to react in June 2022** while CM(D2)/RG(S5) de-risked first.
- Table VIII (qualitative reasoning) — decline-oriented cause/effect mass across the top-15 relations: short-term persona class-1 6.896 vs class-2 0.853; medium 6.725 vs 0.792; long-term 5.540 vs 1.473 (the model is structurally pessimistic; consistent with the class-1 prediction counts in Tables III/V).

### Independently reproduced

not independently reproduced

### Negative evidence

- **Barely-above-chance accuracy:** best configuration 0.366 vs 0.333 chance (Table II) — the edge in raw classification is thin, and the paper reports **no confidence intervals or significance tests** for any accuracy or Sharpe figure (`data gap`).
- **Upside detection is weak:** class-2 (rise) precision 0.176–0.202 and recall 0.193–0.243 (Tables III, V); the strategies profit mostly by *not holding* during falls, not by calling rallies.
- **The ensemble's own ablation cuts both ways:** the long-term persona alone (0.378) beats the inter-persona ensemble (0.366) on accuracy (Fig. 2 vs Table II); the ensemble only wins on decline-F1 (Table IV). Persona diversity is therefore not uniformly beneficial — `source-reported` internal tension.
- **Sensitive ensemble degrades accuracy** (0.307–0.324, below chance) — Table II.
- **Regime conditionality:** buy-and-hold wins best-mean Sharpe in the Low-CPI period, and baselines win most return/volatility/MDD cells in Table VII; the paper's own conclusion states traditional strategies are better during declining CPI and in sharp downturns (Section VI).
- **Single macro episode:** High period is essentially Nov 2021 – Aug 2022 (one inflation scare) plus one month (Dec 2023); the regime claim rests on one 26-month window — `source-reported` scope, Scout-noted fragility.
- **Single model, single snapshot:** only `gpt-4-0613`; no second LLM, no prompt perturbation, no vendor-robustness test (`source-reported` absence).
- **No cost model:** fees/spread/slippage/turnover absent entirely → net performance unknown (`not stated in source`).
- **Non-standard metrics:** Sharpe has no risk-free rate, and return/volatility/drawdown are divided by average position size, which mechanically flatters low-average-position (defensive) strategies relative to a conventional calculation — normalization is `source-reported`, the bias direction is Scout interpretation.
- **Slow crash response:** June 2022 drawdown not captured by the LLM strategies (Section V-C) — `source-reported`.
- **Availability risk:** the pinned `gpt-4-0613` snapshot may be retired by the provider, threatening exact reproducibility — Scout-noted operational negative evidence.

## Falsification plan

Each threshold below is a `research-defined falsification threshold` unless the source explicitly states it; every operational choice not in the source is `research-proposed`.

1. **Point-in-time replication with named data vendors.** Rebuild indicators A–G from specified vendors with release-lag discipline; run the frozen prompt × 5 trials × 3 personas. *Fail if* the mode×mode accuracy 95% block-bootstrap lower bound over days is ≤ 0.333 (chance).
2. **Net-of-cost test (`research-proposed` cost grid: 2 / 5 / 10 bps per position change plus a no-cost control).** *Fail if* Pattern 1's full-sample Sharpe (computed conventionally, with a stated risk-free rate and without the ÷average-position normalization) is ≤ buy-and-hold under the mid cost point.
3. **Persona ablation.** Compare long-persona-alone vs mode-across-personas on both accuracy and F1(class 1). *Fail if* the inter-persona ensemble does not beat the best single persona on F1(class 1) — this would attribute the paper's headline to one persona, not ensemble diversity.
4. **Cross-model robustness (`research-proposed`).** Repeat with at least two current model families. *Fail if* class-1 F1 advantage over chance and the class-2 precision both collapse (class-2 precision < 0.20 in all models would mark the upside channel permanently dead).
5. **Regime out-of-sample.** Pre-register the CPI-High/CPI-Low rule *with publication lag* and test on a second inflation cycle. *Fail if* Pattern 1 − buy-and-hold Sharpe ≤ 0 in High regimes out-of-sample (the paper's central tradable claim).
6. **Parameter perturbation (`research-proposed`).** ±2%/±3% target, 5/15-day lookback, position step 0.1/0.4, `d_flat` 3/10. *Fail if* the sign of the High-regime Sharpe advantage flips anywhere in this grid (fragility = no robust effect).
7. **Placebo / label shuffle.** Shuffle daily classes within month. *Fail if* shuffled-label strategies produce Sharpe spreads comparable to the real ones (would indicate the position-lattice + evaluation normalization, not the LLM, generates the pattern).
8. **Competing explanation.** Test a pure "reduce equity beta when VIX + 30–10 spread rise" rule (the model's dominant Table VIII reasoning). *Fail if* that rule matches Pattern 1 — the LLM would then be an expensive encoding of two indicator thresholds.

Action on failure: keep the record research-only; do not promote to candidate pool.

## Crypto portability

**`unproven`.** The mechanism and evidence are entirely traditional-asset (US equities + US bonds driven by US rates/VIX/DXY/CPI); the source contains no crypto experiment, so this must not be labeled `direct`. A port would have to replace the 40/60 stock-bond portfolio with, e.g., a BTC/eth-neutral or BTC/stablecoin basket and the seven indicators with crypto-native analogues (funding, basis, OI, stablecoin flow) plus whatever macro prints still matter — all of that construction is `research-proposed` and untested. Crypto-specific risks: 24/7 sessions vs daily macro prints (signal staleness between releases), CPI publication lag becomes a larger fraction of a fast market, venue fragmentation and funding/liquidation mechanics do not exist in the source's long-only 0–1 position model, and LLM API latency/cost is trivial at daily cadence but prompt-sensitivity risk is higher in a market that never closes. Not authorization to trade anything.

## Limitations

- `underspecified`: indicator vendors/instruments, signal time-of-day/timezone, warm-up conventions, GPT-4 sampling parameters, missing-data handling.
- `not stated in source`: any transaction cost, spread, slippage, turnover, impact, or capacity treatment; any statistical significance test or confidence interval; peer-review status.
- `data gap`: point-in-time availability of the rate/VIX/DXY inputs; whether indicator A's construction has look-ahead; turnover implied by 0.2-step daily adjustments.
- `not independently reproduced`: every performance and accuracy number above is the authors' own report.
- Identification limits: one 26-month window spanning one inflation episode; single model snapshot; evaluation metrics normalized by average position and Sharpe without a risk-free rate, so cross-strategy comparisons are not conventional.
- Incremental-write check: this is a new family for the repository (persona-ensemble macro-timing of a stock-bond portfolio), not a duplicate of the finfluencer-twin, KOL-consensus, LLM-alpha-weighting, or prediction-market-LLM records (see Provenance dedup audit).

## Implementation status

`implementation_status: not-implemented`. Nothing in this record has been implemented or run in our research stack: no prompt was executed, no data was pulled, no backtest was reproduced, and no Qlib, Paper, Testnet, or Live stage has been touched. The source's own prompt/experiment repository (https://github.com/YoshiaAbe/llm_based_portfolio_management, cited in the paper, HTTP 200 verified 2026-09-22) exists but no commit was pinned and no claim here relies on its contents.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. Presence of this record in the staging repository does **not** mean: passed Research Intake Review, entered Hermes Wiki Brain, entered the production candidate pool, completed Qlib full-backtest validation, became a frozen survivor or leaderboard entry, profitable, validated alpha, approved for implementation, approved for paper trading, approved for testnet, or approved for live trading.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` — canonical schema contract read for this capture (specification, not a strategy claim). No other stable Hermes Wiki Brain page for this mechanism was verified; no Wiki link is fabricated here.

Related records in this repository (different sources, listed for retrieval only):

- `digital-twin-finfluencer-belief-elicitation-silent-region-cross-sectional-2026-09-06.md` — LLM persona replicas, but stock-level belief elicitation rather than macro-indicator portfolio timing.
- `llm-distilled-kol-consensus-capability-factor-aggregation-2026-09-18.md` — consensus aggregation over distilled crypto KOL capability factors.
- `prediction-market-llm-confidence-weighted-value-bet-2026-09-04.md` — point-in-time LLM posterior value betting on Polymarket (arXiv:2604.14199).
- `adaptive-alpha-weighting-ppo-llm-generated-alphas-2026-09-05.md` — PPO weighting of LLM-generated alpha formulas.
- `llm-news-probing-excess-return-sentiment-timing-2026-09-06.md` — news-sentiment timing without personas or ensembles.

## Sources

1. Yoshia Abe, Shuhei Matsuo, Ryoma Kondo, Ryohei Hisano. *"Leveraging Large Language Models for Institutional Portfolio Management: Persona-Based Ensembles."* arXiv:2411.19515v1 [cs.CE, cs.MA], submitted 29 November 2024 07:18:50 UTC, CC BY 4.0. https://arxiv.org/abs/2411.19515 — DOI: https://doi.org/10.48550/arXiv.2411.19515. (Sections I–VI; Tables I–VIII; Figs. 1–5.)
2. Full text (HTML) of the same v1 paper, used for the primary-source checksum of every number in this record: https://arxiv.org/html/2411.19515v1.
3. Experiment/prompt repository referenced by the paper (cited for traceability only; no empirical claim in this record is drawn from it): https://github.com/YoshiaAbe/llm_based_portfolio_management.
