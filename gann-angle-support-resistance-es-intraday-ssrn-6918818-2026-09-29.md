---
schema: strategy-research-record-v1
title: "Gann Angle-Derived Support and Resistance at One-Minute Frequency on E-mini S&P 500 Futures (SSRN 6918818)"
created: 2026-09-29
updated: 2026-09-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - technical-analysis
  - gann-angles
  - equity-index-futures
  - es-futures
  - intraday
  - order-clustering
  - event-study
  - ssrn
status: research-only
confidence: medium
source_as_of: 2026-06-19
sources:
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6918818"
  - "https://doi.org/10.2139/ssrn.6918818"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "C1: three unreconciled source dates (landing Date Written 2026-04-14 / PDF /CreationDate 2026-06-11 / landing Posted 2026-06-19)"
  - "C2: SSRN landing heading '0 References' against 38 numbered entries printed in the pinned PDF"
  - "C3: Section 4.2 prints a round-trip cost of 'approximately 0.26 basis points of notional value' while its own figures imply 1.18 bp"
  - "C4: Section 4.5 claims power above 0.80 for d = 0.10 at 450-600 events; normal-approximation power is 0.564-0.688 two-sided (0.683-0.789 one-sided)"
  - "C5: Section 6.1 says the near-touch signal count is 'approximately 1,273 per year' while body Table 3 prints n = 1,273 for the entire three-year OOS window"
  - "C6: Section 6.1 says positions last 'approximately 5 bars (25 minutes)' while the bars are M1 (5 bars = 5 minutes)"
  - "C7: Section 5.1 prints an OOS hit rate of 61.2% while 748/1,227 = 60.96%"
  - "C8: hypothesis-label collision - Section 1 calls fan crossings 'H4' and the hierarchy null 'H4null', while Section 3.5 makes Hypothesis 4 the fan crossings and Section 3.6 makes the hierarchy F08/F09"
  - "C9: Section 3.1 says 'the eight Gann angles' and enumerates seven (8x1, 4x1, 2x1, 1x1, 1x2, 1x4, 1x8)"
  - "C10: body Table 3 'Sign-flip permutation Sharpe' row prints 0.240 / 0.317, identical to the Cohen's d in the rows above rather than a Sharpe ratio"
  - "C11: Section 1 prices slippage 'per trade' ($12.50) while Section 4.2 prices it 'per side' ($12.50) - a factor-of-two cost ambiguity"
  - "C12: body Table 4 F03 (trending) subperiod row prints Pre-COVID d = -0.068 significant although the entire IS trending sample is n = 636, and the printed subperiod d's cannot be reconciled with the pooled IS d = -0.181"
  - "C13: duplicate table numbering - body Table 1 / Table 2 and a second 'Table 1' / 'Table 2' printed after the reference list carry different content"
---

# Gann Angle-Derived Support and Resistance at One-Minute Frequency on E-mini S&P 500 Futures (SSRN 6918818)

## Provenance

- **Primary source (landing):** `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6918818`, DOI `10.2139/ssrn.6918818`, read in a browser session on **2026-09-29** after the Cloudflare interstitial cleared. Landing prints: title *Do Gann Angles Work? An Empirical Test of Angle-Derived Support and Resistance in High-Frequency Equity Futures*; author line **"Max Brown" / "Independent"** (PDF title block prints **"Max Brown ACMA, CGMA / Independent Researcher"**); **14 Pages**; **Date Written: April 14, 2026**; **Posted: 19 Jun 2026**; suggested citation "(April 14, 2026)"; heading **"0 References"**; heading "0 Citations"; **DOWNLOADS 251**; **ABSTRACT VIEWS 463**; keywords "Gann analysis, technical analysis, support/resistance, equity-index futures, intraday price dynamics, market microstructure"; JEL G12, G14, G17; licence **"All rights reserved. No reuse allowed without permission."** No ORCID, no printed email, no journal, no issue and no peer-review statement appear on the landing or in the PDF; the PDF title block says **"Prepared for submission to the Journal of Financial Markets"**, so publication status is **not stated in source** beyond *submitted / working paper*.
- **Pinned PDF:** retrieved 2026-09-29 through the landing's **Open PDF in Browser** delivery link (the in-session redirect target is a short-lived presigned object; **no presigned or session-bound URL is stored in this record**), **580,917 bytes**, **14 pages**, SHA-256 `20e985d162284ea98f80d2bc36ee55528d75ff41db2e372998139df76921d509`. Metadata: `/Title "Paper1_Gann_Angles.docx"`, `/Producer "Microsoft: Print To PDF"`, `/Author ""`, `/CreationDate D:20260611114833+01'00'`. Text extracted with **pypdf 6.16.2** to **57,124 characters / 763 lines with 14 page markers**, all 14 pages read in full (Sections 1-7, body Tables 1-4, two further tables printed after the reference list, the Conflict of Interest and Data Availability block, and the reference list counted entry by entry).
- **Dates are kept unreconciled (C1):** Date Written 2026-04-14, PDF CreationDate 2026-06-11, Posted 2026-06-19. Data sample ends 2025-12-31.
- **Reference list:** **38 numbered entries** printed in the PDF (counted by scanning entries carrying a publication year) against the landing's **"0 References"** heading (C2). Entries including Jegadeesh-Titman (1993), Karpoff (1987) and Blume-Easley-O'Hara (1994) appear in the list without an identifiable in-text citation in Sections 1-7.
- **Conflict of interest / data availability (source-reported):** "The author designed, coded, and intends to commercialise the technical indicators examined in this study", with replication assets claimed to be "publicly available at AlgForge (https://algforge.com)". That host returned a **connection timeout** from this environment on **2026-09-29** (both `curl -L` and a browser navigation timed out), so the replication package is **unverified / data gap**, not confirmed absent.
- **Companion paper:** Section 3.1 and Section 6.4 cite "the companion paper (Paper 2)" for a 3x3 normalisation-constant grid and an "F02 null result"; **no title, DOI, SSRN id or URL is printed anywhere in the pinned PDF** -> data gap.
- **Pre-registration:** the abstract states "All hypotheses are pre-registered against an in-sample period"; **no registry, timestamp, URL or identifier is printed anywhere in the pinned PDF** -> data gap.
- **Repo-wide source-identity dedup (pre-write, hidden-inclusive):** `rg -uuu` over the entire checkout (including `.git`, `.mimo-worktrees`, `.agents`, `.hermes` and `coverage_manifest.csv`, 1,088,787 bytes) for `6918818`, `10.2139/ssrn.6918818` (via `6918818`), `Do Gann Angles`, `Angle-Derived Support`, `Max Brown`, `algforge` (case-insensitive), `near-touch arrow`, `fan crossing`, `support and resistance` returned **zero files**. Generic-adjacent tokens reported honestly: `Gann` matches 6 rows inside `coverage_manifest.csv`, all **Chinese-language strategy titles from a different corpus flagged `needs_semantic_review`** (e.g. `基于甘氏角度的动态趋势跟踪交易策略`, `Gann-HiLo-Activator-Strategy`, `Gann-High-Low`) with no SSRN id, no author and no title overlap with this source, plus 2 substring hits of `Gannon` in a Polymarket prediction-market record; case-insensitive `gann` in `*.md` otherwise hits only `Hansen-Jagannathan` / `Jagannathan` / `Gannon`; `near-touch` hits only `subordinated-market-observables-clock-separation-impact-2026-09-17.md` (arXiv 2609.13715, square-root impact); `NinjaTrader` hits only `mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05.md`. **Positive control `novy-marx` returned 19 files in the same session.** `git log --oneline -20` was used as a convenience glance only.
- `git pull origin main` at run start: already up to date at `9b97a35`.

## Economic mechanism

### Source-reported

The source frames Gann fan lines as **coordination devices rather than geometric law**: if a large enough practitioner community places limit orders, stops and entries at the same angle-derived price levels, the aggregated order flow creates detectable price reactions regardless of whether the geometry has intrinsic predictive content (Section 1, Section 6.1, invoking Osler 2003/2006 round-number order clustering, the Adaptive Markets Hypothesis, and the microstructure literature on level effects). Its three surviving predictions are read as: resting orders arriving at first contact with a publicised level (anchor revisits, H1), reinforcement from entries taken on near-touches (arrow signals, H3), and breakout orders placed beyond fan lines failing and reverting (fan-crossing reversal, "Wyckoff shakeout", H4). The null hierarchy result is read as evidence that practitioners trade only the commonly taught 1x1 family rather than the whole fan spectrum (Section 5.5, Section 6.1).

### Research interpretation

- **Hypothesised mechanism:** *shared-focal-level order clustering* - a self-fulfilling intraday liquidity effect at price levels defined by (i) rolling session extremes and (ii) time-price-scaled rays from those extremes. It is a **microstructure / coordination hypothesis**, not a forecasting hypothesis about information.
- **Component roles (as the source defines them):**
  - Level generator: session anchors (rolling 100-bar highest-high / lowest-low) + fan lines at fixed slopes from those anchors, scaled by a normalisation constant.
  - Regime/context: stressed / normal / trending classification (rolling 90-session range median) conditions the H2 (F03) result only.
  - Entry signal (H3/F06): near-touch without crossing, traded **with** the line.
  - Anti-signal (H4/F07): first close on the wrong side of a fan line, traded **against** the break (returns printed significantly negative).
  - Holding/exit: fixed 5-bar horizon after costs.
- **Falsifiable statement:** conditioned on level proximity, the signed 5-minute forward return should differ from zero in the direction the source states, and the effect should attenuate once round-number, VWAP and pivot-point proximity are controlled - the source names this alternative itself (Section 6.2).
- **Alternative reading kept open:** H1's anchor construction is a rolling-high/low (Donchian-like) construct, so the effect could be generic extremum re-testing rather than anything Gann-specific (source's own alternative explanation, Section 6.2).

## Signal

All four features are machine-coded event studies on 1-minute bars; **holding horizon = 5 M1 bars** for every reported return ("5-bar net return horizon after transaction costs", end-of-PDF Table 1 caption).

**Common geometry (Section 3.1)**
- Anchor detection: for each session, the highest high and lowest low within a **rolling 100-bar lookback window**; "these anchors are held fixed for the remainder of the session".
- Fan lines projected forward from each anchor at slopes of the stated Gann angles, "scaled by a **normalisation constant of 100 points per session (390 M1 bars in regular trading hours)**". Robustness re-runs at 80 and 120 points per session (Section 6.3).
- **Underspecified:** (a) the normalisation semantics - Section 3.1 also says "the 1x1 line, rising or falling at one price unit per bar", which is 390 points per session, and the text never states whether the constant sets the 1x1 slope as `100/390` points per bar, `1` point per bar, or something else; (b) **the ATR period is never specified** ("within one ATR", 11 occurrences of `ATR`, zero period definitions); (c) **the timestamp at which the rolling-window anchors are declared and frozen is not specified**; (d) tie handling when a bar is within 1 ATR of more than one line.

**F01 - Anchor revisits (Hypothesis 1, Section 3.2)**
- Event: the **first close within 1 ATR of an anchor** after that anchor is established (body Table 1 description).
- Direction: high-anchor revisits signed negative (resistance), low-anchor revisits signed positive (support); reported statistic is the signed 5-bar return.
- Counts: **2,826 IS events / 1,227 OOS events** over 1,748 / 743 sessions (1.62 and 1.66 events per session, research-computed).

**F03 - 1x1 angle cumulative abnormal return (Hypothesis 2, Section 3.3)**
- Event: bars closing **within 1 ATR of the 1x1 line**; statistic is the 5-bar CAR, compared across stressed / normal / trending regimes.
- Counts: **2,386 / 1,022 events**; the trending-regime subset printed in end-of-PDF Table 1 is **636 / 256**.

**F06 - Near-touch arrow signals (Hypothesis 3, Section 3.4)**
- Event: "a close within one ATR of the relevant fan line that **does not cross it**"; the abstract, Section 3.4's worked examples and end-of-PDF Table 1 all pin the traded line to the **1x1** ("F06 Near-touch 1x1"), while Section 3.4's first sentence says "the relevant fan line" - read here as **1x1 only**, with the prose ambiguity recorded.
- Direction: **with the line** - buy arrow on a touch of the rising 1x1 from a low anchor, sell arrow on a touch of the declining 1x1 from a high anchor.
- Counts: **2,945 / 1,273 events**; buy/sell split counts are **not printed** (research-computed from t and d: IS ~ 1,421 buy + 1,518 sell = 2,939 vs printed 2,945; OOS ~ 604 + 669 = 1,273 = printed 1,273).

**F07 - Fan crossings (Hypothesis 4, Section 3.5)**
- Event: the **first close on the wrong side of a fan line**; returns signed by crossing direction (1x2 crossing from above expected negative, 2x1 crossing from below expected positive).
- Counts: 1x2 **2,291 / 980**; 2x1 **2,980 / 1,256**; 1x1 **2,627 / 1,135**.
- Reported result: signed net returns are **significantly negative** for all three lines, i.e. the source's own trading implication is to **fade** the break, not follow it.

**F08 / F09 - internal contrasts (Section 3.6, not part of the four headline hypotheses)**
- F08: whether 4x1 / 1x4 produce larger absolute returns than 1x1 (7,424 / 3,213 events).
- F09: whether a strict monotone steepness hierarchy `8x1 > 4x1 > 2x1 > 1x1 > 1x2 > 1x4 > 1x8` holds (12,892 / 5,512 events) - tested with Jonckheere-Terpstra and Spearman.

**Regime classifier (Section 4.3):** rolling 90-session window; session is `stressed` if intraday range > 1.5x the rolling median range, `trending` if < 0.70x, else `normal`; ~ 20% / 55% / 25% in IS.

**Not specified anywhere (data gap, never treated as 0):** position sizing, capital allocation, treatment of overlapping/concurrent events, portfolio construction, equity curve, drawdown, net portfolio Sharpe, entry price beyond "market order", slippage in points per fill, order type choice between the two arrows, re-entry rules, and whether signals are taken on every qualifying bar or only the first per session (F01/F06/F07 say "first"/event-based; F03 is bar-based).

## Required data

- **Instrument / universe:** E-mini S&P 500 **continuous front-month futures (ES)**, single instrument; source states average daily volume above 1.5 million contracts during the study period.
- **Venue / vendor:** NinjaTrader **ratio-adjusted continuous contract** (multiplicative back-adjustment across quarterly rolls); the source states results are "qualitatively unchanged when using the unadjusted front-month series" but prints no numbers for that check -> data gap.
- **Market type:** exchange-traded equity-index futures (not crypto, not options, not spot).
- **Timeframe:** **1-minute (M1) OHLCV**, regular trading hours only, **09:30-16:00 Eastern Time**, 390 bars per session, timezone and session boundaries explicit.
- **Sample:** **2016-01-04 through 2025-12-31**; sessions with >5% missing bars or "obvious data errors" removed; **2,491 complete sessions = 1,748 in-sample (2016-2022) + 743 out-of-sample (2023-2025)**.
- **Fields:** OHLCV only. No order book, no trades/aggressor side, no open interest, no funding, no borrow, no options surface, no fundamentals - **the study is deliberately OHLCV-only**, and Section 6.4 states that order-book data would be required to identify the mechanism.
- **Derived series:** ATR (period **unspecified**), rolling 100-bar session extremes, fan-line price paths, rolling 90-session median range.
- **Point-in-time:** no publication lag is involved (pure price data); the IS/OOS split is the only look-ahead control, plus the claim that hypotheses were locked before the IS period ended (no registry proof, data gap).
- **Missing data:** source-side rule only (>5% missing bars -> drop session); no imputation rule stated.

## Execution assumptions

Cost determination was made from a **Methods-level read of Sections 4.1, 4.2, 4.4, 6.3, 6.4 plus a whole-document term scan of the pinned text**, not from the abstract.

- **Order type:** **market order**, stated explicitly - "The slippage assumption reflects a realistic market-order execution cost" and "we apply the conservative market-order assumption throughout" (Section 4.2). `market order` appears hyphenated as `market-order` twice; `limit order`/`limit-order` appears 4 times as the rejected alternative.
- **Fill model:** **not stated** beyond the market-order assumption (`fill`/`filled` has zero real occurrences in the pinned text; the two substring hits are inside "self-fulfilling"); signal-to-fill timing (same bar close vs next bar open) is **not stated** -> data gap.
- **Commission:** **$4.50 round-trip** (exchange + NFA fees), stated (Section 4.2); `commission` appears twice (Section 1 and Section 4.2).
- **Slippage:** **one tick = 0.25 ES points = $12.50 per side** (Section 4.2); Section 1 instead says "$12.50 slippage **per trade**" (C11). `slippage` appears 5 times.
- **Spread:** qualitative only - "the bid-ask spread at non-stressed times is typically one tick" (Section 4.2); no measured spread series, no stressed-spread figure. `bid-ask` appears 3 times (1 of them inside this cost paragraph, 2 in the literature review), `spread` 8 times (mostly theory prose).
- **Market impact:** `market impact` has **0 occurrences**; the 2 hits of `impact` are literature prose; the source instead argues ES is liquid enough that "individual trades do not move prices". Impact is therefore **not modelled -> data gap, never zero**.
- **Latency:** `latency` **0 occurrences** -> data gap.
- **Turnover / capacity / participation:** `turnover` **0**, `capacity` **0**, `participation` 1 (qualitative sentence about afternoon participation). Position size is never stated -> **no capacity model**.
- **Borrow / shorting / leverage / margin / funding:** `borrow` 0, `leverage` 1 hit (Section 6.1's hedged "perhaps 1.5-2.0 depending on leverage"), `margin` 1 hit (inside "marginally"), `funding` 0. Futures shorting has no borrow cost in the source's setting, but **no margin or leverage model is printed** -> data gap.
- **Cost applied:** every event return is reduced by the round trip before t-statistics, Sharpe ratios and confidence intervals (Section 4.2); the conclusion restates the round trip as "$4.50 RT + 0.25 pt slippage" (end-of-PDF Table 1 caption).
- **Cost in notional terms:** Section 4.2 prints "**approximately 0.26 basis points** of notional value" - **arithmetically irreconcilable** with the same paragraph (C3; see Independently reproduced).
- **Holding / exit:** fixed **5 M1 bars**, no stop, no take-profit, no time-based exit beyond the 5-bar horizon, no re-entry rule.
- **Distinguishable assumptions:** *source-reported* = market order, $4.50 RT commission, $12.50/side slippage, 5-bar horizon, RTH-only. *Not source-reported (research-proposed if ever used)* = next-bar-open entry, position sizing, event de-overlap, latency, capacity cap, portfolio netting.

## Evidence

### Source-reported

All figures below are **third-party claims from the pinned PDF**, none verified by us, each carrying its table/section provenance. `IS = 2016-2022 (1,748 sessions)`, `OOS = 2023-2025 (743 sessions)`; all p-values printed are **Benjamini-Hochberg adjusted at q = 0.05** (Section 4.4).

**H1 - anchor revisits (body Table 2 Panel A, n = 2,826 / 1,227)**
- 5-bar signed return: **IS t = 22.10, d = 0.416, p_adj < 0.001**; **OOS t = 17.41, d = 0.497, p_adj < 0.001** (abstract and Section 5.1).
- 15-bar: IS t = 22.95, d = 0.432; OOS t = 18.08, d = 0.516. 30-bar: IS t = 23.15, d = 0.435; OOS t = 13.27, d = 0.379.
- Distance-quintile OLS: **IS t = 2.13, p_adj = 0.042**; **OOS t = 1.39, p_adj = 0.211 (not significant)**.
- Politis-Romano stationary bootstrap annualised Sharpe: **IS 6.60 [5.75, 8.04]**; **OOS 7.89 [6.79, 8.98]** (1,000 replications).
- Hit rate after costs: **IS 1,706/2,826 = 60.4%**; **OOS 748/1,227 printed as 61.2%** (C7). Mean signed return **approximately 0.28 ES points ($14 per contract) after costs** (Section 5.1).
- Time-of-day split: first hour IS d = 0.313 / OOS d = 0.391; final hour IS d = 0.542 / OOS d = 0.609 (Section 5.1).

**H2 - 1x1 CAR (body Table 2 Panel B, n = 2,386 / 1,022)**
- Trending regime 5-bar CAR: **IS t = -4.56, d = -0.181, p_adj < 0.001**; **OOS t = -3.52, d = -0.220, p_adj = 0.008**.
- Normal regime IS d = -0.061, p_adj = 0.080 (ns); stressed regime IS d = +0.092, p_adj = 0.097 (ns); **unconditional 5-bar CAR IS d = -0.025, OOS d = -0.013 (not significant)**.
- Kruskal-Wallis across regimes: IS 14.96, p_adj = 0.003; OOS 12.67, p_adj = 0.013. Bullish-market CAR: IS t = -3.42, d = -0.095, p_adj = 0.003; **OOS t = -2.37, d = -0.102, p_adj = 0.054 (ns)**. Bull vs bear: IS d = -0.139, p_adj = 0.003; OOS d = -0.161, p_adj = 0.050.

**H3 - near-touch arrows (body Table 3 Panel A, n = 2,945 / 1,273)**
- All arrows: **IS t = 13.03, d = 0.240, p_adj < 0.001**; **OOS t = 11.30, d = 0.317, p_adj < 0.001**.
- Buy arrows: IS t = 9.01, d = 0.239; OOS t = 7.15, d = 0.291. Sell arrows: IS t = 9.43, d = 0.242; OOS t = 8.87, d = 0.343. Buy-vs-sell: IS t = 0.33, p = 0.742 (ns); OOS t = -0.34, p = 0.736 (ns).
- Sign-flip permutation test, **10,000 iterations**: p_adj < 0.001 in both periods (the row labelled "Sign-flip permutation Sharpe" prints 0.240 / 0.317, i.e. the d values - C10).
- **Annualised bootstrap Sharpe: IS 3.81, OOS 5.03** (the headline number; the source states in Section 6.1 that this is the Sharpe of *individual signal events*, not of a continuously invested portfolio).
- Kruskal-Wallis by regime: IS 15.27 p_adj < 0.001; OOS 7.46 p_adj = 0.028. By time-of-day: IS 170.7 p_adj < 0.001; OOS 62.82 p_adj < 0.001.

**H4 - fan crossings (body Table 3 Panel B)**
- 1x2 (n = 2,291 / 980): IS t = -7.41, d = -0.155; OOS t = -5.31, d = -0.170 (both p_adj < 0.001).
- 2x1 (n = 2,980 / 1,256): IS t = -9.39, d = -0.172; OOS t = -5.65, d = -0.159 (both p_adj < 0.001).
- 1x1 (n = 2,627 / 1,135): IS t = -12.50, d = -0.244; OOS t = -6.44, d = -0.191 (both p_adj < 0.001).
- Steepness OLS: IS t = 0.43, p_adj = 0.511 (ns); OOS t = 0.03, p_adj = 0.860 (ns).

**Internal contrasts (Section 5.5)**
- F08: 1x4 absolute-return effect IS at 15-bar (d = -0.113, p_adj = 0.001) and 30-bar (d = -0.145, p_adj < 0.001); **all OOS tests non-significant (best p_adj = 0.191)**.
- F09 hierarchy: Jonckheere-Terpstra **p_adj = 0.727 IS / 0.808 OOS** on n = 12,892 / 5,512; Spearman near zero in all subperiods.

**Subperiods (body Table 4 and end-of-PDF Table 2)**
- F01 d: Pre-COVID 0.482 (n = 1,621), COVID-2020 0.400 (n = 407), Post-COVID 0.485 (n = 798), Rate-Cycle OOS 0.506 (n = 837), AI-Rally OOS 0.494 (n = 390); all p_adj < 0.001.
- F06 d: 0.218 (n = 1,693), 0.305 (n = 419), 0.279 (n = 833), 0.302 (n = 862), 0.352 (n = 411); all p_adj < 0.001.
- F07 2x1 d: Pre-COVID -0.264, COVID-2020 -0.153, Post-COVID -0.093 (p_adj = 0.015), Rate-Cycle OOS -0.208 (n = 848, p_adj < 0.001), **AI-Rally OOS -0.094 (n = 408, p_adj = 0.118, ns)**.
- F03 (trending) subperiod row in body Table 4 prints Pre-COVID -0.068 with a significance marker and Post-COVID -0.005 (ns) - see C12.

**Robustness claimed (Section 6.3, not printed as tables)**
- Normalisation constant 80 / 120 points per session: "qualitatively unchanged", effect sizes within one standard error of baseline.
- ATR threshold 0.5 / 1.5 ATR: fewer-larger / more-smaller events, directionally consistent.
- All primary IS results remain significant at p < 0.01 under Bonferroni.
- Anchor lookback 50 / 150 bars: F01 OOS bootstrap Sharpe ranges **6.92 (50-bar) to 8.34 (150-bar)** vs baseline 7.89.
- Clustered standard errors ~ 12% larger than i.i.d., "implying that the reported t-statistics overstate precision by a factor of approximately 1.12" (Section 4.4).

**Statistical protocol:** one-sample t-tests with Cohen's d, sign-flip permutation (10,000), Politis-Romano stationary bootstrap (1,000 reps, Patton-Politis-White automatic block length), OLS, Jonckheere-Terpstra, Spearman, Kruskal-Wallis, BH FDR at q = 0.05, five-subperiod robustness rule requiring p_adj < 0.05 in at least two of five subperiods (Section 4.5).

### Independently reproduced

**not independently reproduced**

We did not re-run the event study: the paper's data (NinjaTrader ratio-adjusted continuous ES M1) and its code are not available to us, the AlgForge replication host timed out (2026-09-29), and Scout scope excludes backtesting. What we *did* verify is arithmetic and provenance against the pinned PDF (script `gann_check.py`, pypdf 6.16.2 extraction, **all assertions either reproduced or recorded as contradictions above**):

- **Reproduced (16/16):** the one-sample identity `d = t / sqrt(n)` holds for every printed headline row using the printed n - F01 5/15/30-bar IS and OOS (0.4157/0.4970/0.4317/0.5162/0.4355/0.3788 vs 0.416/0.497/0.432/0.516/0.435/0.379), F06 all-arrows IS/OOS (0.2401/0.3167 vs 0.240/0.317), F07 1x2/2x1/1x1 IS and OOS (-0.1548/-0.1696/-0.1720/-0.1594/-0.2439/-0.1912 vs -0.155/-0.170/-0.172/-0.159/-0.244/-0.191), F03 trending IS/OOS using end-Table 1 n = 636/256 (-0.1808/-0.2198 vs -0.181/-0.220).
- **Reproduced:** all subperiod n sums - F01 1,621+407+798 = 2,826 and 837+390 = 1,227; F06 1,693+419+833 = 2,945 and 862+411 = 1,273; F07 2x1 848+408 = 1,256.
- **Reproduced:** F01 IS hit rate 1,706/2,826 = 60.37% (printed 60.4%).
- **Reproduced:** $14 per contract = 0.28 ES points x $50/point; 0.28 points = 1.12 ticks of 0.25 points (the conclusion's "roughly 0.5-1.0 ticks of edge per signal after costs").
- **Reproduced:** implied buy/sell arrow sub-sample counts from t and d (IS ~ 1,421 + 1,518 = 2,939 vs printed 2,945; OOS ~ 604 + 669 = 1,273 = printed) - consistent within rounding, confirming the split counts are simply unprinted.
- **Reproduced:** reference-entry count = **38** entries carrying a publication year (vs landing "0 References").
- **Reproduced:** angle enumeration = **7** items in the "eight Gann angles" list (C9).
- **Context (research-computed, not a source claim):** the printed annualised bootstrap Sharpes sit at 0.770-0.790 of `d x sqrt(events per year)` (F01 IS 6.60 vs 8.36; F01 OOS 7.89 vs 10.05; F06 IS 3.81 vs 4.92; F06 OOS 5.03 vs 6.53), i.e. an effective-sample haircut of roughly 0.6x consistent with multiple events clustering inside the same session.
- **Failed to reconcile (recorded as contradictions, not as source errors we corrected):** C3 cost-in-bp (computed 1.180 bp vs printed 0.26 bp; even the cheapest reading of the same paragraph gives 0.68 bp), C4 power (0.564-0.688 two-sided / 0.683-0.789 one-sided vs "exceeds 0.80"), C7 OOS hit rate (60.96% vs 61.2%), C5 signal frequency (1,273/3 years = 424.3 per year vs "approximately 1,273 per year"), C6 horizon (5 M1 bars = 5 minutes vs "25 minutes"), C12 (a subperiod |d| = 0.068 needs n >= 831 to reach |t| >= 1.96 while the whole IS trending sample is n = 636).

### Negative evidence

1. Hypothesis 2 fails unconditionally: overall 5-bar CAR is **not significant in either period** (IS d = -0.025, OOS d = -0.013).
2. H2 normal-regime effect is non-significant after BH (IS d = -0.061, p_adj = 0.080) and the stressed-regime effect has the **opposite sign** to the hypothesis (IS d = +0.092, p_adj = 0.097).
3. H2 bullish-market CAR fails OOS (p_adj = 0.054) and bull-vs-bear sits exactly on the 0.050 boundary OOS.
4. F08 extreme fan lines (4x1/1x4) are **uniformly non-significant OOS** (best p_adj = 0.191); only IS cells appear.
5. F09 monotone steepness hierarchy is **flatly null** on the study's largest sample (n = 12,892 IS / 5,512 OOS; JT p_adj = 0.727 / 0.808) - the strict form of Gann's own theory is rejected by the paper.
6. H1's distance-decay (a claimed specific test of the level hypothesis) **fails to replicate OOS** (p_adj = 0.211).
7. F07 2x1 fails one of the two OOS subperiods (AI-Rally p_adj = 0.118) and its OOS d shrinks to -0.094.
8. The source's own Section 6.1 caveat: the 3.81-5.03 "Sharpe" is an **event-level** statistic, and "the all-in annual Sharpe ratio of a practical implementation would be considerably lower - **perhaps 1.5-2.0** depending on leverage" (a hedged, unprinted estimate).
9. No portfolio-level artefact exists anywhere in the paper: **no equity curve, no drawdown, no net portfolio Sharpe, no position sizing, no treatment of overlapping events** - F01 and F06 alone fire ~1.6 events per session with a 5-bar holding period, so overlap is unavoidable and unaddressed.
10. Reported t-statistics are acknowledged by the source to overstate precision by ~1.12x under session-clustered standard errors.
11. Three of four headline hypotheses rest on **sign/magnitude of a small per-event edge**: the source's own conclusion puts it at "roughly 0.5-1.0 ticks of edge per signal after costs".
12. **Conflict of interest:** the author "intends to commercialise the technical indicators examined in this study" (Conflict of Interest block).
13. **Replication package unverifiable:** `https://algforge.com` timed out from this environment on 2026-09-29 (curl 45 s timeout; browser navigation timeout); no code, data or results file was retrieved. The paper points only to a bare homepage, not a commit, DOI or archive.
14. **Pre-registration asserted without artefact:** no registry, timestamp, URL or identifier anywhere in the pinned PDF.
15. Single instrument (ES), single venue data path (NinjaTrader continuous), single decade; the source itself asks for replication on NQ/MES and 5-/15-minute aggregations (Section 6.4).
16. Mechanism not identified: **no order-book data**, so order clustering cannot be separated from round-number, VWAP or pivot-point proximity - the source states "Without order book data, we cannot definitively rule this out" (Section 6.2).
17. Alternative-explanation exposure acknowledged by the source: the anchor construction "is related to Donchian channels and pivot-point systems" (Section 6.2), so H1 may be generic extremum re-testing.
18. Effect-size dependence on discretionary thresholds: the 1-ATR proximity rule is "based on practitioner convention, not optimisation", and the ATR period itself is never defined - a third party cannot reconstruct the exact event set.
19. Underlying level-effect literature is itself contested: the paper cites Sullivan-Timmermann-White (1999) data-snooping corrections and Park-Irwin (2007) unresolved cost/data-snooping concerns as context.
20. SSRN working paper, **0 citations**, independent single author, "All rights reserved. No reuse allowed without permission." - low external validation and a redistribution constraint (this record normalises only short printed values, table cells and section references).
21. Family multiplicity: 9 features x several horizons x thresholds x 5 subperiods are searched, with BH applied *within* each feature study only (Section 4.4), not across the whole family; no deflated-Sharpe or White reality-check adjustment is reported.
22. Cost sensitivity is only argued, never swept: no breakeven-cost table exists; the printed 0.26 bp figure is itself wrong by ~4.5x (C3), so any net-of-cost reading must be recomputed from first principles.
23. Adjacent contrary/competing records already in this repository: pre-registered 225-cell opening-range-breakout falsification on nine US futures (SSRN 7428398), `mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05` (NinjaTrader intraday OHLCV gross-edge ceiling on MNQ), `cme-futures-ifvg-cisd-opening-breakout-disproof-2026-09-16`, `tradingview-strong-pressure-zones-sweep-reclaim-2026-09-27`, `btc-30m-wyckoff-squeeze-multilayer-trend-momentum-2026-09-14`, `long-only-us-equity-ath-trend-following-...-ssrn-5084316-2026-09-27` and `crypto-cross-sectional-nearness-to-52-week-high-momentum-2026-08-31` (anchor-based levels from a different source and mechanism).

## Falsification plan

Everything below is **research-defined / research-proposed** by this Scout - none of these thresholds comes from the source, and the source prints no failure rules of its own. No-retuning rule: **all parameters stay frozen at the values printed in the pinned PDF; a failed gate may not be rescued by re-optimising thresholds on the evaluation sample.**

- **F1 - printed-value reproduction (research-defined).** Re-derive every `d = t / sqrt(n)` cell in body Tables 2-3 and end-of-PDF Table 1 from a re-implemented event study, at tolerance +/-0.02 d and +/-5% event counts. Fail if any headline cell misses.
- **F2 - second-vendor data gate (research-defined).** Rebuild ES M1 RTH 2016-2025 from an independent vendor (different ratio-adjustment). Fail if the OOS H1 d falls below **0.20** or the sign of H3/H4 flips.
- **F3 - ATR-period reconstruction gate (research-defined).** Sweep ATR period {10, 14, 20} (the parameter the source never states). Fail if the sign of H1 or H3 changes anywhere in the sweep.
- **F4 - normalisation-semantics gate (research-defined).** Implement both readings of the constant (1x1 = 100/390 points per bar vs 1x1 = 1 point per bar) and the source's 80/100/120 sweep. Fail if either reading reverses the H1/H3/H4 signs.
- **F5 - anchor-freeze semantics gate (research-defined).** Compare the source's "frozen for the remainder of the session" anchors against fully rolling anchors. Fail if frozen-anchor H1 d drops below 0.10.
- **F6 - cost ladder (research-defined).** Round-trip cost ladder of 0 / 1x / 2x / 4x the source's own $29.50 round trip (plus an explicit tick-by-tick bid-ask model). Fail the tradability claim if H3's net mean signed return is <= 0 at 1x.
- **F7 - portfolio-level gate (research-defined).** Build one account curve: 1 contract per signal, entry at the next bar's open (market order), 5-bar exit, all signals de-overlapped by first-come-first-served with one position at a time. Fail if net-of-cost annualised Sharpe <= 1.0 or maximum drawdown > 25% over 2016-2025. This gate directly targets the source's own "perhaps 1.5-2.0" hedge.
- **F8 - competing-explanation controls (research-defined).** Add round-number proximity, distance to session VWAP, classic pivot-point distance and Donchian-channel position as controls in a cross-sectional regression on signed 5-bar returns. Fail the Gann-specific claim if the anchor/fan coefficients become insignificant at p_adj >= 0.10.
- **F9 - placebo levels (research-defined).** Generate 10,000 pseudo-anchor sets (random price levels matched on distance-to-price and time-of-day). Fail if the observed H1 d does not exceed the **95th percentile** of the placebo distribution.
- **F10 - cross-instrument / cross-bar gate (research-defined).** Repeat on NQ, MES and on 5-minute bars. Fail generalisability if fewer than **2 of 3** variants reproduce the H1 and H3 signs OOS.
- **F11 - frozen forward window (research-defined).** Freeze every rule and run 2026-01-01 onward as a true forward test. Fail if the monthly H3 hit rate is <= 50% for **12 consecutive months**.
- **F12 - multiplicity gate (research-defined).** Re-run the whole 9-feature x horizon x threshold family under a single Benjamini-Hochberg correction at q < 0.10 across the full family (not per feature) plus a deflated-Sharpe adjustment. Fail if H1/H3/H4 no longer clear.
- **F13 - capacity / participation (research-proposed).** Cap participation at research-proposed **20% of 20-day average volume** in contracts and re-scale; fail the capacity claim if net edge per event falls below half the reported 0.28 points.
- **Action on failure:** any failed gate downgrades the corresponding hypothesis to `rejected` in a follow-up record; parameters are not retuned to rescue it.

## Crypto portability

**adapted** - the *mechanism* (shared focal price levels attracting clustered orders) is venue-agnostic in principle, but **every implementation detail of this study is equity-futures-session-specific, and the source contains zero crypto evidence**, so crypto performance stays **unproven**.

Porting risks:
- **Session structure:** the normalisation constant is defined as "100 points per session (**390 M1 bars in regular trading hours**)" and anchors are session high/low. Crypto trades 24/7 with no RTH session; there is no natural 390-bar session, so both the constant and the "session anchor" must be redefined (e.g. UTC-day or 24h rolling window) - a **research-proposed** choice, not a source rule.
- **Practitioner population:** the mechanism requires a large community actually drawing Gann fans on that instrument. Whether the Gann-practitioner population is comparably large on BTC/USDT perps is **unstated / unmeasured** - without it, the coordination mechanism has no causal driver.
- **Instrument and multiplier:** ES has a $50/point multiplier, 0.25-point tick and ~$12.50 one-tick cost; crypto perps have different tick sizes, contract multipliers, and maker/taker schedules - the flat $4.50 + $12.50 model does not transport.
- **Spot vs perpetual:** no funding, no liquidation engine and no mark/index price exist in the source; on perps a 5-bar holding window spans funding intervals in some venues, which the source never models.
- **Venue fragmentation:** level effects measured on one deep book (CME Globex) may not appear when the same "level" is fragmented across Binance/Bybit/OKX/Hyperliquid order books.
- **Listing/survivorship and candles:** continuous perp feeds re-base on contract swaps and delistings; candle boundaries, timestamps and stale-book handling differ from a single exchange's M1 series.
- **Tick/lot rules:** exchange-specific minimum price increments and lot sizes alter what "within 1 ATR of the line" means in ticks.

## Limitations

- **underspecified:** ATR period; normalisation-constant semantics; anchor-freeze timestamp; tie handling; F06's "relevant fan line" vs 1x1; buy/sell sub-sample counts; F03 subperiod n; signal-to-fill timing; position sizing; overlap handling.
- **data gap (never zero):** latency, fill model, market impact, participation rate, turnover, capacity, borrow/margin/leverage model, measured spread, stressed-regime spread, portfolio net returns, drawdown, replication package availability, pre-registration artefact, companion-paper identity.
- **not independently reproduced:** all empirical results; only arithmetic identities and provenance were checked.
- **contested / internally inconsistent:** 13 recorded contradictions (frontmatter `contradictions`), of which C3, C4, C5, C6, C7 and C12 are arithmetic failures reproduced by our own script against the pinned text.
- **source quality:** SSRN working paper, 0 citations, independent single author, commercial interest disclosed, licence restricts reuse, journal submission status only.
- **identification:** no order-book data, so the coordination mechanism is asserted rather than shown; round-number/VWAP/pivot and generic extremum-retest explanations remain live (source's own Section 6.2).
- **sample:** one instrument, one decade, one data vendor, RTH only, no pre-2016 or post-2025 window, no cross-asset test.
- **incremental-write check:** no existing repository record shares this source identity or this mechanism (angle-derived geometric levels as intraday S/R events on equity-index futures); closest neighbours differ in source, mechanism and market (see Negative evidence item 23).

## Implementation status

`implementation_status: not-implemented`.

Nothing in this record has been implemented in our research stack: no event study was re-run, no ES data was downloaded, no signal generator, backtest, production card, Qlib run, Paper, Testnet or Live workflow exists for this hypothesis. The only artifacts produced by this run are this Markdown record, the pinned PDF text extraction in scratch, and an arithmetic-only check script.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`.

The presence of this record **does not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet or live trading. Those are separate, explicitly gated decisions taken downstream of this repository.

## Related Wiki records

Read-only Wiki Brain searches run this session: `kb_search "Gann angles support resistance technical analysis"` -> **0 results**; `kb_search "order clustering price levels intraday futures technical rules"` -> 1 hit, `quant/korean-venue-share-indicator-kvsi-cross-exchange-rl-2026-09-05.md`, which is unrelated (Korean venue-share indicator for RL crypto trading) and therefore **not linked as related**. `kb_read quant/strategy-research-record-spec-v2.md` -> file not found; the run failed closed onto `quant/strategy-research-record-spec-v1.md` (canonical, 10,289 bytes, sha256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`). **No related Wiki page is known, so no Wiki link is written here** (fabricating one is forbidden). No page was written to Wiki Brain by this run.

## Sources

- Brown, Max. *Do Gann Angles Work? An Empirical Test of Angle-Derived Support and Resistance in High-Frequency Equity Futures*. SSRN working paper, DOI `10.2139/ssrn.6918818`, landing `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6918818`, Date Written 2026-04-14, Posted 2026-06-19, 14 pages, all rights reserved / no reuse without permission. Pinned PDF SHA-256 `20e985d162284ea98f80d2bc36ee55528d75ff41db2e372998139df76921d509` (580,917 bytes), read in full 2026-09-29. All quantitative claims in this record trace to this PDF by section, body/end-table number, or abstract.
- Replication package named by the source: `https://algforge.com` - **retrieval failed (connection timeout) on 2026-09-29; availability unverified**.
- (Neighbouring repository records cited only as dedup/negative-evidence context, each with its own source: SSRN 7428398 opening-range-breakout falsification; SSRN 5084316 all-time-high trend record; SSRN 7073258 own-SMA cash-retreat record; arXiv 2609.13715 subordinated market observables; TradingView Strong Pressure Zones `https://www.tradingview.com/script/27MBFCQ0-Strong-Pressure-Zones-ProjectSyndicate/`.)
