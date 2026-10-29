---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "vnpy BollChannel BB18-3.4 touch with CCI10 polarity and ATR30 x5.2 trailing stop; independent BTC-USDT spot 15m long-flat derivative"
created: 2026-10-30
updated: 2026-10-30
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - vnpy
status: research-only
confidence: medium
source_as_of: 2026-10-04
sources:
  - https://github.com/vnpy/vnpy_ctastrategy/blob/c212d603e68a5f4dbbc160fe8f7f8b1e06be2494/vnpy_ctastrategy/strategies/boll_channel_strategy.py
  - https://github.com/vnpy/vnpy/blob/c6e231caf32b7fc97e6459817fff66458cf7e7c4/vnpy/trader/utility.py
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# vnpy BollChannel BB-touch/CCI-polarity long — independent derivative

## Provenance

- **Primary source:** public vnpy CTA example-strategy collection `vnpy/vnpy_ctastrategy`, file `vnpy_ctastrategy/strategies/boll_channel_strategy.py` (class `BollChannelStrategy(CtaTemplate)`, the only strategy class in the file; docstring: use Bollinger Channel plus CCI for entries and ATR stop for exits), read in full at immutable commit **`c212d603e68a5f4dbbc160fe8f7f8b1e06be2494`** (2026-10-04, latest commit touching this file — a type-annotation completion; no signal line changed by it): https://github.com/vnpy/vnpy_ctastrategy/blob/c212d603e68a5f4dbbc160fe8f7f8b1e06be2494/vnpy_ctastrategy/strategies/boll_channel_strategy.py . Verified bytes this run: **144 lines, 3785 bytes**, SHA256 `4a8f717506c68ea46138ccca13491aa8e5b6336a71ce2d0dd3e0d3faa3b46332`, Git blob SHA `122b7d7c0fba9ddacdba2e2d49a3a15edbac3f3c` matching the GitHub API blob SHA at the pinned commit. Repository HEAD re-checked this run via `git ls-remote` (`7a8768d`); the file fetched at HEAD is byte-identical to the pinned-commit bytes, so the pin is the file's current content. No login, no paywall.
- **Source facts actually verified (effective literals):** `boll_window = 18`; `boll_dev = 3.4`; `cci_window = 10`; `atr_window = 30`; `sl_multiplier = 5.2`; `fixed_size = 1`; `author = "用Python的交易员"`. Decision loop is the 15-minute bar callback (`BarGenerator(self.on_bar, 15, self.on_15min_bar)`); flat entries are stop orders — `buy(boll_up, fixed_size, True)` when `cci_value > 0`, `short(boll_down, fixed_size, True)` when `cci_value < 0`; position branches maintain trade extremes and re-place stop exits every bar after `cancel_all()` — long `long_stop = intra_trade_high - atr_value * sl_multiplier` via `sell(..., True)`, short `short_stop = intra_trade_low + atr_value * sl_multiplier` via `cover(..., True)`. There is no ROI ladder, no fixed stoploss, no trailing-stop helper, no time exit, no `startup_candle_count`, no hyperopt/`*Parameter`, no protections, no resample/informative pair, no leverage/margin/funding/market concept (the file names no venue, pair, or timeframe unit — the 15 is a minute-window count). Full-file token census this run: 1 `BarGenerator` (the 15-window synthesis call only); 0 `minimal_roi`; 0 `stoploss` attribute; 0 `trailing_stop`; 0 `custom_exit` / `custom_stoploss`; 0 `use_exit_signal` / `exit_profit_only`; 0 `can_short`; 0 `position_adjustment` / `pyramiding` / `max_open` / `cooldown`; 0 `volume` (no volume column is ever named or read); 0 `fillna` / `ffill` / `interpolate`; 0 negative shifts; 0 `leverage` / `funding` / `mark_price`. Entries act only in the `pos == 0` branch, long exits only in `pos > 0`, short exits only in `pos < 0` — branches never mix, and opposite-direction signals while positioned are ignored (no reversal), literal source state machine.
- **Indicator-construction source (same lane, separately pinned):** `vnpy/vnpy` file `vnpy/trader/utility.py` at immutable commit **`c6e231caf32b7fc97e6459817fff66458cf7e7c4`** (verified as that repository's HEAD via `git ls-remote` this run; 41642 bytes read in full): `ArrayManager(size = 100)` default, `inited` set once `count >= size`, rolling left-shift ring of the last 100 bars with the newest bar appended; `boll(n, dev)` returns `talib.SMA(close, n) ± talib.STDDEV(close, n, 1) * dev`; `cci(n)` returns `talib.CCI(high, low, close, n)`; `atr(n)` returns `talib.ATR(high, low, close, n)` — scalar legs read the array's last element. No reviewer repair may substitute another SMA/STDDEV variant, another CCI/ATR length, or a sibling file's constant.
- **Prior vnpy proposal fenced (different source file):** PR **#448** (`research/hermes-vnpy-atr-rsi-20261024-...`, closed `NOT_LOSSLESS` 2026-10-25) pinned `vnpy_ctastrategy/strategies/atr_rsi_strategy.py` — ATR(22)-above-10-bar-mean gated RSI(5) 66/34 entries with a 0.8% trailing stop, two-sided, 1d. This record pins a **different file** (`boll_channel_strategy.py`) with a different mechanism (BB(18, 3.4) band-touch with CCI(10) polarity, ATR(30) x5.2 extreme-minus-multiple stop, 15m, spot long-flat). Different immutable source, different gates, different venue/timeframe/side — not a duplicate, paraphrase, or trivial parameter variant. The #448 review's three blocker classes are answered here by explicit researcher choices, never by asking the reviewer to invent them: (1) **Binance SPOT, leverage 1, fixed `Q = 0.001` BTC, hypothetical 0.1% per-side fee, no funding leg** (spot has none — not a zero-funding claim about perpetuals), with capital/precision/ledger fully specified below; (2) the already-reviewed single-pair spot OHLCV → controller action → MARKET-close simulator primitive with byte-verified pinned paths below; (3) indicator state explicitly pinned to **continuous full-history TA-Lib state** (researcher choice — disclosed difference from the source's rolling-100 recompute, never presented as source-native equivalence).
- **Independent researcher-defined executable derivative (NOT source-native):** source venue/pair is agnostic, so pin single-asset Binance **BTC-USDT spot 15m**; the source's 1m→15m bar synthesis is replaced by **native 15m klines** (same 15-minute decision grid, disclosed); the futures-style stop-limit entries/exits are adapted to **completed-bar-touch signals with next-completed-bar-close MARKET fills and close-bracket stop evaluation** at pinned priority; the short leg is **dropped** (spot cannot short — disclosed event change); indicator state is continuous full-history (disclosed above); fixed `Q = Decimal("0.001")` BTC, 10,000 USDT starting cash, 0.1% hypothetical per-side fee, **110-bar** researcher warmup pin (mirrors the source's 100-bar ArrayManager init gate with ATR30 seed margin); single-unit/no-add/no-cooldown position pin; exact-Decimal ledger with fail-closed reconciliation. These researcher choices change trade events and economics.
- **Frozen identity:** `VN:BollChannel|c212d60|independent-derived-20261030|BinanceSpot-BTC-USDT-UTC15m|E(cci10>0,H>=upBB18-3.4)|Xtrail hi-5.2xatr30 close-bracket|noROI-noSL-notime|next-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-each-side|warmup110|Decimal-ledger`. Any signal, timing, cost or position change creates a different derivative.

## Economic mechanism

### Source-reported

The file's docstring reports a Bollinger-Channel-plus-CCI entry with ATR-stop idea (author prose, **not traceable table/figure evidence and not relied upon here**). The coded mechanism: on each completed 15-minute bar, when flat, rest a buy-stop at the upper BB(18, 3.4) band if CCI(10) is positive, or a sell-stop at the lower band if CCI(10) is negative; once positioned, trail the extreme (highest high while long, lowest low while short) and rest the exit stop a fixed 5.2 ATR(30) multiples beyond it. No profit target, no fixed stop, no time exit — the position lives until the multiple-based stop is touched.

### Research interpretation

A band-touch breakout buyer that refuses to buy falling tape: the touch proves displacement, the CCI-polarity leg proves the displacement points up, and the 5.2-multiple stop gives the trade room to breathe while cutting it when the extreme decays by a fixed volatility budget. Unlike pure band-break records (touch alone), the entry stands aside whenever CCI is non-positive, so drifts that pierce the band without momentum confirmation are not chased. Unlike fixed-percent-stop records, the exit is a volatility-multiple trailing extreme, so holding time stretches in calm trends and compresses in expansions. The coded consequence is a patient buyer of momentum-confirmed band touches that exits only on volatility-budget exhaustion. No performance, profitability, Qlib parity or Survivor claim.

## Signal

Exact rules as pinned (any other BB window/deviation, CCI/ATR length, multiple, strictness, fill, frame, book, or leg combination is a different, unpinned rule):

```text
mid[t] = TA-Lib SMA18(C); sd[t] = TA-Lib STDDEV18(C, nbdev 1)
up[t]  = mid[t] + 3.4*sd[t]; dn[t] = mid[t] - 3.4*sd[t]
cci[t] = TA-Lib CCI10(H,L,C); atr[t] = TA-Lib ATR30(H,L,C)
ENTER[t] = (cci[t] > 0) AND (H[t] >= up[t])          // flat only, touch-bracket
STOP[t]  = hi - 5.2*atr[t], hi = max(H[f..t])        // long only, close-bracket
EXIT[t]  = (C[t] <= STOP[t])
```

- **Indicator-state pin (answers the #448-blocker-3 class):** all five series run on **continuous full-history TA-Lib state** seeded over the warmup — the researcher's explicit choice. The source recomputes the same TA-Lib calls on a rolling 100-bar window (`ArrayManager` shift ring, verified bytes above); the two states can differ near the 66/34-style strict boundaries, so this record never claims source-trade equivalence — the derivative is assessed on its own spec. TA-Lib Wilder/SMA seeding needs the warmup below; NaN-leading comparisons and edges are false.
- **Band-touch transcription:** the source's buy-stop at `boll_up` triggers on intrabar touch; the derivative signals on the completed bar's touch (`H[t] >= up[t]`) with CCI polarity on the same bar, and fills at the next completed close — disclosed adaptation, same 15-minute grid, no intrabar path claim. `cci == 0` fires nothing (strict); `H == up` exactly fires the touch (inclusive, mirrors stop-touch semantics).
- **Stop transcription:** the source re-places `intra_high - 5.2*ATR` as a stop order each bar; the derivative evaluates `C[t] <= hi - 5.2*atr[t]` on completed closes, with `hi` ratcheting on bar highs only (never down on its own — but the stop level itself may fall when ATR contracts, literally as coded, never ratcheted). `atr[t]` includes bar t (causal — same bar whose close is compared). `C == STOP` exactly exits (inclusive, mirrors stop-trigger semantics).
- **Mutual-exclusion proof (no tie-break pin required):** entries act only from FLAT, exits only while LONG, and fill bars evaluate nothing — signal and exit never co-fire by state separation. Single exit leg, so no exit-exit priority exists. The reviewer is never asked to invent an ordering.
- **Warmup:** first **110** valid fully completed 15m bars, indices 0–109, are data-only, FLAT, and never emit orders (researcher pin mirroring the source's 100-bar `ArrayManager` init gate with ATR30 seed margin). First decision may occur at index 110. Pre-seed bars could never fire in any case. No optimizer, ML, external feed, negative shift, future extremum, repaint or fitted parameter at research time.
- **BUY state:** initial `FLAT`, 0 BTC, 10,000 USDT cash. At eligible `E[t]` (`t >= 110`), if FLAT with no pending order and `ENTER[t]` true, queue exactly one fixed `Q = Decimal("0.001")` BTC MARKET BUY for the **next completed bar** `f = t+1`; do not use bar f's data to decide at t. At `E[f]`, use actual finite `C[f]` as the idealized simulator fill, if `cash >= Q*C[f]*(1+fee)` in exact Decimal. If insufficient cash, consume the signal, remain FLAT, and do not invent a partial fill or deferred order. A confirmed full fill sets LONG, records fill price `P = C[f]` and `fill_index = f`, seeds `hi = H[f]`. No signal or exit evaluation on the fill bar.
- **LONG exits (evaluated at each `E[t]`, `t > f`; at most one exit per bar):** the **sole** exit leg is the trailing-multiple stop: update `hi = max(hi, H[t])`, compute `STOP[t] = hi - Decimal("5.2")*atr[t]`, exit if `C[t] <= STOP[t]`. The winning exit queues exactly one MARKET SELL for the next completed bar `s = t+1` at real `C[s]`, sells the full Q, sets FLAT. No exit executes if its required future bar is absent; the pending order stays unfilled at sample end. No evaluation on the SELL fill bar; earliest re-entry decision is a later eligible bar. There is explicitly **no ROI rung, no fixed stoploss, no time exit, no opposite-signal exit** — the file ships none and this record adds none.
- **State priority and exclusions:** at most one pending action and one position; a pending order takes precedence over new signals. There is no cooldown, pyramiding, DCA/safety orders, averaging, partial sizing, shorts, borrowing, leverage, margin, shared-capital concurrency, session filter, intrabar stop/limit/maker, multi-timeframe feed, or end-of-sample forced liquidation. An open LONG at the end is valued at the last **actual valid close**, never synthetically liquidated. Same-bar entry/exit exclusion holds by construction.
- **Exact Decimal ledger (position truth):** all research accounting uses `Decimal(str(x))` for observed closes (never `Decimal(float)`), exact `Q`, exact products. BUY debits `Q*P*(1+fee)` USDT and credits exactly Q BTC; SELL debits exactly Q BTC and credits `Q*P*(1-fee)` USDT. `FLAT` holds **iff** ledger BTC `== Decimal("0")` exactly — arithmetically guaranteed since the identical Q added at fill is subtracted at close; no epsilon exists anywhere. Simulator quote/fee outputs are cross-checked only: if `|sim_quote - Q*P| > max(1e-8, 1e-12*Q*P)` or the fee check fails, or side/amount disagree, **abort the run as ENGINE_MISMATCH** — never round, never absorb dust, never infer state from the simulator. The controller-side ledger alone drives FLAT/LONG.

## Required data

Only actual Binance BTC-USDT spot UTC 15m O/H/L/C/V (volume read for validation only — no signal leg reads it, literally as in the source). Indicator-plus-touch predicates use bar t's **completed** inputs at `E[t] = T[t] + 900 seconds` (T[t] the exchange open timestamp); the queued order's fill at `E[t+1]` is not used retroactively. Stop extreme/ATR accounting starts at the **confirmed full-fill** bar, not the signal bar. No synthesized sub-timeframe, funding rate, order book, multi-asset feed, external sentiment or ML inference. Input validation: strictly increasing, gap-free 900-second UTC open timestamps; finite positive O/H/L/C, `H >= max(O,C)`, `L <= min(O,C)`, `H >= L`, finite `V >= 0`, no duplicate bars. **Abort the research run** on any missing, invalid, duplicate or discontinuous candle; do not forward-fill, interpolate, fabricate prices, quietly skip a gap, or emit synthetic fills/mark prices.

## Execution assumptions

- **Pinned contract:** Hummingbot package **`20260920`**, `hummingbot/VERSION = dev-2.17.0` (bytes read at the bounded commit this run), bounded source commit **`HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`**. This cycle verified: `VERSION` file content `dev-2.17.0`; `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` `INTERVALS` maps **`15m`** (with `1m`/`1h` and higher); `backtesting_data_provider.py:140` returns `Decimal("1")` when price is absent — **never** used for fills or marking, actual positive closes required; `strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` branches MARKET, takes the fill row's real `close` as `entry_price`, computes `float(config.amount) * entry_price`, writes quote/fees, and returns `CloseType.POSITION_HOLD`. The float line is exactly why this record's position truth is the independent Decimal ledger, never simulator auto-netting. No wheel re-download/hash this cycle; prior independently reviewed alpha PR **#414** reports 902/902 matching wheel Python files and SHA256 `ea5a929c...a148`; the independent Auditor must confirm that evidence applies to the pinned package and path.
- **Controller/executor:** `BacktestingEngineBase.simulate_execution` iterates feature rows, updates state, then calls `controller.determine_executor_actions()` and processes `CreateExecutorAction`. A **future dedicated controller is not implemented**; it must queue the previous completed signal and emit `OrderExecutorConfig(connector_name="binance", trading_pair="BTC-USDT", side=TradeType.BUY/SELL, amount=Decimal("0.001"), position_action=OPEN/CLOSE, execution_strategy=ExecutionStrategy.MARKET, price=None, leverage=1)` on the designated fill row, without using that row to decide the preceding signal. No claim of a deployed controller or exchange-accepted order.
- **Actual fill path:** MARKET uses the first supplied row's real `close`; sets `filled_amount_quote = float(amount)*close`, `cum_fees_quote = trade_cost * filled_amount_quote`; returns `POSITION_HOLD`. The engine's raw row timestamp is bar-open; this research model reports the **effective historical fill event** as `E[fill_row]`, not a claim a real order could execute at the completed close. A delayed controller dispatch on row `t+1` is required. The simulator does not independently verify live latency, spread, partial fills, tick/lot/min-notional or exchange acceptance; any such failure aborts per the ledger rule instead of rounding.
- **Missing price and economic limitations:** no **additional modeled** slippage is included in this idealized MARKET-close research convention; this is **not** a claim of zero real slippage. The 0.1% fee is an explicit research assumption, **not** a verified Binance tier. Spot unleveraged BTC/USDT has no perpetual funding or liquidation cash flow; this does **not** assume perpetual funding is zero. Real exchange fees, liquidity, precision and market impact are unverified.
- **Reused capability boundary:** this uses only the already reviewed single-pair Binance spot OHLCV → controller action → MARKET-close `OrderExecutorSimulator` → POSITION_HOLD primitive, as previously documented in alpha PRs **#414** and **#550** (plus the admitted 15m Bandtastic spot record's bounded path on this same frame). The new strategy changes only controller-side BB-touch/CCI-polarity predicates, the single trailing-multiple close-bracket stop and the Decimal ledger; not the data/executor market path. No Hummingbot or Qlib test is performed in this Scout. If a new execution primitive is required, one representative Hummingbot↔Qlib event-level parity validation is required **before mass screening**, not as a profitability admission gate.

## Evidence

### Source-reported

The pinned `boll_channel_strategy.py` bytes support every constant cited above (18/3.4/10/30/5.2/1, the 15-window decision loop, flat-only stop entries gated on CCI polarity, extreme-minus-multiple stop exits, `cancel_all` per bar, position-gated branches). The pinned `utility.py` bytes support the ArrayManager 100-bar init gate and the SMA/STDDEV/CCI/ATR constructions cited above. The file ships no sample, window, trade count, or cost basis — this record adopts no source-reported performance (see Evidence).

### Independently reproduced

**None** for this candidate's vnpy trades, Hummingbot/Qlib events, performance, OOS or realized fees. Only the pinned strategy bytes, the ArrayManager source, and pinned-engine source paths above were inspected; prior PR engine proof is referenced with limitations.

### Negative evidence

Pre-write dedup 2026-10-30 against `main@5a3d1297` (**450** root-level strategy records, README counter **450** — full tree, excluding two READMEs): filename/content search for `boll_channel`, `bollchannel`, `vnpy`, `veighna`, and the `BB(18, 3.4)`-with-`CCI(10)` conjunction returns **zero strategy records** — no pool record cites this source file or conjoins a 3.4-deviation band-touch with CCI polarity and a 5.2-multiple ATR trailing stop. The eleven open `research/*` PRs (#48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593) were inspected by source/title/branch and none uses this source or rule. Closed-PR search returns only the same-lane-different-file #448 (vnpy AtrRsi — ATR22/ATRMA10/RSI5-66/34, two-sided 1d; different file, different gates, fenced above). Nearest pool neighbors use different mechanisms: `hummingbot-bollinger-v1-bbp-extreme` (percent-b %B extremes, 1d — oscillator-level, never band-touch-plus-CCI); `fmz-483087-triple-bollinger-simultaneous-breach` (triple simultaneous lower-band breach, 1h — breach-count construction, no CCI leg, no trailing-multiple exit); `freqtrade-bband-rsi-dip-buy` (BB20 dip with RSI conjunction, different legs and exit stack); `tradingview-exlux-bb20-ema10-persistent-bias` (BB20/EMA10 bias persistence with time exits, 1d — different construction). This is not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

Future authorized research only (no backtest, trading, deployment or cron change here): rolling-100 vs continuous-state divergence at CCI==0 and touch boundaries; `H == up` touch firing vs `H == up - epsilon` silence; `C == STOP` exit firing; ATR-contraction stop lowering (non-ratchet proof); warmup 109/110 boundary; signal t versus fill f; insufficient cash; last-bar pending; full-fill fee ledger; `Decimal(str())` versus float reconciliation; ENGINE_MISMATCH abort path; native-15m vs synthesized-15m grid equivalence check (disclosed substitution, never claimed identical).

## Crypto portability

Binance BTC-USDT spot, 15m, unleveraged long-flat. The long-only book expresses unchanged on a spot venue with no borrowing, no leverage and no funding leg. No perpetual, margin, multi-asset, or cross-venue dependency is introduced. Real venue precision (tick/lot/min-notional), fees and liquidity must still abort-or-verify per the ledger rule before any execution use.

## Limitations

- Idealized next-completed-bar-close MARKET fills; no claim a live order achieves the completed close; no slippage model beyond the assumed 0.1% per-side fee (not a verified Binance tier).
- vnpy intrabar stop-order triggering is adapted to completed-bar-touch signals with close-bracket stop evaluation; trade events differ from a literal vnpy backtest.
- Continuous full-history indicator state is a researcher choice that can differ from the source's rolling-100 recompute near strict boundaries — disclosed, never source-native.
- The source's short leg is dropped (spot cannot short) and its 1m→15m synthesis is replaced by native 15m klines — both disclosed event changes.
- Exact-Decimal indicator arithmetic is pinned for reproducibility; bit-identity with any particular TA-Lib float build is not claimed — threshold-boundary sensitivity is disclosed.
- PASS here means pinned-engine expressibility of this fully specified derivative, not profitability, Qlib parity, Survivor status, source-native equivalence, or any live/Paper/Testnet authorization.

## Implementation status

`implementation_status: not-implemented`. No controller, executor config, backtest, Qlib recipe, or deployment artifact is created here. If this candidate is formally selected for execution without a reproducible executable recipe, the engineering route is `IMPLEMENTATION_NEEDED` (minimal strategy-specific implementation, then the same 01–05), never a second admission flag.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. `hb_ready_status: PASS` is a **Scout six-gate proposal awaiting independent Hermes Auditor review**, not independent approval, Qlib parity, Survivor, Hummingbot Certified, profitability or Paper/Testnet/Live authorization. The Auditor alone may source-fact remediate the exact head, merge on verified PASS, or close NOT_LOSSLESS. The existing signed GitHub webhook receiver alone performs post-merge README bookkeeping; Scout does not touch main/README or any workflow.

## Related Wiki records

None. This Scout cycle writes no Wiki Brain records.

## Sources

- https://github.com/vnpy/vnpy_ctastrategy/blob/c212d603e68a5f4dbbc160fe8f7f8b1e06be2494/vnpy_ctastrategy/strategies/boll_channel_strategy.py — vnpy, *BollChannelStrategy*, pinned commit 2026-10-04 (144 lines, 3785 bytes, SHA256 `4a8f7175…3faa3b`, blob `122b7d7c…bac3f3c`).
- https://github.com/vnpy/vnpy/blob/c6e231caf32b7fc97e6459817fff66458cf7e7c4/vnpy/trader/utility.py — `ArrayManager` rolling-100 init gate and SMA/STDDEV/CCI/ATR constructions, read 2026-10-30.
- https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3 — pinned engine source inspected (VERSION, 15m INTERVALS, MARKET-close simulator path, absent-price guard).
- https://github.com/HCH725/alpha-strategy-research/pull/414 — prior independent pinned wheel/source and MARKET primitive evidence.
- https://github.com/HCH725/alpha-strategy-research/pull/550 — prior bounded spot MARKET-close research execution evidence.
- https://github.com/HCH725/alpha-strategy-research/pull/448 — same-lane different-file prior proposal (vnpy AtrRsi, closed NOT_LOSSLESS); fenced as a different source with answered blocker classes.
