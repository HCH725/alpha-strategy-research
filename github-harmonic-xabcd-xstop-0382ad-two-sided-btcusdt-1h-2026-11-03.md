---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: GitHub djoffrey completed-XABCD zigzag-census X-stop 0.382AD-box two-sided on BTCUSDT 1h
created: 2026-11-03
updated: 2026-11-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-06-26
sources:
  - https://github.com/djoffrey/HarmonicPatterns
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# djoffrey/HarmonicPatterns completed-XABCD zigzag-census X-stop 0.382AD-box — independent BTC-USDT 1h derivative

## Provenance

**Canonical source (cloned and pinned live over HTTPS this cycle):** GitHub repository **`djoffrey/HarmonicPatterns`** ("A library written in Python to search harmonic patterns automatically", MIT license), pinned commit **`1e0cd81a96132a1c3337dbbfce39f13d4606758b`** (`2026-06-26 17:14:12 +0800`, `refact(pkg): modernize packaging with pyproject.toml and uv, ...`). Record `source_as_of` is that commit stamp, never a fetch date. Core file **`src/harmonic_patterns.py`: 1,496 lines / 55,417 bytes**, sha256 **`4a33437efd9be2651f24cf3ca57e672f7c3c4cf02ae9d13969cae8385e052cfb`**; **`src/settings.py`: 16 lines / 434 bytes** with `ERROR_RATE = 0.05` (line 6), `MAIN_SYMBOLS` headed by `BTC/USDT`, `PERIODS = ['30m', '1h', '4h']`. No LICENSE ambiguity (MIT at repo root). Short-literal citation only — no source block reproduced.

**Order-affecting logic read verbatim (code governs):** constructor defaults `error_allowed=0.05, strict=True` (line 36); asymmetric equality `is_eq(n, m) = (m·0.95 ≤ n ≤ m)` — tolerance on the below side only, hard ceiling at the ideal ratio (lines 42–46); strict membership `is_in(n, l, r)` = `n` is_eq-matches some listed Fibonacci ratio inside `[l, r]` (lines 48–59) over exactly 15 ratios `FIBB_RATIOS = [0.618, 1.618, 0.786, 0.886, 1.13, 1.27, 0.382, 0.5, 0.707, 1.41, 2.0, 2.24, 2.618, 3.14, 3.618]` (lines 15–20); Double-Zig-Zag pivot machine `get_zigzag(df, window)` (lines 61–106, attribution comment to the TradingView Double-Zig-Zag script at line 63) with rolling-`window` prior-bar extremes, direction latch, extension-revision of the provisional last pivot only, and both-extremes bars recording the HIGH leg; completed-pattern census functions for all ten detectors in fixed order `gartley, bat, altbat, butterfly, crab, deepcrab, shark, 5o, cypher, abcd` (lines 1283–1294), e.g. Gartley `is_eq(XAB,0.618) ∧ is_in(ABC,0.382,0.886) ∧ is_in(BCD,1.13,1.168) ∧ is_eq(XAD,0.786) ∧ is_eq(ABCD,1)` (lines 236–242); universal direction `direction = 1 if D<C else -1` (bullish iff D below C); scan loop `for window in [8, 13, 21, 34, 55]` (line 1452) with `only_last` taking each window's last quintuple and the `last_n` filter keeping quintuples whose D-pivot index equals `len(df) − last_n` (lines 1461–1467, `assert last_n < 5` at line 1449); cross-window dedup by bar-index quintuple, first-window keep (lines 1366–1386). The live-alert entrypoint (`examples/run_detect.py`, line 144) runs `only_last=True` with the `last_n=4` default (line 93); the README quickstart scans `BTC/USDT 1h` with `error_allowed=0.05, strict=True`.

**No trading rules ship in the source (verified by grep this cycle):** zero hits for `stop_loss|take_profit|position_action|order_|leverage|quantity|amount` across the core file — the library is a pure detector (plus predictors and plotters, both fenced OUT below). Entry, side-mapping, exits, sizing, costs, warmup and state are therefore 100% researcher-declared derivative design, predeclared here before review, never attributed to the source.

**Derived-record declaration:** this file specifies a separately identified derived executable strategy, not a lossless reproduction. Researcher-declared adaptations are exactly nine: (1) research market/timeframe Binance BTC-USDT perpetual `1h` — source-native frame (settings list `BTC/USDT`, periods list `1h`; perpetual is the minimal realistic venue because both firing legs include short exposure needing margin — disclosed); (2) fire timing: close-decided evaluation with the source's own live-alert convention (`only_last=True`, `last_n=4`: fire iff a last-quintuple census passes with D-index `== t−4`), entries/reversals/flat-exits fill next-bar-open MARKET (researcher fill pin — disclosed); (3) direction→side mapping `+1→LONG / −1→SHORT`, two-sided (researcher pin — disclosed); (4) risk box `SL = X` pivot price, `TP = D + 0.382·(A−D)` (Carney-textbook-inspired 0.382-AD first target, pinned as researcher design, never a source fact — disclosed); (5) state pin — single position, no adds, same-side refire no-op, opposite fresh fire reverses (close+open at the same next open), per-held-bar code order opposite-signal → SL-touch → TP-touch (SL wins ties) → 336-bar time-cap, all with next-open fills (disclosed); (6) fixed **0.01 BTC** sizing (≈770.0 USDT at probe close 76,998.0, above verified 50-USDT min-notional and 0.001 min-qty; Isolated 1× — disclosed); (7) explicit **0.05%/side research cost**, slippage unmodeled (disclosed); (8) **500-bar warmup**, pre-warmup bars flat (55 = structural max zigzag window, plus researcher margin per the admitted precedent chain — disclosed); (9) degenerate-leg guard (any zero XA/AB/BC/XC leg skips the quintuple — the source would ZeroDivisionError; crash-avoidance, disclosed) and fenced-out predict/visualize paths (`predict_pattern`, `plot_patterns` — dropped, disclosed).

**Fire-once uniqueness (answers closed-PR #537 blocker 1 by construction):** a quintuple's D-index equals `t−4` for exactly one decision bar `t`; pre-warmup completions can never refire later, and no retirement set or seen-latch is needed — the actionable event set is uniquely reproducible from the rule alone.

**Immutable derivative identity:** `GitHub:djoffrey-HarmonicPatterns@1e0cd81|XABCD-completed-census-10det-strict-err0.05-W8-13-21-34-55-lastquint-D==t-4|independent-derived-v1|BinancePerp:BTC-USDT:1h|TWO-SIDED|0.01BTC|nextopen-MARKET|SL=X|TP=D+0.382AD|fee0.0005|lev1x-isolated|reversal-dominate-stopfirst-noop-timecap336|warmup500|2026-11-03`. Changing any ratio, window, lag, timing, market, risk, cost, leverage or direction creates a different derivative.

## Economic mechanism

### Source-reported

Mean-reversion at completed harmonic reversal zones: five alternating ZigZag pivots (X,A,B,C,D) whose leg ratios lock to Fibonacci ideals are labeled bullish/bearish by D-vs-C. The README claims only detection scope (9–10 patterns, completed + predicting scanning, crypto-market examples); it ships no performance figure, no trade rule, no market thesis — none adopted.

### Research interpretation

Unlike pool single-swing Fib machines (one retracement level, long-flat) and unlike pool candle-shape machines (bar-local geometry), this machine trades **five-pivot ratio locks**: the ZigZag compresses hundreds of bars into an alternating extreme skeleton, and the strict below-only census admits only quintuples whose four ratios sit just under Fibonacci ideals. The conjunction is the edge object: structure (alternating pivots) × harmony (four simultaneous ratio locks) × confirmation (D four bars old, still the last pivot). Live-window rate is 12 post-warmup fires per 62,690 1h bars (abcd 3 / fiveo 2 / cypher 5 / shark 2; gartley/bat/altbat/butterfly/crab/deepcrab zero — see Limitations for the as-coded feasibility proof), driving 12 entries and 12 exits (2 SL / 10 TP / 0 reversals / 0 time-caps). The self-scaling X-stop/0.382AD-target box breathes with each pattern's own XA span — quiet compressions risk/take little, extended patterns risk/take more.

## Signal — Gate 1, fully pinned derivative

Index completed UTC 1-hour bars `t = 0, 1, ...` with real Binance BTC-USDT futures `C[t]` closes, `H[t]`/`L[t]` extremes, `O[t]` opens. A bar with missing/nonfinite/non-positive OHLC is invalid (excluded from extremes and pivots).

- **ZigZag (source-faithful, per window `w ∈ {8,13,21,34,55}`):** for `idx ≥ 1`, `HH = max(H[idx−w..idx−1])`, `LL = min(L[idx−w..idx−1])` (bars strictly before `idx`; `idx < w` yields no pivots — exact `ta.MAX/MIN` NaN port); `newH = (H[idx] ≥ HH)`, `newL = (L[idx] ≤ LL)`; direction latch and last-pivot revision exactly per lines 76–106 (both-extremes bar records HIGH; revision only replaces the last pivot).
- **Census (actionable only `t ≥ 500`, at bar `t`'s close):** per window, if ≥5 pivots over bars `[0..t]`, take the last quintuple; run the ten completed detectors in source order with `err = 0.05`, strict; keep firings with D-index `== t−4`. Cross-window dedup by bar-index quintuple (windows in source loop order, first keep). First surviving candidate wins the bar (co-fires counted, others ignored — disclosed; live co-fire count is 0).
- **Direction:** `+1 (D<C) → LONG`, `−1 → SHORT` (researcher mapping — disclosed).
- **Risk box (researcher-designed):** `SL = X`; `TP = D + 0.382·(A−D)` (identical formula both sides).
- **Resolution (explicit researcher pin):** entries/reversals fill next-bar-open MARKET; each held bar `v ≥ fill+1` (fill-bar exclusion per the admitted ledger-lag discipline) evaluates at its close — opposite fresh fire first (reversal dominates: close old, open new at the same next open), else SL-touch (`L[v]≤SL` long / `H[v]≥SL` short), else TP-touch (`H[v]≥TP` long / `L[v]≤TP` short); SL+TP co-fire is one flat close (stop wins); time-cap `v − fill ≥ 336` closes flat. Single position, no adds: same-side refire is a no-op.

## Required data / Gate 6 causality

**Warmup:** minimum 500 contiguous valid completed 1h bars; covers the 55-bar max zigzag scale plus multi-pivot formation span (live D−X spans run 35–145 bars, median 81 — comfortably inside) with researcher margin. No warmup-bar trades; pre-warmup flat by record rule; pre-warmup completions never refire (uniqueness proof above).

Binance Kline `timestamp` is bar-open `T[t]` (pinned perpetual-candles path; `1h` is a carried `INTERVALS` entry `3600` — byte-verified at the pin this cycle; forming bar dropped by `closeTime`, completed-only probe verified live this cycle: 62,690 bars 2019-09-08→2026-11-02). Bars become available no earlier than `T[t]+3600s`. All decisions use completed bars only; fills at next-bar open. The online zigzag uses only bars `≤ t` (prefix-equivalence proven by the prefixcheck tape: online snapshot equals standalone recompute on 260 bars × 5 windows). The D pivot is the provisional last pivot and may later be revised/extended by the source's own revision rule — the decision at `t` still uses only data `≤ t` (point-in-time; whipsaw risk disclosed, never back-filled). No MTF call, session template, second feed, repainted graphic, or future extremum. Signal-on-final-bar prints hold without filling — no invented fills. If this effective-time discipline cannot be enforced, Gates 5/6 fail in implementation.

## Execution assumptions / Gate 5 pinned Hummingbot path

**Exact bounded engine:** Hummingbot package label `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (ancestor of local checkout `2dbc844` verified this cycle via `merge-base --is-ancestor`; re-verified at the pin this cycle: `async def run_backtesting` in `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` line 221, `def determine_executor_actions` in `hummingbot/strategy/strategy_v2_base.py` line 747, `class OrderExecutorSimulator` byte-present in `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` line 9, `INTERVALS "1h": 3600` in `hummingbot/data_feed/candles_feed/binance_perpetual_candles/constants.py` line 18). Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative validation for this source/package path; this Scout did not independently rehash the wheel. A different deployed package must be revalidated.

- **Market/feed:** Binance BTC-USDT **perpetual futures** venue (source-native frame — settings name `BTC/USDT`; perpetual is the minimal realistic two-sided venue with native short exposure, answering closed-PR #627's spot-short blocker by construction — no borrowing, no spot inventory claim), one 1h OHLCV stream (single-feed design — no MTF, no session, no second symbol). Opens feed next-open fills.
- **Controller path:** `BacktestingEngineBase.run_backtesting` → `controller.determine_executor_actions` → `CreateExecutorAction(OrderExecutorConfig)` → `OrderExecutorSimulator.simulate`. A **strategy-specific, not-yet-implemented** controller must compute the five-window online zigzag, the ten-detector strict census, the D==t−4 fire rule with index-tuple dedup, and the X-stop/0.382AD-box state pin. The generic executor does not calculate the strategy.
- **Orders (OrderExecutor only — PositionExecutor deliberately unused):** entries `side = BUY/SELL`, `position_action = OPEN`, closes/reversals `position_action = CLOSE`, `amount = Decimal("0.01")` (≈770.0 USDT at probe close — above verified 50-USDT min-notional and 0.001 min-qty), `connector_name = "binance"`, `trading_pair = "BTC-USDT"`, `execution_strategy = MARKET`, `price = None`, `leverage = 1` (Isolated). MARKET legs fill at the next bar's **open** per the record timing pin. No fill executes if its required future bar is absent. Exit evaluation starts at `fill+1`, so every exit decision acts on a fill confirmed at least one full bar earlier (admitted ledger-lag discipline). Controller must use confirmed executor/hold state with a persistent ledger, never infer position from order requests. Fills are never conditional on equity, funding, or buying power: fixed-size 1× single-position with no compounding and no abort rule (disclosed).
- **Fees and accounting:** 0.05% per filled side is a RESEARCHER research-model pin; slippage unmodeled, **not** evidence of zero real slippage (disclosed). Funding is **flagged, never zeroed**: 1h holds routinely span funding stamps — modeled economics are not realized/canonical funding. No margin/cash-ledger behavior beyond the simulator's own accounting is claimed. Precision beyond min-qty/min-notional/tick facts, partial fills, market impact and live fee tier remain unverified — not an execution or profitability approval.
- **Package/commit binding disclosure:** `20260920` is retained as the policy package **label only**; Gate 5 is bounded to the pinned commit's research-simulation semantics re-verified above, reusing the previously reviewed MARKET next-open primitive with close-decided prior-bar-anchored exits and no novel executor type. Sibling PASS records are execution-path evidence only, never proof of this candidate.

## Evidence

### Source-reported

The pinned file ships the complete detection machine: asymmetric `is_eq`, strict fib-matching `is_in`, the 15-ratio table, the Double-Zig-Zag pivot engine, all ten completed-pattern censuses with exact lines, the `[8,13,21,34,55]` window loop, the `only_last`/`last_n` fire filter, index-tuple dedup, and the `1 if D<C else -1` direction rule; settings/README pin `BTC/USDT`, `1h`, `err 0.05`, strict; the live scanner pins `only_last=True, last_n=4`. It ships no performance figure and no trading rule of any kind — none adopted.

### Independently reproduced

**None.** No strategy backtest, event-level Qlib/Hummingbot parity, wheel rehash, deployment or profitability experiment occurred. Pinned engine source inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the port pipeline (exact-NaN zigzag with online/standalone prefix-equivalence, byte-faithful strict census with asymmetric `is_eq`, D==t−4 fire rule, dedup, and the fill+1 state machine), run in scratch (never committed).

**Planted-tape verification (this cycle, deterministic PASS, double-run identical):** T0 TIE prints all-flat over 80 bars (digest `e3b0c44298`); T1 BULL prints one window-8 bullish-bat fire (D==t−4 verified) driving 1 LONG open / 1 TP close ending flat (digest `6d0ae87e0c`); T2 BEAR mirror prints 1 SHORT open / 1 SL close ending flat (digest `c8ea0abc68`); T3 REV prints LONG / REV-close + SHORT-open same next-open / TP close ending flat (digest `ae29ea0bc6`); T4a ratio-miss (XAD pulled to 0.70) prints neither-fire 0 opens (digest `e3b0c44298`); T4b warmup-gate prints all-flat (digest `e3b0c44298`). T1 additionally caught a 0.00005 excursion above the 0.5 ideal rejected by the right-closed `is_eq` — the asymmetric port is behaviorally exact.

**Live-exchange microstructure probes (this cycle, futures 1h klines, 62,690 completed bars 2019-09-08→2026-11-02, forming bar dropped by closeTime, last close 76,998.0):** 12 post-warmup fires (abcd 3: bars 1532/23172/26304; fiveo 2: 3315/31226; cypher 5: 11778/21671/31294/57552/58971; shark 2: 20287/62346; gartley/bat/altbat/butterfly/crab/deepcrab zero) driving 12 state-machine opens / 12 closes (2 SL-touch / 10 TP-touch / 0 reversals / 0 time-caps) ending FLAT (event digest `a584b579f4`, signal digest `a89f066ec2`); first fire at bar 1532 (warmup sane); D−X spans 35–145 (median 81); co-fire bars 0; sub-window bars 20,000–40,000 print 6 events ending FLAT, same honest cut (digest `4077771dca`). 0.01 BTC ≈ 770.0 USDT notional at window close. Two independent runs produce identical digests. Admission is engineering capability, never an event-rate or profitability claim.

### Negative evidence

At the pre-write snapshot `main@3982abe5`, working-tree searches for `harmonic`/`gartley`/`zigzag`/`xabcd`/`butterfly`/`deepcrab`/`alt-bat`/`cypher` return **zero** strategy records (the lone `fibb` hit is a Supertrend-BB indicator record — different mechanism). Nearest pool siblings are single-swing Fib machines (`fibonacci-retracement-reclaim-long-btcusdt-1d`, `fmz-fib-retrace-swing-tsl-level-long-flat-btcusdt-1d` — one retracement level, long-flat, 1d), five-axis distinct from a five-pivot four-ratio census traded two-sided on 1h under an X-stop/AD-target box. Sixteen open `research/*` PRs inspected by per-PR title/head — no collision (nearest lanes are Alpha57-VWAP, EMA-stack-RSI, OneTrend, dual-MACD, volume-dip, supertrend, Heracles, ClucMay, AdxSmas, CCI, 2yMA, SSL, Chandelier, Gaussian, Larry-Williams — none a harmonic machine). Closed-PR scan surfaces exactly two harmonic family members, both materially distinct AND both closed for blockers this record structurally answers: #627 (TradingView Harmonic-Pulse indicator, spot market with unbacked SHORT, close-bracket exits — different source, different signal, different venue, different book; its spot-short gate-2/5 blocker cannot occur on this perpetual record); #537 (mattpartida harmonic-pattern-cli, Gartley-PRZ long-flat 1d — different source, single-pattern long-only 1d; its warmup-event ambiguity is answered by the fire-once D==t−4 construction, and its ledger-lag gap by the fill+1 exit discipline). Not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

After independent admission and separate downstream selection only: compare the frozen census box book against (a) window-subset twins (single-window 8 / 34 / 55 — isolating the multi-window loop; researcher variation), (b) per-pattern twins (abcd-only, cypher-only — isolating which detectors carry the 12 live events; researcher variation), (c) target twins at 0.618 AD and box twins with an X-margin stop (isolating the 0.382/SL@X researcher pins — never attributed to source), (d) lag twins at last_n 0/2/8 (isolating the 4-bar confirmation; researcher variation), and (e) warmup/timecap sensitivity (500 vs 1000, 336 vs 168). Check event rate, SL/TP/reversal attribution, hold-time distribution, and fill-anchor slippage. Event-level Qlib/Hummingbot parity of the strategy/execution path is required before mass screening if that path introduces a new unverified capability; do not interpret HB_READY as parity or profitability.

## Crypto portability

This derivative is **BTC-USDT Binance futures 1h** only — the source's own scanner frame, no port claimed. Stated plainly: the machine needs completed-bar OHLC plus the 500-bar admission warmup (lookback-bound); the entries are last-quintuple completed-XABCD locks with D four bars old at a live-window rate of ~12 fires per 62,690 1h bars; the exits are an X-stop/0.382AD-target box with reversal dominance and a 336-bar time-cap; 1h slippage plus funding apply to every held span. The ported legs carry no session, calendar, or gap dependence (the file ships zero session logic, disclosed), so 24/7 crypto continuous trading introduces no anchor or session-template port of any kind. No rescaling, no cross-asset claim is made. No frequency, profitability, or capacity claim is made. Seven-coin, 1h/4h/1d, BO/SO 6/6/6, and 3×/5× futures experiments are optional separate downstream campaigns, **not** admission requirements or silently authorized equivalent executions.

## Limitations

The venue-perpetual choice for two-sided margin, direction→side mapping, next-open fills, X-stop/0.382AD-target box, reversal dominance, stop-wins-tie, same-side no-op, fill+1 evaluation, 336-bar time-cap, 500 warmup, 0.01 BTC 1× sizing, 0.05% research fee, degenerate-leg guard, and predict/plot drops are researcher pins, never attributed to the source. **As-coded feasibility fence:** the completed-Gartley census is near-infeasible as written — with `BCD ≤ 1.13` and `XAB ≤ 0.618`, alternating-leg geometry caps `XAD` at `0.618·(1+0.886·0.13) ≈ 0.689`, below the required `0.786·0.95 ≈ 0.747` (the `1.13~1.168` BCD band reads like an author typo for a wider extension band — asserted as analysis, never repaired); Crab fails analogously on its `XAD == 1.618` leg. Both stay in the machine source-faithfully and simply never contribute (live zeros corroborate). The D pivot is provisional (source revision rule) — entries act point-in-time with disclosed whipsaw risk. The page ships no LICENSE ambiguity (MIT — short-literal citation only, research-only use asserted, no commercial claim). No Qlib parity, historical Survivor, HB Certified, Paper/Testnet/Live or profitability claim.

## Implementation status

`not-implemented`: no dedicated controller, Qlib executable recipe or deployment artifact was created. PASS is a bounded research-expressibility proposal, not a claim of already runnable materialization. A selected strategy may later need the minimal strategy-specific implementation without a second admission flag.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review must independently inspect this exact PR head, remediate only primary-source-verifiable facts, then PASS exact-head merge or NOT_LOSSLESS close. Scout does not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- Primary implementation + pin: https://github.com/djoffrey/HarmonicPatterns (MIT; commit `1e0cd81a96132a1c3337dbbfce39f13d4606758b` 2026-06-26; `src/harmonic_patterns.py` 1,496 lines / 55,417 bytes, sha256 `4a33437efd9be2651f24cf3ca57e672f7c3c4cf02ae9d13969cae8385e052cfb`; `src/settings.py` `ERROR_RATE = 0.05`, `BTC/USDT`, `1h`; live scanner `only_last=True, last_n=4`; zero trading-rule words by grep — short-literal citation only)
- Exchange verification: Binance futures `fapi/v1/exchangeInfo` (`BTCUSDT`, `PERPETUAL`, `TRADING`, `tickSize 0.10`, min-qty 0.001, min-notional 50) plus `fapi/v1/klines` 1h microstructure probes (62,690 completed bars 2019-09-08→2026-11-02, forming bar dropped by closeTime, 12 fires → 12 opens / 12 closes; plant digests `e3b0c44298`/`6d0ae87e0c`/`c8ea0abc68`/`ae29ea0bc6`, signal digest `a89f066ec2`, window digest `a584b579f4`, sub-window digest `4077771dca`, prefix-equivalence proven), fetched live 2026-11-03
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged pinned package/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
- Closed family lineages (different sources/mechanisms, blockers structurally answered): PR #627 (`tradingview-harmonic-pulse-xabcd-close-bracket-two-sided-btcusdt-1h-2026-10-30.md`, spot-short NOT_LOSSLESS); PR #537 (`github-harmonic-pattern-cli-gartley-prz-long-flat-btcusdt-1d-2026-10-28.md`, warmup/ledger NOT_LOSSLESS)
- Nearest pool lineages (different mechanisms): `fibonacci-retracement-reclaim-long-btcusdt-1d-2026-10-10.md`; `fmz-fib-retrace-swing-tsl-level-long-flat-btcusdt-1d-2026-11-01.md`
