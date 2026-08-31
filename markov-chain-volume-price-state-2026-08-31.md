---
schema: strategy-research-record-v1
title: "Markov Chain Volume-Price State Strategy"
created: 2026-08-31
updated: 2026-08-31
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - markov-chain
status: research-only
confidence: medium
source_as_of: 2026-01-01
sources:
  - https://github.com/jehumtine/markov-chain-trading-strategy
  - https://github.com/jehumtine/markov-chain-trading-strategy/blob/11286554f829529a3c9a4dfb6439a1decbec42b9/data_processor.py
  - https://github.com/jehumtine/markov-chain-trading-strategy/blob/11286554f829529a3c9a4dfb6439a1decbec42b9/backtester.py
  - https://github.com/jehumtine/markov-chain-trading-strategy/blob/11286554f829529a3c9a4dfb6439a1decbec42b9/main.py
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: true
contradictions:
  - "The repository's 4h resample is timestamped at the start of each 4h bin and merged backward into lower-timeframe rows, which can expose completed 4h information before it is causally available."
---

# Markov Chain Volume-Price State Strategy

## Provenance
- Repository URL: https://github.com/jehumtine/markov-chain-trading-strategy
- Full commit SHA: 11286554f829529a3c9a4dfb6439a1decbec42b9
- Exact file path: `data_processor.py`, `backtester.py`, `main.py`
- Relevant immutable source URLs:
  - https://github.com/jehumtine/markov-chain-trading-strategy/blob/11286554f829529a3c9a4dfb6439a1decbec42b9/data_processor.py
  - https://github.com/jehumtine/markov-chain-trading-strategy/blob/11286554f829529a3c9a4dfb6439a1decbec42b9/backtester.py
  - https://github.com/jehumtine/markov-chain-trading-strategy/blob/11286554f829529a3c9a4dfb6439a1decbec42b9/main.py

## Economic mechanism
### Source-reported
The advent of algorithmic trading has fundamentally transformed financial markets... This paradigm shift has spurred a continuous search for sophisticated quantitative models that can identify and exploit market inefficiencies... The core of the strategy is to discretize market behavior into a finite set of states based on price action and trading volume. By analyzing historical data, the model identifies "useful sequences" of states that have a high probability of preceding a specific bullish or bearish movement. These sequences are then used to generate trading signals.

### Research interpretation
Market behavior can be discretized into states representing price momentum (normalized by ATR) and volume regimes (relative to SMA). Sequences of these states exhibit short-term persistence or identifiable transition patterns (Markov property) that predict future short-term directional movement. The strategy exploits these non-random transition probabilities in cryptocurrency price and volume action to forecast immediate market direction.

## Signal
- The strategy discretizes each candle into one of 12 states:
  - Price state (0 to 3) is determined by `diff_close / atr`. (0: strong uptrend, 1: mild uptrend, 2: mild downtrend, 3: strong downtrend).
  - Volume state (0 to 2) is determined by comparing current volume to a rolling 24-period volume SMA with high/low multipliers.
  - Final state = `price_state * 3 + volume_state`.
- **Lookback / Training**: A transition matrix is built empirically from historical state sequences of length `sequence_length` to the subsequent state.
- **Signal formation**: If the probability of transitioning from the current sequence of states to a bullish state exceeds a defined `min_signal_probability`, a buy signal is generated. A bearish expected transition generates a sell signal.
- **Entry**: Buy on a long signal.
- **Exit**: Exit a long position if a sell signal occurs AND the position is currently profitable (`current_price > buy_price`). Or exit via dynamic stop-loss / take-profit based on ATR at entry.
- **Parameters**: `price_state_threshold`, `volume_high_multiplier`, `volume_low_multiplier`, `atr_period`, `sequence_length`, `min_signal_probability`, `sl_multiplier`, `tp_multiplier`.

## Required data
- **Market type:** The source repository consumes cryptocurrency OHLCV files but does not establish a venue/contract-type requirement; Spot vs perpetual portability must be tested rather than assumed.
- Timeframe: Tested on 1h, with state transitions mapped based on 4h resampled data (in source code).
- OHLCV fields.

## Execution assumptions
- The backtester evaluates the sequence ending before index `i + sequence_length` and uses price at `i + sequence_length`, i.e. next-row execution relative to the sequence. However, the 4H state construction itself has a separate timestamp-alignment concern described below.
- Stop-loss and take-profit require intra-bar or tick-level simulation for precise fills.
- Backtest includes assumptions for commissions and slippage.
- Position sizing uses an equal division of available capital across maximum concurrent positions.

## Evidence
### Source-reported
The repository README reports for SOL/USDT 1h data (2019-2024): Sharpe Ratio 2.91, Sortino Ratio 261.22, Win Rate 72.70%, Max Drawdown 12.5%, Total Trades 111, and states that hyperparameter optimization was applied via Walk-Forward Analysis. The current pinned `main.py` default invocation instead references a BTC 2019-2024 output directory, so the README performance claim should not be silently attributed to that default run.

### Independently reproduced
Not independently reproduced.

### Negative evidence
None identified in the reviewed sources; absence is not evidence of no negative result. High reported Sharpe combined with a low number of trades (111 over 5 years on 1h data) suggests high selectivity or potential overfitting to specific market regimes despite Walk-Forward Analysis claims.

## Falsification plan
- Construct explicit PyBroker implementation of the 12-state Markov chain logic.
- Run rigorous out-of-sample testing on non-optimized pairs (e.g., BTC, ETH) across varying market regimes.
- Verify if transition probabilities are stable over time or if the matrix requires constant refitting.
- Stress test the "exit on sell signal only if profitable" rule, as it acts as an asymmetrical holding mechanism that may heavily skew win rate.

## Crypto portability
direct

## Limitations
- underspecified robustness of transition probabilities across different assets.
- not independently reproduced.
- **Material source-code caveat:** `merge_4h_state()` uses pandas `resample('4h')` with default left-edge timestamps, computes each completed 4H OHLCV/state, then `merge_asof(..., direction='backward')` onto the lower-timeframe dataframe. Without shifting the 4H state to its availability time, lower-timeframe rows inside a 4H bin can receive information from that bin's eventual close/high/low/volume. Any reproduction must correct and separately test this look-ahead risk before interpreting the reported backtest evidence.
- Transition-matrix training must also remain strictly isolated from the evaluation window.

## Implementation status
not-implemented

## Adoption boundary
This is research material only. A record being present in this repository does not mean: profitable, validated alpha, approved for implementation, approved for paper trading, approved for testnet, or approved for live trading.

## Related Wiki records
None

## Sources
- https://github.com/jehumtine/markov-chain-trading-strategy
