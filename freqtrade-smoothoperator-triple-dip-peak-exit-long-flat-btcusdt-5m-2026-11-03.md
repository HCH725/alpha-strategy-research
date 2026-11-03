---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "freqtrade SmoothOperator triple-dip TEMA-composite peak exit long with 10pct ROI and 5pct stop; independent BTC-USDT spot 5m long-flat derivative"
created: 2026-11-03
updated: 2026-11-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - freqtrade
  - source-backed
status: research-only
confidence: medium
source_as_of: 2022-07-10
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/7f91ff52bb664423ae673092a6a18d76c50c2c29/user_data/strategies/berlinguyinca/SmoothOperator.py
  - https://github.com/TA-Lib/ta-lib/blob/v0.6.4/src/ta_func/ta_MFI.c
  - https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# SmoothOperator triple-dip peak-exit long — independent derivative

## Provenance

- **Primary source:** public freqtrade strategy collection `freqtrade/freqtrade-strategies`, file `user_data/strategies/berlinguyinca/SmoothOperator.py` (class `SmoothOperator(IStrategy)` plus file-local helper class `StrategyHelper`; docstring attributes the idea to Gert Wohlgemuth: combining common indicators with heavy smoothing to detect a non-completed peak shape), read in full at immutable commit **`7f91ff52bb664423ae673092a6a18d76c50c2c29`** (2022-07-10, latest commit touching this file — an interface-version addition; no signal line changed by it; current repo HEAD `f3340ce` carries byte-identical content). Verified bytes this run: **304 lines, 13297 bytes**, SHA256 `46f608cc51f9b18e9bb52983776a6d55d9b13814a93f7666cc8ecdb4f86c3915`, Git blob SHA `cf5b30a86d11bc63e0b2dfb84a2a02ea30590838` matching the GitHub API blob SHA at the pinned commit. No login, no paywall.
- **Author playground disclaimer (disclosed, not adopted as a rule change):** the file header reads `DO NOT USE, just playing with smooting and graphs!` and the entry block carries large commented-out alternative gates (volume pump-guard, MACD filter, entry-band spike, candle-pattern OR, composite `< 0` arm). None of the commented alternatives fire — this record pins ONLY the live uncommented literals below. The disclaimer questions maturity, never determinism; every live line is a fixed formula.
- **Source facts actually verified (effective literals):** `INTERFACE_VERSION = 3`; `timeframe = '5m'`; `minimal_roi = {"0": 0.10}` (single 10% rung); `stoploss = -0.05`; trailing-stop comment only (`trailing_stop` literal absent — no trailing). Entry is the triple-OR `(VBottom | Oversold | SlowBuild)` AND the uptrend gate `close > close.shift(1)` (`enter_long = 1`). Exit is the triple-OR `(CompositePeak | Green9 | PumpOverbought)` (`exit_long = 1`). Full-file token census this run: 0 `short`; 1 `trailing` (prose comment `should be converted to a trailing stop loss` only — never a semantic); 0 `startup_candle_count`; 0 `use_exit_signal` / `exit_profit_only` / `ignore_roi` overrides (framework defaults True/False/False apply — exits fire even at a loss, disclosed defaults, never file literals); 0 `order_types` / `order_time_in_force`; 0 `leverage` / `can_short`; 0 `position_adjustment` / `pyramiding` / `max_open_trades` / `stake_amount`; 0 `informative` / `resample` / `merge`; 0 `hyperopt` / `*Parameter` (no fitted spaces); 3 `CDL` (comments only — no candle-pattern leg fires); 1 `volume` (comment only — live code reads volume solely inside the MFI14 construction, disclosed below); 0 `fillna` / `ffill` / `interpolate`; 0 negative shifts.
- **Dead columns fenced (computed, never gated):** `adx` (ADX14), `bb_lowerband`/`bb_upperband`/`bb_middleband` (BB20 std 2, graphing-only), `entry_bb_*` (BB20 std 1.6, unused — the live rail is the std-2 `bb_middleband`), `macd`/`macdsignal`/`macdhist`, `ema_close`, `bpercent`, `bsharp`/`bsharp_slow`/`bsharp_medium`/`bsharp_fast`, `candle_size`, `sma_slow`/`sma_medium`/`sma_fast` (SMA 200/100/50, never gated — warmup need not cover them). Live legs use ONLY: `cci` (CCI20), `rsi` (RSI14), `mfi` (MFI14 incl. volume), their EMA11 smooths, the TEMA21 composite, `average` (OHLC mean), `bb_middleband`, raw O/H/L/C. No reviewer repair may enable a fenced column or substitute a sibling constant.
- **Independent researcher-defined executable derivative (NOT source-native):** source pair list is agnostic, so pin single-asset Binance **BTC-USDT spot 5m**; freqtrade intrabar stop/ROI evaluation is adapted to **completed-bar-close evaluation with pinned priority stop-level → ROI → exit-signal**; ROI `{"0": 0.10}` maps to gross `>= 0.10` at post-fill bar age `a >= 1`; the −5% stop evaluates on completed closes as `C[t] <= P*0.95`; fills are next-completed-bar-close historical MARKET fills; fixed `Q = Decimal("0.001")` BTC, 10,000 USDT starting cash, 0.1% hypothetical per-side fee, 100-bar researcher warmup pin (the file ships no `startup_candle_count`; 100 covers the TEMA21 chained seed ≈ 60 + EMA11 seed 10 + CCI20/RSI14/MFI14 seeds with margin; dead SMA200 is fenced, never gated); single-unit/no-add/no-cooldown position pin; exact-Decimal ledger with fail-closed reconciliation. These researcher choices change trade events and economics.
- **Frozen identity:** `FT:SmoothOperator.py|7f91ff5|independent-derived-20261103|BinanceSpot-BTC-USDT-UTC5m|E3or(VBottom5fall+rail+ccir0129,OverSold-rail-cci200,SlowBuild-mfi10)+uptrend|Peak3or(compT-peak,green9,pump-cci200-rsi70)|ROI10pct@a1-gross|stop-5pct|next-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-each-side|warmup100|Decimal-ledger`. Any signal, timing, cost or position change creates a different derivative.

## Economic mechanism

### Source-reported

The file's docstring reports a smoothing idea (heavy EMA/TEMA smoothing of RSI/MFI/CCI to catch a peak shape before completion — author prose, **not traceable table/figure evidence and not relied upon here**). The coded mechanism: buy only a bar where one of three dip shapes prints (a five-bar V-bottom under the BB midline with cold CCI/RSI, a deep BB-midline washout with CCI below −200, or a slow-bleed MFI crush below 10) while the bar itself still ticks up; stand aside to flat when the smoothed composite crests above 100 and rolls over, when nine straight green bars print, or when CCI/RSI jointly overheat — behind a single 10% ROI rung and a −5% stop.

### Research interpretation

A triple-OR dip-catcher with a triple-OR peak exit, long-only. Unlike single-pattern records, the entry refuses to depend on one dip shape: the V-bottom arm demands a left-lopsided five-bar fall with rail and oscillator proof, the washout arm demands genuine extremity (CCI −200 with MFI confirmation), and the slow-build arm catches grinds the first two miss (MFI below 10 with RSI weaker than MFI) — frequency comes from the 5m frame, selectivity from the conjunction plus the uptrend tick. Unlike single-arm exits, the exit sells either a smoothed-composite crest, exhaustion (nine green), or joint overbought — chop that recovers without cresting or overheating is held, not banked. The coded consequence is a buyer of confirmed micro-dips that harvests only crested, exhausted or overheated recoveries, with a tight −5% stop and a 10% first-profit rung. No performance, profitability, Qlib parity or Survivor claim.

## Signal

Exact rules as pinned (any other CCI/RSI/MFI period, EMA/TEMA length, threshold, strictness, shift, rail pairing, ROI rung, stop, fill, frame, book, or leg combination is a different, unpinned rule):

```text
avg[t]  = (O+H+L+C)[t]/4
bbm[t]  = SMA20(close)                       // std-2 BB midline; bands dead
cci[t]  = TA-Lib CCI20 (high/low/close)
rsi[t]  = TA-Lib RSI14 (close, Wilder)
mfi[t]  = TA-Lib MFI14 rolling-sum (100*pos/(pos+neg), total<1.0 -> 0.0; volume inside)
rsiS/mfiS/cciS = TA-Lib EMA11 of rsi/mfi/cci
comp[t] = (rsiS*1.125 + mfiS*1.125 + cciS)/3
compT[t]= TA-Lib TEMA21(comp)
VBottom = (avg[-5]>avg[-4]>avg[-3]>avg[-2]>avg[-1]) AND (avg[-1]<avg[0])
        AND (low[-1]<bbm) AND (cci[-1]<-100) AND (rsi[-1]<30)
Oversold= (low<bbm) AND (cci<-200) AND (rsi<30) AND (mfi<30)
SlowBld = (mfi<10) AND (cci<-150) AND (rsi<mfi)
ENTER[t]= (VBottom OR Oversold OR SlowBld) AND (close[t]>close[t-1])
Peak    = (compT>100) AND (compT[-1]>compT) AND (compT[-2]<compT[-1]) AND (compT[-3]<compT[-2])
Green9  = open<close at t,t-1,...,t-8        // helper named eight_green_candles; literally nine bars
Pump    = (cci>200) AND (rsi>70)
EXITSIG[t] = Peak OR Green9 OR Pump
```

- **Commented alternatives fenced:** the file's commented volume-guard, MACD filter, entry-band spike, candle-pattern OR and `mfi_rsi_cci_smooth < 0` arm never execute and are never pinned. `seven_green_candles`, `eight_red_candles`, `four_green_one_red_candle`, `four_red_one_green_candle` helpers are never called — only `eight_green_candles` fires, literally nine consecutive green completed bars, disclosed naming quirk.
- **Exact boundaries:** strict throughout (`<`, `>`, `OR` exactly as coded — a low exactly on `bbm`, any oscillator exactly on its threshold, `close` exactly equal to its prior close, or `compT` exactly on 100 fires nothing on that conjunct). All shifts are non-negative completed-bar inputs; no repaint, no future extremum, no negative shift. Volume fires no independent leg — zero-volume bars behave literally through MFI arithmetic, disclosed.
- **Warmup:** first **100** valid fully completed 5m bars, indices 0–99, are data-only, FLAT, and never emit orders (researcher pin — the file ships no `startup_candle_count`; 100 covers the TEMA21 chained seed plus every live 20/14/11-period seed with margin; the dead SMA200 is fenced, never gated). First decision may occur at index 100. NaN-leading comparisons and edges are false, so pre-seed bars could never fire in any case. No optimizer, ML, external feed, negative shift, future extremum, repaint or fitted parameter at research time.
- **BUY state:** initial `FLAT`, 0 BTC, 10,000 USDT cash. At eligible `E[t]` (`t >= 100`), if FLAT with no pending order and `ENTER[t]` true, queue exactly one fixed `Q = Decimal("0.001")` BTC MARKET BUY for the **next completed bar** `f = t+1`; do not use bar f's data to decide at t. At `E[f]`, use actual finite `C[f]` as the idealized simulator fill, if `cash >= Q*C[f]*(1+fee)` in exact Decimal. If insufficient cash, consume the signal, remain FLAT, and do not invent a partial fill or deferred order. A confirmed full fill sets LONG, records fill price `P = C[f]` and `fill_index = f`. No signal or exit evaluation on the fill bar.
- **LONG exits (evaluated at each `E[t]`, `t > f`, in fixed priority; at most one exit per bar):** (1) **stop:** exit if `C[t] <= P*0.95`; (2) **ROI** on fee-exclusive gross `(C[t]-P)/P`: exit if `>= 0.10` at post-fill bar age `a = t-f >= 1`; (3) **exit-signal:** exit if `EXITSIG[t]` true (`use_exit_signal` True / `exit_profit_only` False framework defaults — fires even at a loss, disclosed defaults). The winning exit queues exactly one MARKET SELL for the next completed bar `s = t+1` at real `C[s]`, sells the full Q, sets FLAT. No exit executes if its required future bar is absent; the pending order stays unfilled at sample end. No evaluation on the SELL fill bar; earliest re-entry decision is a later eligible bar.
- **State priority and exclusions:** at most one pending action and one position; a pending order takes precedence over new signals. There is no cooldown, pyramiding, DCA/safety orders, averaging, partial sizing, shorts, borrowing, leverage, margin, shared-capital concurrency, session filter, intrabar stop/limit/maker, or end-of-sample forced liquidation. An open LONG at the end is valued at the last **actual valid close**, never synthetically liquidated. Same-bar entry/exit exclusion holds by construction: entries act only from FLAT, exits only while LONG, and fill bars evaluate nothing.
- **Exact Decimal ledger (position truth):** all research accounting uses `Decimal(str(x))` for observed closes (never `Decimal(float)`), exact `Q`, exact products. BUY debits `Q*P*(1+fee)` USDT and credits exactly Q BTC; SELL debits exactly Q BTC and credits `Q*P*(1-fee)` USDT. `FLAT` holds **iff** ledger BTC `== Decimal("0")` exactly — arithmetically guaranteed since the identical Q added at fill is subtracted at close; no epsilon exists anywhere. Simulator quote/fee outputs are cross-checked only: if `|sim_quote - Q*P| > max(1e-8, 1e-12*Q*P)` or the fee check fails, or side/amount disagree, **abort the run as ENGINE_MISMATCH** — never round, never absorb dust, never infer state from the simulator. The controller-side ledger alone drives FLAT/LONG.

## Required data

Only actual Binance BTC-USDT spot UTC 5m O/H/L/C/V (volume read solely inside the MFI14 construction — no independent volume gate). Indicator-plus-rail predicates use bar t's **completed** inputs at `E[t] = T[t] + 300 seconds` (T[t] the exchange open timestamp); the queued order's fill at `E[t+1]` is not used retroactively. Stop high-water/age accounting starts at the **confirmed full-fill** index, not the signal bar. No higher/lower timeframe, funding rate, order book, multi-asset feed, external sentiment or ML inference. Input validation: strictly increasing, gap-free 300-second UTC open timestamps; finite positive O/H/L/C, `H >= max(O,C)`, `L <= min(O,C)`, `H >= L`, finite `V >= 0`, no duplicate bars. **Abort the research run** on any missing, invalid, duplicate or discontinuous candle; do not forward-fill, interpolate, fabricate prices, quietly skip a gap, or emit synthetic fills/mark prices.

## Execution assumptions

- **Pinned contract:** Hummingbot package **`20260920`**, `hummingbot/VERSION = dev-2.17.0` (bytes read at the bounded commit in a prior reviewed cycle), bounded source commit **`HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`**. This cycle verified via the GitHub API at the pinned commit: `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` `INTERVALS` maps **`5m`** (with `1s`/`1m`/`3m`/`15m`/`30m`/`1h`/`2h`/`4h` and higher); `backtesting_data_provider.py` returns `Decimal("1")` when price is absent — **never** used for fills or marking, actual positive closes required; `strategy_v2/backtesting/executors_simulator/order_executor_simulator.py:22` branches MARKET, `:56` takes the fill row's real `close` as `entry_price`, `:59` computes `float(config.amount) * entry_price`, `:60-62` writes quote/fees, `:70` returns `CloseType.POSITION_HOLD`. The float line is exactly why this record's position truth is the independent Decimal ledger, never simulator auto-netting. No wheel re-download/hash this cycle; prior independently reviewed alpha PR **#414** reports 902/902 matching wheel Python files and SHA256 `ea5a929c...a148`; the independent Auditor must confirm that evidence applies to the pinned package and path.
- **Controller/executor:** `BacktestingEngineBase.simulate_execution` iterates feature rows, updates state, then calls `controller.determine_executor_actions()` and processes `CreateExecutorAction`. A **future dedicated controller is not implemented**; it must queue the previous completed signal and emit `OrderExecutorConfig(connector_name="binance", trading_pair="BTC-USDT", side=TradeType.BUY/SELL, amount=Decimal("0.001"), position_action=OPEN/CLOSE, execution_strategy=ExecutionStrategy.MARKET, price=None, leverage=1)` on the designated fill row, without using that row to decide the preceding signal. No claim of a deployed controller or exchange-accepted order.
- **Actual fill path:** MARKET uses the first supplied row's real `close`; sets `filled_amount_quote = float(amount)*close`, `cum_fees_quote = trade_cost * filled_amount_quote`; returns `POSITION_HOLD`. The engine's raw row timestamp is bar-open; this research model reports the **effective historical fill event** as `E[fill_row]`, not a claim a real order could execute at the completed close. A delayed controller dispatch on row `t+1` is required. The simulator does not independently verify live latency, spread, partial fills, tick/lot/min-notional or exchange acceptance; any such failure aborts per the ledger rule instead of rounding.
- **Missing price and economic limitations:** no **additional modeled** slippage is included in this idealized MARKET-close research convention; this is **not** a claim of zero real slippage. The 0.1% fee is an explicit research assumption, **not** a verified Binance tier. Spot unleveraged BTC/USDT has no perpetual funding or liquidation cash flow; this does **not** assume perpetual funding is zero. Real exchange fees, liquidity, precision and market impact are unverified.
- **Reused capability boundary:** this uses only the already reviewed single-pair Binance spot OHLCV → controller action → MARKET-close `OrderExecutorSimulator` → POSITION_HOLD primitive, as previously documented in alpha PRs **#414** and **#550** (plus admitted spot records' bounded paths). The new strategy changes only controller-side CCI/RSI/MFI/EMA/TEMA/BB predicates, the single-rung ROI/stop bar-close stack and the Decimal ledger; not the data/executor market path. No Hummingbot or Qlib test is performed in this Scout. If a new execution primitive is required, one representative Hummingbot↔Qlib event-level parity validation is required **before mass screening**, not as a profitability admission gate.

## Evidence

### Source-reported

The pinned `SmoothOperator.py` bytes support every constant cited above (timeframe, ROI rung, stop, the triple-OR entry with the uptrend gate, the triple-OR exit, `INTERFACE_VERSION`). The header disclaimer and commented alternatives support no live rule and are fenced above. The TA-Lib `ta_MFI.c` v0.6.4 bytes support the rolling-sum formula and the `total < 1.0 → 0.0` guard.

### Independently reproduced

Float-transcription probe (TA-Lib-semantics EMA/SMA/Wilder-RSI/CCI/MFI/TEMA re-implemented in pandas — honest transcription, **not** bit-identical TA-Lib) over **5,000 live Binance BTC-USDT spot 5m bars**: post-warmup ENTER fires **20** (raw pre-uptrend-gate: VBottom 22, Oversold 45, SlowBuild 1); exits Peak 0, Green9 5, PumpOverbought 38; zero same-bar entry/exit co-fires in the 1,000-bar subsample; causality verified by construction (no negative shift anywhere; `shift(0)` is the current completed bar). Naive next-bar-close long-flat walk with the pinned priority completes without internal contradiction. No freqtrade backtest, Hummingbot/Qlib event, performance, OOS or realized-fee claim.

### Negative evidence

Pre-write dedup 2026-11-03 against `main@45d248be` (full tree, excluding two READMEs): filename/content search for `smoothoperator`, `mfi_rsi_cci`, `eight_green`, and the triple-OR dip conjunction returns **zero strategy records** — no pool record cites this source file or conjoins a V-bottom/washout/slow-build entry with a TEMA-composite-crest exit. The sole hit is a sibling-fence mention inside the admitted TechnicalExample record, which explicitly excludes this file. All open `research/*` PRs (#48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646, #662, #688, #690, #708) were inspected by source/title/branch and none uses this source or rule. Nearest pool neighbors use different mechanisms: `freqtrade-smoothscalp-7gate` (seven-conjunct EMA-rail entry, 1m, ROI 1% / stop −50%); `freqtrade-cofibit-stochf-ema-rail-adx-gated` (five-conjunct StochF-rail-ADX, 5m, hyperopt ladder); `td-sequential-setup9-perfected` (sequential-count family, different construction); `freqtrade-technical-cmf-sign-state` (CMF-sign state, fences this file as a sibling). This is not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

Future authorized research only (no backtest, trading, deployment or cron change here): rail-equality (`low == bbm` no-fire); oscillator/threshold exact-boundary no-fire; `close == close[-1]` no-fire; V-bottom shift-chain off-by-one; Green9 eight-vs-nine boundary; composite-crest shape off-by-one; TEMA21-vs-naive-EMA divergence at the 100 boundary; MFI rolling-vs-Wilder divergence at the 30/10 boundaries; zero-volume bars behaving literally through MFI; NaN-leading pre-seed silence; warmup 99/100 boundary; signal t versus fill f; stop versus ROI versus exit-signal priority ties; ROI age-1 boundary; insufficient cash; last-bar pending; full-fill fee ledger; `Decimal(str())` versus float reconciliation; ENGINE_MISMATCH abort path.

## Crypto portability

Binance BTC-USDT spot, 5m, unleveraged long-flat. The long-only book expresses unchanged on a spot venue with no borrowing, no leverage and no funding leg. No perpetual, margin, multi-asset, or cross-venue dependency is introduced. Real venue precision (tick/lot/min-notional), fees and liquidity must still abort-or-verify per the ledger rule before any execution use.

## Limitations

- Idealized next-completed-bar-close MARKET fills; no claim a live order achieves the completed close; no slippage model beyond the assumed 0.1% per-side fee (not a verified Binance tier).
- Freqtrade intrabar stop/ROI evaluation is adapted to completed-bar-close evaluation with the disclosed priority; trade events differ from a literal freqtrade backtest.
- Exact-Decimal indicator arithmetic is pinned for reproducibility; bit-identity with any particular TA-Lib float build is not claimed — threshold-boundary sensitivity is disclosed.
- The file's `DO NOT USE` playground header and commented alternatives are disclosed and never adopted; single-unit pin is a researcher choice, disclosed.
- PASS here means pinned-engine expressibility of this fully specified derivative, not profitability, Qlib parity, Survivor status, source-native equivalence, or any live/Paper/Testnet authorization.

## Implementation status

`implementation_status: not-implemented`. No controller, executor config, backtest, Qlib recipe, or deployment artifact is created here. If this candidate is formally selected for execution without a reproducible executable recipe, the engineering route is `IMPLEMENTATION_NEEDED` (minimal strategy-specific implementation, then the same 01–05), never a second admission flag.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. `hb_ready_status: PASS` is a **Scout six-gate proposal awaiting independent Hermes Auditor review**, not independent approval, Qlib parity, Survivor, Hummingbot Certified, profitability or Paper/Testnet/Live authorization. The Auditor alone may source-fact remediate the exact head, merge on verified PASS, or close NOT_LOSSLESS. The existing signed GitHub webhook receiver alone performs post-merge README bookkeeping; Scout does not touch main/README or any workflow.

## Related Wiki records

None. This Scout cycle writes no Wiki Brain records.

## Sources

- https://github.com/freqtrade/freqtrade-strategies/blob/7f91ff52bb664423ae673092a6a18d76c50c2c29/user_data/strategies/berlinguyinca/SmoothOperator.py — berlinguyinca, *SmoothOperator* (Gert Wohlgemuth idea), pinned commit 2022-07-10 (304 lines, 13297 bytes, SHA256 `46f608cc…8ecdb4f8`, blob `cf5b30a8…30590838`).
- https://github.com/TA-Lib/ta-lib/blob/v0.6.4/src/ta_func/ta_MFI.c — first-party TA-Lib rolling-sum MFI with ring-buffer flows and the `total < 1.0 → 0.0` guard, read 2026-11-03.
- https://github.com/HCH725/hummingbot/blob/8b0e067e80ab62f10846d518dcb5a8218527ddb3/hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py — pinned engine `5m` INTERVALS mapping, read 2026-11-03 via API at the bounded commit.
- https://github.com/HCH725/alpha-strategy-research/pull/414 — prior independent pinned wheel/source and MARKET primitive evidence.
- https://github.com/HCH725/alpha-strategy-research/pull/550 — prior bounded spot MARKET-close research execution evidence.
