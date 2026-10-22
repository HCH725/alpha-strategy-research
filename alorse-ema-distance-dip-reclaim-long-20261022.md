---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Alorse EMA distance dip-buy, body-vetoed, EMA-reclaim exit long-flat research derivative"
created: 2026-10-22
updated: 2026-10-22
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-22
sources:
  - https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/trend/EMA%20Moving%20away%20Strategy%20%5BAlorse%5D.pine
  - https://github.com/Alorse/pinescript-strategies
  - https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Alorse EMA distance dip-buy, body-vetoed, EMA-reclaim exit long-flat research derivative

## Provenance

- Primary original program inspected end to end: https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/trend/EMA%20Moving%20away%20Strategy%20%5BAlorse%5D.pine, commit `8fb3837ddcd137f1450c3e82d654ff3df24d54d5` (committed `2026-08-25T11:48:57Z`), file `strategies/trend/EMA Moving away Strategy [Alorse].pine`, Pine v5.
- Byte-identity check: the file fetched from `raw.githubusercontent.com` at the pinned commit is 1784 bytes, 44 lines, SHA-256 `c68da51ff0a411b0d26d2126f0a4a69c03ec6296dee3cdd9da6773f554dfa036`; `git hash-object` reproduces blob `68bf809fc4ac43badacf827208d6e749668369dc`, identical to the GitHub blob SHA at that commit — the entire file was retrieved and read.
- Source header (quoted, never extended): `strategy("EMA Moving away Strategy [Alorse]", overlay=true, pyramiding=0, currency=currency.USD, default_qty_type=strategy.percent_of_equity, initial_capital=1000, default_qty_value=10, commission_type=strategy.commission.percent, commission_value=0.01)`. No `process_orders_on_close`, no `calc_on_every_tick` — under Pine defaults the source's market orders fill at the next bar's open. No `request.security`, no multi-timeframe, no date-range filter, no hyperopt/optimizer import anywhere in the 44 lines.
- This candidate is an **explicitly derived research execution version** of the source's long leg only. Researcher-declared adaptations, predeclared here and nowhere else: (1) market pin `BTCUSDT` spot on Binance `1h` (the source names no market or venue); (2) long-only — the source short leg (`short_entry_condition`, short exit, short stop) is scoped out because spot cannot short, and the short-only `not last4CandlesGreen` filter goes with it; (3) completed-bar decision at bar `t` fills at the next simulator bar `t+1` **close** via a one-tick controller lag plus the native MARKET first-row-close primitive (the source fills next-bar open — the open-vs-close difference is an explicit derivation, divergence reported, never parity); (4) fixed 100 USDT entry notional from 1000 USDT starting capital with no compounding (the source's percent-of-*current*-equity compounding is explicitly not modeled); (5) fixed run fee `trade_cost=0.0001` numerically matching the source's 0.01% commission; (6) the source's intrabar stop becomes a completed-bar-close stop check under the fixed precedence below; (7) a 70-bar warmup floor (the source ships no warmup guard). Never presented as an author-native or economically equivalent backtest.
- Engine evidence anchored not to latest master but to existing `HCH725/hummingbot` commit `8b0e067e80ab62f10846d518dcb5a8218527ddb3`, dated `2026-09-20T12:10:22Z`; its `hummingbot/VERSION` is **dev-2.17.0**, matching the pinned Hummingbot VERSION and September-20 benchmark vintage. Full-source inspection and preexisting tests below. No fill logs or image digest invented.
- Pre-write dedup (2026-10-22): working-tree content search for `moving away`, `moving_away`, and the exact conjunction (distance-below-EMA55 × body-size veto × EMA-reclaim exit × 2% stop) returns zero strategy records. Nearest pool cousins are different constructions: `alorse-dmi-winner-threebar-di-ema55` gates on three-bar DMI with an EMA55 trend filter (no distance leg, no body veto, no reclaim exit); `ema-20-50-cross` is a naked EMA cross (no distance, no veto, different windows); `freqtrade-emaskippump` buys EMA-stack dips under a volume veto with BB confirmation (stack, not distance; different exit/risk); `forven-ema-rsi-pullback-reclaim` needs an RSI leg the source never reads. No open `research/*` PR (#48, #49, #63, #89, #92, #251, #304, #331, #350, #353) trades an EMA-distance dip rule. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: buy when price sits at least 2% below its own EMA55 while the current candle body is small (under 2% of open) — a quiet, non-capitulation discount — and stand aside back to flat when price reclaims the EMA55, with a 2% fixed stop behind every long. No behavioural, structural, or risk-premium channel is claimed anywhere in the 44 lines.

### Research interpretation

Patient mean-reversion dip machine, long-only. The distance leg supplies the edge (only stretched tape qualifies — price riding at or above the average buys nothing), while the body veto rejects the entry on violent expansion bars (a −5% crash bar prints no entry even 2% under the average — the discount must arrive quietly). Unlike cross records (fire on rotation timing), nothing here crosses anything: the book opens on position (distance) and closes on position (reclaim). The 2% stop mirrors the 2% entry distance one-for-one, so the stop is a symmetric invalidation of the discount thesis, not a tuned risk regime. The exit is deliberately slow — a market that bottoms 4% under the average and crawls back is held the whole way; only the reclaim or the stop ends it.

## Signal

Pinned source defaults (`src=close`, `length=55`, `moving_away=2`, `stop_loss_pct=2`):

```text
ema[t]      = ta.ema(close, 55)
lc_pct[t]   = abs((close[t]-open[t])/open[t]*100)
long_entry  = (close[t] <= ema[t]*(1-0.02)) AND (lc_pct[t] < 2)   // source long_entry_condition
reclaim     = (close[t] >= ema[t])                               // source Long close
stop_level  = fill_price*(1-0.02)                                // source Long SL from position_avg_price
floor       = leading-window bars: unseeded comparisons false (see Required data)
```

- Trade events: `Long` entry on a bar printing `long_entry` while flat; full close on a bar printing `reclaim` or breaching `stop_level` while held. `stop_level` is fixed at fill time from the single fill price (single-unit, no adds ever — there is no averaging for `position_avg_price` to average over).
- Exact boundaries (pinned semantics): the distance leg is inclusive (`<=` — a close exactly 2.000% under the average qualifies); the body veto is strict (`<` — a body exactly 2.000% of open fails it); the reclaim leg is inclusive (`>=` — a close exactly on the average exits). All preserved throughout.
- Mutual-exclusion proof (no tie-break pin required): any entry bar has `close <= 0.98*ema` while any reclaim bar has `close >= ema` — strictly disjoint on every bar with `ema > 0`, so entry and signal-exit never co-print. The stop leg exists only on a held book and the entry leg is evaluated only on a flat book, so stop and entry never compete either. On a held bar printing both reclaim and stop breach, the fixed precedence (stop first, then reclaim) closes the full unit flat either way — no intrabar ordering assumption is needed for the net state.
- Direction: long-only by derivation. The source short block (`short_entry_condition`, `strategy.entry("Short")`, short close, short stop) is scoped out in Provenance adaptation (2) — a two-sided reading would contradict this record. The long-only book expresses unchanged on a spot venue (see Crypto portability).
- Exits and risk (explicit, complete): the EMA-reclaim signal exit and the 2% fixed stop are the complete position-closing set. No take-profit, no trailing, no time exit, no breakeven move — the source ships none for the long leg, explicitly none here, not invented.
- Position rule (source-native, not invented): `pyramiding=0` — at most one open position; an entry signal while positioned is rejected (hold-no-op); a flat book treats exit/stop legs as no-ops; re-entry re-arms on any qualifying discount bar after any exit (no cooldown specified — explicitly none, not invented). Pre-first-signal and pre-warmup bars are flat by record rule.
- Determinism note for the reviewer: the rule reads only completed-bar `open`/`close` (distance, body, reclaim) plus the causal 55-bar EMA seed — fixed non-negative offsets, no forward reference. No `high`/`low` read, no volume read, no funding/OI/mark-price read, no `request.*`, no session/calendar call, no resample/interpolate, no fitted parameter anywhere in the 44-line gating path.

## Required data

- Completed `1h` bars of BTCUSDT spot: `open`/`close` only (entry distance, body veto, EMA55 seed, reclaim exit). No `high`/`low` read, no bar `volume` read, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, calendar, session-template, or cross-venue state is read by any order-gating line. No multi-symbol, multi-timeframe, or external-feed dependency of any kind (zero `request.*` calls in the file).
- Single decision timeframe `1h` (researcher choice — the file prints no timeframe; venue feed and symbol normalization are the only market steps, and no source-market equivalence is claimed). One evaluation per completed bar; every window reads the decision bar's causal past only.
- Warmup (researcher pin, disclosed): 70 one-hour bars held flat (~3 days). Covers the 55-bar EMA seed with margin. The file ships no warmup guard — quoted absence, never filled in from elsewhere. Coded behaviour underneath: unseeded EMA comparisons cannot fire the inclusive/strict legs early, and the record-rule floor holds every pre-seed bar flat regardless. No repainting, no negative shift, no future bars/extrema, no full-sample normalization. One evaluation per completed bar; the fill for decision bar `t` lands on bar `t+1`'s close, and `t+1`'s own signal is never used for that fill — no end-of-history phantom order.

## Execution assumptions — exact preexisting Hummingbot code path

- `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` has `hummingbot/VERSION=dev-2.17.0`. Specifically inspect `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py`: `BacktestingEngineBase.run_backtesting(controller_config,start,end,backtesting_resolution='1h',trade_cost=0.0001)` — `trade_cost` is an **explicit run input override** (the generic default at that SHA is `0.0002`, a different number); `prepare_market_data` merges timestamped spot OHLCV; `simulate_execution` visits each row and routes the controller's `CreateExecutorAction(OrderExecutorConfig)` through `simulate_executor` to `OrderExecutorSimulator` over the per-tick slice starting at the action row.
- `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py`: `execution_strategy=MARKET` fills at the first simulated slice row's `close` with that row's timestamp; fee `trade_cost * amount_quote`; returns `POSITION_HOLD`. The strategy-specific controller emits the stored completed-`t` decision at tick `t+1`, so the fill lands on `t+1`'s close — causally after the decision bar, with no same-bar decision/fill race and no maker-touch, queue, or intrabar-path-dependent fill.
- `BacktestPositionHold._process_order` in the backtesting tree nets BUY and SELL against one spot long and carries average acquisition cost, quote turnover and realized PnL/fees; a SELL for exactly the held base amount flattens it, never opens short.
- `hummingbot/strategy_v2/backtesting/backtesting_data_provider.py`: `get_candles_df` serving the Binance spot BTC-USDT `1h` feed; `initialize_trading_rules('binance')` and `quantize_order_amount` use actual Binance spot trade size increments. For any amount below min order notional or missing actual candle, that execution is omitted with explicit failure; no fake price, balance, or automatic accept. The 100 USDT notional sits far above spot minima, but the rule binds regardless.
- This primitive's `CreateExecutorAction` carrying `OrderExecutorConfig` with MARKET order types already appears in the version-pinned `controllers/generic/pmm_mister.py` for existing controller actions. Here a strategy-specific controller's source-signal calculation **has not been implemented**, as allowed by `implementation_status: not-implemented`; the admission verifies the already-existing execution primitive, not a finished strategy implementation. No new DSL/registry/admission gate.
- Existing version-pinned tests at `test/hummingbot/strategy_v2/backtesting/test_backtest_position_hold.py` (`test_buy_sell_netting`, `test_full_netting_closes_position`) plus `test_backtesting_final_tick_ledger.py` Binance spot final-row accounting cases. Tests inspected at this SHA but **not run** in this admission; no strategy-level backtest claimed.
- 1000 USDT starting research capital; 100 USDT fixed entry notional, no compounding (the source's 100%-of-*current*-equity sizing is different and explicitly not modeled). Match the exit BTC amount to the actual filled/quantized BUY base quantity. Fixed `trade_cost=0.0001` (0.01% one-way) chosen to numerically match the source's own commission; not purported actual Binance taker fee or VIP tier. Spread/slippage/maker queue NOT modeled, and results not sold as real net PnL. Spot has no perpetual funding or liquidation, so missing historical futures funding is not silently entered as zero. House 3x/5x futures and BO6/SO6/SO6 DCA are *separate* potential research variants, not the admitted spot signal record.

## Evidence

### Source-reported

The file ships the full construction (44 lines: the EMA55/body inputs, the long discount entry, the reclaim close, the 2% long stop, the scoped-out short block, and the strategy header pin). It ships no sample, window, trade count, or cost basis — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced. Version-aligned source code and preexisting tests are inspectable at the cited immutable SHAs. Gate 5 is a bounded research-simulator expressibility statement, not an assertion about live fills or a particular binary digest.

### Negative evidence

1. Leading-window behaviour fenced: the EMA55 seed cannot satisfy the inclusive distance leg before seeding, and the strict body veto on unseeded bars is likewise false — no leg can fire early. The 70-bar record-rule floor additionally holds every pre-seed bar flat — disclosed, not repaired. The file ships no warmup constant, so the floor is purely a researcher pin, never misattributed.
2. Exact-touch rule fenced: distance and reclaim are inclusive while the body veto is strict — a close exactly 2% under the average enters (body permitting); a body exactly 2% of open vetoes; a close exactly on the average exits. Strictness and inclusivity preserved throughout — disclosed, not smoothed.
3. Open-zero fence: `lc_pct` divides by `open[t]`; venue prices are strictly positive on the admitted domain, and a zero/negative open bar is outside that domain and produces no signal — coded fact, disclosed, with no invented guard.
4. Fill-timing fence: the source fills next-bar open under Pine defaults; this record fills next-bar (`t+1`) close via the disclosed one-tick controller lag plus the verified MARKET first-row-close primitive. The open-vs-close difference is an explicit derivation — divergence from the source fill is reported, never called parity.
5. Short-scope fence: the entire short block (entry with its `not last4CandlesGreen` filter, close, stop) is removed by researcher choice for spot long-only — disclosed in Provenance, never silently kept, and the `last4CandlesGreen` computation goes with it.
6. No-TP/trailing/time-exit fence: the long leg ships no take-profit, no trailing, no time exit — explicitly none, never to be added by repair. The 2% stop is the sole risk leg besides the reclaim exit.
7. Co-print arithmetic fenced (proven, not asserted): entry and reclaim need strictly disjoint close-vs-average regions; stop and entry live on opposite book states; stop-plus-reclaim on one held bar closes flat under the fixed precedence regardless of order. The reviewer is never asked to invent an ordering.
8. Cousin records fenced as different constructions (none conjoins an EMA-distance discount with a body-size veto, an EMA-reclaim exit, and a symmetric fixed stop, oscillator-free, on `1h`): the pool's EMA/dip cousins all carry an extra leg (DMI, RSI, volume, BB) or trade naked crosses/stacks the source never prints. Dropping the distance leg, the veto, or the stop, adding any oscillator, or changing any window/threshold/frame would each be a different, unpinned rule — none is admitted here.
9. Derivation boundary fenced: the only non-source-native behaviours in this record are the BTCUSDT-spot-`1h` market choice, the long-only scope, the `t+1`-close fills, the fixed-notional/no-compound sizing, the `0.0001` run fee, the bar-close stop evaluation with fixed precedence, and the 70-bar floor — all predeclared above. The EMA55 construction, the 2% distance, the 2% body veto, the reclaim exit, the 2% stop, and all comparison strictness are source-verbatim effective behaviour.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: EMA55 / 2% distance (inclusive) / 2% body veto (strict) / reclaim exit (inclusive) / 2% stop / single-unit long-only / `1h` BTCUSDT spot / `t+1`-close fills with fixed precedence are frozen.

- F1 — Distance relevance: replacing the discount leg with a plain below-average state (enter any close under EMA55 with the veto, same exit/risk) must not improve net expectancy; fail ⇒ the 2% stretch adds nothing over position alone.
- F2 — Veto relevance: dropping the body veto (pure distance entry, same exit/risk) must not improve net expectancy; fail ⇒ the quiet-arrival filter adds nothing over the discount alone.
- F3 — Stop relevance: removing the 2% stop (reclaim-only exits) must not improve net expectancy; fail ⇒ the symmetric stop adds nothing over the bare reclaim machine.

## Crypto portability

BTCUSDT Binance spot `1h` is the research pin (source names no market). Long-only with full-unit open/close expresses unchanged on any spot venue with no naked shorting. No session, calendar, or equity-hours concept is read anywhere — every window is a trailing bar count on the decision frame, portable across 24/7 crypto tape. No volume field is consumed at all. Funding is declared nowhere in the source and cannot arise on spot; any futures/DCA port requires its own explicit market and cost assumptions rather than silent universal compatibility.

## Limitations

- The source stop is an intrabar TradingView stop; this record evaluates the stop on completed-bar closes — a gap straight through the stop level exits at the close, not at the level. Disclosed derivation, not repaired; gap-through loss is unbounded by the level in the derived version.
- Pinned simulator `trade_cost` covers explicit per-side commission only — no spread, no slippage, no maker-depth queue, no real fee-tier mapping. Not sold as real net PnL.
- No source-native next-open fill parity or deployed controller is asserted; the controller remains `not-implemented` and only the preexisting MARKET primitive plus netting/accounting path is verified.
- A market that grinds sideways exactly on the average holds flat forever (no entry without the 2% stretch); a market that re-stretches after every reclaim re-enters without rest (no cooldown by design).

## Implementation status

`not-implemented` — no dedicated implementation/deployment artifact exists. Per the repository contract, `not-implemented` does not revoke HB_READY PASS or permit downstream research to refuse admission; if formally selected for execution without a reproducible executable recipe, the route is `IMPLEMENTATION_NEEDED` (add the minimal strategy-specific implementation, return to the same pipeline), never a second admission flag.

## Adoption boundary

`adoption: not-approved`, `approval_scope: research-only`, `status: research-only`. This record is downstream research admission only — not a profitability claim, not Qlib parity, not Paper/Testnet/Live permission.

## Related Wiki records

None — no Wiki Brain write was performed for this admission (Scout PR-only workflow).

## Sources

- Primary: https://github.com/Alorse/pinescript-strategies/blob/8fb3837ddcd137f1450c3e82d654ff3df24d54d5/strategies/trend/EMA%20Moving%20away%20Strategy%20%5BAlorse%5D.pine
- Collection: https://github.com/Alorse/pinescript-strategies
- Engine: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Engine version: https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/VERSION
- Existing tests: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3/test/hummingbot/strategy_v2/backtesting
- HB_READY contract: https://github.com/HCH725/alpha-strategy-research/blob/main/.github/HB_READY_REVIEW.md
