---
schema: strategy-research-record-v1
title: "UQ-LOB: SNR-Gated Selective Prediction on Cryptocurrency Limit Order Books - Calibrated In-Context Uncertainty as a Trade-Only-When-Reliable Gate at 5/10/15 Second Horizons"
created: 2026-09-29
updated: 2026-09-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - limit-order-book
  - market-microstructure
  - high-frequency
  - uncertainty-quantification
  - selective-prediction
  - calibrated-regression
  - neural-processes
  - confidence-gating
  - kraken
  - deep-learning
status: research-only
confidence: high
source_as_of: 2026-09-25
sources:
  - "Manoharan, Derrick Gilchrist Edward; Linna, Eljas; Baltakys, Kestutis; Dong, Hao; Kanniainen, Juho, 'UQ-LOB: Uncertainty-Aware Limit Order Book Mid-Price Forecasting', arXiv:2609.31491v1 [cs.AI], submitted 25 Sep 2026 16:33:23 UTC, license CC BY 4.0. DOI: 10.48550/arXiv.2609.31491. https://arxiv.org/abs/2609.31491"
  - "Pinned primary full text read end to end: https://arxiv.org/html/2609.31491v1 (361606 bytes, SHA-256 3fe388886fed609475bee81470dae1e1d46b620efa268dc72e13597ee65cf080), retrieved 2026-09-29"
  - "arXiv metadata page read 2026-09-29: https://arxiv.org/abs/2609.31491"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Code-release claim with no locatable artifact: Section 4.1 states 'we release code, all label thresholds and scale values, and the dataset statistics needed to reconstruct the pipeline' and the Reproducibility Statement states 'We release the complete source code for the D-TABL encoder, both UQ heads, and the training and evaluation pipelines, including the context construction of Appendix A.5', yet a full href scan of the pinned HTML returns zero external repository or project URLs, the arXiv abstract page carries no Comments field, and there is no Code Availability section anywhere in the pinned version - so the code location is not stated in source and cannot be resolved from the primary source."
  - "Section 5.4 prose against its own printed numbers: the text claims that 'at the top decile the regression head matches or exceeds the classifier (0.57 versus 0.56 at 5 s, 0.55 versus 0.50 at 10 s, 0.51 versus 0.52 at 15 s)' while the 15 s pair it prints is 0.51 against 0.52, i.e. strictly below; the reconciling convention (tie tolerance, or rounding of the underlying unrounded means) is not stated in source."
  - "Headline gating gain has no gated chance comparator: the abstract and Section 5.2 headline a directional macro F1 rise of 0.11-0.15 at the top confidence decile, but Table 1's caption and Section 5.2 both state that the prior-matched random reference (0.337 / 0.350 / 0.362 at 5 / 10 / 15 s) 'is only valid for the full test set and rises under gating' and 'does not apply to the gated rows', and no gated null value is printed in any table - so the reported gain cannot be assessed against chance from the printed record."
  - "Metric switch between the abstract framing and the printed per-class table: the abstract states gating 'raises directional macro F1 ... at every horizon', while Table 8 shows the conventional three-class macro F1 at 5 s falling from 0.410 on the full test set to 0.357 at the top 50 percent and 0.353 at the top 30 percent before recovering to 0.381 at the top 10 percent and 0.413 at the top 1 percent, with stationary-class F1 collapsing 0.390 to 0.000; Section 5.2 documents the switch to a directional-only macro but the abstract does not disclose that the improvement holds only after the stationary class is excluded."
---

# UQ-LOB: SNR-Gated Selective Prediction on Cryptocurrency Limit Order Books - Calibrated In-Context Uncertainty as a Trade-Only-When-Reliable Gate at 5/10/15 Second Horizons

## Provenance

**Primary source (single, read in full).**

- Manoharan, Derrick Gilchrist Edward; Linna, Eljas; Baltakys, Kestutis; Dong, Hao; Kanniainen, Juho, *"UQ-LOB: Uncertainty-Aware Limit Order Book Mid-Price Forecasting"*, **arXiv:2609.31491v1 [cs.AI]**, submitted **Fri, 25 Sep 2026 16:33:23 UTC** (5,022 KB). arXiv-issued DOI `10.48550/arXiv.2609.31491`; the abstract page prints this as "arXiv-issued DOI via DataCite (pending registration)". Landing: https://arxiv.org/abs/2609.31491
- **Author list, exactly as printed on the HTML title block and in the arXiv API `<name>` order (5 authors, no ORCID printed):** 1. Derrick Gilchrist Edward Manoharan; 2. Eljas Linna; 3. Kestutis Baltakys; 4. Hao Dong; 5. Juho Kanniainen. Affiliation block for every author: Data Science Research Centre, Tampere University, Tampere, Finland; Manoharan carries the "Corresponding author" marker and a `derrick.edwardmanoharan@tuni.fi` address; Linna, Baltakys, Dong and Kanniainen each print an email address.
- **Version / date:** v1 only, 25 Sep 2026. No v2 existed at capture.
- **Subject class:** primary category `cs.AI` only; the abstract page prints `Subjects: Artificial Intelligence (cs.AI)` and the arXiv listing carries no `q-fin` cross-list.
- **License:** `CC BY 4.0`, printed in the HTML banner.
- **Publication / peer-review status:** **not stated in source.** There is no `Comments` field, no journal reference, no publisher DOI, and no peer-review statement on the abstract page. The AI Use Statement refers to "the ICLR 2027 AI Policy for Authors", which indicates an intended ICLR 2027 submission; **acceptance, venue and review outcome are not stated in source** and are recorded as `not stated in source`.
- **Pinned primary text:** https://arxiv.org/html/2609.31491v1 - **361,606 bytes**, SHA-256 `3fe388886fed609475bee81470dae1e1d46b620efa268dc72e13597ee65cf080`, retrieved 2026-09-29 and read end to end (text-extracted to 71,530 characters / 2,346 lines): Abstract, Sections 1-7, Ethics Statement, Reproducibility Statement, AI Use Statement, the full References list, Appendix A.1-A.7 (Algorithm 1), Appendix B.1-B.4, Appendix C, Tables 1-8 and the captions of Figures 1-10. Every quantitative claim below is transcribed from that pinned text with section/table/figure provenance.
- **PDF:** https://arxiv.org/pdf/2609.31491 was not downloaded this run; a PDF checksum is therefore a `data gap`. The abstract landing page (41,891 bytes) was read separately for the submission history and subject metadata.
- **Code:** the Reproducibility Statement and Section 4.1 both assert a code release, but the pinned HTML contains **no repository URL of any kind** (verified by a full `href` scan that returns only arXiv-internal, LaTeXML, font and funder links) and the abstract page has no Comments field. **Artifact location: not stated in source.**
- **Data:** Section 4.1 states the raw Level-2/Level-3 order-book data "cannot be redistributed" because no data-sharing agreement is in place with the exchange. Raw data: `data gap` for any independent reproduction.
- **Sample / universe / cost / status anchors (all verified against the pinned text):** data span **November 2025 to February 2026**, seven USD-quoted assets on **Kraken** (BTC, ETH, SOL, LTC, DOGE, SUI, TAO), approximately **5.2 billion events over 600 asset-days** (Appendix B Table 6 sums to 5.196 billion events and 600 days, research-computed); splits **train through 18 Jan 2026 / validation 19-31 Jan 2026 / test 1-15 Feb 2026**, described as "about 68%, 15% and 17% of asset-days"; **no transaction-cost, fee, slippage, spread or fill model exists anywhere in the paper** - see Execution assumptions and Evidence.

**Repository dedup (step 5, hidden-inclusive, run 2026-09-29).** `rg -uuu` over the entire checkout including `.git`, `.mimo-worktrees`, `.agents`, `.hermes` and `coverage_manifest.csv` for `2609.31491`, `UQ-LOB`, `Manoharan`, `Tampere` and `2609.31491` variants returned **0 hits**; `Kanniainen` returned **3 hits, all inside `temporal-kolmogorov-arnold-networks-high-frequency-lob-alpha-decay-2026-09-02.md`**, where the name occurs only as a co-author of the cited FI-2010 benchmark reference (Ntakaris, Magris, Kanniainen, Gabbouj, Iosifidis, *Journal of Forecasting* 37(8), 2018) - a different source identity. `selective-prediction` / `confidence-gat*` hits exist in seven unrelated records (LLM prediction-market, 0DTE, gold-futures, equity-ranker and meta-learning sources), all with different canonical source identities. `coverage_manifest.csv` (5,808 lines) contains 0 hits for `31491` and 0 for `UQ-LOB|Manoharan|Tampere`. `git log --oneline -20` was used only as a convenience glance, not as dedup.

**Four-axis distinction from the nearest existing records (source identity differs in every pair):**

- `temporal-kolmogorov-arnold-networks-high-frequency-lob-alpha-decay-2026-09-02.md` - source `arXiv:2601.02310` (Ahmad Makinde) on FI-2010, 5 Finnish equities, NASDAQ Nordic, June 2010; different paper, different venue, different universe, no uncertainty gate.
- `explainable-lob-microstructure-universal-feature-crypto-perp-2026-09-08.md` - source `arXiv:2602.00776` (Bieganowski and Ślepaczuk); a feature-library / interpretability study with CatBoost, no calibrated UQ head and no selective-prediction gate.
- `two-level-uncertainty-cross-sectional-ranker-regime-trust-gate-tail-cap-2026-09-05.md` - source `arXiv:2603.13252` (Ursina Sanderink); uncertainty gating applied to a **daily equity cross-sectional ranker** with epistemic (DEUP) uncertainty and a position-level tail cap; different horizon (daily vs 5-15 s), different market (US equity vs crypto LOB), different uncertainty class (epistemic vs aleatoric/in-context).
- `crypto-day-night-session-lagged-reversal-kraken-btc-eth-cutoff-search-2026-09-27.md` - shares the **Kraken venue** only; a session-boundary lagged-reversal study on candles, not an order-book forecasting record, and a different source identity.

## Economic mechanism

### Source-reported

The authors' stated rationale, without upgrading it to fact:

- The limit order book is "the mechanism through which price discovery takes place in most electronic markets"; thousands of events per second make it carry "microstructural signal about the next few seconds of price formation that predictive models seek to exploit" (Section 1).
- Deep LOB forecasters are "overwhelmingly point predictors: they emit a direction or a displacement, but not how much that output should be trusted". Because "predictability varies sharply across market regimes and even across consecutive windows, and every action incurs fees and slippage, the practically relevant question is rarely 'which way will the price move?' but 'is this forecast reliable enough to act on?'" (Section 1). This is the selective-prediction / reject-option framing of Chow (1970), El-Yaniv and Wiener (2010) and Geifman and El-Yaniv (2017).
- The proposed remedy is input-dependent (**aleatoric**) uncertainty that is calibrated: "an interval claimed to cover 68% of outcomes should do so empirically" (Section 1). The head conditions each forecast on a context set of recently completed windows whose outcomes are already realised, "so that the forecast can adapt to the prevailing regime without any gradient update" (Section 1, Section 3.2).
- The scalar gate is the predicted signal-to-noise ratio `SNR = |mu|/sigma`: "a large predicted displacement paired with a small predicted uncertainty is both worth acting on and sharply estimated" (Section 3.5).
- Distinction the authors draw against prior work: BDLOB (Zhang et al., 2018) and Magris et al. (2023) derive uncertainty from a distribution over network weights (epistemic, multiple stochastic passes at inference), whereas this head "predicts input-dependent (aleatoric) uncertainty in a single forward pass and conditions it on recently realised outcomes" (Section 2).
- The authors state explicitly that **no economic return channel is claimed**: "We evaluate directional reliability, not profitability; a trading simulation with realistic execution and fees is required before any claim about returns" (Section 7), and the Ethics Statement states "We make no claim of profitability".

### Research interpretation

Stated as falsifiable hypotheses, with component roles separated:

```text
Representation: D-TABL encoder (three bilinear layers + temporal-attention TABL layer)
                over 512-event windows of tokenised L2/L3 book events
Distribution:   UQ head emitting N(mu, sigma^2) over the tick displacement at t+h
Regime input:   in-context set of the C = 15 most recent windows whose labels are
                fully realised by t (causal constraint, Equation 1)
Gate:           retain only predictions whose SNR = |mu|/sigma exceeds a percentile cut
                (the "trade only when reliable" rule)
Risk / exit:    NONE in the source - no stop, no sizing, no exit rule exists
```

- **H1 (confidence ranking - the mechanism the source actually tests).** Predicted SNR is monotonically related to realised directional accuracy, so restricting evaluation - and, research-proposed, trading - to the top SNR tier raises directional skill above what the same model achieves on the full test set. This is an *informational* mechanism: microstructure order-flow information propagating over 5-15 seconds, and the model knowing when it has it.
- **H2 (in-context regime adaptation).** Because the head re-reads the 15 most recently realised windows at every prediction, sigma responds to a volatility/regime shift without retraining; this is the specific reason the source expects gating to keep working when train and test class balances diverge (the BTC-USD case). If shuffling or removing the context set leaves the gating gain intact, H2 is false.
- **H3 (selectivity economics - research-proposed bridge, NOT source-reported).** Trading fewer, higher-confidence events raises per-trade edge enough to clear a crypto taker fee plus half-spread at 5-15 s horizons. **The source never tests this**; it is the load-bearing untested link between the reported F1 numbers and any tradable claim, and it is the primary target of the falsification plan below.
- **No market-friction, risk-premium, liquidity-provision or behavioral channel is claimed by the source.** The hypothesised edge is purely predictive/informational. A correlation-plus-abstention construction is not a mechanism by itself; if H1 does not survive the chance-comparator and plain-encoder ablations in F2-F4, nothing is left.

## Signal

**Source-reported construction (fully specified where the source specifies it)**

**Formation timestamp.** The event stream is segmented into **non-overlapping windows of `L = 512` events** (Section 4.2). `t` is the timestamp of the last event of a window, i.e. the model's present moment (Section 3.1). The prediction is produced at `t`.

**Labels.** To reflect execution latency, the start price is the mid-price at the **first event at or after `t + d`**, with fixed latency **`d = 0.0005 s`** (Table 5, Appendix A.7.1). The end price is the **mean mid-price over the `k = 10` events immediately at or before `t_start + h`** (Equation 14); if fewer than `k` events are available the example is discarded rather than smoothed over a shorter window. Horizons computed in Appendix B: `h in {5, 10, 15, 30} s`; **experiments use `h in {5, 10, 15} s`**.

- Regression target: `y_h(t) = p_end - p_start` in ticks (Section 3.1).
- Classification label: `tau_h^LR = alpha * sigma_h^LR` with **`alpha = 0.25` throughout**, `sigma_h^LR` the standard deviation of the mid-price log-return over `h` computed on the **training split only**, converted to ticks at the window's price level as `delta_h(t) = p_start * (exp(tau_h^LR) - 1)`; `up` if `y >= delta`, `down` if `y <= -delta`, `stationary` otherwise (Equations 15-16, Appendix A.7.2).
- Regression-to-class comparison uses a calibrated multiplier `k*` on the threshold, selected on the held-out **calibration half of the validation period** by matching the predicted stationary proportion to the true one (Equation 17, Appendix A.7.3).

**Confidence score.** UQ-regression: `SNR = |mu| / sigma`. UQ-classification: `max_c p_c` (Section 3.5).

**Gating.** "Gating at percentile `q` retains the `(100 - q)%` most confident predictions of each asset-horizon test set and evaluates only on those; `q = 0` is the full test set" (Section 3.5). Reported tiers: `q = 0, 10, ..., 90` (Table 1) and `Top 50% / 30% / 10% / 5% / 1%` (Table 2, Table 8).

**Causality of the conditioning set.** Equation 1 / Algorithm 1: a context window ending at `t_i^c` is admissible only if its label realisation time `e_i^c = t_i^c + d + h <= t`. The paper states this "is strictly stronger than merely requiring the context and target input windows not to overlap: it also excludes context windows whose label horizon runs past `t`, which would leak future price information into the prediction", and that "the same construction is used at training, validation and test time" (Section 3.2, Appendix A.5).

**Input features (Section 4.2, Appendix A.6).** Each event becomes a discrete token from a vocabulary `|V| = 439` built from five categorical attributes (event type, side, discretised volume, discretised price distance from the opposing best quote, simultaneity flag); events deeper than `L_max = 10` levels are discarded. Seven continuous features per event: log inter-event time, log tick distance from the opposing best quote, log relative volume, depth-normalised flow imbalance `DNFI = (dQ1_b - dQ1_a) / (Q1_b + Q1_a)`, cumulative sums of DNFI over the preceding 50 and 200 events, and queue imbalance `QI = (Q1_b - Q1_a) / (Q1_b + Q1_a)` (Equation 10, building on Cont, Kukanov and Stoikov 2014). The token is embedded to 8 dimensions and concatenated with the 7 continuous features to give `X in R^(15 x 512)` (Equation 13).

**Architecture and training (Section 3.3, 3.4, 4.3, Appendices A.1-A.4).** D-TABL encoder (three bilinear layers + temporal-attention layer) pretrained on the three-class label, separately for each of the **21 asset-horizon pairs**; the UQ head is then attached and the whole model fine-tuned end-to-end. Head: shared linear projection, context encoder (3-layer GELU MLP), self-attention over the 15 context points, cross-attention readout, 5-layer GELU MLP decoder. UQ-regression loss `L = 1.0*NLL + 0.1*WMAE + 0.5*dir + 0.5*calib` (Equation 5), with `p = 4`, `w_max = 40` (Equation 6), directional margin `m = 1.0` (Equation 7) and `B = 3` calibration bins targeting `E|Z| = sqrt(2/pi)` (Equation 8); variance `sigma^2 = y_ref^2 * softplus(nu) + eps`, `eps = 1e-8` (Equation 4). UQ-classification uses class-weighted cross-entropy with `w_c proportional to 1/f_c` normalised to sum to 3. AdamW, learning rates `(1e-5, 5e-5)` for encoder/head, weight decay 0.0, linear warmup 10k steps, cosine restarts `T0 = 15k, T_mult = 2, eta_min = 1e-5, gamma = 0.5`, max 15 epochs, early stopping on validation `R_w^2` (regression) or macro F1 (classification), **random seed train/test `42 / 999` (single seed)**. Parameter count (Table 4): encoder 268,356 + projection 24,704 + trunk 766,784 + decoder 165,378 (regression) or 165,731 (classification) = **1,225,222 / 1,225,575 total** (sums verified research-computed; Section 4.3 rounds these to 0.27M / 0.79M / 0.17M / 1.23M). Hardware: single NVIDIA GH200; Section 4.3 states ~210 GPU-hours for all 42 UQ models, Appendix A.3 adds ~78.75 GPU-hours of encoder pretraining for ~289 GPU-hours total (78.75 + 210 = 288.75, research-computed).

**Other Table 5 hyperparameters.** Window `L = 512`, vocabulary 439, embedding dim 8, 7 continuous features, `L_max = 10`, latency `d = 0.0005 s`, end-price smoothing `k = 10`, threshold multiplier `alpha = 0.25`, context size `C = 15`, instances per batch 16, projection dim 128, attention dim 256, attention heads 4, context-encoder depth 3, decoder depth 5, `B = 3`, `eps = 1e-8`. Values shared across assets and horizons were "fixed a priori or chosen on the validation split of BTC-USD at 5 s and then held fixed for all other pairs".

**Entry / exit / sizing**

- **Entry: NOT specified by the source.** The paper contains **no trading rule of any kind** - no entry trigger, no order type, no side-selection rule, no fill assumption.
- **Exit / holding period: NOT specified by the source.** The evaluation horizon `h in {5, 10, 15} s` bounds the prediction target but is never declared as a holding period.
- **Position sizing: NOT specified by the source** (`data gap`; the only "position sizing" string in the paper belongs to a cited prior work, Section 2).
- **Research-proposed operationalization (clearly labelled, not source-reported).** For falsification only: at time `t`, if `SNR(t) >= theta` where `theta` is a percentile cut **frozen on the validation period**, take the first marketable quote after `t + 0.5 ms` in the sign of `mu` for one unit, and flatten at `t_start + h`; no re-entry within the same window; `theta` and `h` are never re-tuned on test. **Every element of this paragraph is research-proposed.** The signal is otherwise **fully specified** for the forecasting task and **underspecified** for trading, because the trading layer is absent from the source.

## Required data

- **Instrument / universe:** seven USD-quoted spot assets on Kraken: **BTC, ETH, SOL, LTC, DOGE, SUI, TAO** (Section 4.1). Spot only - no perpetual, no futures, no options.
- **Venue / market type:** Kraken cryptocurrency exchange, **public market data API**, Level-2 **and Level-3** order-book data (Section 4.1). Single venue.
- **Sample period:** **November 2025 to February 2026**; approximately **5.2 billion events over 600 asset-days** (Section 4.1). Appendix B Table 6 per asset (source-reported): BTC 94 days / 1.254 B events / 156 events per s / 6.42 ms mean inter-event time / tick $0.10; ETH 70 / 0.903 B / 151 / 6.61 ms / $0.01; DOGE 97 / 1.124 B / 134 / 7.46 ms / 1e-7; SOL 78 / 0.539 B / 80 / 12.50 ms / $0.01; TAO 84 / 0.577 B / 80 / 12.58 ms / 0.0001; SUI 94 / 0.523 B / 64 / 15.52 ms / 0.0001; LTC 83 / 0.276 B / 39 / 25.97 ms / $0.01. Research-computed checks: events sum to **5.196 billion** against the stated "approximately 5.2 billion"; days sum to exactly **600**.
- **Timeframe / bar convention:** **no bars** - the raw event stream is windowed into non-overlapping **512-event** segments; horizons are wall-clock (5/10/15 s) but measured in event time internally.
- **Fields used:** event type, side, discretised volume, discretised price distance from the opposing best quote, simultaneity flag, inter-event time, tick distance, relative volume, best-level bid/ask queue sizes (for DNFI and QI), mid-price. **Not used:** trades/aggressor side, funding, mark/index/basis, open interest, options surface, order-book snapshots beyond 10 levels, on-chain or sentiment fields.
- **Point-in-time / availability:** causal context constraint `e_i^c <= t` (Equation 1, Algorithm 1); label thresholds `sigma_h^LR`, `tau_h^LR` and scales `y_ref` computed on the **training split only** (Appendix B.4); validation split into two equal halves for model selection and for `k*` calibration; test strictly out-of-sample and chronologically after both.
- **Timestamps / timezone:** the paper gives event timestamps at sub-second precision (mean inter-event times 6.42-25.97 ms) but **states no timezone, clock source or session convention** - `data gap`.
- **Missing-data handling:** examples with fewer than `k = 10` events available before `t_end` are **discarded**; events deeper than `L_max = 10` are **discarded**; no imputation is described. Class-balance and drift diagnostics are reported per asset and horizon (Figures 7-8, Appendix B.2-B.3).
- **Funding / fee / spread needs:** the paper models none. A tradable reproduction would additionally need Kraken's published maker/taker schedule, top-of-book quotes for a realised spread series, and (if ported to perps) the funding time series - **all absent from the source**.

## Execution assumptions

Determination made by reading Sections 3.1, 4.1, 5.3, 7, the Ethics Statement, Appendix A.7.1 and Table 5 of the pinned text, plus a whole-document word scan of the extracted 71,530-character text.

**What the source actually assumes:**

- **Signal-to-order timing / latency:** a **fixed `d = 0.0005 s` (0.5 ms)** delay is inserted between the window end `t` and the label's start price, described as "to reflect execution latency ... entering a position incurs a small, fixed latency `d` before it can be realised" (Section 3.1, Appendix A.7.1, Table 5). This is a **label anchor**, not an execution model; no venue, colocation or network justification for 0.5 ms is given, and no latency distribution, jitter or order-round-trip time appears anywhere.
- **Reference price:** mid-price throughout (start and end prices are mid-prices), not a trade price and not a quote you could hit.

**What the source does not assume (all `data gap`, never zero):** a whole-document scan returns **zero modelled occurrences** of transaction cost, commission, maker/taker fee schedule, slippage model, bid-ask spread series, market impact, order type, fill model, participation rate, capacity, leverage, margin, borrow, inventory, funding, liquidation, turnover, Sharpe, drawdown, PnL or backtest. The words `fees`, `slippage` and `transaction cost` appear only as prose motivation at Section 1 ("every action incurs fees and slippage"), Section 3.5 ("after fees, are the only ones a trader can profit from"), Section 5.3 ("most valuable after transaction costs") and Section 7 ("a trading simulation with realistic execution and fees is required"); **no number accompanies any of them**. The string "Sharpe" does not occur (the only match is the unrelated word "sharpen"). The single `funding` occurrence is the arXiv footer "Major funding support from".

**Explicit source admission:** Section 7, "Economic evaluation": *"We evaluate directional reliability, not profitability; a trading simulation with realistic execution and fees is required before any claim about returns."* Ethics Statement: *"We make no claim of profitability."*

**Our position:** because the source specifies no entry, no exit, no sizing and no cost, **every operational trading choice required to turn this into a strategy is research-proposed**, and the record is therefore a falsifiable hypothesis capture, not a backtest.

## Evidence

### Source-reported

All figures below are source-reported, transcribed from the pinned `arXiv:2609.31491v1` HTML with provenance, and **none has been independently reproduced**.

**Table 1 - directional macro F1 (mean of down and up F1, stationary excluded), pooled over the seven assets, as a function of the retained confidence percentile.** Row `0` = full test set; row `90` = most confident 10 percent.

| Horizon | Head | Gate q=0 F1(down) | F1(up) | Mean | Gate q=90 F1(down) | F1(up) | Mean |
|---|---|---|---|---|---|---|---|
| 5 s | UQ-regression (SNR) | 0.45 | 0.39 | **0.42** | 0.60 | 0.54 | **0.57** |
| 5 s | UQ-classification (softmax) | 0.48 | 0.42 | **0.45** | 0.61 | 0.51 | **0.56** |
| 10 s | UQ-regression (SNR) | 0.43 | 0.39 | **0.41** | 0.57 | 0.53 | **0.55** |
| 10 s | UQ-classification (softmax) | 0.46 | 0.43 | **0.45** | 0.55 | 0.46 | **0.50** |
| 15 s | UQ-regression (SNR) | 0.44 | 0.36 | **0.40** | 0.57 | 0.46 | **0.51** |
| 15 s | UQ-classification (softmax) | 0.47 | 0.42 | **0.45** | 0.57 | 0.47 | **0.52** |

- Prior-matched random-classifier reference on the **full test set only** (Table 1 caption): **0.337 at 5 s** (`p_stat = 0.326`), **0.350 at 10 s** (`p_stat = 0.300`), **0.362 at 15 s** (`p_stat = 0.276`); the caption states the formula `(1 - p_stat)/2` and that it "does not apply to the gated rows". Research-computed check: `(1-0.326)/2 = 0.337`, `(1-0.300)/2 = 0.350`, `(1-0.276)/2 = 0.362` - exact.
- Abstract / Section 5.2 / Section 6 headline: gating by SNR raises directional macro F1 by **0.11-0.15** at the top confidence decile and **0.05-0.11** for the classification head under softmax gating, "at every horizon". Research-computed from the printed means: regression gains **+0.15 / +0.14 / +0.11** (5/10/15 s) and classification gains **+0.11 / +0.05 / +0.07** - both consistent with the stated ranges.
- Intermediate tiers (Table 1, UQ-regression means): 5 s `0.42 -> 0.44 -> 0.46 -> 0.48 -> 0.49 -> 0.50 -> 0.51 -> 0.52 -> 0.54 -> 0.57` for `q = 0,10,...,90`; 10 s `0.41 -> 0.43 -> 0.45 -> 0.47 -> 0.48 -> 0.49 -> 0.50 -> 0.51 -> 0.52 -> 0.55`; 15 s `0.40 -> 0.42 -> 0.44 -> 0.46 -> 0.47 -> 0.47 -> 0.48 -> 0.48 -> 0.49 -> 0.51`.
- Section 5.4 (regression vs classification): on the full test set the dedicated classifier is stronger by **0.03-0.05** (0.45 vs 0.40-0.42); at the top decile the regression head "matches or exceeds" it at **0.57 vs 0.56 (5 s)**, **0.55 vs 0.50 (10 s)**, **0.51 vs 0.52 (15 s)**; gating gain is larger for SNR than softmax "at every horizon (+0.11 to +0.15 versus +0.05 to +0.11)".
- Section 5.2: three-class accuracy under SNR gating for BTC-USD rises "from about 45% to 57% at 5 s" (Figure 10); magnitude-weighted `R_w^2` for BTC-USD rises "from roughly 9% on the full 5 s test set to over 50% in the top decile" (Figure 4). UQ-classification, softmax gating, BTC-USD: macro F1 "0.47 on the full 5 s test set to nearly 0.68 in the top decile", accuracy "from about 48% to 68%" (Figures 9-10).
- Section 5.2 caveats printed by the source: both heads score lower on the **up** class than the **down** class at every tier, "as the asymmetry is shared, it reflects the test period rather than either head"; and "since the prior-matched reference rises with the gate ... the top-decile values should not be read against the full-set reference of 0.34-0.36".

**Table 2 - per-class directional F1 of UQ-regression restricted to large true moves (`|y| > q67`, the upper tercile of true displacement magnitude), by SNR tier** (a prior-matched random classifier scores about 0.5 here by construction, per Section 5.3):

| H | Top 50% down / up | Top 30% | Top 10% | Top 5% | Top 1% |
|---|---|---|---|---|---|
| 5 s | 0.69 / 0.63 | 0.73 / 0.67 | 0.81 / 0.75 | 0.84 / 0.79 | **0.88 / 0.83** |
| 10 s | 0.65 / 0.59 | 0.68 / 0.63 | 0.75 / 0.70 | 0.78 / 0.73 | 0.85 / 0.78 |
| 15 s | 0.65 / 0.52 | 0.68 / 0.53 | 0.74 / 0.59 | 0.76 / 0.61 | 0.81 / 0.68 |

The abstract's "directional F1 of 0.88 (down) and 0.83 (up) at the 5-second horizon" is the top-1 percent 5 s row. Research-computed: the 5 s down-class gain from top 50 percent to top 1 percent is **+0.19** and the up-class gain is **+0.20**.

**Table 3 - calibration of UQ-regression (full test set, pooled over assets):**

| Metric | 5 s | 10 s | 15 s |
|---|---|---|---|
| Coverage 68 (nominal 0.68) | 0.682 | 0.682 | 0.681 |
| Coverage 95 (nominal 0.95) | 0.904 | 0.904 | 0.907 |
| Calibration error `|cov68 - 0.68|` | 0.048 | 0.048 | 0.045 |
| NLPD | 5.278 | 5.586 | 5.778 |

Section 5.1: "Empirical 68% coverage is 68.1-68.2%, essentially nominal ... The 95% interval, however, covers only 90.4-90.7% of outcomes: the residual distribution is heavier tailed than a Gaussian."

**Table 8 (Appendix C) - UQ-regression per-class F1 by SNR tier at 5 s, pooled over assets** (the source's own decomposition showing why three-class macro F1 is unsuitable under gating):

| Metric | Top 100% | Top 50% | Top 30% | Top 10% | Top 1% |
|---|---|---|---|---|---|
| F1 (Down) | 0.447 | 0.526 | 0.549 | 0.598 | 0.640 |
| F1 (Up) | 0.393 | 0.477 | 0.499 | 0.544 | 0.598 |
| F1 (Stationary) | 0.390 | 0.067 | 0.012 | 0.000 | 0.000 |
| Macro F1 (three-class) | 0.410 | 0.357 | 0.353 | 0.381 | 0.413 |

Research-computed row means reproduce the printed macro column exactly (0.410 / 0.3567 / 0.3533 / 0.3807 / 0.4127).

**Table 4 / Section 4.3 - parameter counts:** 268,356 encoder + 24,704 projection + 766,784 trunk + 165,378 (regression) or 165,731 (classification) = **1,225,222 / 1,225,575**, rounded in Section 4.3 to 0.27M / 0.79M / 0.17M / 1.23M (all sums research-computed and exact).

**Table 5 hyperparameters, Table 6 dataset statistics, Table 7 per-asset threshold and scale values:** transcribed in the Signal and Required data sections above. Table 7 examples (training split): BTC `sigma_5s = 1.82e-04`, `tau_5s = 4.50e-05`, `y_ref = 155` ticks; TAO `sigma_5s = 5.01e-04`, `tau_5s = 1.25e-04`, `y_ref = 628`; LTC `y_ref = 2` ticks at 5/10/15 s and 3 at 30 s.

**Distribution shift actually present in the headline sample (Section 7, Appendix B.2):** for BTC-USD the training split assigns roughly **70%** of windows to the stationary class at 5 s while the test split assigns **27%**; at 10 s and 15 s train/test stationary shares are **64% vs 19%** and **57% vs 15%**. Appendix B.3: "BTC-USD, the most liquid asset in the dataset, drifts most, reflecting a shift in volatility regime between the training and test windows ... This shift is the main source of distribution mismatch in our evaluation."

**Scale of the evaluation:** 21 asset-horizon pairs x 10 gating tiers x 2 heads in Table 1 alone; test period **1-15 February 2026** (15 calendar days); single seed (Table 5: train/test seeds 42 / 999).

**Cost / profitability:** no cost, no return, no risk statistic of any kind is reported. **`data gap`, never zero.**

### Independently reproduced

not independently reproduced

### Negative evidence

1. **The source explicitly disclaims profitability.** Section 7: "We evaluate directional reliability, not profitability; a trading simulation with realistic execution and fees is required before any claim about returns." Ethics Statement: "We make no claim of profitability." There is therefore **no economic evidence of any kind** attached to the mechanism.
2. **Zero cost model.** Whole-document scan of the pinned text returns no transaction cost, commission, fee schedule, slippage model, bid-ask series, spread, market impact, order type, fill model, participation or capacity value; `Sharpe`, `drawdown`, `turnover`, `backtest`, `PnL`, `inventory`, `borrow`, `leverage`, `margin` and `liquidation` do not occur. All are `data gap` and must never be read as zero.
3. **Before gating, the forecaster is barely above its own chance reference.** Table 1 full-test-set directional macro F1 is **0.42 / 0.41 / 0.40** (UQ-regression) against prior-matched chance **0.337 / 0.350 / 0.362** - absolute margins of about +0.08 / +0.06 / +0.04 before the gate is applied.
4. **The headline gated gain has no valid chance comparator.** Table 1's caption and Section 5.2 state the prior-matched reference "is only valid for the full test set and rises under gating" and "does not apply to the gated rows", yet no gated null is printed anywhere - so `0.57 vs 0.42` cannot be compared against what a random gated classifier would score.
5. **The improvement is metric-dependent.** Table 8 shows conventional three-class macro F1 *falling* under gating from 0.410 to 0.357 (top 50 percent) and 0.353 (top 30 percent) before recovering to 0.381 and 0.413, with stationary-class F1 collapsing 0.390 -> 0.067 -> 0.012 -> 0.000. The gain appears only after the stationary class is excluded from the metric.
6. **Single seed, no error bars.** Table 5 fixes train/test seeds at 42/999; Section 7 lists "multi-seed error bars" among the missing analyses. Every F1 and calibration number in the paper is one draw.
7. **No baseline against the cheap alternative.** Section 7: "a comparison against weight-space uncertainty (MC dropout, deep ensembles) and against gating the base encoder's own softmax ... would sharpen the attribution of the gains to in-context conditioning." Gating a plain classifier's softmax is the obvious zero-cost control and it is absent - so the marginal value of the UQ head over "just gate the existing model" is unestablished.
8. **No ablation of the four loss terms or of the context set.** Section 7 lists both as missing, so the attribution of the gain to *in-context conditioning* (H2) rather than to the heteroscedastic NLL / WMAE / directional / calibration terms is unproven.
9. **Fifteen-day test window, one venue, one regime episode.** Test = 1-15 Feb 2026 on Kraken only. Section 7: "a longer test period spanning several regimes is needed to establish robustness."
10. **Large regime shift inside the headline sample.** BTC-USD stationary share 70% (train) vs 27% (test) at 5 s, 64% vs 19% at 10 s, 57% vs 15% at 15 s; Appendix B.3 says BTC "drifts most" and calls it "the main source of distribution mismatch". The gating result is being measured across a volatility-regime change that is not independently replicated.
11. **Weak baseline fit.** Figure 4 / Section 5.2: BTC-USD magnitude-weighted `R_w^2` on the full 5 s test set is "roughly 9%". The underlying displacement forecast explains little before gating.
12. **Tail miscalibration.** Table 3 / Section 5.1: the nominal 95% interval covers only **90.4-90.7%**, because "Equation 8 constrains only the first absolute moment of the standardised residual, so it enforces the one-sigma level but not the tails" (Section 7). Any sizing or threshold rule driven by `sigma` inherits this under-coverage.
13. **Calibration numbers are reported without a baseline.** NLPD 5.278 / 5.586 / 5.778 and calibration error 0.048 / 0.048 / 0.045 (Table 3) have no comparator model, so "near-nominal" cannot be ranked against anything.
14. **Persistent up-class weakness.** Table 1: `F1(up) < F1(down)` at every tier and every horizon (e.g. 0.36 vs 0.44 at 15 s full set). The source attributes this to the test period and does not resolve it.
15. **Gate percentile is swept on the test set.** Section 3.5 defines gating as an evaluation protocol over `q = 0..90` and the "top decile" headline is read off that sweep; **no rule for selecting `q` out of sample is specified anywhere**, so the reported top-decile numbers are a best-point on a test-set curve.
16. **An extra fitted quantity sits in the evaluation plumbing.** Equation 17: the regression head's predictions are converted to classes using a multiplier `k*` chosen by sweeping on a validation half to match stationary proportions - one more tuned parameter between raw output and the reported F1.
17. **Raw data cannot be redistributed.** Section 4.1: no data-sharing agreement with Kraken, so the exact sample is unavailable; only thresholds, scales and summary statistics are said to be released.
18. **The claimed code release is not locatable.** Full `href` scan of the pinned HTML returns no repository URL; the abstract page has no Comments field; there is no Code Availability section. Reproduction therefore has neither the data nor an addressable artifact.
19. **Per-asset, per-horizon models.** 21 separately trained models on one venue (Section 4.3, Section 7 "Scope"); no cross-asset pooling, no cross-venue test, no evidence the gate transfers.
20. **Economic relevance is asserted without any cost quantity.** Section 3.5 states large moves are "the only ones a trader can profit from" and Section 5.3 calls large 5-second moves "exactly the regime ... in which a reliable signal is most valuable after transaction costs", yet no cost, edge or breakeven number exists in the paper - the motivation is economic while the evidence is purely statistical.
21. **Adjacency caveat.** This repository already holds several crypto/high-frequency LOB records built on different sources; none of them is a replication of this paper. **None identified in the reviewed sources beyond the 20 items above; absence is not evidence of no negative result.**

## Falsification plan

All thresholds below are **research-defined falsification thresholds** (the source declares none), and every operational trading rule is **research-proposed**. Data: Kraken-class L2/L3 event streams for the same seven USD pairs (plus one second venue for F13), same splits, same released label thresholds.

- **F1 - Printed-value reproduction gate.** Reproduce the six Table 1 row-0 and row-90 directional macro F1 values (0.42 / 0.45 / 0.41 / 0.45 / 0.40 / 0.45 and 0.57 / 0.56 / 0.55 / 0.50 / 0.51 / 0.52) to within **+/-0.01** on the published splits using the released thresholds and scales. **Failure** = any 4 of 6 cells outside tolerance -> the record's source-reported numbers are treated as unreproducible and nothing downstream proceeds.
- **F2 - Gated-chance comparator gate.** Recompute the prior-matched random reference **on each gated subset** (as Table 1's caption requires but never prints): `(1 - p_stat_gated)/2` with `p_stat` measured inside the retained subset. Require the top-decile gain over *that* gated chance to be **>= +0.05** directional macro F1 at **2 of 3 horizons**. **Failure** = the headline gain is a class-composition artifact -> withdraw H1.
- **F3 - Plain-encoder softmax-gating ablation (the missing baseline).** Gate the **pretrained D-TABL encoder's own three-class softmax** at the identical retained fraction, no UQ head. Require UQ-SNR gating to beat it by **>= +0.03** directional macro F1 at **2 of 3 horizons**. **Failure** = the cheap alternative suffices; the UQ head adds no gating value -> withdraw the mechanism claim.
- **F4 - Weight-space UQ baseline.** MC-dropout and a 5-member deep ensemble on the same encoder, gated at the identical retained fraction; same **>= +0.03 / 2-of-3** rule as F3. **Failure** = aleatoric in-context UQ is not superior to epistemic UQ -> narrow the claim to "gating works", not "this head is needed".
- **F5 - In-context conditioning ablation (tests H2).** Replace the context set with (a) `C = 0` (no context) and (b) `C = 15` with context labels circularly shuffled within the asset. Require the top-decile F1 to drop by **>= 0.02** under both relative to the full head. **Failure** = the gain comes from the loss terms, not from conditioning on realised outcomes -> withdraw H2.
- **F6 - Per-trade cost ladder (tests H3).** Convert the frozen gate into the research-proposed one-unit long/short rule (Signal section) and deduct a two-way cost of **{0, 1, 2, 5, 10, 20} bp per side** on top of a one-tick-plus-half-spread cross at `t + 0.5 ms`. **Research-defined failure:** mean net edge per trade **<= 0 at 2 bp per side** at 2 of 3 horizons -> H3 rejected; no tradability claim survives.
- **F7 - Gate-selection honesty.** Select `q` (and `h`) **on the validation period only**, freeze, evaluate once on test. Require the frozen gate's gain over the full test set to be **>= 50% of the reported +0.11 to +0.15**. **Failure** = the headline is test-set gate selection -> mark Table 1 as exploratory.
- **F8 - Multi-seed audit.** 10 independent seeds x 7 assets x 3 horizons. Require the seed-bootstrap 95% interval of the top-decile gain to **exclude 0 at >= 2 horizons**. **Failure** = single-seed noise.
- **F9 - Regime holdout.** Extend the test to **>= 90 consecutive days spanning >= 2 volatility regimes** on the same frozen models. Require sign-preserving gains at >= 2 horizons **and** stationary-share train/test drift **<= 20 pp** on every asset used in the headline. **Failure** = the BTC-style 70% -> 27% shift is doing the work -> robustness claim withdrawn.
- **F10 - Tail-recalibration gate.** Refit with a Student-t likelihood or post-hoc conformal recalibration until empirical 95% coverage lands in **[0.93, 0.97]**. Require the top-decile directional F1 at fixed `q` to move by **< 0.03**. **Failure** = prior SNR gating was miscalibrated and the tier memberships are unstable.
- **F11 - Circular-shift placebo.** Circularly shift the SNR ranking within each asset-horizon test set **1,000 times**; require the observed top-decile gain to exceed the **95th percentile** of the placebo distribution at >= 2 horizons. **Failure** = the ranking carries no information.
- **F12 - Multiplicity control.** Family = 21 asset-horizon cells x 10 gating tiers x 2 heads (>= 420 tests). Apply **Benjamini-Hochberg at q < 0.10**; if fewer than half the headline cells survive, report the result as exploratory only.
- **F13 - Cross-venue replication.** Repeat the frozen protocol on **Binance and/or Coinbase** L2 (or L3) data. Require **>= 2 of 3 venues** to preserve the sign and >= +0.03 gain at >= 2 horizons. **Failure** = Kraken-specific microstructure.
- **F14 - End-to-end economic gate.** Full simulation with a declared order type, a queue-aware fill model, a realistic latency distribution (not a fixed 0.5 ms), the venue's published maker/taker schedule, turnover and a capacity cap. **Research-defined failure:** net Sharpe **<= 0** or mean net edge **<= 0** at the venue's own published taker schedule -> **no adoption, no implementation**; the record stays research-only permanently.

**Action on failure (research-defined).** Failure of F1 or F2 -> the source-reported numbers are marked unreproducible and H1 is withdrawn. Failure of F3/F4/F5 -> the mechanism claim is narrowed to "confidence gating works on this forecaster" and the UQ-specific narrative is dropped. Failure of F6 or F14 -> no implementation, no Paper/Testnet/Live consideration. F7-F13 failures downgrade the evidence to exploratory. No failure path permits retuning to rescue the claim without a new record.

## Crypto portability

**direct.**

The evidence base is itself cryptocurrency: seven USD-quoted spot assets on Kraken, Level-2/Level-3 order books, November 2025 - February 2026, 5.196 billion events (research-computed sum of Table 6). No porting step is required to apply the mechanism to crypto microstructure.

Residual crypto-specific risks inside that `direct` setting:

- **Spot only.** The paper uses spot mid-prices on one venue. Nothing is established for perpetual futures: funding, mark/index price, basis and liquidation are absent from both the data and the model, and a perpetual port would need them.
- **Single venue.** Kraken event rates span 39-156 events/s with mean inter-event times 6.42-25.97 ms across the seven assets (Table 6). Section 7 of the source notes the analogous cross-market lesson is not a rescaling exercise; a Binance/Bybit/Coinbase book has different tick density, depth and queue dynamics, so the 512-event window covers very different wall-clock spans.
- **24/7 session structure.** No session boundaries are modelled; the 15-day test window contains no session-rollover variety to check against.
- **Event-time vs wall-clock.** Windows are 512 events but horizons are 5/10/15 s; on a quiet asset a 15 s horizon spans 585 events (LTC) versus 2,340 (BTC) - Table 6 - while the end-price smoothing window is a fixed `k = 10` events for all assets, so smoothing covers a proportionally larger fraction of the horizon for low-rate assets.
- **Liquidity / capacity.** No depth, participation or capacity analysis exists; at 5-15 s horizons the number of trades a strategy can do is bounded by queue position, which the paper never models.
- **Point-in-time and latency.** A fixed 0.5 ms label anchor is not a distributed-venue latency model; clock source and timezone are `data gap`.
- **Listing and survivorship.** SUI and TAO are relatively new listings with shorter histories; no listing-date or survivorship handling is discussed.

Crypto portability being `direct` is **not** authorization to trade.

## Limitations

- **underspecified** for trading: no entry, no exit, no holding-period rule, no sizing, no order type, no fill model, no cost - every operational element of a strategy is research-proposed.
- **data gap:** transaction cost, fees, commission, slippage, spread series, market impact, participation, capacity, leverage, margin, borrow, inventory, funding, liquidation, turnover, Sharpe, drawdown, PnL, timezone/clock, session convention.
- **data gap:** raw Kraken L2/L3 data (no data-sharing agreement) and the claimed code artifact (no URL in the pinned version).
- **not independently reproduced:** every source-reported number in this record.
- **unproven:** the economic translation from F1 to net-of-cost edge (H3); the source explicitly defers it.
- **unproven:** that the in-context conditioning, rather than the four loss terms, produces the gain (no ablation, Section 7).
- **unproven:** that the UQ head beats gating a plain encoder's softmax or weight-space uncertainty (no baseline, Section 7).
- Single seed (42/999), single venue, 15-day test window, per-asset/per-horizon models, no cross-venue evidence.
- Distribution shift between train and test is severe for the most liquid asset and is not independently replicated.
- Tail calibration fails at the 95% level (90.4-90.7% coverage), so `sigma`-driven thresholds are not trustworthy in the tails.
- Gate percentile is chosen on the test curve; no out-of-sample gate-selection rule exists in the source.
- Source-quality: **preprint only** - no journal, no peer-review statement, no citations counted, no acceptance stated; `code` and `data` both unavailable for verification.
- Publication-bias and search-space concerns: 21 asset-horizon pairs x 10 tiers x 2 heads with no multiplicity control (see F12).

## Implementation status

`implementation_status: not-implemented`.

No implementation exists in our research stack. We did not train a D-TABL encoder, did not attach a UQ head, did not obtain Kraken data, did not run any backtest, did not install dependencies, and did not touch Qlib, Paper, Testnet or Live. Nothing in this record has been executed by us; the only verification performed is provenance and internal arithmetic on the pinned primary text (Table 6 column sums, Table 1 row means and gating deltas, the prior-matched chance formula, Table 4 parameter sums, GPU-hour arithmetic and Table 8 row means), all labelled research-computed.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

This record's presence in the repository means only that normalized research material entered the public staging pool. It does **not** mean:

- passed Research Intake Review;
- entered Hermes Wiki Brain;
- entered the production candidate pool;
- completed Qlib full-backtest validation;
- became a frozen survivor or leaderboard entry;
- profitable, validated alpha, or a demonstrated net-of-cost edge;
- approved for implementation, Paper, Testnet or Live.

No Scout output may promote itself by wording, evidence count or confidence. Any adoption or implementation decision is a separate, explicitly reviewed step.

## Related Wiki records

Verified adjacent pages returned by a read-only `kb_search` on 2026-09-29 (no Wiki Brain writes were made; no page was fabricated):

- [[quant/two-level-uncertainty-cross-sectional-ranker-regime-trust-gate-tail-cap-2026-09-05]] - the closest conceptual neighbour: uncertainty-driven abstention/gating, but on a daily US-equity cross-sectional ranker with epistemic uncertainty, different horizon, market and uncertainty class.
- [[quant/temporal-kolmogorov-arnold-networks-high-frequency-lob-alpha-decay-2026-09-02]] - high-frequency LOB forecasting and alpha decay on FI-2010; different source, venue and era, no UQ gate.
- [[quant/order-flow-imbalance-predictive-decoupling-cost-falsification-2026-09-12]] - order-flow imbalance (the DNFI/QI family this paper's features build on) with an explicit cost falsification.
- [[quant/crypto-order-flow-online-sgd-microstructure-horizon-cost-falsification-2026-09-13]] - crypto microstructure direction at short horizons with taker-cost falsification.
- [[quant/crypto-perpetual-order-flow-entropy-microstructure-taker-cost-falsification-2026-09-13]] - crypto perpetual order-flow direction and taker-cost falsification.
- [[quant/hawkes-order-flow-imbalance-self-excitation-microstructure-2026-09-12]] - self-exciting order-flow predictability in BTCUSDT with a transaction-cost friction barrier.
- [[quant/deep-rl-market-making-regime-switching-bocpd-scenario-bandit-2026-09-11]] - the only adjacent record addressing quoting/inventory, which this paper does not model at all.

Repository-adjacent but different sources (listed for retrieval only, not linked as Wiki pages): `explainable-lob-microstructure-universal-feature-crypto-perp-2026-09-08.md` (arXiv:2602.00776) and `crypto-day-night-session-lagged-reversal-kraken-btc-eth-cutoff-search-2026-09-27.md` (shared Kraken venue only).

## Sources

1. Manoharan, D. G. E.; Linna, E.; Baltakys, K.; Dong, H.; Kanniainen, J. (2026). *UQ-LOB: Uncertainty-Aware Limit Order Book Mid-Price Forecasting*. **arXiv:2609.31491v1 [cs.AI]**, submitted 25 Sep 2026 16:33:23 UTC. DOI 10.48550/arXiv.2609.31491. https://arxiv.org/abs/2609.31491 - primary source; license CC BY 4.0; no journal reference, no peer-review statement, no Comments field.
2. Same paper, pinned full text read end to end on 2026-09-29: https://arxiv.org/html/2609.31491v1 - 361,606 bytes, SHA-256 `3fe388886fed609475bee81470dae1e1d46b620efa268dc72e13597ee65cf080`. Source of every Table 1-8 value, every Section 1-7 statement, Appendix A-C and Algorithm 1 used above.
3. Same paper, arXiv abstract/metadata page read 2026-09-29: https://arxiv.org/abs/2609.31491 - submission history, subject class, DOI status.
4. Cited works referenced only as the source's own context (not used for any empirical claim in this record): Gould et al. (2013) *Quantitative Finance* 13(11); Glosten and Milgrom (1985) *JFE* 14(1); Cont, Kukanov and Stoikov (2014) *JFE* 12(1); Zhang, Zohren and Roberts (2019a) *IEEE TSP* 67(11); Zhang, Zohren and Roberts (2018) BDLOB; Tran, Iosifidis, Kanniainen and Gabbouj (2018) *IEEE TNNLS* 30(5); Ntakaris et al. (2018) *Journal of Forecasting* 37(8); Linna, Baltakys, Iosifidis and Kanniainen (2025) LOBERT, arXiv:2511.12563; Levi et al. (2022) *Sensors* 22(15); Kim et al. (2019) attentive neural processes; Seitzer et al. (2022) arXiv:2203.09168; Chow (1970); Geifman and El-Yaniv (2017).

No other source was used. No secondary summary, search snippet or model-generated description contributed any strategy rule or empirical number in this record.
