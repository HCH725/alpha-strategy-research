---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Forven Gap-Fill 1% gap-down open-vs-prev-close long-flat BTCUSDT 1h derivative
created: 2026-10-25
updated: 2026-10-25
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-24
sources:
  - https://github.com/judder659/Forven/blob/14397ae45d2d88fe78b8a2bec6e4b638daed845d/forven/strategies/builtin/gap_fill.py
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forven Gap-Fill 1% gap-down — independent BTC-USDT spot 1h long-flat derivative

## Provenance

**Primary public GitHub source (read end to end via raw fetch at the pinned commit this run):** repository https://github.com/judder659/Forven (open-source crypto backtesting project; each `forven/strategies/builtin/*.py` file is one executable strategy class emitting `Signal(entry_signal, exit_signal, price, direction, confidence, indicators)`). Immutable pin: commit `14397ae45d2d88fe78b8a2bec6e4b638daed845d` (committed `2026-10-24T21:21:05Z`; verified as repository HEAD via `git ls-remote` during this cycle), path `forven/strategies/builtin/gap_fill.py`, class `GapFillStrategy`, roster entry `("PREBUILT-GAP-FILL", GapFillStrategy, {"_asset": "BTC"})`. The 3192-byte raw download at the pinned commit reproduces blob SHA `1348cea1dbd3bbdd36c2c917632c350619ee3570` under `git hash-object` (byte-identity verified this run; SHA-256 `260020132a5b3db6d41a2e5cf99f81170faea0a749332710849c390ae4fa4114`).

**Facts directly read from the pinned file (long side only; no short path exists):** `default_params = {"gap_pct": 1.0, "leverage": 1.0}`; `parameter_space = {"gap_pct": (0.5, 3.0, 0.5)}` (a documented search surface only — this record pins the default `1.0` and runs no search); `compatible_regimes = {"RANGE_BOUND"}` (metadata never read by `generate_signal`, disclosed as non-gating, same family pattern as the admitted Chaikin-MF record's `TREND_UP` label). Signal rule verbatim: `gap = (curr_open - prev_close) / prev_close` with `curr_open = open[-1]`, `prev_close = close[-2]`, `curr_close = close[-1]`; entry fires only inside `if gap < 0 and gap_abs >= min_gap_pct` (i.e. open at least 1% under the previous close); on such bars `exit_ = curr_close >= prev_close` (the exit leg lives *inside* the gap-down branch — non-gap bars print no signal at all, and every exit bar is simultaneously an entry bar). Guards: `len(df) < 3` and `prev_close == 0` both return no-signal. `price=round(curr_close, 4)` — the decision bar's own close. `confidence = min(gap_abs / min_gap_pct * 0.5, 1.0)` on entry bars (diagnostic only, conditions no order line). Token census over the file this run: 0 `enter_short` / 0 `exit_short` / 0 `short` direction (long-only is coded, never an omission); 0 coded `stoploss` / `trailing` / `take_profit` / `time_exit` / `funding` / `volume` legs — the line-87 comment phrase "or stop loss" is uncoded prose with no implementation anywhere in the file, fenced here, never treated as a risk leg. The signal path reads `open` and `close` only.

**Explicit independent derivative, NOT source-native/lossless:** this record pins the source-default 1% gap formula, strict inequalities, gap-branch exit asymmetry, guards, and long-only posture, but predeclares exactly five researcher choices: (1) market/timeframe pin BTC-USDT Binance spot `1h` (the file names no venue or timeframe; the roster default `_asset BTC` is carried, venue/frame are researcher pins); (2) completed-bar decisions with modeled same-row MARKET close fills (the source `Signal.price` is the decision bar's own close; Forven live fill behavior is scoped out, never claimed); (3) a no-op tie-break on FLAT-collision bars — when a gap-down bar prints both entry and same-bar recovery while flat, this record fills nothing (the source code specifies no collision handling; entering-then-exiting at one close would pay two fees for zero gross, so the no-op reading is pinned and disclosed — a different tie treatment is a different research identity); (4) a 30-completed-bar warmup, flat by record rule (structural minimum is the 3rd bar per the `len<3` guard; 30 is margin, disclosed); (5) fixed 0.001 BTC sizing on 10,000 USDT cash with a 0.1% per-side *assumed research* fee. This is a new fully specified derivative, **not** a claim about the Forven engine's own backtest behavior.

**Immutable derivative identity:** `GH:judder659/Forven@14397ae:gap_fill.py | derived-v1-gap1pct-open-vs-prevclose-exit-inside-branch-flat-collision-noop | BinanceSpot:BTC-USDT:1h:LONG-FLAT:0.001BTC:close-MARKET | 2026-10-25`. Any change to threshold, formula, tie-break, warmup, fee, fill, sizing, or market creates a different research identity.

## Economic mechanism

### Source-reported

The file's own docstring: detect gaps between previous close and current open; enter on a gap exceeding the threshold, betting on a partial or full fill back toward the previous close. No behavioural channel, no performance number, and no market-selection claim appear in the file.

### Research interpretation

Gap-fill reversal, long-only, state-holding. A ≥1% overnight-style dislocation (open printed ≥1% below the prior close) is treated as transient liquidity dislocation; the unit bets on reversion toward the prior close and surrenders only when a *fresh* gap-down bar recovers to its own prior close within the bar — positions are otherwise held through all non-gap bars indefinitely. Entry is easy (every qualifying gap-down), exit is strict (gap-down *plus* same-bar recovery), so holding time is unbounded and driven entirely by the arrival of a recovering gap bar. No return, Sharpe, win rate, or survivor status is asserted.

## Signal

**Input and clock:** exactly one Binance **spot** BTC-USDT UTC **1h** candle stream, `(open_time,O,H,L,C,V)`, strictly contiguous 3600-second opening timestamps. `open_time` is the exchange candle-open Unix timestamp; a completed candle becomes available only at `open_time+3600`. Compute and act only after that completion. Require finite positive O/H/L/C, H >= max(O,C), L <= min(O,C), finite nonnegative V, and valid strictly increasing timestamps. No forward fill, synthetic open/close, higher-timeframe peeking, or missing-price substitution.

**Researcher-pinned rule mathematics (source-default threshold, source-strict inequalities):**

1. For bar `t>=1` with `C[t-1]>0`: `gap[t]=(O[t]-C[t-1])/C[t-1]`. `gapBar[t] = gap[t]<0 && |gap[t]|>=0.01`. `recov[t] = gapBar[t] && C[t]>=C[t-1]`. For `t<1`, or `C[t-1]==0`, or any non-finite input: no signal (source guards, coded).
2. Maintain `position in {FLAT,LONG}`; initialize `FLAT`. After **30 contiguous valid fully completed bars**, on each bar `t` apply **exactly once**:
   - If `LONG`: if `recov[t]`, model one full `SELL` of 0.001 BTC, set `FLAT`; otherwise HOLD. Entry bars while LONG are ignored. Never exit and re-enter on the same bar.
   - If `FLAT`: if `gapBar[t] && !recov[t]`, place one `BUY` of 0.001 BTC **only if affordable**, set `LONG`. If `gapBar[t] && recov[t]` (collision), fill **nothing** — the pinned researcher no-op tie-break. Otherwise remain FLAT. Exits while FLAT are deterministic no-ops.
3. Re-entry re-arms on the next qualifying gap-down bar after any exit (no cooldown specified — explicitly none, not invented).
4. **Explicitly disabled:** any short leg; stop-loss / take-profit / trailing / time-limit legs (the file's "or stop loss" comment is uncoded prose, never a leg); ROI targets; pyramiding; BO/SO/DCA; averaging; compounding; concurrent positions; cross-pair capital sharing; maker/limit/next-open/intrabar execution; discretionary exits; the `parameter_space` search surface (defaults pinned, no search run); the `RANGE_BOUND` label as a gate; the `confidence` formula as an order condition; or any hidden Hummingbot default risk order. No stop is a deliberate research risk.
5. **Invalid/missing candles:** stop the run as **data-incomplete** if any candle is missing, duplicated, malformed, out-of-order, non-finite, non-contiguous (open_time step != 3600), or any required print is undefined after warmup. This guard is load-bearing here: a data outage spanned by `O[t]` vs `C[t-1]` would fabricate a gap, so continuity is verified pre-engine and never bridged. Do not fabricate a fill, silently drop a row, reset position state mid-run, or sell an existing LONG at an invented price. A restarted independent run must establish 30 new contiguous valid completed bars and a fresh FLAT state.

## Required data

One real Binance BTC-USDT **spot** 1h OHLCV feed and its UTC opening timestamps. The rule reads `O[t]`, `C[t]`, `C[t-1]` only; H/L are validity-checked, V is validity-checked but never signal-forming. No order book, ML model, funding, mark/index price, cross-asset input (no BTC-dominance, F&G, DXY, VIX, liquidation, or futures-funding read exists in the file), multi-timeframe alignment, session template, or future print. The source's pair-agnostic prose is **not** claimed to have been reproduced; this 1h BTC-USDT variant is explicitly independent.

## Execution assumptions — actual pinned Hummingbot model

**Pinned research engine:** Hummingbot policy package **20260920** (label only — see disclosure below), VERSION **dev-2.17.0**, source `HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`. Previously merged [Alpha PR #414](https://github.com/HCH725/alpha-strategy-research/pull/414) records a 902/902 wheel/source Python-file match and wheel SHA256 `ea5a929c52095bc03fd34f5b3fb2fbfef068f7ea880af6c38290d1ddb729a148`; this Scout did **not** rehash the installed wheel. In this cycle the following real source paths were directly read at the pinned commit via `git show 8b0e067:...` against the local checkout (commit verified present by `git cat-file`, confirmed ancestor of the working tree), not inferred from a feature list:

- **Feed/data:** `hummingbot/data_feed/candles_feed/binance_spot_candles/constants.py` explicitly maps `1h` in `INTERVALS`; `binance_spot_candles.py::_parse_rest_candles` maps Binance open timestamp `row[0]` and OHLCV `row[1..5]`. `hummingbot/strategy_v2/backtesting/backtesting_engine_base.py::prepare_market_data` exposes `open/high/low/close/volume` from `*_bt` columns with a `dropna`; its `dropna` is **not** proof of data continuity — the derivative requires the pre-engine contiguity check above so outage-spanning fake gaps cannot hide.
- **Controller/executor:** the pinned `BacktestingEngineBase.simulate_execution` iterates processed rows, invokes `update_state(row)` then `controller.determine_executor_actions()` and routes `CreateExecutorAction` to `OrderExecutorSimulator`. The pinned `OrderExecutorConfig` supports `connector_name="binance"`, `trading_pair="BTC-USDT"`, `side=BUY/SELL`, `amount=Decimal("0.001")`, `execution_strategy=MARKET`, `price=None`, `leverage=1`. A dedicated strategy controller/recipe is **not yet implemented**.
- **Real fill and clock semantics:** `hummingbot/strategy_v2/backtesting/executors_simulator/order_executor_simulator.py` MARKET execution fills at the **first supplied row**, uses that row's `close` as `entry_price`, records `filled_amount_quote=amount*close` and `cum_fees_quote=trade_cost*filled_amount_quote`, and returns `CloseType.POSITION_HOLD`. The engine's raw timestamp is the candle **opening label**; the economic decision and modeled fill effective time are **opening label + 3600 seconds**. This is the simulator's same-close convention, **not** a claim of executable live post-close market fills. Do not relabel a limit fill as same-close MARKET or fabricate missing prices.
- **Position and costs:** `BacktestPositionHold` (defined in `backtesting_engine_base.py`) nets opposite-side base quantities and realizes **gross** quote PnL; executor fees are accumulated separately. Use `Q=0.001 BTC`, starting unborrowed cash `10000 USDT`, no other positions, and an **assumed research fee** `trade_cost=0.001` of filled quote on **each** buy/sell. A BUY is affordable only if `cash >= Q*C[t]*(1+0.001)`. On BUY debit `Q*C[t]*(1+0.001)`; on SELL credit `Q*C[t]*(1-0.001)`. `net_roundtrip_pnl = Q*(sell_close-buy_close)-0.001*Q*(buy_close+sell_close)`. While LONG, mark cash plus `Q*last_valid_close` without inventing a hypothetical sell; an open position is **not** automatically liquidated at the end. Spot funding is **not applicable**, not a zero-perpetual-funding assumption.
- **Package/commit binding disclosure (Gate-5 #411/#424):** `setup.py` at the pinned commit assigns version `20260729`, not `20260920`; `hummingbot/VERSION` at the pin reads `dev-2.17.0`. No package-to-commit mapping is invented here — `20260920` is retained as the policy package **label only**, and Gate 5 is bounded to the pinned commit's research-simulation semantics re-verified above, reusing the previously reviewed MARKET same-close primitive (#441/#442 lane) with no novel execution primitive (no stop/limit/trailing/next-open/intrabar leg is introduced). Sibling PASS records are execution-path evidence only, never proof of this candidate.
- **Boundaries:** simulator MARKET fills are full-quantity, single-close synthetic fills. Real exchange fee tiers, spreads, latency, slippage, depth, partial fills, lot/tick minimums and production precision are **not verified**. No CEX slippage path is inferred (the pinned OrderExecutorConfig comments mark `slippage_pct` Gateway-swaps-only). No live cost/fill guarantee or HB Certified status is claimed. The bounded spot 1h controller/executor/candle/position path reuses previously reviewed primitives, not a claim that this particular strategy has been backtested.

## Evidence

### Source-reported

The pinned 3192-byte file ships the complete construction: the `(open[-1]-close[-2])/close[-2]` gap formula, the 1% default threshold with its `(0.5, 3.0, 0.5)` search surface, entry strictly inside the gap-down branch, the exit leg (`close[-1] >= close[-2]`) strictly inside the same branch, the long-only posture (zero short tokens), the `len<3` / `prev_close==0` guards, the decision-bar-close `price`, the diagnostic `confidence`/indicators, and the `PREBUILT-GAP-FILL` BTC roster entry. It ships no timeframe, no venue, no sizing, no capital, no fee, and no coded stop leg. No source performance table, trade count, or date range exists anywhere in the file.

### Independently reproduced

**None.** No strategy backtest, event-level Qlib/Hummingbot parity, Pine/code execution comparison, live order, testnet/paper trade, wheel rehash, deployment or profitability experiment occurred. Pinned engine source inspection demonstrates a bounded model path, not completed executable implementation. The only executable artifact this run is a researcher self-check of the gap recurrence plus the derived FLAT/LONG machine on a 7-bar synthetic series (entry bar, hold bar, exit bar, FLAT-collision bar, idle bars), run in scratch (never committed): `SELF-CHECK OK: [('BUY', 2, 98.5), ('SELL', 4, 99.5)]` — logic verification only, not a backtest, not parity.

### Negative evidence and deduplication

At the pre-write snapshot `main@11a65f7`, the root Git tree contained **328** strategy Markdown records. Exact-identity working-tree searches for `GapFillStrategy`, `PREBUILT-GAP-FILL`, `gap_fill.py`, and `Gap Fill (` return **zero** records using this source file, class, or roster name. Content searches for `gap down`, `gap_down`, and `gap_pct` return zero signal rules (the only `prev_close` hits in the tree are other Forven siblings' diagnostic true-range prose such as `|high - prev_close|` inside ATR-helper documentation — no order line reads a gap). Ten open `research/*` PRs (#48, #49, #63, #89, #92, #251, #304, #331, #350, #353) were inspected for source overlap; none uses this file or an open-vs-prev-close gap mechanism (the nearest exit-philosophy cousin, #304 Forven CCI, is an oscillator recross — different construction). No open, merged, or closed PR touches gap-fill. Pool cousins are fenced as different mechanisms: `turnaround-tuesday-*` is a calendar/weekday effect (no price-gap read); Donchian/ORB/breakout records trigger on range extremes (no open-vs-prior-close dislocation); mean-reversion records (zscore/BB/RSI families) trigger on indicator levels (no gap formula). This is a materially different signal construction, not a trivial parameter variant.

## Falsification plan

After independent admission and separate downstream selection only: compare the frozen 1%-gap rule against (a) a threshold-off baseline (any gap-down bar, same exits) and (b) a no-tie-break baseline (FLAT-collision bars enter-then-exit at one close, same fees) on identical contiguous BTC-USDT 1h data with the same declared costs; check gap-event rate, same-bar-recovery rate, and sensitivity to the 30-bar warmup. Event-level Qlib/Hummingbot parity of the strategy/execution path is required before mass screening if that path introduces a new unverified capability; do not interpret HB_READY as parity or profitability.

## Crypto portability

This derivative is **BTC-USDT Binance spot 1h** only. Stated plainly: on a continuous 24/7 spot book, `O[t]` vs `C[t-1]` differ only by inter-trade tick moves — session-style gaps do not exist, so qualifying ≥1% hourly gaps are rare violent-move artifacts, and the expected signal rate is very low. No frequency, profitability, or capacity claim is made; rarity is an economic observation, never an admission fact. Seven-coin, 1h/4h/1d, BO/SO 6/6/6, and 3×/5× futures experiments are optional separate downstream campaigns, **not** admission requirements or silently authorized equivalent executions.

## Limitations

The 1h frame, venue, sizing, costs, warmup, same-close MARKET fills, and the FLAT-collision no-op are researcher pins, never attributed to the source. Forven's own same-bar collision handling was not verified and is scoped out — the no-op is the derived record's rule, and a different tie treatment would be a different identity. The uncoded "or stop loss" comment is prose, not a leg: adverse moves are held through with no cut. A LONG whose recovering gap bar never arrives is held indefinitely with no time exit. Pending-no-state: there is no pending state beyond the unit itself. Package/source binding cites an earlier independent review for the wheel hash rather than a fresh rehash. No Qlib parity, historical Survivor, HB Certified, Paper/Testnet/Live or profitability claim.

## Implementation status

`not-implemented`: no dedicated controller, Qlib executable recipe or deployment artifact was created. PASS is a bounded research-expressibility proposal, not a claim of already runnable materialization. A selected strategy may later need the minimal strategy-specific implementation without a second admission flag.

## Adoption boundary

`status: research-only`; `implementation_status: not-implemented`; `adoption: not-approved`; `approval_scope: research-only`. Independent Hermes Auditor GitHub Webhook Review must independently inspect this exact PR head, remediate only primary-source-verifiable facts, then PASS exact-head merge or NOT_LOSSLESS close. Scout does not approve, merge, close, trade, backtest or deploy.

## Related Wiki records

None asserted.

## Sources

- Forven primary (pinned): https://github.com/judder659/Forven/blob/14397ae45d2d88fe78b8a2bec6e4b638daed845d/forven/strategies/builtin/gap_fill.py
- Forven repository: https://github.com/judder659/Forven
- Pinned Hummingbot source: https://github.com/HCH725/hummingbot/tree/8b0e067e80ab62f10846d518dcb5a8218527ddb3
- Prior independently merged pinned package/source evidence: https://github.com/HCH725/alpha-strategy-research/pull/414
