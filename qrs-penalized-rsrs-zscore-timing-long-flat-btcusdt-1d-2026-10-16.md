---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: QRS penalized RSRS z-score timing long-flat on BTCUSDT 1d bars
created: 2026-10-16
updated: 2026-10-16
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: high
source_as_of: 2026-10-03
sources:
  - https://github.com/hugo2046/QuantsPlaybook
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# QRS penalized RSRS z-score timing long-flat on BTCUSDT 1d bars

## Provenance

Primary source read end to end during this cycle (2026-10-16), pinned immutable:

- Repository: https://github.com/hugo2046/QuantsPlaybook at commit `3f83a77f4c7996ed8185b8979a42c4372c1d811f` (committed `2026-10-03 +0800`, verified locally via `git fetch` + `git rev-parse HEAD` byte-match; adopted as `source_as_of`).
- Signal construction: `SignalMaker/qrs.py` (361 lines) — `QRSCreator` class with `calc_beta`, `calc_zscore`, `calc_regulation`, and `fit(regression_window=18, zscore_window=600, n=2, adjust_regulation=False, use_simple_beta=False)` (all defaults pinned in the signature).
- Executable strategy: `C-择时类/QRS择时信号/strategy/rsrs_strategy.py` (194 lines) — class `RSRSStrategy` (long-flat; the adopted machine) plus a separate class `RSRSTwoSidetrategy` (explicitly NOT adopted here, fenced below).
- Wiring notebook: `C-择时类/QRS择时信号/QRS.ipynb` (40 cells) — baseline cells pin `QRSCreator(low_df, high_df)`, `qrs.fit(18, 600)`, `upperbound = 0.7`, `lowerbound = -0.7`, `RSRSStrategy` with `strategy_kwargs={"verbose": False, "hold_num": 1}`.
- Data feed: `C-择时类/QRS择时信号/backtrader_utils/datafeed.py` — `DailyOHLCVUSLFeed` carries `open/high/low/close/volume/upperbound/signal/lowerbound` daily columns.
- Report lineage kept separate (context only, never gate evidence): `C-择时类/RSRS择时指标/择时-20170501-光大证券-择时系列报告之一：基于阻力支撑相对强度（RSRS）的市场择时.pdf` (the 2017 Essence report family behind N=18/M=600/±0.7) and `20191117-光大证券-技术指标系列报告之六：RSRS择时~回顾与改进.pdf`; the QRS penalty construction cites `20210121-中金公司-量化择时系列（1）：金融工程视角下的技术择时艺术.pdf` (mirrored under `C-择时类/QRS择时信号/参考/`).
- Code census of the adopted machine: 1 `CrossUp(d.signal, d.upperbound)` entry trigger / 1 `CrossDown(d.signal, d.lowerbound)` exit trigger / 1 `self.buy(... Market)` / 1 `self.close(... Market)` / 0 `strategy.exit`-equivalents (no stop/limit/target/trailing/time-exit argument anywhere) / 0 short-order calls in `RSRSStrategy` / position guards `if not size` (enter) and `if size` (exit) / `hold_num=1` / `commission=0.01` (1% reserve, recorded as absent portable economics) / A-share 100-lot rounding helper `calculate_ashare_order_size` (venue-specific, replaced by derivation).
- No `LICENSE` file exists at the pinned commit. This record cites and normalizes the rule and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the source. Researcher-declared adaptations are exactly four: (1) market pin `BTCUSDT` Binance futures `1d` (the source trades A-share index/ETF daily bars — `000300.SH` and multi-index panels; the daily decision frame is kept source-native, only the market/venue is adapted and disclosed here, never presented as a source claim); (2) same-bar-close market fills (the backtrader source fills `Market` orders on the next bar by engine default with the comment `以下个bar的开盘价买入`; this record pins completed-bar decision with same-bar-close execution, predeclared per pool precedent); (3) an adopted 620-bar warmup with pre-warmup bars flat by record rule (covers the 18-bar regression seed plus the 600-bar z-score seed plus index alignment, with margin — see Required data); (4) house sizing/capital/costs replacing the source demo economics (`commission=0.01` reserve, full-equity single slot, 100-share lots — recorded as absent portable economics, never as evidence). The `18` / `600` / `n=2` / `±0.7` constants, the OLS-slope × corr² signal, the cross-pair triggers, the long-flat posture, and the no-stop-no-target stance are source-pinned. **No Safety Order, no DCA event, no pyramiding, no short leg, and no time exit is admitted in this record's version.**

Pre-write dedup (2026-10-16): working-tree case-insensitive searches for `rsrs`, `qrs`, `nadaraya`, `阻力支撑`, `qrscrator`, and `quantsplaybook` return zero strategy records. Closest pool record `linreg-channel-band-touch-two-sided-btcusdt-1d` regresses price on time for channel rails — a different signal object (price-vs-time slope bands, never high-on-low cross-sectional slope, never z-scored, never correlation-penalized). Open `research/*` PRs are only #48, #49, #63, #89, #92 (Larry Williams streak, Gaussian StochRSI, SuperTrend flip, Chandelier Exit, SSL channel) — zero slope/z-score content in any of them.

## Economic mechanism

### Source-reported

Resistance-support relative strength: when the 18-day OLS slope of `high` on `low` is unusually strong versus its own 600-day history (z-score above +0.7 after the correlation penalty), buyers are lifting highs faster than lows can sag — trend support dominates, so the machine holds the market long. When the penalized z-score breaks below −0.7, support has failed relative to history and the machine stands flat. The squared-correlation multiplier (`regulation = corr²`, default `n=2`) penalizes slopes computed from noisy, low-correlation windows: a steep slope nobody agrees on (low |corr|) is shrunk toward zero and cannot trigger. Between the rails the machine keeps its prior state (latch).

### Research interpretation

Standardized-slope state machine, long-flat. Unlike oscillator-threshold systems (a raw level crossing trades), here the trigger object is a doubly-normalized statistic: first normalized across price scale by the regression itself (slope is unit-free strength, not points), then normalized across history by the z-score (strength relative to its own 600-day distribution), then gated by fit quality (corr²). Unlike plain moving-average or breakout timing, there is no price level, no band touch, and no lookback extremum anywhere — the only question asked each bar is whether relative support strength is historically extreme. The price of the corr² penalty is blindness to steep-but-disorderly advances (high slope, low correlation never arms); the price of the 600-day memory is slowness to re-rate after volatility-regime shifts. The ±0.7 rails with a hold zone make this a slow latch, not a cross-and-fade: most bars do nothing by design.

## Signal

Exact rule as pinned (all constants are call-site literals or pinned signature defaults; any other value is a different, unpinned rule):

- Declarations (derived): single-asset state machine over `BTCUSDT 1d` with same-bar-close execution and house sizing/costs (see Execution assumptions). At most one long position; zero short exposure by record rule.
- Regression (pinned verbatim, `calc_beta`): over the trailing 18 bars `t-17..t`, `beta(t) = std(high)/std(low) × corr(high, low)` with population moments (`np.std` default `ddof=0`). This is algebraically the OLS slope of `high` on `low` (verified numerically during this cycle: agreement with `lstsq` to <1e-12 on random data).
- Standardization (pinned verbatim, `calc_zscore` + `calc_zscore_beta`): `z(t) = (beta(t) − mean(beta[t-599..t])) / std(beta[t-599..t])` with `nanmean`/`nanstd`, `ddof=0`.
- Penalty (pinned verbatim, `calc_regulation` with default `n=2`): `R(t) = corr(high, low; t-17..t)²` over the same trailing 18 bars.
- Signal (pinned verbatim, `fit(18, 600)` defaults — corr-inclusive beta, no regulation adjustment, no simple-beta): `S(t) = z(t) × R(t)`.
- Rails (pinned verbatim, notebook cells 13/21/31): `upperbound = +0.7`, `lowerbound = −0.7`, constant series.
- Long entry (pinned verbatim, backtrader `CrossUp` semantics): `S(t-1) <= +0.7 and S(t) > +0.7` while flat → buy. (`CrossUp` fires exactly on the upward rail cross; the `if not size` guard makes re-crosses while positioned no-ops.)
- Flat exit (pinned verbatim, backtrader `CrossDown` semantics): `S(t-1) >= −0.7 and S(t) < −0.7` while positioned → close all. (`CloseDown` fires exactly on the downward rail cross; the `if size` guard makes crosses while flat no-ops.)
- Latch equivalence disclosed: under the single-position guards, the cross pair is exactly the state machine "long above +0.7, flat below −0.7, hold between" — no separate state variable is needed or invented.
- Exits/risk: rail-cross exit only. No stop, no target, no trailing, no time exit — explicitly none by record rule, never hidden (0 stop/limit/target arguments in the shipped class).
- Direction: long-flat only. Zero short-order calls exist in `RSRSStrategy`; the venue needs no short permission for this machine.
- Re-entry: after any close, the next upward rail cross re-enters (no cooldown specified — explicitly none, not invented). Same-direction re-cross while positioned is a no-op by the shipped guard.

## Required data

- Completed `1d` bars of BTCUSDT: `high`, `low` (signal regression), `close` (fill reference only — no order-gating line reads `close` directionally). `volume` is carried by the source feed but read by zero order-gating lines (fenced as dead column). No funding, OI, mark/index price, order-book, on-chain, sentiment, macro, calendar, session, or cross-asset state is read anywhere.
- Single decision timeframe `1d` (no multi-timeframe call, no `security`-equivalent, no cross-sectional ranking — the notebook's multi-index panel runs each code independently with no shared state; this record pins one asset).
- Warmup: `beta` needs 18 bars; `z` needs 600 betas; output index starts at raw bar 616 (0-based) per `get_index(18, 600)` (`index[616:]`), so the first computable signal sits on the 617th bar (1-based). The adopted warmup is the first 620 completed `1d` bars flat by record rule (full seed plus margin; no signal before bar 621 may trade). All windows are trailing (`sliding_window` yields `[k..k+17]` ascending, `calc_zscore(arr)[-1]` scores the window's last element) — causal under same-bar-close fills. No repainting, no negative shift, no full-sample normalization; one evaluation per completed bar.

## Execution assumptions

- Research market: BTCUSDT Binance futures under the house overlay (source trades A-share index/ETF daily bars — market/venue adaptation disclosed in Provenance, never presented as a source claim; the `1d` decision frame is source-native).
- Order timing (predeclared derivation): completed-bar decision with same-bar-close execution, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) — the same verified execution primitive as the admitted `three-down-three-up-consec-close-long-btcusdt-1h`, `qstick-zero-cross-trend-two-sided-btcusdt-1h`, and `eight-day-run-sma5-momentum-reversal-two-sided-btcusdt-1d` PASS records (single-frame completed-bar decision, same-bar-close market fill, no protective stop/limit legs anywhere in the derived machine, hence no same-bar TP/SL ordering ambiguity; each bar's outcome is a deterministic event: hold, open, or close). No maker-touch, queue, multi-asset sync, lower/multi-timeframe alignment, non-OHLCV input, or intrabar-path-dependent fill is required by any line of this record.
- Sizing/capital/costs: the source ships venue-bound economics (full-equity single slot, 1% commission reserve, 100-share lots — recorded as absent portable economics, never as evidence) — derived evaluation carries the fixed, reproducible house research cost model (Base 6% + Safety 6% + Safety 6% notional framing, Isolated, 3x/5x; pinned house cost assumptions for fees plus modeled funding — no hypothetical zero funding claimed, never presented as source-native behavior). Funding is modeled, never reported as realized or canonical funding. No Safety-Order/DCA event participates in the admitted trigger machine regardless of downstream campaign settings.
- Concurrency: one order path over one single-asset engine position — at most one long exposure at a time; no second position is constructed anywhere. No shared portfolio state, no cross-sectional ranking, no multi-pair logic.

## Evidence

### Source-reported

The pinned code ships the full construction (OLS-slope beta, 600-window z-score, corr² regulation with `n=2`, `fit(18, 600)` defaults, `±0.7` rails, the `CrossUp`/`CrossDown` trigger pair, the single-position guards, `hold_num=1`), and the notebook ships cumulative-return plots and trade-stat tables for A-share indices/ETFs. This record carries zero source-reported performance numbers: exact empirical figures require traceable table/figure/section provenance and are omitted, never paraphrased.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. No performance carried, admitted plainly: the notebook's plots/tables are A-share venue evidence for a different market; no number is transferred to this crypto-derivative record, and this record claims none.
2. Long-flat posture provably complete: 0 short-order calls in `RSRSStrategy` — a two-sided reading would contradict the shipped class. The sibling `RSRSTwoSidetrategy` (open on either rail cross, close on either rail recross) is a separate, unadopted class — fenced as a different, unpinned rule, never merged into this admission.
3. No hidden exits or risk layer: 0 stop/limit/target/trailing/time arguments in the adopted class — the no-stop/no-target posture is the record rule, explicitly none, never hidden.
4. No hidden variants admitted: the notebook experiments with `n` (lag/power) sweeps, `adjust_regulation=True`, and `use_simple_beta=True` — all are research sweeps around the baseline, and none is admitted here. The admitted signal is exactly `fit(18, 600)` defaults. A reviewer must not pick among these variants to rescue or reshape the record.
5. Trailing-window causality proved: `sliding_window` yields ascending trailing windows only; `beta[k]` reads raw bars `k..k+17`; `z[j]` scores `beta[j..j+599]` at its last element; every input to `S(t)` is complete at bar `t`'s close.
6. Dead columns fenced: `volume` rides the feed but gates nothing; `open` is referenced only in the sizing comment path replaced by derivation. Neither touches any trigger.
7. Seed determinism fenced: pre-seed bars produce no signal row at all (`get_index` starts at raw bar 616); the adopted 620-bar flat absorbs all seeding structurally regardless of convention. No seeded value ever trades.
8. Slope-identity check disclosed: `calc_beta` equals the OLS slope algebraically and numerically (<1e-12 vs `lstsq` on random data, verified during this cycle) — stated once as construction evidence, never as performance.
9. Overlap fence, admitted plainly: the pool's linear-regression record regresses price on time for channel rails; the pool's correlation record (if any) never multiplies a z-scored slope by corr² with ±0.7 rail latches. Shared "regression/correlation" vocabulary is not shared signal: high-on-low slope × 600-day z × corr² with rail-cross latch exists nowhere else in the pool.
10. Derivation boundary fenced: the only non-source-native behaviors are the A-share→`BTCUSDT` market/venue pin (frame kept), per-completed-bar evaluation with same-bar-close fills (source fills next-bar-open by engine default), the adopted 620-bar warmup with record-rule pre-warmup flat, and house sizing/costs with no admitted Safety-Order/DCA event — all predeclared above; the `18`/`600`/`n=2`/`±0.7` literals, the penalized-z signal, the cross pair, the guards, the long-flat posture, and the risk posture are source-pinned or predeclared. This record is therefore never evidence that any other market, frame, length, window, power, rail set, variant flag, or timing of the source passes.
11. Division of evidence disclosed: the formula, literals, trigger pair, guards, feed columns, and notebook wiring above were verified by reading the pinned files at the verified commit during this cycle; the report PDFs are cited as lineage context only and were not used for any gate.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: `18` / `600` / `n=2` / corr-inclusive beta / `±0.7` rails / cross-pair triggers / rail-cross exit / no-stop-no-target posture / long-flat / `1d` BTCUSDT / same-bar-close fills are frozen.

- F1 — Rail relevance: replacing the `±0.7` rails with `0.0`/`0.0` (sign latch, same signal) must not improve net expectancy; fail ⇒ the historical-extremity rails add nothing over a plain sign latch on this market.
- F2 — Penalty relevance: dropping the corr² multiplier (plain RSRS z-score, same rails/machine) must not improve net expectancy; fail ⇒ the fit-quality penalty adds nothing over the unpenalized z-score on this market.
- F3 — Memory relevance: shortening the z-score window `600 → 60` (same beta, rails, machine) must not improve net expectancy; fail ⇒ the 600-day history normalization adds nothing over a quarterly memory on this market.

## Crypto portability

Pinned to BTCUSDT Binance futures under the house overlay (source trades A-share index/ETF daily bars — market/venue adaptation disclosed, `1d` frame kept source-native). The rule reads completed daily high/low only, so no open-print, session, or cross-venue difference can touch any order-gating line beyond each calendar-day bar's own prints — but spot-vs-perp prints can still differ structurally (funding-driven drift, venue aggregation), so the futures-venue pin is load-bearing and disclosed. Lengths `18`/`600` are fixed bar-count constants, so no fixed-pip recalibration is needed across assets — cross-asset behavior differences are still real and unclaimed. The rule is long-flat, so a spot-only deployment expresses the full machine; no short permission is assumed anywhere. No funding-dependent leg, no stablecoin-specific assumption, no session template (A-share T+1/limit-board microstructure has no analogue here and none is modeled), no cross-venue state. The 24/7 crypto market has no opens/gaps/sessions for the rule to read beyond each bar's own prints (no session gating anywhere; the regression treats each daily bar identically); decision boundaries are calendar-day bars of the venue feed, disclosed. The 620-bar warmup consumes roughly 1.7 years of daily history before the first signal — disclosed as a data-availability cost. Extension to other house-universe assets or timeframes would be a different, unpinned claim.

## Limitations

- No source economics: the source ships venue-bound sizing (100-share lots, 1% reserve) with no portable fee/slippage/leverage assumption — derived evaluation must carry the full house cost load, and this record reports no net performance of any kind.
- No price stop, no time stop: adverse excursion after entry has no guardrail beyond the −0.7 rail cross, which may arrive many bars later or after deep excursion; a leg whose exit print never arrives is held indefinitely. This is the record-rule posture, disclosed as a principal risk.
- Single-position concentration: the machine holds full size or nothing — there is no scale-in, no partial exit, and no flat resting state between the rails other than staying in the prior state; alternating rail adjacency in choppy regimes can churn full-size entries and exits with no dampener, by the prescribed design.
- Penalty blindness: steep slopes printed from low-correlation windows are shrunk by corr² and never arm a trigger — disorderly advances are sat out by the prescribed design.
- Slow memory: the 600-day z-score window re-rates slowly after volatility-regime shifts; post-shift extremes are judged against stale history, by the prescribed design.
- Warmup cost: 620 daily bars of venue history are consumed before the first legal signal — backtest coverage on young markets is structurally short, disclosed.
- Next-bar timing reading: the same-bar-close fill is a predeclared derivation from the source's next-bar-open engine fills; an engine modeling next-open entries would trade different (slightly later) events.
- Venue-portability residual: A-share T+1 settlement, price limits, and index microstructure have no crypto analogue and none is modeled — the derivative carries only the arithmetic rule, disclosed.

## Implementation status

Not implemented. No Hummingbot controller, no Qlib screen, no Paper/Testnet/Live run exists for this record. Any future implementation must demonstrate the pinned-engine path (package `20260920`, VERSION `dev-2.17.0`) and representative event-level Qlib/HB parity before mass screening.

## Adoption boundary

Research-only. Not approved for any adoption, sizing, or live-trading use. Downstream house overlays (DCA matrix, leverage, capital) are separately declared experiments, never source-native behavior and never part of this admission — no Safety-Order/DCA event is admitted in this record's version. Promotion requires the standard downstream evidence chain, never this record alone.

## Related Wiki records

None.

## Sources

- Public GitHub implementation, QuantsPlaybook by Hugo (QRS penalized-RSRS timing: `SignalMaker/qrs.py` + `C-择时类/QRS择时信号/strategy/rsrs_strategy.py` + `QRS.ipynb`, pinned commit `3f83a77f4c7996ed8185b8979a42c4372c1d811f` dated 2026-10-03, N=18/M=600/n=2/±0.7 long-flat baseline verified from the pinned files during this cycle): https://github.com/hugo2046/QuantsPlaybook
