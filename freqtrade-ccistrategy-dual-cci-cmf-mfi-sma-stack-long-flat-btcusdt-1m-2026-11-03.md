---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: freqtrade CCIStrategy dual-CCI CMF/MFI 5m-SMA-stack long-flat on BTCUSDT 1m bars
created: 2026-11-03
updated: 2026-11-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-08
sources:
  - https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/CCIStrategy.py
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# freqtrade CCIStrategy dual-CCI + CMF/MFI + 5m-SMA-stack — independent BTC-USDT spot 1m long-flat derivative

## Provenance

**Primary public GitHub identity:** `freqtrade/freqtrade-strategies`, file `user_data/strategies/berlinguyinca/CCIStrategy.py`, class `CCIStrategy(IStrategy)` (the only class in the file; verified by `^class ` count of 1 over the full 120 lines this cycle). Pinned commit `f3340ce11f5bdf62f598522e64d1f5638eaa13f5` (committed `2026-09-08T16:42:47Z`), returned as the repository `main` HEAD by `git ls-remote` this cycle (2026-11-03) — the same HEAD the admitted `berlinguyinca` AverageStrategy sibling pinned on 2026-10-31. GitHub blob SHA `b3f17834e1905d6037de54ffdc2341e1067a3d60`, 4459 bytes, 120 lines; the raw file fetched at the pinned commit reproduces that blob via `git hash-object` (SHA-256 `c3b1f8b57850d12a1e1b4e1ec42e92b842b2384f439e177f9e711bd20d698aad`) — the entire file was read, not sampled. The file's last-touch commit is `bcca7d7aef0df373c29b80532c8c02663f25ae3f` (`2022-07-10T13:14:30Z`, interface-version sweep); the blob at that commit is byte-identical (`b3f17834…`, 4459 bytes), so no newer file revision exists to diverge from. The repository carries a GPLv3 `LICENSE`; this record cites and normalizes the rule (single-line declarations only for gate evidence) and reproduces no source block.

**The file's own words (quoted for gate evidence, never extended):** `timeframe = '1m'`; `minimal_roi = {"0": 0.1}` (single 10% rung); `stoploss = -0.02`; `ta.CCI(dataframe, timeperiod=170)` / `ta.CCI(dataframe, timeperiod=34)` / `ta.RSI(dataframe)` / `ta.MFI(dataframe)`; in-file `chaikin_mf` with `periods=20`, `mfv.fillna(0.0)` on zero-range bars, `rolling(periods).sum()` ratio; `resample` helper: `df.resample('5min', label="right")` OHLC aggregation, `ta.SMA` 100/50/25/200 on the 5m closes named `resample_sma/medium/short` (50) /`resample_long` (200), `df.resample('1min')` downsample with `interpolate(method='time')`, left-merge on `date`. Entry is the six-way AND `(cci_one < -100) & (cci_two < -100) & (cmf < -0.1) & (mfi < 25) & (resample_medium > resample_short) & (resample_long < close)` setting `enter_long`. Exit is the five-way AND `(cci_one > 100) & (cci_two > 100) & (cmf > 0.3) & (resample_sma < resample_medium) & (resample_medium < resample_short)` setting `exit_long`. The file ships no market, venue, sizing, capital, fee, warmup, performance figure, or trade count of any kind.

**Full-file token census (verified by search over the 120 lines this cycle):** 0 `IntParameter(`/`DecimalParameter(`/`CategoricalParameter(`/`BooleanParameter(` (every threshold is a literal — no fitted space, no variant menu); 1 `enter_long` / 1 `exit_long`; 0 `enter_short` / 0 `exit_short` / 0 `short` (long-flat by construction); 16 `resample` (helper + legs); 1 `interpolate`; 0 `adjust_trade_position` / 0 `position_adjustment` / 0 `custom_stake` / 0 `leverage(` / 0 `can_short` (framework defaults apply, disclosed below); 0 `trailing_stop` / 0 `startup_candle_count` / 0 `protections` / 0 `cooldown`; 0 `use_exit_signal` / 0 `exit_profit_only` / 0 `order_types` / 0 `process_only_new_candles`; 0 `informative` / 0 `mark_price` / 0 `funding`; 0 `crossed_above` / 0 `crossed_below` (level states, never edges); 4 `volume` (all inside the `chaikin_mf` definition — no volume-weighted fill, no depth model). `ta.RSI` and the `qtpylib.bollinger_bands` trio are computed but never read by any order-gating line (dropped, disclosed).

**Out-of-file calls pinned (all resolved by name, all literal-or-default):** `ta.CCI`/`ta.MFI`/`ta.SMA` (TA-Lib abstract defaults: CCI over typical price `(H+L+C)/3` with the `0.015 × mean-deviation` normalization, zero-deviation prints `0.0`; MFI period 14; SMA over close); `ta.RSI` (default 14, computed but unread). The record defines every formula below rather than relying on any vendor copy.

**Declared independent derivative v1, NOT source-native/lossless:** select **Binance BTC-USDT spot 1m, long/flat only**; pin every file-default literal above; keep the file's single-rung 10% ROI as a fixed 10% take-profit and the `-0.02` stoploss as a fixed 2% stop (source literals, never re-tuned); replace the file's `interpolate(method='time')` upsampling with a last-completed forward-hold (the interpolation reads the not-yet-completed next 5m grid point on every non-grid 1m bar — future leakage fenced OUT, never ported; the forward-hold matches Freqtrade's own `resampled_merge` causal convention); fix one `0.01 BTC` unit, one-position-only, no DCA, no cooldown; fix a 1020-completed-bar warmup; next-bar-open MARKET fills with evaluation from fill+1 and the SL > TP > signal same-bar ordering below. All changes are part of this **separate strategy**, not evidence that the source file is expressible unchanged.

**Immutable research identity:** `FT-CCIStrategy-f3340ce | derived-v1-dualCCI170-34_CMF20_MFI14_SMAstack5m | BTC-USDT-binance-spot-1m | long-flat | TP10-SL2-nextopen | 2026-11-03`. Changing any component changes the derivative identity.

**Pre-write dedup:** `main@5cfaa382`, 529 root-level strategy Markdown records. Working-tree searches for `CCIStrategy` return only the sibling-fence mentions inside `freqtrade-strategy005` and `freqtrade-technical-cmf-sign-state` — both explicitly fence this file as a different, unclaimed construction (dual-CCI dip plus resampled-trend insurance, 1m), never a record. Sixteen open `research/*` PRs inspected by number/title/head — none uses this file or rule (nearest is #304, the Forven single-CCI(20) ±100 recross long-flat on 1h: one oscillator, recross edges, no CMF/MFI/SMA leg, no ROI/stop, different source — fenced in Negative evidence). Nearest pool families are materially different constructions (see Negative evidence): Eterna single-CCI(20) ±100/±200 cross-plus-extreme two-sided 4h; Forven single-CCI(20) recross 1h; SmoothScalp 1m seven-gate (STOCHF/EMA/ADX/MFI/single-CCI14, 1% ROI, −50% stop, no CMF, no 5m stack, no dual-CCI); Technical CMF-sign-state 5m (single-CMF-sign, no CCI); Forven Chaikin-MF-threshold 1h and Forven MFI-threshold 1h (single-indicator thresholds, zero CCI tokens); CCI-EMA-RSI-cross-trailing 1h (triple-gate plus ratchet). No pool record conjoins dual-length CCI with CMF, MFI, and a 5m-SMA regime stack. Not a duplicate, paraphrase, or trivial parameter variant.

## Economic mechanism

### Source-reported

The source claims only what its code prints: on 1m bars, buy when the 170-bar and 34-bar CCIs both sit under −100 while 20-bar Chaikin money flow sits under −0.1, 14-bar MFI sits under 25, the 5m 50-bar average sits above the 5m 25-bar average, and price sits above the 5m 200-bar average; sell when both CCIs sit over +100 with money flow over +0.3 under a stacked 5m 100 < 50 < 25 average decline; a single 10% ROI rung and a −2% stoploss backstop positions under Freqtrade execution. No market, sample, or performance claim is adopted.

### Research interpretation

Dip-buying inside a 5m uptrend with washed-out oscillators: the 5m-SMA stack (`SMA50 > SMA25`, `close > SMA200`) refuses downtrends and deep breaks — entries only print on pullbacks that hold the long average — while the four oscillator legs (dual-CCI depth, CMF outflow, MFI washout) refuse early entries before selling exhausts. Unlike the pool's bare single-CCI recross records (which fire on two threshold comparisons with no confirmation), this six-way AND fires strictly later and rarer — the live window prints 9 entries over ~7 days of 1m bars — at the cost of holding through the whole pullback with only the 10%/−2% backstops plus the opposite-extreme conjunction as exits. Unlike stop-and-reverse systems there is no short leg and no flip book: a flat book simply waits. The 5m legs move only once per five 1m bars under the forward-hold pin, so the 1m-native oscillators drive timing while the 5m stack drives permission.

## Signal — Gate 1, fully pinned derivative

**Input:** one UTC Binance BTC-USDT spot 1m OHLCV stream `O[t],H[t],L[t],C[t],V[t]`; `t` is a completed bar. Validate finite `O,H,L,C>0`, `H>=max(O,C)`, `L<=min(O,C)`, `V>=0`, strictly consecutive open-time timestamps 60 seconds apart, no duplicates. Reject the run before feature preparation on any missing/invalid/nonconsecutive bar; no dropna bridging, synthetic bars, or price fallback.

**Features (file-default literals pinned):** with `TP=(H+L+C)/3`: `cciN[t]=(TP[t]−mean(TP[t−N+1..t]))/(0.015×mean(|TP−mean|))`, `N∈{170,34}`, zero-deviation prints `0.0`; `mfi[t]` standard 14-bar money-flow index (`100×pos/(pos+neg)`, all-flat window prints `0.0`); `cmf[t]=sum(mfv,20)/sum(V,20)` with `mfv=((C−L)−(H−C))/(H−L)` per bar, `0.0` on zero-range bars (source `fillna`), `NaN` when the 20-bar volume sum is zero or any read is non-finite; 5m grid `O5/H5/L5/C5` from completed right-labeled 5-minute bins with `smaK[t]=mean(C5, K)`, `K∈{25,50,100,200}`, forward-held (last-completed value carried across the five 1m bars — the causal pin replacing interpolation; developing-bin reads fenced out, never evaluated). `rsi14` and the Bollinger trio are never materialized in this derivative — computed-but-unread in source, absent here. NaN-leading comparisons are false, so pre-seed bars can never fire.

**Completed-bar long entry predicate `E[t]`** (exact six-way AND, no epsilon, `t≥1020`, every feature finite, FLAT, no pending order): `cci170[t]<−100 & cci34[t]<−100 & cmf[t]<−0.1 & mfi[t]<25 & s50[t]>s25[t] & C[t]>s200[t]`.

**Signal exit `X[t]`** (exact five-way AND, no epsilon, LONG only): `cci170[t]>+100 & cci34[t]>+100 & cmf[t]>+0.3 & s100[t]<s50[t] & s50[t]<s25[t]`. An open LONG additionally carries a latched 10% take-profit (`C≥entry×1.10`) and 2% stop (`C≤entry×0.98`) from the file's ROI/stoploss literals. Exits evaluate from fill+1 onward at bar closes with next-bar-open fills; same-bar co-fire order is SL first, then TP, then signal (one flat close — predeclared researcher pin, disclosed, never a source sentence).

**Co-fire pin (proven mutually exclusive, disclosed):** `E[t]` needs both CCIs strictly under −100 while `X[t]` needs both strictly over +100 — jointly impossible on one bar; a bar at exact ±100 satisfies neither (held, never forced). Entry fires only when FLAT and exits only when LONG, so no ordering between the two conjunctions exists to verify. No funding/OI/mark-price read anywhere in the gating path.

**Direction (Gate 2):** BUY only; SELL only to close the confirmed long. No short, borrowing, futures, hedge, leverage, negative inventory, or cross-market trade. The file contains no short leg anywhere (verified zero `enter_short`/`exit_short`/`short` code tokens).

**Risk (Gate 3, explicit):** opposite-extreme signal exit plus fixed 10% TP plus fixed 2% SL (`use_exit_signal=True`, `exit_profit_only=False` framework defaults apply — exits fire even at a loss; disclosed defaults, never file literals). No trailing (absent in source), no time stop, no partial exit, no averaging, no forced end-of-data liquidation, no silent executor default.

**State (Gate 4):** `FLAT`, `BUY_PENDING`, `LONG`, `SELL_PENDING`. Initialize `FLAT` after 1020 valid completed bars. A BUY request transitions to `BUY_PENDING`; only a confirmed MARKET fill transitions to LONG. A missing/failed/unconfirmed fill **halts** this research run; never synthesize inventory. While LONG, all entry predicates are ignored (no `adjust_trade_position` exists in source — single by construction). SELL request transitions to `SELL_PENDING`; only a confirmed filled SELL of the complete 0.01 BTC returns to FLAT. No cooldown is specified (explicitly none, not invented); re-entry re-arms on the next `E[t]` bar after any exit. No pyramiding, no DCA/safety orders (the downstream house overlay is not active in this admission), no concurrency, no compounding. A pending order prohibits additional actions. An end-of-sample LONG is marked at the last real valid close, not closed with an invented fill.

## Required data / Gate 6 causality

**Warmup:** minimum 1020 contiguous completed 1m bars before the first actionable bar — 200 completed 5m windows for the SMA200 seed (the binding structural minimum; first finite feature row verified at 1m index 1000 this cycle) plus 4 windows margin per the admitted precedent chain. No warmup-bar trades; initial state and all rolling values start from the actual first historical bar, not from full-sample fitted statistics. Pre-warmup and any NaN-feature bars are flat by record rule; missing bars halt the run — prices are never fabricated. No repainting (5m legs read completed bins only under the forward-hold pin; the file's developing-bin interpolation is fenced out), no negative shift, no future reference, no full-sample normalization; exactly one evaluation per completed 1m bar.

Binance Kline `timestamp` is the **bar-open** `T[t]`; a bar's OHLCV and every derived line become available no earlier than `T[t]+60s`, and each 5m grid value no earlier than its bin's completion. All decisions and fills are effective at completed-bar closes with next-bar-open fills. If this effective-time discipline cannot be enforced, Gates 5/6 fail in implementation.

## Execution assumptions / Gate 5 pinned Hummingbot path

**Exact bounded engine:** Hummingbot package label `20260920`, VERSION `dev-2.17.0`, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3` (ancestor of local checkout `2dbc844` verified this cycle via `merge-base --is-ancestor`; code paths re-verified at the pin this cycle: `async def run_backtesting` in `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py` line 221, `def determine_executor_actions` in `hummingbot/strategy/strategy_v2_base.py` line 747, `class OrderExecutorSimulator` byte-present in `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` line 9, `INTERVALS "1m"/"5m"` in `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` lines 13/15). Prior merged Alpha PR **#414** reports a 902/902 wheel-file byte match and 33-assert representative validation for this source/package path; this Scout did not independently rehash the wheel. A different deployed package must be revalidated. A strategy-specific, not-yet-implemented controller must compute the dual-CCI/CMF/MFI/5m-SMA features with the forward-hold pin and the TP/SL latch via `CreateExecutorAction(OrderExecutorConfig)` market legs; the generic executor does not calculate the strategy.

- **Market/feed:** `BinanceSpotCandles` one-spot-stream design — `binance` connector, `BTC-USDT`, `1m` decision frame with a derived causal 5m grid (single feed, no second symbol, no session, no cross-venue state). Opens feed next-open fills.
- **Orders (OrderExecutor only — PositionExecutor deliberately unused):** `side=BUY/SELL`, `position_action=OPEN/CLOSE`, `amount=Decimal("0.01")` (≈768.5 USDT at probe close 76,852.02 — above the verified 5-USDT min-notional and 0.00001 min-qty; 10,000 USDT cash), `connector_name="binance"`, `trading_pair="BTC-USDT"`, `execution_strategy=MARKET`, `price=None`, `leverage=1` (spot). MARKET legs fill at the next bar's **open** per the record timing pin (Freqtrade-backtest-faithful; never a live-engine claim). No fill executes if its required future bar is absent. Exit evaluation starts at `fill+1`, so every exit decision acts on a fill confirmed at least one full bar earlier. Controller must use confirmed executor/hold state with a persistent ledger, never infer position from order requests. Fills are never conditional on equity or buying power beyond the fixed single unit with no compounding and no abort rule (disclosed).
- **Fees and accounting:** pin `trade_cost=0.0002` per filled side (the pinned `run_backtesting` default, same lane primitive as the admitted AverageStrategy sibling) — **hypothetical 0.02% each side**, not actual Binance fee; no slippage/spread modeled, **not** evidence of zero real slippage. Never treat engine PnL as fee-inclusive net equity without rebuilding from the fill ledger plus recorded fees. Spot funding is **not applicable**, never fabricated as futures zero. Precision beyond min-qty/min-notional/tick facts, partial fills, market impact and live fee tier remain unverified — not an execution or profitability approval.
- **Package/commit binding disclosure:** `20260920` is retained as the policy package **label only**; Gate 5 is bounded to the pinned commit's research-simulation semantics re-verified above, reusing the previously reviewed MARKET next-open primitive with close-decided signal legs and fixed TP/SL legs and no novel executor type. The local checkout additionally carries the DCA early-stop settlement fix — this derivative holds no DCA leg and its stop/TP legs never invoke intrabar stop-fill semantics (close-decided, next-open by record rule), so that change cannot move any event here. Sibling PASS records are execution-path evidence only, never proof of this candidate.

## Evidence

### Source-reported

The pinned 4459-byte file ships the complete construction: the `1m` timeframe, the `{"0": 0.1}` ROI rung, the `-0.02` stoploss, the literal CCI(170)/CCI(34)/MFI/SMA(100/50/25/200)/CMF(20) constructions with the in-file money-flow formula, the right-labeled 5m resample with time-interpolation, the six-way entry AND, the five-way exit AND, and the long-flat posture (zero short tokens). It ships no performance figure of any kind — none adopted.

### Independently reproduced

**None.** No strategy backtest, event-level Qlib/Hummingbot parity, wheel rehash, deployment or profitability experiment occurred. Pinned engine source inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifacts this run are researcher self-checks of the predicate/feature/state pipeline (definitional TA-Lib-conformant re-implementation — not byte-parity with TA-Lib — 1020-bar warmup, forward-hold 5m discipline, next-open single-unit long-flat machine with SL > TP > signal ordering), run in scratch (never committed): logic verification only, not a backtest, not parity.

**Planted-tape verification (this cycle, deterministic PASS):** TAPE-CONST (dead-flat 1400 bars) prints post-warmup all-flat (0 entries / 0 exits, FLAT); TAPE-RISE (monotone drift) prints all-flat (no washed-out bar, FLAT); TAPE-SINE (±3 amplitude wave) prints all-flat (oscillators never reach the ±100 extremes, FLAT); TAPE-CRASH (flat base plus 120-bar triangle chop above the grid SMA200) prints 1 post-warmup entry driving 1 open / 1 signal-exit close ending FLAT — the full six-leg entry path and the opposite-extreme exit path both proven reachable, first finite feature row at 1m index 1000 on every tape.

**Live-exchange microstructure probes (this cycle, spot 1m klines, 9,999 completed bars ≈ 2026-10-27→2026-11-03, forming bar dropped by closeTime, 0 non-finite rows, last close 76,852.02):** first finite feature row at index 1000 (structural SMA200 minimum; 20-bar researcher margin to the 1020 warmup); 8,979 post-warmup defined bars drive 9 state-machine entries / 8 exits (7 opposite-extreme signal exits / 0 TP / 1 SL) ending LONG-held at the honest window cut with no invented fill. Feature ranges live: CCI170 [−494.47, +613.64], CCI34 [−537.60, +495.44], MFI [0.00, 100.00], CMF [−0.74, +0.72]. Repeated runs print identical event counts. 0.01 BTC ≈ 768.5 USDT notional at window close. Admission is engineering capability, never an event-rate or profitability claim.

### Negative evidence

1. Hyperopt absence fenced: the file instantiates zero `*Parameter` objects — every threshold, length, rung, and stop is a literal. There is no variant menu to choose from, so a reviewer must not substitute any re-tuned value.
2. Interpolation leakage fenced: the file's `interpolate(method='time')` blends each non-grid 1m row from the next (not yet completed) 5m grid point. This record replaces it with the last-completed forward-hold and evaluates every 1m bar causally; any developing-bin read the source backtester may perform is fenced OUT and unclaimed — the record is never evidence the file runs leak-free as written.
3. Unread columns fenced: `rsi14` and the Bollinger trio are computed but never gate any leg — dropped, never reintroduced as confirmation. A reviewer must not graft them back as filters.
4. Exact-zero and NaN determinism fenced: strict inequalities throughout — exact-threshold prints satisfy neither leg (held); any non-finite feature bar is a no-fire bar by record rule; zero-range bars contribute `0.0` money-flow (source `fillna`), and a zero 20-bar volume sum prints `NaN` (flat, never interpolated).
5. Overlap fences, admitted plainly: open PR #304 (Forven single-CCI(20) ±100 recross pair, 1h, no gate, no CMF/MFI/SMA, no ROI/stop, different repository) is a bare-oscillator recross object — this record's six-way AND never reduces to it on any bar (different oscillator count, lengths, gate set, exits, frame, source); sibling `cci-threshold-extreme-reversal` (Eterna single-CCI(20) ±100 crosses plus ±200 extremes, two-sided 4h, no stops, no gates) differs on every axis the same way plus direction; sibling `freqtrade-smoothscalp-7gate` (1m STOCHF/EMA/ADX/MFI/single-CCI14 with 1% ROI and −50% stop, no CMF, no dual-CCI, no 5m stack) is a different conjunction with different lengths and exits; siblings `freqtrade-technical-cmf-sign-state` (single-CMF-sign, 5m), `forven-chaikin-mf-threshold-cross` and `forven-mfi-threshold-cross` (single-indicator thresholds, zero CCI tokens) share vocabulary, never signal; `cci-ema-rsi-cross-trailing-stop`, `freqtrade-strategy004`, `freqtrade-swinghightosky`, `freqtrade-macd-cci-dip/cross` carry extra cross/gate/trailing machinery this rule never reads; the `berlinguyinca` Quickie/SmoothScalp/Average/FSample/FOtt/FSupertrend/FAdxSma records are different files, indicators, and legs. Shared `CCI ±100` vocabulary is not shared signal.
6. No hidden variants admitted: any other CCI length, threshold, CMF/MFI period or level, SMA window, resample factor, ROI rung, stop distance, frame, fill, venue, or book is a different, unpinned rule. A reviewer must not pick among these to rescue or reshape the record.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: dual-CCI170/34 / six-leg entry / five-leg signal exit / 10%-TP / 2%-SL / next-open fills / `1m` BTCUSDT spot are frozen.

- F1 — Second-CCI relevance: a CCI170-only twin (entry drops the `cci34<-100` leg, exit drops `cci34>+100` — same grid, fills, book, TP/SL) must not improve net expectancy; fail ⇒ the 34-bar leg adds nothing over the slow oscillator alone.
- F2 — Flow-gate relevance: a no-flow twin (entry drops CMF/MFI legs, exit drops the CMF leg — same grid, fills, book, TP/SL) must not improve net expectancy; fail ⇒ the money-flow conjunction adds nothing over the dual-CCI-plus-stack rule alone.
- F3 — Stack relevance: a no-stack twin (entry drops both 5m-SMA legs, exit drops the SMA-stack legs — same grid, fills, book, TP/SL) must not improve net expectancy; fail ⇒ the 5m regime permission adds nothing over the 1m oscillators alone.

Event-level Qlib/Hummingbot parity of the strategy/execution path is required before mass screening if that path introduces a new unverified capability; do not interpret HB_READY as parity or profitability.

## Crypto portability

This derivative is **BTC-USDT Binance spot 1m** only — a researcher frame/venue pin on a venue-free file, no port claimed. Stated plainly: the machine needs completed-bar 1m OHLCV plus the 1020-bar admission warmup (200 completed 5m windows for the SMA200 seed plus margin); entries are six-leg dip conjunctions with a live-window rate of 9 per ~7 days; exits are the opposite-extreme conjunction plus file-literal 10% TP / 2% SL with next-open fills; 1m spreads and (non-)funding apply as stated (spot — no funding leg exists to model). The ported legs carry no session, calendar, or gap dependence, so 24/7 crypto continuous trading introduces no anchor or session-template port of any kind. No rescaling, no cross-asset claim is made. No frequency, profitability, or capacity claim is made. Seven-coin, 1h/4h/1d, BO/SO 6/6/6, and 3×/5× futures experiments are optional separate downstream campaigns, **not** admission requirements or silently authorized equivalent executions.

## Limitations

The spot-1m venue/frame pin, forward-hold causal discipline (replacing interpolation), next-open fills, fill+1 evaluation, SL > TP > signal ordering, exit-dominates discipline, 1020 warmup, invalid-bar halt pin, 0.01 BTC sizing, 0.0002 research fee, and all display-column drops are researcher pins, never attributed to the source. The developing-bin reads the source backtester may perform are fenced out, not modeled. The 10%/−2% backstops bind only at bar closes under the research-model convention — intrabar touch-then-recover paths are not modeled, disclosed. Same-side refires while LONG are no-ops and never average down by construction. The page ships GPLv3 (short-literal citation only, research-only use asserted, no commercial claim). No Qlib parity, historical Survivor, HB Certified, Paper/Testnet/Live or profitability claim.

## Implementation status

`not-implemented`: no dedicated controller, Qlib executable recipe or deployment artifact was created. PASS is a bounded research-expressibility proposal, not a claim of already runnable materialization. A selected strategy may later need the minimal strategy-specific implementation without a second admission flag.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review must independently inspect this exact PR head, remediate only primary-source-verifiable facts, then PASS exact-head merge or NOT_LOSSLESS close. Scout does not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- Primary implementation + pin: https://github.com/freqtrade/freqtrade-strategies/blob/f3340ce11f5bdf62f598522e64d1f5638eaa13f5/user_data/strategies/berlinguyinca/CCIStrategy.py (commit `f3340ce11f5bdf62f598522e64d1f5638eaa13f5`, 2026-09-08, still `main` HEAD verified live 2026-11-03; blob `b3f17834e1905d6037de54ffdc2341e1067a3d60`; 120 lines / 4,459 bytes; raw sha256 `c3b1f8b57850d12a1e1b4e1ec42e92b842b2384f439e177f9e711bd20d698aad` verified live 2026-11-03; file last touched `bcca7d7aef0df373c29b80532c8c02663f25ae3f` 2022-07-10 with byte-identical blob; repo GPLv3 — short-literal citation only)
- Exchange verification: Binance spot `api/v3/exchangeInfo` (`BTCUSDT`, `TRADING`, `tickSize 0.01`, min-qty 0.00001, min-notional 5) plus `api/v3/klines` 1m microstructure probes (9,999 completed bars ≈ 2026-10-27→2026-11-03, forming bar dropped by closeTime, 0 non-finite rows, first finite feature row index 1000, 9 entries / 8 exits ending LONG-held; tape digests CONST/RISE/SINE all-flat, CRASH-triangle 1 entry / 1 signal exit FLAT), fetched live 2026-11-03
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged pinned package/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
- Same-repo admitted siblings (different files/mechanisms, this file explicitly fenced out as unclaimed): `freqtrade-average-ema8-21-cross-volume-gated-long-flat-btcusdt-4h-2026-10-31.md`; `freqtrade-smoothscalp-7gate-stochf-ema-mfi-cci-long-flat-btcusdt-1m-2026-10-30.md`; `freqtrade-technical-cmf-sign-state-long-flat-btcusdt-5m-2026-10-22.md`; `freqtrade-strategy005-volume-surge-fisher-washout-long-flat-btcusdt-5m-2026-10-21.md`
- Nearest oscillator lineage (different source/construction/legs/frame/exits): `cci-threshold-extreme-reversal-two-sided-btcusdt-4h-2026-10-12.md`; open PR #304 `forven-cci-oversold-recross-long-flat-btcusdt-1h-2026-10-19.md`
