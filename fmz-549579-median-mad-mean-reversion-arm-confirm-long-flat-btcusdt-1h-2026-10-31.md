---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: "FMZ 549579 median/MAD robust mean-reversion two-phase arm-confirm long-flat BTC spot 1h independent derivative"
created: 2026-10-31
updated: 2026-10-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - fmz
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-16
sources:
  - https://www.fmz.com/strategy/549579
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FMZ 549579 median/MAD mean-reversion — independent long-flat derivative

## Provenance

- **Primary source:** public first-party FMZ page https://www.fmz.com/strategy/549579 — *Mean-Reversion Teaching Strategy (Median/MAD)* (Chinese title 中位数绝对偏差均值回归教学策略), `Created: 2026-09-16 11:33:42`, `Copy: 0`, `Hits: 173`. This cycle the page served **796,371 bytes** over HTTPS with HTTP 200 using a plain browser user-agent; the complete bilingual (Chinese/English) strategy description and the full FMZ JavaScript program are embedded verbatim in the served stream and were decoded end to end (strategy code ≈ 33 KB, 713 decoded lines from file header through `function main()` to the closing `Sleep(POLL_INTERVAL_MS)` loop). No login, no paywall, no bypass. Only rule tokens are normalized and cited here; no large source block is copied into this repository.
- **Source facts actually verified:** panel parameters `Lookback=120`, `ArmZ=2.5`, `EntryZ=2.0`, `OrderLots=1` contract, `Leverage=1`, `StopLossPercent=4` (parameter table present in both languages; `CheckParameters` enforces `Lookback>=20` integer, `0<EntryZ<ArmZ`, `OrderLots>=1` integer, `Leverage>=1` integer, `StopLossPercent>=0`). Teaching fixed values in code: `CONFIRM_BARS=2`, `MAX_ARM_BARS=20`, `ENTRY_ANCHOR_DRIFT_MAD=0.5`, `EXIT_ANCHOR_DRIFT_MAD=1.0`, `EXIT_REMAINING_RATIO=0.25`, `MAX_HOLD_BARS=30`, `FEE_PER_SIDE_PCT=0.05`, `SLIPPAGE_PER_SIDE_PCT=0.05`, `COST_COVERAGE_MULTIPLE=3`, `COOLDOWN_BARS=3`, `MIN_SCALE=1e-10`. Statistics use only **completed** bars (`signalIndex = records.length - 2`, forming bar excluded); the main loop requires `records.length >= Lookback + 2`. The page honestly states the code passed `node --check` plus offline logic tests, and that **no FMZ backtest, paper run, or live micro-run has been performed** — so no performance claim ships anywhere.
- **Full-logic census this run:** 5 phases (`idle` / `armed_long` / `armed_short` / `long` / `short`); arm on `z<=-ArmZ` (long) / `z>=ArmZ` (short); armed-bar cap 20, entry drift gate 0.5 MAD, extreme tracking, strict `|z|` contraction counting with `1e-9` epsilon, side check, `|z|<=EntryZ` + `confirmCount>=2` entry; open-time target-cross and 3× cost-room vetoes; holding exits in fixed order (frozen-target reclaim or 25%-remaining → re-breach of arm extreme → 1.0-MAD drift → 30-bar timeout); realtime 4% emergency stop from entry average; single-position guard (`throw` on multiple positions, refuse repeat opens); 3-bar post-close cooldown; state persistence via `_G` (research equivalent: in-memory state). Display-only machinery (`Chart`, `LogStatus`, `DrawTradeMarker`, status table) never gates a trade.
- **Independent researcher-defined executable derivative (NOT source-native):** source is a two-sided single-symbol **futures swap** system (`CONTRACT_CODE="swap"`, contracts in lots, leverage, funding-uncapped). This record pins **Binance BTC-USDT spot 1h LONG/FLAT only**; the entire short arm/entry/holding leg is disabled, never evaluated. Contracts/lots become fixed `Q=Decimal("0.001")` BTC; leverage/funding/margin legs are absent (spot has none — this does **not** claim futures funding is zero). Fills are next-completed-bar-close historical MARKET fills; the source's realtime intrabar emergency stop is adapted to completed-bar-close evaluation with pinned **stop-first** priority (same conversion class as merged Alpha FMZ records #590/482829); market-order fill-wait becomes the idealized fill rule below. Cash 10,000 USDT, hypothetical 0.1% fee per side. Warmup 120 completed 1h bars (first signal bar `t=120`: 120 priors + signal close; mirrors the source's `Lookback+2` record rule). These researcher choices change trade events and economics.
- **Frozen identity:** `FMZ:549579|median-MAD|Lookback120|ArmZ2.5|EntryZ2.0|confirm2of|armcap20|drift0.5-in/1.0-out|remain0.25|maxhold30|costroom0.6pct|stop4pct-stopfirst|long-only|BinanceSpot-BTC-USDT-UTC1h|next-completed-close-MARKET|Q0.001BTC|cash10000USDT|fee0.001-side|warmup120|Decimal-ledger|cooldown3`. Any signal, timing, cost, or position change creates a different derivative.

## Economic mechanism

### Source-reported

Prices oscillate around a slow-moving statistical regime better described by robust estimators (median, MAD) than by mean/standard deviation, which single extreme bars distort. The system therefore (1) arms only on a ≥2.5-robust-scale log deviation, (2) demands visible contraction (two consecutive strictly shrinking `|z|` prints back inside 2.0) before fading the move, (3) freezes the regime center at entry so a drifting center cannot fake a completed reversion, and (4) admits defeat on re-widening beyond the armed extreme, 1.0-scale drift, 30-bar timeout, or a 4% adverse excursion. A 3× estimated-round-trip cost room veto skips trades whose target cannot pay costs. The page's own risk note states the model identifies deviation only, cannot judge intrinsic value, and cannot guarantee reversion.

### Research interpretation

A robust-scale snap-back fade with a two-phase trigger (extremity-then-contraction) rather than a single-threshold fade: the armed phase refuses both V-shaped instant reversals that never printed extremity persistence and slow bleeds that keep widening. Unlike mean/σ z-score records, every location/scale input here is median-based, so one spike bar moves neither the center nor the scale — the trigger is deliberately insensitive to the very bars that fool moment-based bands. The frozen-center target plus the remaining-ratio (25%) exit banks partial reversion instead of demanding a full round trip. No performance, profitability, Qlib parity, or Survivor claim.

## Signal

Exact rules as pinned (any other lookback, threshold, count, price basis, frame, book, or leg combination is a different, unpinned rule):

```text
L[t]      = ln(C[t])                                            // natural log, exact Decimal transcendent pinned below
CENTER[t] = median(L[t-120 .. t-1])                             // 120 priors, completed bars only
MAD[t]    = median(|L[i] - CENTER[t]|, i in t-120..t-1)
SCALE[t]  = 1.4826 * MAD[t]                                     // null if non-finite or <= 1e-10
Z[t]      = (L[t] - CENTER[t]) / SCALE[t]                       // null when SCALE null
```

- **Median pin:** ascending numeric sort; even count 2k → mean of elements k-1 and k (0-indexed); so CENTER over 120 values = mean of 60th/61st sorted values; MAD likewise over 120 absolute deviations. Researcher arithmetic: extended-precision decimal log (at least 12 significant digits, ties impossible at gate boundaries in practice — equality with a bound never fires since all gates are strict except `|z|<=EntryZ`, `z<=-ArmZ` arming, and `C>=target`; exact-boundary prints are measure-zero and disclosed as boundary-tolerant).
- **States (single in-memory machine, initial IDLE, cooldown 0):**
  - **IDLE** at completed bar `t>=120`: if cooldown>0, cooldown-- and wait. Else if `Z[t]<=-2.5` → ARMED_LONG (store `armCenter=CENTER[t]`, `armScale=SCALE[t]`, `armExtreme=Z[t]`, `prevAbs=|Z[t]|`, `confirm=0`, `armBars=0`). Short-side arming is disabled in this derivative (never evaluated, not silently deleted from provenance).
  - **ARMED_LONG** at each later completed bar (in order): `armBars++`; if `armBars>20` → IDLE, no cooldown (observation timeout). Else if `|CENTER[t]-armCenter|/armScale>0.5` → IDLE, no cooldown (reference invalidated). Else update `armExtreme=min(armExtreme,Z[t])`; if `|Z[t]|<prevAbs-1e-9` then `confirm++` else `confirm=0`; `prevAbs=|Z[t]|`. If `Z[t]>=0` → IDLE, no cooldown (crossed center). Else if `|Z[t]|<=2.0` AND `confirm>=2` → attempt open: require `C[t]<centerPrice[t]` (else IDLE, opportunity gone) AND `|target-C[t]|/C[t]*100>=0.6` (else IDLE, cannot cover 3× the 0.2% estimated round trip); on pass, queue exactly one fixed `Q=Decimal("0.001")` BTC MARKET BUY for next completed bar `f=t+1`.
  - **Fill:** at `E[f]`, use actual finite `C[f]`; require `cash>=Q*C[f]*(1+fee)` in exact Decimal or consume the signal and return to IDLE with cooldown 3 (source consumes the counter on the signal bar alike). On fill set LONG, `P=C[f]`, `entryDist=|ln(P)-ln(target)|` with `target=centerPrice[t]`, `entryScale=SCALE[t]`, freeze `armExtreme`; `holdBars=0`. No evaluation on the fill bar.
  - **LONG exits** (each `t>f`, fixed priority, at most one exit per bar; exit queues SELL for next completed bar at its real close, full Q, then IDLE + cooldown 3): (1) **stop:** `(C[t]-P)/P<=-0.04` fee-exclusive, checked first; (2) **reversion:** `C[t]>=target` OR (`entryDist>0` AND `|ln(C[t])-ln(target)|<=0.25*entryDist`); (3) **re-widening:** `Z[t]<=armExtreme` (recomputed with live CENTER/SCALE each bar, exactly as the source recomputes stats per bar); (4) **drift:** `|CENTER[t]-ln(target)|/entryScale>1.0`; (5) **timeout:** `holdBars>=30` (incremented per evaluated bar). No exit executes if its fill bar is absent; pending stays unfilled at sample end.
- **Liveness proof:** `|z|<=2.0` contains 0 strictly inside, and two consecutive contractions occur on any rounded bottoming path; the rule can fire. The `C[t]<target` + 0.6%-room vetoes only refuse already-completed or cost-uncovered setups.
- **Exact strictness:** arming `<=`, confirmation `<=`, target `>=`, stop `<=`, drift/timeout `>`/`>=`, contraction `<prevAbs-1e-9` — preserved verbatim, never smoothed.
- **Warmup:** bars 0–119 update indicators but never arm, queue, or fill. First decision at index 120 (120 priors + signal close). `Z` null bars (degenerate MAD) fire nothing and advance no state except cooldown countdown in IDLE.
- **State exclusions:** at most one pending action and one position; pending takes precedence; fill bars evaluate nothing. No pyramiding, DCA/safety orders, partials, trailing, shorts, leverage, margin, multi-asset legs, session filters, intrabar orders, or end-of-sample forced liquidation. An open LONG at sample end is marked at the last actual valid close, never synthetically closed.
- **Exact Decimal ledger (position truth):** `Decimal(str(C))` closes, exact Q. BUY debits `Q*P*(1+fee)`; SELL credits `Q*P*(1-fee)`. FLAT iff ledger BTC `==Decimal("0")`. Simulator outputs are cross-checked only (`|sim_quote-Q*P|>max(1e-8,1e-12*Q*P)` or side/amount mismatch → abort as ENGINE_MISMATCH). Float dust, auto-netting, and missing-price fallbacks are never read for state.

## Required data

Only actual Binance BTC-USDT spot UTC 1h O/H/L/C/V (volume validated, never gated — the source reads none). Decisions at `E[t]=T[t]+3600s` on completed bar `t`; fills use the next completed bar's actual close, never retroactively. Validation: strictly increasing gap-free 3600s UTC opens; finite positive O/H/L/C; `H>=max(O,C)`, `L<=min(O,C)`; finite `V>=0`; no duplicates. **Abort the research run** on any missing/invalid/duplicate/discontinuous candle; never forward-fill, interpolate, fabricate, or skip.

## Execution assumptions

- **Pinned contract:** Hummingbot package **`20260920`**, `hummingbot/VERSION = dev-2.17.0`, bounded source commit **`HCH725/hummingbot@8b0e067e80ab62f10846d518dcb5a8218527ddb3`**. Verified this run at that commit: `constants.py` 993 bytes with `INTERVALS` mapping **`1h`** (with `1m`/`4h`/`1d`); `binance_spot_candles.py` 3,924 bytes; `order_executor_simulator.py` 3,913 bytes (MARKET branch fills first row at real `close`, `filled_amount_quote=float(amount)*close`, `cum_fees_quote=trade_cost*filled_amount_quote`, `CloseType.POSITION_HOLD`); `backtesting_data_provider.py` 8,823 bytes (`get_price_by_type` missing-price `Decimal("1")` fallback re-verified and **forbidden** here — actual closes required); `backtesting_engine_base.py:269` `simulate_execution`, `:284` controller `determine_executor_actions()`. Sizes identical to prior independently reviewed FMZ Alpha records; no wheel rehash this cycle.
- **Controller/executor:** a **future dedicated controller is not implemented**; it must implement the IDLE/ARMED/LONG machine above and emit `OrderExecutorConfig(connector_name="binance", trading_pair="BTC-USDT", side=BUY/SELL, amount=Decimal("0.001"), position_action=OPEN/CLOSE, execution_strategy=MARKET, price=None, leverage=1)` on the designated fill row only. No deployed controller or exchange-accepted order is claimed.
- **Fill convention:** idealized historical next-completed-close MARKET fills reported at effective `E[fill]`; not a claim a live order achieves the completed close. No slippage model beyond the assumed 0.1%/side fee (not a verified Binance tier); the 0.6% cost-room gate is the source's own 3×(0.05%+0.05%)×2 estimate, kept verbatim — it covers the research fee and is **not** a verified cost model.
- **Economic limitations:** spot unleveraged BTC/USDT has no funding/liquidation leg; this does **not** assume perpetual funding is zero. Real fees, precision, liquidity, and market impact are unverified; any such failure aborts per the ledger rule.
- **Reused capability boundary:** single-pair Binance spot OHLCV → controller action → MARKET-close `OrderExecutorSimulator` → POSITION_HOLD, as reviewed in Alpha PRs **#414** and FMZ records **#590/482829**. New here are only controller-side median/MAD predicates and the arm/hold state machine — no new data/executor path. No Hummingbot/Qlib test in this Scout. A new execution primitive would need one representative Hummingbot↔Qlib event-level parity validation **before mass screening**, never as a profitability gate.

## Evidence

### Source-reported

First-party FMZ page 549579 (created 2026-09-16): Lookback 120 / ArmZ 2.5 / EntryZ 2.0 / 1 contract / 1× / 4% stop panel; CONFIRM 2 / arm-cap 20 / drift 0.5-in-1.0-out / 25% remaining / 30-bar hold / 3× cost room / 3-bar cooldown fixed values; `node --check` + offline state-transition tests; **no backtest, paper, or live run performed**. No Sharpe/win-rate/return figure ships on the page (scanned this cycle — none present).

### Independently reproduced

**None** for this candidate's trades, Hummingbot/Qlib events, performance, OOS, or realized fees. Only the page bytes, decoded program logic, and pinned-engine paths above were inspected; prior PR engine proof is referenced with limitations.

### Negative evidence

Pre-write dedup 2026-10-31 against `main@9ca1fbfb` (**465** root-level strategy records, README counter **465**): filename/content search for `549579`, `MAD`, `median`, `armExtreme`, `CONFIRM_BARS`, `targetCenter` returns **zero same-source records** — no pool record sources this FMZ page or its median/MAD two-phase rule. The 12 open `research/*` PRs (#48, #49, #63, #89, #92, #251, #304, #331, #350, #353, #593, #646) were inspected by source/title/branch — none uses this URL or rule. Nearest pool neighbors use different constructions: `fmz-482829-zscore-anomaly-reversal` (mean/σ z-score spike fade on ETH 2h — moment-based, single-phase, no arming/drift/frozen-target machinery); `fmz-486567-log-price-zscore-dynamic-stop` (log z-score with dynamic stop, 1d); `fmz-482890-quantile-band-trigger-confirm` (quantile bands, 1h); `fmz-483087-triple-bollinger-simultaneous-breach` (triple-BB breach, 1h); freqtrade `CombinedBinHAndCluc` (BB-penetration dip, 5m). None trades a median/MAD robust-scale extremity-arm plus strict-contraction-confirm entry with a frozen-center/drift/timeout exit stack. Not a duplicate, paraphrase, or trivial parameter variant.

## Falsification plan

Future authorized research only (no backtest, trading, deployment, or cron change here): even-count median averaging check; MAD-degenerate (`<=1e-10`) no-fire bars; warmup 119/120 boundary; arm on `z=-2.5` exact; no-arm at `z=-2.49`; contraction reset on flat `|z|` (1e-9 epsilon); confirm-1 vs confirm-2 boundary; center-cross disarm; 20/21 arm-bar timeout; 0.5 drift disarm; cost-room 0.6% veto; signal-vs-fill bar separation; stop-vs-target priority ties; 25%-remaining boundary with `entryDist>0` guard; re-widening at `armExtreme` equality; 1.0 drift close; 29/30 hold-bar timeout; 3-bar cooldown gating; insufficient-cash consume; last-bar pending; fee ledger; `Decimal(str())` reconciliation; ENGINE_MISMATCH abort path.

## Crypto portability

Binance BTC-USDT spot, 1h, unleveraged long-flat. The long-only book expresses unchanged on a spot venue with no borrowing, leverage, or funding leg. The disabled short leg is a deliberate TOS/venue adaptation, not a claim about short-side economics. Real venue precision (tick/lot/min-notional), fees, and liquidity must still abort-or-verify per the ledger rule before any execution use.

## Limitations

- Idealized next-completed-bar-close MARKET fills; no claim a live order achieves the completed close; no slippage model beyond the assumed 0.1%/side fee.
- The source's realtime intrabar 4% emergency stop is evaluated on completed-bar closes with stop-first priority; intrabar excursions beyond 4% that recover by the close are not modeled — disclosed adaptation.
- Short-side machinery is disabled, not modeled; the record says nothing about short profitability or futures funding.
- Exact-boundary prints (`z` exactly ±2.5/±2.0, `C` exactly on target) are boundary-tolerant by construction; bit-identity with any particular JS `Math.log`/sort build is not claimed.
- The 120-bar warmup is the source's `Lookback+2` record rule restated for completed bars, not a fitted choice.
- PASS here means pinned-engine expressibility of this fully specified derivative, not profitability, Qlib parity, Survivor status, source-native equivalence, or any live/Paper/Testnet authorization.

## Implementation status

`implementation_status: not-implemented`. No controller, executor config, backtest, Qlib recipe, or deployment artifact is created here. If this candidate is formally selected for execution without a reproducible executable recipe, the engineering route is `IMPLEMENTATION_NEEDED` (minimal strategy-specific implementation, then the same 01–05), never a second admission flag.

## Adoption boundary

`status: research-only`, `adoption: not-approved`, `approval_scope: research-only`. `hb_ready_status: PASS` is a **Scout six-gate proposal awaiting independent Hermes Auditor review**, not independent approval, Qlib parity, Survivor, Hummingbot Certified, profitability, or Paper/Testnet/Live authorization. The Auditor alone may source-fact remediate the exact head, merge on verified PASS, or close NOT_LOSSLESS. The existing signed GitHub webhook receiver alone performs post-merge README bookkeeping; Scout does not touch main/README or any workflow.

## Related Wiki records

None. This Scout cycle writes no Wiki Brain records.
