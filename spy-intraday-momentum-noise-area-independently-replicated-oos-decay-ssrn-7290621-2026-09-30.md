---
schema: strategy-research-record-v1
title: "Independent out-of-sample replication of the Zarattini/Aziz/Barbon SPY Noise-Area intraday momentum strategy (SSRN 7290621): in-sample Sharpe 1.34 reproduces, out-of-sample Sharpe 0.39 over May 2024 - March 2026"
created: 2026-09-30
updated: 2026-09-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - spy
  - etf
  - intraday-momentum
  - out-of-sample-replication
  - ssrn
status: research-only
confidence: medium
source_as_of: "2026-08-19 (SSRN posting; underlying 1-minute data through 2026-03-31)"
sources:
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7290621"
  - "https://doi.org/10.2139/ssrn.7290621"
  - "https://papers.ssrn.com/sol3/Delivery.cfm/7290621.pdf?abstractid=7290621&mirid=1 (pinned PDF, 696466 bytes, SHA-256 cfc08247491705e34655064b22590c70562ae6daa31d459e16421718fd30c5bb)"
  - "https://github.com/PazSheimy/spy-intraday-momentum-oos (commit 32fd5a31e793fefae4deae0fb65fc2e4585a7b01 on main)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Independent out-of-sample replication of the Zarattini/Aziz/Barbon SPY Noise-Area intraday momentum strategy (SSRN 7290621): in-sample Sharpe 1.34 reproduces, out-of-sample Sharpe 0.39 over May 2024 - March 2026

## Provenance

**Primary source identity (SSRN working paper)**

- **Title exactly as printed on the SSRN landing page and on PDF page 1:** *Out-of-Sample Evaluation of an Intraday Momentum Strategy for the S&P 500 ETF (SPY)* (no title variant on either surface).
- **Author, as rendered on the SSRN landing page (read 2026-09-30):** `Sheimy Paz`, affiliation printed as `University of South Florida`.
- **Author, as printed in the PDF byline (PDF page 1):** `Sheimy Paz Serpa` with email `sheimypazserpa@gmail.com` and the line `First Version: June 2026`; **no affiliation is printed in the PDF**, and the PDF carries no `University of South Florida` string. The repository BibTeX entry also renders the author as `Paz Serpa, Sheimy`. **Unreconciled:** the landing page name/affiliation, the PDF byline and the repository citation differ in name form and affiliation; recorded as printed, not resolved, and it does not affect any claim in the record.
- **Dates (SSRN landing, read 2026-09-30):** `12 Pages Posted: 19 Aug 2026`; `Date Written: June 02, 2026`; the "Suggested Citation" block prints `Paz, Sheimy, Out-of-Sample Evaluation of an Intraday Momentum Strategy for the S&P 500 ETF (SPY) (June 02, 2026)`. The PDF prints `First Version: June 2026`. PDF metadata `/CreationDate` and `/ModDate` are both `D:20260815185509Z`.
- **Stable identifiers:** SSRN abstract id `7290621`; DOI `10.2139/ssrn.7290621`; landing `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7290621`; short form `https://ssrn.com/abstract=7290621`.
- **Publication status:** SSRN working paper. The landing page prints **no journal reference, no publisher DOI other than the SSRN DOI, and no peer-review statement** -> publication status beyond "SSRN working paper" is `not stated in source`; peer review is **not** claimed. Landing categories: `Capital Markets: Asset Pricing & Valuation` and `Capital Markets: Market Efficiency`. PDF prints `JEL Classification: G11, G12, G14`.
- **License (landing, "License Information"):** `This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License.` The record therefore cites and normalizes short printed values and section references only and does not redistribute the paper text.
- **Declarations (landing):** Declaration of Interest - no competing financial or personal interests; Ethics Approval - not applicable (aggregate market price data only); Funder Statement - no external funding. Landing statistics at read time: `251` downloads, `431` abstract views, `0 References`, `0 Citations`.
- **Surface discrepancy recorded, not a claim contradiction:** the SSRN metadata block prints `0 References` while the pinned PDF's reference list contains **8** entries (Baltussen et al. 2021; Gao et al. 2018; Jegadeesh & Titman 1993; Lo 2002; Rosa 2022; Zarattini & Aziz 2023; Zarattini & Aziz 2024; Zarattini, Aziz & Barbon 2025). This is a landing-metadata vs document discrepancy, so `contested: false` and `contradictions: []` are retained - no statement inside the source contradicts another statement inside the source.

**Pinned primary surfaces actually read**

- **Pinned primary PDF:** `https://papers.ssrn.com/sol3/Delivery.cfm/7290621.pdf?abstractid=7290621&mirid=1`, fetched **2026-09-30**, **696,466 bytes**, **SHA-256 `cfc08247491705e34655064b22590c70562ae6daa31d459e16421718fd30c5bb`**, PDF `/Producer` `pdfTeX-1.40.25` / `/Creator` `LaTeX with hyperref` / empty `/Author`, `/Title`, `/Keywords`, **12 pages**, `pypdf 6.16.2` extraction of **18,435 characters / 342 lines**, read **end to end**: title page, Abstract, Keywords, JEL, Sections 1-6, Equations (1)-(3), Tables 1-4, Figure 1-3 captions and in-caption values, the full 8-item reference list, and Appendix A (`Data and Code Availability`). SSRN serves this file behind a Cloudflare challenge: plain `curl` returned HTTP 403 on the landing page and on all `Delivery.cfm` forms, so the file was retrieved **through a real browser session on 2026-09-30** and byte-verified by SHA-256 after decoding.
- **Pinned primary landing page:** `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7290621`, read **2026-09-30** through the same browser session (the initial `curl` fetch returned HTTP 403 with a Cloudflare interstitial). Source for the author rendering, page count, posted/written dates, abstract wording, keywords, license, the three declaration blocks, the suggested citation and the download/view counters.
- **Repository copy of the paper:** the GitHub tree at the pinned commit contains `paper/Out-of-Sample_Intraday_Momentum_SPY_PazSerpa_2026.pdf` at **666,127 bytes**, which does **not** match the SSRN-served 696,466 bytes. The repository copy was **not** downloaded, so no cross-surface comparison of the two PDF renders was performed - `data gap`; all quotations in this record come from the SSRN-served pinned PDF only.
- **Fidelity verification:** a separate script (`spy_fidelity.py`) re-checks **162 quoted fragments and printed literals** against the pinned PDF text, the pinned landing-page text, the three pinned repository files and the pinned GitHub commit object; prose quotes are matched after whitespace/hyphen normalization while sign-sensitive numeric literals are matched as **exact raw substrings**, so a stripped minus sign cannot hide a sign error. It exits **0** with **0 mismatches**. Nothing from the repository was executed.

**Pinned companion code (read-only, never executed)**

- **Repository:** `https://github.com/PazSheimy/spy-intraday-momentum-oos`.
- **Immutable commit:** `32fd5a31e793fefae4deae0fb65fc2e4585a7b01` on `main`, verified two ways on 2026-09-30: `git ls-remote` returned that same SHA for both `HEAD` and `refs/heads/main`, and the GitHub API commit endpoint returned it with parent `0a59426a4290afbb1b17d4a931224241dbdb528e`, commit message `Rename paper files to match title; update README references`, author and committer both `sheimy <sheimypazserpa@gmail.com>` dated `2026-08-15T19:44:43Z`.
- **Repository metadata (GitHub API, 2026-09-30):** public, not archived, `default_branch: main`, language `Python`, `created_at 2026-08-15T17:47:19Z`, `pushed_at 2026-08-15T19:44:32Z`, size 1082 KB, **MIT License**, 1 star, 1 fork, 0 open issues, no topics, no homepage. The repository README states the paper text and figures in `paper/` are (c) 2026 Sheimy Paz Serpa, all rights reserved, while the code is MIT.
- **Tree at that commit:** `git trees` API call `recursive=1` returned `truncated: false` with **20 entries**: `.gitignore` (439 B), `INIT_AND_PUSH.md` (1,383 B), `LICENSE` (1,073 B), `README.md` (6,658 B), `data/README.md` (1,946 B), `data/raw/SPY/SAMPLE_SPY_1min.csv` (313 B), `paper/Out-of-Sample_Intraday_Momentum_SPY_PazSerpa_2026.pdf` (666,127 B), `paper/Out-of-Sample_Intraday_Momentum_SPY_PazSerpa_2026.tex` (26,859 B), `requirements.txt` (40 B), `results/zarattini_drawdowns.png` (147,583 B), `results/zarattini_oos_equity.png` (166,377 B), `results/zarattini_rolling_sharpe.png` (145,936 B), `src/zarattini_intraday_momentum.py` (17,008 B), `src/zarattini_paper_analysis.py` (12,377 B).
- **Files pinned by raw fetch at that exact SHA, byte counts matching the GitHub tree exactly:** `README.md` = 6,658 bytes, **SHA-256 `43f9dcddfb0ebe75c4538396059ff9ac573270636febe08fad0d3b497ace2475`**; `src/zarattini_intraday_momentum.py` = 17,008 bytes, **SHA-256 `778df2ebdd5e863dfac09c8fa9b078619b07be17118b24391845d7436097129b`**; `data/README.md` = 1,946 bytes, **SHA-256 `5d7ebd7a699f33bbc32ce86d5937d9fb49a4758050f38397746e3350bafb0d66`**. All three were read in full. **No repository code was executed** in this run (no Python from the repository was run, no data were downloaded, no environment was created).
- **Code URL as printed in the source:** the PDF's Appendix A prints the repository URL with a non-TLS `http` scheme; the record normalizes it to `https` while keeping the identical path `github.com/PazSheimy/spy-intraday-momentum-oos`.

**Source-reported data window (from the pinned PDF, Section 2 and Appendix A)**

- 1-minute OHLCV bars for **SPY** sourced from **IQFeed (DTN)**, **2 January 2015 - 31 March 2026**, **1,101,234 intraday bars** across **2,827 trading days**, filtered to regular market hours **09:30-15:59 Eastern Time**.
- **In-sample (IS):** 2 January 2015 - 30 April 2024, **2,333 trading days**. **Out-of-sample (OOS):** 1 May 2024 - 31 March 2026, **480 trading days**. The source states the OOS start date "corresponds to the end of the original paper's data period".
- Dividends are **not** adjusted; the source states SPY dividends are "approximately 1.3% annually relative to SPY's price level during our sample period" and that the original implementation includes a dividend adjustment for the previous-day close used in the Noise Area calculation.
- The 1-minute IQFeed data is licensed and **not redistributed**; `data/README.md` at the pinned commit documents the required CSV schema (`timestamp, open, high, low, close, volume`, US Eastern timestamps) and names IQFeed, Polygon, Databento, Alpaca and Interactive Brokers as acceptable equivalent sources, warning that vendor bar-construction differences produce small deviations from the published numbers.

**Repository-wide source-identity deduplication (deterministic, performed before writing)**

- Hidden-inclusive `rg -uuu` across the **whole checkout** (`.git`, `.mimo-worktrees`, `.agents`, `.hermes`, all root `*.md`, `coverage_manifest.csv`, `*.json`, `*.txt`) for each of `7290621`, `10.2139/ssrn.7290621`, `Sheimy`, `Paz Serpa`, `PazSheimy`, `spy-intraday-momentum-oos`, and the exact title substring `Out-of-Sample Evaluation of an Intraday Momentum` -> **exit 1, zero matching files**.
- Positive control in the same session: `rg -uuu -l "novy-marx"` -> **41 files**, proving the scan was live and non-empty.
- `git pull origin main` was run at the start of this run and again immediately before writing: both returned `Already up to date` with `origin/main` at `86aef06`; `git log --oneline -20` was used as a **convenience glance only** and does not by itself satisfy the dedup contract.
- `coverage_manifest.csv` (5,808 lines, 1,088,787 bytes, present in this checkout) contained **zero** hits for every pattern above.
- **Material distinction against the nearest existing records (five axes stated):**
  1. `spy-intraday-momentum-noise-area-band-vwap-stop-dynamic-sizing-2026-09-23.md` - **different source identity** (SSRN `4824172`, Zarattini/Aziz/Barbon) and a different object: that record captures the **original strategy specification and its in-sample claims**, whereas this record captures an **independent replication plus a pre-declared out-of-sample decay test** by a different author on independent vendor data; the mechanism axis (persistence vs decay), the evidence class (OOS falsification with formal tests vs original backtest), the material data dependency (independent IQFeed 1-minute history with its own IS/OOS split) and the horizon/regime (1 May 2024 - 31 March 2026, a window the original never evaluates) all differ. The original strategy rule itself is **not** re-claimed here as new: the record explicitly attributes every rule to Zarattini et al. (2025).
  2. `opening-range-breakout-pre-registered-225-cell-futures-cost-falsification-2026-09-27.md` - different source, different instrument class (index/metal/energy futures), different signal (opening-range breakout grid) and a pre-registered 225-cell cost falsification rather than a temporal OOS replication.
  3. `spy-nbbo-lag-resolved-push-response-conditional-anomaly-2026-09-24.md` - same ticker but a descriptive event-time conditional-moment study of consolidated quotes with **no performance numbers**, versus a rule-based backtest with formal IS/OOS tests.
  4. `ensemble-donchian-trend-following-crypto-top20-rotational-2026-09-20.md` and `long-only-us-equity-ath-trend-following-vol-sizing-atr-ratchet-turnover-control-ssrn-5084316-2026-09-27.md` - share the Zarattini author line but are different SSRN sources, different asset classes (crypto top-20 rotation; long-only US equity all-time-high trend) and different horizons (daily/weekly, not half-hourly intraday).
  5. `us-equity-momentum-rebalance-timing-luck-tranching-cost-aware-ssrn-5747964-2026-09-27.md` - shares the `4824172` citation only as upstream prior art; its own source and mechanism (rebalance-timing luck / tranching) are unrelated to a 1-minute intraday band-breach rule.
- **Incremental-write check:** under the v1 spec's incremental-write threshold this capture qualifies on **"new falsification or negative evidence"** and **"new execution/cost evidence"** for a strategy family already staged in this repository, not on a new signal family.

**Wiki Brain resolution (read-only, no write)**

- `kb_read("quant/strategy-research-record-spec-v2.md")` -> `Error executing tool kb_read: [Errno 2] No such file or directory`, so the run **failed closed onto the canonical v1 specification**: `quant/strategy-research-record-spec-v1.md`, **10,289 bytes**, **SHA-256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`**, read in full and used for `schema: strategy-research-record-v1`, the required section order and the adoption-boundary wording.
- `kb_search("intraday momentum SPY Noise Area VWAP trailing stop")` -> **0 results** (no page asserted from it).
- `kb_search("out-of-sample decay replication strategy persistence falsification")` -> **8 results**, of which only `quant/llm-news-enhanced-cross-sectional-momentum-tilt` is asserted below (verified by a direct `kb_read`, 21,058 bytes, SHA-256 `1c026ccfbe8603cf6d2354823f996864ae72540a34b175d539901378f16aeb59`); the other seven cover unrelated mechanisms and are not linked.
- **No page was written to Wiki Brain**, no Kanban task was created, no backtest was run, no market data were downloaded, and no dependency was installed.

## Economic mechanism

### Source-reported

The strategy rule itself is attributed by this source to Zarattini, Aziz & Barbon (2025); the PDF states in Section 3 that "The following restates their method for completeness; the strategy specification is entirely theirs. All parameter choices, signal rules, and risk-management components originate from the original paper."

- **Original rationale as restated (Section 1):** the strategy "identifies demand/supply imbalances using a time-varying 'Noise Area' derived from recent price action. When the market moves outside this equilibrium zone, the strategy initiates trend-following positions with dynamic trailing stops incorporating the Volume Weighted Average Price (VWAP). Combined with volatility-targeting position sizing", the original authors "report a total return of 1,985% from 2007 to 2024, with a Sharpe Ratio of 1.33 and near-zero correlation with the broader market." (These original-paper figures are **quoted by this source**; SSRN `4824172` was not opened by this run, so they are one further remove from primary - see `## Sources`.)
- **This source's own thesis (Sections 1 and 5):** the original results "are evaluated exclusively in-sample", and its parameters ("the 14-day lookback for the Noise Area, the 30-minute trade frequency, the VWAP-based trailing stops, and the 2% volatility target") "are all fixed choices that, while not formally optimized, were presumably selected because they produced favorable results on the historical data. Without out-of-sample validation, it is impossible to distinguish genuine market inefficiency from favorable parameter selection."
- **Candidate explanations the source offers for OOS degradation (Section 5.1), all labelled by the source as potential rather than tested:** (a) **market microstructure change** - "the explosive growth of 0-DTE (zero days to expiration) options on SPY since 2022 has fundamentally altered intraday price dynamics", with dealer gamma hedging creating "intraday mean-reversion pressure that directly opposes the trend-following logic of the strategy"; the source notes Zarattini et al. acknowledge the mechanism in their Section 4.5 "but do not test for its impact on strategy profitability over time"; (b) **crowding** - "the original paper has received significant attention in the active trading community since its initial publication in 2024", and "marginal profits per trade are small"; (c) **regime dependence** - the strategy "performs best in volatile, trending markets (2018, 2020, 2022) and worst in low-volatility, range-bound or steadily trending markets (2016-2017, 2025)"; (d) **normal variation** - "with only 480 OOS trading days, the evidence against the strategy is suggestive but not conclusive".
- **Prior literature the source invokes:** Jegadeesh & Titman (1993) for momentum; Gao et al. (2018) and Baltussen et al. (2021) for market intraday momentum; **Rosa (2022), which the source says "documents a post-2013 decline in the predictability of intraday momentum, attributing it to market adaptation"**; Lo (2002) for the Sharpe-ratio standard error used in its own test.

### Research interpretation

- **Mechanism class:** intraday time-series continuation (momentum) gated by a volatility-normalized equilibrium band, with a session-VWAP-anchored trend exit and daily volatility-targeted sizing. The hypothesised friction/behaviour channel is an intraday buyer/seller imbalance that persists for tens of minutes once price leaves a recent-equilibrium zone, i.e. slow intraday information absorption plus liquidity-provision re-balancing, not a fundamental risk premium.
- **Component roles (ablation is required before assuming each contributes):**

```text
Regime / band:      Noise Area - per time-of-day 14-day mean of |open -> close| % move,
                    applied as UB = max(Open, PrevClose) x (1 + sigma_bar),
                                  LB = min(Open, PrevClose) x (1 - sigma_bar)
Primary signal:     at the half-hourly decision grid, close > UB AND close > VWAP -> long (+1);
                    close < LB AND close < VWAP -> short (-1); otherwise flat (0)
Exit / confirmation: the inverted condition at the same grid (equivalent, per the source's own
                    Section 3.3 argument, to a trailing stop max(UB, VWAP) for longs and
                    min(LB, VWAP) for shorts); forced flat at the session close
Risk / size:        Shares = AUM / Open x min(0.02 / sigma_hat_14d, 4) - a 2% daily volatility
                    target with a 4x leverage cap; no overnight exposure
```

- **Falsifiable form of the hypothesis this record actually tests:** *H-persistence* - net-of-cost SPY intraday continuation on this half-hourly band-breach rule remains economically positive and statistically distinguishable from zero on data postdating the original sample. The source's own evidence **weakens** H-persistence: the OOS daily mean is not distinguishable from zero (t = 0.542, p = 0.588), the OOS excess over SPY is negative (not significant), and the IS-to-OOS Sharpe drop is significant (z = 17.053, p < 0.001) - while a direct IS-vs-OOS mean comparison does *not* reject equality (Welch t = 1.139, p = 0.255), so the decay evidence is strong on a risk-adjusted basis and weak on a raw-mean basis.
- **Scope note (dedup-critical):** this capture is a **replication-and-decay record**. The signal construction belongs to Zarattini et al. (2025) and is already staged in this repository; the incremental research object is the persistence/decay hypothesis, its formal tests, and the execution/cost specification of the independent replication.

## Signal

Everything in this section is `source-reported` unless explicitly marked `research-proposed` or `code-level` (i.e. read from the pinned repository file `src/zarattini_intraday_momentum.py` at commit `32fd5a31e793fefae4deae0fb65fc2e4585a7b01`, read only, never executed).

- **Formation timestamp / tradability:** evaluated on 1-minute bars restricted to 09:30-15:59 ET. Section 3.2 states decisions occur "At 30-minute intervals (10:00, 10:30, 11:00, ...)". `code-level`: the decision bars are selected by `min_from_open % 30 == 0` where `min_from_open` counts the 09:30 bar as 1, which selects the **09:59, 10:29, 10:59, ...** bars; the exposure vector is then `.shift(1)`, so the resulting position begins on the **10:00, 10:30, 11:00, ...** bars, matching the paper's stated grid. The paper does not describe this bar-alignment detail - `underspecified` in the paper, resolved by the pinned code.
- **Lookback:** Noise Area uses, for each time-of-day, the mean absolute percentage move from the session open to the close at that time over the prior **14 trading days** (Section 3.1). `code-level`: implemented as a per-minute-of-day rolling mean with `window=14, min_periods=13` followed by a one-row (one-day) `shift` within the minute-of-day group, i.e. a 14-day lookback lagged one day. Position sizing uses the **14-day standard deviation of SPY daily returns** (`code-level`: requires `d_idx > 14`, so the first 15 sessions produce no sizing).
- **Long entry:** close **above** the upper boundary **and** above session VWAP at a decision bar -> `+1`.
- **Short entry:** close **below** the lower boundary **and** below session VWAP at a decision bar -> `-1`.
- **Exit:** the inverted condition at a subsequent decision bar, or the session close. `code-level`: exposure is forward-filled but the forward-fill "stops at zeros", each session starts flat, and `np.append(exposure, 0)` forces a closing trade at the last bar, so **no position is ever held overnight**. The source states positions are "held until the next signal change or market close".
- **Holding period:** intraday only; expected holding period is the remainder of the session; overlapping positions are impossible because there is a single instrument and a single net exposure series (`code-level`).
- **Parameters (all fixed, none tuned in this study; `source-reported` unless noted):**

| Parameter | Value | Where stated |
| :--- | :--- | :--- |
| Noise Area lookback | 14 trading days | PDF Section 3.1 |
| Band multiplier | 1.0 (`BAND_MULT = 1.0`) | `code-level` (the PDF writes the band as `(1 +/- sigma_bar)`) |
| Decision frequency | every 30 minutes | PDF Section 3.2; `code-level` `TRADE_FREQ = 30` |
| Volatility target | 2% daily (`TARGET_VOL = 0.02`) | PDF Section 3.4, Eq. (3) |
| Volatility estimator | 14-day standard deviation of SPY daily returns | PDF Section 3.4 |
| Leverage cap | 4x capital | PDF Section 3.4 |
| Starting AUM | 100,000 | `code-level` `AUM_0 = 100_000.0` |
| Commission | USD 0.0035 per share | PDF Section 3.5 |
| Slippage | USD 0.001 per share | PDF Section 3.5 |
| Per-order commission floor | USD 0.35 (`MIN_COMM_ORDER`) | `code-level` only - not in the PDF |
| OOS boundary | 2024-05-01 (`OOS_START`) | PDF Section 2; `code-level` |

- **VWAP convention:** the PDF does **not** state how VWAP is computed - `underspecified` in the paper. `code-level`: cumulative `volume * (high + low + close) / 3` divided by cumulative `volume`, computed **within each session** (typical-price VWAP).
- **NaN handling in sizing:** `code-level`, if the 14-day volatility input is `NaN` or zero the code sizes to the **full 4x cap** rather than staying flat. This fallback is not described in the paper - `underspecified` in the paper, `code-level` in the pinned file.
- **Reconstruction status:** the rule is **reconstructable** from the PDF Section 3 plus the pinned `code-level` details above. Residual `underspecified` items are: the VWAP price convention, the decision-bar alignment, the NaN-volatility fallback, the per-order commission floor, and whether the original's dividend adjustment should be applied to the Noise Area previous close (this replication omits it).

## Required data

- **Instrument:** SPY - SPDR S&P 500 ETF Trust, cash ETF, quoted in USD (`source-reported`). Price-only accounting: **dividends are not adjusted** (`source-reported`, ~1.3%/yr omitted).
- **Universe:** a **single instrument**; there is no cross-section, no screening, no reconstitution and therefore no survivorship dimension (`source-reported`).
- **Venue / market type:** US listed ETF, spot cash market, regular session only; no futures, no options, no perpetuals (`source-reported`).
- **Timeframe:** 1-minute OHLCV bars, **09:30-15:59 ET** only; `code-level` loader concatenates all CSVs in `data/raw/SPY/`, sorts by timestamp, then filters on `time >= 09:30 and time <= 15:59`.
- **Fields used:** `timestamp, open, high, low, close, volume`. Derived: per-session typical-price VWAP (cumulative), absolute open-to-close percentage move per minute-of-day, session close-to-close daily returns, 14-day rolling standard deviation of those returns, previous session close, session open.
- **Point-in-time / availability:** every input is trailing - prior-14-day averages, previous close, session open, and a session-to-date VWAP. No fundamentals, no announcements, no vendor revisions are involved. The IS/OOS boundary (2024-05-01) is declared by the source as "the end of the original paper's data period", i.e. it is a **chronology-based** split, not a performance-selected one (`source-reported`).
- **Timestamp / timezone:** US Eastern Time, minute precision (`source-reported` and `data/README.md`). Out-of-order, duplicate or missing-bar handling is **not described** in either surface - `data gap`.
- **Missing data / warm-up:** `code-level` skips any session whose Noise Area series is entirely `NaN`, and sizing needs `d_idx > 14`. The paper does not state how many sessions are dropped from the return series. Research-computed: 2,333 (IS) + 480 (OOS) = **2,813** against the stated **2,827** trading days in the dataset, a gap of **14** sessions, which the paper does not explain (the value 14 coincides numerically with the stated 14-day lookback, but the source does not attribute the gap to warm-up - recorded as an unexplained arithmetic gap, not as a cause).
- **Funding / fee / spread needs:** commission and slippage are observed-as-modeled constants (Section 3.5). **Borrow cost on the short leg, financing cost on up-to-4x leverage, quoted spread, market impact, and participation limits are all absent from both surfaces** - `data gap`, never treated as zero.

## Execution assumptions

- **Signal-to-order timing:** `code-level` - the exposure series is shifted by exactly **one 1-minute bar**, so decisions are acted on at the next 1-minute bar close (next-bar execution at 1-minute resolution). The paper does not state the fill timing - `underspecified` in the paper.
- **Order type / fill model:** implicit fill at the 1-minute bar close used for P&L (`code-level`: gross P&L is `sum(exposure * close.diff()) * shares`). No order book, no partial fills, no queue position, no limit-order modelling, no marketable-vs-non-marketable distinction - `data gap`.
- **Fees:** `source-reported` (PDF Section 3.5, the only `Transaction Costs` passage in the document): "We apply a commission of $0.0035 per share and a slippage of $0.001 per share, consistent with the assumptions of Zarattini et al. (2025), based on Interactive Brokers pricing." `code-level`: `total_cost_per_share = 0.0035 + 0.001 = 0.0045`; the daily charge is `trades_count * max(0.35, 0.0045 * shares)`, where `trades_count` counts every exposure change including entries, exits and the forced flat at the close. Research-computed: the USD 0.35 per-order floor binds only when `shares < 77.8` (0.35 / 0.0045), i.e. essentially only for very small accounts, so at the code's USD 100,000 starting AUM the per-share term dominates.
- **Slippage:** a flat per-share allowance, not a spread- or impact-based model - `source-reported`. There is **no bid-ask spread path, no market impact, no participation cap and no latency model** - `data gap`.
- **Spread / impact / capacity:** the pinned PDF contains **zero** occurrences of `spread`, `bid-ask`, `impact` in a market-impact sense (both `impact` hits are "negligible impact on results" and "impact on strategy profitability"), `turnover`, `capacity`, `latency`, `limit order`, `market order`, `fill`, `participation` - so no capacity claim can be made - `data gap`.
- **Leverage / margin / financing:** up to **4x capital** (`source-reported`, "Following mainstream brokerage limits"), with **no financing or margin cost charged** - `data gap`. The single `margin` occurrence in the PDF is the phrase "marginal profits per trade", not a margin requirement.
- **Borrow / shorting:** the strategy takes explicit **short SPY** positions (`source-reported`, signal `-1`), but **no borrow fee, locate requirement or borrow-availability constraint is modelled** - `data gap`.
- **Overnight / funding:** flat by the session close, so no overnight gap, dividend or financing exposure is carried - `code-level` and consistent with the paper's "held until ... market close".
- **Latency / partial fills / failures:** not modelled - `data gap`.
- **Reproduction barrier:** the exact 1-minute IQFeed history is licensed and not redistributed, so an independent party must supply an equivalent vendor feed; the source itself warns vendor bar construction "can produce small deviations from the published numbers" - `source-reported`.

## Evidence

### Source-reported

All figures below are third-party claims read directly from the pinned SSRN PDF (696,466 bytes, SHA-256 `cfc08247...c5bb`) and are **not independently reproduced**. Market/universe for every figure: **SPY cash ETF, 1-minute bars, regular session only, net of USD 0.0035 + USD 0.001 per share**, except the explicitly labelled original-paper column.

**Original-paper column (quoted by this source, one further remove - SSRN 4824172 was not opened this run):** total return `1,985%`, annualized return `19.6%`, annualized volatility `14.3%`, Sharpe `1.33`, hit ratio `43%`, maximum drawdown `25%`, sample `2007-2024` (PDF Table 1, first column). Research-computed: a 1,985% total return (factor 20.85) compounding to 19.6% annually implies **16.97 years**, consistent with the source's own phrase "9.3 vs 17 years".

**Table 1 - In-sample replication vs the original (PDF Section 4.1, Table 1):**

| Metric | Paper (2007-2024) | Replication (2015-2024) |
| :--- | ---: | ---: |
| Total Return (%) | 1,985 | 432.6 |
| Annualized Return (%) | 19.6 | 19.8 |
| Annualized Volatility (%) | 14.3 | 14.3 |
| Sharpe Ratio | 1.33 | 1.34 |
| Hit Ratio (%) | 43 | 44.8 |
| Maximum Drawdown (%) | 25 | 26.2 |

Accompanying text (Section 4.1): "The in-sample daily mean return of 0.076% is highly statistically significant (t = 4.06, p < 0.001)."

**Table 2 - In-sample vs out-of-sample (PDF Section 4.2, Table 2):**

| Metric | IS (2015-2024) | OOS (May 2024-Mar 2026) |
| :--- | ---: | ---: |
| Total Return (%) | 432.6 | 9.4 |
| Annualized Return (%) | 19.8 | 4.8 |
| Annualized Volatility (%) | 14.3 | 14.7 |
| Sharpe Ratio | 1.34 | 0.39 |
| Hit Ratio (%) | 44.8 | 45.0 |
| Max Drawdown (%) | 26.2 | 18.5 |
| Best Day (%) | 9.12 | 9.55 |
| Worst Day (%) | -5.15 | -3.10 |
| SPY Buy & Hold Total (%) | 143.6 | 29.5 |
| SPY Buy & Hold Sharpe | 0.62 | 0.91 |

Accompanying text (Section 4.2): "The OOS daily mean return of 0.023% is not statistically different from zero (t = 0.54, p = 0.59). The strategy does not generate significant alpha over SPY in the OOS period (excess daily return = -0.036%, t = -0.54, p = 0.59). Notably, the hit ratio remains stable at approximately 45% in both periods, and the volatility profile is unchanged (14.3% IS vs 14.7% OOS). The deterioration is entirely in the magnitude of winning trades relative to losing trades, not in the frequency of wins."

**Table 3 - Year-by-year (PDF Section 4.3, Table 3), columns: Year / Strategy % / SPY B&H % / Sharpe / Hit % / Period:**

| Year | Strategy | SPY B&H | Sharpe | Hit | Period |
| :--- | ---: | ---: | ---: | ---: | :--- |
| 2015 | 21.0 | -1.0 | 1.64 | 46.9 | IS |
| 2016 | -13.4 | 9.6 | -0.86 | 34.0 | IS |
| 2017 | -8.8 | 19.4 | -0.73 | 35.1 | IS |
| 2018 | 60.5 | -6.3 | 2.70 | 43.9 | IS |
| 2019 | 8.4 | 28.7 | 0.77 | 42.0 | IS |
| 2020 | 26.2 | 16.1 | 1.60 | 44.7 | IS |
| 2021 | 32.8 | 27.0 | 1.97 | 57.6 | IS |
| 2022 | 23.7 | -19.5 | 1.55 | 45.9 | IS |
| 2023 | 37.8 | 24.3 | 2.56 | 52.5 | IS |
| 2024 | 30.1 | 23.3 | 1.91 | 46.5 | Split |
| 2025 | -2.7 | 16.4 | -0.10 | 44.4 | OOS |
| 2026 | -3.1 | -4.6 | -0.99 | 46.2 | OOS |

The source's own reading: "The yearly data reveals that the OOS underperformance is not unprecedented. The strategy experienced two consecutive negative years during the in-sample period (2016: -13.4%, 2017: -8.8%) ... However, the 2016-2017 drawdown occurred during a period of historically low volatility and strong trending markets."

**Table 4 - Statistical tests (PDF Section 4.4, Table 4):**

| Test | Statistic | p-value | Result |
| :--- | ---: | ---: | :--- |
| IS mean return > 0 | 4.064 | < 0.001 | Significant |
| OOS mean return > 0 | 0.542 | 0.588 | Not significant |
| IS mean != OOS mean (Welch's t) | 1.139 | 0.255 | No significant difference |
| Sharpe IS != Sharpe OOS | 17.053 | < 0.001 | Significant decline |

The source states the Sharpe test uses "the standard error approximation from Lo (2002)" and reconciles the split picture: "While the in-sample mean return is highly significant and the OOS mean return is not, a direct comparison of the two means does not reject equality at conventional significance levels (p = 0.255). This is partly because 480 OOS days provide limited statistical power..."

**Figures (PDF Sections 4.5 and captions):** Figure 1 - rolling 12-month Sharpe stayed above 1.0 for most of mid-2018 to mid-2024 with peaks above 3.0 in 2019 and late 2023, then "declines sharply, turning negative by early 2026"; the caption reads "The strategy's rolling Sharpe declines from above 2.0 to below zero after the OOS boundary." Figure 2 - cumulative equity curve, "Out-of-sample, the strategy underperforms buy-and-hold by approximately 20 percentage points." Figure 3 - drawdown profile, "The OOS period shows a persistent drawdown without the sharp recoveries observed during in-sample drawdowns."

**Data-availability statement (Appendix A):** "All backtests were conducted using Python 3.11 with 1-minute OHLCV data from IQFeed (DTN). The full replication code, including the strategy implementation, statistical tests, and figure-generation scripts, is publicly available" at the GitHub repository named above. "The underlying 1-minute IQFeed data is licensed and therefore not redistributed; the repository documents the required data format so the results can be reproduced with an equivalent 1-minute source."

### Independently reproduced

`not independently reproduced`

Arithmetic-only consistency checks (research-computed from the printed values above; these are **not** a reproduction, no strategy code was run, no market data were obtained): the script `spy_oos_checks.py` exits 0 with **46 checks / 0 mismatches**, covering - annualization identity `432.6%` over `2,333/252` years -> `19.80%` (printed 19.8) and `9.4%` over `480/252` years -> `4.83%` (printed 4.8); Sharpe reconstruction `0.076% x sqrt(252) / 14.3% = 1.34` and `0.023% x sqrt(252) / 14.7% = 0.39`; IS one-sample t `4.062` vs printed `4.064`, OOS one-sample t `0.538` vs printed `0.542`, Welch t `1.136` vs printed `1.139` (all within rounding of the printed 3-decimal means); Lo (2002) standard errors `SE_IS = 0.0285`, `SE_OOS = 0.0473`, `SE_diff = 0.0553` giving `z = 17.19` against the printed `17.053`, with the printed `z` implying a Sharpe difference of `0.9427` rather than the rounded `0.95` (i.e. consistent with unrounded inputs); the implied annualization of the quoted original pair `1,985% / 19.6%` = `16.97` years; day-count identity `2,333 + 480 = 2,813` vs the stated `2,827` (gap `14`, unexplained by the source); bar-per-day identity `1,101,234 / 2,827 = 389.5` against a 390-minute regular session (09:30-15:59); geometric decomposition of the OOS window - `(1.094) / ((1 - 0.027) x (1 - 0.031)) - 1 = +16.0%` implied for May-December 2024 so that **all of the OOS gain is concentrated in 2024 and 2025 + 2026 YTD are both negative**, and the mirrored SPY decomposition `(1.295) / ((1 + 0.164) x (1 - 0.046)) - 1 = +16.6%` for May-December 2024; the 2024 "Split" row decomposition implying Jan-Apr 2024 strategy `+12.1%` and SPY `+5.7%`; gaps and deltas `19.8 - 19.6 = +0.2pp`, `1.34 - 1.33 = +0.01`, `44.8 - 43 = +1.8pp`, `26.2 - 25 = +1.2pp`, `1.34 - 0.39 = -0.95 (-70.9%)`, `29.5 - 9.4 = 20.1pp`, `45.0 - 44.8 = +0.2pp` against the Sharpe collapse (frequency stable, magnitude not); the commission-floor breakpoint `0.35 / 0.0045 = 77.8` shares; and exact re-derivation of every printed Table 1-4 cell from its own row/column labels (row identity, column identity and sample window checked cell by cell so no value is moved across the IS/OOS boundary).

### Negative evidence

Numbered so the count is auditable; `source-reported` unless marked research-computed.

1. **OOS Sharpe collapse:** `1.34` (IS) -> `0.39` (OOS), i.e. `-0.95`, `-70.9%` (research-computed from Table 2).
2. **The collapse is formally significant:** Sharpe IS vs OOS `z = 17.053`, `p < 0.001` (Table 4), using the Lo (2002) standard error.
3. **OOS raw mean is indistinguishable from zero:** daily mean `0.023%`, `t = 0.542`, `p = 0.588` (Table 4 / Section 4.2).
4. **No OOS alpha over the benchmark:** excess daily return vs SPY `-0.036%`, `t = -0.54`, `p = 0.59` (Section 4.2).
5. **OOS badly lags passive:** total return `9.4%` vs SPY buy-and-hold `29.5%`, a `20.1pp` shortfall (Table 2, research-computed gap), while SPY's own OOS Sharpe (`0.91`) is `2.3x` the strategy's (research-computed).
6. **Two consecutive negative OOS periods with no recovery:** 2025 `-2.7%`, 2026 YTD `-3.1%` (Table 3), and the source states the current decline "shows no signs of reversal through March 2026" with rolling 12-month Sharpe negative by early 2026 (Section 4.5).
7. **All of the OOS gain sits in the first eight months:** research-computed geometric decomposition of Table 2 and Table 3 puts May-December 2024 at `+16.0%` for the strategy, leaving 2025 and 2026 YTD net negative - the headline OOS number is propped up by the only OOS months that immediately follow the original sample.
8. **The original evidence is exclusively in-sample:** "These results are compelling, but they are evaluated exclusively in-sample", and the parameters "were presumably selected because they produced favorable results on the historical data" (Section 1) - an explicit selection-bias admission by the replicator about the original study.
9. **Decay is in trade magnitude, not win frequency:** hit ratio `44.8%` -> `45.0%` and volatility `14.3%` -> `14.7%` are flat while the Sharpe collapses (Section 4.2) - the source's own diagnosis that "the deterioration is entirely in the magnitude of winning trades relative to losing trades".
10. **Power caveat that the source itself raises:** the Welch test of means does **not** reject equality (`t = 1.139`, `p = 0.255`), and "with only 480 OOS trading days, the evidence against the strategy is suggestive but not conclusive" / "A definitive assessment may require additional years of OOS data" (Sections 4.4 and 5.1).
11. **Prior literature already documents intraday-momentum decay:** the source cites Rosa (2022) as documenting "a post-2013 decline in the predictability of intraday momentum, attributing it to market adaptation" (Section 1) - this replication is consistent with, not independent of, an existing decay literature.
12. **Analogue decay already occurred inside the sample:** 2016 `-13.4%` and 2017 `-8.8%` are two consecutive in-sample negative years of similar magnitude, so a comparable drawdown history exists even before the OOS window (Table 3) - the source uses this to argue the OOS result might be normal variation.
13. **Regime dependence is admitted:** best in volatile trending markets, worst in "low-volatility, range-bound or steadily trending markets (2016-2017, 2025)" (Section 5.1) - the edge is conditional on a regime the OOS window did not provide.
14. **The 0-DTE mechanism is proposed but untested:** the source explicitly notes the original authors "do not test for its impact on strategy profitability over time" (Section 5.1) - so the leading microstructural explanation for the decay has **no** supporting test in either paper.
15. **The crowding explanation is likewise untested:** it rests on "significant attention in the active trading community since its initial publication in 2024" with no measurement (Section 5.1).
16. **Short-side economics are unmodelled:** the rule shorts SPY but no borrow fee, locate or availability constraint appears anywhere - `data gap`.
17. **Leverage financing is unmodelled:** up to 4x capital with zero financing cost charged - `data gap`.
18. **Spread, impact, participation, turnover, capacity, latency, order type and fill model are all absent** from the pinned PDF (census: `spread` 0, `bid-ask` 0, `turnover` 0, `capacity` 0, `latency` 0, `limit order` 0, `market order` 0, `fill` 0, `participation` 0; `commission` 1 and `slippage` 1, both inside the single Section 3.5 sentence) - `data gap`.
19. **Only a flat per-share friction proxy exists:** USD 0.0035 + USD 0.001 per share with a USD 0.35 per-order floor (`code-level`), i.e. no spread-crossing decision, no impact curve, and a cost model that does not vary with volatility or side.
20. **Dividend omission:** approximately 1.3%/yr of SPY distributions are not adjusted, and the source concedes this "may cause minor discrepancies in the Noise Area calculation around ex-dividend dates"; its "negligible" assessment is the author's own estimate, not a test (Sections 2 and 5.2).
21. **In-sample window is truncated relative to the original:** starts 2015 rather than 2007, "missing the 2007-2014 period that includes the 2008 financial crisis", which the source concedes "could bias our in-sample Sharpe Ratio estimate" (Section 5.2).
22. **OOS window is short:** "approximately two years ... is short by the standards of long-run strategy evaluation" (Section 5.2).
23. **Implementation is not the original:** "we do not replicate the original paper's Matlab implementation; differences in floating-point arithmetic, data alignment, or edge-case handling could produce minor deviations" (Section 5.2).
24. **Exact reproduction is gated on licensed data:** the 1-minute IQFeed history is not redistributed, and `data/README.md` warns that vendor bar construction "can produce small deviations from the published numbers" - so the printed numbers cannot be regenerated from public inputs alone - `data gap`.
25. **No capacity, turnover or trade-count statistics are reported anywhere in the paper** (the code counts trades per day but the paper never prints the series) - `data gap`.
26. **Working-paper status and thin independent scrutiny:** SSRN working paper with no journal reference and no peer-review statement, `251` downloads and `431` abstract views at read time, and a companion repository created and last pushed on the same day (2026-08-15) with 1 star and 1 fork.
27. **Arithmetic gaps the source does not reconcile:** the stated dataset of `2,827` trading days exceeds `2,333 + 480 = 2,813` by `14` sessions (research-computed), and the landing page's `0 References` conflicts with the PDF's 8-item reference list (recorded in Provenance) - neither is explained in the source.

## Falsification plan

Every threshold below is a `research-defined falsification threshold` and every operational choice not present in the source is `research-proposed`. Each gate states data, sample/regime, metric, threshold and action.

- **F1 - Printed-value reproduction.** Data: a licensed 1-minute SPY history (IQFeed, Polygon, Databento, Alpaca or IB) for 2015-01-02 to 2026-03-31, regular session only. Protocol: run the pinned repository at `32fd5a31e793fefae4deae0fb65fc2e4585a7b01` unmodified. Metric: IS Sharpe, OOS Sharpe, IS/OOS annualized return. Threshold (`research-defined falsification threshold`): IS Sharpe within `1.34 +/- 0.05` and OOS Sharpe within `0.39 +/- 0.05`, and both annualized returns within `+/- 0.5pp`. **Action on failure:** treat every printed number in this record as unreproducible and downgrade the whole capture to `underspecified`.
- **F2 - Frozen forward window.** Data: SPY 1-minute bars from **2026-04-01** onward, with the evaluation start frozen at 2026-10-01 and a minimum of **12 months** of new data (`research-proposed`). Metric: net OOS Sharpe over the frozen window with **no parameter changes of any kind**. Threshold (`research-defined falsification threshold`): net Sharpe `>= 1.00` retains the persistence claim; `<= 0.50` confirms decay; in between is inconclusive. **Action on failure (<= 0.50):** reject H-persistence for this rule on SPY and record the family as decayed.
- **F3 - Cost ladder.** Data: same as F1. Protocol: re-run at `0`, `0.0035 + 0.001`, `0.01` and `0.02` USD per share per side, plus a spread-crossing variant that charges half-spread on entry and exit. Metric: OOS net Sharpe. Threshold (`research-defined falsification threshold`): fail implementability if OOS net Sharpe `< 0.20` at `0.01` USD per share. **Action on failure:** classify as not implementable even if the gross signal survives.
- **F4 - Friction completeness ladder.** Protocol: add the missing frictions the source does not model (`research-proposed`): short-borrow fee on short notional and financing on levered gross at `0 / 50 / 100 / 200` bps per year, plus a `5 / 10 / 20` bps round-trip impact term. Threshold (`research-defined falsification threshold`): fail if OOS net Sharpe `< 0.10` at the `100 bps` financing and `10 bps` impact point. **Action on failure:** the strategy has no margin of safety against realistic friction.
- **F5 - Dividend-adjustment ablation.** Protocol: rebuild the Noise Area previous close on a dividend-adjusted series and re-run both windows. Threshold (`research-defined falsification threshold`): fail the replication claim if either IS or OOS Sharpe moves by more than `0.05`, or if the IS-OOS gap moves by more than `0.05`. **Action on failure:** part of the measured decay is a dividend artefact, not edge decay.
- **F6 - Parameter-sensitivity grid (no retuning against OOS).** Protocol: perturb only within pre-declared ranges chosen **without looking at OOS data** (`research-proposed`): lookback `7/10/14/20/30`, decision grid `15/30/60` minutes, vol target `1%/2%/3%`, band multiplier `0.5/1.0/1.5` - 135 cells. Metric: distribution of OOS Sharpe across cells. Threshold (`research-defined falsification threshold`): the decay claim survives if the **median** OOS Sharpe `< 0.60` and fewer than `20%` of cells reach OOS Sharpe `>= 1.00`. **Action on failure:** decay is a parameter-mismatch artefact rather than edge loss; withdraw the decay claim and re-specify.
- **F7 - Placebo / signal randomization.** Protocol: (a) flip the sign of every signal; (b) circularly shift the exposure series by `+/- 21` trading days; (c) replace the Noise Area with a band of identical width centered on the open. Metric: OOS Sharpe of each placebo vs the real rule. Threshold (`research-defined falsification threshold`): fail the mechanism claim if the real rule's OOS Sharpe is not greater than the 95th percentile of the placebo distribution (1,000 draws for (b)). **Action on failure:** the OOS window contains no exploitable intraday continuation at all and the IS result is consistent with selection luck.
- **F8 - Benchmark gate.** Protocol: compare the OOS net rule against (a) SPY buy-and-hold, (b) a flat/no-position book, (c) a naive always-long-at-the-decision-grid book. Threshold (`research-defined falsification threshold`): fail as an allocation if OOS net Sharpe `<= ` the SPY buy-and-hold Sharpe **or** OOS total return `<` SPY total return. **Action on failure (already observed in the source: `0.39` vs `0.91` and `9.4%` vs `29.5%`):** the rule cannot be justified as a standalone allocation on the current evidence; only a hedged or diversified use could be reconsidered, which requires a separate record.
- **F9 - Regime decomposition.** Protocol: split the OOS window into realized-volatility terciles computed **only from trailing data** (30-day trailing realized vol of 1-minute returns, `research-proposed`). Metric: OOS Sharpe per tercile vs the IS tercile profile. Threshold (`research-defined falsification threshold`): the decay claim fails if the high-volatility tercile OOS Sharpe `>= 1.00` **and** the decay is fully explained by an over-representation of the low-vol tercile. **Action on failure:** relabel the finding as regime absence, not edge decay.
- **F10 - 0-DTE / microstructure reversal test.** Protocol: measure 1-minute and 5-minute return autocorrelation of SPY in matched pre-2022 and post-2022 windows, and regress daily strategy P&L on that autocorrelation. Threshold (`research-defined falsification threshold`): the source's proposed mechanism fails if post-2022 short-horizon reversal does not increase at the `95%` level, or if the strategy's daily P&L has no negative relation to it (two-sided `p >= 0.05`). **Action on failure:** drop the 0-DTE explanation; it is an untested story.
- **F11 - Crowding-timing test.** Protocol: date the strategy's public circulation (first SSRN posting 2024-05-10 and subsequent revisions/downloads) and test whether the decay break-point is statistically later than that date (Chow / Bai-Perron on the daily return series, `research-proposed`). Threshold (`research-defined falsification threshold`): crowding fails as an explanation if decay begins **before** wide circulation. **Action on failure:** reject the crowding channel; retain only regime and adaptation channels.
- **F12 - Power gate with multiplicity control.** Protocol: extend the OOS sample until the IS-vs-OOS mean comparison has `>= 1,200` OOS trading days, and report both the Welch test and a deflated Sharpe ratio accounting for the historical parameter search (`research-defined`). Threshold (`research-defined falsification threshold`): withdraw the decay claim if at that power the IS-OOS difference is no longer significant at `p < 0.05`; conversely treat persistence as rejected only if the deflated OOS Sharpe is also `< 0.50`. **Action on failure:** the conclusion is under-powered and must be restated as inconclusive.
- **F13 - Second-vendor bar-construction gate.** Protocol: re-run F1 on a second independent 1-minute vendor for the identical calendar window. Threshold (`research-defined falsification threshold`): fail reproducibility if |OOS Sharpe difference| `> 0.15` or |IS Sharpe difference| `> 0.10`. **Action on failure:** the printed numbers are vendor-bar artefacts and must not be quoted as strategy properties.
- **F14 - Turnover and capacity bound.** Protocol: from the exposure series compute per-day one-way turnover in shares and the share of 1-minute bar volume required, then compare with SPY consolidated volume. Threshold (`research-defined falsification threshold`): fail implementability if required participation exceeds `1%` of bar volume in more than `5%` of in-position minutes, or if daily one-way turnover exceeds `100%` of the position at the 4x cap (`research-defined`). **Action on failure:** the rule is capacity-constrained and any capacity claim must be removed.

**Explicit no-retuning rule:** F2, F6, F7, F9, F10, F11, F12 and F13 are evaluated with the 14-day lookback, the 30-minute grid, the 2% vol target, the `1.0` band multiplier, the 4x leverage cap, the 2024-05-01 boundary, the 0.0035/0.001 per-share cost pair and the decision-bar alignment **frozen exactly as pinned**. A failed gate may not be rescued by adjusting any of those values, by re-selecting the OOS start, by switching vendors after seeing results, or by reporting a favourable sub-window. Only F6 explores parameter space, and it must do so without consulting OOS data when choosing its ranges.

## Crypto portability

**Portability status: `adapted`** (mechanism ports in form, performance is `unproven`, and several structural features break).

- **What ports:** the mechanism - a volatility-normalized equilibrium band plus a volume-anchored trailing exit plus daily vol targeting - is instrument-agnostic and is routinely implementable on BTC/ETH perpetuals or on a top-N liquid coin basket (`research-proposed`). The sizing formula and the 4x cap translate directly to exchange leverage limits.
- **What does not port cleanly:** the source studies **only SPY**; `bitcoin`, `ethereum`, `perpetual`, `funding`, `24/7` and `crypto` all have **zero occurrences** in the pinned PDF, so there is no crypto evidence in this record - `unproven`.
- **Session structure:** the Noise Area is anchored on the exchange open and the previous close (`max/min(Open, PrevClose)`), on a 09:30-15:59 ET regular session, on a session VWAP, and on a forced flat at the session close. A 24/7 market has no session open, no official close, no gap term of that kind, and no natural intraday reset; defining the equivalent boundaries (e.g. UTC 00:00, futures mark-time, or per-venue open) is a `research-proposed` redesign, not a port.
- **Funding and borrow:** perpetual funding settles roughly every 8 hours and short exposure pays or receives it; the source models **no** funding, no borrow and no financing, so a ported version must add a funding term that can dominate a `0.39`-Sharpe-class edge - `data gap`.
- **Venue fragmentation and liquidity:** SPY is a single deep instrument on consolidated US equity venues; crypto liquidity is split across venues with different 1-minute bar constructions, and the source itself shows vendor bar differences matter even for one ETF.
- **Mark / index price and liquidation:** levered short crypto positions carry mark-price liquidation risk that does not exist for an ETF cash position; the source has no liquidation model - `data gap`.
- **Cost anchor:** the USD 0.0035 + USD 0.001 per-share pair is an Interactive Brokers equity schedule and carries no information about taker/maker fees, funding spreads or gas on crypto venues - `data gap`.
- **Clock and candle boundaries:** minute bars must be aligned to exchange timestamps with documented treatment of gaps, delistings and halts; the source does not describe out-of-order or missing-bar handling - `data gap`.

## Limitations

- **`not independently reproduced`** - nothing in this record has been reproduced by us; no strategy code was executed and no market data were obtained in this run.
- **`source-reported`** - all performance, test-statistic and sample figures are third-party claims from a working paper whose peer-review status is `not stated in source`.
- **`one further remove`** - every figure attributed to Zarattini, Aziz & Barbon (2025) (`1,985%`, `19.6%`, `1.33`, `2007-2024`, `43%`, `25%`) is quoted **by this source**; SSRN `4824172` was not opened this run, so those figures are not primary-verified here. They are also already staged separately in this repository from a direct read of that SSRN item.
- **`underspecified` in the source:** the VWAP price convention; the exact decision-bar alignment (10:00 vs the bar just before it); the NaN-volatility sizing fallback; the per-order commission floor; out-of-order/missing bar handling; the reason 14 sessions are unaccounted for between the stated dataset and the stated IS/OOS day counts; whether the strategy's parameters were ever formally optimized (the source says "presumably selected").
- **`data gap`:** spread, market impact, participation, turnover statistics, capacity, latency, order type, fill model, borrow availability and cost, financing cost on the 4x leverage, dividend adjustment, and the licensed 1-minute input data itself.
- **`unproven` explanations:** the 0-DTE/gamma-hedging channel and the crowding channel are explicitly proposed but explicitly untested by both the original and the replication.
- **Statistical limitations:** 480 OOS trading days; the raw-mean comparison does not reject (`p = 0.255`) while the Sharpe comparison does; no multiplicity adjustment is reported even though the original parameters were chosen on historical data; no deflated Sharpe ratio, no probability-of-backtest-overfitting measure and no walk-forward re-estimation are reported.
- **Design limitation:** the IS/OOS split is a single chronological cut at 2024-05-01 with no rolling or repeated OOS evaluation, so one 1.9-year path carries the entire decay claim.
- **Universe limitation:** a single instrument in a single asset class; there is no cross-sectional diversification, so the reported path is one realization of one symbol.
- **Attribution limitation:** this record must not be read as an independent validation of the Zarattini et al. strategy, nor as evidence that intraday momentum is dead; it documents one replication's OOS window.
- **Surface limitation:** the repository's own copy of the paper PDF (666,127 bytes) was not pinned, so no cross-surface numeric audit between the two renders was possible - `data gap`.
- **Public-safety:** no secrets, credentials, private data, local paths or licensed market data are contained in this record; the licensed 1-minute history is referenced by vendor name only.

## Implementation status

`not-implemented`

The frontmatter of this record reads `status: research-only`, `implementation_status: not-implemented`, `adoption: not-approved`, `approval_scope: research-only`.

Nothing in this strategy or this replication exists in our research stack. Specifically: no SPY 1-minute data loader, no Noise Area / VWAP / vol-target engine, no backtest, no production card, no candidate-pool entry, no Qlib full backtest, and no Paper, Testnet or Live run has been performed. The upstream implementation described here is **third-party code in a public repository, read but never executed**; no dependency was installed and no market data were downloaded during this run. Any future implementation requires a separate, explicit implementation decision and independent validation on point-in-time data.

## Adoption boundary

This document is **research capture only**. Its presence in this repository does **not** mean:

- passed Research Intake Review;
- entered Hermes Wiki Brain;
- entered the production candidate pool;
- completed Qlib full-backtest validation;
- became a frozen survivor or leaderboard entry;
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

Nothing here authorizes Paper, Testnet or Live execution, and no wording, evidence count, confidence value or schedule behaviour of this record can promote it. Any later adoption or implementation decision must be explicit, separately reviewed, and based on this record plus current live sources.

## Related Wiki records

- `[[quant/llm-news-enhanced-cross-sectional-momentum-tilt]]` - verified to exist by direct `kb_read` (21,058 bytes, SHA-256 `1c026ccfbe8603cf6d2354823f996864ae72540a34b175d539901378f16aeb59`). Different paper (`arXiv:2510.26228`, LLM-confirmed cross-sectional momentum) and a different mechanism (monthly cross-sectional tilt vs half-hourly intraday band breach); linked only for author-lineage orientation, since Barbon and Zarattini appear in both source author lines.
- `kb_search("intraday momentum SPY Noise Area VWAP trailing stop")` returned **0 pages**, so **no Wiki page for this strategy family, for SSRN 7290621 or for SSRN 4824172 exists** and none is asserted. The other seven pages returned by the second `kb_search` cover unrelated mechanisms (A-share order-age imbalance, crypto flush reversal, altcoin liquidity-lag LightGBM, foundation-transformer arb, Fourier-residue reversal, crude crack spread, BTC turn-of-candle seasonality) and are deliberately **not** linked.

Repository neighbours (plain file names for reviewer orientation, **not** Wiki links):

- `spy-intraday-momentum-noise-area-band-vwap-stop-dynamic-sizing-2026-09-23.md` - the original strategy record (SSRN 4824172) that this replication evaluates.
- `opening-range-breakout-pre-registered-225-cell-futures-cost-falsification-2026-09-27.md` - another intraday-boundary falsification, different instrument class and pre-registered cost grid.
- `spy-nbbo-lag-resolved-push-response-conditional-anomaly-2026-09-24.md` - same ticker, descriptive event-time quote study with no performance numbers.
- `us-equity-momentum-rebalance-timing-luck-tranching-cost-aware-ssrn-5747964-2026-09-27.md` - cites the same upstream `4824172` prior art; unrelated mechanism.
- `ensemble-donchian-trend-following-crypto-top20-rotational-2026-09-20.md` - Zarattini author line, crypto daily rotation, different horizon and asset class.

## Sources

1. Sheimy Paz (SSRN landing) / Sheimy Paz Serpa (PDF byline), *Out-of-Sample Evaluation of an Intraday Momentum Strategy for the S&P 500 ETF (SPY)*. SSRN working paper, 12 pages, Date Written June 02, 2026, Posted 19 Aug 2026.
   - Abstract page (read 2026-09-30): `https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7290621`
   - Stable short form: `https://ssrn.com/abstract=7290621`
   - DOI: `https://doi.org/10.2139/ssrn.7290621`
   - **Pinned full text** (fetched 2026-09-30 via a real browser session; plain `curl` is blocked by Cloudflare HTTP 403): `https://papers.ssrn.com/sol3/Delivery.cfm/7290621.pdf?abstractid=7290621&mirid=1` - **696,466 bytes, 12 pages, SHA-256 `cfc08247491705e34655064b22590c70562ae6daa31d459e16421718fd30c5bb`**, `pypdf 6.16.2` extraction of 18,435 characters read end to end; provenance for Sections 1-6, Equations (1)-(3), Tables 1-4, Figure 1-3 captions, the 8-item reference list, and Appendix A.
   - License: CC BY-NC-ND 4.0 (as printed on the landing page); text is cited and normalized, not redistributed.
2. Companion replication repository: `https://github.com/PazSheimy/spy-intraday-momentum-oos`, pinned at **full commit SHA `32fd5a31e793fefae4deae0fb65fc2e4585a7b01`** on `main` (verified by `git ls-remote` and the GitHub API on 2026-09-30; parent `0a59426a4290afbb1b17d4a931224241dbdb528e`; MIT license; created 2026-08-15T17:47:19Z, pushed 2026-08-15T19:44:32Z).
   - `README.md` at that SHA - 6,658 bytes, SHA-256 `43f9dcddfb0ebe75c4538396059ff9ac573270636febe08fad0d3b497ace2475` - read in full; source for the headline result table, the attribution block, the parameter list (`OOS_START`, 2% vol target, 4x cap, 30-minute grid, USD 0.0035 + USD 0.001 per share) and the repository structure.
   - `src/zarattini_intraday_momentum.py` at that SHA - 17,008 bytes, SHA-256 `778df2ebdd5e863dfac09c8fa9b078619b07be17118b24391845d7436097129b` - read in full, **never executed**; source for every `code-level` item above (config constants, VWAP convention, decision-bar alignment, exposure shift, sizing fallback, commission floor, forward-fill/flat-at-close logic).
   - `data/README.md` at that SHA - 1,946 bytes, SHA-256 `5d7ebd7a699f33bbc32ce86d5937d9fb49a4758050f38397746e3350bafb0d66` - read in full; source for the required CSV schema, the RTH filter, the IQFeed licensing restriction and the vendor-substitution caveat.
   - GitHub API: repository metadata, commit object and recursive tree at the same SHA (all read-only).
3. **Upstream strategy source, cited at one further remove (not opened by this run):** Carlo Zarattini, Andrew Aziz, Andrea Barbon, *Beat the Market: An Effective Intraday Momentum Strategy for S&P500 ETF (SPY)*, SSRN `abstract_id=4824172`, DOI `10.2139/ssrn.4824172`. All `1,985% / 19.6% / 1.33 / 2007-2024 / 43% / 25%` figures in this record are **as quoted by source 1**, and the strategy specification itself is attributed to that paper by source 1's Section 3. A separate record for SSRN 4824172 already exists in this repository from a direct read.
4. Works cited **inside** source 1 (bibliographic only, not opened): Baltussen, Da, Lammers & Martens (2021), *JFE* 142(1):377-403; Gao, Han, Li & Zhou (2018), *JFE* 129(2):394-414; Jegadeesh & Titman (1993), *JF* 48(1):65-91; Lo (2002), *FAJ* 58(4):36-52; Rosa (2022), *JFM* 60:100718; Zarattini & Aziz (2023), SSRN working paper; Zarattini & Aziz (2024), SSRN working paper.
