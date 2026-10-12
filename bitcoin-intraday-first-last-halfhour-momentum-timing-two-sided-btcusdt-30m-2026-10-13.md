---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Bitcoin intraday first-to-last half-hour momentum timing two-sided on BTCUSDT 30m
created: 2026-10-13
updated: 2026-10-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-10-13
sources:
  - https://doi.org/10.1111/fire.12290
  - https://centaur.reading.ac.uk/100181/3/21Sep2021Bitcoin%20Intraday%20Time-Series%20Momentum.R2.pdf
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Bitcoin intraday first-to-last half-hour momentum timing two-sided on BTCUSDT 30m

## Provenance

Primary source read end to end (author-accepted manuscript PDF, University of Reading CentAUR record 100181, downloaded live over HTTPS during this cycle, 645825 bytes, text layer fully extracted and read — cover page carries the publisher-version citation advisory, recorded in Limitations):

- Shen, Urquhart & Wang (2022), `Bitcoin intraday time-series momentum`, *Financial Review* 57(2), pp. 319–344, DOI `10.1111/fire.12290`. The first Bitcoin-native study of Gao et al. (2018) intraday time-series momentum: with no open/close in 24/7 Bitcoin, the authors select each exchange's opening at its volume spike and the common close at 5pm EST (start of the CME Bitcoin-futures 60-minute break), on tick data aggregated to 1-minute bars from bitcoincharts.com (five BTC/USD venues, earliest available through 2020-12-31; thin Bitstamp 2011–2012 trading discarded by source rule, fn. 9).
- Pinned source facts with section/equation/table provenance: session table (Table 1 — Bitfinex 9:05–17:00 / Bitstamp 9:00–17:00 / CEX.IO 9:00–17:00 / Coinbase 9:40–17:00 / Kraken 9:15–17:00, all EST); first half-hour return `rONFH,t = p(o+30,t)/p(c,t-1) − 1` from the previous day's close to 30 minutes after opening, eq. (1) §2; second-to-last `rSLH` eq. (2) and last half-hour `rLH` eq. (3) (last half hour = 4:30pm–5:00pm, restated §6); headline market-timing rule `η(rONFH) = rLH if rONFH > 0 else −rLH`, i.e. long the last half hour on a positive first half hour and short otherwise, position closed at the market close every day, eq. (7) §3.4; combined dual-signal rule with flat states eq. (8) §3.4 — explicitly NOT adopted (see Negative evidence).
- Licence and rights: the manuscript is a repository-hosted accepted version under the archive's end-user terms; this record cites and normalizes the rule with equation/table/section pointers and reproduces no source block beyond single-line declarations quoted for gate evidence.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy, not a lossless reproduction of the paper. Researcher-declared adaptations are exactly five: (1) one frozen opening `09:00` ET (the modal earliest of the paper's 9:00–9:40 EST per-exchange volume-spike range — a clock freeze, never a claim about volume spikes); (2) single venue `BTCUSDT` on Binance USDT-M perpetuals replacing the paper's five-spot-exchange pooled BTC/USD (no cross-venue equivalence claimed); (3) all windows frozen on the `America/New_York` wall clock (DST-aware, mapped deterministically to UTC bars) replacing the paper's EST prose; (4) 30-minute-bar discretization — signal from completed bars, entry at the 16:30 ET bar open, exit at the 17:00 ET bar close, i.e. a one-bar hold; (5) house sizing/capital/costs (full-equity single position, Isolated 1x, taker fees both legs, funding by schedule inspection — see Execution assumptions). Source-native and unmodified: the sign rule (long iff `rONFH > 0`, short otherwise, equality to short per eq. 7), the once-per-day cadence, the full-window hold with no stops, and the time exit at the close.

Pre-write dedup (2026-10-13): case-insensitive working-tree searches for `intraday`, `half.hour`, `halfhour`, `session`, `time.of.day`, `first.half`, `volume.spike`, `shen`, `gao.han`, and `fire.12290` return no strategy record using this source or mechanism. Closest pool records differ in mechanism class: `monday-drift-weekly-calendar-hold-btcusdt-1h-2026-10-06.md` holds a weekly calendar window (different horizon and trigger — weekday, not a same-day return sign); `tsmom-12m-sign-monthly-long-btcusdt-1d-2026-10-10.md` is 12-month time-series momentum (different horizon by ~700x); `dual-thrust-open-range-breakout-two-sided-btcusdt-1d-2026-10-10.md` breaks a daily open-range band with k1/k2 multiples (different trigger, different exit); `etf-3day-reversion-ema5-mean-reversion-long-btcusdt-1d-2026-10-08.md` is multi-day indicator mean reversion (opposite direction family). Open `research/*` PRs are only #48 (Larry Williams streak long), #49 (Gaussian StochRSI breakout long), #63 (SuperTrend flip long), #89 (Chandelier Exit long), and #92 (SSL channel reversal) — no intraday, half-hour, or timing overlap in open, merged, or closed PRs. Five-axis distinction: no pool record and no open PR times a 30-minute clock window by the sign of an overnight-to-morning return with a same-day time exit. Not a trivial parameter variant.

## Economic mechanism

### Source-reported

Liquidity-provision aftermath of the open, not late-informed trading (§4): overnight news creates same-direction order imbalance in the high-volume session after opening; intraday liquidity providers lean against it, then — unwilling to cut losers quickly (disposition effect) yet forced to flatten before the close by overnight-risk management — trade WITH the first half-hour direction into the close, printing positive first-to-last autocorrelation. The paper rejects the late-informed-news channel (Bitcoin-news interaction insignificant, §4.1, Table 9 Panel B) and supports liquidity provision (Corwin–Schultz spread interaction significant at 1%, t ≈ 8.85/8.18, §4.2, Table 9 Panel D). Predictability concentrates on high-volume days (R² 3.86% vs 1.09% low, Table 4 §3.3) and high-volatility days (R² 2.83%, high-vol only, Table 4 §3.3).

### Research interpretation

A once-a-day, 30-minute, sign-timing machine: read the market's overnight digestion at 9:30 ET, then ride the liquidity providers' forced flattening into the 5pm ET close — long green mornings, short red ones, flat the other 23.5 hours. Unlike every indicator record in the pool there is no smoothing, no band, no level, no oscillator: the entire signal is one ratio of two completed-bar closes. Unlike the calendar-hold records (Monday drift, Santa, January, sell-in-May, turn-of-month) the trigger is a same-day measured return, not a date. Unlike reversal records the bet is WITH the morning move, and unlike breakout records nothing must print through a level — any nonzero morning drift, however small, takes a side. The exposure profile is the honest edge and the honest cost at once: at most 30 minutes of market risk per day (drawdown-avoidance by construction, strongest in Bitcoin downturns per Table 5 §3.4), but two fee-paying fills per day against a ~3 bps breakeven (see Negative evidence). This port is research interpretation, not source-reported fact.

## Signal

Frozen parameters (any other value is a different, unpinned rule): `open = 09:00` / `signal_read = 09:30` / `trade_open = 16:30` / `trade_close = 17:00` (all `America/New_York` wall clock) / `frame = 30m` / `equality → short` / `missing anchor bar → flat day`.

Definitions on completed 30m bars (all timestamps ET; `C(B)` = close of bar `B`):

```text
rONFH,d = C(09:00–09:30 ET bar on day d) / C(16:30–17:00 ET bar on day d-1) − 1
```

Decision and fills for day `d` (fixed order, predeclared):

```text
signal known at 09:30 ET from completed bars only (7 hours before any order)
dir_d = LONG if rONFH,d > 0 else SHORT        // equality goes SHORT, eq. (7) verbatim
enter at open of the 16:30–17:00 ET bar on day d in direction dir_d
exit the full position at close of the same 16:30–17:00 ET bar (time exit, no other exit)
flat at all other times; at most one position per day; no pyramiding
```

State rules: no stop-loss, no take-profit, no trailing, no opposite-signal exit — explicitly disabled per source (the paper holds the full window unconditionally), never defaults to assume. Re-entry needs only the next day's signal — no cooldown, explicitly none, not invented. Warmup: the first calendar day is flat by record rule (no prior 17:00 ET close exists); the first tradable window is the second day's 16:30 ET bar — deterministic, no invention. If any of the three anchor bars (prior close bar, 09:00–09:30 bar, 16:30–17:00 bar) is missing for day `d`, day `d` is flat by record rule — prices are never fabricated. The paper's volume/volatility sorts (Table 4) are conditioning analysis, not entry gates, and are not adopted. The paper's second-to-last-half-hour and combined rules (eq. 8) are not adopted.

Direction: two-sided (long/short selected daily by sign). Shorts are native to USDT-M margin (no uptick rule, no borrow desk). No always-in-market claim: flat outside the daily 30-minute window, during warmup, and on missing-bar days are explicit.

## Required data

- `30m` bars of one pair: `open` (window-entry fill), `high`/`low` (range reference only — no order-gating line reads them), `close` (signal ratio, exit fill). No volume, funding, OI, mark/index, L2, sentiment, news-count, spread-estimator, session, or cross-market input anywhere in the signal path (the paper's news counts, Corwin–Schultz spreads, and volume sorts are explanation/conditioning machinery, explicitly scoped out).
- Warmup is derivable and exact: one prior 17:00 ET close plus the first 09:30 ET read — the first calendar day is flat by record rule; the first tradable bar is the second day's 16:30–17:00 ET bar. Before that, direction is undefined and the record holds flat.
- No repainting, no negative shift, no full-sample normalization, no unfinished-bar read: the signal for day `d` is a function of bars completed by 09:30 ET on day `d`, executed 7 hours later; the exit reads the completed trade-window bar only.

## Execution assumptions

- Research market: `BTCUSDT` Binance USDT-M perpetual, `30m` decision frame (declared port; the paper's venues are five BTC/USD spot exchanges 2013–2020 — no cross-venue equivalence claimed beyond the same clock-window sign mechanics).
- Order timing (predeclared derivation): market entry at the open of the 16:30 ET 30m bar, market exit at the close of the same bar — a one-bar hold with fixed enter-at-open/exit-at-close order, so no same-bar stop/target ambiguity exists (no stops exist). Compatible with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`) on the same bar-open/bar-close fill path as the admitted 30m/15m/2h records — no maker-touch, queue, or partial-fill claims.
- Sizing/capital/costs: single position per day, notional 100% of equity at signal time (source-faithful: the paper's timing returns are full-capital strategy returns compared against buy-and-hold), Isolated 1x, no borrow. Pinned Binance non-VIP USDT-M fees costed at taker on both legs. Funding: the frozen window contains no 00:00/08:00/16:00 UTC funding timestamp under either mapping (winter 21:30–22:00 UTC; summer 20:30–21:00 UTC) — realized funding is exactly zero by schedule inspection, flagged as schedule-derived, never zero-by-assumption. Tick `0.01 USDT`, lot `0.001 BTC`.
- Concurrency: at most one position on this single market for 30 minutes per day; no second market, so no portfolio caps, selection, or rollover exist — not-applicable by construction on a non-expiring single perp, disclosed, never silently kept. No house DCA overlay is admitted: any safety-order layering would change trade events and would be a different, unpinned strategy (fenced, same as the Turtle-Soup and 1-3-1 records).

## Evidence

### Source-reported

With exact table/section provenance (accepted manuscript): pooled slope 0.968, Newey–West t = 4.38 (1% level), R² = 1.44% (§3.1, Table 3); out-of-sample R² 1.09% (first half hour alone), 1.40% (second-last alone), 1.61% (both) (§3.2); timing-rule annualized returns 7.82% (first-half-hour signal), 17.32% (second-last signal), 16.69% (combined) vs 6.54% always-long and 154.62% buy-and-hold, all three timing rules with positive Sharpe ratios and success rates over 50% (Table 5, §3.4); yearly splits show the timing value concentrates in Bitcoin downturn years 2014/2015/2018 while buy-and-hold wins 2013/2016/2017 (Table 5, §3.4); full-sample breakeven costs 3/7/10 bps unlevered, rising to 29/64/96 bps at 10:1 margin (Table 8, §3.7); high-volume-day R² 3.86%, high-volatility-day R² 2.83% (Table 4, §3.3); effect stronger when the first half hour is positive (Table 7, §3.6); the 10am–4pm ET alternative window predicts more weakly, supporting the volume-spike-to-5pm main window (§5.3, Table 12). No Sharpe point values, trade counts, or drawdown figures are carried beyond what the prose states — omitted rather than reconstructed.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- Fee headwind is real and fenced: the adopted `η(rONFH)` rule's full-sample breakeven is 3 bps (Table 8, §3.7 — the paper notes unprofitability at 25 bps Bitstamp fees), while the pinned Binance non-VIP taker round trip exceeds it — at 1x Isolated the derived rule is expected to be net-negative after costs. The paper's margin-leverage profitability (10:1) is venue leverage, not claimed here. Admission is not a profitability test; this record must never be read as a net-profit claim.
- Anti-cherry-picking fence: this record adopts the paper's HEADLINE first-to-last rule (7.82%/yr), not the better-performing second-last rule (17.32%/yr) or combined rule (16.69%/yr) — the SLH/combined variants, the mean-variance utility/CER analysis (Table 6, needs recursive vol forecasts — unpinned estimation, scoped out), and the JPY/KRW extensions (significant but weaker, t = 2.38/2.50, §5.2) are listed here so no reviewer mistakes this file for them.
- Sample age: source data ends 2020-12-31 across early spot venues; post-2020 regime, perp microstructure, and fee schedules are outside the paper — crypto-portability beyond clock mechanics is unproven.
- Frozen-open fence: `09:00` ET is one fixed choice inside the paper's 9:00–9:40 EST per-exchange range (Table 1); volume-spike dynamics are not modeled, and a different frozen minute is a different, unpinned strategy.
- Spot-perp basis drift over the 30-minute hold and any 30m-bar open/close slippage beyond taker fees are unmodeled and disclosed, never zero-claimed.
- The paper's mechanism tests (news counts, CS spreads) explain but do not trade; this record claims no mechanism edge beyond the sign rule itself.
- The `年化80%`-style sidebar risk does not apply here (no FMZ page involved); the only numbers carried are the paper's own tables above.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 09:00/09:30/16:30/17:00 America/New_York windows / 30m frame / sign rule with equality-to-short / one-bar hold / full-equity 1x / taker both legs / BTCUSDT are frozen.

- F1 — Sign relevance: a fade twin (SHORT iff `rONFH > 0`, same windows/fills) must not improve net expectancy; fail ⇒ the morning sign adds nothing over its mirror.
- F2 — Window relevance: a midday twin (same sign rule, 12:00–12:30 ET hold, same fills) must not improve net expectancy; fail ⇒ the 16:30–17:00 ET liquidity-provision window adds nothing over an arbitrary half hour.
- F3 — Hold-length relevance: a next-bar-carry twin (exit at the 17:30 ET bar close instead of 17:00) must not improve net expectancy; fail ⇒ the paper's exact close adds nothing over a slower exit.
- F4 — Timing relevance: the always-long LH twin (long every 16:30 ET bar, same exits) must not improve net expectancy; fail ⇒ timing adds nothing over unconditional late-day exposure (paper's own 6.54% benchmark logic).

## Crypto portability

Bitcoin-native by construction — the paper IS a Bitcoin study, the strongest portability posture in the pool. Perpetuals never expire, so rollover is structurally absent (not silently ignored). 24/7 trading needs no pit-session mapping; the paper already solved the no-open/no-close problem via volume-spike opens, and this record freezes that solution to a clock. Shorts are native to USDT-M margin. Tick (0.01 USDT) and lot (0.001 BTC) granularity are stated above. Single-market porting drops the paper's five-exchange pooling — this record makes no diversification or venue-averaging claim. Spot-perp basis over 30 minutes is unmodeled (see Limitations). Funding is exactly zero by funding-schedule inspection, not by assumption.

## Limitations

- Accepted-manuscript basis: the PDF cover advises referring to the publisher version for citation — equation/table/section pointers above are to the accepted text; the auditor should confirm numbering against the DOI version for any disputed fact.
- Sample ends 2020-12-31; post-2020 data, venues, and fee regimes are outside source evidence.
- 30m-bar discretization approximates the paper's 1-minute aggregation; sub-bar paths (e.g. a 9:30 ET print differing from the 09:00–09:30 bar close) are missed on purpose — bar closes are the frozen model.
- `America/New_York` DST mapping must be implemented exactly; a fixed-UTC-offset implementation is a different, unpinned strategy.
- Spot-perp basis drift, bar open/close slippage beyond taker fees, and any funding-schedule change after this cycle are unmodeled; funding zero rests on the current 00:00/08:00/16:00 UTC schedule.
- Fixed full-equity sizing with no drawdown shrink: consecutive adverse days compound at full weight — downstream must size accordingly.
- Funding-zero-by-schedule and event-level Qlib/Hummingbot parity are required before any mass screening, not claimed here.

## Implementation status

Not implemented. No code was executed and no Hummingbot/Qlib/n8n run was performed in this cycle; all compatibility statements above refer to the pinned-model bar-open/bar-close path shared with the admitted sub-1h records.

## Adoption boundary

Research-only. Not approved for Paper, Testnet, or Live trading. No downstream screening, sizing, or deployment authorization is granted by this record.

## Related Wiki records

None.

## Sources

- https://doi.org/10.1111/fire.12290 (primary — Shen, Urquhart & Wang (2022), Financial Review 57(2):319–344; rule eqs. (1)(2)(3)(7)(8), Tables 1/3/4/5/7/8/9/12, §§2–6 as cited above)
- https://centaur.reading.ac.uk/100181/3/21Sep2021Bitcoin%20Intraday%20Time-Series%20Momentum.R2.pdf (primary — author-accepted manuscript via Reading CentAUR record 100181, fetched 2026-10-13 over HTTPS, 645825-byte PDF with text layer read end to end; repository end-user terms apply — cite and normalize only, no source-block redistribution)
