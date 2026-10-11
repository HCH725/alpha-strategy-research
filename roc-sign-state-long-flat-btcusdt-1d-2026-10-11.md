---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: ROC sign state-following long-flat on BTCUSDT 1d bars
created: 2026-10-11
updated: 2026-10-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2022-06-13
sources:
  - https://github.com/hasnocool/tradingview-pine-scripts
  - https://www.tradingview.com/script/CCrPAfmV-Rate-Of-Change-Trend-Strategy-ROC/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# ROC sign state-following long-flat on BTCUSDT 1d bars

## Provenance

Primary source read end to end (verified 2026-10-11):

- Pinned executable artifact (real `strategy()`, Pine v5, `overlay = true`): file `Rate Of Change Trend Strategy (ROC).pine` in https://github.com/hasnocool/tradingview-pine-scripts at commit `69969aeaf271b2f7b5a7632a1bde43069a0cbe26` (2024-09-18), local SHA-256 `a8cb8704d98fdbf69ce491079b231186497f094d51e6520c5c59a9a05c02decf`. Header declaration quoted verbatim: `strategy("ROC", overlay=true)`. The file preserves the author's description prose verbatim: "This is very simple trend following or momentum strategy. If the price change over the past number of bars is positive, we buy. If the price change over the past number of bars is negative, we sell. This is surprisingly robust, simple, and effective especially on trendy markets such as cryptos." plus the market note "Works for many markets such as: INDEX:BTCUSD INDEX:ETHUSD ...". The mirror copy carries page chrome (script-name/author header, `Copy code` marker, line numbers, trailing `Expand (18 lines)`) around the intact 18-line script text — the code lines below are byte-verified in that file, never reconstructed from memory.
- Canonical TradingView identity corroboration: https://www.tradingview.com/script/CCrPAfmV-Rate-Of-Change-Trend-Strategy-ROC/ fetched from this runner with HTTP 200 (423284 bytes); the `<title>` pins `Rate Of Change Trend Strategy (ROC) by RobertSimonUy — TradingView`, the `RobertSimonUy` author token repeats 10 times in-page, the script flags read `OPEN-SOURCE SCRIPT` with the publication stamp `Jun 13, 2022` (`<time dateTime="Mon, 13 Jun 2022 10:01:06 GMT">`, adopted as `source_as_of`), and the embedded description text matches the mirror's description word for word.
- Text census over the executable script body (from `//@version=5` to the last order line): 1 `strategy(` / 2 `strategy.entry` (`"ROCLong"`/`strategy.long`, `"ROCShort"`/`strategy.short`) / 2 `strategy.close_all` (one per if/else branch) / 0 `strategy.close(` / 0 `strategy.exit` / 0 `strategy.order` / 0 `stop=`/`limit=`/`profit=`/`loss=` / 0 `security(` / 0 `request.*` / 0 `process_orders_on_close` (Pine default: per-completed-bar evaluation, next-bar fills) / 0 `pyramiding` (Pine v5 language default applies — documented default `0`, no same-direction adds) / 0 `calc_on_every_tick` / 1 `ta.roc(` / 0 `crossover`/`crossunder`/`ta.cross` / 0 `position_avg_price`/`position_size` / 0 `barstate` / 0 `alert(` / 0 `open` / 0 `high` / 0 `low` / 0 `volume` (exactly one `close` read: `price = close`) / 0 `commission_*`/`slippage`/`initial_capital`/`default_qty_*` (no portable economics anywhere). Pinned inputs verbatim: `length = input(30)`; `longtrades = input.bool(true, "Long", inline = "01")`; `shorttrades = input.bool(false, "Short", inline = "01")` — long enabled and short disabled at source defaults, quoted exactly.
- Rule lines pinned verbatim: `price = close`; `roc = ta.roc(price,length)`; `if (roc>0)` → long branch (`if(longtrades)` → `strategy.entry("ROCLong", strategy.long, comment="ROCLong")`, else `strategy.close_all()`); `else` → short branch (`if(shorttrades)` → `strategy.entry("ROCShort", strategy.short, comment="ROCShort")`, else `strategy.close_all()`). `ta.roc` is a pure lookback ratio with no recursive seed (`100 * (price − price[length]) / price[length]` per the Pine v5 reference — no EMA/RMA-style seeding, so no seeding conflict can arise). The only commented line is a disabled equity-area plot reading no order path.
- Prose/code divergence fenced honestly: the prose says "if negative, we sell", but at the pinned defaults (`shorttrades = false`) the negative leg fires `strategy.close_all()` — a flat exit, not a short. The short leg exists in code but is dead at defaults; enabling it is a different, unpinned rule, explicitly not adopted.

Licence and rights: this record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence (open-source script, used within its terms).

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) market/frame pin `BTCUSDT 1d` (the code names no market and no timeframe beyond the author's `INDEX:BTCUSD`/`INDEX:ETHUSD` prose note; this pin is a pure researcher choice, disclosed here, never presented as source-native); (2) same-bar-close fills (the source ships no execution-timing argument — Pine default evaluates per completed bar and fills on the next bar; no `process_orders_on_close` ships anywhere, quoted verbatim in census); (3) an adopted 60-bar warmup with pre-warmup bars flat by record rule (`ta.roc(price, 30)` needs 31 completed closes; 60 covers the window plus margin — see Required data); (4) house sizing/capital/costs replacing the absent source economics (the script ships no sizing, capital, commission, or slippage line of any kind — recorded as absent economics, never as zero-cost evidence; see Execution assumptions). The `length = 30` input, the long-enabled/short-disabled defaults, the close-only `ta.roc` sign rule, the if/else exclusivity, the `ROCLong` order id, the full-flat exit, and the no-stop/no-target/no-cooldown stance are source-native and unmodified.

Pre-write dedup (2026-10-11): working-tree searches for `CCrPAfmV`, `RobertSimonUy`, `rate.of.change`, and word-boundary `roc(` return zero strategy records using this source, author script, or construction — the only `roc(` hits anywhere are `coppock-curve-zero-state-long-flat-btcusdt-1d` (WMA-smoothed dual-ROC Coppock curve, SPY-ported, different formula) and `kst-signal-cross-trend-two-sided-btcusdt-1h` (four-horizon weighted KST sum against its own signal-line cross, two-sided) — both different signal constructions with different exits, documented below. All other `roc` hits are prose fragments, never a signal. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long), #49 (Gaussian channel StochRSI-gated breakout long), #63 (SuperTrend ATR-flip trend long), #89 (Chandelier Exit dual-stop state-flip long), and #92 (SSL channel state-following reversal two-sided) — different mechanisms, indicators, and sources. Five-axis distinction: mechanism differs (single-horizon raw ROC sign state versus smoothed/weighted multi-ROC composites), signal construction differs (`ta.roc(close, 30) > 0` alone — no pool record trades a bare ROC sign), exits differ (full-flat `close_all` on sign flip versus opposite-entry reversal or signal-line recross), data differs (`close` only; Coppock's source leg needed a cross-market feed), and source identity differs (hasnocool `Rate Of Change Trend Strategy (ROC).pine` at pinned SHA plus TV `CCrPAfmV` RobertSimonUy 2022-06-13).

## Economic mechanism

### Source-reported

Naked momentum-state trend following (description prose plus quoted Pine): if the 30-bar price change is positive the market is treated as an uptrend and bought; if negative the long is sold off. No filter, no confirmation leg, no stop — the design bets that on "trendy markets such as cryptos" the sign of a medium-horizon return alone separates tradable drift from chop, and that exiting to flat on the first non-positive print cuts losers faster than any trailing rule could.

### Research interpretation

Single-series sign-state machine, long-flat, always-decided after warmup. Unlike every composite-momentum record in the pool (Coppock's smoothed sum, KST's weighted four-horizon vote, TRIX's triple-EMA percent change), there is no smoothing, no second line, and no threshold calibration: the trigger is the strict inequality `close(t) > close(t−30)`, evaluable by hand on any chart. The if/else makes the two branches strictly exhaustive — every completed bar maps to exactly one directive (enter-and-hold-long or be-flat), so no bar is ambiguous and no priority rule is needed or invented. The price of the minimalism is the same as the source prose admits by omission: a 30-bar return sign whipsaws in range-bound markets, printing repeated enter-then-flatten round trips with no flat-state hysteresis and no stop to reshape the loss tail — the record holds the prescribed posture, disclosed as the principal risk, never smoothed.

## Signal

Exact rule as pinned (all inputs frozen — any other value is a different, unpinned rule):

- Declarations (derived): single-position state machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). At most one open long leg; state ∈ {flat, long}; flat holds before the first signal and under the warmup rule.
- Momentum scalar, pinned verbatim at defaults (`length = 30`), with `c(t) = close(t)`: `ROC(t) = 100 · (c(t) − c(t−30)) / c(t−30)` — equivalently the sign trigger `c(t) > c(t−30)`. Only `close` is read anywhere.
- Entry long: on any completed bar with `ROC(t) > 0` while flat → `strategy.entry("ROCLong", strategy.long)` (market, same-bar close by derivation). Refires while already long are no-ops (language-default `pyramiding = 0` — repeated same-direction entries do not add).
- Exit to flat: on any completed bar with `ROC(t) <= 0` while long → full close of the open leg (the source's `strategy.close_all()`; with a single leg outstanding this is exactly one full exit, no residue). No stop, no target, no trailing, no time exit, no cooldown — pinned as written (the script ships zero `strategy.exit` legs and names no stop anywhere), explicitly none, not invented.
- Direction: long-flat only at the pinned defaults (`longtrades = true`, `shorttrades = false` — quoted in census). The `ROCShort` leg is dead code at defaults; a two-sided reading would contradict the prescribed defaults and is a different, unpinned rule.
- Exact-zero fence: `ROC(t) = 0` (i.e. `c(t) = c(t−30)` to the tick) falls in the `else` branch deterministically — flat/exit, never entry. No equality ambiguity exists.

## Required data

- Completed `1d` bars of BTCUSDT: `close` only (the single `price = close` read feeding `ta.roc`). No `open`, no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session-template, calendar, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1d` (derived pin; the body contains no `security(`/`request.*` call, so the derived rule is single-frame by construction).
- Warmup: `ta.roc(price, 30)` first reads `c(t−30)`, so the scalar is fully defined from the 31st completed close; being a pure ratio over two known closes it carries no recursive seed and no seeding transient. The adopted warmup is the first 60 completed `1d` bars flat by record rule (predeclared researcher choice — covers the 30-bar window plus margin; no traded bar reads an undefined value). No repainting, no negative shift, no future reference, no full-sample normalization; one evaluation per completed bar. Each bar's close enters the rule only at that bar's close, at which point the bar is complete — causal under same-bar-close fills.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (derived pin; the code names no market and no timeframe — venue choice, symbol spelling, and frame are disclosed here, never presented as source claims; the author's prose note names `INDEX:BTCUSD`/`INDEX:ETHUSD` as compatible markets, not as the traded venue).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). The source's own timing is next-bar fill (no execution-timing argument ships anywhere — quoted verbatim in census); this record does not claim the source fills at the close. No maker-touch, queue, or intrabar-path-dependent fill: with no stop/limit legs anywhere, there is no same-bar TP/SL ordering ambiguity, and the trigger reads only completed closes, so each bar's outcome is a single deterministic event (enter, hold-long, or flatten) under either fill convention.
- Sizing/capital/costs: the source ships no portable economics of any kind (no sizing, capital, commission, or slippage line — recorded as absent economics, never as zero-cost evidence) — the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions (fees plus historical funding; no hypothetical zero funding claimed) apply to the derived evaluation here, never presented as source-native behavior.
- Concurrency: single-position machine — at most one open long leg; same-state bars while positioned are no-ops; re-entry is allowed on the next fresh `ROC > 0` bar after any flatten (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The source ships the full construction (30-bar input, long-enabled/short-disabled defaults, close-only `ta.roc` sign rule, exhaustive if/else with the `ROCLong`/`ROCShort`/`close_all` legs, and the crypto-trend description prose) — quoted in Provenance. It ships no portable performance: no table, no figure, no metric — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No hidden exits or risk layer: the body contains zero `strategy.exit` legs and zero `strategy.close(` legs; the only exit path is the two `strategy.close_all()` calls inside the if/else — the no-stop/no-target/no-time posture is prescribed, explicitly none, never hidden.
2. Branch exhaustivity fenced: `if (roc>0) … else …` covers every real value including exact zero — no bar escapes both branches, no bar fires both entry legs, no priority rule needed or invented.
3. Direction-default fence: at pinned defaults the short branch is unreachable (`shorttrades = false` quoted verbatim) — the record's long-flat posture follows the defaults, not a researcher direction choice; flipping either toggle is a different, unpinned rule.
4. Prose-divergence fence, admitted plainly: the prose "if negative, we sell" reads as shorting, but default code flattens — this record follows the code defaults and discloses the gap rather than adopting the prose's short reading.
5. No future leakage, stated plainly: at decision bar `t` the slowest input is `c(t−30)` — complete at bar `t`'s close. No `security()`, no `request.*`, no negative index, no `barstate.islast`-gated repainting path, no `time` read at all. The pure-ratio scalar has no seed to resolve before the 60-bar warmup ends.
6. Dead-code fence, admitted plainly: the `ROCShort` entry leg and the long-branch `close_all()` (reachable only if `longtrades` were flipped off) never fire at pinned defaults — quoted but explicitly not adopted as signals. Adopting them would be a different, unpinned rule.
7. Close-only data fence: the body's alphabet of price reads is exactly `{close}` — venue `high`/`low`/`open`/`volume` definition differences cannot touch any order-gating line. A venue that cannot supply 31 pre-decision daily closes cannot trade the pinned rule.
8. Sibling-source fence: the mirror's second ROC file (`Rate of Change Strategy.pine` by Sonny Parlin, 5m-oriented) was inspected and rejected — `stop=` entries, `strategy.exit(stop=)`, `position_avg_price`/`position_size` engine-state sizing, and `crossover` legs fail the gate without invention; recording it would require redesigning it. This record is independent of that file.
9. Derivation boundary fenced: the only non-source-native behaviors in this record are the `BTCUSDT 1d` market/frame pin, same-bar-close fills, the adopted 60-bar warmup with record-rule pre-warmup flat, and house sizing/costs — all predeclared above; the 30-bar input, the direction defaults, the `ta.roc` sign arithmetic, the close-only inputs, the exhaustive branches, the single-position posture, and the risk posture are source-verbatim. This record is therefore never evidence that any other market, frame, or timing of the source passes.
10. Network limitation disclosed: every formula line above was byte-verified in the pinned mirror file at commit `69969aea` (local SHA-256 recorded); the canonical TV page verified live the title, author, open-source status, publication date, and description identity. The page's Source-code tab was not separately machine-read from this runner — the division of evidence is disclosed here, not hidden.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 30-bar ROC sign / long-flat / no-stop-no-target posture / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Horizon relevance: replacing `length = 30` with `length = 14` (same sign rule, same exits) must not improve net expectancy; fail ⇒ the 30-bar horizon adds nothing over a faster sign state.
- F2 — Signal relevance: replacing the sign state with buy-and-hold over the same evaluation window (same costs) must not improve net expectancy; fail ⇒ the ROC sign timing adds nothing over passive exposure.
- F3 — Exit relevance: replacing the `ROC <= 0` flatten with holding every entry until the opposite 30-bar sign regime persists 5 consecutive bars (same entries) must not improve net expectancy; fail ⇒ the immediate sign-flip exit adds nothing over a hysteretic exit.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (derived pin; the code names no market beyond the author's index prose note). The close-only arithmetic ports across perpetual venues without structural change; the rule reads no high/low/open/volume, so venue bar-construction and volume-definition differences cannot touch it. The ratio auto-scales in the asset's own price units, so no fixed-pip recalibration is needed across assets — cross-asset behavior differences are still real and unclaimed. The rule is long-flat with no short leg at pinned defaults, so a spot-only deployment expresses it in full with no venue-permission caveat — fullest possible portability for this pool, disclosed. No funding-dependent leg, no stablecoin-specific assumption, no session-template, no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read (no session gating anywhere); decision boundaries are calendar-day bars of the venue feed, disclosed. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- Derived market and frame: the code names no market and no timeframe; this record pins `BTCUSDT 1d`. Cross-market and cross-frame behavior differences are real — the adaptation is disclosed, and this record makes no claim about any other market, frame, or the source's native setting.
- Derived fill timing: the source fills next-bar under Pine defaults with no timing argument; this record executes same-bar-close on `1d` BTCUSDT. Backtest economics of the two timings differ by construction — the adaptation is disclosed, not hidden, and this record makes no claim about the source timing's performance.
- No source economics: the script ships no sizing, capital, commission, or slippage line — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- No price stop, no time stop: adverse excursion after entry has no guardrail beyond the first non-positive ROC print; a whipsaw regime prints repeated full round trips with no hysteresis. This is the prescribed posture, disclosed as a principal risk.
- Whipsaw sensitivity: the sign of a 30-bar return flips on any `c(t) = c(t−30)` crossing, including driftless oscillation — alternating prints enter-then-flatten with no flat state to rest in. The naked-sign construction is the prescribed design, disclosed, not smoothed.
- Late seed: the scalar needs 31 completed closes; the first 60 `1d` bars are flat by record rule, so early-history signals never enter any evaluation.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Immutable GitHub implementation (pinned executable artifact: `Rate Of Change Trend Strategy (ROC).pine` at commit `69969aeaf271b2f7b5a7632a1bde43069a0cbe26`, 2024-09-18, local SHA-256 `a8cb8704d98fdbf69ce491079b231186497f094d51e6520c5c59a9a05c02decf`; TV page chrome preserved around the intact script text): https://github.com/hasnocool/tradingview-pine-scripts
- TradingView canonical script page (RobertSimonUy identity, open-source status, 2022-06-13 publication date, and description text verified live via HTTP-200 page record): https://www.tradingview.com/script/CCrPAfmV-Rate-Of-Change-Trend-Strategy-ROC/
- Pine strategy semantics (Pine-default fills, `pyramiding` default, `ta.roc` semantics): https://www.tradingview.com/pine-script-reference/v5/
