---
schema: strategy-research-record-v1
title: "Moving Average Distance (MAD) cross-sectional anchoring long–short in US equities — plus fundamentals-based Performance Deviation Index (PDI) (SSRN 3111334 working paper)"
created: 2026-09-26
updated: 2026-09-26
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - us-equities
  - cross-sectional
  - momentum
  - technical-analysis
  - anchoring
  - transaction-costs
  - working-paper
  - negative-evidence
status: research-only
confidence: medium
source_as_of: 2018-10-03
sources:
  - "https://anderson-review.ucla.edu/wp-content/uploads/2021/03/Avramov-Kaplanski-Subra_2018_SSRN-id3111334.pdf (PINNED PRIMARY: 1,844,843 bytes, SHA-256 0aed1cbc651e334f0bafd3694310d31a2a57a41cacd9a529670346d8cb609e85, 77 pages, PDF /CreationDate D:20181003092421, retrieved 2026-09-26)"
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3111334 (SSRN abstract page — HTTP 403 Cloudflare challenge on 2026-09-26 via curl AND browser; current SSRN revision could not be opened)"
  - "https://onlinelibrary.wiley.com/doi/10.1002/rfe.1118 (peer-reviewed related article 'Moving average distance as a predictor of equity returns', Review of Financial Economics 39(2):127-145, first published 18 September 2020 — landing page + abstract read 2026-09-26; full text paywalled, /doi/full redirects to /doi/abs)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Moving Average Distance (MAD) cross-sectional anchoring long–short in US equities — plus fundamentals-based Performance Deviation Index (PDI) (SSRN 3111334 working paper)

## Provenance

**Primary source (one document, pinned by content hash):**

- **PDF:** `https://anderson-review.ucla.edu/wp-content/uploads/2021/03/Avramov-Kaplanski-Subra_2018_SSRN-id3111334.pdf` — **1,844,843 bytes**, **SHA-256 `0aed1cbc651e334f0bafd3694310d31a2a57a41cacd9a529670346d8cb609e85`**, retrieved 2026-09-26 (curl, HTTP 200). **77 pages** (pypdf). PDF metadata: `/Title: Microsoft Word - avma28`, `/CreationDate: D:20181003092421`, `/Producer: GPL Ghostscript 8.15`. Hosted on the UCLA Anderson Review site (URL path `/2021/03/`, i.e. hosted in 2021; the document itself is the 3 Oct 2018 PDF build).
- **Every page footer of the pinned document (verbatim):** `Electronic copy available at: https://ssrn.com/abstract=3111334` → SSRN abstract id **3111334** is the source identity.
- **Title (pinned PDF, p.1):** *Stock Return Predictability: New Evidence from Moving Averages of Prices and Firm Fundamentals*.
- **Author list (pinned PDF, p.1, exactly as printed):** **Doron Avramov** (IDC Herzliya), **Guy Kaplanski** (Bar-Ilan University), **Avanidhar Subrahmanyam** (The Anderson School at UCLA, corresponding author; e-mail printed `subra@anderson.ucla.edu` in the related journal version). Keywords: momentum, behavioral finance, time series. JEL: G12, G14.
- **Version/date:** PDF build date **2018-10-03**. The SSRN *posting* date and the existence of any later SSRN revision are **`not stated in source`** — `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3111334` and `…/Delivery.cfm?abstractid=3111334` both returned **HTTP 403 (Cloudflare)** on 2026-09-26 from curl *and* from a browser, so the current SSRN text could not be diffed against this PDF.
- **Publication status (peer-review relationship):** the pinned document carries **no DOI, no journal, no peer-review statement** anywhere (keyword scan of all 77 pages). A **peer-reviewed related article by the same three authors with a different title** was opened and verified at Wiley on 2026-09-26: **Avramov, D., Kaplanski, G., & Subrahmanyam, A., "Moving average distance as a predictor of equity returns", *Review of Financial Economics* 39(2), April 2021, pp. 127–145, DOI `10.1002/rfe.1118`, "First published: 18 September 2020", article type "Original Article"**, whose printed acknowledgment thanks "an anonymous referee". Its full text is **paywalled** (`/doi/full/10.1002/rfe.1118` redirects to `/doi/abs/…`), so **every performance number, sample window, universe detail and cost treatment of the journal version is `data gap` in this record and is NOT used.** Whether the pinned 2018 manuscript *is* an earlier revision of that article is **`not verified`** (secondary listings assert SSRN 3111334 now carries the title *Moving Average Distance as a Predictor of Equity Returns*; that is a **source-reported claim of a secondary source, not verified**, because SSRN returns 403).
- **Sample period (pinned PDF §2, p.6 and every table caption):** **June 1977 to October 2015**; **806,485 monthly returns for 8,367 firms**. Exception: Table 6 (PDI) caption says **June 1977 to October 2017** "whereas the Baker and Wurgler sentiment data is up to 2015"; the international section starts **2001**; §1 prose refers to "the recent 2001-2016 period". These internal date inconsistencies are recorded in **Limitations** and are not silently reconciled.
- **Universe (§2, p.6):** all U.S. firms on **NYSE, AMEX, NASDAQ** with CRSP **share codes 10 and 11** (common stock) and **positive prior-year book equity in Compustat**; excludes EOM price **<$5**, stocks **not traded that month**, stocks **without the previous 12 months of return observations**, and stocks without the control-variable records; requires **≥2 years of Compustat listing** (Fama-French 1993 backfill guard); accounting data updated **end of June each year**; **delisting returns from the CRSP daily delisting file** are added following Shumway (1997).
- **Transaction-cost treatment (read in §5 "Transaction costs", pp.23–25, plus Table 8 caption — not inferred from the abstract):** the paper reports **two break-even transaction-cost statistics only**; it prints **no net-of-cost return series, no fee schedule, no bid-ask/impact/fill model, and no turnover figure for any strategy**. Benchmarks used for perspective are external (Korajczyk–Sadka 2004 effective spreads; Novy-Marx–Velikov 2016 monthly costs). Full detail in **Execution assumptions**.
- **Core performance numbers** are quoted below **only** with their Table/Figure/Section provenance in the pinned 2018 PDF, always labelled **gross** (before costs). No number from the Wiley journal version or from any blog is reused as a result.
- **Data/code availability:** keyword scan of all 77 pages for `github`, `code availability`, `data availability`, `available at`, `available upon request`, `replication` → the only hits are the SSRN footer, the sentence about real-time accounting-data release dates (§2), and "guarantee data availability" about accounting records. → **no data-availability statement, no code-availability statement, no repository**: all availability fields `not stated in source`. CRSP/Compustat/I-B-E/S/WRDS are **licensed**, so results are **not publicly reproducible**.
- **How it was read:** the PDF text layer was extracted with `pypdf` (page-level, all 77 pages) and **§1, §2, §3.1–§3.3, §4.1–§4.4, §5, §6, §7, §8, Appendix A plus Tables 1–10 and 12 were read directly** — not via any secondary summary. Equation (1)'s stacked fraction extracts in ambiguous line order in plain text; the ratio direction was therefore re-verified from **Appendix A verbatim** ("Moving Average Distance (MAD) = 21-day moving average/200-day moving average") and cross-checked against the threshold logic in the Table 5 caption (`long MAD ≥ 1.1` / `short MAD ≤ 0.9`) and the journal abstract's "ratios of 21-day to 200-day moving averages".
- **Deduplication (step 5, deterministic, whole repository):** content search across **all** `*.md` under the repo root (including the untracked hidden trees `.mimo-worktrees/`, `.agents/`, `.hermes/`) and `coverage_manifest.csv` returned **0 hits** for every source-identity token: `3111334`, `10.1002/rfe.1118`, `rfe.1118`, `Kaplanski`, `MRAT`, `Performance Deviation Index`, `Moving Average Distance as a Predictor`, `Stock Return Predictability: New Evidence`. Broad mechanism sweep `moving average distance` → only two **incidental** phrase hits inside other records (`cross-sectional-equity-ridge-percentile-rank-alpha-2026-09-03.md` "porting rationale", `alphaschema-…` example list); `Avramov` → only **Avramov & He, arXiv:2602.20856** (SDF-orthogonalized downside-beta anomaly mining — **different paper, different authors, different mechanism**); `anchoring` → only two incidental phrase uses. **No existing record covers this source** → new record permitted under the hard cap of one.

## Economic mechanism

### Source-reported

The paper's stated mechanism is **anchoring bias** (Tversky & Kahneman, 1974): investors anchor on a long-run moving average — MA(200), the most popular long-term anchor per Brock, LeBaron & Lakonishok (1992) and the longest MA used by Han, Yang & Zhou (2013). §1's worked example: if the anchor is 40 and news says fair value is 60, the gap is large so agents underreact, the short-run average only creeps toward 50, and price then **drifts** the remaining distance; if news says 41, the gap is negligible and price adjusts immediately. Hence **the magnitude of the short-run/long-run distance measures the degree of underreaction** — not the mere fact of a crossover.

Source-reported consequences the paper tests: (a) the effect should be **stronger for sudden (vs gradual) price changes**; (b) because underreaction should not undo itself, **profits do not reverse even at 24–36 months**, which the authors argue rules out *continuing overreaction*; (c) the risk explanation is "challenging" because returns survive factor models and top-MAD stocks are not riskier on the measures used; (d) the gradual-diffusion explanation is challenged because top MAD stocks are **large, liquid, institutionally held, closely covered and have dispersion no higher** than the rest of the cross-section (Table 9 Panel B: top MAD market cap $1,664m vs bottom $1,187m; turnover 0.22 vs 0.18; institutional share 0.37 vs 0.37; analysts 3.55 vs 4.69). Conditioning on recent earnings surprises and analyst recommendation changes leaves MAD's predictive slope significant (§4.4), which the authors read as *agreement* of price drift with news sign rather than independent information. The same anchor logic is applied to **fundamentals** — the *Performance Deviation Index* (PDI) measures the deviation of the latest quarterly accounting figures from their trailing three-quarter mean, on the view that investors anchor on trailing accounting averages (§4.1).

The source is explicit that it is documenting **predictability**, not a causal structural estimate.

### Research interpretation

Falsifiable hypothesis: **cross-sectional continuation is an increasing function of a stock's distance from a long-horizon anchor**, and the anchor is *specifically the 200-day price average* (plus the accounting-mean anchor for PDI) rather than "momentum" in general. The mechanism makes separable, testable predictions: (i) the *ratio* should beat the *crossover* dummy (a crossover only measures sign, not distance); (ii) the effect should survive conditioning on classic momentum (months −2…−6), 52-week high and the Han-Zhou-Zhu trend factor; (iii) it should be a **long-side** phenomenon if underreaction among marginal buyers dominates short-side constraints; (iv) it should decay to zero (or turn insignificant) by 13–24 months rather than reverse.

Component roles (for schema completeness): **primary signal** = MAD = MA(21)/MA(200) (cross-sectional ratio); **alternative/secondary signal** = PDI (fundamentals deviation) and the binary MAS/MDS signal variants; **risk overlay** = none specified by the source; **horizon** = 1–24 months (reported holding periods 1/3/6/12/18/24; strongest at 2–6 months); **exit rule / stop / sizing / leverage** = **not specified by source** → any such choice is `research-proposed`.

## Signal

**Exact source-reported definition (Appendix A + §2 equation (1) + Table 5 caption):**

- `MAD = MA(21) / MA(200)` — arithmetic mean of the last **21** daily closes divided by the mean of the last **200** daily closes; **prices adjusted for splits and dividend distributions** (§2). Appendix A verbatim: "Moving Average Distance (MAD) = 21-day moving average/200-day moving average of stock".
- **Descriptive statistic (Table 1 Panel A):** MAD mean **1.050**, standard deviation **0.210**.
- **Robustness variants stated in footnote 6 (§2):** long anchor **MA(250)** ("the approximate annual moving average in terms of trading days") and short-term moving averages ranging from **5 to 35 trading days**. Numerator averaged over recent prices because a single day is a noisy proxy.
- **Binary / signal variants (§2):** `MAS` — price **above** the 200-day moving average; `MDS`/MAD signal — **unity if MAD exceeds (falls below) specified thresholds** (i.e. a >1 / ≤1 indicator in the Table 5 usage).
- **Discretized threshold variable (Table 2 caption):** `MAD Threshold = γ` records **+1 if MAD > 1+γ, −1 if MAD < 1−γ, else 0**, with **γ ∈ {0.1, 0.2, 0.3}**.
- **PDI (§4.1):** seven items — Cash & short-term investments, Retained Earnings, Operating Income, Sales, CAPEX, Invested Capital, Inventories — extended with IB; deviation = latest quarterly release (**used only if it falls within the previous six months**) minus the mean of the preceding three quarters, **scaled by total assets**; each deviation **percentile-ranked against all stocks over the previous year**, sign-flipped for invested capital and inventories (sign convention in §4.1), **equally weighted across items monthly**; **90-day assumed release lag** when the exact release date is unavailable.

**Portfolio construction (source-reported, Table 5 caption, §3.1–§3.3):**

- **Rebalance:** monthly; portfolios "constructed by equally weighting stocks"; Table 1/3/4/5 report **next month's** average returns, so formation uses data through month-end and the return measured is the following month's. **Exact formation timestamp, timezone, and execution price (close vs next open) are `underspecified` in the source.**
- **Holding periods reported:** 1, 3, 6, 12, 18, 24 months; for horizons beyond one month the source states "portfolios with different time horizons are equal-weighted" (Jegadeesh–Titman 1993 rebalancing). The precise aggregation of overlapping cohorts across horizons is `underspecified`.
- **Five zero-cost strategies compared:** (1) **MAD signal** — long MAD>1, short MAD≤1; (2) **MAD decile** — long top decile, short bottom decile of the MAD cross-section; (3)–(5) **MAD threshold 0.1 / 0.2 / 0.3** — long MAD ≥ 1+γ, short MAD ≤ 1−γ. A sixth, **PDI decile**, is run alongside for the fundamentals anchor.
- **Sorts used elsewhere:** top 30% / mid 40% / bottom 30% double sorts vs MOM, 52HIGH, TRND (Table 3); 10×10 sequential independent MAD×MOM sorts (Table 4); decile sorts for all horizons in Tables 1 and 5.
- **Market/industry timing rule (§6, Table 10 caption):** buy the industry/market index each month if `MAD > 1` (signal) else T-bills; the **threshold** version buys `(1/e × index − (1−1/e) × T-bills)` if `MAD > 1 + threshold`, where `e = (#months MAD > 1+threshold) / (#months MAD > 1)` over a rolling window that grows to the first 60 months then stays at 60 — "ensures the average exposure to the market over the sample period is the same across strategies". Market-level thresholds are **0.025 and 0.05** (PDI uses 0.5 and 0.0125, "equivalent to the first MAD threshold of 0.025"). Note this timing rule is **not** the cross-sectional long-short; do not mix the two.
- **International rule (§7):** from **2001**, all WRDS countries **excluding Greece and the Czech Republic** (incomplete data); IMF T-bill rate as risk-free (fallback: market interest rate, then 3-month deposit rate); market-timing threshold **0.05**.
- **Not specified by source → `research-proposed` / `data gap`:** position sizing, stop-loss, risk targeting, leverage, margin, borrow availability and stock-loan fee for the short leg, liquidity/ADV screens, any capacity constraint, and the ordering/limit discipline around month-end formation.

## Required data

- Daily, **split- and dividend-adjusted** closes for all NYSE/AMEX/NASDAQ common stocks (share codes 10/11), with ≥200 trading days of history for MA(200).
- **CRSP** monthly returns **plus the CRSP daily delisting file** (delisting returns must be added per Shumway 1997 or the cross-section is contaminated).
- **Compustat** annual + quarterly fundamentals: positive prior-year book equity, ≥2 years of listing; the **7 accounting items** needed for PDI.
- Controls used by the source require: ME, BE/ME, Han-Zhou-Zhu trend, Ang idiosyncratic volatility, turnover, Amihud illiquidity, 52-week-high ratio, SUE (8 quarters), I/B/E/S recommendation revision & dispersion, net issues, asset growth, Y/B, I/A, ROE, GP, accruals, ROA, NOA, Ohlson O-score, Baker-Wurgler sentiment index, Ken French industry factors, CRSP VW index + 30-day T-bills; **19 firm-level predictive characteristics** are stated as controls in §2.
- **Point-in-time discipline (source-reported):** accounting data updated **end of June** each year; **≥2-year Compustat listing**; **90-day release lag** for PDI when release dates are missing; delisting returns included.
- **Missing data (source-reported):** stocks lacking 12 months of returns, not traded that month, priced <$5, or missing control records are **excluded**; imputation beyond that is `not stated in source`.
- **Timezone / calendar / candle boundaries:** `data gap` (US equity session is implied but never stated).
- **Crypto data:** none — the source contains **zero** crypto evidence.

## Execution assumptions

**Source-stated (§5 + Table 8 caption — read in the Methods-level section, not inferred from the abstract):**

1. **Two break-even cost schemes only.**
   - **(i)** the transaction cost that would **zero out the average abnormal return (alpha)** of the zero-cost portfolios;
   - **(ii)** the transaction cost that makes the portfolio's **certainty-equivalent return equal that of the zero-cost market portfolio** (long CRSP value-weighted composite index, short 30-day T-bills), with **certainty equivalent = mean return − 0.5 × risk-aversion × variance, risk aversion = 2**. `na` means **the strategy does not deliver a positive certainty-equivalent return at any cost**.
2. **Table 8 caption states the tabulated figures are "the transaction costs multiplied by the portfolio average turnover (both long and short positions)"**, and the prose then compares those figures directly with **per-trade** effective spreads (Korajczyk–Sadka 2004: 0.16–141 bps, mean 5.59 bps; momentum top/bottom decile 5.01 vs 14.97 bps and 5.49 vs 14.50 bps; Novy-Marx–Velikov 2016 momentum & PEAD monthly costs 1963–2013: **10–40 bps**). Whether the tabulated statistic and the benchmarks are on the **same per-trade vs total-drag basis is not stated** → **`underspecified`**, and the paper's conclusion "payoffs largely exceed reasonable transaction costs" inherits that ambiguity.
3. **Actual strategy turnover is never printed anywhere in the paper** (only firm-level `TURN` means in Table 1/9 are shown) → turnover, and therefore capacity, is a **`data gap`**, not zero.
4. **Nothing else is modelled:** commissions, spread schedule, slippage, market impact, participation rate, borrow/stock-loan fee and availability on the short leg, margin/financing, latency, fill/partial-fill, liquidation, and turnover are all **`data gap`** and must never be recorded as 0.

**Break-even results actually printed (Table 8, sample June 1977–October 2015, bps, holding period 1/3/6/12/18/24 months):**

| Strategy | (i) alpha-zeroing | (ii) certainty-equivalent |
|---|---|---|
| MAD signal (long >1, short ≤1) | 161 / 236 / 452 / 698 / 686 / 736 | **na / na / na / na / na / na** |
| MAD decile (top−bottom) | 184 / 277 / 510 / 667 / 542 / 524 | 27 / 68 / 129 / 10 / na / na |
| MAD threshold 0.10 | 234 / 350 / 654 / 995 / 1036 / 1084 | 78 / 136 / 246 / 222 / na / na |
| MAD threshold 0.20 | 289 / 445 / 796 / 1169 / 1133 / 1153 | 118 / 212 / 376 / 409 / 28 / na |
| MAD threshold 0.30 | 335 / 516 / 915 / 1245 / 1121 / 1036 | 114 / 233 / 443 / 437 / na / na |
| PDI decile | 199 / 218 / 249 / 341 / 379 / 506 | 128 / 114 / 441 / na / na / na |

**Not specified by source → `research-proposed` (never presented as source-reported):** any concrete fee ladder, next-open execution, bid-ask model, participation cap, borrow fee, or the decision to trade long-only vs long-short.

## Evidence

### Source-reported

All figures below are **from the pinned 2018 PDF, gross of costs, annualized by monthly × 12 with no compounding unless stated**, each with its Table/Figure/Section provenance.

- **Table 1 Panel B (June 1977–October 2015, next-month average returns by MAD decile, %):** `0.84 / 1.04 / 1.14 / 1.17 / 1.20 / 1.28 / 1.30 / 1.27 / 1.50 / 1.92`, **top−bottom = 1.09***; §3 text reports the equal-means null for extreme deciles rejected at **t = 3.62**. **Figure 1 Panel B:** for months 2–6 the top−bottom spread is **≈ 7%**.
- **Table 2 (monthly Fama-MacBeth, slopes ×10⁴, t in parentheses; controls = MOM, 52HIGH, TRND):** MAD `2.79 (5.80)` at t+1 · `11.54 (8.98)` at t+2:t+6 · `6.04 (5.05)` at t+7:t+12 · **`−0.04 (−0.02)` at t+13:t+24**. In **2001–2015**, MAD `1.98 (2.80)` while **MOM `0.12 (0.70)`**, 52HIGH `−0.68 (−1.26)`, TRND `3.25 (0.45)`. Risk-adjusted (FF3 + one of cross-sectional momentum / time-series momentum / trend): `2.41 (5.78)` / `2.33 (5.58)` / `2.08 (4.79)`. Threshold variables: 0.1 `0.23 (4.29)`, 0.2 `0.44 (6.04)`, 0.3 `0.51 (5.19)`. States: high sentiment `2.92 (5.21)`, low `2.50 (2.87)`; low volatility `3.32 (5.01)`, high `2.23 (3.28)`; high liquidity `2.63 (4.15)`, low `2.90 (4.06)`.
- **Table 3 (30/40/30 double sorts, next-month %, top−bottom MAD diff inside each control portfolio):** within **MOM** bottom/mid/top: **0.44**\*\* / **0.33**\* / **0.63**\*\*; within **52HIGH**: **0.54**\*\* / **0.73**\*\*\* / **1.36**\*\*\*; within **TRND**: **0.99**\*\*\* / **0.38**\*\* / **0.47**\*\*.
- **Table 4 (10×10 sequential MAD then MOM, months −2…−6):** next-month MAD spread is positive in **every one of the 10 MOM deciles**: `1.06** … 1.44***` (sequential sorts) and `0.79** … 1.10***` (sorted independently). Months 2–6: diffs `5.13*** – 6.86***`. Months 7–12: diffs still positive `2.93*** – 4.88***`, but **the MAD dimension within the smallest/largest MOM rows turns negative (−4.34***, −6.29***)**.
- **Table 5 Panel A (long−short, FF3 alphas, annual %, 1/3/6/12/18/24 months):** MAD signal `6.87 (4.40) / 6.69 (4.64) / 6.41 (4.90) / 4.95 (4.98) / 3.24 (3.89) / 2.61 (3.62)`; MAD decile `15.10 (4.27) / 15.13 (4.75) / 13.93 (4.78) / 9.11 (4.08) / 4.94 (2.65) / 3.58 (2.29)`; threshold 0.10 `14.20 (6.22) … 5.48 (4.96)`; threshold 0.20 `19.97 (6.46) … 6.63 (4.35)`; threshold 0.30 `25.41 (5.62) … 6.55 (3.15)`.
- **Table 5 Panel B (long leg vs T-bills, same alphas):** MAD signal `3.37 (4.26) … 1.87 (3.12)`; MAD decile `8.92 (5.20) / 7.82 (5.34) / 6.54 (5.09) / 3.48 (3.36) / 1.38 (1.45) / 1.07 (1.12)`; threshold 0.10 `5.47 (5.00) … 2.04 (2.95)`; threshold 0.20 `8.65 (6.05) … 1.59 (1.90)`; threshold 0.30 `10.52 (5.55) / 7.83 (4.41) / 6.34 (4.15) / 3.62 (3.02) / 1.38 (1.29) / 0.72 (0.70)`.
- **Table 6 (PDI, FM slopes ×10⁴):** PDI `2.24 (14.22)` t+1 · `2.21 (14.11)` t+2:t+6 · `1.98 (13.03)` t+7:t+12 · `1.89 (7.43)` t+13:t+24; sample caption **June 1977–October 2017**. Component slopes: Cash `1.57 (4.57)`, Operating Income `2.00 (1.90)`, Retained Earnings `0.88 (1.91)`, CAPEX `1.49 (2.72)`, Invested Capital `−1.59 (−6.41)`, Inventories `−4.18 (−7.12)`, Sales `1.14 (3.34)`, **IB `0.47 (0.50)` (insignificant)**. **MAD enters jointly at `2.54 (5.45)`**.
- **Table 7 (FF5 zero-cost factor-mimicking portfolios, annual %):** *equal-weighted* 1-month: PDI `15.49 (13.10)`, MAD decile `12.51 (3.46)`, 0.10 `12.15 (5.21)`, 0.20 `17.78 (5.60)`, 0.30 `22.24 (4.79)`; *value-weighted* 1-month: `9.60 (4.91) / 9.97 (2.15) / 7.43 (2.39) / 15.85 (3.83) / 22.45 (3.74)`; *value-weighted* 12-month: `4.13 (3.34) / 8.05 (2.72) / 8.45 (4.07) / 12.90 (4.56) / 16.41 (4.72)`.
- **Figure 2 (buy portfolios, $1 invested June 1977, monthly rebalancing, gross):** terminal values **$324.36** (MAD signal), **$2,066.46** (MAD decile), **$671.12 / $2,115.81 / $4,158.35** (thresholds 0.1/0.2/0.3) against **$59.98** for the CRSP value-weighted index; sell portfolios **$35.25 / $15.30 / $5.65 / $2.04 / $0.39**.
- **Table 9 Panel A (risk profile, equal-weighted):** top MAD decile — stock mean 200-day daily STD **17.03**, portfolio monthly STD **7.18**, FF5 intercept **1.24 (8.49)**, loadings market **0.98**, size **1.09**, HML **−0.42**, RMW **−0.28**, CMA **0.26**; bottom MAD decile — **16.03 / 7.86 / intercept 0.20 (1.04)**, loadings **1.23 / 0.69 / 0.35 / −0.38 / −0.55**. §5 prose summary: market and value loadings **significantly smaller** for top vs bottom, size and investment loadings **significantly larger**, profitability loadings **indistinguishable**; equal-slopes t-tests reject equal market/size/value/investment loadings at 1%.
- **Table 10 (market/industry timing, annual alpha vs market factor, %):** market row **1927-2015 column header** — MAD signal `2.88 (2.85)`, threshold 0.025 `4.54 (3.97)`, threshold 0.05 `5.67 (4.08)`; **2001–2015** `4.90 (2.52) / 5.88 (2.64) / 7.00 (2.74)`; PDI signal `3.20 (2.66)`, PDI threshold `3.45 (2.61)`; all-industry composite `3.13 (3.81) / 4.71 (5.15) / 6.27 (5.83)` (2001–2015: `5.03 (3.14) / 6.08 (3.29) / 6.78 (3.13)`).
- **§7 international:** cross-country MAD slopes "uniformly positive and mostly significant" for 1–24 months; with all global factor controls "significant for every horizon at the 5% level or less" (Table 11). Market timing with threshold 0.05 gives **positive alpha for all 38 economies, significant at 10% or better for 32**. All-inclusive strategies: **8.11%–12.28% equal-weighted (t = 4.98–6.11)** and **6.42%–9.81% value-weighted (t = 3.92–4.61)** vs the global market portfolio (bottom of Table 12).
- **§1 headline claim (not tied to a table):** "Returns from the strategy are in excess of **12% per year**" — recorded as a source-reported *introduction* claim whose exact strategy/horizon mapping is `underspecified`.
- **Journal-version abstract (verified on Wiley 2026-09-26, quoted but NOT used as a result):** "Annualized value-weighted alphas from the accompanying hedge portfolios are around 9%, and the predictability goes beyond momentum, 52-week highs, profitability, and other prominent anomalies. MAD-based investment payoffs survive reasonable trading costs faced by institutions, and are stronger on the long side relative to the short counterpart."

### Independently reproduced

**not independently reproduced.** Nothing here was re-run: no backtest, no simulation, no re-estimation was performed by Scout (research-only mandate). CRSP/Compustat/I-B-E/S are licensed, and the source ships **no code and no data**.

### Negative evidence

1. **No net-of-cost return exists anywhere in the paper.** Only break-even thresholds (Table 8). Every performance number above is **gross**.
2. **Table 8 scheme (ii): the MAD *signal* strategy is `na` at every horizon (1→24 months)** — it never produces a positive certainty-equivalent return at any cost versus the market portfolio at risk aversion 2. The source still concludes the strategies "largely exceed reasonable transaction costs".
3. **§5 + Appendix F (Sharpe test à la MacKinlay 1995):** "portfolios that employ the **MAD signal or extreme MAD-based deciles produce Sharpe ratios that are not significantly greater than that of the value-weighted CRSP index**. In contrast, the fixed thresholds and the PDI-based decile strategy yield Sharpe ratios that are significantly greater … for investment horizons of up to one year."
4. **Table 8 scheme (ii) collapses with horizon:** MAD decile falls `27 → 68 → 129 → 10 → na → na`; threshold 0.20 falls to `28` at 18 months and `na` at 24; PDI `na` from 12 months on.
5. **Table 5 Panel B:** the long leg's decile alpha is **insignificant at 18 and 24 months** (`1.38 (1.45)`, `1.07 (1.12)`); threshold 0.30 long leg is insignificant at 18 and 24 months (`1.38 (1.29)`, `0.72 (0.70)`); threshold 0.20 falls to `1.59 (1.90)` at 24 months.
6. **Table 2:** MAD's Fama-MacBeth slope is **exactly zero at 13–24 months** (`−0.04 (−0.02)`) — the effect does not just slow, it stops.
7. **Table 4:** within the smallest/largest MOM deciles, the MAD spread over months 7–12 is **negative** (`−4.34***`, `−6.29***`) — the interaction with momentum is not uniform.
8. **Table 9 Panel A:** top MAD decile has **different factor loadings** (market 0.98 vs 1.23, HML −0.42 vs 0.35, size 1.09 vs 0.69, CMA 0.26 vs −0.55) and the **bottom decile's own five-factor intercept is insignificant** (`0.20 (1.04)`). Risk differences are *reduced*, not *eliminated*.
9. **Table 7:** value-weighted alphas are materially smaller than equal-weighted at 1 month (MAD decile `9.97` VW vs `12.51` EW) and the source acknowledges the Hou-Xue-Zhang-style critique; microcap control is only the **$5 price screen**.
10. **Sharpe-ratio criterion, scheme (ii) `na`, VW shrinkage, and the long-leg decay together** mean the implementable version of the trade is far weaker than the headline long-short table.
11. **No out-of-sample protocol.** "2001–2015" and the 2001+ international section are in-sample sub-period / same-team / same-method splits — no frozen hold-out, no walk-forward, no pre-registered period.
12. **No multiple-testing correction** across 6 horizons × 2 weightings × 6 strategies × 4 model specs × 6 market states × 15 double-sorts × 12 industries × 37 countries.
13. **No permutation / bootstrap null** for the cross-sectional spread; only parametric t-values.
14. **Evidence is entirely pre-2018** (main sample ends October 2015) → nothing on the 2018–2026 anomaly-decay regime. The introduction's "2001-2016" wording vs the tables' "2001-2015" is an internal inconsistency.
15. **Universe restrictions are part of the result:** positive book equity, ≥2-year Compustat listing, $5 floor, share codes 10/11 → excludes young firms, financials-by-code, REITs/ADRs/closed-end funds, and anything under $5. Survivorship/backfill is mitigated, not eliminated.
16. **Short leg is modelled as frictionless:** no borrow availability, no stock-loan fee, no hard-to-borrow screen, no recall risk — for 1977–2015 shorting a decile of small caps.
17. **Capacity unknowable:** turnover is never printed; the break-even statistic's basis is `underspecified` (see Execution assumptions).
18. **Not publicly reproducible:** licensed data, no code, no data-availability statement.
19. **Version risk:** the record pins a **2018 working-paper PDF**; a peer-reviewed article with a *different title* exists (RFE 39(2):127–145, DOI `10.1002/rfe.1118`) and secondary sources describe a **December 2023 SSRN revision with a different sample (July 1977–December 2018) and different figures**. Those figures are **not used here** because neither document could be opened. Any number that differs between versions is `data gap`.
20. **Internal cross-reference errors in the source:** Table 8's caption says alphas are "reported in Table 4" while the alphas are in Table 5; §5 says the risk comparison is in "Panel A of Table 8" while it is Table 9 Panel A; §7 says "37 international equity markets" then "38 economies"; Table 10's column header reads "1927-2015" though the sample begins June 1977.

## Falsification plan

Every threshold below is **`research-defined`** (Scout-generated), not source-reported. Failure of any gate ⇒ keep `status: research-only`, do not promote.

- **F1 — Independent forward replication (`research-defined`).** Point-in-time monthly MAD on the frozen universe (CRSP share codes 10/11, EOM price ≥ $5, ≥200 daily bars) for **2018-01 → present**: top−bottom decile EW next-month spread must have **Newey-West (6 lags) t ≥ 1.96** and a positive sign in **≥ 60% of calendar years**. Otherwise the effect is declared **dead in the current regime**.
- **F2 — Cost ladder (`research-defined`).** Re-price every one of the five MAD strategies at **0 / 1 / 5 / 10 / 20 / 30 bps one-way**, plus a **5 bp platform/fee line**. **Fail** if net-of-cost alpha ≤ 0 at **10 bps one-way** for the decile or threshold strategies. (The source's own break-even claims are re-checked against these, since it never prints turnover.)
- **F3 — Turnover audit (`research-defined`).** Compute one-way monthly turnover for each strategy; if turnover exceeds **40% per month**, the Table 8 break-even claims are re-derived on that turnover before any further use. Source prints **no turnover** → this is mandatory, not optional.
- **F4 — Anchoring-specific test (`research-defined`).** Conditional on MOM decile **and** a 52-week-high distance control **and** a 200-day-distance-from-52W-high control, MAD must keep an FM slope with **t ≥ 1.96** on an independent sample. If MAD dies once plain "distance from long-run high" is controlled, the *anchoring* claim fails (the generic momentum claim may survive).
- **F5 — Distance vs crossover (`research-defined`).** Reproduce the source's own discrimination test: the **ratio** must beat the **binary crossover** dummy with a difference significant at **p < 0.05** in the new sample; otherwise the strategy degenerates into a classic MA-cross rule and the record's mechanism claim is downgraded.
- **F6 — Permutation null (`research-defined`).** **1,000 circular-shift permutations** of the cross-sectional MAD ranking within each month; the observed spread must exceed the **95th percentile** of the null.
- **F7 — Multiplicity (`research-defined`).** Benjamini-Hochberg **q < 0.10** across the full grid actually reported (6 horizons × EW/VW × 6 strategies), evaluated in one family.
- **F8 — Risk-factor horse race (`research-defined`).** Alphas re-estimated on **FF5 + momentum + q-factor** and against **beta/size/liquidity/ivol-matched controls**; alpha must stay **> 0 with t ≥ 1.96**, else the risk explanation wins and the record flips to "risk story".
- **F9 — Value-weighted + liquidity gate (`research-defined`).** VW returns with a **30-day ADV ≥ $1,000,000** screen (research-proposed). If only the EW version survives, the implementable claim is downgraded to "EW only, microcap-driven".
- **F10 — Long-side ablation (`research-defined`).** Report long-only vs long-short separately; if the long-only alpha at 12 months is insignificant (as Table 5 Panel B suggests it may be at 18–24), **record long-only as the only candidate implementation** and drop the short leg's cost/borrow risk from consideration rather than assuming it away.
- **F11 — Regime stability (`research-defined`).** Split 2018–2026 into **four sub-periods**; require **≥ 3 of 4** positive with sign consistent, else "regime-dependent, not adoptable".
- **F12 — Transport test to crypto (`research-defined`).** Port MRAT to the top-50 liquid perpetuals by 30-day dollar volume, monthly, same ratio; require a cross-sectional FM slope with **t ≥ 1.96**, sign matching equities, and survival after a **10 bps one-way** cost. **Fail ⇒ crypto portability is rejected**, not merely "unproven".
- **F13 — Capacity (`research-defined`).** **$10,000,000 notional at ≤ 10% of 20-day dollar volume**; if projected impact exceeds the applicable Table 8 scheme-(ii) break-even at the chosen horizon, **fail**.

## Crypto portability

**unproven.** The pinned source contains **zero** cryptocurrency or perpetual-futures evidence: its markets are US common stocks (June 1977–October 2015), industry indices, and 37–38 international equity markets from 2001. Under the repository rule, this may **not** be labelled `direct`.

- **Mechanism that would plausibly transport (`research-proposed`):** a 200-day (or 200-bar) long anchor versus a ~21-bar short average is a generic underreaction-to-anchor story that does not require fundamentals, dividends or accounting data — appealing precisely because PDI would have no clean crypto analogue (no trailing earnings anchor).
- **Why it might fail (`research-proposed` risk list):** 24/7 sessions mean MA(200) spans ~2.9 calendar days less history per year than in equities and bar boundaries are ambiguous (UTC vs exchange-local vs funding-interval); crypto cross-sections have far higher turnover and delisting rates (survivorship/backfill discipline must be rebuilt); price scales differ by orders of magnitude across a top-50 set (rank-based sizing required); the short leg needs perp funding, borrow and liquidation modelling that the source does **not** provide; venue fragmentation and candle gaps corrupt MA(200); perpetual funding is an extra state variable with no equity counterpart.
- **Gate:** only **F12** can promote this from `unproven`; until then no crypto operationalization may be described as source-reported.

## Limitations

- `underspecified`: formation timestamp/timezone/execution price; multi-horizon cohort aggregation; the per-trade vs total-drag basis of Table 8's break-even statistic and its comparison to per-trade spreads; the exact strategy behind §1's "in excess of 12% per year"; whether the journal version supersedes this manuscript.
- `data gap`: **actual strategy turnover**, capacity, borrow/stock-loan cost, commissions, spread/slippage/impact, participation, margin/financing, fill model, liquidation, latency; the journal version's sample period, universe, cost treatment and all its numbers; SSRN's current revision content (403); code and data availability.
- `not independently reproduced`: every performance and statistical figure in this record.
- `unproven`: any crypto/other-market portability claim.
- Source-internal inconsistencies recorded verbatim rather than smoothed over: 37 vs 38 economies (§7); sample "June 1977–October 2015" vs Table 6's "October 2017" vs §1's "2001-2016" vs Table 10's "1927-2015" header; Table 8 caption pointing at "Table 4" and §5 pointing at "Table 8" for the risk panel (actually Table 5 and Table 9).
- Version risk: the pinned document is a **2018 working-paper PDF**, not the peer-reviewed article; secondary sources describe a **December 2023 SSRN revision with a longer sample (to December 2018) and different figures**, which could not be opened and is therefore excluded.
- Publication-bias and author-overlap risk: the related journal article exists but was only readable at abstract level; no referee reports were seen.

## Implementation status

**not-implemented.** No code written, no data pipeline built, no backtest run, no paper-trading, no order generation. This record is documentation of a source plus a falsification plan.

## Adoption boundary

**not-approved / approval_scope: research-only.** This record may be read, cited, and used to design a falsification test. It must not be used to allocate capital, generate orders, justify a live or paper position, or be described as validated. Nothing here is investment advice; it is a source-backed research hypothesis with explicit negative evidence. Adoption requires an independent record that has cleared the repository's verification gates — in particular F1 (forward replication), F2/F3 (costs and turnover), F9 (value-weighting), and, for any crypto use, F12.

## Related Wiki records

`kb_search` for "moving average distance momentum anchoring cross-sectional equity returns" → **0 results**. Broader query "technical analysis moving average cross-sectional momentum anomaly" → **1 result**: [[quant/model-free-statistical-arbitrage-empirical-mean-reversion-time-reinforcement-learning-2026-09-05]] — price-history-based and therefore mechanism-adjacent, but a **different source, different mechanism (mean-reversion timing / RL policy) and different universe**; linked as adjacent only. **No closely matching Wiki page exists for this source**, and no other links are asserted.

## Sources

1. **Pinned primary (all numbers in this record):** `https://anderson-review.ucla.edu/wp-content/uploads/2021/03/Avramov-Kaplanski-Subra_2018_SSRN-id3111334.pdf` — *Stock Return Predictability: New Evidence from Moving Averages of Prices and Firm Fundamentals*, Doron Avramov, Guy Kaplanski, Avanidhar Subrahmanyam; **1,844,843 bytes, SHA-256 `0aed1cbc651e334f0bafd3694310d31a2a57a41cacd9a529670346d8cb609e85`**, 77 pages, PDF date 2018-10-03, every page footer `https://ssrn.com/abstract=3111334`; retrieved and read 2026-09-26.
2. **SSRN abstract page (source identity, not readable):** `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3111334` — HTTP 403 Cloudflare challenge on 2026-09-26 (curl and browser).
3. **Peer-reviewed related article (bibliographic + abstract verified only):** `https://onlinelibrary.wiley.com/doi/10.1002/rfe.1118` — *Moving average distance as a predictor of equity returns*, *Review of Financial Economics* 39(2), April 2021, pp. 127–145, first published 18 September 2020; full text paywalled (`/doi/full` → `/doi/abs`), read 2026-09-26. No number from it is used as a result in this record.
4. **Discovery aids only (NO number in this record is taken from them):** Alpha Architect's write-up of the study; Aligrithm's secondary summary (which cites SSRN 3111334 under the later title and reports a July 1977–December 2018 sample and different alpha figures — explicitly excluded as a secondary, unverifiable version); IDEAS/RePEc listing for the RFE article.
