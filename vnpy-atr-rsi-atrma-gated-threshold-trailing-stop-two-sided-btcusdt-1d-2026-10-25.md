---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: vnpy AtrRsi ATR-MA-gated RSI-threshold trailing-stop two-sided on BTCUSDT 1d bars
created: 2026-10-25
updated: 2026-10-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-04
sources:
  - https://github.com/vnpy/vnpy_ctastrategy
  - https://github.com/vnpy/vnpy_ctastrategy/blob/c212d603e68a5f4dbbc160fe8f7f8b1e06be2494/vnpy_ctastrategy/strategies/atr_rsi_strategy.py
  - https://github.com/vnpy/vnpy
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# vnpy AtrRsi ATR-MA-gated RSI-threshold trailing-stop two-sided on BTCUSDT 1d bars

## Provenance

Primary sources read end to end and pinned during this cycle (2026-10-25):

- Strategy file (fetched live this cycle via the GitHub contents API at the pinned commit; local audit copy byte-identical, 3767 bytes, 145 lines, SHA-256 `b71ecf36e51e53dec8610c72680cd01435caad8b880869ae039f4111537dc1f0`): repository `https://github.com/vnpy/vnpy_ctastrategy`, exact file `vnpy_ctastrategy/strategies/atr_rsi_strategy.py`, class `AtrRsiStrategy` (`用ATR与RSI开仓，并用跟踪止损平仓的策略` — "open positions with ATR and RSI, close positions with a trailing stop"; author field `用Python的交易员`). File last-touch commit `c212d603e68a5f4dbbc160fe8f7f8b1e06be2494` (2026-10-04, `[Mod] 补全类型注解`, verified as the newest commit touching this path via the GitHub commits API this cycle; blob SHA `c31ea8a61769d7618cac50efefff9291bb1034b6`) — adopted as record `source_as_of`, never a fetch date. Frozen literals (file lines 22–27): `atr_length = 22`, `atr_ma_length = 10`, `rsi_length = 5`, `rsi_entry = 16`, `trailing_percent = 0.8`, `fixed_size = 1`. Derived thresholds (lines 64–65, `on_init`): `rsi_buy = 50 + rsi_entry = 66`, `rsi_sell = 50 - rsi_entry = 34`. Entry block (lines 103–111): `pos == 0` gate, then strict `atr_value > atr_ma`, then strict `rsi_value > rsi_buy` → `buy(close + 5, 1)` / strict `rsi_value < rsi_sell` → `short(close - 5, 1)` (mutually exclusive `if`/`elif`, never both). Trailing block (lines 113–125): long leg ratchets `intra_trade_high` and posts `sell(intra_trade_high * (1 - 0.8 / 100), stop=True)`; short leg mirrors with `intra_trade_low * (1 + 0.8 / 100)` and `cover(..., stop=True)`. Per-bar `cancel_all()` (line 91) with stop re-placement, `am.inited` gate (line 95), and live seed `load_bar(10)` (line 67).
- Indicator/operator semantics (fetched live this cycle): repository `https://github.com/vnpy/vnpy`, file `vnpy/trader/utility.py` at commit `c6e231caf32b7fc97e6459817fff66458cf7e7c4` (1304 lines): `ArrayManager.__init__(size = 100)` with `count`/`inited` (lines 511–515), `inited` flips only when `count >= size` (lines 529–531) — the strategy constructs a default `ArrayManager()`, so no evaluation exists before 100 bars by code; `atr(n)` delegates to `talib.ATR(high, low, close, n)` (lines 854–863); `rsi(n)` delegates to `talib.RSI(close, n)` (lines 884–893) — both canonical Wilder smoothing via TA-Lib. The `atr_ma` leg is a plain numpy `.mean()` over the last `atr_ma_length = 10` ATR values (strategy line 100), i.e. SMA(ATR(22), 10). The strategy repo declares `vnpy>=4.4.0` in `pyproject.toml` (a version range, fenced — the cited base semantics are verified at the fetched base SHA above).
- Licence and rights: the strategy repo is MIT-licensed (`pyproject.toml`, `license = {text = "MIT"}`). This record cites and normalizes the rule (single-line facts and formulas only for gate evidence) and reproduces no source block beyond single-line declarations.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the vnpy example. The file prints exact parameters, thresholds, gates, and trailing formulas, but ships no market, no timeframe, no fill semantics portable outside vnpy's live engine, and no cost concept. Researcher-declared adaptations are exactly six: (1) research market/timeframe `BTCUSDT` Binance USDT-M perpetual `1d` (the file names no market or timeframe — daily-bar CTA context with the `load_bar` day-seed is the stated rationale, never a source claim; perpetual is the minimal realistic venue because the short leg needs margin); (2) completed-bar decisions with same-bar-close market fills for entries and stop-cross exits (the file fires immediate marketable-limit orders at `close ± 5` intrabar with resting stop-markets intrabar — deviation class identical to the admitted chande-kroll, ut-bot, and nick-rypock records' bar-port, disclosed, never an advantage claim); (3) stop trigger ported from intrabar touch to completed-bar close-cross against the same ratcheted level (deviation disclosed; timing differs by construction, no equivalence claimed); (4) the `± 5` limit offset dropped (unmodelable price-unit microstructure on daily crypto bars — economics differ by construction, never claimed equivalent); (5) an adopted 110-completed-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 100-bar `ArrayManager.inited` gate, plus margin — see Required data); (6) house sizing/costs with modeled funding while held (the strategy file ships no fee, slippage, or funding concept — vnpy applies costs at its backtesting-engine level, never inside this file — never presented as zero-cost evidence). The `22/10/5/16 → 66/34` parameters, the strict comparisons, the `pos == 0` entry gate, the trailing `0.8%` formulas, the single-unit posture, and the no-signal-exit / no-reversal / no-target / no-time-exit posture are source-grounded and unmodified.

Pre-write dedup (2026-10-25): working-tree case-insensitive searches for `vnpy`, `ctastrategy`, `atrrsi`, `atr_rsi`, `AtrRsi`, `用Python的交易员`, and `trailing_percent` return zero strategy records — no admitted rule uses this source, author field, file, class, or trailing-percent construction. Open `research/*` PRs are only #353 (Heracles Keltner-Donchian band-ratio long-flat), #350 (ClucMay BB-discount EMA-gated long-flat), #331 (AdxSmas SMA-cross long-flat), #304 (forven CCI oversold-recross long-flat), #251 (Swift 2-year MA multiplier zone-state), #92 (SSL channel reversal), #89 (Chandelier dual-stop), #63 (SuperTrend flip), #49 (Gaussian StochRSI breakout), and #48 (Larry Williams 3-EMA streak) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class (see Negative evidence 6). This is a new family (first vnpy-sourced record in the pool), not a parameter variant.

## Economic mechanism

### Source-reported

Volatility-expansion-gated short-horizon RSI extremes with trailing-stop-only exits. The file's own one-line thesis is `用ATR与RSI开仓，并用跟踪止损平仓` — entries require volatility to be expanding (`ATR(22)` above its own 10-bar mean) and then buy `RSI(5)` strength above 66 or short `RSI(5)` weakness below 34; every exit is a `0.8%` trailing stop off the position's own extreme, re-posted each bar after `cancel_all()`. The file ships no behavioural, structural, or risk-premium mechanism beyond this measurement construction, and no fixed stop, target, or time leg of any kind.

### Research interpretation

Gate-plus-trigger-plus-ratchet machine, two-sided. Unlike pure RSI-threshold records (rsi-classic fires RSI(14) 30/60 long-only with signal closes and no gate, no stop), nothing here trades without the ATR-expansion vote — compressions are flat by construction. Unlike the calendar-anchored ATR-gated RSI record (turnaround-tuesday holds Monday-to-Wednesday on SMA30/RSI3/close-ATR with a time exit), there is no weekday, no moving-average level, no time exit, and the book is two-sided with stop-only exits. Unlike pure ATR trailers (ut-bot ratchets an ATR multiple off close with edge-flip reversal; nick-rypock ratchets a percentage channel with reversal; chandelier trails Donchian extremes) there is no always-in-market reversal — the ATR read gates entries only, never exits, and a stop-out returns the book to flat until a fresh signal. Unlike stop-band reversal records (chande-kroll, turtle-2N) the stop is a percentage of the trade's own extreme, not a band level, and crossing it flattens rather than reverses. The failure mode is plain: the carried-over `0.8%` trail is tight against daily-crypto volatility, so fresh entries can stop out on the next bar with no guardrail beyond the trail itself — disclosed, never tuned.

## Signal

Exact rule as pinned (`22/10/5/16 → 66/34/0.8%`, strict comparisons, single-unit — any other value is a different, unpinned rule):

- Inputs: `close`, `high`, `low` on completed `1d` bars. No `open` (except as fill price), no `volume`, no second asset or timeframe is read by any order-gating line (the file's `ArrayManager` carries volume arrays, but no leg of `AtrRsiStrategy` reads them).
- Indicators (base-pinned Wilder/TA-Lib): `ATR22[t] = talib.ATR(high, low, close, 22)[t]`; `ATRMA[t] = mean(ATR22[t-9..t])`; `RSI5[t] = talib.RSI(close, 5)[t]`. All reads reference the just-closed completed bar only.
- Entry, only from flat (`pos == 0` at bar start, file lines 103–111): if `ATR22[t] > ATRMA[t]` (strict — equality does not fire) and `RSI5[t] > 66` (strict) → long one unit; elif `RSI5[t] < 34` (strict) → short one unit. The `if`/`elif` makes the two legs mutually exclusive on every bar by code. Fill at the same bar's close, market, one single unit.
- Trailing exits, the sole exit path: while long, `H[t] = max(H[t-1], high[t])` (seeded at the entry bar's high, file lines 104/114) with level `L_long[t] = H[t] × (1 − 0.008)`; while short, `D[t] = min(D[t-1], low[t])` with level `L_short[t] = D[t] × (1 + 0.008)`. Exit the full unit at the same bar's close when `close[t] < L_long[t]` (long) or `close[t] > L_short[t]` (short) — the completed-bar port of the file's intrabar touch trigger (adaptation (3), disclosed). No opposite-signal exit exists anywhere: an opposite RSI print while positioned is a no-op by the `pos == 0` gate — reversal must never be assumed.
- Sequencing (source-code order, pinned): the entry bar evaluates the flat branch only, so no bar can both open and stop out — entry and exit are mutually exclusive on one bar by construction. After a stop-out the book is flat and re-arms on the next gated signal only (no cooldown specified — explicitly none, not invented). Pre-first-signal bars are flat.
- Direction: two-sided (long leg and short leg are both native). Shorts are native to USDT-M margin (no uptick rule, no borrow desk).
- Risk legs (pinned absence, not invented): no fixed stop beyond the trailing ratchet, no take-profit, no time exit — the file ships none, carried over exactly, disclosed in Provenance adaptation (6), never upgraded into a source claim.

## Required data

- Completed `1d` bars of BTCUSDT: `high`, `low`, `close` only (`high`/`low` feed ATR(22) and the intra-trade extremes; `close` feeds RSI(5) and both fills). No `open`, no `volume`, no funding-signal, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar-table, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (researcher choice — the file names no timeframe; no multi-timeframe call, no second feed).
- Warmup: 110 completed `1d` bars flat by record rule — structural minimum is the 100-bar `ArrayManager.inited` gate (base file lines 511–531; the strategy constructs a default manager and returns before evaluation until `count >= 100`), which already covers TA-Lib RSI(5)/ATR(22) seeding and the 10-value ATR mean; 10 bars of margin follow the admitted warmup-margin precedent. The file's `load_bar(10)` live-seed call is a non-gating engine convenience, fenced — the record's warmup rule alone governs. Missing bars are skipped on available completed bars only — prices are never fabricated. No repainting (all reads reference the just-closed bar), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance USDT-M perpetual under the house overlay (researcher choice — the file names no venue; vnpy CTA context is futures-generic; no source-market equivalence is claimed; perpetual is the minimal realistic venue because the short leg needs margin).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close market fills for entries and trailing-stop-cross exits — compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) on the same verified primitive as the admitted chande-kroll, ut-bot, and nick-rypock records' fills. This record claims no other fill convention: no `± 5` limit offset (adaptation (4)), no maker-touch, no queue, no intrabar-path-dependent fill. With at most one order event per bar and entry/exit mutually exclusive by construction, same-bar ordering is trivially the written event.
- Stop modeling: the ratcheted level is recomputed every bar from completed-bar extremes (the completed-bar equivalent of the file's per-bar `cancel_all()` plus stop re-placement); the trigger is the completed-bar close cross (adaptation (3)). No resting intrabar order, no touch-price fill, and no hidden Hummingbot stop-order default is relied upon.
- Sizing/capital/costs: the file ships no sizing beyond `fixed_size = 1`, and no capital, fee, slippage, margin, or funding concept (costs live at vnpy's backtesting-engine level, never in this file — recorded as an absent-economics stub, never as zero-cost evidence). The explicit house overlay (single-unit frame, pinned house taker fees both legs, modeled funding while held) applies to the derived evaluation here, never presented as source-native behavior. Funding is never zero-claimed: two-sided holds span the `00:00`/`08:00`/`16:00 UTC` funding stamps, so every held bar carries modeled funding.
- Concurrency: at most one single-asset engine position at any time; a stop-cross closes to flat in one step with no reversal leg. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no hedge-mode requirement by construction.

## Evidence

### Source-reported

With exact provenance (strategy file at pinned commit `c212d60`, blob `c31ea8a6`, read end to end this cycle): the `22/10/5/16/0.8/1` frozen literals (lines 22–27); the `66/34` threshold derivation (lines 64–65); the `pos == 0` gate with strict `ATR > MA` and strict `RSI > 66` / `RSI < 34` branches and `close ± 5` order prices (lines 103–111); the long/short trailing formulas with `stop=True` legs (lines 113–125); the per-bar `cancel_all()` (line 91); the `am.inited` gate (line 95); the `load_bar(10)` seed (line 67). With exact base provenance (vnpy base `vnpy/trader/utility.py` at `c6e231c`, read this cycle): the default 100-bar `ArrayManager` with the `count >= size` init gate (lines 511–531) and the TA-Lib `ATR`/`RSI` delegation (lines 854–863, 884–893). This record claims no source-reported performance number of any kind — the file ships no return, win rate, trade count, or table — and no reproduced performance exists.

### Independently reproduced

Not independently reproduced. A logic-synthesis self-check (Wilder RSI/ATR reimplementation in numpy over synthetic bars, completed-bar port semantics: strict gates, 66/34 branches, 0.8% ratchet, close-cross exits, entry-bar sequencing) executed this cycle and passed deterministically (`SELF-CHECK OK`: 24 events across 260 bars with all entry-gate asserts holding) — this is a state-machine synthesis check only, not a backtest, not TA-Lib parity (TA-Lib is not installed in this environment), and not performance evidence.

### Negative evidence

1. Fill deviation fenced, admitted plainly: the file fires immediate marketable-limit orders (`close ± 5`) with resting stop-markets intrabar. This record instead pins completed-bar same-close market fills with close-cross stop triggers — the same bar-port class as the admitted chande-kroll, ut-bot, and nick-rypock records, predeclared in Provenance adaptations (2)–(4). A reviewer must not cite the file as evidence for any intrabar, limit, touch-price, or next-open timing.
2. Timeframe and venue fenced: the file names no market or timeframe. `1d` BTCUSDT-perpetual is the disclosed researcher pin (Provenance adaptation (1)); a reviewer must not cite the file as evidence for any frame or venue.
3. No-signal-exit fenced: the `pos == 0` gate means an opposite RSI extreme printed while positioned changes nothing — the sole exit path is the trailing stop. A signal-flatten or reversal reading would contradict the coded gate and is explicitly not this record.
4. Dead-state fenced: inside the long branch the file overwrites `intra_trade_low` with the bar low (line 115) without reading it for the long stop (and mirrors `intra_trade_high` in the short branch, line 122) — provably inert state maintenance, carried as written, gating nothing.
5. `load_bar(10)` fenced: a live-trading history seed, not an evaluation gate — the record's 110-bar warmup rule alone governs; a reviewer must not shorten warmup to 10 bars.
6. Overlap fences, admitted plainly: pool `rsi-classic-level-reversal` trades RSI(14) 30/60 long-only with signal closes (no ATR gate, no stop, different RSI spec and book); pool `turnaround-tuesday` is a Monday-gated calendar hold with SMA30/RSI3/close-ATR legs and a Wednesday time exit (no trailing stop, long-flat spot); pool `ut-bot-atr-trailing-stop-flip` ratchets an ATR multiple off close with edge-flip always-in-market reversal (no RSI, no ATR-vs-MA gate, no flat state); pool `nick-rypock-trailing-reverse` ratchets a percentage channel with reversal (no ATR, no RSI); pool `chande-kroll-stop` reverses on Donchian-derived stop-band crosses under an ADX gate (reversal exits, no RSI, no ATR-vs-MA gate, no flat state); pool `turtle-system-2` breaks Donchian channels with 2N stops and half-N adds (no RSI, reversal-capable book); pool `rvi-swma-cross-ema-stack-atr-stop-target` enters on RVI/SWMA/EMA-stack crosses with ATR stop-plus-target (different signal, has a target); pool `bookstaber-atr-momentum-breakout` and `forven-atr-breakout-channel` enter ATR/channel breakouts (no RSI thresholds, no MA-of-ATR gate, no trailing-only exits); pool `triple-ema-volstop-tp` and `support-resistance-fractal-trailing-breakout` carry take-profit or fractal-anchored trails (different anchors, profit legs). Shared `RSI`/`ATR`/`trailing` vocabulary is not shared signal.
7. No hidden variants admitted: any other lookback, any other threshold pair, any smoothed or ranked gate, any fixed stop/target/time exit, any signal-flatten or reversal exit, any other frame, fill, venue, or book is a different, unpinned rule. A reviewer must not pick among these to rescue or reshape the record.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `22/10/5/16 → 66/34` / strict gates / `pos == 0` entry gate / `0.8%` ratchet with close-cross exits / stop-only exits / two-sided / `1d` BTCUSDT perpetual / same-bar-close fills are frozen.

- F1 — ATR-gate relevance: an RSI-only twin (same 66/34 thresholds and 0.8% trailing exits, ATR gate removed — same book, fills) must not improve net expectancy; fail ⇒ the volatility-expansion gate adds nothing over bare RSI-threshold trading.
- F2 — Trailing-exit relevance: an opposite-signal-flatten twin (same gated entries, but flatten the full unit on the opposite RSI threshold print instead of trailing — same book, fills) must not improve net expectancy; fail ⇒ the trailing ratchet adds nothing over signal-driven flattening.
- F3 — Threshold relevance: a 70/30 twin (same gate, same ratchet, same book, fills) must not improve net expectancy; fail ⇒ the pinned 66/34 carries no advantage over the neighboring round-number thresholds and the record's literal choice is arbitrary.

## Crypto portability

Pinned to BTCUSDT Binance USDT-M perpetual under the house overlay (declared port of a venue-free example file). The rule reads completed daily bars only, so no pit-session, gap, roll, split/dividend-adjustment, or corporate-action logic ports (CN-futures session specifics are a non-issue on the 24/7 tape — disclosed, not modeled). The `± 5` price-unit offset is dropped rather than ported (adaptation (4)). The rule is two-sided, so a spot-only deployment expresses only long-firing bars while short-firing bars stay venue-gated (never silently converted) — a spot-only variant would be a different, unpinned claim. No warmup history beyond 110 `1d` bars is consumed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Tight carried-over trail: `0.8%` off the trade extreme is tight against daily-crypto volatility — fresh entries may stop out on the very next bar with no other guardrail. This is the file's posture, disclosed as the record's principal risk, never tuned.
- No signal exit: adverse drift that never touches the ratchet is ridden until it does — the opposite RSI print alone changes nothing, disclosed.
- Gate blindness: compressions with `ATR22 <= ATRMA` suppress every entry even when RSI prints textbook extremes — the gate's silence is the coded trade, disclosed.
- Single-venue port residual: CN-futures-generic example vs Binance perpetual execution (prints, fees, funding, margin mechanics beyond the house model) is unclaimed, disclosed.
- Fill-port residual: same-bar-close fills with close-cross stop triggers differ bar-by-bar from the file's immediate-limit/resting-stop behavior — economics differ by construction, never claimed equivalent.
- Performance evidence is absent: nothing here is calibrated, fitted, or tuned to any backtest.
- Author scope: the file is a framework example strategy (`MIT`), not a vetted retail trading system — this record is research-only and claims no live suitability.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior and never part of this admission — no Safety-Order/DCA event is admitted in this record's version. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- vnpy `vnpy_ctastrategy` (MIT framework example — `AtrRsiStrategy` at `vnpy_ctastrategy/strategies/atr_rsi_strategy.py`, pinned to file last-touch commit `c212d603e68a5f4dbbc160fe8f7f8b1e06be2494` dated 2026-10-04: 22/10/5/16/0.8 literals, 66/34 derivation, strict gated entries, trailing-stop formulas, `pos == 0` gate — read end to end via contents API 2026-10-25): https://github.com/vnpy/vnpy_ctastrategy
- Same file at the pinned commit (formula and gate evidence): https://github.com/vnpy/vnpy_ctastrategy/blob/c212d603e68a5f4dbbc160fe8f7f8b1e06be2494/vnpy_ctastrategy/strategies/atr_rsi_strategy.py
- vnpy base `vnpy/trader/utility.py` at `c6e231caf32b7fc97e6459817fff66458cf7e7c4` (ArrayManager 100-bar default with init gate, TA-Lib Wilder ATR/RSI delegation, dependency `vnpy>=4.4.0` per strategy-repo `pyproject.toml` — read 2026-10-25): https://github.com/vnpy/vnpy
