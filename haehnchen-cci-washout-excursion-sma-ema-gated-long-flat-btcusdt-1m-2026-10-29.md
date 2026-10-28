---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Haehnchen CCI washout-excursion SMA-EMA-gated long-flat on BTCUSDT spot 1m bars
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
  - https://github.com/Haehnchen/crypto-trading-bot/blob/cb9563344a20ea7ac89ff214d350f141d1521219/src/strategy/strategies/cci.ts
  - https://github.com/Haehnchen/crypto-trading-bot
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Haehnchen CCI washout-excursion SMA-EMA-gated long-flat — independent BTC-USDT spot 1m derivative

## Provenance

**Primary public GitHub identity:** `Haehnchen/crypto-trading-bot` (open-source CCXT crypto trading bot, MIT, test-covered v2 strategy framework). File `src/strategy/strategies/cci.ts`, class `Cci extends StrategyBase` (the only class in the file; the companions are the option/interface/type declarations only). Pinned commit `cb9563344a20ea7ac89ff214d350f141d1521219` (committed `2026-08-02T09:15:51Z`, message `Update to typescript 7`; verified as the repository HEAD via `git ls-remote` this cycle — record `source_as_of` is that commit date, never a fetch date). Git blob SHA `0a71d6df28a852fa71bd1893cd458b3de0d931ce` (matches the GitHub tree entry for this path at the pinned commit), size 3828 bytes, 118 lines, SHA-256 `26d430fd549c2899c6082d8e4e86bbd0c0631a35bf2fe47ccc3d9ae223a0f82b`; the raw file fetched at the pinned commit reproduces that blob via `git hash-object` — the entire file was read, not sampled.

**The file's own words (quoted for gate evidence, never extended):** header comment `Long: CCI crosses above -100 from below (after reaching -200) when price > SMA200 or EMA200` / `Short: CCI crosses below 100 from above (after reaching 200) when price < SMA200 and EMA200` / `Close: CCI reverses from overbought/oversold zone`. Defaults `cci_length: 14`, `sma_length: 200`, `ema_length: 200` — no hyperopt, no hidden branch. A flat book opens only when the regime side agrees and the oversold crossing carries a proven −200 washout inside the live window; a positioned book closes on the overbought/oversold reversal against it (`signal.close()` with `return`, so no entry fires on a close bar).

**Out-of-file calls pinned (all read at the pinned commit):** `src/utils/indicators.ts` computes `cci` via TA-Lib `CCI` on candle `high`/`low`/`close` (`inputs: ['high', 'low', 'close']`, filed length passed as `optInTimePeriod`); `sma`/`ema` via TA-Lib `SMA`/`EMA` on the close series — `src/modules/strategy/v2/indicator_calculator.ts` feeds every non-`sourceCandle` indicator `candles.map(c => c.close)`, and `sma`/`ema` are absent from the `sourceCandle` list while `cci` is present. Results are null-padded to candle alignment (`Indicator values are null during warmup period`). `src/modules/strategy/v2/typed_backtest.ts` steps one strategy execution per ascending completed candle with `price = candle.close` (`context.price`), pushes the current bar's indicator values into the accumulated arrays *before* executing (so slices read the current completed bar plus its causal past), and clears position state on `close` (`lastSignal = undefined`). `src/modules/services.ts` imports `Cci` (L64) and registers it in the runnable v2 strategy registry (L583) — not an orphan file. The unit test `test/modules/strategy/v2/strategies/cci.test.ts` pins the filed defaults (`cci_length 14`, `sma_length 200`, `ema_length 200`), asserts no signals in the first 30 fixture bars, and runs the `btc-usdt-15m` fixture — disclosed as fixture only, never adopted as the record frame. No `volume` column is read by any gating line.

**Full-file token census (verified over the 118 lines this cycle):** 1 `goLong` / 1 `goShort` / 1 `signal.close` (the complete action set); 0 `stop` / 0 `trailing` / 0 `target` (no protective machinery of any kind — disclosed absence, never repaired); 0 `volume` / 0 `shift` / 0 `request` / 0 `security` / 0 `typical_price` / 0 `position_avg_price` / 0 `position_size` / 0 `leverage` / 0 `funding` / 0 `hyperopt`. The `long` / `short` tokens are exactly the direction plumbing (header comment, `isLong`, `lastSignal` comparisons, the two entries, the close arms) — no second leg hides anywhere.

**Declared independent derivative v1, NOT source-native/lossless:** this record specifies a separately identified derived executable strategy. Researcher-declared adaptations are exactly six, all predeclared here and repeated in their sections: (1) research market Binance BTC-USDT **spot** (the source names no market); (2) research timeframe **`1m`** (the source is timeframe-agnostic; its unit-test fixture is `btc-usdt-15m` data, disclosed as fixture only, never adopted as the frame); (3) **long/flat only — the source short arm (`before >= 100 && last <= 100` with a +200 excursion while below both averages, `goShort`) is explicitly disabled** in this book, so long-side economics differ from the two-sided source and nothing here is evidence the source passes unchanged; (4) completed-bar decisions with **same-bar-close MARKET fills** (matches the source backtester's own close-price convention); (5) fixed 0.001 BTC single-unit/no-add/no-cooldown position pin with a 200-bar researcher warmup floor; (6) hypothetical 0.0002/side cost pin with spot (funding-N/A) accounting **plus an explicitly frozen no-quantization synthetic precision model** (see Execution assumptions — quantities, prices and residuals leave nothing to implementation choice). Every threshold, lookback, indicator length, regime comparison, excursion depth, and edge polarity is source-verbatim.

**Immutable research identity:** `Haehnchen-cci-cb95633 | derived-v1-longflat | BTC-USDT-binance-spot-1m | cci14-excursion200-sma200-ema200 | samebar-close-0.001BTC | 2026-10-29`. Changing any component changes the derivative identity.

**Pre-write dedup (2026-10-29):** working-tree base is current `main@646a93b0` (416 root strategy records, README pool count 416, every record verified `hb_ready_status: PASS` — zero non-PASS files). No `haehnchen-cci*` record exists (only the admitted `haehnchen-ccimacd` and `haehnchen-macd` siblings). All ten open `research/*` PRs examined by branch and title — none uses this file or rule. Nearest families are materially different constructions: `haehnchen-ccimacd` (CCI40 ±150 twelve-bar window + MACD-histogram 5L/5R pivot + ADX veto + SMA400 — no −200 excursion, no dual-MA OR-gate, different exit); `cci-threshold-extreme-reversal` (4h two-sided bare CCI20-on-close ±100 cross with a one-bar ±200 turn leg, no excursion-depth proof, no regime gate, opposite-signal exits); open PR #304 forven-CCI (1h bare CCI20 typical-price ±100 recross with no excursion and no gate, perpetual house overlay — this record adds the −200 washout proof plus the SMA/EMA OR-gate, a different signal); `cci-ema-rsi-cross-trailing-stop` (trailing engine-state exit, different construction); `freqtrade-swinghightosky-cci-rsi` / `freqtrade-strategy004-adx-cci-dual-stoch` (RSI/stoch co-gates, no excursion); `freqtrade-macd-cci-dip-state` / `freqtrade-macd-cross-cci-edge` (MACD-led, CCI is a secondary gate). None conjoins a CCI −100 recross-up carrying a proven −200 washout with a price-vs-SMA200/EMA200 OR-gate and an overbought-reversal exit. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the CCI's return above −100 only after the tape has proven a −200 washout inside the live window, and only on the side the slow averages permit — price at or above either the SMA200 or the EMA200 — then surrender the long the moment the CCI reverses down out of overbought territory. No behavioural, structural, or risk-premium channel is claimed anywhere in the 118 lines; the repository README self-describes the bot as not production ready (adopted as a limitation, never as a rule).

### Research interpretation

A regime-permitted washout-reversal buyer, long-only. Unlike bare CCI-recross records that buy every −100 return including shallow wobbles in dead tape, the −200 excursion proof vetoes any entry whose oversold dip never reached genuine washout depth — the crossing is necessary but never sufficient. Unlike single-average gate records, the OR-gate reads the tape as bid as long as *either* slow average confirms — a price pinned between a flat SMA200 and a rising EMA200 still arms, while a price under both is left alone. The exit is deliberately impatient at the top but patient everywhere else: no stop, no target, no clock — a long whose CCI never reaches overbought is held (the close arm needs the `before > 100` print, not the regime), and an underwater long whose CCI keeps printing below +100 is held, not forgiven. The coded consequence is a buyer of proven-washout CCI recoveries inside average-confirmed tape, harvesting only overbought reversals.

## Signal

Exact rule as pinned (any other CCI length, average length, threshold, excursion depth, gate polarity, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own:

```text
CCI[t]    = TA-Lib CCI(high, low, close; timeperiod 14)
SMA200[t] = TA-Lib SMA(close, 200)
EMA200[t] = TA-Lib EMA(close, 200)
price[t]  = close[t]
isLong[t] = (price[t] >= SMA200[t]) OR (price[t] >= EMA200[t])
win[t]    = last up-to-4 non-null CCI values ending at t   // getIndicatorSlice('cci', 4), nulls filtered
before    = win[t][-2]; last = win[t][-1]
washout   = min over the contiguous run of win values < -100 ending at `before` is <= -200
entry[t]  = FLAT AND isLong[t] AND (before <= -100) AND (last >= -100) AND washout
exit[t]   = LONG AND (before > 100) AND (last < 100)   // source close() arm, long book only
```

- Trade events: `entry` opens the full 0.001 BTC on a flat book; `exit` closes it in full. No pyramiding, no averaging, no partial — the positioned book ignores further qualifying bars and the flat book ignores reversal bars (the disabled short arm is a no-op without a short book — disclosed, not repaired).
- Exact boundaries (pinned semantics): entry is non-strict on both bars (`before <= -100`, `last >= -100` — a last-bar touch exactly at −100 can fire with a proven washout); the exit is strict on both bars (`before > 100`, `last < 100` — exact ±100 touches fire nothing); regime is non-strict on both legs (exact equality reads long). Derived consequence, disclosed not repaired: a `before` bar touching exactly −100 breaks the backward scan immediately (`min = last >= -100`), so the washout can never prove and that bar cannot fire — effective entries need `before` strictly below −100. The `14` / `200` / `200` / `±100` / `∓200` literals are never tuned here.
- Washout window fenced (verified, disclosed not repaired): the backward scan runs only over the live 4-value slice and stops at the first value `>= -100` — a −200 print five or more bars back is invisible and proves nothing. Entries therefore require the washout and the recovery inside the same 4-bar window.
- Close-first ordering fenced (verified, disclosed not repaired): the source evaluates the close arms before the entry arms and `return`s after `signal.close()` — a bar printing the reversal on a LONG book closes and never enters on the same bar. `entry` needs `before <= -100` while `exit` needs `before > 100` — both can never co-print on one bar. No same-bar entry+exit ordering is ever needed beyond the disclosed position pin (flat → entry-only, positioned → exit-only, never a round-trip).
- Null-guard fenced: any leg with fewer than 2 non-null values returns silently — pre-seed bars print nothing and hold flat (no `fillna` exists to smear seeds forward).
- Direction: long-only derived book. The source short arm exists and is **explicitly disabled here** — a two-sided reading of this record would contradict it. The long-only book expresses unchanged on a spot venue with no naked shorting (see Crypto portability).
- Exits and risk (explicit): the single overbought-reversal close is the complete position-closing set. No stop, no target, no trailing, no breakeven move, no time exit, no forced end-of-data liquidation — **all explicitly absent** (source-faithful: the census proves none ships), never to be added by repair. Indefinite holds are possible and disclosed.
- Position rule (predeclared researcher pin mirroring source structure): single 0.001 BTC unit, at most one open position; re-entry re-arms on the next completed bar printing a fresh `entry` after any exit (no cooldown — explicitly none, source has none); pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar high/low/close (CCI) and closes (averages, regime) with fixed non-negative offsets (4/3/3-bar slices plus the bounded backward scan — no forward reference) — no volume, funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, informative merge, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. The `Math.round` calls feed `debugAll` cosmetics only and condition nothing. The source backtester's per-completed-candle step is the file's own framework contract.

## Required data

- Completed `1m` bars of BTCUSDT spot: `high`/`low`/`close` for the CCI leg, `close` for the SMA200/EMA200 legs and the regime comparison. No `open`, no volume, funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1m` (researcher pin — the source is timeframe-agnostic; its test fixture timeframe is not adopted). One evaluation per completed bar; every window reads the decision bar and its causal past only; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 200 completed one-minute bars held flat (~3.3 hours). Covers the SMA200/EMA200 seed (first values at index 199), the CCI14 seed, and the 4/3/3-bar slices with margin. Coded behaviour underneath: pre-seed TA-Lib outputs are null and the file filters nulls (slices shorter than 2 return early — no leg can fire early; no `fillna` exists to smear seeds forward). No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance **spot** under a fixed-size research pin (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed). No leverage, no margin, no funding.
- Order timing (derived, disclosed): completed-bar decision with **same-bar-close MARKET fills** — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted spot-1m siblings use. This mirrors the source backtester's own close-price convention (`price = candle.close` per completed candle). No maker-touch, queue, or intrabar-path-dependent fill: entry and the overbought-reversal exit are both bar-close-evaluated; the before-bar exclusivity fence leaves no ambiguous same-bar fill order to the engine beyond the disclosed position pin.
- Interval precedent (exact, disclosed): the admitted spot-1m siblings on `main` bound the verified path to Binance **spot**, leverage 1, fixed 0.001 BTC, `OrderExecutor` MARKET / `POSITION_HOLD`, and hypothetical `trade_cost=0.0002` per side — this record rides that same specified single-frame completed-bar `1m` Binance spot candle path, not an assumed one. Decision/availability timestamps, fills, and costs ride the same specified path: `BinanceSpotCandles` parses Binance `/api/v3/klines` open-time OHLCV with `1m` in its supported INTERVALS (full OHLCV rows, so the CCI high/low/close read is served, not assumed); `OrderExecutorSimulator` MARKET fills fully at the first provided row's close ending `CloseType.POSITION_HOLD`; the strategy-specific controller (not yet implemented) must calculate the exact CCI/SMA/EMA state and perform close-availability gating — the generic executor does not calculate the strategy. Spot funding is **not applicable**, never fabricated as futures zero. This Scout did not independently rehash the pinned wheel or re-run the representative engine validation — reuse of the verified path only, stated so the reviewer need not guess.
- Precision/quantization (frozen researcher model — nothing left to implementation choice): **unquantized synthetic fills**. Every entry buys exactly 0.001 BTC at the observed decision-bar close and every exit sells exactly that 0.001 BTC at its observed close; no lot-size rounding, no tick rounding, no partial fills, no order rejection, no min-notional gate, no residual dust — residual quantity is zero by construction after every exit. There is no second quantity, price, or residual rule to choose later; any venue-real quantization would be a different, unpinned rule. A missing or non-finite close never supplies a substitute fill or mark price — invalid or absent prices stop the run.
- Sizing/capital/costs: the source ships no sizing, capital, fee, or funding concept — sizing and costs ride an explicit fixed-size pin (0.001 BTC, leverage 1, hypothetical 0.0002 each side: `cum_fees_quote = trade_cost*amount*observed_close`), never presented as source-native behaviour. One round trip of 0.001 BTC: gross `0.001*(sell_close-buy_close)`; explicit research net `gross - 0.0002*0.001*(buy_close+sell_close)`. No slippage/spread modeled — not evidence of zero real slippage.
- Concurrency: at most one position at any time; the entry opens the full unit on a flat book; the overbought-reversal exit closes it in full; re-entry after an exit needs only the next qualifying entry bar (no cooldown — explicitly none). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. Safety orders/DCA are explicitly disabled. A pending order prohibits additional actions. An end-of-sample LONG is marked at the last real valid close, not closed with an invented fill (differs from the source backtester's end-of-data close — disclosed derivation, never a fill claim).
- Price integrity: validate every observed finite positive high/low/close before order creation; a missing-pair price fallback must never supply a substitute fill or mark price. Invalid or absent prices stop the run, not manufacture fills. No data source or engine ability is inferred merely from a supported interval or class name.

## Evidence

### Source-reported

The file ships the full construction (118 lines: the header contract, the three-length default block, the three-indicator wiring, the regime/excursion state machine, and the `Cci` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced. No backtest was run for this admission; HB_READY here is an engine-capability check, not a profitability result.

### Negative evidence

1. Leading-window behaviour fenced: pre-seed TA-Lib outputs are null and filtered (slices shorter than 2 return early — no leg can fire early; no `fillna` exists to smear seeds forward). The 200-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rules fenced: strict exit edges fire nothing when either bar prints exactly ±100; the regime reads long on exact equality on either leg; a `before` touch exactly at −100 breaks the washout scan and cannot fire — disclosed, not smoothed.
3. Washout-window fenced (verified, not assumed): the backward scan covers only the live 4-value slice and stops at the first value `>= -100` — a −200 print five or more bars back proves nothing. Shallow −100 recrosses without in-window washout print nothing.
4. Edge exclusivity fenced (verified, not assumed): `entry` needs `before <= -100`, `exit` needs `before > 100` — mutually exclusive per bar; the source close-first-`return` additionally bars any close-bar entry. The position pin resolves every residual (flat → entry-only, positioned → exit-only, never a same-bar round-trip).
5. Zero-variance fenced: flat tape pins SMA/EMA onto the flat line (regime reads long on equality — entry still needs a CCI excursion that flat tape cannot print) and the CCI onto a zero plateau (both edges test false at exactly ±100-adjacent prints; a constant series yields CCI 0, which fires neither the −100 entry nor the +100 exit). No division by zero exists anywhere in the gating path — disclosed, not repaired.
6. No-protection fenced: the census proves zero stop/target/trailing/time machinery ships — positions rely solely on the overbought reversal and may be held indefinitely; this record adopts that fate explicitly and no reviewer repair may add protection.
7. Derivation-effect fenced: apart from the six declared adaptations (spot market, 1m frame, disabled short arm, same-bar-close fills, fixed-size/warmup pins, hypothetical costs with frozen precision), this record computes no behaviour differently from the file's letter — CCI length, average lengths, thresholds, excursion depth, gate polarity, and both edges are verbatim; no reviewer invention is needed to execute it.
8. Cousin records fenced as different constructions (none conjoins a washout-proven −100 recross with a dual-average OR-gate): the admitted `haehnchen-ccimacd` sibling (CCI40 ±150 window + histogram pivot + ADX + SMA400), the bare-recross siblings (no excursion proof, no gate), the trailing-stop CCI sibling (engine-state exit), and the MACD/CCI, RSI/stoch co-gated siblings (different leading legs). Not a threshold re-tuning of any of them.
9. Sibling-file fence: every other strategy file in the source repository is a separate pin — its constants must never be substituted into this record. The `btc-usdt-15m` unit-test fixture is test data only, never the record frame.
10. Source-limitation fence: the repository self-describes as not production ready; no performance, robustness, or deployability claim is adopted from it.
11. Derivation boundary fenced: the non-source-native behaviours in this record are exactly the six declared adaptations — all predeclared above. The CCI −100 edge, −200 washout proof, dual-average OR-gate, reversal exit, and long-side entry conjunction are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: CCI length / SMA-EMA lengths / ±100 thresholds / −200 excursion / OR-gate polarity / disabled short arm / single-unit long-only / `1m` BTCUSDT spot / same-bar-close fills / frozen precision model are frozen.

- F1 — Excursion relevance: dropping the −200 washout proof (bare −100 recross with the same gate and exit) must not improve net expectancy; fail ⇒ the excursion adds nothing over the ungated recross.
- F2 — Gate relevance: dropping the SMA200/EMA200 OR-gate (same excursion entry, same exit) must not improve net expectancy; fail ⇒ the dual-average gate adds nothing over the ungated washout edge.
- F3 — Exit relevance: replacing the overbought-reversal exit with a regime-loss exit (price below *both* averages closes the long; same entry) must not improve net expectancy; fail ⇒ the reversal exit adds nothing over the regime exit.

## Crypto portability

Binance BTC-USDT spot 1m only, under this record's identity. No leverage, funding, or margin; porting to another spot pair/timeframe is a new identity, not covered here. The long-only book needs no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape. The CCI leg reads high/low/close and the average legs read close; no exotic feed is required.

## Limitations

- TA-Lib CCI/SMA/EMA internals (typical-price differencing, mean-deviation scaling, EMA seeding, SMA rolling semantics) live in their library outside the pinned file — pinned by call with the filed lengths, not re-derived; seeding effects sit under the disclosed 200-bar floor.
- Researcher-chosen (not source-native): Binance BTC-USDT spot market, 1m frame, disabled short arm, same-bar-close fill convention, 0.001 BTC size, 200-bar warmup, 0.0002/side hypothetical cost, frozen unquantized synthetic precision model, next-bar re-arm with no cooldown, end-of-sample mark (not close). No historical backtest statistics reproduced; no Qlib parity, survivor label, trading approval or deployment. Before mass Qlib screening, any *new* execution primitive/data requirement must receive representative Qlib/Hummingbot event-level parity; strategy-specific final HB certification is downstream.
- The unit-test fixture timeframe and the repository's non-production self-description constrain nothing in this record and license nothing beyond it.

## Implementation status

`not-implemented`: no controller, config, or Qlib recipe ships with this record. Downstream materialization via `IMPLEMENTATION_NEEDED` only, never a second admission flag.

## Adoption boundary

`research-only` / `not-approved`. PASS here admits the declared derivative to model-consistent research; it authorizes no Paper/Testnet/Live trading.

## Related Wiki records

None.

## Sources

- https://github.com/Haehnchen/crypto-trading-bot/blob/cb9563344a20ea7ac89ff214d350f141d1521219/src/strategy/strategies/cci.ts
- https://github.com/Haehnchen/crypto-trading-bot
