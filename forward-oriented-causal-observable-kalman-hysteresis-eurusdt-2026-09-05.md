---
schema: strategy-research-record-v1
hb_ready_status: NOT_LOSSLESS
title: Forward-Oriented Causal Observables via Kalman-Stabilized Multi-Feature Aggregation and Adaptive Phase-Lead Derivative Operator on High-Frequency
  EURUSDT
created: '2026-10-08'
updated: '2026-10-08'
type: strategy-research-record
tags:
- quant
- strategy-research
- source-backed
status: research-only
confidence: medium
source_as_of: '2026-10-08'
sources:
- https://arxiv.org/abs/2512.24621v1
- https://github.com/HCH725/alpha-strategy-research/blob/8dfde96fac5a470647e75d8a9e8eada1d5655ebb/forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05.md
- HCH725/validated-survivor-research commit 15c0a95162b60a664b43ac60157225c7300ad789
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forward-Oriented Causal Observables via Kalman-Stabilized Multi-Feature Aggregation and Adaptive Phase-Lead Derivative Operator on High-Frequency EURUSDT

## Provenance

- Family identity：`forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05`；本次 consolidation 只按原 baseline family_id，不依 Sharpe 重新排名／挑選。
- Primary source：https://arxiv.org/abs/2512.24621v1。
- 既有 source-backed 研究紀錄：commit `8dfde96fac5a470647e75d8a9e8eada1d5655ebb`，`forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05.md`，Git blob `7a42bfc1ef89cec9e5981965fd488aa43b480657`。 本紀錄未捏造不存在的逐檔 reviewed_commit；採可回收的最初 root-record commit。
- `quant/forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05.md` 的 raw SHA-256 為 `eabe95e74dc1d876c600503ea72e2823c1e06fe918f5434704a9ed156e8e6c0a`；它在 review-state 的 `ingested_wiki_records` 中，state 最後審查 commit 為 `2799e34c5c7f8d6f7036e35d9ae7468832712c97`。這是 ingestion provenance，不是本輪 source parity 或逐檔新審查；Wiki bytes 不冒稱與原 Git blob 相同。
- Historical input：`HCH725/validated-survivor-research` commit `15c0a95162b60a664b43ac60157225c7300ad789` 的 `survivors/<survivor_id>/baseline.json`，本家族 10 筆，cohorts：`BNBUSDT/1d`, `BNBUSDT/4h`, `BTCUSDT/1d`, `BTCUSDT/4h`, `ETHUSDT/1d`, `ETHUSDT/30m`, `ETHUSDT/4h`, `SOLUSDT/1d`, `SOLUSDT/1h`, `SOLUSDT/4h`。
- Derived leaderboard：同一 repo `leaderboard/leaderboard.json`，raw SHA-256 `e8fdd38c8468960eee5b574e93d27615635bcb266fe481ab8c1409720d96c42e`；它不是 frozen bundle 本身，也不是採用 gate。

- Source-to-legacy-Qlib mapping gap：family 名称、strategy flags/case IDs 或舊 PASS 不證明原文 source-native signal、模型 weights、universe、因果時序與執行機制一致。除本紀錄明列已釘選的程式規則外，沒有補造代碼對照。paper方法、研究解讀與historical DCA分層保留；尚未證明多個 legacy codes 對應不同完整 core mechanisms，故不任意拆成新策略。

## Economic mechanism

### Source-reported

來源將 heterogeneous candle micro-features 先 causally center、線性混合與一維 Kalman stabilization，再與 smoothed causal derivative 以 adaptive operator 合成，減少 filter phase lag。

### Research interpretation

這是方法／假說的普通研究封存，不是把歷史 survivor 標籤當成新 alpha。機制層分類與單筆 cohort 的 DCA 收益不同；statistical forecast、risk allocator 或負面 study 均不得被默換成已驗證的 crypto 交易規則。

## Signal

歷史研究紀錄列 RSI(14)、MFI(14)、MACD(12,26,9) histogram、Bollinger %B(20,2σ)、expanding median centering、q=0.01/r=0.1 Kalman 與 θ=0.06 long/flat hysteresis。這些是可追溯的舊研究轉錄，非本輪全文/程式逐式復驗；derivative smoothing/initialization、source-to-legacy signal_rule_version=1 及不同 symbols/timeframes 的 mapping 仍未證實。

## Required data

來源本身是 EURUSDT 1-minute OHLCV 的 high-frequency application；歷史 baseline 的 BTC/ETH/BNB/SOL 與較慢 cohort 不得被誤寫成原文的 instrument/timeframe。

Historical cohort resolution、parameters 與 data cutoff 以 Evidence 的原 JSON 為準，不補齊不存在的字段，不降採樣、不改 symbol。baseline 不含完整行情 manifest、signal arrays、model checkpoints 或逐筆 trade ledger；它不是可直接執行的策略定義。

## Execution assumptions

舊研究紀錄載 frictionless long/flat、bar-close decision / next-open execution 與 FX-style session exclusions。不能以現行 same-bar-close 替代 next-open 而稱無損。

Historical DCA 參數只代表當時研究配置，並非 paper 原生規則，也不是目前 house overlay。未重新量測 fees、funding、margin/liquidation、slippage、intrabar path 或 fills；hash references 不是原資料 bytes 已重新驗證的宣告。

## Evidence

### Source-reported

本輪讀取 versioned primary landing 的 abstract，確認上述 method-level 主張；更細的 signal 配置以釘選原研究紀錄為轉錄來源，未宣稱已重新逐式審閱整篇 methods 或 source code。原文績效不是下列 crypto baseline metrics。

### Independently reproduced

Not independently reproduced. 本輪只驗 source identity／文件轉錄，沒有 Qlib rerun、Hummingbot reproduction、Paper 或 Testnet。

### Negative evidence

來源摘要明示後續 regime shifts 下 performance degradation；causal filter 不保證經濟有效。高周轉與 frictionless evaluation 的可交易性尚未確認；不沿用舊 Wiki 的未核實 monthly-cost 算術。

### HISTORICAL QLIB SURVIVOR EVIDENCE — 非目前 Hummingbot reproduction

以下每個 baseline JSON 保留全部原鍵／數值／null／巢狀結構，唯一刪除 top-level `bundle_path` 的機器絕對路徑。bundle 邏輯定位仍可由 family_id / round_id / run_id 與 survivor ID 找到；不假裝本輪讀取已退役結果盤。每筆獨立列 raw baseline-file SHA-256，它與 `params_sha256`、`bundle_sha256`（檔案 bytes）、`bundle_identity_sha256`（歷史 identity recipe）互不相同。

鍵名 `net_pnl` / `sharpe` / `max_dd_pct` / `annualized_return` 原樣保留，不重命名成 ROI、不對 MDD 改 sign／比例／百分點、不跨 lineage 默認同一 annualization。baseline 欄位缺席不同於 null；不從另一層悄悄補值。`source_verdict: PASS` 與 `neighbourhood.passed` 都是 HISTORICAL，不能解讀成今日 efficacy、source parity 或 HB_READY PASS。

每筆另列 `leaderboard_snapshot`：`additional_fields` 為 derived index 額外欄位，`baseline_field_overrides` 為該 index 與 baseline 不同的完整 top-level 值；空 object 明示無差異。兩者都不回寫 baseline。僅非 null 的 `evidence_manifest_path` 去除原 results-root 絕對前綴，保留 `_survivors/...` 相對 locator；null 留 null。rank / top10 / package PRESENT / FROZEN_ONLY 只是當時 derived state，不能解讀為今天 evidence package bytes 存在或新 forward evidence。

#### sv-1f72d5690f5cde07 — HISTORICAL

Baseline file SHA-256：`10ff0ff4142f33f0965bdc0c429f3b6a68e8bb3e704d041d3709c2ab8dd443fa`；archive locator：`survivors/sv-1f72d5690f5cde07/baseline.json`。

```json
{"survivor_id":"sv-1f72d5690f5cde07","family_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05","round_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05-r1","run_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05-r1-u2","kanban_task_id":null,"cohort":"ETHUSDT/30m","symbol":"ETHUSDT","timeframe":"30m","challenger_of":null,"strategy_params":{"signal_rule_version":1},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.1,"breakeven_tp_pct":0.01,"invalidation_pct":0.1},"params_sha256":"sha256:8fbefafc1390c583ffe5dfd65f915234c3ae5efe5ba35d495fcf438879cd9aea","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:a4055b16c39091d0b5203d9abb14b49cb25e856fa03174d217a094f90abe65bc","bundle_identity_sha256":"sha256:8ef1135c007194ab7b0db4b66a551a12d36722e6dce6dd977ffead8cf1b145a2","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":2393.002910175395,"sharpe":1.3239259384380235,"episodes":1265,"max_dd_pct":1.5021001367147464},"oos":{"net_pnl":525.2222461939909,"sharpe":1.2348232729291424,"episodes":332,"max_dd_pct":1.2109421460899592},"full":{"net_pnl":2916.810411190717,"sharpe":1.3119915044160309,"episodes":1596,"max_dd_pct":1.9483061160009918,"annualized_return":0.019957545893316997,"avg_trades_per_year":339.90612244897954},"robustness":{"fee_2x":{"net_pnl":57.950073192292415,"sharpe":0.025741380950598938,"max_dd_pct":3.66872954752687},"funding_2x":{"net_pnl":2872.6275057312037,"sharpe":1.2919127396431687,"max_dd_pct":1.9566588111586574},"entry_delay_1_bar":{"net_pnl":599.472843444057,"sharpe":0.20612478122408512,"max_dd_pct":4.33613569850836},"slippage_2ticks":{"net_pnl":2879.111941216979,"sharpe":1.2955919768798556,"max_dd_pct":1.9525338067803413}},"robustness_stress_floor_net_pnl":57.950073192292415,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":0.75,"passed":true,"neighbours":4,"agreeing":3}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-1f72d5690f5cde07","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":59,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-32288b624e5b352d — HISTORICAL

Baseline file SHA-256：`1495ac4499d6c8ca709f5ad967c0de40eafdfdabd9398d4954402599e8ee7b13`；archive locator：`survivors/sv-32288b624e5b352d/baseline.json`。

```json
{"survivor_id":"sv-32288b624e5b352d","family_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05","round_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05-r1","run_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05-r1-u2","kanban_task_id":null,"cohort":"BTCUSDT/1d","symbol":"BTCUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"signal_rule_version":1},"dca_params":{"spacing_pct":0.02,"size_multiplier":1.0,"breakeven_tp_pct":0.01,"invalidation_pct":0.05},"params_sha256":"sha256:f29026490f22ab696211d0c4e7ad172e0435d420edbc3dee3fcde280c341d2ee","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:a4055b16c39091d0b5203d9abb14b49cb25e856fa03174d217a094f90abe65bc","bundle_identity_sha256":"sha256:8ef1135c007194ab7b0db4b66a551a12d36722e6dce6dd977ffead8cf1b145a2","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":284.67253235124696,"sharpe":6.028265568007256,"episodes":23,"max_dd_pct":0.0},"oos":{"net_pnl":98.13133467147442,"sharpe":5.5857880746695034,"episodes":7,"max_dd_pct":0.0},"full":{"net_pnl":382.80386702272136,"sharpe":5.8307698482341275,"episodes":30,"max_dd_pct":0.0,"annualized_return":0.002704029760037585,"avg_trades_per_year":6.389212827988338},"robustness":{"fee_2x":{"net_pnl":339.58892063097954,"sharpe":5.8225206806091,"max_dd_pct":0.0},"funding_2x":{"net_pnl":378.9298969535399,"sharpe":5.758047918368048,"max_dd_pct":0.0},"entry_delay_1_bar":{"net_pnl":365.91371887365307,"sharpe":4.8609323686188395,"max_dd_pct":0.0},"slippage_2ticks":{"net_pnl":382.6967127318009,"sharpe":5.831333409331172,"max_dd_pct":0.0}},"robustness_stress_floor_net_pnl":339.58892063097954,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":5,"agreeing":5}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-32288b624e5b352d","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":19,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-323e26539a865132 — HISTORICAL

Baseline file SHA-256：`f6cb57c5541d238024d23634c55eff90dc93297e8240ce584896cbfd8a198d11`；archive locator：`survivors/sv-323e26539a865132/baseline.json`。

```json
{"survivor_id":"sv-323e26539a865132","family_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05","round_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05-r1","run_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05-r1-u2","kanban_task_id":null,"cohort":"SOLUSDT/4h","symbol":"SOLUSDT","timeframe":"4h","challenger_of":null,"strategy_params":{"signal_rule_version":1},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.0,"breakeven_tp_pct":0.01,"invalidation_pct":0.05},"params_sha256":"sha256:efac001d959af4fee84c1b6048cc74de0d074db056d65c65e59488fc46ed0452","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:a4055b16c39091d0b5203d9abb14b49cb25e856fa03174d217a094f90abe65bc","bundle_identity_sha256":"sha256:8ef1135c007194ab7b0db4b66a551a12d36722e6dce6dd977ffead8cf1b145a2","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":2430.5059378039587,"sharpe":1.917074624050189,"episodes":170,"max_dd_pct":2.167745086722649},"oos":{"net_pnl":658.0876711859042,"sharpe":6.27123807420034,"episodes":41,"max_dd_pct":0.17146468437526963},"full":{"net_pnl":3070.699910738455,"sharpe":2.1363429059509627,"episodes":210,"max_dd_pct":2.1257811324330826,"annualized_return":0.020971228383764418,"avg_trades_per_year":44.724489795918366},"robustness":{"fee_2x":{"net_pnl":2573.908488012804,"sharpe":1.7773509832560765,"max_dd_pct":2.2308376784024286},"funding_2x":{"net_pnl":3055.3457929009314,"sharpe":2.120785251296099,"max_dd_pct":2.126768551963001},"entry_delay_1_bar":{"net_pnl":3384.814926054337,"sharpe":4.30332312920322,"max_dd_pct":0.6586981544781642},"slippage_2ticks":{"net_pnl":3006.339892519221,"sharpe":2.0600611018290675,"max_dd_pct":2.20885524798476}},"robustness_stress_floor_net_pnl":2573.908488012804,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":4,"agreeing":4}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-323e26539a865132","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":15,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-7194dc610fe3683e — HISTORICAL

Baseline file SHA-256：`a0e2ed98fbe04e1fd5ada47de4bd9ce83d1ca1f55093529fd4076e3d5e3a4a36`；archive locator：`survivors/sv-7194dc610fe3683e/baseline.json`。

```json
{"survivor_id":"sv-7194dc610fe3683e","family_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05","round_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05-r1","run_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05-r1-u2","kanban_task_id":null,"cohort":"SOLUSDT/1h","symbol":"SOLUSDT","timeframe":"1h","challenger_of":null,"strategy_params":{"signal_rule_version":1},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.1,"breakeven_tp_pct":0.01,"invalidation_pct":0.05},"params_sha256":"sha256:065b6a5b08aa17a165232194fb2be06f55e35a8c2556648ea95fb61c2654f711","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:a4055b16c39091d0b5203d9abb14b49cb25e856fa03174d217a094f90abe65bc","bundle_identity_sha256":"sha256:8ef1135c007194ab7b0db4b66a551a12d36722e6dce6dd977ffead8cf1b145a2","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":4637.325454914612,"sharpe":2.345694624856194,"episodes":651,"max_dd_pct":1.7418770794233305},"oos":{"net_pnl":642.9922943715633,"sharpe":1.7359907078680177,"episodes":163,"max_dd_pct":1.095631510671888},"full":{"net_pnl":5280.317749286174,"sharpe":2.2420140536048696,"episodes":814,"max_dd_pct":1.7233399204579953,"annualized_return":0.03513202527097903,"avg_trades_per_year":173.3606413994169},"robustness":{"fee_2x":{"net_pnl":3466.3358508505175,"sharpe":1.4597872029504018,"max_dd_pct":1.9227951249519835},"funding_2x":{"net_pnl":5263.10326789416,"sharpe":2.2343034988309336,"max_dd_pct":1.724046667766486},"entry_delay_1_bar":{"net_pnl":4803.914667031215,"sharpe":1.9178138830327351,"max_dd_pct":1.2629718794882399},"slippage_2ticks":{"net_pnl":3521.0977651793014,"sharpe":1.0981162958116764,"max_dd_pct":3.0802875663641647}},"robustness_stress_floor_net_pnl":3466.3358508505175,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":4,"agreeing":4}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-7194dc610fe3683e","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":52,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-85d5c2df2ce1abcc — HISTORICAL

Baseline file SHA-256：`aa1014a2235d1dd8f9d7fc4b0b8845084ba5a835e511362a06778b3295e1389c`；archive locator：`survivors/sv-85d5c2df2ce1abcc/baseline.json`。

```json
{"survivor_id":"sv-85d5c2df2ce1abcc","family_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05","round_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05-r1","run_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05-r1-u2","kanban_task_id":null,"cohort":"BNBUSDT/4h","symbol":"BNBUSDT","timeframe":"4h","challenger_of":null,"strategy_params":{"signal_rule_version":1},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.0,"breakeven_tp_pct":0.01,"invalidation_pct":0.05},"params_sha256":"sha256:efac001d959af4fee84c1b6048cc74de0d074db056d65c65e59488fc46ed0452","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:a4055b16c39091d0b5203d9abb14b49cb25e856fa03174d217a094f90abe65bc","bundle_identity_sha256":"sha256:8ef1135c007194ab7b0db4b66a551a12d36722e6dce6dd977ffead8cf1b145a2","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":1905.29962559619,"sharpe":4.493579602905544,"episodes":160,"max_dd_pct":0.26735977701123437},"oos":{"net_pnl":406.35490634941357,"sharpe":2.981738689680687,"episodes":42,"max_dd_pct":0.4521083204764016},"full":{"net_pnl":2302.6694399532958,"sharpe":4.114825120238708,"episodes":201,"max_dd_pct":0.42564571664012113,"annualized_return":0.015874624034125207,"avg_trades_per_year":42.80772594752186},"robustness":{"fee_2x":{"net_pnl":1924.3281376365137,"sharpe":3.4736094865960627,"max_dd_pct":0.49252439685974725},"funding_2x":{"net_pnl":2301.0755486589956,"sharpe":4.116881312940912,"max_dd_pct":0.43034168465868},"entry_delay_1_bar":{"net_pnl":2329.5610156632733,"sharpe":3.62542392802337,"max_dd_pct":0.6538833783314726},"slippage_2ticks":{"net_pnl":2291.631883020597,"sharpe":4.089499363212747,"max_dd_pct":0.4283037533552428}},"robustness_stress_floor_net_pnl":1924.3281376365137,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":0.75,"passed":true,"neighbours":4,"agreeing":3}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-85d5c2df2ce1abcc","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":37,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-abfc42191930b1a6 — HISTORICAL

Baseline file SHA-256：`91a70fe5db021a250b60d6b75a5184bfd3ca314a5389b3a377d7e0fdbcd724fe`；archive locator：`survivors/sv-abfc42191930b1a6/baseline.json`。

```json
{"survivor_id":"sv-abfc42191930b1a6","family_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05","round_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05-r1","run_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05-r1-u2","kanban_task_id":null,"cohort":"BNBUSDT/1d","symbol":"BNBUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"signal_rule_version":1},"dca_params":{"spacing_pct":0.04,"size_multiplier":1.0,"breakeven_tp_pct":0.02,"invalidation_pct":0.1},"params_sha256":"sha256:e40df9d6a1c67927a18ab61e96bd35ccdb75759a93f2e09efeef7550399b9864","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:a4055b16c39091d0b5203d9abb14b49cb25e856fa03174d217a094f90abe65bc","bundle_identity_sha256":"sha256:8ef1135c007194ab7b0db4b66a551a12d36722e6dce6dd977ffead8cf1b145a2","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":802.9606992821983,"sharpe":6.621985133946868,"episodes":28,"max_dd_pct":0.0},"oos":{"net_pnl":93.27499842971535,"sharpe":93.15645345058088,"episodes":5,"max_dd_pct":0.0},"full":{"net_pnl":877.2556057196059,"sharpe":6.187271289252075,"episodes":32,"max_dd_pct":0.0,"annualized_return":0.006157307891717423,"avg_trades_per_year":6.815160349854227},"robustness":{"fee_2x":{"net_pnl":830.7962098441399,"sharpe":6.187231254850891,"max_dd_pct":0.0},"funding_2x":{"net_pnl":882.1788563824512,"sharpe":6.161177908171674,"max_dd_pct":0.0},"entry_delay_1_bar":{"net_pnl":746.6789129821263,"sharpe":5.402398342433042,"max_dd_pct":0.05131714829692619},"slippage_2ticks":{"net_pnl":876.0479415253719,"sharpe":6.190138064114024,"max_dd_pct":0.0}},"robustness_stress_floor_net_pnl":746.6789129821263,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":0.8,"passed":true,"neighbours":5,"agreeing":4}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-abfc42191930b1a6","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":3,"in_top10":true,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-bef94903d52ee124 — HISTORICAL

Baseline file SHA-256：`bb898b3ec5b242026a7965231d1275eb90b1d16b7e1ac81f3e777ded950e3413`；archive locator：`survivors/sv-bef94903d52ee124/baseline.json`。

```json
{"survivor_id":"sv-bef94903d52ee124","family_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05","round_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05-r1","run_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05-r1-u2","kanban_task_id":null,"cohort":"ETHUSDT/1d","symbol":"ETHUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"signal_rule_version":1},"dca_params":{"spacing_pct":0.04,"size_multiplier":1.0,"breakeven_tp_pct":0.02,"invalidation_pct":0.1},"params_sha256":"sha256:e40df9d6a1c67927a18ab61e96bd35ccdb75759a93f2e09efeef7550399b9864","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:a4055b16c39091d0b5203d9abb14b49cb25e856fa03174d217a094f90abe65bc","bundle_identity_sha256":"sha256:8ef1135c007194ab7b0db4b66a551a12d36722e6dce6dd977ffead8cf1b145a2","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":604.2266265640253,"sharpe":4.179822903338328,"episodes":22,"max_dd_pct":0.0},"oos":{"net_pnl":151.42813547696232,"sharpe":7.22287186278929,"episodes":5,"max_dd_pct":0.0},"full":{"net_pnl":755.6547620409876,"sharpe":4.484217490969408,"episodes":27,"max_dd_pct":0.0,"annualized_return":0.005312099146554283,"avg_trades_per_year":5.750291545189504},"robustness":{"fee_2x":{"net_pnl":715.2548552362972,"sharpe":4.482588072534897,"max_dd_pct":0.0},"funding_2x":{"net_pnl":751.8958215057846,"sharpe":4.4551393186031065,"max_dd_pct":0.0},"entry_delay_1_bar":{"net_pnl":93.02872274881284,"sharpe":0.06865764174890195,"max_dd_pct":1.9816350235485898},"slippage_2ticks":{"net_pnl":755.4684823425202,"sharpe":4.484066098069668,"max_dd_pct":0.0}},"robustness_stress_floor_net_pnl":93.02872274881284,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":0.8,"passed":true,"neighbours":5,"agreeing":4}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-bef94903d52ee124","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":13,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-cfd89115149556cf — HISTORICAL

Baseline file SHA-256：`11f542f872b279f468fbebfb68f6e1d797b3e0b45061291872c8472a6dae0045`；archive locator：`survivors/sv-cfd89115149556cf/baseline.json`。

```json
{"survivor_id":"sv-cfd89115149556cf","family_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05","round_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05-r1","run_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05-r1-u2","kanban_task_id":null,"cohort":"SOLUSDT/1d","symbol":"SOLUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"signal_rule_version":1},"dca_params":{"spacing_pct":0.04,"size_multiplier":1.0,"breakeven_tp_pct":0.03,"invalidation_pct":0.1},"params_sha256":"sha256:a98015a368ce31cc1d7ef7e5ccb7067e0d98347bada8b4db1c008fc516b065b2","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:a4055b16c39091d0b5203d9abb14b49cb25e856fa03174d217a094f90abe65bc","bundle_identity_sha256":"sha256:8ef1135c007194ab7b0db4b66a551a12d36722e6dce6dd977ffead8cf1b145a2","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":933.5169768564716,"sharpe":4.444188337701129,"episodes":21,"max_dd_pct":0.0},"oos":{"net_pnl":288.8653533156646,"sharpe":5.400690849305715,"episodes":6,"max_dd_pct":0.0},"full":{"net_pnl":1222.3823301721363,"sharpe":4.653348974993258,"episodes":27,"max_dd_pct":0.0,"annualized_return":0.008541987978000876,"avg_trades_per_year":5.750291545189504},"robustness":{"fee_2x":{"net_pnl":1178.7472389841867,"sharpe":4.6540974485622915,"max_dd_pct":0.0},"funding_2x":{"net_pnl":1218.2173756329096,"sharpe":4.619302115065263,"max_dd_pct":0.0},"entry_delay_1_bar":{"net_pnl":593.5027745229683,"sharpe":0.4205083279570081,"max_dd_pct":1.9888021742663713},"slippage_2ticks":{"net_pnl":1213.6083271460877,"sharpe":4.647581128184449,"max_dd_pct":0.0}},"robustness_stress_floor_net_pnl":593.5027745229683,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":4,"agreeing":4}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-cfd89115149556cf","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":20,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-e10338930250f078 — HISTORICAL

Baseline file SHA-256：`6d44f5568f039d077b695d5214f70760c78dcb031c07e7b58438257d8d5e1372`；archive locator：`survivors/sv-e10338930250f078/baseline.json`。

```json
{"survivor_id":"sv-e10338930250f078","family_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05","round_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05-r1","run_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05-r1-u2","kanban_task_id":null,"cohort":"ETHUSDT/4h","symbol":"ETHUSDT","timeframe":"4h","challenger_of":null,"strategy_params":{"signal_rule_version":1},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.0,"breakeven_tp_pct":0.01,"invalidation_pct":0.1},"params_sha256":"sha256:2192502a7aa7cd3d72b88b83c3f158faf690d364198531b8f25375cac6cba1e3","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:a4055b16c39091d0b5203d9abb14b49cb25e856fa03174d217a094f90abe65bc","bundle_identity_sha256":"sha256:8ef1135c007194ab7b0db4b66a551a12d36722e6dce6dd977ffead8cf1b145a2","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":2540.98918829779,"sharpe":6.215377636989005,"episodes":155,"max_dd_pct":0.2177575189626794},"oos":{"net_pnl":437.7094078078911,"sharpe":3.5774418326814996,"episodes":41,"max_dd_pct":0.3858460399530576},"full":{"net_pnl":2969.7317097184073,"sharpe":5.568191484162797,"episodes":195,"max_dd_pct":0.356213685438697,"annualized_return":0.02030656271207354,"avg_trades_per_year":41.52988338192419},"robustness":{"fee_2x":{"net_pnl":2557.034927190308,"sharpe":4.97728190402962,"max_dd_pct":0.4004981062730904},"funding_2x":{"net_pnl":2958.5951457654805,"sharpe":5.5729710156685925,"max_dd_pct":0.3569051200806239},"entry_delay_1_bar":{"net_pnl":2542.9119074333057,"sharpe":2.115833379402006,"max_dd_pct":1.5173156402577936},"slippage_2ticks":{"net_pnl":2967.536560158116,"sharpe":5.563770184606497,"max_dd_pct":0.35668079636354694}},"robustness_stress_floor_net_pnl":2542.9119074333057,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":4,"agreeing":4}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-e10338930250f078","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":29,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-fc399eb7f5e7132a — HISTORICAL

Baseline file SHA-256：`99913a9df6d55e93019357fb1eb02c1bbf0960ae1e186603649ffbed630e0c53`；archive locator：`survivors/sv-fc399eb7f5e7132a/baseline.json`。

```json
{"survivor_id":"sv-fc399eb7f5e7132a","family_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05","round_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05-r1","run_id":"forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05-r1-u2","kanban_task_id":null,"cohort":"BTCUSDT/4h","symbol":"BTCUSDT","timeframe":"4h","challenger_of":null,"strategy_params":{"signal_rule_version":1},"dca_params":{"spacing_pct":0.02,"size_multiplier":1.1,"breakeven_tp_pct":0.02,"invalidation_pct":0.1},"params_sha256":"sha256:44226c79a9662a71fa77047751f8999d1c282d07edeb55fbceac470b0a8b46c3","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:a4055b16c39091d0b5203d9abb14b49cb25e856fa03174d217a094f90abe65bc","bundle_identity_sha256":"sha256:8ef1135c007194ab7b0db4b66a551a12d36722e6dce6dd977ffead8cf1b145a2","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":2251.73353793386,"sharpe":2.485895590500898,"episodes":160,"max_dd_pct":0.6861788774478336},"oos":{"net_pnl":392.374822754785,"sharpe":1.8405594690352682,"episodes":40,"max_dd_pct":0.5214859625203875},"full":{"net_pnl":2625.153959180452,"sharpe":2.3538146180468797,"episodes":199,"max_dd_pct":0.691583548736346,"annualized_return":0.0180261039113101,"avg_trades_per_year":42.38177842565597},"robustness":{"fee_2x":{"net_pnl":2269.355699280987,"sharpe":2.0514557978319456,"max_dd_pct":0.8150059173546609},"funding_2x":{"net_pnl":2589.5483793310573,"sharpe":2.3236858071397606,"max_dd_pct":0.7045589245043341},"entry_delay_1_bar":{"net_pnl":2095.1172004695663,"sharpe":1.7066580881404785,"max_dd_pct":1.1864693289913248},"slippage_2ticks":{"net_pnl":2623.8220089474535,"sharpe":2.352449272193711,"max_dd_pct":0.6918336828350001}},"robustness_stress_floor_net_pnl":2095.1172004695663,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":6,"agreeing":6}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-fc399eb7f5e7132a","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":50,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

## Falsification plan

1. 先恢復 exact source-to-case / model / signal / timing 對照，若不能證明便維持 source-mapping gap；不得以調參 rescue 或另寫 proxy 宣稱復現原文。
2. 若將來另獲執行授權，先用 prefix/suffix perturbation、landed-label checks、formation-to-order timestamps 與 universe alignment 反證 look-ahead；再以同一事件模型核對 fills、funding、fee、margin 及 parameter sensitivity。
3. 保留負面 controls、成本壓力、完整 denominator 與未觀測欄位。對 forecasting / risk-control 主張，須各有 baseline/ablation，不能單靠一個 per-coin Sharpe 認定方法有效。
4. 以上僅是未來 research tests，不是這張 archival PR 已跑過的測試，也不授權 backtest、pipeline 或交易。

## Crypto portability

來源本身含 crypto evidence，但目標、成本、時間尺度與 policy mapping 不能由旧 survivors 自動證實。

## Limitations

- baseline 與 leaderboard 是 frozen/derived archival summaries，不包含完整 robustness grid 的所有未勝出 cases、鄰居逐筆結果、source-native code/model 或事件序列；現存四 stress grids 和 neighborhood summary 全保留，缺失資料不捏造。
- historical/OOS/full 的細分日期與 split recipe 未隨 baseline 提供；只保留 exact data cutoff 與原 identity，除有已回收 source 證據外不推論 slice endpoints。
- 存在 survivor selection、搜尋過的 evaluation periods、樣本數不足、資料／成本／模型身份尚未回收的限制；不因 baseline 帶 PASS 而移除。
- Metric definitions/units 可跨 engine lineage 不同；baseline 与 derived leaderboard 的補算差異各自保留，不混寫成新的績效真值。

## Implementation status

Not implemented in the current research/runtime stack. Historical code / baselines 在此只作 Provenance/Evidence；本輪未實作、修復、採用或部署策略。

## Adoption boundary

`hb_ready_status: NOT_LOSSLESS`。來源 1-minute、next-open 與 derivative/state initialization gaps 皆阻止 PASS；舊 signal_rule_version 並非 independent lossless proof。

Research-only、not-approved；不能進目前 Hummingbot/Qlib 績效下游，不是 Paper/Testnet/Live approval。普通 non-Scout reconstruction 紀錄可經獨立 provenance/research review 保留，並非 Scout one-file PASS admission。

## Related Wiki records

`quant/forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05.md` — 本紀錄上列 hash 的原研究 provenance，未修改 Wiki。

## Sources

1. Primary：https://arxiv.org/abs/2512.24621v1
2. Pinned historical source：https://github.com/HCH725/alpha-strategy-research/blob/8dfde96fac5a470647e75d8a9e8eada1d5655ebb/forward-oriented-causal-observable-kalman-hysteresis-eurusdt-2026-09-05.md
3. Historical baseline/leaderboard archive：https://github.com/HCH725/validated-survivor-research/tree/15c0a95162b60a664b43ac60157225c7300ad789；commit 及 per-baseline raw digests 以上述 Provenance/Evidence 為準，並未聲稱所有 reference 可供匿名讀者直接下載。
