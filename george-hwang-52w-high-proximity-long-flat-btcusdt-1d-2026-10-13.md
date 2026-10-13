---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: George-Hwang 2004 52-week-high proximity sequential long-flat on BTCUSDT 1d bars
created: 2026-10-13
updated: 2026-10-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2004-10-01
sources:
  - https://bauer.uh.edu/tgeorge/papers/gh4-paper.pdf
  - https://doi.org/10.1111/j.1540-6261.2004.00695.x
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1104491
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# George-Hwang 2004 52-week-high proximity sequential long-flat on BTCUSDT 1d bars

## Provenance

Primary source identity verified end to end (author-hosted published-paper PDF, DOI landing, and SSRN record page read 2026-10-13; methods verified verbatim in the 32-page text layer of the author's PDF the same day):

- George, Thomas J. & Hwang, Chuan-Yang, `The 52-Week High and Momentum Investing` — Journal of Finance, vol. LIX, no. 5, 2145–2176 (October 2004). DOI `10.1111/j.1540-6261.2004.00695.x`; SSRN abstract `1104491`. Canonical file: https://bauer.uh.edu/tgeorge/papers/gh4-paper.pdf (`THE JOURNAL OF FINANCE • VOL. LIX, NO. 5 • OCTOBER 2004`, title/authors/abstract verified in-text, pp. 2145–2176).
- Pinned headline spec (Abstract, read verbatim): `When coupled with a stock's current price, a readily available piece of information—the 52-week high price–explains a large portion of the profits from momentum investing. Nearness to the 52-week high dominates and improves upon the forecasting power of past returns (both individual and industry returns) for future returns. Future returns forecast using the 52-week high do not reverse in the long run.` Sample window adopted at section level only (Table I caption: average monthly portfolio returns from July 1963 through December 2001).
- Pinned construction facts (pp. 2149–2150, read verbatim from the text layer): `The strategy is to hold, for 6 months, a self-financing portfolio that is long the winner and short the loser portfolios.` / `In any particular month t of a (6, 6) strategy, the return to winners is calculated as the equally weighted average of the month t returns from six separate winner portfolios, each formed in one of the 6 consecutive prior months` / `For the 52-week high strategy, stocks are ranked based on Pi,t−1 / highi,t−1, where Pi,t−1 is the price of stock i at the end of month t − 1 and highi,t−1 is the highest price of stock i during the 12-month period that ends on the last day of month t − 1.` / `The winner (loser) portfolio for the 52-week high strategy is the equally weighted portfolio of the 30% of stocks with the highest (lowest) ratio of current price to the 52-week high.` / `We focus the early discussion in the paper on (6, 6) strategies` with robustness to `(6, 12), (12, 6), and (12, 12) strategies.` Portfolio-level headline numbers fenced, never adopted here: Table I legs earn `around 0.45% per month` across all three strategies; ex-January the 52-week-high leg prints `1.30% / 0.07% / 1.23%` (t `7.06`) and January-only prints `−8.27%` (t `−5.49`); `profits from the JT and 52-week high strategies more than double when the January effect is removed— from 0.48 to 1.07% and from 0.45 to 1.23%, respectively` — every cell describes the paper's equity spread study, never a single-asset BTCUSDT derivative (see Negative evidence 1–2).
- Skip pin (footnote 3, p. 2149, read verbatim): `To abstract from bid-ask bounce, we skip a month between ranking and holding periods in our regression tests. We do not skip a month for the more descriptive Tables I–IV to better compare with numbers reported in existing studies such as JT, so our initial description of methods ignores the skip.` This record adopts the descriptive no-skip leg; the regression skip-a-month variant is fenced, never read.
- Licence and rights: the paper is a published journal article — this record cites and normalizes the rule (short phrases and formulas only) and reproduces no figures, tables, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the paper's descriptive (6, 6) no-skip 52-week-high winner leg ported to one crypto asset as a sequential 6-calendar-month long-or-flat hold — not a lossless reproduction of the paper's cross-sectional 30%-tail spread study. Researcher-declared adaptations are exactly six: (1) single-asset BTCUSDT Binance perpetual (the CRSP cross-section, the winner-minus-loser zero-cost spread, the equally weighted tails, and every portfolio-level performance claim are fenced off, never carried — see Negative evidence 1); (2) the winner mapping is pinned to the at-the-trailing-high binary `C_T >= H_T` (a single asset has no cross-section to rank, so the continuous top-30% sort cannot be evaluated — the paper's own winner-leg prose, `When good news has pushed a stock's price near or to a new 52-week high ... resulting in a continuation`, names the `to a new 52-week high` print as the continuation trigger, and this record trades exactly that print with no invented threshold constant — see Signal); (3) sequential non-overlapping 6-calendar-month holding blocks on completed `1d` closes with next-open fills (the paper holds six overlapping cohorts with 1/6 monthly turnover; the derived port holds one cohort per block so single-position state stays explicit — a material event-timing change, declared here, never implied); (4) the descriptive no-skip pin (the regression skip-a-month variant is fenced by the paper's own footnote); (5) an adopted twelve-full-calendar-month warmup flat by record rule plus house fees/funding treatment replacing the paper's cost-free CRSP accounting; (6) fixed 100%-equity single-position sizing with no leverage (the paper holds equally weighted 30% tails, never a single-asset book). The 12-month trailing-high window, the no-skip pin, the 6-month holding length, the 30%-tail winner-leg lineage, and the no-stop/no-target/no-trailing posture (signal-roll exits only) are source-faithful.

Pre-write dedup (2026-10-13): working-tree case-insensitive sweeps for `52-week`, `52 week`, `week-high`, `week high`, `george`, `hwang`, `proximity`, `nearness`, `trailing high`, `12-month high`, `all-time high`, `52w` return no strategy record in the main tree — the only hits are citation/prose fragments (the slow-stochastic record's George Lane %K/%D lineage line, the gann-hilo record's own dedup paragraph about a deleted 1-ATR-proximity history file, `nearest`-wording in three FMZ-lane overlay paragraphs, `anchor`-wording for anchored-VWAP/mean-reversion prose). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources; 120 closed PRs carry no 52-week-high, Hwang, or proximity-momentum title. Closest pool records differ in mechanism class: `jegadeesh-titman-6m-6m-momentum-long-flat-btcusdt-1d-2026-10-13.md` trades the sign of a 6-month cumulative return (a past-change sensor, half the window, fully recent-weighted); `novy-marx-12-7-intermediate-momentum-long-flat-btcusdt-1d-2026-10-13.md` trades the sign of a lagged intermediate return that deliberately ignores the six most recent months (opposite recency handling, a change not a level); `tsmom-12m-sign-monthly-long-btcusdt-1d-2026-10-10.md` rolls a 1-month hold on a 12-month return sign (one-sixth the holding, no level anywhere); `faber-gtaa-10m-sma-monthly-regime-long-flat-btcusdt-1d-2026-10-13.md` compares a price level against its own 10-month average (an average, never a trailing extreme); `bll-trb-200-percent-band-fixed-10d-two-sided-btcusdt-1d-2026-10-13.md` buys 1% penetrations of a 200-close extreme and holds exactly ten bars two-sided (a penetration event with a fixed bar-count exit, two-hundredth the holding, opposite direction handling); `turtle-system-2-55d-breakout-2n-stop-half-n-add-two-sided-btcusdt-1d-2026-10-12.md` and `donchian-20-10-breakout-btcusdt-1h-2026-10-06.md` break N-bar high/low channels with trailing exits and stops (channel-breakout entries with exit legs, never a month-end state with a fixed block hold); the calendar holds carry no price-conditioned leg at all. Five-axis distinction: no pool record and no open PR holds a sequential six-calendar-month block long-or-flat on the month-end at-the-trailing-12-month-high state.

## Economic mechanism

### Source-reported

Price-level anchoring, not past-change extrapolation: `we find that nearness to the 52-week high is a better predictor of future returns than are past returns, and that nearness to the 52-week high has predictive power whether or not stocks have experienced extreme past returns. This suggests that price levels are more important determinants of momentum effects than are past price changes.` The paper's behavioral reading (pp. 2146–2147): `traders use the 52-week high as a reference point against which they evaluate the potential impact of news. When good news has pushed a stock's price near or to a new 52-week high, traders are reluctant to bid the price of the stock higher even if the information warrants it.` / `The information eventually prevails and the price moves up, resulting in a continuation.` — framed as the experimental `adjustment and anchoring bias` (`traders might use the 52-week high as an "anchor," like the random number in the experiments when assessing the increment in stock value implied by new information`), resolved without overcorrection: `short-term underreaction is best characterized as an anchoring bias that the market resolves without the overcorrection that results in long-term reversals` (all mechanism framing fenced to the paper's 1963–2001 equity sample, never adopted as a crypto claim here).

### Research interpretation

Trailing-extreme regime port: the 12-month trailing high is a slow step function that only ratchets on fresh extremes, so the at-high print fires only when the month-end close confirms the year's best bid — a grinding drift that never sets a fresh extreme never triggers, and a wick that pierces intraday but closes below fires nothing. The locked 6-month block with no intra-block trading makes whipsaws structurally impossible inside the half-year — the strategy can be up to six months stale but can never chase a mid-block spike or flip on a single red month. Unlike return-sign momentum (Jegadeesh-Titman 6/6, TSMOM-12m, Novy-Marx) the sensor is a level ratio with no return arithmetic anywhere: a 40% six-month rally that still sits 20% under the yearly high prints flat here and long there. Unlike moving-average regimes (Faber) the reference is a trailing extreme, never a smoothing: price hugging its average from below prints long there and flat here. Unlike penetration breakouts (BLL-TRB, Donchian, Turtle) there is no entry event and no exit leg — only a month-end state read once per half-year. The bet, as derived, is purely on the paper's `near or to a new 52-week high` continuation trigger surviving the port to BTCUSDT at half-year cadence, never on a return, average, band, oscillator, volume, calendar-seasonal, or funding anchor.

## Signal

Exact rule as pinned (12-month trailing-high window ending at the block-end month, no skip, at-high binary, 6-month sequential blocks — any other value is a different, unpinned rule):

- Decision bar: the last completed `1d` bar dated in a block-end calendar month T (blocks are consecutive non-overlapping 6-calendar-month groups tiling forward from the first decidable month-end; month membership is the UTC calendar date of each daily bar — deterministic on the 24/7 tape).
- Trailing high (pinned literal read of `the highest price ... during the 12-month period that ends on the last day of month t − 1`): `H_T = max(high)` over all completed `1d` bars dated in calendar months T−11..T (twelve full calendar months ending with the decision month; daily `high`, never close-only extremes, never volume-weighted or adjusted series — BTC has no distributions to adjust for; `H_T > 0` on any traded tape so the ratio needs no zero-guard branch).
- Proximity (pinned): `ρ_T = C_T / H_T` where `C_T` is the close of the decision bar. Since the decision bar's own daily high is inside the window, `C_T <= H_T` mathematically and `ρ_T <= 1` always.
- Position target for the next block of six calendar months T+1..T+6 (pinned at-high binary, tie to long): `C_T >= H_T` (i.e. `ρ_T` at its mathematical maximum — the month-end close is the trailing 12-month high) → long; `C_T < H_T` → flat. The `>=` spelling pins the measure-zero equality print to long with no second rule and no float-tolerance concept; no threshold constant exists anywhere in this record.
- Skip (pinned, not a parameter): none — this record adopts the paper's descriptive Tables I–IV leg; the regression skip-a-month variant is fenced by the paper's own footnote, never read.
- Orders (pinned): at most one order event per 6-month block boundary, placed for the first `1d` open of month T+1 (next-open fill after the decision bar — the declared causal port; the paper turns over 1/6 of six overlapping cohorts at month beginnings with no executable fill convention, so the sequential next-open fill is declared, never implied): flat→long target buys 100% equity; long→flat target closes all; unchanged target places nothing. No intra-block evaluation, no intra-block orders, no adds, no partials, no second decision inside months T+1..T+6 for any reason including large adverse excursion.
- Risk legs (pinned absence, not invented): the paper ships no stop/target/trailing/time-exit concept — the sole position-closing path is the next block-end state mapping to flat. The derived posture is explicitly no stop, no target, no trailing, no intra-block exit; a half-year adverse move is ridden in full by construction.
- Direction: long-or-flat, derived-and-declared (the futures venue is still pinned as the research market under the house overlay with the short permission simply unused, and a spot-only deployment expresses the identical event set).

## Required data

- Completed `1d` bars of BTCUSDT only: daily `high` (trailing-maximum window) and the decision-bar `close` (numerator and settlement); `open` only as fill price. No `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: 6-calendar-month blocks. One evaluation per block on the last completed daily bar of the block-end month; fills land on the next daily bar's open (first open of the new block). All window inputs are completed-bar values — no provisional month-end extreme is ever used.
- Warmup: twelve full calendar months of `1d` bars before the first decision (every bar in months T−11..T must exist). Bars before the first decidable block-end are flat by record rule; no signal before the thirteenth calendar month's first open may trade. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port; no cross-venue equivalence claimed).
- Order timing (declared causal port of the paper's month-beginning turnover cadence): block-end completed-bar decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill is claimed. At most one order exists per block boundary, so there is no same-bar dual-fire to sequence.
- Cash leg: flat earns nothing by record rule. No T-bill, stablecoin-lending, funding-rebate, or synthetic yield is substituted; the paper's cost-free accounting accrues no cash yield to either leg.
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity. The paper reports cost-free strategy returns, so derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — long blocks carry realized funding, flat blocks carry none, and the form holds genuine flat blocks so it is never an always-in-position funding accumulator). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; re-entry after a flat block needs only the next at-high block print (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no overlapping cohorts (the paper's six sleeves with 1/6 monthly turnover are replaced by the declared sequential single sleeve — see Limitations). The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

The paper ships every adopted construction fact: the descriptive (6, 6) overlapping six-cohort construction with month-t ranking on `P/high` and the 30% equally weighted tails (pp. 2149–2150), the no-skip descriptive pin with the skip confined to regressions (footnote 3), the 12-month trailing-high definition, the July-1963–December-2001 sample (Table I caption), the (6, 12)/(12, 6)/(12, 12) robustness legs, and the at/near-the-high continuation prose that this record's binary port trades. It ships zero adopted performance numbers for this record: the ~0.45%/month Table I cells, the 1.30/0.07/1.23% ex-January row, the −8.27% January-only spread, and every t-statistic describe the paper's equity 30%-tail study, never a single-asset BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Cross-section fenced: every headline result (30% sorts, equal weighting, winner-minus-loser spreads, nested JT/MG spanning, January splits, the 0.45/1.23/−8.27 cells) belongs to a cross-sectional equity study — none transfers to a single-asset BTCUSDT derivative, and none is adopted.
2. January pathology disclosed: the source spread collapses in January (`−8.27%`, t `−5.49`) because loser tails rebound (`12.11%` January-only) on the paper's own tax-loss-selling account — the derived long-only form holds no loser leg, but its winner-leg lineage shares the calendar exposure and claims no January behavior of any kind.
3. No crypto sample anywhere: no 1963–2001 equity evidence speaks to BTCUSDT behavior; single-asset crypto at-high momentum is unevidenced by the source and may differ arbitrarily. The locked 6-month block can ride a full half-year drawdown with no exit by construction (flat-while-below-high at block ends is equally possible; multi-year bears print flat for years).
4. Cost silence fenced: the paper's spreads are cost-free returns, not net-of-cost tradable P&L — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
5. Overlap admission: the source holds six overlapping sleeves with monthly 1/6 turnover while this record holds one sequential sleeve per block — a declared material timing change; any turnover, smoothing, or diversification property of the overlapping construction is discarded, not carried.
6. Binary simplification: the paper ranks a continuous proximity ratio into 30% tails; this record trades only the mathematical-maximum print. Any conditioning information in the mid- and near-high ranks is discarded by declared derivation, and the `high`-vs-close read of `highest price` is the declared literal pin — a close-extreme reimplementation would be a different, unpinned rule.
7. Block latency: the grid can only react at 6-month boundaries to a state already baked at the boundary; a fresh regime break is missed for up to half a year by construction — pinned, not recovered.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 12-month trailing-high window ending at block-end / no skip / at-high `>=`-long-else-flat / block-end decision / next-open fills / single-position sequential long-flat / signal-only exit / `1d` BTCUSDT are frozen.

- F1 — Level-vs-change relevance: replacing the pinned at-high level state with the JT-style 6-month cumulative-return sign on the identical block grid (same holds, same fills) must not improve net expectancy; fail ⇒ the trailing-extreme level carries no advantage over the recent-change sign on the same tape.
- F2 — Holding-length relevance: replacing the pinned 6-month sequential holding with a 1-month holding on the identical at-high state (same grid phase) must not improve net expectancy; fail ⇒ the half-year commitment carries no advantage over the monthly roll.
- F3 — Direction-twin relevance: the contrarian-signed twin on the identical block grid (long iff `C_T < H_T`, flat at highs) must not outperform the pinned at-high mapping; fail ⇒ the paper's `near or to a new high` continuation leg does not survive the port and the record's trigger is doing negative work.
- F4 — Full-size relevance: replacing fixed 100%-equity sizing with fixed 50%-equity sizing must not improve risk-adjusted expectancy; fail ⇒ the declared size pin is doing unacknowledged work — or the record's size choice is arbitrary leverage in disguise.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid 6-calendar-month blocks on `1d` highs/closes; max-and-ratio arithmetic with no venue-specific read). The arithmetic ports across perpetual venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session template, no cross-venue state. The 24/7 crypto market has no opens/sessions for the rule to read (month membership is the UTC calendar date of the daily bar — deterministic on any continuously traded tape). Extension to other house-universe assets, windows, or near-high bands would be a different, unpinned claim.

## Limitations

- Single-asset port: the paper's evidence is cross-sectional across individual equities; single-asset BTCUSDT behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Sequential-holding deviation: the source's overlapping six-sleeve construction with monthly turnover is replaced by one sequential sleeve per block; turnover smoothing and cohort diversification are lost by declared derivation, and replication disputes are decided against this record's pin, never patched silently.
- Binary simplification: the paper buys/sells ranked 30% tails of a continuous ratio; this record trades only the maximum print. Any distributional information in the paper's sort is discarded by declared derivation, not silently carried.
- `Highest price` read: pinned to daily `high`; the regression-skip variant, alternate windows ((6, 12)/(12, 6)/(12, 12)), and any near-high band are fenced alternatives, never fallback pins.
- Cash without yield: flat blocks earn nothing here while neither paper leg accrues cash yield either — long-horizon comparisons against any yield-bearing benchmark are structurally mismatched, disclosed, not patched.
- No executable fill in source: the paper turns over cohorts at month beginnings with no fill convention; this record fills next open. On gapping block boundaries the two fills differ, and the difference is a declared derivation boundary — replication disputes are decided against this record's pin, never patched silently.
- No price stop, no intra-block exit: adverse excursion inside the six-month holding block has no guardrail; the next decision is months away by construction. This is the source-faithful posture, disclosed as the record's principal risk.
- Stale-signal latency: the window ends at the block boundary and the position then locks for six months; fresh information is structurally ignored for half a year — pinned, not recovered.
- Warmup cost: the first twelve calendar months are flat by record rule, so any textbook at-high print completing inside warmup is deliberately untraded — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- https://bauer.uh.edu/tgeorge/papers/gh4-paper.pdf
- https://doi.org/10.1111/j.1540-6261.2004.00695.x
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1104491
