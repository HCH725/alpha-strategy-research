---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: NW endpoint envelope contrarian two-sided on BTCUSDT 1d bars
created: 2026-10-16
updated: 2026-10-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: high
source_as_of: 2025-01-02
sources:
  - https://www.tradingview.com/script/Iko0E2kL-Nadaraya-Watson-Envelope-LuxAlgo/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# NW endpoint envelope contrarian two-sided on BTCUSDT 1d bars

## Provenance

Primary sources read end to end during this cycle (2026-10-16), pinned immutable:

- Canonical page: `Nadaraya-Watson Envelope [LuxAlgo]` at https://www.tradingview.com/script/Iko0E2kL-Nadaraya-Watson-Envelope-LuxAlgo/ — fetched live during this cycle (HTTP 200, 328738 bytes of landing HTML). Page carries the `OPEN-SOURCE SCRIPT` badge; settings text pins `Bandwidth: Controls the degree of smoothness of the envelopes`, `Mult: Controls the envelope width`, and a `Source` input; methodology text states the envelope is `based on Kernel Smoothing`, follows a `contrarian methodology`, offers a `non-repainting smoothing method` in settings, and explains the non-repainting method estimates trend with an `endpoint Nadaraya-Watson estimator`.
- Construction mirror (rule evidence): `marz-hunter/xauusd`, file `scalping-5min/Nadaraya-Watson Envelope [LuxAlgo]`, file commit `9d11d5c872` (committed `2025-01-02 UTC`, sole commit touching that path, adopted as `source_as_of`; blob SHA `7f3b082b61c230c2b51189f5a79de47a8628d2a5`). File header reads `© LuxAlgo` under `CC BY-NC-SA 4.0`. 118 lines / 4637 bytes, read verbatim this cycle; every literal below is byte-present in that file.
- Pinned defaults (input lines): `h = input.float(8.,'Bandwidth', minval = 0)`, `mult = input.float(3., minval = 0)`, `src = input(close, 'Source')`, plus the mode toggle `repaint = input(true, 'Repainting Smoothing', ...)` with tooltip `Disabling repainting will cause the indicator to output the endpoints of the calculations`.
- Pinned kernel (function line): `gauss(x, h) => math.exp(-(math.pow(x, 2)/(h * h * 2)))` — Gaussian kernel, bandwidth `h`.
- Pinned endpoint block (adopted machine): one-sided weights `w = gauss(i, h)` for `i = 0 to 499` accumulated once into `coefs` with `den := coefs.sum()`; per-bar `out += src[i] * coefs.get(i)` for `i = 0 to 499`, then `out /= den`; `mae = ta.sma(math.abs(src - out), 499) * mult`; `upper = out + mae`; `lower = out - mae`.
- Pinned cues (adopted triggers): `plotshape(ta.crossunder(close, out - mae) ? low : na, "Crossunder", ... text = '▲', ...)` at the low and `plotshape(ta.crossover(close, out + mae) ? high : na, "Crossover", ... text = '▼', ...)` at the high.
- Code census of the 118-line file: 0 `strategy.*` calls (indicator-only — the flip machine below is the disclosed derivation, never a source claim) / 0 `request.*` / 0 `timeframe.*` / 0 `stop=` / `limit=` / target / trailing / time-exit inputs or calls anywhere / 2 `plotshape` cue lines (adopted) / 1 repainting compute-and-display block plus 1 dashboard-table block (explicitly NOT adopted, fenced below). Color/style/line-count inputs are display-only and inert.
- Licence and rights: this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. The source ships an indicator with two smoothing modes and no order leg; this record pins exactly one executable reading. Researcher-declared adaptations are exactly five: (1) market pin `BTCUSDT` Binance futures `1d` (the indicator is market-agnostic — no market is named anywhere in the file; only the venue/frame pin is adapted and disclosed here, never presented as a source claim); (2) endpoint non-repainting mode pinned (`repaint=false` wiring adopted verbatim) with the default repainting mode explicitly excluded, never blended; (3) `src=close` pinned (the source default input, never re-chosen); (4) indicator→executable flip machine: the two `plotshape` cues become a two-sided reversal machine (▲ → long, ▼ → short, opposite cue reverses, same-side repeat is a no-op) with completed-bar decision and same-bar-close fills, predeclared per pool precedent; (5) an adopted 1000-bar warmup with pre-warmup bars flat by record rule plus house sizing/capital/costs (the file ships no economics of any kind — recorded as absent, never as evidence). The `8` / `3` / `500` / Gaussian-kernel / MAE-band / cross-pair / contrarian-fade construction is source-pinned. **No stop, no target, no trailing, no time exit, no pyramiding, and no gate/filter beyond the two crosses is admitted in this record's version.**

Pre-write dedup (2026-10-16): working-tree case-insensitive searches for `nadaraya`, `luxalgo`, `nw-endpoint`, and `endpoint envelope` return zero strategy records (the sole `nadaraya` hit pool-wide is the QRS record's own dedup sentence reporting zero NW content; `kernel` appears only as Grinblatt-Han's turnover-weighting prose, never as a signal). Open `research/*` PRs are only #48, #49, #63, #89, #92 (Larry Williams streak, Gaussian-channel StochRSI, SuperTrend flip, Chandelier Exit, SSL channel) — none is a kernel-regression envelope.

## Economic mechanism

### Source-reported

Kernel-smoothing extremity fade: the endpoint NW estimator reads the trailing price tape through a Gaussian weighting window to estimate the underlying trend; mean absolute deviation around that estimate, tripled, draws the envelope rails. Price punching through a rail has stretched unusually far from its own estimated center, so the contrarian reading expects a snap-back — ▲ prints under downside punches (long-side cue), ▼ prints over upside punches (short-side cue). The canonical page states this plainly: an envelope `based on Kernel Smoothing` that `follows a contrarian methodology`, with the non-repainting path built on an `endpoint Nadaraya-Watson estimator`.

### Research interpretation

Trailing-kernel mean-reversion state machine, two-sided. Unlike moving-average-band breakouts (a 20-bar EMA ± 2σ continuation bet, e.g. open PR #49), here the center is a 500-bar Gaussian-weighted trailing mean — a slow, smooth anchor, not a reactive one — and the trade direction is the opposite: fade the punch, never chase it. Unlike price-on-time regression channels (pool `linreg-channel-band-touch`, rails from regressing price on bar index), no time regressor exists anywhere: weights depend only on lag distance, never on price scale or trend slope, so the bands breathe with realized wiggle (MAE) rather than with fitted slope. The price of the one-sided kernel is endpoint lag (the estimate trails fast turns by construction); the price of the 3× MAE rails is rarity (most bars do nothing by design); the price of the fade is catching every genuine breakout against the position until the opposite rail confirms the reversal.

## Signal

Exact rule as pinned (all constants are source input defaults or loop literals; any other value is a different, unpinned rule):

- Declarations (derived): single-asset two-sided reversal machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). At most one position; zero-or-long-or-short, never both sides at once.
- Kernel weights (pinned verbatim): `w[i] = exp(-(i²)/(2·8²))` for lag `i = 0..499`, normalized by `den = Σw` (one-sided trailing Gaussian, bandwidth `h=8`, fixed at first bar — no refit, no adaptation, no lookahead by construction).
- Center (pinned verbatim): `out(t) = Σ_{i=0}^{499} close[t-i]·w[i] / den`.
- Width (pinned verbatim): `mae(t) = 3 × mean_{k=0}^{498} |close[t-k] − out(t)|` (trailing 499-bar SMA of absolute deviation against the *current-bar* estimate — exactly as coded, never re-expressed as historical per-bar deviations).
- Rails (pinned verbatim): `upper(t) = out(t) + mae(t)`, `lower(t) = out(t) − mae(t)`.
- Long cue (pinned verbatim, Pine v5 strict cross): `close[t-1] >= lower[t-1] and close[t] < lower[t]` (downside punch through the lower rail) → ▲ → enter/reverse to LONG.
- Short cue (pinned verbatim, Pine v5 strict cross): `close[t-1] <= upper[t-1] and close[t] > upper[t]` (upside punch through the upper rail) → ▼ → enter/reverse to SHORT.
- Flip discipline (derived, predeclared): each cue closes any opposite position and opens its own side; a same-side repeat cue while already positioned is a no-op (no add, no reset). Touches without strict crossing never fire.
- Exits/risk: opposite-cue reversal only. No stop, no target, no trailing, no time exit — explicitly none by record rule (0 such calls/inputs exist in the 118-line file).
- Direction: two-sided fade. Both cue legs exist in the file (▲ and ▼ `plotshape` lines); the venue needs short permission for the full machine (Binance futures — realistic; a spot-only deployment would express the long leg only and is NOT this record's version).
- Re-entry: after any reversal, the next opposite cue reverses again (no cooldown specified — explicitly none, not invented).

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (center, width, and both cue lines read `close` and nothing else — `high`/`low` appear solely as label-plot anchors, never in any order-gating expression; `volume` is read by zero lines). No funding, OI, mark/index price, order-book, on-chain, sentiment, macro, calendar, session, or cross-asset state is read anywhere.
- Single decision timeframe `1d` (no multi-timeframe call, no `request.*`, no cross-sectional ranking — one asset, one frame).
- Warmup: the center needs 500 closes; the width needs 499 deviation terms against seeded centers, so the first fully-seeded bar sits at 0-based index 997. The adopted warmup is the first 1000 completed `1d` bars flat by record rule (full seed plus margin; no cue before bar 1001 may trade). Every window is trailing and every input is complete at the bar's close under same-bar-close fills — causal, no repaint path (the repainting display block is fenced out of this record entirely).

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (the indicator names no market — venue/frame adaptation disclosed in Provenance, never presented as a source claim).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) — the same verified execution primitive as the admitted `three-down-three-up-consec-close-long-btcusdt-1h`, `qstick-zero-cross-trend-two-sided-btcusdt-1h`, and `eight-day-run-sma5-momentum-reversal-two-sided-btcusdt-1d` PASS records (single-frame completed-bar decision, same-bar-close market fill, no protective stop/limit legs anywhere in the derived machine, hence no same-bar TP/SL ordering ambiguity; each bar's outcome is a deterministic event: hold, open-long, open-short, or reverse). No maker-touch, queue, multi-asset sync, lower/multi-timeframe alignment, non-OHLCV input, or intrabar-path-dependent fill is required by any line of this record. The TV ▲/▼ markers confirm on bar close under the endpoint mode, matching this timing exactly.
- Sizing/capital/costs: the file ships no economics (no capital, sizing, fee, or slippage line of any kind — recorded as absent portable economics, never as evidence) — derived evaluation carries the fixed, reproducible house research cost model (Base 6% + Safety 6% + Safety 6% notional framing, Isolated, 3x/5x; pinned house cost assumptions for fees plus modeled funding — no hypothetical zero funding claimed, never presented as source-native behavior). Funding is modeled, never reported as realized or canonical funding. No Safety-Order/DCA event participates in the admitted cue machine regardless of downstream campaign settings.
- Concurrency: one order path over one single-asset engine position — at most one exposure (long or short) at a time; no second position is constructed anywhere. No shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The pinned file ships the full construction (Gaussian kernel, `h=8`, one-sided 500-weight endpoint estimator, 499-bar SMA-of-deviation width with `mult=3`, `±mae` rails, the ▲/▼ cross pair, `close` default). The canonical page ships the contrarian methodology and the endpoint non-repainting mode. Neither ships any performance number: this record carries zero source-reported performance figures — exact empirical figures require traceable table/figure/section provenance and are omitted, never paraphrased.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No performance carried, admitted plainly: an indicator page plus a signal-only file is venue/market-agnostic construction evidence; no number exists to transfer, and this record claims none.
2. Repainting mode fenced, with reason: the `barstate.islast` full-window block recomputes all 500 historical points on every bar (future bars enter past estimates — structural lookahead), so it can never satisfy gate 6; this record adopts only the trailing endpoint block and a reviewer must not blend the two modes.
3. Indicator→machine boundary fenced: the file contains 0 order calls, so the flip discipline (reverse on opposite cue, no-op on repeat) is the predeclared derivation, never a source claim; this record is therefore never evidence that LuxAlgo endorses any executable posture.
4. No hidden risk layer: 0 stop/limit/target/trailing/time inputs or calls in 118 lines — the no-stop/no-target posture is the record rule, explicitly none, never hidden.
5. Degenerate-tape edge fenced: a perfectly flat 499-bar tape makes `mae = 0` and all three lines coincide; strict-cross semantics then cannot fire (no strict inequality possible) — deterministic no-trade, never patched.
6. One-sided causality proved: endpoint weights are fixed at the first bar from lag distance only (`gauss(i, h)`, no price input); every price read is `src[i]` with `i >= 0` (current or past closes); the width SMA is trailing. No future, repainted, or incomplete-bar input reaches any cue.
7. Overlap fences, admitted plainly: open PR #49 is a 20-bar EMA ± 2 sample-σ *breakout continuation* (long-only, StochRSI `k>d` gate, BNB) — opposite center scale, opposite width statistic, opposite trade direction, plus a gate this record forbids. Pool `linreg-channel-band-touch` regresses price on bar index for channel rails — a time-slope object, never a lag-weighted mean. Pool `starc-band-breakout` (SMA ± ATR multiples, breakout) shares neither the kernel center nor the MAE width nor the fade direction. Shared "band/envelope/channel" vocabulary is not shared signal.
8. No hidden variants admitted: `h`, `mult`, `src`, window `500/499`, and the `repaint` toggle are file inputs a user *could* change — every non-default combination is a different, unpinned rule. The admitted signal is exactly defaults with `repaint=false`. A reviewer must not pick among these to rescue or reshape the record.
9. Derivation boundary fenced: the only non-source-native behaviors are the market/venue pin, the indicator→flip-machine executable reading with same-bar-close fills, the adopted 1000-bar flat warmup, and house sizing/costs with no admitted Safety-Order/DCA event — all predeclared above; the kernel, literals, rails, cross pair, and fade posture are source-pinned or predeclared. This record is therefore never evidence that any other market, frame, bandwidth, multiplier, window, source, mode, or timing passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `h=8` / `mult=3` / `500/499` windows / Gaussian kernel / `close` source / endpoint mode / cross-pair cues / opposite-cue reversal / no-stop-no-target posture / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Width relevance: narrowing the rails `mult 3 → 1` (same center, same cues, same machine) must not improve net expectancy; fail ⇒ the triple-deviation extremity rails add nothing over a near-center fade on this market.
- F2 — Kernel relevance: replacing the endpoint NW center with a plain `SMA(500)` center (same 3× trailing-MAE rails, same cues, same machine) must not improve net expectancy; fail ⇒ the Gaussian lag-weighting adds nothing over an unweighted mean on this market.
- F3 — Fade-direction relevance: a breakout twin (long on the upside punch, short on the downside punch — same rails, same machine, reversed sides) must not improve net expectancy; fail ⇒ the source's contrarian direction adds nothing over continuation on this market.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (the indicator names no market — venue pin disclosed). The rule reads completed daily closes only, so no open-print, session, or cross-venue difference can touch any order-gating line beyond each calendar-day bar's own prints — but spot-vs-perp prints can still differ structurally (funding-driven drift, venue aggregation), so the futures-venue pin is load-bearing and disclosed. Lengths `500/499` are fixed bar-count constants, so no fixed-pip recalibration is needed across assets — cross-asset behavior differences are still real and unclaimed. The 24/7 crypto market has no opens/gaps/sessions for the rule to read beyond each bar's own prints (no session gating anywhere; the kernel treats each daily bar identically); decision boundaries are calendar-day bars of the venue feed, disclosed. The rule is two-sided, so a spot-only deployment expresses the long leg only and is NOT this record's version — short permission is assumed and disclosed. No funding-dependent leg, no stablecoin-specific assumption. The 1000-bar warmup consumes roughly 2.7 years of daily history before the first cue — disclosed as a data-availability cost. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- No price stop, no time stop: adverse excursion after a fade entry has no guardrail beyond the opposite rail's punch, which may arrive many bars later, after deep excursion, or never on a genuine breakout run. This is the record-rule posture, disclosed as a principal risk.
- Breakout blindness by design: every sustained trend begins as a rail punch against the position; the machine fades first and asks questions only at the far rail.
- Slow anchor: the 500-bar one-sided kernel re-rates sluggishly after volatility-regime shifts; post-shift extremes are judged against stale smooth history, by the prescribed design.
- Width uses the current-bar estimate across the whole deviation window (exactly as coded), so in a fast trend the rails lag twice — once in the center, once in the width.
- Rare signals: 3× MAE rails on daily bars fire infrequently; the machine sits flat-or-holding for long stretches, and sample counts per market are structurally small.
- Warmup cost: 1000 daily bars of venue history are consumed before the first legal cue — backtest coverage on young markets is structurally short, disclosed.
- Same-bar-close timing reading: the endpoint ▲/▼ markers confirm on bar close, matching the adopted fills; an engine modeling next-open entries would trade different (slightly later) events.
- Venue-portability residual: the rule carries only the arithmetic construction — any venue's prints, fees, funding, and short mechanics beyond the house model are unclaimed, disclosed.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior and never part of this admission — no Safety-Order/DCA event is admitted in this record's version. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Canonical TradingView strategy/indicator page, LuxAlgo (Nadaraya-Watson Envelope: kernel-smoothing envelope, contrarian methodology, endpoint non-repainting estimator, open-source script, fetched live during this cycle): https://www.tradingview.com/script/Iko0E2kL-Nadaraya-Watson-Envelope-LuxAlgo/
- Construction mirror read end to end this cycle, `marz-hunter/xauusd` file `scalping-5min/Nadaraya-Watson Envelope [LuxAlgo]` (118 lines; © LuxAlgo, CC BY-NC-SA 4.0; file commit `9d11d5c872` dated 2025-01-02; endpoint block, `h=8` / `mult=3` / `close` defaults, ▲/▼ cross pair verified from the pinned bytes): https://github.com/marz-hunter/xauusd
