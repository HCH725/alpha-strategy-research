---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: VCTS ADX-TTI-VPCI volume-confirmed trend long-flat on BTCUSDT 1d bars
created: 2026-10-15
updated: 2026-10-15
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2024-07-16
sources:
  - https://www.tradingview.com/script/K3s5dmdv-TASC-2024-08-Volume-Confirmation-For-A-Trend-System/
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# VCTS ADX-TTI-VPCI volume-confirmed trend long-flat on BTCUSDT 1d bars

## Provenance

Primary source read end to end (TradingView canonical strategy page plus its full open-source block, fetched 2026-10-15 in a real browser session):

- Canonical page: https://www.tradingview.com/script/K3s5dmdv-TASC-2024-08-Volume-Confirmation-For-A-Trend-System/ (`TASC 2024.08 Volume Confirmation For A Trend System` by `PineCodersTASC`, `OPEN-SOURCE SCRIPT`, page stamp Jul 16 2024, adopted as `source_as_of`). Page description in substance: a trend-following system implementation of the techniques Buff Pelz Dormeier discusses in his `Volume Confirmation For A Trend System` article from the August 2024 edition of TASC's Traders' Tips, combining Average Directional Index (ADX), Trend Thrust Indicator (TTI), and Volume Price Confirmation Indicator (VPCI). Dormeier/article lineage is preserved here, never claimed by the page publisher. The page's demo chart shows TSLA 4h (Cboe One) — display context only, never a rule. The page carries no performance table, figure, trade count, date range, or cost basis in its prose — only qualitative author prose (`outperformed similar strategies he tested`, `significantly higher returns and enhanced perceived reliability`, no numbers) — this record claims no source-reported performance (see Evidence).
- Full 92-line `//@version=5` block read in the page's source viewer (`View in Pine Editor・92 lines` affordance). Verbatim source declaration, with the absences it discloses load-bearing for the derived status below: `strategy(title, stitle, false)` — the positional `false` is `overlay`; no `pyramiding` (default 0: single open position, repeat entries rejected), no `default_qty_type`/`default_qty_value` (default one contract), no commission, no slippage, no `process_orders_on_close`, no `calc_on_every_tick`, no stop/limit/profit/loss argument. Source fills are therefore next-bar-open by Pine default evaluated once per completed bar; this record's same-bar-close execution is a separately identified researcher adaptation, never presented as source-native (see Execution assumptions).
- Pinned source inputs (all seven, defaults frozen): `lenADX = 14` (ADX Length), `smt = 14` (ADX Smoothing), `fastTTI = 13` (TTI Fast Average), `slowTTI = 26` (TTI Slow Average), `smtTTI = 9` (TTI Signal Length), `shortVP = 5` (VPCI Short-Term Average), `longVP = 25` (VPCI Long-Term Average). Retuning any of them would be a different, unpinned rule.
- Text census over the pinned block: 1 `strategy(` declaration / 1 `strategy.entry` (`"entry"` with `strategy.long`, no price/qty/when argument) / 1 `strategy.close_all` (`"exit"` on the VPCI-contradiction leg) / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `time(` / 0 bare `open` (the rule reads `high`/`low` via `ta.change`/`ta.atr`, `close` via VWMA/SMA, and `volume` via the VM ratio only) / 0 `crossover(`/`crossunder(` (the entry is a level conjunction, not a cross — see Signal) / 6 `plot(` + 2 `fill(` (render only — none gates any order; the `VPCI*10` plot scaling is display-only).
- Licence and rights: the canonical page is an open-source PineCodersTASC Traders' Tips publication of a Dormeier-article construction. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) research market/timeframe BTCUSDT `1d` (the script takes no symbol, timeframe, session, or venue input and makes no live multi-symbol call; the script NOTE itself applies the system to one instrument at a time, unlike the article's S&P 500 5%-per-name screening portfolio, which is excluded by construction — see Limitations); (2) same-bar-close fills (the source fills next-bar-open — no execution-timing argument ships anywhere, quoted verbatim in census); (3) an adopted 100-bar warmup with pre-warmup bars flat by record rule (structural minimum is the 34th completed bar — see Required data); (4) house sizing/capital/costs replacing the code defaults (see Execution assumptions). Market choice, fill timing, warmup length, and economics are therefore never presented as source-native. The ADX/TTI/VPCI constructions, all seven constants, the triple-conjunction entry, the single `"entry"` long leg, the VPCI-contradiction `close_all`, `pyramiding` default 0, long-only direction, and the no-stop/no-target posture are source-native and unmodified.

Pre-write dedup (2026-10-15): working-tree case-insensitive filename search for `vcts`, `tti`, `vpci`, `dorm`, `trend-thrust`, `volume-confirm`, `K3s5dmdv`, and `pinecoderstasc` returns zero strategy records using this source identity, author, article, or indicator — no pool record computes a Trend Thrust Indicator, a VPC×VPR×VM product, or a volume-multiple-adjusted VWMA spread. Content search for `trend thrust`, `volume price confirmation`, `Dormeier`, `PineCodersTASC`, `K3s5dmdv`, and `Volume Confirmation For A Trend System` returns zero records (the sole `volume-price` content hit pool-wide is the PVT-EMA record, a different cumulative oscillator with no VWMA, no ratio, no multiplier, and no ADX/TTI conjunction). Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Closest pool records differ in mechanism class: `adx-di-cross-strength-gated-two-sided-btcusdt-1d-2026-10-12.md` trades +DI/−DI crosses two-sided (this rule never computes a DI cross, trades long-only, and conjoins two volume-weighted constructions no ADX record contains); `obv-ema-crossover-trend-two-sided-btcusdt-1d-2026-10-10.md`, `pvo-signal-cross-volume-momentum-two-sided-btcusdt-1d-2026-10-12.md`, `cmf-velocity-zero-cross-ema200-bracket-two-sided-btcusdt-1d-2026-10-10.md`, and `klinger-volume-oscillator-trigger-flip-two-sided-btcusdt-1d-2026-10-10.md` are single volume oscillators with cross/zero triggers (none computes TTI, VPCI, or any triple conjunction with an ADX level gate); `alma-cross-volume-gate-btcusdt-1d-2026-10-09.md` uses volume only as a gate on a moving-average cross (different trigger, different construction). Five-axis distinction: source identity differs (PineCodersTASC TASC Aug-2024 Traders' Tips Dormeier lineage versus all pool sources), signal construction differs (volume-multiple-adjusted VWMA spread plus VPC×VPR×VM product plus Wilder-RMA ADX — computed nowhere in the pool), trigger differs (first-bar-of-triple-conjunction long entry with VPCI-contradiction flat exit — not a cross, not a flip, not a band touch), data differs (`volume` read only through the VM ratio alongside `high`/`low`/`close`; no `open`, no funding, no second frame), direction differs (long-flat with flat as a first-class resting state versus predominantly two-sided records).

## Economic mechanism

### Source-reported

Volume-confirmed trend following (page OVERVIEW/CONCEPTS/CALCULATIONS prose plus code structure): Dormeier's search moved from ADX+MACD+OBV to ADX+TTI+VPCI because OBV's volume confirmation improved trading, VPCI weighs volume and price proportionally instead of cumulatively, and TTI adds volume enhancement to a MACD-like spread. ADX above 30 demands a pronounced trend before anything can fire; TTI above its signal demands thrust; VPCI above zero demands that volume confirm rather than contradict the trend. The exit is the mirror discipline stated verbatim in substance: signals to close occur when the VPCI is below 0, indicating a contradiction — volume has stopped confirming, so the position is closed in full rather than nursed.

### Research interpretation

Triple-conjunction long-flat with a contradiction-gated neutral state. Unlike always-in-market holders (Qstick, AC, bandpass records) that must be long or short after warmup, this system rests flat whenever volume contradicts — flat is a first-class state entered by rule, not a residue. Unlike single-oscillator cross systems (OBV-EMA, PVO-signal, CMF-velocity records) that trade one construction's event, every entry here requires three simultaneous truths across three custodians: trend strength (ADX level), thrust direction (TTI level vs its own signal), and volume confirmation (VPCI sign). The TTI's volume multiple squares the fast/slow VWMA ratio, so thrust scales superlinearly with volume-weighted price separation; the VPCI multiplies a VWMA–SMA contradiction term (VPC) by a short-horizon volume bias (VPR) and a volume-trend ratio (VM), so confirmation needs agreement across horizon and across price-versus-volume weighting. The honestly priced cost is entry clustering: in a confirmed trend every post-exit bar re-qualifies immediately, so the system re-enters at once rather than waiting for a fresh cross (see Negative evidence).

## Signal

Exact rule as pinned (defaults quoted — inputs unmodified):

- Declaration (derived): `strategy(title, stitle, false)` with `pyramiding` default 0 pinned (source-native: at most one open position under the single order ID `"entry"`; repeat entry calls while positioned are rejected no-ops). `process_orders_on_close=true` is the predeclared researcher adaptation (no such argument ships in the source). `calc_on_every_tick` is unset (default false: exactly one evaluation per completed bar).
- ADX (pinned, `lenADX = 14`, `smt = 14`): `upDM = ta.change(high)`; `dwDM = -ta.change(low)`; `pDM = na(upDM) ? na : upDM > dwDM and upDM > 0 ? upDM : 0`; `mDM = na(dwDM) ? na : dwDM > upDM and dwDM > 0 ? dwDM : 0`; `ATR = ta.atr(lenADX)`; `pDI = fixnan(100 * ta.rma(pDM, lenADX) / ATR)`; `mDI = fixnan(100 * ta.rma(mDM, lenADX) / ATR)`; `ADX = 100*ta.rma(math.abs((pDI - mDI) / (pDI + mDI)), smt)`.
- TTI (pinned, `fastTTI = 13`, `slowTTI = 26`, `smtTTI = 9`): `fastMA = ta.vwma(close, 13)`; `slowMA = ta.vwma(close, 26)`; `vMult = math.pow((fastMA / slowMA), 2)`; `VEFA = fastMA * vMult`; `VESA = slowMA / vMult`; `TTI = VEFA - VESA`; `signal = ta.sma(TTI, 9)`.
- VPCI (pinned, `shortVP = 5`, `longVP = 25`): `VPC = ta.vwma(close, 25) - ta.sma(close, 25)`; `VPR = ta.vwma(close, 5) / ta.sma(close, 5)`; `VM = ta.sma(volume, 5) / ta.sma(volume, 25)`; `VPCI = VPC * VPR * VM`.
- Entry long (pinned): `if ADX > 30` and `if TTI > signal` and `if VPCI > 0` → `strategy.entry("entry", strategy.long)`. Code truth governs: the three predicates are level comparisons evaluated every completed bar, not `crossover`/`crossunder` calls (the page CALCULATIONS prose says `crosses above` for the TTI leg, but the pinned block contains zero cross functions — the effective event under `pyramiding` 0 is the first bar of the triple conjunction after any flat, and re-entry fires on the first qualifying bar, never mid-conjunction). Same-bar-close execution under the derived declaration.
- Exit flat (pinned): `if VPCI < 0` → `strategy.close_all("exit")` — any open long is closed in full at the adopted fill. No stop, no target, no trailing, no time exit — pinned as written, explicitly none, not invented.
- Direction: long-only long-flat. No short leg exists anywhere in the block; the short side is disabled by source construction, never by researcher choice. A venue without shorting expresses this rule unchanged.
- Ordering determinism: the entry conjunction requires `VPCI > 0` while the exit requires `VPCI < 0`, so no single bar can satisfy both — no same-bar entry/exit conflict exists to resolve under any evaluation order. The entry block precedes the exit block in the source and is preserved as ordered.
- Display isolation: the six plots and two fills feed no order condition; the `VPCI*10` plot scaling is render-only. Order logic reads exactly the entry conjunction plus the exit predicate.

## Required data

- Completed `1d` bars of BTCUSDT: `high` and `low` (ADX directional movement and ATR), `close` (all VWMA/SMA price legs), and `volume` (VM ratio only: `ta.sma(volume, 5) / ta.sma(volume, 25)`). No `open` series, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (researcher-declared; the script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction).
- Warmup: VWMA/SMA legs need their full lengths (`slowTTI = 26`, `longVP = 25`); `signal = ta.sma(TTI, 9)` over a TTI numeric from the 26th bar is first numeric on the 34th completed bar, which is the structural minimum for the full triple conjunction. `ta.rma`/`fixnan` ADX legs are numeric earlier and never the binding constraint. Structural minimum is therefore the 34th completed `1d` bar; the adopted warmup is the first 100 completed `1d` bars flat by record rule (predeclared researcher choice). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (researcher-declared per the derived declaration; venue/symbol spelling is naming only, never presented as source-native semantics).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. The source's own timing is next-bar-open (no execution-timing argument ships anywhere — quoted verbatim in Provenance); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill. With no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and the entry/exit predicates are mutually exclusive every bar (see Signal), so no ordering resolution is required.
- Engine path for `1d` (gate 5, stated plainly): `1d` is a Binance-documented USDT-M kline interval; the derived rule needs only completed `1d` candles (`high`/`low`/`close` plus bar `volume` for the VM ratio) on a single frame — no second timeframe, no unfinished-bar read, no intrabar path, no funding/OI/mark-price leg. The volume leg is the same bar-volume-ratio path already admitted in pool volume records (PVO/OBV/CMF/Klinger/ALMA-gate family); nothing here reads tick-level, quote-level, or cross-venue volume. That is the same single-frame completed-bar path as the admitted `1d` records; the ADX/TTI/VPCI recursions advance deterministically from known bars with `na`/`fixnan` seeds, so no hidden lookahead is ever modeled. Anything beyond that single-frame completed-bar path would be a different, unverified claim — none is admitted here.
- Sizing/capital/costs: the code ships no quantity, commission, or slippage argument (one default contract; the page DISCLAIMER's `10% of equity` / `5 ticks` prose describes tester settings, never coded economics), so evaluation carries the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions here, never presented as source-native behavior. Historical funding is flagged per the house baseline: no campaign may claim complete realized-funding performance without a verified implementation.
- Concurrency: `pyramiding` default 0 is source-pinned — at most one open long under the fixed order ID `"entry"`; repeat conjunction bars while positioned are rejected no-ops; the exit leg closes all; re-entry is allowed on the very next qualifying bar after any flat (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic — the article's 5%-per-name S&P 500 screening portfolio is excluded by construction (see Limitations).

## Evidence

### Source-reported

The page ships the full construction (Wilder-RMA ADX function with both lengths, volume-multiple TTI with fast/slow/signal lengths, VPC×VPR×VM product with short/long lengths, all seven defaults, the triple-conjunction `"entry"` long leg, the VPCI-contradiction `close_all("exit")` leg, default single-position semantics, and the Dormeier-article lineage note with the single-instrument NOTE). It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — the only performance language is qualitative author prose with no numbers attached. This record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.exit`, 0 `strategy.order` — the sole position-closing path is the coded VPCI-contradiction `close_all` leg. The absence is coded (the order block ends with the exit leg before no further order call), disclosed in Signal for the reviewer rather than upgraded into a source claim.
2. Entry/exit mutual exclusion holds on every bar by arithmetic (`VPCI > 0` versus `VPCI < 0`), even though they sit in separate `if` statements — so no single bar can satisfy more than one order leg under any evaluation order.
3. Prose/code wording gap, fenced: the page CALCULATIONS prose says the TTI leg `crosses above` its signal, but the pinned block evaluates `TTI > signal` as a level every bar with zero cross functions in census. Code governs this record (first-bar-of-conjunction event under `pyramiding` 0); the prose verb is never used to invent a cross trigger. A reviewer reading only the prose would mis-specify the trigger — the block is quoted for exactly this reason.
4. Re-entry clustering, admitted plainly: after a contradiction exit, the very next bar satisfying all three levels re-enters at once — there is no cooldown, no fresh-cross requirement, no re-confirmation delay. A market oscillating around VPCI zero with ADX pinned above 30 can compound consecutive exit/re-entry pairs at the close. This is the coded trade, disclosed, not a tunable parameter here.
5. Boundary ties hold their side: exactly-equal prints (`ADX == 30`, `TTI == signal`, `VPCI == 0`) satisfy neither entry nor exit, so no order fires and the book carries the prior state; a `na` ADX/TTI/signal/VPCI print (pre-warmup or degenerate early bars) falsifies every comparison, so no order can fire without full numeric inputs; a zero 25-bar volume window would zero the VM denominator, which cannot occur on BTCUSDT `1d` and is fenced as out-of-scope rather than modeled; warmup bars are flat by record rule.
6. The seven lengths (14/14/13/26/9/5/25), the ADX>30 threshold, the VPCI>0 / VPCI<0 pair, the VWMA/SMA function choices, the squared volume multiple, the fixed order IDs, `pyramiding` 0, long-only direction, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning a constant, moving the ADX threshold, adding a stop/target/cooldown/trailing, switching a moving-average variant, disabling the volume leg, or enabling a short side would each be a different, unpinned rule — none is admitted here.
7. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT `1d` market/frame choice, same-bar-close fills, the adopted 100-bar warmup with record-rule pre-warmup flat, and house sizing — all predeclared above; every construction, constant, threshold, comparison, transition, exit leg, and risk posture is source-verbatim. This record is therefore never evidence that the original next-bar-open demo-chart source itself passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: ADX(14,14) / TTI(13,26,9) / VPCI(5,25) / ADX>30 / TTI>signal level / VPCI>0 entry with VPCI<0 exit / `pyramiding` 0 / long-only / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Thrust relevance: dropping the TTI leg (ADX>30 with VPCI>0 entry, VPCI<0 exit) must not improve net expectancy; fail ⇒ the volume-multiple thrust adds nothing over strength-plus-confirmation alone.
- F2 — Contradiction-exit relevance: replacing the VPCI<0 exit with an ADX<30 strength-breakdown exit (entries unchanged) must not improve net expectancy; fail ⇒ the volume-contradiction exit is dominated by simply following strength out.
- F3 — Strength-gate relevance: dropping the ADX>30 gate (TTI>signal with VPCI>0 entry, VPCI<0 exit) must not improve net expectancy; fail ⇒ the pronounced-trend demand adds nothing over thrust-plus-confirmation alone.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (researcher-declared venue family). The `high`/`low`/`close`/bar-`volume` logic ports across perpetual venues publishing standard klines without structural change; the rule is long-only, so a spot-only deployment expresses it unchanged. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read beyond completed `1d` bars, so session-gap behavior needs no approximation. Bar-volume semantics differ across venues (wash/quote-volume conventions), which is carried as data risk, never modeled away. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived market/frame: the source pins no symbol, venue, or timeframe (its demo chart shows TSLA 4h — display context only); BTCUSDT `1d` is a researcher choice. Results on any other market or frame are a different, unpinned claim.
- Derived fill timing: the source fills next-bar-open evaluated once per completed bar; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- Article portfolio excluded: the article allocates 5% of equity per qualifying S&P 500 constituent with proceeds recycling and cash residuals; the script NOTE applies the system to one instrument at a time, and this record pins exactly that single-instrument reading. Any multi-name screening, rotation, or cash-buffer behavior would be a different, unpinned rule — none is admitted here.
- No price stop and no time stop: adverse excursion after entry has no guardrail beyond the VPCI-contradiction exit, which arrives only when volume stops confirming; a slow-bleed trend with VPCI pinned positive never exits until contradiction prints. Re-entry clustering around VPCI zero can compound consecutive exit/re-entry losses. This is the coded posture, disclosed as the record's principal risk.
- Source economics replaced: the code declares no quantity/commission/slippage (the DISCLAIMER's 10%-equity/5-tick prose is tester-setting description, never coded economics); derived evaluation carries the full house cost load instead, and this record reports no net performance of any kind.
- Warmup cost: the adopted 100-bar warmup means the system is blind for the first 100 bars of any `1d` evaluation window (structural minimum 34).
- Performance evidence is absent: neither the page prose (qualitative author claims only, no numbers) nor the open-source block reports any number; nothing here is calibrated, fitted, or tuned to any window.
- Licence: the canonical page is an open-source PineCodersTASC Traders' Tips publication of a Dormeier-article construction — downstream implementation must honor its House-Rules terms; this record copies no code block.

## Implementation status

Not implemented. No Hummingbot controller/executor, no Qlib screening, no Paper/Testnet/Live run has been performed from this record. Admission claims pinned-engine expressibility only (see Execution assumptions), subject to independent six-gate review.

## Adoption boundary

Research-only. Not approved for any downstream screening, parity run, or trading authorization. Only a `PASS` under the live six-gate contract may merge this record into `main`; any `NOT_LOSSLESS` finding closes the PR lane without promotion.

## Related Wiki records

None.

## Sources

- Canonical TradingView strategy page (fetched 2026-10-15 in a real browser session; title/author/date/description read; full 92-line `//@version=5` block read end to end in the page source viewer; no order logic invented): https://www.tradingview.com/script/K3s5dmdv-TASC-2024-08-Volume-Confirmation-For-A-Trend-System/
- Pine Script strategy semantics reference (evaluation defaults only — `process_orders_on_close`, `calc_on_every_tick`, `pyramiding`, `strategy.entry`/`strategy.close_all` single-position semantics — never a source of strategy facts): https://www.tradingview.com/pine-script-docs/concepts/strategies/
