---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Freqtrade AverageStrategy EMA-8/21 mirror-cross volume-gated ROI/SL BTC spot 4h long-flat — independent derivative"
created: 2026-10-30
updated: 2026-10-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - freqtrade
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/AverageStrategy.py
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade AverageStrategy EMA-8/21 mirror-cross with volume gate and ROI/stoploss — BTC spot 4h independent research derivative

## Provenance

- **GitHub primary (immutable):** `freqtrade/freqtrade-strategies@f3340ce11f5bdf62f598522e64d1f5638eaa13f5`, file `user_data/strategies/berlinguyinca/AverageStrategy.py`, class `AverageStrategy` (author **Gert Wohlgemuth**; docstring: *"buys and sells on crossovers — doesn't really perform that well and its just a proof of concept"*). This cycle the raw file was fetched end to end (**2,630 bytes**, md5 `c395b86001b92cbe84f75cb4e68e019c`); local `git hash-object` = `dbb0ba65518e1932cfd7cbccb04a01b0d308d493`, identical to the GitHub blob SHA returned for this path at this commit. Commit date 2026-09-08 verified via API. Only rule tokens are normalized and cited here; no source block is copied into this repository.
- **Declaration-line census on the verbatim file:** 1 `timeframe = '4h'`; `minimal_roi = {"0": 0.5}` (single 50% level, no time steps); `stoploss = -0.2` (−20%); `trailing_stop = False` with `trailing_stop_positive = None` (trailing explicitly off, source-native); `buy_range_short = IntParameter(5, 20, default=8)`; `buy_range_long = IntParameter(20, 120, default=21)`; `populate_indicators` computes only `ema{val}` over the union of both parameter ranges; `populate_entry_trend` sets `enter_long` on `crossed_above(ema_short, ema_long) & (volume > 0)`; `populate_exit_trend` sets `exit_long` on the mirrored `crossed_above(ema_long, ema_short) & (volume > 0)`. The file sets **no** `startup_candle_count`, **no** `order_types`, **no** `max_open_trades`/`stake_amount`, **no** protections/cooldown, **no** `can_short`, **no** custom stoploss, **no** informative/resampled timeframe, **no** `volume`-derived indicator — freqtrade config/backtest defaults govern those source-side behaviors and are NOT adopted here.
- **Explicit independent derivative, and ONLY this derivative is proposed for HB_READY:** researcher pins hyperopt defaults **EMA-8/EMA-21**, keeps the exact mirror-cross entry/exit construction with the strict `volume > 0` gate, keeps the single 50% ROI level and −20% stoploss as frozen close-evaluated levels with stop-first priority (same conversion class as merged Alpha PR #590 / FMZ 482829 record / FMZ 482670 record #638), keeps trailing off, but trades Binance **BTCUSDT spot** UTC **4h** LONG/FLAT with fixed 0.001 BTC, 10,000 USDT cash, hypothetical 0.1% fee per side, completed-bar decisions with next-completed-close MARKET fills, single position (config-dependent concurrency dropped as a declared change), warmup 100, and an explicit controller-memory Decimal ledger that never consults engine delayed views. Freqtrade next-open fills, limit-order config defaults, stake/config sizing and backtest loop ordering are dropped as declared changes. These alter possible trade events and economics. No original backtest performance or source-native event equivalence is claimed; the file ships no Sharpe/win-rate/return figures (it carries only a hyperopt-results comment block for a different strategy context — no performance numbers are cited here).
- **Immutable research identity:** `freqtrade-strategies:f3340ce|AverageStrategy.py-blob-dbb0ba65|GertWohlgemuth|derived-v1-20261030|BinanceSpot:BTCUSDT:UTC4h|EMA8x21-mirrorcross|Vgt0|ROI1.5-frozen|SL0.8-frozen-stopfirst|t-to-tplus1-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-side|warmup100|exact-Decimal-ledger-no-views|no-DCA`.
- **Dedup, 2026-10-30:** `main` at `9278fdb1ed674da94e65e1b3c5b3541d22cb41fa`, 460 root strategy records / README 460; working-tree searches for `AverageStrategy`, `average-strategy`, `buy_range_short`, `Gert Wohlgemuth` return no same-source record (the two `Bb.py` hits are unrelated freqtrade records; `8/21` hits are unrelated numbers). All 11 open research PRs inspected by source/title/branch — none uses this GitHub path or rule. Closest pool neighbors use different signal objects: `freqtrade-crossema-28-48-stochrsi` crosses EMA-28/48 with StochRSI thresholds (different lengths, different gate family, no ROI/SL pair, no volume gate); `forven-ema-cross-adx-regime` requires an ADX regime gate (different conjunction, different exits). This derivative's 8/21 mirror-cross + strict volume gate + frozen 50%-ROI/−20%-SL pair on 4h is not a paraphrase or trivial parameter variant.
- **Relation to closed history (not current records):** remote branches `research/hermes-averagestrategy-*` (Oct 21–29) and Scout PR #612 (head `8f434d16`, closed NOT_LOSSLESS) used the same source file. #612's stated blockers were (i) unpinned precision/no-rounding semantics with float-residual `is_closed` risk and (ii) reliance on the generic POSITION_HOLD path plus the 3600 s terminated-executor window for 4h state. This record is a new branch that pins exactly those missing rules (§Signal degenerate pins, §Execution assumptions controller-memory ledger and view-independence); it does not merge or revive any closed branch. Closed PRs remain terminal per policy.

## Economic mechanism

### Source-reported

A short EMA crossing above a long EMA identifies upside momentum onset (entries long only while the cross is fresh and the bar printed volume); the mirrored cross identifies momentum exhaustion (exit); a 50% take-profit banks outliers and a −20% stoploss caps tail loss. The author explicitly calls it a proof of concept that "doesn't really perform that well". This is a qualitative hypothesis, not independently validated profitability.

### Research interpretation

Test whether a fresh hourly-regime-agnostic EMA-8/21 cross on 4h BTC, admitted only on printed-volume bars, predicts appreciation to +50% before −20% — with the mirrored cross as the signal exit. The derivative measures only this frozen bracket on BTCUSDT spot 4h; it cannot speak for the source's hyperopt ranges, config sizing, limit fills, or multi-pair use.

## Signal

- Input: strictly chronological, **completed** UTC Binance Spot BTC-USDT `4h` candles indexed `t=0,1,...`; use `O/H/L/C/V[t]`; consecutive open timestamps must step exactly 14,400 s. Reject missing/duplicate/gapped 4h bars, nonfinite/nonpositive prices, any candle with `H<max(O,C)`, `L>min(O,C)`, `L>H`, or nonfinite/negative volume. Reject/abort invalid research segment; never synthesize prices, forward-fill signals, or silently skip a broken bar.
- **Researcher-pinned arithmetic (own executable rule; upstream helper bit-identity not claimed):** `EMA_N` recursively with `α=2/(N+1)`, seeded by the SMA of the first N closes, first valid at index N−1 (`E8` at 7, `E21` at 20). The recursion contains **no division by market data** (α is a constant), so no zero-denominator class exists; the only undefined values are pre-seed indices, and any gate reading an undefined value is false. Post-warmup (`t>=100`) every indicator read is provably defined (seed indices 7/20 < 100, volume validated finite), so the undefined branch is unreachable after warmup — it is a seed formalism, not a data decision. **Fail-closed scope (pinned, answering the #640 distinction):** fail-closed aborts the segment only on invalid/missing candle data (§Input), never on indicator seeding; seeding-undefined reads are false by construction and cannot occur post-warmup.
- **Fresh-cross convention (pinned):** entry cross ≡ `(E8[t−1]<=E21[t−1]) ∧ (E8[t]>E21[t])`; reverse cross ≡ `(E21[t−1]<=E8[t−1]) ∧ (E21[t]>E8[t])`. Equality fires only on the `<=` leg, never as a cross by itself; NaN comparisons are false. The source calls `qtpylib.crossed_above` (unpinned upstream helper); this derivative does NOT depend on that helper's exact equality convention — the rule above is the complete executable definition.
- **Entry conjunction (all on completed bar `t`, FLAT, no pending, `t>=100`):** fresh entry cross AND `V[t]>0` (strict; zero-volume bars never fire). On fire: queue exactly one BUY of 0.001 BTC for `t+1`. No provisional cash test at signal time — sufficiency is decided once, at fill, against the actual fill price (below).
- **Fill (BUY_PENDING, validated `t+1` row with actual close `P=C[t+1]`, finite `P>0`):** if `cash >= Q*P*(1+f)` with `Q=Decimal("0.001")`, `f=Decimal("0.001")` → fill: `cash -= Q*P*(1+f)`, `base = Q` exactly, anchor `P_fill = P`. Else consume the intent without a fill, stay FLAT, and require a brand-new cross (no queue persistence). Missing/invalid `t+1` row → order remains unfilled, state unchanged, reported as such.
- **Exit (LONG, no pending, first eligible bar strictly after the BUY-fill bar):** on completed bar `t` with `u=t−1`, levels anchored at actual fill `P_fill` (`SL=0.8*P_fill`, `ROI=1.5*P_fill`): (1) if `C[u]<=SL` queue one full-position SELL (stop, checked **first** — pinned stop-first priority when one close breaches both); else (2) if `C[u]>=ROI` queue the same SELL (take-profit); else (3) if fresh reverse cross AND `V[t]>0` queue the same SELL (signal exit). Fill at `t+1` completed close: `cash += Q*P*(1-f)`, `base=0`. SELL requires `base==Q` exactly on the own ledger, else abort (no phantom-position exit).
- **Same-bar precedence (pinned):** exits are evaluated before entries on every bar. While LONG with both an exit and a fresh entry cross on one bar, the exit wins and the entry cross is consumed (re-entry needs a new cross after flat). While FLAT, an exit-signal has no position to act on and the entry proceeds normally. A queued action's fill bar generates no new order (indicators still update).
- **Warmup:** bars `0..99` update indicators but cannot queue or fill. First eligible signal `t=100` (covers EMA-21 seed at 20, cross comparability at 21, with margin). First fill `t=101`.
- **State:** FLAT, BUY_PENDING, LONG, SELL_PENDING; exactly one position and one pending order at most. On BUY fill enter LONG; on SELL fill become FLAT. No re-entry without a fresh cross after flat, no pyramiding, simultaneous positions, short, hedge, borrowing, DCA, safety orders, partial exits, dynamic sizing, trailing (source sets `trailing_stop=False` — adopted as explicitly disabled), time exit beyond the single frozen ROI level, protections/cooldown (none in source — explicitly absent), or forced end-of-sample liquidation. An unfilled end-of-sample pending order remains unfilled and is reported as such.
- **Risk and disabled behavior:** no protective stop beyond the frozen −20% bracket, no trailing, no time exit, no discretionary override. The frozen bracket plus the mirrored-cross signal exit are the only risk mechanisms; gap risk across 4h closes jumping over both levels is real and undisguised (sequential closes apply in order; a single close beyond both exits as a stop under pinned priority). Loss and indefinite holding (if no exit ever close-triggers) are possible; no hidden executor SL/TP defaults.
- **Pinned dead source elements (never decision-read, disclosed):** the hyperopt ranges `IntParameter(5,20)` / `IntParameter(20,120)` (only defaults 8/21 adopted), absent `startup_candle_count` (freqtrade default governs the source; derivative warmup 100 supersedes), absent `order_types` (source-side limit config defaults dropped for the declared MARKET convention), absent `max_open_trades`/`stake_amount` (config concurrency dropped for single-position LONG/FLAT), absent protections, `plot`/`populate` display helpers, and the file's hyperopt-comment block.

## Required data

Single Binance Spot `BTC-USDT` UTC 4h OHLCV series, validated for completeness and chronological availability. All gates derive from validated O/H/L/C/V only (volume solely for the strict `>0` gate). Only completed-bar indicator values and the fixed-fee cash ledger are decision-critical. No funding, order book, open interest, cross-market synchronization, alternate timeframe, or private feed is required. Historical MARKET fill prices must be actual validated next-bar close data, never the backtesting provider's missing-price fallback.

## Execution assumptions — demonstrated bounded pinned-engine research path

- **Pinned engine:** Hummingbot package `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. The pinned `hummingbot/VERSION`, Binance spot candles `constants.py` (993 bytes), `binance_spot_candles.py` (3,924 bytes), `executors_simulator/order_executor_simulator.py` (3,913 bytes) and `backtesting_data_provider.py` (8,823 bytes) were byte-fetched and directly read at this pinned commit this cycle (sizes identical to prior independent review); `backtesting_engine_base.py` verified: `simulate_execution` advances `update_state(row)` before controller `determine_executor_actions()`. Prior independently reviewed representative primitive is Alpha PR #414; no wheel rehash or candidate-specific backtest was run.
- **Real data path:** `BinanceSpotCandles.INTERVALS` includes `4h` (re-verified this cycle); Binance REST `/api/v3/klines` parser takes the actual Kline opening timestamp (`row[0]`). A candle's stored `timestamp=T[t]` is **open time**; its `H/L/C/V` are decision-available only after `T[t]+14400 seconds` for a complete UTC 4h bar. The candidate's own controller must reject incomplete last bars, gaps and invalid prices **before** engine preparation/dropna; no missing-price `Decimal("1")` fallback (pinned `get_price_by_type` fallback re-verified this cycle and is **forbidden** here).
- **Controller/executor path:** the future dedicated controller (NOT yet implemented) will implement the EMA-8/21 state and one-bar pending action. `OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),execution_strategy=MARKET,price=None,leverage=1,position_action=OPEN/CLOSE)`. SELL size equals the recorded base inventory exactly. Pinned `OrderExecutorSimulator.simulate` for MARKET fills on the first supplied row at its actual `close`, sets `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*filled_amount_quote`, and terminates `POSITION_HOLD`. No limit/maker/intrabar fill or unverified cross-asset path is required.
- **Deterministic controller-memory accounting contract (pinned; no delayed-view dependence):** position/cash state lives ONLY in the controller's own Decimal ledger (`cash`, `base`, pending flag, anchored `P_fill`/`SL`/`ROI`), updated solely on (i) validated completed-bar data and (ii) modeled historical full-fills at actual next-bar closes. The controller NEVER reads `executors_info`, `positions_held`, pending-hold queues, or terminated-executor views for state; its transitions are therefore independent of `terminated_executors_window` (any value, including the pinned 3600 s default), of `update_state`/`determine_executor_actions` ordering, and of POSITION_HOLD netting lag. The pinned simulator's MARKET-first-row-close/full-fill/quote-fee behavior is cited only as representative primitive evidence (#414 class) for the fill convention, not as the state-reporting path.
- **Exact-quantity / no-rounding semantics (pinned; #612 residual class closed):** amounts are exact `Decimal("0.001")` on validated close strings; no lot/tick quantization is applied anywhere (`quantize_order_amount` is never called and real exchange-valid orders are never claimed); SELL quantity is identically the recorded `base` (exact Decimal equality, no tolerance). The pinned simulator's internal `float(config.amount)*entry_price` line (re-read this cycle) is acknowledged and deliberately NOT used for state — state equality holds on the controller-memory Decimal ledger, where no float residual can arise by construction. There is no tolerance, no epsilon-close, and no `is_closed`-style float-netting check in this record's state machine.
- **Exact causal fill mapping:** decide at `T[t]+14400` using data through completed bar `t`; dispatch the stored order only on the `t+1` row, and model a retrospective full fill at actual `C[t+1]`, effective `T[t+1]+14400`. The row's opening timestamp is not misrepresented as fill availability. Do not use `C[t+1]` or indicators recomputed on `t+1` to decide at `t`; the `t+1` indicator state may update but does not create another action on the fill bar. This is an **idealized historical next-completed-close** convention, not live close-order timing or a live close-order guarantee. No claim equates any close with any neighboring open.
- **Exact modeled cash/inventory ledger:** initial cash `10000 USDT`, BTC inventory 0, fixed `Q=Decimal("0.001")`, hypothetical quote fee rate `f=Decimal("0.001")` per executed side (the source declares no commission; this fee is a researcher input, not a source fact). Successful BUY: `cash -= Q*P*(1+f)`, `base=Q`. Successful SELL: `cash += Q*P*(1-f)`, `base=0`. Invalid inventory or nonfinite/absent price aborts, not a fabricated fill. Round-trip fee-net quote PnL `Q*(Pexit-Pentry)-f*Q*(Pentry+Pexit)`. Controller ledger uses `Decimal` on original validated close strings, not native gross PnL as fee-net equity. On each full-fill-only modeled action pass `trade_cost=0.001` to pinned simulator; do not double-subtract fees.
- **Research economics boundary:** this is a **fixed idealized full-fill** historical Spot model. Research fee 0.1% per side is a declared hypothetical input, NOT verified Binance fee tier. Zero **modeled** spread/slippage is an explicit idealization, not an observed zero. Exchange-specific lot/tick rounding, min-notional, historical order acceptance, latency, partial fills, liquidity and live fee tier are not verified or claimed compatible. Do not call `quantize_order_amount` or assert real exchange-valid orders from this model. Spot has no perpetual funding/margin/liquidation leg; do not fabricate futures funding observations. PASS only concerns this precisely bounded historical model; actual trading would require separate validation and authorization.
- **Fail closed:** reject invalid candles, insufficient warmup, nonpositive/nonfinite fill prices, degenerate `ROI<=P_fill/SL>=P_fill` anchors (impossible for positive `P_fill` — asserted, not assumed), missing next close, price fallbacks and contradictory pending/position states. No paper/testnet/live order path, trading, Qlib run or Hummingbot run is authorized by this record.

## Evidence

### Source-reported

First-party GitHub file (AverageStrategy.py, Gert Wohlgemuth): EMA short/long crossover entries and mirrored exits, each AND-gated with strict `volume > 0`; hyperopt `IntParameter` ranges 5–20 / 20–120 with defaults 8/21; `timeframe = '4h'`; `minimal_roi = {"0": 0.5}`; `stoploss = -0.2`; `trailing_stop = False`; no startup count, order types, protections, or multi-timeframe logic in the file. It provides no independently verified performance (the author disclaims performance outright) and no commission model.

### Independently reproduced

Not independently reproduced. No freqtrade trade sequence, candidate-specific Hummingbot execution, Qlib parity, profitability, OOS or Survivor status was reproduced. The full 2,630-byte file was fetched and hash-verified this cycle; the pinned Hummingbot **source capability** paths were directly inspected at the pinned commit; existing independently accepted primitive evidence #414 is referenced without claiming the derivative controller exists.

### Negative evidence

Upstream `qtpylib.crossed_above` equality convention, TA-Lib/freqtrade-version bit-identity, live fill quality and any source commission model were not obtained or adopted. Fixed sizing, close-fill timing, close-evaluated ROI/SL exits, single-position concurrency and warmup 100 are explicitly researcher choices. Main and open PR dedup found no same GitHub path or materially identical 8/21 mirror-cross + volume + ROI/SL conjunction. Real exchange precision, fees, fill quality and partial executions are unverified.

## Six-gate assessment — Scout proposal, not independent audit

1. **Determinism:** pinned EMA-8/21 recursion with SMA seed and first-valid indices, pinned fresh-cross equality convention, strict volume gate, frozen 1.5×-ROI/0.8×-SL anchors, stop-first/signal/entry precedence, single pending, 100-bar warmup, division-free arithmetic with seed-formalism undefined handling — no fitted parameters adopted (hyperopt ranges disclosed, defaults pinned).
2. **Direction:** BTC-USDT Binance Spot LONG/FLAT; no short leg exists in source or derivative, no borrow/leverage.
3. **Entry/exit/risk:** fresh-cross + volume entry, mirrored-cross signal exit, frozen-bracket close-evaluated stop-first exits, trailing/time/protections explicitly disabled or absent by construction.
4. **Position:** one fixed 0.001 BTC position, 10000 USDT exact-Decimal ledger, one pending, fill-bar no-action, fresh-cross re-entry, no DCA/pyramiding/cooldown; state transitions defined solely on the controller-memory ledger with no tolerance or view dependence.
5. **Pinned engine:** actual 4h Binance spot candles, pinned controller/action/MARKET close-fill/POSITION_HOLD and quote-fee model verified from source this cycle; bounded hypothetical full-fill research accounting with explicit no-rounding/exact-quantity semantics, independent of terminated-executor window and engine view ordering.
6. **Causality:** all gates use completed bars only (lookbacks `t−1..t−20` available at `T[t]+14400`), warmup precedes decisions, open timestamps corrected to close availability, `t` signal → `t+1` completed-close modeled fill, no future-data decision leakage, no close/open equality claim.

`hb_ready_status: PASS` is a **Scout research admission proposal** for this independent derivative only; independent Hermes Auditor decides exact-head PASS, source-verifiable remediation or NOT_LOSSLESS. It is not proof of source-native equivalence, profitability, Qlib parity, implementation, HB Certified survivor or live readiness.

## Falsification plan

Not executed: adversarial tests for equality on the cross `<=` leg, zero-volume bars adjacent to crosses, simultaneous exit+entry cross while LONG, single-bar gaps over both bracket levels (stop-first check), fill-bar decision suppression, cash-insufficiency at fill with consumed signal, fees, missing next close and sample-end pending order. A later representative Qlib↔Hummingbot event-level primitive parity check is required before mass screening if this path is not already covered by validated evidence; candidate-specific performance research is separate.

## Crypto portability

BTC-USDT spot 4h is an independent study selection (the source timeframe is itself 4h; venue/symbol transfer disclosed), not an HB_READY whitelist. Applying this structure to other coins/timeframes, the hyperopt ranges, config sizing, limit fills, house BO/SO 6/6/6, futures leverage, or new fill conventions requires separately declared research assumptions and capability checks; it is not silently the original freqtrade program.

## Limitations

No freqtrade replay bit-identity, live fill quality, or source commission model exists. Close-evaluated ROI/SL exits can materially lag (or entirely miss, in a never-close-breached drift) freqtrade's native intrabar handling; the 50% ROI level is near-unreachable on 4h BTC and is kept as a frozen declared level, not a forecast. No trailing or time exit beyond the single ROI level; slow bleed inside the bracket and indefinite holding are possible. The hypothetical 0.1% fee and idealized full-fill/zero-modeled-slippage Spot ledger are not exchange-realistic order acceptance or canonical realized costs. No controller implementation, candidate-specific event parity, backtest, reproduced returns or deployment exists.

## Implementation status

`not-implemented`: no strategy-specific controller, Qlib recipe or executable deployment. HB_READY research admission is not implementation approval.

## Adoption boundary

`research-only`, `not-approved`; no Paper/Testnet/Live, capital authorization or Qlib/Hummingbot run. Only independent Hermes Auditor GitHub Webhook Review may remediate/review/merge or close; only the existing signed GitHub webhook receiver performs post-merge README count bookkeeping.

## Related Wiki records

None required; no separate registry or research artifact was created.

## Sources

- Freqtrade strategies primary: https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/AverageStrategy.py — Gert Wohlgemuth AverageStrategy, full 2,630-byte file inspected verbatim 2026-10-30 (blob `dbb0ba65518e1932cfd7cbccb04a01b0d308d493`, md5 `c395b86001b92cbe84f75cb4e68e019c`).
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently reviewed execution primitive: https://github.com/HCH725/alpha-strategy-research/pull/414
- Same stop/limit→close-evaluated conversion class: merged Alpha FMZ 482829 record / PR #590; ledger pattern: merged FMZ 482670 record / PR #638
- Closed same-source history (distinguished, not revived): Scout PR #612 (NOT_LOSSLESS: unpinned precision ledger + delayed-view dependence — both pinned anew here)
