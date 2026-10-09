---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Coppock curve zero-state long/flat on BTCUSDT 1d bars
created: 2026-10-09
updated: 2026-10-09
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-11-13
sources:
  - https://www.fmz.com/strategy/431926
  - https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E5%9F%BA%E4%BA%8ECoppock%E6%9B%B2%E7%BA%BF%E7%9A%84%E9%87%8F%E5%8C%96%E4%BA%A4%E6%98%93%E7%AD%96%E7%95%A5Coppock-Curve-Based-Quantitative-Trading-Strategy.md
  - https://www.tradingview.com/pine-script-reference/v4/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Coppock curve zero-state long/flat on BTCUSDT 1d bars

## Provenance

Primary source read end to end (immutable public mirror file plus its recorded FMZ canonical page, fetched 2026-10-09):

- Canonical page: https://www.fmz.com/strategy/431926 (page title carries `Coppock`, publisher account `ChaoZhang`). Fetched over HTTPS during this cycle (771724 bytes): the page embeds the full Pine block byte-verbatim — `curve = wma(roc(source, longRoCLength) + roc(source, shortRoCLength), wmaLength)` with the `ticker = security(security, "D", close)` SPY-daily feed line, the `if (Bull) strategy.entry("Long", strategy.long, ...)` / `if (Bear) strategy.close("Long", qty_percent=100, ...)` order pair, and the `strategy.exit(id="Long Trail Stop", stop=longStopPrice)` leg — and the page-embedded `/*backtest*/` header (`start: 2023-10-13 00:00:00`, `end: 2023-11-12 23:59:00`, `period: 1d`, `basePeriod: 1h`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`). Word-boundary counts over the whole landing HTML: `Sharpe` 0, `Net Profit` 0, `Win Rate` 0, `Max Drawdown` 0 — the page ships no performance numbers of any kind (adopted as `source_as_of` 2023-11-13 from the mirror `Last Modified` stamp; the page exposes no separate Created stamp in the fetched state). The bilingual prose (formula `10-period WMA of 14-period ROC + 11-period ROC`, zero-up-cross buys / zero-down-cross sells, optional trailing stop, `$SPY` proxy signal) matches the code it embeds — no prose/code divergence except the trail-stop arithmetic fenced below.
- Immutable mirror actually executed against (primary code source): repository https://github.com/fmzquant/strategies, full commit SHA `7853bb2bf262c4567ac238d3552d97f0e50cb801` (verified repository head at research time via `git ls-remote` — the same head pin as the merged Darvas, Double-Seven, DPO-EMA, KST, Schaff, TRIX, SQZMOM-LB, Aroon, Qstick, AC, Elder-ray, ActionZone and MACD admissions), exact file path `基于Coppock曲线的量化交易策略Coppock-Curve-Based-Quantitative-Trading-Strategy.md` (non-ASCII filename preserved verbatim; percent-encoded blob URL in Sources). File 6790 bytes, blob SHA `6d089ff76f0da59991cbfef609df5ef3c6ba9bbb` (verified against the GitHub contents API at the pinned commit — size and SHA both match; content bytes re-downloaded at the pin are byte-identical, sha256 `e45327cd1a96437a`). The mirror prints `> Detail` = https://www.fmz.com/strategy/431926 and `> Last Modified` = 2023-11-13 11:44:55. The mirror `> Author` field is `ChaoZhang`; the embedded code header carries `// © RolandoSantos` under MPL 2.0 — both attributions are kept separate here, neither is claimed as Hermes authorship.
- Text census over the pinned code block: 1 `strategy.entry` (`strategy.entry("Long", strategy.long, comment = "LE")`, inside `if (Bull)`, no price/`qty` argument — market entry) / 1 `strategy.close` (`strategy.close("Long", qty_percent=100, comment="close")`, inside `if (Bear)`) / 1 `strategy.exit` (the trail-stop leg, arithmetic no-op at the pinned default — see Signal) / 0 `strategy.order` / 0 `request.*` / 1 `security(` (`ticker = security(security, "D", close)` with `security = input("SPY")` — the cross-market feed this derived record ports away, predeclared below) / 0 `time(` / 0 `volume` / 0 `open` / 0 `high` / 0 `low` (the rule reads `close` only: 4 `close` hits, two inside `roc(source, ...)` via the ticker plus the stop arithmetic) / 2 `roc(` / 1 `wma(` / exactly 5 `input(...)` declarations (`Trail Long Loss (%)` 100, `security` "SPY", `WMA Length` 10, `Long RoC Length` 14, `Short RoC Length` 11 — all pinned at defaults; any other value is a different, unpinned rule). `pyramiding`, `process_orders_on_close`, `calc_on_every_tick`, `commission_*` and `slippage` are unset throughout (Pine language defaults apply). `//@version=4` is declared; the `strategy(...)` declaration ships with `default_qty_type=strategy.cash, default_qty_value=10000, initial_capital=10000` (source sizing, replaced by the house overlay in the derived record — predeclared). The 3 `hline` calls (±100/0 bands) and the single `plot(curve)` render display only and feed no order condition.
- Page/mirror performance language is absent entirely (no table, figure, or number anywhere) — this record claims no source-reported performance and no reproduced performance.

Licence and rights: the canonical page is a public FMZ strategy publication by ChaoZhang; the embedded code header attributes © RolandoSantos under MPL 2.0. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) signal-source port from the source's `security("SPY", "D", close)` cross-market feed to the traded market's own `1d` closes — `curve = wma(roc(close, 14) + roc(close, 11), 10)` on BTCUSDT (the pinned engine has no SPY equity feed/connector, so the source-native SPY-signal/BTC-execution split cannot satisfy gate 5; the ported formula is otherwise verbatim); (2) same-bar-close fills (the source fills next-bar-open — no `process_orders_on_close` ships anywhere); (3) an adopted 50-bar warmup with pre-warmup bars flat by record rule (covers the 14-bar ROC window plus the 10-bar WMA smoothing plus seeding margin — see Required data); (4) house sizing/capital/costs replacing the absent-apart-from-cash-sizing source economics (see Execution assumptions). The WMA/ROC arithmetic (10/14/11), the zero-level state triggers, the `if (Bull)` / `if (Bear)` exclusivity, the `Long` order ID, long/flat handling, and the no-stop posture (trail leg arithmetic no-op at the pinned default 100 — a pinned fact, not an adaptation) are source-native and unmodified.

Pre-write dedup (2026-10-09): working-tree case-insensitive searches for `431926`, `coppock`, and `Copp Curve` return zero admitted rules using this source, author publication, or mechanism — the only contiguous `coppock` hits anywhere are prose search-terms inside the merged TRIX and Qstick records' own dedup paragraphs (never a Coppock rule, indicator, or order). Same-publisher ChaoZhang records exist (KST, Aroon, TRIX, Schaff, MACD-Pine, Qstick, Chandelier-PR) but carry different canonical identities, different indicator families, and different order sets. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long — single file verified), #49 (Gaussian channel StochRSI-gated breakout long — single file verified), #58 (reconstruction batch — file list verified, no Coppock/ROC record), #63 (SuperTrend ATR-flip trend long — single file verified), and #89 (Chandelier Exit dual-stop state-flip long — single file verified) — different mechanisms, indicators, and sources. Closest pool record is a different mechanism class: `fisher-zero-cross-reversal-btcusdt-1d-2026-10-09.md` is a normalized nonlinear-transform zero-CROSS system, two-sided with reversal on the cross edge. Five-axis distinction: mechanism differs (this record holds a level STATE — long on every bar the ROC-sum smoothing sits above zero, flat on every bar below — versus edge-triggered cross reversal), signal construction differs (`wma(roc14 + roc11, 10)` momentum-sum smoothing versus Fisher-transformed price normalization — no pool record evaluates a summed-ROC WMA against zero), exits differ in event set (state-loss flat exit on `curve < 0` with full close, no opposite-side entry versus reversal into short), source identity differs (FMZ 431926 November-2023 ChaoZhang/RolandoSantos versus other FMZ IDs or TV authors), and direction handling differs (long/flat single side with the short side explicitly absent versus symmetric two-sided).

## Economic mechanism

### Source-reported

Classic Coppock rotation: the summed 11/14-bar rate-of-change, smoothed by a 10-bar WMA, measures medium-term momentum accumulation. When the smoothed sum sits above zero, upside momentum is judged dominant and the system aligns long; when it sits below zero, momentum is judged exhausted and the system stands flat. The design bets that the zero-state of smoothed multi-window momentum on the daily frame separates durable drift from chop, and that sidestepping sub-zero regimes harvests more drift than it surrenders to lag at regime births.

### Research interpretation

Bounded-state momentum system with no price level, band, cloud, stop, or confirmation leg — long/flat and state-held after the first signal. Unlike cross-edge systems (MACD, Fisher, KST) that trade only the crossing bar, this system re-asserts the state every bar: `if (Bull)` re-fires the long entry on each above-zero bar (a no-op while positioned under the pinned no-pyramiding default), so the position persists by state, not by edge memory. Unlike two-sided reversal systems there is no short leg and no always-in-market grind — sub-zero regimes are flat, so chop below zero costs only opportunity, never adverse exposure. Unlike the SPY-proxy source, the derived record spends its signal on the traded market itself (predeclared port): the bet is on BTCUSDT's own smoothed-momentum persistence, never on equity-crypto basis, a level, breakout, squeeze, calendar, or mean-reversion anchor.

## Signal

Exact rule as pinned (10/14/11 frozen — the three lengths at defaults; any other value is a different, unpinned rule):

- Declaration (derived): `//@version=4`-era builtins (`roc`, `wma`, `strategy.*` v4 semantics observed). Source `strategy(...)` cash sizing replaced by the house overlay (predeclared). `calc_on_every_tick` is unset (defaults false: exactly one evaluation per completed bar). No commission, margin, or capital assumption beyond the shipped `$10k` cash sizing ships anywhere — pinned as replaced, with house costs applying to the derived evaluation (see Execution assumptions).
- Indicator arithmetic (pinned, source ported): `curve = wma(roc(close, 14) + roc(close, 11), 10)` — the 14-bar and 11-bar rates of change of the `1d` close, summed, then smoothed by a 10-bar linearly-weighted average. The source computes this on `security("SPY", "D", close)`; the derived record computes it on BTCUSDT's own `1d` closes (predeclared adaptation — the only series change; lengths, operators, and order are verbatim).
- Entry long: `if (Bull)` where `Bull = curve > 0` → `strategy.entry("Long", strategy.long)` — asserted on every above-zero bar on confirmed closes, with same-bar-close execution under the derived declaration. While already long, refires are no-ops under the pinned no-pyramiding default (no `pyramiding` ships anywhere).
- Exit flat: `if (Bear)` where `Bear = curve < 0` → `strategy.close("Long", qty_percent=100)` — full close on every below-zero bar, same execution. `Bull`/`Bear` are mutually exclusive on every bar by construction (`curve` cannot be both strictly above and strictly below zero), so no bar can ever fire entry and close together — no same-bar ordering ambiguity exists anywhere in this record. The measure-zero edge `curve == 0` fires neither leg (pinned: both strict comparisons fail) and the position simply holds — stated, not patched.
- Risk legs (pinned arithmetic, not invented): the `strategy.exit(id="Long Trail Stop", stop=longStopPrice)` leg ships with default `Trail Long Loss (%) = 100`, so `stopValue = close * (1 − 1.00) = 0` and `longStopPrice = max(0, prior) = 0` on any positive-price asset — the stop rests at zero and can never trigger. The derived posture is therefore explicitly no stop, no target, no trailing, no time exit — pinned as written arithmetic, never hidden, never a researcher removal.
- Direction: long/flat single side. No short entry ships anywhere (the short side is explicitly absent, not omitted by accident). Before the first above-zero bar the system is flat (no position by construction).
- Display isolation: the 3 `hline` bands and the single `plot(curve)` render only and cannot change any order.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (sole series read by `roc(close, ...)` in the derived record). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line. The source's SPY-daily `security()` dependency is removed by the predeclared port — the derived record has no multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision timeframe `1d` (source-native per the page-embedded `period: 1d` header; `basePeriod: 1h` equals native 1h execution granularity — 24 1h bars per 1d bar on a 24/7 venue — and with market-entry/full-close legs only plus an arithmetic no-op stop, no intrabar path exists for the base to affect). The order logic makes no live `request.*` call, so it is single-frame by construction.
- Warmup: the ROC windows need 14 completed `1d` bars and the WMA smoothing needs 10 bars of summed output on top. The adopted warmup is the first 50 completed `1d` bars flat by record rule (predeclared researcher choice — covers 14 + 10 plus seeding margin); no signal before bar 51 may trade. No repainting (`roc`/`wma` read only completed closes), no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (source venue is already `Futures_Binance BTC_USDT` on the source-native `1d` frame — naming normalization to `BTCUSDT` is the only market change; the signal-series port SPY→BTCUSDT is the predeclared derivation, never presented as source-native).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar-open (no execution-timing argument ships anywhere); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with mutually exclusive state legs and a never-triggering stop, there is no same-bar ordering ambiguity of any kind.
- Sizing/capital/costs: the source ships only the `$10k` cash/10000-capital header sizing with no commission, fee, slippage, margin, or funding assumption — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed — the source declares no funding treatment at all) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: no `pyramiding` ships anywhere, pinning the language default of no same-direction adds — at most one unit under the fixed order ID `Long`; `if (Bull)` refires while already positioned are no-ops; re-entry is allowed immediately on the next above-zero bar after a flat exit (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. Long-only: no margin short is ever required.

## Evidence

### Source-reported

The mirror ships the full construction (SPY-daily `security()` feed line, 10/14/11 inputs, `wma(roc + roc)` decomposition, `Bull = curve > 0` / `Bear = curve < 0` state definitions, fixed `Long` order ID, long-entry plus full-close legs, the 100%-default trail-stop block, the `Coppock Curve` title), the page-embedded 1d/1h Oct→Nov-2023 backtest header, and the bilingual zero-cross prose. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: 0 `strategy.order`, and the single shipped `strategy.exit` leg rests at stop-price zero by default arithmetic (`close × (1 − 1.00) = 0`, `max` never lifts it on positive prices) — the sole position-closing path is the `strategy.close` on `curve < 0`. The absence of any live stop is coded arithmetic, disclosed, not a tunable parameter here.
2. State-held exposure, admitted plainly: once `curve` turns positive the system holds the long on every subsequent above-zero bar until a sub-zero bar — there is no stop, no target, no time-stop. A market that grinds sideways just above zero holds full exposure through the chop; adverse excursion after entry has no guardrail of any kind. This is the coded trade, disclosed, not a tunable parameter here.
3. Lag at regime births: the signal smooths an already two-window-derived series (ROC 11 + ROC 14, then WMA 10) — a sharp V-recovery must drag the smoothed sum across the full zero gap before any trigger prints, so entries arrive strictly after the turn by code. The lag is the coded smoother, disclosed, not shortened.
4. Source basis fenced: the source trades BTC off SPY's daily Coppock curve (equity-crypto proxy basis — disclosed, never adopted). The derived record spends the identical formula on BTCUSDT's own closes instead; any divergence between SPY-signal timing and self-signal timing belongs to the predeclared port, and this record is therefore never evidence that the original SPY-proxy source itself passes.
5. Derivation boundary fenced: the only non-source-native behaviors in this record are the SPY→BTCUSDT signal-series port, same-bar-close fills, the adopted 50-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; lengths, operators, the zero-level state triggers, the `if (Bull)` / `if (Bear)` exclusivity, the `curve == 0` hold edge, the order ID, long/flat handling, and the arithmetic no-stop posture are source-verbatim. This record is therefore never evidence that the original next-bar-open SPY-proxy source itself passes.
6. The `10` / `14` / `11` literals, the strict state definitions (not touch, not cross-edge), the full-quantity close, the long-only stance, and the no-stop/no-target/no-cooldown stance are pinned, not removed: retuning any length, converting state-holding into edge-crossing, adding a stop/target/filter/cooldown/gate, adding a short leg, or exiting partially instead of in full would each be a different, unpinned rule — none is admitted here.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `10/14/11` / close-only ROC-sum WMA / strict zero-state legs / long/flat / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — State relevance: replacing the zero-state posture with passive buy-and-hold over the same evaluation window must not improve net expectancy; fail ⇒ the zero-state gate adds nothing over holding the market.
- F2 — Smoothing relevance: replacing the smoothed `wma(roc14 + roc11, 10)` with the raw summed ROC sign (`roc14 + roc11 > 0` long, `< 0` flat) must not improve net expectancy; fail ⇒ the 10-bar WMA smoothing adds nothing over the raw momentum sum.
- F3 — Parameter relevance: replacing the pinned `10/14/11` triple with any adjacent classic triple must not improve net expectancy; fail ⇒ the pinned defaults carry no advantage over neighboring smoothings and the record's literal choice is arbitrary.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision frame source-native `1d`; signal series ported from the SPY-daily feed — predeclared). The close-only arithmetic ports across perpetual venues without structural change. Long-only flat-capable: no margin short is ever required, so a spot-only deployment expresses the identical event set. No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no `time(` gating anywhere), so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Signal-series port: the source signal is SPY-daily closes; the derived signal is BTCUSDT-`1d` closes. Momentum-regime timing of an equity index and a crypto perpetual differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- Derived fill timing: the source fills next-bar-open on a 1d-decision/1h-base backtest; this record executes same-bar-close on `1d` BTCUSDT perpetual. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden.
- No price stop, no time stop, no short side: adverse excursion after entry has no guardrail beyond the sub-zero flat exit, which may arrive many bars later or after deep excursion; a market that trends against the position without printing `curve < 0` is held indefinitely; sub-zero upside drift is sat out flat. This is the coded posture, disclosed as the record's principal risk.
- No source cost declaration: no capital beyond the `$10k` cash header, no sizing beyond it, no commission, fee, slippage, margin, or funding assumption ships anywhere in the source — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Venue naming only: the source venue is already `Futures_Binance BTC_USDT`; the derived venue is Binance `BTCUSDT` perpetual. Microstructure, tick size, fee, and funding differences are carried by the house overlay — no equivalence is claimed.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- FMZ canonical strategy page (ChaoZhang): https://www.fmz.com/strategy/431926
- Immutable mirror file at pinned commit `7853bb2bf262c4567ac238d3552d97f0e50cb801` (blob `6d089ff76f0da59991cbfef609df5ef3c6ba9bbb`, 6790 bytes): https://github.com/fmzquant/strategies/blob/7853bb2bf262c4567ac238d3552d97f0e50cb801/%E5%9F%BA%E4%BA%8ECoppock%E6%9B%B2%E7%BA%BF%E7%9A%84%E9%87%8F%E5%8C%96%E4%BA%A4%E6%98%93%E7%AD%96%E7%95%A5Coppock-Curve-Based-Quantitative-Trading-Strategy.md
- Pine strategy semantics (order calls, default execution, v4 built-ins): https://www.tradingview.com/pine-script-reference/v4/
