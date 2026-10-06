---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven S01512 Monday Drift weekly calendar-hold system on BTCUSDT 1h bars
created: 2026-10-06
updated: 2026-10-06
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-06
sources:
  - https://github.com/judder659/Forven/blob/98266984fa85391e58760eb6a1b5e45707504ecd/forven/docs/pine/monday_drift.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven S01512 Monday Drift weekly calendar-hold system on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project with package, docs, frontend, and license files; 358 stars as read on 2026-10-06).
- Pinned commit SHA: `98266984fa85391e58760eb6a1b5e45707504ecd` (`ls-remote` HEAD check on 2026-10-06 confirms this is still the repository head).
- Exact file path: `forven/docs/pine/monday_drift.pine`.
- GitHub blob SHA at the pinned commit: `84f73bcf0a06c61ffb72d132605e05451c786689`, size 4635 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is byte-identical (`cmp` clean on re-download) to the copy inspected; SHA-256 `94d22114e1cd84ca1f422ea47c93738d4acfe03a8bb0da05f87020d83bfa16aa`, 4635 bytes.
- The file is a 98-line Pine v6 program (`//@version=6`) with a header comment block identifying it as "Monday Drift — TradingView clone of Forven S01512", strategy_id `S01512 (monday_drift)`, dataset `BTC/USDT-1h (binance)`, window `2023-12-31 00:00 UTC → 2026-04-19 23:00 UTC`, leverage `1x`, fee model `~11 bps round-trip (5.5 bps per side)`.
- The `S01512` identifier occurs nowhere else in the repository (code search returns only this file), so there is no competing variant to choose between.

Pre-write dedup (2026-10-06): case-insensitive search of the working tree for `monday`, `dayofweek`, `s01512`, `forven`, `seasonal` returns no calendar/weekday strategy (the only `drift` hits are the English word inside mechanism prose of three unrelated indicator records); `supertrend` hits are likewise only passing mentions, and no pool record uses a calendar signal. `gh pr list --state open` is empty, so no open `research/*` PR shares this source or signal. Against the 9 records on `main` (ATR breakout, ADX exhaustion, dynamic RSI, Hull/EMA band, Gann HiLo, Ichimoku + ADX, erf dead-band, Kaufman pivots, VIDYA + CMO): mechanism, signal construction, and source identity are all distinct.

## Economic mechanism

### Source-reported

The source claims only what its header prints: a "pure calendar strategy" that trades "once a week, 24-hour hold" — long Monday 00:00 UTC, flat Tuesday 00:00 UTC. No behavioural, structural, or risk-premium channel is claimed. The header's robustness note (OOS Sharpe 1.24 on a 70/30 split over ~118 trades "is not a lucky streak", effect "held across BTC and SOL", deploy with a win-rate kill-switch below 55% over 5 live trades) is position sizing/risk commentary, not mechanism.

### Research interpretation

Falsifiable hypothesis: the Monday 00:00 UTC → Tuesday 00:00 UTC window captures a week-open drift — weekend information accumulation and week-start rebalancing flows expressing as a positive 24-hour drift in BTC often enough to carry a long-only weekly hold. The bet is calendar-seasonal direction, not any price-pattern reading: the rule never looks at price. This is a ported seasonality hypothesis; the source supplies no sample beyond its own backtest window and no evidence beyond the table cited below, so the mechanism is research interpretation, not source-reported fact.

## Signal

All symbols below are the program's own identifiers; all values are program defaults, pinned.

Engine semantics (explicit in source): `process_orders_on_close = true`, `calc_on_every_tick = false`, `pyramiding = 0`. Completed-bar decision with same-bar-close execution; no intrabar evaluation.

Inputs (defaults):

```text
entry_dow = 2 (Monday; Pine dayofweek scale 1=Sun..7=Sat), entry_hour = 0 (UTC)
exit_dow  = 3 (Tuesday),                              exit_hour  = 0 (UTC)
use_window = true
start_ts = 1703980800000 (2023-12-31 00:00:00 UTC)
end_ts   = 1776675600000 (2026-04-19 23:00:00 UTC)
```

Clock (exact, deterministic functions of bar time only):

```text
dow = dayofweek(time, "UTC"); hr = hour(time, "UTC")
in_window = not use_window or (time >= start_ts and time <= end_ts)
is_entry_bar = (dow == entry_dow) and (hr == entry_hour)
is_exit_bar  = (dow == exit_dow)  and (hr == exit_hour)
```

Trade events (the complete order-call set — one `strategy.entry`, one `strategy.close`, one window-end `strategy.close_all`, zero `strategy.exit`/`strategy.order` calls):

```text
if in_window and is_entry_bar -> strategy.entry("MondayLong", strategy.long)
if is_exit_bar                  -> strategy.close("MondayLong")
if use_window and (time > end_ts) -> strategy.close_all()
```

Direction: long-only. The program contains no short entry path, so the short side is absent by construction and recorded as explicitly disabled. Spot-compatible (no naked shorting required); leverage in the source backtest is 1x.

Exits and risk (explicit): signal exit is the time-based Tuesday 00:00 UTC close (24-hour hold); opposite-signal exit is not applicable (no opposite signal exists); stop loss, take profit, trailing stop are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `strategy.close` on a flat position (e.g. an exit bar with no open entry) is a deterministic no-op.

Position and re-entry (explicit): `pyramiding = 0` with a single entry id means same-side re-entry while positioned is rejected by the engine; after the Tuesday exit the position is flat, so the next Monday entry is the only possible re-entry — fully specified, no cooldown, no missing rule. `strategy.position_size` appears only in a `bgcolor` visual, never in signal logic.

Calendar-data note for the reviewer: the signal reads no price at all — only `time` via `dayofweek`/`hour` in fixed UTC. Bar timestamps are part of candle data available to the pinned backtester; the transform is a pure deterministic function with no external feed, no session table, and no look-ahead (the timestamp of a completed bar is known at its close). The program contains zero `request.*`, `barstate.*`, indicator, or price references in signal logic.

## Required data

- 1h bars of one pair carrying trustworthy UTC timestamps; the rule reads `time` only. No OHLCV fields, no indicators, no timeframe reference, no funding/OI/mark feeds, no order-book, news, or cross-venue state.
- Crypto 24/7 trading means Monday 00:00 and Tuesday 00:00 UTC bars always exist; no weekend-gap handling is needed or present.
- Warmup is derivable and trivial: zero lookback — one bar (the bar whose own timestamp is evaluated).

## Execution assumptions

- Source execution semantics: `process_orders_on_close = true` — on 1h bars the Monday 00:00 UTC bar (opening exactly at 00:00) is the entry bar with fill at its close; the Tuesday 00:00 UTC bar is the exit bar with fill at its close. Nominal hold is 24 hourly bars. Compatible with the pinned Hummingbot baseline lane; no conversion required.
- Research market (explicitly labeled house overlay, not source-native): `BTCUSDT`, `1h` decision timeframe. The source dataset is Binance `BTC/USDT-1h`; because the signal is a pure function of bar timestamps, substituting the USDT-margined quote price series cannot change any signal, event, direction, or timing — the substitution is event-neutral and the label keeps contract identity explicit.
- Source sizing (`strategy.percent_of_equity`, 100) and the source commission model (0.055% per side, ~11 bps round trip) are event-neutral accounting: replaced downstream by the standard house execution overlay (Base 6% + Safety 6% + 6%, Isolated, 3×/5×, pinned Binance fees plus realized funding). The overlay changes no signal, event, or exit.
- Window inputs (`use_window = true` with the fixed Forven window) are backtest scope, not signal: they exist so TradingView totals line up with the Forven run. Both facts are pinned as read — the core weekly rule is window-independent, while the as-coded defaults trade only inside 2023-12-31 → 2026-04-19 and force flat afterwards. Downstream must state which scoping it applies; it must not silently re-tune the window on final OOS data.

## Evidence

### Source-reported

Printed in the file header comment (traceable to the header table, not reproduced from anywhere else):

```text
Full run (~2y 3m, BTC, long-only, 1x, ~11 bps round-trip):
  118 trades, win_rate 0.542, CAGR +94.45%, Sharpe 1.41, max_dd 44.33%, profit_factor 1.70
OOS segment: CAGR +58.39%, Sharpe 1.24 (70/30 split)
1-year slice 2025-04-20 → 2026-04-19: TV 53 trades / 0.491 / +18.77% / PF 1.60
  vs Forven 50 / 0.460 / +14.50%
```

Recorded exactly as printed, including the 53-vs-50 trade-count mismatch between the two engines on the same slice (stated, not explained away).

### Independently reproduced

Not independently reproduced.

### Negative evidence

No contradictory performance or failure report is cited in source. The absence of evidence is recorded as absence, not as support.

## Falsification plan

Research tests only — none of these substitutes for a missing rule (no rule is missing):

1. Weekday permutation: run the identical 24-hour-hold rule on Tuesday→Wednesday through Sunday→Monday; if Monday shows no edge over the other six weekday legs out-of-sample, the calendar hypothesis is rejected.
2. Subperiod stability: split the window into halves; a sign flip or collapse in either half rejects robustness (the source's own 70/30 OOS split is the baseline to beat, not to re-tune on).
3. Cost sensitivity: re-run with round-trip costs doubled; a calendar edge that needs sub-11-bps costs to survive is execution fiction, not signal.
4. Engine parity: reproduce the 2025-04-20 → 2026-04-19 slice trade by trade and explain the 53-vs-50 count gap before trusting any port.
5. Always-flat-before-first-entry accounting: verify the backtest holds flat until the first Monday 00:00 UTC bar in scope; any deviation is an implementation bug, not a strategy property.

## Crypto portability

The rule ports cleanly to 24/7 crypto bars precisely because it ignores price: no session calendar, no gap logic, no dividends/splits, no exchange-timezone call beyond the fixed UTC clock already in source. One port note: the pinned defaults trade only inside the hardcoded Forven window, so a downstream run on full BTCUSDT 1h history must explicitly declare its window scoping (see Execution assumptions) rather than inheriting a 2026-04-19 cutoff silently.

## Limitations

1. No protective stop exists in source; tail risk during the 24-hour hold is borne fully by the time exit. Recorded as explicitly disabled per source — must not be "repaired" with an invented stop.
2. The fixed backtest window is part of the pinned defaults. The weekly rule itself is window-independent, but any downstream run must state its scoping; re-tuning the window on final OOS data is forbidden by the house overlay contract.
3. The header's cross-asset claim ("held across BTC and SOL") ships no SOL table in this file and is therefore not cited as evidence — only the BTC numbers above are recorded.
4. Confidence is `medium` (interpretation confidence): the rule text is complete and unambiguous with zero price-dependent ambiguity, but the source offers only its own backtest table, no peer review, and no market-microstructure account of the Monday effect.
5. Only program defaults are pinned. Input variants (different weekday legs, hours, or windows) are research tests, not separate strategies, and must not be cherry-picked.

## Implementation status

- `not-implemented`. No Hummingbot/Qlib/n8n/Paper/Testnet/Live work has been performed or is authorized by this record.

## Adoption boundary

- `research-only`, `not-approved`. Admission of this record would mean only that its core signal and causal trade-event semantics are losslessly expressible under the pinned backtester with the labeled house overlay — not profitability, survival, or any trading approval.

## Related Wiki records

- None. No Wiki Brain write was performed for this cycle.

## Sources

- Immutable program file at pinned commit (all rules): https://github.com/judder659/Forven/blob/98266984fa85391e58760eb6a1b5e45707504ecd/forven/docs/pine/monday_drift.pine
- Repository (project context, 358 stars as of 2026-10-06): https://github.com/judder659/Forven
