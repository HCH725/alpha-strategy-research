---
schema: strategy-research-record-v1
hb_ready_status: PASS
title: Alexander-Fama-Blume 5-percent filter trailing-extremum long-flat on BTCUSDT 1d bars
created: 2026-10-14
updated: 2026-10-14
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 1966-01-01
sources:
  - http://e-m-h.org/FaBl66.pdf
  - https://www.jstor.org/stable/2351744
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Alexander-Fama-Blume 5-percent filter trailing-extremum long-flat on BTCUSDT 1d bars

## Provenance

Primary source identity verified end to end (full text fetched live and read in full locally, 2026-10-14):

- Eugene F. Fama, Marshall E. Blume, `Filter Rules and Stock-Market Trading` — The Journal of Business, vol. 39, no. 1, part 2: Supplement on Security Prices (January 1966), 226–241. JSTOR stable `https://www.jstor.org/stable/2351744`.
- Actually-read text: `http://e-m-h.org/FaBl66.pdf`, fetched live 2026-10-14 as a 2,181,824-byte 17-page scanned PDF (SHA-256 `176b7aec…260e`), rasterized locally at 200 DPI and OCR-read in full (50,438 characters across all 17 pages, running heads `FILTER RULES AND STOCK-MARKET TRADING` / `THE JOURNAL OF BUSINESS` intact).
- Pinned rule mechanics (paper text, read verbatim modulo OCR spacing noise): `until its price moves down at least x per cent from a subsequent high, at which time simultaneously sell and go short. The short position is maintained until the daily closing price rises at least x per cent above a subsequent low at which time one covers and buys. Moves less than x per cent in either direction are ignored` — daily closing prices, path-dependent trailing extrema, symmetric long-short reversals.
- Pinned method (Notes to Table 1, read verbatim): `With an x per cent filter, an initial position is taken as soon as there is an up-move or a down-move (whichever comes first) where the total price change is equal to or greater than x per cent. The position is assumed to be taken on the first day for which the price change equals or exceeds the x per cent limit`; `The closing price on the day a position is opened defines a reference price: a peak in the case of a long transaction and a trough in the case of a short transaction`; each subsequent day checks the close against the reference (`x per cent below the reference (peak) price` / `x per cent above the reference (trough) price`), ratcheting the reference on new extremes; `Any positions open at the end of the sampling period are disregarded. Thus only completed transactions are included`; returns use daily compounding with dividends `positive for long transactions and negative for` short transactions (the short seller reimburses the lender).
- Pinned sample frame: `applied to series of daily closing prices for each of the individual securities of the Dow-Jones Industrial Average`; `initial dates of the samples vary from January, 1956, to April, 1958, but are usually about the end of 1957. The final date is always September 26, 1962. Thus there are thirty samples with 1,200 to 1,700 observations per sample`; `Twenty-four different filters ranging from 0.5 per cent to 50 per cent` (table headers 0.005–0.500, verified across Tables 1–3).
- Pinned Alexander lineage inside the paper: `Alexander reported tests of the filter technique for filters ranging in size from 5 to 50 per cent. The tests covered different time periods from 1897 to 1959 and involved closing "prices" for two indexes, the Dow-Jones Industrials from 1897 to 1929 and Standard and Poor's Industrials from 1929 to 1959`; Alexander's headline rule (secondary-verified verbatim via the Purdue CIBER working paper quoting Alexander 1961 p. 23): `if the market moves up 5% go long and stay long until it moves down 5% at which time sell and go short until it again moves up 5%. Ignore moves of less than 5%` — Sidney S. Alexander, `Price Movements in Speculative Markets: Trends or Random Walks`, Industrial Management Review 2 (May 1961), 7–26; `In his later paper [2, Table 1] Alexander reworked his earlier results` for discontinuity bias, finding the technique ex-commissions `typically superior to a buy-and-hold policy, at least for the period 1928-61` (dividend bias still uncorrected there); Mandelbrot `[10, pp. 417-18]` discontinuity critique preserved (`the purchase price will often be somewhat higher than the low plus x per cent, while the sale price will often be below the high minus x per cent`).
- Pinned headline findings fenced to the paper's samples — shorts: `the short positions initiated by the filter rule are usually disastrous for the investor. Only one security, Alcoa, has positive average returns per filter on short transactions`; all-securities short average `-.1279` versus buy-and-hold `.0986`; longs: all-securities average `.0822` versus buy-and-hold `.0986` (`thirteen securities have greater average returns per filter` on longs); with commissions `none of the filters consistently produce large returns. All filters below 12 per cent and above 25 per cent produce negative average returns per security after commissions`, 12–25% positives are `small when compared to .0986`; only four securities (`American Tel. and Tel., General Foods, Procter and Gamble, and Sears`) show positive average returns per filter with commissions; the 0.5% filter fired 12,514 transactions averaging `approximately 0.1 per cent on each complete transaction`, erased in practice by clearinghouse/specialist fees and idle funds (long-only 0.5% variant `.209` → `.125` after clearinghouse fees versus `.0986`); the 5% modified-reverse rule (short signals operated as longs) prints `.160` versus `.0986` before the same idle-funds and fee deductions; serial correlations agree in sign (daily positive in 22/30, avg `.026`, rank correlation `.76` with 0.5% filter returns; four-day negative in 21/30, avg `-.038`; nine-day negative in 24/30, avg `-.053`; 5% filter versus four-day rank correlation `.45`); terminal verdict: `for practical purposes the random-walk model is an adequate description of price behavior`. This record adopts zero performance numbers as expectations — they are fenced source-sample facts (see Negative evidence 1).
- Licence and rights: the record cites and normalizes the rule (short definitional phrases and Table 2/3 numeric facts only) and reproduces no figures, tables, or extended prose.

**Derived-record declaration (read before review):** this file specifies a separately identified derived executable strategy — the Alexander 5% filter's trailing-extremum reversal machine isolated as a single-asset long-flat rule — not a lossless reproduction of the 30-stock DJIA long-short study. Researcher-declared adaptations are exactly four: (1) the 5% size pinned from Alexander's headline/smallest filter (`corresponding to a 5% filter we might have the rule…`, filters `from 5 to 50 per cent`) among the 24 sizes Fama-Blume tested — any other x is a different, unpinned rule (see Negative evidence 2); (2) the short leg disabled: wherever the source would `simultaneously sell and go short`, this record goes flat and keeps tracking the trailing trough — the paper's own short-leg verdict (`usually disastrous`, `-.1279`) is the disclosed rationale, the long-short twin is falsification F3; (3) paper same-day-close fills moved to next-bar-open fills (the paper `assumed` first-day-close execution with no order timing; the shift is strictly more causal — see Execution assumptions); (4) single-asset BTCUSDT Binance venue with fixed 100%-equity 1× sizing and a structural warmup to the 2017-08-17 first close (the paper sizes no portfolio and ships no venue, sizing, or costs). The trailing-extremum state machine, the `equal to or greater than x per cent` trigger convention, the reference-ratchet, and the opposite-trigger exit are source-faithful.

Pre-write dedup (2026-10-14): working-tree case-insensitive filename searches for `filter` return only `bandpass-filter-*` (Ehlers DSP cycle filter, frequency-domain sign — never a price-percentage rule), `ichimoku-*-trend-filter-*` (cloud regime gate — never an extremum machine), and `mama-fama-hilbert-*` (Ehlers MAMA/FAMA indicator — a different Fama entirely); content searches for `alexander`, `fama-blume`, `fama and blume`, `filter rule`, `filter technique`, `trailing-extremum`, and `2351744` return zero strategy records. Open `research/*` PRs are only #48 (Larry Williams streak), #49 (Gaussian StochRSI), #63 (SuperTrend), #89 (Chandelier Exit), #92 (SSL channel) — different mechanisms and sources. Closest pool records differ in mechanism class: `bll-trb-200-percent-band-fixed-10d-*` fires on a fixed 200-day-window breakout with a fixed 10-day time exit (windowed level versus path-dependent running extremum; time exit versus opposite-trigger exit; two-sided versus long-flat); `bll-vma-*`, `darvas-box-*`, `donchian-20-10-*`, `turtle-system-2-*`, `nr7-*`, and `inside-bar-*` are all fixed-window constructions with no trailing-extremum state; the ATR-trailing family (`alphatrend-*`, `nick-rypock-*`, `ut-bot-*`, `triple-ema-volstop-*`) attaches volatility-unit stops to indicator entries, never a symmetric percentage-from-extremum entry-and-exit machine; formation-window reversals (`debondt-thaler-36m-*`, `jegadeesh-1990-*`, `lehmann-1990-*`, `etf-3day-*`) reverse fixed-horizon formations, never trailing-extremum triggers.

## Economic mechanism

### Source-reported

Gradual-adjustment trend persistence as the professionals' belief under test, fenced to the paper's 1956–1962 equity samples: the filter was `formulated ... to test the belief, widely held among market professionals, that prices adjust gradually to new information` via `certain trend generating facts` that `generate trends rather than instantaneous jumps because most of those trading in speculative markets have imperfect knowledge`; empirically the paper finds only two surviving traces — tiny-move persistence (`the conditional probability of a positive (negative) change tomorrow, given a positive (negative) change today, is greater than the unconditional probability, but the effect ... decreases very rapidly`) and intermediate-move negative dependence — both too small to survive costs, ending at `for practical purposes the random-walk model is an adequate description of price behavior`. All mechanism framing fenced to the paper's samples, never adopted as a crypto claim here.

### Research interpretation

Path-dependent trailing-extremum reversal, long-only, continuous-state cadence. Unlike every fixed-window breakout record the reference is not a rolling maximum but a running extremum that resets at each signal: after a long exit the market must prove itself up 5% from the post-exit lows (a V-shape re-entry the windowed records cannot express), and while long the exit trails every new high (no fixed hold, no indicator flip). Unlike formation-sign records (JT/TSMOM/Novy-Marx) there is no lookback window and no formation return — only the live distance from the running extreme. Unlike ATR-trailing records the trail is a fixed 5% of price, never a volatility multiple, and it doubles as the entry trigger on the other side. Unlike calendar/count/volume records no date, statistic, or volume is ever read. The bet, as derived, is purely that the oldest documented mechanical trend rule — which failed to beat buy-and-hold in 1960s equities — ports to BTCUSDT daily bars as a disciplined long-flat regime machine, with the paper's own negative verdict riding along undisguised.

## Signal

Exact rule as pinned (5% filter, trailing trough/peak state, close decisions, next-open fills, long-flat — any other percentage, reference convention, fill timing, or tie treatment is a different, unpinned rule):

- Bar grid: completed `1d` bars of BTCUSDT only. The signal reads `close` exclusively; `open` is the fill price, `high`/`low`/`volume` gate nothing.
- State variables (pinned): side ∈ {flat, long}; `trough` ( live while flat); `peak` (live while long). Both are trailing references over signal-day closes only.
- Initialization (pinned structural warmup): flat with `trough` = the first tape close (2017-08-17 C 4285.08, verified live 2026-10-14) — first entry needs a close at or above 4285.08 × 1.05 = 4499.334.
- While flat, on each completed daily close c: if c ≥ `trough` × 1.05 → enter long at the next bar's open (100% equity, 1×); set `peak` = c (the signal-day close, paper convention — never the fill price). Else if c < `trough` → `trough` = c (ratchet down; a first-move-down simply deepens the trough — the source would short here, explicitly disabled, never traded). Else → no action (`Moves less than x per cent in either direction are ignored`).
- While long, on each completed daily close c: if c ≤ `peak` × 0.95 → exit to flat at the next bar's open (full position); set `trough` = c (immediate re-arm, no cooldown). Else if c > `peak` → `peak` = c (ratchet up). Else → no action.
- Trigger convention (source-faithful): `equal to or greater than x per cent` — exact 5.000…% equality fires (measure-zero tie treatment pinned, never redefined).
- Risk legs (pinned absence, not invented): no stop, no target, no additional trailing, no opposite-signal concept beyond the 5% exit itself, no time exit (the paper disregards only end-of-sample opens; here the tape has no end — positions ride until the 5% trigger); every adverse excursion inside ±5% of the running extreme is ridden in full by construction.
- Direction: long-or-flat, derived-and-declared (the source reverses into shorts; the flat leg replaces every short leg one-for-one, and the short permission is explicitly unused — F3 tests exactly this adaptation). The futures venue is still pinned as the research market under the house overlay with the short permission simply unused, and a spot-only deployment expresses the identical event set.

## Required data

- Completed `1d` bars of BTCUSDT only: `close` as the sole signal input and `open` as the fill price (no `high`, no `low`, no `volume`, no funding, OI, mark/index price, liquidation, trade, order-book, on-chain, supply-feed, sentiment, macro, media-count, session-template, or cross-venue state gates any order). No multi-symbol, multi-timeframe, or external-feed dependency of any kind.
- Single decision grid: every daily-bar close evaluates at most one state transition; fills land on the next daily bar's open. At most one order exists per day boundary, so there is no same-bar dual-fire to sequence.
- Warmup: one bar (structural, not conventional): the 2017-08-17 close initializes the first trough; no lookback, no normalization, no estimated quantity. No repainting (references use closes at or before the decision close), no negative shift, no future reference, no full-sample anything (the signal is a running state machine, not an estimated statistic).

## Execution assumptions

- Research market: BTCUSDT Binance perpetual under the house overlay (declared port of the paper's 30-stock DJIA universe; no cross-venue equivalence claimed).
- Order timing (declared causal port; the paper `assumed` same-first-day-close execution): close decision with next-bar-open market fills, compatible 1:1 with the pinned Hummingbot backtester (package `20260920`, VERSION `dev-2.17.0`). No maker-touch, queue, or intrabar-path-dependent fill is claimed. The one-day fill lag versus the paper is a conservative friction, never an advantage claim.
- Cash leg: flat earns nothing by record rule. No T-bill, stablecoin-lending, funding-rebate, or synthetic yield is substituted; the dividend economics of the paper (long +, short −) collapse here to long-only exposure with no dividend analogue on the perpetual.
- Sizing/capital/costs: fixed 100%-equity single position, no adds, no leverage (1×, no margin concept), no compounding concept beyond equity. Derived evaluation must carry the explicit house overlay (pinned house fees plus historical funding treatment; no hypothetical zero funding claimed — long days carry realized funding, flat days carry none; the idle-trough periods that Fama-Blume flags as return diluters are genuine flat days here too). The downstream standard DCA matrix is a separately declared experiment, never strategy behavior here.
- Concurrency: at most one long position at any time; the state machine admits exactly one side, so overlapping entries are structurally impossible (no ignore-rule needed beyond the single-position book); after any exit the trough re-arms immediately (no cooldown specified — explicitly none, not invented). Single engine position; no shared portfolio state, no cross-sectional ranking, no multi-pair logic, no overlapping cohorts. The unused short permission requires no margin-short modeling. Safety orders: explicitly none.

## Evidence

### Source-reported

The paper ships every adopted headline fact quoted in Provenance: the daily-close long-short reversal mechanics with the `ignored` sub-threshold rule, the first-signal `equal to or exceeds` entry convention with `peak`/`trough` references and ratchets, the end-of-sample open-position disregard, the daily-compounding dividend-signed returns, the 30-security January-1956–April-1958 → September-26-1962 frame with 1,200–1,700 observations, the 24-filter 0.5%–50% grid, Alexander's 5–50% 1897–1959 index tests with their pre-correction profits, Alexander's discontinuity-bias rework with the 1928–61 ex-commission edge, the Mandelbrot jump critique, the `usually disastrous` short verdict (`-.1279` versus `.0986`, Alcoa the lone short-positive), the long average (`.0822` versus `.0986`, 13/30 beating), the four commission-surviving securities, the below-12%/above-25% commission-negative bands with small 12–25% positives, the 12,514-transaction 0.5% churn (`approximately 0.1 per cent on each complete transaction`), the `.209` → `.125` clearinghouse haircut on the long-only 0.5% variant, the `.160` modified-reverse 5% print before idle-funds deductions, the serial-correlation correspondence (`.76` / `.45` rank correlations), and the `adequate description` random-walk verdict. It ships zero adopted performance numbers for this record: every mean, count, and comparison describes its equity samples, never a single-asset BTCUSDT derivative — this record claims no source-reported performance and no reproduced performance.

### Independently reproduced

Not independently reproduced.

### Negative evidence

1. Negative headline fenced: the source's tradable conclusion is that no filter beats buy-and-hold after realistic costs — every mean, t-flavoured comparison, transaction count, and dollar figure belongs to 1956–1962 DJIA stocks, none transfers to BTCUSDT, and none is adopted as an expectation. Any dispute over exact magnitudes is decided against this record, never patched by inference.
2. Threshold-choice derivation disclosed: 5% is a researcher pin from Alexander's headline/smallest filter among 24 paper-tested sizes (0.5%–50%). A 0.5%, 1%, 12%, or 50% variant would be a different, unpinned rule — F2 tests exactly the smallest-filter alternative the paper discusses, and the 50% corner (4 transactions across 30 stocks/5y per Table 3) is fenced as statistically vacuous by the paper's own `probably not reliable` note on the largest filters.
3. Disabled-short derivation disclosed: the source's tradable object reverses into shorts; this record flats instead, although the idle-trough periods dilute the long-only print exactly the way the paper warns (`funds will probably be idle a substantial fraction of the time`). F3 runs the source-native long-short twin to price this adaptation.
4. Fill-lag derivation disclosed: the paper executes `on the first day for which the price change equals or exceeds` the limit; this record fills one bar later at the next open. The lag is a declared friction (gap-against-entry on breakouts, gap-for-exit on breakdowns), never paper-native.
5. Cross-market, cross-era port unevidenced: 1960s dividend-paying single-name equities versus a 24/7 no-dividend crypto perpetual, sixty years later, with no corporate-action calendar, no specialist, and volatility an order of magnitude higher — the port bets on rule-structure persistence, not on any verified crypto analogue, and the paper's verdict says the structure earned nothing even at home.
6. Derivation boundary fenced: the only non-paper behavior is the four declared adaptations (5% pin, flat-for-short, next-open fills, single asset plus fixed sizing plus structural warmup plus house costs); the trailing-extremum machine, the trigger convention, the ratchets, and the opposite-trigger exit are source-faithful. This record is therefore never evidence that the paper's equity study passes.

## Falsification plan

Research-defined thresholds only (never substitutes for missing rules); global no-retuning rule: 5% filter / trailing trough-peak state / `equal-to-or-greater` trigger / close decisions / next-open fills / sequential single-position 100%-equity 1× long-flat / `1d` BTCUSDT are frozen.

- F1 — Buy-and-hold relevance: an always-long twin (same fills and costs, never exiting) must not improve net expectancy; fail ⇒ the paper's verdict replicates here and the 5% machine does no work over the baseline it failed to beat at home.
- F2 — Threshold relevance: a 0.5% filter twin (the paper's most-discussed small size, same machine and fills) must not improve net expectancy; fail ⇒ the small-move persistence the paper documents ports better than the pinned headline size and the 5% pin points the wrong way.
- F3 — Adaptation cost: a source-native long-short twin (short where the paper shorts, same grid and fills, dividends moot) must not improve net expectancy; fail ⇒ disabling the short leg destroys the machine's value and the flat-for-short derivation is the wrong port (the paper's `-.1279` short verdict notwithstanding).
- F4 — Mechanism placebo: a fixed-window breakout twin (past-200-close high ×1.01 entry, fixed 10-day time exit — the BLL-TRB shape already in-pool, same fills and costs) must not match-or-beat the trailing-extremum machine per trade; fail ⇒ windowed breakouts explain any result, not the path-dependent extremum state.

## Crypto portability

Pinned to BTCUSDT Binance perpetual under the house overlay (decision grid every daily-bar close on `1d` bars; fills at next-bar opens; no venue-specific read). The arithmetic ports across perpetual venues without structural change (no corporate-action or calendar adjustment exists to recheck; the dividend ± treatment collapses to nothing on a perpetual). No short leg exists to port (a spot-only deployment expresses the identical event set — pinned, not approximated). No funding-dependent leg, no stablecoin-specific assumption, no volume-dependent leg, no session-template, no media-count input, no cross-venue state. Extension to other house-universe assets, filter sizes, reference conventions, fill timings, or timeframes would be a different, unpinned claim.

## Limitations

- Single-asset port: the paper's evidence is a 30-stock 1956–1962 study whose headline is failure; BTCUSDT 5%-filter behavior is unevidenced by the source and may differ arbitrarily — no performance is claimed here for exactly this reason.
- Mechanism mismatch: whatever gradual-adjustment persistence sat behind 1960s equities has no established crypto analogue (24/7 global tape, no open/close session, non-U.S. participant majority, perpetual-funding holders, stablecoin quote, thin early history, volatility an order of magnitude above 1960s single names) — and the paper concludes the dependence was unexploitable even contemporaneously.
- Threshold fragility: 5% is one of 24 tested sizes; BTC daily noise dwarfs 1960s single-name noise, so the machine may churn (1957-style 12,514-transaction grind at small sizes) or starve (4-transaction vacuity at large sizes) — pinned, not tuned.
- Fill-lag bleed: every signal pays the overnight/next-day gap versus the paper's assumed close; fast continuation markets tax entries and fast reversals subsidize exits asymmetrically — declared, not modeled away.
- Warmup cost: everything before the first ≥5% post-2017-08-17 trough confirmation is flat by record rule — pinned, not recovered.
- No price stop, no non-trigger exit: adverse excursion inside the ±5% band has no guardrail; the next decision is always tomorrow's close by construction.

## Implementation status

not-implemented. No Hummingbot controller/executor has been written for this record; the Execution assumptions section names the exact pinned engine path (package `20260920`, VERSION `dev-2.17.0`, every-close decisions on completed `1d` bars, next-bar-open market fills, single-asset 100%-equity 1× long-or-flat) that a future implementation must target, with representative event-level Qlib/Hummingbot parity required before any mass screening.

## Adoption boundary

research-only. Not approved for Paper, Testnet, or Live trading. PASS means the declared derived strategy is causally expressible under the pinned Hummingbot model — not profitable, not Qlib-paritied, not source-equivalent, not live-tradable.

## Related Wiki records

None.

## Sources

- Fama, Eugene F. and Blume, Marshall E. (1966). Filter Rules and Stock-Market Trading. The Journal of Business 39(1), Part 2, 226–241. https://www.jstor.org/stable/2351744 (full text fetched live 2026-10-14 via http://e-m-h.org/FaBl66.pdf, 2,181,824-byte 17-page scan, SHA-256 `176b7aec…260e`, OCR-read in full locally — 50,438 characters)
- Alexander, Sidney S. (1961). Price Movements in Speculative Markets: Trends or Random Walks. Industrial Management Review 2, 7–26 (rule text and 5–50% range verified via the paper's own account plus the Purdue CIBER working-paper verbatim quote of p. 23, cross-checked 2026-10-14)
- Binance public spot kline feed (verified live 2026-10-14: tape-open continuity 2017-08-17 O 4261.48 C 4285.08 → 2017-08-18 O 4285.08 C 4108.37 → 2017-08-19 O 4108.37 C 4139.98; first-trough initialization close 4285.08, first-entry threshold 4499.334)
