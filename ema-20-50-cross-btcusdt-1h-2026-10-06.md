---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven S01508 Simple EMA 20/50 cross system on BTCUSDT 1h bars
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
  - https://github.com/judder659/Forven/blob/98266984fa85391e58760eb6a1b5e45707504ecd/forven/docs/pine/simple_ema_cross_demo.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven S01508 Simple EMA 20/50 cross system on BTCUSDT 1h bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/judder659/Forven (open-source backtesting project with package, docs, frontend, and license files; 358 stars as read on 2026-10-06).
- Pinned commit SHA: `98266984fa85391e58760eb6a1b5e45707504ecd` (`ls-remote` HEAD check on 2026-10-06 confirms this is still the repository head, same pin as the S01509 Donchian and S01512 Monday Drift admissions).
- Exact file path: `forven/docs/pine/simple_ema_cross_demo.pine`.
- GitHub blob SHA at the pinned commit: `9fb269b213e565b9367d1c5969ef52f497c1dfa6`, size 4412 bytes.
- Byte-identity check: the file downloaded from `raw.githubusercontent.com` at the pinned commit is byte-identical (`cmp` clean on re-download) to the copy inspected; SHA-256 `fd23ce351101cabd32ba963343d90ae559b5c0d71db1801928c9ff2265ae7f49`, 4412 bytes, 95 lines.
- The file is a Pine v6 program (`//@version=6`) with a header comment block identifying it as "Simple EMA(20)/EMA(50) Cross — TradingView clone of Forven S01508", strategy_id `S01508 (simple_ema_cross_demo)`, dataset `BTC/USDT-1h (binance)`, window `2025-04-19 17:00 UTC → 2026-04-19 16:00 UTC (8760 bars)`, leverage `1x`, fee model `~11 bps round-trip (5.5 bps per side) inferred from trades`.
- The sibling demo `simple_donchian_breakout_demo.pine` (S01509, already admitted) is a different mechanism (Donchian channels with `ta.highest`/`ta.lowest`) and is not this candidate. The builtin Python family `forven/strategies/builtin/ema_cross.py` (S016/S018/S00011) adds an ADX >= 20 trend filter plus a 200-bar EMA regime filter that are absent from this Pine file — a different rule with extra gating, not this candidate. This record pins only the Pine demo file above.

Pre-write dedup (2026-10-06): case-insensitive search of the working tree for `s01508`, `simple_ema_cross`, `ema20/50`, `ema 20/50` returns no strategy record using this source or signal — the only hits are a mechanism-distinguishing note inside the Donchian S01509 record naming S01508 as explicitly different, not a record of it. `gh pr list --state open` shows only PR #33 on a `reconstruction/*` lane (Wasserstein portfolio family, different mechanism and different lane), so no open `research/*` PR shares this source or signal. Against the 12 PASS records on `main` (Bookstaber ATR breakout, DMI Swings ADX-45 exhaustion, Donchian 20/10 breakout, DRM dynamic RSI, EHMA range band, Flying Dragon offset-MA band, Gann HiLo, Ichimoku + ADX, Monday Drift calendar hold, P-Signal erf dead-band, Kaufman pivots, VIDYA + CMO): mechanism, signal construction, and source identity are all distinct — no plain two-EMA close-cross record exists in the pool.

## Economic mechanism

### Source-reported

The source claims only what its header prints: a "cross-validate Forven backtest math against TradingView" clone — classic two-moving-average trend following, long when the fast average is on top, flat when it falls back below. No behavioural, structural, or risk-premium channel is claimed. The header's math note equates `pandas close.ewm(span=L, adjust=False).mean()` with `Pine ta.ema(close, L)` as "mathematically identical: EMA_t = α·src + (1−α)·EMA_{t−1}, α = 2/(L+1), with EMA seeded from the first observation", adding only that a handful of trades of difference across the full year should be expected "strictly from warmup/boundary effects".

### Research interpretation

Falsifiable hypothesis: 1h EMA20/50 cross persistence captures medium-horizon trend drift — a fast average printing above the slow average signals buying pressure strong enough to carry for tens of hours, while the cross back below signals the drift has failed and the long is cut. The bet is on moving-average trend persistence at the ~1–2-day scale, not on any oscillator level, volatility band, or calendar effect. This is a ported trend-following hypothesis; the source supplies no sample beyond its own 12-month window and its own table shows sub-breakeven expectancy there (see Evidence), so the mechanism is research interpretation, not source-reported fact.

## Signal

All symbols below are the program's own identifiers; all values are program defaults, pinned.

Engine semantics (explicit in source): `process_orders_on_close = true`, `calc_on_every_tick = false`, `pyramiding = 0`. Completed-bar decision with same-bar-close execution; no intrabar evaluation.

Inputs (defaults):

```text
ema_fast_len = 20 (EMA fast length; minval 2)
ema_slow_len = 50 (EMA slow length; minval 3)
use_window = true
start_ts = 1745082000000 (2025-04-19 17:00:00 UTC)
end_ts   = 1776614400000 (2026-04-19 16:00:00 UTC)
```

Indicators (exact, causal — close-only exponential averages, α = 2/(L+1), seeded from the first observation per the header math note):

```text
ema_fast = ta.ema(close, ema_fast_len)   // α = 2/21
ema_slow = ta.ema(close, ema_slow_len)   // α = 2/51
in_window  = not use_window or (time >= start_ts and time <= end_ts)
cross_up   = ta.crossover(ema_fast, ema_slow)    // prev_fast <= prev_slow and curr_fast > curr_slow
cross_down = ta.crossunder(ema_fast, ema_slow)   // prev_fast >= prev_slow and curr_fast < curr_slow
```

Trade events (the complete order-call set — one `strategy.entry`, one `strategy.close`, one window-end `strategy.close_all`; zero `strategy.exit` / `strategy.order` / `strategy.stop` / `strategy.cancel` calls):

```text
if in_window and cross_up -> strategy.entry("Long", strategy.long)
if cross_down             -> strategy.close("Long")
if use_window and (time > end_ts) -> strategy.close_all()
```

Direction: long-only. The program contains no `strategy.short` path anywhere (verified by full-file search), so the short side is absent by construction and recorded as explicitly disabled. Spot-compatible (no naked shorting required); source backtest leverage is 1x.

Exits and risk (explicit): signal exit is the cross back down (`ta.crossunder`); opposite-signal exit is not applicable (no opposite signal exists in a long-only rule); stop loss, take profit, trailing stop, and time limit are absent in source and recorded as explicitly disabled, not as defaults to be assumed. `strategy.close` on a flat position (e.g. a cross-down bar with no open entry) is a deterministic no-op. The exit leg is intentionally NOT gated by `in_window`, so a position opened inside the window is still cut by a later cross-down even outside it; the terminal `close_all` only forces flat after the window end so TradingView totals line up with the Forven run.

Position and re-entry (explicit): `pyramiding = 0` with a single entry id means same-side re-entry while positioned is rejected by the engine; after the cross-down exit the position is flat, so the next `cross_up` bar is the only possible re-entry — fully specified, no cooldown, no missing rule. No `position_size`, `position_avg_price`, `openprofit`, or `opentrades` reference exists anywhere in the file, so no position-aware state conditions any signal or exit.

Conflict priority (provably irrelevant): `cross_up` and `cross_down` cannot fire on the same bar. `ta.crossover` requires previous fast <= previous slow with current fast strictly above current slow; `ta.crossunder` requires the exact reverse. Both jointly true would require current fast strictly above AND strictly below current slow — impossible; when the two averages print exactly equal, both are false. No priority rule is needed and none is missing.

Determinism note for the reviewer: the rule uses only `ta.ema` over `close` plus `ta.crossover` / `ta.crossunder` strict-cross semantics — no `request.*`, `security()`, `barstate.*`, `alert()`, `import`, Heikin-Ashi, `timeframe*`, `rightBars`, volume-weighted logic, or stop/limit order arguments anywhere in the file (verified by full-file search returning zero matches). The file's only `time` read is the window gate.

## Required data

- 1h bars of one pair: `open/high/low/close/volume` with the signal reading `close` (both EMAs) and `time` (window gate only). No indicator beyond the two deterministic EMAs computed from those candles.
- No funding, OI, mark/index price, liquidation, trade/aggressor, L2/order-book, on-chain, options/Greeks, sentiment/news, macro, or cross-venue state is referenced or required.
- Warmup is derivable and exact: 50 bars (the max of the two lookbacks 50/20). Both EMAs are defined from the first observation per the header seeding note, so early-bar crosses are deterministic rather than `na`-gated; 50 bars marks the slow-EMA steady state, and the header itself attributes only a handful of full-year trade deltas to warmup/boundary effects — deterministic, no invention.

## Execution assumptions

- Source execution semantics: `process_orders_on_close = true` on 1h bars — the cross is decided on the completed bar and filled at that same bar's close. Compatible with the pinned Hummingbot baseline lane; no conversion required.
- Research market (explicitly labeled house overlay, not source-native): `BTCUSDT`, `1h` decision timeframe. The source dataset is Binance `BTC/USDT-1h` and its own How-to-use instructs "Open BINANCE:BTCUSDT on the 1H chart" — i.e. the source itself identifies the BTCUSDT 1h chart as the applicable series (slash/no-slash is notation for the same Binance BTC/USDT chart family). No price-series substitution is performed: the record uses the same BTCUSDT 1h klines the source instructs. The downstream futures overlay (Isolated 3x/5x, pinned fees plus realized funding) is event-neutral accounting on this long-only spot-compatible rule — funding accrues only while a long is open (flat periods accrue nothing) and changes no signal, event, direction, or exit.
- Source sizing (`strategy.percent_of_equity`, 100) and the source commission model (0.055% per side, ~11 bps round trip, slippage 0) are event-neutral accounting: replaced downstream by the standard house execution overlay (Base 6% + Safety 6% + 6%, Isolated, 3x/5x, pinned Binance fees plus realized funding). The overlay changes no signal, event, or exit.
- Window inputs (`use_window = true` with the fixed Forven window) are backtest scope, not signal: they exist so TradingView totals line up with the Forven run. Both facts are pinned as read — the EMA 20/50 cross rule itself is window-independent, while the as-coded defaults admit entries only inside 2025-04-19 17:00 UTC → 2026-04-19 16:00 UTC (exits remain live outside it) and force flat afterwards. Downstream must state which scoping it applies; it must not silently re-tune the window on final OOS data.

## Evidence

### Source-reported

Printed in the file header comment (traceable to the header table, not reproduced from anywhere else):

```text
In-sample (8.4m):      59 trades, win_rate 0.237,  return_pct -0.188, profit_factor 0.686, max_dd 0.268
Out-of-sample (3.6m):  21 trades, win_rate 0.333,  return_pct +0.012, profit_factor 1.087, max_dd 0.139
Combined (~1y):        80 trades, win_rate —,      return_pct —,      profit_factor 0.793, max_dd —
```

Recorded exactly as printed, including the `—` blanks: the header prints no combined win rate, return, or drawdown — only 80 combined trades (59 + 21) and profit factor 0.793. The figures are leverage-1x, long-only, single-side, net of the ~11 bps round-trip model. HB_READY is expressibility, not profitability, so the sub-breakeven combined expectancy is not a gate fail, but downstream must not present this rule as historically profitable on this window.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The source's own table is negative evidence on this 12-month window (combined profit factor 0.793; in-sample return -18.8%): a plain EMA 20/50 long-only cross did not make money on BTC 1h in 2025-04 → 2026-04 net of ~11 bps round-trip costs, with only the small 21-trade OOS slice marginally positive (+1.2%, profit factor 1.087). No other contradictory performance or failure report is cited in source. The absence of further evidence is recorded as absence, not as support.

## Falsification plan

Research tests only — none of these substitutes for a missing rule (no rule is missing):

1. Length swap: run entry 50 / exit 20 (inverted) and entry 20 / exit 20 (symmetric); a rule whose sign depends on the exact 20/50 pair rather than on trend-drift persistence is curve-fit, not signal.
2. Subperiod stability: split the 12-month window into halves; a sign flip or collapse concentrated in one half rejects robustness (the source's own IS/OOS split is the baseline to beat, not to re-tune on).
3. Cost sensitivity: re-run with round-trip costs doubled; a cross edge that needs sub-11-bps costs to survive is execution fiction, not signal.
4. Engine parity: reproduce the 8760-bar window trade by trade (80 combined trades) and explain any count gap before trusting any port — the header asserts EMA math is identical across engines, so residual deltas must come from warmup seeding, fee precision, or flat-equity accounting, never from signal reinterpretation.
5. Always-flat-before-first-cross accounting: verify the backtest holds flat until the first `ta.crossover` in scope; any deviation is an implementation bug, not a strategy property.

## Crypto portability

The rule ports cleanly to 24/7 crypto bars: no session calendar, no gap logic, no dividends/splits, no exchange-timezone call beyond the fixed UTC window constants already in source. Two port notes: (a) the pinned defaults admit entries only inside the hardcoded Forven window, so a downstream run on full BTCUSDT 1h history must explicitly declare its window scoping rather than inheriting a 2026-04-19 cutoff silently; (b) crypto 1h trends can whipsaw the 20/50 pair through repeated crosses in range-bound regimes, which exercises the exit-then-immediate-re-entry path often — expected behavior, not a bug.

## Limitations

1. No protective stop exists in source; tail risk on vertical adverse moves is borne fully by the cross-down exit. Recorded as explicitly disabled per source — must not be "repaired" with an invented stop.
2. The fixed backtest window is part of the pinned defaults. The EMA cross rule itself is window-independent, but any downstream run must state its scoping; re-tuning the window or the 20/50 lengths on final OOS data is forbidden by the house overlay contract.
3. Source expectancy on the printed window is sub-breakeven (see Evidence); this record establishes expressibility only and makes no profitability claim.
4. Confidence is `medium` (interpretation confidence): the rule text is complete and unambiguous with header-certified EMA equivalence, but the source is a cross-validation demo clone offering only its own backtest table, no peer review, and no market-microstructure account of 1h trend persistence.
5. Only program defaults are pinned. Input variants (different EMA lengths or windows) are research tests, not separate strategies, and must not be cherry-picked.

## Implementation status

- `not-implemented`. No Hummingbot/Qlib/n8n/Paper/Testnet/Live work has been performed or is authorized by this record.

## Adoption boundary

- `research-only`, `not-approved`. Admission of this record would mean only that its core signal and causal trade-event semantics are losslessly expressible under the pinned backtester with the labeled house overlay — not profitability, survival, or any trading approval.

## Related Wiki records

- None. No Wiki Brain write was performed for this cycle.

## Sources

- Immutable program file at pinned commit (all rules): https://github.com/judder659/Forven/blob/98266984fa85391e58760eb6a1b5e45707504ecd/forven/docs/pine/simple_ema_cross_demo.pine
- Repository (project context, 358 stars as of 2026-10-06): https://github.com/judder659/Forven
