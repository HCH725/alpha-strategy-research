---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Haehnchen CciMacd MACD-histogram-pivot CCI-window ADX-veto SMA-gated long-flat on BTCUSDT spot 1m bars
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
  - https://github.com/Haehnchen/crypto-trading-bot/blob/cb9563344a20ea7ac89ff214d350f141d1521219/src/strategy/strategies/cci_macd.ts
  - https://github.com/Haehnchen/crypto-trading-bot
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Haehnchen CciMacd histogram-pivot CCI-ADX-SMA long-flat — independent BTC-USDT spot 1m derivative

## Provenance

**Primary public GitHub identity:** `Haehnchen/crypto-trading-bot` (open-source CCXT crypto trading bot, MIT, test-covered v2 strategy framework). File `src/strategy/strategies/cci_macd.ts`, class `CciMacd extends StrategyBase` (the only class in the file). Pinned commit `cb9563344a20ea7ac89ff214d350f141d1521219` (committed `2026-08-02T09:15:51Z`, message `Update to typescript 7`; verified as the repository HEAD via `git ls-remote` this cycle — record `source_as_of` is that commit date, never a fetch date). Git blob SHA `4a6322109e2bd84b41913c6595969e0fdffe8ab7`, size 5848 bytes, 184 lines, SHA-256 `b02a1fc91a9b249ea779c4a925f73f983a412e641cbeac3834ceec334b95411c`; the raw file fetched at the pinned commit reproduces that blob via `git hash-object` — the entire file was read, not sampled.

**The file's own words (quoted for gate evidence, never extended):** header comment `Long: MACD histogram has a low pivot (<0) AND CCI recently touched -150 → open if price > SMA` / `Short: MACD histogram has a high pivot (>0) AND CCI recently touched +150 → open if price < SMA` / `Close: Opposite signal fires against current position`. Defaults `macd_pivot_reversal: 5`, `cci_trigger: 150`, `cci_cross_lookback_for_macd_trigger: 12`, `macd_fast_length: 24`, `macd_slow_length: 52`, `macd_signal_length: 18`, `sma_length: 400`, `cci_length: 40`, `adx_length: 14` — no hyperopt, no hidden branch. Entry needs flat book (`!lastSignal`), non-sideways tape, and direction agreement; positioned book closes only on the opposite setup (`signal.close()`); same-bar open+close is structurally impossible (`if/else-if`).

**Out-of-file calls pinned (all read at the pinned commit):** `src/utils/indicators.ts` computes `cci` via TA-Lib `CCI` on `high/low/close` (candle-source list includes `cci`), `adx` via TA-Lib `ADX` on `high/low/close`, `macd` via TA-Lib `MACD` on the close series with `histogram = outMACDHist` (MACD minus signal), `sma` via TA-Lib `SMA` on the close series. `src/modules/strategy/v2/typed_backtest.ts` executes one strategy step per completed candle with `price = candle.close`, fills entries/exits at the row close price, and clears position state on `close`. `src/modules/services.ts` imports `CciMacd` (L69) and registers it in the runnable `StrategyRegistry` list — not an orphan file. The unit test `test/modules/strategy/v2/strategies/cci_macd.test.ts` pins `cci_length 40`, `sma_length 400`, `macd_fast_length 24`, `cci_trigger 150` — the filed defaults, cross-checked. No `volume` column is read by any gating line.

**Full-file token census (verified over the 184 lines this cycle):** 1 `goLong` / 1 `goShort` / 1 `signal.close` (the complete action set); 0 `stop` / 0 `trailing` / 0 `target` (no protective machinery of any kind — disclosed absence, never repaired); 0 `volume` / 0 `shift` / 0 `request` / 0 `security` / 0 `typical_price`; 0 `leverage` / 0 `funding` / 0 `hyperopt`. The 7 `short` / 8 `long` tokens are exactly the direction plumbing (header comment, `allowedDirection`, `currentSignal` type/assignments, the two entries, the two `lastSignal` comparisons) — no second leg hides anywhere.

**Declared independent derivative v1, NOT source-native/lossless:** this record specifies a separately identified derived executable strategy. Researcher-declared adaptations are exactly six, all predeclared here and repeated in their sections: (1) research market Binance BTC-USDT **spot** (the source names no market); (2) research timeframe **`1m`** (the source is timeframe-agnostic; its unit-test fixture is `btc-usdt-15m` data, disclosed as fixture only, never adopted as the frame); (3) **long/flat only — the source short arm (`macdPivot.high>0` + CCI `>=+150`, L138-140, `goShort` L159-161) is explicitly disabled** in this book, so long-side economics differ from the two-sided source and nothing here is evidence the source passes unchanged; (4) completed-bar decisions with **same-bar-close MARKET fills** (matches the source backtester's own close-price convention); (5) fixed 0.001 BTC single-unit/no-add/no-cooldown position pin with a 400-bar researcher warmup floor; (6) hypothetical 0.0002/side cost pin with spot (funding-N/A) accounting. Every threshold, lookback, pivot leg, CCI window, ADX veto, and SMA gate is source-verbatim.

**Immutable research identity:** `Haehnchen-cci_macd-cb95633 | derived-v1-longflat | BTC-USDT-binance-spot-1m | hist5-cci40x12-adx10veto-sma400 | samebar-close-0.001BTC | 2026-10-28`. Changing any component changes the derivative identity.

**Pre-write dedup (2026-10-28):** working-tree base is current `main@5a2e741` (412 root strategy records, README pool count 412, every record verified `hb_ready_status: PASS` — zero non-PASS files). Content search for `Haehnchen`, `cci_macd`, `CciMacd`, `crypto-trading-bot`, `24/52/18`, `SMA400`, `histogram pivot`, `macd_pivot`, `pivot_reversal` returns **zero** records. All ten open `research/*` PRs examined by branch and title — none uses this file or rule. Nearest families are materially different constructions: `freqtrade-macd-cci-dip-state` (5m MACD 12/26/9 level-state + CCI14 ±50/±100, no pivot, no ADX veto, no SMA400), `freqtrade-macd-cross-cci-edge` (5m MACD cross-edge + CCI gate, no histogram pivot), `hummingbot-macdbb-bbp-macdh-turn` (1d %B-MACD-turn, different family), `cci-threshold-extreme-reversal` (4h Pine CCI threshold-cross, no MACD/ADX/SMA), open PR #304 forven CCI (pure CCI recross, 1h). None conjoins a MACD-histogram 5L/5R pivot with a CCI40 ±150 twelve-bar window, an ADX≤25 ten-bar sideways veto, and an SMA400 direction gate. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: open when a confirmed MACD-histogram pivot prints on the correct side of zero together with an extreme CCI print inside the trailing twelve-bar window, in the direction the price sits relative to its 400-bar average, unless the tape reads sideways — and close only when the mirror setup prints against the position. No behavioural, structural, or risk-premium channel is claimed anywhere in the 184 lines; the repository README self-describes the bot as not production ready (adopted as a limitation, never as a rule).

### Research interpretation

A pivot-confirmed exhaustion buyer, long-only. Unlike level-state MACD records that hold while MACD sits above signal, the pivot leg fires only on a confirmed local extremum of the histogram (a turn, not a level — a merely-positive-but-flat histogram prints nothing). Unlike pure CCI-washout records, the CCI leg is a recency window, not a crossing edge: any ±150 touch within twelve bars arms the setup. Two permission keys AND with the pivot: the trend must not be certified-chop (ADX veto — all-ten ≤25 prints nothing even on a perfect pivot+CCI) AND price must sit above its 400-bar average (slow gravitational veto). The exit is deliberately patient: no stop, no target, no clock — an underwater long that never sees a mirror setup is held, not forgiven. The coded consequence is a buyer of confirmed histogram turns at statistical extremes inside non-chop tape above the long-run average, harvesting only mirror-signal reversals.

## Signal

Exact rule as pinned (any other pivot width, CCI length/trigger/window, ADX length/threshold/count, SMA length, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own:

```text
HIST[t]   = TA-Lib MACD(close, 24, 52, 18) histogram (MACD line minus signal)
SMA400[t] = TA-Lib SMA(close, 400)
CCI40[t]  = TA-Lib CCI(high, low, close, 40)
ADX14[t]  = TA-Lib ADX(high, low, close, 14)
pivot     = getPivotPoints(last 15 HIST, left 5, right 5): window = HIST[t-10..t],
            middle = HIST[t-5]; high-pivot iff no window value strictly > middle;
            low-pivot iff no window value strictly < middle
longSetup[t]  = low-pivot AND (middle < 0) AND any(CCI40[t-11..t] <= -150)
shortSetup[t] = high-pivot AND (middle > 0) AND any(CCI40[t-11..t] >= +150)
allowed[t]    = (C[t] > SMA400[t]) ? long : short
sideways[t]   = last 10 ADX14 all <= 25 (needs >= 10 values)
entry[t]      = FLAT AND longSetup[t] AND (allowed[t] == long) AND NOT sideways[t]
exit[t]       = LONG AND shortSetup[t]   // source close() arm, long book only
```

- Trade events: `entry` opens the full 0.001 BTC on a flat book; `exit` closes it in full. No pyramiding, no averaging, no partial — the positioned book ignores further `longSetup` bars and the flat book ignores `shortSetup` bars (the disabled arm is a no-op without a short book — disclosed, not repaired).
- Exact boundaries (pinned semantics): pivot comparisons are strict (`>`/`<` — plateau ties still count as pivots); pivot zero-side tests are strict (`>0`/`<0` — a middle exactly at zero is neither); CCI window tests are non-strict (`<=-150` / `>=+150` — exact touch arms); direction is strict (`C > SMA400` — exact equality reads short and blocks entry); ADX veto is non-strict (`<=25` — all-ten exactly at 25 still vetos). The `5` / `12` / `150` / `24` / `52` / `18` / `400` / `40` / `14` / `25` / `10` literals are never tuned here.
- Setup exclusivity fenced (verified arithmetic, disclosed not repaired): high-pivot needs middle `>0`, low-pivot needs middle `<0` — both setups can never co-print on one bar. No same-bar entry+exit ordering is ever needed: the position pin alone resolves every bar (flat → entry-only, positioned → exit-only, never a round-trip).
- Direction: long-only derived book. The source short arm exists (cited lines above) and is **explicitly disabled here** — a two-sided reading of this record would contradict it. The long-only book expresses unchanged on a spot venue with no naked shorting (see Crypto portability).
- Exits and risk (explicit): the single opposite-signal close is the complete position-closing set. No stop, no target, no trailing, no breakeven move, no time exit, no forced end-of-data liquidation — **all explicitly absent** (source-faithful: the census proves none ships), never to be added by repair. Indefinite holds are possible and disclosed.
- Position rule (predeclared researcher pin mirroring source structure): single 0.001 BTC unit, at most one open position; re-entry re-arms on the next completed bar printing a fresh `entry` after any exit (no cooldown — explicitly none, source has none); pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar OHLC (`high`/`low`/`close` for CCI/ADX, `close` for MACD/SMA/direction) with fixed non-negative offsets (trailing windows plus the t-5 pivot confirmation — no forward reference) — no volume, funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, resample, informative merge, interpolate, hyperopt parameter, or stop/limit order argument anywhere in the gating path. The source backtester's per-completed-candle step is the file's own framework contract.

## Required data

- Completed `1m` bars of BTCUSDT spot: `high`/`low`/`close` for the CCI40/ADX14 path, `close` for the MACD/SMA/direction path. No volume, funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1m` (researcher pin — the source is timeframe-agnostic; its test fixture timeframe is not adopted). One evaluation per completed bar; every window reads the decision bar and its causal past only; fills land on the decision bar's own close under the derived rule below.
- Warmup (researcher pin, disclosed): 400 completed one-minute bars held flat (~6.7 hours). Covers the SMA400 seed (first value at index 399), the MACD slow-52/signal-18 seed, the CCI40 seed, the ADX14 seed, the 15-histogram pivot window, the 12-CCI window, and the 10-ADX veto with margin. Coded behaviour underneath: pre-seed TA-Lib outputs are null and the file filters nulls (every short-window guard simply stays short — no leg can fire early; no `fillna` exists to smear seeds forward). No repainting, no negative shift, no future bars/extrema, no full-sample normalization.

## Execution assumptions

- Research market: BTCUSDT Binance **spot** under a fixed-size research pin (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed). No leverage, no margin, no funding.
- Order timing (derived, disclosed): completed-bar decision with **same-bar-close MARKET fills** — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted spot-1m sibling below uses. This mirrors the source backtester's own close-price convention (`price = candle.close` per completed candle). No maker-touch, queue, or intrabar-path-dependent fill: entry and the opposite-signal exit are both bar-close-evaluated; the setup-exclusivity fence leaves no ambiguous same-bar fill order to the engine beyond the disclosed position pin.
- Interval precedent (exact, disclosed): the admitted `freqtrade-low-bb-98-sub-band-dip-close-bracket-long-flat-btcusdt-1m-2026-10-27.md` record on `main` bounds the verified path to Binance **spot**, leverage 1, fixed 0.001 BTC, `OrderExecutor` MARKET / `POSITION_HOLD`, and hypothetical `trade_cost=0.0002` per side — this record rides that same specified single-frame completed-bar `1m` Binance spot candle path, not an assumed one. Decision/availability timestamps, fills, and costs ride the same specified path: `BinanceSpotCandles` parses Binance `/api/v3/klines` open-time OHLCV with `1m` in its supported INTERVALS; `OrderExecutorSimulator` MARKET fills fully at the first provided row's close ending `CloseType.POSITION_HOLD`; the strategy-specific controller (not yet implemented) must calculate the exact pivot/CCI/ADX/SMA state and perform close-availability gating — the generic executor does not calculate the strategy. Pin fees/precision downstream; spot funding is **not applicable**, never fabricated as futures zero. This Scout did not independently rehash the pinned wheel or re-run the representative engine validation — reuse of the verified path only, stated so the reviewer need not guess.
- Sizing/capital/costs: the source ships no sizing, capital, fee, or funding concept — sizing and costs ride an explicit fixed-size pin (0.001 BTC, leverage 1, hypothetical 0.0002 each side: `cum_fees_quote = trade_cost*amount*observed_close`), never presented as source-native behaviour. One round trip of 0.001 BTC: gross `0.001*(sell_close-buy_close)`; explicit research net `gross - 0.0002*0.001*(buy_close+sell_close)`. No slippage/spread modeled — not evidence of zero real slippage.
- Concurrency: at most one position at any time; the entry opens the full unit on a flat book; the opposite-signal exit closes it in full; re-entry after an exit needs only the next qualifying entry bar (no cooldown — explicitly none). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. Safety orders/DCA are explicitly disabled. A pending order prohibits additional actions. An end-of-sample LONG is marked at the last real valid close, not closed with an invented fill (differs from the source backtester's end-of-data close — disclosed derivation, never a fill claim).
- Price integrity: validate every observed finite positive close before order creation; a missing-pair price fallback must never supply a substitute fill or mark price. Invalid or absent prices stop the run, not manufacture fills. No data source or engine ability is inferred merely from a supported interval or class name.

## Evidence

### Source-reported

The file ships the full construction (184 lines: the pivot helper, the nine-literal default block, the four-indicator wiring, the setup/entry/exit state machine, and the `CciMacd` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced. No backtest was run for this admission; HB_READY here is an engine-capability check, not a profitability result.

### Negative evidence

1. Leading-window behaviour fenced: pre-seed TA-Lib outputs are null and filtered (no leg can fire early; no `fillna` exists to smear seeds forward). The 400-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired.
2. Exact-touch rules fenced: strict pivot/direction legs fire nothing on equality; the CCI window arms on exact touch; the ADX veto blocks on all-ten exactly at 25 — disclosed, not smoothed.
3. Setup exclusivity fenced (verified, not assumed): opposite zero-side pivot tests make long/short setups mutually exclusive per bar; the position pin resolves every residual (flat → entry-only, positioned → exit-only, never a same-bar round-trip).
4. Zero-variance fenced: flat tape pins CCI toward 0/NaN (failing the ±150 window), ADX toward 0/NaN (vetoing via all-ten ≤25), MACD histogram onto a zero plateau (both pivots test false at exactly zero middle), and SMA400 onto the flat line (strict `>` fails on equality). No division by zero exists anywhere in the gating path — disclosed, not repaired.
5. No-protection fenced: the census proves zero stop/target/trailing/time machinery ships — positions rely solely on the mirror setup and may be held indefinitely; this record adopts that fate explicitly and no reviewer repair may add protection.
6. Derivation-effect fenced: apart from the six declared adaptations (spot market, 1m frame, disabled short arm, same-bar-close fills, fixed-size/warmup pins, hypothetical costs), this record computes no behaviour differently from the file's letter — every threshold, lookback, pivot leg, window, veto, and gate is verbatim; no reviewer invention is needed to execute it.
7. Cousin records fenced as different constructions (none conjoins an MACD-histogram 5L/5R pivot with a CCI40 ±150 twelve-bar window, an ADX≤25 ten-bar veto, and an SMA400 gate): the admitted MACD-CCI dip-state sibling (5m level-state, no pivot/veto/SMA400), the MACD-cross CCI-edge sibling (5m cross-edge, no pivot), the MACD-BB %B-turn sibling (1d, different family), the CCI threshold-cross sibling (4h Pine, no MACD/ADX/SMA), and open PR #304 (pure CCI recross, 1h). Not a threshold re-tuning of any of them.
8. Sibling-file fence: every other strategy file in the source repository is a separate pin — its constants must never be substituted into this record. The `btc-usdt-15m` unit-test fixture is test data only, never the record frame.
9. Source-limitation fence: the repository self-describes as not production ready; no performance, robustness, or deployability claim is adopted from it.
10. Derivation boundary fenced: the non-source-native behaviours in this record are exactly the six declared adaptations — all predeclared above. The pivot arithmetic, CCI window, ADX veto, SMA gate, opposite-signal exit, and long-side entry conjunction are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: pivot width / CCI length-trigger-window / ADX length-threshold-count / SMA length / MACD lengths / disabled short arm / single-unit long-only / `1m` BTCUSDT spot / same-bar-close fills are frozen.

- F1 — ADX-veto relevance: dropping the all-ten `<=25` veto (same pivot-plus-CCI-plus-SMA entry, same exit) must not improve net expectancy; fail ⇒ the sideways veto adds nothing over the unvetoed pivot state.
- F2 — CCI-window relevance: replacing the twelve-bar ±150 recency window with a single-bar extreme print (same pivot-plus-SMA entry, same exit) must not improve net expectancy; fail ⇒ the window adds nothing over the single-bar extreme.
- F3 — SMA-gate relevance: dropping the `C > SMA400` direction conjunct (same pivot-plus-CCI entry with ADX veto, same exit) must not improve net expectancy; fail ⇒ the slow-average gate adds nothing over the ungated setup.

## Crypto portability

Binance BTC-USDT spot 1m only, under this record's identity. No leverage, funding, or margin; porting to another spot pair/timeframe is a new identity, not covered here. The long-only book needs no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count, portable across 24/7 crypto tape. Only standard OHLC candle fields are read (`high`/`low`/`close` for CCI/ADX, `close` for MACD/SMA); no exotic feed is required.

## Limitations

- TA-Lib CCI/ADX/MACD/SMA internals (typical-price averaging, Wilder/EMA seeding, histogram differencing) live in their library outside the pinned file — pinned by call with the filed lengths, not re-derived; exact reproduction inherits those modules' seeding and rolling semantics alongside the file-local wiring, under the disclosed 400-bar floor.
- Researcher-chosen (not source-native): Binance BTC-USDT spot market, 1m frame, disabled short arm, same-bar-close fill convention, 0.001 BTC size, 400-bar warmup, 0.0002/side hypothetical cost, next-bar re-arm with no cooldown, end-of-sample mark (not close). No historical backtest statistics reproduced; no Qlib parity, survivor label, trading approval or deployment. Before mass Qlib screening, any *new* execution primitive/data requirement must receive representative Qlib/Hummingbot event-level parity; strategy-specific final HB certification is downstream.
- The unit-test fixture timeframe and the repository's non-production self-description constrain nothing in this record and license nothing beyond it.

## Implementation status

`not-implemented`: no controller, config, or Qlib recipe ships with this record. Downstream materialization via `IMPLEMENTATION_NEEDED` only, never a second admission flag.

## Adoption boundary

`research-only` / `not-approved`. PASS here admits the declared derivative to model-consistent research; it authorizes no Paper/Testnet/Live trading.

## Related Wiki records

None.

## Sources

- https://github.com/Haehnchen/crypto-trading-bot/blob/cb9563344a20ea7ac89ff214d350f141d1521219/src/strategy/strategies/cci_macd.ts
- https://github.com/Haehnchen/crypto-trading-bot
