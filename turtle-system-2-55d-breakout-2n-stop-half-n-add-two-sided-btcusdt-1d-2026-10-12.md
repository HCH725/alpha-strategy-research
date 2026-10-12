---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Turtle System 2 55-day breakout with 2N stops and half-N adds two-sided on BTCUSDT 1d
created: 2026-10-12
updated: 2026-10-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-12
sources:
  - https://www.tradingblox.com/originalturtles/originalturtlerules.pdf
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Turtle System 2 55-day breakout with 2N stops and half-N adds two-sided on BTCUSDT 1d

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Official site of the Original Turtles: https://www.tradingblox.com/originalturtles/ (rules page https://www.tradingblox.com/originalturtles/originalturtlerules.htm links the free complete-rules PDF with "No registration required").
- Exact file: https://www.tradingblox.com/originalturtles/originalturtlerules.pdf — 27 pages, retrieved 2026-10-12, SHA-256 `cfd448f2061379b7813eecec7d1a12d9eaa396a771da4db0b7be593d4`.
- Authorship as printed: the Complete Turtle Trading System rules as taught by Richard Dennis and William Eckhardt, published free and in full by an Original Turtle (Curtis Faith). Chapters read in full: 1 A Complete Trading System, 2 Markets, 3 Position Sizing, 4 Entries, 5 Stops, 6 Exits, 7 Tactics, 8 Further Study. The PDF carries a scanned-image text layer, so it was read via full-page renders of all 27 pages — no page skipped, no rule inferred from secondary summaries.
- Every numeric rule below (55/20, 20-day N, 1%, 1/2 N, 2 N, 4 units, 4/6/10/12 caps) is pinned to its chapter; anything not in those chapters is labeled a researcher-declared derivation in the declaration below.

Pre-write dedup (2026-10-12): case-insensitive working-tree searches for `turtle`, `system 2`, `system2`, `55-day`, `failsafe`, `whipsaw` (the source's alternate-stop name), and `2N` return no strategy record using this source or mechanism. The only `turtle` hit is a prose mention inside `donchian-20-10-breakout-btcusdt-1h-2026-10-06.md`, which is a different mechanism on five axes (Forven Pine source vs Original-Turtle rules; long-only 20/10 close-fill vs two-sided 55/20 stop-touch; zero stops/targets vs 2N stops; `pyramiding = 0` vs up-to-4-unit adds; no sizing concept vs volatility-unit sizing). The `55` inside the Klinger record is a slow-EMA length in a volume oscillator, unrelated. Open `research/*` PRs are only #48, #49, #63, #89, #92 (streak/channel/SuperTrend/Chandelier/SSL mechanisms) — no Turtle overlap in open, merged, or closed PRs.

## Economic mechanism

### Source-reported

Volatility-normalized trend following as a complete system (Ch 1–6): size every position so that 1N of adverse movement equals 1% of equity; enter on Donchian-channel breakouts; cut every losing leg with a predefined 2N stop (Ch 5: "non-negotiable exits ... each time, every time, without fail"); exit winning legs only on the opposite-direction channel breakout (Ch 6: most breakouts fail, so winners must be held long enough to pay for the losses); pyramid winners at 1/2 N intervals up to 4 units. No behavioral or risk-premium channel beyond capturing infrequent large trends is claimed.

### Research interpretation

Falsifiable hypothesis: a 55-day-extreme break on BTCUSDT 1d marks a volatility-adjusted regime displacement large enough to trend; N-based sizing keeps dollar risk per unit constant across volatility regimes; half-N pyramiding concentrates exposure only after the market confirms the break with further favorable movement. This port is research interpretation, not source-reported fact.

## Signal

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy built on source-offered System 2, not a lossless reproduction of the Turtle portfolio. Researcher-declared adaptations are exactly six: (1) market pin `BTCUSDT` on Binance USDT-M perpetuals, `1d` frame (the source trades a US-futures portfolio on daily bars); (2) System 2 only — the source explicitly offers this ("Some of us chose to trade all our equity using System 2"), so System 1, its last-breakout-winner skip filter, and the 55-day failsafe entry are out of scope by design, never silently dropped; (3) resting-stop touch-fill discretization on daily bars with gap-at-open fills (the source watches prices intraday; this record freezes the pinned-engine-compatible bar model below and never claims pit fills); (4) notional-equity accounting anchor `E = 10,000 USDT` with 0.001 BTC lot truncation (linear, event-neutral at this scale — disclosed); (5) adopted 60-bar warmup, flat by record rule (covers the 55-bar channel plus the 20-bar N seed plus 5 bars margin); (6) house costs/isolated-margin framing replacing pit commissions (see Execution assumptions). Channel lengths, N formula, unit formula, add spacing, stop distance, 4-unit cap, two-sided posture, and the breakout-exit rule are source-verbatim.

Frozen parameters (any other value is a different, unpinned rule): `entry_len = 55` / `exit_len = 20` / `N_len = 20` / `risk_pct = 1%` / `add_step = 0.5N` / `stop_dist = 2N` / `max_units = 4` / `tick = 0.01 USDT`.

Volatility (source-verbatim, Ch 3):

```text
TR_T = max(H_T - L_T, H_T - C_{T-1}, C_{T-1} - L_T)
N_seed = SMA20 of the first 20 TR values
N_T = (19 * N_{T-1} + TR_T) / 20
```

Unit sizing (source-verbatim, Ch 3; dollars-per-point is 1 USDT per 1 BTC of perp notional):

```text
Unit_BTC(T) = (0.01 * E) / N_{T-1}, floored to 0.001 BTC lots
```

If a floored unit is below the 0.001 minimum lot, the entry is skipped by record rule (deterministic; unreachable at E = 10,000 and normal BTC volatility — disclosed, never silently rounded up).

Reference levels for bar T, frozen from completed bars only (causal — nothing reads bar T or later):

```text
EL_long(T)  = max(H_{T-55..T-1}) + tick
EL_short(T) = min(L_{T-55..T-1}) - tick
XL_long(T)  = min(L_{T-20..T-1})    // long exit: 20-day opposite breakout
XS_short(T) = max(H_{T-20..T-1})    // short exit: 20-day opposite breakout
```

State machine (single market, never simultaneously long and short):

```text
flat + touch of EL_long  -> buy 1 unit (fill: EL_long; gap open beyond -> fill at open)
flat + touch of EL_short -> sell 1 unit (fill: EL_short; gap open beyond -> fill at open)
positioned + favorable touch of (last_fill +/- 0.5N) -> add 1 unit, while units < 4
  (each add reprices EVERY surviving unit's stop to newest_fill -/+ 2N, source-verbatim Ch 5;
   a gap through several add levels fills one unit per crossed level at the open, up to 4 total)
positioned + adverse touch of a unit's stop (entry -/+ 2N, repriced as above)
  -> that unit exits at its stop (gap-through -> fill at open; no Whipsaw re-entry, disclosed exclusion)
positioned + touch of the opposite 20-day exit level -> ALL surviving units exit at the level
  (gap-through -> fill at open)
```

Same-bar resolution order on bar T (fixed, conservative, fully specified): (1) stops of existing units; (2) opposite-breakout exit of survivors; (3) adds on survivors (sequential while the favorable extreme keeps reaching); (4) flat-state entries; (5) stop-check on units filled this same bar (same-bar entry-then-stop is possible, disclosed). Stop-first priority governs every same-bar overlap (protection before exits before adds before entries — a predeclared derivation; the source sequences by live price path, which daily bars cannot recover).

Entry tiebreak (predeclared derivation): a single bar can touch both entry levels (giant-range bar). The nearer level to the bar's open fills first as the first-touch-in-time proxy; an exact mid tie goes long. Opposite 55-day touch while positioned needs no extra rule: `min(L55) <= min(L20)` always, so a short-entry touch on a long-held bar implies the long exit already fired earlier in the same fixed order — reversals resolve deterministically.

Direction: two-sided. Long and short legs are symmetric; the short leg requires margin-short permission, realistic on the pinned perpetual venue. No always-in-market claim: flat states before the first signal, after exits/stops, and during warmup are explicit.

## Required data

- `1d` bars of one pair: `open/high/low/close` reading `high` (long entry/adds, short exit), `low` (short entry/adds, long exit), `close` (TR chaining only), `open` (gap-fill rule only). No volume, funding, OI, mark/index, L2, sentiment, or cross-market input anywhere in the signal path.
- Warmup is derivable and exact: 55 bars for the entry channel (the maximum lookback; the 20-bar N seed is a subset) plus 5 bars margin = first 60 completed `1d` bars flat by record rule; the first tradable bar is bar 61. Before that, all levels are undefined and the record holds flat — deterministic, no invention.
- No repainting, no negative shift, no full-sample normalization, no unfinished-bar read: every level for bar T is a function of bars `< T`.

## Execution assumptions

- Research market: `BTCUSDT` Binance USDT-M perpetual, `1d` decision frame, under the house overlay (declared port; the source venue is 1980s US futures — no cross-venue equivalence claimed beyond the same daily-bar breakout mechanics).
- Order timing (predeclared derivation): resting-stop touch-fill model on daily bars — entries, adds, stops, and breakout exits fill at their exact levels on touch; any gap opening through a level fills at the open (source-verbatim gap rule, Ch 4). Fixed same-bar order with stop-first priority and the nearer-to-open entry tiebreak (see Signal). Compatible with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) on the same first-touch stop-resolution path as the admitted fixed-RR/ATR stop-target records — no maker-touch, queue, or partial-fill claims; fills at level approximate the source's limit-order-near-market aspiration (Ch 7) and are disclosed as an approximation, with fast-market wait-and-stabilize tactics (Ch 7) explicitly scoped out.
- Sizing/capital/costs: source volatility-unit sizing preserved as the position-size rule (it prices adds, not just P&L); the `E = 10,000 USDT` notional anchor is event-neutral linear accounting. Maximum exposure is bounded by record rule: `V_max = 4 * 0.01 * E * P / N` USDT; adds that would breach Isolated 3x buying power are blocked (deterministic guard, disclosed derivation). Pinned Binance non-VIP USDT-M fees costed at taker (conservative vs the limit aspiration) plus realized historical funding accrual while positioned (long or short) — no hypothetical zero funding claimed anywhere.
- Concurrency: at most 4 units in one direction on this single market; no second market, so the source's 4/6/10/12 portfolio caps, buy-strength/sell-weakness selection, and contract rollover (Ch 2/3/7) are not-applicable by construction on a non-expiring single perp — disclosed, never silently kept. Re-entry after any flat needs only the next 55-day touch — no cooldown specified, explicitly none, not invented. The source's 20%-notional-shrink per 10% drawdown (Ch 3) is excluded by design (fixed notional) and fenced in Limitations.

## Evidence

### Source-reported

The rules document ships no performance table, figure, backtest, win rate, or return claim of any kind — this record therefore carries strictly zero performance figures, source-reported or otherwise. The document's only numbers are definitional (55/20/20-day, 1%, 1/2N, 2N, 4 units, 4/6/10/12 caps) and one worked sizing arithmetic example (Ch 3, Heating-Oil unit computation corroborating the Unit formula — cited as formula corroboration, never as performance). The Oct-1987 anecdote (Ch 3) is prose, not a table, and is not recorded as evidence.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- The Whipsaw alternate stop (1/2N stops with re-entry, Ch 5) is a documented source-offered variant that this record does NOT trade — listed here so no reviewer mistakes this file for it.
- System 1 with its last-breakout-winner skip filter and 55-day failsafe (Ch 4) is NOT in this record; System 2 takes every breakout with no filter (source-verbatim for S2).
- Take-profit, trailing-stop, and time-exit legs are absent in source and recorded as explicitly disabled, not as defaults to assume. The complete closing set is exactly: per-unit 2N stops plus the all-units 20-day opposite-breakout exit.
- The fixed notional excludes the source's drawdown shrink rule; any downstream overlay (DCA, shrink, second market) would change trade events and would be a different, separately specified strategy.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 55/20 lengths / 20-day N / 1% unit / half-N adds / 2N stops / 4-unit cap / two-sided / BTCUSDT 1d / stop-touch fills are frozen.

- F1 — Channel relevance: a 20/10 twin (same stops, adds, sizing, fills) must not improve net expectancy; fail ⇒ the 55/20 geometry adds nothing over its shorter twin.
- F2 — Stop relevance: removing the 2N per-unit stops while keeping entries, adds, and breakout exits (same fills otherwise) must not improve net expectancy; fail ⇒ the coded stops add nothing over their unstopped twin.
- F3 — Add relevance: single-unit-only (no half-N adds, same entries/stops/exits) must not improve net expectancy; fail ⇒ pyramiding adds nothing over its single-unit twin.

## Crypto portability

Perpetuals never expire, so contract rollover is structurally absent (not silently ignored). 24/7 trading removes pit-session gaps; the gap-at-open fill rule then binds only on volatility jumps, still deterministic. Shorts are native to USDT-M margin (no uptick rule, no borrow desk). Tick (0.01 USDT) and lot (0.001 BTC) granularity are stated above. Single-market porting drops the portfolio breadth the source relies on for diversification — this record makes no diversification claim and must not be read as the source's multi-market system.

## Limitations

- Discretized daily-bar stop-touch fills are an approximation of pit order watching, not pit fills; limit-aspiration and fast-market patience (Ch 7) are scoped out — fills at level/open are the frozen model.
- System-2-only by design: Sharpe-relevant S1 trades are missed on purpose; this file is never evidence about System 1.
- Fixed 10,000 USDT notional with no drawdown shrink: deeper drawdowns than the source's shrink rule would permit — downstream must size accordingly.
- First-touch ordering (stop-first, nearer-to-open tiebreak) is a researcher discretization where the source follows live path; same-bar multi-event bars resolve by record rule, disclosed above.
- Funding is flagged as realized-accrual, not yet verified against a funding-accounting implementation; representative event-level Qlib/Hummingbot parity is required before any mass screening, not claimed here.

## Implementation status

Not implemented. No code was executed and no Hummingbot/Qlib/n8n run was performed in this cycle; all compatibility statements above refer to the pinned-model path shared with the admitted stop-target records.

## Adoption boundary

Research-only. Not approved for Paper, Testnet, or Live trading. No downstream screening, sizing, or deployment authorization is granted by this record.

## Related Wiki records

None.

## Sources

- https://www.tradingblox.com/originalturtles/originalturtlerules.pdf (primary — 27-page complete-rules PDF, SHA-256 `cfd448f2061379b7813eecec7d1a12d9eaa396a771da4db0b7be593d4`, retrieved 2026-10-12)
- https://www.tradingblox.com/originalturtles/originalturtlerules.htm (official rules page identifying the PDF as the free complete rule set)
