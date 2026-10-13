---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: BLL VMA 1-200 1% band state-following two-sided on BTCUSDT 1d
created: 2026-10-13
updated: 2026-10-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 1992-12-01
sources:
  - https://www.kevinsheppard.com/files/teaching/mfe/advanced-econometrics/Brock_Lakonishok_LeBaron.pdf
  - https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1992.tb04681.x
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# BLL VMA 1-200 1% band state-following two-sided on BTCUSDT 1d

## Provenance

Primary source read end to end in its methods and results sections (the artifact behind every rule citation below):

- Brock, W., Lakonishok, J., LeBaron, B., `Simple Technical Trading Rules and the Stochastic Properties of Stock Returns`, The Journal of Finance 47(5), 1731–1764 (December 1992), DOI `10.1111/j.1540-6261.1992.tb04681.x` (adopted as `source_as_of` 1992-12-01).
- Exact file read: https://www.kevinsheppard.com/files/teaching/mfe/advanced-econometrics/Brock_Lakonishok_LeBaron.pdf — 34 pages, retrieved 2026-10-13, 350,357 bytes, SHA-256 `9f9c2ab3e02ce9319cab5c5c115c711f6b5fb497b3ab5f19ce5f964245364b7a`. The PDF carries a scanned-image text layer, so it was read via full-page renders; the rule-definition passages (§I.B, journal pp. 1735–1736) and the VMA results table (Table II Panel A, journal p. 1739) were transcribed verbatim, and every number below comes from those pages — no rule or figure was taken from a secondary summary.
- Bibliographic cross-checks (abstract/identity only, never rule text): https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1992.tb04681.x and https://www.santafe.edu/research/results/working-papers/simple-technical-trading-rules-and-the-stochastic- (same title/authors/sample, confirming the published identity).
- Licence and rights: the paper is a published journal article — this record cites and normalizes the rule (short phrases and formulas only) and reproduces no figures, tables, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the paper's headline VMA(1,200) 1%-band rule ported to one crypto asset with fixed sizing — not a lossless reproduction of the paper's DJIA return-classification study. Researcher-declared adaptations are exactly six: (1) market pin `BTCUSDT` on Binance USDT-M perpetuals, `1d` frame (the source classifies daily DJIA closes 1897–1986 and runs no portfolio); (2) single-rule pin VMA(1,200,0.01) — the paper's own named "most popular" moving-average rule (1-day vs 200-day) with the 1% band, chosen on that predeclared bibliographic rationale and never on relative performance (the (1,50,0.01) row prints a larger spread and is deliberately not picked — see Negative evidence 5); (3) inside-band → flat mapping (the source classifies only buy/sell days and leaves inside-band days unclassified; a tradable port must do something there, so this record holds flat — disclosed derivation, never presented as a source sentence); (4) fixed 100%-equity single position at 1× with no adds (the source ships no sizing concept); (5) next-open market fills on the daily grid (the source is a day-classification return study, execution-silent beyond signal definition); (6) an adopted 200-bar warmup flat by record rule plus house fees/funding treatment replacing the paper's pre-cost return accounting (the paper reports gross-of-cost day-class returns). The (1,200) lengths, the 1% band, the above/below/band state logic, the go-long/go-short posture, the variable-length state-hold semantics, and the no-stop/signal-only posture are source-faithful.

Pre-write dedup (2026-10-13): working-tree case-insensitive searches for `brock`, `lebaron`, `lakonishok` (beyond the Lakonishok-Smidt prose citation inside the turn-of-month record, a different paper and mechanism), `variable.length`, `trading.range.break`, and `moving.average.oscillator` return zero strategy records using this source or mechanism. A second sweep for `1-200`, `1, 200`, `200-day`, and `sma200`/`sma-200` returns only incidental mentions: `SMA200` as a regime *gate* for other triggers (slow-stochastic record, double-seven record), never as the signal itself. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak), #49 (Gaussian channel StochRSI breakout), #63 (SuperTrend ATR-flip), #89 (Chandelier Exit stop-flip), #92 (SSL channel reversal) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `golden-cross-sma-regime-gated-long-btcusdt-1h-2026-10-08.md` fires on a fast/slow two-average cross (SMA50 × SMA200 edge), never on price displacement from its own 200-day average; `ema-20-50-cross-btcusdt-1h-2026-10-06.md` is a two-EMA cross with no band and no flat state; `donchian-20-10-breakout-btcusdt-1h-2026-10-06.md` breaks a 20-bar highest-high/lowest-low channel, never a moving-average band. Five-axis distinction: no pool record and no open PR holds a position on close-vs-own-200-day-average displacement beyond a ±1% band with an inside-band flat state, two-sided, on a daily state machine.

## Economic mechanism

### Source-reported

Persistent-drift capture through a noise-banded price-vs-trend state: the VMA rule "attempts to simulate a strategy where traders go long as the short moving average moves above the long and short when it is below" (§I.B), with the band quoted as the whiplash guard ("We test the moving average rule both with and without a one percent band"). Buy-day returns exceed sell-day returns across all ten MA variants and the spread survives four nulls (random walk, AR(1), GARCH-M, Exponential GARCH — Abstract and §I close), which the paper reads as evidence that past-price trend states carry predictive content no short-memory null reproduces.

### Research interpretation

Slow low-pass trend-state following port: with the short leg pinned at 1 day, the "short average" is the close itself, so the rule reduces to measuring how far price has displaced from its own 200-day mean — a pure level-displacement gauge with no smoothing-variant or line-cross choice anywhere. The ±1% band is the entire whipsaw defense: inside it the system stands flat rather than chattering, so every position begins only after a confirmed >1% displacement and ends the moment displacement decays back into the band or flips. Unlike two-average crosses (Golden Cross, EMA-20/50) there is no fast-line/slow-line edge to catch — the trigger is distance-from-mean, not a cross event. Unlike channel breakouts (Donchian-20/10) there is no rolling extreme to pierce — the reference is a mean, so a grinding drift that never prints a fresh extreme still accumulates displacement and still fires. The bet, as derived, is purely on BTCUSDT 200-day displacement persistence at daily cadence, never on a cross, extreme, oscillator, volume, calendar, or funding anchor.

## Signal

Exact rule as pinned (VMA(1,200,0.01) daily state machine — any other length, band, hold, or mapping is a different, unpinned rule):

- Inputs at the close of completed bar T: `C_T` (the 1-day "short average" — the paper's short period is one day, so no averaging is computed) and `L_T = mean(C_{T-199} … C_T)` (200-day simple average of closes, the paper's long period).
- State (pinned, strict — evaluated on every completed close from bar 200):
  `C_T > L_T * 1.01` → LONG; `C_T < L_T * 0.99` → SHORT; otherwise (inside the band) → FLAT. The equality legs are measure-zero on live tape and belong to FLAT by record rule — disclosed tie convention, not a source sentence.
- Orders (pinned): on any state change versus the current position, one market order at the next bar's open (open T+1): flat→long buys 100% equity; long→flat and short→flat close all; long→short and short→long flip through a close-all plus opposite entry at the same open. A bar whose state matches the current side places nothing — no adds, no partials, no re-entry edge while positioned.
- Risk legs (pinned absence, not invented): the paper ships no stop/target/trailing/time-exit concept for VMA — the sole position-closing path is the state machine leaving the side (band re-entry or opposite displacement). The derived posture is explicitly no stop, no target, no trailing, no time exit; a multi-week adverse displacement is ridden in full by construction.
- Direction: two-sided (source-native posture — "go long as the short moving average moves above the long and short when it is below"). The short leg requires margin-short permission, realistic on the pinned perpetual venue. No always-in-market claim: warmup bars and inside-band bars are explicitly flat.

## Required data

- Completed `1d` closes of BTCUSDT only: the close chain feeds `C_T` and `L_T`; `open` is read solely as the fill price. No `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, or cross-venue state gates any order. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: daily close. One evaluation per completed daily bar; fills land on the next daily bar's open. All signal inputs are completed-bar closes — no provisional close is ever used.
- Warmup: 200 completed `1d` bars before the first decision (the 200-close long average is the binding seed). Bars 1–200 are flat by record rule; the first decidable close is bar 200 and its fill lands on bar 201's open. No signal before the seed window completes may trade. No repainting, no negative shift, no future reference, no full-sample normalization; the 24/7 tape needs no session template (bar membership is the venue's own daily grid — deterministic).

## Execution assumptions

- Research market: `BTCUSDT` Binance USDT-M perpetual, `1d` decision frame, under the house overlay (declared port; the source venue is the pre-decimalization DJIA cash index — no cross-venue equivalence claimed beyond the same close-vs-average displacement mechanics).
- Order timing (declared port of the paper's day-classification cadence): completed-close decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill: the only legs are state-transition market orders, at most one per bar, and there is no same-bar dual-fire to sequence (state is a single value per bar by construction).
- Sizing/capital/costs: fixed 100%-equity single position at 1×, no adds, no leverage concept, no compounding concept beyond equity — declared derivative replacing nothing (the paper ships no sizing). The paper reports pre-cost day-class returns, so derived evaluation must carry the explicit house overlay (pinned house fees at taker plus realized historical funding accrual while positioned long or short — no hypothetical zero funding claimed anywhere; inside-band and warmup flat spells are genuine non-accrual time). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one position on this single market at any time; re-entry after flat needs only the next LONG/SHORT state (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The paper ships the full construction adopted here: two-average oscillator with (short, long) ∈ {(1,50), (1,150), (5,150), (1,200), (2,200)} tested with and without a 1% band (§I.B); the VMA state rule — buy (sell) while the short average sits above (below) the long by more than the band, no signal inside the band, traders long above and short below (§I.B, transcribed verbatim); the FMA fixed-10-day-hold crossover variant defined and fenced (not adopted — see Negative evidence 6); TRB penetration rules defined and fenced (not adopted); DJIA daily closes from the first trading day of 1897 to the last trading day of 1986, ~90 years (§I.A); Table I headnote (§II.A) records returns as log differences of the index level.

Pinned headline numbers (Table II Panel A, full sample 1897–1986, VMA(1,200,0.01) row, transcribed digit-for-digit): N(Buy) 14105, N(Sell) 8450, Buy mean 0.00040/day (t 2.01907), Sell mean −0.00030/day (t −3.48278), fraction Buy>0 0.5384, fraction Sell>0 0.4924, Buy−Sell 0.00070/day (t 4.73865). Abstract-level claims adopted as context only: buy signals consistently generate higher returns than sell signals with lower volatility, and the spreads are inconsistent with the random-walk, AR(1), GARCH-M, and Exponential-GARCH nulls. This record adopts zero performance numbers for BTCUSDT and claims no reproduced performance of any kind.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Single-asset boundary fenced: every headline number above describes DJIA day-classification, never a BTCUSDT position — single-asset crypto behavior is unevidenced by the source and may differ arbitrarily. This record is never evidence that the paper's equity-index result passes anything on crypto.
2. Pre-cost boundary fenced: the paper reports gross-of-cost day-class returns with no commission, spread, or carry concept; derived evaluation must carry the full house cost load (fees plus historical funding accrual), and this record reports no net performance of any kind.
3. Dividend boundary fenced: the paper's footnoted convention excludes dividends from index returns; a USDT-M perpetual has no dividend analogue, so the port is arithmetically cleaner than the source on this axis — disclosed, never counted as an edge.
4. Inside-band mapping fenced: flat-inside-the-band is the sole non-paper behavior in the state machine (the source merely leaves such days unclassified). A replication dispute on band-edge bars would be decided against this record's mapping, never patched silently.
5. Anti-cherry-pick fenced: the (1,50,0.01) row prints the largest full-sample Buy−Sell spread (0.00094/day, t 6.04189) and is deliberately not pinned; the pin follows the paper's own "most popular rule is 1–200" sentence. Picking the headline rule over the best-printing row is predeclared method, not performance selection.
6. Sibling rules fenced: the FMA 10-day-hold crossover variant, the zero-band all-days-classified variant, all other (short, long) pairs, and the TRB(50/150/200) penetration rules are explicitly out of scope — each would be a different, unpinned record. The variable-length state-hold (hold the side until the state leaves it) is the adopted semantic; the fixed-10-day FMA semantic is never mixed in.
7. The (1,200) lengths / 1% band / close-vs-mean state / next-open / single-position 1× / signal-only-exit stance is pinned, not removed: shortening the long average, dropping or widening the band, trading the cross edge instead of the state, adding a stop/target/filter/cooldown, sizing partially, or switching to the FMA hold would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: VMA(1,200,0.01) / close-vs-mean state / next-open fills / single-position 1× two-sided / signal-only exit / `1d` BTCUSDT are frozen.

- F1 — Band relevance: removing the band (0.00, all-days-classified) must not improve net expectancy; fail ⇒ the whiplash guard adds nothing over the raw displacement state.
- F2 — Length relevance: replacing the pinned (1,200) with the fastest paper variant (1,50) at the same 1% band must not improve net expectancy; fail ⇒ the 200-day low-pass carries no advantage over the faster formation.
- F3 — Hold-semantics relevance: replacing the variable-length state-hold with the paper's own FMA 10-day fixed-hold crossover semantic (same 1,200 lengths, same band) must not improve net expectancy; fail ⇒ the state-hold adds nothing over the fixed-hold crossover.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid daily close on `1d` bars; close-to-close arithmetic with no venue-specific read). The arithmetic ports across perpetual venues without structural change. The 24/7 crypto market has no opens/sessions for the rule to read (bar membership is the venue's own daily grid — deterministic on any continuously traded tape). No volume-dependent leg, no session template, no cross-venue state, no stablecoin-specific assumption. Extension to other house-universe assets, other (short, long) pairs, other bands, or the FMA/TRB siblings would each be a different, unpinned claim.

## Limitations

- Researcher market port: the source evidence is a 90-year US equity index; crypto microstructure, volatility scale, and 24/7 calendar mechanics differ structurally — no performance is claimed here for exactly this reason.
- Single-asset day-state: the paper classifies index days; this record trades one perp's state transitions — unavoidably different economics (gap risk, funding, liquidation framing), all disclosed in Execution assumptions.
- Fixed sizing: 100%-equity 1× concentrates risk in high-vol regimes with no volatility targeting; displacement-decay drawdowns are structurally unbuffered.
- Log-vs-simple boundary: the paper's return metric is log-differences; the derived signal is level-based (band on the average ratio) and therefore metric-invariant, but any derived P&L evaluation must state its own return convention — never borrowed silently from the paper.
- No price stop, signal-only exits: adverse displacement has no guardrail; the next state change can be weeks away by construction. This is the source-faithful posture, disclosed as the record's principal risk.
- Funding posture: two-sided with genuine flat interludes (warmup plus inside-band spells accrue nothing), but long-held displacement legs accrue historical funding like any perp position — evaluation must model it, and the pinned simulator's unverified funding-accounting boundary is flagged, never assumed away.
- Warmup cost: the first 200 daily bars are flat by record rule, so any textbook displacement completing inside warmup is deliberately untraded — pinned, not recovered.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Brock, W., Lakonishok, J., LeBaron, B., Simple Technical Trading Rules and the Stochastic Properties of Stock Returns, The Journal of Finance 47(5), 1731–1764 (1992), scanned published-paper PDF read in full methods/results (34 pages, 350,357 bytes, SHA-256 `9f9c2ab3e02ce9319cab5c5c115c711f6b5fb497b3ab5f19ce5f964245364b7a`, retrieved 2026-10-13): https://www.kevinsheppard.com/files/teaching/mfe/advanced-econometrics/Brock_Lakonishok_LeBaron.pdf
- Publisher record (DOI 10.1111/j.1540-6261.1992.tb04681.x, identity cross-check): https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1992.tb04681.x
