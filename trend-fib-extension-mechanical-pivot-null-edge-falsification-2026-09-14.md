---
schema: strategy-research-record-v1
title: "Trend-Based Fibonacci Extension with Mechanical Pivot Anchors: Sample-Widening Null-Edge Falsification"
created: 2026-09-14
updated: 2026-09-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-13
sources:
  - "https://github.com/karthikcyadav98/fib-extension-paper (commit 22d583fb5edad062c9fa18dbe77a398527f13d57, README.md; fibx/strategy.py; fibx/universe.py)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Trend-Based Fibonacci Extension with Mechanical Pivot Anchors: Sample-Widening Null-Edge Falsification

## Provenance

- **Source:** Public GitHub repository `karthikcyadav98/fib-extension-paper`
- **Repository URL:** https://github.com/karthikcyadav98/fib-extension-paper
- **Full commit SHA (snapshot read for this record):** `22d583fb5edad062c9fa18dbe77a398527f13d57`
- **Author-commit establishing forex-only null-edge findings:** `47c61502596e873624fcf86ba6213e6742c100c7` (message documents -0.07R / PF 0.88 over 355 trades and rejection of session-of-day effect)
- **Primary paths read:** `README.md`, `fibx/strategy.py`, `fibx/universe.py`
- **Author:** karthikcyadav98
- **Source as-of:** repository tip including live paper bot commits through 2026-09-13
- **Source type:** Public open-source mechanised implementation with historical backtest, 72-cell robustness sweep, out-of-sample variant harness, and a $1,000 live paper account

## Economic mechanism

### Source-reported

The discretionary "trend-based Fibonacci extension" thesis claims that after a confirmed impulse (swing low → swing high) and a valid pullback that holds above the impulse origin, price often continues to mechanical extension targets at 1.272× and 1.618× the impulse leg, measured from the pullback trough. The author's implementation replaces discretionary swing selection with fixed fractal pivot rules so the same chart always produces the same trade. The author reports that the **Fibonacci constants themselves are not the edge**: a flat-2R null model using identical entries and stops was beaten in 51/72 cells by fib scale-out, but the author attributes that to the *scale-out-and-trail exit structure*, not to the numbers 1.272/1.618. Headline source conclusion: **no edge**. Across a 72-configuration sweep (1,281 trades) only 1 cell was profitable; median cell −0.12R/trade; best cell +0.002R (breakeven to three decimals). Widening the sample repeatedly destroyed any apparent edge in the same direction.

### Research interpretation

The reconstructable hypothesis under test is: *trend + confirmed pullback + Fibonacci extension targets generate positive expectancy after realistic one-way all-in costs*. The source itself treats this as a **null-edge process** once sample size and parameter breadth are honest. Material incremental value of this capture is therefore **negative evidence / falsification methodology**: mechanical pivot selection (removes discretionary cherry-picking), explicit cost structure, parameter-surface robustness, and a documented *sample-widening* collapse pattern that is a useful falsification template for other technical family captures. This is **research-proposed** framing of the record's value as a negative-evidence template; the author's null-edge conclusion is source-reported.

## Signal

- **Formation timestamp / availability:** Signal is evaluated on each completed bar close. Pivots are usable only from their `confirm_idx` (after `pivot_right` bars of confirmation), so no signal can be built from a bar that had not printed. Live paper path uses Deriv REST updates approximately every 15 minutes (GitHub Actions); dashboard prices stream ~1s from browser WebSocket. Historical path: Yahoo 1h resampled to 4h by absolute time (not bar counting) so weekend fusion is avoided.
- **Lookback:** EMA50 / EMA200 trend filter; ATR(14) stop pad; fractal pivots with `pivot_left=5`, `pivot_right=5` (defaults).
- **Long entry (mirrored for shorts):**
  1. Trend filter: `close > EMA50 > EMA200`.
  2. Anchor triple: P1 confirmed swing low → P2 confirmed swing high after P1 → P3 confirmed swing low after P2 with `P3 > P1` (higher-low pullback; break of P1 voids the leg).
  3. Leg: `leg = P2 − P1`.
  4. Retracement: `(P2 − P3) / leg` must lie in `[0.236, 0.786]`.
  5. Trigger: first close through prior bar's extreme (`close > prior high` for long) within `entry_window=10` bars of P3 confirmation.
  6. Quality gate: reward:risk to T1 must be `≥ 2.0`; stop distance must be `≥ 0.5 × ATR(14)`.
- **Exits:**
  - T1 = `P3 + 1.272 × leg` — exit half (default scale-out).
  - T2 = `P3 + 1.618 × leg` — exit remainder.
  - Stop = `P3 − 1.5 × ATR(14)`; move to breakeven after T1 fill (README); bar containing both stop and target scored as **stop** (conservative fill rule).
  - Time exit: `max_bars_in_trade = 60`.
- **Holding period:** Path-dependent; exits at first of stop / T1+T2 / 60 bars. No overlapping positions on the same `(side, P3)` anchor (one trade per pullback).
- **Parameters (source DEFAULTS, explicitly optimistic by selection):** `pivot_left=5`, `pivot_right=5`, `ema_fast=50`, `ema_slow=200`, `atr_period=14`, `stop_atr_mult=1.5`, `retrace_min=0.236`, `retrace_max=0.786`, `ext_t1=1.272`, `ext_t2=1.618`, `entry_window=10`, `min_rr=2.0`, `allow_short=true`, `min_risk_atr=0.5`, `max_bars_in_trade=60`. Source states these are the **best cell of a 72-config sweep** chosen after seeing results; live results should be treated as an **upper bound**, not an expectation.
- **Position sizing (paper path):** 1% equity risk per trade; max 8 concurrent positions; 35% notional cap per position; per-currency net exposure cap `MAX_CCY_EXPOSURE=3`. Sizing rule is source-reported for the paper account, not an alpha claim.

## Required data

- **Instrument:** Live primary: 16 forex pairs on 4h bars (7 majors + 9 crosses). Historical comparison universe includes crypto (`BTCUSDT`, `ETHUSDT`) and India daily (`^NSEI`, `RELIANCE.NS`) as **reference only**, not live-traded.
- **Venue / data source:** Historical: Yahoo Finance 1h FX (`{pair}=X`) resampled to 4h, range `730d`. Live: Deriv REST for paper fills/state; browser Deriv WebSocket for dashboard prices. Crypto reference: Binance symbols in `universe.REFERENCE`.
- **Timeframe:** 4h bars (live and headline backtest); source notes 1h FX was cost-dominated (−0.048R / 405 trades) so 4h was chosen as a cost-structure fix, still breakeven (+0.006R on 4 pairs).
- **Fields:** OHLC bars; computed EMA50/EMA200, ATR(14), fractal pivots.
- **Point-in-time:** Pivot confirmation lag of `pivot_right=5` bars is enforced via `confirm_idx`. Yahoo feed is static historical; Deriv live feed is ~258 days deep (declared trade-off in `universe.py`).
- **Timestamp:** Yahoo/Deriv timestamps as published; resample buckets by absolute time to avoid fusing Friday–Sunday bars.
- **Missing-data:** Not exhaustively specified. Source documents Yahoo 429/UA, CA-bundle, and weekend-resample issues as handled; no formal imputation policy.
- **Funding/fee/spread:** `cost_bps` is **one-way and all-in** (spread + commission + slippage) charged on every fill. Majors ~0.5–1.2 bps; JPY/AUD crosses up to 2.2 bps. Crypto reference cost 5.5 bps. No crypto funding-rate model in this implementation (spot-style cost model on the crypto reference symbols).

## Execution assumptions

- **Signal-to-order timing:** Intent at bar close; fill simulation and paper broker execute per bar path. Live Actions cadence ~15 min (workflow historically also 4x/hour in earlier author commit notes).
- **Order type / fill model (source-reported conservative rules):** Bar containing both stop and target scores **stop**. Gap fills at **open**, not the level. Internal paper fills only; real broker execution not used (OANDA/FXCM refused author's residency; Deriv API sells contracts rather than spot FX with stop/target).
- **Fees/slippage:** Embedded in per-instrument `cost_bps` (see above). Source explicitly recounts an early ~6bps round-trip over-charge that made forex look worse than it was.
- **Leverage / margin:** Paper account $1,000 start with 1% risk sizing and exposure caps; no live leverage claim.
- **Capacity:** Not assessed. 4h FX majors typically have ample capacity for retail-sized risk; no institutional capacity claim is made.
- **Latency:** Not latency-sensitive at 4h; live paper is not a low-latency system.

## Evidence

### Source-reported

- **Headline live-config result (forex 16 pairs, 4h):** −0.07R per trade, 33.8% win rate, PF 0.88 (README).
- **72-cell parameter sweep (1,281 trades):** 1/72 cells profitable; median cell 29.3% WR, −0.12R; best cell +0.002R (breakeven). Strategy is not one bad parameter choice away from working.
- **Fib vs flat-2R null:** Fib scale-out beat identical-entry/stop flat-2R null in 51/72 cells; author attributes this to scale-out/exit structure, **not** Fibonacci constants.
- **Sample-widening collapse (author's key falsification pattern):**
  | Sample | Trades | Avg R |
  |---|---:|---:|
  | crypto, 4 pairs | 152 | **+0.18** |
  | crypto, 10 pairs | 384 | **+0.01** |
  | forex 4h, 4 pairs | 97 | **+0.006** |
  | forex 4h, 16 pairs | 355 | **−0.07** |
- **Out-of-sample variant harness (`research.py`, 12 hypothesis-driven variants, 70/30 time split):** none cleared 2 standard errors OOS. Train winner +0.559R collapsed to +0.180 ± 0.393 on 21 test trades. Best-looking filter reduced to "don't trade 1h forex" (cost structure). Asia session effect +0.147R decayed +0.264R → +0.029R on split-half.
- **Live paper:** $1,000 start, 1% risk, max 8 positions, currency exposure cap; fills simulated; live config is best-cell of sweep (optimistic by construction).

### Independently reproduced

`not independently reproduced`.

### Negative evidence

This entire record **is** the negative evidence capture: parameter-surface near-uniform non-profitability, sample-widening destruction of apparent edge, OOS variant collapse, cost dominance at 1h, and explicit author conclusion of no edge. Related repository captures of technical/fib-family retail ideas without this level of mechanical + cost + OOS discipline should be treated as weaker until similarly falsified. No third-party independent replication study of this specific repo was identified in the sources reviewed for this run.

## Falsification plan

Operational tests already executed or directly implied by the source (research-defined thresholds marked):

1. **Parameter surface:** 72-config sweep; if median cell remains ≤0R and max cell ≈0R, family fails a **research-defined falsification threshold** of requiring median cell > 0R after all-in costs.
2. **Sample widening:** Add instruments/markets sequentially; if avg R trends toward 0 or negative as N grows (crypto 4→10; forex 4→16), treat small-sample positive R as false positive (**research-defined falsification threshold**).
3. **OOS / walk-forward:** 70/30 time split on 12 variants; require effect > 2 SE OOS; none passed.
4. **Cost stress:** Compare 1h vs 4h; if edge is created/destroyed by `cost_bps` alone, classify as cost artifact not alpha.
5. **Placebo / structure ablation:** Flat-2R null vs fib targets on identical entries; if fib constants add nothing beyond scale-out structure, Fibonacci labeling is not causal.
6. **Session/regime placebo:** Split-half on session-of-day filter; decay indicates noise.
7. **Further crypto portability test (not run by source):** Re-run mechanical rules on liquid crypto perpetuals with funding-aware costs and queue/latency stress; pre-declare failure if net edge ≤ 0 after maker/taker + funding. **research-defined falsification threshold**.

## Crypto portability

- **Status:** **unproven / source-tested and null on small samples**.
- **Source-reported crypto path:** Reference universe includes BTCUSDT/ETHUSDT 4h with 5.5 bps one-way cost. Early crypto 4-pair sample showed +0.18R (152 trades); expanding to 10 pairs collapsed to +0.01R (384 trades) — same sample-widening failure as FX.
- **Adaptation gaps if retested on crypto perpetuals:**
  - Funding rate not modeled (spot-style costs only).
  - No maker/taker queue model; no liquidation/OI filters.
  - 24/7 calendar removes FX session structure; pivot confirmation and ATR scale would need re-estimation.
  - Stablecoin/quote fragmentation and venue risk not addressed.
- **Interpretation:** Direct port is **not** authorized by this capture. The only crypto-specific increment is **negative portability evidence**: apparent early crypto edge vanished when the crypto sample was widened. Portability remains a research question, not a tradeable claim.

## Limitations

- Single-author public repo; not peer-reviewed; zero stars/watchers at as-of date.
- Historical FX depends on Yahoo 1h→4h resample; live Deriv history is short (~258 days); live vs historical data sources intentionally differ.
- DEFAULTS are post-selection best cell — optimistic bias acknowledged by author.
- Crypto reference is small and cost-model simplified (no funding).
- No institutional capacity, market-impact, or latency analysis.
- Discretionary Fibonacci trading literature is broad; this capture is only the **mechanical** subset and should not be generalized to all discretionary fib usage.
- Independent reproduction has not been performed for this Scout run.

## Implementation status

`not-implemented` in our systems. The source repository implements Python stdlib backtest, robustness sweep, paper broker, and GitHub Actions live paper loop. This research capture does not modify NautilusTrader, PyBroker, or any quantitative runtime, and does not create implementation/backtest/Paper/Testnet/Live tasks.

## Adoption boundary

`research-only` / `not-implemented` / `not-approved` / `approval_scope: research-only`. Presence of this record means only that a reconstructable technical hypothesis and its **negative** evidence were normalized for intake review. It is not strategy adoption, implementation authorization, or permission to run Paper/Testnet/Live. The source's own conclusion is that the strategy has no edge.

## Related Wiki records

Repository-local conceptual neighbors (not exhaustive Wiki Brain links):

- `retail-signal-three-gate-falsification-oscillator-volume-calendar-trend-2026-09-04.md` — retail indicator stacking falsification
- `crypto-smc-fvg-bpr-liquidity-retracement-random-walk-falsification-2026-09-12.md` — retail structure/retracement falsification
- `mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05.md` — cost/ceiling falsification pattern
- `crypto-walk-forward-window-optimization-double-oos-momentum-2026-09-04.md` — walk-forward / OOS discipline

No pre-existing record in this repository implements mechanical P1/P2/P3 Fibonacci extension anchors with this sample-widening null-edge design; this capture is not a paraphrase of those neighbors.

## Sources

- https://github.com/karthikcyadav98/fib-extension-paper
- https://github.com/karthikcyadav98/fib-extension-paper/blob/22d583fb5edad062c9fa18dbe77a398527f13d57/README.md
- https://github.com/karthikcyadav98/fib-extension-paper/blob/22d583fb5edad062c9fa18dbe77a398527f13d57/fibx/strategy.py
- https://github.com/karthikcyadav98/fib-extension-paper/blob/22d583fb5edad062c9fa18dbe77a398527f13d57/fibx/universe.py
- https://github.com/karthikcyadav98/fib-extension-paper/commit/47c61502596e873624fcf86ba6213e6742c100c7
