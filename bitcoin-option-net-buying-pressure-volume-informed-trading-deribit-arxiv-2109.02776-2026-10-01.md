---
schema: strategy-research-record-v1
title: "Delta-Weighted Option Net Buying Pressure and Lagged Option Volume as Short-Horizon Predictors of Bitcoin Spot Return and Volatility (Deribit BTC Options)"
created: 2026-10-01
updated: 2026-10-01
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - bitcoin
  - options
  - deribit
  - order-flow
  - net-buying-pressure
  - informed-trading
  - volatility
  - microstructure
status: research-only
confidence: medium
source_as_of: 2026-10-01
sources:
  - "https://arxiv.org/abs/2109.02776"
  - "https://arxiv.org/pdf/2109.02776v2"
  - "https://doi.org/10.1016/j.finmar.2022.100764"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Section 3 prose states that 'the annual average ATM net buying pressures shot up from 455 USD in 2017 to 94,818 USD in 2020', but Table 6 Panel B (Average Hourly Net Buying Pressure, ATM row, Call columns) prints 19,432 under 2020 and 94,818 under the 2021 column; the printed 455 for 2017 matches, the printed year for 94,818 does not. Unreconciled; the table cells are treated as truth."
  - "Section 3 prose states that 'On average during 2020, the net buying pressure on ITM calls is 109.48 USD million', but Table 6 Panel B (ITM row, 2020 Call column) prints 12,395 with the table note giving units of USD (the Figure 3 caption gives USD million for the same class of measure). The same sentence's ratio claim ('about 2/3rds of the buying pressure on ATM calls') does reproduce from the table (12,395 / 19,432 = 0.64), so the value 109.48 USD million and its unit cannot be reconciled with any printed cell. Unreconciled; the table cells are treated as truth."
  - "Section 2 data-cleaning prose is internally inconsistent: of a stated 3,431,071-entry full set, 2,152 trades with missing option type (0.062 percent, reproduces) and 'another 2,447 (0.71 percent)' outside the [0, 500] percent implied-volatility bounds are removed, yet the printed cleaned set of 3,427,160 entries requires only 3,911 total exclusions, i.e. an unstated 688-trade overlap between the two exclusion rules (3,431,071 - 2,152 - 2,447 = 3,426,472, not 3,427,160); and 2,447 / 3,431,071 = 0.071 percent, not the printed 0.71 percent (a factor-of-10 discrepancy). Unreconciled; the printed entry counts are treated as truth and the printed percentage as an error."
  - "Section 3 closes by claiming that Table 5 shows bitcoin options traders 'possess superior, if short-lived, information about the future direction of bitcoin spot and option prices that would allow them to generate abnormal returns', yet the same section states that the direction-carrying variable, order imbalance N, 'has no predictive power for returns over the next interval', and Table 5 prints N with no star at 1-hour, 1-day and 5-day horizons for returns while the only significant return predictor is the unsigned lagged volume change Delta-v. The claim that unsigned volume carries 'information about the future direction' is not reconciled with the table. Unreconciled; the table cells and the paper's own null sentence are treated as truth."
---

# Delta-Weighted Option Net Buying Pressure and Lagged Option Volume as Short-Horizon Predictors of Bitcoin Spot Return and Volatility (Deribit BTC Options)

## Provenance

- **Paper:** Carol Alexander, Jun Deng, Jianfen Feng and Huning Wan, "Net Buying Pressure and the Information in Bitcoin Option Trades."
- **Author list (exactly as printed on page 1):** Carol Alexander (marked corresponding author, double asterisk); Jun Deng; Jianfen Feng; Huning Wan (single asterisks). Four authors, same order on the arXiv landing page and in the arXiv API author list.
- **Affiliations (page-1 footnotes, contact addresses deliberately not reproduced):** corresponding author - University of Sussex Business School and Peking University HSBC Business School, Brighton, UK; the other three authors - School of Banking and Finance, University of International Business and Economics, Beijing, China. JEL Classification G32, G11. Keywords: Deribit options; Informed traders; Market makers; Volatility information; Directional information.
- **Preprint:** arXiv:2109.02776v2 [q-fin.GN]. Landing-page submission history: `[v1] Mon, 6 Sep 2021 23:47:35 UTC (7,799 KB)` and `[v2] Fri, 25 Mar 2022 13:08:38 UTC (2,974 KB)`; page 1 carries the stamp `arXiv:2109.02776v2 [q-fin.GN] 25 Mar 2022`; the manuscript dateline on page 1 reads `This Version: March 28, 2022` (three days after the v2 upload date - recorded, not reconciled). Comments cell: `35 pages`. Subjects: primary General Finance `q-fin.GN`, no cross-lists.
- **Publication status:** the pinned arXiv record carries **no journal reference and no DOI** (arXiv API `journal_ref` NONE, `doi` NONE), but a **peer-reviewed journal version exists**: Crossref (queried over HTTPS on 2026-10-01) returns DOI `10.1016/j.finmar.2022.100764`, *Journal of Financial Markets*, volume 63, article 100764, published 2023-03, same four authors in the same order; Crossref also returns the SSRN preprint DOI `10.2139/ssrn.3915901` (2021). Footnote 12 of the pinned PDF thanks "an anonymous referee" for a robustness-check suggestion, which is consistent with journal review. **Whether the pinned arXiv v2 text is identical to the published article is a `data gap`: the Crossref/journal abstract is worded differently from the arXiv v2 abstract, and the published tables were not retrieved, so every number in this record traces to arXiv v2 only.**
- **Licence:** the arXiv landing page shows CC BY-SA 4.0 (`creativecommons.org/licenses/by-sa/4.0/`).
- **Stable URLs:** abstract `https://arxiv.org/abs/2109.02776`; PDF (pinned v2) `https://arxiv.org/pdf/2109.02776v2`; journal DOI `https://doi.org/10.1016/j.finmar.2022.100764`; API `https://export.arxiv.org/api/query?id_list=2109.02776`.
- **Primary-source checksum (fetched 2026-10-01 over HTTPS):**
  - Landing page: **40,118 bytes**, SHA-256 `695c741f1f460b283063d4f7bd09fbb0034202829e8cf82887fac549ab33a42d` - used for the title, the four `citation_author` entries, the two-version submission history, the `35 pages` comment, the single `q-fin.GN` subject, the CC BY-SA 4.0 licence and the absence of Journal-reference and DOI rows.
  - PDF: **1,439,561 bytes**, SHA-256 `6fbd49f8f551813a6e622777e16160ef20e176b2247afe1aa5ffcd59ad377432`, extracted with pypdf into **35 pages / 91,531 characters / 1,374 lines** (96,480-byte UTF-8 file, SHA-256 of the file `514bda047862e869150f1cb3921d9b176f2e95b2350ad4a6683fd8815553e8f5`), **read end to end** covering the page-1 author block and abstract, Sections 1-6, Tables 1-13 (every printed cell), the captions of Figures 1-3, footnotes 1-13 including footnote 12, and the 32-item reference list.
  - arXiv API record: **2,260 bytes**, SHA-256 `9d0b494a53a0b36a34b4c18f16c5595d8486424cf9a5f5d7de56a36b1110270d` - `published` 2021-09-06T23:47:35Z, `updated` is the feed-level response timestamp, single entry, `arxiv:comment` "35 pages", no `journal_ref`, no `doi`.
  - **Text-layer caveat recorded, not reconciled:** pypdf preserves Unicode ligatures, so the raw text layer spells words such as "significant", "profit", "efficient" and "coefficient" with fi/fl ligatures. Every count in the census below was taken **after** normalising `\ufb00-\ufb04` to `ff`, `fi`, `fl`, `ffi`, `ffl`; a pre-normalisation census undercounts those terms and must not be reused.
- **Data as-of:** Deribit bitcoin options tick-by-tick trades **1 January 2017 to 28 July 2021** (Table 1 note), retrieved through the Deribit application program interface, "which no longer provides historical data but our sample can be accessed from Tardis or CoinAPI"; the sample "stops after July 2021 because there are data only for very short maturity trades". Comparison data: daily-frequency S&P 500 index options from Wharton Research Data Services, 8,688,408 entries (4,362,860 calls / 50.21 percent, 4,325,548 puts / 49.79 percent), "only available until 2020". Reported empirical results are for 2019, 2020 and the first seven months of 2021 (Section 5); 2017 and 2018 results exist but are not reported because volumes were very low.
- **Cost/slippage treatment - determined at Methods level**, by reading Sections 1-6, equations (1)-(6), Tables 1-13 and footnotes, **plus a ligature-normalised whole-document word census of the pinned 91,782-character (normalised) text layer**: `fee` 1 and `fees` 1 (the same single occurrence, in Section 1 about managed bitcoin funds that "charge high fees"), `transaction cost` 1 (Section 1: "transaction costs are much higher in options than they are in spot and futures markets"), `slippage` 0, `bid-ask` 0, `bid ask` 0, `spread` 5 (all either the realised-implied "volatility spread" VS = RV-IV or the phrase "wide-spread academic interest"), `commission` 1 (only inside "U.S. Securities and Exchange Commission"), `borrow` 0, `leverage` 8 (all descriptive or as the regressor control alpha_1/beta_1: Easley-style determinants, "up to 100X leverage" on Deribit, the leverage effect), `liquidation` 1 (only inside a reference title), `capacity` 0, `latency` 0, `funding` 0, `maker` 23 (all inside "market maker(s)"), `taker` 0, `fill` 1 (only "fill this important gap"), `market impact` 0, `bps` 0, `turnover` 0, `order book` 1 (only the Deribit index-construction sentence), `participation` 2 (both prose about retail/speculator participation), `backtest` 0, `sharpe` 0, `sharpe ratio` 0, `cagr` 0, `drawdown` 0, `win rate` 0, `annualised` 3 / `annualized` 0, `risk-adjusted` 0, `holding period` 0, `abnormal return` 1 (the Section 3 strategy sentence), `profit` 2 (the Section 1 risk-reversal example and one reference title), `portfolio` 2, `strategy` 3 and `trading strategy` 1, `return` 20 / `returns` 11, `volume` 64, `p-value` 0, `t-stat` 0, `standard error` 0, `confidence interval` 0, `r2` 0, `heterosked` 0, `newey` 0, `robust` 3 (two robustness statements and one "robustness check" footnote), `bootstrap` 0, `significan` 28, `look-ahead` 0, `survivorship` 0, `point-in-time` 0, `seed` 0, `repository` 0, `github` 0, `code` 0, `data availability` 0, `reproduc` 0, `peer` 0, `referee` 1, `acknowledg` 2, `orcid` 0, `competing` 0, `grant` 0, `nobs` 5. **There is therefore no fee schedule, no bid-ask/spread, slippage, fill, latency, participation or market-impact model anywhere in the paper, no return or risk metric of any kind, and no standard errors, t-statistics or R-squared - significance is reported only as star levels. Every one of those fields is a `data gap` and must never be read as zero cost or as validated performance.**
- **Source-identity deduplication (pre-write, 2026-10-01, hidden-inclusive ripgrep across the entire checkout including `.git`, `.mimo-worktrees`, `.agents`, `.hermes` and `coverage_manifest.csv`):** `2109.02776` **0 files**, `Net Buying Pressure and the Information` **0**, `10.1016/j.finmar.2022.100764` **0**, `finmar.2022.100764` **0**, `3915901` **0**, `Bollen and Whaley` **0**, `Jianfen Feng` **0**, `Huning Wan` **0**, `volatility-motivated` **0**. Author probe `Carol Alexander` **6 files** = exactly two other records plus their four `.mimo-worktrees` copies, and both cite *different* Alexander papers (Alexander & Heck, "Price discovery in Bitcoin", JIMF 109, 102247, 2020; Alexander & Heck, "The impact of unregulated markets", J. Financial Stability 50, 100776, 2020; Alexander, Heck & Kaeck, "The Role of Binance in Bitcoin Volatility Transmission", Applied Mathematical Finance 29(4), 2022) - **different source identities, different mechanisms**. Loose probes: `Bollen` **1 file** (the Polymarket comment-attention record, where the hit is "Mao, Counts & Bollen (2011)" - a sentiment reference, unrelated); `net buying` **5 top-level markdown files**, none about option trades on Deribit; `finmar` **3 top-level markdown files**, all citing Anastasopoulos, Gradojevic, Liu, Maynard & Tsiakas, "Order flow and cryptocurrency returns", *Journal of Financial Markets* 79 (2026) 101047 - a **different paper** (spot/futures order flow, cross-sectional crypto panel) whose distinction is stated under Related Wiki records; `Deribit` **220 files** (Deribit is a common venue), none of which pairs Deribit with delta-weighted option net buying pressure - the exact probe `net buying pressure` in `*.md` returns **1 file** and that hit is spot/perpetual order-flow imbalance prose in the Hyperliquid record. Positive control `novy-marx` **55 files** before the write. `git log --oneline -20` was used as a convenience glance only, never as dedup.

## Economic mechanism

### Source-reported

The paper is a **price-discovery and demand-decomposition study of an existing market**, not a return-premium claim. Its stated object is "the information we can derive from trading patterns in bitcoin options, by modelling their implied volatilities" (Section 6). Three competing hypotheses are tested against hourly aggregates of Deribit tick trades (Section 1):

- **Limits-to-arbitrage (supply side):** market makers "would manage inventory at a rational level, so changes in net demand would affect option prices and hence also their implied volatilities"; hedging costs "increase with the imbalance of a market maker's net positions", so "the market maker's options supply curves slope upwards". Prediction: changes in implied volatility are negatively autocorrelated (significant alpha_5 < 0 in equations (4) and (5)).
- **Volatility-learning hypothesis:** the market maker learns about future **volatility** from ATM option demand and updates the whole smile; volatility traders "have no reason to prefer ATM calls to ATM puts", so calls and puts are demanded symmetrically. Rationale given for why volatility information dominates: "transaction costs are much higher in options than they are in spot and futures markets, so directional information is easier to exploit by trading in spot and futures than it is by trading in options. However, volatility can only be traded in options markets".
- **Directional-learning hypothesis:** informed traders hold "privileged information about the direction of future movements in the price of the underlying", buy calls and sell puts (or the reverse), so net buying pressure on calls and puts moves with opposite signs.
- **Informed-trading / volume channel (Section 3):** lagged changes in option trading volume `Delta-v` and lagged aggregate order imbalance `N` are regressors for one-period-ahead bitcoin spot return `r`, change in implied volatility `Delta-IV` and change in realised volatility `Delta-RV`.
- **Source-reported headline results:** limits-to-arbitrage is confirmed across all moneyness categories (Section 5: "the limits-to-arbitrage hypothesis is consistently supported across moneyness categories"); volatility-motivated demand dominates directional-motivated demand ("beta_3 is always greater than beta_4", Table 8), which the paper contrasts with developed index-options markets where directional learning dominates; directional demand is significant mainly in OTM and DOTM options and "only directional learning is evidenced by ATM puts in 2021", which the authors attribute to the 2021 price bubble; volatility-informed traders prefer short- and medium-term maturities, and directional learning is supported "only during Asian and US trading times" (Table 13).
- **The only trade the source actually sketches (Section 1):** "Suppose a trader believes that the bitcoin market is about to enter a particularly volatile month ahead ... Then the trader should enter a bearish risk reversal strategy by writing DOTM calls and using the premium to buy DOTM puts of the same maturity." No threshold, sizing, entry timestamp, exit rule or cost hurdle is given - `underspecified`.
- **The source's own tradeability sentence (Section 3):** the Table 5 results "suggest that bitcoin options traders may indeed possess superior, if short-lived, information about the future direction of bitcoin spot and option prices that would allow them to generate abnormal returns by developing a suitable trading strategy for bitcoin options." The paper **does not build or backtest such a strategy** - see the recorded contradiction in frontmatter.

### Research interpretation

Falsifiable mechanism statement: **aggressor-signed option order flow is a noisy, horizon-limited state variable for the next period's volatility (and possibly return) of the underlying.** The mechanism splits into two separable channels with different evidence quality:

```text
Regime: none required by the source. Research-proposed (optional) gating only: pre-2019 versus 2019+ (the source reports informed trading "only emerged after 2019" and suppresses 2017-2018 results).
Primary signal A (source-reported, VOLATILITY channel): lagged hourly delta-weighted net buying pressure N, and its decompositions V (volatility-motivated) and D (directional-motivated) by moneyness k, forecast same-signed changes in implied and realised volatility at 1 hour and 1 day (Table 5, N column: IV 6.36e-5*** and 3.96e-5***; RV 4.35e-7*** and 9.94e-6***).
Primary signal B (source-reported, DIRECTION channel): lagged hourly change in option trading volume Delta-v, not the signed imbalance, forecasts next-hour and next-day bitcoin spot return (Table 5, Delta-v column: 0.27*** and 0.51***).
Null that must travel with the record (source-reported): the direction-signed aggregate order imbalance N has NO predictive power for returns at 1 hour, 1 day or 5 days (Table 5, N column, all three return rows unstarred; stated explicitly in Section 3).
Confirmation (source-reported, structural): implied-volatility changes are mean-reverting with alpha_5 roughly -0.40 to -0.47 in ATM/OTM/DOTM cells (Table 7), about twice the magnitude of the -0.17 (S&P 500) and -0.23 (TAIEX) values the paper relays from other studies - i.e. the Deribit smile is more demand-sensitive than developed-market smiles.
Decision layer (research-proposed, NOT specified by the source): any long-volatility position (risk reversal, straddle) or any directional spot/perpetual position taken when signal A or B crosses a threshold. Threshold, sizing, holding period, order type, cost hurdle and stop rules are entirely research-proposed.
```

The alpha claim under test is narrow: *hourly Deribit option flow contains decision-relevant information about the next 1-24 hours of bitcoin volatility, and unsigned option volume contains decision-relevant information about the next 1-24 hours of bitcoin spot return, beyond own-lag dynamics.* **The source conducts no trading simulation, prints no cost model and reports no return or risk metric, so every P&L statement built on this record is a ported, research-proposed hypothesis.**

## Signal

All items are **source-reported** unless explicitly marked research-proposed / research-defined / `data gap`.

- **Formation timestamp:** tick trades are aggregated into **hourly** bins between `t-1` and `t` (Section 3 and Section 5: "We use implied volatility and net buying pressure measures at the hourly frequency"). Deribit timestamps are in milliseconds; settlement is at 08:00 UTC and the time-of-day analysis uses explicit UTC slots (Table 12), so bins are implicitly UTC - the paper never states a timezone convention for binning (`underspecified`).
- **Signal A - aggregate order imbalance (equation 1):** `N_t = sum_i B_i,t * |Delta_i,t| - sum_i S_i,t * |Delta_i,t|`, where `B` is buyer-initiated and `S` seller-initiated option volume in the hour and `|Delta|` is the absolute Black-Scholes delta of the traded option.
- **Signal A2 - moneyness- and type-specific net buying pressure (equation 1):** `A^k_{j,t}` with `j` in {Call, Put} and `k` in {DOTM, OTM, ATM, ITM, DITM}, same delta weighting.
- **Signal A3 - Chen-Wang decomposition (equations 2 and 3):** directional-motivated demand `D^k_{C,t} = (A^k_{C,t} - A^k_{P,t}) / 2` with `D^k_{P,t} = -D^k_{C,t}`; volatility-motivated demand `V^k_t = (A^k_{C,t} + A^k_{P,t}) / 2`. A footnote states that relative (volume-normalised) versions `D/TV`, `V/TV` were computed, are "qualitatively unchanged", and are **not reported** ("available on request") - `data gap`.
- **Moneyness classification:** Black-Scholes delta computed with a single sigma for all options = the **15-day realised volatility of bitcoin daily log returns** (chosen "because it avoids any endogeneity concerns in our regressions where the dependent variable is implied volatility"); options with `|Delta| < 0.02` or `> 0.98` are excluded "because of the distortions due to stale prices and illiquidity". Bands: DOTM (0.02, 0.125], OTM (0.125, 0.375], ATM (0.375, 0.625], ITM (0.625, 0.875], DITM (0.875, 0.98]. Claimed robustness to 30-day RV, to the option's own implied volatility and to K/S moneyness is stated but the results are "available from the authors on request" - `data gap`.
- **Maturity buckets:** short-term [1, 7] days, medium-term [8, 21] days, longer-term >= 22 days, chosen "so that trading volume is approximately equal in each".
- **Signal B - volume change `Delta-v`:** "the change in bitcoin option trading volume". **The construction of `Delta-v` (level difference, log difference, normalised change, which aggregation) is never defined anywhere in the paper** - `data gap`, and it makes the printed gamma_2 magnitudes uninterpretable in economic units.
- **Regression - information content (Section 3, Table 5):** `x_t = gamma_0 + gamma_1 * x_{t-1} + gamma_2 * y_{t-1}` with `x` in {bitcoin spot index return `r`, `Delta-IV`, `Delta-RV`} and `y` in {`Delta-v`, `N`}, at 1-hour, 1-day and 5-day intervals. **Neither the sample window of Table 5 nor its observation count, nor the exact IV/RV series definition used as `x`, nor any standard error, t-statistic or R-squared is stated** - `underspecified` / `data gap`.
- **Regression - Bollen-Whaley test (equation 4, Table 7):** change in ATM (and, by equation (5), OTM/DOTM) implied volatility on contemporaneous spot return `r_t` (leverage control), spot volume `v_t` (information-flow control, proxied by aggregated USD volume on **Bitstamp, Coinbase and Gemini**), net buying pressure on the cell's own options `A^k_{j,t}`, net buying pressure on ATM options `A^ATM_{i,t}`, and the lagged change in implied volatility.
- **Regression - Chen-Wang test (equation 6, Tables 8-11 and 13):** same regressors with `V^k_t` and `D^k_{j,t}` in place of ATM net buying pressure, for `k` in {ATM, OTM, DOTM} and by maturity bucket and by UTC time slot.
- **Frequency robustness (Section 5):** "our results are robust to several other data frequencies, such as 4 or 8 hours **but not if we aggregate to the daily frequency**", with the daily results "available on request" - `data gap` for the daily specification.
- **Long entry / short entry / exit / holding period / re-entry / sizing / multi-timeframe dependencies:** `not stated in source`. The only directional prescription is the qualitative bearish risk-reversal example quoted under Economic mechanism; there is no threshold, no stop, no sizing, no holding period and no cost hurdle anywhere in the paper.
  - *Research-proposed (not source-reported) operationalization, offered only so the hypotheses are testable:* (a) volatility leg - go long BTC option volatility (or a delta-hedged straddle/strangle) at the top of hour `t` when the standardised lagged `V^ATM` (or `N`) exceeds a research-defined threshold, exit after a research-defined horizon; (b) directional leg - take a same-signed spot/perpetual position when standardised lagged `Delta-v` exceeds a research-defined threshold. **Standardisation method, threshold, sizing, holding period, order type, stop and cost hurdle are entirely research-proposed and have no source support.**

## Required data

- **Instrument / universe:** all Deribit bitcoin options - European calls and puts, nominal 1 BTC, settlement 08:00 UTC, cash-settled in bitcoin, expiries 1 day to 12 months (1-, 2-day and 1-, 2-, 3-weekly listings added from 2019). Cleaning as printed: 3,431,071 raw trades to 3,427,160 (1,833,838 calls / 53.51 percent, 1,593,322 puts / 46.49 percent) after dropping missing option type and out-of-bound implied volatilities (see the recorded contradiction on the exclusion arithmetic).
- **Venue:** Deribit (the paper states Deribit is about 80 percent of global bitcoin option volume at the time of writing). Underlying reference: the Deribit bitcoin index, an equally weighted average of USD spot on Bitstamp, Gemini, Bitfinex, Bittrex, Itbit, Coinbase, LMAX Digital and Kraken, excluding exchanges with invalid data or delayed order books.
- **Market type:** crypto **options** (bitcoin) plus a **spot** leg; no perpetual-futures data is used (`funding` 0 occurrences).
- **Timeframe:** tick-level trades with millisecond timestamps aggregated to 1 hour (source-robust at 4 and 8 hours, not at daily); regressions at 1-hour, 1-day and 5-day lags; sample 2017-01-01 to 2021-07-28 with reported results for 2019, 2020 and 2021 YTD.
- **Fields:** option expiry, strike, contract type, **trading direction (buyer- or seller-initiated)**, implied volatility, option price in BTC, traded amount in BTC, underlying index price in USD, millisecond timestamp; spot volume proxy from Bitstamp + Coinbase + Gemini USD volumes; bitcoin daily log returns for the 15-day realised volatility used in delta classification.
- **Point-in-time / availability:** `not addressed in source` - no publication-lag, revision or look-ahead audit (`look-ahead` 0, `point-in-time` 0). All inputs are exchange-observed market data, so the look-ahead risk is mainly in the simultaneity the source itself concedes: "the regressions we perform are not designed to detect the direction of causality" (Section 5).
- **Timestamp / timezone:** millisecond exchange timestamps; UTC implied by Table 12's slots and the 08:00 UTC settlement; no explicit binning convention, clock-drift or out-of-order handling - `underspecified`.
- **Missing data:** 2,152 trades with missing option type dropped; 2,447 trades outside the exchange's [0, 500] percent implied-volatility bounds dropped (arithmetic recorded as a contradiction); no other imputation rule is stated.
- **Data availability risk:** the Deribit API "no longer provides historical data"; the source says its sample "can be accessed from Tardis or CoinAPI" - both are third-party commercial archives. Aggressor-side flags on Deribit option trades are exactly the field most likely to be absent from free sources - `data gap`.
- **Funding/fee/spread needs:** `not stated in source` - the paper models no fees, spreads, funding or slippage because it performs no trading simulation.

## Execution assumptions

- **Signal-to-order timing:** `not stated in source`. The paper is explicit that a daily window is "too wide to detect informed trading in such a fast-changing and volatile market" and that information flows "during the course of one day", so any tradable version inherits a very short effective horizon.
- **Order type / fill model / latency / partial fills / cancellations:** `not stated in source`.
- **Fees / spread / slippage / impact / participation / capacity:** **none modeled - see the Methods-level census in Provenance. Do not read this as "costs are zero"; it is a price-discovery study.** The only friction statements are qualitative: option transaction costs are "much higher ... than ... in spot and futures markets" (Section 1), and "as the bitcoin options market matures, we could expect trading costs to diminish" (Section 5).
- **Leverage / margin / borrow:** not modeled. Descriptive only: Deribit and similar platforms "offer up 100X leverage"; margin on established options exchanges is linked to underlying volatility while crypto platforms are not.
- **Shorting:** not addressed for the spot leg; option legs are naturally two-sided.
- **Market micro-facts available from the source:** contract nominal 1 BTC, cash-settled in bitcoin, 24/7 trading every day of the year, 1-2 day options about 20 percent of Deribit volume, call-put volume ratio about 54:46 after 2019 versus about 4:6 for S&P 500 index options, bitcoin's volatility risk premium consistently negative and much larger in magnitude than S&P 500's (Table 3), exchange-implied-volatility bounds [0, 500] percent.
- Whether any of this survives realistic option execution frictions is **not addressed by the source** and is the central open question for any adoption decision.

## Evidence

### Source-reported

All figures below are source-reported from arXiv:2109.02776v2, are **regression coefficients, counts and market-structure shares - not P&L -** and have not been independently reproduced. Each is tied to its table/section.

**Table 1 - option volume share by maturity (percent).**

| Contract | Bucket | 2017 | 2018 | 2019 | 2020 | 2021 |
| --- | --- | --- | --- | --- | --- | --- |
| Deribit BTC | 1-7 days | 27.35 | 19.17 | 35.31 | 42.19 | 38.09 |
| Deribit BTC | 8-21 days | 21.46 | 14.41 | 26.73 | 27.18 | 30.54 |
| Deribit BTC | >= 22 days | 51.18 | 66.42 | 37.96 | 30.63 | 31.38 |
| S&P 500 | 1-7 days | 21.86 | 21.21 | 23.43 | 28.01 | n/a (data to 2020) |
| S&P 500 | 8-90 days | 66.95 | 67.43 | 61.30 | 54.33 | n/a |
| S&P 500 | >= 91 days | 11.19 | 11.37 | 15.27 | 17.66 | n/a |

Row sums reproduce to 100.00 +/- 0.01 from the printed cells.

**Table 2 - volume by moneyness (percent of total) and totals.** Deribit call shares (DOTM, OTM, ATM, ITM, DITM) 2017: 2.86, 13.93, 26.27, 14.47, 3.53 (sum 61.06); 2018: 18.44, 21.66, 16.24, 7.20, 1.61 (65.15); 2019: 14.62, 21.12, 12.86, 4.46, 1.16 (54.22); 2020: 12.74, 21.74, 14.39, 3.38, 1.04 (53.29); 2021: 13.71, 22.61, 12.87, 2.54, 0.71 (52.44). Put shares 2017: 10.34, 16.85, 9.10, 2.13, 0.53 (38.94); 2018: 7.75, 13.24, 7.73, 4.05, 2.08 (34.85); 2019: 13.83, 20.15, 9.11, 2.17, 0.52 (45.78); 2020: 12.78, 21.41, 11.04, 1.28, 0.20 (46.71); 2021: 13.43, 23.01, 9.74, 1.12, 0.25 (47.56, printed row sums to 47.55 - a 0.01 rounding residual, recorded). Totals in USD billions: 0.16 + 0.10 = 0.26 (2017), 0.93 + 0.50 = 1.43 (2018), 4.27 + 3.60 = 7.87 (2019), 23.59 + 20.68 = 44.27 (2020), 53.99 + 48.97 = 102.96 (2021 YTD). Contract counts in millions: 0.02 + 0.02 = 0.04 (2017) and 2.36 + 2.08 = 4.44 (2020), matching the Section 2 prose "increases 111-fold from 0.04 million in 2017 to 4.4 million in 2020" (4.44 / 0.04 = 111) and "increases 400-fold, from only 0.26 USD billion in 2017 to 102.96 USD billion in 2021" (102.96 / 0.26 = 396, rounded to 400 in the prose).

**Table 3 - realised volatility, implied volatility, volatility spread (VS = RV - IV), annual averages.**

| Year | BTC RV | BTC IV | BTC VS | S&P RV | S&P IV | S&P VS | S&P IV correlation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2017 | 0.93 | 1.05 | -0.12 | 0.08 | 0.17 | -0.09 | 0.02 |
| 2018 | 0.85 | 0.97 | -0.12 | 0.17 | 0.20 | -0.03 | -0.02 |
| 2019 | 0.65 | 0.80 | -0.15 | 0.15 | 0.19 | -0.04 | 0.07 |
| 2020 | 0.64 | 0.76 | -0.12 | 0.32 | 0.31 | 0.002 | 0.17 |

**Table 4 - implied-volatility curve, level / left slope / right slope (scaled by ATM IV).** Deribit: 2017 0.996 / -0.035 / 0.045; 2018 0.868 / -0.026 / 0.050; 2019 0.716 / -0.032 / 0.023; 2020 0.618 / -0.081 / 0.039; four-year mean 0.799 / -0.044 / 0.039. S&P 500: 0.108 / -0.312 / -0.200; 0.142 / -0.296 / -0.166; 0.142 / -0.285 / -0.180; 0.247 / -0.284 / -0.176; mean 0.160 / -0.294 / -0.180. Supporting prose: realised skewness -0.0715 for bitcoin against -0.732 for the S&P 500.

**Table 5 - information content of option trading volume (Delta-v) and aggregate order imbalance (N).** Specification `x_t = gamma_0 + gamma_1 x_{t-1} + gamma_2 y_{t-1}`; `***` marks the 1 percent level as printed; the table prints **no standard errors, t-statistics, R-squared or Nobs**.

| x | Horizon | y = Delta-v: gamma_0 | gamma_1 | gamma_2 | y = N: gamma_0 | gamma_1 | gamma_2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Return | 1-Hour | 0.0001*** | -0.053*** | **0.27*** | 0.0001*** | -0.053*** | 8.43e-7 (ns) |
| Return | 1-Day | 0.002*** | -0.084*** | **0.51*** | 0.0016*** | -0.086*** | -1.38e-6 (ns) |
| Return | 5-Days | 0.016*** | -0.025 (ns) | 0.068 (ns) | 0.018*** | -0.0027 (ns) | -6.08e-6 (ns) |
| IV | 1-Hour | -0.0019*** | -0.42*** | **4.27*** | -0.0021*** | -0.42*** | **6.36e-5*** |
| IV | 1-Day | -0.0036*** | -0.067*** | **3.32*** | -0.0055*** | -0.11*** | **3.96e-5*** |
| IV | 5-Days | -0.0077 (ns) | 0.14*** | 1.73*** | -0.010*** | 0.057 (ns) | 3.02e-6 (ns) |
| RV | 1-Hour | -1.02e-5*** | 0.034*** | **0.18*** | -1.49e-5*** | 0.031*** | **4.35e-7*** |
| RV | 1-Day | -0.0007*** | 0.41*** | **0.30*** | -0.0012*** | 0.39*** | **9.94e-6*** |
| RV | 5-Days | -0.0078 (ns) | 0.35*** | -0.48 (ns) | -0.014*** | 0.35*** | 2.89e-5*** |

Section 3 reading of this table: "hourly trading volume has a significant positive effect on returns and realised volatility over the next hour ... Hourly and daily net buying pressure also have a highly significant effect on both realised and implied volatilities. In contrast to trading volume, order imbalance during the hourly, daily or 5-day interval has no predictive power for returns over the next interval."

**Table 6 Panel B - average hourly net buying pressure (printed unit: USD), by year, Call / Put.**

| Moneyness | 2017 | 2018 | 2019 | 2020 | 2021 (to 28 Jul) |
| --- | --- | --- | --- | --- | --- |
| DOTM | 6 / -21 | -150 / -61 | -1,340 / -1,256 | -3,777 / -781 | -18,221 / -14,559 |
| OTM | -124 / 49 | -635 / -162 | -1,256 / -67 | -1,029 / -8,669 | 64,381 / -18,015 |
| ATM | 455 / -84 | 234 / 123 | 4,270 / 2,016 | 19,432 / -3,575 | 94,818 / 108,546 |
| ITM | 659 / 62 | 229 / -211 | 3,127 / 1,854 | 12,395 / 10,213 | 16,297 / -10,498 |
| DITM | 364 / 22 | 316 / 837 | 875 / 453 | 11,745 / 1,361 | 17,614 / -2,430 |
| Totals | 1,360 / 26 | -7 / 526 | 5,676 / 2,999 | 38,767 / -1,451 | 174,889 / 63,045 |

Panels A, C and D of the same table give net buying volume, directional net buying pressure for calls and volatility net buying pressure; the 2021 directional totals for calls are DOTM -1,498, OTM 41,198, ATM -6,864, ITM 13,397, DITM 10,022 (total 55,922) and the 2021 volatility totals are DOTM -16,390, OTM 23,183, ATM 101,682, ITM 2,900, DITM 7,592 (total 118,967). **Two prose cells contradict this table - recorded in the frontmatter.**

**Table 7 - Bollen-Whaley test (equation 4/5), selected alpha_5 (lagged change in implied volatility) values with Nobs.** ATM call: -0.458*** (2019, N=5,868), -0.426*** (2020, N=8,315), -0.395*** (2021, N=4,192). ATM put: -0.413*** (5,034), -0.399*** (7,883), -0.397*** (4,094). OTM call: -0.443*** (6,548), -0.431*** (8,581), -0.386*** (4,343). DOTM call: -0.430*** (5,040), -0.466*** (7,748), -0.419*** (4,214). Spot-volume control alpha_2 for ATM call: 0.067***, 0.116***, 0.041***. The paper compares these with "-0.17 ... for the S&P 500 options market in Bollen and Whaley (2004)" and "about -0.23 for TAIEX index options" in Chen and Wang (2017) - **values relayed from other papers, not computed here**.

**Table 8 - Chen-Wang test (equation 6), selected beta_3 (volatility-motivated demand) versus beta_4 (directional-motivated demand) with Nobs.** ATM call: 4.336*** vs 1.808 (ns) in 2019 (N=5,868); 0.720*** vs 0.086 (ns) in 2020 (N=8,315); 0.215*** vs 0.184** in 2021 (N=4,192). ATM put: 7.609*** vs 7.58 (ns) in 2019 (N=5,034); 1.000*** vs 0.349 (ns) in 2020 (N=7,883); 0.011 (ns) vs -0.243 (ns) in 2021 (N=4,094). OTM call: 6.594*** vs 1.685 (ns) in 2019 (N=6,550); 1.599*** vs 0.982*** in 2020 (N=8,581); 0.484*** vs 0.335*** in 2021 (N=4,343). DOTM call: 33.172*** vs 11.951* in 2019 (N=5,042); 6.970*** vs 7.018*** in 2020 (N=7,747); 2.493*** vs 1.756*** in 2021 (N=4,214). Section 5 summary: "Since for ATM, OTM and DOTM options the estimate of beta_3 is always greater than that of beta_4, volatility-motivated trades consistently dominate directional-motivated trades", and "We estimate a ratio beta_3/beta_4 about 3:2 for OTM calls" (the printed OTM-call cells give 6.594/1.685 = 3.9 in 2019, 1.599/0.982 = 1.6 in 2020 and 0.484/0.335 = 1.4 in 2021 - the year to which "about 3:2" refers is not stated; `underspecified`).

**Tables 9-11 - Chen-Wang test by maturity bucket, 2019 / 2020 / 2021 (beta_3 vs beta_4, Nobs).** Examples: 2019 ATM call [1,7] 6.855*** vs 5.322** (N=2,662), [8,21] 7.989*** vs -3.077 (ns) (N=2,056), >=22 1.857 (ns) vs 2.12 (ns) (N=2,453); 2020 ATM call [1,7] 1.717*** vs 0.779 (ns) (N=6,834), >=22 0.338 (ns) vs 0.009 (ns) (N=4,756); 2021 ATM call [1,7] 0.153 (ns) vs 0.442** (N=3,620), >=22 0.121 (ns) vs 0.286*** (N=3,332); 2020 OTM call [1,7] 5.168*** vs 2.946*** (N=7,408) and >=22 0.623 (ns) vs 0.74* (N=5,031); 2020 DOTM put [1,7] 20.181*** vs 14.017*** (N=5,704) and >=22 3.667** vs 2.756* (N=3,465). Section 5 reading: "volatility-informed traders prefer short-term and medium-term options ... In 2020, trading on longer-term ATM options only supports the limits-to-arbitrage hypothesis, whereas it is directional trading that dominates prices of the longer-term OTM calls, and volatility information that drives the prices of longer-term DOTM puts ... overall they encompass less informed trades than short- and medium-term options."

**Table 12 - average net buying pressure by UTC time slot (Call / Put).** 2020 Panel A: Asia 331.96 / -134.49, Europe 804.47 / 473.04, US 118.93 / -358.11. 2021 Panel A: Asia 1,854.06 / 459.91, Europe 1,856.20 / 1,070.60, US 448.06 / 42.02; 2021 Panel B (directional, calls): 697.08 / 396.61 / 203.02; 2021 Panel C (volatility): 1,156.99 / 1,467.21 / 245.04. Prose: "option trader's net buying pressure is much lower during US trading times ... directional-motivated demand is greatest during Asian trading times and volatility-motivated demand most evident during European trading times."

**Table 13 - time-of-day learning test, estimated on 2020 and 2021 only.** Directional coefficient beta_4 is significant for OTM calls in (0,8] (0.959***) and (16,24] (1.697***) but not in (8,16] (0.242 ns); for DOTM calls in (0,8] (6.510***) and (16,24] (9.339***) but not in (8,16] (0.596 ns); for ATM calls beta_4 is never significant (0.222, -0.561, 0.461 - all ns). Section 5 conclusion: "directional learning is only supported during Asian and US trading times."

**Sections 1-2 structural claims (source-reported):** Deribit "accounts for about 80% of bitcoin option trading volume across global exchanges"; 1- and 2-day options "constitute almost 20% of the total volume" on Deribit; bitcoin's total option volume grew 400-fold from 2017 to 2021 YTD; informed traders "only emerged after 2019"; the market's 1-7 day share rose from 19.17 percent (2018) to 38.09 percent (2021); bitcoin's ATM volatility "often around 100%" against "around 20% most of the time" for the S&P 500 (Section 6).

### Independently reproduced

not independently reproduced

### Negative evidence

1. **The direction-signed signal is null at every tested horizon:** Table 5 prints no star for `N` against returns at 1 hour (8.43e-7), 1 day (-1.38e-6) or 5 days (-6.08e-6), and Section 3 states outright that order imbalance "has no predictive power for returns over the next interval". Any directional alpha built on net buying pressure is therefore contradicted by the source's own headline table.
2. **The only significant return predictor is unsigned:** `Delta-v`, which carries no sign, so it cannot by itself support the source's "information about the future direction" sentence (recorded as a contradiction).
3. **No trading evidence whatsoever:** zero occurrences of `backtest`, `sharpe`, `cagr`, `drawdown`, `win rate`, `turnover`, `risk-adjusted`, `holding period`; no portfolio rule, no P&L, no benchmark. The single `abnormal return` occurrence is a suggestion that a strategy "could" be built.
4. **Zero cost modeling:** no fee schedule, bid-ask, slippage, fill, latency, participation or market-impact treatment (Provenance census) - a `data gap`, never a zero.
5. **No inference machinery:** `standard error` 0, `t-stat` 0, `p-value` 0, `r2` 0, `confidence interval` 0, `bootstrap` 0, `heterosked` 0, `newey` 0 - significance exists only as star levels, so no economic magnitude can be judged against its own uncertainty.
6. **Multiplicity uncontrolled:** Tables 5, 7, 8, 9, 10, 11 and 13 print several hundred starred coefficients across three years, three moneyness groups, three maturity buckets and three time slots with `benjamini`/`bonferroni`/`fdr` not present in the document at all.
7. **Sample window of the headline table unstated:** Table 5 never says which years or how many observations underlie its gamma estimates, nor which implied-volatility series `Delta-IV` refers to (no moneyness bucket is named for the IV/RV dependent variables).
8. **Frequency fragility acknowledged by the source:** results hold at 1, 4 and 8 hours "but not if we aggregate to the daily frequency", and the daily results are not published - so the effect dies at exactly the horizon a slower trader would use.
9. **Stale and truncated sample:** data end 28 July 2021 because later data were "confined to short-term options only"; more than five years of market structure (ETF era, multiple competing options venues, post-2021 regimes) is absent.
10. **2017-2018 suppressed:** the source reports "weak support for the limits-to-arbitrage hypothesis but ... no evidence of either directional or volatility learning" for 2017-2018 and does not print those results - a selection on the maturing period.
11. **Non-tradable data path:** the Deribit API "no longer provides historical data"; reproduction depends on Tardis or CoinAPI archives, and aggressor-side flags are the critical field.
12. **No causal identification:** "the regressions we perform are not designed to detect the direction of causality, and that is beyond the scope of this paper" - volume could rise because price moved, not the reverse.
13. **Simultaneity in the controls:** contemporaneous spot return and spot volume enter the implied-volatility regressions (equations 4-6), and the Table 5 design uses only lags of the predictors - the paper never establishes ordering between option flow and spot return within the same hour.
14. **Moneyness assignment is ad hoc by the source's own words:** "Using a 15-day realised volatility is, of course, ad hoc", with the robustness variants unpublished ("available from the authors on request").
15. **Normalised decompositions unpublished:** footnote 12 says the volume-normalised directional/volatility pressures are "qualitatively unchanged" but they are not shown.
16. **Delta truncation:** options with `|Delta| < 0.02` or `> 0.98` are excluded as stale/illiquid, so the extremes of the surface - where DOTM squeeze dynamics live - are removed from the very measure used to detect directional informed trading.
17. **Exchange-implied-volatility bounds** [0, 500] percent are used as a data filter; the source treats out-of-bound quotes as outliers rather than as a market state.
18. **Single venue and single underlying:** Deribit only, bitcoin only; no cross-venue option flow (OKX, LedgerX, Huobi and others are named as the other 20 percent but not analysed), no ethereum options although Deribit lists them.
19. **S&P 500 comparison is proprietary and truncated:** WRDS data end 2020 while the bitcoin sample runs to 2021, so the two markets are never compared over an identical window.
20. **Published-version text unverified:** the pinned arXiv v2 may differ from the Journal of Financial Markets article (abstract wording differs), so all numbers here are preprint numbers.
21. **Source-internal contradictions:** four are recorded in frontmatter (Table 6 prose year, Table 6 prose value and unit, data-cleaning arithmetic and percentage, Section 3 direction claim).
22. **The beta_3/beta_4 "about 3:2" summary does not reproduce for 2019** (3.9 from the printed cells) and the year it refers to is unstated.
23. **No independent replication, replication attempt or contrary published study on this mechanism was found in this run; absence is not evidence of no negative result.**

## Falsification plan

Every threshold below is **research-defined** (a Scout-chosen acceptance/failure cutoff) unless explicitly quoted from the source. Each gate names a fail condition and an action.

**No-retuning rule:** the hourly aggregation, equations (1)-(6), the delta-weighted construction of `N`/`A`/`D`/`V`, the 15-day realised-volatility moneyness mapping, the five delta bands with the [0.02, 0.98] truncation, the maturity buckets [1,7] / [8,21] / >=22 days, the spot-volume proxy of Bitstamp + Coinbase + Gemini, the 1-hour / 1-day / 5-day lags, the 2019 / 2020 / 2021-YTD sub-periods, the 2021-07-28 sample end and every F-threshold below are **frozen**. Any change requires a new record; results from a changed configuration may not be used to rescue a failed gate.

- **F1 - printed-value reproduction.** Fail condition: any cell of Tables 1-13 re-extracted from the pinned PDF differs from this record. **Action:** halt, mark the record unreliable, correct or withdraw it before any further use.
- **F2 - data-cleaning arithmetic gate.** Fail condition: the printed 3,431,071 -> 3,427,160 transition cannot be reproduced from the two stated exclusion rules, or 2,447 / 3,431,071 does not equal the printed percentage. **Status: currently FAILING** (688-trade gap; 0.071 percent vs printed 0.71 percent). **Action:** treat all level counts as approximate, never quote the printed cleaning percentages, and require re-derivation from raw trades in any replication.
- **F3 - prose-versus-table identity gate.** Fail condition: a Section 3 numerical sentence does not hold in Table 6. **Status: currently FAILING** (two cells). **Action:** table cells are truth; no claim in this record may rest on the Section 3 narrative numbers.
- **F4 - direction-channel null replication (research-defined).** Fail condition: on a fresh Deribit sample, the lagged signed aggregate `N` predicts next-hour or next-day BTC spot return with |t| >= 2.0 in the Table 5 specification. **Action:** if it *fails to reach* |t| >= 2.0 at 1 hour and 1 day (the expected outcome given the source), the directional hypothesis is rejected and the record keeps only the volatility channel; if it *does* reach it, the source's own null is overturned and the record must be rewritten as contested in the other direction. Either way, no directional adoption without a separate cost gate.
- **F5 - volume-channel replication (research-defined).** Fail condition: the sign of `gamma_2` for `Delta-v` against 1-hour and 1-day returns is not positive in the frozen specification, or |t| < 2.0 at either horizon. **Action:** drop the volume-to-return channel entirely; retain only the volatility channel.
- **F6 - volatility-channel replication (research-defined).** Fail condition: lagged `N` fails to predict 1-hour and 1-day `Delta-IV` and `Delta-RV` with |t| >= 2.0 and the same sign as Table 5. **Action:** reject the volatility channel and reduce the record to a market-structure note with no tradable content.
- **F7 - placebo gate (research-defined).** Fail condition: the real `gamma_2` is not above the 95th percentile of 1,000 permutations of the lagged predictor across hours (circular block shuffle of 24-hour blocks to preserve intraday seasonality). **Action:** treat the effect as seasonality artefact and stop.
- **F8 - frequency-stability gate (source-anchored).** Fail condition: the effect does not replicate at 4 and 8 hours, the two frequencies the source explicitly claims to be robust at. **Action:** classify the result as a sub-hour microstructure artefact; no adoption claim above 1-hour horizons.
- **F9 - cost-hurdle gate (research-proposed).** Fail condition: charging a research-defined cost ladder of {0, 1, 2, 5, 10} bps per side on the spot/perpetual leg plus research-defined option half-spreads of {5, 10, 20, 50} vol-points and one round trip of delta rebalancing per hour makes the frozen volume-conditioned rule's expected value <= 0 at every rung. **Action:** record stays research-only permanently; no implementation candidate may advance on coefficient significance alone.
- **F10 - executability / data gate.** Fail condition: Deribit tick data with aggressor-side flags cannot be obtained for the sample (API no longer serves history; Tardis/CoinAPI access unverified), or the aggressor flag is missing for more than 5 percent of trades (research-defined). **Action:** the record is marked permanently non-reproducible and cannot support any adoption decision.
- **F11 - multiplicity gate (research-defined).** Fail condition: fewer than half of the starred cells in Table 5 survive Benjamini-Hochberg at q < 0.10 across the 18 Table-5 cells (3 horizons x 3 dependent variables x 2 predictors). **Action:** withdraw all significance language; keep only effect directions.
- **F12 - sub-period and regime stability (research-defined).** Fail condition: the sign of the frozen 1-hour `Delta-v` -> return coefficient flips across the 2019 / 2020 / 2021 sub-periods, or does not persist in a frozen 2021-08-01 to 2026-09-30 forward window. **Action:** classify the original result as a single-regime artefact of the 2021 bubble; record remains research-only.

Action on failure for every gate: retain the record as research-only, record the failure in this record's negative evidence, and do not retune the frozen configuration post hoc.

## Crypto portability

**direct** - the source is crypto-native: Deribit bitcoin options tick trades and a bitcoin spot index, 24/7, with crypto-specific features (1- and 2-day expiries, up to 100X leverage, bitcoin-cash settlement, [0, 500] percent IV bounds) analysed as first-class facts rather than as an adaptation.

- **What ports as-is:** the delta-weighted aggressor-side imbalance construction, the Chen-Wang directional/volatility decomposition, the moneyness and maturity bucketing, the hourly aggregation and the Bollen-Whaley/Chen-Wang regression family. They require only a venue that publishes trade-level aggressor direction.
- **What is crypto-specific here:** the result that *volatility* learning dominates *directional* learning is explicitly contrasted with developed equity-index option markets and is attributed to bitcoin's jumps, unclear fundamentals and segmented derivatives venues - it should not be assumed to transfer to equity or FX options.
- **Spot vs perpetual:** the source's return leg is the Deribit **bitcoin index spot** return. Porting the directional read to perpetual futures introduces funding, mark/index divergence, liquidation mechanics and leverage that the source never models (`funding` 0 occurrences) - any perpetual port is an `adapted` extension of this record, not evidence from it.
- **Venue fragmentation:** Deribit was about 80 percent of BTC option volume when written; today's share, competing venues (OKX, Binance, Bybit) and on-chain/perp-option hybrids are `data gap`.
- **Data risk in crypto specifically:** historical Deribit tick data with aggressor flags are no longer served by the exchange API; the source's own recommendation (Tardis, CoinAPI) is commercial. Surviving-venue and delisted-expiry selection are unaddressed.
- **24/7 sessions:** no session boundaries, but time-of-day effects are real in this data (Table 12/13), so any binning must preserve UTC slots rather than exchange "sessions".
- Portability is not authorization to trade; no crypto backtest of this mechanism exists in our stack.

## Limitations

- **Source status:** arXiv preprint v2 (25 Mar 2022, manuscript dated 28 Mar 2022) of a peer-reviewed article (*Journal of Financial Markets* 63, 100764, March 2023); the pinned preprint carries no journal reference, and the published text was not retrieved, so table identity between versions is a `data gap`.
- **No trading layer:** entry, exit, sizing, holding period, order type, fill model and all costs are `not stated in source`; the paper is a price-discovery study and says so.
- **`data gap`:** construction of `Delta-v`; Table 5 sample window and Nobs; which IV/RV series the Table 5 dependent variables use; standard errors / t-statistics / R-squared anywhere; the daily-frequency results; the normalised `D/TV`, `V/TV` decompositions; the sigma-robustness variants for moneyness; the 2017-2018 regressions.
- **`underspecified`:** timezone/binning convention; whether "about 3:2" refers to 2019, 2020 or 2021; the manuscript-date versus v2-upload-date gap; the unit of Table 6 (USD) versus Figure 3 (USD million) for the same class of measure.
- **Four recorded source-internal contradictions** (frontmatter `contested: true`).
- **Null direction channel, positive volatility channel** - the two must never be reported as one result.
- **Horizon ceiling:** effects are documented at 1 hour / 1 day only, are explicitly not robust at daily frequency, and the source notes the information is "short-lived".
- **Single-venue, single-asset, 2017-2021 sample** ending before the spot-ETF era; 2017-2018 results withheld by the source.
- **Publication and selection bias:** only a favourable maturity window is shown; no pre-registration, no holdout, no walk-forward (`holdout`/`walk-forward` absent from the document).
- **Not independently reproduced;** every number above is third-party source-reported and is a coefficient, count or share, not a return.
- **Crypto porting of the directional channel to perpetuals or to other venues is `adapted`, not `direct`.**

## Implementation status

`not-implemented`. No implementation, backtest, prototype, paper trading or validation exists in our research stack. Nothing in Qlib, Paper, Testnet or Live has been touched by this record. The source ships no code and names no repository (`repository` 0, `github` 0, `code` 0), so there was nothing to run.

## Adoption boundary

This record is research material only. Its presence in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib full-backtest validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation; approved for paper trading; approved for testnet; approved for live trading.

## Related Wiki records

- Read-only Wiki Brain resolution on 2026-10-01: `quant/strategy-research-record-spec-v2.md` returned **file not found**, so this run failed closed onto `quant/strategy-research-record-spec-v1.md` (canonical, 10,289 bytes, SHA-256 `4561578a2a991aaa8252b31a8b6fd0a46b98c853ef77599521436ee6ff2fcaa7`). Resolution was done by read-only filesystem search of the local vault; **zero Wiki Brain pages were written.**
- Three verified existing Wiki pages are linked with the mechanism difference stated:
  - [[quant/bitcoin-option-rnd-low-volatility-high-vrp-regime-2026-09-01]] - bitcoin option risk-neutral-distribution / volatility-risk-premium **regime** signals read from the IV surface; same market (BTC options) but a **level/skew** signal for regime timing, whereas this record uses **aggressor-side trade flow** (delta-weighted imbalance) at hourly frequency.
  - [[quant/crypto-options-dvol-iv-premium-shock-spot-predictor-2026-09-13]] - Deribit **dvol index shocks** as a spot predictor; again an IV-level signal, not order-flow; different material data dependency (index quotes vs trade-level aggressor flags).
  - [[quant/hyperliquid-perpetual-order-flow-imbalance-depth-elasticity-nonlinearity-2026-09-13]] - order-flow imbalance as a mechanism, but on a **perpetual-futures CLOB** (spot/perp book depth and queue state), i.e. a different instrument class, different horizon and different data dependency from **option-trade** imbalance weighted by Black-Scholes delta.
- Repository-adjacent records (same checkout, different source identities and materially distinct mechanisms):
  - `retail-option-imbalance-slim-cross-section-us-equity-ssrn-6781743-2026-09-28` - **closest in mechanism, different on all other axes**: retail-signed option imbalance used as a **cross-sectional US-equity factor across stocks** versus delta-weighted aggressor imbalance as a **single-asset time-series predictor for bitcoin**; different market type (equity options vs crypto options), different signal construction (retail classification vs delta weighting), different material data dependency.
  - `crypto-multilevel-order-flow-imbalance-intraday-2026-08-31`, `crypto-world-order-flow-cross-sectional-quintile-weekly-2026-08-31`, `crypto-nonlinear-multifiat-order-flow-ml-daily-quintiles-2026-09-03` - all three are built on Anastasopoulos et al., "Order flow and cryptocurrency returns", *Journal of Financial Markets* 79 (2026) 101047: **spot/futures order flow over a cross-sectional crypto panel** at daily/weekly horizons, versus **option-trade order flow on one asset** at hourly horizons with a volatility (IV/RV) target; different source identity, instrument class, horizon and target variable.
  - `bitcoin-options-dealer-gamma-exposure-gex-regime-2026-09-01` and `bitcoin-option-expiry-gamma-intraday-spot-reversal-2026-09-21` - dealer **positioning/gamma-exposure** mechanics derived from open interest and expiry calendars, not from aggressor-signed trades; different data dependency (open interest vs trade side).
  - `crypto-multilevel-order-flow-imbalance-intraday-2026-08-31` and `binance-perpetual-order-flow-imbalance-horizon-decay-queue-imbalance-falsification-2026-09-13` - book-level OFI with queue state on perpetuals; different instrument, different construction (book depth imbalance vs trade imbalance), different universe.
  - `crypto-options-implied-correlation-dispersion-2026-08-31`, `ophr-multi-agent-options-volatility-trading-hedger-routing-deribit-2026-09-25` - options records that share the venue but study cross-sectional IV dispersion and multi-agent hedging/routing respectively, with no aggressor-flow signal.
  - None of these shares this source identity (arXiv:2109.02776 / DOI 10.1016/j.finmar.2022.100764), and none studies delta-weighted **option** net buying pressure as an hourly predictor of **bitcoin spot return and volatility**.

## Sources

1. Alexander, C., Deng, J., Feng, J., & Wan, H. (2022). "Net Buying Pressure and the Information in Bitcoin Option Trades." arXiv:2109.02776v2 [q-fin.GN], v1 submitted 6 September 2021, v2 submitted 25 March 2022, manuscript dated 28 March 2022, 35 pages, CC BY-SA 4.0. Abstract: `https://arxiv.org/abs/2109.02776`; pinned PDF (1,439,561 bytes, SHA-256 `6fbd49f8f551813a6e622777e16160ef20e176b2247afe1aa5ffcd59ad377432`): `https://arxiv.org/pdf/2109.02776v2`. All quantitative claims in this record trace to Tables 1-13, Sections 1-6 and footnotes 1-13 of that preprint and are labelled source-reported.
2. Published version (metadata only, used for publication-status verification): Alexander, C., Deng, J., Feng, J., & Wan, H. (2023). "Net buying pressure and the information in bitcoin option trades." *Journal of Financial Markets*, 63, 100764. DOI `https://doi.org/10.1016/j.finmar.2022.100764` (Crossref registry record retrieved over HTTPS on 2026-10-01, together with the SSRN preprint record `https://doi.org/10.2139/ssrn.3915901`). The published text and tables were **not** retrieved; no claim in this record rests on them.
3. arXiv API record used only for version/date/publication-status verification: `https://export.arxiv.org/api/query?id_list=2109.02776` (2,260 bytes, SHA-256 `9d0b494a53a0b36a34b4c18f16c5595d8486424cf9a5f5d7de56a36b1110270d`).
4. Data archives named by the primary paper (used by it, not directly by us): Deribit historical option trades via Tardis and CoinAPI (commercial), and Wharton Research Data Services for the S&P 500 index-option comparison sample.
