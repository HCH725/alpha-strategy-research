---
schema: strategy-research-record-v1
title: "Magic-Strike Fair Value of Variance and Gamma Contracts as a Smile-Implied Relative-Value Monitor (arXiv:2609.33913v1)"
created: 2026-09-30
updated: 2026-09-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-30
sources:
  - https://arxiv.org/abs/2609.33913v1
  - https://arxiv.org/pdf/2609.33913v1
  - https://github.com/fbourgey/bergomi-guyon/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Magic-Strike Fair Value of Variance and Gamma Contracts as a Smile-Implied Relative-Value Monitor (arXiv:2609.33913v1)

## Provenance

**Primary source identity**

- Paper: *Magic strikes for variance and gamma contracts, and other attainable claims*.
- Author list exactly as printed on PDF page 1: **Florian Bourgey** (NYU, fb2615@nyu.edu) and **Jim Gatheral** (Baruch College, CUNY, jim.gatheral@baruch.cuny.edu). No other author, no acknowledgements section, no funding statement, no conflict statement, no data-availability statement, no ORCID appear in the pinned text; all stay `data gap`.
- Identifier: `arXiv:2609.33913v1`, primary subject **q-fin.MF only** (no cross-lists), MSC classes 91G20 and 91G60.
- Version/date: **single version v1**, landing submission history `Sun, 27 Sep 2026 20:48:28 UTC (224 KB)`. The PDF first page is dated **September 29, 2026** and the page footer reads `arXiv:2609.33913v1 [q-fin.MF] 27 Sep 2026`, so the printed manuscript date is two days after the recorded submission date; recorded as printed and **not reconciled**.
- Publication status: the landing page carries **no Comments field, no Journal-reference field and no publisher DOI**. The only DOI is the arXiv-issued DataCite DOI `10.48550/arXiv.2609.33913`, whose tooltip reads "arXiv-issued DOI via DataCite (pending registration)". Publication status is therefore **arXiv preprint only; peer review not stated in source** as of 2026-09-30.
- Licence: **CC BY 4.0** (landing-page licence link and licence icon).
- Companion dependency named by the source but **not read in this run**: reference `[BG26] Florian Bourgey and Jim Gatheral. Demystifying the Bergomi-Guyon expansion. SSRN:7468158, 2026`, which supplies the sixth-order Bergomi-Guyon smile expansion, the Mathematica file `aBG.m` and the notebook `MagicStrikes.nb`; its content stays `data gap`.
- Code pointer printed in Section 1: `https://github.com/fbourgey/bergomi-guyon/`. The repository returned **HTTP 200 on 2026-09-30**; it was **not cloned, not read and no commit SHA was pinned**, so immutable code provenance stays `data gap`. No third-party code was executed in this run.

**Pinned artefact (fetched 2026-09-30)**

- `https://arxiv.org/pdf/2609.33913v1`, **715,539 bytes**, SHA-256 `4d50ada580407887bab2792cc7d3570b9cea2303309f34cfb96a8c4d7aee9851`, **19 pages**, extracted with pypdf 6.16.2 to **40,600 characters / 1,602 lines** and **read end to end**: Abstract, Sections 1-6, Equations (1.1)-(4.6), Corollary 2.1, Proposition 2.1, Propositions 3.1-3.4, Lemma 3.1, Theorem 4.1, Corollary 4.1, Algorithm 1, Definition 3.1, Remarks 3.1-3.5 and 4.1, Table 5.1, Table 5.2, Figure 5.1-5.6 captions, footnotes 1-4, the AI Use Disclosure, and the **13-item reference list**.
- `https://arxiv.org/abs/2609.33913v1`, 40,322 bytes, SHA-256 `db722fad0ab14c4160eb6f5d6c23f4c8500da82564503f5bf4d98cc55eca0b2c`, used for dateline, authors, subjects, DOI and licence metadata.
- The submission-history line prints the source package as `224 KB` while the served PDF is 715,539 bytes; the two are **not reconciled** here (different artefacts: e-print source versus rendered PDF).
- This record is **ASCII-only**. The source prints "Alos" and "Radoicic" with diacritics and uses ceiling, square-root and symbol notation; those are transliterated where cited.

**Repository workflow**

- `README.md` read in full (575 lines) on this run.
- Canonical specification resolved from Hermes Wiki Brain **read-only**: `kb_read quant/strategy-research-record-spec-v2.md` returned **file not found**, so the run **failed closed onto `quant/strategy-research-record-spec-v1.md`**, 10,289 bytes, SHA-256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`.
- `git pull origin main` returned `Already up to date` at the start of the run. `git log --oneline -20` was used as a **convenience glance only**, not as dedup.
- Hidden-inclusive pre-write dedup (`rg -uuu` across the whole checkout, including `.git`, `.mimo-worktrees`, `.agents`, `.hermes`): identity tokens `2609.33913`, `Magic strikes`, `fbourgey`, `bergomi-guyon`, `Florian Bourgey`, `variance and gamma contracts` all returned **zero files**; `coverage_manifest.csv` (5,808 rows) returned **0 hits** for `2609.33913|magic strike|bourgey|bergomi` and **0 rows** for `gatheral`; positive control `novy-marx` matched **43 `*.md` files** (46 files including non-markdown) before this write and **44** after it, the delta being this record itself (the control token appears only in this sentence). A second author/cited-work scan for `Jim Gatheral|Masaaki Fukasawa|Rolloos|zero vanna|Chriss-Morokoff` returned only `spy-options-svi-surface-rv-falsification-adverse-selection-2026-09-12.md` and `risk-sensitive-option-market-making-arbitrage-free-essvi-cvar-2026-09-17.md`, neither of which shares this source identity.

**Sample, universe, cost treatment (primary-source checksum fields)**

- **Sample period:** no return sample exists. Model-based tests use **15 evenly spaced maturities between 0.05 and 1.0 years** (Section 5) under two Heston parameter sets and two rough Bergomi parameter sets. Market tests use **four SPX implied-volatility surfaces: 10 February 2025, 4 April 2025, 7 April 2025 and 2 July 2025** (Section 5.3, Figure 5.6).
- **Universe:** SPX index option smile slices (Section 5.3) plus two simulated forward-variance model families of the form (1.1). No individual-equity, futures, crypto or rate option data appears.
- **Transaction cost / slippage treatment:** determined at **Methods level** by reading Sections 1-6 end to end plus a **whole-document census of the pinned 40,600-character text**, which returns **zero** occurrences of `transaction cost`, `trading cost`, `slippage`, `commission`, `bid-ask`, `spread`, `turnover`, `market impact`, `participation`, `latency`, `market order`, `limit order`, `fill model`, `execution`, `borrow`, `short sale`, `margin`, `funding`, `fee`, `capacity`, `liquidity`, `walk-forward`, `deflated`, `Benjamini`, `FDR`, `multiple testing`, `Sharpe`, `PnL`, `profit`, `crypto`, `bitcoin`, `ethereum`, `perpetual`, `arbitrage` and `no-arbitrage`. The only near hits are `leverage` once as the *leverage contract* `L = G - M` (Section 4.2.2), `bid and ask` once in the Figure 5.6 caption (gray shading of Fukasawa bid/ask-smile estimates), `variance swap` and `volatility swap` only inside reference titles, and `Return` once as the keyword of Algorithm 1 line 6. **There is therefore no cost model, no fill model, no execution model and no performance metric of any kind in the source.** Order type, fill price, signal-to-order delay, half-spread crossing, borrow, margin, financing, participation, latency and every capacity limit stay `data gap` and are **never treated as zero**.

## Economic mechanism

### Source-reported

The source is a derivatives-pricing paper, not a trading paper. Its stated mechanism:

- The fair value of a **variance contract** `M(T) = E[<X>_{0,T}]` and of a **gamma contract** `G(T) = E[(S_T/S_0)<X>_{0,T}]` equals a Gaussian-weighted integral of the implied total variance smile in the Fukasawa `z`-coordinate (equations (1.2) and (1.3), the "Fukasawa representations"), which are exact up to interpolation and extrapolation but **require numerical strike inversion over the whole extrapolated smile**.
- Leading-order practitioners' approximations are single-strike: `M(T) ~= sigma_-(0)^2`, `G(T) ~= sigma_+(0)^2` (equation (1.4)); the Rolloos-Arslan rule approximates the volatility contract by `sigma_-(0)`, the implied volatility at the zero-vanna strike. All of these are exact only to first order in the forest expansion and "lose accuracy for the strongly skewed smiles observed in practice".
- The paper's contribution is a family of **fixed-point approximations that read the smile only at a small number of "magic strikes"** `k0 + j*Delta_k` with `k0 = -M/2`, `Delta_k = sqrt(M)` for the variance contract (and `k0 = +G/2`, `Delta_k = sqrt(G)` for the gamma contract), derived from the forest expansion of Alos-Gatheral-Radoicic and the explicit Bergomi-Guyon smile expansion of the companion paper. Explicit formulae are given to **fifth order** for the variance contract (Proposition 3.2), the gamma contract (Proposition 3.3, via the reflection `G[Sigma] = M[Sigma_-]`, Lemma 3.1) and the one-parameter family of European **power payoffs** `e^{p X_{0,T}}`, `p in [0,1]`, of which variance (`p=0`) and gamma (`p=1`) are the endpoints (Proposition 3.4).
- **Theorem 4.1** proves such representations exist at every order for every European claim (growth condition `|g(S_0 e^k)| <= C e^{a|k|}`) and, by extension, for any **attainable** claim (replicable by a fixed European-option portfolio plus a model-free hedge). The abstract states that at order `n`, `2*ceil(n/2)+1` magic strikes suffice.
- **Section 4.3 is a negative theorem**: the **volatility contract** `E[sqrt(<X>_{0,T}>)]` is **not attainable**, and its maturity-`T` smile does not determine the leading correction to the Rolloos-Arslan approximation; the correction (equation (4.6)) is proportional to `rho^2` and vanishes when `rho = 0`.
- Accuracy condition stated by the authors: "the approximations are independent of how the smile is extrapolated beyond them" because the smile is read only within about two standard deviations of `k0`; what the method *does* require is that "the smile be locally polynomial: its accuracy is governed by the quality of the polynomial fit at the magic strikes" (Section 6).

### Research interpretation

Stated as a falsifiable hypothesis, in our words, with every operational choice labelled:

- **Hypothesis (research interpretation):** because the variance- and gamma-contract fair values are recoverable from as few as **one to five listed option quotes per maturity slice** (source-reported strike counts, Remark 3.2), the gap between a *listed* variance/volatility product's quoted price and the magic-strike smile-implied fair value is a **cheap, extrapolation-robust, real-time monitor** whose conditional mean is non-zero and mean-reverting. If that conditional mean is non-zero after half-spread and fees, the deviation is a tradable **relative-value / basis** signal (sell the expensive leg, buy the cheap leg, hold to convergence).
- **Component roles (hybrid):**
  - Signal construction: read total implied variance at the magic strikes of the chosen order and solve the paper's fixed point for `M` or `G` (source-reported formulae).
  - Fair-value leg: the same magic-strike estimate, or the full-surface Fukasawa integral as a cross-check (source-reported benchmark).
  - Observed leg: the quoted price of a listed variance/volatility product (**research-proposed**; the source never names, prices or evaluates any listed product).
  - Entry / exit / sizing thresholds: **research-proposed**, not present in the source.
- The mechanism class is **volatility relative value / pricing-error convergence**, not a risk premium and not a directional forecast. The source claims **no** mispricing, **no** mean reversion and **no** return; those are our hypotheses and must be tested, not assumed.
- A second, purely methodological interpretation is also testable and is separately gated below: that the magic-strike estimator reproduces a full-surface benchmark at materially lower compute while remaining invariant to smile extrapolation.

## Signal

**The source specifies no trading rule.** There is no entry, no exit, no holding period, no sizing, no universe filter and no tradable timestamp anywhere in the pinned text. Everything below is therefore either (a) source-reported *pricing* logic or (b) explicitly `research-proposed` operationalisation.

- **Formation timestamp (source-reported, pricing):** the smile `Sigma(k) = sigma_BS(k,T)^2 * T` for a fixed expiry `T`, assumed known at `t = 0` with `t = 0` set without loss of generality (Section 1). The market application reads each maturity slice's smile on one of four dated SPX snapshots (Section 5.3).
- **Tradable timestamp (research-proposed):** form the estimate at the option chain's official close, compare against the listed product's same-timestamp quote, and act at the next session's opening auction. Not in source.
- **Lookback:** none. The estimator is **single-snapshot**; no rolling window, no warm-up and no history enter the formula. The only "windows" in the paper are numerical, not informational.
- **Signal construction (source-reported, order 1 to 5):**
  - Order 1: `M1 = d0 = Sigma(k0)` with `k0 = -M/2`, `Delta_k = sqrt(M)`, i.e. the single-strike rule; equivalent to `sigma_-(0)^2`.
  - Order 2: `M2 = M*d2 + 0.5*d1^2 + M1`, equivalently the fixed point in equation (3.1): `0.5*Sigma(k0+Delta_k) + 0.5*Sigma(k0-Delta_k) + (1/(8M))*[Sigma(k0+Delta_k) - Sigma(k0-Delta_k)]^2 = M + O(eps^3)`.
  - Orders 3, 4, 5: Proposition 3.2, expressed in the finite-difference stencil `d0..d4` of Definition 3.1 over strikes `k0 + j*Delta_k`, `j in {0,+-1,+-2}`.
  - Gamma: Proposition 3.3, identical algebra with `M -> G`, `d_j -> (-1)^j d_j`, `k0 = +G/2`.
  - Power payoffs: Proposition 3.4 with `k0 = (p - 1/2)*W_p`, `Delta_k = sqrt(W_p)`, `omega = lambda_p * W_p`, `q = 2p - 1`, `lambda_p = 0.5*p*(p-1)`.
  - Stencil parameter `z` (Section 3.4): weights on the five strikes are non-negative iff `z in [sqrt(3)/2, sqrt(3)]` at order 5 and iff `z >= 1` at order 2; the intersection `[1, sqrt(3)]` is why the source fixes `z = 1`.
  - Strike counts actually used (Remark 3.2): **one, two, three, five and five** strikes for `M1..M5`.
  - Each order is a **fixed point**: iterate to convergence in `M` (or `G`, or `W_p`). Iteration count, tolerance and starting value are **not stated in source** -> `data gap`.
- **Long / short entry (research-proposed):** enter the relative-value trade only when `|listed_quote - magic_strike_fair_value|` exceeds a pre-declared threshold; direction is short the over-priced leg and long the under-priced leg. Threshold, band half-width and minimum quote size are `research-proposed`.
- **Exit (research-proposed):** convergence to the band, or expiry of the horizon, or a stop. None is in source.
- **Holding period (research-proposed):** the source gives no horizon; a candidate is a fixed 1-to-20-session hold chosen before testing (`research-proposed`), with a no-retuning rule below.
- **Position sizing (research-proposed):** equal notional per maturity slice or inverse-to-volatility scaling; **not in source**.
- **Re-entry / overlapping positions:** `underspecified` in source and `research-proposed` for any implementation.
- **Fully specified?** The *pricing* rule is fully specified to fifth order (formulae, stencils, strike locations, fixed points). The *trading* rule is entirely `research-proposed`. The record must not be read as a reproducible strategy until the research-proposed layer is fixed and pre-registered.

## Required data

- **Instrument:** index (or single-name) European-style listed options across a full strike-by-maturity grid; plus, for the relative-value use, a listed variance/volatility product with a quoted price at the same timestamp (**research-proposed**; the source names none).
- **Universe:** SPX index options as used in Section 5.3 are the only market universe in the source. Any other universe is a port, not a source result.
- **Venue / market type:** options on a regulated exchange; spot-equivalent underlying for the share-measure reflection. The source does not name a venue, an exchange or a data vendor for the SPX surfaces -> `data gap` (OptionMetrics or similar is **not** stated; do not assume it).
- **Timeframe:** a single snapshot per date for the source; for any implementation, an end-of-day slice plus the next-session execution price (`research-proposed`).
- **Fields:** strike `K`, underlying `S_0`, expiry `T`, bid, ask and mid implied volatility per `(K,T)`, the total-variance smile `Sigma(k)` with `k = log(K/S_0)`, forward/spot inputs, and the discount/forward curve needed to convert to total variance. Greeks are **not** required by the estimator itself (the paper's whole point is to avoid them), but Delta/Gamma are needed for hedging (**research-proposed**).
- **Point-in-time:** quotes must be stamped at their exchange time; the source performs no point-in-time, no look-ahead and no revision audit -> `data gap`. Two of the four SPX dates (4 April and 7 April 2025) sit inside a known high-volatility window, so date selection must be pre-declared to avoid selection on outcomes (`research-proposed`).
- **Timestamp/timezone:** `underspecified` in source; the source gives dates only, no times, no timezone, no candle convention.
- **Missing data / interpolation:** the source **interpolates the smile on each maturity slice** and **extrapolates flat outside the observed log-moneyness range** (Section 5.3); interpolation scheme details (method, node choice) are `data gap`. Stale, suspended or one-sided quotes are unaddressed -> `data gap`.
- **Funding/fee/spread needs:** every one of these is `data gap` in the source and must be supplied by any implementation (`research-proposed`), never assumed to be zero.

## Execution assumptions

Everything in this section is `data gap` in the source except where explicitly marked source-reported.

- **Signal-to-order timing:** `data gap` (source-reported: none).
- **Same-bar / next-bar execution:** `data gap` in source; next-session open is `research-proposed`.
- **Order type:** `data gap`. **Fill model:** `data gap`. **Execution price:** the source prices option portfolios off **mid smiles** (Figure 5.6 caption: "using mid smiles") but never asserts a mid-price fill; a mid fill is an assumption, not a source claim.
- **Fees / spread / slippage / impact / participation / latency:** `data gap`, census-verified zero occurrences.
- **Half-spread:** the only bid/ask information anywhere in the source is the Figure 5.6 **gray shading of Fukasawa estimates from bid and ask smiles**, used as benchmark uncertainty, not as a cost.
- **Borrow / shorting / margin / financing:** `data gap` (single-name short-option positions would require collateral treatment; not addressed).
- **Capacity / liquidity / turnover:** `data gap`; the source reports no turnover of any kind. It does report computational cost: on the same data set, runtimes in seconds on a **MacBook Air M5, 24 GB RAM** were **0.022** for the Fukasawa benchmark and **0.037, 0.049, 0.070, 0.14, 0.19** for orders 1 through 5 (Section 5.3) - i.e. compute, not trading cost.
- **Partial fills / failures:** `data gap`.
- **Conclusion:** the result must **not** be presented as tradable. Any net-of-cost claim is `research-proposed` until measured.

## Evidence

### Source-reported

All figures below are third-party claims from the pinned v1 PDF, each with Table/Figure/Section provenance. **The source reports no return, no Sharpe, no drawdown, no win rate, no PnL and no turnover of any kind**; every number is a pricing-approximation accuracy or runtime figure.

**Model tests (Section 5, Figures 5.1-5.5, Tables 5.1-5.2)**

- Table 5.1 Heston parameter sets: **Set I** `[Ber15, Chapter 6]` `V0 = 0.16`, `V_bar = 0.04`, `lambda = 1.0`, `eta = 0.6`, `rho = -0.8`; **Set II** `[BDDM24]` `V0 = 0.117`, `V_bar = 0.048`, `lambda = 3.37`, `eta = 1.99`, `rho = -0.68`. Model tests use **15 evenly spaced maturities between 0.05 and 1.0 years** (Section 5). Heston variance and gamma contracts have closed forms (Section 5.1).
- Figure 5.1 / Figure 5.4 (magic-strike placement): order-5 variance magic strikes are `k0, k0 +- Delta_k, k0 +- 2*Delta_k` with `k0 = -c_M5/2`, `Delta_k = sqrt(c_M5)`, `c_M5` the fifth-order fixed-point estimate; the paper states the strikes "move further from the money as the volatility-of-volatility and skew increase, but remain well behaved across maturities in both calibrations".
- Figure 5.2 (Heston): "For Set I, orders 2-5 improve substantially on the first-order approximation. Increasing the order does not always improve the estimate, however. In Set II, orders 2 and 3 are more accurate than orders 4 and 5 over much of the maturity range; the latter overestimate both contract values."
- Table 5.2 rough Bergomi parameter sets `[BDDM24]`: **Set I** `H = 0.23`, `eta = 1.5`, `rho = -0.62`; **Set II** `H = 0.11`, `eta = 2.39`, `rho = -0.86`. Simulation: **300 time steps**, **five independent batches of 3x10^5 Monte Carlo paths each**, antithetic variates; the gamma benchmark is Monte Carlo while `M(T) = integral xi_0(u) du` is deterministic (Section 5.2).
- Figure 5.5 (rough Bergomi): "For both parameter sets, orders 2-5 substantially improve on the first-order approximation. The preferred order nevertheless depends on the contract and maturity. For Set II, the fourth-order variance approximation tracks the benchmark particularly closely, whereas the second- and third-order gamma approximations are generally closer to the benchmark than the fourth- and fifth-order estimates. The latter tend to overestimate the gamma contract value at longer maturities." Monte Carlo confidence intervals come from the five batches.

**Market tests (Section 5.3, Figure 5.6)**

- SPX implied volatility surfaces on **10 February 2025, 4 April 2025, 7 April 2025, 2 July 2025**; smile interpolated on each maturity slice and extrapolated flat outside the observed log-moneyness range; benchmark = Fukasawa representations (1.2) and (1.3) on the **same interpolated smile with 10 quadrature nodes**; Figure 5.6 maturity axis spans **0.00 to 2.00 years**.
- "On every slice shown, the magic strikes lie within the quoted strike range, so the magic-strike estimates are independent of the extrapolation choice."
- "On 10 February and 2 July, orders 4 and 5 are closer to the plotted Fukasawa values than orders 2 and 3 for variance, but **lie above the Fukasawa estimates for gamma**. On the two April dates, orders 2-5 are more closely grouped."
- Third-party marks: "The Vola Dynamics 4 marks shown for 2 July 2025 are also in close agreement with the magic-strike estimates"; footnote 4: "We are very grateful to Vola Dynamics for providing their variance and gamma contract marks."
- Runtimes (Section 5.3): **0.022 s** Fukasawa benchmark; **0.037 / 0.049 / 0.070 / 0.14 / 0.19 s** for orders 1-5 (MacBook Air M5, 24 GB RAM).
- Abstract/Section 6 summary claims: "Numerical tests under the Heston and rough Bergomi models demonstrate good accuracy even for strongly skewed smiles, and the method applies directly to interpolated market smiles without strike inversion"; "on SPX market data the method tracks the Fukasawa benchmark."

**Structural / theoretical claims (Sections 2-4)**

- Proposition 2.1: every prefactor in the smile expansion `a_l(k)` is a polynomial in `k` of degree exactly `l`; `F_6` already has **23 trees**; coefficients are supplied explicitly through order 6 in `aBG.m`; `F_6` and the notebook `MagicStrikes.nb` are referenced but not read here.
- Proposition 3.1 (second-order fixed point), Propositions 3.2-3.4 (orders 1-5 for variance, gamma, power payoffs), Lemma 3.1 (`G[Sigma] = M[Sigma_-]`), Section 3.4 (`z in [1, sqrt(3)]`, `z = 1`), Theorem 4.1 and Corollary 4.1 (existence at every order for European and attainable claims).
- Section 4.2.2: leverage contract `L = G - M`; stochasticity contract `zeta = var[X_{0,T}] - E[<X>_{0,T}]^2 = -dW_p/dp |_{p=0}` inherits its magic-strike approximation from the power contract with no new strikes, "at worst the sum of two such errors; the claims themselves being small, the relative error is correspondingly larger".
- Section 4.3: Rolloos-Arslan error `= (eps^2/(2*sqrt(M)))*[-M^2 + (3/4)*(.)^2*M^3] + O(eps^3)`; "Both terms in (4.6) are proportional to `rho^2`, so the second-order correction to the RA approximation vanishes when `rho = 0`. **The smile does not determine this correction** ... no functional of the smile can supply the correction (4.6). In particular, the volatility contract is not attainable."
- Section 4.1: the approximation "fits a polynomial to the smile at the magic strikes and prices the contract as if the smile were that polynomial"; accuracy holds "because, and to the extent that, the smile is locally polynomial".
- AI Use Disclosure: the authors "made extensive use of generative artificial intelligence tools (Claude Opus 5 and Claude Fable 5)" for writing, editing, exploring ideas, proposing proof strategies and checking arguments, and accept full responsibility.
- Publication status: arXiv preprint only (no Comments, no journal reference, no publisher DOI); source-reported, **not independently verified**.

### Independently reproduced

not independently reproduced

Arithmetic-only consistency checks (no source result was reproduced; no source code was run): (1) the Heston closed forms printed in Section 5.1 give `M(1)/T = 0.1159` for Set I and `0.0678` for Set II, and `G(1)/T = 0.0964` for Set I, all inside the printed Figure 5.2 axis ranges (0.10-0.15 variance Set I, 0.04-0.10 variance Set II, 0.08-0.15 gamma Set I); (2) the equation (3.1) fixed point reduces algebraically to `0.5*(Sigma+ + Sigma-) + (Sigma+ - Sigma-)^2/(8M)`, which is exactly `M2` from Proposition 3.2 after `M/Delta_k^2 = 1`, confirming the Remark 3.2 claim that `M2` uses only the two off-centre strikes; (3) `d_-(k) = 0` gives `k = -Sigma(k)/2`, confirming the `k0 = -M/2` variance magic-strike location and `M1 = Sigma(-M/2) = M + O(eps^2)` from Section 3; (4) `sqrt(3)/2 = 0.8660` and `sqrt(3) = 1.7321`, so the intersection of the order-5 and order-2 non-negativity conditions is `[1.0000, 1.7321]` as stated in Section 3.4; (5) rough Bergomi total paths = `5 * 3x10^5 = 1.5x10^6` per parameter set; (6) runtime ratios versus the Fukasawa benchmark: order 1 = 1.68x, order 5 = 8.64x; (7) the abstract's strike count at order 5 is `2*ceil(5/2)+1 = 7` against Remark 3.2's five strikes (see Limitations); (8) all four SPX dates and both April dates confirmed present in Section 5.3.

### Negative evidence

1. **No performance evidence at all.** The source contains zero occurrences of Sharpe, return, PnL, profit, turnover or win rate; nothing supports a profitability claim, and a pricing-accuracy paper is not evidence of a tradable edge.
2. **No cost model of any kind.** Census-verified zero occurrences of transaction cost, slippage, commission, bid-ask cost, spread cost, market impact, participation, latency, order type, fill model, borrow, margin, funding, fee or capacity - so half-spread crossing, fees and impact are entirely unmeasured and must never be treated as zero.
3. **Higher order is not monotone.** Heston Set II: orders 4 and 5 are *worse* than orders 2 and 3 over much of the maturity range and overestimate both contract values (Figure 5.2).
4. **Order choice is contract- and maturity-dependent.** Rough Bergomi Set II: the 4th-order variance estimate tracks best while 2nd/3rd-order gamma beat 4th/5th, and 4th/5th overestimate gamma at long maturities (Figure 5.5) - there is no single defensible default order.
5. **Systematic one-sided market error.** On 2 of the 4 SPX dates, orders 4 and 5 sit **above** the Fukasawa benchmark for the gamma contract (Section 5.3) - a sign-consistent pricing bias at the highest orders, i.e. exactly where an implementation would want accuracy.
6. **The benchmark is itself approximate.** "Truth" is a 10-quadrature-node numerical integral over an *interpolated* smile with *flat extrapolation*; the source never establishes that this benchmark is exact, so all agreement figures inherit benchmark error.
7. **Only four dated snapshots.** Four SPX days in 2025 (two inside the April 2025 drawdown window), no time series, no rolling out-of-sample, no regime split, no cross-market replication.
8. **Quoted-range dependence is asserted only for shown slices.** "On every slice shown" is a claim about displayed figures; the paper separately notes that going to higher orders "typically introduces strikes outside the listed range", which in live data means unquotable or interpolated strikes.
9. **The locally-polynomial condition has no live diagnostic.** The authors state accuracy is governed by the quality of the polynomial fit at the magic strikes, but supply no ex-ante test for when the fit fails on live data.
10. **The volatility contract is proven un-priceable from the smile.** Section 4.3 shows the Rolloos-Arslan correction is not determined by the maturity-`T` smile; any strategy that prices or trades a volatility contract off the smile alone is resting on a result the source itself disproves.
11. **Model class is narrow.** All tests are forward-variance models of form (1.1): no stochastic rates, no dividends, no jumps, no basis between spot and forward, no term-structure dynamics of the forward variance curve validated on market data.
12. **Mid-smile input.** Estimates use mid smiles; a mid is not an executable price, and bid/ask is used only to shade the benchmark band.
13. **Third-party marks are not reproducible.** The Vola Dynamics marks for 2 July 2025 were provided by the vendor (footnote 4) and cannot be re-derived from the pinned text.
14. **Strike-count count is not reconciled.** The abstract says `2*ceil(n/2)+1 = 7` strikes suffice at order 5, Section 4.2.1 says "any `n+1` of them reconstruct the polynomial" (6 at order 5), and Remark 3.2 says the constructed `M5` uses **five** strikes from `{k0, +-Delta_k, +-2*Delta_k}`; the text does not reconcile the three counts (see Limitations - recorded as underspecified, not adjudicated here).
15. **Unstated fixed-point numerics.** Iteration count, convergence tolerance, starting value and handling of non-convergence are `data gap`, so "fifth-order accuracy" is not operationally pinned.
16. **Companion-paper dependency not read.** The sixth-order Bergomi-Guyon expansion, `aBG.m` and `MagicStrikes.nb` live in reference `[BG26]` (SSRN:7468158) and were not opened in this run; the derivation's upper orders are therefore unverified here.
17. **Code not pinned and not executed.** The GitHub repository returned HTTP 200 but has no commit SHA pinned in this record and was never read; there is no replication package statement in the paper.
18. **Preprint-only, two days old at capture.** v1 submitted 27 Sep 2026, manuscript dated 29 Sep 2026, captured 30 Sep 2026; no Comments, no journal reference, no publisher DOI, DataCite DOI "pending registration"; peer review not stated in source.
19. **Single-version, single-author-pair, heavy AI assistance disclosed.** Two authors, one version, and an explicit statement of extensive generative-AI use for writing, proof strategy and argument checking.
20. **No evidence that any deviation is exploitable.** The source never prices a listed product, never measures a deviation, never tests convergence and never models the frictions that would consume it; the relative-value hypothesis is entirely ours to prove or refute.

## Falsification plan

Every threshold below is `research-defined` (a Scout-chosen acceptance/failure cutoff), and every operational rule is `research-proposed`. Failure action is pre-declared; **no gate may be rescued by retuning** (see the no-retuning rule).

- **F1 - Printed-value reproduction gate.** Recompute, from pinned SPX slices for 10 Feb, 4 Apr, 7 Apr and 2 Jul 2025, the magic-strike estimates at orders 1-5 and the 10-node Fukasawa benchmark. *Fail if* any of the 4 dates x 2 contracts has `|M5 - Fukasawa| / Fukasawa > 0.05` (research-defined 5%). *Action:* stop; treat the estimator as non-reproducible and drop the candidate.
- **F2 - Heston closed-form gate.** Recompute orders 1-5 against the closed-form `M(T)`, `G(T)` of Section 5.1 across the 15 maturities for both parameter sets. *Fail if* median relative error for orders 2-3 exceeds 1% (research-defined) in either set. *Action:* reject the fixed-point implementation before any market test.
- **F3 - Rough-Bergomi Monte-Carlo gate.** Reproduce Figure 5.5 with 5 batches of 3x10^5 paths, antithetic, 300 steps. *Fail if* order-2/3 estimates fall outside the printed 95% batch interval in more than 2 of 4 panels (research-defined). *Action:* stop.
- **F4 - Pre-declared order gate.** Fix a single order **before** market testing (baseline: order 3, chosen because the source itself shows orders 4-5 are not monotonically better). *Fail if* the pre-declared order is changed after seeing market results. *Action:* invalidate the run, restart from a new pre-registration.
- **F5 - Extrapolation-invariance gate.** Re-run all slices with three extrapolations (flat, linear, skewed-SVI tail) and two interpolations. *Fail if* the magic-strike estimate moves by more than 1% (research-defined) whenever all magic strikes lie inside the quoted range; separately *fail if* magic strikes fall outside the quoted range on more than 5% of slices (research-defined). *Action:* mark the monitor as unusable for live quotes.
- **F6 - Benchmark-uncertainty gate.** Recompute the Fukasawa benchmark at 10, 100 and 1000 quadrature nodes and on bid versus ask smiles. *Fail if* the trading signal is smaller than the benchmark's own bid-to-ask band (research-defined: signal must exceed the band). *Action:* the edge is inside measurement noise; reject.
- **F7 - Executable-price gate.** Re-price every leg at touch (or at the next session's open) instead of mid. *Fail if* the deviation shrinks by more than 50% relative to mid (research-defined). *Action:* the effect is a spread artefact; reject.
- **F8 - Cost ladder gate.** Apply 0, 1, 2, 5, 10, 20 and 50 bps per side plus a half-spread. *Fail if* mean net deviation (research-defined: net-of-cost edge) is not strictly positive at 10 bps and the ordering of net edges is not monotone in cost. *Action:* reject as non-tradable.
- **F9 - Listed-product convergence gate (the core alpha test).** With a fixed band and a fixed 1-to-20-session horizon (`research-proposed`), require that deviations signed toward the magic-strike fair value revert by at least 50% of the initial gap (research-defined) in at least 60% of episodes (research-defined), over at least 100 independent episodes. *Fail if* either condition is missed. *Action:* reject the relative-value hypothesis; keep only the pricing-estimator claim.
- **F10 - Volatility-contract prohibition gate.** Any variant that prices or trades the **volatility contract** from the smile alone must be discarded *a priori*, because Section 4.3 proves the smile does not determine the correction. *Fail if* such a variant appears in any tested spec. *Action:* remove; the source's negative theorem is binding.
- **F11 - Locally-polynomial diagnostic gate.** Pre-register a fit-residual statistic at the five magic strikes (e.g. degree-4 least-squares residual of `Sigma(k)`). *Fail if* episodes with a residual above the pre-declared cutoff behave no better than the rest (research-defined cutoff: median net edge of the clean subset must exceed that of the full set). *Action:* abandon the estimator as a live monitor.
- **F12 - Multiple-testing control.** Across all (order x contract x maturity x date x cost) cells, apply Benjamini-Hochberg at `q < 0.10` (research-defined) and report a deflated Sharpe over the full comparison family if any return series is produced. *Fail if* no cell survives. *Action:* report as null.
- **F13 - Regime / date-selection gate.** Split pre-declared as 10 Feb vs the two April dates vs 2 Jul, and repeat with an additional set of at least 20 further dates chosen by a rule fixed in advance (e.g. all third-Friday expiries in a fixed window). *Fail if* the sign of the mean deviation flips across the pre-declared splits (research-defined). *Action:* reject generalisation; retain only a date-conditional claim.
- **F14 - Frozen forward window.** Freeze every parameter on or before 2026-09-30 and evaluate on data from 2026-10-01 forward for at least 12 months (`research-defined` horizon). *Fail if* the forward net edge is non-positive. *Action:* terminal reject for adoption purposes.

**No-retuning rule:** the order, the stencil `z = 1`, the strike locations `k0 = -M/2` (variance) and `k0 = +G/2` (gamma), `Delta_k = sqrt(M or G)`, the interpolation/extrapolation choices, the band, the horizon and every threshold above are frozen at first run. A failed gate is reported as failed; parameters may not be changed to rescue it. Any change starts a new, separately labelled experiment.

**Ablations for the estimator claim:** order 1 (single strike) vs order 2 vs order 3 vs order 5; magic-strike estimator vs full-surface Fukasawa integral vs a calibrated-model price; variance contract vs gamma contract; mid vs bid vs ask input.

## Crypto portability

`adapted` - mechanics port, evidence does not; **crypto performance unproven**.

- The estimator is instrument-agnostic: any liquid **European** option smile supplies `Sigma(k)`, and Deribit/OKX/Binance BTC and ETH option chains are European, so the magic-strike computation itself ports unchanged.
- **There is no listed crypto variance or gamma contract** to serve as the observed leg of the relative-value trade. Crypto offers perpetual funding, variance-proxy perps and basket/vol products on some venues, none of which is a variance contract quoted off the same smile; the "listed leg" would have to be synthesised (synthetic variance note, or a realized-volatility proxy), which changes the payoff and is `research-proposed`, not source-supported.
- 24/7 sessions, candle boundaries and timestamp alignment differ from the SPX four-date snapshots; no session/rollover convention is in source.
- Venue fragmentation: BTC/ETH smiles differ materially across Deribit, OKX and Binance; cross-venue basis and index/mark-price definitions are unmodelled in the source.
- Funding, margin and liquidation affect any hedged implementation but are absent from the source (`data gap`).
- Liquidity and open interest in far wings are thin, so magic strikes two standard deviations from the money may be unquotable far more often than in SPX options.
- Survivorship/listing churn and the absence of a single benchmark index are unaddressed.
- Because the source contains **zero** crypto content (census: `crypto`, `bitcoin`, `ethereum`, `perpetual` all zero), crypto use must be labelled `adapted` with `unproven` performance, never `direct`.

## Limitations

- `underspecified`: fixed-point iteration count, tolerance, starting value and non-convergence handling.
- `underspecified`: interpolation method on each maturity slice; flat extrapolation is stated, its alternatives are not.
- `data gap`: venue, data vendor, quote times and timezone for the four SPX dates.
- `data gap`: discount/forward curve construction; the source writes total variance directly and never shows the forward extraction.
- `data gap`: every execution, cost, capacity and borrow field (census-verified).
- `not independently reproduced` for all source results; only arithmetic cross-checks were run.
- `unproven`: the relative-value hypothesis itself - the source neither states nor tests it.
- The strike-count tension (abstract `7`, Section 4.2.1 `n+1 = 6`, Remark 3.2 `five` for `M5`) is recorded as **underspecified and not adjudicated** in this run; it is not asserted as a proven contradiction, and `contested` therefore stays `false`.
- Validation is four dated snapshots plus simulated models; there is no time series, no out-of-sample test, no walk-forward, no point-in-time audit and no multiple-testing control in the source.
- Companion paper `[BG26]` and the Mathematica artefacts were not read; upper-order derivations rest on an unverified dependency.
- Publication status is preprint-only with an AI-use disclosure; acceptance claims are absent rather than false.
- This record does not modify any engine, does not run backtests, and does not download market data.

## Implementation status

`not-implemented`.

Nothing has been implemented in our research stack. No estimator code was written or run, no third-party code (including `github.com/fbourgey/bergomi-guyon`) was executed, no market data was downloaded, no backtest was performed, and no Qlib, Paper, Testnet or Live verification of any kind occurred. The only executable artefacts produced by this run were arithmetic-only cross-checks of printed closed forms.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

The presence of this record in the repository means only that a normalised research capture exists. It does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; or approved for live trading. No wording, evidence count or gate count in this record promotes it.

## Related Wiki records

Adjacent concepts located by read-only `kb_search` in Hermes Wiki Brain (three queries; one returned a single adjacent page, one returned verified neighbours, one returned **zero** pages and was not used to fabricate a link). No Wiki page was written by this run.

- [[quant/spy-options-svi-surface-rv-falsification-adverse-selection-2026-09-12]] - nearest neighbour: option-smile relative value with explicit adverse-selection and friction falsification on SPX/SPY options.
- [[quant/nuclear-energy-equity-options-short-put-variance-risk-premium-2026-09-02]] - variance-risk-premium harvesting via option selling; complements, does not overlap, this pricing-estimator mechanism.
- [[quant/equity-index-dispersion-correlation-risk-premium-spread-friction-falsification-2026-09-13]] - index-option relative-value with realised-spread friction falsification.
- [[quant/defi-cfmm-intrinsic-liquidity-carr-madan-delta-hedge-2026-09-01]] - model-free option spanning and delta-hedged valuation, related in method.

Repository neighbours with a **different source identity and a different mechanism** (linked for reviewer orientation, not as Wiki links): `spy-options-svi-surface-rv-falsification-adverse-selection-2026-09-12.md`, `risk-sensitive-option-market-making-arbitrage-free-essvi-cvar-2026-09-17.md`, `perpetual-variance-swap-optimal-entry-exit-hypergeometric-stopping-2026-09-17.md`, `taming-the-greeks-option-inductive-bias-delta-penalty-arxiv-2609.33767-2026-09-29.md`, `option-implied-tail-factor-zoo-ds-lasso-arxiv-2609.31263-2026-09-28.md`.

## Sources

1. Florian Bourgey and Jim Gatheral, *Magic strikes for variance and gamma contracts, and other attainable claims*, arXiv:2609.33913v1 [q-fin.MF], submitted 27 Sep 2026, manuscript dated 29 Sep 2026, CC BY 4.0. Landing: https://arxiv.org/abs/2609.33913v1 . PDF (pinned): https://arxiv.org/pdf/2609.33913v1 - 715,539 bytes, SHA-256 `4d50ada580407887bab2792cc7d3570b9cea2303309f34cfb96a8c4d7aee9851`, fetched 2026-09-30. DataCite DOI `10.48550/arXiv.2609.33913` (pending registration; no publisher DOI, no journal reference).
2. Companion repository named in Section 1 of the paper: https://github.com/fbourgey/bergomi-guyon/ - HTTP 200 on 2026-09-30, not cloned, not read, no commit SHA pinned.
3. Companion paper cited by the source as reference `[BG26]`: Florian Bourgey and Jim Gatheral, *Demystifying the Bergomi-Guyon expansion*, SSRN:7468158, 2026 - **not read in this run**; cited only as the source's own dependency.

No secondary summary, aggregator, SEO page or model-generated digest was used as a source for any claim in this record.
