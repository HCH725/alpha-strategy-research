---
schema: strategy-research-record-v1
title: "Long-Only Time-Series Trend Above Each Name's Own Moving Average with Cash Retreat on US Large Caps: A Walk-Forward Pass That Attribution Dissolves to One Stock (SSRN 7073258)"
created: 2026-09-28
updated: 2026-09-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equity
  - us-large-cap
  - trend-following
  - time-series-momentum
  - cash-retreat
  - walk-forward
  - single-name-concentration
  - attribution-audit
  - survivorship-bias
  - drawdown-reduction
  - backtest-audit
status: research-only
confidence: medium
source_as_of: 2026-07-24
sources:
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7073258"
  - "https://dx.doi.org/10.2139/ssrn.7073258"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Headline CAGR-gap conflict: section 1 says the walk-forward posts 'a fourteen-percentage-point CAGR advantage over the index', while the printed stitched values are 34.1% against 20.8% (section 4.3, Table 7 row 6) = +13.3pp, and section 4.5 itself writes '+13.3' and '+20.5'."
  - "Universal drawdown phrasing vs printed cells: the abstract claims maximum drawdowns of '-13% to -19% against -24% to -34% for buy-and-hold' and section 5.2 says the cash-retreat advantage 'survives every attribution layer', yet Table 2's worst in-sample cell prints -35.7% against SPY's -33.8% and Table 7 row 12 / Figure 5 print -38.6% for the 99-name high-volatility tercile, which the source itself calls 'worse than buy-and-hold'. The -13% to -19% range holds only for the full-universe walk-forward rows."
  - "'Every cell of its 36-point parameter grid beats buy-and-hold in-sample' (abstract, section 4.2) is Sharpe-scoped (section 1 states it explicitly for the Sharpe ratio), but the abstract's unqualified wording is contradicted on drawdown: Table 2's worst cell has a deeper maximum drawdown (-35.7%) than buy-and-hold (-33.8%)."
  - "Out-of-sample span printed two ways: Table 3 labels the stitched block 'Stitched (629 days)' while section 4.7 says all walk-forward rows share an OOS span of '627-629 trading days'."
  - "Attribution configuration not disclosed in the protocol: section 3.3 describes the volatility-tercile layer only as 'run the strategy independently within each tercile', but the Table 4 caption and Figure 4 run the trend rule at '100d/top-3', not the section 3.1 default of 100d/5 used for the Table 1 baseline; the deviation is never flagged as a specification change."
  - "Reference-count conflict: the SSRN landing prints heading '0 References' while the pinned PDF carries 13 numbered reference entries (Bailey-Borwein-Lopez de Prado-Zhu 2014 through Sullivan-Timmermann-White 1999, including the uncited-ID companion entry 'Malan, P. (2026)')."
---

# Long-Only Time-Series Trend Above Each Name's Own Moving Average with Cash Retreat on US Large Caps: A Walk-Forward Pass That Attribution Dissolves to One Stock (SSRN 7073258)

## Provenance

- **Primary source:** Malan, Prashant. "One Ticker Deep: The Trend Strategy That Passed Every Test and Still Shouldn't Be Believed." SSRN working paper, DOI `10.2139/ssrn.7073258`.
- **Canonical stable URLs:** landing `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7073258`; DOI `https://dx.doi.org/10.2139/ssrn.7073258`.
- **Author exactly as source:** "Prashant Malan", sole author, affiliation line "Independent" (landing); PDF title block prints "Author: Prashant Malan" with no affiliation, no co-authors, no ORCID, no email and no contact address in the pinned text. The landing carries a collapsed "Show contact information" control that was **not expanded**, so any contact data behind it is `data gap` rather than "none".
- **Version / dates (all printed forms preserved, unreconciled):** PDF title block "Draft: July 2026"; PDF metadata `/CreationDate` `D:20260707152510+00'00'` (2026-07-07 15:25:10 UTC); landing "Date Written: July 07, 2026"; landing "Posted: 24 Jul 2026"; suggested citation "July 07, 2026". Landing shows "20 Pages", matching the pinned 20-page PDF. No "Last revised" field is printed, so a version number beyond the single posting is `not stated in source`.
- **Companion paper dependency:** the PDF states on page 1 that it is the "Companion paper to 'Do Simple Cross-sectional Trend Strategies Survive Honest Validation? Evidence from a Small US Large-Cap Universe, 2020-2024.'" and the reference list gives "Malan, P. (2026). ... Working paper, SSRN." with **no abstract number, DOI or URL**, so the companion's identity is `underspecified` inside this source (the engine, cost model and walk-forward loop are explicitly delegated to that companion's appendix).
- **Publication / peer-review status:** SSRN working paper. The landing prints no journal, no issue, no peer-review statement and no preprint banner; the pinned text contains no peer-review claim, so publication and peer-review status are `not stated in source`.
- **License:** the landing shows the SSRN license line "The copyright holder has granted SSRN a license. All rights reserved. No reuse allowed without permission." Only printed values, section/table references and short quoted phrases are normalised here; no source prose is reproduced wholesale.
- **Landing statistics at read time (2026-09-28):** heading "0 References", heading "0 Citations", DOWNLOADS moving 113 -> 114 and ABSTRACT VIEWS 285 -> 287 during the session (bot-verification interstitial cleared first); keywords "trend following, time-series momentum, backtest overfitting, attribution, survivorship bias, concentration risk"; JEL codes G11, G12, G14.
- **Pinned PDF retrieval:** the landing page was opened in a browser session on 2026-09-28 and the "Open PDF in Browser" `Delivery.cfm/7073258.pdf?abstractid=7073258&mirid=1&type=2` link was followed; that delivery link resolves in-session to a temporary time-limited object URL which was used transiently to fetch the bytes. **No presigned, expiring or session-bound URL is stored anywhere in this record.** Artifact: **1,067,814 bytes, PDF 1.4, 20 pages, SHA-256 `349bacf866834dce805a4f1f42028f4eee1f49d1dc974f1acdfae593927f4eb7`**; text extracted with pypdf 6.16.2 to **38,879 characters across all 20 pages**, and **all 20 pages were read**, including the abstract, sections 1-7, Tables 1-7, Figure 1-8 captions, the 13-entry reference list, Appendix A source code (A.1-A.4) and Appendix B replication commands. PDF metadata: `/Title` "paper", `/Producer` "Skia/PDF m149", `/Creator` a HeadlessChrome/Edge 149 print pipeline, i.e. the file was produced by a browser print-to-PDF step rather than a typesetting system (which explains the tab-separated text layer).
- **Code / data availability:** no GitHub, OSF, Zenodo or any repository URL appears in the pinned text (word scan: `github` = 0). Appendix A gives only a local "Repository layout: research/{data, strategies, backtest}" and Appendix B requires "Alpaca paper-trading keys in a local .env", so code and data availability are `data gap` (author-on-request is `not stated in source`).
- **AI / funding / conflict disclosure:** no AI-use disclosure, no funding statement and no competing-interest statement appears in the pinned text (`data gap` - the sections are absent, which is not the same as "none declared").
- **Dedup (pre-write, hidden-inclusive):** `rg -uuu` over the whole checkout including `.git/`, `.mimo-worktrees/`, `.agents/`, `.hermes/` and `coverage_manifest.csv` for `7073258`, `ssrn.7073258`, `One Ticker Deep`, `Prashant Malan`, `Malan`, `Cross-Sectional Trend Strategies Survive`, `survive honest validation`, `ex-NVDA`, `UNIVERSE_2020` and `run_trend_follow` returned **zero source-identity hits** (exit 1); `novy-marx` positive control returned 9 files in the same session; `Alpaca` (a data-vendor name, not a source identity) hit only 5 unrelated records. `git log --oneline -20` was used as a convenience glance only, never as the dedup.
- **Four-axis distinction (source identity and mechanism differ in every pair):**
  - vs `long-only-us-equity-ath-trend-following-vol-sizing-atr-ratchet-turnover-control-ssrn-5084316-2026-09-27` (SSRN 5084316, Zarattini/Pagani/Wilcox): that source's signal is an all-time-high breakout with a ratcheting `ATH x (1 - ATR/Close)^10` stop and inverse-volatility sizing on a ~31,000-name survivorship-free panel 1950-2024, with the friction layer as the studied object; this source's signal is a **positive own-SMA score ranking with cash retreat, fixed 1/n sizing and no stop**, on 26/99 US large caps 2020-2024, with **single-name attribution of a walk-forward pass** as the studied object.
  - vs `industry-trend-keltner-donchian-fallback-wfa-falsification-arxiv-2412.14361-2026-09-23` (arXiv 2412.14361 / SSRN 4857230): dual-channel Keltner-Donchian trend on 48 US **industry** portfolios with fallback allocations and a momentum overlay; this record is single-name long-only own-MA concentration with no channel breakout and no industry aggregation, from a different source identity.
  - vs `us-equity-vortex-top2-cross-sectional-trend-phase-robustness-2026-09-13` (GitHub `SailorChina/us-stock-factor-backtest` @ `46d81b44...`): that signal is a Vortex-indicator cross-sectional Top2 with liquidity gating, studied for rebalance-phase and execution-drag robustness on 2018-2026 data; different source, different indicator (Vortex vs `P/SMA_n - 1`), different robustness object (phase/liquidity vs single-name concentration).
  - vs `published-equity-anomaly-zoo-large-cap-post-2005-luck-adjusted-null-arxiv-2607.06502-2026-09-23` (Chen & Welch, arXiv 2607.06502): that record is a luck-adjusted null across ~200 published anomalies; this source's cross-sectional long-short results (Table 6 rows 1-2) are its **own** walk-forward runs of MA crossover and 12-1 momentum on two universes, and its distinctive contribution is the attribution ladder on a rule that passed, which the anomaly-zoo record does not provide.

## Economic mechanism

### Source-reported

The author's stated mechanism has two separable parts. First, the rule is a **time-series (not cross-sectional) trend test**: "Each stock is compared to its own trailing moving average rather than to its peers. Names trading above their average are candidates to hold; names below it are sold" (section 1), so the zero line of `P/SMA_n - 1` is an economically meaningful buy/sell boundary rather than a rank cut. Because sizing is fixed at `1/n_hold` instead of renormalised, "gross exposure floats between 0 and 100% with the breadth of the uptrend - this is the mechanism that de-risks the book in broad selloffs without any dedicated crash logic" (section 3.1); the source calls this the "cash-retreat mechanism" and reads it as the source of the drawdown reduction (Figure 1, section 5.2).

Second, the paper's own conclusion is that the **return** component does not survive attribution and the **risk** component does. Its explanation of the passing backtest is explicitly a concentration story: the rule "is a momentum-concentration device: it channels the portfolio into whatever the universe's highest-volatility uptrend is, and 2020-2024 supplied a historic one. Its Sharpe advantage is an artefact of that supply. Its drawdown advantage, by contrast, is mechanical" (section 5.2). The residual claim the author is willing to defend is "market-like returns with materially smaller drawdowns", not "34% a year", and he ties it to the established reading of time-series momentum as primarily a tail-risk modifier (citing Moskowitz, Ooi and Pedersen 2012 and Faber 2007, both read inside the pinned PDF).

### Research interpretation

Hypothesised mechanism in falsifiable form: a **volatility-conditioned momentum-concentration device plus a mechanical gross-exposure throttle**.

- The throttle (risk channel) is deterministic and stock-independent: when broad trends break, fewer names qualify, gross exposure falls, and the left tail is truncated without a crash rule. This channel predicts drawdown reduction that survives removal of any single constituent - which is exactly what the source reports (section 4.5).
- The concentration (return channel) predicts the opposite: the excess return should be a function of the universe's single largest volatility-adjusted winner, should be monotone in trailing volatility, and should fail to replicate on universes lacking such a winner. The source reports all three (Tables 4-5).

Component roles, preserved rather than collapsed:

```text
Regime (source): implicit only - name qualifies if score = P/SMA_n - 1 > 0 at rebalance
Primary signal (source): rank positive-score names by score, hold the top n_hold at 1/n_hold each
Confirmation filter (source): none - no volume, volatility, breadth or macro gate exists
Risk / exit (source): no stop, no take-profit; shortfall (and the whole book) sits in cash;
                      weights held constant between 5-day rebalances; rf = 0 on cash
Evaluation (source): 60/40 chronological split + 5-fold walk-forward (select every 126 trading
                     days on a trailing 378-day window), 36-cell grid, 5 bps per unit gross turnover
What is NOT a component: borrow, margin, leverage, market impact, capacity, order type - all data gap
```

Alternative explanations the source itself tests and rejects/keeps open: survivorship of the stock list (rejected as the cause - fixing the universe *improves* the headline, section 4.6); breadth of the universe (rejected as the explanation for the companion paper's long-short failures, Table 6); single-name luck (confirmed - the paper's own verdict). Explanations the paper does **not** test and we consider live: factor exposure (no regression on market/size/momentum/volatility factors is run - the source lists this as a limitation in section 6), and a general high-volatility-beta exposure rather than a trend mechanism. Both remain open.

## Signal

All items below are `source-reported` unless explicitly labelled `research-proposed` or `underspecified`.

- **Formation timestamp:** at each rebalance date, defined in Appendix A.1 as `prices.index[window::rebalance_days]`, i.e. the `window`-th bar and every `rebalance_days` bars after it. The engine applies no look-ahead: "weights lag their signal by one day" (section 3.2). Whether the underlying price is the adjusted close or the daily VWAP is `underspecified` (both fields are fetched per section 2.1; the Appendix A.1 helper takes a `prices` frame without stating which field).
- **Lookback:** `n`-day simple moving average of price, default `n = 100` (section 3.1); swept over `n in {20, 40, 60, 80, 100, 125, 150, 200, 250}` (section 3.2, Appendix A.4). Warm-up: the first `window` bars produce no rebalance date (`index[window::5]`), so the effective start is `window` bars after 2020-01-02; endpoints are neither stated as inclusive nor exclusive beyond that code - `underspecified` for the 250-day cell.
- **Long entry:** among names with `score > 0`, take the `n_hold` highest scores and weight each `1/n_hold` (Appendix A.1). Ties are broken by the pandas `sort_values` order on the score vector - tie handling is `underspecified` (no explicit rule printed).
- **Short entry:** none. The strategy is long-only; the short side exists only in the companion paper's dollar-neutral constructions, which are quoted here only as Table 6 rows.
- **Exit:** not time-based and not stop-based. A held name exits at the next rebalance if its score is no longer among the top `n_hold` positive scores; if fewer than `n_hold` names qualify the shortfall stays in cash; if none qualify the book is entirely in cash (section 3.1). There is no stop-loss, take-profit or trailing rule anywhere in the pinned text (word scan: `stop` = 0, `stops` = 1 and that single hit is the idiom "stops short of formal factor attribution").
- **Holding period:** positions are held constant between rebalances, so 5 trading days per rebalance cycle; no re-entry rule between rebalances (`target.ffill()` in Appendix A.1).
- **Parameters:** `window` (9 values above), `n_hold in {3, 5, 8, 10}` (36 cells total), `rebalance_days = 5`, default configuration `100d / 5` (section 3.1). Walk-forward selection: re-select the cell every 126 trading days on a trailing 378-day window, concatenate the out-of-sample blocks (section 3.2). The volatility-tercile attribution runs use `100d/top-3` per the Table 4 caption - a configuration change from the baseline that the protocol description does not flag (frontmatter contradiction 5).
- **Position sizing:** fixed `1/n_hold` per held name, gross exposure between 0 and 100%, deliberately not renormalised; no leverage, no margin, no cash yield (risk-free rate set to zero, section 3.2).
- **Attribution protocols (fixed before inspecting results, section 3.3):** (a) volatility terciles ranked on **full-sample** annualised volatility (source acknowledges mild look-ahead and calls the sort diagnostic only); (b) single-name exclusion of NVIDIA with the whole walk-forward re-run; (c) universe replacement plus re-running the companion paper's two long-short strategies on the broadened universe as a negative control.
- **Reproducibility verdict:** the rule itself is unusually well specified for a working paper - Appendix A.1 prints the strategy function and Appendix B prints the exact command for each table and figure. What is `underspecified` is the **evaluation harness** (engine, turnover definition, cost application order, tie handling, price field), all of which the paper delegates to the companion paper's appendix, which is not part of this source.

## Required data

- **Instruments / universe:** US listed common stocks, two panels - (i) a 26-name liquid large-cap list across five sectors "hand-picked in 2026, i.e. after the sample" (section 2.2), of which **17 names are printed** in the Figure 4 caption (low-volatility tercile JNJ, KO, PEP, WMT, MRK, MCD, PFE, V at 19.7-27.9% annualised vol; high-volatility tercile XOM, CVX, AMZN, BAC, ADBE, CRM, INTC, META, NVDA at 34.2-53.9%) - the remaining 9 members are `data gap`; (ii) a 99-name list "reconstructing S&P 100 membership as of January 2020" (section 2.2, Appendix A.4), of which the appendix prints 10 leading tickers, the literal comment "# ... 79 further names ...", and 9 trailing tickers (98 of the claimed 99 are accounted for), so the full list is `underspecified` and not reconstructable from the paper alone.
- **Venue / market type:** no venue is named for execution; data come from the **Alpaca Market Data API** (section 2.1), spot cash equities, long-only, no derivatives.
- **Timeframe:** daily bars, split- and dividend-adjusted, 2 January 2020 to 30 December 2024, 1,257 trading days, with fields open, high, low, close, volume, trade count and daily VWAP (section 2.1). SPY proxies buy-and-hold and is "never tradable".
- **Point-in-time:** the 26-name universe is explicitly **not** point-in-time (selected in 2026, after the sample); the 99-name universe is selected on January 2020 information but "membership is reconstructed from public sources rather than a licensed point-in-time constituents file" and mid-sample delistings (Allergan acquired May 2020; Raytheon/United Technologies merged April 2020) "could not be included because the data vendor does not serve delisted tickers" (section 2.2) - so both panels retain survivorship of the Shumway (1997) type.
- **Fields needed to reproduce:** adjusted OHLC for `P/SMA_n`, calendar of rebalance days, and SPY adjusted close for the benchmark; no funding, mark/index, order-book, open interest, options, borrow or on-chain data are used.
- **Timestamp / timezone:** `data gap` - no timezone, session-boundary or bar-closing convention is stated; "trading days" are taken to be US equity sessions by implication only.
- **Missing data:** the source states all 99 names have "full 1,257-day coverage"; no imputation, halt or partial-bar policy is printed (`data gap`).
- **Cost fields:** commission, exchange/regulatory fees, bid-ask spread, slippage, market impact, participation, borrow, latency, fill model and turnover definition are **not observed, not modelled and mostly not mentioned** anywhere in the pinned text (see Execution assumptions); the single cost input is a flat `5 bps per unit of gross turnover`.

## Execution assumptions

**Source-level cost determination (Methods-level read, not an abstract-only judgment).** The pinned PDF's section 2 "Data and universes", section 3 "Strategy and methodology" (3.1 rule, 3.2 shared machinery, 3.3 attribution protocols), section 6 "Limitations", Appendix A source code and Appendix B replication instructions were read in full, and a whole-document word scan of the extracted 38,879-character text returned **zero** occurrences of: `transaction cost`, `fee`, `fees`, `commission`, `slippage`, `bid-ask`, `spread`, `latency`, `fill`, `fills`, `market impact`, `maker`, `taker`, `limit order`, `market order`, `execution`, `order book`, `premium`, `leverage`, `stop`. The words that do appear are all in non-modelling roles: `cost` 2 + `costs` 2, both times as "the backtest engine, cost model and validation protocols are identical to the companion paper" / "costs of 5 bps per unit of gross turnover" / "Costs remain 5 bps on turnover" / "the engine, cost model and walk-forward loop are listed in the companion paper's appendix"; `bps` 2 (the same 5 bps rule); `turnover` 6 (the 5 bps base, Table 2's two turnover cells 0.091 / 0.215, the "2.4 times the turnover" comparison and "average daily turnover 0.09"); `impact`, `borrow` and `capacity` 1 each, all inside the single section 6 sentence "Costs remain 5 bps on turnover with no borrow, impact, or capacity modelling"; `margin` 1, inside the idiom "passed, with margin" (section 7), not a margin model; `stops` 1, inside "stops short of formal factor attribution" (section 6).

Consequences, recorded as `data gap` and **never** as zero: order type, signal-to-order delay, same-bar vs next-bar fills, partial fills, commission and exchange fees, bid-ask spread, slippage, market impact, participation/capacity, leverage, margin, borrow (irrelevant to the long-only leg but relevant to the quoted long-short rows), latency, turnover units and definition, and cash yield. The **5 bps per unit of gross turnover** charge is the paper's entire friction model, and its mechanics (per-side vs round-turn, turnover denominator, application ordering relative to the one-day signal lag) are `underspecified` because they live in the companion paper's appendix.

**Research-proposed evaluation protocol (ours, not the source's):** signal computed on adjusted close at rebalance day `t`, orders submitted at the next session's open (`t+1`, consistent with the source's one-day lag), taker on the qualifying buys, fixed `1/n_hold` target weights with integer-share rounding at $100,000 notional per book, cash at the risk-free rate, and a friction ladder of 0/1/2/5/10/20 bps per unit of gross turnover **plus** an explicit per-share commission and a half-spread model. Every element of that paragraph is `research-proposed`.

## Evidence

### Source-reported

Every figure below is `source-reported`, has not been reproduced by us, and carries Table/Figure/Section provenance from the pinned PDF (SHA-256 `349bacf8...f4eb7`, 20 pages).

- **Table 1 (baseline 100d/5, 26-name universe, 2020-2024, vs SPY buy-and-hold):** total return 184.1% vs 95.3%; CAGR 23.3% vs 14.4%; Sharpe 1.12 vs 0.76; maximum drawdown -23.2% vs -33.8%; annualised volatility 20.6% vs 20.6%; average gross exposure 91.2% vs 100%.
- **Table 2 (in-sample sweep of all 36 cells, 26-name, SPY Sharpe 0.76):** every cell's Sharpe exceeds the index; range 0.89 to 1.43, median 1.20. Best cell 80d/3 names: Sharpe 1.43, CAGR 39.2%, MaxDD -19.9%, ann. vol 25.3%, turnover 0.091. Worst cell 20d/3 names: Sharpe 0.89, CAGR 21.3%, MaxDD -35.7%, ann. vol 25.3%, turnover 0.215. Section 4.2: the 20-day column is uniformly the worst, at identical volatility to the best cell but "barely half the return with 2.4 times the turnover", and it has a deeper drawdown than buy-and-hold.
- **Section 4.3 (60/40 chronological split, 26-name):** training window December 2020 - May 2023 selects 80/3 (train Sharpe 1.52); frozen on the test window it returns Sharpe 1.20, CAGR 31.9%, MaxDD -19.9%; the test-optimal oracle cell is 250/10 at Sharpe 2.16.
- **Table 3 (walk-forward, 26-name, five folds, selected cell and fold Sharpe):** Jun 2022 - Dec 2022 `125/3` -0.69; Dec 2022 - Jun 2023 `200/3` 3.03; Jul 2023 - Dec 2023 `80/3` 0.83; Jan 2024 - Jul 2024 `40/3` 3.26; Jul 2024 - Dec 2024 `40/3` -0.61; stitched block labelled "629 days". Stitched out-of-sample: **Sharpe 1.36, CAGR 34.1%, total +108.0%, MaxDD -18.6%, against SPY 1.30 and 20.8% over the identical span**. Every fold selects `n_hold = 3`, the most concentrated book allowed (section 4.3).
- **Table 4 (performance within full-sample volatility terciles, trend rule at 100d/top-3, full sample):** 26-name - low vol Sharpe 0.60 / CAGR 7.0%, medium 0.84 / 14.3%, high 1.52 / 43.2%; 99-name - low 0.52 / 6.9%, medium 0.71 / 12.4%, high 1.22 / 36.6%; the companion paper's MA long-short in the same buckets: 26-name 0.08 / -0.65 / 0.76, 99-name -0.34 / -0.41 / 0.16; SPY 0.76 / 14.4%.
- **Figure 4 / Figure 5 captions:** 26-name low-volatility tercile = JNJ, KO, PEP, WMT, MRK, MCD, PFE, V (19.7-27.9% vol), high-volatility tercile = XOM, CVX, AMZN, BAC, ADBE, CRM, INTC, META, NVDA (34.2-53.9% vol); the 99-name repeat uses 33 names per tercile and shows the high-volatility bucket's MaxDD at **-38.6%**, "worse than buy-and-hold", against only -23.2% on the 2026-picked list.
- **Table 5 (complete walk-forward with and without NVIDIA, selection loop included):** 26-name with NVDA Sharpe 1.36 / CAGR 34.1%, without NVDA 1.13 / 23.0%; 99-name with NVDA 1.53 / 41.3%, without NVDA 1.05 / 23.2%; SPY 1.30 / 20.8% on the same span. Section 4.5: the CAGR advantage falls from +13.3 and +20.5pp to +2.2 and +2.4pp; ex-NVDA CAGRs are 23.0% (26 names) and 23.2% (99 names); ex-NVDA maximum drawdowns are -19.2% and -16.7% against roughly -24% for the index.
- **Table 6 (walk-forward Sharpe, three strategies x both universes):** MA crossover long-short 0.35 (26) / -0.31 (99); momentum 12-1 long-short 0.22 / 0.18; trend-following directional 1.36 / 1.53; trend-following ex-NVDA 1.13 / 1.05; SPY 1.30. Construction caveat printed with the table: the long-short book was held at 5 names per side on both universes (19% tails on 26 names, 5% on 99) and "a decile-style construction on the broad universe was not tested".
- **Table 7 (master comparison, all 18 scenarios):** 1 in-sample baseline 1.12 / 23.3% / -23.2%; 2 sweep best cell 1.43 / 39.2% / -19.9%; 3 sweep worst cell 0.89 / 21.3% / -35.7%; 4 train/test split 26-name OOS 1.20 / 31.9% / -19.9%; 5 train/test split 99-name OOS 1.36 / 41.3% / -18.1%; 6 walk-forward 26-name 1.36 / 34.1% / -18.6%; 7 walk-forward 99-name 1.53 / 41.3% / -13.4%; 8 walk-forward ex-NVDA 26-name 1.13 / 23.0% / -19.2%; 9 walk-forward ex-NVDA 99-name 1.05 / 23.2% / -16.7%; 10 low-volatility tercile 0.60/0.52, 7.0%/6.9%, -16.9%/-24.4%; 11 medium-volatility tercile 0.84/0.71, 14.3%/12.4%, -24.4%/-25.1%; 12 high-volatility tercile 1.52/1.22, 43.2%/36.6%, -23.2%/-38.6%; 13 MA long-short walk-forward 0.35 / 3.8% / -15.2%; 14 MA long-short walk-forward 99 -0.31 / -5.4% / -33.5%; 15 momentum 12-1 walk-forward 0.22 / 2.1% / -23.3%; 16 momentum 12-1 walk-forward 99 0.18 / 1.7% / -20.9%; 17 SPY buy-and-hold OOS span 1.30 / 20.8% / ~-24%; 18 SPY buy-and-hold full sample 0.76 / 14.4% / -33.8%.
- **Section 4.6:** on the cleaner 99-name universe the with-NVDA result improves (1.53 vs 1.36, CAGR 41.3%, drawdown -13.4%, "no negative folds") because "73 additional 2020-era names gave the selector more high-vol winners to rotate through"; only the exclusion test shows the improvement rests on the same single-name foundation.
- **Cost-relevant printed values (sections 3.2, 6 and Table 2):** 5 bps per unit of gross turnover; average daily turnover 0.09 for the trend rule; Table 2 turnover cells 0.091 (80d/3) and 0.215 (20d/3); risk-free rate fixed at zero for Sharpe ("for a long-only book this flatters slightly more than for a dollar-neutral one", section 3.2).
- **Overall claim (abstract, section 5.2, section 7):** a clean validation protocol "can still bless a lucky strategy"; the durable residual is "market-like returns with maximum drawdowns roughly a third smaller than buy-and-hold" plus a rejected breadth conjecture.

### Independently reproduced

not independently reproduced.

Scout-side provenance and internal-arithmetic checks only (these verify that this record quotes the source consistently; they are **not** an empirical reproduction of the study):

- Landing read in a browser session on 2026-09-28 after the Cloudflare interstitial cleared; pinned PDF re-hashed in-session to SHA-256 `349bacf866834dce805a4f1f42028f4eee1f49d1dc974f1acdfae593927f4eb7` (1,067,814 bytes, 20 pages); all cited headline literals were presence-checked programmatically against the 38,879-character extracted text with whitespace and unicode-minus normalisation.
- `34.1 - 20.8 = 13.3` and `41.3 - 20.8 = 20.5` reproduce section 4.5's "+13.3" and "+20.5"; `23.0 - 20.8 = 2.2` and `23.2 - 20.8 = 2.4` reproduce its "+2.2" and "+2.4"; `34.1` vs the section 1 phrase "fourteen-percentage-point" does **not** reconcile (frontmatter contradiction 1).
- `(1 + 1.841)^(1/4.98) - 1 = 23.2%` reproduces Table 1's 23.3% CAGR to rounding, and `(1 + 0.953)^(1/4.98) - 1 = 14.3%` reproduces SPY's 14.4%; `(1 + 1.080)^(629/252) - 1 = 34.2%` is consistent with the stitched 34.1% CAGR at the printed 629-day span.
- Grid arithmetic: 9 windows x 4 `n_hold` values = 36 cells (section 3.2); `0.215 / 0.091 = 2.36` reproduces section 4.2's "2.4 times the turnover"; `99 - 26 = 73` reproduces section 4.6's "73 additional names".
- Walk-forward arithmetic: 378 trailing days + 126-day blocks from a 2020-01-02 start places the first test block in mid-2022, consistent with Table 3's first fold of Jun 2022 - Dec 2022; five 126-day folds imply 630 trading days against the printed 629 (and section 4.7's "627-629"), i.e. the span is internally near-consistent but printed two ways.
- Word-scan counts (0 for transaction cost / fee / commission / slippage / bid-ask / spread / latency / fill / market impact / maker / taker / order type / execution / order book / premium / leverage / stop; 2+2 for cost/costs; 6 for turnover; 1 each for impact, borrow, capacity) were produced against the pinned text itself, together with a section-level read of sections 2, 3, 6 and Appendices A-B.
- Reference list counted entry by entry: 13 entries, against the landing's "0 References" heading (frontmatter contradiction 6).
- SSRN landing, DOI resolution, license line and paper statistics were read directly; no claim in this record comes from a search-result summary or secondary write-up.

### Negative evidence

1. Removing **one** ticker collapses the headline: walk-forward Sharpe 1.36 -> 1.13 (26-name) and 1.53 -> 1.05 (99-name), both below SPY's 1.30 on the same span (Table 5).
2. The CAGR edge over the index falls from +13.3pp and +20.5pp to +2.2pp and +2.4pp after that single exclusion (Table 5, section 4.5) - "inside the noise band of a two-and-a-half-year window" by the source's own description.
3. The ex-NVDA CAGRs are nearly identical across the two universes (23.0% vs 23.2%), which the source reads as direct evidence that "the excess return was NVIDIA" (section 4.5).
4. Performance is monotone in volatility and lives entirely in the top tercile; in the bottom two terciles - two-thirds of either universe - trend-following **underperforms buy-and-hold** (Table 4: low 7.0%/6.9% and medium 14.3%/12.4% against SPY 14.4%).
5. On the survivorship-corrected universe the high-volatility tercile suffers a **-38.6% maximum drawdown, worse than buy-and-hold**, where the 2026-picked list showed -23.2% (Figure 5, Table 7 row 12) - the clean universe reveals downside the hand-picked list had erased.
6. The source's own worst in-sample cell has a deeper drawdown than the index (-35.7% vs -33.8%, Table 2), so the "every cell beats buy-and-hold" claim is Sharpe-only (frontmatter contradiction 3).
7. The cross-sectional alternatives fail everywhere: MA crossover long-short walk-forward Sharpe 0.35 (26-name) and -0.31 (99-name); 12-1 momentum 0.22 and 0.18 - "Neither long-short signal has an out-of-sample edge at either universe size" (Table 6, section 4.6).
8. The companion paper's breadth conjecture is rejected by the source's own negative control: quadrupling the universe does not rescue momentum and pushes the MA long-short negative (Table 6).
9. The benchmark gap is statistically thin by the source's own words: "1.36 versus 1.30 over two and a half years is statistically indistinguishable" (section 4.3).
10. Fold dispersion is enormous (-0.69 to +3.26) with two of five folds negative (Table 3), so every stitched number carries wide error bands (section 6).
11. The walk-forward persistently selects `n_hold = 3`, the maximum concentration available, in every fold (section 4.3) - a selection behaviour the source flags as foreshadowing the attribution result.
12. A 36-for-36 in-sample sweep on a post-sample-selected universe is explicitly called "a red flag, not a robustness certificate" by the source (section 4.2).
13. The primary universe is a textbook survivorship defect: 26 names "hand-picked in 2026, i.e. after the sample", conspicuously including NVIDIA (section 2.2).
14. The "fixed" universe still retains survivorship: mid-sample delistings (Allergan, Raytheon/United Technologies) are excluded because the vendor does not serve delisted tickers, and membership is reconstructed from public sources rather than a licensed point-in-time file (section 2.2).
15. The volatility terciles use **full-sample** volatility, i.e. mild look-ahead, acknowledged as "diagnostic only" - the tercile result is therefore a location diagnostic, not a tradable sort (section 3.3, section 6).
16. Cost treatment is a single flat 5 bps per unit of gross turnover with "no borrow, impact, or capacity modelling"; there is no fee, spread, slippage, order-type or fill model anywhere in the paper (section 6 plus whole-document word scan) - the source itself calls the treatment "generous to all strategies".
17. The cost model itself is not in this paper: "The engine, cost model and walk-forward loop are listed in the companion paper's appendix" (Appendix A), and the companion is cited without an SSRN identifier, so turnover definition, cost ordering and execution conventions are `underspecified`/`data gap`.
18. No sizing, leverage, margin, capacity or cash-yield model exists; Sharpe uses a zero risk-free rate, which the source concedes flatters a long-only book (section 3.2).
19. The annualisation convention behind every Sharpe in the paper is never stated (`data gap`).
20. The default-configuration turnover is never printed (Table 2 prints only the 80d/3 and 20d/3 cells plus section 6's "average daily turnover 0.09"), and the units of the Table 2 turnover column are not defined (`underspecified`).
21. Single five-year window containing "exactly one regime cycle" and, by the source's own argument, exactly one historic outlier episode; section 5.2 states the bigger claim would require "a stationary supply of NVIDIAs", of which the sample contains one draw.
22. Small, partially disclosed universes: 26 names of which only 17 are printed, and 99 names of which the abridged Appendix A.4 list accounts for 98 - neither panel is reconstructable from the paper alone.
23. The long-short comparison is held at 5 names per side on both universes (19% tails vs 5% tails), a construction caveat the source prints itself; a decile-style construction on the broad universe was never tested (Table 6).
24. No formal factor attribution is performed: "regressing the strategy's returns on market, size, momentum and volatility factors would quantify what the sorts only locate" (section 6) - so it remains open whether the rule is simply long high-volatility beta.
25. The attribution toolkit is "deliberately elementary"; the top-k exclusion curve (k = 1, 2, 3, ...) that would map the concentration profile is "left for the replication package", which is not public (section 6, Appendix A/B).
26. No public code or data artifact: no repository URL anywhere in the pinned text, and Appendix B requires private Alpaca API keys - independent reproduction requires rebuilding both the engine and the universe lists from scratch.
27. No AI-use, funding or competing-interest disclosure sections exist in the pinned text (`data gap`), and the SSRN landing shows 0 Citations, a "0 References" heading and 114 downloads / 287 abstract views at read time - treat all figures as unreviewed third-party claims by a sole unaffiliated author.
28. Two printed values look duplicated across distinct specifications without explanation: Table 7 row 5 (train/test split, 99-name) prints CAGR 41.3% identical to row 7 (walk-forward, 99-name) while its Sharpe differs (1.36 vs 1.53), and Table 7 row 12 (26-name high-volatility tercile) prints MaxDD -23.2% identical to the full-universe baseline MaxDD in Table 1; neither coincidence is reconciled in the text.
29. Related negative literature already in this repository points the same way: `published-equity-anomaly-zoo-large-cap-post-2005-luck-adjusted-null-arxiv-2607.06502-2026-09-23` reports a luck-adjusted near-null for published anomalies in investable US large caps post-2005, and `long-only-us-equity-ath-trend-following-vol-sizing-atr-ratchet-turnover-control-ssrn-5084316-2026-09-27` documents small-account cost collapse and a withheld turnover-control mechanism in the nearest long-only US equity trend construction - both are direct cautionary context for a 2020-2024 single-cycle backtest.

## Falsification plan

All thresholds below are `research-defined falsification thresholds` (Scout-chosen, not the source's), and all operational rules not printed in the source are `research-proposed`.

- **F1 - Baseline reproduction gate (`research-defined`).** Rebuild the 26-name and 99-name panels from Alpaca (or an equivalent split/dividend-adjusted daily source) and reproduce Table 1 and Table 3. Fail if the baseline 100d/5 Sharpe is outside 1.12 +/- 0.10, the CAGR outside 23.3% +/- 2.0pp, or the stitched walk-forward Sharpe outside 1.36 +/- 0.10; failure action: classify the source as non-reproducible and drop every downstream claim.
- **F2 - Fold-selection reproduction gate (`research-defined`).** Re-run the walk-forward (378-day training window, 126-day test blocks, 36-cell grid). Fail if the five selected cells are not `{125/3, 200/3, 80/3, 40/3, 40/3}` or if two or more folds are negative; failure action: treat the stitched 1.36 as protocol-dependent rather than a property of the rule.
- **F3 - Single-name concentration curve (`research-defined`).** Produce the top-k exclusion curve (k = 1, 2, 3, 5, 10, by full-sample contribution) on both universes with the selection loop re-run each time. Fail the **alpha** claim if excluding any 1 to 3 names drops the walk-forward Sharpe below SPY's 1.30 or cuts the CAGR edge below +5.0pp; failure action: record the strategy as a single-name bet and retain only the risk claim.
- **F4 - Frozen forward test (`research-defined`).** Freeze the rule (window, `n_hold`, sizing, 5-day rebalance) on 2024-12-30 and evaluate 2025-01-01 through 2026-12-31 out of sample on a point-in-time universe. Fail if the forward walk-forward Sharpe is <= the S&P 500's Sharpe over the same span, or if the forward CAGR edge is <= 0, or if any single stock contributes more than 50% of the gross excess return.
- **F5 - Cost ladder (`research-defined`).** Apply 0/1/2/5/10/20 bps per unit of gross turnover **plus** an explicit commission and half-spread model (both `research-proposed`). Fail the return claim if the CAGR edge over the index vanishes at 5 bps, and fail the risk claim if the maximum-drawdown advantage over the index shrinks by more than half at 10 bps.
- **F6 - Volatility-tercile replication (`research-defined`).** Re-run the tercile split on trailing (point-in-time) 252-day volatility instead of full-sample volatility. Fail the source's attribution if the low/medium/high ordering of excess return is not monotone on both universes; fail the universal-trend reading if low and medium terciles still underperform buy-and-hold.
- **F7 - "Stationary supply of NVIDIAs" test (`research-defined`).** Define an ex-ante rule (trailing 252-day volatility in the top tercile **and** trailing 126-day return in the top quartile) that would have selected high-volatility uptrend winners using only information available at each rebalance, then run the strategy restricted to that ex-ante cohort. Fail the mechanism claim if the ex-ante cohort version shows no positive CAGR edge over the index across both universes; this directly tests the source's stated precondition in section 5.2.
- **F8 - Universe-replacement sensitivity (`research-defined`).** Repeat the walk-forward on at least three independently reconstructed start-of-sample universes (S&P 100 Jan 2020, S&P 500 Jan 2020, top-99 by start-of-sample dollar volume). Fail the generalisation claim if a positive CAGR edge appears only in universes that contain NVIDIA, or if two of three universes produce a Sharpe below the index.
- **F9 - Survivorship / look-ahead audit (`research-defined`).** Rebuild the panels with point-in-time constituents **including** mid-sample delistings (Allergan, Raytheon/UTC and their analogues) and with adjusted prices re-derived from raw splits. Fail if the CAGR edge falls by more than 50% relative to the printed values, i.e. if universe hygiene rather than the rule explains the residual.
- **F10 - Multiplicity control (`research-defined`).** Count the full searched family the source actually ran (36 grid cells x 2 universes x 2 validation protocols x 3 terciles x 1 single-name exclusion x 2 long-short baselines) and apply Benjamini-Hochberg at q < 0.10. Fail if the walk-forward edge does not survive as a selection-adjusted result.
- **F11 - Baseline hurdle set (`research-defined`).** Compare against SPY, an equal-weight panel, 12-1 momentum, the companion's MA crossover, and a 200-day-timing buy-and-hold (the Faber-style cash-retreat benchmark the source cites). Fail the trend rule's incremental claim if it does not beat the 200-day-timing benchmark on a return-to-maximum-drawdown ratio; success there but not on raw Sharpe means the rule is a drawdown wrapper, not alpha.
- **F12 - Drawdown-reduction residual gate (`research-defined`).** The source's surviving claim is a mechanical one. Fail it if, across all three universes/specifications, the ex-NVDA maximum drawdown is not at least 30% smaller than buy-and-hold's on the same span, or if the cash-retreat book is in cash in fewer than 5% of sessions through broad selloffs (i.e. the throttle never fired).
- **F13 - Selection-adjusted inference (`research-defined`).** Compute the deflated Sharpe ratio (Bailey and Lopez de Prado, cited by the source) and a Hansen SPA across the 36-cell grid and both universes, with fold-level block bootstrap over the 629-day stitched span. Fail if the selection-adjusted Sharpe is not distinguishable from SPY's 1.30, i.e. if the reported 1.36/1.53 advantage is inside the noise band the source already concedes.
- **F14 - Implementation and capacity gate (`research-proposed` rule, `research-defined` thresholds).** Execute the rule at next session's open with a one-day signal lag, integer shares, and books of $1M / $10M / $100M with a square-root impact term and a 10% ADV participation cap. Fail if the net CAGR edge over the index is <= 0 at $10M AUM, or if the drawdown advantage at $100M is less than half the published advantage.

## Crypto portability

`unproven` - the source holds **zero** crypto evidence: all results are US listed cash equities on a 2020-2024 daily panel with a US-index benchmark, and neither the strategy nor any attribution layer is evaluated on crypto.

Porting would be a hypothesis, not a replication, and the specific obstacles are structural:

- **Session structure:** the 5-day rebalance cadence and the notion of a "trading day" are exchange-calendar artifacts; crypto trades 24/7, so the rebalance clock, the daily-bar SMA and the 126/378-day walk-forward grid all need re-definition (`research-proposed`: 8-hour or daily UTC bars, 5-day = 120-hour rebalance).
- **Cash retreat:** the throttle parks exposure in a non-yielding cash balance on equities; in crypto the equivalent is a stablecoin or an off-exchange balance, which introduces issuer/venue risk the source never models, and "cash" during a crash is exactly when stablecoin and venue risk peaks.
- **Universe construction:** there is no S&P-100-analogue point-in-time file for crypto; listing history, delistings, hard forks, rebrands and stablecoin quoting conventions make the survivorship problem *worse*, not better, so F8/F9 would be mandatory before any crypto claim.
- **Volatility-tercile finding:** the source's core attribution (edge lives in the highest-volatility tercile) transfers poorly because crypto cross-sectional volatility is far higher and more regime-dependent, and single-name concentration risk maps to single-asset concentration (BTC/ETH dominance) rather than to an equity outlier.
- **Costs and execution:** 5 bps per unit of gross turnover ignores crypto maker/taker schedules, funding on any hedged leg, liquidation mechanics on leveraged books, and venue fragmentation; none of these exist in the source.

Crypto portability is therefore `unproven` and is not authorization to trade anything.

## Limitations

- `underspecified`: price field behind `P/SMA_n`, rebalance-date origin beyond the Appendix A code, tie handling, turnover units and default-configuration turnover, cost application ordering (per-side vs round-turn), Sharpe annualisation convention, timezone/session definition, and the full 26-name and 99-name ticker lists.
- `data gap`: every order-type, spread, fee, slippage, impact, participation, capacity, leverage, margin, borrow, latency and cash-yield field; the companion paper that carries the engine and cost model (no SSRN identifier printed); code and data availability (no repository URL); AI/funding/conflict disclosures; contact information behind the landing's collapsed control.
- `not independently reproduced`: every performance, attribution and fold-level figure in this record - we verified provenance, hashes and internal arithmetic only.
- `unproven`: the mechanism claim itself. The paper's verdict is negative on the return component and modest on the risk component, and neither has been tested outside one five-year window.
- Sample: 1,257 trading days (2020-01-02 to 2024-12-30), one regime cycle, two small universes (26 and 99 names) neither fully disclosed, one benchmark (SPY), and a single historic outlier episode.
- Selection: 36 grid cells searched in-sample, protocol choice shared with a companion paper that reported the failures, and attribution layers chosen by the author (though declared fixed before inspection); no pre-registration, no untouched hold-out after 2024.
- Identification: no factor regression, so high-volatility beta, idiosyncratic-volatility exposure and momentum-crash exposure are not separated from the trend mechanism (section 6).
- Source quality: sole author, affiliation "Independent", SSRN working paper, 0 Citations, 0 References heading, 114 downloads at read time, no peer review, no public code, and a companion paper that cannot be located from this source's own reference list.
- Internal consistency: six unreconciled contradictions are recorded in the frontmatter, including a headline CAGR gap stated two ways and a universal drawdown claim that two printed cells violate.
- Publication-bias concern: this is a deliberately skeptical paper, so the usual "only positive results get posted" bias runs the other way - but its **positive** headline (the passing walk-forward) is exactly the kind of result that gets quoted without the attribution section that follows it.
- This record is research material. It contains no independent validation, no backtest, no implementation and no trading approval.

## Implementation status

`implementation_status: not-implemented`. Nothing in this record has been implemented in our research stack: no panel reconstruction, no signal code, no backtest, no Qlib run, no Paper, Testnet or Live activity, and no Wiki Brain ingestion. The `research-proposed` evaluation protocol above exists only as a falsification specification.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. The presence of this record in the staging repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading. Any later adoption or implementation decision must be explicit, separately reviewed and based on this record plus current sources.

## Related Wiki records

Verified adjacent pages returned by a read-only Wiki Brain search this run (no page was written, and no page is linked that was not returned by the search):

- [[quant/alphatrend-adaptive-exit-generalization-falsification-crypto-perpetual-2026-09-13]]
- [[quant/crypto-perpetual-supertrend-wpr-trend-following-cost-gate-falsification-2026-09-12]]
- [[quant/crypto-trend-atlas-causal-multi-speed-perpetual-portfolio-2026-09-12]]
- [[quant/futures-quad-trend-carry-skew-vov-composite-2026-09-11]]
- [[quant/crypto-walk-forward-window-optimization-double-oos-momentum-2026-09-04]]

The first search of this run (`time-series trend following walk-forward validation drawdown cash retreat`) returned 0 pages; the second (`trend following momentum backtest overfitting`) returned the 8 pages of which the 5 above are the closest. No Wiki Brain page for this specific source identity (SSRN 7073258), for "One Ticker Deep", for Prashant Malan or for the companion paper's title was found; that absence is stated rather than filled with an invented link.

## Sources

- Malan, P. (2026). *One Ticker Deep: The Trend Strategy That Passed Every Test and Still Shouldn't Be Believed*. SSRN Working Paper. Landing: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7073258 (read 2026-09-28; 20 Pages; Date Written 07 Jul 2026; Posted 24 Jul 2026; "Draft: July 2026" on the PDF title block; All rights reserved / no reuse allowed without permission; 0 Citations; 0 References heading; 114 downloads / 287 abstract views at read time).
- DOI: https://dx.doi.org/10.2139/ssrn.7073258
- Pinned PDF retrieved through the landing page's "Open PDF in Browser" delivery link on 2026-09-28 (that delivery link resolves in-session to a temporary time-limited object URL used transiently to fetch the bytes; no presigned or session-bound URL retained): **1,067,814 bytes, 20 pages, SHA-256 `349bacf866834dce805a4f1f42028f4eee1f49d1dc974f1acdfae593927f4eb7`**; text extracted with pypdf 6.16.2 to 38,879 characters and all 20 pages read (sections 1-7, Tables 1-7, Figures 1-8 captions, references, Appendices A-B).
- Companion paper cited by the source but **not** retrievable from this source's reference list (no SSRN identifier printed): Malan, P. (2026). *Do Simple Cross-Sectional Trend Strategies Survive Honest Validation? Evidence from a Small US Large-Cap Universe, 2020-2024*. Working paper, SSRN. Recorded as `underspecified`; none of its numbers are quoted in this record except where this paper's own Tables 6-7 restate them.
- Works cited inside the source that its framing leans on (read as part of the pinned PDF's reference list, not independently consulted): Moskowitz, Ooi and Pedersen (2012); Faber (2007); Jegadeesh and Titman (1993); Brock, Lakonishok and LeBaron (1992); Daniel and Moskowitz (2016); Barroso and Santa-Clara (2015); Harvey, Liu and Zhu (2016); Bailey and Lopez de Prado (2014); Bailey, Borwein, Lopez de Prado and Zhu (2014); Lopez de Prado (2018); Sullivan, Timmermann and White (1999); Shumway (1997).
