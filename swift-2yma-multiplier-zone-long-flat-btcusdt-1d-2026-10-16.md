---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Swift 2-year MA multiplier 1x-5x zone-state long-flat on BTCUSDT 1d bars
created: 2026-10-16
updated: 2026-10-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-16
sources:
  - https://www.tradingview.com/script/73lAnK5m-Bitcoin-2-Year-MA-Multiplier-by-Godtrix/
  - https://www.lookintobitcoin.com/charts/bitcoin-investor-tool/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Swift 2-year MA multiplier 1x-5x zone-state long-flat on BTCUSDT 1d bars

## Provenance

Primary A — stable public script page, read end to end via direct fetch 2026-10-16 (TradingView `Bitcoin 2-Year MA Multiplier by Godtrix`, author godtrix, open-source script):

- Full Indicator Overview prose pinned verbatim: a moving-average line (the 2yr MA) plus a multiplication of that line (2yr MA x5); the x5 multiplication is of the price values of the 2yr moving average, not of its time period; buying when price drops below the 2yr MA; selling when price goes above the 2yr MA x 5.
- Credit line pinned verbatim: `Created By Philip Swift`, `Date Created July 2017`, `BITSTAMP:BTCUSD`.
- Executable inputs pinned verbatim from the page's embedded widget state: `Length` 730 (`defval: 730`, `min: 1`), price source `close`, timeframe `D` (daily). The embedded plotted series satisfies upper == 5 x lower exactly (maximum relative deviation 0.0 across all 282 plotted points), confirming the fixed-multiple construction.

Primary B — creator's official methodology page, read end to end via direct fetch 2026-10-16 (LookIntoBitcoin `Bitcoin Investor Tool: 2-Year MA Multiplier`):

- `2yr MA x5 is the default, but you can also set lower multiples using the chart legend`; `Historically, accumulating bitcoin when price drops below the 2yr MA (green line)`; `Selling Bitcoin when price approaches the 2yr MA x 5 (red line)`.
- Zone framing pinned verbatim: price `historically low (in the green zone) or high (in the red zone) or neutral (between the green and red zones)` — the middle-retain state below is source-native, not invented.
- `macro, high time frame level` context; `Created By Philip Swift`, `Date Created July 2017`.

Neither page ships any performance number for any executable rule: no return, win rate, profit factor, trade count, date range, or cost table. `outsized returns` is qualitative book language. This record claims no source-reported performance and no reproduced performance.

Rights: both pages are public (an open-source script plus a public methodology page). This record cites and normalizes the rule and reproduces only short phrases quoted for gate evidence; no source code is copied.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Source-native and unmodified: the 730-length average of daily closes, the upper line fixed at 5 x the lower line (of price values), the accumulate-below-lower / distribute-above-upper / neutral-middle semantics, the long-only direction, and the no-stop/no-target posture (no such leg exists in either primary). Researcher-declared adaptations are exactly five: (1) research market/timeframe BTCUSDT `1d` (the script pins `BITSTAMP:BTCUSD` with a `D` input and LookIntoBitcoin is Bitcoin-daily; the 1:1 daily-bar port is declared, never claimed as source venue); (2) strict completed-bar cross predicates (see Signal); (3) next-`1d`-open market fills — both primaries are indicator pages, not `strategy()` code, so no order timing exists in source; timing is modeled on the admitted `1d` next-open path, never presented as source-native; (4) an adopted 800-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 731st completed bar — see Required data); (5) house sizing/capital/costs replacing unstated source costs. The MA type is pinned to SMA as the plain-meaning executable reading of the script's `moving average (MA) line` (the script exposes no MA-type input — one hardcoded average); any EMA/WMA/SMMA is a different, unpinned rule, and the open-source Pine remains the reviewer's source-verifiable check for this single pin.

Pre-write dedup (2026-10-16): working-tree case-insensitive filename search for `2yma`, `multiplier-band`, `2-year`, `investor-tool` and content search for `MA Multiplier`, `MA730`, `730-day`, `Pi Cycle`, `rainbow`, `Golden Ratio Multiplier` return zero strategy records (all `multiplier` hits in the pool are ATR/Bollinger/contract-size vocabulary; `swift` hits only the English adverb; `730` hits only a price print). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class (see Negative evidence 7). This is a new family, not a parameter variant: no pool record trades a 730-bar fixed-multiple 1x/5x zone-state.

## Economic mechanism

### Source-reported

Long-horizon Bitcoin valuation zones. Price below its own 2-year average marks historical accumulation (fearful, over-contracted markets); price above 5 x that average marks historical distribution (over-excited, over-extended markets); between the two lines is neutral. The two lines bracketed prior cycle lows and highs. The tool is explicitly a long-term, macro high-timeframe investment lens.

### Research interpretation

Asymmetric two-threshold zone-state long-flat on a slow valuation band. Unlike midline-cross systems (pool golden-cross 50/200, Faber 10-month SMA regime, NVI 255EMA regime) there is no cross-and-flip — the middle zone retains state by source design. Unlike sigma envelopes (pool Bollinger breakout/midline-exit, Keltner, STARC, LinReg channel, NW endpoint envelope, GKV adaptive band) the band is a fixed 1x/5x multiple of one 730-bar average, not a volatility scaling; events are outside-zone threshold crosses, not breakout-and-revert. Unlike Ehlers/cycle oscillators the signal is a plain long average with no transform, no Hilbert machinery, and no fast-vs-slow cross. The book is single-unit long-flat; no pyramiding; the short side is disabled by source construction.

## Signal

Exact rule as pinned (constants quoted — inputs unmodified):

- Price input (pinned): `close` series only. `MA730[t] = SMA(close[t-729..t])`. `Upper[t] = 5 x MA730[t]`. Single daily frame. No `open`, `high`, `low`, `volume`, funding, OI, mark/index price, order-book, on-chain, sentiment, macro, or cross-venue state on the order path.
- Entry long (source semantic `drops below the 2yr MA`): `close[1] >= MA730[1]` and `close[0] < MA730[0]` → buy next `1d` open.
- Exit to flat (source semantic `goes above the 2yr MA x 5`; LookIntoBitcoin's softer `approaches` is fenced, never the trigger): `close[1] <= Upper[1]` and `close[0] > Upper[0]` → sell next `1d` open.
- Middle zone (source semantic `neutral (between the green and red zones)`): retain the prior state — long stays long, flat stays flat.
- Boundary ties hold their side: exact equality on the completed bar is neither a cross-under nor a cross-over, so no order fires and the book carries the prior state.
- No dual-fire is possible, structurally, not by rule: `MA730 > 0` always, so lower < upper always — one close cannot be both below the lower line and above the upper line. No tie-break is needed or admitted.
- Direction: long-only with flat state; the short side is explicitly disabled (no short leg exists in either primary).
- Position rule: single-unit; repeat entry predicates while already long are no-ops (no pyramiding, no averaging, no second unit). Re-entry is immediate on the next fresh entry cross after flat (no cooldown specified — explicitly none, not invented).
- Exits: the upper-band cross is the sole position-closing path. No stop, no target, no trailing, no time exit — pinned as written, explicitly none, not invented.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (730 trailing closes per evaluation). No `open`, `high`, `low`, `volume`, no funding, OI, mark/index price, or any external feed is read by any order-gating line.
- Single decision timeframe `1d` (`D` pinned on the script input; LookIntoBitcoin frames the tool at a macro high timeframe).
- Warmup: `MA730` needs 730 closes and each cross predicate needs the prior bar's alignment, so the first evaluable signal sits on the 731st completed bar (structural minimum). The adopted warmup is the first 800 completed `1d` bars flat by record rule (predeclared researcher choice). No repainting, no negative shift, no future reference, no full-sample normalization (trailing SMA only); one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (researcher-declared; venue/symbol spelling is naming only, never presented as source-native semantics). The long-flat book needs no short-side instrument.
- Order timing (researcher-declared, modeled): completed-bar decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester — the same next-open path as the admitted `1d` records. No maker-touch, queue, or intrabar-path-dependent fill. With no stop/limit legs anywhere there is no same-bar TP/SL ordering ambiguity; dual-fire is structurally impossible (see Signal).
- Engine path for `1d` (gate 5, stated plainly): `1d` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `1d` candles (`close` series) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no volume-definition dependence, no funding/OI/mark-price leg. That is the same single-frame completed-bar plus next-open path as the admitted `1d` records; the SMA730 recurrence advances deterministically from known closes, so no hidden lookahead is ever modeled. Anything beyond that path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: unstated source costs are replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions here, never presented as source-native behavior. The book is long-or-flat, so modeled funding accrues only while long — flagged per the house baseline, never zero-claimed; no campaign may claim complete realized-funding performance without a verified implementation.
- Concurrency: single-unit long-flat by record rule (repeat entries while long are no-ops; dual-fire impossible); single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

With exact provenance (both pages read end to end via direct fetch this cycle): the TradingView script title, author, open-source status, and full Indicator Overview prose (2yr MA + x5-of-price-values construction, buy-below / sell-above semantics, Swift / July-2017 / BITSTAMP:BTCUSD lineage); the embedded `Length = 730` / `close` / `D` inputs with the exact 5.0 upper ratio confirmed in the page's own plotted data; the LookIntoBitcoin default-x5 note, adjustable-multiples legend disclosure, accumulate/distribute/neutral zone language, macro high-timeframe context, and matching Swift / July-2017 lineage. Both pages ship zero performance numbers for any executable rule — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Indicator, not strategy: neither primary ships order code or fill timing — the completed-bar/next-open timing is researcher-declared executable specification (adaptation 3), assessed against this record's own fully specified derived version, never as source fidelity. A reviewer must not re-time it to same-bar-close to rescue or reshape the record.
2. Soft-language fence: LookIntoBitcoin's `approaches`, `attempts to identify`, and adjustable legend multiples are book softness and options — the pinned trigger is the strict cross above 5 x MA730 and the pinned multiple is exactly 5. No other multiple, no proximity band, no blended exit is admitted.
3. Sibling variants fenced, never adopted: third-party 183-lookback copies, adjustable-multiplier / adjustable-MA-type script variants, the 200-week MA heatmap, the Golden Ratio Multiplier (350DMA x Fibonacci multiples), the Pi Cycle (111DMA vs 350DMA x 2), and log-regression rainbow bands are different, unpinned rules — a reviewer must not graft any of their lengths, multiples, or triggers onto this record.
4. MA-type pin disclosed: the script's `moving average (MA) line` with no MA-type input is pinned here as SMA by plain-meaning executive choice (adaptation 5); EMA/WMA/SMMA/hull variants are different unpinned rules. The open-source Pine is the reviewer's source-verifiable check — only a Pine-verifiable repair is admissible, never a preference pick.
5. Structural patience disclosed: the exit leg fires only above 5 x MA730, so in any regime where price never reaches the upper line, a long persists with no guardrail (no stop by source design) while accruing while-long modeled funding; entries cluster in deep multi-year bears, so one round trip can span years (capital lockup). This is the coded trade, disclosed, not tuned away.
6. Middle-retain is source-native (`neutral (between the green and red zones)`), equality ties hold side, warmup bars are flat by record rule, and dual-fire is arithmetically impossible — none of these is a hidden rule.
7. Overlap fences, admitted plainly: pool `golden-cross-sma-regime` trades a 50/200 average-vs-average cross flip (different event — flip, no neutral zone); pool `faber-gtaa-10m-sma` trades a 10-month SMA monthly regime across assets (different horizon, frame, and universe); pool `nvi-255ema-regime` trades a volume-index regime (different signal family); pool `bollinger-band-breakout-long-midline-exit` trades an SMA20 +/- 2-sigma breakout with midline exit (different construction — sigma envelope vs fixed 1x/5x multiple; different horizon — 20 vs 730; different state machine — breakout/midline vs outside-zone cross with neutral retain); pool keltner/STARC/LinReg/NW-envelope/GKV/EHMA-range/T3-Tillson records trade volatility-scaled or regression envelopes (different bands); pool `ema-cloud`, `super-guppy-ema-stack`, `tema-dema-hma-cross` trade stack/cross events (different events). Shared `moving average` / `band` vocabulary is not shared signal.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules — the rule is complete); global no-retuning rule: `close` input / SMA730 recurrence / `Length = 730` / `Upper = 5 x MA730` / strict cross predicates / single-unit long-flat book with neutral-middle retain / next-open fills / no-stop posture / `1d` BTCUSDT are frozen.

- F1 — Upper-line relevance: an exit-at-midline twin (entry as pinned; exit on `close` crossing above `MA730` instead of above `Upper`; same book and timing) must not improve net expectancy; fail ⇒ waiting for the 5x line adds nothing over exiting at the midline.
- F2 — Window relevance: a 365-day twin (`SMA365` with a 5x upper, same zone-state machine, book, and timing) must not improve net expectancy; fail ⇒ the 2-year window adds nothing over a 1-year window.
- F3 — Multiple relevance: a 3x twin (`SMA730` with a 3x upper, same machine, book, and timing) must not improve net expectancy; fail ⇒ the 5x multiple adds nothing over 3x.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (declared port of a Bitcoin-daily tool whose script venue is BITSTAMP:BTCUSD). The rule reads completed daily closes only, so no pit-session, gap, or roll logic ports. The fixed-length arithmetic needs no recalibration across assets, yet 24/7 crypto execution vs the source's Bitcoin-spot history is a real mismatch — unclaimed and undisguised (see Negative evidence 5). The rule is long-flat, so spot and futures both express it without venue gating; funding accrues only while long and is modeled, never zero-claimed. No warmup history beyond 800 daily bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- No price stop, no time stop: adverse excursion after entry has no guardrail before the upper-band cross, by the source design — the record's principal risk.
- Extreme patience: 730-bar memory with rare signals; round trips can span years; long flat stretches idle the book while entries lock capital through deep bears.
- Next-open lag: each cross is detected at the completed-bar close and filled at the next open, systematically one bar late at both ends of multi-year turns.
- Single-venue daily port: Bitcoin-tool provenance vs 24/7 BTCUSDT daily execution is a declared derivation with unclaimed portability residual (prints, fees, funding, margin mechanics beyond the house model).
- Performance evidence is absent: no source reports a number for any executable version of this rule, and none is claimed here.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior and never part of this admission — no Safety-Order/DCA event is admitted in this record's version. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- TradingView public open-source script page, `Bitcoin 2-Year MA Multiplier by Godtrix` (godtrix; full Indicator Overview prose; `Length = 730` / `close` / `D` inputs; exact 5.0 upper ratio in page data; Created By Philip Swift; Date Created July 2017; BITSTAMP:BTCUSD — read end to end via direct fetch 2026-10-16): https://www.tradingview.com/script/73lAnK5m-Bitcoin-2-Year-MA-Multiplier-by-Godtrix/
- LookIntoBitcoin official methodology page, `Bitcoin Investor Tool: 2-Year MA Multiplier` (x5 default with adjustable legend multiples; accumulate-below / sell-above / neutral-between zone language; macro high-timeframe context; Created By Philip Swift; Date Created July 2017 — read end to end via direct fetch 2026-10-16): https://www.lookintobitcoin.com/charts/bitcoin-investor-tool/
