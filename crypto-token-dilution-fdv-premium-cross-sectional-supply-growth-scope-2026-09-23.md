---
schema: strategy-research-record-v1
title: Crypto Token Dilution Premium — FDV Premium and 12-Week Dilution Rate Cross-Sectional Short-Side Characteristic with Blue-Chip and Coin-Age Scope Boundaries
created: 2026-09-23
updated: 2026-09-23
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-03-31
sources:
  - "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6636258"
  - "https://doi.org/10.2139/ssrn.6636258"
  - "https://papers.ssrn.com/sol3/Delivery.cfm/6636258.pdf?abstractid=6636258&mirid=1&type=2"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Token Dilution Premium — FDV Premium and 12-Week Dilution Rate Cross-Sectional Characteristic with Blue-Chip / Coin-Age Scope Boundaries

## Provenance

- **Primary source (pin version):** Yulin Guo (sole author; affiliation on source: Peking University HSBC Business School), *"Token Dilution and the Cross-Section of Cryptocurrency Returns."*
- **Stable identifiers:** SSRN abstract_id `6636258`; DOI `10.2139/ssrn.6636258`. SSRN landing states **63 Pages, Posted 24 Apr 2026, Last revised 20 May 2026, Date Written April 22, 2026**; the pinned PDF cover is dated **May 20, 2026**.
- **Primary-source checksum (performed 2026-09-23, SSRN Delivery PDF read in-browser after Cloudflare clearance):** 462,351 bytes, `sha256 a3256518645be2a2739e6a82c67683d5318978f9739183b0824cee422c9e76f3`, **63 pages**. The **complete text** (Abstract; §1–§7; Eqs. 1–17; Tables 1–13; Internet Appendix Tables IA.1–IA.6; references) was read, plus the SSRN landing page (author block, page count, posted/revised dates, license `"No reuse allowed without permission"` → this record only normalizes citation and does not reproduce the work).
- **Author list exactly as source:** *Yulin Guo* (single author), confirmed on both the PDF cover (page 1) and the SSRN author block.
- **Publication / review status:** **SSRN working paper / preprint.** No journal reference, forthcoming notice, or peer-review statement appears on the landing page or in the pinned PDF → journal status `data gap` (not stated in source).
- **Sample period / universe / cost treatment:** see `Required data` and `Execution assumptions`; all read from the pinned PDF Methods (§3), Results (§4–§6) and Internet Appendix, not from the abstract alone.
- **Source/data as-of:** weekly data **November 2020 – March 2026** (≈279 weeks) → `source_as_of: 2026-03-31` (data end, not posting date).
- **Source-identity deduplication (deterministic, whole repository, pre-write):** ripgrep across **all `*.md` records** for `6636258`, `10.2139/ssrn.6636258`, exact title `Token Dilution and the Cross-Section`, author `Yulin Guo`, plus mechanism keys `FDV premium`, `dilution rate`, `float ratio`, `circulating supply`, `fully diluted valuation`, `share issuance` → **no record cites this source identity; no existing record title covers token dilution / float / FDV**. Mechanism neighbors compared and listed in `Related Wiki records`; each differs in at least one of mechanism, signal construction, or source → genuinely new capture.

## Economic mechanism

### Source-reported

The author frames token supply expansion as the one component of a token's fundamental value that is governed by **publicly observable protocol rules and vesting schedules** rather than discretionary corporate decisions (§1). Under the rational benchmark of Cong, Li & Wang (2021) and Biais et al. (2023), announced dilution should already be in price, leaving no ex-post cross-sectional relation (§1, §2.2). The paper documents such a relation and attributes it to **limited investor attention**: converting public unlock information into a priced quantity is costly, and that interpretive attention concentrates in large-cap and mature tokens (§1, §5.4). The equity analogue is the share-issuance anomaly of Pontiff & Woodgate (2008) and Fama & French (2008) (§2.3). The author explicitly **rejects the mechanical price-pressure channel** (Brunnermeier–Pedersen 2009): the premium is not amplified in illiquid coins (§5.1, Table 9; Internet Appendix IA.3 double sorts). A **second, coexisting channel** is claimed: aggregate dilution-risk (dilution beta) carries a **positive** systematic premium interpreted (by the author, explicitly labeled *post hoc*, §4.7.2) as compensation for procyclical exposure (§4.7, Table 8).

### Research interpretation

Falsifiable form of the hypothesis (Scout normalization; labels explicit):

- **Characteristic channel (primary):** high expected/realized supply dilution (high FDV premium, high 12-week dilution rate) → **lower next-week cross-sectional returns**; a short-high-dilution / long-low-dilution weekly cross-sectional spread should be positive. Mechanism class: **behavioral under-reaction to public supply information (limited attention) under limits to arbitrage**, not risk compensation and not order-book pressure.
- **Scope prediction (falsifiable, source-reported as scope analysis §5.2–§5.3):** the characteristic effect should be **absent in the top-five blue-chip tokens** and **absent in coins listed ≥52 weeks**, i.e. it lives where attention/arbitrage capital are scarce.
- **Systematic channel (secondary):** a rolling 52-week two-factor **dilution beta** should earn a positive risk premium *net of* the characteristic measures (§4.7). Whether this channel is risk or mispricing is contested inside the source itself (author calls the reading post hoc, §4.7.2).
- Component roles for any future tradable test: *Universe scope* (non-blue-chip, early-life coins) + *level signal* (FDV premium) + *flow signal* (12-week dilution rate) + *risk/neutralizer* (size control via conditional sorts). Do not assume each contributes — ablation is required (see `Falsification plan`).

## Signal

All operational items below are **source-reported** unless tagged `research-proposed`:

- **Formation timestamp:** all independent variables measured at **end of week t** and lagged one week relative to dependent weekly return (§3.4: "All independent variables are lagged by one week … to avoid look-ahead bias"). Weekly frequency built from **end-of-week prices/market caps and summed daily volume** (§3.1). Timezone / candle-boundary convention for "end of week": `underspecified` (not stated in source).
- **Lookback:** dilution rate smoothing windows K ∈ {4, 8, 12} weeks, headline uses **12-week MA** of the weekly % change in circulating supply (Eqs. 3–5); momentum control = 4-week cumulative return (Eq. 7); volatility control = 4-week std (Eq. 8); Amihud ILLIQ (Eq. 9); turnover (Eq. 10). Minimum data requirement: ≥26 weeks per coin (§3.1). Endpoint inclusivity: `underspecified`.
- **Level signals:** `FloatRatio = CirculatingSupply / MaxSupply` (Eq. 1; total supply used when no max, e.g. ETH); `FDV Premium = FDV / MarketCap = MaxSupply / CirculatingSupply` (Eq. 2); FDV premium is `1/FloatRatio` but is the dominant level predictor after winsorization (§3.2, §4.6).
- **Flow signal:** `DilutionRate = (CircSupply_t − CircSupply_{t−1}) / CircSupply_{t−1}`, smoothed 12 weeks (Eqs. 3–5). Circulating supply is **derived** as `MarketCap / Price` because historical supply is paywalled at the CoinGecko Analyst tier; validated against the Bitcoin halving schedule (derived BTC dilution ≈0.83%/yr, §3.2.3).
- **Portfolio construction (source-reported, §4.1–§4.2):** each week, equal-weight sort all sample coins into quintiles on the lagged dilution measure → **Q1 = low dilution (long side), Q5 = high dilution (short side)**; weekly next-period returns; headline spread **Q1 − Q5**, annualized as `weekly mean × 52 × 100`. **Conditional variant:** first tercile-sort by lagged size (log mcap), then quintile-sort by the dilution measure within tercile, average across the three size groups. Newey–West standard errors with 4 lags throughout.
- **Regression form (source-reported, §4.3–§4.4):** weekly Fama–MacBeth cross-sections, `r_{i,t} = γ0 + γ1·Dilution_{i,t−1} + γ′·X_{i,t−1} + ε` (Eq. 11), controls = size, 4-week momentum, 4-week volatility, Amihud ILLIQ (+ turnover in the paired models). **Paired design:** Model A = FloatRatio + Dil12w + controls (Eq. 12); Model B = FDV Premium + Dil12w + controls (Eq. 13) — the two level measures are never entered together (multicollinearity, §4.4).
- **Systematic signal (source-reported, §4.7):** value-weighted aggregate dilution rate → AR(1) residual = dilution innovation η_t (Eq. 15, φ1 = −0.367, t = −6.56, R² 0.135, Internet Appendix IA.2) → per-coin rolling **52-week** two-factor beta β_DIL (min 26 obs, Eq. 16) → weekly quintile sort on lagged β_DIL (Table 7).
- **Cleaning (source-reported, §3.4):** drop weekly returns < −90% or > +1000%; cross-sectional winsorization at 1st/99th percentiles within each week (sensitivity at 0.5/99.5 and 2.5/97.5 in IA.5).
- **Entry/exit/holding mechanics for a tradable implementation** (order type, fill price, rebalance timestamp, position limits, whether the Q1−Q5 spread is traded as such): the paper is an asset-pricing study and **does not specify a tradable execution recipe** → any concrete trading rule built on these sorts is `research-proposed` until specified; **not** source-reported.

## Required data

Source-reported (§3.1):

- **Universe:** top 500 coins by market cap from the **CoinGecko API** cross-sectional snapshot, **plus inactive/delisted coins** via `status=inactive` (explicit survivorship mitigation); excludes stablecoins (USDT/USDC/DAI/BUSD), wrapped and bridged tokens; ≥26 weeks of data; final **404 unique coins, average 220 coins/week, 61,464 coin-week observations, 279 weeks (Nov 2020 – Mar 2026)** (§3.1, Table 1 notes).
- **Venue / market type:** CoinGecko aggregate (tracking >18,000 coins on >1,000 exchanges, §3.1) — **spot-style aggregated market data; no single execution venue specified**; per `Required data` conventions this must be treated as multi-exchange aggregated spot, `underspecified` for any single-venue tradability.
- **Fields:** daily price, market cap, 24h volume (`/coins/{id}/market_chart`); cross-sectional circulating/total/max supply and FDV (`/coins/markets`), aggregated to weekly (§3.1).
- **Point-in-time:** `status=inactive` inclusion plus one-week lagging of all predictors (§3.4). Whether CoinGecko supply/FDV fields are point-in-time restated (backfilled/ revised) → **`data gap` / `underspecified`** (not stated in source); the derived-supply workaround (§3.2.3) inherits any such revisions.
- **Timestamp/timezone:** `underspecified` (weekly aggregation convention not pinned to a timezone in source).
- **Missing data:** coins with <26 weeks dropped; imputation not mentioned (and would be forbidden under the spec) → none stated.
- **Funding/fee/spread needs:** see `Execution assumptions` — none modeled.

## Execution assumptions

Read from the pinned PDF's Methods (§3), Results (§4–§6) and Internet Appendix; findings are direct observations of the pin version:

- **Signal-to-order timing / order type / fill model / latency / partial fills:** **not stated in source** → `data gap`.
- **Transaction costs, fees, bid-ask spread, slippage, market impact:** **no cost, fee, spread, slippage, funding, borrow, leverage or fill assumption appears anywhere in §3–§7 or the Internet Appendix**; every reported portfolio return (Tables 3, 4, 7, 10, 11, IA.3) is therefore a **gross, cost-unadjusted** figure (observation made on the pinned full text, not on the abstract). The only cost-adjacent content is (a) the Amihud ILLIQ and turnover **controls**, which are covariates, not cost models, and (b) a qualitative remark in §2.4 that "shorting costs are substantial and vary widely across coins" — acknowledged but **not modeled**. → costs = `data gap` / `not stated in source` for the backtest numbers.
- **Funding / liquidation (if ported to perpetuals):** not addressed at all → `not stated in source`.
- **Borrow / shorting availability for the Q5 (high-dilution) leg:** not addressed operationally; §2.4/§5.2–§5.3 instead argue the premium is concentrated in **small, early-life, hard-to-short** coins (Stambaugh–Yu–Yuan logic), which is itself a capacity/shortability warning.
- **Gross vs net:** all numbers are **gross-of-cost** (source never states otherwise and no cost line exists) — recorded as a direct full-text observation, `not stated in source` as an explicit label by the author.
- Any execution assumption added later by us (e.g., next-week-open fills, taker fees, borrow rates) must be labeled `research-proposed`.

## Evidence

### Source-reported

All figures below are third-party (`source-reported`), from the pinned SSRN PDF (63 pp., sha256 `a3256518…c9e76f3`), Nov 2020 – Mar 2026, 404 coins, weekly, **gross of any transaction cost**, Newey–West 4 lags:

- **Headline regression (Table 5, individual FM measures + controls):** FDV Premium coef **−0.000633, t = −3.13 (1%)**; Dilution Rate 12w coef **−0.218754, t = −2.62 (1%)**; Float Ratio **+0.006622, t = +1.96 (5%)**; raw rate t = −0.45; 4w t = −1.05; 8w t = −1.91.
- **Paired regressions (Table 6):** Dil12w **t = −2.79 (Model A)** and **t = −2.54 (Model B)**; FDV Premium in Model B **−0.000473, t = −2.43 (5%)**; Float in Model A t = +1.33 (insignificant); N = 61,464 / 404 coins / 279 weeks.
- **Unconditional quintile sorts (Table 3):** FDV Premium Q1 − Q5 = **+27.9%/yr, t = +1.43 (ns at 5%)** (Q1 81.9% vs Q5 54.1%); Dil12w Q1 − Q5 = **+25.0%/yr, t = +1.71 (10%)**; Float Ratio sort −27.6%, t = −1.44 (sign driven by size correlation, §4.1).
- **Size-conditional sorts (Table 4):** FDV Premium **+31.6%/yr, t = +1.72 (10%)**; Dil12w +22.3%, t = +1.45 (ns); Dil8w +22.6%, t = +1.28 (ns).
- **Value-weighted (Table 10):** full-sample VW FM collapses — FDV t = **−0.41**, Dil12w t = **−0.95** (Panel A); but **VW size-conditional FDV = +34.4%/yr, t = +2.03 (5%)** (Panel C).
- **Blue-chip exclusion (Table 11, VW, top-5 = BTC/ETH/BNB/XRP/SOL removed; 60,069 obs / 399 coins):** Dil12w **t = −2.43 (5%)**, 8w t = −1.94; paired Model B Dil12w **t = −2.03**; size-conditional sorts +28.9% (t = +1.47) and +25.5% (t = +1.63).
- **Lifecycle (Table 12, equal-weighted FM):** new coins (<52 wks): Float **t = +3.66**, FDV **t = −4.50 (1%)**, Dil12w **t = −2.55**; mature (≥52 wks): Float +0.33, FDV **t = −0.75**, Dil12w **t = −0.61** (obs 16,938 new vs 44,526 mature; same coin can be in both — within-coin design, §5.3).
- **Price-pressure rejection (Table 9):** standardized FDV×ILLIQ interaction t = **−0.54**, Dil12w×ILLIQ t = **+0.04**; main dilution effects stay significant (t = −2.08 / −2.58). Internet Appendix IA.3 3×3 double sorts: difference-in-differences across liquidity terciles **−19.03% (t = −0.75)** for FDV and **−17.76% (t = −0.82)** for Dil12w — gradient **opposite** to the price-pressure prediction (author notes a formal rejection would need a stronger sample).
- **Systematic dilution-beta channel (Tables 7–8):** quintile sort Q1 − Q5 = **−32.36%/yr, t = −2.78 (1%)** (Q5 +28.6% vs Q1 −3.8%); FM beta-only **+0.000206, t = +2.72 (1%)**, with controls **t = +2.10 (5%)**, with characteristics + controls **t = +1.76 (10%)**; β_DIL ⊥ β_MKT (avg ρ = +0.05); valid betas for 373 coins / 50,690 obs.
- **Robustness (Table 13, IA.1, IA.5, IA.6):** Dil12w negative in all 7 subsamples under both paired models, ≥5% in 5/7 (Model A); significance improves monotonically with smoothing window (IA.1: raw −0.45 → 4w −0.83 → 8w −1.81 → 12w −2.54); stronger, not weaker, under 2.5/97.5 winsorization (t = −3.11); Wald test fails to reject equality of the paired flow coefficient in all 7 subsamples (p 0.46–0.83 except middle-80%-by-size p = 0.072).
- **Descriptive anchors (Table 1):** mean weekly return 0.78% (sd 16.7%); mean FDV premium 2.76 (P95 7.79); mean Dil12w 0.56%/week ≈ 29%/yr.
- The paper reports **no Sharpe ratio, no drawdown, no turnover, no IC, no train/test split** for these portfolios → any such metric for this strategy is `data gap` / `not stated in source`.

### Independently reproduced

not independently reproduced.

### Negative evidence

- **Value-weighted full sample is a null** (Table 10 Panel A: FDV t = −0.41, Dil12w t = −0.95) — the premium exists only outside the top-5 coins and in early-life coins (Tables 11–12). A naive full-universe VW implementation would find nothing.
- **Unconditional sorts barely clear conventional significance** (FDV t = 1.43; Dil12w t = 1.71 only at 10%); only the size-conditional and scope-restricted variants reach 5% (Table 4, Table 10C, Table 11A/B).
- **Mature coins (≥52 weeks): every dilution measure collapses** (FDV t = −0.75/−0.44 paired; Dil12w t = −0.61/−0.64, Table 12) — for the bulk of a typical investable universe the effect is statistically indistinguishable from zero.
- **Raw and 4-week dilution rates are noise** (t = −0.45 / −1.05, Table 5; IA.1); the signal needs ≥12 weeks of smoothing.
- **Float ratio sign flips** in the unconditional sort (−27.6%, t = −1.44, Table 3 Panel A) and is insignificant in the paired design — level-measure choice materially changes results (§4.4, §4.6).
- **Dilution-beta premium is fragile:** falls to t = +1.76 (10%) once characteristics are added (Table 8 col. 3), and the author explicitly labels the procyclical-risk interpretation **post hoc** with alternatives "cannot be fully ruled out at weekly frequency" (§4.7.2).
- **Mechanism identification is indirect:** limited attention is inferred from where the premium lives, not measured (§7 limitations); correlated early-life frictions (larger unlock events, higher retail share, greater shorting frictions) are **not excluded** (§5.3, §7).
- **Costs & shortability:** gross returns only; the premium concentrates in small, new, hard-to-short coins (§2.4 acknowledges shorting costs are substantial and variable) — no borrow, funding, spread or impact model anywhere in the pin version → the 25–34% spreads are not net-of-cost evidence.
- **No out-of-sample design, no holdout, no multiple-testing control:** the paper runs full-sample FM/sorts plus 7 subsamples, 3 winsorization cutoffs and an Internet Appendix, with **no DSR/FDR correction and no frozen test window** — a multiple-testing concern given Hou–Xue–Zhang (2020), which the paper itself cites for scope mapping.
- **Publication-decay risk flagged by the author:** McLean–Pontiff (2016) decay after publication is posed as an open future test (§7) — not yet evidence either way.
- **Measurement layer:** single data source; circulating supply is *derived* (Mcap/Price) and validated only against the Bitcoin schedule; on-chain cross-validation absent (§7).

## Falsification plan

Each test: data / sample / metric / threshold / action. All thresholds are **`research-defined falsification threshold`**; any construction choice not in the source is **`research-proposed`**.

1. **Point-in-time data audit (prerequisite).** Rebuild the panel with point-in-time CoinGecko supply/FDV snapshots (or an on-chain supply series). If FDV premium / Dil12w series materially differ from the derived series (correlation < 0.9 `research-defined`), treat the original signal as data-revision-contaminated and stop.
2. **True out-of-sample freeze.** Freeze signal definitions now; evaluate 2026-04 → 2027-03 (never used by the source). **Failure rule (`research-defined`):** one-sided FM t-statistic on Dil12w < 2.0 **or** size-conditional Q1−Q5 annualized spread ≤ 0 → reject tradability claim; if t < 1.64 the hypothesis is marked weakened and not advanced.
3. **Cost ladder (gross → net).** Re-run the weekly size-conditional sort under 5 / 10 / 20 / 50 bps per side plus modelled spread and small-cap borrow fee. **Failure rule (`research-defined`):** the Q1−Q5 spread turns negative at ≤ 20 bps/side → reject as tradable; report at which rung it dies.
4. **Short-leg feasibility.** For each Q5 name, require an actual borrow/perp short quote at signal time. **Failure rule (`research-defined`):** < 70% of Q5 notional shortable → the long-short claim is untestable as stated; fall back to a long-only low-dilution test and re-report.
5. **Scope ablation (does the boundary carry the alpha?).** Re-estimate the spread (a) full universe, (b) ex-top-5, (c) <52-week coins only, (d) EW vs VW, (e) size-conditional vs unconditional. **Prediction from source (weaker claims must hold):** effect present in (b)/(c) and absent/unsignificant in the blue-chip VW segment. If it is strongest exactly in blue chips VW → mechanism claim falsified.
6. **Component ablation for the hybrid.** Standalone FDV, standalone Dil12w, both, and each + size conditioning. **Failure rule (`research-defined`):** if the composite adds < 20% to the t-stat of the best single component, the "level × flow" framing is not supported — keep only the surviving component.
7. **Placebo / shuffled label.** Permute dilution labels within size terciles × age bucket, 1,000 draws. **Failure rule (`research-defined`):** real spread within the placebo 95% interval → reject.
8. **Mechanism discrimination (attention vs price pressure vs risk).** Re-run Dil×ILLIQ interactions and the 3×3 liquidity double sort. **Failure rule (`research-defined`):** premium significantly *larger* in the illiquid tercile (DiD > 0, p < 0.05) → the source's price-pressure rejection fails and the mechanism label must be rewritten.
9. **Direct attention proxy test.** Interact the signal with measurable attention (Google Trends / aggregator page views / analyst-coverage proxy). **Failure rule (`research-defined`):** premium flat or larger where attention is high → limited-attention story falsified.
10. **Risk-vs-mispricing (characteristic conditioning).** Test whether the spread survives controlling for β_DIL, size, momentum, and downside beta simultaneously. **Failure rule (`research-defined`):** FM t on the dilution characteristic < 1.96 once covariance controls are in → reclassify from mispricing to risk-compensation (or noise).
11. **Multiple-testing control.** Deflated Sharpe / BHY correction across the full spec grid (7 subsamples × 3 measures × 2 weightings × 3 winsorizations). **Failure rule (`research-defined`):** FDR-adjusted q > 0.10 for the headline claim → downgrade to exploratory.
12. **Post-publication decay watch** (the paper's own open question, §7): rolling yearly t-statistics; **failure rule (`research-defined`):** two consecutive calendar years with t < 1.0 → treat as decayed.

## Crypto portability

**direct** — the source is itself a cryptocurrency cross-sectional study (CoinGecko universe, 2020–2026 crypto spot data); no porting of an equity mechanism is required. Caveats that still bind (each `underspecified` or explicit in source):

- **Spot vs perpetual:** results are on aggregated **spot-style** market data; whether the premium transfers to perp pricing (with funding, mark/index basis) is untested → if traded on perps, that adaptation is `research-proposed`, and any funding/borrow cost model is ours, not the source's.
- **24/7 session:** weekly bar boundaries/timezone not pinned by the source; candle-boundary choice can move end-of-week returns → `underspecified`.
- **Venue fragmentation:** signal data are CoinGecko aggregates across >1,000 exchanges; tradability at any single venue (depth, listings, delistings) is untested; the sample deliberately includes **delisted/inactive** coins, so live implementability of the short leg on those names is impossible (they stop trading) — a genuine backtest-vs-live divergence.
- **Funding / borrow / liquidation:** not modeled anywhere; shorting the high-dilution leg in small new coins is exactly where §2.4 says shorting costs are substantial and heterogeneous.
- **Survivorship/point-in-time:** mitigated by `status=inactive` inclusion (§3.1) but supply-field point-in-time revisions are `data gap`.
- **Stablecoin/quote effects:** stablecoins and wrapped/bridged tokens excluded (§3.1); results do not speak to them.
- **Crypto portability ≠ authorization to trade** (spec: portability is not approval).

## Limitations

- `data gap`: **no transaction cost / spread / slippage / funding / borrow / fill model anywhere in the pinned full text** — all portfolio numbers are gross (direct observation of §3–§7 + IA; the author never states a cost assumption → `not stated in source`).
- `data gap`: no Sharpe, drawdown, turnover, IC, capacity or capacity-related statistic reported; no tradable execution recipe (order type, fill timestamp, holding rule beyond weekly rebalance of sorts).
- `underspecified`: weekly bar timezone/boundary; endpoint conventions; point-in-time behavior of CoinGecko supply/FDV fields; single-venue tradability; journal/peer-review status.
- `data gap`: journal status / peer review not stated (SSRN working paper only).
- `not independently reproduced`: no figure here has been reproduced by us; no code or data release is identified in the source (code availability: `data gap`).
- Identification: limited-attention mechanism is indirect (§7); early-life confounds not excluded (§5.3); dilution-beta risk reading admitted post hoc (§4.7.2).
- Statistical: full-sample in-sample design, no holdout, no DSR/FDR across an extensive spec grid; unconditional sort significance is weak; headline 25–34% spreads come from variants (size-conditional / scope-restricted / VW-conditional), not from the plain unconditional EW sort.
- Economic: premium concentrated in small, new, hard-to-short, partly delisted coins → capacity, borrow and delisting-attrition risk; value-weighted full-sample effect is null.
- Source-quality: preprint on SSRN, single author, single data vendor, derived supply measure validated only against Bitcoin's schedule.
- `unproven`: everything in this record remains unproven for our own system.

## Implementation status

`not-implemented`. No signal has been coded, no panel rebuilt, no backtest run, no prototype created in our research stack. Nothing here implies Qlib full-backtest validation, survivor status, or Paper/Testnet/Live activity — none has occurred.

## Adoption boundary

Research material only. Presence in this repository does **not** mean: passed Research Intake Review; entered Hermes Wiki Brain; entered the production candidate pool; completed Qlib validation; became a frozen survivor or leaderboard entry; profitable; validated alpha; approved for implementation, paper trading, testnet, or live trading. `status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. No wording, evidence count, or confidence value in this record promotes it.

## Related Wiki records

- `[[quant/strategy-research-record-spec-v1]]` — canonical schema this record conforms to (the only real Wiki link; this run wrote **nothing** to Wiki Brain).
- Mechanism neighbors found by pre-write search (**file names only — non-Wiki references, not written or updated by this run**):
  - `crypto-token-unlock-72h-supply-shock-event-short-2026-09-12.md` — Kim (2026), 72-hour **event-study short** on 52 discrete unlock events (GitHub `gameworkerkim/vibe-investing`). Different source and different mechanism: discrete event shock vs persistent cross-sectional supply characteristic; different horizon (72h event vs weekly recurring).
  - `crypto-cross-sectional-locked-supply-staking-conviction-2026-09-01.md` — To, SSRN 7314420, **locked supply / staking conviction** premium. Different source; complementary (lock-up) rather than dilution (unreleased float) signal construction.
  - `crypto-cross-sectional-dispersion-scaled-momentum-20d-daily-2026-09-01.md` — Zhang & Makgolo, SSRN 6648082, dispersion-conditioned **momentum** regime. Different source and demand-side signal; relevant only as a candidate control/conditioning variable.
  - `short-term-drawdown-reversal-walk-forward-timing-gated-calls-2026-09-11.md` — mentions FDV/mcap only as a `research-proposed` valuation guard, not as the primary signal; no shared source identity.
- Equity conceptual anchor (not a capture of the same source): Pontiff & Woodgate (2008) share-issuance anomaly is cited by the paper as motivation (§2.3); no repository record cites it as a primary source.

## Sources

1. Yulin Guo, *"Token Dilution and the Cross-Section of Cryptocurrency Returns,"* SSRN Working Paper, abstract_id **6636258**, DOI **10.2139/ssrn.6636258**; posted 24 Apr 2026, last revised 20 May 2026, Date Written 22 Apr 2026, 63 pages. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6636258 ; https://doi.org/10.2139/ssrn.6636258
2. Same paper, Delivery PDF (primary source actually read in full for this record): https://papers.ssrn.com/sol3/Delivery.cfm/6636258.pdf?abstractid=6636258&mirid=1&type=2 — 462,351 bytes, 63 pp., `sha256 a3256518645be2a2739e6a82c67683d5318978f9739183b0824cee422c9e76f3` (retrieved 2026-09-23). License: "No reuse allowed without permission" → citation/normalization only.
3. Data vendor named by the source (not an independent source of any claim here): CoinGecko API, `/coins/markets` and `/coins/{id}/market_chart` endpoints (§3.1).

All performance and statistical claims in this record are `source-reported` from item 1/2 with the Table provenance given inline; none has been independently reproduced.
