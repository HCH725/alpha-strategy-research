---
schema: strategy-research-record-v1
title: "Crypto Perpetual Futures Predictor Zoo: 170-Characteristic Sorts Spanned by a Log-Basis + Price-Volume Two-Factor Model"
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - cross-sectional
  - basis
  - price-volume
  - factor-spanning
  - binance
status: research-only
confidence: medium
source_as_of: 2023-07-01
sources:
  - "Yi Cao, Pengfei Luo, Yuhan Cheng, Yizhe Dong, 'Anatomy of Cryptocurrency Perpetual Futures Returns', SSRN abstract_id=6795783 (v2, posted 2026-05-19), DOI 10.2139/ssrn.6795783; v1 abstract_id=6365329 (posted 2026-03-07). SSRN-delivered PDF is abstract-only (1 page), SHA-256 3977282ac4fae399b69598ea4df26125c2c098c61c042ff90c50f51adee62ca0, 194,385 bytes, retrieved 2026-09-23"
  - "Pengfei Luo, 'Three Essays on Futures Expected Returns: From Dated Futures to Perpetual Futures', PhD thesis, University of Edinburgh, 2024 — Chapter 3 is the full-text version of the same study; https://era.ed.ac.uk/items/ed3909ca-1fc6-4e44-9c49-89c9ed77f5b9 (bitstream 1da6437c-a50f-4d48-add9-fdf5158c1e8b), PDF SHA-256 759a036f1f0c921d335e2e2567b2d8e5ce3088c5e16d4ed5bf98875983d74521, 3,855,020 bytes, 249 pp., retrieved 2026-09-23"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Perpetual Futures Predictor Zoo: 170-Characteristic Sorts Spanned by a Log-Basis + Price-Volume Two-Factor Model

## Provenance

- **Primary source (identity):** Yi Cao (Xi'an Jiaotong-Liverpool University), Pengfei Luo (University of Edinburgh), Yuhan Cheng (School of Management, Shandong University; China Mobile Research Institute), Yizhe Dong (University of Edinburgh Business School), *"Anatomy of Cryptocurrency Perpetual Futures Returns."* SSRN v2 `abstract_id=6795783`, DOI `10.2139/ssrn.6795783`, posted 2026-05-19; v1 `abstract_id=6365329`, posted 2026-03-07. Landing pages reviewed 2026-09-23. **Status: preprint, explicitly "not peer reviewed"; PDF cover states "Preprint submitted to Journal of Banking and Finance May 19, 2026" — no journal publication.** SSRN license: *"No reuse allowed without permission"* — this record only normalizes and briefly quotes claims, it does not reproduce the work.
- **Primary-source checksum (SSRN PDF, retrieved 2026-09-23 through the Cloudflare-passed browser session):** `Delivery.cfm/9b8df809-…-MECA.pdf?abstractid=6795783` → **194,385 bytes, SHA-256 `3977282ac4fae399b69598ea4df26125c2c098c61c042ff90c50f51adee62ca0`, 1 page.** The delivered PDF contains **only the abstract page** (authors, JEL C63/F47, keywords, acknowledgements, Declaration of Interest). **Methods, sample period, tables and statistics are NOT in the SSRN delivery → for the pinned SSRN version those fields are `data gap`.**
- **Full-text primary source used for methods/numbers (co-author's doctoral thesis, same study):** Pengfei Luo, *"Three Essays on Futures Expected Returns: From Dated Futures to Perpetual Futures,"* PhD thesis, University of Edinburgh, 2024 — **Chapter 3** carries the identical design and claims as the SSRN abstract (cost-of-carry model, 170 predictors, 63 significant, log-basis + price-volume two-factor spanning). Public record: https://era.ed.ac.uk/items/ed3909ca-1fc6-4e44-9c49-89c9ed77f5b9, bitstream `1da6437c-a50f-4d48-add9-fdf5158c1e8b`, **PDF 3,855,020 bytes, SHA-256 `759a036f1f0c921d335e2e2567b2d8e5ce3088c5e16d4ed5bf98875983d74521`, 249 pp.**, read in full for Chapter 3 (§3.1–§3.5, Tables 18–35, Figures 3–8) and Chapter 5 limitations on 2026-09-23. Every methods/performance number below is cited to a Chapter 3 section or table; **version drift between the 2024 thesis chapter and the 2026 SSRN revision is unverified → `data gap`** (one observable difference: the SSRN abstract names the fifth category *"volatility"* while the thesis names it *"uncertainty"*).
- **Sample period (thesis Ch.3):** 2020-01-01 → 2023-07-01 (stated §3.2.2/§3.3 "Jan 2020 to the Jul 2023", Ch.5 limitation "2020-1-1 to 2023-7-1"). **`source_as_of: 2023-07-01` pins the data end.**
- **Universe (thesis §3.3):** all USDT-margined perpetual futures contracts **listed on Binance** for ≥1 day with **daily price volume > $1M**; 190 contracts cumulatively over 2019–2023 (new listings 3/76/47/23/41 per year, Table 18 Panel A); **hourly** perpetual futures data; funding fee settled **every 8 hours** (all Binance contracts in-sample).
- **Transaction-cost treatment:** the Chapter 3 methods (§3.3 data, §3.4 sorts, §3.5 factor regressions) were read in full text and **contain no fee, spread, slippage, market-impact, borrow or leverage modeling for the reported holding / long-short returns** (full-text search of Ch.3: zero hits for "transaction cost / trading cost / slippage / bid-ask / commission"; the only "zero trading costs" phrase is in the literature review describing prior theory, not the authors' method). Funding fee **yield** enters as a cash-yield component of the holding return, not as a cost. This is a **direct observation of the thesis chapter, labeled as Scout observation, not author wording**; for the pinned SSRN 2026 version (abstract-only delivery) cost treatment = `data gap / not stated in source`.
- **Repository-wide source-identity dedup (2026-09-23, ripgrep over ALL `*.md`):** `6365329`, `6795783`, `10.2139/ssrn.6795783`, `10.2139/ssrn.6365329`, exact title *"Anatomy of Cryptocurrency Perpetual Futures Returns"*, `Yi Cao`/`Pengfei Luo`/`Yuhan Cheng`/`Yizhe Dong`, `170 return predictors`, `predictor zoo`, `two-factor spanning`, `FBAS`, `FPRV`, `category momentum`, `Three essays on futures expected returns`, `era.ed.ac.uk` → **zero hits; this source identity is not in the repository.** Mechanism neighbors checked and confirmed distinct (each a different source + different signal): `crypto-futures-cross-sectional-basis-high-low-1d-2026-08-31.md` (Chi et al. 10.1002/fut.22425, **dated** OKX futures, daily, basis only), `crypto-futures-cross-sectional-basis-momentum-slope-2026-08-31.md` (Boons–Prado framework), `crypto-perpetual-funding-rate-carry-spot-perp-2026-08-31.md` (Christin et al., delta-neutral carry), `crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11.md` (Vine, net-of-costs funding carry), `crypto-perpetual-no-arbitrage-deviation-2026-08-31.md` (He et al. arXiv 2212.06888, no-arb bounds), `crypto-funding-carry-plus-cross-sectional-dispersion-binance-perp-2026-09-17.md` (funding dispersion arb), `crypto-adjacent-futures-weekly-basis-return-reversal-2026-09-03.md` (SSRN 5250499, adjacent-maturity reversal). Materially distinct in at least **source identity, mechanism claim (170-characteristic zoo + two-factor spanning vs single basis/carry signal), universe (Binance perpetual holding return vs dated futures / delta-neutral book) and horizon (8h funding-period rebalance)**.

## Economic mechanism

### Source-reported

The authors build a **cost-of-carry model tailored to digital assets** in which the perpetual price–spot link implies a **positive convenience yield** and **negligible off-chain storage costs** (thesis §3.2.2; estimated unsigned convenience-yield means 0.0001 (XRP) to 0.5428 (BTC), storage cost means/medians between −0.01% and 0.03%, §3.2.2.3). A log-linear approximation then decomposes the expected holding return of a perpetual future into **(i) the current log basis, (ii) misperception of the forward-looking spot price, and (iii) the expected futures–spot spread over the contract's 8-hour "maturity"** (§3.2.1.3, §3.2.3; SSRN abstract). Because the funding fee mechanically tracks and closes the spot–futures gap every 8 hours, the basis is expected to be the dominant cross-sectional return driver (§3.4.1). The second claimed driver is **price-volume**: liquidity/attention channels — periodic trading attracted by the funding mechanism mean low liquidity today maps to higher subsequent returns, while *signed* price-volume imbalance maps positively (§3.4.3.2, §3.5 conclusion). The paper's central claim is that **a two-factor model — log-basis factor FBAS plus price-volume factor FPRV — explains all 63 significant strategies**, so that after spanning, **none of the 63 alphas remains statistically significant** (§3.5.1–§3.5.3; SSRN abstract: "effectively explains all 63 strategies").

### Research interpretation

Falsifiable hypothesis H1 (**basis channel**): at each 8-hour funding boundary, cross-sectional differences in the spot–perp gap forecast the next funding-period holding return, with **low/negative-basis contracts outperforming high-basis contracts**, the edge concentrated in the **term (basis-convergence) component plus the funding-fee cash yield**, not in spot drift. Falsifiable hypothesis H2 (**price-volume channel**): liquidity/attention characteristics carry independent cross-sectional information — *unsigned* size-of-flow variables in a **U-shaped (non-monotone)** relation, *signed* imbalance variables in a **monotone positive** relation (§3.4.3.2, Figures 7–8). Falsifiable hypothesis H3 (**spanning / no independent alpha**): once FBAS and FPRV are controlled, every one of the 63 raw spreads has zero alpha — i.e. the "predictor zoo" of perpetual-futures strategies **collapses to two systematic sources** (basis convergence and price-volume liquidity), which is the opposite of the spot-market conclusion where momentum and size are core factors (Liu–Tsyvinski–Wu 2022, as contrasted by the source). Risk/friction named: funding-mechanism-motivated periodic liquidity provision; **no cost channel is modeled by the source** (see Execution assumptions).

## Signal

All items below are **source-reported from thesis Chapter 3** unless marked `research-proposed` / `underspecified`.

- **Formation timestamp:** at each **funding-fee payment time t** (8-hour boundaries; all in-sample Binance contracts use 8h funding), immediately after settlement (§3.4). Exact clock timezone convention **not stated → `data gap`**.
- **Sort construction:** quintile (5-portfolio) cross-sectional sort of all in-universe perpetuals on one characteristic at time t; **equal-weighted** within portfolio, absolute weights scaled to sum 1 (§3.4 preamble, Table 19 caption).
- **Characteristics (170 total):** thesis intro taxonomy — **basis 10, momentum 10, liquidity 48, size 10, uncertainty 92**; Table 35 row taxonomy — Basis(Log-Basis/Basis/BM) 10, Momentum 10, Volume 8, Scaled Volume 8, Volume Imbalance 8, Price Volume (PV & Var PV & PV-Imbalance & Var PV-Imbalance) 32, Size 10, DAMIHUD 8, Beta 28, Max Return 8, Variance Return 8, IDIOVOL 16, DELAY MKT 16 (sum 170). **Mapping between the two taxonomies is not explicitly given → `underspecified`.** Return-based variables use lookbacks **L ∈ {1, 7, 14, 21, 28, 56, 112, 350, 700} days**, each day = three 8h rolling contracts (§3.4.2, Table 23 note); basis variables are measured at t (Table 19 caption).
- **Holding / exit:** the **Holding strategy** buys the contract at t and holds to the next funding payment **t+N (N = 8h), the "maturity"**, receiving the realized opposite-side funding fee as cash yield; portfolio rebalancing **every eight hours** (§3.4, §3.4.3.1). Return identity: **Holding = Spot + Term + Funding** (Tables 19–21 decomposition).
- **Direction:** basis sorts → **"1-5" = Low-minus-High** (long lowest-basis quintile, short highest) (§3.4.1); basis-momentum sorts → **"1-5" = High-minus-Low** (§3.4.2); momentum sorts → 5th minus 1st quintile (§3.4.3.1).
- **Reported metric:** time-series average of **weekly equal-weighted** portfolio returns of the 1-5 spread; **t-statistics use Newey–West standard errors with 4 lags** (Table 19–34 captions).
- **Sizing / leverage / stops / capacity:** **not stated in source → `data gap`** (no vol targeting, no stop, no leverage rule anywhere in Ch.3).
- **Reproducibility:** the sort rule is reconstructable at concept level; **per-characteristic formulas for all 170 variables are only partially enumerated in the read text (Table 23 lists definitions for the return-based family) → treat the remaining exact formulas as `underspecified` pending the SSRN full text.**

## Required data

- **Venue/universe:** Binance USDT-margined perpetual futures, **hourly OHLCV** (funding-period aware), 2020-01-01→2023-07-01; point-in-time listing dates and **daily traded notional > $1M filter** applied cross-sectionally (§3.3).
- **Funding:** the 8-hour funding-rate/settlement schedule per contract (enters both as rebalance clock and as the cash-yield leg).
- **Spot leg:** spot/index prices to split Holding into Spot / Term components (§3.2.1.3 decomposition) — exact spot data source **not stated → `data gap`**.
- **Size/attention fields:** market capitalization for MCAP/Max-Price size sorts and market beta vs the equal-weighted market index (Table 18 Panel B EW index; §3.4.3.4) — **data vendor not stated → `data gap`**.
- **Universe hygiene:** point-in-time delisting/discontinuation handling — Ch.3 notes discontinuations occurred (2021: several contracts discontinued, §3.3) but **explicit survivorship treatment is not stated → `data gap`** (possible survivorship in a >$1M-volume filter).
- **Timestamps:** funding boundaries are exchange-defined; **timezone/24-7 week-boundary convention not stated → `data gap`**.
- **Missing data:** stale/suspended-contract handling **not stated → `data gap`**; imputation not described.

## Execution assumptions

- **Signal-to-order:** source is an academic sort study; **no order type, fill model, latency, partial-fill or failure handling is stated → `not stated in source`.**
- **Rebalance cadence:** every 8 hours at funding settlement, equal-weighted quintiles, 1-5 long-short (§3.4.3.1) — high turnover by construction; **turnover is never reported → `data gap`.**
- **Fees / spread / slippage / impact:** **not modeled anywhere in Ch.3 methods** (direct full-text observation of the thesis chapter; for the SSRN-pinned version, abstract-only delivery → `data gap / not stated in source`). All returns above are therefore **gross of trading costs but inclusive of funding-fee yield received/paid** (funding is part of the Holding-return identity, not an assumed cost).
- **Borrow / shorting / leverage / margin:** shorting the high-basis quintile on USDT-margined perps is mechanically assumed by the long-short construction; **borrow availability, margin, leverage caps and liquidation risk are not discussed → `not stated in source`.**
- **Scout arithmetic sanity check (not source-reported):** 2.66%/week × 52 = 138.3%/yr matches the source's own annualization (§3.4.1), confirming the annualization is a simple weekly×52 gross figure.

## Evidence

### Source-reported

Every figure below is `source-reported`, not reproduced by us; provenance in parentheses.

- **Universe/market scale:** Market Index mean weekly return **1.10%** (SD 0.102), EW index **1.40%** (SD 0.133), BTCUSDT 1.00%, ETHUSDT 2.00%, BNBUSDT 2.20%, XRPUSDT 1.80%; 190 contracts cumulative; mean weekly price volume **$308.58M**, median **$37.77M** (Table 18 Panel A/B; Jan 2020–Jul 2023).
- **Headline basis sort (Table 19, §3.4.1):** log-basis **1-5 spread = +2.66%/week (t = 9.54)**; raw-basis 1-5 = **+1.98%/week (t = 8.46)**; source annualizes to **138.32% and 102.96%** respectively (§3.4.1 prose, gross, NW 4 lags). Decomposition of the log-basis spread: **Spot +0.28%/wk (t = 1.25, insignificant), Term +2.11%/wk (t = 26.22), Funding +0.26%/wk (t = 8.71)** (Table 19) — i.e. the spread is **convergence + funding, not spot drift**.
- **Basis-momentum (Table 21, §3.4.2):** (7-day, 3 contracts/day) **1-5 = +1.88%/week (Table 21 t = 8.50**; §3.4.2 prose states t = 8.14 — **internal text/table discrepancy noted**); 700-day lookback weakest at **+0.50%/week (t = 2.52)**; monotone decline in returns as lookback lengthens.
- **Momentum weakness (Table 24, §3.4.3.1):** only 1-day **−0.58% (t = −2.00)**, 1-to-7-day **+0.79% (t = 2.25)**, 7-day **+1.09% (t = 3.26)** significant; **all other horizons insignificant at 5%**; source explicitly contrasts with **1.6%/week** spot momentum in Liu–Tsyvinski–Wu (2022).
- **Price-volume (§3.4.3.2):** signed price-volume imbalance 1% significant spreads span **+0.81% (t = 3.56) to +1.39% (t = 5.92)** (7 of 8 at 1%); taker-maker imbalance unadjusted returns **0.53%–1.39%/week**; **unsigned PV and Var(PV) are U-shaped (non-monotone)** across quintiles for lookbacks 1–112 days (Figure 7); DAMIHUD 14d **+0.77% (t = 2.63)**, 56d **+0.84% (t = 2.67)**.
- **Size / uncertainty (§3.4.3.3–§3.4.3.4):** Max(Price) 28d **+0.77%/wk (t = 2.56)**; MCAP **+0.66%/wk (t = 1.96)**; 7-day beta **+0.82% (t = 2.66)** and beta² **+0.83% (t = 2.68)**; **no size variable reaches 1% significance** (Table 35: Size 10 tested, 0 at 1%).
- **Zoo tally (Table 35, §3.4.4 / §3.5.1):** **170 tested → 63 significant at 5%, 40 at 1% (24%)**; at 1%: **Basis 9/10 (90%), Price-Volume 26/32 (81%), Momentum 1/10 (10%), Size 0/10 (0%)**, DAMIHUD 2/8, Beta 2/28.
- **Two-factor spanning (§3.5.1–§3.5.3):** FBAS = log-basis long-short factor; FPRV built from the **32 price-volume long-short portfolio returns (formations 1–350 days)**, PCA'd into **FPRV1–3** (three-component version) or a **variance-weighted single FPRV**; the two-factor model **explains all 63 strategies and after adjustment "none of the alphas from the 63 strategies retains statistical significance"** (§3.5.3 summary, thesis pp.56–57).
- **Publication/verification status:** SSRN **preprint, not peer reviewed**, submitted to *Journal of Banking & Finance* (PDF cover, 2026-05-19); abstract-level claims (170 predictors / 63 significant / two-factor explains all 63) verified verbatim against the SSRN abstract PDF.
- **Not reported anywhere in the read text:** Sharpe, max drawdown, turnover, IC/ICIR, capacity, net-of-cost returns, out-of-sample split, multiple-testing correction → **all `data gap / not stated in source`.**

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **The source's own headline is a null on independent alpha:** after FBAS + FPRV spanning, **none of the 63 spreads keeps a significant alpha (§3.5.3)** — the "63 profitable strategies" reduce to two systematic sources; anything marketed as 63 distinct edges is contradicted by the paper itself.
- **Momentum and size — the core spot-market factors (Liu–Tsyvinski–Wu 2022) — largely fail here:** momentum 1/10 at 1%, size 0/10 at 1% (Table 35); source itself calls the divergence "substantially different" (§3.4.4).
- **Non-monotone sorts:** unsigned price-volume variables are **U-shaped** (Figures 7–8) → a naive 1-5 long-short on those characteristics is not a valid monotone portfolio and its spread can be sign-unstable across lookbacks.
- **Regime boundary is baked in:** sample ends **2023-07-01**; since **September 2023 Binance migrated new listings to 4-hour funding** and by the thesis writing date (Nov 2024) **~1/3 of contracts run 4h funding** — the source explicitly warns this structural shift may make previously effective factors **lose their pricing power** (Ch.5 limitation). The mechanism is defined on 8h settlements that no longer cover the whole universe.
- **Zero cost modeling** in all Ch.3 methods (direct observation): with **8-hour rebalancing of a 1-5 perpetual long-short**, round-trip fees/spread/impact plausibly compete with the Term + Funding components (**0.26%/wk funding leg is smaller than a handful of basis-point round-trips at daily turnover**; the cost-erosion claim is a Scout reading, `research-proposed`, untested).
- **Multiple testing unaddressed:** 170 characteristics screened at 5% with **no FDR/Bonferroni/deflated statistic reported** → expected false positives at 5% ≈ 8.5 under the null, and the 63-count has no selection correction (`data gap`).
- **Possible survivorship:** >$1M-volume universe filter with discontinuations noted but point-in-time delisting handling unstated (§3.3) → the cross-section may over-represent survivors (`data gap`).
- **Internal inconsistency:** basis-momentum (7*3) t-stat stated as 8.14 in §3.4.2 prose vs **8.50 in Table 21** — small but recorded.
- **Version gap:** SSRN delivery is abstract-only; 2024-thesis → 2026-SSRN revision could have changed samples/tables (`data gap`).

## Falsification plan

Thresholds not fixed by the source are labeled **`research-defined falsification threshold`**; operational choices are **`research-proposed`**.

1. **Point-in-time replication (H1):** rebuild the Binance perp panel 2020-01→2023-07 (hourly, >$1M filter, delisted contracts included), EW quintiles, 8h rebalance, NW(4). **Fail** if the log-basis 1-5 spread reproduces with the wrong sign or **t < 1.96 (`research-defined`)**.
2. **Cost ladder (H1/H2 net):** re-run all headline spreads net at 2 / 5 / 10 / 20 bps per round-trip plus funding-period crossing. **Fail** if the 2.66%/wk and +0.81…1.39%/wk spreads go **t < 1.96 net at 10 bps (`research-defined`)**, or any spread's net expectancy ≤ 0 at 20 bps → downgrade to non-tradable.
3. **Turnover audit:** report daily turnover of the 8h-rebalanced 1-5 book; **fail** if realized annual turnover makes even 5 bps/RT exceed the gross spread (`research-defined`, computed from replication, not from source).
4. **Multiple-testing re-tally (H2):** apply Benjamini–Hochberg **q ≤ 0.10 (`research-defined`)** across the 170 tests. **Fail** if fewer than **half of the 63 (`research-defined`)** survive; report survivors by family.
5. **Spanning replication (H3):** re-estimate FBAS + FPRV1–3 and re-test the 63 alphas. **Fail H3** if ≥ 1 alpha stays significant at 5% after spanning **and** the result is stable across two sub-periods (`research-defined`) → mark H3 contested; **fail the zoo interpretation** if the two factors span everything *and* the factors themselves are cost-negative (then the honest conclusion is "no tradable alpha", which falsifies H1/H2 economically).
6. **Ablation of the return identity:** decompose net performance into Spot / Term / Funding legs (as Table 19 does gross). **Fail H1's mechanism** if the Term + Funding legs are wiped by costs while the Spot leg is noise (`research-defined`).
7. **4h-funding regime test (source-flagged):** repeat on contracts that migrated to 4h funding (post-2023-09) and on 8h survivors separately. **Fail generalization** if the basis family's 1-5 t-stat drops **< 1.96 in the 4h subsample (`research-defined`)** — this is the exact risk the author states in Ch.5.
8. **Universe/survivorship ablation:** rebuild with point-in-time listing + delisting (no forward volume filter). **Fail** if the headline spread halves vs the naive universe (`research-defined`).
9. **Venue portability:** repeat on OKX/Bybit perps (different funding schedules). **Fail** if the basis spread is Binance-only (`research-defined`).
10. **Action on failure:** any failed test downgrades the affected hypothesis from `research-proposed candidate` to rejected; no parameter retuning is allowed to rescue a failed threshold (retuning voids the test — `research-defined` anti-overfit rule).

## Crypto portability

**direct.** The source is itself Binance perpetual-futures research; no porting step is required. Crypto-specific risks nonetheless apply: single-venue dependence (Binance-only, USDT-margined), 24/7 boundaries with unstated timezone convention, funding-schedule heterogeneity (8h → 4h migration since 2023-09), cross-venue fragmentation of the spot reference used for basis, liquidity/market-impact absent from the model, and short-leg feasibility on contracts that later delist. Portability ≠ authorization to trade.

## Limitations

- `data gap` — **SSRN pinned version delivers an abstract only (1 page)**; methods/tables taken from the co-author's 2024 thesis Chapter 3; 2024→2026 version drift unverified.
- `data gap` — no transaction costs, fees, spread, slippage, impact, borrow, leverage anywhere in the methods (direct observation of thesis Ch.3); Sharpe/MDD/turnover/IC/capacity/net returns **not stated in source**.
- `data gap` — point-in-time delisting/survivorship handling, spot-price and market-cap data vendors, timestamp timezone, missing-data policy not stated.
- `underspecified` — mapping between the intro 5-group taxonomy (basis/momentum/liquidity/size/uncertainty) and the Table 35 13-row taxonomy; exact formulas for all 170 characteristics.
- `unproven` — no out-of-sample split, no multiple-testing correction, no independent replication (and none performed by us).
- `not independently reproduced` — every performance number is source-reported.
- Regime ceiling: mechanism defined on 8h funding, while ~1/3 of the Binance universe moved to 4h after sample end (source's own limitation).
- Publication-bias/selection: preprint, not peer reviewed, submitted venue only; 170-screened zoo with 5% uncorrected thresholds.
- Internal inconsistency recorded: basis-momentum t-stat 8.14 (prose) vs 8.50 (Table 21).

## Implementation status

`not-implemented.` No replication, backtest, prototype or data pipeline exists in our research stack; nothing has been wired to Qlib, Paper, Testnet or Live. This record is normalized research material only.

## Adoption boundary

Presence in this repository does **not** mean: passed Research Intake Review, entered Hermes Wiki Brain, entered the production candidate pool, completed Qlib full-backtest validation, became a frozen survivor or leaderboard entry, profitable, validated alpha, or approved for implementation / paper / testnet / live trading. `status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

## Related Wiki records

- Real Wiki link (read-only this run; **no Wiki writes performed**): [[quant/strategy-research-record-spec-v1]]
- Filename neighbors below are **plain filenames, NOT Wiki links, and were not written or modified this run** — they were read only for dedup: `crypto-futures-cross-sectional-basis-high-low-1d-2026-08-31.md` (dated-futures basis), `crypto-futures-cross-sectional-basis-momentum-slope-2026-08-31.md` (basis-momentum), `crypto-perpetual-funding-rate-carry-spot-perp-2026-08-31.md` (delta-neutral carry), `crypto-funding-rate-cross-sectional-carry-factor-net-costs-2026-09-11.md` (net-of-cost funding carry), `crypto-perpetual-no-arbitrage-deviation-2026-08-31.md` (no-arbitrage bounds), `crypto-funding-carry-plus-cross-sectional-dispersion-binance-perp-2026-09-17.md` (funding dispersion), `crypto-adjacent-futures-weekly-basis-return-reversal-2026-09-03.md` (adjacent-maturity reversal).

## Sources

1. Yi Cao, Pengfei Luo, Yuhan Cheng, Yizhe Dong, *"Anatomy of Cryptocurrency Perpetual Futures Returns,"* SSRN `abstract_id=6795783` (posted 2026-05-19), DOI `10.2139/ssrn.6795783` — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6795783 ; v1 `abstract_id=6365329` (posted 2026-03-07), DOI `10.2139/ssrn.6365329` — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6365329 . SSRN-delivered PDF (abstract-only, 1 p.), 194,385 bytes, SHA-256 `3977282ac4fae399b69598ea4df26125c2c098c61c042ff90c50f51adee62ca0`, retrieved 2026-09-23. Landing + PDF read in full; license "No reuse allowed without permission" (claims normalized, no reproduction).
2. Pengfei Luo, *"Three Essays on Futures Expected Returns: From Dated Futures to Perpetual Futures,"* PhD thesis, The University of Edinburgh, 2024 — Chapter 3 (full text of the same study) and Chapter 5 (limitations); public item https://era.ed.ac.uk/items/ed3909ca-1fc6-4e44-9c49-89c9ed77f5b9 , bitstream `1da6437c-a50f-4d48-add9-fdf5158c1e8b`, PDF 3,855,020 bytes, SHA-256 `759a036f1f0c921d335e2e2567b2d8e5ce3088c5e16d4ed5bf98875983d74521`, 249 pp., read 2026-09-23. Every methods/performance figure in this record traces to Chapter 3 §3.1–§3.5 or Tables 18–35 as cited inline.
3. Dedup anchors referenced above (existing repository records, read-only): filenames listed in "Related Wiki records".
