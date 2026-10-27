---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Freqtrade MACDRSI200 MACD-cross RSI-washout EMA200-gated long-flat on BTCUSDT 5m bars
created: 2026-10-28
updated: 2026-10-28
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-11-05
sources:
  - https://github.com/davidzr/freqtrade-strategies/blob/9623c1f3d8c7f60c8b411010fa26377e6ca99ab9/strategies/MACDRSI200/MACDRSI200.py
  - https://github.com/davidzr/freqtrade-strategies/tree/9623c1f3d8c7f60c8b411010fa26377e6ca99ab9
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade MACDRSI200 MACD-cross RSI-washout EMA200-gated long-flat on BTCUSDT 5m bars

## Provenance

**Primary source (immutable, read end to end this cycle):** repository `davidzr/freqtrade-strategies`, pinned commit `9623c1f3d8c7f60c8b411010fa26377e6ca99ab9` (committed `2023-11-05T15:22:08Z`, message `initial commit`; verified as the repository HEAD via `git ls-remote` during this cycle — record `source_as_of` is that commit date, never a fetch date). Exact file path: `strategies/MACDRSI200/MACDRSI200.py`. Class `MACDRSI200(IStrategy)` (the only class in the file).

- GitHub contents API at the pin returns blob SHA `a7803e5f83d79a36edb1cbec67758b637176c782`, size 1979 bytes.
- Byte-identity check: the file fetched at the pinned commit is 1979 bytes, 64 lines, SHA-256 `2a562c45320ca466e129c179594d0cba2364e111bead419abe09b3c8f8e14bc3`, and local `git hash-object` reproduces `a7803e5f…176c782` — the entire file was retrieved and inspected, not sampled.
- Old-framework markers (quoted, never modernized): `ticker_interval = '5m'` (pre-`timeframe` API); `populate_buy_trend` / `populate_sell_trend` writing the legacy `'buy']` / `'sell']` columns; no `INTERFACE_VERSION` literal ships anywhere (the single case-insensitive `interface` hit is the `from freqtrade.strategy.interface import IStrategy` import line). No author header ships in the file.
- Source-verbatim trading configuration (quoted): `minimal_roi = {"0": 0.03024, "296": 0.02924, "596": 0.02545, "840": 0.02444, "966": 0.02096, "1258": 0.01709, "1411": 0.01598, "1702": 0.0122, "1893": 0.00732, "2053": 0.00493, "2113": 0}`; `stoploss = -0.04032`. No `trailing`, no `startup_candle_count`, no `use_sell_signal` / `sell_profit_only` override, no `can_short`, no `process_only_new_candles`, no `position_adjustment`, no `protections`, no `leverage`, no order-type mapping ships anywhere.
- Source-verbatim signal code (quoted): indicators use TA-Lib through `import talib.abstract as ta` (never the `ta` Python package — no `ema_indicator` / `stochrsi` calls anywhere): `ta.EMA(dataframe, timeperiod=200)`; `ta.MACD(dataframe, fastperiod=24, slowperiod=56, signalperiod=6)`; `ta.RSI(dataframe)` twice (plain `rsi` and a dead `sell-rsi` column, fenced below). Buy leg: `(rsi.rolling(8).min() < 41) & (close > ema200) & (qtpylib.crossed_above(macd, macdsignal))` → `'buy'] = 1`. Sell leg: `(rsi.rolling(8).max() > 93) & (macd > 0) & (qtpylib.crossed_below(macd, macdsignal))` → `'sell'] = 1`.
- Out-of-file calls pinned by name (both standard, disclosed as external): `ta.EMA` / `ta.MACD` / `ta.RSI` (TA-Lib semantics: SMA-seeded EMA, Wilder RSI with default `timeperiod=14`); `qtpylib.crossed_above(a, b)` / `crossed_below(a, b)` (edge detectors on consecutive completed bars — their internal arithmetic lives outside this file and is never re-derived here). No DB, no network, no `request.*`, no `security()`, no session/calendar call in the file.
- Full-file token census (verified over the 64 lines this cycle): 0 `short` (no short leg anywhere); 0 `trailing`; 0 `volume` (no volume read anywhere — the rule is pure close-price); 0 `position_adjustment` / 0 `protections` / 0 `leverage` / 0 `cooldown` / 0 `max_open_trades` / 0 `startup_candle` / 0 `can_short` / 0 `informative` in code (the position pin below is a predeclared researcher rule, never a file semantic); `sell-rsi` is computed but never read by any order line (display-only, fenced below).
- The file ships no market, no sizing, no fee/funding concept, and no performance figure (no backtest table, no trade count, no window) — this record adopts no source-reported performance (see Evidence).

**Independent derivative — NOT source-native or lossless:** researcher-declared adaptations are exactly: (1) market **Binance BTCUSDT spot 5m** (the source names no market; no timeframe adaptation — the source is already 5m); (2) **completed-bar close-effective MARKET** fills (the old file ships no order-type mapping; framework intrabar sequencing is not reproduced); (3) source ROI ladder and stoploss kept **verbatim** as the risk legs (values below, including their fitted-looking five-decimal precision — preserved, never re-fitted, never endorsed); (4) fixed **0.001 BTC** sizing on 10,000 USDT unborrowed cash with hypothetical **0.01% per-side** simulator cost (the source ships no sizing or cost basis); (5) warmup adopts **210 consecutive valid completed 5m bars**, flat before that by record rule (the source ships no `startup_candle_count`; the pin covers the EMA200 seed plus every read — see Required data); (6) exits evaluated at each completed bar close in the fixed priority **stoploss > ROI ladder > signal exit**, full close, all-or-nothing. All six choices can change source trades and are evaluated only as this independently specified executable research strategy.

**Immutable identity:** `FT:MACDRSI200:davidzr@9623c1f3 | independent-derived-v1:2026-10-28 | MACD(24,56,6)-cross:talib | RSI14-8bar-washout:BUYmin<41/SELLmax>93 | EMA200-gate | ROI-ladder11+SL4.032pct-verbatim | BinanceSpot:BTC-USDT:5m:LONG-FLAT:0.001BTC | completed-close-MARKET:SL>ROI>signal`. Any change in windows, thresholds, operators, market, clock, size, cost, state, priority, or fill model is a different research version.

**Pre-write dedup (2026-10-28, main SHA `430e70b`):** current `main` has 393 root-level strategy Markdown records and README pool count 393. Working-tree filename/content searches for `MACDRSI200`, `macdrsi`, `fastperiod=24`, `slowperiod=56`, and `rolling(8)` return zero records. All 10 currently open `research/*` PRs were inspected (#48 Larry Williams streak, #49 Gaussian StochRSI, #63 SuperTrend flip, #89 Chandelier Exit, #92 SSL channel, #251 Swift 2YMA, #304 Forven CCI, #331 AdxSmas, #350 ClucMay, #353 Heracles Keltner-Donchian) — none cites this source or any MACD(24,56,6)-plus-RSI-washout rule. The closed-PR sweep (recent closed research PRs #480–#539, including #502 Bandtastic 15m, #515 SmoothScalp 1m, #478 RobotradingBody 4h, #481 TrueStrategy-Ichimoku 15m, #539 MultiRSI 5m) plus repo issue/PR search for `MACDRSI` returns no same-source or same-rule candidate. Closest pool mechanisms are fenced as different constructions: (a) `freqtrade-macd-cci-dip-state-…` trades a MACD **level** with a **CCI** dip on standard periods — this candidate trades a MACD **cross edge** with an **RSI rolling-window** washout on non-standard (24,56,6) periods; (b) `freqtrade-macd-cross-cci-edge-…` trades a MACD cross with a **CCI edge** and no trend gate — this candidate gates on **close > EMA200** and exits on an RSI-93 extreme; (c) `freqtrade-awesome-macd-…` and `forven-macd-cross-adx-regime-…` use AO / ADX-DI confirmation, never an RSI washout; (d) `forven-ema-rsi-pullback-reclaim-…` has an EMA+RSI pullback but no MACD leg at all. No duplicate source or materially identical normalized rule was identified.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy the bar where the intermediate trend filter is satisfied (close above EMA200), short-horizon momentum just washed out (14-bar RSI printed under 41 at least once in the last 8 bars), and momentum turns (MACD(24,56,6) crosses above its signal line); exit when momentum is extremely overbought (RSI printed above 93 at least once in the last 8 bars) while MACD stays positive and crosses back below signal. An 11-rung declining ROI ladder (3.024% immediate down to breakeven after 2113 minutes) and a −4.032% stoploss backstop every position. No behavioural, structural, or risk-premium channel is claimed anywhere in the 64 lines.

### Research interpretation

A patient trend-following trigger with a washout lock, long-only. Unlike pure MACD-cross records that buy every golden cross including counter-trend chop, the EMA200 gate plus the RSI-washout precondition refuses crosses that arrive without a preceding dip — the cross must be a recovery, not a drift. Unlike level-based RSI records (buy every sub-threshold print), the cross requirement refuses washes that never turned. The exit is deliberately asymmetric and rare: RSI must have screamed above 93 within 8 bars while MACD rolls over — most positions therefore close through the ROI ladder or the stop, so the book behaves as a time-decaying profit harvester with an overbought-ejection override. The coded consequence is a buyer of confirmed post-dip trend resumption that banks measured profit quickly and ejects only on genuine exhaustion.

## Signal

Exact rule as pinned (any other MACD period triple, RSI length, washout window, threshold, EMA length, price basis, ROI/SL pair, priority, fill, frame, book, or leg combination is a different, unpinned rule). All identifiers below are the program's own:

```text
ema200[t]     = TA-Lib EMA(close, 200)                  // SMA-seeded
macd[t]       = TA-Lib MACD(close, 24, 56, 6).macd
macdsig[t]    = TA-Lib MACD(close, 24, 56, 6).signal
rsi14[t]      = TA-Lib RSI(close, 14)                   // Wilder smoothing
rsi8min[t]    = min(rsi14[t-7 .. t])
rsi8max[t]    = max(rsi14[t-7 .. t])
x_up[t]       = (macd[t] > macdsig[t]) AND (macd[t-1] <= macdsig[t-1])
x_dn[t]       = (macd[t] < macdsig[t]) AND (macd[t-1] >= macdsig[t-1])
entry         = (rsi8min[t] < 41) AND (close[t] > ema200[t]) AND x_up[t]       // buy = 1
exit_sig      = (rsi8max[t] > 93) AND (macd[t] > 0) AND x_dn[t]                // sell = 1
risk          = 11-rung ROI ladder {"0":0.03024,"296":0.02924,"596":0.02545,"840":0.02444,
                "966":0.02096,"1258":0.01709,"1411":0.01598,"1702":0.0122,"1893":0.00732,
                "2053":0.00493,"2113":0} (minutes since entry -> minimum profit fraction)
                plus fixed stop at -4.032% (stoploss -0.04032)
guard         = leading-window bars: every rolling/seeded comparison over NaN is false (see Required data)
```

- Trade events: `buy=1` on any bar printing the three-conjunct entry, direction long-only; `sell=1` on bars printing the three-conjunct signal exit. Both legs are levels that can reprint across consecutive bars (no one-shot latch in code).
- Exact boundaries (pinned semantics): entry conjuncts strict (`<`, `>`, strict cross edges — RSI exactly 41, a close exactly on EMA200, or a MACD exactly on signal fires nothing); exit conjuncts strict (`>`, `>`, strict cross edge). Strictness preserved throughout — disclosed, not smoothed.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `x_up[t]` (requires `macd[t] > macdsig[t]`) while any signal-exit bar has `x_dn[t]` (requires `macd[t] < macdsig[t]`) — entry and signal-exit never co-print on any bar, degenerate or otherwise. ROI/stop cannot co-fire with entry on the entry bar either (zero distance at the fill). The reviewer is never asked to invent an ordering.
- Direction: long-only. Zero `short` tokens ship anywhere and the old-framework default carries no short leg — a two-sided reading would contradict the file. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit, single priority): on every completed bar close while positioned, evaluate in the fixed order **stoploss first, then the ROI ladder rung for the elapsed minutes, then the signal exit**; the first firing leg closes the full position; no partial closes, no second evaluation pass on the same bar. No trailing, no time exit, no breakeven move — explicitly none, not invented.
- Position rule (predeclared researcher pin): single-unit 0.001 BTC, at most one open position per market; a positioned book treats further entry bars as hold-no-ops (no pyramiding, no averaging — no `position_adjustment` ships anywhere); a flat book treats exit/risk legs as no-ops; re-entry re-arms on any qualifying entry bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar closes (EMA/MACD/RSI all consume `close`; the file never reads `high`/`low`/`open` in any gating line) with fixed non-negative offsets — no `volume`, no funding/OI/mark-price read, no `request.*`, `security()`, session/calendar call, or stop/limit order argument anywhere in the gating path. The legacy `'buy']`/`'sell']` per-completed-bar column semantics are the file's own framework contract; this derivative keeps the completed-bar clock and replaces only the fill/sequencing with the single rule in Execution assumptions.

## Required data

- Completed `5m` bars of BTCUSDT: `close` only. No `high`/`low`/`open` in any gating line, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (the file defines no `informative_pairs` method).
- Single decision timeframe `5m` (source-native — the file prints `ticker_interval = '5m'`). One evaluation per completed bar; the 200-bar EMA, the 56-bar MACD leg, the 14-bar RSI, and the 8-bar washout windows read the decision bar and its causal past only — no shift tricks, no future reference; fills land on the decision bar's own close under the derived rule.
- Warmup (researcher pin, disclosed): 210 consecutive valid completed 5m bars held flat. Covers the EMA200 seed (TA-Lib first valid output at index 199), the MACD signal seed (first valid at index 60), the RSI seed (first valid at index 14), and the 8-bar washout reads, with margin. Coded behaviour underneath: seeded windows print NaN until valid and every strict NaN comparison is false — no leg can fire early (verified: zero entry/exit bars before index 210 over 1000 live bars). No repainting, no negative shift, no future bars/extrema, no full-sample normalization. The `sell-rsi` column is computed but never read — fenced as display-only, never gated.

## Execution assumptions

- Research market: BTCUSDT Binance spot 5m under the house overlay (researcher choice — the source names no market; venue spelling and symbol normalization are the only market steps, and no source-market equivalence is claimed).
- Order timing (derived, disclosed, single rule): completed-bar decision with same-bar-close MARKET fills — the decision bar's own close, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) via the same bar-close lane primitive the admitted Freqtrade-sourced 5m siblings (`freqtrade-cofibit-stochf-ema-rail`, `freqtrade-combined-binh-cluc`, `freqtrade-universalmacd`) use; the admitted 1m Low_BB derivative further bounds this frame from below. No maker-touch, queue, or intrabar-path-dependent fill: entry, the signal exit, and the ROI/stop legs are all bar-close-evaluated in the Signal priority; legacy framework intrabar sequencing is explicitly not reproduced. The Signal mutual-exclusion proof plus the fixed exit priority leaves no ambiguous same-bar fill order to the engine.
- Interval precedent (disclosed, not assumed): `5m` carries extensive PASS precedent on `main` — no novel-interval confirmation is required for this frame. Decision/availability timestamps, fills, costs, and leverage/margin accounting ride the specified path; pin fees/funding/precision downstream and never report hypothetical zero funding as realized funding.
- Sizing/capital/costs: the source ships no sizing, capital, fee, margin, or funding concept — its ROI ladder and stoploss percentages are preserved verbatim as the risk legs while sizing (fixed 0.001 BTC on 10,000 USDT unborrowed cash) and costs (hypothetical 0.01% per-side simulator cost; the source declares no funding treatment at all) ride the explicit researcher freeze under the single-unit/no-add position pin from Signal, never presented as source-native behaviour.
- Concurrency: at most one position per market at any time; the entry conjunction opens the full unit on a flat book; the stoploss, the ROI leg, or the signal exit closes it in full; re-entry after an exit needs only the next qualifying entry bar (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The file ships the full construction (64 lines: the TA-Lib EMA200 / MACD(24,56,6) / RSI calls, the two three-conjunct order legs, the `ticker_interval` / 11-rung `minimal_roi` / `stoploss` literals, and the `MACDRSI200(IStrategy)` class pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

On 2026-10-28, 1000 live Binance BTCUSDT 5m klines were evaluated with two independently written implementations (explicit-loop TA-Lib-style seeding vs separately written running-mean/recursion variant): all four indicator columns (EMA200, MACD line, MACD signal, RSI14) agree exactly (NaN masks plus values to 1e-9), and the full entry/exit signal columns are identical across passes. Post-warmup (bar 210) result: 3 entry bars (indices 263, 440, 669), 0 signal-exit bars, 0 same-bar entry/exit collisions, 0 pre-warmup signals. Hand-check of entry bar 263: close 80631.01 > EMA200 80618.44, 8-bar RSI minimum 31.243 < 41, MACD −77.6565 crossing above signal −77.9636 from below (−80.0839 vs −78.0865) — every conjunct prints as pinned. Earliest fully-valid bar indices observed (EMA200 199, RSI 14, MACD signal 60) confirm the 210-bar warmup covers all reads. No market-data, simulated-fill, or performance claim is made beyond these signal-column facts.

### Negative evidence

1. The signal exit is rare by construction (RSI must print above 93 within 8 bars while MACD rolls over from above zero): zero signal-exits fired in the 1000-bar verification window. The position economy therefore rides the ROI ladder and the stoploss most of the time — disclosed, not hidden; exit completeness never depends on the rare leg alone.
2. The 11-rung ROI ladder carries fitted-looking five-decimal values (0.03024 … 0.00493). They are kept verbatim as shipped literals and carry no endorsement of optimality; any re-fitted ladder is a different, unpinned rule.
3. The source is an old-framework file (legacy column names, no warmup literal, no order-type mapping, limit-order-era semantics). The MARKET-fill replacement, the 210-bar warmup, the fixed sizing/cost freeze, and the bar-close exit priority are researcher adaptations owned by this derivative — a source-native reading would need framework archaeology this record does not claim.
4. The `sell-rsi` column and the BB-style display columns some siblings carry are absent/unused here; nothing display-only gates any order.
5. Verification covers one 1000-bar (~3.5-day) live window for signal-column correctness only — not a backtest, not a profitability claim, not a fill-economics proof.
6. Nearest-pool cousins are fenced in Provenance as different constructions (MACD level-vs-cross, CCI-vs-RSI oscillator, ADX/AO confirmation, EMA200-gate presence) — none combines a MACD(24,56,6) cross edge with an RSI rolling-window washout and an EMA200 gate on one timeframe.

## Falsification plan

- Recompute the four indicator columns and both signal columns over any full Binance BTCUSDT 5m history with TA-Lib (or the dual-pass recipe above): any bar where the entry/exit columns diverge from the Signal formulas falsifies this record.
- Any entry or exit bar before 210 consecutive valid completed bars falsifies the warmup pin.
- Any bar co-printing entry and signal-exit falsifies the mutual-exclusion proof (requires `macd[t]` both strictly above and strictly below `macdsig[t]` — arithmetically impossible under the pinned formulas).
- A reviewer-side check that the pinned blob differs from `a7803e5f…176c782`, or that the davidzr pin `9623c1f3` does not contain this file at this path, falsifies the provenance.

## Crypto portability

BTCUSDT Binance spot 5m is the declared research market. The long-flat book (at most one unlevered long, full closes, no short leg, no margin call path) expresses unchanged on any BTC spot venue with 5m completed-bar closes; no perpetual, leverage, funding, or borrow concept is required. TA-Lib indicator arithmetic is venue-independent; only the close series moves. Finer (1m, per the admitted Low_BB derivative) and coarser (1h, per the admitted CrossEMA derivative) bar-close lanes already have PASS precedent in this pool — 5m sits between demonstrated bounds.

## Limitations

- The ROI ladder values look hyperopt-fitted; kept verbatim, never endorsed or re-tuned.
- Signal exits are rare (see Negative evidence 1) — time-decay ROI harvesting plus the wide-action stop do the economic work.
- Old-framework limit-order semantics were replaced by close-effective MARKET fills; framework intrabar sequencing is not reproduced — backtest numbers from the source framework, if any ever surface, are not comparable to this derivative.
- TA-Lib itself is version-unpinned by the source; the pinned semantics are SMA-seeded EMA, Wilder RSI(14), and consecutive-bar cross edges as verified.
- The source declares no fees, slippage, or funding; the 0.01% per-side figure is a simulator placeholder, and funding must be pinned downstream — never reported as realized zero.
- Single ~3.5-day verification window; no OOS, profitability, or Qlib-parity claim.
- Fixed 0.001 BTC sizing is a research freeze, not a capital recommendation.

## Implementation status

`not-implemented`: no dedicated implementation, deployment artifact, Qlib recipe, or execution binding ships with this record. Per the downstream invariant, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; when this strategy is formally selected for execution without a reproducible executable recipe, the engineering route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, then return to the same research flow without redoing HB_READY).

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission. No live, Paper, Testnet, or trading action is authorized by this record.

## Related Wiki records

None.
