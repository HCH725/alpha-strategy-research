---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: STARC band breakout latched two-sided on BTCUSDT 1d bars
created: 2026-10-11
updated: 2026-10-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-12-05
sources:
  - https://www.fmz.com/strategy/434325
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/STARC%E9%80%9A%E9%81%93%E5%9B%9E%E6%B5%8B%E7%AD%96%E7%95%A5STARC-Channel-Backtest-Strategy.md
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# STARC band breakout latched two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-11):

- Canonical page: https://www.fmz.com/strategy/434325 (page title carrying `STARC Channel Backtest Strategy` 22 times page-wide, author token `ChaoZhang`, code token `HPotter`, and reusable parameter token `1.33` present page-wide). Fetched live over HTTPS during this cycle with HTTP 200 (766633 bytes). The page embeds the executable `/*backtest*/` header verbatim: `start: 2023-11-04 00:00:00`, `end: 2023-12-04 00:00:00`, `period: 2h`, `basePeriod: 15m`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`. The ZH/EN prose states the rule twice: baseline = n-day SMA, upper band = SMA + K x ATR, lower band = SMA − K x ATR, buy when close breaks above the upper band, sell when close breaks below the lower band, plus a long/short switching mechanism — and it explicitly recommends `日线等中长线周期` (daily and other medium-long cycles) as the suitable trading cycle (adopted as `source_as_of` 2023-12-05 from the mirror's `> Last Modified` stamp 2023-12-05 14:52:20). Word-boundary counts over the whole landing HTML: `Sharpe` 0, `Win Rate` 0, `Max Drawdown` 0, `Annualized` 0, `Profit` 0 — the page ships no performance numbers of any kind.
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (commit date 2025-04-30 11:10:28 +0800; repository head verified via the GitHub commits API — the same head pin as the merged KST, Schaff, TRIX, SQZMOM-LB, Aroon, Qstick, AC, Elder-ray, Fibonacci, FRAMA, Balance-of-Power, ROC, WaveTrend and T3-Tillson admissions), exact file path `STARC通道回测策略STARC-Channel-Backtest-Strategy.md` (non-ASCII filename preserved verbatim; percent-encoded blob URL in Sources). File 8388 bytes, blob SHA `87717f5e554bbbff901c149bf08583fd414dad8f` (verified against the GitHub contents API at the pinned commit — size and SHA both match). The mirror prints `> Author` = `ChaoZhang` (mirror porter), `> Detail` = https://www.fmz.com/strategy/434325, and its `[trans]` prose matches the canonical page text quoted above. The executable Pine block carries its own header `// Copyright by HPotter v1.0 23/04/2018` (no licence tag ships — cited, never redistributed beyond single-line declarations quoted for gate evidence).
- Full `//@version=2` block read in full (37 Pine lines, `strategy(title="STARC Bands Backtest", overlay = true)` — no sizing, capital, cost, timing, or pyramiding argument ships anywhere in the declaration). The executable order block is the two pinned inputs feeding one SMA plus one ATR, the two band arithmetics, the `pos` latch, the `possig` selector, and the two state-guarded entries: `if (possig == 1)` → `strategy.entry("Long", strategy.long)`; `if (possig == -1)` → `strategy.entry("Short", strategy.short)`. Everything else is display-only (`barcolor`/`plot` x3 — feeding no order condition).
- Text census over the pinned code block: 1 `strategy(` / 2 `strategy.entry` (`"Long"`/`strategy.long`, `"Short"`/`strategy.short`, both inside single-`if` state guards, no `when=`/`qty=`/`limit=`/`stop=` qualifiers) / 0 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 0 `security(` / 0 `request.*` / 0 `timeframe(` / 0 `time(` / 0 `volume` / 0 `barstate` / 0 `timenow` / 0 `ta.` (v2 built-ins `sma(` x1 / `atr(` x1 only) / 0 `crossover` / 0 `crossunder` / 0 `cross(` / 1 `nz(` (`nz(pos[1], 0)`, the latch seed only) / 0 `var` / 0 `pyramiding` / 0 `process_orders_on_close` / 0 `calc_on_every_tick` / 0 `max_bars_back` / 0 `initial_capital` / 0 `default_qty` / exactly 4 `input(` (`LengthMA = input(5, minval=1)`, `LengthATR = input(15, minval=1)`, `K = input(1.33, minval=0.01, step = 0.01)`, `reverse = input(false, title="Trade reverse")`). No portable economics of any kind ships anywhere — recorded as an absent-economics stub, never as zero-cost evidence.
- No risk layer ships anywhere in the source: zero close/exit/risk legs. Reversal through the opposite entry is therefore the only coded position-closing path, pinned as written (declared explicitly, never hidden), not a researcher invention.

Licence and rights: the executable block ships an HPotter copyright line via the public FMZ publication with no licence tag; this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) market/frame pin `BTCUSDT 1d` (the code names no market and no timeframe; the mirror's executable `/*backtest*/` stanza backtests `Futures_Binance BTC_USDT` at `period: 2h`/`basePeriod: 15m`, while the page prose explicitly recommends daily and other medium-long cycles — this pin follows the prose recommendation on the stanza's venue, disclosed here, never presented as source-native); (2) same-bar-close fills (the source ships no execution-timing argument — Pine default evaluates per completed bar and fills on the next bar; no `process_orders_on_close` ships anywhere, quoted verbatim in census); (3) an adopted 100-bar warmup with pre-warmup bars flat by record rule (covers the SMA(5) plus the RMA-smoothed ATR(15) seed with margin — see Required data); (4) house sizing/capital/costs replacing the absent source economics (see Execution assumptions). The SMA/ATR variants, `5`/`15`/`1.33` inputs, the strict band-break tests, the `pos` latch with `reverse = false`, the every-bar state entries with reversal-only exits, and the no-stop/no-target/no-cooldown stance are source-native and unmodified. No tie-break had to be invented: the source calls no `cross`/`crossover` function anywhere — every comparison is a strict inequality with a single deterministic outcome per bar (see Negative evidence).

Pre-write dedup (2026-10-11): working-tree case-insensitive searches for `starc`, `stoller`, and `434325` return zero hits in any strategy record — no `main` record evaluates a STARC band anywhere. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `keltner-momentum-breakout-gated-btcusdt-1d` breaks an EMA(20) ± 1.5 x ATR(20) envelope AND-gated with a 14-bar momentum-sign filter, closes legs explicitly (`strategy.close` x2), and fires on v5 cross events (FMZ 481364, 2025) — this record breaks an SMA(5) ± 1.33 x ATR(15) envelope with no momentum gate, no close leg (reversal-only exits), and v2 strict-inequality latch tests (FMZ 434325, HPotter 2018); `sideways-dmi-bollinger-breakout-long-btcusdt-4h` breaks standard-deviation bands (a dispersion multiple, never an ATR range multiple); `donchian-20-10-breakout-btcusdt-1h` breaks highest-high/lowest-low rails (no average at all). No pool record computes an SMA-centred ATR-multiple channel, latches its break state across bars, or pins the 5/15/1.33 triple.

## Economic mechanism

### Source-reported

Short-horizon breakout capture on a self-scaling range channel (mirror prose plus code): Manning Stoller's channel centres on a fast SMA(5) of close and widths itself with the market's own recent range — 1.33 multiples of ATR(15) — so the band breathes with realised bar size rather than with a fixed distance or a statistical multiple. A close printing above the upper band is prescribed as trend evidence for the long side; a close below the lower band is the exact image for the short side. The `pos` latch then holds the posture through any bar that prints back inside the channel, so exits need no target: the design bets that a range-channel break on the fast 5/15 pair resolves further in the break direction, and that the opposite break — not a level — is the timely exit. There is no stop, no target, no flat-holding logic beyond the pre-first-entry flat.

### Research interpretation

Fast range-channel breakout system, two-sided, latched, always-in-market after the first entry. Unlike the Keltner-family record, there is no second opinion anywhere: no momentum gate, no second average, no volume print — the close-versus-band test alone moves the book, and the latch supplies all the patience the system has. Inside-the-channel bars are structural rests (the latch carries the old posture forward, so chop that never reaches a band never trades), while the price of the latch is commitment: a leg whose opposite band never breaks is held indefinitely, and alternating breaks print full reversals with no resting flat. The entries re-fire on every in-state bar, but with no pyramiding argument shipped anywhere the effective path under the shipped Pine defaults is open-then-hold with full reversal on the opposite break — same-side refires cannot open additive exposure (see Execution assumptions). The bet is on fast SMA-centred range breaks, not on any slope test, volatility-multiple gate, volume confirmation, calendar effect, or second timeframe.

## Signal

Exact rule as pinned (`LengthMA = 5`, `LengthATR = 15`, `K = 1.33`, `reverse = false` frozen — any other value is a different, unpinned rule):

- Declarations (derived): single-position state machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). State ∈ {flat, long, short}; flat exists only before the first entry — after the first `"Long"`/`"Short"` fill the latch is 1 or −1 and the book is always positioned.
- STARC bands, pinned verbatim: `xMA = sma(close, 5)`; `xATR = atr(15)` (v2 RMA-smoothed true range, causal); `xSTARCBandUp = xMA + xATR * 1.33`; `xSTARCBandDn = xMA − xATR * 1.33`.
- Latch and entries (pinned verbatim): `pos(t) = close(t) > Up(t) ? 1 : close(t) < Dn(t) ? −1 : nz(pos(t−1), 0)`; `possig(t) = pos(t)` at pinned `reverse = false`; `possig == 1` → `strategy.entry("Long", strategy.long)`; `possig == −1` → `strategy.entry("Short", strategy.short)`. From flat the first in-state bar opens the leg; from the opposite leg the entry reverses in full as a single atomic reversal event (Pine opposite-side entry semantics); same-side refires on subsequent in-state bars add no exposure under the shipped no-pyramiding declaration. The `reverse = true` reading (long where the rule says short) is a different, unpinned rule — explicitly not this record. No stop, no target, no trailing, no time exit, no cooldown — pinned as written (zero close/exit/risk legs ship anywhere), explicitly none, not invented.
- Strict-inequality determinism: a close printing exactly on either band satisfies neither break leg (the latch holds by fall-through); `Up(t) > Dn(t)` strictly whenever `xATR(t) > 0`, and a zero-range bar simply narrows the channel to the midline while both tests stay strict and deterministic. No tie-break is invented because none is needed.
- Direction: two-sided with pre-first-entry flat only. A long-only or short-only reading would contradict the prescribed `"Short"` leg; each is a different, unpinned rule.

## Required data

- Completed `1d` bars of BTCUSDT: `close` (midline source and break test), `high`/`low` (inside the ATR true-range chain only — no order-gating line reads them directly). No `open`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (derived pin following the prose's explicit daily-cycle recommendation; the body contains no `security(`/`request.*` call, so the derived rule is single-frame by construction).
- Warmup: the binding seed is the RMA-smoothed ATR(15) (time constant 15 bars — five to six constants ≈ 75–90 bars to settle; the SMA(5) is negligible beside it). The adopted warmup is the first 100 completed `1d` bars flat by record rule (predeclared researcher choice — covers the ATR seed plus margin; no traded bar reads a seeded value). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Each bar's OHLC enters the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (derived pin following the executable header's `Futures_Binance BTC_USDT` venue with the prose's explicit daily-cycle recommendation — venue transfer and symbol spelling are disclosed here, never presented as source-native). Full two-sided expression assumes a futures venue; a spot-only deployment expresses the long state and reversal mechanics only to the extent the venue permits shorting — disclosed.
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar fill (no execution-timing argument ships anywhere — quoted verbatim in census); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and the two state guards are mutually exclusive per bar, so each bar's outcome is a single deterministic event (hold, open, or atomic reversal) under either fill convention.
- Sizing/capital/costs: the source ships no portable economics of any kind (no `initial_capital`, no `default_qty`, no commission/slippage/funding argument ships anywhere — recorded as an absent-economics stub, never as zero-cost evidence) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: single-position machine by latch-plus-default construction — at most one open leg; same-side refires on consecutive in-state bars add no exposure (no `pyramiding` ships anywhere and none is needed for the effective path); the opposite break reverses in full as one atomic event; re-entry is allowed on the next fresh opposite break after any reversal (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The mirror ships the full construction (SMA(5) midline, ATR(15) range chain, 1.33 multiple, both band arithmetics, the `pos` latch with `nz(pos[1], 0)` seed, the `reverse = false` selector, the two state-guarded `"Long"`/`"Short"` entries, and the `/*backtest*/` stanza (2023-11-04→2023-12-04, `Futures_Binance BTC_USDT`, `period: 2h`/`basePeriod: 15m`)), plus the prose rule statement and the explicit daily-cycle recommendation — quoted in Provenance. It ships no portable performance: no table, no figure, no metric — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: the body contains zero `strategy.close` / `strategy.exit` / `strategy.order` legs and zero `stop=`/`limit=` qualifiers; the only position-closing path is the opposite-side `strategy.entry` reversal on the next opposite break. The no-stop/no-target/no-time posture is prescribed, explicitly none, never hidden.
2. Break exclusivity fenced: the long leg requires `close(t) > Up(t)` while the short leg requires `close(t) < Dn(t)` — with `Up(t) ≥ Dn(t)` always, no bar satisfies both guards, so no priority rule is needed or invented, and no bar produces both an open and a reversal.
3. Same-side refire semantics stated plainly: the entries fire on every in-state bar (not only on latch change — unlike flip-detector records), but no `pyramiding` argument ships anywhere, so under the shipped declaration same-side refires open no additive exposure — the effective path is open-then-hold with full reversal on the opposite break. Any stacked-adds reading would contradict the shipped declaration and is explicitly not this record.
4. On-band and zero-range determinism fenced: a close exactly equal to either band fails the strict `>`/`<` test (latch holds by the ternary fall-through); a zero-range bar narrows both bands onto the midline while every test stays strict. Both outcomes fall directly out of the quoted strict inequalities — no researcher tie-break, no alternative reading.
5. Latch-seed fence, stated plainly: `nz(pos[1], 0)` seeds the pre-history latch at 0 (flat), and while `sma`/`atr` resolve from `na` the strict comparisons cannot print a break — combined with the record-rule 100-bar warmup flat, no seeded value ever trades.
6. `reverse` fence, stated plainly: the pinned rule holds `reverse = false` so `possig = pos`; the `reverse = true` mirror image (long where the rule says short) is fully coded but is a different, unpinned rule — explicitly not this record.
7. No future leakage in the stack, stated plainly: at decision bar `t` the slowest input is the RMA-ATR(15) resolving long before the 100-bar warmup ends — every input is complete at bar `t`'s close. No `security()`, no `request.*`, no negative index, no `time` read at all, no `barstate`-gated path. All `barcolor`/`plot` calls render only and drive no order.
8. HLC data fence, admitted plainly: the order-gating chain reads venue `high`/`low` through the ATR true-range smoother — venue bar-construction differences can touch `xATR`, both bands, and hence every break test. A venue that cannot supply completed HLC daily bars cannot trade the pinned rule; extension to heikin-ashi or otherwise resampled feeds would be a different, unpinned rule.
9. Always-in-market posture provably complete: after the first entry the latch is ±1 with symmetric state entries on both legs — the book is long or short on every post-warmup bar. No third direction exists; the flat state exists only pre-first-entry.
10. Derivation boundary fenced: the only non-source-native behaviors in this record are the `BTCUSDT 1d` market/frame pin, same-bar-close fills, the adopted 100-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the SMA/ATR variants, the `5`/`15`/`1.33` inputs, the band arithmetics, the strict break tests, the latch with `reverse = false`, the reversal-only exit path, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, or timing of the source passes.
11. Network limitation disclosed: every formula line above was byte-verified in the pinned mirror file at commit `7853bb2` (8388 bytes, blob SHA recorded, matching the contents API at the pinned SHA); the FMZ canonical page verified live the title, the `ChaoZhang`/`HPotter` tokens, the ZH/EN rule prose with its daily-cycle recommendation, the `1.33` parameter, and the `Futures_Binance BTC_USDT` backtest stanza — the division of evidence is disclosed here, not hidden.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: SMA(5) / ATR(15) / K = 1.33 / strict band-break tests / latch with `reverse = false` / reversal-only exits / no-stop-no-target posture / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Channel relevance: dropping the ATR width (naked SMA(5) midline-cross latch, same entries) must not improve net expectancy; fail ⇒ the 1.33 x ATR range width adds nothing over the bare midline.
- F2 — Short-leg relevance: disabling the short leg (long-only with the same band-break entries, closing to flat on the opposite break) must not improve net expectancy; fail ⇒ two-sided expression adds nothing over the long leg alone.
- F3 — Fast-specification relevance: replacing the 5/15 pair with a slow 20/20 STARC reading (same 1.33 multiple, same latch) must not improve net expectancy; fail ⇒ the pinned fast specification adds nothing over a slow reading of the same channel.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (derived pin following the executable header's own `Futures_Binance BTC_USDT` venue with the prose's explicit daily-cycle recommendation). The SMA/ATR arithmetic ports across perpetual venues without structural change, but venue bar-construction differences touch `high`/`low` and hence the ATR chain, both bands, and every break test — disclosed above, not hand-waved. The range channel auto-scales in the asset's own price units, so no fixed-pip recalibration is needed across assets — cross-asset behavior differences are still real and unclaimed. The rule is two-sided with no stop leg, so a spot-only deployment expresses the long state and reversal mechanics only to the extent the venue permits shorting — full two-sided expression assumes a futures venue, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no session gating anywhere); decision boundaries are calendar-day bars of the venue feed, disclosed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-bar with no timing argument; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- Derived market and frame: the code names no market and no timeframe, and its stanza backtests `2h`/`15m`; this record pins `BTCUSDT 1d` following the prose's explicit daily-cycle recommendation on the stanza's venue. Cross-market and cross-frame behavior differences are real — the adaptation is disclosed, and this record makes no claim about any other market, frame, or the source's native setting.
- Always-in-market commitment: after the first entry the book is never flat; adverse excursion after entry has no guardrail beyond the opposite break, and a leg whose opposite band never breaks is held indefinitely. This is the prescribed posture, disclosed as the principal risk.
- Whipsaw sensitivity: alternating breaks print repeated full reversals with no flat state to rest in, and a touch that stops inside the channel strands the book in the old leg through the whole move. The break-plus-latch asymmetry is the prescribed design, disclosed, not smoothed.
- No source economics: beyond the bare `strategy(...)` title/overlay plumbing the source ships no capital, sizing, commission, slippage, funding, or margin assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Seed coverage: the RMA-ATR(15) needs roughly 75–90 completed closes plus margin; the first 100 `1d` bars are flat by record rule, so early-history signals never enter any evaluation.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- FMZ canonical strategy page (rule prose with daily-cycle recommendation plus `Futures_Binance BTC_USDT` backtest stanza verified live via HTTP-200 page record): https://www.fmz.com/strategy/434325
- Immutable mirror file at pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (blob `87717f5e554bbbff901c149bf08583fd414dad8f`, 8388 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/STARC%E9%80%9A%E9%81%93%E5%9B%9E%E6%B5%8B%E7%AD%96%E7%95%A5STARC-Channel-Backtest-Strategy.md
- Pine strategy semantics (order calls, default execution, built-in `sma`/`atr` semantics): https://www.tradingview.com/pine-script-reference/v5/
