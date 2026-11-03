---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: TradingView noise-area breakout VWAP-checkpoint session-flat two-sided on BTCUSDT 5m
created: 2026-11-03
updated: 2026-11-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-11-03
sources:
  - https://www.tradingview.com/script/jiwqijwC-INTRADAY-MOMENTUM-DIGGA-Noise-Area-Breakout/
  - https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4824172
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TradingView noise-area breakout VWAP-checkpoint session-flat two-sided on BTCUSDT 5m

## Provenance

Primary source identity verified end to end (page fetched live and read 2026-11-03; full Pine source read line by line, 386 lines):

- TradingView OPEN-SOURCE SCRIPT `$$$ INTRADAY MOMENTUM DIGGA $$$ v1.0 - Noise Area Breakout` by publisher `PINEDIGGA`, stable URL `https://www.tradingview.com/script/jiwqijwC-INTRADAY-MOMENTUM-DIGGA-Noise-Area-Breakout/` (script ID `jiwqijwC`). Page header confirms `OPEN-SOURCE SCRIPT`; code header reads `MPL-2.0 / © PINEDIGGA`. No invite-only, paywall, or login wall on the logic.
- Pinned declaration (source lines 438–441): `strategy("$$$ INTRADAY MOMENTUM DIGGA $$$ v1.0 - Noise Area Breakout", ..., initial_capital=100000, default_qty_type=strategy.fixed, default_qty_value=1, commission_type=strategy.commission.cash_per_contract, commission_value=0, slippage=3, process_orders_on_close=false, pyramiding=0, max_bars_back=500, margin_long=0, margin_short=0)`. No `process_orders_on_close` override anywhere else (Pine default = next-bar-open market fills); no `strategy.exit` / `strategy.order` anywhere (order census on the fetched source: 2 `strategy.entry`, 4 `strategy.close_all`, 0 `strategy.exit`, 0 `strategy.order`); no `request.*` / `security(` (census 0).
- Pinned inputs (defaults frozen, source lines 450–462): `qtyIn=1.0`, `dirIn="Both"`, `sessIn="0930-1600"`, `TZ="America/New_York"`, `LOOK=14`, `bandMult=1.0`, `CHK=30` (options 15/30/60), `useVwap=true`, `useGap=true`, `skipHol=true`, `tmMode="Filter + 5m exit"` with an explicit `"Off"` option. All remaining inputs are display-only visuals/alerts/table.
- Idea lineage (source lines 398–401 and page text): independent clean-room build of Zarattini, Aziz & Barbon (2024), "Beat the Market: An Effective Intraday Momentum Strategy" (SSRN abstract 4824172; Swiss Finance Institute RP 24-97; SPY intraday momentum 2007–early 2024). The paper is lineage context only — no paper number, return, or Sharpe is adopted anywhere in this record.
- Licence and rights: this record cites and normalizes the rule (short phrases and definitional recurrence only) and reproduces no extended prose, figures, or performance numbers.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the source's noise-band-plus-VWAP checkpoint construction ported to BTCUSDT 5m with fixed sizing and close-evaluated fills — not a lossless reproduction of the author's NQ-futures chart setup. Researcher-declared adaptations are exactly six: (1) single-asset BTCUSDT Binance USDT-M perpetual venue (the author ships no venue pin in code; `dirIn="Both"` default means the short permission is genuinely used); (2) fixed 0.01 BTC 1× isolated sizing replacing the author's 1-contract fixed sizing; (3) `tmMode="Off"` — a source-provided option, and the author's own stated original rule ("To use the original rule, set Trend Magic 15m to Off"; the default forward-test layer self-declares it failed its pre-registered test); (4) `skipHol=false` — a source-provided option whose tooltip says "Turn off for non-US markets" (crypto has no US exchange holidays; the Mon–Fri session grid is retained); (5) completed-bar-close decision with same-bar-close market fills (declared conversion of the author's next-bar-open fills — the established close-evaluated conversion class already used by admitted pool records); (6) structural 6,000-completed-5m-bar warmup (the author ships none — first fully defined signal needs 14 filed sessions). The session grid, lookback, band/VWAP construction, strict-inequality gates, state priority, checkpoint cadence, session-close filing rule, and no-bracket stance are source-faithful. This record is therefore never evidence that the author's script passes.

Pre-write dedup (2026-11-03): working-tree base is current `main@9888932e` (535 root strategy records). Case-insensitive content searches for `jiwqijwC`, `pinedigga`, `momentum digga`, `zarattini`, `noise area`, `noise band` return zero same-source hits (the only `beat the market` hit is FMZ-438783's unrelated Sunil-Halai volatility-percentile rule, disclosed). `trend magic` returns zero strategy records. The five broad-pattern hits are different mechanisms: `worldquant-alpha101-intraday-momentum` (daily single-bar close-location sign book, no bands/VWAP/checkpoints/session), `imi-50-midline-cross` (everget Intraday Momentum Index oscillator cross, no session grid), `bll-vma-percent-band` (daily VMA drift band), `fmz-430902` (relative-momentum-index latch). All 16 open `research/*` PRs enumerated by number/title/branch — none is this script, publisher, paper, or construction. Five-axis distinction: no pool record and no open PR conditions exposure on a 14-session same-clock-time noise band with gap-anchored max/min levels gated by session VWAP at 12 half-hour checkpoints with forced 16:00 ET flat.

## Economic mechanism

### Source-reported

Most of the session is noise for that time of day; an abnormal move away from the open — beyond the average same-clock-time excursion of the last 14 sessions, gap-adjusted, and confirmed against the session VWAP — indicates a demand/supply imbalance worth following until the close, with the checkpoint band itself as the trailing exit and nothing held overnight. (Author's expectation framing fenced: ~40% win rate, profit from a handful of trend days a year, clusters of quick stopped trades are the cost of the rule, re-entries pay net of cost — mechanism color only, never adopted as a crypto claim.)

### Research interpretation

Time-of-day-normalized breakout, two-sided, 5-minute cadence, session-flat. Unlike single-lookback volatility-breakout records the threshold is a same-clock-time seasonal: each of the 12 checkpoints carries its own 14-session mean excursion, so the funnel starts narrow at 09:30 and widens through the day. Unlike oscillator-cross records there is no cross event anywhere — the state is a checkpoint latch (`want ∈ {1, −1, 0}`) recomputed only at half-hour marks, and VWAP is both a second entry gate and the trailing exit level. Unlike bracket records there is no stop/target artifact at all: risk is the checkpoint re-evaluation plus the hard 16:00 ET close. The bet, as derived, is purely that time-of-day noise envelopes confirmed by VWAP port to BTCUSDT 5m bars inside a US-cash-session grid — and chop stretches pay checkpoint round trips, disclosed, with no tuning inside this record.

## Signal

Exact rule as pinned (5m decision grid; close-evaluated market fills; two-sided — any other session, lookback, threshold, sizing, or fill is a different, unpinned rule):

- R1 — Measure grid: completed `5m` bars of BTCUSDT only. Session clock is America/New_York (DST-aware ET wall clock derived deterministically from bar timestamps): `OPEN_M=570` (09:30), `CLOSE_M=960` (16:00), weekdays Monday–Friday only. A bar belongs to a session iff its start minute `mStart ∈ [570, 960)`.
- R2 — Checkpoints: `NCHK = max(1, int((960−570−1)/30)) = 12` (recomputed independently this cycle — exact). Checks fire when a bar's close minute reaches `570+30·k` for `k=1..12`, i.e. 10:00, 10:30, …, 15:30 ET, evaluated on that bar's close. A missing checkpoint bar is caught up by the next bar at the last printed price (source `while` catch-up, pinned); on continuous crypto 5m this path is structurally idle.
- R3 — Session state (source lines 625–635): on the first in-session bar of a new day, `dayOk = (mStart == 570)` (a bar starting exactly at the open; `skipHol=false` pinned so no holiday logic fires), `dOpen = open` of that bar, `prevClose = lastClose` (16:00 close of the last filed day), VWAP accumulators reset, `nextChk = 0`, `want = 0`.
- R4 — Noise band (source lines 647–653, 668–676): at checkpoint `j`, `sg = 1.0 · mean over the 14 filed sessions of |close at checkpoint j ÷ that session's open − 1|`; `ub = max(dOpen, prevClose)·(1+sg)`, `lb = min(dOpen, prevClose)·(1−sg)` (`useVwap`/`useGap` pinned enabled — disabling either is a different, unpinned rule).
- R5 — VWAP (source lines 640–644): `cumPV += hlc3·volume`, `cumV += volume` over the session's bars to the check; `vw = cumPV/cumV` (`hlc3` fallback iff `cumV == 0`, pinned).
- R6 — Latch (source lines 680–684, strict inequalities pinned): `upT = max(ub, vw)`, `dnT = min(lb, vw)`; `want = 1` iff `close > upT` (long leg live — `dirIn="Both"` pinned), `−1` iff `close < dnT`, else `0`. Since `upT ≥ dnT` by construction, long/short are mutually exclusive — no same-bar dual-fire ambiguity.
- R7 — Orders (source lines 689–695): only on a checkpoint bar where `want` changed since the prior checkpoint: `want==1` → market long entry, `want==−1` → market short entry (reversal nets at the same close, `pyramiding=0` pinned), `want==0` → `close_all("Stop")` — the checkpoint trailing exit. Fills at that bar's close (declared conversion of the author's next-bar-open fill).
- R8 — Session close (source lines 702–719): the bar ending at 16:00 (`mEnd ≥ 960`) closes everything at its close, sets `want = 0`, then files the day into the 14-session history iff `dayOk` and all 12 checkpoints printed and `mEnd == 960` exactly; `lastClose = close`. Nothing is ever held past the session.
- R9 — Outside-session guard (source lines 621–623, pinned as-is): any position alive outside the session grid is closed immediately.
- R10 — Risk legs (pinned absence, not invented): no take-profit, no ATR stop, no time exit beyond the session close, no cooldown, no adds/partials/pyramiding — explicitly none, matching the shipped code (zero `strategy.exit`).
- R11 — Warmup and gaps: flat until 6,000 completed `5m` bars (≈20.8 calendar days — covers 14 filed weekday sessions plus `prevClose` seeding and DST-boundary margin; structural need is 14 filed sessions for `ready`). Missing-bar stretches freeze evaluation at the prior target — never backfilled, never forced flat.
- R12 — Invariant identifier: `TV:pinedigga-jiwqijwC|noise14x1.0_chk30_gap-vwap_both|tmOff_skipHolOff|independent-derived-v1|BinanceFutures:BTC-USDT:5m|TWO-SIDED|closeeval-MARKET|fee0.0005|lev1x|size0.01|sess0930-1600_ET_MoFr|warmup6000|2026-11-03` (any constant, option, direction, sizing, or cost change is a different derivative).

## Required data

- Completed `5m` bars of BTCUSDT only: `open`/`high`/`low`/`close`/`volume` (session anchor, gap anchor, band excursions, VWAP via `hlc3·volume`, checkpoint closes, fill prices). Timestamps double as the ET session clock. No funding/OI/mark-index read gates any order, no sentiment/macro/on-chain/cross-venue state.
- Checkpoint grid: one latch evaluation per half-hour mark (12 per session); entries/reversals/flat-exits fill at the checkpoint bar's close; session-close exit at the 16:00 bar's close. All inputs are completed-bar values.
- Warmup: flat until 6,000 completed bars (structural). No repainting, no negative shift, no future reference, no full-sample normalization (every leg is a trailing statistic over filed sessions; boundaries are constants).

## Execution assumptions

- Research market: BTCUSDT Binance USDT-M perpetual, 1× isolated, fixed 0.01 BTC per entry, no adds, no compounding. Both legs default-enabled, so the short permission is genuinely used.
- Order timing (declared close-evaluated conversion; the author ships next-bar-open fills): checkpoint-bar-close decision with same-bar-close market fills for entries/reversals/flat-exits and the session-close exit — the same lane primitive admitted Forven-sibling records use. No maker-touch, queue, or intrabar-path-dependent fill is claimed. R6's mutual-exclusion proof leaves no ambiguous same-bar fill order.
- Sizing/capital/costs: fixed 0.01 BTC per entry; explicit research cost overlay 0.05% taker fee per side plus realized funding while in position — no hypothetical zero funding is claimed anywhere (the author's 0-commission/3-tick NQ slippage does not port to crypto). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one position at any time (`pyramiding=0`); reversal nets at a single close so overlapping entries are structurally impossible; re-entry after a checkpoint stop is explicitly allowed (the author's measured "re-entries pay" property is preserved as behavior, not as a number); no cooldown — explicitly none, not invented. Single engine position; no shared portfolio state, no multi-pair logic. Safety orders: explicitly none.
- Pinned-engine path (verified against local checkout `2dbc844`, `VERSION=2.17.0`): `data_feed/candles_feed/candles_base.py:35` maps `5m → 300`; `strategy_v2/backtesting/backtesting_engine_base.py:284-287` feeds `processed_features.loc[i:max_ts]` (window from the decision row) into `simulate_executor`; `strategy_v2/backtesting/executors_simulator/order_executor_simulator.py:22-24,56` fills MARKET at the first window row's `close`. Hence a completed-bar-t decision fills at `close[t]` — the coded timing. The ET session clock, checkpoint catch-up, VWAP accumulation, and holiday-off branch are deterministic controller logic over completed klines; no external feed is required.

## Evidence

### Source-reported

The script page and code comments ship every adopted headline fact quoted in Provenance: the 14-session same-clock-time noise band, the gap anchor, the 30-minute checkpoint grid (10:00–15:30 ET), the close-above-max/close-below-min VWAP double gate, next-bar-open fills, the checkpoint trailing stop, the 16:00 ET close with day-filing, Mon–Fri grid, `Both` direction default, fixed sizing, and the Trend Magic Off-means-original-rule instruction. It ships zero adopted performance numbers for this record: no NQ point total, profit factor, win rate, drawdown, trade count, or per-trade figure from the page, tooltips, or reference engine is adopted anywhere — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Logic checks executed during this scout cycle (this cycle's own Python, synthetic inputs only — no real-market replay, no profitability figure):

- `NCHK = max(1, int((960−570−1)/30)) = 12`; checkpoints at 10:00 … 15:30 ET — exact match to the author's stated grid.
- Order census on the fetched source text: 2 `strategy.entry` (L/S), 4 `strategy.close_all` (outside-session guard, TM exit, checkpoint Stop, session Close), 0 `strategy.exit`, 0 `strategy.order`, 0 `request.*`/`security(` — matches the line-by-line read (TM exit is dead code under the pinned `tmMode="Off"`).
- Band arithmetic on a synthetic 14×12 excursion table: `sg = mean = 0.037857` → `ub = max(100, 99.5)·1.037857`, `lb = min(100, 99.5)·0.962143`; `upT ≥ dnT` holds by construction so no checkpoint can print both sides.
- Dead-session check: with all excursions zero, `sg = 0`, bands collapse to the gap anchor and VWAP decides alone — no phantom signal path.

### Negative evidence

1. Fill-conversion lag fenced: derived close-evaluated fills differ from the author's next-bar-open fills by up to one full `5m` bar on every checkpoint trade — fast checkpoint-to-checkpoint reversals give back more than the author's tester would show. This is the coded trade, disclosed, not a tunable parameter here.
2. Session-grid移植 fenced: the US-cash-session grid (Mon–Fri 09:30–16:00 ET) is an equity construct; BTCUSDT trades 24/7, so ~74% of weekly bars are structurally sidelined and weekend trend moves are never touched — the derived event set is its own object, never the author's NQ output.
3. Number silence fenced: no NQ point total, profit factor, win rate, drawdown, trade count, or per-trade figure from the script page, tooltips, or reference engine is adopted anywhere, and any dispute over exact magnitudes is decided against this record, never patched by inference.
4. Derivation boundary fenced: the only non-author behavior is the six declared adaptations (venue, fixed sizing, TM Off, holiday-skip Off, close-evaluated fills, 6,000-bar warmup); the session grid, lookback, band/VWAP construction, strict gates, state priority, checkpoint cadence, filing rule, and no-bracket stance are source-faithful. This record is therefore never evidence that the author's script passes.
5. Fully exposed at checkpoints: between two half-hour marks an adverse excursion of any size is ridden without any exit path by construction — the checkpoint-only risk model, disclosed.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `14` sessions / `×1.0` width / `30`-minute grid / gap anchor / VWAP double gate / strict inequalities / `Both` / TM Off / holiday-skip Off / close-evaluated fills / fixed 0.01 BTC 1× two-sided / BTCUSDT `5m` / Mon–Fri 09:30–16:00 ET are frozen.

- F1 — Seasonality relevance: a pooled-volatility twin (single trailing 14-session mean excursion applied to all checkpoints, same grid/gates/fills) must not improve net expectancy; fail ⇒ the same-clock-time seasonal structure adds nothing over a plain widening funnel.
- F2 — VWAP relevance: a band-only twin (VWAP gate forced pass, trailing exit at the band alone) must not improve net expectancy; fail ⇒ the VWAP double gate and VWAP-side trailing exit are fee-burning decoration.
- F3 — Checkpoint relevance: a every-bar twin (latch evaluated on every 5m close, same bands/VWAP/session-flat) must not improve net expectancy; fail ⇒ the half-hour checkpoint discipline destroys more expectancy than it saves in avoided noise trades.
- F4 — Selectivity relevance: buy-and-hold over the same sample must not improve net expectancy; fail ⇒ sitting out non-signal hours and weekends costs more in missed drift than it saves in avoided chop.

## Crypto portability

Pinned to BTCUSDT Binance USDT-M perpetual (decision grid completed `5m` bar closes inside the ET session grid; fills at those closes; volume read from the same klines; no venue-specific read). The arithmetic ports across perpetual venues without structural change (no corporate-action or calendar adjustment exists to recheck; a spot-only deployment expresses the long-leg event set — pinned, not approximated — while the short leg requires a margin venue). Extension to other house-universe assets, timeframes, sessions, lookbacks, widths, or grids would be a different, unpinned claim.

## Limitations

- Single-asset port: the author's evidence is NQ futures inside a US-cash-session grid; BTCUSDT 5m checkpoint behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Conversion lag: close-evaluated fills deviate from the author's next-bar-open execution on every checkpoint trade — the derived event set is its own object, never the author's tester output.
- Weekend blindness: the retained Mon–Fri grid ignores Saturday–Sunday crypto price action entirely — a pinned artifact of the equity-session port, not a market claim.
- DST handling: the ET wall clock must be DST-aware in the controller; a fixed-offset implementation would misplace the grid for part of the year — flagged as an implementation obligation, not strategy behavior.
- VWAP fallback: sessions opening on zero-volume stretches fall back toward `hlc3` prints — fenced by the pinned `cumV == 0` branch, never traded around.

## Implementation status

Not implemented. No Hummingbot controller, Qlib recipe, or backtest artifact exists for this record; `hb_ready_status: PASS` admits it to model-consistent research only.

## Adoption boundary

Research-only. Not approved for Paper, Testnet, or Live trading. Any execution requires a separate downstream authorization plus the `IMPLEMENTATION_NEEDED` materialization route; this record carries no executable recipe.

## Related Wiki records

None.

## Sources

- TradingView OPEN-SOURCE SCRIPT by PINEDIGGA (script ID `jiwqijwC`), fetched and read live 2026-11-03: https://www.tradingview.com/script/jiwqijwC-INTRADAY-MOMENTUM-DIGGA-Noise-Area-Breakout/
- Idea lineage (context only, no numbers adopted): Zarattini, Aziz & Barbon (2024), "Beat the Market: An Effective Intraday Momentum Strategy for S&P500 ETF (SPY)" — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4824172
