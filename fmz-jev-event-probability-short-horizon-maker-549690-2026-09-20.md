---
schema: strategy-research-record-v1
title: "FMZ Jev Event-Probability Short-Horizon Post-Only Maker on Binance USDⓈ-M Perpetual (549690)"
created: 2026-09-20
updated: 2026-09-20
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - event-probability
  - market-making
  - adverse-selection
  - perpetual
  - fmz
status: research-only
confidence: low
source_as_of: 2026-09-20
sources:
  - "FMZ strategy page: 'Jev 币安U本位永续决策交易 (Version 3.0)' / 'Jev-Driven Short-Horizon Maker Strategy for Binance USDⓈ-M Futures V3', strategy id 549690, created 2026-09-18 15:37:13, page author ianzeng123. https://www.fmz.com/strategy/549690 (public description + default parameter table reviewed 2026-09-20; full source login-gated)"
  - "FMZ digest (companion narrative, identity-linked author neighborhood): 'No Explanations, Just Decisions: Plugging Jev into a Perpetual Strategy — Run It First, Talk Later', author 发明者量化-小小梦, reviewed as digest listing 2026-09-20. https://www.fmz.com/digest"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FMZ Jev Event-Probability Short-Horizon Post-Only Maker on Binance USDⓈ-M Perpetual (549690)

## Provenance

- **Source URL (strategy):** https://www.fmz.com/strategy/549690
- **Source type:** Public FMZ strategy page with Chinese operational narrative and explicit default parameter table; full JavaScript body login-gated.
- **Platform:** FMZ / 发明者量化
- **Source-reported title variants:** page title 「Jev 币安U本位永续决策交易 (Version 3.0)」; description banner 「Jev 驱动的币安 U 本位永续短周期 Maker 策略 V3」.
- **Page author (source-reported):** `ianzeng123`
- **Created (source-reported):** 2026-09-18 15:37:13; last-modified noted on page as within ~8 hours of review (2026-09-20) — **page version may move after this capture**.
- **Source reviewed as of:** 2026-09-20 (public description + parameter table + risk/verification sections; not full source)
- **External signal dependency:** source requires a filled `JevApiKey` before live/paper order paths; Jev is an **external event-probability service** whose model weights/calibration are **not published on the FMZ page** (`black-box signal component`).
- **Deduplication audit (2026-09-20; against `origin/main` `b91869f`):** `git grep` found **no** prior record citing FMZ id `549690` or a Jev-driven Binance perpetual maker family. Adjacent records are different:
  - `polymarket-btc15-adaptive-conditional-probability-terminal-distance-uncertainty-fmz-11020-2026-09-18.md` / FMZ 548121 — binary-market terminal probability on Polymarket, not exchange-perp maker execution.
  - `fmz-binance-okx-cross-exchange-spot-spread-hedging-549412-2026-09-19.md` — cross-venue spot spread hedge, not event-probability microstructure maker.
  - `fmz-online-bar-learning-update-speed-noise-negative-evidence-546440-2026-09-20.md` — online logistic bar learning shadow comparison, not external Jev + GTX lifecycle.
  - Conformal Kelly / fractional Kelly grid records — capital sizing families, not this signal/execution split.
  - FMZ APFF 548843 / meme rotation 548617 — multi-factor or cross-sectional rotation, different mechanism.

## Economic mechanism

### Source-reported

Source-reported problem framing: vendors/models often answer buy/sell/wait as one mixed decision. V3 **splits** model judgment from local account execution:

1. External **Jev** predicts which **mutually exclusive** future mid-price return bin will occur at **5 / 15 / 30 / 60 seconds** (five bins: large down, small down, narrow, small up, large up).
2. Jev separately evaluates **adverse-selection risk after a buy fill vs a sell fill**.
3. Jev estimates **passive fill probability** near best bid/ask.
4. **Local rules only** decide position state, max size, fee coverage, signal TTL, quote price, open/reduce/close actions.

Source-reported separation of failure modes: “model weak direction” vs “hard to fill” vs “quote cannot cover cost” vs “local risk forbids entry”.

Source-reported market-state inputs to Jev (not account state): order-book depth, Microprice, VAMP, book imbalance, near-term OFI, aggressive trade side, CVD, multi-window price changes and volatility. **Account balance, actual position, trading permissions, and prior model decisions are not fed to Jev** (source-reported anti-contamination design).

Source-reported path calibration: prediction bins are **not** fixed thresholds shared across symbols; program prefers recent **1-minute** candle vol, falls back to realtime sampled vol, and adjusts narrow band, large-move bounds, price-deviation tolerance, and requote distance. Large-move bounds also face a **trading-cost floor** so sub-fee wiggles are not treated as opportunities.

Source-reported validation stance on the page: JavaScript offline syntax check only; **no** FMZ backtest report, DryRun sample set, paper order log, or live micro-account ledger is provided as independently checkable evidence. Source risk banner states Jev probabilities are **not fully calibrated for the instrument**, are not deterministic win rates, and the V3 path **currently has no hard stop, no daily loss circuit breaker, and no liquidation-distance guard**; exits after hold-budget are **reduce-only maker** and not guaranteed to fill.

### Research interpretation

Normalized architecture (scout interpretation, not source claims of profitability):

```text
External model (Jev): market state → multi-horizon binned mid-return probs
                    + per-side adverse-selection score
                    + passive fill probability
Local rules:        threshold gates + cost coverage + size/TTL/data-quality
                    + GTX/Post-Only lifecycle + hold-budget reduce-only exit
Observability:      accuracy vs always-narrow baseline, Brier, calibration,
                    fill-prob vs realized fill, post-fill 1/5/30s path
```

Research interpretation:

1. **Mechanism hypothesis:** very short-horizon mid-price moves and passive-fill adverse selection are partially predictable from visible book/trade state; a pure maker who prices to expected adverse selection + costs can extract residual if the external probability is better than chance **and** calibratable.
2. **Signal half is black-box:** without public Jev weights/API schema, an independent researcher can reconstruct **local gates and lifecycle**, not the probability engine. This record therefore captures **operational research architecture + public defaults**, not a reproducible alpha signal.
3. **Execution half is reconstructable:** GTX-only, multi-gate conjunction, TTL, order-age requote, hold-budget reduce-only, cost-floor on large bins — these are falsifiable operational claims even if Jev is opaque.
4. **Boundary:** “model thinks X” is not fill quality; source itself designs observability for that gap. Incremental value vs in-repo records is **explicit model/execution split + adverse-selection tracking design**, not claimed PnL.

## Signal

### Formation timestamp

- Market sample: every `SAMPLE_MS = 1000` ms (1s) for book/trades/mid.
- Warm-up: source-reported continuous preheat **≥ 60 seconds** plus book-timestamp / last-trade / trade-batch quality checks before a new Jev request is allowed.
- Jev request: async; minimum spacing `LOOP_INTERVAL_MS = 5000` ms; main trading decision cycle stated as **30 seconds** (`SIGNAL_HORIZON_MS = 30000`).
- Prediction usable only while age ≤ `SIGNAL_TTL_MS = 10000` ms.
- Exchange clock/timezone alignment beyond FMZ timestamps is **underspecified** on the public page.

### Lookback

- Path/vol calibration uses recent **1-minute** closed bars when enough history exists; else realtime sampled vol (exact bar count for “enough” **underspecified**).
- Multi-horizon prediction spans 5/15/30/60s (source-reported); local trading loop primarily acts on the **30s** horizon gate.
- No fixed technical-indicator lookback such as RSI/MACD is claimed on the public page.

### Entry (new risk)

Candidate side = higher probability among **large-up vs large-down** bins. New position requires **all** source-reported gates:

1. Candidate-side large-move probability ≥ `OPEN_THRESHOLD = 0.55`.
2. Five-class distribution confidence ≥ `MIN_CONFIDENCE = 0.45`.
3. Same-side passive fill probability ≥ `MIN_FILL_PROB = 0.25`.
4. Prediction still within `SIGNAL_TTL_MS = 10000`.
5. Current price not clearly off prediction start (dynamic tolerance; numeric default **underspecified** beyond vol calibration narrative).
6. Predicted range covers maker fee + exit budget + `EDGE_BUFFER_BPS = 0.5`.
7. Post-order absolute net position ≤ `MaxPosition` (default 0.003 base units).
8. Order size/notional meets exchange contract rules (precision/min notional read at start; refuse start if missing).
9. Book/trade data not missing, stale beyond `MAX_DATA_AGE_MS = 3000`, or suspected dropped batches.

**Order type (source-reported):** GTX / Post-Only only — never cross the spread on entry.

**Quote placement (source-reported qualitative rule):** lower adverse risk or weaker fill chance → closer to best; higher adverse risk **and** still expected fill → retreat **one to two minimum price increments** on the more favorable side. Exact tick count selected by local logic; full formula in login-gated source (`underspecified` numerically).

### Reduce / opposite exposure

If candidate side opposes current net position, source prioritizes **reduce** over flip:

- Reduce gate uses direction probability ≥ `REDUCE_THRESHOLD = 0.40`.
- Reduce does **not** require open-level confidence or fill-prob gates.
- New opposite exposure only after prior net exposure is gone (source-reported).

### Exit

Source-reported protections and exits:

- Open signals expire at 10s TTL → cancel stale open-risk orders.
- Order alive `MAX_ORDER_AGE_MS = 30000` → cancel or requote.
- Price deviates beyond dynamic tolerance from prediction start → cancel.
- Book/trade quality fails → cancel non-reduce / new-risk orders.
- Remaining orders would breach max net → cancel.
- Hold budget expires → cancel unfinished opens; place **reduce-only maker** on the position side.
- Hold budget default: `HOLDING_BUDGET_MULTIPLE = 4` × 30s main horizon = **120 seconds**.
- Jev request failure → exponential backoff; cancel non-reduce orders.
- Unconfirmed cancel terminal state → stop sending new orders.
- Uncertain order outcome → lock new orders pending manual reconciliation.
- Requote only when direction, open/reduce flag, size, age, or price deviation meets replacement conditions (anti-churn queue-position narrative).

**Hard stop / daily loss / liquidation-distance guards:** source states V3 **does not currently provide** these (`not implemented in source`). Exit fill after 120s is **not guaranteed**.

### Holding period

- Expected / budgeted: **120 seconds** (4 × 30s), reduce-only maker after budget.
- Source does not claim positions always close at 120s.
- Overlapping positions: single symbol, **net** position model (no simultaneous long+short hedge stated).

### Parameters (source-reported public defaults)

| Parameter | Default | Role |
|-----------|---------|------|
| JevApiKey | (empty; required) | External Jev credentials |
| TradeSymbol | `BTC_USDT.swap` | Binance USDⓈ-M only (`BASE_QUOTE.swap`) |
| DryRunMode | `true` | Observation only until explicitly disabled |
| TradeAmount | `0.001` | Base size per open/reduce |
| MaxPosition | `0.003` | Max absolute net |
| Leverage | `1` | Allowed 1–125 on page |
| OPEN_THRESHOLD | `0.55` | New-position large-move prob |
| REDUCE_THRESHOLD | `0.40` | Reduce-opposite direction prob |
| MIN_CONFIDENCE | `0.45` | Open distribution confidence |
| MIN_FILL_PROB | `0.25` | Open passive fill prob |
| SIGNAL_HORIZON_MS | `30000` | Main horizon |
| SIGNAL_TTL_MS | `10000` | Signal freshness |
| HOLDING_BUDGET_MULTIPLE | `4` | Hold budget = 4× horizon |
| LOOP_INTERVAL_MS | `5000` | Min Jev request spacing |
| SAMPLE_MS | `1000` | Market sample period |
| MAX_ORDER_AGE_MS | `30000` | Order lifetime |
| MAX_DATA_AGE_MS | `3000` | Max book/trade age |
| MAKER_FEE | `0.0002` | Local fee constant (not auto-read from account tier) |
| EXIT_SLIPPAGE_BPS | `0.5` | Exit cost buffer |
| EDGE_BUFFER_BPS | `0.5` | Extra safety buffer on cost coverage |
| TAIL_TARGET_RATE | `0.30` | Dynamic large-bin calibration target (one tail) |

**Underspecified:** Jev model/API response schema; dynamic price-deviation tolerance numeric default; exact requote tick choice; commission tier auto-sync; independent performance series.

### Position sizing

Fixed base `TradeAmount` per action, capped by `MaxPosition`; leverage user-set (default 1). **Not** Kelly-scaled, **not** vol-scaled position size in the public parameter table. Cost coverage uses `MAKER_FEE + EXIT_SLIPPAGE_BPS + EDGE_BUFFER_BPS`.

### Specification completeness

- **Local execution defaults: high** (parameter table public).
- **External probability engine: low / not reconstructable** from this page.
- **Evidence of live/paper edge: none provided on page** beyond syntax check.

## Required data

- **Instrument:** single Binance U-margined perpetual (`BASE_QUOTE.swap`); default BTC_USDT.swap; source says **only** Binance USDⓈ-M supported.
- **Universe:** one configured symbol (not multi-asset rotation).
- **Venue:** FMZ-connected Binance USDⓈ-M futures API.
- **Market type:** perpetual futures; linear USDT.
- **Timeframe:** 1s market samples; 1m bars for path/vol calibration; multi-second prediction horizons 5/15/30/60s.
- **Fields (source-reported inputs to Jev):** book depth, Microprice, VAMP, imbalance, near OFI, aggressor side, CVD, multi-window price change/vol. Local also needs last trade, mid, position, open orders, contract tick/lot/min notional, equity only for local risk (not sent to Jev).
- **Point-in-time:** signals expire in 10s; data older than 3s blocks new-risk; warm-up ≥60s. No explicit train/test split — online inference only.
- **Timestamp:** FMZ/exchange timestamps; full clock discipline **underspecified**.
- **Missing-data:** source rejects start if price/qty precision unavailable; quality checks on book/trades; Jev failures → backoff + cancel non-reduce.
- **Funding/fee/spread:** local `MAKER_FEE=0.0002` is a **constant, not account-API truth**; funding not modeled in public defaults; spread implicit in post-only quote distance.

## Execution assumptions

Source-reported:

- Post-only GTX entry; reduce-only maker exit after hold budget.
- Re-read position+book immediately before send; recheck TTL/deviation/cost.
- Order protection loop (TTL, age, deviation, data quality, max net, hold budget, Jev failure, unconfirmed cancel).
- Prefer reduce over flip when signal opposes inventory.

Not established / research interpretation:

- Queue position, partial fills, maker rebate actualization, latency Jev→order, and adverse-selection realized cost series are **not provided**.
- Treat public defaults as **research reconstruction of operational rules**, not proof of fill economics.
- Explicit source risk: no hard stop / daily DD circuit / liquidation-distance protection in V3.

## Evidence

### Source-reported

- Public FMZ page 549690 reviewed 2026-09-20: architecture narrative, multi-gate open/reduce logic, GTX-only policy, 120s hold-budget reduce-only exit, full default parameter table, observability list (5-class accuracy vs always-narrow baseline, Brier, non-overlapping samples, confidence calibration, post-fill 1/5/30s path **before fees**).
- Source-reported verification: **JS offline syntax check passed**; source contains config/contract-spec/data-freshness/Jev-schema/order-terminal validation scaffolding (claimed on page).
- Source-reported **absence of performance evidence:** no independently checkable FMZ backtest, DryRun samples, paper logs, or live micro ledgers attached; companion digest narrative is **not** treated here as validated PnL for this V3 artifact.
- Source risk language: uncalibrated event probabilities; not win rate; no hard stop / daily loss / liquidation-distance guard in current V3; DryRun recommended first.

### Independently reproduced

`not independently reproduced`

### Negative evidence

- Source-reported structural negatives: external probability may be miscalibrated per symbol; reduce-only exit may not fill within budget; maker fee constant may diverge from true tier; missing hard risk guards; syntax check ≠ trading validation.
- Research interpretation: even if local gates are conservative, **black-box Jev** creates vendor lock-in and non-reproducibility — a methodological negative for any claim of portable alpha.
- Research interpretation: post-only + 120s reduce-only without hard stop is a **tail-risk path** under gaps/funding/liquidation cascades; absence of observed loss reports is not evidence of safety.
- No in-repo independent replication of 549690 this cycle.
- `none identified in the reviewed sources` beyond the source’s own risk/verification caveats regarding third-party audited failures; **absence is not evidence of no negative result**.

## Falsification plan

Research-proposed (not executed; not authorized):

1. **Always-narrow baseline (research-defined falsification threshold):** On the same symbol/sample, compare Jev 5-class accuracy and Brier vs a baseline that always predicts the narrow bin. Fail any “predictive event model” claim if Jev does not beat that baseline out-of-sample on non-overlapping labels.
2. **Calibration by confidence bin:** Empirical hit rate vs `MIN_CONFIDENCE` buckets. Fail operational use at 0.45 if observed accuracy in the action band does not exceed threshold − research-defined tolerance (research-defined threshold: accuracy ≥ probability reported by model in that bin; else overconfident).
3. **Fill-probability honesty:** Compare Jev passive-fill prob to realized GTX fill rate by side/queue age. Fail quote-retreat logic claims if realized fills diverge systematically from scored probs.
4. **Adverse-selection observability:** Post-fill mid path at 1/5/30s net of `MAKER_FEE + EXIT_SLIPPAGE_BPS + EDGE_BUFFER_BPS`. Fail maker-edge hypothesis if mean post-fill move is consistently against the fill beyond cost budget.
5. **Local-gate ablation:** Open with all gates vs dropping cost-coverage or fill-prob gate. Fail “gates necessary” claim if relaxed gates do not worsen adverse outcomes; fail “gates sufficient” if full gates still lose after costs.
6. **Hold-budget stress:** 60s / 120s / 240s / hard time+stop. Fail “120s budget adequate” if inventory tail or fee drag worsens without compensating gross.
7. **Risk-guard counterfactual (research-defined):** Add research-defined hard stop and daily loss cap in simulation only. Fail any implication that current V3 defaults are safer than guarded variants under gap/vol jump scenarios.
8. **Vendor substitution:** Replace Jev with a simple public heuristic (e.g., imbalance-only bins). Fail “Jev necessary” if a trivial public model matches gates’ net path after costs on the same data.
9. **Action on failure:** Keep `research-only`; do not implement live; do not treat FMZ page or digest as validated alpha.

## Crypto portability

**Portability: `adapted` for venue packaging (crypto perps); `unproven` for net outcomes; signal engine `not portable as open method`.**

- Direct in form: Binance USDⓈ-M microstructure + post-only maker is a common crypto perps surface; 24/7 timestamps fit continuous sampling.
- Adapted constraints: single-symbol net posture; funding not in public cost gates; liquidation risk real despite default leverage 1 if user raises leverage (allowed 1–125 on page).
- Unproven: Jev calibration on non-BTC perps; exchange fragmentation changes queue/fill/adverse selection.
- Stablecoin/quote effects: USDT margin/withdrawal and venue risk remain.
- **Not portable as reconstructable research method** without a public probability engine or frozen API spec + commit.
- Crypto portability is not authorization to trade.

## Limitations

- **Black-box external signal (Jev API)** — core prediction not reconstructable from public page; only local gates/lifecycle are.
- **`not independently reproduced`**
- **No audited public performance evidence** on the strategy page for V3.
- **Missing hard risk controls** (source-stated): no hard stop, no daily DD circuit, no liquidation-distance guard.
- **Fee model is a local constant**, not account-tier truth; funding omitted from public defaults.
- **Page mutability:** last-modified within hours of review; later versions may change defaults.
- **Author neighborhood overlap** with other ianzeng123 FMZ pages does **not** transfer outcome evidence across strategies.
- Incremental value: **public operational defaults + explicit model/execution split + adverse-selection observability design** on FMZ 549690; distinct from Polymarket probability records, cross-venue hedge, online bar-learning, and Kelly/grid capital records.
- Ordinary copy-trading / fear-greed / SuperTrend template pages on FMZ square were **not** captured (below incremental bar).

## Implementation status

No implementation in our research stack. Does not modify NautilusTrader/PyBroker/Qlib; does not authorize Paper/Testnet/Live. Does not call Jev or any external trading API.

`implementation_status: not-implemented`

Source-side: FMZ hosts JavaScript strategy 549690; full body login-gated; page claims syntax check only — **not** treated as our validation.

## Adoption boundary

Research-only. Presence here does **not** mean profitable, validated, or approved for implementation, paper, testnet, or live trading.

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

No record promotes itself by wording or schedule. Any later adoption requires explicit separate review.

## Related Wiki records

No stable Hermes Wiki Brain path known at write time. Do not fabricate Wiki links.

In-repo related (different mechanisms): Polymarket BTC15 conditional-probability FMZ 11020 / 548121 family; FMZ 549412 cross-exchange hedge; FMZ 546440 online learning negative evidence; conformal/fractional Kelly sizing records; FMZ D-Man V3 546875; APFF 548843; meme momentum 548617 (already covered under cross-sectional meme record).

## Sources

1. FMZ strategy page. 「Jev 币安U本位永续决策交易 (Version 3.0)」 / Jev-Driven Short-Horizon Maker Strategy for Binance USDⓈ-M Futures V3, strategy id **549690**, created 2026-09-18 15:37:13, page author ianzeng123. https://www.fmz.com/strategy/549690 (public description + default parameter table + risk/verification sections reviewed 2026-09-20; full source login-gated).
2. FMZ digest listing. 「No Explanations, Just Decisions: Plugging Jev into a Perpetual Strategy — Run It First, Talk Later」, author 发明者量化-小小梦. https://www.fmz.com/digest (listing reviewed 2026-09-20; used only as companion narrative identity, not as performance proof for 549690).
