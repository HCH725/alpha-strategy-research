---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Dual Thrust open-range breakout reversal two-sided on BTCUSDT 1d bars
created: 2026-10-10
updated: 2026-10-10
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2023-09-19
sources:
  - https://www.fmz.com/strategy/427267
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Dual Thrust open-range breakout reversal two-sided on BTCUSDT 1d bars

## Provenance

Primary source read end to end (canonical FMZ page fetched over HTTPS during this cycle):

- Canonical page: https://www.fmz.com/strategy/427267 (page title `Dual Thrust Strategy | FMZ`, bilingual body `双轨突破策略|Dual Thrust Strategy`, `Created: 2023-09-19 16:27:12` — adopted as `source_as_of`). Fetched during this cycle (768565 bytes): the page states the rule in both languages (highest high HH and lowest low LL over the recent N bars; highest close HC and lowest close LC; Range is the larger of HH-LC and HC-LL; BuyLine is opening price plus k1*Range; SellLine is opening price minus k2*Range; go long when close breaks above BuyLine; go short when close breaks below SellLine), the `/*backtest ... */` header (`start: 2023-09-11 00:00:00`, `end: 2023-09-18 00:00:00`, `period: 10m`, `basePeriod: 1m`, `exchanges: [{"eid":"Futures_Binance","currency":"BTC_USDT"}]`, each marker byte-present twice on the page), and the strategy header (`strategy("Dual Thrust Strategy",overlay=true,initial_capital=1000)`). Word-boundary counts over the whole landing HTML: `Net Profit` 0, `Sharpe` 0, `Win Rate` 0, `Total Profit` 0 — the page ships no performance numbers of any kind. The author handle is not exposed in the fetched static HTML (author-dependent API fields render client-side); no publisher claim is made beyond the canonical URL and Created stamp.
- Text census over the pinned Pine v3 block: 1 `strategy(` / 0 `study(` / 2 `strategy.entry` (`"enter long"` long on `LongCondition`, `"enter short"` short on `ShortCondition`) / 0 `strategy.exit` / 0 `strategy.close` / 0 `strategy.order` / 0 `stop=` legs / 0 `limit=` legs / 4 `input(` declarations (`k1 = 0.67`, `k2 = 0.62`, `TimeFrame = '240'`, `len = 20` — each value confirmed both in the code block and in the page's `Strategy parameters` argument table `v_input_1..4`) / 1 `crossover(` (`LongCondition=crossover(close,BuyLine)`) / 1 `crossunder(` (`ShortCondition=crossunder(close,SellLine)`) / 4 `security(` calls (HH/LC/HC/LL on the `TimeFrame` with `barmerge.lookahead_off`; BuyLine/SellLine on `"D"` open with `barmerge.lookahead_off`) / 0 `process_orders_on_close` (Pine default governs, recorded as source-declared-by-default) / 0 `pyramiding` (default `0` governs, recorded likewise) / 0 `calc_on_every_tick` (default `false` governs). Full rail lines read verbatim: `Range=max(HH-LC,HC-LL)`, `BuyLine=<daily open>+k1*Range`, `SellLine=<daily open>-k2*Range`.
- The classic Dual Thrust reversal posture is stated on the page's own lineage (the MyLanguage sibling FMZ 169230 states it explicitly: "a reversal system with no separate stop loss … the reverse signal is also the closing signal") and matches the pinned code exactly: the only position-changing paths are the two opposite entries; no stop, target, trailing, or time leg ships anywhere in executable form.
- Page performance language is absent entirely (no table, figure, or number) — this record claims no source-reported performance and no reproduced performance.

Licence and rights: the canonical page is a public FMZ strategy publication with no licence header in the artifact. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly five: (1) research market/timeframe BTCUSDT `1d` single-frame (the script's `240`-minute `security` frame plus daily-open rail plus `10m`/`1m` FMZ-platform execution is FMZ-platform timing, not HB-modelable source timing — the `TimeFrame` input is superseded by the derived frame; same port rationale as the admitted OBV record, whose source block was `1h`/`15m`); (2) same-bar-close fills on completed-bar decisions (the Pine block ships no `process_orders_on_close`, so its default timing is next-bar-open — this record does not claim source timing); (3) an adopted 100-bar warmup with pre-warmup bars flat by record rule (the len-20 leg needs 20 completed bars; 100 covers seeding plus the range transient with margin — see Required data); (4) house sizing/capital/costs replacing the block's `initial_capital=1000` placeholder (see Execution assumptions; the Pine no-pyramiding default is preserved as the single-position rule); (5) the two rails are computed from the same `1d` frame's prior completed bars plus the current bar's open (the source rails read a `240`-minute frame and a daily open — this record does not claim identical multi-frame paths, only the same pinned literals, formula shape, strict cross edges, and reversal posture). Formula shape, k1/k2/len literals, strict cross-edge definitions, both entry IDs, the reversal-only exit posture, two-sided direction, and every no-stop/no-target/no-trailing/no-time exclusion are source-native and unmodified.

Pre-write dedup (2026-10-10): working-tree case-insensitive searches for `dual.thrust`, `BuyLine=<daily-open>`, `SellLine`, and `427267` return zero strategy records using any open-anchored dual-rail construction — the single `buyline/sellline` hit is the Chande-momentum record's oscillator thresholds (`buyline = -80`, `sellline = +80` on a ChandeMO oscillator, unrelated mechanism); `427267` and `Dual Thrust` return zero titles. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Five-axis distinction: mechanism differs (open-anchored dual-rail breakout `open +/- k*max(HH-LC,HC-LL)` — the pool's Donchian record breaks the raw highest-high/lowest-low channel with no open anchor and no range-max construction; the Darvas/NR7/Keltner records are box, contraction, or ATR-envelope constructions; SuperTrend/Chandelier/SSL are ATR- or MA-channel trailing flips), signal construction differs (close crossing an open-offset rail pair with asymmetric k1/k2, versus oscillator crosses, price-EMA crosses, or band touches), exits differ (pure reversal-only with explicitly no stop/target/trailing/time leg — no pool breakout record shares this exact risk posture on this construction), source identity differs (FMZ 427267, Sep-2023, versus other FMZ IDs or TV authors), and direction handling differs (two-sided reversal system, always-in-market after the first signal with an explicit pre-first-signal flat state, versus long-only breakout holders).

## Economic mechanism

### Source-reported

Opening-range breakout capture (mirror title `Dual Thrust Strategy`): the day's opening price anchors two rails set from the recent volatility range, going long on upside breakouts and short on downside breakouts to ride the trend that forms around the open. The bands adapt automatically to historical volatility (no subjective levels), the asymmetric k1/k2 suit products with different up/down volatility, and the breakout shape is claimed to carry relatively high signal quality. Holding is flexible across trend horizons.

### Research interpretation

Open-anchored volatility-breakout holding with a reversal-only book, two-sided. Unlike the pool's Donchian record (which breaks the raw highest-high/lowest-low channel and holds long-only), this system never buys a level — it buys distance from the open: a slow grind that never prints a fresh N-bar high fires nothing here, while a single explosive day that gaps the open-relative distance fires immediately even with no channel extreme touched. Unlike ATR-envelope trailers (SuperTrend/Chandelier/UT-Bot in pool and queue), the rails reset every bar from the current open rather than trailing behind price, so chop around the open whipsaws the full unit while a sustained drift is ridden without any trailing give-back parameter. Unlike oscillator-cross systems it reads no normalized momentum at all — only raw range geometry. The bet is on multi-day open-relative expansion persistence at the ~weeks scale under the 20-bar structural leg, not on any price level, band, calendar effect, or volume flow.

## Signal

Exact rule as pinned (k1 0.67, k2 0.62, len 20, strict edges — any other value is a different, unpinned rule):

- Lines (pinned shape, derived single frame): on each completed `1d` bar `t`, over the 20 prior completed bars (`t-20..t-1`): `HH[t] = highest(high, 20)`, `LL[t] = lowest(low, 20)`, `HC[t] = highest(close, 20)`, `LC[t] = lowest(close, 20)`; `Range[t] = max(HH[t]-LC[t], HC[t]-LL[t])`; `BuyLine[t] = open[t] + 0.67*Range[t]`; `SellLine[t] = open[t] - 0.62*Range[t]` (the source `security(...,barmerge.lookahead_off)` completed-bar semantics are preserved: no rail reads the forming bar's high/low/close, and the open leg reads only the current bar's already-printed open).
- Entry long: `long_event = crossover(close, BuyLine)` (strict: `close[t-1] <= BuyLine[t-1]` and `close[t] > BuyLine[t]`) while flat → buy-open long at the same-bar close under the derived declaration.
- Entry short: `short_event = crossunder(close, SellLine)` (strict mirror) while flat → sell-open short at the same-bar close.
- Reversal: a contra-side event while positioned closes the full unit and opens the full contra unit at the same single close price (one net fill step — the Pine `strategy.entry("enter short")`-while-long reversal mapped onto the derived fill; no same-bar ordering ambiguity exists because entry, reversal, and close share one decision price, and the two events are mutually exclusive by construction since `BuyLine[t] >= SellLine[t]` always).
- Same-side refire while positioned is a no-op (Pine default no-pyramiding preserved as the single-position rule); pre-first-signal flat by construction (no position exists before the first event).
- Direction: two-sided reversal system — always-in-market after the first signal (long or short), flat only before the first signal.
- Risk legs (pinned absences, not invented): 0 `strategy.exit`, 0 `strategy.close`, 0 `stop=` legs, 0 `limit=` legs — no stop-loss, no take-profit, no trailing, no time exit anywhere in the block. The sole position-closing path is the opposite entry reversing the unit. This is the coded posture pinned as written (declared explicitly, never hidden), not a researcher invention.
- Display/plumbing isolation: the two `plot(` legs (`offset=1`) render only and gate no order; the two `plotshape(` legs are gated on `strategy.position_size` display conditions and open no position; the two `alertcondition(` legs mirror the entry conditions and route no order.

## Required data

- Completed `1d` bars of BTCUSDT: `open` (rail anchor of the decision bar), `close` (cross comparison), `high`/`low` (inside the 20-bar HH/LL extremes only). No funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (declared research frame per the derivation; the script's `240` input is superseded — the derived strategy is single-frame by construction).
- Warmup: the len-20 leg needs 20 completed `1d` closes before HH/LL/HC/LC are statistically settled; the range-max transient needs no extra structure beyond seeding. The adopted warmup is the first 100 completed `1d` bars flat by record rule (predeclared researcher choice — 5× the structural length, covering seeding plus the early-range transient with margin). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar; every `security` semantic preserved as completed-bar-only (`lookahead_off`).

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (declared port; the source venue `Futures_Binance BTC_USDT` names no separate spot/perp/margin layout — no cross-venue equivalence claimed beyond the same manufacturer venue family).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution for entries and reversals, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar-open on a `10m`-decision/`1m`-base FMZ backtest (no execution-timing override ships anywhere); this record does not claim source fills. No maker-touch, queue, or intrabar-path-dependent fill: with one decision price per bar and mutually exclusive events, there is no same-bar entry ordering ambiguity.
- Sizing/capital/costs: the block's `initial_capital=1000` ships no portable economics — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) replace it here, never presented as source-native behavior.
- Concurrency: at most one position (long or short) at any time after the first signal; the opposite event reverses in full in one step; no cooldown specified — explicitly none, not invented. Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic. The short leg requires margin-short permission, realistic on the pinned perpetual venue.

## Evidence

### Source-reported

The page ships the full construction (k1/k2/TimeFrame/len inputs with pinned defaults, the four `security` rail lines, the `Range=max(HH-LC,HC-LL)` line, the BuyLine/SellLine rail lines, the strict cross pair, the two entry IDs, the plotted rails, and the September-2023 `10m`/`1m` Binance backtest header), the title stamps, and the Created stamp. It ships zero performance numbers: no return, no win rate, no profit factor, no trade count, no Strategy Tester table or figure — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No risk layer of any kind, admitted plainly: 0 `strategy.exit`, 0 `strategy.close`, 0 `stop=`/`limit=` legs — a trend that reverses slowly without ever printing a contra-side cross is ridden all the way back, and a vertical adverse move on the entry bar itself has no guardrail. This is the coded posture, disclosed, not a tunable parameter here.
2. Open-anchor whipsaw, admitted plainly: the rails reset from every bar's open, so chop oscillating around the open prints alternating raw crosses that flip the full unit bar after bar (with no stop or cooldown to dampen it). Tightening either k would be a different, unpinned rule — none is admitted here.
3. Range-zero edge, admitted plainly: 20 identical bars make `Range = 0`, so `BuyLine = SellLine = open[t]` and the system degrades to a pure close-vs-open cross (long on up-close, short on down-close). Structural, disclosed, and unencounterable on `1d` BTCUSDT outside a venue outage.
4. Asymmetry boundary fenced: k1 (0.67) exceeds k2 (0.62), so the long rail sits fractionally further from the open than the short rail — shorts trigger on slightly smaller expansions. Symmetricizing or retuning either k would be a different, unpinned rule — none is admitted here.
5. Derivation boundary fenced: the only non-source-native behaviors in this record are the BTCUSDT-`1d` single research frame (superseding the `240` input and the daily-open rail basis), same-bar-close fills, the adopted 100-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; k1, k2, len, the range-max formula shape, strict cross edges, both entry IDs, the reversal-only exit posture, two-sided direction, the pre-first-signal flat state, and every no-stop/no-target/no-trailing/no-time exclusion are source-verbatim. This record is therefore never evidence that the original multi-frame FMZ deployment passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: k1 0.67 / k2 0.62 / len 20 / range-max formula / strict cross edges / full-unit reversal / no-stop-no-target-no-trailing-no-time / two-sided / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Rail relevance: replacing the open-anchored rails with raw Donchian-channel breaks (long on close above prior-20 highest high, short on close below prior-20 lowest low, same reversal-only book) must not improve net expectancy; fail ⇒ the open anchor plus range-max construction adds nothing over a plain channel breakout.
- F2 — Asymmetry relevance: symmetricizing the rails (k1 = k2 = 0.62, long rail pulled to the short distance) must not improve net expectancy; fail ⇒ the source's long-further asymmetry adds nothing over symmetric rails.
- F3 — Reversal relevance: replacing the always-in-market reversal book with a flat-after-signal book (each event opens a unit that is held until the contra event closes it flat, re-entering only on the next same-side event) must not improve net expectancy; fail ⇒ staying perpetually exposed adds nothing over signal-and-hold episodes.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (declared port of an FMZ Binance-futures source context). The OHLC arithmetic ports across perpetual venues without structural change; both sides are explicit legs, so a spot-only deployment expresses the long half unchanged while the short half stays venue-gated (short permission unused, never silently converted). No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read beyond the bar's own printed open, so session-gap behavior needs no approximation. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived frame and fill timing: the source computes rails on a `240`-minute frame with a daily-open anchor and fills next-bar-open on a `10m`-decision/`1m`-base Binance backtest; this record computes rails on `1d` bars from the same-bar open and executes same-bar-close. Backtest economics of the two framings, timings, and venues differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source configuration's performance.
- No source cost declaration beyond an `initial_capital=1000` placeholder: no fee, slippage, or funding assumption ships anywhere usable — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- Always-in-market exposure: after the first signal the book is never flat by code, so adverse drift between crosses is held in full — long unhedged stretches are the coded trade, disclosed, not smoothed.
- Scale selectivity: len-20 rails on `1d` bars describe multi-week expansion geometry, so the system fires infrequently and spends long stretches positioned through chop — long idle/adverse stretches are the coded trade, disclosed, not smoothed.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- FMZ canonical strategy page (Created 2023-09-19 16:27:12): https://www.fmz.com/strategy/427267
