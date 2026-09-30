---
schema: strategy-research-record-v1
title: "Spread-Gated Hawkes-Flocking Best-Quote Dynamics with Closed-Form Single-Period Limit-Order Placement Sizing (arXiv:2609.36631v1)"
created: 2026-09-30
updated: 2026-09-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - microstructure
  - hawkes-processes
  - limit-order-book
  - limit-order-placement
  - point-process
  - execution
  - us-equities
status: research-only
confidence: medium
source_as_of: 2026-09-30
sources:
  - https://arxiv.org/abs/2609.36631v1
  - https://arxiv.org/pdf/2609.36631v1
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Table 9 MSFT full-model log-likelihood printed 107.5 is inconsistent with the same row's AIC -187.4 and BIC -117.1, both of which imply 105.7 (k=12, n=2600); unreconciled."
  - "Table 15 reports the MSFT narrow-flocking constraint (alpha_1n = alpha_2n = 0) as Rejected at p<0.0001 while Table 8 prints MSFT alpha_1n = 0.0001 (s.e. 4.0) and alpha_2n = 0.007 (s.e. 7.3), i.e. point estimates numerically at zero; a likelihood-ratio rejection cannot be reconciled with those printed estimates; unreconciled."
---

# Spread-Gated Hawkes-Flocking Best-Quote Dynamics with Closed-Form Single-Period Limit-Order Placement Sizing (arXiv:2609.36631v1)

## Provenance

**Primary source identity**

- Paper: *A Spread-Gated Hawkes-Flocking Model for Best Bid and Ask Dynamics, with an Application to Limit Order Placement*.
- Author list exactly as printed on PDF page 1: **Hyoeun Lee** (asterisk footnote: Department of Statistics, University of Illinois, `hyoeun@illinois.edu`) and **Kiseop Lee** (dagger footnote: Department of Statistics, Purdue University, `kiseop@purdue.edu`). PDF metadata `/Author` reads `Hyoeun Lee; Kiseop Lee`; the landing page prints `Authors: Hyoeun Lee, Kiseop Lee`. No other author, no acknowledgements section, no funding statement, no conflict statement, no data-availability statement, no code-availability statement and no ORCID appear in the pinned text; all stay `data gap`.
- Identifier: `arXiv:2609.36631v1`, primary subject **q-fin.CP** with cross-list **q-fin.MF** (landing page `Computational Finance (q-fin.CP) ; Mathematical Finance (q-fin.MF)`; PDF masthead `arXiv:2609.36631v1 [q-fin.CP] 29 Sep 2026`).
- Version/date: **single version v1**, landing dateline `[Submitted on 29 Sep 2026]`, submission history `[v1] Tue, 29 Sep 2026 03:40:21 UTC (254 KB)` from Hyoeun Lee. The PDF first page is dated **September 30, 2026**, so the printed manuscript date is one day after the recorded submission date; recorded as printed and **not reconciled**.
- Publication status: the landing page carries **no Comments row and no Journal-reference row**. The only DOI is the arXiv-issued DataCite DOI `https://doi.org/10.48550/arXiv.2609.36631`, whose tooltip reads `arXiv-issued DOI via DataCite (pending registration)` (PDF metadata `/DOI` carries the same value). Publication status is therefore **arXiv preprint only; peer review not stated in source** as of 2026-09-30.
- Licence: landing-page `view license` link and PDF metadata `/License` both read `http://arxiv.org/licenses/nonexclusive-distrib/1.0/` - the **arXiv.org perpetual non-exclusive distribution licence**, not a Creative Commons licence. The text is therefore cited and normalized only, never redistributed.
- Data dependency named by the source: **LOBSTER level-5 limit order book data** (reference `[15]` R. Huang and T. Polak, *LOBSTER: Limit order book reconstruction system*, SSRN Electronic Journal, 2011). The vendor URL, licence and file identifiers are **not stated in source**; the data was not downloaded in this run.
- No repository, no code pointer, no `github`, no `repository`, no `code available`, no `data availability` and no reproducibility statement appear anywhere in the pinned text (whole-document census, all zero; the single `reproduc` hit is the verb *reproduces* in the Section 5 conclusion). Immutable code provenance therefore stays `data gap`. No third-party code was executed in this run.

**Pinned artefact (fetched 2026-09-30)**

- `https://arxiv.org/pdf/2609.36631v1`, **531,062 bytes**, SHA-256 `567fc606bf13d48f2761d25f65f6af1931ca9930d46a366e83e7d1c54d62abb6`, **34 pages**, extracted with pypdf 6.16.2 to **77,345 characters / 2,160 lines** and **read end to end**: Abstract, Sections 1, 1.1, 2, 2.1, 2.2, 2.3, 3, 3.1, 3.2, 3.3, 4, 4.1, 4.2, 4.3, 5, Tables 1-16 and their captions, Figures 1-3 captions, Lemma 1, Proposition 1, Lemma 2, Corollary 1, Remarks 1-3, equations (2.1)-(4.3), Appendix A (remaining Lemma 2 proofs and Tables 10-13), Appendix B (multi-start diagnostics, restricted fits, separate-baseline test, MSFT residuals), and the **37-item reference list**.
- `https://arxiv.org/abs/2609.36631v1`, 40,876 bytes, SHA-256 `860f4c10dd84b6f42f068174d988cd6869049b497ddb7bd2a2673d9c5cc2a5d8`, used for dateline, authors, subjects, DOI cell, licence link and submission history.
- PDF producer strings: `/Creator` `arXiv GenPDF (tex2pdf:0d14211)`, `/Producer` `pikepdf 8.15.1`, `/Title` matching the printed title, `/arXivID` `https://arxiv.org/abs/2609.36631v1`.
- The submission-history line reports the source package as `254 KB` while the served PDF is 531,062 bytes; the two are **not reconciled** here (different artefacts: e-print source versus rendered PDF).
- This record is **ASCII-only**. The source prints Greek letters and symbols; those are transliterated (`alpha_1n`, `Psi`, `Phi`, `rho`, `lambda`, `eta`, `delta`, `tau`, `theta`, `sigma_G^2`) where cited.

**Sample, universe, cost treatment (primary-source checksum fields)**

- **Sample period:** estimation and illustration use **one trading day, 2012-06-21**, restricted to the **10:00-15:30** window (Section 3.3). Simulation validation uses synthetic horizons `T in {500, 2000, 10000}` with `R = 200` paths (Section 3.2, Table 7). **No return sample and no time series of portfolio outcomes exist anywhere in the source.**
- **Universe:** **two US large-tick common stocks, INTC and MSFT**, on that single day - 1,768 classified best-quote events for INTC and 2,600 for MSFT, tick size `delta = $0.01` (Section 3.3). AMZN appears only as a screen (spread at one tick just **0.16%** of the 10:00-15:30 window, time-weighted median spread **12 ticks**) and is **not** modelled. No futures, no crypto, no options, no cross-sectional panel.
- **Transaction cost / slippage treatment:** determined at **Methods level** by reading Sections 2, 3, 4 (4.1, 4.2, 4.3), 5, Remarks 1-3, Tables 1, 5, 8-16 and Appendices A-B end to end, plus a **whole-document census of the pinned 77,345-character text**, which returns **zero** occurrences of `commission(s)`, `fee(s)`, `slippage`, `transaction cost`, `spread cost`, `maker`, `taker`, `borrow`, `funding`, `leverage`, `liquidation`, `capacity`, `turnover`, `partial fill`, `participation`, `Sharpe`, `CAGR`, `annualized`, `backtest`, `walk-forward`, `timezone` and `crypto`. The only friction-like terms that do appear are: **`rebate` exactly once** (Table 5 defines `r` as *Exchange rebate*, used in Section 4.3 as `r = $0.0003`), `adverse selection` four times (two of them inside reference titles, one stating that "the single-period objective also abstracts from adverse selection ... in this section the execution probabilities `q_j^i` are inputs", Remark 3), `latency` twice (both inside reference titles), `market impact` once (inside reference title `[3]`) and `impact` once more as "expected cash-flow impact". **There is therefore no commission model, no fee model, no slippage model, no spread-crossing cost, no impact model, no latency model and no borrow/funding/liquidation model in the source**; the only explicitly modelled cash-flow adjustment is the positive per-share exchange rebate `r`. Order type beyond the four resting levels, queue position, partial fills, signal-to-order delay, participation, session/closing behaviour and every capacity limit stay `data gap` and are **never treated as zero**. Execution probabilities `q_j^i` are **external inputs**, illustrative only (`q_1^a = 0.7`, `q_2^a = 0.5` in Section 4.3) and are explicitly *not* estimated by the model.

**Repository workflow**

- `README.md` read in full (575 lines) on this run.
- Canonical specification resolved from Hermes Wiki Brain **read-only**: `kb_read quant/strategy-research-record-spec-v2.md` returned **file not found**, so the run **failed closed onto `quant/strategy-research-record-spec-v1.md`**, 10,289 bytes, SHA-256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`.
- `git pull origin main` at run start fast-forwarded `a412632..d8b2512` (another scout's TradingView Bollinger record); `git log --oneline -20` was used as a **convenience glance only**, not as dedup.
- Hidden-inclusive pre-write dedup (`rg -uuu` across the whole checkout, including `.git`, `.mimo-worktrees`, `.agents`, `.hermes`): identity tokens `2609.36631`, `Hyoeun`, `Spread-Gated`, `spread-gated`, `hawkes-flocking`, `Hawkes flocking`, `arXiv.2609.36631` and the exact paper title all returned **zero files**; the token `flocking` (case-insensitive) returned **zero files** anywhere in the checkout; `coverage_manifest.csv` returned **0 hits** for `2609.36631|Hyoeun|flocking`; positive control `novy-marx` matched **43 files** in the same session, confirming the scan reached the hidden directories.
- Author-overlap scan: `Kiseop Lee` matched **3 files**, all copies (root checkout plus two `.mimo-worktrees` copies) of the single existing record `model-free-statistical-arbitrage-empirical-mean-reversion-time-reinforcement-learning-2026-09-05.md`, which captures a **different paper** (`arXiv:2403.12180`, Ning and Lee, reinforcement-learning statistical arbitrage). Shared author only; source identity, mechanism, universe, horizon and evidence class all differ, so the dedup rule does not block this record (stated again in `Related Wiki records`).

## Economic mechanism

### Source-reported

The source is a microstructure **modelling** paper with a deliberately modest single-period trading illustration, not a return-premium paper. Its stated mechanism and contributions:

- Four counting processes track the best-quote movements `Au`, `Ad`, `Bu`, `Bd` (equations (2.1)-(2.5)); because prices move in ticks `delta`, the spread obeys `S(t) >= delta` (equation (2.9)), so spread-narrowing movements must be suppressed at the minimum.
- The conditional intensity (equation (2.11)) is `lambda_t = [mu + integral h(t-u) dN_u] o g(t)` with the gate `g = (1, I(S>delta), I(S>delta), 1)`, which forces the narrowing intensities `lambda_A^d` and `lambda_B^u` to **zero** whenever `S(t) = delta`.
- The kernel splits as `h = Phi + k o Psi` (equation (2.13)): `Phi` is a within-side self-/mutually-exciting exponential Hawkes kernel (parameters `alpha_is`, `alpha_ic`, decay `beta_i`), and `Psi` is the **cross-side "flocking" kernel** (parameters `alpha_iw` for the widening state, `alpha_in` for the narrowing state) whose row-by-row activation is decided by the 0-1 matrix `k(t)` of equation (2.15) - the current spread state. The name is inherited from Jang, Lee and Lee [18].
- **Proposition 1** proves non-explosion on every finite horizon by monotone thinning against a dominating Hawkes process with kernel `bar_h = Phi + Psi` (Lemma 1), with **no condition on the spectral radius** `rho(M-bar)`. Remark 2 states explicitly that non-explosion is **not** recurrence or stationarity, and that whether the fitted spread process is recurrent is an unsettled empirical question.
- Estimation is exact **O(N) recursive maximum likelihood** (Section 3.1), 12 parameters, validated by simulation (Section 3.2, Table 7) and applied to LOBSTER data (Section 3.3). The source states the fitted role of the flocking term is "a rapid, millisecond-scale re-narrowing of the spread after a widening event" (Section 2.2).
- The trading application (Section 4) observes `(A(t), B(t), S(t))` plus the fitted `theta`, places **one** resting limit order at one of four price levels (`A(t)`, `A(t)+delta`, `B(t)`, `B(t)-delta`) with free quantity, and evaluates one-step conditional mean and variance of mark-to-market wealth `G = X + (A+B)/2 * Y` at the **first subsequent best-quote movement** `t+tau`. Utility is `H(t,pi) = mu_G - eta * sigma_G^2` (equation (4.2)). Because `mu_G` is linear and `sigma_G^2` quadratic in the quantity `l`, `H` is a **concave quadratic** in `l`, giving the closed form of Corollary 1: `l* = -c1/(2 c2)` and `max H = -c1^2/(4 c2) + c0`, with `c2 = -eta * Var(Z) <= 0`.
- The source does **not** claim that the model predicts returns. It claims (a) that the cross-side term is needed to fit best-quote dynamics, and (b) that the fitted next-event probabilities plus externally supplied execution probabilities are enough to size a single passive order.

### Research interpretation

Falsifiable form of the mechanism we normalize:

- **Regime/state:** the spread is a two-state process (`S = delta` versus `S > delta`) on large-tick names, and the state gates which quote movements can occur.
- **Signal:** the conditional intensity vector at time `t` gives next-event probabilities `p = lambda/Lambda`, which determine, together with fill probabilities `q_j^i`, the expected half-spread-plus-rebate capture and its variance for each resting price level.
- **Economic channel:** liquidity provision / spread capture - a passive order earns roughly the spread fraction plus rebate when filled and loses when the quote moves through it. The hypothesised edge is **better state-dependent prediction of imminent quote moves** (spread re-narrowing after a widening event), i.e. a microstructure-forecasting edge feeding an execution-size decision.
- **Not claimed by us or the source:** no directional return prediction, no cross-sectional premium, no risk premium. The strategy is an **execution/sizing optimisation**, and its economic viability hinges on adverse selection and fill realism - both of which the source explicitly leaves out.
- Role separation: *state gate* = `I(S>delta)` structure; *primary signal* = fitted Hawkes-flocking intensities and their next-event probabilities; *fill model* = external `q_j^i` (not part of the model); *risk* = mean-variance penalty `eta`; *sizing* = closed-form `l*`. Ablation is mandatory: the source itself shows the `Psi = 0` ablation on fit, but never on trading outcomes (`data gap`).

## Signal

Normalized so a researcher can reconstruct the decision; anything not printed by the source is labelled.

- **Formation timestamp:** continuous-time decision at `t` while the book is open; the state is `(A(t), B(t), S(t))` and `theta` fitted from the event history (in the source, fitted on the same day, Section 3.3). Tradable immediately in principle. The source restricts analysis to the **10:00-15:30** window to avoid open/close seasonality but prints **no timezone** (`timezone` census 0) - clock convention stays `data gap`.
- **Lookback:** the intensity uses the full event history since the process start via an exponential accumulator (O(N) recursion, Section 3.1); decay rates `beta_1`, `beta_2` of order 400-840 per second imply an effective memory of milliseconds (Table 8 caption: memory consistent with sub-10 ms clustering). Estimation window = the whole 10:00-15:30 session of 2012-06-21. Warm-up, inclusive/exclusive endpoints and event-collision rules: tied timestamps are collapsed, simultaneous ask-and-bid moves and multi-tick jumps are **excluded** (both "well under 1% of transitions") - stated in Section 3.3.
- **State gate:** if `S(t) = delta`, then `lambda_A^d = lambda_B^u = 0`, so the next movement is `Au` or `Bd` only (Section 4.3).
- **Long/short entry (source-reported):** at `t` choose **one** of four resting actions - sell `l_a` at `A(t)` (best ask), sell `l_a` at `A(t)+delta` (second-best ask), buy `l_b` at `B(t)` (best bid), buy `l_b` at `B(t)-delta` (second-best bid). Remark 3 excludes deeper levels and marketable (immediate) limit orders by design; the third-best probability `q_3` enters only to describe bumping, not as a placement choice.
- **Quantity:** closed form from Corollary 1 for each level (worked out explicitly for the best ask; "the remaining three price levels follow the same argument", with Appendix A giving their `mu_G` and `sigma_G^2`). `l* = -c1/(2 c2)`, `max H = -c1^2/(4 c2) + c0`.
- **Exit / holding period:** the evaluation horizon is the **first subsequent best-quote movement** `t+tau` (mean `tau` about **22 seconds** from the minimum-spread state in the sample, Section 4.3). The source does **not** specify cancellation, replacement, partial-fill carry-over, inventory continuation, or what happens if the order is never filled before the close - **underspecified**.
- **Parameters (all source-reported):** 12 fitted parameters per stock (Table 8); `S(t) = delta = $0.01`; `r = $0.0003` exchange rebate; `eta = 1`; initial inventory `Y(t) = 0`; `q_1^a = 0.7` and `q_2^a = 0.5` explicitly labelled *illustrative*; day-averaged next-event frequencies `p_A^u ~= 0.455` (402 of 883) and `p_B^d ~= 0.545` (481 of 883).
- **Illustration outputs (source-reported):** `K ~= 0.00406`, `c2 ~= -2.4e-5`, `l* ~= 85 shares`, `H|_(l=l*) ~= $0.17`; fitted-intensity variant evaluated at each of the 883 minimum-spread moments gives median `83` shares, **86% of evaluations within 5 shares** of the static value, three moments above 200 shares and one outlier at **7,297** shares; halving `eta` doubles `l*` to about **169** shares; `85` shares is **under 1%** of the median displayed size at the INTC best ask (about **11,900** shares).
- **Position sizing logic:** `l*` from the closed form; **no** session cap, no notional cap, no risk limit, no scaling rule is given - any such rule would be `research-proposed`.
- **Multi-timeframe / re-entry:** none specified; the source states the multi-period extension is future work. Overall the rule is **analytically closed-form but operationally underspecified** (no submission cadence, no queue handling, no re-entry, no inventory policy).

## Required data

- **Instrument / universe:** INTC and MSFT (US common stock, large-tick at `delta = $0.01`); the model's two-state gating assumes single-tick best-quote moves (observed under 0.5% multi-tick moves for these names).
- **Venue / market type:** US equity limit order book; the source does not name the consolidated venue beyond the vendor (LOBSTER reconstructs Nasdaq order flow) - venue detail is `data gap`.
- **Data:** **LOBSTER level-5** order-by-order book reconstruction for **2012-06-21**, from which best ask/bid price series are extracted; required fields: best bid and best ask prices and their event timestamps, plus tick size. Trades, depth beyond level 5, open interest, borrow and corporate actions are **not used**.
- **Timeframe:** event (point-process) data, sub-millisecond resolution implied by sub-10 ms clustering and decay rates of hundreds per second; window 10:00-15:30.
- **Timestamp:** timezone **not stated** (`data gap`); precision, alignment of tied timestamps (collapsed) and out-of-order handling (not stated) are partially specified; session convention is the stated 10:00-15:30 restriction.
- **Point-in-time / leakage:** parameters are estimated on the **same day** used for the placement illustration - there is no train/test split, no rolling refit and no out-of-sample evaluation anywhere (`data gap`; the source lists out-of-sample full-vs-`Psi=0` comparison as future work).
- **Missing data:** exclusions are stated (simultaneous ask-and-bid moves, multi-tick jumps, tied-timestamp collapse) but no null/stale/suspended-print policy is given - `data gap`.
- **Cost/fee/spread needs:** for any real use, venue fee schedule, rebate schedule, spread at decision, latency and queue position would be required; the source supplies only `r = $0.0003` and illustrative `q` - every other friction field is `data gap`.

## Execution assumptions

- **Signal-to-order timing:** decision and order placement at the same instant `t`; no latency, no polling delay, no asynchronous-data assumption is modelled (`latency` appears only in reference titles).
- **Order type:** resting (passive) limit orders at the best or second-best quote only; marketable limit orders and deeper levels excluded by design (Remark 3).
- **Fill model:** Bernoulli execution by the next price movement with probability `q_j^i` that is **externally supplied**, not modelled; queue position is explicitly not modelled (Section 4.3, Conclusion), and the source says realistic order sizes require queue-position estimation a la Figueroa-Lopez et al. [11]. Illustrative values `q_1^a = 0.7`, `q_2^a = 0.5`.
- **Fees / rebate:** no commissions or fees; a **positive exchange rebate `r = $0.0003`** per executed share is credited in the cash-flow table (Table 5, Table 10).
- **Spread / slippage / impact:** spread enters the *payoff* (half-spread capture and `+-delta/2` quote moves), not as a crossing cost; slippage, market impact, participation and order type beyond the four levels are absent (`data gap`).
- **Adverse selection:** **explicitly abstracted** (Remark 3: "abstracts from adverse selection, which links an order's fill probability to its profitability ... the execution probabilities `q_j^i` are inputs"). This is the single largest economic assumption gap.
- **Latency / partial fills / failures:** not modelled; partial fills collapse into the Bernoulli `q`; no failure handling (`data gap`).
- **Leverage / margin / borrow / funding:** zero occurrences; not applicable to the illustration (`data gap` for any deployment).
- **Capacity:** not addressed; the illustration's `l* ~= 85` shares against a median displayed size of about 11,900 shares at the INTC best ask is a realism comment on `q`, **not** a capacity claim.
- What the source assumes vs what a Scout would have to assume: everything above is source-stated; **any** concrete submission cadence, cancellation policy, inventory cap or fee schedule added later must be labelled `research-proposed`.

## Evidence

### Source-reported

All figures below are **source-reported** (third-party), all are **model-fit or illustration values, not returns**: the source contains no return series, no Sharpe, no CAGR, no drawdown, no win rate and no turnover (whole-document census, all zero). There is therefore **no gross-versus-net-of-cost distinction to make** - no performance number exists to be netted. Every figure is traceable to a table, figure or section of the pinned v1 PDF.

- **Fit of the full model versus the `Psi = 0` null (Table 9, 2012-06-21, 10:00-15:30):** INTC log-likelihood `-572.5` full versus `-5269.4` null, AIC `1169.0` versus `10554.8`, BIC `1234.7` versus `10598.6`; MSFT log-likelihood `107.5` full versus `-6867.3` null, AIC `-187.4` versus `13750.6`, BIC `-117.1` versus `13797.5`. Caption: the likelihood-ratio statistic exceeds **9,300 on 4 degrees of freedom** for both stocks (research-recomputed from the printed log-likelihoods: **9,393.8 INTC, 13,949.6 MSFT**). The source flags that the null parameters sit on the boundary of their `>= 0` domain, so the chi-square-4 reference is not exact (Self and Liang [34]), and - because goodness-of-fit fails - reads the comparison as **relative fit only**.
- **Stronger separate-baseline test (Table 16, four baselines, 30 starts per stock per model):** INTC 14-parameter log-likelihood `-458.4`, AIC `944.9`, BIC `1021.6` versus `Psi=0` (10 parameters) `-3035.6`, `6091.2`, `6146.0`, LR `5154.3`; MSFT `256.5`, `-485.0`, `-402.9` versus `-3286.5`, `6592.9`, `6651.6`, LR `7085.9`. `Psi = 0` still rejected; all AIC/BIC identities reproduce.
- **Point estimates (Table 8, full 12-parameter model; est (asymptotic s.e.)):** INTC `mu_1 0.0202 (0.0010)`, `mu_2 0.0220 (0.0011)`, `beta_1 438.89 (25.2)`, `beta_2 679.43 (39.0)`, `alpha_1s 0.052 (5.9)`, `alpha_1c 80.23 (8.8)`, `alpha_1n 3.073 (3.1)`, `alpha_1w 300.55 (23.1)`, `alpha_2s 0.034 (31.0)`, `alpha_2c 164.77 (21.4)`, `alpha_2n 0.001 (12.4)`, `alpha_2w 496.58 (40.3)`, `rho(M-bar) 0.87-0.92`; MSFT `mu_1 0.0278 (0.0012)`, `mu_2 0.0329 (0.0013)`, `beta_1 550.47 (25.1)`, `beta_2 840.01 (41.8)`, `alpha_1s 2.920 (2.9)`, `alpha_1c 178.03 (12.9)`, `alpha_1n 0.0001 (4.0)`, `alpha_1w 411.05 (25.4)`, `alpha_2s 9.912 (12.1)`, `alpha_2c 128.67 (12.6)`, `alpha_2n 0.007 (7.3)`, `alpha_2w 591.95 (41.1)`, `rho(M-bar) 0.91-1.00`. The source states the small coefficients `alpha_is` and `alpha_in` **cannot be distinguished from zero**.
- **Endogeneity (Section 3.3):** regime-specific spectral radii about **0.71 (INTC) and 0.73 (MSFT)** at minimum spread, **0.44 and 0.49** at wider spreads, against **0.92 and 0.98** for the ungated `rho(M-bar)`; the ungated value overstates the gated process.
- **Sample facts (Section 3.3):** 1,768 INTC events and 2,600 MSFT events; 884 widening and 884 narrowing events for INTC, 1,300 each for MSFT; spread at one tick **over 99%** of the time for INTC/MSFT (only about three-quarters of order-book updates, because brief two-tick excursions generate many updates); multi-tick best-quote moves **under 0.5%**; AMZN screen 0.16% one-tick, median spread 12 ticks; decay estimates correspond to memory of order milliseconds.
- **Precision (Section 3.3 and Appendix B):** scaled condition numbers **486 (INTC) / 449 (MSFT)**; information eigenvalues **5.7 to 2.8e3** and **5.7 to 2.6e3**; the least-determined direction is dominated by `alpha_2w` (s.e. about 40 units, 8% of the INTC estimate, 7% MSFT); "**about 18 trading days** would bring every direction of the parameter space to within 10% of its scale" (research-recomputed: `(40.3/10)^2 = 16.2` and `(41.1/10)^2 = 16.9` days, consistent with "about 18").
- **Optimisation difficulty (Table 14):** **30 starts (INTC) / 24 starts (MSFT)**; best log-likelihood `-572.5` / `107.5`; **log-likelihood range across nominally converged starts 769.8 / 1472.2**; condition numbers as above.
- **Restricted fits (Table 15):** self-excitation `= 0` on INTC - **inconclusive** (footnote: negative LR statistic because the full model's own multi-start search had not found its best fit); narrow-flocking `= 0` on MSFT - **Rejected, p<0.0001**; aliasing `alpha_1c = alpha_1w, alpha_2c = alpha_2w` - **Rejected, p<0.0001 on both stocks**.
- **Residual diagnostics (Section 3.3, Figures 1 and 3):** time-rescaled residuals are tested against Exponential(1); **Kolmogorov-Smirnov rejects for every event type under both models (p<0.05)**. Compensator counts: under `Psi = 0` the model generates only **116 of INTC's 884** narrowing events (**142 of 1,300** for MSFT) against **408** (**589**) under the full model; the full model still overstates widening events (**1,337 versus 884** for INTC).
- **Simulation validation (Section 3.2, Table 7):** `R = 200` paths, `T in {500, 2000, 10000}` with 334.6 / 1344.9 / 6734.7 average events per path, true parameter set with `rho(M-bar) ~= 0.886`. `beta_2` bias falls `0.1106 -> 0.0230 -> 0.0059` (about 9% of its true value at `T = 500`), and every parameter's standard deviation shrinks monotonically with `T`.
- **Placement illustration (Section 4.3):** at the minimum-spread state, 883 successor events split 402 `Au` / 481 `Bd`, giving `p_A^u ~= 0.455`, `p_B^d ~= 0.545`; with `q_1^a = 0.7`, `S = delta = $0.01`, `r = $0.0003`, `eta = 1`, `Y = 0`: `K ~= 0.00406`, `c2 ~= -2.4e-5`, **`l* ~= 85` shares**, **`H ~= $0.17`**; live-intensity variant median **83** shares with **86%** within 5 shares, three moments above 200 and a **7,297**-share outlier; mean time to next movement about **22 seconds**; two-tick state about **1%** of the time with next move `Ad` in **51%** and `Bu` in **49%** of INTC occurrences; `l*` is **under 1%** of the median displayed best-ask size of about **11,900** shares; halving `eta` gives about **169** shares.
- **Figure 2 (Section 4.2):** four panels show that **no single action is uniformly optimal** - the ranking among the four resting levels flips with the order-flow intensities, the execution probabilities and `eta`.

### Independently reproduced

not independently reproduced

Arithmetic-only cross-checks were run against the pinned printed values (see `Limitations` and `Falsification plan`); they verify internal arithmetic, **not** the empirical claims. No market data was downloaded, no model was re-estimated, no third-party code was executed and no backtest was performed.

### Negative evidence

1. **No performance evidence exists.** The source reports no return, no Sharpe, no drawdown, no win rate, no turnover and no backtest of any kind (census: `Sharpe`, `CAGR`, `annualized`, `backtest`, `walk-forward` all zero). The only trading number is a single-order expected utility of about `$0.17` under illustrative inputs.
2. **Neither model is correctly specified.** Time-rescaled residuals are rejected against Exponential(1) for **every event type under both models (KS, p<0.05)** - the source states the single-exponential kernel is too rigid for multi-timescale clustering.
3. **The full model still misfits the data it was fitted to**: it generates 1,337 INTC widening events against 884 observed, and only 408 of 884 narrowing events (589 of 1,300 for MSFT).
4. **One trading day, two stocks, 4,368 events total** (1,768 + 2,600). The source explicitly lists "more trading days and more stocks, together with out-of-sample comparisons" as future work, so there is **no out-of-sample evidence of any kind**.
5. **Multimodal likelihood**: nominally converged fits span **769.8** (INTC) and **1472.2** (MSFT) log-likelihood units (Table 14), so a single optimisation run is unreliable; multi-start is mandatory.
6. **The self-excitation restriction test on INTC is reported as inconclusive because the full model's own multi-start search had not found its best fit** (Table 15 footnote) - i.e. the reported best fit may not be the maximum, which directly weakens every likelihood comparison in the paper.
7. **Asymptotics are not justified.** The source states stationarity and ergodicity are **not** established (Remark 2, Section 3), so standard errors are reported as "approximate, descriptive measures of precision", and the goodness-of-fit diagnostics "call into question" the correctness assumption behind them.
8. **Boundary and specification caveats on the headline test**: the LR reference distribution is not exact at the boundary, and the source itself downgrades the whole comparison to "relative fit".
9. **Execution probabilities are illustrative, not estimated** (`q_1^a = 0.7`, `q_2^a = 0.5`), and the source calls them "the binding modeling input for realistic order sizes" - the headline `l* ~= 85` shares is therefore driven by an unsourced input and is **under 1% of the median displayed size** (about 11,900 shares), i.e. plainly unrealistic in scale.
10. **Sizing is extremely sensitive to an uncalibrated parameter**: halving `eta` doubles `l*` (`85 -> 169`); `eta = 1` is chosen without any calibration rationale (`data gap`).
11. **Live-intensity sizing has a heavy tail**: three of 883 evaluations exceed 200 shares and one reaches **7,297 shares**, about 86x the static value, so the closed form can emit untradable sizes when the recent event history is dense.
12. **Adverse selection is explicitly excluded** from the objective (Remark 3), so fill probability is decoupled from profitability - precisely the link that determines whether liquidity provision earns or loses.
13. **No friction except a positive rebate**: commissions, fees, slippage, spread-crossing cost, impact, latency, participation, borrow and funding all have zero occurrences; the utility calculation can therefore only be an upper bound.
14. **Single-period by construction**: no cancellation, no repeat submission, no inventory carry, no session close, no multi-period sequencing - the source states this is left to future work, so no strategy-level (as opposed to single-order) claim is supported.
15. **Two printed-value contradictions** are recorded in the frontmatter and below (Table 9 MSFT log-likelihood; Table 15 versus Table 8 on MSFT narrow-flocking), so at least two quantitative statements in the source cannot be taken at face value.
16. **Table 15 tension on near-zero coefficients**: `alpha_1n`/`alpha_2n` are printed at or near zero with large standard errors on **both** stocks (INTC `3.073 (3.1)` and `0.001 (12.4)`; MSFT `0.0001 (4.0)` and `0.007 (7.3)`), i.e. individually indistinguishable from zero, yet one of the two stocks' narrow-flocking restriction is reported as strongly rejected.
17. **Generalisation beyond large-tick names is untested and is claimed to be inappropriate**: AMZN is screened out (one-tick spread only 0.16% of the window), so the mechanism is asserted only where the two-state gating is nearly degenerate - the model has not been shown to add value where the spread actually varies.
18. **Recurrence/stationarity of the fitted spread process is an open question** (Remark 2): the compensator implies more widening than narrowing events, so the estimated state process may drift, and the day-averaged next-event frequencies used in the illustration may not be stable.
19. **Sample-size warning in-source**: the source notes Lee and Seo [24] simulate 5,000-10,000 events while these series have 1,768 and 2,600, and that optimiser success improves with sample size - i.e. the source itself says the sample is small by the standards of the literature it compares to.
20. **No code, no data-availability statement, no reproducibility statement** (all zero), so nothing in the paper can be re-run from published artefacts; LOBSTER data is commercial.
21. **None of this is contradicted by an external study because no external study of this specific model exists yet**; absence of contrary literature is not evidence of robustness.

## Falsification plan

Every threshold below is `research-defined` (a Scout-chosen acceptance/failure cutoff), and every operational rule not printed by the source is `research-proposed`. Failure action is pre-declared; **no gate may be rescued by retuning** (see the no-retuning rule).

- **F1 - Printed-value reproduction gate.** From the pinned inputs (`p_A^u = 402/883`, `p_B^d = 481/883`, `q_1^a = 0.7`, `q_2^a = 0.5`, `S = delta = 0.01`, `r = 0.0003`, `eta = 1`, `Y = 0`), recompute `K`, `c2`, `l*`, `max H`, and the Table 9 / Table 16 AIC, BIC and LR statistics. *Fail if* any value deviates from the printed one by more than **1% relative (research-defined)**. *Action:* stop; treat the source's arithmetic as non-reproducible and drop the record's quantitative claims. **Status at capture: the Section 4.3 chain reproduces (`K = 0.004064`, `c2 = -2.398e-5`, `l* = 84.7`, `H = 0.1722`), but the Table 9 MSFT full-model log-likelihood does not - contradiction 1 must be resolved by the authors or the value discarded.**
- **F2 - Optimisation reproducibility gate.** Re-run the multi-start MLE with the source's protocol (>= 30 log-uniform starts, gradient plus derivative-free fallback) and fixed seeds on the same day. *Fail if* the best log-likelihood differs from the printed value by more than **0.5 units (research-defined)** across two independent runs, or if the reported range across starts is not within **10% of 769.8 (INTC) / 1472.2 (MSFT) (research-defined)**. *Action:* the fit is not reproducible; reject every downstream claim.
- **F3 - Cross-day, cross-stock replication gate (core model claim).** Repeat the full-vs-`Psi=0` comparison on at least **20 independent trading days** and at least **10 large-tick US names (research-proposed scope)**, each with separate baselines (Table 16 protocol). *Fail if* the boundary-adjusted test fails to reject `Psi = 0` on more than **25% of day-name cells (research-defined)**. *Action:* the cross-side term is not a stable feature; the mechanism claim is rejected.
- **F4 - Out-of-sample fit gate.** Estimate `theta` on day `d-1` (or the preceding 5 days, `research-proposed`) and score the held-out day's log-likelihood for both models. *Fail if* the full model's per-event held-out advantage over `Psi = 0` is below **0.01 nats/event (research-defined)** in the median cell. *Action:* the improvement is in-sample fitting, not structure.
- **F5 - Goodness-of-fit gate.** Re-run the time-rescaled residual KS tests with Benjamini-Hochberg correction at `q < 0.10 (research-defined)` across 4 event types x 2 models x held-out days. *Fail if* any event type is still rejected. *Action:* keep only a relative-fit claim, never a calibrated-probability claim. **Status at capture: currently failing (source reports raw p<0.05 everywhere).**
- **F6 - Fill-model calibration gate (the binding input).** Estimate `q_j^i` from queue position / order-by-order replay rather than assuming them. *Fail if* the calibrated `q_1^a` differs from the illustrative `0.7` by more than **0.15 absolute (research-defined)**, or if `l*` under calibrated `q` differs from the printed `85` shares by more than **50% (research-defined)**. *Action:* the sizing illustration is invalid; rebuild before any test.
- **F7 - Adverse-selection / markout gate (the economic core).** For simulated or replayed fills, measure the change in mid price between fill and the next `delta`-move (and over 1 second, `research-proposed`). *Fail if* mean post-fill markout net of the half-spread and rebate is **<= 0 (research-defined)**. *Action:* there is no liquidity-provision edge; the record degrades to a modelling-only artefact.
- **F8 - Cost ladder gate.** Re-run the utility calculation with commissions/fees of 0, 0.5, 1, 2 and 5 bps per side plus a half-spread, and with latency of 0, 1, 10 and 50 ms (`research-proposed ladder`). *Fail if* `max H` at the illustrated size becomes **<= 0 at any ladder rung at or above the venue's standard retail fee schedule (research-defined)**. *Action:* reject as non-tradable.
- **F9 - Sizing robustness gate.** Perturb `eta` by `+-25%` and each `q` by `+-0.15` (`research-proposed`). *Fail if* `l*` moves by more than **50% (research-defined)** under any single perturbation. *Action:* the sizing rule is not operationally meaningful; report only the qualitative placement ranking. **Status at capture: source's own numbers already trip a 50% version of this gate (halving `eta` doubles `l*`).**
- **F10 - Placement-ablation gate (trading, not likelihood).** Compare expected net utility per order for full model vs `Psi = 0` vs time-shuffled-event placebo on held-out days, with the same `q` for all three. *Fail if* the full model's utility advantage over **both** controls is **<= 0 (research-defined)**. *Action:* the flocking term is not economically useful even if it is statistically preferred.
- **F11 - Strategy-level replay gate.** Run a multi-period event-level replay (`research-proposed`: submit one resting order per minimum-spread state, cancel on the opposite-side event, cap `l*` at a pre-declared share cap) over at least **12 months of data (research-defined)** with the venue fee schedule. *Fail if* net Sharpe of the capture PnL is **<= 0 (research-defined)** or if results depend on the single day 2012-06-21 alone. *Action:* terminal reject for adoption purposes.
- **F12 - Multiple-testing / model-selection hygiene.** Report the full distribution of converged log-likelihoods and apply Benjamini-Hochberg at `q < 0.10 (research-defined)` across all day x stock x specification comparisons, including the Table 15 family. *Fail if* no comparison survives, or if the two frontmatter contradictions cannot be resolved from the authors' artefacts. *Action:* report the model-selection evidence as uncorrected and downgrade every quantitative claim.

**No-retuning rule:** the model structure (gate, `Phi`, `Psi`, exponential kernels), the 12-parameter count, the multi-start protocol, the 10:00-15:30 window, the four-level action set, `eta`, `r`, the illustrative `q` values, and every threshold above are frozen at first run. A failed gate is reported as failed; parameters may not be changed to rescue it. Any change starts a new, separately labelled experiment.

**Ablations for the mechanism claim:** `Psi = 0` (already run by the source on fit); separate-baselines variant (Table 16); self-excitation `= 0`; narrow-flocking `= 0`; aliasing `alpha_ic = alpha_iw`; time-shuffled-event placebo; `q` held common across models; `eta` sweep; one-tick-state-only versus two-tick-state-only evaluation.

## Crypto portability

`adapted` - the machinery ports in form, the evidence does not; **crypto performance unproven and economic viability unproven**.

- The state-gate/intensity/optimisation structure is instrument-agnostic in principle: any venue with a discrete tick and a top-of-book has `S(t) >= delta` and four (or two) best-quote movement types.
- **Tick regime mismatch:** the source's whole gating story rests on large-tick names where the spread sits at `delta` over 99% of the time and multi-tick moves are under 0.5%. BTC/USDT and other top crypto pairs have a relative tick far smaller than INTC/MSFT in 2012, so the frequency of `S > delta` states, the two-tick excursion process and therefore every fitted `alpha_iw`/`alpha_in` are not transferable - this is our `research-proposed` expectation, not a source result.
- **Rebate sign:** the illustrated edge contains `r = $0.0003` as a **positive** per-share rebate. Most crypto venues charge rather than pay makers on top pairs (or pay near zero), so `K`, `c2` and the optimal size can change materially or change sign; no crypto fee schedule appears in the source (`data gap`).
- **24/7 sessions:** there is no 10:00-15:30 window to avoid open/close seasonality, no session close, and candle/timestamp boundaries differ; the source prints no timezone at all.
- **Perpetual-specific:** funding, mark/index price, maintenance margin and liquidation have **zero occurrences** in the source; a perpetual implementation would have to model them (`data gap`), and funding interacts directly with resting-quote inventory.
- **Venue fragmentation and data:** the source depends on LOBSTER level-5 equities data; crypto would need exchange-native L2/L3 streams with different sequencing, snapshot and connection-reset semantics, plus a choice among venues with different tick and queue rules (`data gap`).
- **Liquidity / queue competition:** crypto top-of-book queue dynamics, spoofing/cancel bursts and latency competitions differ from Nasdaq order flow; queue position is unmodelled even in the source.
- **Census:** `crypto`, `bitcoin`, `ethereum`, `perpetual`, `Binance`, `USDT` all have **zero occurrences** in the pinned text, so portability must be labelled `adapted` with `unproven` performance, never `direct`.

## Limitations

- `underspecified`: submission cadence, cancellation/replacement policy, partial-fill carry-over, inventory policy `Y(t)` beyond the `Y = 0` illustration, session/close handling, re-entry rules.
- `underspecified`: timezone and clock convention; venue beyond the LOBSTER citation; whether parameters are refit daily in any deployment.
- `data gap`: every friction field except the rebate `r` (census-verified); queue position; execution probabilities (illustrative only); capacity and participation; borrow/margin/funding.
- `data gap`: no code, no repository, no data-availability statement, no reproducibility statement; LOBSTER data is commercial and was not obtained.
- `data gap`: no out-of-sample, no multi-day, multi-stock panel, no train/test split, no point-in-time audit, no multiple-testing control.
- `not independently reproduced` for every source-reported number; only arithmetic cross-checks of printed identities were executed.
- `unproven`: the economic value of the whole pipeline - the source never computes a trading PnL, a Sharpe or a cost-adjusted return.
- **Two source-internal contradictions are recorded in the frontmatter and left unreconciled:** (i) Table 9's MSFT full-model log-likelihood `107.5` versus the AIC `-187.4` and BIC `-117.1` printed in the same row, which imply `105.7` for `k = 12`, `n = 2600` (all other rows of Tables 9 and 16 reconcile exactly); (ii) Table 15's MSFT narrow-flocking `Rejected, p<0.0001` versus Table 8's MSFT `alpha_1n = 0.0001 (s.e. 4.0)` and `alpha_2n = 0.007 (s.e. 7.3)`, since a restriction set exactly at the reported maximum must yield a likelihood ratio near zero. Candidate explanations (digit transposition; a local mode reached by one search; a stock-label swap; unreliable boundary standard errors) are **not stated in source** and are not adjudicated here.
- Publication status is **preprint-only** with no peer-review statement; acceptance claims are absent rather than false.
- The licence is the arXiv non-exclusive distribution licence, not CC, so long excerpts are not reproduced here.
- This record does not modify any engine, does not run backtests, does not download market data and does not execute third-party code.

## Implementation status

`not-implemented`.

Nothing has been implemented in our research stack. No model was fitted, no code from the source (none exists) was executed, no LOBSTER or other market data was downloaded, no backtest, simulation or order replay was performed, and no Qlib, Paper, Testnet or Live verification of any kind occurred. The only executable artefacts produced by this run were arithmetic-only cross-checks of the source's printed identities (AIC/BIC/LR identities, Table 7 RMSE identities, and the Section 4.3 `K`/`c2`/`l*`/`H` chain), which test internal consistency rather than empirical validity.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

The presence of this record in the repository means only that a normalised research capture exists. It does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. No wording, evidence count or gate count in this record promotes it.

## Related Wiki records

Adjacent concepts located read-only: one `kb_search` for `Hawkes limit order book` returned ten pages, and direct vault-file existence checks confirmed that the four linked paths below are present as pages inside the Hermes Wiki Brain vault. No Wiki page was written, moved or deleted by this run.

- [[quant/hawkes-self-exciting-lob-return-sign-forecasting-coe-2026-09-02]] - closest in technique (Hawkes LOB), but the object is **return-sign forecasting in crypto** rather than best-quote dynamics plus placement sizing.
- [[quant/hawkes-order-flow-imbalance-self-excitation-microstructure-2026-09-12]] - order-flow-imbalance cross-capture and the transaction-cost barrier in BTCUSDT; a **predictive-signal** claim, not a placement decision.
- [[quant/order-flow-two-layer-hawkes-core-reaction-rough-impact-2026-09-02]] - two-layer Hawkes decomposition with rough impact; **impact/execution** focus without best-quote state gating.
- [[quant/model-free-statistical-arbitrage-empirical-mean-reversion-time-reinforcement-learning-2026-09-05]] - shares co-author **Kiseop Lee** only; different source identity (`arXiv:2403.12180`), different mechanism (RL statistical arbitrage), different universe and horizon.

Repository neighbours with a **different source identity and a materially different mechanism** (listed for reviewer orientation, not as Wiki links): `hawkes-self-exciting-lob-return-sign-forecasting-coe-2026-09-02.md` (crypto return-sign prediction); `hawkes-order-flow-imbalance-self-excitation-microstructure-2026-09-12.md` (BTCUSDT OFI capture); `order-flow-filtration-trade-grounded-imbalance-hawkes-2026-09-17.md` (directional signal extraction, `arXiv:2507.22712`); `sequential-limit-order-execution-quoting-signal-adaptive-triangular-hjb-2026-09-02.md` (multi-period HJB quoting with alpha signals, `arXiv:2605.24242`); `contrarian-market-making-fill-probability-order-flow-2026-09-01.md` (fill-probability vs poise, `arXiv:2502.18625`); `model-free-passive-execution-order-level-shadowing-ppov-2026-09-17.md` (model-free passive execution benchmark, `arXiv:2609.18019`); `microstructure-mean-reversion-optimal-symmetric-band-waiting-option-2026-09-02.md` (band-threshold mean reversion with option value of waiting); `model-free-statistical-arbitrage-empirical-mean-reversion-time-reinforcement-learning-2026-09-05.md` (shared author only).

Five-axis distinction summary: against every neighbour above, **source identity** differs (this paper's `arXiv:2609.36631` appears nowhere else in the checkout), and at least one of **mechanism** (spread-gated cross-side best-quote dynamics feeding a closed-form placement size), **signal construction** (conditional-intensity next-event probabilities plus externally supplied fill probabilities), **universe/market type** (US large-tick equities, single day, top-of-book), **horizon/regime** (millisecond-scale event horizon, single-period, one-tick-gated regime) or **material data dependency** (LOBSTER level-5 order-by-order equities book) differs in every pair.

## Sources

1. Hyoeun Lee and Kiseop Lee, *A Spread-Gated Hawkes-Flocking Model for Best Bid and Ask Dynamics, with an Application to Limit Order Placement*, arXiv:2609.36631v1 [q-fin.CP] (cross-list q-fin.MF), submitted 29 Sep 2026 03:40:21 UTC, manuscript dated 30 Sep 2026, arXiv.org perpetual non-exclusive licence. Landing: https://arxiv.org/abs/2609.36631v1 . PDF (pinned): https://arxiv.org/pdf/2609.36631v1 - 531,062 bytes, SHA-256 `567fc606bf13d48f2761d25f65f6af1931ca9930d46a366e83e7d1c54d62abb6`, 34 pages, fetched 2026-09-30. arXiv-issued DataCite DOI `10.48550/arXiv.2609.36631` (pending registration; no publisher DOI, no journal reference, no Comments field).
2. Data vendor cited **inside** source reference `[15]` (not opened, not used as a claim source here): R. Huang and T. Polak, *LOBSTER: Limit order book reconstruction system*, SSRN Electronic Journal, 2011.
3. Prior work cited **inside** the source for context only (not opened, not used as a claim source here): Zheng, Roueff and Abergel [37]; Jang, Lee and Lee [18]; Lee and Seo [24]; Morariu-Patrichi and Pakkanen [26]; Sfendourakis and Muni Toke [35]; Figueroa-Lopez, Lee and Pasupathy [11]; Lehalle and Mounjid [25]; Guo, de Larrard and Ruan [13]; Self and Liang [34].

No secondary summary, aggregator, SEO page or model-generated digest was used as a source for any claim in this record.
