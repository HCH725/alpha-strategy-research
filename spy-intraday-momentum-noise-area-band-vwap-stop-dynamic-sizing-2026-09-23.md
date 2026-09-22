---
schema: strategy-research-record-v1
title: SPY intraday momentum with time-of-day Noise Area bands, VWAP trailing stop and volatility-targeted sizing (SSRN 4824172)
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-09-22
sources:
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4824172"
  - "https://doi.org/10.2139/ssrn.4824172"
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7323419"
  - "https://concretumgroup.com/coding/"
  - "https://www.tradingview.com/script/CUpWCZhe-Concretum-Bands/"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# SPY Intraday Momentum with Time-of-Day Noise Area Bands, VWAP Trailing Stop and Volatility-Targeted Sizing

## Provenance

**Primary source (pinned version, read in full this run):**
Carlo Zarattini, Andrew Aziz, Andrea Barbon, *"Beat the Market — An Effective Intraday Momentum Strategy for S&P500 ETF (SPY)"*, Swiss Finance Institute Research Paper No. 24-97, Available at SSRN: `abstract_id=4824172`, DOI `10.2139/ssrn.4824172`.

- **Complete author list exactly as source (PDF cover, footnote affiliations):** Carlo Zarattini¹ — Concretum Research, Viale Carlo Cattaneo 1, 6900 Lugano, Switzerland; Andrew Aziz (affiliations 2 and 3) — Peak Capital Trading, 744 West Hastings Street, Vancouver, BC, Canada V6C 1A5 and Bear Bull Traders, same address; Andrea Barbon⁴ — University of St.Gallen, Dufourstrasse 50, 9000 St. Gallen, Switzerland (and Swiss Finance Institute, per page header). No other authors.
- **Version/date:** PDF cover states *First Version: May 10, 2024; This Version: September 22, 2025*. SSRN abstract page (read 2026-09-23): 43 pages, Posted 14 May 2024, Last revised 22 Sep 2025, Date Written May 10, 2024. Record `source_as_of` = 2025-09-22 (pinned PDF version date).
- **Sample period / universe:** 1-minute regular-session data, **May 2007 – April 2024**, single instrument **SPY** (plus VIX for regime tests); §2 *Data*.
- **Primary-source checksum (performed 2026-09-23):** SSRN abstract page read directly, then the 43-page PDF downloaded through the same browser session (local file SHA-256 `865010dfd938d513c1cd22a7be5932bc232afe498c3cf493d6d8bd4b0de86ebb`) and read cover-to-cover: §1–§5, Tables 1–6, Table A1, Figures 1–10, References, FAQs Q1–Q25. Every quantitative field below was taken from that pinned PDF with its Table/Section anchor.
- **Publication / peer-review status:** SSRN working paper circulated in the Swiss Finance Institute research-paper series. The source states no journal reference, no non-SSRN DOI, and no editorial/peer-review acceptance → **peer-review status: `not stated in source`**; not presumed published or under review anywhere.
- **Rights:** SSRN license notice on the abstract page reads "All rights reserved. No reuse allowed without permission." This record therefore cites and normalizes the idea and short figures only; no wholesale copying.

**Secondary source used only for negative/replication evidence (read in full this run, kept strictly separate from the primary):**
José Enrique Delgado (Independent Research), *"'Beat the Market' Revisited — An Independent Replication and Statistical Audit of an Intraday Momentum Strategy"*, SSRN `abstract_id=7323419`, DOI `10.2139/ssrn.7323419`; 23 pages, Posted 21 Aug 2026, Date Written August 20, 2026, CC BY-NC 4.0; PDF read in full (local SHA-256 `84f454f8c4e41c333b622d3ac0ce04cfb611535715943d55b5691d59ca24bdd9`), data as-of 14 Aug 2026. This is an independent third party, not the original authors.

**Companion implementation assets (source-reported links, entry pages verified HTTP 200 this run):**
`https://concretumgroup.com/coding/` (hub listed in FAQ Q1, verified 200) hosts the authors' Matlab and Python reference backtests; FAQ Q1 additionally prints two `bit.ly` short links for the Matlab and Python notebooks — those short links are quoted as printed but their destinations were **not independently resolved in this run** (shortener resolution is blocked in this unattended environment) → `data gap`. The free TradingView indicator `Concretum Bands` (FAQ Q3): `https://www.tradingview.com/script/CUpWCZhe-Concretum-Bands/`, verified HTTP 200, public and traceable. Data vendor: IQFeed (§2, FAQ Q2); the raw database is not shared by the authors "due to contractual agreements" (FAQ Q2).

**Whole-repository dedup (performed before writing, 2026-09-23):** ripgrep across **all** `*.md` plus `coverage_manifest.csv` for `4824172`, `7323419`, `10.2139/ssrn.4824172`, `Beat the Market`, `Andrew Aziz`, `Noise Area`, `Concretum Bands`, `CUpWCZhe`, `IQFeed` → **zero hits** other than an unrelated Halperin title substring ("…To Beat the Market?"). `Concretum`/`Zarattini` appear only in `ensemble-donchian-trend-following-crypto-top20-rotational-2026-09-20.md` (SSRN 5209907, crypto trend, different paper) and `llm-news-enhanced-cross-sectional-momentum-tilt-2026-09-06.md` (arXiv 2510.26228, different mechanism). Material distinction from neighbours: **source identity** (DOI 10.2139/ssrn.4824172, unique), **universe/market type** (US single-ETF intraday equity vs. crypto daily rotation, LLM news tilt, or retail crypto microstructure), **signal construction** (time-of-day-varying noise band from average move-from-open + semi-hourly checkpoint grid + VWAP/band trailing stop + 2% vol-target sizing), **horizon/regime** (intraday, flat overnight, 09:30–16:00 ET session). Not a reframe of an existing record.

## Economic mechanism

### Source-reported

The authors argue that intraday trends in SPY originate from a persistent, significant imbalance between buyers and sellers during a session ("sticky demand/supply imbalances", §1, §3). They ground this in the Jegadeesh–Titman momentum effect and its candidate micro-foundations: under-reaction to news, the disposition effect (Frazzini), limited attention (Della Vigna–Pollet), and slow-moving capital (Duffie). They extend Gao et al. (*Market intraday momentum*, JFE 2018) and Baltussen et al. (*Hedging demand and market intraday momentum*, JFE 2021): the academic constructions trade mostly in the last 30 minutes, whereas their model enters "as soon as there is an indication of abnormal demand/supply imbalance" anywhere in the session (§1). They further hypothesize (§4.5) that dealer gamma/delta-hedging flows amplify or suppress intraday continuation — high recent RSI ⇒ dealers more likely long-gamma ⇒ intraday trends get sold into ⇒ lower strategy returns.

### Research interpretation

Falsifiable hypothesis: a **time-of-day-normalized breakout** (price leaving a band whose width equals the average absolute move-from-open for that clock time over the prior 14 days) isolates "abnormal" intraday displacement from the well-known U-shaped intraday volatility profile; once displacement is detected, under-reaction plus hedging-flow feedback produces continuation within the session. Component roles (source-reported roles; no claim that each independently adds alpha — ablation is required):

```text
Regime / normalization:  time-of-day Noise Area band = Open/Close-anchored ± (14-day average |close/open − 1| per HH:MM), Volatility Multiplier = 1
Primary signal:          semi-hourly (HH:00 / HH:30) breach of the band → long above / short below, gap-aware anchors
Confirmation:            VWAP confirmation at entry exists in the authors' published reference code (reported by Delgado §2.2 against the authors' Python code), not in the paper text
Risk / exit:             trailing stop = max(current upper band, VWAP) for longs / min(current lower band, VWAP) for shorts; all positions flattened at 16:00
Sizing:                  daily volatility target σ_target = 2% with leverage capped at 4×, i.e. multiplier min(4, 0.02/σ_SPY,14d)
```

Two distinct channels must not be conflated: (i) the *entry* hypothesis (abnormal displacement predicts same-day continuation), and (ii) the *risk-budget* hypothesis (vol-targeting with up to 4× leverage converts that continuation into the headline return). The paper's own Table 1 shows the unlevered, opposite-band-stop base variant **underperforming** SPY buy-and-hold in total return (178% vs 227%) — see Evidence.

## Signal

All rules below are `source-reported` unless marked. Formation/tradability: signals are evaluated on 1-minute bars but **acted on only at semi-hourly checkpoints** `h ∈ {10:00, 10:30, …, 16:00}` (§3; first possible position 10:00, §4.3). Regular US equity session; the paper does **not** state a timezone explicitly → `data gap` (US Eastern session implied by 09:30/16:00 conventions, but that reading is `research interpretation`).

- **Lookback / band construction (§3):** for each prior day `t−i`, `i = [1,14]` (inclusive), and each time-of-day `HH:MM`, `move = |Close(t−i,HH:MM) / Open(t−i,9:30) − 1|`; `σ(t,HH:MM)` = simple average of those 14 moves. Boundaries: `UpperBound = max(Open(t,9:30), Close(t−1,16:00)) × (1 + σ)`, `LowerBound = min(Open(t,9:30), Close(t−1,16:00)) × (1 − σ)` — i.e. the anchors are gap-aware (overnight gap shifts the band). Width is scaled by a Volatility Multiplier (paper uses VM = 1; §4.4 defines VM, >1 more conservative). Warm-up handling for the first 14 days is not stated → `data gap`.
- **Long entry:** at a checkpoint, price above `UpperBound` (base wording). **Short entry:** price below `LowerBound`. Simultaneous/tie handling not stated → `underspecified`.
- **Entry-price convention:** the paper's slippage experiment measures slippage "relative to the Open price of minute HH:MM" (§4.6), implying fills at the checkpoint minute open; the paper never states the fill convention in §3 → this reading is `research interpretation`, entry price otherwise `underspecified`.
- **Entry confirmation (paper vs. code divergence):** Delgado §2.2 reports that the authors' published Python reference code additionally requires **VWAP confirmation at entry** (long valid only above *both* band and VWAP; short below *both*), and that a band-only textual replication generated materially more signals (Delgado §3.3). The ZAB paper text does not contain this rule → record it as source-reported **by the replication source against the authors' code**, and flag the written specification as incomplete (`data gap` in the primary text).
- **Exit:** (a) all positions closed at market Close 16:00 — flat overnight by design (§3, Figure 2 caption); (b) trailing stop at checkpoints: long stop = `max(UpperBound, VWAP)`, short stop = `min(LowerBound, VWAP)` (§3); in the base variant the stop is the opposite band, and a stop triggers a close plus an opposite-direction re-entry (§3). Stop checks also only occur on the semi-hourly grid (§3). Precedence when stop and Close coincide is not stated → `underspecified`.
- **VWAP definition:** computed on market-hours data only (§3 footnote 2, deferring to the authors' prior VWAP paper). The formula/price base (typical price) is **not given in this paper** — reported by Delgado §2.2 as typical-price VWAP in the reference code → `data gap` in the primary text.
- **Holding period:** intraday only; at most one net position; expected holding from first checkpoint breach to stop or 16:00; no overlapping positions.
- **Position sizing:** base model = 100% of prior-day equity ÷ entry price (§3). Flagship model: `Shares = AUM(t−1) × min(4, σ_target/σ_SPY,t) / Open(t,9:30)` with `σ_target = 2%` and `σ_SPY,t` = sample standard deviation of the prior **14 daily returns** (§3 formula), leverage hard-capped at **4×** ("in line with mainstream brokerage policies").
- **Parameters and their provenance:** lookback `L = 14` (paper's fixed choice; FAQ Q6 shows 5–90 sensitivity and that 90 is better, FAQ Q14 uses this to argue against ex-post tuning); VM = 1 (§4.4 shows risk-adjusted optimum ≈1.5 but keeps 1 "to maintain simplicity and statistical intuition"); `σ_target = 2%`; cap `4×`. Fixed-vs-tuned status of `2%` and `4×`: chosen by the authors, optimization history not disclosed → `underspecified`.
- **Fully specified?** No. Marked `underspecified` on: fill price convention, timezone, warm-up, dividend/adjustment convention of the gap anchor, tie handling, exit precedence, margin/borrow treatment.

## Required data

- **Instrument/universe:** SPY only (single US equity ETF); no constituent or survivorship machinery. Replication/FAQ extensions: QQQ, other liquid US ETFs/stocks (chart only), IWM (adverse, Delgado), 33 futures markets (Q13, author-reported).
- **Venue/market type:** US spot ETF, regular session; not crypto.
- **Timeframe:** 1-minute OHLCV bars, aggregated to semi-hourly checkpoints; daily bars for the 14-day vol target; VIX (CBOE) at the open for §4.1 regime tests; daily RSI(5) of SPY for the §4.5 gamma-proxy regression.
- **Fields:** open/high/low/close/volume per minute; prior-day close (gap anchor); VWAP path within the session; 30-day ADV and 30-day price volatility (I-Star cost model, FAQ Q15); monthly traded-share volume (commission tier, §4.6).
- **Point-in-time:** price-derived only; no publication lag, revisions or restatement risk → look-ahead risk is limited to same-minute execution timing (see Execution assumptions). The reference-code vs paper divergence (VWAP-at-entry, dividend adjustment, Delgado §3.3) is a specification point-in-time hazard for any re-implementer.
- **Timestamps:** exchange session timestamps; timezone not stated in source → `data gap`.
- **Missing data / dividends:** the primary paper does not state its dividend/adjustment convention for the previous-close anchor; Delgado §3.3 documents that turning the code's dividend adjustment on/off moves the result (≈1,985% vs ≈1,965%) → `data gap` (primary), resolved only by consulting the code.
- **Data availability:** IQFeed 1-minute history is commercial; authors cannot share the database (FAQ Q2); free alternatives named by the authors: Polygon (2y), Alpaca (7y).

## Execution assumptions

- **Signal-to-order:** market orders sent at/just before the checkpoint minute; the slippage study "instruct[s] an algorithm to send market orders on SPY for $100,000 just a few milliseconds before the start of minute HH:MM" (§4.6). Live automation the authors describe (FAQ Q11): IQFeed signals → IB via IB-MATLAB (source-reported; a *slightly modified* version is traded by the authors).
- **Fill model:** fill at the checkpoint-minute open implied by the §4.6 slippage definition; partial fills, queue position and order-book interaction are **not modeled** → `underspecified`.
- **Fees (§4.6):** commission **$0.0035 per share** (Interactive Brokers entry-level rate); reduced tier **$0.0020/share** when 1-month trailing volume exceeds 300,000 shares, applied on ≈**20% of days** in the backtest.
- **Slippage (§4.6):** fixed **$0.001 per share**, calibrated from a live experiment in April 2024 (Interactive Brokers, $100,000 market orders, random side, **>1,000 trades, >$50 million notional**): average slippage ≈ **$0.001**, median **$0.0005** vs the minute-Open price. Authors acknowledge this may rise with AUM.
- **Spread:** no separate bid-ask spread line item is specified; the per-share slippage is measured against the minute open and is the only cross-the-spread estimate given → characterize as *slippage-as-measured*, spread separately `not stated in source`.
- **Impact:** only in FAQ Q15 — I-Star (Kissell–Malamut) model with large-cap parameters (`a1,a2,a3 = 687, 0.70, 0.72`), Q = shares, ADV30, σ30 → **Sharpe 1.17 vs 1.33**, yearly alpha **>15% vs ≈20%** (source-reported, FAQ Q15).
- **Leverage/margin:** up to **4×**; margin financing cost, rate, and overnight balance are `not stated in source` (the book is flat overnight, which bounds but does not eliminate financing intraday).
- **Borrow/shorting:** the strategy shorts SPY intraday; borrow availability, stock-loan fee and locate constraints are `not stated in source`.
- **Latency:** 1-minute data granularity with minute-level checkpoints; no millisecond-level latency model beyond the pre-minute market-order experiment.
- **Capacity:** explicitly left open (authors suggest advanced execution techniques for larger size) → capacity `underspecified`.

## Evidence

### Source-reported

All figures from the pinned primary PDF (SSRN 4824172, This Version 22 Sep 2025), sample **May 2007–April 2024** unless noted; all are third-party claims (`source-reported`), net of the §4.6 cost model (commission $0.0035/share + slippage $0.001/share):

- **Flagship (Table 3 / Table A1, "Curr.Band + VWAP" stop, dynamic sizing):** total return **1,985%**, IRR **19.6%**, vol **14.3%**, **Sharpe 1.33**, hit ratio **43%**, MDD **25%**, alpha **19.6%**, beta **−0.07**, skew **+1.22**, worst day **−4.5%**, best day **+9.1%**.
- **Intermediate steps (Table 1, Table 2):** base model (stop at opposite band, 100% size) total **178%**, IRR **6.2%**, vol 10.9%, **Sharpe 0.61**, hit 54%, MDD 21%, alpha 7.1%, beta −0.05, skew **−1.24**, worst day **−10.3%**; adding the current-band+VWAP stop (100% size) gives total **380%**, IRR **9.7%**, vol 7.7%, **Sharpe 1.24**, MDD 12%. **SPY buy-and-hold:** total **227%**, IRR 7.2%, vol 20.2%, Sharpe **0.45**, MDD **56%** (Tables 1–3, A1). → the headline result requires *both* the VWAP stop *and* the 4×-capped vol-target sizing.
- **Trade-level (Table 4):** trades **5,494** (base) → **7,668** (VWAP stop / dynamic), avg PnL **$0.09–0.10 per share**, hit 53%/37%/37%, max loss trade −8.6% → −4.0% → **−2.9%** (dynamic), max gain **+9.1%** (dynamic).
- **Vol regimes (§4.1, Figure 8):** Sharpe ≈ **1.50** on days with VIX > 6 at the open, ≈ **3.50** when VIX > 40, declining at extreme VIX (few observations).
- **Daily patterns (§4.2, Table 5;** significance highlighted at 10%, no multiple-testing adjustment stated**):** unconditional 2,620 obs, avg **12 bps/day**, t = **5.34**, hit 43%, Sharpe 1.7; **NR4** 660 obs, **22 bps**, t = 5.14, Sharpe 3.2; NR7 367 obs, 16 bps, t = 3.07; Triangle 664 obs, 14 bps, t = 3.19; Inside/Outside days not significant (t = 0.85 / 1.05); **Trend Day** null-to-negative (215 obs, −2 bps, t = −0.24); Big Tail 85 obs (authors call it statistically unreliable).
- **Day-of-week (§4.3, Table 6):** Wed 18 bps t = 3.42, Thu 12 bps t = 2.39, Fri 13 bps t = 2.39, Tue 9 bps t = 2.00; **Monday not significant** (9 bps, t = 1.84).
- **Gamma proxy (§4.5):** OLS of strategy daily return (bps) on prior-close SPY **5-day RSI**: **β = −3.25, p = 0.001** (interpreted by the authors as dealer-gamma conditioning).
- **VM sweep (§4.4, Figure 9):** total return negatively correlated with VM; best risk-adjusted returns near **VM ≈ 1.5**; paper keeps VM = 1.
- **Parameter sensitivity (FAQ Q6, window not stated):** lookback 5→1,856%/1.31; 10→1,570%/1.23; **14→2,108%/1.35**; 20→2,060%/1.33; 25→2,189%/1.35; 30→1,941%/1.31; 60→1,842%/1.31; **90→2,757%/1.50**, MDD 13%. FAQ Q14: optimal VM 1.5 raises Sharpe "1.35 → 1.55".
- **Stress periods (FAQ Q7):** positive in all 10 worst S&P 500 quarters (e.g. Q4 2008 market −22% → strategy **+16%**; Q1 2020 −19% → +7%; Q4 2018 −14% → +31%).
- **Cost sensitivity:** Figure 10 total return vs commission levels (chart); FAQ Q15 I-Star → Sharpe **1.17**.
- **VWAP-only stop ablation (FAQ Q22, window May 2007–Dec 2024):** Sharpe **1.17** vs **1.35** for band+VWAP, trades 6,728 vs 7,964 → the two-sided stop matters.
- **Cross-asset (FAQ Q12, Q13):** chart claim that a diversified multi-ETF/stock portfolio over 2018–Aug 2024 would exceed Sharpe **2** (chart only, no table); 33 futures markets Jan 2007–Sep 2024: only **2 negative**, average Sharpe **0.60**, diversified portfolio Sharpe **1.65** (instrument identities are masked/not recoverable from the PDF text layer in our extraction → `data gap`).
- **Post-publication (FAQ Q24, monthly table):** 2024 full year **+32.2%**; 2025 Jan–Aug **+1.0%**. (FAQ Q4 table covers only Jan–Apr 2024 = 12.9%, consistent with the pinned sample window.)
- **Publication/decay stance (FAQ Q16):** authors assert minimal decay risk due to liquidity, trend-following nature, and institutional inability to trade intraday — a source-reported opinion, not evidence.

### Independently reproduced

not independently reproduced

(no implementation in our stack; research-only document verification performed this run). An independent third-party replication exists and is reported here strictly as that source's claims (Delgado, SSRN 7323419, Aug 2026, TradeStation 1-minute data, Jan 2000–Aug 2026, ~2.6M bars):
- **Table 2 (paper window replication):** total **1,989.0%**, annualized **19.6%**, vol 14.4%, **Sharpe 1.317**, hit 43.6%, MDD −24.5%, trades 7,742 — vs the paper's 1,985% / 19.6% / 14.3% / 1.33 / 43% / −25% / 7,668 — but only after adopting the code's **typical-price VWAP** and **VWAP confirmation at entry** (§3.3).
- **Table 3 (post-publication reconciliation):** 2024 **31.8%** vs authors' 32.2%; 2025 Jan–Aug **1.4%** vs authors' 1.0%; all 20 months Jan 2024–Aug 2025 within 0.65 pp of the authors' Q24 values (mean abs. diff ≈0.25 pp).
- **Cross-asset:** QQQ base specification ≈ **3,572%** total, Sharpe **0.987** over full history (§5.3) — generalization reported as *heterogeneous*, not universal.

### Negative evidence

- **Recent regime is weak (Delgado Table 4):** 2 Sep 2025 – 14 Aug 2026 → **−8.1%**, **Sharpe −0.461**, vol 16.4%, MDD −17.4%. Pooled May 2024–14 Aug 2026 → +9.7%, **Sharpe 0.35**, MDD −21.0%. The first post-publication stretch was strong (1 May 2024–29 Aug 2025: +19.3%, Sharpe 1.057; exact-convention 13 May 2024–29 Aug 2025: +23.3%, Sharpe 1.284), so the evidence shows **regime dependence plus a materially weak latest ~12 months**, not clean immediate decay.
- **Non-stationary Sharpe (Delgado Table 5, Figure 3):** pre-paper Jan 2000–Apr 2007 Sharpe **0.53**, paper window ≈**1.31**, pooled post-paper 0.35, full-sample 0.996; rolling 252-session Sharpe declines sharply after Aug 2025 → "1.33" is not a stationary unconditional estimate.
- **Multiple-testing / overfitting (Delgado §5.2, Table 6, Research-status note):** CSCV **PBO 38.49%** (historical convention) and **40.87%** (common-valid); 129-trial ledger reconstructed, **80 SPY search alternatives**; Deflated Sharpe Ratio **99.999986796%** for the final frozen candidate — but the paper's own classification is "**retrospectively significant but not prospectively validated**" (p. 1) because the extension search was adaptive over data observed during development.
- **Cross-asset adverse evidence (Delgado §5.3, Figure 5):** unmodified base engine on **IWM** Sharpe **0.450** (logged ADVERSE_EVIDENCE, not re-optimized); SPY-tuned layers do **not** improve QQQ (Config J 0.809, rel-vol sizing 0.913, performance overlay 0.967, all below QQQ base 0.987).
- **Specification fragility (Delgado §3.3):** a text-only replication was "materially weaker" until two code-only details (typical-price VWAP, VWAP-at-entry confirmation) were adopted; the residual paper-vs-code convention (dividend adjustment: ≈1,985% vs ≈1,965.4%) is documented, not reconciled → the written paper alone is not fully reproducible.
- **Authors' own base variant is weak:** Table 1 base model trails buy-and-hold in total return (178% vs 227%), Sharpe 0.61, skew −1.24, worst day −10.33%; the 20 Jan 2022 case study loses 2.19% in a late-day reversal (§3, Figure 4).
- **Null/negative conditioning results in-source:** Trend-Day filter t = −0.24 (§4.2); Monday not significant (§4.3); short-trade PnL unrelated to same-day VIX (FAQ Q19, p = 0.91); VIX-threshold gating of shorts does not help (FAQ Q20); gating shorts to below-SMA bear markets sacrifices profitability (FAQ Q21).
- **Cost erosion:** I-Star market impact cuts Sharpe 1.33 → **1.17** and alpha ≈20% → >15% (FAQ Q15); tighter stops raise trade count 5,494 → 7,668, so results are cost-tick sensitive (§3).
- **Prior literature decay (cited inside the primary, §1):** Rosa (2022) documents declining intraday-momentum predictability after 2013 and strong regime dependence — source-reported as contrary prior work.
- **Internal numeric inconsistencies in the primary (flagged, not repaired):** (i) FAQ Q6/Q14 base Sharpe **1.35** and lookback-14 total **2,108%** vs main Table 3 **1.33 / 1,985%**, with **no window stated for Q6** → `data gap`; (ii) trade count **7,668** (Table 4, through Apr 2024) vs **7,964** (FAQ Q22, explicitly May 2007–Dec 2024) → window differs and is stated, but reinforces that FAQ tables sit on different samples.

## Falsification plan

Every operational rule and cutoff below is **`research-proposed`** (trading/implementation choices) or **`research-defined`** (acceptance/failure thresholds); none are claimed as source-reported unless the anchor is cited.

1. **Frozen prospective test (primary test).** *Data:* SPY 1-minute bars, checkpoints 10:00–16:00 ET, from the freeze date forward ≥ 12 months. *Rule:* freeze L = 14, VM = 1, `σ_target` = 2%, cap 4×, band+VWAP stop, VWAP-at-entry confirmation, costs $0.0035 + $0.001 per share (`research-proposed`, mirroring §4.6). *Metric:* annualized Sharpe and cumulative net return. *Threshold* (`research-defined`): net Sharpe ≤ 0 over the ≥12-month window → prospective failure, record marked failed for adoption regardless of historical stats (Delgado's own criterion: "the passage of time with frozen parameters"). *Action:* report and stop any adoption discussion.
2. **Independent-vendor replication.** *Data:* an independent 1-minute feed (e.g. Polygon/Alpaca/Databento), May 2007–April 2024, paper window. *Metric:* Sharpe, total return, trade count vs 1.317/1,989%/7,742 (Delgado Table 2). *Threshold* (`research-defined`): replication Sharpe < 1.00 **or** >20% of calendar months disagree in sign with the authors' Q24 monthly series → `data gap`/vendor-dependency failure. *Action:* downgrade `confidence` to low and re-label the headline as vendor-specific.
3. **Paper-text vs code ablation.** *Data:* same window/engine, four cells: {band-only, band+VWAP confirmation} × {close-only, typical-price VWAP}. *Metric:* Sharpe delta. *Threshold* (`research-defined`): |ΔSharpe| > 0.20 between textual and coded spec → the written primary source is materially underspecified; record must cite the code commit as the operative spec. *Action:* pin code version, mark Signal as code-defined.
4. **Parameter-plateau test.** *Data:* 5×5 grid lookback {7,14,21,30,60} × VM {0.7,1.0,1.3,1.6,2.0} (Delgado §5.1 grid) evaluated on disjoint subperiods. *Metric:* rank of the paper default (14, 1.0) within each subperiod. *Threshold* (`research-defined`): default in the bottom half of grid Sharpes in ≥2 of 4 equal subperiods → parameter non-robustness. *Action:* treat the mechanism, not the parameters, as the claim; no retuning without a logged ledger.
5. **Cost/impact stress.** *Data:* full paper window. *Variants:* commission {0.002, 0.0035, 0.007} $/share; per-share slippage {0.001, 0.002}; I-Star large-cap (FAQ Q15); plus a spread term of {0, 1, 2} bp per side (`research-proposed`). *Threshold* (`research-defined`): Sharpe < 1.00 under I-Star **and** any single realistic cost bump → economic fragility. *Action:* mark cost-sensitive, do not advance.
6. **Regime/decay monitoring.** *Data:* rolling 252-session Sharpe from Delgado's frozen replication, updated monthly. *Metric:* cumulative net return and rolling Sharpe after 14 Aug 2026. *Threshold* (`research-defined`): trailing 12-month net Sharpe < 0 **and** cumulative post-publication net return < 0 through ≥24 months after the 22 Sep 2025 version → decay/absence evidence sufficient to reject the prospective claim. *Action:* record rejection with the window quoted.
7. **Cross-venue/instrument placebo.** *Data:* identical, unretuned rules on IWM, DIA, QQQ over matched windows. *Threshold* (`research-defined`): ≥2 of 3 with full-window Sharpe < 0.50 (IWM already 0.450 per Delgado §5.3) → mechanism is not general, restrict any claim to large-cap index ETFs. *Action:* label SPY/limit-universe specific.
8. **Timing placebo.** *Data:* shift every checkpoint by ±30 minutes, and compare band-breach-every-minute vs the semi-hourly grid. *Metric:* Sharpe difference. *Threshold* (`research-defined`): placebo within 0.10 Sharpe of the published grid → the semi-hourly structure is not the carrier of the effect (or, if breach-every-minute dominates, checkpoint restriction is a cost artifact). *Action:* simplify or reject the timing claim.
9. **Mechanism ablation vs generic breakout.** *Data:* full window. *Comparators:* static opening-range breakout (Crabel/ORB family) and the academic last-30-minute intraday-momentum construction (Gao et al.). *Threshold* (`research-defined`): the time-varying band must beat both by ≥0.15 Sharpe net to support the "time-of-day normalization" mechanism specifically; otherwise the record's mechanism statement is weakened to generic breakout. *Action:* rewrite Economic mechanism accordingly.
10. **Multiple-testing discipline.** *Rule:* every tried variant logged (replicate Delgado's 129-trial/80-alternative ledger practice). *Threshold* (`research-defined`): any tuned variant with Deflated Sharpe Ratio < 95% at the logged trial count → rejected regardless of raw Sharpe. *Action:* only ledger-accounted results may be quoted.

## Crypto portability

**unproven.** The primary source contains **zero crypto evidence**: single US equity ETF, 09:30–16:00 ET session, May 2007–April 2024, VIX-based regime analysis, per-share commission/slippage calibrated on IBKR SPY. Porting risks (all `research interpretation`):

- **Session structure:** the Noise Area is anchored to a single daily Open and a previous Close gap, checkpoints are keyed to {10:00…16:00}, and every position is flattened at 16:00. Crypto trades 24/7 with no session open/close, so the gap anchor, the "average move from open by clock time" normalization, and the flat-at-close rule all need a redesigned time base (e.g. per-venue candle boundaries) — a different signal construction, not a parameter change.
- **Market type / costs:** US ETF per-share costs ($0.0035 + $0.001/share) do not translate; crypto spot/perp costs are bps-based taker/maker plus **funding** on perps, none of which the source models.
- **Shorting/leverage:** shorting SPY needs no funding flow; a crypto short perp incurs funding, and the 4× cap is a brokerage constraint, not a venue invariant; liquidation mechanics are absent from the source.
- **Data/timezone:** IQFeed 1-minute US equities → exchange klines with different aggregations, weekend/holiday gaps, and venue fragmentation; VWAP defined over the "regular session" has no crypto equivalent.
- **Cross-asset warning from the replication:** even within equities, generalization was heterogeneous (QQQ ≈0.987, IWM 0.450, Delgado §5.3) — there is no basis to expect direct transfer to a different asset class.
- The only crypto-adjacent mention in the source is FAQ Q12's chart including **BITO** (a US-listed Bitcoin futures ETF), which is still US-market session structure and is chart-only (`data gap`).

**Do not cite this record as crypto evidence.** Any crypto version must be labeled a ported hypothesis with its own validation.

## Limitations

- `not independently reproduced` (by us); we performed document-level primary-source verification only.
- `underspecified`: fill price convention, timezone, warm-up handling, dividend/adjustment convention for the gap anchor, tie/exit precedence, sizing-parameter (`2%`, `4×`) optimization history, borrow and financing treatment, capacity/partial fills.
- `data gap`: FAQ Q6/Q14 window unstated (its 1.35/2,108% cannot be reconciled with Table 3's 1.33/1,985% from the text); Q13 futures instrument identities not recoverable from our PDF text extraction; `bit.ly` code-link destinations not resolved in this run; raw IQFeed database unavailable under vendor contract (FAQ Q2).
- Paper text omits rules that exist in the authors' reference code (typical-price VWAP, VWAP-at-entry confirmation) — re-implementing from the PDF alone reproduces a materially different strategy (Delgado §3.3).
- Single author-team backtest, single flagship instrument, practitioner-authored (authors commercialize research tooling and trade a "slightly modified version", FAQ Q11) → conflict-of-interest/selection risk; SSRN license "No reuse allowed without permission".
- Statistical hygiene: §4.2/§4.3 run many pattern/day-of-week tests with 10% highlighting and no stated multiple-testing correction (`research interpretation` of the source's own method); headline depends on leverage-targeted sizing rather than raw directional edge (base Sharpe 0.61, alpha 7.1% vs SPY total-return underperformance, Table 1).
- Independent replication exists but is itself a single retrospective study, adaptive at its extension stage, explicitly **not prospectively validated** (Delgado p. 1); PBO ≈39–41%.
- Sample ends April 2024 for all main tables; FAQ extends monthly to Aug 2025; the replication's latest 12 months are negative — the most decision-relevant regime is the least documented by the original authors.
- `unproven` beyond US large-cap index ETFs; crypto portability `unproven`.

## Implementation status

`not-implemented`. Nothing in this record has been implemented in our research stack: no code, no backtest, no Qlib run, no production card, no Paper/Testnet/Live activity. All quoted performance is third-party (`source-reported`) and none of it has been independently reproduced by us. The linked Matlab/Python/TradingView assets belong to the source authors and have only been link-verified (HTTP 200), not executed.

## Adoption boundary

Presence of this record in this repository means only normalized research material in a public staging pool. It does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; or approved for implementation, paper trading, testnet, or live trading. `status: research-only`, `implementation_status: not-implemented`, `adoption: not-approved`, `approval_scope: research-only`.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` — the canonical schema specification (read this run). **Hermes Wiki Brain was not written this run**; no other Wiki links are asserted, and none were fabricated.

Neighboring repository records (file names only, different source identities and mechanisms):
- `ensemble-donchian-trend-following-crypto-top20-rotational-2026-09-20.md` — same first author (Zarattini) but SSRN 5209907, daily crypto Donchian rotation; distinct universe and horizon.
- `llm-news-enhanced-cross-sectional-momentum-tilt-2026-09-06.md` — overlapping authors (Barbon/Zarattini), LLM news tilt on cross-sectional equities; distinct signal construction.
- `bitcoin-intraday-time-series-momentum-volume-session-2026-08-31.md` — academic last-30-minute intraday time-series momentum in Bitcoin; contrast case for the crypto-portability section.
- `tradingview-hvp-triggered-opening-range-breakout-reversal-2026-09-16.md` — ORB-family breakout from a different public source.
- `intraday-overreaction-momentum-finbert-emotion-classifier-2026-09-05.md` — news-conditioned intraday momentum; different data dependency.

## Sources

1. Carlo Zarattini, Andrew Aziz, Andrea Barbon. "Beat the Market — An Effective Intraday Momentum Strategy for S&P500 ETF (SPY)." Swiss Finance Institute Research Paper No. 24-97. SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4824172 ; DOI: https://doi.org/10.2139/ssrn.4824172 . First Version May 10, 2024; This Version September 22, 2025; posted 14 May 2024, last revised 22 Sep 2025; 43 pages. (Primary source; all Table 1–6 / Table A1 / Figure 8–10 / §4.6 / FAQ Q1–Q25 anchors in this record refer to this pinned PDF.)
2. José Enrique Delgado. "'Beat the Market' Revisited — An Independent Replication and Statistical Audit of an Intraday Momentum Strategy." Independent Research. SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7323419 ; DOI: https://doi.org/10.2139/ssrn.7323419 . Date Written August 20, 2026; posted 21 Aug 2026; 23 pages; data through 14 Aug 2026. (Used only for replication/negative evidence; all such figures are attributed to this source.)
3. Authors' code hub (entry page verified HTTP 200 on 2026-09-23): https://concretumgroup.com/coding/ (hosts the Matlab/Python reference backtests; FAQ Q1 also prints two bit.ly short links, destinations not resolved in this run).
4. TradingView public indicator "Concretum Bands" (verified HTTP 200 on 2026-09-23): https://www.tradingview.com/script/CUpWCZhe-Concretum-Bands/
5. Concretum Group paper landing page (verified HTTP 200 on 2026-09-23): https://concretumgroup.com/beat-the-market-an-effective-intraday-momentum-strategy-for-sp500-etf-spy/
