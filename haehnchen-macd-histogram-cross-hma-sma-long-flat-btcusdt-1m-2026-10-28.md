---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Haehnchen Macd MACD-histogram-cross HMA-regime SMA-gated long-flat on BTCUSDT spot 1m bars
created: 2026-10-28
updated: 2026-10-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-08-02
sources:
  - https://github.com/Haehnchen/crypto-trading-bot/blob/cb9563344a20ea7ac89ff214d350f141d1521219/src/strategy/strategies/macd.ts
  - https://github.com/Haehnchen/crypto-trading-bot
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Haehnchen Macd histogram-cross HMA-SMA long-flat — independent BTC-USDT spot 1m derivative

## Provenance

**Primary public GitHub identity:** `Haehnchen/crypto-trading-bot` (open-source CCXT crypto trading bot, MIT, test-covered v2 strategy framework). File `src/strategy/strategies/macd.ts`, class `Macd extends StrategyBase` (the only class in the file). Pinned commit `cb9563344a20ea7ac89ff214d350f141d1521219` (committed `2026-08-02T09:15:51Z`, message `Update to typescript 7`; verified as the repository HEAD via `git ls-remote` this cycle — record `source_as_of` is that commit date, never a fetch date). Git blob SHA `66fce9cf227d83771fce4819ef1c59eaf9a1c278`, size 3353 bytes, 108 lines, SHA-256 `d5835ff0ba79a99af1ca93d077c0e99d7d6bc3d5e211dfdaaa67b4068a1864d0`; the raw file fetched at the pinned commit reproduces that blob via `git hash-object` — the entire file was read, not sampled.

**The file's own words (quoted for gate evidence, never extended):** header comment `Long: MACD histogram crosses above 0 when HMA >= SMA200` / `Short: MACD histogram crosses below 0 when HMA < SMA200` / `Close: Histogram reverses against position`. Defaults `default_ma_type: 'EMA'`, `fast_period: 12`, `slow_period: 26`, `signal_period: 9`, `hma_length: 9`, `sma_length: 200` — no hyperopt, no hidden branch. Entry needs the regime side to agree with the histogram edge; a positioned book closes on the histogram reversal against it (`signal.close()` with `return`, so no entry fires on a close bar); a flat book opens only on its side's edge.

**Out-of-file calls pinned (all read at the pinned commit):** `src/utils/indicators.ts` computes `macd_ext` via TA-Lib `MACDEXT` on the close series with all three MA legs defaulting to the filed `default_ma_type` (`EMA`: `optInFastMAType/SlowMAType/SignalMAType` all resolve through `getMaTypeFromString`, unknown strings fall back to index 1 = EMA) and `histogram = outMACDHist` (MACD minus signal); `hma` via the file-local Hull recipe on the close series (`halfPeriod = floor(9/2) = 4`, `sqrtPeriod = floor(sqrt(9)) = 3`, `raw = 2*WMA4 - WMA9`, `HMA = WMA(raw, 3)`, `offset = 9 - 4 = 5`); `sma` via TA-Lib `SMA` on the close series. `src/modules/strategy/v2/typed_backtest.ts` executes one strategy step per completed candle with `price = candle.close`, fills entries/exits at the row close price, and clears position state on `close` (`lastSignal = undefined`). `src/modules/services.ts` imports `Macd` (L65) and registers it in the runnable strategy list (L584) — not an orphan file. The unit test `test/modules/strategy/v2/strategies/macd.test.ts` pins `default_ma_type EMA`, `fast_period 12`, `slow_period 26`, `signal_period 9`, `hma_length 9`, `sma_length 200` — the filed defaults, cross-checked. No `volume` column is read by any gating line.

**Full-file token census (verified over the 108 lines this cycle):** 1 `goLong` / 1 `goShort` / 1 `signal.close` (the complete action set); 0 `stop` / 0 `trailing` / 0 `target` (no protective machinery of any kind — disclosed absence, never repaired); 0 `volume` / 0 `shift` / 0 `request` / 0 `security` / 0 `typical_price`; 0 `leverage` / 0 `funding` / 0 `hyperopt`. The `long` / `short` tokens are exactly the direction plumbing (header comment, `isLong`, `lastSignal` comparisons, the two entries, the close arms) — no second leg hides anywhere.

**Declared independent derivative v1, NOT source-native/lossless:** this record specifies a separately identified derived executable strategy. Researcher-declared adaptations are exactly six, all predeclared here and repeated in their sections: (1) research market Binance BTC-USDT **spot** (the source names no market); (2) research timeframe **`1m`** (the source is timeframe-agnostic; its unit-test fixture is `btc-usdt-15m` data, disclosed as fixture only, never adopted as the frame); (3) **long/flat only — the source short arm (histogram `before > 0 && current < 0` with `HMA < SMA200`, `goShort`) is explicitly disabled** in this book, so long-side economics differ from the two-sided source and nothing here is evidence the source passes unchanged; (4) completed-bar decisions with **same-bar-close MARKET fills** (matches the source backtester's own close-price convention); (5) fixed 0.001 BTC single-unit/no-add/no-cooldown position pin with a 200-bar researcher warmup floor; (6) hypothetical 0.0002/side cost pin with spot (funding-N/A) accounting. Every threshold, lookback, MA type, period, regime comparison, and histogram edge is source-verbatim.

**Immutable research identity:** `Haehnchen-macd-cb95633 | derived-v1-longflat | BTC-USDT-binance-spot-1m | hist0cross-hma9-sma200 | samebar-close-0.001BTC | 2026-10-28`. Changing any component changes the derivative identity.

**Pre-write dedup (2026-10-28):** working-tree base is current `main@092277f` (414 root strategy records, README pool count 414, every record verified `hb_ready_status: PASS` — zero non-PASS files). Content search for `Haehnchen`, `crypto-trading-bot`, `strategies/macd.ts`, `66fce9cf`, `macd_ext`, `MACDEXT`, `hma_length`, `HMA >= SMA200` returns exactly one record — the admitted `haehnchen-ccimacd` sibling (MACD-histogram 5L/5R **pivot** + CCI40 ±150 twelve-bar window + ADX veto + SMA400 — a different construction, fenced below). All ten open `research/*` PRs examined by branch and title — none uses this file or rule. Nearest families are materially different constructions: `macd-signal-cross-reversal` (1d bare MACD **line/signal** cross, no histogram edge, no HMA/SMA regime gate), `forven-hma-cross` (1h dual-Hull 9/21 cross pair, no MACD leg at all), `forven-macd-cross-adx-regime` (MACD cross + ADX regime, no HMA/SMA leg), `freqtrade-macd-cci-dip-state` / `freqtrade-macd-cross-cci-edge` (MACD + CCI gates, no HMA/SMA regime), `hull-ema-crossover-reversal` (Hull-vs-EMA cross, no MACD). None conjoins a MACD-histogram zero-cross edge with an HMA9-vs-SMA200 regime gate. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: ride the MACD histogram's zero-cross edge, but only on the side the Hull-vs-SMA regime permits — longs only when the fast Hull sits at or above the slow average, shorts only when it sits below — and surrender the position the moment the histogram reverses against it. No behavioural, structural, or risk-premium channel is claimed anywhere in the 108 lines; the repository README self-describes the bot as not production ready (adopted as a limitation, never as a rule).

### Research interpretation

A regime-permitted momentum-edge buyer, long-only. Unlike bare MACD-cross records that trade every rotation including counter-trend chop, the HMA9-vs-SMA200 conjunct vetoes any long edge printed while the fast Hull trails the slow average — the histogram edge is necessary but never sufficient. Unlike dual-average cross records (HMA9/21, EMA pairs), the averages here never trigger anything by themselves: they are a side condition, not a signal — a golden cross with a negative histogram prints nothing, and a histogram edge against the regime prints nothing. The exit is deliberately impatient on reversals but patient otherwise: no stop, no target, no clock — a long whose histogram stays positive through a regime flip is held (the close arm needs the histogram reversal, not the regime flip), and an underwater long whose histogram never reverses is held, not forgiven. The coded consequence is a buyer of histogram zero-cross-ups inside Hull-confirmed tape above the long-run average, harvesting only reversal closes.

## Signal

Exact rule as pinned (any other MA type, period, regime comparison, edge polarity, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own:

```text
HIST[t]   = TA-Lib MACDEXT(close, fast 12 EMA, slow 26 EMA, signal 9 EMA) histogram (MACD line minus signal)
HMA9[t]   = in-file Hull(close, 9): WMA(close,4), WMA(close,9), raw = 2*WMA4[+5] - WMA9, HMA = WMA(raw,3)
SMA200[t] = TA-Lib SMA(close, 200)
isLong[t] = (HMA9[t] >= SMA200[t])
longEdge[t]  = (HIST[t-1] < 0) AND (HIST[t] > 0)
revDown[t]   = (HIST[t-1] > 0) AND (HIST[t] < 0)
entry[t]     = FLAT AND isLong[t] AND longEdge[t]
exit[t]      = LONG AND revDown[t]   // source close() arm, long book only
```

- Trade events: `entry` opens the full 0.001 BTC on a flat book; `exit` closes it in full. No pyramiding, no averaging, no partial — the positioned book ignores further `longEdge` bars and the flat book ignores `revDown` bars (the disabled short arm is a no-op without a short book — disclosed, not repaired).
- Exact boundaries (pinned semantics): histogram edges are strict (`<0`/`>0` — a histogram exactly at zero on either bar fires nothing on either side); regime is non-strict (`HMA >= SMA200` — exact equality reads long and blocks the disabled short side). The `EMA` / `12` / `26` / `9` / `9` / `200` literals are never tuned here.
- Close-first ordering fenced (verified, disclosed not repaired): the source evaluates the close arms before the entry arms and `return`s after `signal.close()` — a bar printing `revDown` on a LONG book closes and never enters on the same bar. `longEdge` needs `HIST[t] > 0` while `revDown` needs `HIST[t] < 0` — both can never co-print on one bar. No same-bar entry+exit ordering is ever needed beyond the disclosed position pin (flat → entry-only, positioned → exit-only, never a round-trip).
- Direction: long-only derived book. The source short arm exists and is **explicitly disabled here** — a two-sided reading of this record would contradict it. The long-only book expresses unchanged on a spot venue with no naked shorting (see Crypto portability).
- Exits and risk (explicit): the single histogram-reversal close is the complete position-closing set. No stop, no target, no trailing, no breakeven move, no time exit, no forced end-of-data liquidation — **all explicitly absent** (source-faithful: the census proves none ships), never to be added by repair. Indefinite holds are possible and disclosed.
- Position rule (predeclared researcher pin mirroring source structure): single 0.001 BTC unit, at most one open position; re-entry re-arms on the next completed bar printing a fresh `entry` after any exit (no cooldown — explicitly none, source has none); pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar closes (MACD/SMA/HMA all derive from the close series; HMA's default `source = 'close'`) with fixed non-negative offsets (one-bar edge lookback — no forward reference) — no volume, funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, informative merge, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. The source backtester's per-completed-candle step is the file's own framework contract.

## Required data

- Completed `1m` bars of BTCUSDT spot: `close` only for the MACD/HMA/SMA path and the regime comparison. No `high`/`low`/`open`, no volume, funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1m` (researcher pin — the source is timeframe-agnostic; its test fixture timeframe is not adopted). One evaluation per completed bar; every window reads the decision bar and its causal past only; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 200 completed one-minute bars held flat (~3.3 hours). Covers the SMA200 seed (first value at index 199), the MACD slow-26/signal-9 seed, and the HMA9 seed with margin. Coded behaviour underneath: pre-seed TA-Lib outputs are null and the file filters nulls (slices shorter than the required 2/1/1 lengths return early — no leg can fire early; no `fillna` exists to smear seeds forward). No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance **spot** under a fixed-size research pin (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed). No leverage, no margin, no funding.
- Order timing (derived, disclosed): completed-bar decision with **same-bar-close MARKET fills** — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted spot-1m siblings use. This mirrors the source backtester's own close-price convention (`price = candle.close` per completed candle). No maker-touch, queue, or intrabar-path-dependent fill: entry and the histogram-reversal exit are both bar-close-evaluated; the edge exclusivity fence leaves no ambiguous same-bar fill order to the engine beyond the disclosed position pin.
- Interval precedent (exact, disclosed): the admitted `freqtrade-low-bb-98-sub-band-dip-close-bracket-long-flat-btcusdt-1m-2026-10-27.md` record on `main` bounds the verified path to Binance **spot**, leverage 1, fixed 0.001 BTC, `OrderExecutor` MARKET / `POSITION_HOLD`, and hypothetical `trade_cost=0.0002` per side — this record rides that same specified single-frame completed-bar `1m` Binance spot candle path, not an assumed one. Decision/availability timestamps, fills, and costs ride the same specified path: `BinanceSpotCandles` parses Binance `/api/v3/klines` open-time OHLCV with `1m` in its supported INTERVALS; `OrderExecutorSimulator` MARKET fills fully at the first provided row's close ending `CloseType.POSITION_HOLD`; the strategy-specific controller (not yet implemented) must calculate the exact histogram/HMA/SMA state and perform close-availability gating — the generic executor does not calculate the strategy. Pin fees/precision downstream; spot funding is **not applicable**, never fabricated as futures zero. This Scout did not independently rehash the pinned wheel or re-run the representative engine validation — reuse of the verified path only, stated so the reviewer need not guess.
- Sizing/capital/costs: the source ships no sizing, capital, fee, or funding concept — sizing and costs ride an explicit fixed-size pin (0.001 BTC, leverage 1, hypothetical 0.0002 each side: `cum_fees_quote = trade_cost*amount*observed_close`), never presented as source-native behaviour. One round trip of 0.001 BTC: gross `0.001*(sell_close-buy_close)`; explicit research net `gross - 0.0002*0.001*(buy_close+sell_close)`. No slippage/spread modeled — not evidence of zero real slippage.
- Concurrency: at most one position at any time; the entry opens the full unit on a flat book; the histogram-reversal exit closes it in full; re-entry after an exit needs only the next qualifying entry bar (no cooldown — explicitly none). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. Safety orders/DCA are explicitly disabled. A pending order prohibits additional actions. An end-of-sample LONG is marked at the last real valid close, not closed with an invented fill (differs from the source backtester's end-of-data close — disclosed derivation, never a fill claim).
- Price integrity: validate every observed finite positive close before order creation; a missing-pair price fallback must never supply a substitute fill or mark price. Invalid or absent prices stop the run, not manufacture fills. No data source or engine ability is inferred merely from a supported interval or class name.

## Evidence

### Source-reported

The file ships the full construction (108 lines: the header contract, the six-literal default block, the three-indicator wiring, the regime/edge state machine, and the `Macd` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced. No backtest was run for this admission; HB_READY here is an engine-capability check, not a profitability result.

### Negative evidence

1. Leading-window behaviour fenced: pre-seed TA-Lib outputs are null and filtered (slices shorter than 2/1/1 return early — no leg can fire early; no `fillna` exists to smear seeds forward). The 200-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rules fenced: strict histogram edges fire nothing when either bar prints exactly zero; the regime reads long on exact HMA=SMA equality — disclosed, not smoothed.
3. Edge exclusivity fenced (verified, not assumed): `longEdge` needs `HIST[t] > 0`, `revDown` needs `HIST[t] < 0` — mutually exclusive per bar; the source close-first-`return` additionally bars any close-bar entry. The position pin resolves every residual (flat → entry-only, positioned → exit-only, never a same-bar round-trip).
4. Zero-variance fenced: flat tape pins SMA onto the flat line, HMA onto the flat line (regime reads long on equality — entry still needs a histogram edge that flat tape cannot print), and the MACD histogram onto a zero plateau (both edges test false at exactly zero prints). No division by zero exists anywhere in the gating path — disclosed, not repaired.
5. No-protection fenced: the census proves zero stop/target/trailing/time machinery ships — positions rely solely on the histogram reversal and may be held indefinitely; this record adopts that fate explicitly and no reviewer repair may add protection.
6. Derivation-effect fenced: apart from the six declared adaptations (spot market, 1m frame, disabled short arm, same-bar-close fills, fixed-size/warmup pins, hypothetical costs), this record computes no behaviour differently from the file's letter — MA type, periods, regime comparison, and both histogram edges are verbatim; no reviewer invention is needed to execute it.
7. Cousin records fenced as different constructions (none conjoins a MACD-histogram zero-cross edge with an HMA9-vs-SMA200 regime gate): the admitted bare-MACD sibling (1d line/signal cross, no histogram edge, no regime gate), the dual-Hull sibling (1h HMA9/21 cross pair, no MACD leg), the MACD-ADX sibling (ADX regime, no HMA/SMA leg), the MACD-CCI siblings (CCI gates, no HMA/SMA regime), and the admitted `haehnchen-ccimacd` sibling (histogram 5L/5R **pivot** + CCI window + ADX veto + SMA400 — pivot-turn, not zero-cross-edge, with three extra legs this record has none of). Not a threshold re-tuning of any of them.
8. Sibling-file fence: every other strategy file in the source repository is a separate pin — its constants must never be substituted into this record. The `btc-usdt-15m` unit-test fixture is test data only, never the record frame.
9. Source-limitation fence: the repository self-describes as not production ready; no performance, robustness, or deployability claim is adopted from it.
10. Derivation boundary fenced: the non-source-native behaviours in this record are exactly the six declared adaptations — all predeclared above. The MACDEXT histogram edge, HMA9 regime arithmetic, SMA200 gate, reversal exit, and long-side entry conjunction are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: MA type / fast-slow-signal periods / HMA length / SMA length / regime comparison / histogram edge polarity / disabled short arm / single-unit long-only / `1m` BTCUSDT spot / same-bar-close fills are frozen.

- F1 — Regime-gate relevance: dropping the `HMA >= SMA200` conjunct (same histogram edges, same exit) must not improve net expectancy; fail ⇒ the Hull regime gate adds nothing over the ungated histogram edge.
- F2 — Edge-vs-state relevance: replacing the zero-cross **edge** (`before<0 AND current>0`) with a positive-histogram **state** hold (same regime gate, same exit) must not improve net expectancy; fail ⇒ the edge adds nothing over the level state.
- F3 — Exit relevance: replacing the histogram-reversal exit with a regime-flip exit (`HMA < SMA200` closes the long; same entry) must not improve net expectancy; fail ⇒ the reversal exit adds nothing over the regime exit.

## Crypto portability

Binance BTC-USDT spot 1m only, under this record's identity. No leverage, funding, or margin; porting to another spot pair/timeframe is a new identity, not covered here. The long-only book needs no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape. Only the `close` series is read; no exotic feed is required.

## Limitations

- TA-Lib MACDEXT/SMA internals (EMA seeding, MACD differencing, SMA rolling semantics) live in their library outside the pinned file — pinned by call with the filed MA type and lengths, not re-derived; the in-file HMA WMA cascade inherits its own seeding alongside the file-local wiring, under the disclosed 200-bar floor.
- Researcher-chosen (not source-native): Binance BTC-USDT spot market, 1m frame, disabled short arm, same-bar-close fill convention, 0.001 BTC size, 200-bar warmup, 0.0002/side hypothetical cost, next-bar re-arm with no cooldown, end-of-sample mark (not close). No historical backtest statistics reproduced; no Qlib parity, survivor label, trading approval or deployment. Before mass Qlib screening, any *new* execution primitive/data requirement must receive representative Qlib/Hummingbot event-level parity; strategy-specific final HB certification is downstream.
- The unit-test fixture timeframe and the repository's non-production self-description constrain nothing in this record and license nothing beyond it.

## Implementation status

`not-implemented`: no controller, config, or Qlib recipe ships with this record. Downstream materialization via `IMPLEMENTATION_NEEDED` only, never a second admission flag.

## Adoption boundary

`research-only` / `not-approved`. PASS here admits the declared derivative to model-consistent research; it authorizes no Paper/Testnet/Live trading.

## Related Wiki records

None.

## Sources

- https://github.com/Haehnchen/crypto-trading-bot/blob/cb9563344a20ea7ac89ff214d350f141d1521219/src/strategy/strategies/macd.ts
- https://github.com/Haehnchen/crypto-trading-bot
