---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven ORB trailing-4-bar channel breakout lag-1 derived long-flat on BTCUSDT 1h
created: 2026-10-21
updated: 2026-10-21
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: high
source_as_of: 2026-10-21
sources:
  - https://github.com/judder659/Forven/blob/0a8b07fd02ac6864c0102fec08b6ae7ebfa32875/forven/strategies/builtin/orb.py
  - https://github.com/judder659/Forven/blob/0a8b07fd02ac6864c0102fec08b6ae7ebfa32875/forven/strategies/base.py
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven ORB trailing-4-bar channel breakout lag-1 derived long-flat on BTCUSDT 1h

This record is an **explicitly derived executable strategy** (adaptations D1–D10 below, all researcher-declared).
It is NOT presented as lossless reproduction of the Forven native deployment. The source-native rule is kept
separate in Provenance; the derived rule actually reviewed for the six gates is the lag-1, spot-1h,
PositionExecutor-pinned specification in Signal / Execution assumptions.

## Provenance

- Primary source (immutable): `judder659/Forven @ 0a8b07fd02ac6864c0102fec08b6ae7ebfa32875`
  (commit date 2026-10-21 −0300, message "Retire the Universe books page and its paper books (#240)";
  commit object re-fetched read-only this run; Forven HEAD has since moved, the pin is unaffected).
- Strategy file: `forven/strategies/builtin/orb.py` — 1914 bytes / 51 lines, Git blob `73e8cb8c`,
  SHA-256 `b1008f6bbf8306c882e3a78169633c8863071c8d800dd99e606ee5cc7aa7e2a1`
  (raw download byte-identical to `git show` of the pinned commit, verified with `cmp` this run).
- Framework file: `forven/strategies/base.py` — 12238 bytes / 361 lines, Git blob `27508a2a`,
  SHA-256 `75ada9d2ac362058ccf5971ae6086684ca129bf358682bf3afb8be1727833a1d` (same verification).
- Registry identity: `TYPE_NAME = "orb"` (orb.py L5); `STRATEGIES = [("TOMB-ORB", ORBStrategy, {"_asset": "BTC"})]`
  (orb.py L51). Effective params by base.py L259 merge (`{**default_params, **(params or {})}`):
  `range_bars = 4` (orb.py L16; the registry entry overrides nothing else).
- Source-native rule (verbatim construction, code governs):
  `entry_t = close_t > rolling_high_4.shift(1)_t`, `exit_t = close_t < rolling_low_4.shift(1)_t`
  (orb.py L24–L31), `direction = "long"` constant (orb.py L44), twin scalar/vector paths agree
  (orb.py L22–L46; the scalar `orb_high` indicator reads `rolling(n).max().iloc[-2]`, the same shifted value).
  No stop-loss / take-profit / trailing / time-exit anywhere in the 51 lines. No volume, open, session,
  calendar, funding, or multi-asset read anywhere in either signal path (AST column fence, see Evidence).
- Source-family defaults reused verbatim (not invented): `data_requirements` default declares
  `timeframe: 1h, min_bars: 720` (base.py L317–L331) — this record's 1h frame and 720-bar warmup floor
  are source-side declarations, not researcher choices.
- Deliberately inert source metadata (read, disclosed, never repaired into the rule): `describe()` prose
  "first N bars of the session" (orb.py L21) vs the trailing-rolling code — **code governs**, there is no
  session anchor or calendar in the effective rule; `parameter_space range_bars (2, 10, 2)` (orb.py L47–L48)
  is an unused search grid (defaults rule this record); `compatible_regimes {"VOLATILE", "TREND_UP"}`
  (orb.py L18–L19) is unread in the signal path; `leverage 3.0` (orb.py L16) is unread in the signal path;
  `confidence` / `price` / `indicators` outputs carry no rule.
- No source-reported performance exists in the file (no sample, window, trade count, or cost basis);
  this record claims none.

## Economic mechanism

### Source-reported

A 4-bar trailing Donchian-style channel breakout: buy when price closes above the highest high of the prior
4 bars (long-only breakout momentum); exit when price closes below the lowest low of the prior 4 bars
(symmetric channel stop-and-reverse-to-flat). The file states no economic thesis beyond `describe()`.

### Research interpretation

Short-horizon time-series momentum with a symmetric trailing-channel exit: the 4-bar window makes it the
fastest pure-channel breakout in this family — entries chase immediate closes beyond recent range, exits cut
the full unit as soon as price breaks the trailing floor. No mean-reversion, carry, funding, or volatility
premium claim is made. The lag-1 execution adaptation (D2) delays every event by exactly one 1h bar versus
the native rule; the economics above are otherwise unchanged.

## Signal

All symbols are 1h bars indexed by `i` (row timestamp `T_i` = bar open time; bar close time `C_i`).
`H_i / L_i / C_i` = high / low / close of bar `i`. Window `N = 4` (pinned source default).

- Source-native bar signals (reference only, not traded directly):
  `src_entry_t = C_t > max(H_{t-4..t-1})`, `src_exit_t = C_t < min(L_{t-4..t-1})`, False for `t < 4`
  (`rolling(4)` NaN + `fillna(False)`, orb.py L27–L31).
- Traded decision rule (derived, lag-1 — the reviewed rule):
  at decision row `i`, `ENTRY_DECISION_i = src_entry_{i-1}`, `EXIT_DECISION_i = src_exit_{i-1}`.
  The controller reads **only bars ≤ i−1** for the decision taken at row `i` (enforced by construction:
  every comparison references the once-removed series; no same-row OHLC enters any decision).
- Direction: long-only. `src_entry` opens a long unit; `src_exit` closes it in full. No short leg exists
  anywhere; shorts are explicitly disabled, not defaulted.
- Mutual exclusion (arithmetic proof, not sampling): `max(H window) ≥ min(L window)` always (same window,
  `H ≥ L` per bar), so `C > max(H)` and `C < min(L)` can never co-print on one bar; entry and exit never
  fire on the same decision row and no intrabar fill-order assumption is needed. Grid-confirmed (Evidence).
- Risk legs: none by source design — no SL / TP / trailing / time exit. All four are **explicitly disabled**
  (`TripleBarrierConfig` all-None, D3), never silently defaulted. A position without a later exit signal is
  held to sample end (disclosed, see Limitations).
- Leading behavior: bars 0–3 flat by `fillna(False)`; first valid source signal index 4; first derived
  decision row index 5 (construction minimum 6 bars; the 720-bar source floor dominates — see Required data).
- Gate-1 determinism note: formula, variant (trailing rolling max/min, not session-anchored), lookback (4),
  shift (source shift-1 plus derived lag-1), thresholds (strict `>` / `<`, exact touch fires neither side),
  state transitions (flat→long on entry decision; long→flat on exit decision), and priority (mutual exclusion
  makes priority moot) are all explicit above. Nothing is fitted: the only parameter is the pinned default.

## Required data

- Single frame, single venue: Binance BTCUSDT spot 1h klines (`BTC-USDT` in Hummingbot notation).
  Columns read by the rule: `high`, `low`, `close` only. `open` is loaded by the feed but unread by the rule;
  `volume` / quote-volume / trade-count / taker-volume fields are loaded by the feed but unread by the rule
  (honest feed-vs-rule split; no volume dependence is claimed and none exists).
- Point-in-time availability identity (the Gate-6 basis, all clauses verifiable):
  feed stamps `timestamp = row[0]` = bar **open** time (pinned feed L80–L85); Binance kline spec defines
  `row[0]` = open time and `row[6]` = close time, so bar `b` is complete at `C_b = row[6]_b + 1ms and, on
  contiguous tape, `C_{i-1} = T_i − 1ms`. Decision row `i` reads only bars `≤ i−1`, hence every input bar is
  complete no later than the decision stamp `T_i`. Gapped history only ages the inputs (all still complete
  before `T_i`) and can never leak the future — see Limitations for the contiguity note.
- Warmup: **720 bars** (720 1h bars ≈ 30 days), taken verbatim from the
  source-family `data_requirements` default (base.py L331). Construction minimum is 6 bars
  (first decision row index 5); the 720-bar floor dominates. No warmup value is invented.
- No repainting: trailing rolling extrema over completed bars only; no negative shift; no full-sample
  statistic; no higher-timeframe or intrabar input of any kind.

## Execution assumptions

Pinned engine (immutable, re-read read-only this run):
`HCH725/hummingbot @ 8b0e067e80ab62f10846d518dcb5a8218527ddb3`
(commit date 2026-09-20 +0800, "Merge pull request #8459" — the same date as the `20260920` package baseline;
`hummingbot/VERSION` at this commit reads `dev-2.17.0`, blob `fa1dd206`).
File pins (Git blobs at that commit): `backtesting_engine_base.py 7d1e552d`,
`position_executor_simulator.py 5539f0d2`, `order_executor_simulator.py 3b4e82e9`,
`binance_spot_candles.py 5d0c938a`, `position_executor/data_types.py 32bf8313`.

- D1 market/venue (researcher choice, disclosed): Binance **spot** (`connector_name = "binance"`, which the
  pinned `CandlesFactory` maps to `BinanceSpotCandles`, factory L63–L64; spot utils pin
  `connector: str = "binance"`). Spot ⇒ **no funding term exists anywhere in the specified path**; nothing
  is zeroed, no perpetual/funding/margin concept is invoked. HB pair spelling `BTC-USDT`
  (feed strips `-` for the REST symbol, feed L64–L65).
- D2 fills (derived causality-preserving mapping, disclosed): decision at row `i` (stamp `T_i`, inputs
  bars `≤ i−1`, all available per Required data) → market fill at **row-`i` close `C_i`** (`C_i > T_i`,
  strictly after the decision). Mechanically this is exactly what the pinned simulator does for a market
  entry (`start_timestamp = df min`, `entry_price = first-row close`, position sim L11–L15/L40). No
  restamping is claimed (row stamp stays `T_i`); no "availability = row time" is asserted; the fill is a
  forward event from the decision, and the one-bar delay versus the native rule is the declared cost of
  causality (see Limitations). Same-bar-close is therefore NOT claimed — the traded event is
  next-bar-relative by construction.
- D3 executor (the reviewed config, every field pinned):
  `PositionExecutorConfig(type="position_executor", trading_pair="BTC-USDT", connector_name="binance",
  side=BUY, entry_price=None→decision-row close per sim L40, amount=1000/C_i base units,
  triple_barrier_config={stop_loss=None, take_profit=None, time_limit=None, trailing_stop=None,
  open_order_type=MARKET}, leverage=1, controller_id="main", timestamp=T_i)`.
  All-None barriers are valid (`require_positive` skips `None`, validation.py) and mean explicitly disabled,
  matching the source's absence of risk legs. `open_order_type=MARKET` is pinned (default is LIMIT,
  data_types L37). Fixed **1000-quote notional** sizing adds zero information beyond the engine's own fill
  price (`1000/C_i`). `leverage=1` (config minimum, data_types L84/L97); the source's unread `3.0` is dropped
  with the short/margin apparatus, disclosed here. No DCA / safety orders / house overlay of any kind enter
  this record (the downstream campaign overlay is out of scope by explicit exclusion, not by omission).
- D4 exits: exit decision at row `j` → `StopExecutorAction(executor_id, keep_position=False)` →
  `CloseType.EARLY_STOP`, booking the simulator's fee-aware `net_pnl_quote` into engine realized PnL
  (engine L593–L595). No TP/SL/trailing/time path can fire (all None). No `POSITION_HOLD` is ever created
  on this path (contrast: `OrderExecutor` MARKET always routes POSITION_HOLD, order sim L64–L71 — cited as
  the path deliberately NOT used, because its hold ledger books gross PnL with fees aside).
- D5 fee-aware accounting (in-engine, the former blocker closed by path selection):
  `net_pnl_pct = close-to-close return − 2 × trade_cost` (position sim L45–L46),
  `cum_fees_quote = 2 × trade_cost × filled` (L49); terminated non-hold executors book `net_pnl_quote`
  into `_executor_realized_pnl` (engine L428–L430) and `summarize_results.net_pnl_quote = executor_pnl +
  position_realized_pnl` (engine L612–L624), where the position terms are identically zero on this record's
  path (no holds). Closed-trade PnL is retained in the stopped-executor ledger + accumulator (never dropped).
  The read point for research economics is `summarize_results` (`net_pnl_quote`, `total_fees_quote`),
  NOT the `pnl_timeseries.total_pnl` (which by engine L380 only sums open holds — disclosed, moot here).
- D6 cost model (explicit, fixed): `trade_cost = 0.001` per side = Binance spot Regular taker **0.1000%**
  (Binance fee schedule: Regular `<1M USD / ≥0 BNB → 0.100%/0.100%`; support FAQ: "standard fee of 0.1%
  for regular users"; market fills take liquidity ⇒ taker side). Round trip is provisioned as `2 × 0.001`
  inside the engine (D5). No maker/limit, no BNB-discount, no VIP tier, no slippage add-on is assumed.
- D7 controller/data wiring: a `DirectionalTradingControllerBase`-derived researcher controller;
  `backtesting_resolution = "1h"` = signal frame (run signature default is `1m`, engine L224 — this record
  pins `1h`); strategy candles `CandlesConfig(connector="binance", trading_pair="BTC-USDT", interval="1h")`
  (`"1h" ∈ INTERVALS`, spot constants); the controller supplies **no extra features**, so
  `prepare_market_data` takes the no-features defaults branch (engine L461–L464) — no `merge_asof`, no
  cross-timeframe alignment to prove. Decisions ride the row loop (`update_state` then
  `determine_executor_actions`, engine L282–L291); provider price/time are `close_bt` / row timestamp
  (engine L366–L367).
- D8 position state (Gate 4, complete): at most one live `PositionExecutor` per market; a new entry is
  created only with zero active executor simulations (no holds can exist — `keep_position` is always False);
  re-entry needs only the next entry-decision row; cooldown explicitly none (source specifies none, none is
  added); simultaneous exposure, pyramiding, averaging-down, and safety orders are all explicitly absent.
- D9 SL/TP basis ambiguity (the former basis blocker) does not arise: there are no SL/TP legs; the only
  economics are close-to-close fills minus the fixed round-trip provision, both with exact code lines (D5).
- D10 what is NOT claimed: no profitability, no Qlib parity, no Paper/Testnet/Live permission, no
  source-native equivalence for the adapted timing, no sibling-precedent-as-evidence (every capability above
  cites pinned code lines, never another record).

## Evidence

### Source-reported

The 51-line file ships the complete construction (defaults, twin signal paths, registry entry). It ships no
sample, window, trade count, or cost basis — this record claims no source-reported performance and no
reproduced performance.

### Independently reproduced

Not independently reproduced (no engine run; Scout PR-only workflow). The following read-only logic-shape
checks were executed locally (pure pandas 3.0.6, seed 7, 80-bar synthetic grid, script kept outside the repo):
entries 6 / exits 14 with **zero same-bar co-prints**; bars 0–3 flat; `decision(i) = signal(i−1)` exact;
AST fence that the signal paths read `high/low/close` only (no `volume`/`open`/`leverage`/`parameter_space`/
regime read). These check rule shape only and are not performance evidence.

### Negative evidence

1. Code-governs-session fence: `describe()` "session" prose is aspirational; the traded rule is a trailing
   4-bar channel with no session anchor, no midnight/UTC-day concept, no calendar read — nothing session-like
   is repaired in or assumed.
2. Dead-parameter fence: `leverage 3.0`, `parameter_space`, `compatible_regimes`, `confidence/price/indicators`
   outputs are read and inert; none enters any gate.
3. Strictness fence: strict `>`/`<` — an exact-touch bar fires neither side (coded fact, preserved).
4. Lookback-minimum fence: `rolling(4)` + `shift(1)` + `fillna(False)` ⇒ bars 0–3 flat, first signal index 4,
   first derived decision row index 5; the 720-bar floor dominates regardless.
5. Mutual-exclusion fence: arithmetic proof in Signal (not sample-dependent); grid assert confirms zero
   co-prints, so no fill-ordering assumption exists to dispute.
6. Cousin fence (each a different construction/source/pin — changing any lookback, exit, side, or source
   file yields an unpinned rule): pool `holmberg-orb-normal-tail-breakout-two-sided` (different source,
   session-range + normal-tail statistics, two-sided); `donchian-20-10-breakout-btcusdt-1h`,
   `eterna-donchian-20-1-midline-two-sided`, `forven-donchian-regime-breakout-long-flat`,
   `forven-breakout-range-20bar` (20/10/1-bar lookbacks and midline/floor exits vs this record's symmetric
   4/4 channel); `forven-atr-breakout-channel`, `forven-linreg-channel-breakout`, `forven-keltner-*`,
   `eterna-keltner-*`, `bll-trb/vma-*-percent-band` (band/σ/regression channels, different mechanisms);
   all `alorse-bb-*`, `bollinger-band-breakout-*`, `chartart-bollinger-rsi-*` (Bollinger σ-bands, different
   mechanism). No pool or open-PR record trades a close-vs-trailing-4-bar-high/low symmetric channel,
   long-flat, pinned to Forven `builtin/orb.py @ 0a8b07f`. Open research PRs #48/#49/#63/#89/#92/#251/#304/
   #331/#350/#353 were each checked by slug/signal — none is a 4-bar channel breakout.
7. Sibling-file fence: every other `forven/strategies/builtin/*.py` pin is a separate file with its own
   constants and legs; none may be substituted into this record.
8. Derivation-boundary fence: the ONLY non-source-native behaviors are D1 (BTCUSDT spot 1h venue pin), D2
   (lag-1 causality mapping + row-close fills), D3/D8 (PositionExecutor config, fixed 1000-quote notional,
   single-unit/no-cooldown state), D5–D6 (engine-provisioned 0.001/side costs), D7 (no-features wiring),
   D9 (720-bar floor from the family default). The 4-bar channel, strict thresholds, mutual exclusion,
   long-only stance, and absences of SL/TP/trailing/time/volume/session are source-verbatim effective
   behavior. Closed-not-merged PRs (#360 SuperTrend, #361 RSI S012) are different files/legs and are not
   re-submitted here in any form.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: N=4 /
strict `>`/`<` / shift-1 + lag-1 / long-only / signal-only exits / all-None barriers / single-unit /
1000-quote notional / `1h` BTCUSDT spot / decision-row-close fills / `trade_cost=0.001` are frozen.

- F1 — Entry-timing relevance: entering on the first flat bar after warmup (same signal exits, same costs)
  must not improve net expectancy; fail ⇒ the 4-bar breakout edge adds nothing over exposure timing.
- F2 — Exit-timing relevance: removing the signal exit (hold every entry to sample end, same costs) must not
  improve net expectancy; fail ⇒ the trailing-floor exit adds nothing over buy-and-hold.
- F3 — Mapping-cost relevance: executing with a two-bar lag (decision(i) = signal(i−2), same fills/costs)
  must not improve net expectancy; fail ⇒ the one-bar causality mapping is not the binding cost driver.
  (Fixed comparison, not a tuning proposal; the record stays lag-1 regardless.)

## Crypto portability

BTCUSDT Binance spot `1h` is the research pin (source names `_asset BTC`; frame from the family default).
Long-only full-unit open/close expresses unchanged on any spot venue with no naked shorting. No session,
calendar, equity-hours, volume, funding, or multi-asset concept is read anywhere — every window is a
trailing bar count on the decision frame, portable across 24/7 crypto tape. Funding is absent by venue
choice (spot), not by assumption. Precision/minimums ride the connector trading-rules load (engine
`initialize_trading_rules`); the 1000-quote notional is orders above venue minimums by construction and no
record-level lot assumption is made.

## Limitations

- The lag-1 mapping costs exactly one 1h bar of delay versus the native rule on every event; in fast vertical
  tape this systematically worsens entries and delays exits (declared derivation cost, not a defect to repair).
- No SL/TP/trailing/time exit by source design: adverse excursions run until the opposite channel signal
  (or sample end); gap-through-floor events exit at the next decision-row close, never intrabar.
- `time_limit=None` pins "hold to sample end" for exit-less positions (explicit, faithful to the source's
  lack of a time stop — not a hidden default).
- Availability identity assumes standard contiguous klines (`C_{i-1} = T_i − 1ms`); on gapped history inputs
  are merely older — still complete before `T_i`, so causality holds but signal freshness degrades. Runs on
  non-contiguous history are out of this record's scope unless downstream validation establishes contiguity.
- Fixed 1000-quote notional, no compounding, no pyramiding: economics do not scale with equity; results are
  not leverage- or portfolio-conditioned.
- Spot-only: no short, no funding, no margin; the record says nothing about perpetual behavior.
- `total_amount_quote` (summarize denominator) is a reporting scale, not a capital claim; `net_pnl` ratios
  inherit it.
- Engine evidence is read-only code inspection of the pinned commit (no run performed in this workflow);
  line citations are given so the independent reviewer can re-verify each claim.

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract,
`not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if
formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED`
(add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream
research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- https://github.com/judder659/Forven/blob/0a8b07fd02ac6864c0102fec08b6ae7ebfa32875/forven/strategies/builtin/orb.py
- https://github.com/judder659/Forven/blob/0a8b07fd02ac6864c0102fec08b6ae7ebfa32875/forven/strategies/base.py
- https://github.com/judder659/Forven (pinned commit `0a8b07f`)
- https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/backtesting_engine_base.py
- https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/strategy_v2/backtesting/executors_simulator/position_executor_simulator.py
- https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/data_feed/candles_feed/binance_spot_candles/binance_spot_candles.py
- https://developers.binance.com/docs/binance-spot-api-docs/rest-api/market-data-endpoints (Kline rows: open time / close time field positions)
- https://www.binance.com/en/fee/trading and https://www.binance.com/en/support/faq/fee-structure-on-binance-115000429332 (spot Regular 0.1000% taker basis for `trade_cost=0.001`)
