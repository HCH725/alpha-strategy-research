---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven S01509 Simple Donchian 20/10 breakout system on BTCUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/98266984fa85391e58760eb6a1b5e45707504ecd/forven/docs/pine/simple_donchian_breakout_demo.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven S01509 Simple Donchian 20/10 breakout system on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project with package, docs, frontend, and license files; 358 stars as read on 2026-10-06).
- Pinned commit SHA: `98266984fa85391e58760eb6a1b5e45707504ecd` (`ls-remote` HEAD check on 2026-10-06 confirms this is still the repository head, same pin as the S01512 Monday Drift admission).
- Exact file path: `forven/docs/pine/simple_donchian_breakout_demo.pine`.
- GitHub blob SHA at the pinned commit: `35874ebe709a6d4c19786c2ae7f0daf6f847e920`, size 4839 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is byte-identical (`cmp` clean on re-download) to the copy inspected; SHA-256 `887460b8e4bdbaed70b6f7f1a6d3563ba4bd7d1e739d9b279ee5d3349161e258`, 4839 bytes, 101 lines.
- The file is a Pine v6 program (`//@version=6`) with a header comment block identifying it as "Simple Donchian 20/10 Breakout — TradingView clone of Forven S01509", strategy_id `S01509 (simple_donchian_breakout_demo)`, dataset `BTC/USDT-1h (binance)`, window `2025-04-19 16:00 UTC → 2026-04-19 16:00 UTC (8760 bars)`, leverage `1x`, fee model `~11 bps round-trip (5.5 bps per side) inferred from trades`.
- The `S01509` identifier occurs in exactly one file in the repository (code search returns only this path), so there is no competing variant to choose between. The sibling demo `simple_ema_cross_demo.pine` (S01508) is a different mechanism (EMA cross with `ta.crossover`/`ta.ema`) and is not this candidate.

Pre-write dedup (2026-10-06): case-insensitive search of the working tree for `donchian`, `s01509`, `highest(high` returns no strategy record using this source or signal — the only `donchian` hits are `[[quant/tradingview-choppiness-donchian-breakout-filter-2026-09-16]]` Wiki links inside the Related-Wiki sections of two unrelated indicator records (VIDYA-CMO, Gann-HiLo), not strategy mechanisms. `gh pr list --state open` is empty, so no open `research/*` PR shares this source or signal. Against the 10 PASS records on `main` (Bookstaber ATR breakout, DMI Swings ADX-45 exhaustion, DRM dynamic RSI, EHMA range band, Gann HiLo, Ichimoku + ADX, Monday Drift calendar hold, P-Signal erf dead-band, Kaufman pivots, VIDYA + CMO): mechanism, signal construction, and source identity are all distinct. The TV-mirror Donchian/Chandelier/Keltner/Aroon batch killed in the prior cycle were v4 files without `process_orders_on_close` from a different mirror source — different canonical source identity and different program semantics.

## Economic mechanism

### Source-reported

The source claims only what its header prints: a "cross-validate Forven backtest math against TradingView using a strategy with bit-for-bit deterministic indicators (no EMA-style warmup)" — classic turtle breakout, entry on close above the prior 20-bar high, exit on close below the prior 10-bar low. No behavioural, structural, or risk-premium channel is claimed. The header's math note equates `pandas df['high'].rolling(20).max().shift(1)` with `Pine ta.highest(high[1], 20)` as "bit-for-bit identical — no seeding / warmup ambiguity".

### Research interpretation

Falsifiable hypothesis: short-horizon 1h Donchian breakouts capture trend-continuation bursts — a close printing above the prior 20-hour range signals buying pressure strong enough to carry, while a close below the prior 10-hour low signals the burst has failed and the long is cut. The bet is on 1h-range expansion persistence, not on any oscillator level or calendar effect. This is a ported trend-breakout hypothesis; the source supplies no sample beyond its own 12-month window and its own table shows negative expectancy there (see Evidence), so the mechanism is research interpretation, not source-reported fact.

## Signal

All symbols below are the program's own identifiers; all values are program defaults, pinned.

Engine semantics (explicit in source): `process_orders_on_close = true`, `calc_on_every_tick = false`, `pyramiding = 0`. Completed-bar decision with same-bar-close execution; no intrabar evaluation.

Inputs (defaults):

```text
entry_len = 20 (Entry channel length, prior N-bar high; minval 2)
exit_len  = 10 (Exit channel length, prior N-bar low; minval 2)
use_window = true
start_ts = 1745078400000 (2025-04-19 16:00:00 UTC)
end_ts   = 1776614400000 (2026-04-19 16:00:00 UTC)
```

Channels (exact, causal — max/min over the N bars strictly before the current bar):

```text
prior_high = ta.highest(high[1], entry_len)   // == rolling(20).max().shift(1)
prior_low  = ta.lowest(low[1], exit_len)       // == rolling(10).min().shift(1)
in_window  = not use_window or (time >= start_ts and time <= end_ts)
break_up   = close > prior_high   // strict >
break_down = close < prior_low    // strict <
```

Trade events (the complete order-call set — one `strategy.entry`, one `strategy.close`, one window-end `strategy.close_all`; zero `strategy.exit` / `strategy.order` / `strategy.stop` / `strategy.cancel` calls):

```text
if in_window and break_up -> strategy.entry("Long", strategy.long)
if break_down             -> strategy.close("Long")
if use_window and (time > end_ts) -> strategy.close_all()
```

Direction: long-only. The program contains no short entry path, so the short side is absent by construction and recorded as explicitly disabled. Spot-compatible (no naked shorting required); source backtest leverage is 1x.

Exits and risk (explicit): signal exit is the breakdown close (`close < prior 10-bar low`); opposite-signal exit is not applicable (no opposite signal exists in a long-only rule); stop loss, take profit, trailing stop, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `strategy.close` on a flat position (e.g. a breakdown bar with no open entry) is a deterministic no-op. The exit leg is intentionally NOT gated by `in_window`, so a position opened inside the window is still cut by a later breakdown even outside it; the terminal `close_all` only forces flat after the window end so TradingView totals line up with the Forven run.

Position and re-entry (explicit): `pyramiding = 0` with a single entry id means same-side re-entry while positioned is rejected by the engine; after the breakdown exit the position is flat, so the next `break_up` bar is the only possible re-entry — fully specified, no cooldown, no missing rule. No `position_size`, `position_avg_price`, `openprofit`, or `opentrades` reference exists anywhere in the file, so no position-aware state conditions any signal or exit.

Conflict priority (provably irrelevant): `break_up` and `break_down` cannot fire on the same bar. `prior_high` is a max over 20 prior highs and `prior_low` a min over 10 prior lows; since every bar has `high >= low`, `prior_high >= prior_low` always, and strict `close > prior_high` and `close < prior_low` are mutually exclusive. No priority rule is needed and none is missing.

Determinism note for the reviewer: the rule uses no `crossover()` / `crossunder()` / `ta.cross` call — only strict scalar comparisons of the completed-bar close against the two channel levels — so the Gate-6 tie-semantics precedent does not arise. It uses no `ta.ema/rsi/rma` family at all — only `ta.highest` / `ta.lowest` over shifted (`[1]`) series, which carry no seeding ambiguity (the header states the pandas equivalence bit-for-bit). The file contains zero `request.*`, `security()`, `barstate.*`, `alert()`, `import`, Heikin-Ashi, `rightBars`, or stop/limit order arguments.

## Required data

- 1h bars of one pair: `open/high/low/close/volume` with the signal reading `high` (entry channel), `low` (exit channel), `close` (breakout test), and `time` (window gate only). No indicators beyond the two deterministic channel levels computed from those candles.
- No funding, OI, mark/index price, liquidation, trade/aggressor, L2/order-book, on-chain, options/Greeks, sentiment/news, macro, or cross-venue state is referenced or required.
- Warmup is derivable and exact: 20 bars (the max of the two lookbacks 20/10). Before 20 prior bars exist the channel is `na` and both comparisons are false, so the backtest holds flat — deterministic, no invention.

## Execution assumptions

- Source execution semantics: `process_orders_on_close = true` on 1h bars — the breakout is decided on the completed bar and filled at that same bar's close. Compatible with the pinned Hummingbot baseline lane; no conversion required.
- Research market (explicitly labeled house overlay, not source-native): `BTCUSDT`, `1h` decision timeframe. The source dataset is Binance `BTC/USDT-1h` and its own How-to-use instructs "Open BINANCE:BTCUSDT on the 1H chart" — i.e. the source itself identifies the BTCUSDT 1h chart as the applicable series (slash/no-slash is notation for the same Binance BTC/USDT chart family). No price-series substitution is performed: the record uses the same BTCUSDT 1h klines the source instructs. The downstream futures overlay (Isolated 3x/5x, pinned fees plus realized funding) is event-neutral accounting on this long-only spot-compatible rule — funding accrues only while a long is open (flat periods accrue nothing) and changes no signal, event, direction, or exit.
- Source sizing (`strategy.percent_of_equity`, 100) and the source commission model (0.055% per side, ~11 bps round trip) are event-neutral accounting: replaced downstream by the standard house execution overlay (Base 6% + Safety 6% + 6%, Isolated, 3x/5x, pinned Binance fees plus realized funding). The overlay changes no signal, event, or exit.
- Window inputs (`use_window = true` with the fixed Forven window) are backtest scope, not signal: they exist so TradingView totals line up with the Forven run. Both facts are pinned as read — the Donchian 20/10 rule itself is window-independent, while the as-coded defaults admit entries only inside 2025-04-19 16:00 UTC → 2026-04-19 16:00 UTC (exits remain live outside it) and force flat afterwards. Downstream must state which scoping it applies; it must not silently re-tune the window on final OOS data.

## Evidence

### Source-reported

Printed in the file header comment (traceable to the header table, not reproduced from anywhere else):

```text
In-sample (8.4m):      103 trades, win_rate 0.2621, return_pct -0.345, profit_factor 0.539, max_dd 0.369
Out-of-sample (3.6m):   35 trades, win_rate 0.4000, return_pct -0.026, profit_factor 0.947, max_dd 0.147
Combined (~12m):        138 trades, win_rate 0.2971, return_pct -0.362, profit_factor 0.650, max_dd 0.369 ~
```

Recorded exactly as printed, including the `~` approximation note: max DD is max(IS, OOS) rather than recomputed from the joined return stream — "true full-window drawdown may be slightly larger". The negative expectancy is recorded as read; HB_READY is expressibility, not profitability, so it is not a gate fail, but downstream must not present this rule as historically profitable on this window.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source's own table is negative evidence on this 12-month window (combined return -36.2%, profit factor 0.650): a Donchian 20/10 long-only breakout did not make money on BTC 1h in 2025-04 → 2026-04 net of ~11 bps round-trip costs. No other contradictory performance or failure report is cited in source. The absence of further evidence is recorded as absence, not as support.

## Falsification plan

Research tests only — none of these substitutes for a missing rule (no rule is missing):

1. Length swap: run entry 10 / exit 20 (inverted) and entry 20 / exit 20 (symmetric); a rule whose sign depends on the exact 20/10 pair rather than on range-expansion persistence is curve-fit, not signal.
2. Subperiod stability: split the 12-month window into halves; a sign flip or collapse concentrated in one half rejects robustness (the source's own IS/OOS split is the baseline to beat, not to re-tune on).
3. Cost sensitivity: re-run with round-trip costs doubled; a breakout edge that needs sub-11-bps costs to survive is execution fiction, not signal.
4. Engine parity: reproduce the 8760-bar window trade by trade (138 combined trades) and explain any count gap before trusting any port — the header asserts indicator math is bit-for-bit, so residual deltas must come from fee precision or open-bar equity, never from signal reinterpretation.
5. Always-flat-before-first-breakout accounting: verify the backtest holds flat until the first `close > prior 20-bar high` in scope; any deviation is an implementation bug, not a strategy property.

## Crypto portability

The rule ports cleanly to 24/7 crypto bars: no session calendar, no gap logic, no dividends/splits, no exchange-timezone call beyond the fixed UTC window constants already in source. Two port notes: (a) the pinned defaults admit entries only inside the hardcoded Forven window, so a downstream run on full BTCUSDT 1h history must explicitly declare its window scoping rather than inheriting a 2026-04-19 cutoff silently; (b) crypto 1h trends can sustain longer unbroken runs than the channel expects, which exercises the flat-between-breakdown-and-next-breakout path more often — expected behavior, not a bug.

## Limitations

1. No protective stop exists in source; tail risk on vertical adverse moves is borne fully by the breakdown exit. Recorded as explicitly disabled per source — must not be "repaired" with an invented stop.
2. The fixed backtest window is part of the pinned defaults. The Donchian rule itself is window-independent, but any downstream run must state its scoping; re-tuning the window or the 20/10 lengths on final OOS data is forbidden by the house overlay contract.
3. Source expectancy on the printed window is negative (see Evidence); this record establishes expressibility only and makes no profitability claim.
4. Confidence is `medium` (interpretation confidence): the rule text is complete and unambiguous with bit-for-bit channel math, but the source is a cross-validation demo clone offering only its own backtest table, no peer review, and no market-microstructure account of 1h breakout persistence.
5. Only program defaults are pinned. Input variants (different channel lengths or windows) are research tests, not separate strategies, and must not be cherry-picked.

## Implementation status

- `not-implemented`. No Hummingbot/Qlib/n8n/Paper/Testnet/Live work has been performed or is authorized by this record.

## Adoption boundary

- `research-only`, `not-approved`. Admission of this record would mean only that its core signal and causal trade-event semantics are losslessly expressible under the pinned backtester with the labeled house overlay — not profitability, survival, or any trading approval.

## Related Wiki records

- None. No Wiki Brain write was performed for this cycle.

## Sources

- Immutable program file at pinned commit (all rules): https://github.com/judder659/Forven/blob/98266984fa85391e58760eb6a1b5e45707504ecd/forven/docs/pine/simple_donchian_breakout_demo.pine
- Repository (project context, 358 stars as of 2026-10-06): https://github.com/judder659/Forven
