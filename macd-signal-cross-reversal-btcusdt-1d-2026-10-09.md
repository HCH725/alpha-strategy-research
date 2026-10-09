---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: MACD signal-line cross reversal two-sided on BTCUSDT 1d bars
created: 2026-10-09
updated: 2026-10-09
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2022-05-23
sources:
  - https://www.fmz.com/strategy/356844
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/MACD-Pine%E7%AE%80%E5%8D%95%E7%AD%96%E7%95%A5.md
  - https://www.tradingview.com/pine-script-reference/v5/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# MACD signal-line cross reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-09):

- Canonical page: https://www.fmz.com/strategy/356844 (page title `MACD Pine简单策略 | FMZ`, publisher account `发明者量化`). Fetched over HTTPS during this cycle (729358 bytes): the page embeds the full Pine block byte-verbatim — `ta.macd(close, fastPeriod, slowPeriod, singnalPeriod)` with the `if fast>slow and fast[1]<slow[1]` / `strategy.entry("Enter Long", strategy.long)` / `else if fast<slow and fast[1]>slow[1]` / `strategy.entry("Enter Short", strategy.short)` order block — and the page-embedded `/*backtest*/` header (`start: 2021-05-04 00:00:00`, `end: 2022-05-03 23:59:00`, `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Bitfinex","currency":"BTC_USD"}]`). Word-boundary counts over the whole landing HTML: `Sharpe` 0, `Net Profit` 0, `Profit Factor` 0, `Win Rate` 0, `Annualized` 0, `Max Drawdown` 0 — the page ships no performance numbers of any kind (adopted as `source_as_of` 2022-05-23 from the mirror `Last Modified` stamp; the page exposes no separate Created stamp in the fetched state).
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (verified repository head at research time via `git ls-remote` — the same head pin as the merged Darvas, Double-Seven, DPO-EMA, KST, Schaff, TRIX, SQZMOM-LB, Aroon, Qstick, AC, Elder-ray and ActionZone admissions), exact file path `MACD-Pine简单策略.md` (non-ASCII filename preserved verbatim; percent-encoded blob URL in Sources). File 875 bytes, blob SHA `b013920c8f38ade77dbfe6c05ef69276974abda7` (verified against the GitHub contents API at the pinned commit — size and SHA both match; content bytes re-downloaded at the pin are byte-identical, sha256 `a0f556df90d3479ec83f4831fd9f1cb3702c217ded34ea77cb2fc492452fd10e`). The mirror prints `> Detail` = https://www.fmz.com/strategy/356844 and `> Last Modified` = 2022-05-23 18:08:17. The mirror carries no prose section at all (arguments table plus code only), so there is no prose/code divergence to fence — the code is the entire specification.
- Text census over the pinned code block: 2 `strategy.entry` (`strategy.entry("Enter Long", strategy.long)` / `strategy.entry("Enter Short", strategy.short)`, inside an `if` / `else if` pair, no `when=`, no price/`qty` argument — market entries) / 0 `strategy.close` / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=` / 0 `request.*` / 0 `security(` / 0 `timeframe(` / 0 `time(` / 0 `volume` / 0 `open` / 0 `high` / 0 `low` (the rule reads `close` only, via `ta.macd(close, ...)`) / exactly 3 `input.*` (`fastPeriod = input(12, "fast")`, `slowPeriod = input.int(26, "slow")`, `singnalPeriod = input.float(9, "signal")` — all pinned at defaults; any other value is a different, unpinned rule). No `strategy(...)` declaration ships anywhere; no `//@version` tag ships anywhere (the block uses v5-only builtins `ta.macd`/`input.int`/`input.float`, so it parses only under v5 semantics — stated as observed, never as a shipped declaration). `pyramiding`, `process_orders_on_close`, `calc_on_every_tick`, `initial_capital`, `commission_*` and `slippage` are unset throughout (Pine language defaults apply). The 2 `plot` calls render the two lines only and feed no order condition.
- No risk layer ships anywhere in the source: zero stop/target/trailing/time-exit order legs, and the `else if` structure makes the two entries mutually exclusive on every bar — the reversal-only posture below is therefore the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention.
- Page/mirror performance language is absent entirely (no table, figure, or number anywhere) — this record claims no source-reported performance and no reproduced performance.

Licence and rights: the canonical page is a public FMZ strategy publication by 发明者量化; the pinned code block carries no licence header of its own (the FMZ page is the publication vehicle). This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) same-bar-close fills (the source fills next-bar-open — no `process_orders_on_close` ships anywhere); (2) an adopted 50-bar warmup with pre-warmup bars flat by record rule (covers the slow length 26 plus the 9-bar signal smoothing plus seeding margin — see Required data); (3) house sizing/capital/costs replacing the absent source sizing (no capital, commission, fee, slippage or margin assumption ships anywhere — see Execution assumptions); (4) venue port from the header's `Bitfinex BTC_USD` spot to `BTCUSDT` Binance perpetual on the source-native `1d` frame (the short leg requires a margin venue — see Execution assumptions and Crypto portability). Indicator arithmetic (12/26/9.0 on close), both cross triggers, the `if`/`else if` exclusivity, order IDs, two-sided reversal handling, and the no-stop/no-target risk posture are source-native and unmodified.

Pre-write dedup (2026-10-09): working-tree case-insensitive searches for `356844`, `MACD-Pine`, and `Enter Long` return zero admitted rules using this source, author publication, or mechanism — the only `macd` hits anywhere are incidental prose mentions inside `ema-cloud-7-20-trend-btcusdt-1d-2026-10-07.md`, `ichimoku-rsi-gated-reversal-btcusdt-1d-2026-10-08.md`, `psar-flip-stop-reverse-btcusdt-1d-2026-10-09.md`, `schaff-trend-cycle-band-edge-two-sided-btcusdt-1d-2026-10-09.md` and `vortex-spread-threshold-ema-btcusdt-1d-2026-10-09.md` (unrelated prose, never a MACD-cross rule). Same-publisher 发明者量化 records exist (MACD-Pine simple is the publisher's own square publication) but no pool record shares this canonical identity. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long — single file verified), #49 (Gaussian channel StochRSI-gated breakout long — single file verified), #58 (ML/reconstruction batch — file list verified, no MACD record), and #63 (SuperTrend ATR-flip trend long — single file verified) — different mechanisms, indicators, and sources. The closed non-main PR #17 (MACD histogram) never reached `main` and fires on histogram-zero-cross, a different construction in any case. Closest pool record is a different mechanism class: `ichimoku-macd-triple-confirm-reversal-ethusdt-1h-2026-10-08.md` AND-gates the MACD line/signal cross behind three Ichimoku confirmation legs (Tenkan/Kijun, Chikou, Kumo) on ETHUSDT 1h — a four-leg composite trigger. Five-axis distinction: mechanism differs (this record fires on the naked oscillator cross with zero confirmation legs — every Ichimoku-gated trade event set differs by construction), signal construction differs (single `fast`/`slow` strict-cross condition per side versus a four-condition AND gate), exits differ in event set (pure cross-to-cross reversal with no gate that can veto the exit), source identity differs (FMZ 356844 plus blob `b013920c` versus Coinrule TV plus hasnocool blob `da95fe6`), and research frame/market differ (`1d` BTCUSDT versus `1h` ETHUSDT).

## Economic mechanism

### Source-reported

The mirror ships no prose — the specification is the code: the classic MACD momentum rotation. When the fast MACD line rotates up through its signal line, upside momentum is judged dominant and the system aligns long; when it rotates down through, downside momentum is judged dominant and the system aligns short. The design bets that momentum-line rotations on the daily frame precede multi-day directional drift, and that staying aligned with the last rotation (always-in-market) harvests more drift than it surrenders to whipsaw.

### Research interpretation

Naked-oscillator rotation system with no price-level, band, cloud, or confirmation state — two-sided and always-in-market after the first signal. Unlike raw price-EMA cross systems (EMA-20-50, dual-EMA-engulfing, golden-cross-SMA) that compare smoothed price against smoothed price, this system compares two derived momentum series (both functions of 12/26 EMAs of close, then smoothed again by 9) — entries fire on second-order rotation, strictly later and smoother than first-order price crosses, at the cost of deeper lag into V-turns. Unlike the Ichimoku-MACD composite, no trend/level gate can veto or delay a rotation: every strict cross trades, including crosses printed inside ranges. Unlike flat-capable systems, there is no neutral state after the first signal — a long exists until a death cross reverses it to short and vice versa, so ranging markets grind through repeated full reversals with no stop to truncate them. The bet is on daily-frame momentum persistence, never on a level, breakout, squeeze, calendar, or mean-reversion anchor.

## Signal

Exact rule as pinned (12/26/9.0 frozen — the three inputs at defaults; any other value is a different, unpinned rule):

- Declaration (derived): bare order block with no `strategy(...)` declaration and no `//@version` tag (both pinned as absent); v5-only builtins observed. Same-bar-close execution and house sizing adopted for the derived record (neither ships in the source). `calc_on_every_tick` is unset (defaults false: exactly one evaluation per completed bar). No commission, margin, or capital assumption ships anywhere — pinned as absent, with house costs applying to the derived evaluation (see Execution assumptions).
- Indicator arithmetic (pinned): `[fast, slow, _] = ta.macd(close, 12, 26, 9.0)` — `fast` is the MACD line (12-EMA minus 26-EMA of close), `slow` is the 9-bar signal smoothing of `fast`; the histogram third output is discarded (`_`) and read by no order line.
- Entry long: `if fast > slow and fast[1] < slow[1]` → `strategy.entry("Enter Long", strategy.long)` — fires on the single bar where the MACD line crosses strictly up through the signal line on confirmed closes, with same-bar-close execution under the derived declaration.
- Entry short: `else if fast < slow and fast[1] > slow[1]` → `strategy.entry("Enter Short", strategy.short)` — the exact mirror on the cross down, same execution. The `else if` makes both conditions mutually exclusive on every bar by construction: no bar can ever fire both legs, so no same-bar ordering ambiguity exists anywhere in this record.
- Direction: two-sided with reversal only. No `strategy.close`/`strategy.exit` leg exists; a long closes only when a death cross fires the short entry (which reverses the position under the pinned no-pyramiding default), and vice versa. Before the first cross the system is flat (no position by construction). No stop, no target, no trailing, no time exit — pinned as written, explicitly none, not invented.
- Display isolation: the 2 `plot` calls render the two lines only and cannot change any order.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (sole series read by `ta.macd(close, ...)`). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (source-native per the page-embedded `period: 1d` header; `basePeriod: 1h` equals native 1h execution granularity — 24 1h bars per 1d bar on a 24/7 venue — and with market-entry/reversal legs only and no stop/limit legs anywhere, no intrabar path exists for the base to affect). The script takes no timeframe input and makes no live `request.*`/`security(` call, so it is single-frame by construction.
- Warmup: the slow window needs 26 completed `1d` bars and the signal smoothing needs 9 bars of MACD output on top. The adopted warmup is the first 50 completed `1d` bars flat by record rule (predeclared researcher choice — covers 26 + 9 plus seeding margin); no signal before bar 51 may trade. No repainting (`fast[1]`/`slow[1]` reference only completed prior bars), no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (source-native decision frame `1d` kept; venue ported from the header's `Bitfinex BTC_USD` spot — a predeclared derivation, never presented as source-native. Naming transfer from `BTC_USD` to `BTCUSDT` plus the spot→perpetual port are the only market changes).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar-open (no execution-timing argument ships anywhere); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere and mutually exclusive entries, there is no same-bar ordering ambiguity of any kind.
- Sizing/capital/costs: the source ships no capital, sizing, commission, fee, slippage, or margin assumption anywhere — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: no `pyramiding` ships anywhere, pinning the language default of no same-direction adds — at most one unit per side under the fixed order IDs `Enter Long` / `Enter Short`; opposite-side entries reverse the position in full under that default; same-side refires while already positioned are no-ops; re-entry is allowed immediately on the next opposite cross (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires a margin venue (see Crypto portability).

## Evidence

### Source-reported

The mirror ships the full construction (12/26/9.0 inputs, `ta.macd(close, ...)` decomposition, strict prior-bar-confirmed cross conditions, `if`/`else if` exclusivity, fixed `Enter Long`/`Enter Short` order IDs, two-sided reversal handling), the page-embedded 1d/1h May-2021→May-2022 backtest header, and the `MACD Pine简单策略` title. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.close`, 0 `strategy.exit`, 0 `strategy.order`, 0 `stop=`/`limit=`/`qty`/`when=` — the sole position-closing path on each side is the opposite cross reversing under the no-pyramiding default. The absence is coded (the order block ends with the short entry and only display calls follow).
2. Always-in-market after the first signal, admitted plainly: once the first cross trades, the system holds a position on every subsequent bar until the opposite cross — there is no flat state, no stop, no time-stop. A market that chops sideways across the signal line reverses on every rotation with full exposure each way; adverse excursion after entry has no guardrail of any kind. This is the coded trade, disclosed, not a tunable parameter here.
3. Whipsaw is the structural cost: the naked cross has no confirmation, filter, gate, or minimum-separation rule — rotations printed inside ranges trade identically to rotations printed at trend births. The `else if` exclusivity removes ordering ambiguity but never removes false signals.
4. Lag at V-turns: the signal line smooths an already twice-EMAs-derived series (12/26 then 9) — a sharp reversal must drag the MACD line across the full signal gap before any trigger prints, so entries arrive strictly after the turn by code. The lag is the coded smoother, disclosed, not shortened.
5. Derivation boundary fenced: the only non-source-native behaviors in this record are same-bar-close fills, the adopted 50-bar warmup with record-rule pre-warmup flat, house sizing/costs, and the Bitfinex-spot→Binance-perp venue port — all predeclared above; frame, every literal, the MACD arithmetic, both triggers, the `else if` exclusivity, the order IDs, reversal handling, and the risk posture are source-verbatim. This record is therefore never evidence that the original next-bar-open Bitfinex-spot source itself passes.
6. The `12` / `26` / `9.0` literals (note the float-typed signal input `input.float(9, "signal")`, pinned at 9.0), the strict cross (not touch) triggers, the prior-bar confirmation (`fast[1]`/`slow[1]`), the fixed order IDs, the two-sided posture, the reversal-only exits, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning any length, converting a cross into a touch or a level hold, adding a stop/target/filter/cooldown/gate, dropping a side, or exiting to flat instead of reversing would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `12/26/9.0` / close-only MACD / strict confirmed crosses / `if`+`else if` exclusivity / two-sided reversal / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Cross-timing relevance: replacing the strict-cross trigger with the always-live MACD position state (long whenever `fast > slow`, short whenever `fast < slow`, evaluated every bar) must not improve net expectancy; fail ⇒ the cross timing adds nothing over holding the oscillator state.
- F2 — Short-side relevance: dropping the short leg (long on golden cross, flat — not short — on death cross) must not improve net expectancy; fail ⇒ the two-sided reversal is dominated by a long/flat posture on this market.
- F3 — Parameter relevance: replacing the pinned `12/26/9.0` triple with any adjacent classic triple must not improve net expectancy; fail ⇒ the pinned defaults carry no advantage over neighboring smoothings and the record's literal choice is arbitrary.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision frame source-native `1d`; venue ported from Bitfinex spot — predeclared). The close-only arithmetic ports across perpetual venues without structural change. The short leg requires a margin/perp venue: a spot-only deployment cannot express the death-cross short (exiting to flat instead would be a different, unpinned rule). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived fill timing: the source fills next-bar-open on a 1d-decision/1h-base Bitfinex-spot backtest; this record executes same-bar-close on `1d` BTCUSDT perpetual. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- No price stop, no time stop, no flat state: adverse excursion after entry has no guardrail beyond the opposite rotation, which may arrive many bars later or after deep excursion; a market that trends against the position without printing the opposite cross is held indefinitely. This is the coded posture, disclosed as the record's principal risk.
- No source cost declaration: no capital, sizing, commission, fee, slippage, margin, or funding assumption ships anywhere in the source — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Venue port: the source venue is Bitfinex `BTC_USD` spot; the derived venue is Binance `BTCUSDT` perpetual. Microstructure, tick size, fee, and funding differences are outside the source and carried by the house overlay — no equivalence is claimed.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- FMZ canonical strategy page (发明者量化): https://www.fmz.com/strategy/356844
- Immutable mirror file at pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (blob `b013920c8f38ade77dbfe6c05ef69276974abda7`, 875 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/MACD-Pine%E7%AE%80%E5%8D%95%E7%AD%96%E7%95%A5.md
- Pine strategy semantics (order calls, default execution, built-in averages): https://www.tradingview.com/pine-script-reference/v5/
