---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Faber GTAA 10-month SMA monthly regime long-flat on BTCUSDT 1d bars
created: 2026-10-13
updated: 2026-10-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2013-02-01
sources:
  - https://mebfaber.com/wp-content/uploads/2016/05/SSRN-id962461.pdf
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=962461
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Faber GTAA 10-month SMA monthly regime long-flat on BTCUSDT 1d bars

## Provenance

Primary source read end to end (author-hosted PDF fetched and verified 2026-10-13, 70 pages):

- Mebane T. Faber, `A Quantitative Approach to Tactical Asset Allocation` — May 2006 working paper; Spring 2007, The Journal of Wealth Management; February 2009 Update; February 2013 Update (this run pins the February 2013 update). Canonical file: https://mebfaber.com/wp-content/uploads/2016/05/SSRN-id962461.pdf (author-site mirror of the SSRN paper; title-page identity block `May 2006, Working Paper / Spring 2007, The Journal of Wealth Management / February 2009, Update / February 2013, Update` and `Electronic copy available at: http://ssrn.com/abstract=962461` verified in-text on p.1). Pinned bytes: 945,897 bytes, SHA-256 `f2dabb6d31b18901cb64a0f57cea86f32f514570dcb5840fbeaa4877f24bdd3f`.
- Pinned headline spec (2013 update, p.21, verbatim in sense): `BUY RULE — Buy when monthly price > 10-month SMA.` / `SELL RULE — Sell and move to cash when monthly price < 10-month SMA.` Model criteria (p.19): simple purely mechanical logic, the same model and parameters for every asset class, price-based only. The 10-month SMA is the paper's declared monthly equivalent of the 200-day SMA, chosen because daily history does not reach back far enough for many asset classes (FAQ, p.57).
- Pinned mechanics (p.22, all four numbered notes): (1) all entry/exit prices are on the day of the signal at the close and the model is updated only once a month on the last day of the month — intra-month fluctuations ignored; (2) all data series are monthly total-return series including dividends; (3) cash returns estimated with 90-day Treasury bills; (4) taxes, commissions, and slippage excluded.
- Pinned universe (STEP 1, p.13): five GFD total-return series since 1973 — US Large Cap S&P 500, Foreign Developed MSCI EAFE, US 10-Year Government Bonds, Commodities GSCI, Real Estate NAREIT; the GTAA timing sleeve (STEP 3) holds each sleeve long-or-cash with equal 20% weightings, rebalanced on the monthly grid.
- Bibliographic cross-check: SSRN abstract page https://papers.ssrn.com/sol3/papers.cfm?abstract_id=962461 (The Journal of Wealth Management, Spring 2007; suggested citation `Faber, Meb, A Quantitative Approach to Tactical Asset Allocation (February 1, 2013)`).
- Corroboration and post-sample assessment only (never rule provenance): Faber, `A Quantitative Approach to Tactical Asset Allocation Revisited 10 Years Later`, The Journal of Portfolio Management Multi-Asset Special Issue 2018 (13-page PDF fetched 2026-10-13: 1,760,315 bytes, SHA-256 `3465ff939e26e4001bba7c25d05506124c15fa0882af0dc57bf62921e2884284`): restates the identical buy/sell pair and supplies the out-of-sample discussion adopted under Negative evidence. Licence and rights: the paper is a published journal article — this record cites and normalizes the rule (short phrases and formulas only) and reproduces no figures, tables, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the paper's single-sleeve long-or-cash monthly regime ported to one crypto asset — not a lossless reproduction of the paper's five-class equal-weighted GTAA portfolio. Researcher-declared adaptations are exactly six: (1) single-asset BTCUSDT Binance perpetual (the five-class averaging, the 20% allocation sleeve, and every portfolio-level performance claim are fenced off, never carried — see Negative evidence 1); (2) plain month-end closes replacing the paper's total-return-including-dividends series (BTC pays no distributions; the paper's price-only criterion, p.19, supports the port — see Limitations); (3) cash mapped to flat with no yield (the paper's 90-day T-bill cash leg is fenced; no yield is invented or accrued — see Execution assumptions); (4) calendar-month decision grid on completed `1d` closes with next-open fills (the monthly cadence and last-day-of-month decision point are source-native; the paper's same-signal-day-close fill is fenced as an unmodellable same-bar assumption and replaced by the declared causal port); (5) an adopted 10-calendar-month warmup flat by record rule plus house fees/funding treatment replacing the paper's cost-excluded accounting (note 4, p.22); (6) fixed 100%-equity single-position sizing with no leverage (the paper sizes each sleeve at its allocation weight; one asset needs no cross-sleeve weighting). The 10-month SMA, the strict `>` / `<` comparison, the monthly update, the long-or-cash direction (the paper never shorts — direction is source-native, not a researcher pin), and the no-stop/no-target/no-trailing posture (the paper ships no stop concept anywhere — exits are signal-driven only) are source-faithful.

Pre-write dedup (2026-10-13): working-tree case-insensitive searches for `faber`, `tactical.asset`, `gtaa`, `10-month`, `10.month`, `moreira`, `muir`, `pi.cycle`, `hash.ribbon`, `mayer` return zero strategy records, and no filename carries a monthly-SMA-regime rule. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `tsmom-12m-sign-monthly-long-btcusdt-1d-2026-10-10.md` conditions its monthly hold on the sign of the trailing 12-month cumulative return — a raw return-ratio sign with no average anywhere (that record's own interpretation section distinguishes itself from moving-average signals, the class this record belongs to); `golden-cross-sma-regime-gated-long-btcusdt-1h-2026-10-08.md` fires on a fast/medium dual-average cross (9/50) gated by a third average's level on `1h` bars from a 2020 TradingView script — a cross event, never a price-vs-own-long-average monthly regime from a published paper; `nvi-255ema-regime-long-flat-btcusdt-1d-2026-10-12.md` keys off the Negative Volume Index against a 255-EMA; the calendar holds (`sell-in-may`, `january-barometer`, `monday-drift`, `turn-of-month-4day`, `pre-holiday-drift`, `fomc-pre-announcement-drift`) carry no price-conditioned leg at all. Five-axis distinction: no pool record and no open PR conditions a monthly-held position on the level of price against its own 10-month simple moving average.

## Economic mechanism

### Source-reported

Risk-reduction market timing, not return chasing: a mechanical trend filter that keeps the investor in the risky asset while it rides above its long average and exits to a risk-free asset when it breaks below, so that protracted bear markets are sidestepped at the cost of lagging roaring bull markets — the paper frames the result as equity-like returns with bond-like volatility and drawdown at the diversified-portfolio level (Abstract; STEP 2, pp.18–19 — portfolio-level claim, fenced, never adopted here). The paper is explicit that timing underperforms buy-and-hold in roughly half of all individual years (p.23) and that its value added appears only over full business cycles (p.25).

### Research interpretation

Monthly low-pass regime port: the 10-month average of month-end closes admits only persistent multi-quarter drift as exposure permission, while the once-a-month update with intra-month fluctuations ignored makes whipsaws structurally impossible inside the holding month — the strategy can be late by a whole month but can never overtrade one. Unlike return-sign momentum (TSMOM) there is no formation-ratio choice: the signal is a level comparison against a slow average. Unlike dual-average crosses (Golden Cross) there is no fast leg and no cross event: exposure is a state, re-decided monthly, held until the level reclaims or breaks. The bet, as derived, is purely on BTCUSDT riding above its own 10-month mean at monthly cadence, never on a return sign, band, oscillator, volume, calendar-seasonal, or funding anchor.

## Signal

Exact rule as pinned (10-month SMA, strict comparison, monthly grid — any other value is a different, unpinned rule):

- Decision bar: the last completed `1d` bar dated in calendar month T (month membership is the UTC calendar date of each daily bar — deterministic on the 24/7 tape).
- Level (pinned): `SMA10_T = mean of the 10 month-end closes of months T−9 … T` (simple average, closes only, no variant/smoothing choice left open).
- Position target for calendar month T+1 (pinned, strict): `C_T > SMA10_T` → long; `C_T <= SMA10_T` → flat (the equality leg is pinned to flat — measure-zero on live tape, no tie semantics beyond this; mirrors the paper's strict `>` / `<` pair with the gap closed by record rule).
- Orders (pinned): at most one order event per month, placed for the first `1d` open of month T+1 (next-open fill after the decision bar — the declared causal port of the paper's signal-day-close convention): flat→long target buys 100% equity; long→flat target closes all; unchanged target places nothing. No intra-month evaluation, no intra-month orders, no adds, no partials, no second decision inside month T+1 for any reason including large adverse excursion.
- Risk legs (pinned absence, not invented): the paper ships no stop/target/trailing/time-exit concept — the sole position-closing path is the next month-end signal mapping to flat. The derived posture is explicitly no stop, no target, no trailing, no intra-month exit; a month-long adverse move is ridden in full by construction.
- Direction: long-or-flat, source-native (the paper's sell leg is `move to cash`, never a short; the futures venue is still pinned as the research market under the house overlay with the short permission simply unused, and a spot-only deployment expresses the identical event set).

## Required data

- Completed `1d` closes of BTCUSDT only: ten month-end closes per decision (no `open` except as fill price, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, or cross-venue state gates any order). No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: calendar month. One evaluation per month on the last completed daily bar of the month; fills land on the next daily bar's open (first open of the new month). All formation inputs are completed-bar closes — no provisional month-end value is ever used.
- Warmup: ten full calendar months of `1d` bars before the first decision (all ten month-end closes must exist). Bars before the first decidable month-end are flat by record rule; no signal before the eleventh month-end may trade. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port; no cross-venue equivalence claimed).
- Order timing (declared causal port of the paper's monthly cadence): month-end completed-bar decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The paper's same-signal-day-close fill (note 1, p.22) is fenced, never assumed — no maker-touch, queue, or intrabar-path-dependent fill is claimed. At most one order exists per month, so there is no same-bar dual-fire to sequence.
- Cash leg: flat earns nothing by record rule. The paper's 90-day T-bill cash yield is fenced and never accrued; no stablecoin-lending, funding-rebate, or synthetic yield is substituted.
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity. The paper reports cost-excluded returns (note 4, p.22), so derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — long months carry realized funding, flat months carry none, and the form holds genuine flat months so it is never an always-in-position funding accumulator). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; re-entry after a flat month needs only the next positive month-end signal (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

The paper ships the full construction adopted here: the strict `>` / `<` 10-month-SMA pair (p.21), the once-a-month last-day update with intra-month fluctuations ignored (note 1, p.22), the same-model-every-asset price-only criteria (p.19), the five-class equal-weighted GTAA sleeve design (STEP 1 + STEP 3), and the structural trade facts that the S&P 500 timing sleeve sits invested approximately 70% of the time at less than one round-trip trade per year (p.23). It ships zero adopted performance numbers for this record: every CAGR/Sharpe/drawdown figure describes the paper's equity sleeves or the five-class portfolio, never a single-asset BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Portfolio claims fenced: every headline result (five-class GTAA curves, equity-like-returns/bond-like-volatility framing, allocation-framework exhibits) belongs to the diversified portfolio or to pre-2013 equity sleeves — none transfers to a single-asset BTCUSDT derivative, and none is adopted.
2. Post-publication regime risk (Revisited, Exhibit 5 discussion): after sidestepping 2008–2009, the US timing sleeve underperformed buy-and-hold stocks in six of the next eight years — adopters arriving after the crash struggled to stay with the system. Monthly-regime timing can lag for years in a roaring bull tape.
3. Whipsaw admission (Revisited): market timing carries its own challenges — false-signal whipsaws in choppy markets plus the emotional cost of looking different from peers while they perform. The monthly grid bounds whipsaw frequency but never removes it.
4. Half-the-years admission (2013 update, p.23): the timing sleeve underperforms its index in roughly half of all individual years; value added, if any, appears only over full business cycles (p.25).
5. Cost silence fenced (note 4, p.22): the paper excludes taxes, commissions, and slippage (its Practical Considerations section notwithstanding) — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
6. Post-hoc extensions are not out-of-sample (Revisited, EXTENSIONS lead): departures published after the original paper are shown on full-sample dates beginning in 1972 precisely so as not to imply they are truly out of sample — no extension result is adopted here.
7. No crypto sample anywhere: no equity, bond, commodity, REIT, or post-2013 extension evidence speaks to BTCUSDT behavior; single-asset crypto timing is unevidenced by the source and may differ arbitrarily. The monthly grid further imposes up to a full month of decision latency, a limitation the paper's own daily-vs-monthly FAQ accepts as structural.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 10-month SMA / strict `>`-long-else-flat / month-end decision / next-open fills / single-position long-flat / signal-only exit / `1d` BTCUSDT are frozen.

- F1 — Formation-length relevance: replacing the pinned 10-month average with a 12-month average must not improve net expectancy; fail ⇒ the paper's chosen length carries no advantage over the slower stability-range neighbor.
- F2 — No-skip relevance: ending the 10-close formation one month before the decision bar (skip-latest-month variant) must not improve net expectancy; fail ⇒ the paper's no-skip month-end timing adds nothing over the skipped convention.
- F3 — Full-size relevance: replacing fixed 100%-equity sizing with fixed 50%-equity sizing must not improve risk-adjusted expectancy; fail ⇒ the declared size pin is doing unacknowledged work — or the record's size choice is arbitrary leverage in disguise.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid calendar-month on `1d` closes; close-to-close arithmetic with no venue-specific read). The arithmetic ports across perpetual venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session template, no cross-venue state. The 24/7 crypto market has no opens/sessions for the rule to read (month membership is the UTC calendar date of the daily bar — deterministic on any continuously traded tape). Extension to other house-universe assets or lookbacks would be a different, unpinned claim.

## Limitations

- Single-asset port: the paper's evidence is sleeve- and portfolio-level across five traditional asset classes; single-asset BTCUSDT behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Total-return vs price: the paper's series include dividends and income; BTC has none, so the port is exact in practice, but any future distribution-bearing mapping of this record would need re-derivation, disclosed, not silently carried.
- Cash without yield: flat months earn nothing here while the paper's cash earns T-bill returns — long-horizon comparisons against the paper's sleeves are therefore structurally understated, disclosed, not patched.
- Same-close fill fenced: the paper assumes signal-day-close execution; this record fills next open. On gapping month boundaries the two fills differ, and the difference is a declared derivation boundary — replication disputes are decided against this record's pin, never patched silently.
- No price stop, no intra-month exit: adverse excursion inside the holding month has no guardrail; the next decision is weeks away by construction. This is the source-faithful posture, disclosed as the record's principal risk.
- Monthly latency: the grid can only react at month-end; a mid-month regime break is ridden to month-end by construction — pinned, not recovered.
- Warmup cost: the first ten calendar months are flat by record rule, so any textbook regime completing inside warmup is deliberately untraded — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Faber, Mebane T., A Quantitative Approach to Tactical Asset Allocation (May 2006 working paper; Spring 2007, The Journal of Wealth Management; February 2013 Update pinned — author-hosted PDF, 70 pages, 945,897 bytes, SHA-256 `f2dabb6d31b18901cb64a0f57cea86f32f514570dcb5840fbeaa4877f24bdd3f`, verified 2026-10-13): https://mebfaber.com/wp-content/uploads/2016/05/SSRN-id962461.pdf
- SSRN abstract page (abstract_id=962461, bibliographic cross-check): https://papers.ssrn.com/sol3/papers.cfm?abstract_id=962461
- Faber, A Quantitative Approach to Tactical Asset Allocation Revisited 10 Years Later, The Journal of Portfolio Management Multi-Asset Special Issue 2018 (post-publication assessment for Negative evidence only; 13-page PDF, 1,760,315 bytes, SHA-256 `3465ff939e26e4001bba7c25d05506124c15fa0882af0dc57bf62921e2884284`)
