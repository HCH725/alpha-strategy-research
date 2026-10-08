---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Catching-the-Bottom RSI dip-reversal long-only system on ETHUSDT 1h bars
created: 2026-10-08
updated: 2026-10-08
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: high
source_as_of: 2022-10-12
sources:
  - https://www.tradingview.com/script/ckVsOuxq-Catching-the-Bottom-by-Coinrule/
  - https://learn.coinrule.com/knowledgebase/catching-the-bottom-strategy/
  - https://github.com/hasnocool/tradingview-pine-scripts/blob/69969aeaf271b2f7b5a7632a1bde43069a0cbe26/Catching%20the%20Bottom%20(by%20Coinrule).pine
  - https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
  - https://www.tradingview.com/pine-script-docs/concepts/strategies/
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "Page and academy prose call the averages EMA (EMA100/EMA50/EMA9); the pinned executable block uses first-party `ta.sma` throughout. The code governs: all three averages are pinned as SMA (50/100 entry pair, 9/50 exit pair)."
---
# Catching-the-Bottom RSI dip-reversal long-only system on ETHUSDT 1h bars

## Provenance

Primary source read end to end (TradingView canonical strategy page, live browser read 2026-10-08):

- Canonical page: https://www.tradingview.com/script/ckVsOuxq-Catching-the-Bottom-by-Coinrule/ (`Catching the Bottom (by Coinrule)`, Strategy by Coinrule, `OPEN-SOURCE SCRIPT`, Oct 12 2022, adopted as `source_as_of`).
- Page-chart context at read time: BINANCE MATIC/USDT on a 2h chart — a display context, not a strategy rule (the script takes no symbol, timeframe, session, or venue input).
- Page-stated rules (verbatim substance): ENTRY = RSI has a decrease of 3, RSI < 40, EMA100 has crossed above EMA50 (i.e. the fast leg crossing below the slow leg); EXIT = RSI greater than 65, EMA9 has crossed above EMA50. Page further states the system was backtested from 1 April 2022 to simulate a bear market, that strong pairs include ETH 5m, BNB 5m, XRP 45m, MATIC 30m and MATIC 2h, that each order uses 30% of available coins, and that a 0.1% fee aligned to the Binance base fee is assumed. The page carries no numeric performance table — no returns, win rate, drawdown, or trade-count figures anywhere in the prose (only qualitative "good returns" / "very strong results" claims).
- First-party corroboration (not a second mechanism): https://learn.coinrule.com/knowledgebase/catching-the-bottom-strategy/ (Coinrule Trading Academy) restates the same three entry legs (RSI below 40, RSI decreased by three, MA50 crossing below MA100) and the same two exit legs (RSI above 65, MA9 crossing above MA50).
- Immutable code provenance: hasnocool mirror file `Catching the Bottom (by Coinrule).pine` at pinned commit `69969aeaf271b2f7b5a7632a1bde43069a0cbe26` (verified still the remote HEAD via `git ls-remote` this run), blob `f4bdede39da2e5f876d0a8d2421601a2afaf0dab`, 2617 bytes. The mirror header (`Script Name`, `Author: Coinrule`, RSI/EMA description lead) matches the canonical page, and the embedded 53-line Pine v5 block implements exactly the page-stated rules with defaults (RSI 14 / fall 3 / SMA 50-100 entry cross / RSI 65 / SMA 9-50 exit cross / 2022-04-01 floor / 30%-equity sizing / 0.1% commission — see Signal). The `2022-04-01` code floor is the same date as the page's "back tested from 1 April 2022" statement.
- Censuses over the pinned block: `strategy.entry` 1, `strategy.close` 1, `strategy.exit` 0, `strategy.order` 0, `strategy.close_all` 0, live `request.*` 0 (two `request.security` lines exist only as comments), `security(` 0, `timeframe(` 0, `stop=` 0, `limit=` 0, `profit=` 0, `loss=` 0, `pyramiding` 0, `calc_on_every_tick` 0, `varip` 0, `input.time` 0. Series read by order logic: `close` only, plus bar `time` inside the deterministic date floor (causal, never future). `open`, `high`, `low`, `volume` occur 0 times in any order-gating line. `plot` lines are display-only and never gate an order.

Licence and rights: the canonical page is an open-source publication by Coinrule. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

Pre-write dedup (2026-10-08): working-tree searches for `catching`, `ckVsOuxq`, `vrsi`, and `Catching the Bottom` return 0 strategy records. Open `research/*` PRs are only #48 (Larry Williams 3-EMA channel streak long, FMZ 451075) and #49 (Gaussian channel StochRSI-gated breakout long, FMZ 482888), plus reconstruction-lane #58 — different mechanisms, indicators, and sources. Closest pool records are different mechanism classes: `rsi-classic-level-reversal-btcusdt-1h-2026-10-07.md` (FMZ 441161: bare RSI(14) < 30 entry / RSI > 60 exit, no average, no momentum-fall leg), `oversold-rsi-tight-sl-long-btcusdt-1h-2026-10-07.md` (FMZ 436250: RSI < 30 entry with fixed +/-percentage bar-close exits, no cross anywhere), `rsi-sma-gated-cross-reversal-btcusdt-1d-2026-10-08.md` (SMA 100/150 cross gated by RSI-50 level, two-sided immediate reversal), `rsi-ma-crossover-reversal-btcusdt-1d-2026-10-07.md` (RSI(27) vs SMA(RSI,10) cross, two-sided always-in-market), `cumulative-rsi-dual-threshold-long-btcusdt-1h-2026-10-08.md` (cumulative-RSI threshold system, no cross legs). Five-axis distinction: mechanism differs (three-leg dip-catch conjunction — oversold level AND a 3-point RSI fall AND a 50/100 death-cross edge — with a dual-leg recovery exit, long-only, signal-close only), signal construction differs (no pool record combines an RSI momentum-fall leg with a death-cross edge on entry and a golden-cross edge on exit), exits differ (dual-conjunction close, no percentage leg, no oscillator-only leg), source identity differs (Coinrule TV Oct-2022 `ckVsOuxq` plus hasnocool blob `f4bdede`, not FMZ 441161/436250), and research frame is ETHUSDT `1h` (ETH is source-listed; MATIC itself is outside the house universe).

## Economic mechanism

### Source-reported

A bear-market dip-catching long: it waits until RSI(14) is both weak (below 40) and still falling (down 3 points bar-over-bar) at the exact bar the medium average crosses below the slow average, buying the capitulation bar of a fresh short-term downtrend. It exits only when strength is confirmed on both legs — RSI above 65 together with the 9-bar average re-crossing above the 50-bar average — riding the snap-back until the recovery is corroborated. No stop, target, or time leg exists by construction.

### Research interpretation

Oversold-edge timing with a trend-confirmation veto on both sides. The RSI level-plus-fall legs isolate washed-out-and-worsening bars while the death-cross edge refuses entries outside genuine regime turns, so signals cluster at downtrend birth rather than on every oversold print. The dual-leg exit symmetrically refuses to bank until momentum (RSI>65) and structure (9/50 golden edge) agree the dip has reversed. Both gates are pure close-derived level/edge logic, so the full event sequence is reproducible from completed bars alone. No leverage, sizing, or cost edge is embedded in the signal; the declaration carries only event-neutral accounting lines (1000 capital, 30%-of-equity sizing, 0.1% commission), so the house overlay supplies them (see Execution assumptions).

## Signal

Exact rule as pinned (Pine v5, defaults quoted — inputs unmodified):

- Declaration: `strategy("V3 - Catching the Bottom", overlay=true, initial_capital=1000, process_orders_on_close=true, default_qty_type=strategy.percent_of_equity, default_qty_value=30, commission_type=strategy.commission.percent, commission_value=0.1)`. `calc_on_every_tick` is unset (default false); `pyramiding` is unset (v5 language default 0: no additional same-direction entry while positioned — the same default-convergence earlier PASS reviews accepted for Coinrule blocks, and it is load-bearing here, see Execution assumptions).
- Date floor: `timePeriod = time >= timestamp(syminfo.timezone, 2022, 4, 1, 0, 0)` — deterministic, causal (bar `time` only), true for every bar on/after 2022-04-01. Bars before the floor admit no entries and no closes by explicit rule (pinned, not invented); this is the code form of the page's "back tested from 1 April 2022" bear-market scope.
- Oscillator: `vrsi = ta.rsi(close, length)` with `length = input(14)` default 14 (first-party deterministic Wilder-RMA RSI on `close`).
- Entry legs (all three must hold on the same completed bar): `buyCondition1 = vrsi < 40` (strict; `vrsi == 40` fires nothing); `buyCondition2 = vrsi < vrsi[1] - decrease` with hardcoded `decrease = 3` (strict 3-point bar-over-bar fall; an exact 3.0 fall fires nothing); `buyCondition3 = ta.crossunder(fastEMA, slowEMA)` where `fastEMA = ta.sma(close, 50)` and `slowEMA = ta.sma(close, 100)` (strict v5 crossunder semantics — a tie on either compared bar fires neither leg). Despite the source's `fastEMA`/`slowEMA`/`EMA9`/`EMA50` names, every average is first-party `ta.sma` — pinned as SMA per the code-governs contradiction above.
- Long leg: `strategy.entry(id='Long', direction = strategy.long)` inside `if(buyCondition1 and buyCondition2 and buyCondition3 and timePeriod)`.
- Exit legs (both must hold on the same completed bar): `sellCondition1 = vrsi > 65` (strict); `sellCondition2 = ta.crossover(EMA9, EMA50)` where `EMA9 = ta.sma(close, 9)` and `EMA50 = ta.sma(close, 50)` (strict v5 crossover semantics).
- Exit: `strategy.close(id='Long')` inside `if(sellCondition1 and sellCondition2 and timePeriod)` — full close of the one long, unconditional on price otherwise.
- Direction: long-only, explicitly. No short entry exists anywhere in the block; the short side is disabled by construction.
- Stop-loss / take-profit / trailing / time limit: explicitly none (0 `strategy.exit`, 0 `stop=`/`limit=`/`profit=`/`loss=`). The dual-leg signal close is the sole exit path; otherwise the position is held.
- Inert code, provably excluded: `notInTrade` (defined once, never read by any order condition — write-only), `showDate` (display input, never read), the two commented `request.security` lines (comments, not code — zero live MTF calls), all `plot` lines.

## Required data

- Completed `1h` bars of ETHUSDT: `close` only (RSI, both SMA pairs, both cross edges, both level comparisons) plus bar `time` for the pinned date floor. No `open`, no `high`/`low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, options, sentiment, macro, session, or cross-venue state is read by any order-gating line.
- Single decision timeframe `1h`. The script takes no timeframe input and makes no live `request.*`/`security(`/`timeframe(` call, so it is single-frame by construction; `1h` is adopted as the in-lane research frame because the script is timeframe-agnostic while the source's stated strong frames are all sub-hour except 2h (ETH 5m, BNB 5m, XRP 45m, MATIC 30m, MATIC 2h) — `1h` is the explicitly labeled house-overlay instantiation nearest that applicability, never presented as a source-declared timeframe (see Limitations).
- Warmup: longest live window is 100 bars (`ta.sma(close, 100)`); the crossunder prior-bar reference needs one further bar. First fully-defined evaluation at the 101st completed `1h` bar; no signal is evaluable before that. No repainting, no negative shift, no future reference, no full-sample normalization.

## Execution assumptions

- Research market: ETHUSDT under the house overlay (ETH is explicitly source-listed among the strong pairs and inside the house universe; MATIC itself is outside the universe, so ETH is the closest source-faithful instantiation — never presented as source-native venue semantics; the rule reads closes only).
- Order timing: the declaration sets `process_orders_on_close = true` with `calc_on_every_tick` unset (default false): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester. No next-bar-open, maker-touch, queue, or intrabar-path-dependent fill.
- Sizing/capital: the declaration's 30%-of-equity sizing, 1000 initial capital, and 0.1% commission lines are pure event-neutral accounting (the page's own 30%/0.1% framing confirms their accounting nature), replaced by the explicit house overlay (Base 6% + Safety 6% + Safety 6%, Isolated, 3x/5x) and pinned house cost assumptions, never presented as source-native behavior.
- Concurrency: `pyramiding` is unset (v5 default 0: no same-direction add while positioned). The default is load-bearing here and therefore pinned explicitly: the level legs (RSI < 40, RSI falling) can persist across bars while long, and a second death-cross edge can print before any exit — the admitted rule blocks every such add and holds. Re-entry is allowed immediately after any close whenever the three-leg conjunction fires again (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The canonical page ships prose only: qualitative claims (bear-market scope from April 2022, strong sub-hour crypto pairs, 30% sizing, 0.1% Binance-aligned fee) plus the plain dip-catch risk alluded to by the "bear market" framing. The page carries no numeric performance table — no returns, win rate, drawdown, or trade-count figures. The mirror's trailing "Best on" comment lines carry bare in-sample percentages with no methodology table; they are omitted as figures and cited only for timeframe applicability. Recorded as an explicit gap, not filled: this record claims no source-reported performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Flat-book determinism: with no open position the `strategy.close(id='Long', …)` leg is a deterministic no-op; only a genuine three-leg conjunction can open.
2. Same-bar mutual exclusivity is proven, not assumed: entry needs `vrsi < 40`, exit needs `vrsi > 65` — both can never hold on one bar, so entry and exit never co-fire and no call-order priority is required. The `if`-block form with `process_orders_on_close` executes at the same bar close as `when=` form; form difference changes no event.
3. Boundary ties are defined: `vrsi == 40` blocks entry, `vrsi == 65` blocks exit, an exact 3.0 RSI fall fires nothing, and a tied average on either compared bar fires neither cross leg — ties hold, they never invent an order.
4. The date floor is pinned, not removed: moving the 2022-04-01 floor, switching any average to EMA, reviving a short leg, or adding a stop/target/cooldown would each be a different, unpinned rule — none is admitted here. Under full-history house evaluation, pre-2022-04-01 bars are flat by explicit source rule.
5. Display-code isolation: all `plot` lines never enter any order condition, so display toggling cannot alter any admitted event; the commented MTF lines are not code and change nothing.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: RSI(14) < 40 plus 3-point fall plus SMA50/100 death-cross entry, RSI > 65 plus SMA9/50 golden-cross exit, long-only, `1h` ETHUSDT, same-bar-close fills are frozen.

- F1 — Death-cross relevance: the entry without `buyCondition3` (RSI level + fall legs only) must not improve net expectancy; fail ⇒ the SMA gate earns no keep and the system is a plain RSI-dip system wearing a cross costume.
- F2 — Fall-leg relevance: the entry without the 3-point fall (RSI < 40 + death-cross only) must not improve net expectancy; fail ⇒ the momentum leg adds nothing over a level-plus-cross system.
- F3 — Exit-conjunction relevance: exiting on RSI > 65 alone (SMA9/50 cross leg removed) must not improve net expectancy; fail ⇒ the exit cross is decorative and the system is an oscillator-round-trip system.

## Crypto portability

Pinned to ETHUSDT under the house overlay. The close-derived long-only logic ports to perps or spot without structural change (no short leg exists to drop); no funding-dependent leg, no stablecoin-specific assumption, no cross-venue state. ETH is source-listed applicability; extension to other house-universe assets would be a different, unpinned claim.

## Limitations

- Source-frame transfer: every source-stated strong frame is sub-hour except MATIC 2h (ETH 5m, BNB 5m, XRP 45m, MATIC 30m); the `1h` pin is an explicitly labeled research choice for a timeframe-agnostic script, not a source-declared frame — hourly-bar behavior is untested by the source.
- Warmup cost: the SMA100 leg needs 100 completed bars, so the system is blind for the first 100 bars of any evaluation window and reacts slowly to regime births on hourly bars.
- Level-leg persistence: RSI can sit below 40 and falling for many bars while long; every repeat signal is deterministically blocked by the pinned pyramiding-0 default, so the system cannot scale into deepening washes by construction.
- No adverse-stop protection: exits print only on the dual-leg recovery conjunction, so an adverse drift that never prints RSI > 65 with a 9/50 golden edge is ridden indefinitely; the source's bear-market framing concedes exactly this failure mode.
- Naming gap resolved: prose says EMA, code is SMA — pinned as SMA. Any EMA-variant reading would be a different, unpinned rule.

## Implementation status

- `implementation_status: not-implemented`.
- Normalized rule is fully specified above; no Hummingbot/Qlib/n8n/survivor/Paper/Testnet/Live work has been performed or is authorized by this record.

## Adoption boundary

- `adoption: not-approved`, `approval_scope: research-only`, `status: research-only`.
- This record is semantic normalization only. It is not profitability validation, not a survivor promotion, and not Paper/Testnet/Mainnet authorization. Only `hb_ready_status: PASS` records may enter the current Hummingbot/Qlib performance-research downstream, subject to that workflow's own gates.

## Related Wiki records

None.

## Sources

- Primary: https://www.tradingview.com/script/ckVsOuxq-Catching-the-Bottom-by-Coinrule/ (Strategy by Coinrule, open-source, Oct 12 2022; page rules, bear-market scope, pair/timeframe notes, 30%/0.1% accounting notes, and zero numeric performance claims all live-verified 2026-10-08; display context BINANCE MATIC/USDT 2h).
- First-party corroboration: https://learn.coinrule.com/knowledgebase/catching-the-bottom-strategy/ (Coinrule Trading Academy; three entry legs and two exit legs restated, matching the pinned block).
- Immutable code mirror: https://github.com/hasnocool/tradingview-pine-scripts/blob/69969aeaf271b2f7b5a7632a1bde43069a0cbe26/Catching%20the%20Bottom%20(by%20Coinrule).pine (pinned HEAD verified as remote HEAD this run; blob `f4bdede39da2e5f876d0a8d2421601a2afaf0dab`, 2617 bytes; header and Pine block match the canonical page, code governs over the EMA-naming prose).
- Pine `strategy()` declaration semantics (first-party reference): https://www.tradingview.com/pine-script-reference/v5/#fun_strategy
- Strategy execution model (broker emulator, `process_orders_on_close`): https://www.tradingview.com/pine-script-docs/concepts/strategies/
