---
schema: strategy-research-record-v1
title: "Pure Momentum: Wild-Bootstrap Drift-Significance Filtering of US Equity Momentum (Amundi Working Paper #188)"
created: 2026-09-26
updated: 2026-09-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - momentum
  - us-equities
  - drift-test
  - wild-bootstrap
  - transaction-costs
status: research-only
confidence: medium
source_as_of: 2026-09-26
sources:
  - "https://research-center.amundi.com/article/pure-momentum (Amundi Research Center landing page for Working Paper #188 'Pure Momentum Strategies', page date 2026-03-25, HTTP 200, retrieved 2026-09-26)"
  - "https://research-center.amundi.com/files/nuxeo/dl/d7bc1c57-7420-4526-8dd4-af51d5ff5fb3?inline= (PDF, 2416626 bytes, SHA-256 30ca573883921ac7e35a63fd15cb6e899c708e406df92c436eafb70da020d6e9, retrieved 2026-09-26)"
  - "Amundi Investment Institute Working Paper #188, March 2026; manuscript title page dated November 14, 2025; authors Roberto RENO, Romeo TEDONGAP, Xinyi ZHANG"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Pure Momentum: Wild-Bootstrap Drift-Significance Filtering of US Equity Momentum (Amundi Working Paper #188)

## Provenance

**Primary source (one document, pinned by content hash):**

- **Landing page:** `https://research-center.amundi.com/article/pure-momentum` — title `Pure Momentum Strategies | Amundi Research Center`, page date `2026-03-25`, HTTP 200, retrieved and read 2026-09-26 (landing HTML 150481 bytes, SHA-256 `56289a2aae0a24f36f5ca518791ee86c5946fc70f0de4da8951f2bc6922d1569`). The landing page's own download link is `/files/nuxeo/dl/d7bc1c57-7420-4526-8dd4-af51d5ff5fb3?inline=`, i.e. the PDF below is the page's canonical attachment, not a search-engine guess.
- **PDF:** `https://research-center.amundi.com/files/nuxeo/dl/d7bc1c57-7420-4526-8dd4-af51d5ff5fb3?inline=` — **2,416,626 bytes**, **SHA-256 `30ca573883921ac7e35a63fd15cb6e899c708e406df92c436eafb70da020d6e9`**, retrieved 2026-09-26. 55 pages (extracted with `pypdf`); PDF metadata `/Producer: iLovePDF`, `/ModDate: D:20260324102555Z`.
- **Cover / status line:** `WORKING PAPER #188 | MARCH 2026` (Amundi Investment Institute). The article title page itself is dated **November 14, 2025** — i.e. the manuscript predates the March 2026 Amundi release by ~4 months.
- **Series context:** released under the **ESSEC-Amundi Chair on Asset & Risk Management** (Chair created 2016, co-headed by Marie Brière for Amundi and Elise Gourier / Sofia Brito-Ramos for ESSEC); the cover states "we are pleased to share this working paper authored by ESSEC researchers. This is an ad hoc release, outside our usual publications, reflecting the partnership agreement between our institutions."
- **Distribution banner (verbatim, page 1 and 2):** "Marketing Communication. Document for the exclusive attention of professional clients, investment services providers and any other professional of the financial industry." → this is **institutional marketing-adjacent material, not a journal article**. Public-repo hygiene: this record cites and normalizes; it does not reproduce the paper wholesale.

**Author list (exactly as printed on the title page, page 3):**

| Author | Affiliation (as printed) | E-mail (as printed) |
|---|---|---|
| Roberto Renò † | ESSEC Business School | reno@essec.edu |
| Roméo Tédongap ‡ | ESSEC Business School | tedongap@essec.edu |
| Xinyi Zhang § | University of Warwick | xinyi.zhang.9@wbs.ac.uk |

Acknowledgements name Elise Gourier, Tim Bollerslev, Kris Jacobs, Shuping Shi, Fabio Trojani plus ESSEC/AAAFFI/QFFE/SoFiE/TSE workshop participants; keywords printed as "Momentum, drift test, reversals".

**Publication / version status:** working paper only. **No DOI, no journal, no peer-review statement** anywhere in the pinned PDF. A public-web search on 2026-09-26 for an arXiv or SSRN version of this paper returned **no arXiv record and no SSRN record** (the only "pure momentum" SSRN hit was `ssrn.com/abstract=2467392`, *Optimality of Momentum and Reversal*, an unrelated S&P 500 time-series paper). **No code repository, no data-availability statement, no code-availability statement** — a keyword scan of the full pinned text for `github`, `code availability`, `data availability`, `available at`, `upon request` returned **zero hits**. Data is CRSP (licensed), so the results are **not publicly reproducible**.

**Underlying statistical test:** the drift test itself comes from **Renò and Shi (2025), "Drift sign. Working Paper."** — a separate, also-unpublished working paper cited repeatedly in §2 and footnote 2. This record's source identity is WP #188; the test paper is a method dependency, not the source of the performance numbers.

**How this was read:** the PDF text layer was extracted and Sections 1–8 plus Appendices A–D were read directly (not via any secondary summary); every number below carries its Table/Figure/Section location. **Terminology re-verified 2026-09-26 against the pinned PDF text:** the paper defines both labels verbatim on PDF p.4 — it prints *“We refer to these instances as ‘illusory momentum.’”* (large jump / volatility-driven returns with no economic reason to persist), and for the small-trend case it prints *“existing economic theories (e.g., Da et al., 2014) suggest that smaller returns are more likely to persist, since they can more easily slip under the radar of analysts and traders. We refer to these cases as ‘hidden’ momentum.”* Both terms recur on p.5 and p.7. The Da et al. (2014) attribution and the “hidden momentum” label are therefore source-reported, not Scout-invented.

**Deduplication (step 5, deterministic, whole-repository):** scanned all tracked `*.md` / `*.csv` / `*.json` (993 tracked `.md` files) **and** the untracked hidden trees (`.mimo-worktrees/`, `.agents/`, `.hermes/`) plus `coverage_manifest.csv`. Zero hits for: `research-center.amundi.com`, `d7bc1c57`, `WORKING PAPER  #188`, `Amundi`, `Renò` / `reno` (word), `Tédongap`/`Tedongap` as this paper's author, `Xinyi Zhang`, `ESSEC`, `wild bootstrap`/`wild-bootstrap`, `RHSACD`, `illusory momentum`, `hidden momentum`, `drift sign`, `Shi (2025)`, `Hasbrouck (2009)`. The 16 `pure momentum` hits are all incidental phrase uses inside unrelated records (e.g. `etf-momentum-operational-rules-…` quoting an anti-signal thesis, `latent-drift-kalman-bucy-…` on `κ_p = 0`), and the single `Tédongap` hit is **Farago & Tédongap (2018)** inside `common-firm-level-investor-fears-…` — a different paper by a different author set. **No existing record covers this source or this mechanism** → new record permitted.

## Economic mechanism

### Source-reported

- **Core claim:** the standard Jegadeesh–Titman (1993) 12-month cumulative-return momentum signal is **noisy**. Large past returns frequently reflect (a) **jumps** from new information absorbed almost immediately, or (b) **elevated volatility** from uncertainty — neither has an economic reason to persist in sign. The source names these **"illusory momentum"** and argues such stocks also carry higher risk, so including them lowers risk-adjusted performance.
- **Complementary claim:** genuine but **small** trends get screened out of top/bottom quantiles; citing Da et al. (2014), the source calls these **"hidden momentum"** and argues smaller returns persist because they slip under analysts'/traders' radar.
- **Behavioral channel:** abstract + §4 — "Performance is primarily driven by long positions in winners, supporting theories postulating overconfidence. The bad news instead appears to be incorporated more slowly." Introduction attributes large-move overreaction to **overconfidence**; the asymmetry (good news fast, bad news slow) is asserted, not separately tested.
- **Additional empirical assertion:** "omitting the most recent month is unnecessary to identify winners" — i.e. the skip-month convention inherited from short-term-reversal contamination is dispensable for winners (tested in §6 / Figure 16).
- **Not claimed by the source:** no claim that the drift test creates a new risk premium; the source frames it purely as **signal purification / noise reduction** of an existing premium.

### Research interpretation

- **Component roles:**
  - *Signal-quality filter:* a jump-truncated, wild-bootstrap, one-sided drift significance test on daily returns over the formation window — replaces "rank on cumulative return" with "rank/filter on evidence that the drift is nonzero".
  - *Long leg:* stocks whose positive-drift p-value clears `p* ≥ 1 − α` ("pure winners").
  - *Short leg:* stocks whose negative-drift p-value clears `p* ≤ α` ("pure losers").
  - *Benchmark:* the same-count traditional momentum portfolio ranked on cumulative past returns — a deliberate control for diversification/stock-count effects.
- **Falsifiable hypothesis (Scout formulation):** conditioning a cross-sectional momentum portfolio on a volatility/jump-robust trend test raises **net** risk-adjusted return because it removes positions whose observed return was generated by the diffusion/jump component rather than the drift component.
- **Strongest rival explanation, not excluded by the source:** the source's own §3/§4.2 states that "the proposed test tends to reject more for stocks with **larger market capitalization, higher liquidity, and lower volatility**". A significance test on daily returns is mechanically more powerful for low-volatility, high-liquidity names. The "pure winner" portfolio may therefore be an **implicit large-cap / low-volatility / liquid-quality tilt**, not a trend detector — which would make the effect a repackaged quality/low-vol factor rather than purified momentum. The source does **not** run this ablation (see F6). This is the single most important open question attached to the record.

## Signal

All items below are **source-reported** unless explicitly marked `research-proposed` or `data gap`.

### A. Test construction (Section 2, read directly)

- **Model:** log price over the formation period follows an Itô semimartingale `X_t − X_0 = ∫μ_s ds + ∫σ_s dW_s + J_t` with a compensated jump process `J_t`. **Null:** `∫₀^T μ_t dt = 0`.
- **Truncation:** intra-period increments `X_{iT/n} − X_{(i−1)T/n}` whose absolute value exceeds `κ_n` are truncated out. Footnote 2: theory requires `κ_n → 0` at rate `(T/n)^ω`, `ω < 0.5`; in practice `κ_n` is a multiple of the robust standard deviation `MAD_n / Φ⁻¹(3/4)`, and **"We set the threshold as three times this quantity"** → **`κ_n = 3 × MAD_n / Φ⁻¹(3/4)`**. MAD is preferred to sample variance for outlier robustness.
- **Wild bootstrap:** `B` replications of the truncated return with independent Bernoulli ±1 sign flips at 50% probability (Renò and Shi, 2025). **`B = 1000`** (stated in §3).
- **p-value (Eq. 1):** `p*_{B,n,T} = (1/B) Σ_{j=1..B} 1{ R̃*_{T,n}^j ≤ R̃_{T,n} }`, a **one-sided** test; `1 − p*` is used for the positive-drift alternative (the bootstrapped truncated-return distribution is symmetric). The source states `p*` "can be used directly for portfolio sorting".
- **Sample size:** momentum formation uses daily data, **`n ≈ 230` daily returns on average** (§3); short-term reversal uses **`n ≈ 20.63`** (§6).
- **Robustness variants in source:** Appendix C repeats everything with **`κ_n = 4 × MAD_n`** (four MADs); Appendix D uses an **alternative drift test that dispenses with truncation altogether** (also from Renò & Shi, 2025), printed in figures as the "RHSACD test" (Figure 36 caption).

### B. Double-sort portfolio (Section 4.1 → Table 1)

- **Formation timestamp:** portfolio formed at the **end of each month `t`**; monthly, from **July 1963 to December 2022**. The holding month is `[t, t+1]` (§4.1, PDF p.16).
- **Signal window — the source states two different windows → `underspecified`:**
  - §2 (PDF p.10), the general convention: "denoting by `t` the time in which the new portfolio is formed, this can be (expressed in months) **`[t −12, t −1]`** for momentum, or `[t −1, t]` for reversals."
  - §4.1 (PDF p.16), describing the very portfolios of Table 1: "the signal for creating the portfolios being computed during the formation period **`[t −11, t −1]`**."
  - Both statements are source-reported and both are printed in the pinned PDF; they are **not reconciled anywhere in the paper**. This record therefore reports **both** and does not assert a single window as fact. Any reconstruction must pre-declare which window it uses (and Figure 16's own labelling calls `[t −12, t −1]` "11 months" and `[t −12, t]` "12 months", i.e. the month-counting convention itself is loose).
- **Sort 1:** quintiles on cumulative past return → `Losers, 2, 3, 4, Winners`.
- **Sort 2 (within each quintile):** quintiles on `p*` of **negative** drift → `Low, 2, 3, 4, High`. Source: "low p-values indicate the significance of negative trends, while high p-values indicate the significance of positive trends." → **5 × 5 = 25 cells.**
- **Portfolios:** `HW` = High × Winners (long); `LL` = Low × Losers (short); **`HW-LL` = long HW / short LL.** `W-L(5)` = long Winners quintile / short Losers quintile (5× the stock count). `W-L(25)` = long top-20% of the Winners quintile / short bottom-20% of the Losers quintile → **same stock count as HW-LL** (the size-matched comparator).
- **Sizing / cadence:** **equally weighted**, **1-month holding period**, rebalanced at the end of each month. No vol targeting, no leverage, no stops.

### C. Signal-only portfolios (Section 4.2 → Figures 5/9)

- **Pure losers:** `p* ≤ α`. **Pure winners:** `p* ≥ 1 − α`. `α` grid **1% to 10%** (figures show 1%, 4%, 7%, 10%).
- **Minimum breadth rule (source-specified):** "We require at least 10 stocks to be included in the winner/loser portfolio to trade. If the test detects fewer stocks, we invest in the risk-free rate."
- **Traditional comparator:** same number of stocks at each `α`, selected by cumulative-return ranking (equal-count control).
- Equal-weighted, monthly rebalance, 1-month hold. **Formation window: `underspecified`** — §4.2 never restates it; §2's convention `[t −12, t −1]` is the only stated window for signal-based momentum portfolios, while §4.1 gives `[t −11, t −1]` for the double-sort (see §B above).

### D. Other source-specified operational choices

- **Formation-length test:** Figure 16 compares `[t−12, t−1]` (11 months) against `[t−12, t]` (12 months, last month included) via Barillas et al. (2020); "no significant evidence … of the superiority of the 11-month window".
- **Value weighting:** Figures 15/17 use value-weighted returns with a **10% maximum weight cap** ("To prevent a single large-cap stock from dominating portfolio performance").
- **Penny screen:** exclude stocks **priced below $5 on the portfolio formation date** (Figures 18, 23–26).
- **Crash windows:** Figure 11 uses **9 March 2009 → 28 March 2013** (same window as Daniel & Moskowitz 2016, Figure 2 Panel A) and **24 April 2020 → 30 July 2021**, both at **`α = 10%`**, comparing 6 portfolios (risk-free, market, pure/traditional losers, pure/traditional winners).
- **Short-term reversal variant (Section 6):** identical test with formation window **`[t−1, t]`** (`n ≈ 20.63`), `B = 1000`.

### E. Not specified by the source → `underspecified` / `data gap`

- **Execution timing:** whether the month-end-signal portfolio trades at that close, next session open, or some VWAP — **not stated in source** → `data gap`.
- **Order type, latency, partial fills, price limits, halts:** **not stated in source** → `data gap`.
- **Tie-break / duplicate-handling rules** when two stocks share an identical `p*` or cumulative return at a quantile boundary: **not stated in source** → `data gap`.
- **Maximum position count** above the 10-stock floor, and any ADV/participation cap: **not stated in source** → `data gap`.
- **Short-selling feasibility, borrow recall, stock-loan availability:** **not stated in source** → `data gap`.
- **Position sizing inside each leg:** equal weight (source-specified); no risk parity, no vol scaling, no stop-loss/take-profit/exit rule beyond the fixed 1-month hold → those are **absent, not omitted-by-oversight**, and must not be invented.
- The signal is therefore **reconstructible in portfolio-construction terms but not in execution terms**: an independent researcher can rebuild the portfolios and can *not* reconstruct fills.

## Required data

- **Instrument:** US **common stocks**, CRSP daily returns file; **sharecode 10 or 11**; **exchange code 1, 2, or 3 (NYSE, Amex, Nasdaq)** (§2).
- **Universe filters (§2, source-specified):** valid price before the formation period starts; valid price **and** market capitalization on the formation date; valid return at the end of the formation period; **≥ 70% available values** and **≥ 40% non-zero values** in the formation period. Result: **23,086 stocks, average 3,835 stocks per month.** The source explicitly notes these filters "remove from consideration any stocks that were delisted during the formation period" → **source-disclosed formation-period survivorship.**
- **Delisting treatment:** use the CRSP delisting return when available; for performance-related delisting codes **500 and 520–584** with a missing return, set delisting return to **−30% for NYSE/AMEX** (Shumway 1997) and **−55% for Nasdaq** (Shumway & Warther 1999).
- **Risk-free rate:** **1-month T-bill return from Kenneth French's website**. **Fama–French 5 factors** (Fama & French 2015) and the **momentum factor** also from Kenneth French's site.
- **Timeframe:** daily log returns feed the test; monthly portfolio formation/holding. **Timezone / session convention: not stated in source** → `data gap` (US regular session implied by CRSP, but not asserted by the source).
- **Fields required:** daily close (for returns and for the Gibbs spread estimator), market capitalization, price (penny screen), delisting code/return, dollar volume and Amihud and realized-variance inputs (used in the §3 diagnostics), the effective bid-ask spread series.
- **Point-in-time:** whichever of the two stated formation windows is used (`[t −12, t −1]` per §2 or `[t −11, t −1]` per §4.1), both end strictly before the formation date, so no explicit look-ahead is described; **no revision/vintage handling is discussed** → `data gap`. Train/test boundary: **none described** (see Negative evidence 8).
- **Missing data:** source relies on the CRSP filters above plus **explicit imputation of missing transaction-cost observations** from "the most similar stocks with available cost estimates … Euclidean distance in size and idiosyncratic volatility rank space in line with Novy-Marx and Velikov (2016)" (Appendix A). This imputation is **source-specified and justified**, not a Scout shortcut.
- **Funding / fee / spread needs:**
  - **Spread:** **modeled** — Hasbrouck (2009) effective bid-ask spread, estimated by **Gibbs sampling on daily closing prices**, chosen because it permits a long history and is "highly correlated with the transaction-level estimate" (Appendix A).
  - **Commission, borrow/stock-loan fee, short rebate, market impact, latency, partial fill, leverage/margin/financing, capacity:** **absent from the source → `data gap`, never zero.**

## Execution assumptions

**Source-stated:**

- Order cadence: monthly rebalance at month end; holding 1 month; equal weight (10% cap only in the value-weighted robustness figures).
- **Portfolio cost model (Appendix A, Methods-level read of lines A):** following DeMiguel et al. (2009) (also Novy-Marx & Velikov 2016, Detzel et al. 2023),
  - turnover `TO_t = ½ Σ_{i=1..N} |ω_{i,t} − ω̃_{i,t}|`, where `ω̃_{i,t} = ω_{i,t−1}(1+R^i_t) / Σ ω_{j,t−1}(1+R^j_t)` is the pre-rebalance weight;
  - **`TC_t = Σ_{i=1..N} (c_{i,t} / 2) · |ω_{i,t} − ω̃_{i,t}|`**, with `c_{i,t}` the **relative round-trip transaction cost** of stock `i` at `t` (so half the round trip is charged per unit of weight change);
  - **`R^net_t = Σ ω_{i,t} R^i_t − TC_t`.**
- Cost input = Hasbrouck (2009) effective spread, with early-period gaps imputed by nearest neighbours in size/idio-vol rank space.
- This machinery is applied to the **signal-based** portfolios (Figure 9 net, Figure 14 costs, Figures 17/18, 20, 22, 24, 26, 28, 30, 32, 34) and to the size/weighting/penny/threshold robustness panels.

**Not stated by the source → `data gap` (never modeled as zero):**

- order type (market vs limit), signal-to-order delay, latency, fill model, partial fills/failed trades;
- market impact, participation/ADV capacity, position limits, minimum liquidity;
- **borrow availability, stock-loan fees, recall risk, short rebate** — the short leg's economics rest entirely on these and the source prices only half the spread;
- commissions/brokerage fees, leverage/margin/financing cost, settlement/tax/withdrawal friction.

**Scout reading (labeled):** the source itself cites **Lesmond, Schill & Zhou (2004)**, "The illusory nature of momentum profits", *Journal of Financial Economics* 71(2), 349–380 (in-text form "Lesmond et al. (2004)", PDF p.21; full author list verified in the References, PDF p.38), that standard momentum's gross profits come from frequently trading illiquid, high-cost stocks "especially pronounced when shorting traditional losers" — a spread-only cost model with no borrow fee is therefore the **most likely direction of overstatement for the short leg**. This is Scout interpretation, not a source claim.

## Evidence

### Source-reported

All figures below are **third-party claims by the authors of Amundi WP #188**, traced to the pinned PDF (SHA-256 `30ca5738…020d6e9`), US equities, **July 1963 – December 2022** unless stated. **None has been independently reproduced.**

**Table 1 — "Drift Significance and Momentum", annualized 1-month holding returns in excess of the risk-free rate, volatility, Sharpe.** Table 1's caption states only excess returns / volatility / Sharpe and never mentions transaction costs, while the cost machinery is introduced separately in §4.2 → the table carries **no explicit gross/net label → `underspecified`; the values are treated as gross by Scout reading.**

| Portfolio | Excess return % p.a. (Panel A) | Volatility % p.a. (Panel B) | Sharpe (Panel C) |
|---|---|---|---|
| `HW-LL` (long High-Winners / short Low-Losers) | **19.20** | **30.29** | **0.63** |
| `W-L(25)` (size-matched traditional) | **15.48** | **35.04** | **0.44** |
| `W-L(5)` (5-quintile traditional) | **9.21** | **21.41** | **0.43** |

- Printed p-value pairs under the `W-L` rows (Newey–West paired t, **12 lags**, for returns; two-sample F for variances; Barillas et al. 2020 for max squared Sharpe): Panel A `(0.04) (0.00)`, Panel B `(0.00) (0.00)`, Panel C `(0.04) (0.04)`.
- **Pairing is `underspecified`:** the caption lists the two comparisons as "W-L(5) and W-L(25)" while the column order is `W-L(25), W-L(5), HW-LL`. Scout cross-check on effect magnitude (Panel A: 19.20−9.21 = 9.99 vs 19.20−15.48 = 3.72; Table 2 Small: 21.57−10.02 = 11.55 vs 21.57−14.93 = 6.64) is consistent with **first p ↔ W-L(25), second p ↔ W-L(5)**, i.e. column order. Reported as printed; the pairing is not asserted as source fact.
- **Prose (§4.1):** "The corresponding long-short strategy would have yielded an annualized excess return of **19.20%** over the risk-free rate, considerably higher than the **15.48%** yielded by the traditional momentum long-short strategy, and significantly so, according to a standard t-test." Note the prose's "traditional momentum long-short strategy" = the `W-L(25)` column value (15.48%); the `W-L(5)` column value is 9.21%. **Both are reported here; the source's label wording is loose but the table columns are unambiguous** (verified by the matching Panel B prose: "W–L(5) … volatility is 21.41%" and "using 25 quantiles … its volatility rises to 35.04%").
- **Prose on Sharpe:** "The Sharpe ratio of the HW-LL portfolio is **0.63**, significantly higher than **0.44** of the traditional momentum portfolio with 25 quantiles according to the test statistics of Barillas et al. (2020)."
- Cell-level detail available in the source but not transcribed here: the 5×5 grid places the highest return/vol/Sharpe corners at High-Winners and the worst at Low-Losers; **annualized 5×5 cell volatility range 15.62%–36.47%** (§4.1 prose).

**Signal-based portfolios, gross (§4.2, Figure 5, title "based on signal, gross"):**

- At **`α = 1%`**: **pure winners Sharpe = 0.85**, "93% higher than the Sharpe ratio of traditional winners (**0.44**)", difference statistically significant per Barillas et al. (2020). Footnote 3: the test is significant at the **1% level when α ≤ 3%**, at the **5% level for all other cases except `α = 7%`, significant only at 10%**.
- At **`α = 1%`**: **pure long-short Sharpe = 0.60** vs **traditional long-short = 0.11**; "the difference attenuates as α increases, underlining the importance of testing for profitability".
- Loser leg alone: selling losers "does not appear to be profitable, and the difference between the Sharpe ratio of pure and traditional portfolios is **never significant**."
- Holding-period drift: performance declines as holding period rises from 1 to 12 months (return ↓, risk ↑, Sharpe ↓), but pure beats traditional at all horizons (Figure 6).
- Tail risk: pure long-short shows "substantially lower negative skewness and kurtosis than their traditional counterparts, especially for low values of the significance level" (Figure 7) — **figure-only, exact values `data gap`.**

**Signal-based portfolios, net of cost (§4.2, Figure 9; costs per Appendix A):**

- **`α = 1%`: pure winners net Sharpe = 0.55**, which the source notes is "larger than the **gross** Sharpe ratio of traditional winners".
- **Traditional winners net Sharpe = 0.01**; difference vs pure winners **p = 3.6%**.
- **"Once trading costs are accounted for, the Sharpe ratio of the traditional long–short strategy turns negative."**
- **"On the short side, selling pure losers is no longer profitable after transaction costs, though it remains less unprofitable than shorting traditional losers."**
- Conclusion of §4.2 (verbatim): "**net of transaction costs, it makes sense only to buy the pure winners, since selling the pure losers still implies an increase in volatility and a negative return for the portfolio.**"
- Cost explanation given by the source: "the proposed test tends to reject more for stocks with larger market capitalization, higher liquidity, and lower volatility. Indeed, winners are sensibly less expensive than losers, and pure winners are sensibly less expensive than traditional winners (Figure 8, Panel B)." Pure momentum has "**slightly higher (but practically negligible) average portfolio turnover**" (Figure 8 Panel A) but lower rebalancing cost — **exact turnover and cost levels are plotted only, no printed numbers → `data gap`.**

**Risk-factor attribution (§4.2, Figure 10):** regressions on FF5 + UMD (Carhart 1997 momentum factor) show the pure strategy "exhibits a positive intercept that is statistically significant, **except for the portfolio formed at the 1% significance level**". **Figure-only; no alpha/t values are printed → exact numbers `data gap`.**

**Detection-rate diagnostics (§3,5% level, pooled):**

- **15.28% of positive returns** reveal a significant trend; **14.20% of negative returns** reveal a negative trend.
- By return ventile: in the extreme positive and extreme negative ventiles only **32.30%** and **47.05%** of cases are significant → "**more than half of stocks with the largest returns are not significant … suggesting that their large returns are illusory**".
- Conditional patterns (Figure 2): positive drift significant for high-volume / low-Amihud / low-spread stocks; negative drift significant at the opposite (illiquid, high-cost) end; significant positive drift concentrates in low-volatility periods, negative drift in high-volatility periods.

**Short-term reversal (§6):** at `α = 5%`, significant positive trend in **8.66%** and significant negative trend in **9.04%** of instances (`n ≈ 20.63`). **Buying pure losers beats buying traditional losers only under value weighting and/or penny exclusion, and stays positive net of costs** (Figures 15 and 25); "buying pure winners" of the last month is profitable, i.e. the last month should not be skipped for winners.

**Momentum crashes (§5, Figure 11, `α = 10%`):** over **9 Mar 2009 → 28 Mar 2013**, "pure loser portfolio would have lost roughly a 40% of traditional loser portfolio (**−3.55 vs −5.39**)", i.e. traditional losers' losses "at least 40% higher"; pure winners outperform traditional winners in the same window. Panel B (24 Apr 2020 → 30 Jul 2021) is qualitative in the text → exact values `data gap`. Source's own verdict: the test "**helps mitigating the impact of momentum crashes, although it remains challenging to eliminate them entirely**."

**Size split (Table 2, same July 1963–December 2022 window, NYSE median market cap breakpoint):**

| | Excess % p.a. | Vol % p.a. | Sharpe | p (Sharpe pair) |
|---|---|---|---|---|
| Small `HW-LL` | **21.57** | **30.32** | **0.71** | vs W-L(25) `(0.03)` |
| Small `W-L(25)` | 14.93 | 36.28 | 0.41 | — |
| Small `W-L(5)` | 10.02 | 21.91 | 0.46 | — |
| Large `HW-LL` | **8.80** | **24.53** | **0.36** | vs W-L(25) `(0.13)` |
| Large `W-L(25)` | 13.55 | 29.39 | 0.46 | — |
| Large `W-L(5)` | 4.00 | 18.65 | 0.21 | — |

- Return p-value pairs: Small `(0.01) (0.00)`; Large `(0.01) (0.00)`. Volatility p-value pairs: Small `(0.00) (0.00)`; Large `(0.00) (0.00)`.
- **Prose (§7.1):** "the Sharpe ratio of the HW-LL portfolio is significantly higher than that of the W-L(25) for small-cap stocks (**0.71 vs 0.41**), but **lower for large-cap stocks (0.36 vs 0.46) but the difference is not significant**."
- Prose states the HW-LL return is "significantly increased by **11.57%**" (Small) and "enhanced by **4.80%**" (Large); Scout arithmetic shows these are HW-LL minus **W-L(5)** (21.57−10.02 = 11.55, 8.80−4.00 = 4.80; the 0.02pp gap is table rounding) — **the comparison base is inferred, not stated.** Sharpe improvement significant at 5% (Small) and 10% (Large).

**Robustness asserted by the source (all figure-only → exact values `data gap`):** value weighting with 10% cap and penny exclusion (Figures 17, 18); extended sample **January 1928 – December 2022** gross and net (Figures 19, 20); 4× MAD truncation threshold (Appendix C, Figures 27–34); threshold-free alternative drift test (Appendix D, Figures 35–36).

**Conclusion (§8, verbatim claims):** "highly significant returns with lower risk, consistently outperforming traditional momentum approaches. **Its performance remains robust both in-sample and out-of-sample, and across different asset universes and holding horizons.** … especially strong for winner portfolios, during crisis periods, and over short holding horizons of one to two months."

### Independently reproduced

`not independently reproduced`

(Scout downloaded and hashed the pinned PDF and read its text layer directly — that verifies **artifact identity and internal text/table consistency only**, not the empirical results. No code, no data, no CRSP access, no re-run of any figure or table. Nothing in this record is our own reproduction.)

### Negative evidence

1. **The short leg does not survive costs, by the source's own numbers.** §4.2: "selling pure losers is no longer profitable after transaction costs"; the traditional long-short net Sharpe **turns negative**; the source's operational conclusion is to buy pure winners only. The headline "pure momentum" L/S Sharpe 0.60 (α=1%) is therefore a **gross** number on a strategy whose short side the source itself discards.
2. **The honest comparator narrows the edge materially.** HW-LL 19.20% vs `W-L(5)` 9.21% confounds stock count (HW-LL holds ~5× fewer names). Against the size-matched `W-L(25)` the gross gap is **19.20 vs 15.48 = +3.72pp**, and the Sharpe gap **0.63 vs 0.44** — real but far smaller than the headline implies, and the `W-L(25)` comparator is *more* volatile (35.04 vs 30.29), so part of the Sharpe gain is a vol effect.
3. **The advantage disappears in large caps.** Table 2 Large: HW-LL Sharpe **0.36 < W-L(25) 0.46**, p = **0.13** (not significant), and HW-LL return **8.80 < 13.55**. The source concedes the return is "significantly smaller for large-cap stocks." The effect is a **small-cap phenomenon**, which collides directly with the test's documented preference for large, liquid, low-vol names and with any capacity claim.
4. **Reversal side is weighting-dependent.** Pure-reversal profitability for the long-loser leg exists **only** value-weighted and/or after excluding penny stocks (§6, Figures 15/25); under the paper's default equal weighting the pure reversal long leg underperforms.
5. **Crashes are mitigated, not removed** — source's own words: "it remains challenging to eliminate them entirely" (§5).
6. **Thin breadth.** Only **15.28% / 14.20%** of formation-period returns are significant at 5%, and **> 50% of extreme-ventile moves are not significant** (32.30% / 47.05%). The eligible cross-section at `α = 1%` is smaller still, so the portfolios sit close to the 10-stock floor → concentrated, path-dependent, and exposed to a single-name shock.
7. **Cost model is spread-only.** Commissions, borrow/stock-loan fees, short rebate, impact, latency, fills, leverage/margin are all **absent → `data gap`**. Given the source's own citation of **Lesmond, Schill & Zhou (2004)** ("The illusory nature of momentum profits", JFE 71(2), 349–380; in-text "Lesmond et al. (2004)", PDF p.21) that momentum profits concentrate in illiquid high-cost names, a spread-only model most plausibly **understates** the short-leg cost, not the reverse.
8. **The "out-of-sample" claim has no supporting protocol.** §8 asserts performance "remains robust both in-sample and out-of-sample", but Sections 2–7 describe **no train/test split, no holdout, no walk-forward, no estimation/evaluation separation** — every reported table and figure uses the single full window July 1963–December 2022 (or January 1928–December 2022). The only sample-period exercise is *extending the start date backwards* (§7.3), which is not an out-of-sample test. → **source-internal overclaim / `data gap`.**
9. **The "across different asset universes" claim contradicts the body.** §8 asserts cross-universe robustness; §8's own next paragraph says: "A natural extension of our analysis is to examine the performance of pure momentum strategies across different asset classes, including bonds, currencies, and commodities, and in international equity markets … **We leave this investigation for future research.**" The body covers **US equities only**. → **source-internal contradiction.**
10. **Multiplicity is uncontrolled.** The `α` grid (1–10%) is scanned, the best cell (`α = 1%`) is the one quoted in prose, Barillas tests are run per α, and 36+ figures are produced across weighting/penny/threshold/sample variations — with **no multiple-testing correction anywhere → `data gap`.** (Footnote 3 itself shows the significance level degrading at `α = 7%`.)
11. **Bootstrap resolution floor.** With `B = 1000` the smallest attainable `p*` is `0.001`, so the `α = 1%` selection sits exactly on the bootstrap's resolution floor; classification at the tightest grid point is therefore sensitive to Monte-Carlo noise in `p*` (Scout observation; the source does not address it).
12. **Source quality / publication bias.** Working paper #188, released as *Marketing Communication* restricted to professional clients, sponsored by an asset manager's research institute with two of three authors at the sponsoring Chair's academic partner; **not peer reviewed, no DOI, no arXiv/SSRN, no code, no data availability statement**, CRSP licensed → **non-reproducible by construction.** Zero stars-level external scrutiny identified.
13. **Adjacent same-universe negative evidence in this repository** (independent sources, cited for Intake context, not merged into the claims above): `directional-anomaly-zoo-net-cost-audit-quality-survivor-2026-09-23` reports **equity momentum 12-1 net −0.01 / gross 0.03 (2016–20)** at 10 bp/side and a **2015–2025 momentum factor Sharpe of 0.25**, with the cost cascade cutting positive-OOS predictors 86% → 43% → 19% at 0/30/60 bp per month; `binance-perpetual-cross-sectional-momentum-taker-cost-falsification-2026-09-13` shows momentum dying at retail taker fees in a crypto panel. Both indicate the *baseline* being purified is already fragile net of cost.
14. **No benchmark against alternative denoisers.** The source compares only against its own cumulative-return control — never against volatility-scaled momentum (Barroso & Santa-Clara 2015, cited in its own reference list), against Barroso & Detzel (2021) (which it cites only to note volatility-scaling profits vanish with costs), against skip-month/residual momentum (Blitz, Huij & Martens 2011, cited), or against a plain size/liquidity/volatility-matched control. Without those, **incremental value over a simpler tilt is undemonstrated.**
15. **Table 1 gross/net label is `underspecified`**, and the **p-value column pairing is `underspecified`**; both are reported above as printed rather than resolved.

## Falsification plan

Thresholds below are **`research-defined falsification thresholds` (Scout-chosen, not source-specified)** unless marked source. Data for all tests: a point-in-time daily US-equity panel plus a point-in-time cost panel including borrow.

1. **F1 — Frozen forward window (research-defined).** Data: all formations with formation-end date **after 2026-12-31**, no re-tuning of `α`, `κ_n`, or the 10-stock floor. Metric: net Sharpe of pure winners at `α = 1%` vs net Sharpe of `W-L(25)`. **Threshold:** pure-winner net Sharpe **≤ 0**, or **≤** `W-L(25)` net Sharpe ⇒ **reject** the purification claim. Action: record downgraded to `rejected`.
2. **F2 — Full-cost ladder (research-defined).** Data: same window; cost model extended with commissions **1/3/5 bp per side**, borrow fee **0/10/25/50 bp per year of short notional**, 10% ADV participation cap, and a square-root impact term. Metric: net Sharpe. **Threshold:** pure winners fall below `W-L(25)` net at **any rung ≤ 20 bp/side**, or pure-loser leg net Sharpe **≤ 0** at the source's own 5 bp-equivalent rung ⇒ **reject** the cost-robustness claim for that leg. Action: leg marked cost-fragile; L/S headline withdrawn.
3. **F3 — Large-cap hold-out (research-defined).** Data: NYSE-median-market-cap Large group only, full window. Metric: Sharpe(HW-LL) − Sharpe(`W-L(25)`). **Threshold:** difference **≤ 0 with p ≥ 0.10** ⇒ **reject** "robust across universes". Action: scope narrows to small caps and any capacity claim is voided. *(The source's own Table 2 already sits at 0.36 vs 0.46, p = 0.13 — this test is likely to fail.)*
4. **F4 — Multiple-testing audit (research-defined).** Data: the full reported grid (α × leg × equal/value × penny × threshold × sample). Procedure: Benjamini–Hochberg **q = 0.10** across all "pure beats traditional" superiority cells, plus a deflated-Sharpe check. **Threshold:** **< 50%** of reported superiority cells survive ⇒ **reject** the headline as multiplicity-driven. Action: report only the surviving cells.
5. **F5 — Label-permutation placebo (research-defined).** Procedure: circularly shift the `p*` series by ≥ 12 months (preserving cross-sectional structure), 1,000 draws, rebuild pure winners at `α = 1%`. **Threshold:** placebo net Sharpe **within 0.10** of the real net Sharpe ⇒ **reject** (signal is calendar/structure artifact). Action: signal declared non-discriminating.
6. **F6 — Rival-explanation ablation (research-defined; the decisive test).** Procedure: build a control portfolio selecting the same number of stocks by **size × dollar-volume × idiosyncratic-volatility deciles only**, matched to the pure-winner set's documented rejection profile, with no return-trend input. Metric: net Sharpe and net alpha vs FF5+UMD. **Threshold:** control matches pure winners within **0.05 Sharpe** ⇒ **reject** the "trend detection" mechanism and reclassify the record as a repackaged large/liquid/low-vol tilt. Action: mechanism section rewritten; strategy re-labeled.
7. **F7 — Truncation-threshold perturbation.** Procedure: re-run at `κ_n = 2, 3, 4` MAD (4 is source Appendix C), same everything else. **Threshold:** `α = 1%` pure-winner net Sharpe range **> 0.15** across the three ⇒ **reject** as parameter-fragile. Action: mark `underspecified` parameter sensitivity.
8. **F8 — Bootstrap resolution stress (research-defined).** Procedure: raise `B` from **1000 → 10000** with a fixed random seed set, re-select at `α = 1%`. **Threshold:** **> 10%** of selected names change classification ⇒ **reject** the `α = 1%` headline (selection driven by Monte-Carlo noise at the `p* = 0.001` floor). Action: re-report at `α ≥ 2%` only.
9. **F9 — Walk-forward / regime split (research-defined).** Procedure: rolling 5-year non-overlapping evaluation windows across 1963–2026, no in-window parameter choice. **Threshold:** net Sharpe **≤ 0 in ≥ 40%** of windows, or the 2009/2020 crash windows contributing **> 30%** of total net profit ⇒ **reject** as regime-fragile. Action: record downgraded to `rejected` for production interest.
10. **F10 — Short-leg independent test (research-defined).** Procedure: trade only the pure-loser leg long-short with an explicit borrow feed and recall stress. **Threshold:** net Sharpe **≤ 0** ⇒ **confirm the source's own finding**, strike the L/S headline and record the strategy as long-only. Action: signal specification amended to long-only.
11. **F11 — Turnover audit (research-defined).** Metric: annualized one-way turnover of pure winners at `α = 1%` (source reports it only as Figure 8 plots). **Threshold:** **> 100% per year** ⇒ flag the source's spread-only cost model as understating friction; re-run F2 from the 10 bp/side rung. Action: cost model replaced before any further use.
12. **F12 — Competing-denoiser benchmark (research-defined).** Procedure: compare against volatility-scaled momentum (Barroso–Santa-Clara / Barroso–Detzel) and residual momentum (Blitz et al. 2011) under the identical cost model and equal-count control. **Threshold:** pure winners fail to beat **each** by **≥ 0.10 net Sharpe** ⇒ **reject** incremental value. Action: record becomes background reading, not a candidate.

## Crypto portability

**`unproven`.**

- The source contains **zero crypto evidence** and explicitly defers every non-US-equity asset class to future research (§8). No claim here may be read as crypto empirical evidence.
- **Form-transfer argument (Scout interpretation, not source):** the drift test is a statistical procedure on a return series, so in *form* it is market-agnostic and could be applied to a cross-section of liquid BTC/ETH perpetual returns. That makes the hypothesis **testable**, not **demonstrated**.
- **Crypto-specific risks that break the port:**
  - **Shorting losers** on perps requires funding payments, an initial/maintenance margin, and exposes liquidation chains — none of which the source prices (its cost model is a half-spread only). The source's own finding that the short leg dies even under a *cheap* cost model makes crypto's short leg the least likely to survive.
  - **24/7 sessions** change `n` (a "230 daily returns" window no longer aligns to exchange sessions) and remove the natural month/session boundary the source's rebalance calendar assumes; timestamp/candle conventions and venue-specific session cuts must be redefined.
  - **Funding, mark/index price, and basis** are entirely absent from the source — these dominate perp holding cost and would have to be added to `TC_t`, invalidating the Appendix A arithmetic as-is.
  - **Venue fragmentation and survivorship:** the source relies on CRSP sharecode/exchange filters and a Shumway-style delisting return convention; crypto has no equivalent point-in-time listing/delisting registry, severe delisting survivorship, and no stable universe definition.
  - **Estimator dependence:** the Hasbrouck (2009) Gibbs effective-spread estimator is calibrated on equity daily closes; reusing it on crypto prints is unvalidated.
  - **Jump/truncation behavior:** crypto exhibits far more frequent jumps and volatility clustering, so the 3× MAD truncation and the wild-bootstrap null may mis-calibrate; `κ_n` would need re-derivation (see F7).
- **Status:** any crypto implementation would be a **new, separately validated hypothesis** requiring at minimum F1, F2, F5 and F6 re-run on a crypto panel. Crypto portability is **not** authorization to trade.

## Limitations

- **Source quality:** working paper released as restricted-audience **marketing communication**; **not peer reviewed; no DOI; no arXiv/SSRN version; no code; no data availability statement**; CRSP licensed → **results are not publicly reproducible**.
- **Identification:** the mechanism claim (overconfidence / slow bad-news incorporation) is **asserted, not separately identified**; the strong rival explanation (large/liquid/low-vol selection bias) is **documented by the source but never ablated**.
- **Internal contradictions:** "in-sample and out-of-sample" with **no OOS protocol in the body**; "across different asset universes" while the body covers US equities only and defers other asset classes to future work.
- **Sample/regime:** July 1963–December 2022 (robustness only extends the *start* to 1928); no evaluation of 2023–2026 conditions; two hand-picked crash windows.
- **Multiplicity:** α grid × weighting × penny × threshold × sample with **no correction**; best-cell reporting in prose.
- **Cost/execution:** spread-only cost model; **commissions, borrow, impact, latency, fills, leverage, capacity all `data gap`**; no order type or fill timing stated; turnover figures are plot-only.
- **`underspecified` in source:** Table 1 gross/net label; p-value column pairing; execution timestamps; timezone; tie-breaks; max position count; point-in-time revisions.
- **Statistical:** `B = 1000` puts `α = 1%` on the p-value resolution floor; no confidence intervals around the reported Sharpe differences beyond the Barillas test; no deflated Sharpe; no capacity/ADV analysis; equal weighting across 3,835 names/month including very small issuers.
- **Reproducibility:** `not independently reproduced`; the underlying drift test's asymptotics live in a *separate* unpublished working paper (Renò & Shi, 2025) that this record has not verified.
- **Incremental-write check (spec §Limitations):** this qualifies as a **new family** — drift-significance filtering of a cross-sectional momentum signal is materially distinct from the repository's existing vol-managed, residual, frog-in-the-pan, t-statistic-momentum, ETF-operational, commodity-curve and crypto momentum records in **mechanism (statistical trend verification vs. risk scaling / carry / discretion), signal construction (wild-bootstrap p-value vs. return/volume/funding transforms), and universe (US CRSP equities)**. It is not a reframing of an existing record.
- `not independently reproduced` (repeated deliberately: no table, figure or statistic in this record has been recomputed by us).

## Implementation status

`implementation_status: not-implemented`

Nothing has been built. No drift test implemented, no bootstrap p-value pipeline, no portfolio construction, no CRSP access, no Qlib backtest, no Paper/Testnet/Live work, no strategy family created. This document is a normalized research capture of a third-party working paper. It does not modify NautilusTrader or any downstream runtime.

## Adoption boundary

`status: research-only` · `adoption: not-approved` · `approval_scope: research-only`

Presence of this record in the staging repository means only that normalized, source-traceable research material exists here. It does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. No wording, evidence count, confidence value, or section order in this record promotes it. Any later adoption or implementation decision must be explicit, separately reviewed, and based on this record plus current live sources.

## Related Wiki records

Read-only `kb_search` on 2026-09-26 (no writes performed). Queries returning **zero** results are listed so the gap is explicit: `momentum crash transaction cost illusory trend significance filter` → 0; `equity cross-sectional momentum winners losers overconfidence` → 0; `momentum crash Daniel Moskowitz` → 0 → **there is no dedicated Wiki Brain page for illusory/hidden momentum, drift-significance filtering, or momentum crashes.**

Verified pages returned and used for dedup/context (linked, not quoted):

- [[quant/size-enhanced-left-side-momentum-resga-expected-shortfall-2026-09-04]] — adjacent US-equity cross-sectional momentum record with an independent signal construction and its own cost/tail evidence.
- [[quant/llm-news-enhanced-cross-sectional-momentum-tilt]] — adjacent equity momentum tilt from a different data dependency.
- [[quant/sec-form-13f-institutional-cloning-staleness-falsification-2026-09-13]] — adjacent US-equity record whose central constraint is point-in-time disclosure lag.
- [[quant/crypto-residual-momentum-market-beta-neutralization-2026-09-11]] — crypto residual-momentum record; different market, different signal construction.

Repository-adjacent records (same repo paths, cited as context in Negative evidence; **not** Wiki links): `directional-anomaly-zoo-net-cost-audit-quality-survivor-2026-09-23.md`, `binance-perpetual-cross-sectional-momentum-taker-cost-falsification-2026-09-13.md`, `etf-momentum-operational-rules-super-category-diversification-trailing-stop-2026-09-23.md`.

No record was found whose source identity or mechanism matches this one; nothing was updated, merged or overwritten.

## Sources

1. **Amundi Research Center**, "Pure Momentum Strategies" landing page — `https://research-center.amundi.com/article/pure-momentum` — page date **2026-03-25**, HTTP 200, retrieved **2026-09-26** (HTML 150481 bytes, SHA-256 `56289a2aae0a24f36f5ca518791ee86c5946fc70f0de4da8951f2bc6922d1569`). Landing page lists the paper under *Working Papers*, author meta `Amundi`, and links the PDF below.
2. **Amundi Investment Institute Working Paper #188**, "Pure momentum*", Roberto Renò (ESSEC), Roméo Tédongap (ESSEC), Xinyi Zhang (University of Warwick); cover `WORKING PAPER #188 | MARCH 2026`, manuscript title page dated **November 14, 2025**; PDF `https://research-center.amundi.com/files/nuxeo/dl/d7bc1c57-7420-4526-8dd4-af51d5ff5fb3?inline=` — **2,416,626 bytes**, **SHA-256 `30ca573883921ac7e35a63fd15cb6e899c708e406df92c436eafb70da020d6e9`**, 55 pages, retrieved **2026-09-26**. Locations used (PDF page numbers of the pinned 55-page file, heading positions re-verified 2026-09-26): title page/abstract (p.3), §1 Introduction (heading p.4), §2 Data and methodology (heading p.9), §3 When is momentum significant? (heading p.12, runs to p.14), §4 Is pure momentum trading profitable? (heading p.15), §4.1 Table 1 (p.16–17), §4.2 Figures 5–10 (p.18–24, Figure 5 caption p.19, Figure 9 p.23, Figure 10 p.24), §5 Pure momentum crashes? (heading p.24, Figure 11 p.25), §6 Short-term reversals (heading p.26, Figures 12–16 captions p.27–30), §7 Robustness (heading p.30, Table 2 p.32), §8 Conclusion (heading p.33), References (heading p.34, entries p.34–38), Appendix A transaction cost calculations (heading p.39), Appendix B (heading p.40), Appendix C Robustness to the threshold (heading p.47, runs to p.53), Appendix D Testing without thresholding (heading p.54, runs to p.55).
3. **No DOI, no journal, no arXiv ID, no SSRN ID, no code repository, no data-availability statement** — verified absent from the pinned PDF and from a public web search on **2026-09-26**.

**Method / citation dependencies named inside source #2 (cited, not used as evidence here; author lists re-checked against the References section, PDF p.34–38, on 2026-09-26):** Renò & Shi (2025) "Drift sign. Working Paper." (the drift test itself); Hasbrouck (2009) effective bid-ask spread; **DeMiguel, Garlappi & Uppal (2009)** turnover/cost aggregation (in-text "DeMiguel et al. (2009)"; References p.36); Novy-Marx & Velikov (2016); Detzel et al. (2023); **Barillas, Kan, Robotti & Shanken (2020)** Sharpe comparison, "Model comparison with Sharpe ratios", JFQA 55(6), 1840–1874 (References p.35); Jegadeesh & Titman (1993); Fama & French (1996, 2008, 2015); Daniel & Moskowitz (2016) momentum crashes; **Lesmond, Schill & Zhou (2004)**, "The illusory nature of momentum profits", JFE 71(2), 349–380 (References p.38); Avramov, Chordia & Goyal (2006); Da et al. (2014); Medhat & Schmeling (2022); Shumway (1997); Shumway & Warther (1999); Barroso & Santa-Clara (2015); Barroso & Detzel (2021); Blitz, Huij & Martens (2011); Carhart (1997).
