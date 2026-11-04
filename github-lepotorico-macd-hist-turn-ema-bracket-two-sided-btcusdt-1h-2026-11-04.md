---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: LePotoRico MACD-histogram-turn EMA-trend-gated bracket two-sided on BTCUSDT 1h bars
created: 2026-11-04
updated: 2026-11-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-11-04
sources:
  - https://github.com/LePotoRico2105/pine-script-strategies/blob/e8bb2935b98ca446ad1063fb75a500410d344c5a/strategies/macd_4h_rhythm.pine
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# MACD Histogram Turn (EMA-trend-gated, pip-bracket) — independent BTC-USDT 1h two-sided derivative

## Provenance

**Canonical source (fetched live over HTTPS this cycle, immutable pin):** `LePotoRico2105/pine-script-strategies` commit **`e8bb2935b98ca446ad1063fb75a500410d344c5a`** (2026-04-03 — still the repo HEAD, verified live this cycle via the commits API), file **`strategies/macd_4h_rhythm.pine`**, blob `1979a25da93665b03dae1cc6755ab67507e88588`, **1,736 bytes / 48 lines**, Pine v5, `strategy("MACD 4H Rhythm", ...)` — a real strategy with native entries and exits, not an indicator. Raw bytes re-downloaded this cycle hash to sha256 `c90571375b02cb1e4d3144cff90c42d339e7468dba52020033a0c32abfcffd87`, byte-identical to the working copy. Permalink above. Repo license is **MIT** — short-literal citation only, no source block reproduced. Same repository family as the merged `github-lepotorico-bb-squeeze-width-gated` and `github-lepotorico-smc-ob-fvg` records (a different file, mechanism, and timeframe — fenced below).

**Order-affecting logic read verbatim (code governs):** source defaults `fastLen = 12` / `slowLen = 26` / `signalLen = 9` / `emaFast = 21` / `emaSlow = 50` / `slPips = 50` / `tpPips = 100`; declaration `strategy("MACD 4H Rhythm", overlay=true, default_qty_type=strategy.percent_of_equity, default_qty_value=2)`; pip `pipValue = syminfo.mintick * 10`; indicators `[macdLine, signalLine, histogram] = ta.macd(close[1], 12, 26, 9)`, `histPrev = ta.macd(close[2], 12, 26, 9)`, `fastEMA = ta.ema(close[1], 21)`, `slowEMA = ta.ema(close[1], 50)`; signals `histTurnsPositive = histogram > 0 and histogram[1] <= 0` (mirrored negative), `bullTrend = fastEMA > slowEMA` (mirrored bear); entries `strategy.entry("Long", strategy.long)` / `strategy.entry("Short", strategy.short)`; brackets `strategy.exit("Long Exit", "Long", stop=close - 50*pipValue, limit=close + 100*pipValue)` (mirrored short). The README's strategy-details §3 prose matches the code (histogram-turn + EMA21/50 gate, 50/100-pip 1:2 box, H4).

**Pine-block census (48-line fence):** 1 `strategy(`; 2 `strategy.entry` / 2 `strategy.exit` / 0 `strategy.close` / 0 `strategy.order`; 0 `request.*` / 0 `security(` / 0 `lookahead` / 0 `input.session` / 0 `timeframe.*` / 0 `calc_on_every_tick` / 0 `bar_magnifier` / 0 `pyramiding` / 0 `process_orders_on_close` — all recorded as absent, never filled in. `histPrev = ta.macd(close[2], ...)` is computed and never read (dead diagnostic — fenced as inert, disclosed). Zero `open` / `high` / `low` / `volume` reads for signals (the rule consumes `close` only — `high`/`low` nowhere in signal legs). Every predicate reads `[1]`-shifted confirmed data only (the exit levels latch the signal bar's own `close` — causal, disclosed); the repo's "anti-repainting" header claim holds for the ported legs (verified by construction, disclosed as code fact, not adopted marketing). The README's backtest figures (412 trades, 53.8% win, PF 1.38, MDD 11.7%, Sharpe 1.19, "10 years of M1", 2-pip-spread Backtrex methodology) have no auditable trade-level provenance in the pinned source and are **explicitly not adopted** — none appears below.

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction — the market/timeframe pin (source tested forex H4 per its README; this record pins Binance BTC-USDT perpetual 1h), fixed **0.01 BTC** sizing with 10,000 USDT cash, **0.0005/side** researcher fee and Isolated 1× (source: 2% of equity), pip-distance pin `50/100 × 1.0` USDT (source: `50/100 × syminfo.mintick*10` — pinned at BTCUSDT `tickSize 0.10` so `pipValue = 1.0`, disclosed), close-decided next-bar-open fills for the stop/limit legs (Pine fills `strategy.exit` stops/limits intrabar — the research-model timing convention differs, disclosed), the stop-first same-bar resolution with opposite-setup precedence (below, disclosed), and the 70-bar warmup floor (below, disclosed) are researcher adaptations. All are completely specified here; original claims are kept separate above.

**Immutable derivative identity:** `GH:LePotoRico-e8bb293|macd12-26-9_hist-turn_ema21-50_SL50-TP100|independent-derived-v1|BinanceFutures:BTC-USDT:1h|TWO-SIDED|0.01BTC|nextopen-MARKET|fee0.0005|cash10000|lev1x-isolated|opposite-first-stopfirst-tiehold|warmup70|2026-11-04`. Changing any formula, length, multiple, timing, market, risk, cost, cash, leverage or direction creates a different derivative.

**Pre-write dedup (2026-11-04):** working-tree base is current `main@a290673e` (554 root strategy records, READMEs excluded; this file is the 555th). Filename search for `lepoto.*macd` / `macd.*rhythm` / `hist.*turn` returns zero signal records (the three `macd-histogram` hits are Haehnchen/CCI-ADX and Tradelexx sniper machines, fenced below). Whole-word content search for `histTurnsPositive` / `macd_4h_rhythm` / `1979a25d` / `c9057137` returns zero records (bare `pipValue`/`slPips` hits are zero pool-wide). No open `research/*` PR is this file, author file, or construction (17 open PRs enumerated — #48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708, #725 — none colliding, including #662 Jasonkasei dual-MACD fenced below). Not a duplicate, paraphrase, or trivial parameter variant: five-axis distinction vs nearest pool neighbors is recorded in Negative evidence.

## Economic mechanism

### Source-reported

Momentum ignition confirmed by trend location: when the MACD histogram flips direction (fresh positive/negative momentum) while the EMA21/50 stack names the regime, the market is starting a rhythm leg; the strategy buys the flip in the trend direction, stops 50 pips away, and targets 100 pips (1:2). No behavioural channel beyond this construction is claimed in the 48 lines.

### Research interpretation

Unlike pool MACD records that trade zero-crosses gated by SMA levels with ATR boxes (FMZ MACD-zero-cross, long/short on MACD-line zero-cross + SMA50 + 1.5×/2.0× ATR), signal-crosses gated by zero-side with live-SMA stops (TradersPost MACD86, MACD-signal cross + both-lines-side + SMA200 guillotine + 2R box), or naked cross-to-cross reversals with no gate and no bracket (macd-signal-cross-reversal, always-in-market), this machine gates purely on the histogram-direction turn (no zero-cross, no signal-cross) with an EMA-stack trend filter (no SMA level, no zero-side gate, no oscillator) and exits purely on a latched 50/100 pip box (no ATR, no live-SMA guillotine, no trailing, no opposite-cross exit, no time stop). The failure mode is plain: a histogram flicker inside chop fires entries that stop 50 USDT away, and a vertical trend without any histogram-direction flip never enters at all.

## Signal

Index completed UTC 1-hour bars `t = 0, 1, ...` with real Binance BTC-USDT perpetual `C[t]` for every signal/risk leg. A bar with missing/nonfinite/non-positive close is invalid for signals. All constants are source-default literals; `ta.ema`/`ta.macd` are pinned at Pine defaults (recursive EMA `k = 2/(n+1)`, MACD `macdLine = EMA12 − EMA26`, `signalLine = EMA9(macdLine)`, `histogram = macdLine − signalLine`).

- **Oscillator and trend (causal, per-bar):** `E12[t] = EMA12(C[..t-1])`; `E26[t] = EMA26(C[..t-1])`; `M[t] = E12[t] − E26[t]`; `S[t] = EMA9(M[..t])`; `H[t] = M[t] − S[t]`; `F[t] = EMA21(C[..t-1])`; `SLW[t] = EMA50(C[..t-1])`. First valid `M/S/H` needs the slow-26 + signal-9 seed (34th bar region); first valid `F/SLW` needs the 50-bar seed; first actionable decision needs the histogram-history reference below.
- **Turns and gates (source-exact):** `HTpos[t] = H[t] > 0 and H[t-1] <= 0`; `HTneg[t] = H[t] < 0 and H[t-1] >= 0`; `BULL[t] = F[t] > SLW[t]`; `BEAR[t] = F[t] < SLW[t]` (all strict — equality on either leg fails its predicate).
- **Predicates (actionable only t ≥ 70, at bar `t`'s close):** `long[t] = HTpos[t] and BULL[t]`; `short[t] = HTneg[t] and BEAR[t]`. Pre-warmup bars flat by record rule. Long/short legs are provably mutually exclusive on every bar (`H[t]` cannot be both strictly positive and strictly negative; `F[t]` cannot be both strictly above and strictly below `SLW[t]`) — no entry tie-break is required; flat with both legs is unreachable by construction. Equality edges (`H[t] == 0`, `H[t-1]` ties, `F[t] == SLW[t]`) are explicit neither-fire holds.
- **Source-arithmetic risk (latched at signal bar `t`, never moved):** long `SL = C[t] − 50×1.0`, `TP = C[t] + 100×1.0`; short mirror `SL = C[t] + 50×1.0`, `TP = C[t] − 100×1.0` (`pipValue = 1.0` pinned from verified `tickSize 0.10`, disclosed above).
- **Straddle by construction (explicit researcher pin):** entries require no extra guard — the pip distances are strictly positive so `SL < C[t] < TP` long and `TP < C[t] < SL` short hold on every signal bar by arithmetic; inverted or `na` legs are unreachable at the pinned defaults. No division exists anywhere (zero-division impossible).
- **Resolution (explicit researcher pin):** entries/reversals fill next-bar-open MARKET. Each held bar `v` (fill bar +1 onward) is evaluated at its close in fixed order — opposite setup first (reversal dominates: close then re-enter at next open), else SL-touch (`L[v] <= SL` long / `H[v] >= SL` short), else TP-touch (`H[v] >= TP` long / `L[v] <= TP` short); SL+TP co-fire is one flat close (stop wins). Single position, no adds: same-side refire while positioned is a no-op under the pinned pyramiding-0 rule; re-entry re-arms on any qualifying post-exit signal with no cooldown (explicitly none, not invented).

## Required data

- Completed `1h` bars of BTCUSDT: `close` only (every order-gating line reads `close` with fixed non-negative shifts; no `open`, no `high`/`low`, no `volume`, no funding/OI/mark-price leg, no calendar, no multi-asset input). Exit touches are evaluated against the completed bar's `H/L` range under the research-model convention (disclosed above).
- Warmup: 70 completed `1h` bars flat by record rule (structural minimum is the 51st completed bar — 50-bar EMA50 seed plus the histogram-history reference — plus researcher margin).
- Point-in-time: every window trails over completed bars only; the signal bar's own close is the last input and the bracket-latch reference; fills at next-bar open. No repainting, no negative shift, no future reference, no full-sample normalization, no MTF call, no session template. Exactly one evaluation per completed bar.

## Execution assumptions

**Exact bounded engine:** Hummingbot package label `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (local checkout `2dbc844` verified this cycle: `BacktestingEngineBase.run_backtesting` present in `backtesting_engine_base.py` line 221, `determine_executor_actions` in the controller bases line 747, `OrderExecutorSimulator` class byte-present in `backtesting/executors_simulator/order_executor_simulator.py` line 9, `INTERVALS "1h": 3600` in `binance_perpetual_candles/constants.py` line 18). A different deployed package must be revalidated.

- **Market/feed:** Binance BTC-USDT perpetual, one 1h OHLC stream (single-feed design — no MTF, no session, no second symbol). Next-open MARKET fills for entries and reversals (source-native Pine default timing); the stop/limit bracket is resolved close-decided against completed-bar `H/L` with next-open fills (research-model convention differing from Pine intrabar exit fills, disclosed — same bracket class as the merged SMMA17, SMC and BB-squeeze sibling records).
- **Controller path:** `BacktestingEngineBase.run_backtesting` → `controller.determine_executor_actions` → `CreateExecutorAction(OrderExecutorConfig)` → `OrderExecutorSimulator.simulate`. A **strategy-specific, not-yet-implemented** controller must compute the histogram-turn plus EMA-stack state machine, the latched 50/100 pip bracket, and the opposite-first stop-first tie-hold pin. The generic executor does not calculate the strategy.
- **Sizing/capital (stated plainly):** fixed 0.01 BTC per position, 10,000 USDT cash admission, Isolated 1×, 0.0005/side researcher fee plus modeled funding with explicit limitations (modeled funding is never reported as realized funding; no hypothetical zero funding claimed). The downstream house overlay changes no trade event under the predeclared single-position rule — DCA is a downstream execution experiment, never an admission leg of this version.
- **Risk posture (explicit):** the latched stop+limit bracket is the sole position-ending path besides opposite-signal reversal. Trailing stop, breakeven move, time stop, partial exit, and averaging are absent in source and recorded as explicitly disabled, never defaulted. An end-of-sample open position is marked at the last real valid close, never closed with an invented fill. Missing trade prices are never fabricated (pre-warmup and invalid bars stay flat).

## Evidence

### Source-reported

The pinned 1,736-byte file ships the complete construction (frozen `12/26/9/21/50/50/100`, EMA/MACD legs, histogram-direction-turn triggers both sides, EMA-stack trend gate, pip box with 1:2 RR, two-sided stance, pyramiding-0 default). It ships no performance number of any kind — this record claims no source-reported performance, and no backtest figure is invented here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No twin-signal ambiguity: the file holds exactly one long predicate and one short predicate over shared series — no second decision path, no variant menu, no timeframe input to select between.
2. No estimator ambiguity: `ta.ema`/`ta.macd` are Pine built-ins with pinned default semantics; no ATR, no RMA/EWM, no Wilder alternative exists anywhere in the 48 lines.
3. `histPrev` quarantine, stated plainly: computed on every bar and read by zero order-gating comparisons (the live recency uses `histogram[1]` history-reference, never `histPrev`) — treating it as a gate, filter, or exit leg would be a different, unpinned rule.
4. Sizing quarantine, stated plainly: the `strategy.percent_of_equity / 2` declaration is replaced by the fixed 0.01 BTC research sizing (see Execution assumptions) — position-size changes no signal, gate, trigger, or bracket arithmetic. The `pipValue = syminfo.mintick*10` stub is pinned at `1.0` from the verified `tickSize 0.10` (50/100 USDT box, disclosed port — never a forex-pip claim on crypto).
5. Pool MACD cousins fenced, stated plainly: `fmz-macd-zero-cross-sma50-atr-bracket` trades MACD-line zero-crosses gated by an SMA50 level with a latched ATR box — different trigger × different gate × different risk; `github-traderspost-macd86-zero-sma200-2r` trades MACD-signal crosses gated by both-lines zero-side with a live-SMA200 guillotine plus 2R box — different trigger × different gate × different exit; `macd-signal-cross-reversal` is a naked cross-to-cross reversal with no gate and no bracket (always-in-market) — different gate × different exit × different state; `hummingbot-macdbb-bbp-macdh-turn` trades %B penetration with histogram-vs-line splits (a band-plus-split object) — different signal × different gate; `haehnchen-macd-histogram-cross` / `tradelexx-macd-sniper-hist3` trade HMA/CCI/3-bar confirmations (different conjunctions); open PR #662 Jasonkasei dual-MACD trades a dual-MACD histogram confirmed-cross with a close-bracket (dual vs single MACD, confirmed-cross vs direction-turn, close-bracket vs pip box). Bare `21/50` EMA literals elsewhere are crossover machines without any histogram-turn leg, never this conjunction.
6. Same-repo siblings fenced, stated plainly: `github-lepotorico-bb-squeeze-width-gated` cites `strategies/bollinger_squeeze.pine` (width-gated band breakout with midline-stop/2R box, 1h) and `github-lepotorico-smc-ob-fvg` cites `strategies/smc_ob_fvg.pine` (order-block + FVG + BOS confluence, 4h) — different files, different mechanisms, different risk arithmetic. Consolidating any two into one record would erase load-bearing event differences.
7. README-figure fence, stated plainly: the README §3 results table and Backtrex methodology paragraph are named here only to show they were read and rejected — vendor backtest marketing without trade-level provenance is never evidence, and none of its numbers enters this record.
8. Researcher self-check (logic only, never a backtest, never committed — scratch tape, 170 synthetic 1h bars flat-plus-up-sine-plus-down-sine, SMA-seeded EMA/MACD research convention): histogram-turn longs 2 (`79, 104`) plus shorts 2 (`136, 160`) fire on opposite trends with straddling 50/100 brackets, zero dual-fire bars, and the all-equal degenerate window fires nothing. Digest `5958644e`. `SELF-CHECK OK`. No Qlib/Hummingbot parity, no live/paper order, no profitability experiment occurred.

## Falsification plan

A pinned-engine replay that (a) recomputes `E12/E26/M/S/H/F/SLW` from completed 1h closes and matches the specified long/short event bars exactly, (b) honors next-open fills with the latched 50/100 bracket resolved opposite-first stop-first from fill-bar+1, and (c) preserves the warmup-70 flat prefix, falsifies this record if any event, price, or direction disagrees. Any parameter change (MACD lengths, EMA lengths, pip distances), any gate substitution (zero-cross, signal-cross, ADX/SMA level, zero-side), any exit substitution (ATR box, live-SMA guillotine, trailing stop, time stop), or any timing change (same-bar-close, intrabar fills) is a different derivative and does not falsify this one.

## Crypto portability

The rule reads `close` geometry only and ports to any continuously quoted BTCUSDT perpetual 1h feed. The short legs require a short-capable venue (Binance USDT-M perpetual satisfies this); on a spot-only venue the short legs are inexpressible and the record would not be the same rule. Min-notional/precision: 0.01 BTC notional exceeds the 50-USDT minimum by orders of magnitude at any plausible BTC price; quantity step `0.001` is exact. No calendar, session, or venue-specific tick assumption conditions any signal beyond the pinned `1.0` pipValue disclosed above.

## Limitations

- The stop/limit bracket timing is a disclosed research-model convention (close-decided, next-open fills), not Pine intrabar fills — live/historical slippage through the stop inside a wide-range bar is not modeled beyond the stop-first co-fire rule.
- Exits begin evaluating on fill-bar+1: a fill bar that spans the full 150-USDT box holds through its close by record rule (disclosed, never a source claim).
- The README's forex H4 provenance means crypto-1h behavior is a venue port, not a source-tested claim; no profitability, Sharpe, or win-rate expectation is carried over.
- Single fixed-size position: concurrent-signal capacity, portfolio margin interaction, and multi-strategy capital contention are out of scope for this admission version.
- `ta.ema`/`ta.macd` Pine seeding is pinned as written; the scratch self-check's SMA-seed is a researcher logic-verification convention, never a bit-equality claim with the Pine emulator. Substituting another seeder would be a different, unpinned rule.

## Implementation status

Not implemented. No controller, executor config, Qlib recipe, or deployment artifact exists for this derivative. Admission is an engineering-capability check on the bounded path above, not an executable materialization.

## Adoption boundary

Research-only. Not approved for Paper, Testnet, or Live trading. PASS means the declared derivative is causally expressible on the pinned backtest model — not profitable, not Qlib-paritied, not survivor-certified, not authorized for any live capital.

## Related Wiki records

None.

## Sources

- https://github.com/LePotoRico2105/pine-script-strategies/blob/e8bb2935b98ca446ad1063fb75a500410d344c5a/strategies/macd_4h_rhythm.pine (immutable rule source — read end to end this cycle)
- https://github.com/LePotoRico2105/pine-script-strategies (repository, MIT license, README strategy-details §3 prose — rules adopted, figures rejected)
- https://www.tradingview.com/pine-script-reference/v5/ (ta.ema / ta.macd / histogram history-reference / strategy.exit stop-limit / pyramiding-0 default)
- https://www.tradingview.com/pine-script-docs/concepts/strategies/ (broker-emulator default next-bar-open fills)
