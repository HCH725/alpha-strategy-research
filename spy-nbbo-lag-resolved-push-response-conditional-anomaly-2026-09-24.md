---
schema: strategy-research-record-v1
title: "SPY NBBO lag-resolved push-response conditional anomaly (event-time surface, symmetric/antisymmetric dominance decomposition)"
created: 2026-09-24
updated: 2026-09-24
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - market-microstructure
  - event-time
  - push-response
  - market-mill
  - spy
status: research-only
confidence: medium
source_as_of: 2025-11-09
sources:
  - "https://arxiv.org/abs/2511.06177"
  - "https://arxiv.org/html/2511.06177v1"
  - "https://doi.org/10.48550/arXiv.2511.06177"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# SPY NBBO lag-resolved push-response conditional anomaly (event-time surface with symmetric/antisymmetric dominance decomposition)

## Provenance

**Primary source (pinned version, full text read directly this run):**
Dmitrii Vlasiuk, Mikhail Smirnov, *"Push-response anomalies in high-frequency S&P 500 price series"*, arXiv preprint `arXiv:2511.06177v1 [q-fin.TR]`, submitted **Sun 9 Nov 2025 01:34:00 UTC** (4,157 KB).

- **Complete author list exactly as source (HTML title block):** Dmitrii Vlasiuk — *Affiliation: Department of Mathematics, Columbia University*; Mikhail Smirnov — the rendered affiliation slot for the second author prints **"November 2025"** instead of an institution → **affiliation of Mikhail Smirnov is a data gap** (not stated in source). No other authors. No email addresses printed anywhere in v1 → data gap.
- **Version / status:** submission history shows **only `[v1]`** (no v2/v3); HTML header prints `arXiv:2511.06177v1 [q-fin.TR] 09 Nov 2025`; abs page has **no Comments field, no Journal-ref, no publisher DOI field** → **preprint only**, peer-review status **not stated in source**. DataCite/arXiv DOI `10.48550/arXiv.2511.06177` resolves **200** (checked 2026-09-24). License line in HTML header: **`arXiv.org perpetual non-exclusive license`**.
- **Subjects:** primary `q-fin.TR` (Trading and Market Microstructure); cross-lists `q-fin.CP`, `q-fin.PR`, `q-fin.RM`, `q-fin.ST`.
- **Sample period:** **January 2018 – December 2023** (§II), regular-trading-hours sessions only; ≈**1,512** regular trading days (§II; abstract says "about 1,500").
- **Universe:** **single instrument — SPDR S&P 500 ETF Trust (SPY)**, NBBO quote events consolidated from seven US exchanges (§II).
- **Sample size:** ≈**2.6×10⁹** valid NBBO events after cleaning (§II).
- **Stable URLs used:** abstract `https://arxiv.org/abs/2511.06177`; pinned full text `https://arxiv.org/html/2511.06177v1`; PDF `https://arxiv.org/pdf/2511.06177v1`; figure assets read this run from `https://arxiv.org/html/2511.06177v1/{short_top,short_side,long_top,long_side,heatmap_rho_absz_lag,magnitude_vs_lag,rho_vs_lag}.png`.
- **Verification performed:** pinned v1 HTML full text fetched and read end-to-end (51,652 characters of extracted text, §§I–VI plus reference list); Eqs. (2.1)–(3.22) located; Figures 1–4 captions located; **0 tables exist in v1**; whole-document cost/performance keyword scan executed (counts in §Evidence); Figure 2, Figure 4 and Figure 1(long top view) images downloaded and visually inspected this run (approximate visual reads are labelled as such below).
- **Funding / AI-use / conflict statements:** none printed in the manuscript. The only `funding` / `acknowledge` strings in the fetched page are arXiv and LaTeXML page boilerplate → **not stated in source**.
- **Code / data availability:** no code link, no data-availability statement, no replication package anywhere in v1 (`github` appears 3 times, all inside arXiv's own "Report GitHub Issue" UI chrome; the word `code` appears 0 times).
- **Repository source-identity dedup (performed this run, hidden-inclusive):** ripgrep across **all 2,511 `*.md` files in the repo** (tracked + untracked + `.mimo-worktrees`) **and** `coverage_manifest.csv` for `2511.06177`, `Vlasiuk`, `Dmitrii`, `push-response`, `push response`, `Mikhail Smirnov`, `standardized push`, `push magnitude`, `lag-resolved`, `market mill`, `Leonidov`, `S&P 500 price series`, `NBBO.*SPY` / `SPY.*NBBO` → **0 source-identity hits**. `NBBO` and `Smirnov` keyword probes returned only unrelated records (AMM portfolio-mandate, earnings-premium, Husler-Reiss network, index-dispersion, Bayesian-hybrid optimisation), none of which cite this arXiv ID, these authors, or this mechanism.
- **Mechanically adjacent repo records, distinguished on four axes** (all different source identities, all different mechanisms):
  - `diffusive-price-dynamics-square-root-impact-lmf-levy-walk-2026-09-17.md` (arXiv:2608.00988, Sato/Fujiwara/Kanazawa) — axis **mechanism**: analytic resolution of the diffusive price-dynamics paradox via square-root impact + continuous-time random-walk renewal theory, no conditioning on realized pushes, no lag×magnitude surface, no single-instrument NBBO event study.
  - `portfolio-representation-switching-frictions-order-flow-long-memory-2026-09-17.md` (arXiv:2609.02525, Rodríguez Domínguez) — axis **mechanism/horizon**: first-passage renewal aggregation of switching frictions and execution-weight invariance, not a nonparametric conditional-response estimate on SPY quotes.
  - `spy-intraday-momentum-noise-area-band-vwap-stop-dynamic-sizing-2026-09-23.md` (SSRN 4824172, Zarattini/Aziz/Barbon) — same ticker but axis **signal construction + horizon + data dependency**: half-hour time-of-day intraday-momentum rule on SPY bars with Noise Area bands and VWAP stop, vs. event-time tick-lag conditional-moment surface on consolidated NBBO quotes; and axis **universe of evidence** (a rule with reported backtest vs. a descriptive conditional-moment study with no performance numbers).
  - `crypto-high-frequency-kyles-lambda-price-impact-reversal-2026-08-31.md`, `nasdaq-l3-order-book-imbalance-leakage-falsification-2026-09-13.md`, `order-flow-imbalance-predictive-decoupling-cost-falsification-2026-09-12.md` — axis **mechanism + universe**: Kyle-lambda / book-imbalance estimation and cost falsification on crypto or NASDAQ L3 books, not push-conditioned symmetric/antisymmetric response dominance on SPY NBBO.
- **Wiki Brain pre-write search (read-only; no Wiki write performed):** `kb_search("SPY NBBO event-time push response conditional microstructure lag market mill")` → **0 results**; `kb_search("intraday momentum market microstructure short-horizon predictability order flow")` → 5 adjacent pages, none covering this mechanism (used only as retrieval hooks below).

## Economic mechanism

### Source-reported

The authors test whether consecutive intraday price changes in SPY are **conditionally nonrandom** once each increment is standardized at its own lag (Abstract, §I). They frame the design on the established microstructure literature they cite: bid-ask bounce, inventory control and adverse selection generate short-horizon negative serial correlation (Roll 1984; Glosten–Harris 1988; Hasbrouck 1991); limit-order-book liquidity supply/demand shapes price adjustment (Biais–Hillion–Spatt 1995); order-imbalance persistence coexists with near-zero daily return autocorrelation (Chordia–Roll–Subrahmanyam 2005); order flow has long memory and price impact is transient and state-dependent (Lillo–Mike–Farmer 2005; Bouchaud et al. 2004, 2018); a single trade innovation has transient and permanent components (Kyle 1985).

The specific channels the source names for its own findings are:

1. **Propagator / state-dependent impact (source-reported, §III.1, §IV, §V):** the realized push `p_t(L)` plays the role of a signed flow shock and the response `r_t(L)` is the subsequent impact, estimated nonparametrically on a common lag×magnitude grid rather than fitted to a single decay function; the informative horizon **shifts with push size** rather than lining up at a single lag.
2. **Asymmetric liquidity replenishment after sell-side shocks (source-reported, §V, §VI):** strong negative standardized pushes are followed on average by **stronger positive** conditional responses than mirror-image positive pushes, because shocks that deplete the bid leave intermediaries long inventory and elicit a faster/larger restoring quote revision, while buy-side replenishment after heavy selling arrives more aggressively (citing Hasbrouck 1991; Biais et al. 1995).
3. **Partial, horizon-dependent efficiency (source-reported, Abstract, §IV, §VI):** short lags behave close to efficient; structure appears only beyond them, and short-horizon efficiency is "restored only partially" once symmetric and antisymmetric components are separated.
4. **Competition the source itself raises (source-reported, §I, §IV):** the observed geometry reproduces the classical **"market mill"** asymmetry of Leonidov et al. (2006a–c, 2007, 2009), and the paper positions its contribution as embedding that conditioning in a **lag-resolved 3-D surface with a formal symmetric/antisymmetric dominance measure on NBBO event time**, not as a new microstructural primitive.

### Research interpretation

Falsifiable restatement: **conditional on the size and sign of a realized standardized mid-price move over a past event-time window of length `L`, the conditional mean of the standardized mid-price move over the next `L` events differs from zero in specific regions of (lag, magnitude) space, and the sign/size balance of that conditional mean is state-dependent.** If true, this is an **inventory-replenishment / delayed-flow-adjustment alpha hypothesis**; if the whole surface is zero everywhere after cost and multiplicity control, the mechanism is rejected.

Component roles (Scout normalization of the source's own design; no component is asserted to carry alpha):

```text
Conditioning state:  standardized past mid-price increment ("push") z_p at lag L (event time)
Measurement object:  conditional mean standardized forward increment E[z_r | z_p, L] on a 320-bin grid
Decomposition:       even part S (magnitude-driven) vs odd part A (sign-driven), dominance rho
Asymmetry claim:     |response after negative push| > |response after positive push| (liquidity replenishment)
Tradable layer:      ABSENT in source — see Signal and Execution assumptions
```

Competing explanations that would dissolve the alpha claim rather than support it: (a) residual **bid-ask bounce / quote-arrival artifacts** that survive mid-price construction and the paper's own filters; (b) **microstructure frictions as such** (the source's own cited literature attributes such patterns to frictions, i.e. a cost, not a profit, once spread is paid); (c) **in-sample description** of a full-sample conditional moment with no out-of-sample test; (d) **selection across ~192,000 lag×bin cells with no multiplicity control** (Scout count, see Evidence). The source does not run any of these tests.

## Signal

**Trading signal: `underspecified` — the source specifies no entry rule, no exit rule, no holding-period rule, no sizing rule, no threshold and no execution timestamp anywhere in v1.** What follows is split strictly into what the source does and does not specify.

**Source-reported measurement procedure (fully reconstructable; this is an estimation recipe, not a trading rule):**

- **Formation timestamp:** events are indexed in **event time** — each observation is one NBBO quote update, not a clock interval (§III.1, citing Engle–Russell 1998). Only RTH records **09:30–16:00 ET** are retained (§II). Triplets `(t−L, t, t+L)` are formed **only when all three anchors lie in the same regular session**; pairs crossing the open or close are never constructed (§III.1).
- **Price input:** mid price `m_t = (best bid + best ask)/2`, chosen over transaction price to avoid trade-direction and bid-ask-bounce contamination (§II).
- **Push / response:** `p_t(L) = m_t − m_{t−L}` (Eq. 3.1), `r_t(L) = m_{t+L} − m_t` (Eq. 3.2).
- **Lookback (lags):** two families — **short** `L ∈ {1} ∪ {50, 100, 150, …, 5000}` (Eq. 3.3) and **long** `L ∈ {1000, 2000, 3000, …, 500000}` (Eq. 3.4). *Scout count from the printed sets (not printed by the source): 101 short-lag values + 500 long-lag values = 601 lags.* The same-session rule is enforced for every `L`.
- **Standardization:** per-lag `μ_p(L), σ_p(L), μ_r(L), σ_r(L)` estimated from **all admissible anchors**, then `z_p = (p−μ_p)/σ_p`, `z_r = (r−μ_r)/σ_r` (Eqs. 3.5–3.7). Endpoints/inclusivity of the windows is not further specified beyond the same-session rule → **underspecified detail: whether `μ,σ` are computed once on the full 2018–2023 sample or per sub-sample is not stated in source; the text says "using all admissible anchors", which reads as full-sample → point-in-time leakage risk for any live use (see Limitations).**
- **Winsorization (applied before standardization):** `r_t` truncated at empirical quantiles `q_0.00001` and `q_0.99999` (Eq. 2.1) — trims the most extreme **0.001% in each tail** (§II).
- **Jump filter:** any pair of consecutive mid prices with `|m_t − m_{t−1}| > $1.50` inside one trading day is treated as a data error and **both** affected events are excluded; the source states this preserves **>99.5%** of the data (Eq. 2.2, §II).
- **Binning:** one fixed grid shared by all lags, `z_p ∈ [−4.0, 4.0]`, `Δz_p = 0.025` → **320 equal-width bins** (Eqs. 3.8–3.9); bin index `j(z_p) = 1 + ⌊(z_p − z_min)/Δ⌋`, bin center `z_{p,j} = z_min + (j − ½)Δ` (Eqs. 3.10–3.11). The grid extends to ±4σ because >99% of `z_p` mass lies within ±3σ after winsorization (§III.2).
- **Support rule:** a bin is reported at lag `L` only if it holds `n_min = 200` admissible pairs (Eq. 3.12); bins below support are **omitted and never filled** — no extrapolation, no imputation (§III.2). The source notes this caps the standard error of a standardized bin mean near `1/√200`.
- **Reported quantities:** bin counts `n(L,j)`, mean push `z̄_p(L,j)`, mean response `z̄_r(L,j)` (Eqs. 3.13–3.15); conditional surface `z̄_r(L, z_p) = E[z_r | z_p, L]` (§III.3); even/odd decomposition `S(L,|j|) = ½[z̄_r(+j) + z̄_r(−j)]`, `A(L,|j|) = ½[z̄_r(+j) − z̄_r(−j)]` (Eqs. 3.17–3.18); local dominance `ρ(L,|j|) = A / (|A| + |S| + ε)`, `ε = 10⁻¹²` (Eq. 3.19); support weights `w(L,|j|)` (Eq. 3.20); lag-level dominance `ρ(L)` (Eq. 3.21); response strength `M(L)` and raw-unit `M_raw(L)` (Eq. 3.22).
- **Uncertainty:** bootstrap by **resampling symmetric bin pairs within each lag with probabilities `w(L,|j|)`**, pointwise 95% bands from the 2.5%/97.5% empirical quantiles of `ρ^(b)(L)`; no unsupported cells are created by resampling (§III.3). **The number of bootstrap draws `B` is never printed → data gap.**
- **`Entry / short entry / exit / holding period / re-entry / position sizing / multi-timeframe dependencies:` none exist in the source.** §V only gestures at a construction: map realized pushes at "a fixed lag or a small set of lags" to conditional responses from the standardized surface, convert them into an **expected P&L distribution**, and use the surface both as (i) a signal that selects statistically supported regions **after transaction costs** and (ii) a risk metric attributing realized P&L to lag-specific responses. It further says that for trading "a coarser bar construction may be preferable", that explicit **transaction-cost overlays are future work**, and that one should "identify lags where the post-cost mean-standardized response is materially different from zero within its confidence interval, then restrict trading to those pockets". **No threshold, no lag choice, no direction rule and no cost number is given → every operational choice below is ours, not the source's.**

**Research-proposed operationalization (explicitly NOT source-reported; included only so the hypothesis is testable):**

- **Research-proposed signal:** pre-register a single lag `L*` on a training window only (candidate `L*` = 150,000 event ticks, the middle of the long grid — *our choice*); at anchor `t` compute `z_p` over `[t−L*, t]`; **enter long SPY at `z_p ≤ −1.3`** (negative push, positive conditional response expected) and **enter short SPY at `z_p ≥ +1.3`** (positive push, negative conditional response expected), the ±1.3 threshold taken from the lower edge of the source's printed ridge band `|z_p| ∈ [1.3, 3]` (§IV) but the **cut itself being our choice**.
- **Research-proposed exit:** flat at `t + L*` events (mirror-horizon exit); no stop, no take-profit — *our choice, absent from source*.
- **Research-proposed long-only variant:** hold only the `z_p ≤ −1.3` side, motivated by the source's §V argument that long implementations dominate short implementations because shorting is costly and capacity-limited — the *motivation is source-reported, the rule is ours*.
- **Research-proposed timing:** signal evaluated at event `t`, order sent at the **next NBBO update after `t`** (one-quote delay), fill at that quote ± half spread — *our choice*.
- **Research-proposed sizing:** fixed fraction of capital per active pocket, no leverage — *our choice*.
- **Bar-based variant (source-motivated, thresholds ours):** the source explicitly suggests coarser bars for trading; a 1-minute-bar re-implementation with `L*` converted to clock time would be a *different* signal and must be pre-registered separately.

## Required data

- **Instrument:** SPY only (single ETF). No roll, no corporate actions, no index-rebalance handling needed for the measurement object itself (§II).
- **Universe:** none beyond SPY; no inclusion/exclusion, no survivorship adjustment, no reconstitution — *single-name design, breadth n = 1*.
- **Venue / vendor:** **TAQ** (Ticker Authorization/TAQ quote data as named by the source — the specific TAQ product tier is **not stated in source → data gap**) NBBO consolidated from **NYSE, NASDAQ, NYSE Arca, Cboe BZX, Cboe BYX, Cboe EDGX, Cboe EDGA**, restricted to quotes carrying the **`R` condition flag** (Reg NMS NBBO-eligible regular quotes) (§II). Market type: US equity **spot ETF**.
- **Timeframe / sampling:** **event time** (one observation per NBBO update), not clock time; **RTH 09:30–16:00 ET only**, overnight and pre-market excluded (§II).
- **Fields:** best bid, best ask per venue → consolidated NBBO → mid price; quote timestamps; condition flag; exchange identifier. **No trades, no aggressor side, no depth/levels beyond top of book, no open interest, no funding, no borrow, no options data are used** (§II–III).
- **Point-in-time:** sample **Jan 2018 – Dec 2023**; the paper is a full-sample descriptive study with **no train/test split, no walk-forward, no holdout** (§§II–IV). Per-lag standardization moments are estimated "using all admissible anchors" (§III.1) → **full-sample moments; point-in-time/rolling alternative not specified in source → data gap and leakage risk**.
- **Timestamp/timezone:** ET session bounds stated; clock source, sub-second precision, cross-exchange sequence tie-breaking rule and out-of-order quote handling are **not stated in source → data gap** (material, because a 7-exchange NBBO merge needs a deterministic tie-break).
- **Missing data:** winsorization at the 0.001% tails, removal of `>$1.50` same-day jumps with **both** events dropped, `R`-flag and RTH filters (§II); bins under `n_min = 200` are dropped, never imputed (§III.2). **Imputation is explicitly forbidden by the source's own support rule.**
- **Funding / fee / spread needs:** **not observed, not modeled, not budgeted anywhere in v1 → data gap** (see Execution assumptions).

## Execution assumptions

**Source assumptions: essentially none — the source is a conditional-moment measurement study, not a backtest.**

- Order type: **not stated in source**. Fill model: **not stated in source**. Latency / signal-to-order delay: **not stated in source** (the only `latency` strings in v1 are the citation to Hasbrouck–Saar 2013 and their bibliography title "Low-latency trading"). Participation cap, position limits, leverage/margin, short-borrow availability, partial-fill/failure handling: **all not stated in source**.
- **Cost treatment (primary-source Methods / Data / Discussion read in full, plus whole-document keyword scan of pinned v1):** `slippage` **0**, `commission` **0**, `fees` **0**, `fee` **1** (arXiv page chrome: "have a free development cycle"), `financing` **0**, `turnover` **0**, `margin` **0**, `backtest`/`back-test` **0**, `round-trip` **0**, `Sharpe` **0**, `drawdown` **0**, `win rate`/`hit rate` **0**, `CAGR` **0**, `leverage` **1** (the phrase "leveraged ETFs" in a citation to Baltussen et al. 2021), `borrow` **1** ("methods borrowed from statistical physics"), `capacity` **1** (prose: shorting is "costly and capacity-limited"), `fill` **1** ("bins … are omitted and never filled"), `market impact` **2** (both bibliography titles: Almgren et al. 2005; Gatheral 2010), `latency` **2** (both citation/bibliography), `spread` **5** (four are citations/bibliography, one is §V future work "instruments with wider spreads"), `transaction cost` **2** — **both forward-looking**: §V "a signal that selects statistically supported regions of the surface **after transaction costs**" and §V "We also see scope for incorporating **realized transaction costs** … should also improve trading implementability".
- **Conclusion:** **no fee model, no spread model, no slippage model, no borrow model, no financing model, no market-impact model, no fill model, no latency model and no capacity model exists in the source.** Every one of these is a **data gap**, and must **not** be read as a zero-cost claim. The source itself lists transaction-cost overlays as future work.
- Distinguishing source vs. Scout: the source states cost inclusion is future work; **all execution assumptions in this record's Signal section are `research-proposed` by us.**

## Evidence

### Source-reported

All figures below are third-party claims from the pinned v1 and have **not** been independently reproduced. **The source prints no performance numbers whatsoever** (no Sharpe, CAGR, MDD, win rate, turnover, PnL, IC or t-statistic anywhere in v1 — keyword counts in Negative evidence). Its evidence is therefore *structural*, not a backtest:

- **Sample/structure facts (§II):** ≈2.6×10⁹ valid NBBO events over ≈1,512 RTH days, Jan 2018 – Dec 2023, after the `R`-flag, RTH, winsorization and `>$1.50`-jump filters, with ">99.5% of the data" preserved.
- **Short-lag efficiency (Abstract; §IV, Figure 1 short panels):** for lags **1–5,000 ticks** the expected response clusters **near zero across most push magnitudes**, "suggesting high short-term efficiency"; §IV adds that within the short family the cross-sections are "thin and scattered" and that any apparent structure there is "local and sparsely supported" (support-rule trimming at large offsets within the short grid is named as a cause).
- **Emergence of structure beyond the short grid (Abstract; §IV, Figure 1 long panels):** beyond ~5,000 ticks "pronounced tails emerge"; the long-lag surface is "dense and smooth", with a **bowl around `z_p ≈ 0`** and a **ridge growing for `|z_p| ∈ [1.3, 3]`** as `L` increases toward the middle of the long grid (§IV). *Ridge band `1.3 ≤ |z_p| ≤ 3` is a printed prose value (§IV).*
- **Sign change across push = 0 (§IV, Figure 1 long side view):** `z̄_r(L,j)` changes sign across `z_p = 0` over large regions → an antisymmetric component; amplitude rises with `L` up to a **plateau for strong positive pushes** (structure "flattens … predictability does not keep compounding"), while the **negative-push side shows an apparent lack of plateau** (§IV, flagged by the source for later discussion).
- **Market-mill reproduction (§IV):** "on the lowest few thousand lags (**roughly 5,000–150,000**)" the cross-sections reproduce the Leonidov et al. market-mill asymmetry — positive pushes → negative expected responses, negative pushes → positive expected responses, strongest in the wings and attenuating near zero.
- **Dominance heatmap (§IV, Figure 2 — image downloaded and visually inspected this run):** for **`|z_p| ≲ 0.7` symmetry dominates** "throughout" (printed prose value); for **moderate magnitudes the heatmap turns positive (antisymmetry) over a wide band of lags**; the red/blue boundaries **drift in `L` as a function of `|z_p|`** (horizon of strongest sign information depends on shock size); for the **strongest pushes the heatmap is mostly negative**, i.e. symmetry-dominated, which the source reads as "after strong initial price movements one can expect a positive response" regardless of push sign. *Scout visual read of the printed Figure 2 (approximate, not source-printed numbers): a dense red/antisymmetric band at lags ≈0–50,000 across nearly the whole `|z_p|` range; blue/symmetric regions at larger lags for high `|z_p|` and a vertical blue band at low `|z_p|` (≈0.5–1.0) over lags ≈200,000–400,000; interleaved red patches at ≈250,000–350,000 lags for `|z_p| ≈ 1.5–2.5`.*
- **Aggregate dominance (§IV, Figure 4 — image downloaded and visually inspected this run):** the source's prose says `ρ(L)` "takes large positive values at the shortest lags, then turns negative around the transition from the short-lag grid to the early long-lag region, climbs back toward weakly positive levels across a broad middle range, and finally drifts slightly negative again at the longest lags", with pointwise 95% bootstrap bands. *Scout visual read of the printed Figure 4 (approximate, not source-printed numbers): axes `lag (event ticks)` 0→500,000 and `ρ(L)` −1.00→+1.00; curve starts ≈ +0.65, peaks ≈ +0.78 near lag ≈35,000, first zero crossing near **≈75,000**, trough ≈ **−0.60 near ≈95,000**, second zero crossing near ≈140,000, then a plateau ≈ +0.05 to +0.25 with a local peak ≈ +0.28 near ≈155,000 and another near ≈425,000, a third crossing near ≈465,000 and an end value ≈ −0.22 at 500,000; bands widest at the ends and around the trough, tightest in the ≈150,000–400,000 range.*
- **Response strength (§IV, Figure 3):** `M(L)` rises monotonically from the bottom of the long grid into a **broad plateau around the middle**, then shows a **mild late increase**; the source reads the plateau as conditional response reaching stable amplitude once order-splitting/queue dynamics have propagated. *Figure 3 could not be visually inspected this run (two image-analysis attempts timed out) → its numeric level is a **data gap**; only the prose description is recorded.*
- **Asymmetry (Abstract; §V; §VI):** "strong negative standardized pushes are followed, on average, by stronger positive conditional responses than the mirror positive pushes", attributed to inventory-restoring quote revision and asymmetric book replenishment. *Scout visual read of Figure 1 (long top view): the positive-response lobe for `z_p < 0` reaches closer to `z_r = +1` than the negative-response lobe for `z_p > 0` reaches `z_r = −1`, i.e. the printed surface is visibly asymmetric in the direction the prose claims.*
- **Trading-utility claims (§V, §VI — qualitative only):** the surface "can be used to define tradable pockets and risk controls"; it can drive "a signal that selects statistically supported regions of the surface after transaction costs" and "a risk metric that attributes realized P&L"; expected responses in standardized units can be turned into "an expected P&L distribution". **No P&L, Sharpe or return number is attached to any of these statements.**
- **Falsifiable prediction extracted for this record:** `E[z_r | z_p, L] > 0` for `z_p ≤ −1.3` and `< 0` for `z_p ≥ +1.3` over a mid-to-long lag band, with `|E[z_r|z_p < 0]| > |E[z_r|z_p > 0]|` at matched `|z_p|` (the asymmetry). This is a **Scout restatement of source-reported structure**, not a source-stated trading rule.

### Independently reproduced

not independently reproduced

(What was actually done this run: pinned v1 landing page + full-text HTML read end-to-end; Eqs. 2.1–3.22 and Figures 1–4 located; Figures 1, 2 and 4 downloaded and visually described; whole-document cost/performance keyword scan; repository-wide source-identity dedup. **No NBBO panel was rebuilt, no quotes were pulled, no winsorization/jump filter was re-run, no bin means, no `S/A/ρ/M` statistic and no bootstrap were recomputed, and no trade was simulated.**)

### Negative evidence

1. **Zero trading rule in the source** — no entry, exit, holding period, sizing, threshold, stop or execution timestamp anywhere in v1; the entire trading layer of this record is `research-proposed`.
2. **Zero performance numbers in the source** — `Sharpe` 0, `CAGR` 0, `drawdown` 0, `win rate`/`hit rate` 0, `turnover` 0, `backtest` 0, `round-trip` 0, `P&L` appears 3 times **only as a conceptual object** ("expected P&L distribution", "attributes realized P&L", "explaining realized P&L") with no value. This is a descriptive conditional-moment study, not a backtest — there is no profitability evidence to weigh.
3. **No cost model at all** — `slippage` 0, `commission` 0, `fees` 0, `financing` 0, `margin` 0; the only two `transaction cost` hits are future-work sentences (§V). The source itself says cost overlays are still to be done → any post-cost claim is unsupported by the source.
4. **No fill/latency/capacity model** — order type, fill model, signal-to-order delay, participation cap and borrow availability are all absent (`latency`/`market impact` hits are citations; `capacity` appears once, as prose about shorting being capacity-limited).
5. **Multiplicity is uncontrolled (Scout count, not source-stated):** 601 printed lags × 320 bins ⇒ up to **192,320 candidate cells**, plus 2 lag families × 4 surface panels × 2 decompositions; inference is **pointwise only** (2.5%/97.5% bootstrap quantiles), with **no family-wise or FDR adjustment** and no pre-registration of which pocket was hypothesized.
6. **Full-sample estimation with no out-of-sample test** — Jan 2018–Dec 2023 is used both to estimate per-lag standardization moments and to display the surface; there is no train/test split, no walk-forward, no frozen holdout and no forward period.
7. **Bootstrap design likely understates uncertainty (Scout inference):** resampling is over *bin pairs within a lag with weights `w`*, not over the underlying event series, so it does not propagate serial dependence of quote arrivals (which the source itself invokes via long-memory order flow, Lillo–Mike–Farmer 2005) into the bands. The source does not discuss this.
8. **Bootstrap draw count `B` never printed** → the reported 95% bands are not exactly reproducible (data gap).
9. **Point-in-time leakage risk in the signal as written:** standardization moments `μ,σ` are estimated "using all admissible anchors" over the whole sample; a live system would need rolling past-only moments, and the source never tests whether the surface survives that change → data gap.
10. **Figure–prose location ambiguity on `ρ(L)` (recorded as ambiguity, not a confirmed numeric contradiction):** §IV places the first `ρ(L)` sign change at "the transition from the short-lag grid to the early long-lag region" (the short grid ends at 5,000 ticks), whereas the Scout visual read of printed Figure 4 puts the first zero crossing near ≈75,000 ticks with a ≈−0.60 trough near ≈95,000 — i.e. the symmetry-dominant trough sits **inside** the 5,000–150,000 band where §IV simultaneously says antisymmetric market-mill reversal is evident. Support-weighted aggregation can in principle reconcile the two, but **no numeric grid is printed to check it**, so the tension stays open. `contradictions` therefore remains `[]`: no printed numeric contradiction could be confirmed from figures that carry no numeric table.
11. **Support-rule trimming varies with lag** — the source itself notes the same-session constraint "trims many anchors for larger offsets even within the short grid" (§IV), so cross-lag comparability of bin supports is not uniform; cells with `n < 200` vanish rather than being modelled.
12. **Filter thresholds are heuristics with no sensitivity analysis:** `q_0.00001`/`q_0.99999` winsorization and the `>$1.50` same-day jump cut are asserted (§II) with no robustness table; the `R`-flag, 7-exchange and RTH choices are likewise unvaried.
13. **Breadth n = 1** — one instrument (SPY), one venue set, one 6-year window spanning the COVID regime; the source concedes the methodology should be extended to wider-spread, thinner, more fragmented instruments (§V, §VI) as future work.
14. **Event-time to wall-clock mapping unresolved** — long lags reach 500,000 NBBO updates, whose clock duration varies by orders of magnitude across the day; the source acknowledges "a coarser bar construction may be preferable" for trading but gives no conversion rule → the holding period of any tradable version is **underspecified**.
15. **No code, no data-availability statement, no replication package; TAQ is a licensed commercial feed** → the ≈2.6×10⁹-event pipeline cannot be rebuilt from the paper alone (data gap, not a null result).
16. **Preprint only, single manuscript version, no peer-review status, no funding/AI-use/conflict statement, second author's affiliation printed as a date** → source-quality caveats for a result whose entire content is figure-based.
17. **No competing-explanation test:** bid-ask bounce, quote-arrival artifacts and inventory effects are cited as the mechanism, but no ablation isolates them from a tradable edge; the cited literature (Roll; Glosten–Harris; Hasbrouck) also implies these patterns are *frictions that cost money to trade through*, which is a live threat to the alpha reading.

## Falsification plan

All data, thresholds and failure rules below are **`research-defined` (Scout-chosen)** unless explicitly marked source-reported; all operational trading rules are **`research-proposed`**.

- **F1 — Independent-vendor replication (research-defined).** Rebuild the push-response surface on a second consolidated-quote vendor (not the same TAQ extract) for the same Jan 2018–Dec 2023 SPY RTH sample. **Pass gate:** the ridge band `1.3 ≤ |z_p| ≤ 3` (band itself source-reported, §IV) shows `sign(E[z_r|z_p ≤ −1.3]) > 0` and `sign(E[z_r|z_p ≥ +1.3]) < 0` in at least 60% of mid-to-long lags, with bootstrap `|z| ≥ 2.0`. **Fail →** the structure is vendor/filter-specific; keep `research-only`.
- **F2 — Point-in-time / leakage audit (research-defined).** Re-estimate `μ_p, σ_p, μ_r, σ_r` on **rolling past-only windows** (expanding within each calendar year) instead of full-sample moments, and re-derive the surface. **Fail rule:** sign of the conditional response in the F1 pocket flips in more than 50% of rolling re-estimations, or the pocket's mean `|E[z_r]|` moves by more than ±0.02 standardized units. **Fail →** the surface depends on future moments; mechanism not tradable as stated.
- **F3 — Multiplicity control (research-defined).** Apply Benjamini–Hochberg at `q < 0.10` across the full printed lag×bin grid. **Fail rule:** fewer than half of the cells that carry the source's claimed structure survive. **Fail →** treat the surface as selected-on-sample noise.
- **F4 — Cost ladder (research-defined).** Re-run the F1/F5 rules with per-side costs of **0 / 1 / 2 / 5 / 10 bp** plus **half the quoted spread paid on both legs** and a 1-quote signal delay. **Fail rule:** any edge remaining only at ≤1 bp, or **net Sharpe < 0.5 at 5 bp per side**. **Fail →** mechanism may be real but is not an alpha after frictions.
- **F5 — Frozen pre-registered rule (research-proposed rule, research-defined gate).** Pre-register `L* = 150,000` event ticks, thresholds `z_p ≤ −1.3` (long) / `z_p ≥ +1.3` (short), exit at `t + L*`, one-quote delay, equal notional — all **research-proposed** — on a 2018–2020 training window, then freeze and evaluate 2021–2023. **Pass gate:** out-of-sample net Sharpe ≥ 0.5 **and** positive net P&L in at least 2 of 3 frozen years **and** the long-only variant also positive. **Fail →** keep `research-only`, no retuning to rescue.
- **F6 — Placebo / null surface (research-defined).** 1,000 block-shuffled or circular-shifted push series that preserve the marginal distribution of `z_p` but destroy the push→response link; recompute `ρ(L)` and the pocket statistic each time. **Pass gate:** observed pocket statistic exceeds the 95th percentile of the placebo distribution (`z ≥ 2.0`). **Fail →** structure is an artifact of marginals/autocorrelation-in-levels.
- **F7 — Microstructure-artifact ablation (research-defined).** Repeat the surface three ways: (a) on transaction prices instead of mids; (b) after a bounce control (subtract/orthogonalize the signed spread component); (c) on quote updates that coincide with a trade only. **Fail rule:** the `|z_p| ∈ [1.3, 3]` response amplitude shrinks by more than **50%** in any two variants → the effect collapses into bid-ask bounce / quote-arrival artifacts rather than inventory-replenishment alpha.
- **F8 — Regime and time-of-day breakdown (research-defined).** Split into AM (09:30–12:30) vs PM (12:30–16:00) and into 2018–2019 / 2020–2021 / 2022–2023. **Fail rule:** more than **50%** of the pocket's total response mass comes from 2020–2021 alone, or the negative-push asymmetry reverses sign in either session half. **Fail →** the effect is a single-regime or single-session phenomenon.
- **F9 — Cross-instrument generalization (source-motivated, thresholds research-defined).** The source explicitly proposes extending beyond SPY (§V, §VI). Re-run unchanged on **QQQ and IWM** over the same window. **Pass gate:** the F1 sign pattern reproduces in **at least 2 of 3** instruments. **Fail →** SPY-specific microstructure, not a general mechanism.
- **F10 — Capacity / participation stress (research-defined).** Cap participation at **20% of quote-update-normalized volume**, add the F4 ladder plus a square-root impact term calibrated from the literature the source itself cites (Almgren et al. 2005; Gatheral 2010). **Fail rule:** net Sharpe < 0.5 at **2 bp per side** under that cap. **Fail →** no implementable capacity.
- **Standing failure action (research-defined):** on F1, F2, F3 or F7 failure → mark the hypothesis `rejected` for our purposes and do **not** re-tune thresholds to revive it; F4/F5/F10 failure keeps the record as `research-only` descriptive structure with no tradable claim.

## Crypto portability

**unproven.**

- No source-reported crypto evidence: the paper studies a US equity ETF only; nothing in v1 touches crypto, so `direct` is not available and `adapted` would overstate the evidence.
- **No NBBO-equivalent consolidated quote:** crypto has venue-fragmented, per-exchange top-of-book; a "push" computed on one venue's book is not the same object, and aggregating across venues reintroduces the sequencing/tie-break problems the source never specifies.
- **24/7 sessions break the core construction:** the same-session triplet rule (no crossing the open/close), the RTH 09:30–16:00 filter and the ET session semantics have no crypto analogue; candle/event boundaries and timezone conventions become judgment calls → `adapted` would be required and is not demonstrated by the source.
- **Event-time lag is not comparable across venues or regimes:** 150,000 NBBO updates in SPY RTH is not a fixed clock duration and has no stable crypto counterpart; tick intensity on a memecoin perp can differ by orders of magnitude.
- **Quote quality:** crypto top-of-book is cheap to spoof/stale-quote; mid price is more manipulable than a Reg NMS `R`-flagged consolidated quote, so the mid-price construction the source relies on is weaker.
- **Short side / financing:** the source's own asymmetry claim is partly about *why long implementations dominate* (shorting costly and capacity-limited). In crypto, shorting cost, borrow, **funding accrual (8h)** and perp liquidation are entirely unmodeled here.
- **Liquidity and market impact:** spread, depth and impact profiles differ materially from SPY's seven-exchange NBBO; F10's capacity gate would have to be re-derived, not carried over.
- Portable *hypothesis only*: "condition on a standardized recent move and test whether the conditional response is nonzero and sign-asymmetric" is a testable method on a single liquid perp's book-ticker stream — but that would be a **new** record with its own primary source or its own experiment, not this one.

## Limitations

- `underspecified`: trading layer (entry/exit/holding/sizing/timing), tie-break and sequencing rules for the 7-exchange NBBO merge, TAQ product tier, bootstrap draw count `B`, clock duration of event-time lags, whether standardization moments are full-sample or rolling, second author's affiliation.
- `data gap`: no cost/fill/latency/capacity model; no code, no data-availability statement, no replication package; commercial TAQ dependency; Figure 3 numeric level not inspectable this run (two image-analysis timeouts); no numeric tables anywhere in v1 — all quantitative content lives in prose plus four figures.
- `not independently reproduced`: every structural claim above; no panel was rebuilt and no statistic recomputed.
- `unproven`: profitability, post-cost viability, out-of-sample persistence, cross-instrument generality, and crypto portability.
- Identification: a conditional mean differing from zero in-sample is **not** evidence of a tradable edge once the spread is paid; the source's own cited microstructure literature explains such patterns as frictions.
- Selection: ~192,320 candidate cells (Scout count), pointwise-only bands, no pre-registration, no multiplicity adjustment.
- Regime/breadth: one instrument, one 6-year window, RTH only, COVID inside the sample; no day/night or pre/post-COVID segmentation performed (the source proposes the day-night split as future work, citing Bogousslavsky 2021).
- Source quality: preprint, single version, no journal status, no peer review stated, figure-only evidence, no funding/AI/conflict disclosure.
- Publication bias: a descriptive anomaly paper with no performance table is not subject to backtest-reporting bias, but neither does it carry any falsification burden of its own — the tests above are ours.

## Implementation status

`implementation_status: not-implemented`.

Nothing from this record exists in our research stack. No NBBO/TAQ panel was built, no push-response surface was estimated, no `S/A/ρ/M` statistic was recomputed, no trading rule was implemented, and **no Qlib full backtest, no survivor promotion, and no Paper / Testnet / Live stage has been attempted or implied**. This run produced one normalized Markdown research record in the public staging repository and nothing else.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

Presence of this record **does not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. Any adoption or implementation decision is a separate, explicit, later review.

## Related Wiki records

Pre-write `kb_search` for the exact mechanism (`SPY NBBO event-time push response conditional microstructure lag market mill`) returned **0 results — no Wiki Brain page covers this mechanism, so no direct page link is asserted.** Adjacent pages returned by a broader query are recorded only as retrieval hooks (read-only; **no Wiki write was performed this run**):

- [[quant/fourier-residue-sign-magnitude-equity-reversal-decomposition-2026-09-04]] — closest adjacent: decomposes microstructure return autocorrelation / bounce; relevant as the **competing-explanation** hook for F7.
- [[quant/hawkes-order-flow-imbalance-self-excitation-microstructure-2026-09-12]] — order-flow-imbalance self-excitation and the transaction-cost friction barrier (BTCUSDT); hook for the cost-friction comparison in F4.
- [[quant/crypto-perpetual-order-flow-entropy-microstructure-taker-cost-falsification-2026-09-13]] — order-flow/sign entropy with explicit taker-cost falsification; hook for the crypto-porting experiment if it is ever commissioned.

Repo records read and ruled out as duplicates are listed in Provenance.

## Sources

- Dmitrii Vlasiuk, Mikhail Smirnov, *"Push-response anomalies in high-frequency S&P 500 price series"*, arXiv:2511.06177v1 [q-fin.TR], submitted 9 Nov 2025. Abstract: https://arxiv.org/abs/2511.06177 — pinned full text read this run: https://arxiv.org/html/2511.06177v1 — PDF: https://arxiv.org/pdf/2511.06177v1 — DOI: https://doi.org/10.48550/arXiv.2511.06177 (resolves 200, checked 2026-09-24).
- Figure assets inspected this run from the pinned HTML: `https://arxiv.org/html/2511.06177v1/heatmap_rho_absz_lag.png` (Figure 2), `https://arxiv.org/html/2511.06177v1/rho_vs_lag.png` (Figure 4), `https://arxiv.org/html/2511.06177v1/long_top.png` (Figure 1, long top view), `https://arxiv.org/html/2511.06177v1/magnitude_vs_lag.png` (Figure 3 — download succeeded, visual inspection timed out twice → numeric level a data gap).
- Works cited **by the source** and used only to describe the source's own stated mechanism (claims attributed to the source, not independently verified here): Roll (1984); Glosten–Harris (1988); Hasbrouck (1991); Biais–Hillion–Spatt (1995); Chordia–Roll–Subrahmanyam (2005); Lillo–Mike–Farmer (2005); Bouchaud–Gefen–Potters–Wyart (2004); Bouchaud et al. (2018); Kyle (1985); Leonidov et al. (2006a–c, 2007) and Zaitsev et al. (2009) ["market mill"]; Gatheral (2010); Almgren–Chriss (2001); Almgren et al. (2005); Heston–Korajczyk–Sadka (2010); Baltussen–Da–Lammers–Martens (2021); Stambaugh–Yu–Yuan (2012); Shleifer–Vishny (1997); Bogousslavsky (2021); Lucchese–Pakkanen–Veraart (2024); Engle–Russell (1998); Hasbrouck–Saar (2013).
