---
schema: strategy-research-record-v1
title: "Retained Hidden Excess Generates Memory in Price-Limited Markets: Next-Day Same-Sign Response, Same-Limit Persistence, and Reversal Suppression (NSE Evidence)"
created: 2026-09-11
updated: 2026-09-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - price-limits
  - circuit-breakers
  - limit-up-limit-down
  - latent-state-model
  - heavy-tails
  - order-flow
  - market-microstructure
  - next-day-return-predictability
  - nse-india
status: research-only
confidence: medium
source_as_of: 2026-08-09
sources:
  - "Debraj Das, 'Retained hidden excess generates memory in price-limited markets', arXiv:2608.08625v1 [cond-mat.stat-mech; q-fin.TR], submitted 9 August 2026, 15 pages, 7 figures. https://arxiv.org/abs/2608.08625"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Retained Hidden Excess Generates Memory in Price-Limited Markets: Next-Day Same-Sign Response, Same-Limit Persistence, and Reversal Suppression (NSE Evidence)

## Provenance

- **Primary Source:** Debraj Das (SISSA – International School for Advanced Studies, Trieste, Italy; Istituto dei Sistemi Complessi, Consiglio Nazionale delle Ricerche, Sesto Fiorentino, Italy), *"Retained hidden excess generates memory in price-limited markets"*.
  - arXiv preprint `arXiv:2608.08625v1 [cond-mat.stat-mech; q-fin.TR]`, submitted 9 August 2026 (v1 is the only version in the submission history as of this capture; 15 pages, 7 figures) (`source-reported`).
  - Stable arXiv URL: https://arxiv.org/abs/2608.08625
  - Stable versioned PDF: https://arxiv.org/pdf/2608.08625v1
  - Canonical DOI: [10.48550/arXiv.2608.08625](https://doi.org/10.48550/arXiv.2608.08625)
  - **Publication status:** preprint; no journal reference and no peer-review status are indicated on the landing page as of 2026-09-11 (not peer-reviewed by our standard; source-quality caveat) (`source-reported`).
- **Primary-source verification (performed 2026-09-11 against arXiv landing page + v1 PDF):** author list (single author, Debraj Das — exactly as on source), v1 date (9 Aug 2026), sample period (NSE stocks, November 2007 – June 2026), universe (NSE equities subject to exchange-set daily price bands; base universe of 757 symbols after band-history consistency filtering), transaction-cost treatment (**none modeled or stated anywhere in the paper** — verified by reading the model, data-processing, and appendix sections; no fee/slippage/spread/fill model), core numbers (λ_eff ≈ 0.942; 217/1494 pooled 20% persistence; ν = 3 benchmark; Table III counts), publication status (preprint, no journal ref). No field in this record is sourced from a secondary summary.
- **Data provenance (source-reported):** NSE (National Stock Exchange of India) daily OHLC, volume, and previous-close data obtained from NSE public data archives via the `nselib` Python package; per-symbol price-band ("circuit limit") change disclosures consolidated from 31 October 2007; corporate-action disclosures (bonus issues and stock splits, with ex-date and terms); index data (13 global indices, January 1990 – June 2026, start dates vary by availability) from Yahoo! Finance. The paper states the data are available from the author upon reasonable request — no public data deposit (**data gap**).
- **Repository Deduplication:** Full-repository search (all `*.md` records) for `arXiv:2608.08625`, the DOI, the exact title, "Debraj Das", "retained hidden excess", and "price-limited" found **zero** prior captures. No `coverage_manifest.csv` row covers this source. Adjacent but distinct prior records exist on price-limit *related* topics (China A-share limit-up data contamination; crypto liquidation cascades) and are cited under Related Wiki records; none captures this mechanism, source identity, or signal.

## Economic mechanism

### Source-reported

1. **Clipping creates a hidden excess.** A daily exchange-imposed symmetric price band clips the latent (unconstrained) return $X_t$ at $\pm C$ (return units), so the realized return is $R_t = \mathrm{clip}(X_t, -C, C)$ (Eq. 1). The part removed by clipping is the *hidden excess* $L_t = X_t - R_t$, nonzero only when $|X_t| > C$ (Eq. 2). An upper-limit close ($R_t = +C$) conceals unresolved excess demand; a lower-limit close ($R_t = -C$) conceals unresolved excess supply; the observed close reveals direction but not magnitude (`source-reported`).
2. **Retention converts clipping into memory.** The central hypothesis: a fraction of the hidden excess survives the close and enters the next day's latent return, $X_{t+1} = \epsilon_{t+1} + \lambda L_t$ with i.i.d. daily driving shocks $\{\epsilon_t\}$ and retention coefficient $0 \le \lambda < 1$ (Eq. 3). The hidden excess is the *only* source of temporal coupling: when nothing is clipped, the next latent return is just the independent shock. $\lambda = 0$ reduces the model to independent shocks (`source-reported`). Hence $E[X_{t+1} \mid X_t] = \lambda L_t$: a limit close implies a same-signed conditional drift the next day even though fresh shocks are symmetric and independent (Sec. II).
3. **Heavy tails.** Driving shocks are symmetric with regularly varying tails (finite first moment, no specific form imposed). The stationary latent return preserves the shock tail index $\nu$ but with enhanced far-tail amplitude; the tail behavior is retention-dependent (Sec. III, App. A) (`source-reported`).
4. **Wide-band single-dominant-shock description.** For large $C$, a limit close is attributed to a single dominant extreme shock, characterized by its age $j$ and threshold-exceedance ratio $V \ge 1$ (Pareto-distributed with survival $V^{-\nu}$ in the wide-band limit, Eq. 17–19); the accumulated amplitude $A_j \equiv \sum_{m=0}^{j} \lambda^m$ transforms the overshoot into the current latent state, $X_t \simeq C[1 + A_j(V-1)]$ (Eq. 20–21) (`source-reported`).
5. **Next-day predictions (Sec. V).** Conditional mean responses $m_+(C) \equiv E[R_{t+1} \mid X_t \ge C]$ and $m_-(C) \equiv E[R_{t+1} \mid X_t \le -C]$ (Eq. 22–23). In the wide-band limit, the normalized response converges to a finite nonzero constant, $m_+(C)/C \to M(\lambda,\nu)$ with $m_-(C)/C \to -M(\lambda,\nu)$ by symmetry (Eq. 24–28). $M(\lambda,\nu)$ increases with retention $\lambda$ and tail heaviness $\nu$; in the small-$\lambda$ limit $M(\lambda,\nu) \sim \lambda/(\nu-1)$, so there is **no finite retention threshold**: any nonzero retained fraction produces a positive mean next-day return after an upper-limit close (negative after a lower-limit close) (`source-reported`).
6. **Persistence–reversal asymmetry (Sec. V).** Same-limit persistence probability $P_{++}(C) \equiv \Pr(X_{t+1} \ge C \mid X_t \ge C) \to 1 - \pi_0$ (a finite $O(1)$ limit equal to the total weight of nonzero-age histories, Eq. 31–32), whereas an opposite-limit reversal $P_{+-}(C)$ requires a *second* independent extreme shock and is power-law suppressed, $P_{+-}(C) \sim k C^{-\nu}\Psi(\lambda,\nu)$ (Eq. 33–34). O(1) persistence versus algebraic suppression of reversal is the model's sharpest testable signature (`source-reported`).
7. **NSE data (Sec. VI).** On NSE stocks (Nov 2007 – Jun 2026), upper-limit closes are followed on average by positive next-day returns and lower-limit closes by negative ones across all bands $C \in \{2\%, 5\%, 10\%, 20\%\}$; magnitudes grow with $C$; a single effective retention coefficient does not reproduce the full band and directional dependence (details in Evidence).

### Research interpretation

- **Falsifiable alpha hypothesis:** a public, mechanically defined event (a close at the exchange's daily return band) carries one-sided latent imbalance information whose expected effect on the next close-to-close return is same-signed and increasing in the band width. The mechanism is *delayed price adjustment under a binding constraint* — not trend, not mean reversion, not momentum in the usual sense. If true, it is a cross-sectional, event-driven return-predictability channel (`research-proposed` interpretation of source claims).
- **Two separable deployable statements:** (i) conditional mean drift (direction and band-width scaling), usable as a directional signal for the day after a limit event; (ii) the persistence/reversal asymmetry (O(1) vs power-law-suppressed), which is a state-transition statement about the *next* limit close and is more naturally used for position management (e.g., avoiding counter-limit positioning) than for raw return capture (`research-proposed`).
- **Complementary, not overlapping, with prior captures:** the existing China A-share record in this repository treats limit days as *contamination* (unexecutable prints biasing factors); Das (2026) instead treats the limit event as a *predictive signal carrier*. Same institutional feature, opposite research use (`research-proposed` distinction).
- **Calibration caveat carried forward:** the source's own calibration shows one effective parameter misprices band and direction dependence; the honest claim is a signed, band-monotone effect — not a precise expected return (`source-reported` mismatch; interpretation by us).

## Signal

### Source-reported event definition and statistics

- **Band state:** for a symbol-day with a numeric band $C\%$ in force, applicable limits are $U_t = S_{t-1}(1 + C/100)$ and $D_t = S_{t-1}(1 - C/100)$ relative to the previous close $S_{t-1}$ taken from the exchange record (Eq. C1). NSE fixes $C \in \{2\%, 5\%, 10\%, 20\%\}$ (also a no-band state exists in the disclosures).
- **Event classification:** day $t$ is an upper-circuit day if $S_t \ge U_t(1-\tau)$ and a lower-circuit day if $S_t \le D_t(1+\tau)$, with tolerance $\tau = 0.25\%$; the criterion is one-sided (no bound on how far the close may exceed the nominal limit, because the exchange occasionally revises a band intraday after the limit is first reached) (`source-reported`, Sec. C1).
- **Measured statistics:** empirical conditional means $\hat m_+(C) = \langle R_{t+1} \mid \text{upper circuit at } t \rangle$, $\hat m_-(C)=\langle R_{t+1} \mid \text{lower circuit at } t\rangle$ with $R_{t+1}$ the close-to-close return on the next trading day, plus the empirical frequency of same-direction recurrence (persistence) and opposite-direction recurrence (reversal) (Eq. C2–C3, App. C) (`source-reported`).
- **Timescale:** everything is defined at daily closes; the model deliberately does not resolve the intraday path or the time at which the limit was reached (Sec. II) (`source-reported`).

### Operationalization

The source does **not** define a trading strategy (no entry, exit, holding, sizing, or execution rules) — as a trading signal the specification is **underspecified**. The following operational choices are ours and are `research-proposed`:

- **Entry (research-proposed):** after observing a limit close at day $t$, take a one-day position in the direction of the limit (long after an upper-limit close; short after a lower-limit close). The source's statistics map most cleanly to close$(t)$ → close$(t+1)$; entering at the next session's open is an alternative that must be tested separately (see Execution assumptions and Falsification plan).
- **Exit (research-proposed):** at the next session close (exactly one trading day), matching the horizon of the source's measured statistic.
- **Holding period (research-proposed):** 1 trading day; no multi-day extension is justified by the source's next-day-only derivations. Successive limit closes in the same direction should be netted or counted as separate events consistently; re-entry rules are unspecified (`underspecified`).
- **Band stratification (source-reported scaling / research-proposed selection):** expected effect magnitude increases with $C$; which bands to trade (e.g., exclude the smallest band given the source's own narrow-band failure) is a research-proposed filter.
- **Position sizing (research-proposed):** flat notional per event for event-study evaluation (no compounding, no scaling by band width) until a calibrated expected-magnitude mapping is established.
- **Directional asymmetry (source-reported observation):** empirically the lower-limit response is stronger (mechanical selling/panic channel); a direction-dependent treatment may be warranted — left as an empirical question (`research-proposed`).

## Required data

- **Instrument / universe (`source-reported`):** NSE-listed equities subject to exchange-set daily price bands; base universe of $N_{sym} = 757$ symbols after requiring internally consistent per-symbol band-change histories; final analysis sample of 898,689 daily observations after sequential exclusions (Table I).
- **Venue / market type (`source-reported`):** National Stock Exchange of India, cash equities (spot), daily bars.
- **Fields (`source-reported`):** daily open, high, low, close, volume, previous close (unadjusted for corporate actions as reported by the exchange); per-symbol band-change disclosure history (from 31 October 2007); corporate-action records for bonus issues and stock splits (ex-date and terms).
- **Timeframe (`source-reported`):** daily close-to-close.
- **Point-in-time / availability (`source-reported`):** band values must be reconstructed from the exchange's discrete band-change disclosures; the state after one event must equal the state before the next, else the symbol is excluded entirely. Band revisions can occur intraday (the paper documents exchange-sanctioned intra-band trading beyond the nominal limit). The next-day observation must be the symbol's next actual trading record.
- **Missing-data handling (`source-reported`):** five sequential exclusions — (1) price below INR 10; (2) next record more than 4 calendar days later or absent; (3) band on the following day differs from event day; (4) bonus/split ex-date coincides with observation day or next day; (5) residual band exceedance beyond an additional $0.01C$ tolerance.
- **Costs / funding / borrow (`data gap`):** no fee, spread, slippage, market-impact, funding, or borrow data are required or modeled by the source. For a tradable test on Indian equities, borrow availability for shorting after lower circuits (SLB) and fee/spread/slippage parameters must be added by us (`research-proposed`).
- **Crypto:** no source-specified data mapping exists; a ported test would need a venue with an analogous hard daily constraint or a redefinition of the "close" boundary (see Crypto portability) (`research-proposed`).

## Execution assumptions

- **Source:** none stated. The measured objects are close-to-close returns, gross of all frictions; the paper contains no fill model, no order type, no latency, no capacity and no tradeability discussion (verified across model, results, and appendix sections) (`data gap` / `underspecified`).
- **Structural fillability risk (`research-proposed`):** after a limit close, next-session entry may be impossible or adverse — a stock can open at or beyond a new limit with insufficient opposing liquidity, and the exchange may revise bands intraday. A next-day open-entry variant can therefore partially or fully lose the theoretical edge; this must be measured, not assumed. (Our repository's China A-share record documents the analogous unfillability mechanism for limit-up names.)
- **Test design (`research-proposed`):** entry via next-session market (or marketable limit) order at open and, separately, at prior-day close where achievable; round-trip costs to be stressed at Indian cash-equity levels including brokerage, exchange fees, STT, stamp duty and 0.1–0.3% slippage for mid/small caps; shorts after lower circuits flagged as constrained by SLB availability.
- **Capacity (`research-proposed`):** band events concentrate in smaller/less liquid names (the source's INR 10 floor removes a deep-penny regime); capacity must be bounded by event-day liquidity, and the strategy is not assumed to be scalable.

## Evidence

### Source-reported

1. **Sample and universe (Sec. VI, App. C, Table I):** NSE stocks, November 2007 – June 2026; 757-symbol base universe; 1,163,004 initial observations reduced by five exclusions to 898,689 (Table I: 1,046,516 after low-price; 1,040,234 after trading-continuity; 922,417 after fixed-band; 922,219 after corporate-action; 898,689 after residual band-exceedance).
2. **Parameters fixed without fitting the response (Sec. VI, App. D, Fig. 7, Table II):** tail index fixed at $\nu = 3$, chosen from standardized daily returns of 13 major global equity indices January 1990 – June 2026 (per-index MLE Student's $t$ degrees of freedom range 2.41–3.99, unweighted mean 3.15; Kolmogorov–Smirnov distance ≤ 0.029; moving-block bootstrap $B=2000$, block 20 days). The retention coefficient is estimated from the pooled same-limit persistence at the widest band only: at $C = 20\%$, 217 of 1,494 upper/lower limit closes are followed by another close at the same limit; solving $1-\pi_0(\lambda_{eff}, 3) = 217/1494$ gives $\lambda_{eff} \approx 0.942$ (interpreted by the author as an effective aggregate parameter, not a microscopic retention fraction).
3. **Sign prediction (Sec. VI, Fig. 6):** at every band $C \in \{2\%, 5\%, 10\%, 20\%\}$, the empirical conditional means have the signs predicted by the model — positive next-day return after upper-limit closes, negative after lower-limit closes.
4. **Scale and shape (Sec. VI, Fig. 6):** the theory captures the overall scale and the increase of the mean response magnitude with $C$; agreement is closest near $C = 10\%$; the largest *relative* discrepancy is at the narrowest band $C = 2\%$ (consistent with failure of the wide-band criterion there); at $C = 20\%$ the empirical upper-limit-close response lies substantially below the theoretical prediction (largest absolute discrepancy).
5. **Persistence counts and probabilities (Table III):**

   | Band $C$ | $N_+$ | $N_{++}$ | $P^{emp}_{++}$ | $N_-$ | $N_{--}$ | $P^{emp}_{--}$ | $P^{emp}_{pers}$ |
   | :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
   | 2% | 83 | 62 | 0.7470 | 144 | 117 | 0.8125 | 0.7885 |
   | 5% | 11129 | 5153 | 0.4630 | 8696 | 3724 | 0.4282 | 0.4478 |
   | 10% | 1542 | 387 | 0.2510 | 623 | 192 | 0.3082 | 0.2674 |
   | 20% | 1230 | 163 | 0.1325 | 264 | 54 | 0.2045 | 0.1452 |

   (Directional persistence estimates are not identical, especially at wider bands; the pooled value is a model-based aggregate.)
6. **Theoretical persistence ceiling (Sec. VI, App. E):** for $\nu = 3$, the wide-band asymptote bounds persistence by $Q_{max}(3) \approx 0.1681$. The pooled persistence at $C = 2\%, 5\%, 10\%$ *exceeds* this bound and cannot be described by the large-$C$ asymptote for any admissible $\lambda$; only the 20% band is admissible for the $\lambda$ inversion. Even at 20%, the lower-limit estimate $P^{emp}_{--} = 0.2045$ remains above the symmetric-model ceiling.
7. **Simulations (Sec. IV–V, Figs. 4–5, App. B):** stationary trajectories of length $10^{10}$ with Student's $t$ driving shocks confirm the scaling $m_+(C) \sim C\,M(\lambda,\nu)$ (Fig. 4(a), $\lambda=0.5$), the growth of the normalized response with $\lambda$ and $\nu$ (Fig. 4(b)), $P_{++}(C) \to 1-\pi_0$ and $P_{+-}(C) \sim C^{-\nu}$ (Fig. 5, $\lambda \in \{0.4, 0.6, 0.8\}$, $\nu = 3.5$).

### Independently reproduced

- Not independently reproduced.

### Negative evidence

1. **Calibration failure across bands and directions (source-reported):** a single effective retention coefficient does not reproduce the complete band and directional dependence of the empirical means; the author states this explicitly.
2. **Directional asymmetry above the symmetric model's ceiling (source-reported):** lower-limit persistence at the 20% band (0.2045) exceeds the theoretical upper bound $Q_{max}(3) \approx 0.1681$; the symmetric i.i.d. formulation cannot accommodate it. The author attributes this to mechanically forced selling (panic, margin calls, liquidations) making downward memory stronger than upward.
3. **Narrow-band failure (source-reported):** pooled persistence at $C = 2\%, 5\%, 10\%$ exceeds the wide-band admissibility bound, i.e., the theory's own calibration window excludes three of the four bands; the $C=2\%$ response also shows the largest relative discrepancy.
4. **No cost, execution, or fillability analysis (source-verified omission):** results are gross close-to-close statistics; the structural unfillability of limit-event days (a well-known mechanism, documented in our China A-share staging record) is not addressed and remains a first-order risk to any tradable claim.
5. **Data not publicly deposited (source-reported):** "available from the author upon reasonable request"; reconstruction depends on `nselib` against NSE archives and on band-record consistency — a stale-record artifact class was explicitly identified and excluded (low-price regime), indicating reconstruction fragility.
6. **No inferential statistics on the mean responses in the text (source-reported):** band-wise empirical means are shown graphically (Fig. 6, box plots and jittered points); the main text does not report per-band standard errors or significance tests for $\hat m_\pm(C)$.
7. None else identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

All thresholds below are ours (`research-defined falsification threshold`); the source defines no acceptance criteria:

1. **Sign replication (out-of-sample).** Protocol: event study on NSE (or another banded market) with the source's classification rules, restricted to an out-of-sample period (e.g., 2015–2026, or a held-out half split by symbol). Metric: mean next-day close-to-close return after upper-limit closes. Fail if the mean is ≤ 0 with one-sided t-test p < 0.05, or if the lower-limit mirror (mean ≥ 0) holds, at any of the admissible bands (`research-defined falsification threshold`).
2. **Band-width scaling.** Protocol: regression of next-day return on band width $C$ across events (and within the 10%/20% subsamples). Fail if the slope is ≤ 0 or economically negligible (≤ 0.5× the scaling implied by $M(\lambda_{eff},\nu)$ under the source's own conversion) (`research-defined falsification threshold`).
3. **Persistence–reversal asymmetry.** Protocol: compare $P_{++}(C)$ against the no-memory null (base frequency of limit closes unconditional on a prior limit) and compare $P_{+-}(C)$ against $P_{++}(C)$. Fail if same-limit persistence is not elevated relative to null, or if reversals are not suppressed relative to persistence, for the admissible band(s) (`research-defined falsification threshold`).
4. **Placebo / shuffled-event test.** Protocol: re-pair the observed limit-close days with next-day returns drawn to preserve marginals (date-shuffle placebo). Fail the mechanism attribution if the same-sign response survives shuffling at comparable magnitude (`research-defined falsification threshold`).
5. **Cost stress.** Protocol: charge realistic round-trip costs (fees + 0.1–0.3% slippage + impact according to event-day liquidity) to the event returns. Fail tradability if net edge ≤ 0 in ≥ 60% of events or any full calendar year of the out-of-sample sample (`research-defined falsification threshold`).
6. **Fillability audit.** Protocol: for each event, determine whether the assumed entry (next open or close) was executable (e.g., open not gapped to a new limit; opposing liquidity available). Fail the specified operationalization if > 50% of events are not executable at the assumed price; then either switch to a fill-aware design or mark the strategy untradable as specified (`research-defined falsification threshold`).
7. **Single-parameter sufficiency.** Protocol: split the sample by band and direction and test whether one $(\lambda, \nu)$ pair fits the sign and ordering of all cells (source already reports it does not). If no direction/band-consistent parameterization exists, the *calibrated* version of the hypothesis is weakened (while the qualitative sign hypothesis may survive) (`research-defined falsification threshold`).

## Crypto portability

- **Portability classification: `unproven`.**
- The source mechanism is demonstrated on NSE cash equities under exchange-mandated daily return bands with a well-defined daily close. The cited source does **not** demonstrate the mechanism in crypto markets; no crypto evidence is claimed here.
- **Structural gaps (research-proposed analysis):**
  - Major crypto spot and perpetual venues generally lack exchange-mandated daily return bands and have **no daily close**; the model's clipping + across-close retention structure must be redefined on an artificial boundary (e.g., UTC-day cut) — a material adaptation, not a port.
  - The closest institutional analogues are venue-specific hard constraints (price-band protections, auctions/halts, futures-style price limits on listed crypto derivatives where they exist) and margin-driven mechanics (liquidation cascades, auto-deleveraging), which are venue/margin-driven rather than band-driven. None is demonstrated to behave like a fixed return band; venue rules must be verified at time of use.
  - Crypto-specific confounds: 24/7 timestamping, funding flows, venue fragmentation across tapes, and liquidation prints as aggressive flow.
- Any crypto test would therefore be an *adapted, unproven* hypothesis: define the constraint boundary, verify the venue's actual mechanism, and re-run the falsification plan in that setting (`research-proposed`). Crypto portability is not authorization to trade.

## Limitations

- **Source quality:** single-author preprint (cond-mat.stat-mech primary category), not peer-reviewed as of capture; physics-style minimal model with strong assumptions (i.i.d. symmetric regularly varying shocks; constant band within event windows; close-to-close dynamics that ignore the intraday path).
- **Empirical support is qualitative:** the paper's own conclusions are sign- and ordering-based; a single effective retention coefficient fails to reproduce band and direction dependence; no band-wise numeric means/standard errors are reported in text; three of four bands violate the theory's admissibility bound.
- **No implementation content:** no code, no backtest, no costs, no fills, no capacity analysis; results are conditional statistics, not strategy PnL.
- **Data reproducibility:** not deposited publicly; reconstruction depends on exchange disclosure records and the `nselib` package; the paper documents at least one stale-record artifact class requiring exclusion.
- **Externality/generality:** NSE-specific band regimes and microstructure; behavior may not generalize to other banded markets (China A-shares, other exchanges) or to other constraint types; our repository's China A-share record further shows that limit-up names are often unfillable, which bounds any tradable interpretation.
- **Magnitude unknown for planning (`data gap`):** the calibrated expected-return mapping for the empirical parameter values is presented graphically (Fig. 6); no numeric table of theoretical vs empirical per-band means is given in the text, so no calibrated expected effect size can be quoted from this record without re-deriving $M(\lambda_{eff}, \nu)$ ourselves.

## Implementation status

- `not-implemented`. Research capture only.
- Nothing has been implemented in any of our systems; no code introduced into our research stack; no backtest, paper, testnet, or live-trading verification exists for this hypothesis in our environment.

## Adoption boundary

- `research-only`.
- Frontmatter specification: `adoption: not-approved`, `approval_scope: research-only`.
- Presence in this repository does not imply the hypothesis is profitable, validated, or approved for implementation, paper trading, testnet, or live trading. Our only claim is that the source has been read, its identity and numbers verified against the primary source, and the hypothesis normalized for downstream review.

## Related Wiki records

- [[quant/china-ashare-mask-first-upstream-contamination-adjusted-mse-2026-09-04]] (limit-up days as unexecutable prints and contamination; adjacent negative evidence on tradability of limit-event strategies)
- [[quant/crypto-perpetual-liquidation-cascade-overshoot-reversal-2026-08-31]] (crypto analogue of mechanically forced selling; the mechanism Das attributes the downward-memory asymmetry to)
- [[quant/4h-context-funding-alignment-regime-crypto-perpetual-2026-09-06]] (crypto-perpetual constraint/regime context)

## Sources

- Debraj Das, *"Retained hidden excess generates memory in price-limited markets"*, arXiv:2608.08625v1 [cond-mat.stat-mech; q-fin.TR], submitted 9 August 2026. https://arxiv.org/abs/2608.08625 (PDF: https://arxiv.org/pdf/2608.08625v1; DOI: 10.48550/arXiv.2608.08625). Primary source for all `source-reported` claims above (Eq. 1–3, 17–28, 31–34; Sec. II–VI; Table I–III; Fig. 4–7; App. A–E).
