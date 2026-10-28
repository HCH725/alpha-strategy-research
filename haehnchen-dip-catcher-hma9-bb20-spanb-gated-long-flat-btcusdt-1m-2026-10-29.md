---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Haehnchen DipCatcher HMA9-BB20 retracement cross spanB-gated long-flat on BTCUSDT spot 1m bars
created: 2026-10-29
updated: 2026-10-29
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-08-02
sources:
  - https://github.com/Haehnchen/crypto-trading-bot/blob/cb9563344a20ea7ac89ff214d350f141d1521219/src/strategy/strategies/dip_catcher/dip_catcher.ts
  - https://github.com/Haehnchen/crypto-trading-bot
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Haehnchen DipCatcher HMA/BB retracement-cross spanB-gated long-flat — independent BTC-USDT spot 1m derivative

## Provenance

**Primary public GitHub identity:** `Haehnchen/crypto-trading-bot` (open-source CCXT crypto trading bot, MIT, test-covered v2 strategy framework). File `src/strategy/strategies/dip_catcher/dip_catcher.ts`, class `DipCatcher extends StrategyBase` (the only class in the file; the companions are the option/interface/type declarations only). Pinned commit `cb9563344a20ea7ac89ff214d350f141d1521219` (committed `2026-08-02T09:15:51Z`; verified as the repository HEAD via `git ls-remote` this cycle — record `source_as_of` is that commit date, never a fetch date). File is 4966 bytes, 137 lines, SHA-256 `54e0bfb79c808aa9…`, git blob SHA `5f4e7c24efb9813dcc558d78e1158761d70a58a3` (both computed over the raw bytes fetched at the pinned commit — the entire file was read, not sampled).

**The file's own words (quoted for gate evidence, never extended):** header comment `Long: HMA(low) crosses above BB lower when Ichimoku trend is bullish` / `Short: HMA(high) crosses below BB upper when Ichimoku trend is bearish` / `Close: Opposite crossover occurs while in position`. Description string `HMA/BB retracement catcher with Ichimoku cloud trend filter`. Defaults `trend_cloud_multiplier: 4`, `hma_high_period: 9`, `hma_high_candle_source: 'close'`, `hma_low_period: 9`, `hma_low_candle_source: 'close'`, `hma_length: 9`, `bb_length: 20` — no hyperopt, no hidden branch. A flat book opens only on the band-cross side the spanB gate permits; a positioned book closes on either crossover leg (`signal.close()`, no `return` needed — co-print is mathematically impossible, see Signal).

**Out-of-file calls pinned (all read at the pinned commit):** `src/utils/indicators.ts` (28779 bytes, 883 lines, git blob `89fb6768e1177c8553be4930aae4b13f66968d94`) computes `hma` by hand-rolled causal rolling WMA (`calculateWMA`, L324–337; `hma` L512–532: `halfPeriod=floor(p/2)`, `sqrtPeriod=floor(sqrt(p))`, default length 9, default source `'close'`), `bb` via npm `talib` `BBANDS` on the close series (`length`, `stddev` default 2, `optInMAType: 0` SMA; L365–391), and `ichimoku_cloud` via npm `technicalindicators` `IchimokuCloud` on candle high/low (`conversionPeriod 9*m`, `basePeriod 26*m`, `spanPeriod 52*m`, `displacement 26*m`; L822–840). `package-lock.json` pins `technicalindicators` at exactly `3.1.0` (npm gitHead `7740f17cf681a2b1ace3009f5f396c14cbadf1f1`); the 3.1.0 `IchimokuCloud` generator was read line-for-line this cycle: warmup `period=max(36,104,208,104)=208`, the forward-displacement shift is commented out so `spanB[t]` is the trailing-208-bar `(highest high + lowest low)/2` ending at `t` — fully causal, no future read. `src/modules/strategy/v2/indicator_calculator.ts` (2411 bytes, 63 lines) feeds every non-`sourceCandle` indicator `candles.map(c => c.close)`; `hma` and `ichimoku_cloud` are in the `sourceCandle` list while `bb` is absent — so both HMA legs read the close series (defaults `'close'`), BB reads closes, and the cloud reads high/low. Results are null-padded to candle alignment. `src/modules/strategy/v2/typed_backtest.ts` (450 lines) enforces ascending candles, pushes the current bar's indicator values into the accumulated arrays *before* executing with `price = candle.close`, and clears position state on `close`. `src/strategy/strategy.ts` (269 lines) fixes `isFlat()` as lastSignal undefined-or-`'close'`, `getIndicatorSlice(key, n)` as the last `n` accumulated values including the current bar, and `goLong/goShort/close` as pending-signal setters that never mutate the in-execution flat state. `src/modules/services.ts` (635 lines) imports `DipCatcher` (L68) and registers it in the runnable v2 strategy registry (L582–591) — not an orphan file. The unit test `test/modules/strategy/v2/strategies/dip_catcher.test.ts` (5842 bytes, 161 lines, git blob `1a972f5325000d01f2a9b06b845e80b780a5239e`) pins the filed defaults (`trend_cloud_multiplier 4`, both HMA periods 9, `hma_length 9`, `bb_length 20`, description string), asserts ascending-order rejection and a <30% snapshot signal rate on the `btc-usdt-15m` fixture — disclosed as fixture only, never adopted as the record frame. No `volume` column is read by any gating line.

**Full-file token census (verified over the 137 lines this cycle):** 1 `goLong` / 1 `goShort` / 2 `signal.close` (the complete action set); 0 `stop` / 0 `trailing` / 0 `target` / 0 `volume` / 0 `shift` / 0 `request` / 0 `security` / 0 `hyperopt` / 0 `position_avg_price` / 0 `position_size` / 0 `leverage` / 0 `funding` / 0 order-placement calls. `isFlat` (4) is exactly the two entry guards plus the two close guards; the destructured `lastSignal` (L94) is a dead read that conditions nothing — disclosed, not repaired.

**Declared independent derivative v1, NOT source-native/lossless:** this record specifies a separately identified derived executable strategy. Researcher-declared adaptations are exactly six, all predeclared here and repeated in their sections: (1) research market Binance BTC-USDT **spot** (the source names no market); (2) research timeframe **`1m`** (the source is timeframe-agnostic; the dir README's `"period": "15m"` suggestion and the unit-test fixture are disclosed and never adopted); (3) **long/flat only — the source short arm (`goShort` on the upper cross while bearish) is explicitly disabled** in this book, so long-side economics differ from the two-sided source and nothing here is evidence the source passes unchanged; (4) completed-bar decisions with **same-bar-close MARKET fills** (matches the source backtester's own close-price convention); (5) fixed 0.001 BTC single-unit/no-add/no-cooldown position pin against a 10000 USDT research cash pin, with a 208-bar researcher warmup floor; (6) hypothetical 0.0002/side cost pin with spot (funding-N/A) accounting **plus an explicitly frozen no-quantization synthetic precision model** (see Execution assumptions). Every threshold, lookback, indicator length, source string, gate polarity, and edge polarity is source-verbatim.

**Immutable research identity:** `Haehnchen-dipcatcher-cb95633 | derived-v1-longflat | BTC-USDT-binance-spot-1m | HMA9close-x-BB20lower-spanB208gate | samebar-close-0.001BTC | 2026-10-29`. Changing any component changes the derivative identity.

**Pre-write dedup (2026-10-29):** working-tree base is current `main@920333d3` (425 root strategy records, README pool count 425, every record verified `hb_ready_status: PASS` — zero non-PASS files). No `haehnchen-dip*` / `haehnchen-dca*` / `dip-catcher` / `dca-dipper` record exists (only the admitted `haehnchen-cci`, `haehnchen-ccimacd` and `haehnchen-macd` siblings). All ten open `research/*` PRs examined by branch and title (#48, #49, #63, #89, #92, #251, #304, #331, #350, #353) — none uses this file or rule; open PR #350 (ClucMay BB-discount EMA-gated 5m) gates BB penetration with an EMA, never an HMA9 band-cross with a spanB gate. Nearest families are materially different constructions: `forven-hma-cross` (bare HMA9×HMA21 cross, no band, no cloud gate, 1h); `haehnchen-macd-histogram-cross-hma-sma` (MACD-led sibling, different leading leg); `quantsplaybook-price-volume-resonance-hma-dual-threshold` (dual-threshold, no band cross, no cloud); `freqtrade-low-bb-98-sub-band-dip-close-bracket` (1m BB20-population touch-dip `C<=0.98*lower` with a ±% price bracket — touch, not cross; no HMA; no gate; signal-exit absent); `freqtrade-bband-rsi-dip-buy` (BB+RSI, no HMA, no cloud); `forven-ichimoku-tenkan-kijun-cross-cloud-gated` (tenkan/kijun cross, no HMA/BB legs); `truetstrategy-ichimoku-cloud-ema50-stochrsi` (cloud+EMA50+StochRSI, no HMA/BB cross). None conjoins an HMA9(previous,current)-vs-BB20-band cross-up with an HMA9-vs-spanB(36/104/208) trend gate and an opposite-crossover close. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: catch a dip/retracement by buying the HMA9's reclaim above the lower Bollinger band strictly while the tape reads bullish — HMA9 above Senkou Span B on ×4 Ichimoku geometry — then surrender the long the moment either band-cross prints against the position. The dir README prose (`HMA (source: candle low)`, `higher timeframe (4x multipler)`, `"period": "15m"`) is disclosed and deliberately not adopted: the executable code defaults both HMA sources to `'close'`, runs every leg on one timeframe with zero `request`/`security` calls, and names no market. No behavioural, structural, or risk-premium channel is claimed anywhere in the 137 lines.

### Research interpretation

A gate-kept band-reclaim dip buyer, long-only. Unlike bare BB-touch dip records that buy every band tag including waterfall tags in dead tape, the strict cross-up edge vetoes any bar whose HMA never left the band — the reclaim is necessary, never the touch. Unlike single-gate records, the spanB veto reads the tape as bid only while the fast Hull average holds above the slowest Ichimoku extreme-midpoint — a reclaim printed under the cloud is left alone. The exit is deliberately symmetric-impatient: the same-side reclaim that would re-fire an entry on a flat book instead closes a long book (no pyramiding by construction), and the upper-band cross closes from above. The coded consequence is a buyer of cloud-permitted HMA recoveries off the lower band, harvesting only the next crossover print — with no stop, no target, no clock.

## Signal

Exact rule as pinned (any other HMA length, BB length, cloud multiplier, source string, gate polarity, fill, frame, book, or tie treatment is a different, unpinned rule). All identifiers below are the program's own:

```text
HMA(s,9)[t]  = WMA( 2*WMA(s,4) - WMA(s,9), 3 )[t]     // hand-rolled causal rolling WMA, first value bar 10
BB20[t]      = talib BBANDS(close, 20, 2, 2, SMA)     // lower[t], upper[t]; first bands bar 19
spanB[t]     = (highest high[t-207..t] + lowest low[t-207..t]) / 2   // technicalindicators 3.1.0, first value bar 207
X[t]         = HMA(close,9)[t]                        // hma_high, hma_low and hma are the SAME print by default
isLong[t]    = X[t] > spanB[t]                        // strict; equality reads bearish
longCross[t] = (X[t] > lower[t]) AND (X[t-1] < lower[t-1])     // strict reclaim, both bars
shortCross[t]= (X[t] < upper[t]) AND (X[t-1] > upper[t-1])     // strict mirror
entry[t]     = FLAT AND isLong[t] AND longCross[t]
exit[t]      = LONG AND (longCross[t] OR shortCross[t])        // source close arms, long book only
```

- Trade events: `entry` opens the full 0.001 BTC on a flat book; `exit` closes it in full. No pyramiding, no averaging, no partial — a positioned book closes (never re-enters) on a fresh same-side reclaim, and the flat book ignores cross bars that fail the gate (the disabled short arm is a no-op without a short book — disclosed, not repaired).
- Exact boundaries (pinned semantics): every comparison is strict — touches fire nothing on any leg (`X==lower`, `X==upper`, `X==spanB` all hold). The `14`-free literal set `9 / 20 / 36 / 104 / 208 / 104 / 2σ` is never tuned here.
- Single-print disclosure (verified, not assumed): with filed defaults both band-cross legs read the identical HMA9-on-close series against different bands — any non-`'close'` source option is a different, unpinned rule. The `hma` (gate) leg is likewise HMA9-on-close by construction (no source option exists on it).
- Mutual-exclusion proof (verified, not assumed): `longCross` and `shortCross` can never co-print — both need `lower[t-1] > X[t-1] > upper[t-1]`, i.e. an inverted band (`lower > upper`), impossible since `upper - lower = 4σ >= 0`. The source's missing `return` between the two close arms therefore orders nothing; at most one leg fires per bar and close+close is unreachable. Entry-vs-exit exclusivity follows from the position pin (flat → entry-only, positioned → exit-only, never a round-trip).
- Same-side-close fenced (verified, disclosed not repaired): a fresh `longCross` on a LONG book closes it — entries while positioned are impossible and re-entry needs the next qualifying reclaim after the close bar. No cooldown exists in source — explicitly none, not invented.
- Null-guard fenced: any leg with fewer than the required non-null values returns silently — pre-seed bars print nothing and hold flat (front null-padding with tail alignment; no `fillna` exists to smear seeds forward).
- Direction: long-only derived book. The source short arm exists and is **explicitly disabled here** — a two-sided reading of this record would contradict it. The long-only book expresses unchanged on a spot venue with no naked shorting (see Crypto portability).
- Exits and risk (explicit): the opposite-crossover close is the complete position-closing set. No stop, no target, no trailing, no breakeven move, no time exit, no forced end-of-data liquidation — **all explicitly absent** (source-faithful: the census proves none ships), never to be added by repair. Indefinite holds are possible and disclosed.
- Position rule (predeclared researcher pin mirroring source structure): single 0.001 BTC unit against a 10000 USDT research cash pin, at most one open position; re-entry re-arms on the next completed bar printing a fresh `entry` after any exit (no cooldown — explicitly none, source has none); pre-warmup bars are flat by record rule. A pending order prohibits additional actions.
- Determinism note for the reviewer: the rule reads only completed-bar high/low/close with fixed non-negative offsets (trailing WMA folds, talib BBANDS window, trailing 208-bar span window, one-bar cross lookbacks — no forward reference) — no volume, funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, informative merge, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. The `Math.round` calls feed `debugAll` cosmetics only and condition nothing. The dead `lastSignal` destructure conditions nothing. The source backtester's per-completed-candle step is the file's own framework contract.

## Required data

- Completed `1m` bars of BTCUSDT spot: `high`/`low` for the spanB leg, `close` for both HMA legs, the BB leg and the gate comparison. No `open`, no volume, funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (the dir README's `higher timeframe` prose has no code path — single frame by construction).
- Single decision timeframe `1m` (researcher pin — the source is timeframe-agnostic; its test-fixture and README-suggested timeframes are not adopted). One evaluation per completed bar; every window reads the decision bar and its causal past only; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 208 completed one-minute bars held flat (bars 0–207, ~3.5 hours). Covers the spanB seed (first value bar 207), the BB20 seed (bar 19), the HMA9 seed (bar 10), and the two-bar cloud slice with margin; first eligible decision at zero-based bar 208. Coded behaviour underneath: pre-seed library outputs are null and the file filters nulls (short slices return early — no leg can fire early; no `fillna` exists to smear seeds forward). The cloud feed's internal last-1000-candle slice is behaviour-neutral (the 208-bar span window is always contained, and front null-padding keeps tail alignment exact). No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance **spot** under a fixed-size research pin (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed). No leverage, no margin, no funding.
- Order timing (derived, disclosed): completed-bar decision with **same-bar-close MARKET fills** — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted spot-1m siblings use. This mirrors the source backtester's own close-price convention (`price = candle.close` per completed candle). No maker-touch, queue, or intrabar-path-dependent fill: entry and the crossover exit are both bar-close-evaluated; the co-print impossibility proof leaves no ambiguous same-bar fill order to the engine beyond the disclosed position pin.
- Interval precedent (exact, disclosed): the admitted spot-1m siblings on `main` bound the verified path to Binance **spot**, leverage 1, fixed 0.001 BTC, `OrderExecutor` MARKET / `POSITION_HOLD`, and hypothetical `trade_cost=0.0002` per side — this record rides that same specified single-frame completed-bar `1m` Binance spot candle path, not an assumed one. Pinned engine source re-verified line-level at `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` this cycle: `hummingbot/VERSION=dev-2.17.0`; `BinanceSpotCandles` supports `1m` (default interval `1m`), maps REST Kline row[0] to the **open** timestamp and row[1..5] to OHLCV; `BacktestingDataProvider.get_candles_feed` requests `start_time - max_records*interval` while `get_candles_df` trims to `start_time..end_time` (controller must inspect the actual raw buffer before trimming and reject gaps/short history); `BacktestingEngineBase.prepare_market_data` joins controller features with backward `merge_asof` on raw candle-opening timestamps and overwrites row `timestamp` with the candle-open value; `OrderExecutorSimulator` fills MARKET at the **first supplied actual candle close** (`filled_amount_quote=Q*close`, `cum_fees_quote=trade_cost*filled_amount_quote`) ending `CloseType.POSITION_HOLD`; `OrderExecutorConfig(connector_name/trading_pair/side/amount/OPEN-CLOSE/MARKET/price=None/leverage=1)`; `BacktestPositionHold` nets BUY/SELL base inventory with matched gross PnL and separate fee tracking. Decision/availability timestamps, fills, and costs ride the same specified path. The strategy-specific controller (not yet implemented) must calculate the exact HMA/BB/spanB state and perform close-availability gating — the generic executor does not calculate the strategy. Spot funding is **not applicable**, never fabricated as futures zero. This Scout did not independently rehash the pinned wheel or re-run the representative engine validation — reuse of the verified path only (#414 representative primitive, no novel execution primitive), stated so the reviewer need not guess. The `20260920` package string is retained as a label only; no package-to-commit mapping is invented.
- Precision/quantization (frozen researcher model — nothing left to implementation choice): **unquantized synthetic fills**. Every entry buys exactly 0.001 BTC at the observed decision-bar close and every exit sells exactly that 0.001 BTC at its observed close; no lot-size rounding, no tick rounding, no partial fills, no order rejection, no min-notional gate, no residual dust — residual quantity is zero by construction after every exit. There is no second quantity, price, or residual rule to choose later; any venue-real quantization would be a different, unpinned rule. A missing or non-finite close never supplies a substitute fill or mark price — invalid or absent prices stop the run (the pinned `get_price_by_type` `Decimal("1")` missing-price fallback is explicitly prohibited here).
- Sizing/capital/costs: the source ships no sizing, capital, fee, or funding concept — sizing and costs ride an explicit fixed-size pin (0.001 BTC against 10000 USDT research cash, leverage 1, hypothetical 0.0002 each side: `cum_fees_quote = trade_cost*amount*observed_close`), never presented as source-native behaviour. One round trip of 0.001 BTC: gross `0.001*(sell_close-buy_close)`; explicit research net `gross - 0.0002*0.001*(buy_close+sell_close)`. No slippage/spread modeled — not evidence of zero real slippage.
- Concurrency: at most one position at any time; the entry opens the full unit on a flat book; either crossover exit closes it in full; re-entry after an exit needs only the next qualifying entry bar (no cooldown — explicitly none). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. Safety orders/DCA are explicitly disabled. A pending order prohibits additional actions. An end-of-sample LONG is marked at the last real valid close, not closed with an invented fill (differs from the source backtester's end-of-data handling — disclosed derivation, never a fill claim).
- Price integrity: validate every observed finite positive high/low/close before order creation; a missing-pair price fallback must never supply a substitute fill or mark price. Invalid or absent prices stop the run, not manufacture fills. No data source or engine ability is inferred merely from a supported interval or class name.

## Evidence

### Source-reported

The file ships the full construction (137 lines: the header contract, the seven-field default block, the five-indicator wiring, the gate-plus-cross state machine, and the `DipCatcher` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance. The dir README's `candle low` / `higher timeframe` / `15m` prose is quoted above and deliberately not adopted — code defaults govern.

### Independently reproduced

Not independently reproduced. No backtest was run for this admission; HB_READY here is an engine-capability check, not a profitability result.

### Negative evidence

1. Leading-window behaviour fenced: pre-seed library outputs are null and filtered (short slices return early — no leg can fire early; no `fillna` exists to smear seeds forward). The 208-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rules fenced: every gating comparison is strict — touches on either band, on spanB, or on either cross bar fire nothing; the gate reads bearish on exact equality — disclosed, not smoothed.
3. SpanB causality fenced (verified in library source, not assumed): `technicalindicators@3.1.0` computes spanB over the trailing 208-bar high/low window ending at the current tick; the forward-displacement shift is commented out of the pinned library, so no future bar enters any print. The internal last-1000 slice is behaviour-neutral (window containment plus tail-exact null-padding).
4. Edge exclusivity fenced (verified, not assumed): the two cross legs need jointly inverted bands to co-print — impossible since `upper - lower = 4σ >= 0`. The source's missing inter-arm `return` orders nothing; the position pin resolves every residual (flat → entry-only, positioned → exit-only, never a same-bar round-trip).
5. Same-side-close fenced: a fresh reclaim cross on a LONG book closes rather than compounds — disclosed, not repaired; re-entry needs the next independently qualifying bar.
6. Zero-variance fenced: flat tape pins HMA onto the flat line, BB bands collapse onto it (crosses need strict breaks a flat print cannot make), and spanB onto it (gate needs strict above) — no signal on constant series. No division by zero exists anywhere in the gating path (the BB width division feeds a diagnostic field only, never a predicate) — disclosed, not repaired.
7. No-protection fenced: the census proves zero stop/target/trailing/time machinery ships — positions rely solely on the crossover close and may be held indefinitely; this record adopts that fate explicitly and no reviewer repair may add protection.
8. Derivation-effect fenced: apart from the six declared adaptations (spot market, 1m frame, disabled short arm, same-bar-close fills, fixed-size/warmup pins, hypothetical costs with frozen precision), this record computes no behaviour differently from the file's letter — HMA/BB/cloud lengths, sources, thresholds, gate polarity, and both edges are verbatim; no reviewer invention is needed to execute it.
9. Cousin records fenced as different constructions (none conjoins an HMA9-vs-BB20 cross-up with an HMA9-vs-spanB gate): the bare HMA-cross sibling (no band, no gate), the MACD-led HMA sibling (different leading leg), the dual-threshold HMA sibling, the touch-dip bracket siblings (touch not cross, price bracket not signal exit, no gate), and the tenkan/kijun and cloud-composite Ichimoku siblings (no HMA/BB legs). Not a threshold re-tuning of any of them.
10. Sibling-file fence: every other strategy file in the source repository is a separate pin — its constants must never be substituted into this record. The `btc-usdt-15m` unit-test fixture is test data only, never the record frame.
11. Source-limitation fence: the repository self-describes as not production ready; no performance, robustness, or deployability claim is adopted from it.
12. Derivation boundary fenced: the non-source-native behaviours in this record are exactly the six declared adaptations — all predeclared above. The HMA9 prints, BB20 bands, spanB gate, both cross edges, and long-side entry conjunction are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: HMA lengths / BB length / cloud multiplier / close sources / gate polarity / disabled short arm / single-unit long-only / `1m` BTCUSDT spot / same-bar-close fills / frozen precision model are frozen.

- F1 — Gate relevance: dropping the spanB gate (same HMA/BB cross entry, same exit) must not improve net expectancy; fail ⇒ the cloud gate adds nothing over the ungated reclaim edge.
- F2 — Reclaim relevance: replacing the cross-up entry with a bare band-touch entry (same gate, same exit) must not improve net expectancy; fail ⇒ the reclaim adds nothing over the touch-dip.
- F3 — Exit relevance: replacing the opposite-crossover exit with a band-midline exit (same entry, same gate) must not improve net expectancy; fail ⇒ the crossover exit adds nothing over the midline exit.

## Crypto portability

Binance BTC-USDT spot 1m only, under this record's identity. No leverage, funding, or margin; porting to another spot pair/timeframe is a new identity, not covered here. The long-only book needs no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape. The spanB leg reads high/low and the HMA/BB legs read close; no exotic feed is required.

## Limitations

- TA-Lib BBANDS internals (SMA seeding over the first 20 bars) and `technicalindicators@3.1.0` generator internals live in their libraries outside the pinned file — pinned by call with the filed lengths, not re-derived; seeding effects sit under the disclosed 208-bar floor.
- Researcher-chosen (not source-native): Binance BTC-USDT spot market, 1m frame, disabled short arm, same-bar-close fill convention, 0.001 BTC size against 10000 USDT research cash, 208-bar warmup, 0.0002/side hypothetical cost, frozen unquantized synthetic precision model, next-bar re-arm with no cooldown, end-of-sample mark (not close). No historical backtest statistics reproduced; no Qlib parity, survivor label, trading approval or deployment. Before mass Qlib screening, any *new* execution primitive/data requirement must receive representative Qlib/Hummingbot event-level parity; strategy-specific final HB certification is downstream.
- The unit-test fixture timeframe, the dir README prose suggestions, and the repository's non-production self-description constrain nothing in this record and license nothing beyond it.

## Implementation status

`not-implemented`: no controller, config, or Qlib recipe ships with this record. Downstream materialization via `IMPLEMENTATION_NEEDED` only, never a second admission flag.

## Adoption boundary

`research-only` / `not-approved`. PASS here admits the declared derivative to model-consistent research; it authorizes no Paper/Testnet/Live trading.

## Related Wiki records

None.

## Sources

- https://github.com/Haehnchen/crypto-trading-bot/blob/cb9563344a20ea7ac89ff214d350f141d1521219/src/strategy/strategies/dip_catcher/dip_catcher.ts
- https://github.com/Haehnchen/crypto-trading-bot
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned Hummingbot source inspected via connected GitHub.
- https://github.com/HCH725/alpha-strategy-research/pull/414 — prior independent pinned wheel/source and MARKET-close primitive evidence.
