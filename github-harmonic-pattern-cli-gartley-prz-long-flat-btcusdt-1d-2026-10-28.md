---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Gartley 618/786 PRZ reversal long-flat BTCUSDT 1d (harmonic-pattern-cli independent derivative)"
created: 2026-10-28
updated: 2026-10-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-28
sources:
  - https://github.com/mattpartida/harmonic-pattern-cli
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Gartley 618/786 PRZ reversal — independent research derivative

## Provenance and frozen identity

**Primary GitHub source:** Matt Partida, *harmonic-pattern-cli*, MIT License, public repository read 2026-10-28: https://github.com/mattpartida/harmonic-pattern-cli . Immutable commit `03b1cba75c07a65bf2168e72f62ed6d686deb9e4` (single-commit repository, committed 2026-06-14): exact files `src/harmonic_pattern_cli/pivots.py` (41 lines), `patterns.py` (50 lines), `scanner.py` (122 lines), `models.py`, `cli.py` (`--tolerance` default `0.05`, `--left`/`--right` defaults `2`), `io.py`, `render.py`, plus `tests/test_harmonic_pattern_cli.py` (7 tests) and two Gartley CSV fixtures. No other revision, fork state, or upstream identity is claimed.

**Source-native facts, verified by direct read and local execution:** fractal swing pivots with `left=2`/`right=2` (strict high/low inequality, equal highs/lows ignored, consecutive same-kind pivots collapsed to the more extreme); consecutive five-pivot XABCD windows with strict low-high-low-high-low alternation for bullish direction; GARTLEY ratio gates `xab=(0.618,0.618)`, `abc=(0.382,0.886)`, `bcd=(1.272,1.618)`, `xad=(0.786,0.786)` with tolerance band `low*(1-tol) <= v <= high*(1+tol)`; ratios `xab=|A-B|/|A-X|`, `abc=|C-B|/|A-B|`, `bcd=|C-D|/|C-B|`, `xad=|A-D|/|A-X|`; bullish signal `entry_zone=D±max(|D|*0.01,0.01)`, `stop_loss=X-max(|A-X|*0.05,0.01)`, `targets=[D+0.382*|C-D|, D+0.618*|C-D|]`, invalidation on break below X; match ranking by `(score, risk_reward)` descending. The 7-test suite was executed locally on 2026-10-28 in the pinned file layout and passed 7/7; the sample `sample_gartley.csv` scan reproduced one bullish Gartley (X=100.0, A=120.0, B=108.0, C=115.0, D=104.3; ratios xab=0.6, abc=0.5833, bcd=1.5286, xad=0.785; stop 99.0; targets 108.3874/110.9126; score 0.9924). These runs verify the source logic executes deterministically; they are not a crypto backtest and no profitability is inherited.

**Explicit independent derivative, NOT source-native/lossless:** trade only the bullish Gartley on Binance BTC-USDT **spot 1d**, and deliberately (1) **disable** the source `_with_endpoint_candidates` pseudo-pivots (unconfirmed last-bar extremes) so every pivot is a confirmed fractal, (2) replace the source D±1% zone touch with a completed-close confirmation entry two bars after D, (3) replace curve-fitted zone/stop touches with fully specified completed-close stop at the source stop level and full exit at the source first target (second target intentionally unused, no partials), (4) use fixed **0.001 BTC** per trade and 10,000 USDT initial unborrowed cash, (5) replace any cost assumption with **hypothetical 0.1% per filled side** and no simulated impact, (6) ignore bearish patterns (spot has no short leg), and (7) define warmup, retirement latch, priority and fail-closed behavior below. These changes materially alter trade events and economics; no fixture parity or profitability is claimed.

**Immutable derivative identity:** `GH:mattpartida/harmonic-pattern-cli@03b1cba:gartley-only-bullish | independent-derived-v1:tol0.05:left2:right2:endpoint-disabled | close-confirm-entry:D+2:stopX-5pctXA:TP1-38.2pctCD | BinanceSpot:BTC-USDT:UTC1d:LONG-FLAT:Q0.001BTC | Hummingbot-MARKET-close:cost0.001-per-side | warmup100`. Any altered ratio gate, tolerance, pivot parameter, market, event order, price convention or cost constitutes a different derivative.

## Economic mechanism

### Source-reported

The source asserts no expectancy mechanism; it is a geometric scanner. Its only economics are per-pattern outputs: an entry zone around D, a stop beyond X, two retracement targets of C–D, and a target-2 risk/reward number.

### Research interpretation

Falsifiable hypothesis only: completion of a textbook-approximate bullish Gartley (61.8% XA retracement at B, 78.6% XA completion at D) may mark a short-term exhaustion/reversal zone whose first 38.2% C–D retracement is reached before the X-level stop more often than chance net of costs. No evidence of positive expectancy is asserted.

## Signal — fully defined derived rules

- Input: exactly one Binance BTC-USDT **spot 1d UTC** OHLCV series. Candle `t` is labeled by **open** timestamp `T[t]`, closes and becomes available at `T[t]+86400` seconds. Use only **completed** candles. Require consecutive daily timestamps, finite OHLCV, `high>=max(open,close)>=min(open,close)>=low>0`, `volume>=0`. Any missing, duplicate, non-daily, NaN, nonpositive price or otherwise invalid bar **aborts the research run**; do not interpolate, forward-fill or invent a trade price.
- **Confirmed pivots:** replicate source `find_pivots` arithmetically in exact decimal: bar `i` is a swing high iff `high[i]` strictly exceeds the highs of bars `i-2..i+2` except itself; a swing low iff `low[i]` is strictly below the lows of the same window; equal extremes never qualify; consecutive same-kind pivots collapse to the more extreme (higher high / lower low), keeping the earliest index on exact ties. A pivot at index `i` is **confirmed** only on bars `t >= i+2`. The source endpoint pseudo-pivot augmentation is **disabled**; the last two completed bars can never contribute a pivot.
- **Windows and ratios:** at each completed bar `t`, take all confirmed pivots with index `<= t-2`, in index order with the source collapse applied, and evaluate every consecutive five-pivot window. Direction must be exactly low-high-low-high-low (bullish); anything else is discarded. Ratios use the source formulas `xab=|A-B|/|A-X|`, `abc=|C-B|/|A-B|`, `bcd=|C-D|/|C-B|`, `xad=|A-D|/|A-X|`; a zero denominator voids that window. A bullish **Gartley completion** holds iff all four ratios sit inside `low*(1-0.05) <= v <= high*(1+0.05)` against `xab=(0.618,0.618)`, `abc=(0.382,0.886)`, `bcd=(1.272,1.618)`, `xad=(0.786,0.786)`. Score is the mean of the four source `closeness` values; `risk_reward=(target2-D)/(D-stop)` with the source `_build_signal` bullish formulas. Bat/Butterfly/Crab specs in the source file are explicitly **not traded**.
- **Completion event and priority:** a completion is actionable at the first bar `t` with `D+2 <= t` whose window matches and whose tuple id (five pivot indices plus `gartley`) was never traded. If several unretired completions are actionable at `t`, enter on exactly one, ordered by score desc, then risk_reward desc, then D index asc, then X index asc.
- **Warmup:** consume at least **100 consecutive completed 1d bars** before the first signal; no entry during warmup. Start FLAT with an empty retirement set. No historical pre-warmup signal is carried forward.
- **Entry:** when FLAT and an actionable completion exists at `t`, issue exactly one BUY for **0.001 BTC** at the completed bar's **close** under the pinned historical MARKET-close simulation. Confirm fill; set LONG, `entry_tuple`, `stop_level=X-max(0.05*|A-X|,0.01)`, `tp1_level=D+0.382*|C-D|` (with `|C-D|>0` guaranteed by distinct alternating pivots; a zero `|C-D|` aborts the run); retire the tuple id permanently. The entry bar is **not** evaluated for stop or target exit.
- **LONG stop:** on each subsequent completed candle, **first** test `close[t]<=stop_level`. If true, SELL all 0.001 BTC at that completed close and return FLAT. This is a **close-triggered loss signal**, NOT an exchange protective stop or a guarantee of bounded loss; gaps can exceed the modeled distance.
- **LONG target:** only if stop did not fire: if `close[t]>=tp1_level`, SELL all 0.001 BTC at that completed close and return FLAT. The source second target is intentionally unused; no partial exits, no trailing, no time exit.
- **State/priority:** stop precedes target, exit precedes any entry consideration. Ignore all completions while LONG. After a full exit, no same-bar re-entry; future entry requires a different unretired tuple. One spot long or flat only; no short, pyramiding, averaging, DCA/safety orders, partial fills, timed cooldown, forced final liquidation, independent intrabar high/low touch, exchange stop/limit order, maker/limit, leverage, margin, funding, cross-asset state or portfolio shared-capital allocation. No terminal trade is fabricated if LONG at the last bar; mark the open position at the last close for reporting. Retirement keys on exact pivot indices: a later same-kind tail collapse that replaces a pivot creates a new tuple id, which is disclosed here and may trigger a later separate entry.
- On any missing/failed MARKET fill, insufficient **modeled** cash, nonfinite fee/price, or position-book mismatch outside the tolerance below, **abort the run** rather than inventing an order, cash balance, or missing price. No optimization or parameter search is performed in this record.

## Required data

Binance BTC-USDT spot daily OHLCV only (open-time labeled, completed bars). No volume signal, no second market, no higher/lower-frame feed, no fundamental or off-chain input. Warmup is 100 completed daily bars; pivot confirmation adds an intrinsic two-bar lag after each swing extreme.

## Execution assumptions — demonstrated pinned-engine path and bounded model

**Pinned benchmark:** Hummingbot package `20260920`, `hummingbot/VERSION=dev-2.17.0`, GitHub repository `HCH725/hummingbot` at immutable commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`. The following real code paths were read via GitHub raw files on 2026-10-28; this is **static capability evidence**, not a strategy backtest:

1. **Data/clock:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` (993 bytes) declares `1d` (alongside `5m`/`15m`/`1h`); `binance_spot_candles.py` maps Binance `/api/v3/klines` open-time `row[0]` and OHLCV `row[1..5]`. `backtesting_engine_base.py` exposes processed candle columns (`open_bt`/`close_bt`) and a `close_bt` reference price. Fractal pivots and close-only levels need no hidden feed or unsupported multi-frame synchronization.
2. **Controller/executor:** `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` iterates `update_state(row)`, `controller.determine_executor_actions()`, `CreateExecutorAction`, then `simulate_executor`. A **strategy-specific, not-yet-implemented controller** can hold the explicitly defined pivot list, retirement set and stop/target levels, issuing `OrderExecutorConfig(connector_name="binance", trading_pair="BTC-USDT", side=BUY/SELL, amount=Decimal("0.001"), execution_strategy=MARKET, leverage=1)`. This is a research expressibility argument, **not** a claim that an executable controller already exists.
3. **Fill and causal clock:** `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` chooses the **first supplied candle** for MARKET (`fill_timestamp` is that candle's timestamp label), fills at its `close` (`entry_price`), records `filled_amount_quote=float(amount)*close`, charges `trade_cost*filled_amount_quote`, and returns `CloseType.POSITION_HOLD`. All derivative decisions/fills are explicitly reported at **open timestamp + 86400 seconds**, never represented as available at candle open. Same-close fills are a **historical zero-latency modeling convention**, not an achievable post-close exchange guarantee; there is no next-open, maker, high/low touch or external stop primitive hidden in this derivative.
4. **Spot position and research costs:** Initial modeled cash **10,000 USDT**, position either **0** or **0.001 BTC**. A BUY at price `p` reduces exact Decimal research cash by `0.001*p*(1+0.001)`; a SELL increases it by `0.001*p*(1-0.001)`. The fixed **0.1% per-side fee is a hypothetical research input**, not a source or verified Binance fee. `trade_cost=0.001` is passed to the simulator. Realized net quote PnL = sell proceeds minus buy cost; open equity = cash + 0.001*last_close. Spot funding is **not applicable**, not a fabricated realized zero-funding stream. No margin or liquidation.
5. **Float/Decimal caveat and fail-closed bound:** `OrderExecutorSimulator` uses float for filled quote (`amount_quote=float(config.amount)*entry_price`), while `BacktestPositionHold.add_executor` converts filled quote back to base quantity by division and `is_closed` tests exact `net_amount_base == 0`. Consequently a tiny engine residual is possible even after equal 0.001 BTC BUY/SELL. The derived controller must use its **explicit confirmed-order 0/0.001 BTC state**, never infer re-entry eligibility solely from the engine's exact-zero `positions_held` flag. On each fill reconcile engine net base with exact research inventory, and engine gross PnL/fees with Decimal ledger, allowing at most **1e-10 BTC base residual** and **1e-6 USDT quote rounding discrepancy**; larger deviations, negative modeled cash or an unaccounted fill **abort**, not silently reclassify exposure. These are **research diagnostic bounds**, not claims of exchange lot precision or a fix to the engine.
6. **Capability boundary:** This path models completed 1d OHLCV, one spot pair, historical MARKET-close fills and quote-fee accounting only. It does **not** verify exchange tick/lot/min-notional rules, real order acceptance, market liquidity, actual commission tiers, slippage, partial fills or live stop/limit execution. Simulator modeled price impact/slippage is absent; that is **not** evidence that actual slippage is zero. The source entry-zone touch semantics are deliberately **not** carried over. If any of these unmodeled capabilities becomes materially required, Gate 5 must be reassessed before research expansion.

## Six-gate admission evidence (subject to independent Hermes Auditor)

1. **Determinism:** exact fractal pivot equations, collapse rule, ratio formulas, Gartley gates, 0.05 tolerance band, score/priority order, stop/target formulas, 100-bar warmup, retirement latch, missing-data fail-closed and all parameters frozen.
2. **Direction:** Binance BTC-USDT spot LONG/FLAT; bearish patterns explicitly ignored; short, leverage and margin disabled.
3. **Entry/exit/risk:** confirmation-close entry, completed-close stop at source stop level, full exit at source first target, stop-first priority, no undeclared protective/exit orders; trailing, partials and time exits intentionally disabled.
4. **State:** exact 0.001 BTC, one position, no DCA, no stacking, permanent tuple retirement, no same-bar re-entry, no fixed cooldown, final open position unliquidated.
5. **Pinned compatibility:** verified `1d` Binance spot feed, actual controller/action/MARKET/POSITION_HOLD path, candle-open timestamp normalization, research fees, Decimal ledger plus engine reconciliation and fail-closed precision diagnostics; endpoint pseudo-pivots disabled so no unconfirmed extreme is ever used; no unsupported intrabar fill primitive assumed.
6. **Causality:** confirmed pivots only (D usable no earlier than two bars after its extreme), decision timestamp at daily close, no future reads, repainting, full-sample fit, incomplete higher-timeframe bar or synthetic price; same-close simulator assumption explicitly bounded as historical research only.

## Evidence

### Source-reported

Author provides two Gartley CSV fixtures and 7 unit tests covering bullish/bearish detection, tolerance gating, pivot finding, JSON/markdown rendering, CLI behavior and missing-file handling. No market performance, backtest statistics, or live-trading evidence is reported by the source.

### Independently reproduced

On 2026-10-28 the pinned source tree was fetched at `03b1cba` into an isolated scratch layout; `python -m unittest discover -s tests` passed **7/7 in 0.130s**, and the CLI scan of `sample_gartley.csv` (`--tolerance 0.06`) reproduced exactly one bullish Gartley with the ratios, stop 99.0, targets and score quoted above. This reproduces source determinism only. Otherwise: not independently reproduced; no backtest was run.

### Negative evidence

No backtest, no crypto data run, no fee/liquidity validation and no live evidence exist for this derivative. The confirmation-close entry can fill far from D after fast moves; the 5%-of-XA stop buffer is small relative to daily BTC volatility; gap risk beyond the stop level is real. PASS here is the researcher's **six-gate submission claim**, not independent approval, implementation, Qlib parity, Survivor, profitability or Paper/Testnet/Live authorization.

## Falsification plan

A frozen-data replay of this exact derivative (100-bar warmup, 0.001 BTC, 0.1%/side, fail-closed) is falsified as an interesting candidate if, over the full available Binance BTC-USDT spot 1d history, its net realized quote PnL is negative after modeled costs, or if fewer than five round trips ever trigger (signal too rare to evaluate), or if stop-gap slippage beyond the modeled close fill dominates exits. Any parameter change defines a new derivative, not a repair of this one.

## Crypto portability

Designed directly for BTC-USDT spot daily: 24/7 UTC-day candles remove session-definition problems that equity-harmonic trading has; no corporate-action adjustment is needed. Thin-history or newly listed pairs may never form five confirmed pivots and will simply never signal, which is correct fail-silent behavior short of data errors (which abort).

## Limitations

- Single-pattern (bullish Gartley only), single-pair, single-timeframe study; bearish setups and Bat/Butterfly/Crab detections present in the source file are ignored by design.
- Pivot formation needs sustained swing history; long trends with fewer than five confirmed pivots produce no signal.
- Same-kind tail collapse can replace a pivot after a pattern was traded, creating a new tuple id and a possible second entry on a near-identical structure; retirement does not span such replacements.
- Decimal re-implementation of float ratio arithmetic can differ at exact tolerance boundaries; boundary-touching windows are measure-zero in practice but the pin is disclosed.
- All engine, fee, liquidity and Fractional-precision caveats from Execution assumptions apply.

## Implementation status

`not-implemented`: no controller, configuration, backtest artifact, Qlib recipe or deployment exists for this derivative. A future `IMPLEMENTATION_NEEDED` route may materialize the minimal strategy-specific controller plus frozen replay recipe without redoing HB_READY.

## Adoption boundary

`research-only`, `not-approved`. Nothing in this record authorizes Paper, Testnet, live trading, scheduling, or capital allocation. Downstream screening requires its own representative event-level parity check for any new execution primitive before mass use.

## Related Wiki records

None. No Wiki Brain write is requested by this Scout run.

## Dedup, negative evidence, and downstream boundary

- GitHub main snapshot `430e70b`: **393** root-level strategy Markdown records (395 Markdown files including the two READMEs); README pool count still shows the pre-reconciliation value and is left for the post-merge webhook bookkeeping, not edited here. No filename or file content in current main matches `gartley`, `harmonic`, `carney`, `xabcd`, or this source URL; current open `research/*` PRs show no harmonic candidate. The two NR7/orb records and all RSI/stochastic/ichimoku-dip records use different signal constructions (range-narrowness or oscillator thresholds, no XABCD Fibonacci gates).
- A representative Qlib/Hummingbot event-level parity check is required **before mass screening of any new/unverified execution primitive**, not as an invented seventh admission gate. Independent Hermes Auditor must verify source facts and all six gates at the exact PR head before any merge. No trading, backtest, deployment or scheduling change is requested.
