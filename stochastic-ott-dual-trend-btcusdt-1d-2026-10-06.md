---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Stochastic OTT dual-trend system on BTCUSDT 1d bars
created: 2026-10-06
updated: 2026-10-06
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-06
sources:
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E9%9A%8F%E6%9C%BAOTT%E4%BA%A4%E6%98%93%E7%AD%96%E7%95%A5Stochastic-OTT-Trading-Strategy.md
  - https://www.fmz.com/strategy/432849
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Stochastic OTT dual-trend system on BTCUSDT 1d bars

## Provenance

Immutable source actually read end to end (primary artifact for all rule citations):

- Repository URL: https://github.com/fmzquant/strategies (open FMZ strategy mirror with Pine blocks, argument tables, and FMZ Detail links; no LICENSE file ships in the mirror).
- Pinned commit SHA: `7853bb2bf262c4567ac238d3552d97f0e50cb801` (`ls-remote` HEAD check on 2026-10-06 confirms this is still the repository head, same pin as the Gann HiLo, VIDYA momentum, P-Signal, Bookstaber, and Flying Dragon admissions).
- Exact file path: `随机OTT交易策略Stochastic-OTT-Trading-Strategy.md` (non-ASCII filename preserved verbatim; percent-encoded blob URL above).
- Git blob SHA at the pinned commit: `6f13418642b40d81b72a7210e94cd1d1fd931089`, size 14324 bytes, 417 lines (verified by `git hash-object` reproducing the same SHA).
- Byte-identity check: the blob re-fetched via the GitHub blob API at the pinned SHA is byte-identical (`cmp` clean on re-download); SHA-256 `2d5acfd37b9462c3168dde395621458b911a191b7a1361bc5cd25e832da950f3`.
- The file is an FMZ strategy page: `> Name` (Stochastic-OTT-Trading-Strategy), `> Author` = ChaoZhang (mirror), Pine header prints `// © BigCoinHunter` and `// This source code is subject to the terms of the Mozilla Public License 2.0`, `> Strategy Arguments` table, `> Source (PineScript)` fenced `//@version=5` block, `> Detail` = https://www.fmz.com/strategy/432849, `> Last Modified` = 2023-11-22 10:11:33. This record normalizes the rule and reproduces no source code block.
- The FMZ backtest header inside the Pine block pins `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`, window `2022-11-21 00:00:00 → 2023-11-21 00:00:00`.

Pre-write dedup (2026-10-06): case-insensitive search of the working tree for `stochastic-ott`, `ottfast`, `ottslow`, `ottstoch`, `bigcoinhunter`, `432849` returns no strategy record using this source or signal. `gh pr list --state open` shows only PR #33 on a `reconstruction/*` lane (Wasserstein portfolio family, different mechanism and lane), so no open `research/*` PR shares this source or signal. Against the 13 PASS records on `main` (Bookstaber ATR breakout, DMI Swings ADX-45 exhaustion, Donchian 20/10 breakout, DRM dynamic RSI, EHMA range band, EMA 20/50 cross, Flying Dragon offset-MA band, Gann HiLo, Ichimoku + ADX, Monday Drift calendar hold, P-Signal erf dead-band, Kaufman pivots, VIDYA + CMO) plus closed research PRs (#6 LazyBear WaveTrend, #10 golden/dead MA cross, #17 MACD histogram zero-cross, #20 Ichimoku-RSI): no OTT record exists anywhere, no Stochastic-oscillator record exists anywhere, and no dual-OTT-trailing-stop record exists anywhere — mechanism, signal construction, and source identity are all distinct.

## Economic mechanism

### Source-reported

The source claims only qualitative behavior (no performance numbers are printed anywhere in the file): the OTT indicator has good reversal sensitivity and catches turning points; the Stochastic oscillator filters fake signals and avoids consolidation traps; the MA type is customizable for flexibility; TP/SL points make risk controllable. The Chinese and English description blocks agree on this four-point account. No behavioral, structural, or risk-premium channel beyond short-term reversal plus filter is claimed.

### Research interpretation

Falsifiable hypothesis: 1d dual-OTT trailing-stop flips capture multi-day trend turns — a fast OTT line (1-bar SMA ± 3%) printing above the slow OTT line (1-bar SMA ± 10%) signals buying pressure strong enough to carry for days, while the cross back below signals the turn has failed. The Stochastic-OTT confirmation leg is disabled by default and forms no part of the pinned signal. This is a ported reversal-trend hypothesis; the source supplies no quantitative evidence (see Evidence), so the mechanism is research interpretation, not source-reported fact.

## Signal

All symbols below are the program's own identifiers; all values are program defaults, pinned.

Engine semantics (explicit in source): `pyramiding = 0`, `process_orders_on_close = true`, `default_qty_type = strategy.percent_of_equity`, `default_qty_value = 100`, `initial_capital = 1000`, `commission_type = strategy.commission.percent`, `commission_value = 0.05`. Completed-bar decision with same-bar-close execution; `calc_on_every_tick` and `calc_on_order_fills` are omitted and take Pine v5 defaults (no intrabar evaluation; fills at close). No `strategy.order` call exists anywhere in the file (verified by full-file search).

Inputs (defaults):

```text
src = close (OTT source), src1 = close (Stoch OTT source)
ottFastPercent = 3.0, ottSlowPercent = 10.0
ottFastLength = 1, ottSlowLength = 1
periodK = 500 (%K Length), smoothK = 200 (%K Smoothing)
stochLength = 2, stochPercent = 0.5
mav = "SMA" (options SMA|EMA|WMA|TMA|VAR|WWMA|ZLEMA|TSF)
tp = 0.0, sl = 0.0 (both disabled by default)
stoch = false (Stochastic confirmation OFF by default)
longEntry = true, shortEntry = true (both sides ON by default)
fromYear/Month/Day = 2021/1/1, toYear/Month/Day = 2022/12/30 (Pine window gate)
```

OTT lines (exact, causal — pinned to `mav = "SMA"` default; the seven non-default MA branches are dead code with defaults):

```text
MAvg1 = ta.sma(close, 1), fark1 = MAvg1 * 3.0 * 0.01
longStop1 = MAvg1 - fark1, shortStop1 = MAvg1 + fark1 (trailed with nz/max/min vs prior bar)
dir1 flips to 1 when MAvg1 > prior shortStop, to -1 when MAvg1 < prior longStop
MT1 = dir1 == 1 ? longStop1 : shortStop1
OTTFast = MAvg1 > MT1 ? MT1 * 203/200 : MT1 * 197/200
MAvg2 = ta.sma(close, 1), fark2 = MAvg2 * 10.0 * 0.01 (same trailing construction)
OTTSlow = MAvg2 > MT2 ? MT2 * 210/200 : MT2 * 190/200
long = true when OTTFast > OTTSlow, false when OTTFast < OTTSlow (level, not cross)
```

Signal legs (pinned defaults `stoch = false`, both entries true):

```text
buySignall = window() and long and (not stoppedOutLong)
sellSignall = window() and (not long) and (not stoppedOutShort)
if long -> strategy.entry("LONG", strategy.long, when = buySignall)
else    -> strategy.entry("SHORT", strategy.short, when = sellSignall)
```

The `stoch = true` branch (`k1 > OTTStoch` / `k1 < OTTStoch` with `periodK = 500`, `smoothK = 200`, `stochLength = 2`) is computed but never gates a signal with defaults; it is recorded as explicitly disabled by default, not as part of the pinned signal. The single-side `longEntry`-only / `shortEntry`-only branches (with `strategy.close`) are likewise dead with both-defaults-true.

Direction: two-sided at pinned defaults (both `longEntry` and `shortEntry` default true; both `strategy.long` and `strategy.short` entries present). Spot-incompatible as pinned (short leg requires margin); the house futures overlay applies.

Exits and risk (explicit): opposite-signal exit via reversal entry (with `pyramiding = 0` a trend flip closes the prior leg and opens the opposite — the same reversal-only construction as the admitted Flying Dragon record). The six `strategy.exit` TP/SL calls all require `tp > 0` / `sl > 0`; with pinned `tp = 0.0` and `sl = 0.0` none can fire, recorded as explicitly disabled, not as defaults to be assumed. No trailing stop, no time limit in source.

Position and re-entry (explicit): `pyramiding = 0` rejects same-side re-entry while positioned; the `stoppedOutLong/Short` flags additionally allow only one entry per trend leg (set true on entry, cleared only when the trend flips). After a flip the opposite `strategy.entry` is the only possible next event — fully specified, no fixed-bar cooldown in source (recorded as none; re-entry is governed by trend flip, not by a missing timer). No `position_size` gate conditions entries; `position_avg_price` is read only inside the disabled TP/SL price definitions.

Conflict priority (provably irrelevant): `buySignall` requires `long == true`, `sellSignall` requires `long == false` — both jointly true would require `long` true and false on the same bar, impossible. No priority rule is needed and none is missing.

Determinism note for the reviewer: the pinned signal uses only `ta.sma` over `close` plus `nz`/`math.max`/`math.min` trailing-stop recursion — no `request.*`, `security()`, `barstate.*`, `timeframe*`, `volume`, `funding`, `heikin`, `session`/`dayofweek`/`hour`, or cross-venue state anywhere in the file (verified by full-file search returning zero matches). The file's only `time` read is the window gate.

## Required data

- 1d bars of one pair: `open/high/low/close/volume` with the pinned signal reading `close` (both OTT MAs), `high`/`low` (Stochastic leg only, disabled by default; still listed for completeness), and `time` (window gate only). No indicator beyond deterministic candle-derived MAs and the disabled Stochastic leg.
- No funding, OI, mark/index price, liquidation, trade/aggressor, L2/order-book, on-chain, options/Greeks, sentiment/news, macro, or cross-venue state is referenced or required.
- Warmup is derivable and exact: 500 bars (the max of all file lookbacks: `periodK = 500`, `smoothK = 200`, `math.sum(..., 9)`, `stochLength = 2`, OTT lengths 1). The used-signal leg alone steadies in 2 bars (trailing-stop recursion plus direction state); 500 is the conservative full-file bound covering the always-computed but unused Stochastic leg. Deterministic, no invention.

## Execution assumptions

- Source execution semantics: `process_orders_on_close = true` on 1d bars — the OTT-level decision is made on the completed bar and filled at that same bar's close. Compatible with the pinned Hummingbot baseline lane; no conversion required.
- Research market (explicitly labeled house overlay, not source-native): `BTCUSDT`, `1d` decision timeframe. The FMZ backtest header pins `period: 1d` on `BTC_USDT` (Binance Futures); the record uses the same BTCUSDT 1d klines. No price-series substitution is performed. The downstream futures overlay (Isolated 3x/5x, pinned fees plus realized funding) is event-neutral accounting on this rule — funding accrues only while positioned (flat periods accrue nothing) and changes no signal, event, direction, or exit.
- Source sizing (`strategy.percent_of_equity`, 100) and the source commission model (0.05% per side) are event-neutral accounting: replaced downstream by the standard house execution overlay (Base 6% + Safety 6% + 6%, Isolated, 3x/5x, pinned Binance fees plus realized funding). The overlay changes no signal, event, or exit.
- Window inputs (Pine `window()` 2021-01-01 → 2022-12-30; FMZ backtest 2022-11-21 → 2023-11-21) are backtest scope, not signal: entries fire only inside the Pine window and the FMZ header scopes the mirror run. Both facts are pinned as read — the OTT cross rule itself is window-independent. Downstream must state which scoping it applies; it must not silently re-tune the window on final OOS data.

## Evidence

### Source-reported

No quantitative performance is printed anywhere in the file: there is no returns table, no trade count, no win rate, no profit factor, and no drawdown figure — only a backtest screenshot image link (`upload/asset/17ceb09463a27cc0669.png`, not transcribed) and the qualitative four-point advantage/risk prose summarized above. Exact empirical numbers therefore require no provenance because none are claimed; nothing is invented here.

### Independently reproduced

Not independently reproduced.

### Negative evidence

No contradictory performance or failure report is cited in source. One honest default-configuration note: with pinned `tp = 0.0` / `sl = 0.0` the strategy runs without any protective stop — tail risk on vertical adverse moves is borne fully by the opposite-signal reversal. Recorded as explicitly disabled per source — must not be "repaired" with an invented stop. The absence of further evidence is recorded as absence, not as support.

## Falsification plan

Research tests only — none of these substitutes for a missing rule (no rule is missing):

1. Percent-band swap: run fast 10% / slow 3% (inverted) and fast 3% / slow 3% (symmetric); a rule whose sign depends on the exact 3/10 pair rather than on OTT-turn persistence is curve-fit, not signal.
2. MA-type stability: re-run with `mav = "EMA"` holding lengths at 1; a sign flip concentrated in the SMA-only default rejects robustness (the default is pinned, not to be re-tuned on final OOS data).
3. Stochastic-filter placebo: enable `stoch = true` holding all else at defaults; the filter leg must earn its 500-bar warmup with a stability gain, otherwise it is dead weight, not signal.
4. Subperiod stability: split any downstream 1d history into halves; a sign flip or collapse concentrated in one half rejects robustness (neither the Pine window nor the FMZ window may be re-tuned to rescue it).
5. Cost sensitivity: re-run with round-trip costs doubled; an OTT-turn edge that needs sub-5-bps costs to survive is execution fiction, not signal.

## Crypto portability

The rule ports cleanly to 24/7 crypto bars: no session calendar, no gap logic, no dividends/splits, no exchange-timezone call beyond the fixed window constants already in source. Two port notes: (a) the pinned defaults admit entries only inside the hardcoded Pine window, so a downstream run on full BTCUSDT 1d history must explicitly declare its window scoping rather than inheriting a 2022-12-30 cutoff silently; (b) crypto 1d trends can hold one OTT side for weeks, which exercises the single-entry-per-leg path for long stretches — expected behavior, not a bug.

## Limitations

1. No protective stop exists at pinned defaults; tail risk is borne fully by the reversal exit. Recorded as explicitly disabled per source — must not be "repaired" with an invented stop.
2. The fixed backtest windows are part of the pinned defaults. The OTT cross rule itself is window-independent, but any downstream run must state its scoping; re-tuning the window, the 3/10 percents, or the MA type on final OOS data is forbidden by the house overlay contract.
3. The always-computed Stochastic leg (`periodK = 500`) forces a conservative 500-bar warmup even though it never gates a default signal; downstream must not mistake warmup data cost for signal content.
4. Confidence is `medium` (interpretation confidence): the rule text is complete and unambiguous with an active `strategy()` declaration, but the source is an FMZ mirror page (mirror author ChaoZhang, Pine author BigCoinHunter) offering only qualitative prose and a screenshot, no peer review, and no market-microstructure account of 1d OTT-turn persistence.
5. Only program defaults are pinned. Input variants (different percents, lengths, MA types, enabled Stochastic filter, enabled TP/SL) are research tests, not separate strategies, and must not be cherry-picked.
6. The short leg requires margin; a spot-only downstream cannot run the pinned two-sided rule losslessly and must state any long-only restriction as its own overlay choice, never as source semantics.

## Implementation status

- `not-implemented`. No Hummingbot/Qlib/n8n/Paper/Testnet/Live work has been performed or is authorized by this record.

## Adoption boundary

- `research-only`, `not-approved`. Admission of this record would mean only that its core signal and causal trade-event semantics are losslessly expressible under the pinned backtester with the labeled house overlay — not profitability, survival, or any trading approval.

## Related Wiki records

- None. No Wiki Brain write was performed for this cycle.

## Sources

- Immutable mirror file at pinned commit (all rules): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E9%9A%8F%E6%9C%BAOTT%E4%BA%A4%E6%98%93%E7%AD%96%E7%95%A5Stochastic-OTT-Trading-Strategy.md
- FMZ strategy detail page (mirror `> Detail`, corroboration only): https://www.fmz.com/strategy/432849
- Repository (mirror context): https://github.com/fmzquant/strategies
