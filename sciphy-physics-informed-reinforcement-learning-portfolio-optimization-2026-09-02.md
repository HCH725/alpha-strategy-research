---
schema: strategy-research-record-v1
hb_ready_status: NOT_LOSSLESS
title: SciPhy Reinforcement Learning for Dynamic Institutional Portfolio Allocation with Microstructure Price Impact
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
- https://arxiv.org/abs/2607.15195v1
- https://github.com/HCH725/alpha-strategy-research/blob/c405adc4795154334d9d50950795b4711f00445d/sciphy-physics-informed-reinforcement-learning-portfolio-optimization-2026-09-02.md
- HCH725/validated-survivor-research commit 15c0a95162b60a664b43ac60157225c7300ad789
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# SciPhy Reinforcement Learning for Dynamic Institutional Portfolio Allocation with Microstructure Price Impact

## Provenance

- Family identity：`sciphy-physics-informed-reinforcement-learning-portfolio-optimization-2026-09-02`；本次 consolidation 只按原 baseline family_id，不依 Sharpe 重新排名／挑選。
- Primary source：https://arxiv.org/abs/2607.15195v1。
- 既有 source-backed 研究紀錄：commit `c405adc4795154334d9d50950795b4711f00445d`，`sciphy-physics-informed-reinforcement-learning-portfolio-optimization-2026-09-02.md`，Git blob `19eae00e0fa749fb0f68cadfb15e11e8c9ceb3a1`。 Wiki 明列這組 reviewed_commit/reviewed_blob；本輪已核對原 Git object。
- `quant/sciphy-physics-informed-reinforcement-learning-portfolio-optimization-2026-09-02.md` 的 raw SHA-256 為 `56fb7b3a6a3cbce72c43f49c8a80032ea0c60c700a5aa5dbe308ff8cbe2d9475`；它在 review-state 的 `ingested_wiki_records` 中，state 最後審查 commit 為 `2799e34c5c7f8d6f7036e35d9ae7468832712c97`。這是 ingestion provenance，不是本輪 source parity 或逐檔新審查；Wiki bytes 不冒稱與原 Git blob 相同。
- Historical input：`HCH725/validated-survivor-research` commit `15c0a95162b60a664b43ac60157225c7300ad789` 的 `survivors/<survivor_id>/baseline.json`，本家族 4 筆，cohorts：`BNBUSDT/1d`, `BTCUSDT/1d`, `ETHUSDT/1d`, `SOLUSDT/1d`。
- Derived leaderboard：同一 repo `leaderboard/leaderboard.json`，raw SHA-256 `e8fdd38c8468960eee5b574e93d27615635bcb266fe481ab8c1409720d96c42e`；它不是 frozen bundle 本身，也不是採用 gate。

- Source-to-legacy-Qlib mapping gap：family 名称、strategy flags/case IDs 或舊 PASS 不證明原文 source-native signal、模型 weights、universe、因果時序與執行機制一致。除本紀錄明列已釘選的程式規則外，沒有補造代碼對照。paper方法、研究解讀與historical DCA分層保留；尚未證明多個 legacy codes 對應不同完整 core mechanisms，故不任意拆成新策略。

## Economic mechanism

### Source-reported

SciPhyRL 以 PINN 對 observed paths 上的 Hamilton-Jacobi relation 學習 institutional portfolio control，將 trading-rate control 重寫成 target holdings，並顯式計入 cumulative costs / quadratic impact。

### Research interpretation

這是方法／假說的普通研究封存，不是把歷史 survivor 標籤當成新 alpha。機制層分類與單筆 cohort 的 DCA 收益不同；statistical forecast、risk allocator 或負面 study 均不得被默換成已驗證的 crypto 交易規則。

## Signal

Extended holdings/prices/cumulative-cost state → offline PINN value function → Gibbs target-holdings policy。原研究使用 engineered oracle predictive signal，不是由 OHLCV 已證實可取得的 alpha。baseline episode_days=31 是旧 episode 配置，不能代替 oracle construction、value-network weights、policy priors 或 training identity。

## Required data

來源 14-ETF universe、holdings/price/cost state、microstructure impact inputs、歷史 paths 及 engineered oracle signal。

Historical cohort resolution、parameters 與 data cutoff 以 Evidence 的原 JSON 為準，不補齊不存在的字段，不降採樣、不改 symbol。baseline 不含完整行情 manifest、signal arrays、model checkpoints 或逐筆 trade ledger；它不是可直接執行的策略定義。

## Execution assumptions

來源多期 portfolio holdings jump、self-financing/cost accounting 與 price impact，並非單幣 DCA。episode window 改變亦會影響 objective。

Historical DCA 參數只代表當時研究配置，並非 paper 原生規則，也不是目前 house overlay。未重新量測 fees、funding、margin/liquidation、slippage、intrabar path 或 fills；hash references 不是原資料 bytes 已重新驗證的宣告。

## Evidence

### Source-reported

本輪讀取 versioned primary landing 的 abstract，確認上述 method-level 主張；更細的 signal 配置以釘選原研究紀錄為轉錄來源，未宣稱已重新逐式審閱整篇 methods 或 source code。原文績效不是下列 crypto baseline metrics。

### Independently reproduced

Not independently reproduced. 本輪只驗 source identity／文件轉錄，沒有 Qlib rerun、Hummingbot reproduction、Paper 或 Testnet。

### Negative evidence

來源摘要明列 oracle signal dependency；不能將 controller 效能說成真實 predictive factor alpha。舊 Wiki 的 2026-07-14 submission 與 pinned landing 的 2026-07-16 不同，採版本 landing；oracle / overlap / calibration gaps 仍保留。

### HISTORICAL QLIB SURVIVOR EVIDENCE — 非目前 Hummingbot reproduction

以下每個 baseline JSON 保留全部原鍵／數值／null／巢狀結構，唯一刪除 top-level `bundle_path` 的機器絕對路徑。bundle 邏輯定位仍可由 family_id / round_id / run_id 與 survivor ID 找到；不假裝本輪讀取已退役結果盤。每筆獨立列 raw baseline-file SHA-256，它與 `params_sha256`、`bundle_sha256`（檔案 bytes）、`bundle_identity_sha256`（歷史 identity recipe）互不相同。

鍵名 `net_pnl` / `sharpe` / `max_dd_pct` / `annualized_return` 原樣保留，不重命名成 ROI、不對 MDD 改 sign／比例／百分點、不跨 lineage 默認同一 annualization。baseline 欄位缺席不同於 null；不從另一層悄悄補值。`source_verdict: PASS` 與 `neighbourhood.passed` 都是 HISTORICAL，不能解讀成今日 efficacy、source parity 或 HB_READY PASS。

每筆另列 `leaderboard_snapshot`：`additional_fields` 為 derived index 額外欄位，`baseline_field_overrides` 為該 index 與 baseline 不同的完整 top-level 值；空 object 明示無差異。兩者都不回寫 baseline。僅非 null 的 `evidence_manifest_path` 去除原 results-root 絕對前綴，保留 `_survivors/...` 相對 locator；null 留 null。rank / top10 / package PRESENT / FROZEN_ONLY 只是當時 derived state，不能解讀為今天 evidence package bytes 存在或新 forward evidence。

#### sv-08c12cb88115a730 — HISTORICAL

Baseline file SHA-256：`beac001793342c9099818a2a1dc05c69bb827d3b76da36288c26ce0585fd8f26`；archive locator：`survivors/sv-08c12cb88115a730/baseline.json`。

```json
{"survivor_id":"sv-08c12cb88115a730","family_id":"sciphy-physics-informed-reinforcement-learning-portfolio-optimization-2026-09-02","round_id":"sciphy-physics-informed-reinforcement-learning-portfolio-optimization-2026-09-02-r1","run_id":"sciphy-physics-informed-reinforcement-learning-portfolio-optimization-2026-09-02-r1-u2","kanban_task_id":null,"cohort":"BNBUSDT/1d","symbol":"BNBUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"episode_days":63},"dca_params":{"spacing_pct":0.02,"size_multiplier":1.0,"breakeven_tp_pct":0.02,"invalidation_pct":0.1},"params_sha256":"sha256:9217408c9c4f2417b6726213a326f5206af5d4e7998b3494d89a9fe2b4d3850f","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:9d45e2a4ab41bf880666adc55705c8a20f25badb1a581bf3d1a3f1316ccd8748","bundle_identity_sha256":"sha256:8a4d1ed4812807012dc6a07b27527bb6a49ba11a174d540e498146bebb53bad6","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":158120.66526653437,"sharpe":3.1194340237449834,"episodes":1064,"max_dd_pct":34.06000323633268},"oos":{"net_pnl":32361.75667470534,"sharpe":3.002137037079713,"episodes":263,"max_dd_pct":22.046851838218192},"full":{"net_pnl":190431.2221496571,"sharpe":2.9854056453868374,"episodes":1330,"max_dd_pct":34.06000323633268,"annualized_return":0.5287672013048101,"avg_trades_per_year":283.2551020408163},"robustness":{"fee_2x":{"net_pnl":167459.5124078826,"sharpe":2.701132316384578,"max_dd_pct":35.678596366395915},"funding_2x":{"net_pnl":190209.43229638066,"sharpe":2.983562647025284,"max_dd_pct":34.06000323633268},"entry_delay_1_bar":{"net_pnl":149144.90613691165,"sharpe":2.444989870461816,"max_dd_pct":25.324763293086317},"slippage_2ticks":{"net_pnl":189940.87540140352,"sharpe":2.9777378539760635,"max_dd_pct":34.112699944525524}},"robustness_stress_floor_net_pnl":149144.90613691165,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":7,"agreeing":7}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-08c12cb88115a730","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":36,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-2ed50c3d117ed330 — HISTORICAL

Baseline file SHA-256：`aa1ed8b7ba7c0ef3198a3db5fc2fb985ee06c23618b49554ece302b5a2a40ff3`；archive locator：`survivors/sv-2ed50c3d117ed330/baseline.json`。

```json
{"survivor_id":"sv-2ed50c3d117ed330","family_id":"sciphy-physics-informed-reinforcement-learning-portfolio-optimization-2026-09-02","round_id":"sciphy-physics-informed-reinforcement-learning-portfolio-optimization-2026-09-02-r1","run_id":"sciphy-physics-informed-reinforcement-learning-portfolio-optimization-2026-09-02-r1-u2","kanban_task_id":null,"cohort":"SOLUSDT/1d","symbol":"SOLUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"episode_days":31},"dca_params":{"spacing_pct":0.02,"size_multiplier":1.0,"breakeven_tp_pct":0.03,"invalidation_pct":0.1},"params_sha256":"sha256:9ed0e70d57a2066e523d5ec91a9fcf3dd55771d3fdfc503592feb18715ecaa85","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:9d45e2a4ab41bf880666adc55705c8a20f25badb1a581bf3d1a3f1316ccd8748","bundle_identity_sha256":"sha256:8a4d1ed4812807012dc6a07b27527bb6a49ba11a174d540e498146bebb53bad6","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":317177.12039370683,"sharpe":3.3701073562849992,"episodes":1182,"max_dd_pct":28.380946829198955},"oos":{"net_pnl":65778.95765972455,"sharpe":4.451142527661579,"episodes":278,"max_dd_pct":15.059956368534985},"full":{"net_pnl":381843.81220767327,"sharpe":3.1955586015276722,"episodes":1460,"max_dd_pct":28.380946829198955,"annualized_return":0.7462866039659946,"avg_trades_per_year":310.9416909620991},"robustness":{"fee_2x":{"net_pnl":348503.14432098716,"sharpe":2.952354689455265,"max_dd_pct":30.440186266450368},"funding_2x":{"net_pnl":381784.5156373022,"sharpe":3.195320940943385,"max_dd_pct":28.380946829198955},"entry_delay_1_bar":{"net_pnl":237586.23166475445,"sharpe":1.5679320375475823,"max_dd_pct":55.52404479428302},"slippage_2ticks":{"net_pnl":372916.6394174598,"sharpe":3.1050934476136596,"max_dd_pct":28.846023891029287}},"robustness_stress_floor_net_pnl":237586.23166475445,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":0.8333333333333334,"passed":true,"neighbours":6,"agreeing":5}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-2ed50c3d117ed330","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":22,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-785f3f7bfd931b7c — HISTORICAL

Baseline file SHA-256：`535a8a78577d87bb5379be4540e32e5bd13bf47b4a271a397eb459681dc38aad`；archive locator：`survivors/sv-785f3f7bfd931b7c/baseline.json`。

```json
{"survivor_id":"sv-785f3f7bfd931b7c","family_id":"sciphy-physics-informed-reinforcement-learning-portfolio-optimization-2026-09-02","round_id":"sciphy-physics-informed-reinforcement-learning-portfolio-optimization-2026-09-02-r1","run_id":"sciphy-physics-informed-reinforcement-learning-portfolio-optimization-2026-09-02-r1-u2","kanban_task_id":null,"cohort":"BTCUSDT/1d","symbol":"BTCUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"episode_days":31},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.0,"breakeven_tp_pct":0.01,"invalidation_pct":0.1},"params_sha256":"sha256:270d5eef2032262458244c291e55e7d4e961cbb7149517cad4b7659b95fdfb72","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:9d45e2a4ab41bf880666adc55705c8a20f25badb1a581bf3d1a3f1316ccd8748","bundle_identity_sha256":"sha256:8a4d1ed4812807012dc6a07b27527bb6a49ba11a174d540e498146bebb53bad6","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":215254.21396378535,"sharpe":7.425539724579532,"episodes":1250,"max_dd_pct":9.367857976349695},"oos":{"net_pnl":52987.989957732265,"sharpe":16.729391715148406,"episodes":317,"max_dd_pct":1.6037317418699528},"full":{"net_pnl":268438.3283053558,"sharpe":7.185188392339665,"episodes":1568,"max_dd_pct":9.367857976349695,"annualized_return":0.6305930258370396,"avg_trades_per_year":333.9428571428571},"robustness":{"fee_2x":{"net_pnl":231888.64626440866,"sharpe":6.418946121459604,"max_dd_pct":10.552391585521846},"funding_2x":{"net_pnl":268338.8565461052,"sharpe":7.181980240943072,"max_dd_pct":9.367857976349695},"entry_delay_1_bar":{"net_pnl":216479.3986344901,"sharpe":2.2730075138059487,"max_dd_pct":31.398076556353928},"slippage_2ticks":{"net_pnl":268352.73595597065,"sharpe":7.183132578500928,"max_dd_pct":9.373073115683278}},"robustness_stress_floor_net_pnl":216479.3986344901,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":5,"agreeing":5}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-785f3f7bfd931b7c","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":7,"in_top10":true,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-81beb1320ab1a1dc — HISTORICAL

Baseline file SHA-256：`25bc270544ba36e75563f2c0a01ec4c69f707468be521b2d7d33df82eb223529`；archive locator：`survivors/sv-81beb1320ab1a1dc/baseline.json`。

```json
{"survivor_id":"sv-81beb1320ab1a1dc","family_id":"sciphy-physics-informed-reinforcement-learning-portfolio-optimization-2026-09-02","round_id":"sciphy-physics-informed-reinforcement-learning-portfolio-optimization-2026-09-02-r1","run_id":"sciphy-physics-informed-reinforcement-learning-portfolio-optimization-2026-09-02-r1-u2","kanban_task_id":null,"cohort":"ETHUSDT/1d","symbol":"ETHUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"episode_days":63},"dca_params":{"spacing_pct":0.04,"size_multiplier":1.0,"breakeven_tp_pct":0.02,"invalidation_pct":0.1},"params_sha256":"sha256:4d138ea8796efd06047379d817768f538f98e0dfbeeff1b5f2a0cba71679b4a2","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:9d45e2a4ab41bf880666adc55705c8a20f25badb1a581bf3d1a3f1316ccd8748","bundle_identity_sha256":"sha256:8a4d1ed4812807012dc6a07b27527bb6a49ba11a174d540e498146bebb53bad6","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":120432.64186317056,"sharpe":3.548658980676395,"episodes":1090,"max_dd_pct":15.24599352120069},"oos":{"net_pnl":33832.09479548749,"sharpe":6.561671924447264,"episodes":276,"max_dd_pct":6.578520874911106},"full":{"net_pnl":154254.52450489017,"sharpe":3.5312849814833878,"episodes":1367,"max_dd_pct":15.24599352120069,"annualized_return":0.47153855327348193,"avg_trades_per_year":291.13513119533525},"robustness":{"fee_2x":{"net_pnl":136684.1685359699,"sharpe":3.219493784378331,"max_dd_pct":15.484132737231207},"funding_2x":{"net_pnl":154246.4641745457,"sharpe":3.5314376454862497,"max_dd_pct":15.24599352120069},"entry_delay_1_bar":{"net_pnl":116186.216091764,"sharpe":2.7950121663428975,"max_dd_pct":13.493342980953429},"slippage_2ticks":{"net_pnl":154153.10629493187,"sharpe":3.529454494488614,"max_dd_pct":15.247224622765973}},"robustness_stress_floor_net_pnl":116186.216091764,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":0.8333333333333334,"passed":true,"neighbours":6,"agreeing":5}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-81beb1320ab1a1dc","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":14,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
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

`hb_ready_status: NOT_LOSSLESS`。oracle predictor、multi-asset holdings/cost state 與 impact-controlled portfolio actions 都是 pinned lane 不可無損表達的核心。

Research-only、not-approved；不能進目前 Hummingbot/Qlib 績效下游，不是 Paper/Testnet/Live approval。普通 non-Scout reconstruction 紀錄可經獨立 provenance/research review 保留，並非 Scout one-file PASS admission。

## Related Wiki records

`quant/sciphy-physics-informed-reinforcement-learning-portfolio-optimization-2026-09-02.md` — 本紀錄上列 hash 的原研究 provenance，未修改 Wiki。

## Sources

1. Primary：https://arxiv.org/abs/2607.15195v1
2. Pinned historical source：https://github.com/HCH725/alpha-strategy-research/blob/c405adc4795154334d9d50950795b4711f00445d/sciphy-physics-informed-reinforcement-learning-portfolio-optimization-2026-09-02.md
3. Historical baseline/leaderboard archive：https://github.com/HCH725/validated-survivor-research/tree/15c0a95162b60a664b43ac60157225c7300ad789；commit 及 per-baseline raw digests 以上述 Provenance/Evidence 為準，並未聲稱所有 reference 可供匿名讀者直接下載。
