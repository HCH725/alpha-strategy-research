---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: De Bondt-Thaler 1985 long-term overreaction 36-month loser long-flat on BTCUSDT 1d bars
created: 2026-10-13
updated: 2026-10-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 1985-07-01
sources:
  - https://doi.org/10.1111/j.1540-6261.1985.tb05004.x
  - https://www.semanticscholar.org/paper/00167b90b8fbf57d22b661c32ee8fb39020af12f
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# De Bondt-Thaler 1985 long-term overreaction 36-month loser long-flat on BTCUSDT 1d bars

## Provenance

Primary source identity verified end to end (Crossref record read firsthand 2026-10-13 confirming title, authors, journal, volume/issue/pages, and DOI; Semantic Scholar metadata record confirming title, authors, year 1985, and the same DOI; verbatim paper passages inspected via full-text witnesses quoting the abstract, §I method, and Figure 1 findings with page anchors — all agree):

- De Bondt, Werner F. M. & Thaler, Richard, `Does the Stock Market Overreact?` — The Journal of Finance, vol. 40, no. 3, 793–805 (July 1985). DOI `10.1111/j.1540-6261.1985.tb05004.x`. Canonical DOI landing: https://doi.org/10.1111/j.1540-6261.1985.tb05004.x (Wiley page bot-walled at read time, so no claim is sourced from it beyond the Crossref-confirmed citation).
- Pinned formation spec (§I, read verbatim via full-text witness): `16 three-year periods between January 1930 and December 1977 are examined` — non-overlapping 36-month formation periods; securities are ranked on `cumulative excess returns` and the extreme portfolios hold `35 stocks` each (winners/losers); primary residuals are market-adjusted `u(jt) = R(jt) − R(mt)`, with market-model and Sharpe-Lintner CAPM residuals as robustness legs.
- Pinned test spec (§I, read verbatim): `starting in January 1933 (month 85, the "starting month") and up to December 1980, we now compute the cumulative average residual returns of all securities in the portfolio, for the next 36 months (the "test period," months 85 through 120), i.e., from t = 1 through t = 36` — `CAR(W,n,t)` and `CAR(L,n,t)` averaged across the 16 test periods into `ACAR(W,t)` and `ACAR(L,t)`. The overreaction hypothesis predicts `for t > 0, ACAR(W,t) < 0 and ACAR(L,t) > 0`.
- Pinned headline finding (Figure 1 discussion, read verbatim): `Over the last half-century, loser portfolios of 35 stocks outperform the market by, on average, 19%, thirty-six months after portfolio formation. Winner portfolios, on the other hand, earn about 5% less than the market, so that the difference in cumulative average residual between the extreme portfolios, [ACAR(L,36) − ACAR(W,36)] equals 24% (t-statistic: 2).` Corroborating methodology summary pins the precise cells adopted nowhere here: 24.6% spread (t = 2.20), loser +19.6%, winner −5.0%, 16 non-overlapping three-year test periods, CRSP Monthly Return File, 347–1,089 NYSE stocks per replication, January 1926–December 1982.
- Pinned asymmetry and timing (same discussion, read verbatim): `the overreaction effect is asymmetric; it is much larger for losers than for winners`; `most of the excess returns are realized in January. In months t = 1, t = 13, and t = 25, the loser portfolio earns excess returns of, respectively, 8% (t-statistic: 3), 5% (3), and 4% (2)`; `the overreaction phenomenon mostly occurs during the second and third year of the test period. Twelve months into the test period, the difference in performance between the extreme portfolios is a mere 5% (t-statistic: 0).`
- Pinned risk read (fenced, never adopted): winner CAPM beta 1.369 vs loser 1.026 (`t-statistic on difference: 3.09`) — losers are the less risky leg by this measure, so market adjustment understates the spread; the 5-year formation variant prints `[ACAR(L,60) − ACAR(W,60)] = 0.319 (t = 3.28)` over 10 five-year periods with 50-stock portfolios (both fenced to the paper's equity sample).
- Licence and rights: the paper is a paywalled journal article — this record cites and normalizes the rule (short phrases and formulas only) and reproduces no figures, tables, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the paper's 36-month cumulative-return loser/winner sort ported to one crypto asset as a sequential non-overlapping 36-month-block long-or-flat hold — not a lossless reproduction of the paper's cross-sectional NYSE long-short study. Researcher-declared adaptations are exactly eight: (1) single-asset BTCUSDT Binance spot (the 347–1,089-stock cross-section, the 35-stock extreme portfolios, the winner-minus-loser spread, and every portfolio-level alpha/t-statistic claim are fenced off, never carried — see Negative evidence 1); (2) loser-mapped-to-long / winner-mapped-to-flat with the short permission explicitly unused (the paper is long losers and short winners; this record holds long only when the single asset reads loser-like and holds flat otherwise — see Signal/Execution); (3) plain cumulative return `C_T / C_{T-36} − 1` replacing market-adjusted cumulative excess returns (there is no market index to subtract on a single-asset tape — the loser/winner split is re-expressed as a sign split at zero, declared here, never implied); (4) simple returns pinned where the paper compounds monthly residuals (the ratio form fixes the read; log vs simple is pinned simple by record rule, disclosed, never implied); (5) sequential non-overlapping 36-calendar-month blocks tiling forward from the first decidable month-end (the paper's own 16 non-overlapping three-year periods are the structural precedent — no overlapping sleeves, no 1/36 monthly turnover, never re-tuned); (6) month-end-close decision with next-month-first-open fills (the paper rebalances at test-period beginnings with no executable fill convention, so the sequential next-open fill is declared, never implied); (7) full 36-month holding of whatever the block decision prints, including holding through the paper's own January-concentration and years-2–3 timing (the paper's spread arrives late and in Januarys; this record holds every month of the block identically — the mismatch is disclosed in Negative evidence 3, not patched); (8) an adopted thirty-seven-full-calendar-month warmup with the first signal at the thirty-eighth calendar month's first open (no warmup concept exists in the source — the count is derived arithmetically from the 36-month formation need, frozen in Falsification).

Pre-write dedup (2026-10-13): working-tree case-insensitive sweeps for `debondt`, `de bondt`, `thaler`, `overreact`, `36-month`, `36m`, `loser portfolio`, `long-term reversal`, `long run reversal` return no strategy record in the main tree — the only content hits are passing prose, verified line by line: the jegadeesh-titman-6m-6m record's mechanism paragraph contrasting practitioner 3–12-month continuation against `short-run reversal or long-run overreaction` (one comparative clause, no 36-month rule); the lehmann-1990 record's negative-evidence line on `own-stock overreaction` vs cross-stock lead-lag attribution (a literature caveat, no rule); the p-signal-erf record's `short-horizon overreaction` mechanism hypothesis for 1-hour price changes (a generic word, different horizon, different construction). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources; closed PRs carry no De Bondt, Thaler, overreaction, loser, or 36-month title. Closest pool records differ in mechanism class and horizon: `jegadeesh-1990-monthly-reversal-long-flat-btcusdt-1d-2026-10-13.md` reverses a 1-month formation (36× shorter — a short-horizon snapback sensor, never a multi-year overreaction read); `lehmann-1990-weekly-reversal-long-flat-btcusdt-1d-2026-10-13.md` reverses a 1-week formation (∼150× shorter); `jegadeesh-titman-6m-6m-momentum-long-flat-btcusdt-1d-2026-10-13.md` and `novy-marx-12-7-intermediate-momentum-long-flat-btcusdt-1d-2026-10-13.md` trade WITH the past 6–12-month sign (continuation direction — the opposite side of this record's contrarian mapping); `tsmom-12m-sign-monthly-long-btcusdt-1d-2026-10-10.md` holds a 12-month sign for one month (a monthly direction sensor, never a 36-month block hold). No record in the pool conditions a multi-year block position on the sign of a 36-month cumulative return — the long-horizon overreaction sensor class is absent.

## Economic mechanism

### Source-reported

Representativeness-driven overreaction to dramatic news, in violation of Bayes' rule: `Research in experimental psychology suggests that, in violation of Bayes' rule, most people tend to "overreact" to unexpected and dramatic news events. This study of market efficiency investigates whether such behavior affects stock prices.` The monetizable shape is contrarian and slow: prior extreme losers `outperform the market by, on average, 19%` over the 36 months after formation while prior extreme winners `earn about 5% less than the market` — `Substantial weak form market inefficiencies are discovered`, with the spread arriving mostly in the second and third test years and concentrating in January turn-of-year prints (all mechanism framing fenced to the paper's 1926–1982 NYSE sample, never adopted as a crypto claim here).

### Research interpretation

Multi-year clock contrarian port: the 36-month cumulative return is a slow clock that only three full years of month-end closes can set, so the coming 36-month block's posture is fully known at the block-end close — a tape that compounded below its own three-years-ago print earns the long book for the whole next block, a tape that compounded above it earns nothing for the whole next block. There is no entry event inside the block, no exit leg, and no variance or average read anywhere: the strategy holds one posture per 36-month block and the only thing that ever moves is the block boundary. Unlike short-horizon reversal (Jegadeesh-1990 1-month, Lehmann 1-week) the sensor integrates three full years, so a violent single month barely registers — the record bets on multi-year overextension correcting, never on a weekly/monthly snapback. Unlike continuation momentum (Jegadeesh-Titman 6/6, Novy-Marx 12-7, TSMOM-12m) the mapping is inverted — past strength maps to flat, past weakness maps to long — so on any tape where momentum and overreaction disagree at different horizons the two records print opposite postures by construction. Unlike average-regimes (Faber GTAA) or variance clocks (Moreira-Muir) the reference is the asset's own compounded 36-month path, never a moving average, never a second moment, never a calendar season. The bet, as derived, is purely on the paper's `prior losers outperform prior winners over the next 36 months` surviving the port to BTCUSDT at non-overlapping 36-month cadence with the loser leg mapped to long and the winner leg mapped to flat, never on a return-prediction, seasonal, band, oscillator, volume, or funding anchor.

## Signal

Exact rule as pinned (36-month cumulative simple return from month-end closes, zero-threshold sign split with tie to flat, sequential non-overlapping 36-calendar-month blocks — any other value is a different, unpinned rule):

- Decision bar: the last completed `1d` bar dated in a block-end calendar month T (blocks are consecutive non-overlapping 36-calendar-month groups tiling forward from the first decidable month-end; month membership is the UTC calendar date of each daily bar — deterministic on the 24/7 tape).
- Formation return (pinned declared port of the paper's 36-month cumulative excess return): `R36_T = C_T / C_{T-36} − 1` where `C_T` is the close of the decision bar and `C_{T-36}` is the close of the last completed `1d` bar dated 36 calendar months earlier (month-end closes only — 37 month-end points spanning 36 full months; simple returns pinned by record rule where the paper compounds monthly residuals; no market subtraction exists on a single-asset tape — declared, never implied; `C_{T-36} > 0` on any traded tape so the ratio needs no zero-guard branch).
- Position target for the next block of thirty-six calendar months T+1..T+36 (pinned sign split, tie to flat): `R36_T < 0` (loser-like — the tape compounded below its own three-years-ago print) → long; `R36_T >= 0` → flat. The `>=` spelling pins the measure-zero exact-zero print to flat with no second rule and no float-tolerance concept; no threshold constant exists anywhere in this record — zero is the record's declared loser/winner cut, frozen, never re-tuned.
- Skip (pinned, not a parameter): none — the paper ranks straight 36-month cumulative returns with no skip-a-month concept, and none is added here.
- Orders (pinned): at most one order event per 36-month block boundary, placed for the first `1d` open of month T+1 (next-open fill after the decision bar — the declared causal port; the paper turns over non-overlapping 3-year portfolios at test-period beginnings with no executable fill convention, so the sequential next-open fill is declared, never implied): flat→long target buys 100% equity; long→flat target closes all; unchanged target places nothing. No intra-block evaluation, no intra-block orders, no adds, no partials, no second decision inside months T+1..T+36 for any reason including large adverse excursion.
- Risk legs (pinned absence, not invented): the paper ships no stop/target/trailing/time-exit concept — the sole position-closing path is the next block-end state mapping to flat. The derived posture is explicitly no stop, no target, no trailing, no intra-block exit; a three-year adverse move is ridden in full by construction.
- Direction: long-or-flat, derived-and-declared (the long maps the paper's loser leg; the flat maps the paper's winner leg with the short permission simply unused, and a spot-only deployment expresses the identical event set).

## Required data

- Completed `1d` bars of BTCUSDT only: daily `close` (formation arithmetic and settlement) and `open` as fill price only. No `high`/`low` range read, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: block-end calendar months. One evaluation per 36-month block on the last completed daily bar of the block-end month; fills land on the next daily bar's open (first open of the new block). All window inputs are completed-bar values — no provisional month-end return is ever used.
- Warmup: thirty-seven full calendar months of `1d` bars before the first position (the formation needs month-end closes T−36..T). Bars before the first decidable month-end are position-free by record rule; no signal before the thirty-eighth calendar month's first open may trade. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance spot (declared port — spot is chosen deliberately so no funding leg exists to model; no cross-venue equivalence claimed).
- Order timing (declared causal port of the paper's test-period-beginning turnover cadence): block-end completed-bar decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill is claimed. At most one order exists per block boundary, so there is no same-bar dual-fire to sequence.
- Cash leg: flat earns nothing by record rule. No T-bill, stablecoin-lending, funding-rebate, or synthetic yield is substituted; the paper's cost-free accounting accrues no cash yield to either leg.
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity. The paper reports cost-free strategy returns, so derived evaluation must carry the explicit house overlay (pinned house spot fees on each block-boundary delta; no funding leg exists on spot — and this record claims no hypothetical zero funding on any venue where funding would apply). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; re-entry after a flat block needs only the next loser-like block print (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no overlapping sleeves (the paper's sixteen standalone replications with no turnover between them are replaced by the declared sequential single sleeve tiling forward — see Limitations). The unused short permission requires no margin-short modeling.

## Evidence

### Source-reported

The paper ships every adopted construction fact: the 16 non-overlapping 36-month formation periods (January 1930–December 1977), the 36-month cumulative market-adjusted excess-return rank, the 35-stock extreme winner/loser portfolios, the 36-month test-period CAR/ACAR apparatus with the `ACAR(W,t) < 0` / `ACAR(L,t) > 0` prediction, the market-model and CAPM residual robustness legs, and the 5-year formation variant. It ships zero adopted performance numbers for this record: the 24.6% spread (t = 2.20), the +19.6% loser ACAR, the −5.0% winner ACAR, the January prints (8.1%/5.6%/4.0%), the 12-month 5.4% non-result, the 1.369/1.026 betas, and the 0.319 five-year spread all describe the paper's NYSE cross-sectional study, never a single-asset BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Cross-section fenced: every headline result (spreads, t-statistics, January concentration, beta ordering, five-year variant) belongs to a 347–1,089-stock NYSE cross-sectional study — none transfers to a single-asset BTCUSDT derivative, and none is adopted.
2. Market adjustment dropped: the source ranks cumulative market-adjusted excess returns; a single-asset tape has no market leg to subtract, so this record ranks plain cumulative return against zero — a strictly weaker, researcher-declared cut with no source equivalence claim.
3. Timing mismatch disclosed: the paper's spread arrives mostly in test years 2–3 and concentrates in Januarys, yet this record holds the block posture identically from month 1 through month 36 of every block — early-block drift and non-January months are held by record rule exactly as late-block Januarys are, and any resemblance between the two timing shapes is unevidenced here.
4. No crypto sample anywhere: no 1926–1982 equity evidence speaks to BTCUSDT behavior; single-asset crypto long-horizon reversal is unevidenced by the source and may differ arbitrarily. The loser-mapped long block rides every post-warmup 36-month drawdown leg in full, with no exit by construction (a further three-year slide after a loser print is absorbed whole until the next block).
5. Cost silence fenced: the paper reports cost-free returns with no transaction-cost leg — derived evaluation must carry the full house spot-fee load, and this record reports no net performance of any kind.
6. Researcher cut: the zero threshold, the simple-return read, the sequential-block tiling, and the thirty-seven-month warmup are declared choices, not source facts — a nonzero loser cut, a log-return read, or overlapping sleeves would each be a different, unpinned rule (see F3).
7. Winner-leg economics discarded: the source earns roughly a fifth of its spread from the winner short; mapping winners to flat abandons that leg deliberately — the short-side carry of the original study is fenced, not carried.
8. Block latency: the grid can only re-posture at 36-month boundaries on the prior three years' compounding; a fresh overreaction regime is mistimed for up to three years by construction — pinned, not recovered.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 36-month cumulative simple return from month-end closes / zero sign split with tie to flat / sequential non-overlapping 36-month blocks / block-end decision / next-open fills / single-position long-or-flat 1× / turnover-only changes / `1d` BTCUSDT spot are frozen.

- F1 — Horizon relevance: replacing the pinned 36-month formation with a 12-month formation on the identical block grid must not improve net expectancy; fail ⇒ the three-year clock carries no advantage over the one-year clock on the same tape — or the record's horizon choice is arbitrary leverage in disguise.
- F2 — Direction-of-mapping relevance: the perverse twin mapping long onto `R36_T >= 0` (continuation twin) on the identical grid must not outperform the pinned contrarian mapping; fail ⇒ the overreaction sensor points the wrong way and the tape rewards chasing three-year strength instead.
- F3 — Threshold relevance: replacing the pinned zero cut with a deep-loser cut (`R36_T < −0.20`, same grid, same tie convention) must not improve net expectancy; fail ⇒ the zero split is doing unacknowledged work as a hidden participation filter — or the extreme-tail story the source actually tells was flattened away by the sign split.
- F4 — Participation relevance: replacing the pinned long-or-flat posture with fixed full-size always-long buy-and-hold on the identical grid must not improve net expectancy while also not lowering realized volatility; fail on either clause ⇒ the loser/flat gate is decoration — or flat blocks are the only thing working.

## Crypto portability

Pinned to BTCUSDT Binance spot (decision grid block-end months on `1d` closes; cumulative-return arithmetic with no venue-specific read). The arithmetic ports across spot venues without structural change. No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session template, no cross-venue state. The 24/7 crypto market has no closes/sessions for the rule to read (month membership is the UTC calendar date of the daily bar — deterministic on any continuously traded tape). Extension to other house-universe assets, to the paper's 5-year formation variant, to overlapping sleeves with fractional monthly turnover, to a market-adjusted excess-return read against a crypto index, or to holding horizons other than 36 months would each be a different, unpinned claim.

## Limitations

- Single-asset port: the paper's evidence is cross-sectional across hundreds of NYSE stocks; single-asset BTCUSDT behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Cut substitution: the source's cross-sectional loser/winner rank is replaced by a single-asset sign split at zero; any distributional property tied to extreme-tail membership is lost by declared derivation, and replication disputes are decided against this record's pin, never patched silently.
- Researcher cut: the zero threshold, the simple-return read, the 36-month sequential blocks, and the thirty-seven-month warmup are record rules, not source facts — frozen, falsifiable, never re-tuned.
- Block posture: each 36-month block holds one posture for its whole length; the flat-block opportunity cost and the long-block drawdown absorption are the record's principal risks, disclosed, not patched.
- Winner short abandoned: the source's winner-minus side is mapped to flat, so any spread contribution from shorting three-year strength is deliberately left behind.
- Timing mismatch: the source spread concentrates in test years 2–3 and in Januarys while this record holds all block months identically — disclosed as the record's principal timing risk.
- No executable fill in source: the paper turns over at test-period beginnings with no fill convention; this record fills next open. On gapping block boundaries the two fills differ, and the difference is a declared derivation boundary — replication disputes are decided against this record's pin, never patched silently.
- No price stop, no intra-block exit: adverse excursion inside the 36-month holding block has no guardrail; the next decision is years away by construction. This is the source-faithful posture, disclosed as risk, not patched.
- Warmup cost: the first thirty-seven calendar months are position-free by record rule, and on a young tape only a handful of independent 36-month blocks can ever print — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- https://doi.org/10.1111/j.1540-6261.1985.tb05004.x
- https://www.semanticscholar.org/paper/00167b90b8fbf57d22b661c32ee8fb39020af12f
