---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "Freqtrade smooth-operator Bb mid-upper EMA-stack RSI-gated BTC spot 1h long-flat — independent derivative"
created: 2026-10-30
updated: 2026-10-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2022-08-31
sources:
  - https://github.com/the-smooth-operator/freqtrade-strategies/blob/25334fb79f82af89b78aedc37e6136a81768f9b9/strategies/Bb.py
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Freqtrade smooth-operator Bb mid-upper channel with EMA-stack gate and RSI/rail exit — BTC spot 1h independent research derivative

## Provenance

- **GitHub primary (public, immutable, read end to end):** repository https://github.com/the-smooth-operator/freqtrade-strategies, pinned commit `25334fb79f82af89b78aedc37e6136a81768f9b9` (`Merge pull request #2 from the-smooth-operator/fix-bb`, committer date `2022-08-31T18:54:02Z`, verified via `gh api .../commits/<sha>` this cycle), exact file path `strategies/Bb.py`. GitHub blob SHA `50a94e1af9bbf28ddf526708d754b3735ad2c175`, size 2,340 bytes; the raw file fetched at the pinned commit is 2,340 bytes / 75 lines, md5 `2b415193fe15dd374316bc3d7c2ebfcf`, and `git hash-object` reproduces the blob SHA `50a94e1a…d2c175` — the entire file was retrieved and inspected. Only rule tokens are normalized and cited here; no large source block is copied into this repository.
- **Declaration-line census on the verbatim file:** class `Bb(IStrategy)` (only class in file); `minimal_roi = { "0": 20 }` (2,000%, effectively never-hit — kept as a specified frozen level, never claimed as economics); `stoploss = -0.2`; `trailing_stop = True` with `trailing_stop_positive = 0.05`, `trailing_stop_positive_offset = 0.15`, `trailing_only_offset_is_reached = True` (dropped by this derivative as a declared change — see below); `ticker_interval = '1h'` (old key, no `timeframe` attribute, no exchange/currency line — venue/symbol transfer is a disclosed researcher choice); `use_exit_signal = True`; `ignore_roi_if_entry_signal = False`; `order_types` market entry / market exit / limit stoploss with `stoploss_on_exchange = True` (limit/exchange semantics converted to close-evaluated MARKET, same conversion class as merged Alpha PR #590 / FMZ 482829 record). Indicators: `ta.RSI(dataframe, timeperiod=14)`, `ta.EMA` 9/20/200, `qtpylib.bollinger_bands(qtpylib.typical_price(dataframe), window=20, stds=2)` with only `mid`/`upper` read (`lower` never computed). Entry is one 5-way AND into `enter_long`; exit is one OR/AND expression into `exit_long` (Python `&` binds tighter than `|` — exit is `RSI>75` OR (`close<0.97×mid` AND red bar), pinned). Zero `enter_short`/`exit_short`/`short`, zero `volume`, zero `informative`/`resample`, zero `startup_candle_count`/`can_short`/`process_only_new_candles`, zero `position_adjustment`/`cooldown`/`max_open_trades`, zero `leverage`/`funding`/`mark_price`, zero fitted/hyperopt parameters.
- **Explicit independent derivative, and ONLY this derivative is proposed for HB_READY:** researcher keeps the exact 5-gate entry conjunction (close inside BB mid–upper channel, close above EMA-9, close above EMA-200, EMA-20 above EMA-200) and the exact exit-signal expression, but trades Binance **BTCUSDT spot** UTC **1h** LONG/FLAT with fixed 0.001 BTC, 10,000 USDT cash, hypothetical 0.1% fee per side, completed-bar decisions with next-completed-close MARKET fills, entry-frozen −20% stop and 2,000% ROI levels checked close-evaluated with stop-first priority, and warmup 250. The source **trailing-stop leg is deliberately dropped** (no trailing ratchet is modeled — the pinned engine path for trailing is unverified), limit/exchange stop semantics are converted to MARKET, and venue/symbol/timebase pinning plus warmup are researcher choices. These alter possible trade events and economics. No original backtest performance or source-native event equivalence is claimed; the 75-line file ships no sample, window, trade count, Sharpe, win-rate or return figures.
- **Immutable research identity:** `GH:the-smooth-operator/freqtrade-strategies@25334fb|Bb.py-blob50a94e1|derived-v1-20261030|BinanceSpot:BTCUSDT:UTC1h|BB20-2-midupper-channel|EMA9-20-200-stack|RSI14-exit75|exit-rail-0.97mid-red|SL-20pct-frozen-stopfirst|ROI2000pct-frozen|t-to-tplus1-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-side|warmup250|no-trailing|no-DCA`.
- **Dedup, 2026-10-30:** `main` at `9278fdb1`, 460 root strategy records / README 460; working-tree searches for `the-smooth-operator`, `class Bb(`, `Bb.py`, `trailing_only_offset_is_reached` return no same-source record (the lone `smooth` pool hit is the unrelated `SmoothOperator.py` playground fence inside the TechnicalExampleStrategy record — a different file, never this pin). All 11 open research PRs inspected by source/title/branch — none uses this repository URL or rule. Closest pool neighbors use different signal objects: `freqtrade-bband-rsi-dip-buy` (BbandRsi: RSI<30 AND close under typical-price lower band, `1h` — a lower-band dip, never a mid–upper channel with a 3-EMA stack); `freqtrade-strategy002` (RSI<30 AND slowk<20 AND lower-band AND hammer with SAR/Fisher exit — a 4-gate dip plus pattern print, different gates and exit); `freqtrade-emaskippump` (EMA-dip with BB/volume guards, `5m` — different conjunction); `freqtrade-bandtastic` (1σ lower-band with MFI gates, `15m` — different band/oscillator family). This derivative's mid–upper-channel AND EMA-9/20/200-stack AND RSI-75/red-rail exit conjunction is not a paraphrase or trivial parameter variant.

## Economic mechanism

### Source-reported

The file prints no prose beyond code: buy the bar where price rides inside the upper Bollinger half-channel (above mid, below upper) while the short and medium trend legs stand above the long leg (close above EMA-9 and EMA-200, EMA-20 above EMA-200); stand aside to flat when momentum overheats (RSI above 75) or price sags 3% under the midline on a red bar. A −20% stoploss backstops every position, a 2,000% ROI target effectively never banks, and a 5%/15% trailing ratchet trails profitable excursions. This is a qualitative hypothesis read off the code, not independently validated profitability.

### Research interpretation

Test whether hourly BTC strength that is simultaneously channeled (inside the upper BB half) and trend-stacked (short/medium legs above the 200-bar regime line) persists one bar forward — with overheating (RSI>75) or a red close 3% under the midline as the only signal exits and a frozen −20% stop as the only risk backstop. The derivative measures only this frozen bracket without trailing; it cannot speak for the source's trailing excursions, limit-stop timing, ROI banking, or any venue but Binance spot.

## Signal

- Input: strictly chronological, **completed** UTC Binance Spot BTC-USDT `1h` candles indexed `t=0,1,...`; use `O/H/L/C[t]`. Reject missing/duplicate/gapped hourly bars, nonfinite/nonpositive prices, or any candle with `H<max(O,C)`, `L>min(O,C)`, `L>H`. Reject/abort invalid research segment; never synthesize prices, forward-fill signals, or silently skip a broken bar. Volume is never read (source reads none — census 0 `volume`).
- **Researcher-pinned arithmetic (own executable rule; TA-Lib/qtpylib bit-identity not claimed):** `EMA_N` recursively with `α=2/(N+1)`, seeded by the SMA of the first N closes, first valid at index N−1 (`E9`,`E20`,`E200`). `RSI14` via Wilder RMA of gains/losses seeded by SMA, first valid at 14. `TYP[t]=(H[t]+L[t]+C[t])/3`; `BBmid[t]`/`BBup[t]` = 20-bar SMA of TYP ± 2× population stdev, first valid at 19. Any undefined input makes the dependent value undefined; a gate on undefined is false, never imputed.
- **Entry conjunction (all on completed bar `t`, strict inequalities — equality never fires):** FLAT, no pending, `t>=250`, `BBmid[t]<C[t]<BBup[t]` (strict channel), `C[t]>E9[t]`, `C[t]>E200[t]`, `E20[t]>E200[t]`. On fire: queue exactly one BUY of 0.001 BTC for `t+1`; freeze `SL=0.8×C[t]`, `TP=21×C[t]`; require finite `C[t]>0` and strict `TP>C[t]>SL`, else queue nothing.
- **Exit (LONG, no pending, first eligible bar strictly after the BUY-fill bar):** on completed bar `t` with `u=t−1`, checked in pinned order: if `C[u]<=SL` queue one full-position SELL (stop, checked **first** — pinned stop-first priority when one close breaches several legs); else if `C[u]>=TP` queue the same SELL (2,000% ROI leg — specified, practically never fires); else if `RSI[u]>75` OR (`C[u]<0.97×BBmid[u]` AND `O[u]>C[u]`) queue the same SELL (signal). Fill at `t+1` completed close. No trailing ratchet (dropped leg — levels frozen at entry), no time exit.
- **Warmup:** bars `0..249` update indicators but cannot queue or fill. First eligible signal `t=250` (covers EMA-200 seed at 199, BB at 19, RSI at 14, with margin). First fill `t=251`.
- **State:** FLAT, BUY_PENDING, LONG, SELL_PENDING; exactly one position and one pending order at most. A queued action on `t` attempts one historical fill at `t+1` completed close; process that fill first and do **not** generate a new order on the fill bar, though indicators still update. On BUY fill enter LONG; on SELL fill become FLAT. Entry signals while LONG are ignored (fresh signal after flat required — honors `use_exit_signal=True` structurally; `ignore_roi_if_entry_signal=False` has no separate effect under the one-position rule). No pyramiding, simultaneous positions, short, hedge, borrowing, DCA, safety orders, partial exits, dynamic sizing, cooldown, or forced end-of-sample liquidation. An unfilled end-of-sample pending order remains unfilled and is reported as such.
- **Risk and disabled behavior:** no protective stop beyond the frozen −20% bracket, no trailing (source trailing leg dropped — disclosed change), no time exit, no discretionary override. Gap risk across hourly closes jumping over the stop is real and undisguised (sequential closes apply in order; a single close beyond both stop and signal exits as a stop under pinned priority). Loss and indefinite holding (if no leg ever close-fires) are possible; no hidden executor SL/TP defaults.
- **Pinned dead source elements (never decision-read, disclosed):** `trailing_stop`/`trailing_stop_positive`/`trailing_stop_positive_offset`/`trailing_only_offset_is_reached` (dropped — unverified engine path), limit/`stoploss_on_exchange` semantics (converted to MARKET), `bb_lowerband` (never computed in file), any exchange/currency/timezone outside the pinned BTCUSDT spot UTC 1h choice.

## Required data

Single Binance Spot `BTC-USDT` UTC hourly OHLC series, validated for completeness and chronological availability. All gates derive from validated O/H/L/C only. Only completed-bar indicator values and the fixed-fee cash ledger are decision-critical. No funding, order book, open interest, volume, cross-market synchronization, alternate timeframe, or private feed is required. Historical MARKET fill prices must be actual validated next-bar close data, never the backtesting provider's missing-price fallback.

## Execution assumptions — demonstrated bounded pinned-engine research path

- **Pinned engine:** Hummingbot package `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. The pinned `hummingbot/VERSION`, `data_feed/candles_feed/binance_spot_candles/constants.py` (993 bytes), `binance_spot_candles.py` (3,924 bytes), `strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` (3,913 bytes) and `strategy_v2/backtesting/backtesting_data_provider.py` (8,823 bytes) were byte-fetched and directly read at this pinned commit this cycle (sizes identical to prior independent review); `backtesting_engine_base.py` verified: `simulate_execution` advances `update_state(row)` before controller `determine_executor_actions()`; `BacktestPositionHold` nets buys/sells with gross realized PnL separate from fees. Prior independently reviewed representative primitive is Alpha PR #414; no wheel rehash or candidate-specific backtest was run.
- **Real data path:** `BinanceSpotCandles.INTERVALS` includes `1h`; Binance REST `/api/v3/klines` parser takes the actual Kline opening timestamp (`row[0]`). A candle's stored `timestamp=T[t]` is **open time**; its `H/L/C` are decision-available only after `T[t]+3600 seconds` for a complete UTC hour. The candidate's own controller must reject incomplete last bars, gaps and invalid prices **before** engine preparation/dropna; no missing-price `Decimal("1")` fallback (pinned `get_price_by_type` fallback re-verified this cycle and is **forbidden** here).
- **Controller/executor path:** the future dedicated controller (NOT yet implemented) will implement the BB-channel/EMA-stack state and the RSI/rail exit with frozen SL/TP. `OrderExecutorConfig(connector_name="binance",trading_pair="BTC-USDT",side=BUY/SELL,amount=Decimal("0.001"),execution_strategy=MARKET,price=None,leverage=1,position_action=OPEN/CLOSE)`. SELL size equals the recorded base inventory. `OrderExecutorSimulator.simulate` for MARKET fills on the first supplied row at its actual `close`, sets `filled_amount_quote=amount*close`, `cum_fees_quote=trade_cost*filled_amount_quote`, and terminates `POSITION_HOLD`; `BacktestPositionHold` nets buy/sell and tracks gross realized PnL separately from fees. No limit/maker/intrabar fill, no trailing-ratchet path, no unverified cross-asset path is required.
- **Exact causal fill mapping:** decide at `T[t]+3600` using data through completed bar `t`; dispatch the stored order only on the `t+1` row, and model a retrospective full fill at actual `C[t+1]`, effective `T[t+1]+3600`. The row's opening timestamp is not misrepresented as fill availability. Do not use `C[t+1]` or indicators recomputed on `t+1` to decide at `t`; the `t+1` indicator state may update but does not create another action on the fill bar. This is an **idealized historical next-completed-close** convention, not live close-order timing or a live close-order guarantee. No claim equates any close with any neighboring open.
- **Exact modeled cash/inventory ledger:** initial cash `10000 USDT`, BTC inventory 0, fixed `Q=Decimal("0.001")`, hypothetical quote fee rate `f=Decimal("0.001")` per executed side (the source declares no commission; this fee is a researcher input, not a source fact). On BUY at actual close `P`, require `cash >= Q*P*(1+f)`; otherwise consume BUY intent without a fill, stay FLAT, require a new signal. Successful BUY: `cash -= Q*P*(1+f)`, `base += Q`. SELL requires `base==Q`; successful SELL: `cash += Q*P*(1-f)`, `base=0`. Invalid inventory or nonfinite/absent price aborts, not a fabricated fill. Round-trip fee-net quote PnL `Q*(Pexit-Pentry)-f*Q*(Pentry+Pexit)`. Controller ledger uses `Decimal` on original validated close strings, not native gross PnL as fee-net equity. On each full-fill-only modeled action pass `trade_cost=0.001` to pinned simulator; do not double-subtract fees.
- **Research economics boundary:** this is a **fixed idealized full-fill** historical Spot model. Research fee 0.1% per side is a declared hypothetical input, NOT verified Binance fee tier. Zero **modeled** spread/slippage is an explicit idealization, not an observed zero. Exchange-specific lot/tick rounding, min-notional, historical order acceptance, latency, partial fills, liquidity and live fee tier are not verified or claimed compatible. Do not call `quantize_order_amount` or assert real exchange-valid orders from this model. Spot has no perpetual funding/margin/liquidation leg; do not fabricate futures funding observations. PASS only concerns this precisely bounded historical model; actual trading would require separate validation and authorization.
- **Fail closed:** reject invalid candles, undefined indicators, insufficient warmup, degenerate `TP<=C/SL>=C` freezes, missing next close, price fallbacks and contradictory pending/position states. No paper/testnet/live order path, trading, Qlib run or Hummingbot run is authorized by this record.

## Evidence

### Source-reported

Pinned GitHub file `strategies/Bb.py` at `25334fb` (75 lines, blob `50a94e1a…d2c175`): `ticker_interval='1h'`; indicators RSI-14, EMA-9/20/200, typical-price BB-20/2σ with `mid`/`upper` read; entry 5-way AND (`bb_middleband<close<bb_upperband`, `close>ema9`, `close>ema200`, `ema20>ema200`); exit `rsi>75` OR (`close<0.97×bb_middleband` AND red bar); `stoploss=-0.2`; `minimal_roi={"0":20}`; trailing 5%/15% with only-offset; `use_exit_signal=True`; `ignore_roi_if_entry_signal=False`; market entry/exit with limit exchange stop. It provides no performance, sample, window, trade count or cost basis.

### Independently reproduced

Not independently reproduced. No file trade sequence, candidate-specific Hummingbot execution, Qlib parity, profitability, OOS or Survivor status was reproduced. The full 75-line file was fetched and read verbatim at the pinned commit this cycle (byte-identity proven); the pinned Hummingbot **source capability** paths were directly inspected at the pinned commit; existing independently accepted primitive evidence #414 is referenced without claiming the derivative controller exists.

### Negative evidence

TA-Lib/qtpylib exact seeding/float bit-identity, live fill quality and trailing-ratchet behavior were not obtained — trailing is dropped, not approximated. The 2,000% ROI leg is kept as a specified frozen level that practically never fires (not a claimed profit target). Limit/exchange stop semantics are converted, not preserved. Fixed sizing, close-fill timing, warmup 250, venue/symbol pinning and dropped trailing are explicitly researcher choices. Main and open PR dedup found no same repository/file/commit or materially identical channel-plus-stack conjunction. Real exchange precision, fees, fill quality and partial executions are unverified.

## Six-gate assessment — Scout proposal, not independent audit

1. **Determinism:** RSI-14, EMA-9/20/200, typical-price BB-20/2σ, strict-inequality 5-gate entry, pinned OR/AND exit precedence, frozen −20%/+2,000% levels, 250-bar warmup, na-seeded pinned arithmetic, no fitted parameters.
2. **Direction:** BTC-USDT Binance Spot LONG/FLAT; file carries zero short tokens, short explicitly absent by construction, no borrow/leverage.
3. **Entry/exit/risk:** channel-plus-stack entry, RSI/rail signal exits plus frozen-bracket close-evaluated stop-first exits, trailing explicitly dropped and disclosed, all other protective/trailing/time exits absent by construction.
4. **Position:** one fixed 0.001 BTC position, 10000 USDT ledger, one pending, fill-bar no-action, fresh-signal-after-flat re-entry, no DCA/pyramiding/cooldown.
5. **Pinned engine:** actual 1h Binance spot candles, pinned controller/action/MARKET close-fill/POSITION_HOLD and quote-fee model verified from source this cycle; bounded hypothetical full-fill research accounting only, not exchange-valid orders; trailing path explicitly excluded.
6. **Causality:** all gates use completed bars only (lookbacks `t−1..t−249` available at `T[t]+3600`), warmup precedes decisions, open timestamps corrected to close availability, `t` signal → `t+1` completed-close modeled fill, no future-data decision leakage, no close/open equality claim.

`hb_ready_status: PASS` is a **Scout research admission proposal** for this independent derivative only; independent Hermes Auditor decides exact-head PASS, source-verifiable remediation or NOT_LOSSLESS. It is not proof of source-native equivalence, profitability, Qlib parity, implementation, HB Certified survivor or live readiness.

## Falsification plan

Not executed: adversarial tests for ties on every strict gate (channel edges, EMA equality, RSI-75, 0.97 rail, red-bar equality), zero/degenerate freeze, single-bar gaps over the stop, breakdown on BUY fill bar, entry signals while LONG, insufficient cash, fees, missing next close and sample-end pending order. A later representative Qlib↔Hummingbot event-level primitive parity check is required before mass screening if this path is not already covered by validated evidence; candidate-specific performance research is separate.

## Crypto portability

BTC-USDT spot 1h is an independent study selection (the source pins only `ticker_interval='1h'` with no venue/symbol — transfer disclosed), not an HB_READY whitelist. Applying this structure to other coins/timeframes, the dropped trailing leg, equity sizing, limit-stop timing, house BO/SO 6/6/6, futures leverage, or new fill conventions requires separately declared research assumptions and capability checks; it is not silently the original file.

## Limitations

No TA-Lib/qtpylib replay bit-identity, live fill quality, trailing behavior, or source commission model exists. Close-evaluated exits can materially lag the source's limit-stop/trailing behavior; the dropped trailing ratchet removes the source's profit-protection excursions entirely. No time exit; slow bleed inside the bracket and indefinite holding are possible. The hypothetical 0.1% fee and idealized full-fill/zero-modeled-slippage Spot ledger are not exchange-realistic order acceptance or canonical realized costs. No controller implementation, candidate-specific event parity, backtest, reproduced returns or deployment exists.

## Implementation status

`not-implemented`: no strategy-specific controller, Qlib recipe or executable deployment. HB_READY research admission is not implementation approval.

## Adoption boundary

`research-only`, `not-approved`; no Paper/Testnet/Live, capital authorization or Qlib/Hummingbot run. Only independent Hermes Auditor GitHub Webhook Review may remediate/review/merge or close; only the existing signed GitHub webhook receiver performs post-merge README count bookkeeping.

## Related Wiki records

None required; no separate registry or research artifact was created.

## Sources

- GitHub primary: https://github.com/the-smooth-operator/freqtrade-strategies/blob/25334fb79f82af89b78aedc37e6136a81768f9b9/strategies/Bb.py — class `Bb`, 75 lines inspected verbatim 2026-10-30 (raw 2,340 bytes, blob SHA `50a94e1af9bbf28ddf526708d754b3735ad2c175`, commit date 2022-08-31).
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently reviewed execution primitive: https://github.com/HCH725/alpha-strategy-research/pull/414
- Same stop/limit→close-evaluated conversion class: merged Alpha FMZ 482829 record / PR #590
