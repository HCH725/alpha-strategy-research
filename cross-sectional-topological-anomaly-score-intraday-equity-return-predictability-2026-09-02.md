---
schema: strategy-research-record-v1
hb_ready_status: NOT_LOSSLESS
title: 'Cross-Sectional Topological Anomaly Scores and Intraday Return Predictability: BallMapper, Decoder-Conditional VAE, and Function-on-Function
  Regression'
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
- https://arxiv.org/abs/2606.08586v1
- https://github.com/HCH725/alpha-strategy-research/blob/c405adc4795154334d9d50950795b4711f00445d/cross-sectional-topological-anomaly-score-intraday-equity-return-predictability-2026-09-02.md
- HCH725/validated-survivor-research commit 15c0a95162b60a664b43ac60157225c7300ad789
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Sectional Topological Anomaly Scores and Intraday Return Predictability: BallMapper, Decoder-Conditional VAE, and Function-on-Function Regression

## Provenance

- Family identity：`cross-sectional-topological-anomaly-score-intraday-equity-return-predictability-2026-09-02`；本次 consolidation 只按原 baseline family_id，不依 Sharpe 重新排名／挑選。
- Primary source：https://arxiv.org/abs/2606.08586v1。
- 既有 source-backed 研究紀錄：commit `c405adc4795154334d9d50950795b4711f00445d`，`cross-sectional-topological-anomaly-score-intraday-equity-return-predictability-2026-09-02.md`，Git blob `3d12addcd636cbfffc759397a7eebc13041da67e`。 Wiki 明列這組 reviewed_commit/reviewed_blob；本輪已核對原 Git object。
- `quant/cross-sectional-topological-anomaly-score-intraday-equity-return-predictability-2026-09-02.md` 的 raw SHA-256 為 `6147bbbda71540ada3753c76257715884460cb1b56818b57fdc27da4a8a6736c`；它在 review-state 的 `ingested_wiki_records` 中，state 最後審查 commit 為 `2799e34c5c7f8d6f7036e35d9ae7468832712c97`。這是 ingestion provenance，不是本輪 source parity 或逐檔新審查；Wiki bytes 不冒稱與原 Git blob 相同。
- Historical input：`HCH725/validated-survivor-research` commit `15c0a95162b60a664b43ac60157225c7300ad789` 的 `survivors/<survivor_id>/baseline.json`，本家族 10 筆，cohorts：`BNBUSDT/15m`, `BNBUSDT/5m`, `BTCUSDT/15m`, `BTCUSDT/1h`, `BTCUSDT/30m`, `BTCUSDT/5m`, `ETHUSDT/1h`, `SOLUSDT/15m`, `SOLUSDT/1h`, `SOLUSDT/30m`。
- Derived leaderboard：同一 repo `leaderboard/leaderboard.json`，raw SHA-256 `e8fdd38c8468960eee5b574e93d27615635bcb266fe481ab8c1409720d96c42e`；它不是 frozen bundle 本身，也不是採用 gate。

- Source-to-legacy-Qlib mapping gap：family 名称、strategy flags/case IDs 或舊 PASS 不證明原文 source-native signal、模型 weights、universe、因果時序與執行機制一致。除本紀錄明列已釘選的程式規則外，沒有補造代碼對照。paper方法、研究解讀與historical DCA分層保留；尚未證明多個 legacy codes 對應不同完整 core mechanisms，故不任意拆成新策略。

## Economic mechanism

### Source-reported

BallMapper / decoder-conditional VAE 對跨股票 co-movement 的拓樸偏離評分，再以 function-on-function regression 檢驗 anomaly history 對 return curves 的預測內容。這是 predictive-content study，不是已定義完整交易規則的策略。

### Research interpretation

這是方法／假說的普通研究封存，不是把歷史 survivor 標籤當成新 alpha。機制層分類與單筆 cohort 的 DCA 收益不同；statistical forecast、risk allocator 或負面 study 均不得被默換成已驗證的 crypto 交易規則。

## Signal

Takens embeddings → BallMapper peer structure → VAE anomaly score history → return-curve association。來源沒有把 score 直接指定為方向、入場、退出或可交易 sizing。舊研究紀錄的 directional long/short proposal 明標 research-proposed；baseline method_code=0 不證明原文三種 VAE 中哪一種被忠實使用。

## Required data

來源為十個液態 S&P 500 constituents 的 intraday cross-section、5/15/30/60-minute OHLCV、peer context 與 embedding/model training data。

Historical cohort resolution、parameters 與 data cutoff 以 Evidence 的原 JSON 為準，不補齊不存在的字段，不降採樣、不改 symbol。baseline 不含完整行情 manifest、signal arrays、model checkpoints 或逐筆 trade ledger；它不是可直接執行的策略定義。

## Execution assumptions

來源未建立完整 order timing、fill、fee、impact 或 portfolio backtest。不得為填滿這些缺欄而加入 source-native 假定。

Historical DCA 參數只代表當時研究配置，並非 paper 原生規則，也不是目前 house overlay。未重新量測 fees、funding、margin/liquidation、slippage、intrabar path 或 fills；hash references 不是原資料 bytes 已重新驗證的宣告。

## Evidence

### Source-reported

本輪讀取 versioned primary landing 的 abstract，確認上述 method-level 主張；更細的 signal 配置以釘選原研究紀錄為轉錄來源，未宣稱已重新逐式審閱整篇 methods 或 source code。原文績效不是下列 crypto baseline metrics。

### Independently reproduced

Not independently reproduced. 本輪只驗 source identity／文件轉錄，沒有 Qlib rerun、Hummingbot reproduction、Paper 或 Testnet。

### Negative evidence

原文只確認統計 predictive content，不能轉述為淨 alpha。舊 Wiki 的 W 段同時寫 5b 與約 2.5b，存在轉錄矛盾；delay、warmup 與 trade mapping 不足以無損重建，故本紀錄不挑選其中一式。

### HISTORICAL QLIB SURVIVOR EVIDENCE — 非目前 Hummingbot reproduction

以下每個 baseline JSON 保留全部原鍵／數值／null／巢狀結構，唯一刪除 top-level `bundle_path` 的機器絕對路徑。bundle 邏輯定位仍可由 family_id / round_id / run_id 與 survivor ID 找到；不假裝本輪讀取已退役結果盤。每筆獨立列 raw baseline-file SHA-256，它與 `params_sha256`、`bundle_sha256`（檔案 bytes）、`bundle_identity_sha256`（歷史 identity recipe）互不相同。

鍵名 `net_pnl` / `sharpe` / `max_dd_pct` / `annualized_return` 原樣保留，不重命名成 ROI、不對 MDD 改 sign／比例／百分點、不跨 lineage 默認同一 annualization。baseline 欄位缺席不同於 null；不從另一層悄悄補值。`source_verdict: PASS` 與 `neighbourhood.passed` 都是 HISTORICAL，不能解讀成今日 efficacy、source parity 或 HB_READY PASS。

每筆另列 `leaderboard_snapshot`：`additional_fields` 為 derived index 額外欄位，`baseline_field_overrides` 為該 index 與 baseline 不同的完整 top-level 值；空 object 明示無差異。兩者都不回寫 baseline。僅非 null 的 `evidence_manifest_path` 去除原 results-root 絕對前綴，保留 `_survivors/...` 相對 locator；null 留 null。rank / top10 / package PRESENT / FROZEN_ONLY 只是當時 derived state，不能解讀為今天 evidence package bytes 存在或新 forward evidence。

#### sv-28a83b38eeecfc48 — HISTORICAL

Baseline file SHA-256：`fc676654dd173120e0b4e80f467ecc4beaab3eecfef6d1dbd5fd7ffaf3131197`；archive locator：`survivors/sv-28a83b38eeecfc48/baseline.json`。

```json
{"survivor_id":"sv-28a83b38eeecfc48","family_id":"cross-sectional-topological-anomaly-score-intraday-equity-return-predictability-2026-09-02","round_id":"round-2026-09-20-topological-anomaly-v3","run_id":"run-2026-09-20-topological-anomaly-v3-002","kanban_task_id":"t_0a6aba33","cohort":"BNBUSDT/15m","symbol":"BNBUSDT","timeframe":"15m","challenger_of":null,"strategy_params":{"method_code":0},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.1,"breakeven_tp_pct":0.01,"invalidation_pct":0.1},"params_sha256":"sha256:ecf60cf0f5f264c69fd2172b2c2d5911cd04adb91361d8b5316fb7e18fdbda15","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:c09bced7d444117790d1c8bc67797e2255b5b7edf93e1553c6c6a0ad33b9a037","bundle_identity_sha256":"sha256:d311adf912387e2a5e5e15e19eb213991f2bb4d08d5b1eef2b26710e8a030a1f","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":37746.53384354446,"sharpe":0.6767319921380045,"episodes":889,"max_dd_pct":32.72647169592039},"oos":{"net_pnl":14611.105229206725,"sharpe":1.2232947964612189,"episodes":199,"max_dd_pct":29.878421477686974},"full":{"net_pnl":52357.63907275113,"sharpe":0.7717492032844828,"episodes":1088,"max_dd_pct":35.33180136734287,"annualized_return":0.23977600485624495},"robustness":{"fee_2x":{"net_pnl":20741.71297905551,"sharpe":0.30374605382685776,"max_dd_pct":57.448518617585265},"funding_2x":{"net_pnl":53846.971859708785,"sharpe":0.7908584776983659,"max_dd_pct":34.65154445112363},"entry_delay_1_bar":{"net_pnl":39395.406682734574,"sharpe":0.540446503847465,"max_dd_pct":44.31935901537831},"slippage_2ticks":{"net_pnl":50103.65834382061,"sharpe":0.7375419467609123,"max_dd_pct":36.33997719262747}},"robustness_stress_floor_net_pnl":20741.71297905551,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":0.75,"passed":true,"neighbours":4,"agreeing":3}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-28a83b38eeecfc48","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":60,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{"full":{"net_pnl":52357.63907275113,"sharpe":0.7717492032844828,"episodes":1088,"max_dd_pct":35.33180136734287,"annualized_return":0.23977600485624495,"avg_trades_per_year":231.7154518950437}},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-2e3b14a76b2792e6 — HISTORICAL

Baseline file SHA-256：`a10b50b74f4156596042ca64a3297ba071d72dea5213b529c4cd0be433085936`；archive locator：`survivors/sv-2e3b14a76b2792e6/baseline.json`。

```json
{"survivor_id":"sv-2e3b14a76b2792e6","family_id":"cross-sectional-topological-anomaly-score-intraday-equity-return-predictability-2026-09-02","round_id":"round-2026-09-20-topological-anomaly-v3","run_id":"run-2026-09-20-topological-anomaly-v3-002","kanban_task_id":"t_0a6aba33","cohort":"SOLUSDT/30m","symbol":"SOLUSDT","timeframe":"30m","challenger_of":null,"strategy_params":{"method_code":0},"dca_params":{"spacing_pct":0.03,"size_multiplier":1.1,"breakeven_tp_pct":0.02,"invalidation_pct":0.1},"params_sha256":"sha256:7b7154513d49ef19d4aa520de9db5a1784c99fe76d3fe085884aa077903ef0a1","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:c09bced7d444117790d1c8bc67797e2255b5b7edf93e1553c6c6a0ad33b9a037","bundle_identity_sha256":"sha256:d311adf912387e2a5e5e15e19eb213991f2bb4d08d5b1eef2b26710e8a030a1f","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":43799.80666188656,"sharpe":0.8109789731853481,"episodes":846,"max_dd_pct":19.774185234963127},"oos":{"net_pnl":7235.563289555209,"sharpe":0.6998488860180676,"episodes":183,"max_dd_pct":23.325028076501148},"full":{"net_pnl":51035.369951441804,"sharpe":0.7891519750101869,"episodes":1029,"max_dd_pct":19.774185234963127,"annualized_return":0.23551422548020162},"robustness":{"fee_2x":{"net_pnl":32299.94624350767,"sharpe":0.4964387800853996,"max_dd_pct":27.071527764731684},"funding_2x":{"net_pnl":52597.7987854449,"sharpe":0.8151515834127508,"max_dd_pct":19.392576118856898},"entry_delay_1_bar":{"net_pnl":25260.087586462763,"sharpe":0.3661988066329194,"max_dd_pct":31.402288286516107},"slippage_2ticks":{"net_pnl":50499.04864137935,"sharpe":0.7805936063584853,"max_dd_pct":19.894513835271706}},"robustness_stress_floor_net_pnl":25260.087586462763,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":0.8333333333333334,"passed":true,"neighbours":6,"agreeing":5}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-2e3b14a76b2792e6","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":71,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{"full":{"net_pnl":51035.369951441804,"sharpe":0.7891519750101869,"episodes":1029,"max_dd_pct":19.774185234963127,"annualized_return":0.23551422548020162,"avg_trades_per_year":219.14999999999998}},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-3a43cf7b6c6ac5d9 — HISTORICAL

Baseline file SHA-256：`4d87ccb54de807a28b639ebe5796bc5a7bb501814e2cfbbc80811c182b806d0f`；archive locator：`survivors/sv-3a43cf7b6c6ac5d9/baseline.json`。

```json
{"survivor_id":"sv-3a43cf7b6c6ac5d9","family_id":"cross-sectional-topological-anomaly-score-intraday-equity-return-predictability-2026-09-02","round_id":"round-2026-09-20-topological-anomaly-v3","run_id":"run-2026-09-20-topological-anomaly-v3-002","kanban_task_id":"t_0a6aba33","cohort":"SOLUSDT/1h","symbol":"SOLUSDT","timeframe":"1h","challenger_of":null,"strategy_params":{"method_code":2},"dca_params":{"spacing_pct":0.02,"size_multiplier":1.0,"breakeven_tp_pct":0.03,"invalidation_pct":0.1},"params_sha256":"sha256:435356b31a4d1dfacabe0b18cb770bdd1f25988be72943d445772092454c502d","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:c09bced7d444117790d1c8bc67797e2255b5b7edf93e1553c6c6a0ad33b9a037","bundle_identity_sha256":"sha256:d311adf912387e2a5e5e15e19eb213991f2bb4d08d5b1eef2b26710e8a030a1f","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":82466.38520184126,"sharpe":1.1327010020141486,"episodes":810,"max_dd_pct":31.07242770627692},"oos":{"net_pnl":12789.608755276617,"sharpe":0.8606173197984764,"episodes":169,"max_dd_pct":29.403719064820176},"full":{"net_pnl":95472.72272023663,"sharpe":1.0860822458472532,"episodes":979,"max_dd_pct":31.07242770627692,"annualized_return":0.3560025268341198},"robustness":{"fee_2x":{"net_pnl":72194.89081565906,"sharpe":0.8175887602062073,"max_dd_pct":33.28368560021395},"funding_2x":{"net_pnl":97830.73226729472,"sharpe":1.1145331278907855,"max_dd_pct":30.715720927742098},"entry_delay_1_bar":{"net_pnl":35939.55821744738,"sharpe":0.3853998191498736,"max_dd_pct":125.12133265490894},"slippage_2ticks":{"net_pnl":95025.416493699,"sharpe":1.0806033790658724,"max_dd_pct":31.115633868928565}},"robustness_stress_floor_net_pnl":35939.55821744738,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":5,"agreeing":5}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-3a43cf7b6c6ac5d9","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":69,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{"full":{"net_pnl":95472.72272023663,"sharpe":1.0860822458472532,"episodes":979,"max_dd_pct":31.07242770627692,"annualized_return":0.3560025268341198,"avg_trades_per_year":208.50131195335274}},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-5061c532af027600 — HISTORICAL

Baseline file SHA-256：`6d67d4dee53703bb7fcaaef2feb5a99087a1d3e90fbd833600ed08acadf81130`；archive locator：`survivors/sv-5061c532af027600/baseline.json`。

```json
{"survivor_id":"sv-5061c532af027600","family_id":"cross-sectional-topological-anomaly-score-intraday-equity-return-predictability-2026-09-02","round_id":"round-2026-09-20-topological-anomaly-v3","run_id":"run-2026-09-20-topological-anomaly-v3-002","kanban_task_id":"t_0a6aba33","cohort":"SOLUSDT/15m","symbol":"SOLUSDT","timeframe":"15m","challenger_of":null,"strategy_params":{"method_code":1},"dca_params":{"spacing_pct":0.03,"size_multiplier":1.1,"breakeven_tp_pct":0.03,"invalidation_pct":0.05},"params_sha256":"sha256:bcb29972275d92f1b10c0caffdedde5e6d1f8d9679af6ff1f354e61c9b66686a","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:c09bced7d444117790d1c8bc67797e2255b5b7edf93e1553c6c6a0ad33b9a037","bundle_identity_sha256":"sha256:d311adf912387e2a5e5e15e19eb213991f2bb4d08d5b1eef2b26710e8a030a1f","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":12075.282573110962,"sharpe":0.5928317110704877,"episodes":256,"max_dd_pct":36.61156595646284},"oos":{"net_pnl":4089.733405713809,"sharpe":0.9757003681729185,"episodes":62,"max_dd_pct":13.985290899105962},"full":{"net_pnl":16313.878990583917,"sharpe":0.6622403069157905,"episodes":318,"max_dd_pct":36.61156595646284,"annualized_return":0.09682528394319778},"robustness":{"fee_2x":{"net_pnl":11198.993642847217,"sharpe":0.45306380133354357,"max_dd_pct":40.38701724650828},"funding_2x":{"net_pnl":16499.39836469437,"sharpe":0.6705020317427843,"max_dd_pct":36.44415534165092},"entry_delay_1_bar":{"net_pnl":14655.518581345115,"sharpe":0.6007998350325681,"max_dd_pct":40.64101206461911},"slippage_2ticks":{"net_pnl":16188.040665260909,"sharpe":0.6570739816403232,"max_dd_pct":36.747845826078255}},"robustness_stress_floor_net_pnl":11198.993642847217,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":0.6,"passed":true,"neighbours":5,"agreeing":3}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-5061c532af027600","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":66,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{"full":{"net_pnl":16313.878990583917,"sharpe":0.6622403069157905,"episodes":318,"max_dd_pct":36.61156595646284,"annualized_return":0.09682528394319778,"avg_trades_per_year":67.72565597667638}},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-5892634ea095ec54 — HISTORICAL

Baseline file SHA-256：`2178b211589d802d0ea1098f2c07c588e46c78a2a1df5d640c6ff3f3b7207202`；archive locator：`survivors/sv-5892634ea095ec54/baseline.json`。

```json
{"survivor_id":"sv-5892634ea095ec54","family_id":"cross-sectional-topological-anomaly-score-intraday-equity-return-predictability-2026-09-02","round_id":"round-2026-09-20-topological-anomaly-v3","run_id":"run-2026-09-20-topological-anomaly-v3-002","kanban_task_id":"t_0a6aba33","cohort":"BTCUSDT/5m","symbol":"BTCUSDT","timeframe":"5m","challenger_of":null,"strategy_params":{"method_code":0},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.0,"breakeven_tp_pct":0.03,"invalidation_pct":0.1},"params_sha256":"sha256:624470e0f7d610dcfe5f4b304b42e653b85c158c4b401ba098fb4e867c43fb2c","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:c09bced7d444117790d1c8bc67797e2255b5b7edf93e1553c6c6a0ad33b9a037","bundle_identity_sha256":"sha256:d311adf912387e2a5e5e15e19eb213991f2bb4d08d5b1eef2b26710e8a030a1f","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":23737.982316965103,"sharpe":0.4183494781106393,"episodes":558,"max_dd_pct":47.4976429602035},"oos":{"net_pnl":5101.822002494875,"sharpe":0.58787085851491,"episodes":129,"max_dd_pct":17.26082318443016},"full":{"net_pnl":28839.804319459956,"sharpe":0.4345171126485666,"episodes":687,"max_dd_pct":47.4976429602035,"annualized_return":0.15415183554798606},"robustness":{"fee_2x":{"net_pnl":8406.963129259273,"sharpe":0.12532160488160982,"max_dd_pct":61.34096280425303},"funding_2x":{"net_pnl":30429.624468353704,"sharpe":0.460734629556915,"max_dd_pct":45.9608893563921},"entry_delay_1_bar":{"net_pnl":26924.379945839202,"sharpe":0.3951505855214782,"max_dd_pct":49.4698049417422},"slippage_2ticks":{"net_pnl":28880.57096435933,"sharpe":0.43511559713683573,"max_dd_pct":47.35369966734182}},"robustness_stress_floor_net_pnl":8406.963129259273,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":4,"agreeing":4}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-5892634ea095ec54","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":74,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{"full":{"net_pnl":28839.804319459956,"sharpe":0.4345171126485666,"episodes":687,"max_dd_pct":47.4976429602035,"annualized_return":0.15415183554798606,"avg_trades_per_year":146.31297376093292}},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-774433da4c2b3b1e — HISTORICAL

Baseline file SHA-256：`4a4595396b12adf55d6a5f6f87666b6bdfeb6e0218a07bb48b095f0806ab6348`；archive locator：`survivors/sv-774433da4c2b3b1e/baseline.json`。

```json
{"survivor_id":"sv-774433da4c2b3b1e","family_id":"cross-sectional-topological-anomaly-score-intraday-equity-return-predictability-2026-09-02","round_id":"round-2026-09-20-topological-anomaly-v3","run_id":"run-2026-09-20-topological-anomaly-v3-002","kanban_task_id":"t_0a6aba33","cohort":"ETHUSDT/1h","symbol":"ETHUSDT","timeframe":"1h","challenger_of":null,"strategy_params":{"method_code":0},"dca_params":{"spacing_pct":0.03,"size_multiplier":1.0,"breakeven_tp_pct":0.03,"invalidation_pct":0.05},"params_sha256":"sha256:174a3022c3fcd573363e2a6cf1c3223a1fc1b1174ef81db7454366248c19c094","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:c09bced7d444117790d1c8bc67797e2255b5b7edf93e1553c6c6a0ad33b9a037","bundle_identity_sha256":"sha256:d311adf912387e2a5e5e15e19eb213991f2bb4d08d5b1eef2b26710e8a030a1f","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":11767.454378718769,"sharpe":0.5528593999734821,"episodes":534,"max_dd_pct":20.817989678479282},"oos":{"net_pnl":2515.7450258461895,"sharpe":0.4877085373330774,"episodes":133,"max_dd_pct":20.191891321697405},"full":{"net_pnl":14283.199404564968,"sharpe":0.5402245633590858,"episodes":667,"max_dd_pct":20.817989678479282,"annualized_return":0.08641026897677118},"robustness":{"fee_2x":{"net_pnl":4932.459340633307,"sharpe":0.18593489173792802,"max_dd_pct":29.38456205432972},"funding_2x":{"net_pnl":14282.238020590565,"sharpe":0.540523082346579,"max_dd_pct":20.76112582922326},"entry_delay_1_bar":{"net_pnl":22978.028264284778,"sharpe":0.8782430609547843,"max_dd_pct":26.844232441693656},"slippage_2ticks":{"net_pnl":14217.788555720997,"sharpe":0.5377287038938362,"max_dd_pct":20.860415964621808}},"robustness_stress_floor_net_pnl":4932.459340633307,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":0.8,"passed":true,"neighbours":5,"agreeing":4}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-774433da4c2b3b1e","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":78,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{"full":{"net_pnl":14283.199404564968,"sharpe":0.5402245633590858,"episodes":667,"max_dd_pct":20.817989678479282,"annualized_return":0.08641026897677118,"avg_trades_per_year":142.05349854227404}},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-8fb372e2d76fe246 — HISTORICAL

Baseline file SHA-256：`d69470723871339d7d39e958dbcc33ec1ab7c838ab5320778d01fc3971afaa83`；archive locator：`survivors/sv-8fb372e2d76fe246/baseline.json`。

```json
{"survivor_id":"sv-8fb372e2d76fe246","family_id":"cross-sectional-topological-anomaly-score-intraday-equity-return-predictability-2026-09-02","round_id":"round-2026-09-20-topological-anomaly-v3","run_id":"run-2026-09-20-topological-anomaly-v3-002","kanban_task_id":"t_0a6aba33","cohort":"BTCUSDT/1h","symbol":"BTCUSDT","timeframe":"1h","challenger_of":null,"strategy_params":{"method_code":0},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.1,"breakeven_tp_pct":0.03,"invalidation_pct":0.1},"params_sha256":"sha256:32e995db856a10d7910d9402ac995f80a09afb544b3791f824ba03fb19b3dde5","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:c09bced7d444117790d1c8bc67797e2255b5b7edf93e1553c6c6a0ad33b9a037","bundle_identity_sha256":"sha256:d311adf912387e2a5e5e15e19eb213991f2bb4d08d5b1eef2b26710e8a030a1f","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":69340.33945271379,"sharpe":1.1833390895960396,"episodes":467,"max_dd_pct":14.093824721925309},"oos":{"net_pnl":6007.298654820548,"sharpe":0.5216005141910784,"episodes":119,"max_dd_pct":22.346099910826002},"full":{"net_pnl":75902.07982517772,"sharpe":1.0777724170492573,"episodes":586,"max_dd_pct":14.093824721925309,"annualized_return":0.3079358277529358},"robustness":{"fee_2x":{"net_pnl":53728.070173034655,"sharpe":0.7576930857338122,"max_dd_pct":15.060175750932055},"funding_2x":{"net_pnl":77289.934997662,"sharpe":1.0999056078477347,"max_dd_pct":14.160912753006553},"entry_delay_1_bar":{"net_pnl":48947.187608299566,"sharpe":0.6983842196969845,"max_dd_pct":22.347745532779335},"slippage_2ticks":{"net_pnl":75788.62263516168,"sharpe":1.0760596022519382,"max_dd_pct":14.100256219336432}},"robustness_stress_floor_net_pnl":48947.187608299566,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":4,"agreeing":4}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-8fb372e2d76fe246","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":77,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{"full":{"net_pnl":75902.07982517772,"sharpe":1.0777724170492573,"episodes":586,"max_dd_pct":14.093824721925309,"annualized_return":0.3079358277529358,"avg_trades_per_year":124.80262390670553}},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-cce57163b0ceddbf — HISTORICAL

Baseline file SHA-256：`b9099ab3379735bde1850530afa01c9891f9b191c1335fc8be1e2b89b394544c`；archive locator：`survivors/sv-cce57163b0ceddbf/baseline.json`。

```json
{"survivor_id":"sv-cce57163b0ceddbf","family_id":"cross-sectional-topological-anomaly-score-intraday-equity-return-predictability-2026-09-02","round_id":"round-2026-09-20-topological-anomaly-v3","run_id":"run-2026-09-20-topological-anomaly-v3-002","kanban_task_id":"t_0a6aba33","cohort":"BTCUSDT/15m","symbol":"BTCUSDT","timeframe":"15m","challenger_of":null,"strategy_params":{"method_code":0},"dca_params":{"spacing_pct":0.04,"size_multiplier":1.0,"breakeven_tp_pct":0.02,"invalidation_pct":0.1},"params_sha256":"sha256:d169c2394518607a699af1b7e02d4a2f14f82be614bd09e34fe99f4c0fbb9fec","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:c09bced7d444117790d1c8bc67797e2255b5b7edf93e1553c6c6a0ad33b9a037","bundle_identity_sha256":"sha256:d311adf912387e2a5e5e15e19eb213991f2bb4d08d5b1eef2b26710e8a030a1f","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":10017.99179516806,"sharpe":0.4790914952741606,"episodes":602,"max_dd_pct":30.725062918352293},"oos":{"net_pnl":767.4874308133112,"sharpe":0.2100336890338209,"episodes":144,"max_dd_pct":7.9703510236571615},"full":{"net_pnl":10613.969310083163,"sharpe":0.42887142560504893,"episodes":745,"max_dd_pct":30.725062918352293,"annualized_return":0.06659263844484009},"robustness":{"fee_2x":{"net_pnl":1500.3688892521882,"sharpe":0.060331650776279465,"max_dd_pct":34.8488294023363},"funding_2x":{"net_pnl":10834.698021712002,"sharpe":0.43808234886046826,"max_dd_pct":30.56535427780079},"entry_delay_1_bar":{"net_pnl":3939.023724369259,"sharpe":0.1586679044641687,"max_dd_pct":32.4347899286215},"slippage_2ticks":{"net_pnl":10580.334449822467,"sharpe":0.4274896261172542,"max_dd_pct":30.749831441853853}},"robustness_stress_floor_net_pnl":1500.3688892521882,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":5,"agreeing":5}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-cce57163b0ceddbf","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":88,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{"full":{"net_pnl":10613.969310083163,"sharpe":0.42887142560504893,"episodes":745,"max_dd_pct":30.725062918352293,"annualized_return":0.06659263844484009,"avg_trades_per_year":158.66545189504373}},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-f433567e82c0d043 — HISTORICAL

Baseline file SHA-256：`dbf05f914b1f8ea59692c38ea8bf120e18bfeca3ba4d3a16b871ec63ea0ff647`；archive locator：`survivors/sv-f433567e82c0d043/baseline.json`。

```json
{"survivor_id":"sv-f433567e82c0d043","family_id":"cross-sectional-topological-anomaly-score-intraday-equity-return-predictability-2026-09-02","round_id":"round-2026-09-20-topological-anomaly-v3","run_id":"run-2026-09-20-topological-anomaly-v3-002","kanban_task_id":"t_0a6aba33","cohort":"BTCUSDT/30m","symbol":"BTCUSDT","timeframe":"30m","challenger_of":null,"strategy_params":{"method_code":1},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.1,"breakeven_tp_pct":0.03,"invalidation_pct":0.05},"params_sha256":"sha256:5beb5889ec67060023bd9dcedbbceb8f60529023249dc93f0653dc6f93ef4fd8","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:c09bced7d444117790d1c8bc67797e2255b5b7edf93e1553c6c6a0ad33b9a037","bundle_identity_sha256":"sha256:d311adf912387e2a5e5e15e19eb213991f2bb4d08d5b1eef2b26710e8a030a1f","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":28868.677572839184,"sharpe":0.7767025996551576,"episodes":248,"max_dd_pct":39.73913660166911},"oos":{"net_pnl":10633.6482496228,"sharpe":2.081402257313015,"episodes":56,"max_dd_pct":8.216325138443594},"full":{"net_pnl":38499.19579352579,"sharpe":0.8910812422737595,"episodes":304,"max_dd_pct":39.73913660166911,"annualized_return":0.19210203197343212},"robustness":{"fee_2x":{"net_pnl":28205.21521635828,"sharpe":0.6504497468743917,"max_dd_pct":44.01746957200052},"funding_2x":{"net_pnl":39067.447719152515,"sharpe":0.9007981958092219,"max_dd_pct":39.58458227622172},"entry_delay_1_bar":{"net_pnl":40334.19358741049,"sharpe":0.9683688713484107,"max_dd_pct":31.519873881984477},"slippage_2ticks":{"net_pnl":38450.96107719675,"sharpe":0.8899097385304787,"max_dd_pct":39.76876596890625}},"robustness_stress_floor_net_pnl":28205.21521635828,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":4,"agreeing":4}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-f433567e82c0d043","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":45,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{"full":{"net_pnl":38499.19579352579,"sharpe":0.8910812422737595,"episodes":304,"max_dd_pct":39.73913660166911,"annualized_return":0.19210203197343212,"avg_trades_per_year":64.74402332361515}},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-f8b533dde162100d — HISTORICAL

Baseline file SHA-256：`5b0a91d09d47156e66c4de1b38c4a2d8ebc28de37578265ec2081ceaaa90927a`；archive locator：`survivors/sv-f8b533dde162100d/baseline.json`。

```json
{"survivor_id":"sv-f8b533dde162100d","family_id":"cross-sectional-topological-anomaly-score-intraday-equity-return-predictability-2026-09-02","round_id":"round-2026-09-20-topological-anomaly-v3","run_id":"run-2026-09-20-topological-anomaly-v3-002","kanban_task_id":"t_0a6aba33","cohort":"BNBUSDT/5m","symbol":"BNBUSDT","timeframe":"5m","challenger_of":null,"strategy_params":{"method_code":0},"dca_params":{"spacing_pct":0.04,"size_multiplier":1.0,"breakeven_tp_pct":0.02,"invalidation_pct":0.05},"params_sha256":"sha256:6a162bd3cf355eb9f141ddf024e5a40dab3fa7d52aac271405734a92b969976e","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:c09bced7d444117790d1c8bc67797e2255b5b7edf93e1553c6c6a0ad33b9a037","bundle_identity_sha256":"sha256:d311adf912387e2a5e5e15e19eb213991f2bb4d08d5b1eef2b26710e8a030a1f","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":7106.506112859085,"sharpe":0.4119052659610257,"episodes":647,"max_dd_pct":17.299381164955456},"oos":{"net_pnl":3715.539109436033,"sharpe":1.0526269479639447,"episodes":155,"max_dd_pct":9.287051243644772},"full":{"net_pnl":10868.177766538865,"sharpe":0.5214055166987105,"episodes":801,"max_dd_pct":17.299381164955456,"annualized_return":0.06800970449728627},"robustness":{"fee_2x":{"net_pnl":1325.8336093228645,"sharpe":0.06324032901825918,"max_dd_pct":30.617178479288114},"funding_2x":{"net_pnl":10910.373991104734,"sharpe":0.5237409130436826,"max_dd_pct":17.26517651929645},"entry_delay_1_bar":{"net_pnl":1074.1269990773792,"sharpe":0.050334766212956496,"max_dd_pct":32.88042371714423},"slippage_2ticks":{"net_pnl":8803.968957963203,"sharpe":0.42127393348298287,"max_dd_pct":17.782596629971817}},"robustness_stress_floor_net_pnl":1074.1269990773792,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":0.6,"passed":true,"neighbours":5,"agreeing":3}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-f8b533dde162100d","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":62,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{"full":{"net_pnl":10868.177766538865,"sharpe":0.5214055166987105,"episodes":801,"max_dd_pct":17.299381164955456,"annualized_return":0.06800970449728627,"avg_trades_per_year":170.5919825072886}},"baseline_fields_absent_in_leaderboard":[]}}
```

## Falsification plan

1. 先恢復 exact source-to-case / model / signal / timing 對照，若不能證明便維持 source-mapping gap；不得以調參 rescue 或另寫 proxy 宣稱復現原文。
2. 若將來另獲執行授權，先用 prefix/suffix perturbation、landed-label checks、formation-to-order timestamps 與 universe alignment 反證 look-ahead；再以同一事件模型核對 fills、funding、fee、margin 及 parameter sensitivity。
3. 保留負面 controls、成本壓力、完整 denominator 與未觀測欄位。對 forecasting / risk-control 主張，須各有 baseline/ablation，不能單靠一個 per-coin Sharpe 認定方法有效。
4. 以上僅是未來 research tests，不是這張 archival PR 已跑過的測試，也不授權 backtest、pipeline 或交易。

## Crypto portability

Adapted / unproven。來源股票／ETF／期貨方法與下列 crypto legacy cohorts 是不同層；替换 instrument、calendar、features、model、portfolio 或 fills 均可能改變 estimand。

## Limitations

- baseline 與 leaderboard 是 frozen/derived archival summaries，不包含完整 robustness grid 的所有未勝出 cases、鄰居逐筆結果、source-native code/model 或事件序列；現存四 stress grids 和 neighborhood summary 全保留，缺失資料不捏造。
- historical/OOS/full 的細分日期與 split recipe 未隨 baseline 提供；只保留 exact data cutoff 與原 identity，除有已回收 source 證據外不推論 slice endpoints。
- 存在 survivor selection、搜尋過的 evaluation periods、樣本數不足、資料／成本／模型身份尚未回收的限制；不因 baseline 帶 PASS 而移除。
- Metric definitions/units 可跨 engine lineage 不同；baseline 与 derived leaderboard 的補算差異各自保留，不混寫成新的績效真值。

## Implementation status

Not implemented in the current research/runtime stack. Historical code / baselines 在此只作 Provenance/Evidence；本輪未實作、修復、採用或部署策略。

## Adoption boundary

`hb_ready_status: NOT_LOSSLESS`。cross-sectional graph/VAE state 與缺少 actionable trade semantics，本身即阻止 PASS；5m/15m/30m 歷史 cohorts 亦不得默換 1h。

Research-only、not-approved；不能進目前 Hummingbot/Qlib 績效下游，不是 Paper/Testnet/Live approval。普通 non-Scout reconstruction 紀錄可經獨立 provenance/research review 保留，並非 Scout one-file PASS admission。

## Related Wiki records

`quant/cross-sectional-topological-anomaly-score-intraday-equity-return-predictability-2026-09-02.md` — 本紀錄上列 hash 的原研究 provenance，未修改 Wiki。

## Sources

1. Primary：https://arxiv.org/abs/2606.08586v1
2. Pinned historical source：https://github.com/HCH725/alpha-strategy-research/blob/c405adc4795154334d9d50950795b4711f00445d/cross-sectional-topological-anomaly-score-intraday-equity-return-predictability-2026-09-02.md
3. Historical baseline/leaderboard archive：https://github.com/HCH725/validated-survivor-research/tree/15c0a95162b60a664b43ac60157225c7300ad789；commit 及 per-baseline raw digests 以上述 Provenance/Evidence 為準，並未聲稱所有 reference 可供匿名讀者直接下載。
