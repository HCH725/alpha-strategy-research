---
schema: strategy-research-record-v1
hb_ready_status: NOT_LOSSLESS
title: 'RIEnet: End-to-End Neural Shrinkage of Indefinite Pairwise Correlation Matrices for Incomplete Return Panels'
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
- https://arxiv.org/abs/2608.30446v1
- https://github.com/HCH725/alpha-strategy-research/blob/c405adc4795154334d9d50950795b4711f00445d/neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02.md
- HCH725/validated-survivor-research commit 15c0a95162b60a664b43ac60157225c7300ad789
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# RIEnet: End-to-End Neural Shrinkage of Indefinite Pairwise Correlation Matrices for Incomplete Return Panels

## Provenance

- Family identity：`neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02`；本次 consolidation 只按原 baseline family_id，不依 Sharpe 重新排名／挑選。
- Primary source：https://arxiv.org/abs/2608.30446v1。
- 既有 source-backed 研究紀錄：commit `c405adc4795154334d9d50950795b4711f00445d`，`neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02.md`，Git blob `eab96b9b8f90b29b0b964bebc8609df56f7386f6`。 Wiki 明列這組 reviewed_commit/reviewed_blob；本輪已核對原 Git object。
- `quant/neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02.md` 的 raw SHA-256 為 `86b780b0d0989ca07978e429bddde7cf38781ea8f3a6860905154b07f844b415`；它在 review-state 的 `ingested_wiki_records` 中，state 最後審查 commit 為 `2799e34c5c7f8d6f7036e35d9ae7468832712c97`。這是 ingestion provenance，不是本輪 source parity 或逐檔新審查；Wiki bytes 不冒稱與原 Git blob 相同。
- Historical input：`HCH725/validated-survivor-research` commit `15c0a95162b60a664b43ac60157225c7300ad789` 的 `survivors/<survivor_id>/baseline.json`，本家族 7 筆，cohorts：`BNBUSDT/1d`, `BTCUSDT/15m`, `BTCUSDT/5m`, `ETHUSDT/15m`, `ETHUSDT/1d`, `ETHUSDT/1h`, `SOLUSDT/5m`。
- Derived leaderboard：同一 repo `leaderboard/leaderboard.json`，raw SHA-256 `e8fdd38c8468960eee5b574e93d27615635bcb266fe481ab8c1409720d96c42e`；它不是 frozen bundle 本身，也不是採用 gate。

- Source-to-legacy-Qlib mapping gap：family 名称、strategy flags/case IDs 或舊 PASS 不證明原文 source-native signal、模型 weights、universe、因果時序與執行機制一致。除本紀錄明列已釘選的程式規則外，沒有補造代碼對照。paper方法、研究解讀與historical DCA分層保留；尚未證明多個 legacy codes 對應不同完整 core mechanisms，故不任意拆成新策略。

## Economic mechanism

### Source-reported

RIEnet 對 incomplete return panels 的 indefinite pairwise correlation matrix 作 neural spectral shrinkage。它將含負值的 spectrum 轉成 positive inverse spectrum，使重建 covariance 正定，再以 five-day GMV risk 訓練。

### Research interpretation

這是方法／假說的普通研究封存，不是把歷史 survivor 標籤當成新 alpha。機制層分類與單筆 cohort 的 DCA 收益不同；statistical forecast、risk allocator 或負面 study 均不得被默換成已驗證的 crypto 交易規則。

## Signal

Observation masks / overlap counts + signed eigenvalues/eigenvectors → effective factor sample lengths → BiGRU spectrum mapping → positive-definite covariance → long-only GMV weights。baseline lookback_days/vol_branch_code 不證明 neural weights、mask logic 或 marginal-vol branch 與原文相同。

## Required data

來源為 point-in-time US equity universe（最多 1,500 stocks）、ragged adjusted returns、mask/overlap matrix、corporate actions 與 closing-auction execution inputs。

Historical cohort resolution、parameters 與 data cutoff 以 Evidence 的原 JSON 為準，不補齊不存在的字段，不降採樣、不改 symbol。baseline 不含完整行情 manifest、signal arrays、model checkpoints 或逐筆 trade ledger；它不是可直接執行的策略定義。

## Execution assumptions

來源在多股票 GMV portfolio、five-day risk objective 與 execution-friction simulator 中評估，不是對單幣下方向單。

Historical DCA 參數只代表當時研究配置，並非 paper 原生規則，也不是目前 house overlay。未重新量測 fees、funding、margin/liquidation、slippage、intrabar path 或 fills；hash references 不是原資料 bytes 已重新驗證的宣告。

## Evidence

### Source-reported

本輪讀取 versioned primary landing 的 abstract，確認上述 method-level 主張；更細的 signal 配置以釘選原研究紀錄為轉錄來源，未宣稱已重新逐式審閱整篇 methods 或 source code。原文績效不是下列 crypto baseline metrics。

### Independently reproduced

Not independently reproduced. 本輪只驗 source identity／文件轉錄，沒有 Qlib rerun、Hummingbot reproduction、Paper 或 Testnet。

### Negative evidence

Positive definiteness / variance reduction 不等於 crypto predictive alpha；需避免 survivorship、imputation 與 pairwise-overlap changes 混為同一估計量。baseline 多 resolution 結果並未證明原文 equity universe/model parity。

### HISTORICAL QLIB SURVIVOR EVIDENCE — 非目前 Hummingbot reproduction

以下每個 baseline JSON 保留全部原鍵／數值／null／巢狀結構，唯一刪除 top-level `bundle_path` 的機器絕對路徑。bundle 邏輯定位仍可由 family_id / round_id / run_id 與 survivor ID 找到；不假裝本輪讀取已退役結果盤。每筆獨立列 raw baseline-file SHA-256，它與 `params_sha256`、`bundle_sha256`（檔案 bytes）、`bundle_identity_sha256`（歷史 identity recipe）互不相同。

鍵名 `net_pnl` / `sharpe` / `max_dd_pct` / `annualized_return` 原樣保留，不重命名成 ROI、不對 MDD 改 sign／比例／百分點、不跨 lineage 默認同一 annualization。baseline 欄位缺席不同於 null；不從另一層悄悄補值。`source_verdict: PASS` 與 `neighbourhood.passed` 都是 HISTORICAL，不能解讀成今日 efficacy、source parity 或 HB_READY PASS。

每筆另列 `leaderboard_snapshot`：`additional_fields` 為 derived index 額外欄位，`baseline_field_overrides` 為該 index 與 baseline 不同的完整 top-level 值；空 object 明示無差異。兩者都不回寫 baseline。僅非 null 的 `evidence_manifest_path` 去除原 results-root 絕對前綴，保留 `_survivors/...` 相對 locator；null 留 null。rank / top10 / package PRESENT / FROZEN_ONLY 只是當時 derived state，不能解讀為今天 evidence package bytes 存在或新 forward evidence。

#### sv-74d5537abfa07966 — HISTORICAL

Baseline file SHA-256：`640e9e570e1f427d4a4c90ed8e29bb384888929952314c5cb97c481b5661d0fc`；archive locator：`survivors/sv-74d5537abfa07966/baseline.json`。

```json
{"survivor_id":"sv-74d5537abfa07966","family_id":"neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02","round_id":"neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02-r1","run_id":"neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02-r1-u1","kanban_task_id":null,"cohort":"BTCUSDT/15m","symbol":"BTCUSDT","timeframe":"15m","challenger_of":null,"strategy_params":{"lookback_days":600,"vol_branch_code":0},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.0,"breakeven_tp_pct":0.01,"invalidation_pct":0.1},"params_sha256":"sha256:c05ebc270ee1c12a7ef3f6e2cdef16cbfc1318efc8a158c3597218d7c2a6fd02","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:eb8bf8f86befe731150bb057c9b227d17981df6fe75ebfc4565d7aa1d599ff94","bundle_identity_sha256":"sha256:4a0681025f2890e2226221d3076ea1e1a4985320d731a2fb2660bd97f45845b6","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":26839.49450109773,"sharpe":1.0040953826814836,"episodes":262,"max_dd_pct":20.010885369187957},"oos":{"net_pnl":6478.703083749845,"sharpe":1.7045139083355165,"episodes":65,"max_dd_pct":9.422957155809577},"full":{"net_pnl":33318.197584847585,"sharpe":1.0717808132049498,"episodes":327,"max_dd_pct":20.010885369187957,"annualized_return":null,"avg_trades_per_year":69.64241982507288},"robustness":{"fee_2x":{"net_pnl":25016.713060140537,"sharpe":0.8029967287405616,"max_dd_pct":22.489034206393633},"funding_2x":{"net_pnl":31968.83028031367,"sharpe":1.023540445980219,"max_dd_pct":20.561560197671984},"entry_delay_1_bar":{"net_pnl":20590.475391970205,"sharpe":0.5066915559824942,"max_dd_pct":39.717544850524305},"slippage_2ticks":{"net_pnl":33292.40084145145,"sharpe":1.0709307931350154,"max_dd_pct":20.01834501584929}},"robustness_stress_floor_net_pnl":20590.475391970205,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":6,"agreeing":6}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-74d5537abfa07966","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":53,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-7a7d52beb8117f0b — HISTORICAL

Baseline file SHA-256：`aa8312d90d82d15b99dd2a9c157cfe2ed7c6171be4179bbf795a5010c2c4ed0a`；archive locator：`survivors/sv-7a7d52beb8117f0b/baseline.json`。

```json
{"survivor_id":"sv-7a7d52beb8117f0b","family_id":"neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02","round_id":"neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02-r1","run_id":"neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02-r1-u1","kanban_task_id":null,"cohort":"BTCUSDT/5m","symbol":"BTCUSDT","timeframe":"5m","challenger_of":null,"strategy_params":{"lookback_days":600,"vol_branch_code":0},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.0,"breakeven_tp_pct":0.01,"invalidation_pct":0.1},"params_sha256":"sha256:c05ebc270ee1c12a7ef3f6e2cdef16cbfc1318efc8a158c3597218d7c2a6fd02","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:eb8bf8f86befe731150bb057c9b227d17981df6fe75ebfc4565d7aa1d599ff94","bundle_identity_sha256":"sha256:4a0681025f2890e2226221d3076ea1e1a4985320d731a2fb2660bd97f45845b6","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":26895.690834661582,"sharpe":1.012628682888191,"episodes":262,"max_dd_pct":20.053130253632393},"oos":{"net_pnl":6709.708684769027,"sharpe":1.8532177450881637,"episodes":65,"max_dd_pct":8.711261093441541},"full":{"net_pnl":33605.399519430604,"sharpe":1.0912014518412774,"episodes":327,"max_dd_pct":20.053130253632393,"annualized_return":null,"avg_trades_per_year":69.64241982507288},"robustness":{"fee_2x":{"net_pnl":25393.84067188072,"sharpe":0.8227644956390221,"max_dd_pct":22.50708141720431},"funding_2x":{"net_pnl":32304.662786645717,"sharpe":1.0440363690278676,"max_dd_pct":20.605345156783564},"entry_delay_1_bar":{"net_pnl":33974.411771738516,"sharpe":1.0997714477673677,"max_dd_pct":20.000854718436116},"slippage_2ticks":{"net_pnl":33579.892218924506,"sharpe":1.0903529126903662,"max_dd_pct":20.06056122609388}},"robustness_stress_floor_net_pnl":25393.84067188072,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":6,"agreeing":6}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-7a7d52beb8117f0b","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":49,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-8314773d900382aa — HISTORICAL

Baseline file SHA-256：`3704bb4a99343eb9835bbbe7555108810a52247b32cb0bf049067b129196a6c6`；archive locator：`survivors/sv-8314773d900382aa/baseline.json`。

```json
{"survivor_id":"sv-8314773d900382aa","family_id":"neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02","round_id":"neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02-r1","run_id":"neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02-r1-u1","kanban_task_id":null,"cohort":"ETHUSDT/1d","symbol":"ETHUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"lookback_days":600,"vol_branch_code":0},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.1,"breakeven_tp_pct":0.03,"invalidation_pct":0.05},"params_sha256":"sha256:d02928a65ef246b8e68dfea370dbfbc0d199b75edee34e8fc67cea9c50b6de74","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:eb8bf8f86befe731150bb057c9b227d17981df6fe75ebfc4565d7aa1d599ff94","bundle_identity_sha256":"sha256:4a0681025f2890e2226221d3076ea1e1a4985320d731a2fb2660bd97f45845b6","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":38453.79875918646,"sharpe":1.0614773799285575,"episodes":244,"max_dd_pct":21.775529916315207},"oos":{"net_pnl":3603.776158887714,"sharpe":0.395744836292933,"episodes":60,"max_dd_pct":43.58352100866852},"full":{"net_pnl":42057.57491807416,"sharpe":0.9279228443475509,"episodes":304,"max_dd_pct":21.775529916315207,"annualized_return":null,"avg_trades_per_year":64.74402332361515},"robustness":{"fee_2x":{"net_pnl":34011.0379573083,"sharpe":0.7514478350689077,"max_dd_pct":24.334299596551283},"funding_2x":{"net_pnl":38887.421665184156,"sharpe":0.8583434229919192,"max_dd_pct":22.91337574246398},"entry_delay_1_bar":{"net_pnl":32330.041612633064,"sharpe":0.7775916456499676,"max_dd_pct":21.55292107810039},"slippage_2ticks":{"net_pnl":42012.86562669519,"sharpe":0.9269482166139613,"max_dd_pct":21.788373902112145}},"robustness_stress_floor_net_pnl":32330.041612633064,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":6,"agreeing":6}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-8314773d900382aa","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":80,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-9e5b5054b4639cea — HISTORICAL

Baseline file SHA-256：`2fc2c55b1b68b9c7bbc9c7e9d8282fabd53d84c678ab8eff222615ecf00d13a2`；archive locator：`survivors/sv-9e5b5054b4639cea/baseline.json`。

```json
{"survivor_id":"sv-9e5b5054b4639cea","family_id":"neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02","round_id":"neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02-r1","run_id":"neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02-r1-u1","kanban_task_id":null,"cohort":"BNBUSDT/1d","symbol":"BNBUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"lookback_days":1200,"vol_branch_code":0},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.1,"breakeven_tp_pct":0.03,"invalidation_pct":0.05},"params_sha256":"sha256:e063f2641fa0c1a9eb8c364760e2093e574c034e8eb649a4a3fdae9f73192e66","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:eb8bf8f86befe731150bb057c9b227d17981df6fe75ebfc4565d7aa1d599ff94","bundle_identity_sha256":"sha256:4a0681025f2890e2226221d3076ea1e1a4985320d731a2fb2660bd97f45845b6","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":50427.48372995548,"sharpe":1.5374628188102093,"episodes":225,"max_dd_pct":14.751899322382867},"oos":{"net_pnl":9998.552343414785,"sharpe":1.3370519191608587,"episodes":32,"max_dd_pct":15.068248697118007},"full":{"net_pnl":60426.036073370284,"sharpe":1.499399201599897,"episodes":257,"max_dd_pct":14.751899322382867,"annualized_return":null,"avg_trades_per_year":54.734256559766756},"robustness":{"fee_2x":{"net_pnl":52976.318576301775,"sharpe":1.3224374385240965,"max_dd_pct":16.8386309359738},"funding_2x":{"net_pnl":63493.71770679489,"sharpe":1.5881677368875693,"max_dd_pct":13.138183379110721},"entry_delay_1_bar":{"net_pnl":21613.486524311687,"sharpe":0.5225068087566667,"max_dd_pct":22.18486000637281},"slippage_2ticks":{"net_pnl":60167.464366126966,"sharpe":1.4931976640759064,"max_dd_pct":14.85883249404211}},"robustness_stress_floor_net_pnl":21613.486524311687,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":6,"agreeing":6}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-9e5b5054b4639cea","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":58,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-ae376718fb470c4c — HISTORICAL

Baseline file SHA-256：`9c8525e045a4f75ad18a6f1bbb7dad2b6e498365708aa28cc59b72baa683e8ee`；archive locator：`survivors/sv-ae376718fb470c4c/baseline.json`。

```json
{"survivor_id":"sv-ae376718fb470c4c","family_id":"neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02","round_id":"neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02-r1","run_id":"neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02-r1-u1","kanban_task_id":null,"cohort":"ETHUSDT/1h","symbol":"ETHUSDT","timeframe":"1h","challenger_of":null,"strategy_params":{"lookback_days":600,"vol_branch_code":0},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.0,"breakeven_tp_pct":0.03,"invalidation_pct":0.05},"params_sha256":"sha256:1440cbdd90f5e6094fed89a9d71416c5a8687b7a8e31292b7b9a5fc9911127b1","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:eb8bf8f86befe731150bb057c9b227d17981df6fe75ebfc4565d7aa1d599ff94","bundle_identity_sha256":"sha256:4a0681025f2890e2226221d3076ea1e1a4985320d731a2fb2660bd97f45845b6","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":37109.03527548149,"sharpe":0.8315200158837942,"episodes":252,"max_dd_pct":36.515279412379584},"oos":{"net_pnl":528.554299593909,"sharpe":0.04040197236312226,"episodes":62,"max_dd_pct":49.76875826137735},"full":{"net_pnl":37637.58957507541,"sharpe":0.6510688879021429,"episodes":314,"max_dd_pct":36.515279412379584,"annualized_return":null,"avg_trades_per_year":66.8737609329446},"robustness":{"fee_2x":{"net_pnl":26902.18823230916,"sharpe":0.46394177229390565,"max_dd_pct":37.264111536640435},"funding_2x":{"net_pnl":35207.89496040364,"sharpe":0.60830544063004,"max_dd_pct":36.612641888879324},"entry_delay_1_bar":{"net_pnl":1434.729604001489,"sharpe":0.023735557711928774,"max_dd_pct":67.69314473518821},"slippage_2ticks":{"net_pnl":37574.76810027026,"sharpe":0.6499737873055452,"max_dd_pct":36.51769581024998}},"robustness_stress_floor_net_pnl":1434.729604001489,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":0.8333333333333334,"passed":true,"neighbours":6,"agreeing":5}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-ae376718fb470c4c","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":92,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-f76bfd0f2ea40f71 — HISTORICAL

Baseline file SHA-256：`15260dce835662c6196bcc3c7df1748bed2c7a7fb77d55f13e436fa50e72095b`；archive locator：`survivors/sv-f76bfd0f2ea40f71/baseline.json`。

```json
{"survivor_id":"sv-f76bfd0f2ea40f71","family_id":"neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02","round_id":"neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02-r1","run_id":"neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02-r1-u1","kanban_task_id":null,"cohort":"ETHUSDT/15m","symbol":"ETHUSDT","timeframe":"15m","challenger_of":null,"strategy_params":{"lookback_days":600,"vol_branch_code":0},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.0,"breakeven_tp_pct":0.03,"invalidation_pct":0.05},"params_sha256":"sha256:1440cbdd90f5e6094fed89a9d71416c5a8687b7a8e31292b7b9a5fc9911127b1","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:eb8bf8f86befe731150bb057c9b227d17981df6fe75ebfc4565d7aa1d599ff94","bundle_identity_sha256":"sha256:4a0681025f2890e2226221d3076ea1e1a4985320d731a2fb2660bd97f45845b6","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":20399.09660013247,"sharpe":0.40430118598548104,"episodes":250,"max_dd_pct":45.36104111572404},"oos":{"net_pnl":3864.281934073457,"sharpe":0.28249726076960885,"episodes":62,"max_dd_pct":38.16898463771104},"full":{"net_pnl":24263.37853420591,"sharpe":0.37828486170503356,"episodes":312,"max_dd_pct":45.36104111572404,"annualized_return":null,"avg_trades_per_year":66.44781341107871},"robustness":{"fee_2x":{"net_pnl":12664.079049490196,"sharpe":0.19651316115240583,"max_dd_pct":48.9773044389317},"funding_2x":{"net_pnl":21527.087121714394,"sharpe":0.33493967454781615,"max_dd_pct":45.687793979973065},"entry_delay_1_bar":{"net_pnl":18997.01711433195,"sharpe":0.2928000346368907,"max_dd_pct":66.4438002032527},"slippage_2ticks":{"net_pnl":24194.503127382202,"sharpe":0.3772032726831969,"max_dd_pct":45.38158187001869}},"robustness_stress_floor_net_pnl":12664.079049490196,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":0.8333333333333334,"passed":true,"neighbours":6,"agreeing":5}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-f76bfd0f2ea40f71","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":86,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-fdd9f3f39e846f57 — HISTORICAL

Baseline file SHA-256：`b1b610097dde4ff8a046ce01748f346a201d5678c7ac014a046f5dc29a994483`；archive locator：`survivors/sv-fdd9f3f39e846f57/baseline.json`。

```json
{"survivor_id":"sv-fdd9f3f39e846f57","family_id":"neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02","round_id":"neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02-r1","run_id":"neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02-r1-u1","kanban_task_id":null,"cohort":"SOLUSDT/5m","symbol":"SOLUSDT","timeframe":"5m","challenger_of":null,"strategy_params":{"lookback_days":1200,"vol_branch_code":0},"dca_params":{"spacing_pct":0.02,"size_multiplier":1.1,"breakeven_tp_pct":0.01,"invalidation_pct":0.1},"params_sha256":"sha256:553ab2240df10ec33640b84fdf2305880dc07d4281b0cbcef239c220f15a17c5","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:eb8bf8f86befe731150bb057c9b227d17981df6fe75ebfc4565d7aa1d599ff94","bundle_identity_sha256":"sha256:4a0681025f2890e2226221d3076ea1e1a4985320d731a2fb2660bd97f45845b6","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":15207.654612791925,"sharpe":1.7073904577252008,"episodes":107,"max_dd_pct":8.466054417201878},"oos":{"net_pnl":4637.347340474425,"sharpe":1.0753663967771976,"episodes":64,"max_dd_pct":13.755499320651108},"full":{"net_pnl":19845.001953266354,"sharpe":1.4346600713153803,"episodes":171,"max_dd_pct":9.690719124762529,"annualized_return":null,"avg_trades_per_year":36.41851311953352},"robustness":{"fee_2x":{"net_pnl":16228.238499653664,"sharpe":1.1875849695447978,"max_dd_pct":10.792930584696643},"funding_2x":{"net_pnl":21195.82033476499,"sharpe":1.529756494370513,"max_dd_pct":9.060820761485875},"entry_delay_1_bar":{"net_pnl":2220.6140010688073,"sharpe":0.0582587820522001,"max_dd_pct":42.64349831473365},"slippage_2ticks":{"net_pnl":2411.134086121073,"sharpe":0.06420877219257644,"max_dd_pct":48.52166277359136}},"robustness_stress_floor_net_pnl":2220.6140010688073,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":0.7142857142857143,"passed":true,"neighbours":7,"agreeing":5}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-fdd9f3f39e846f57","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":61,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
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

`hb_ready_status: NOT_LOSSLESS`。ragged cross-asset covariance、portfolio weights/shared capital 與 auction simulator 不符合單 pair candle-only event model。

Research-only、not-approved；不能進目前 Hummingbot/Qlib 績效下游，不是 Paper/Testnet/Live approval。普通 non-Scout reconstruction 紀錄可經獨立 provenance/research review 保留，並非 Scout one-file PASS admission。

## Related Wiki records

`quant/neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02.md` — 本紀錄上列 hash 的原研究 provenance，未修改 Wiki。

## Sources

1. Primary：https://arxiv.org/abs/2608.30446v1
2. Pinned historical source：https://github.com/HCH725/alpha-strategy-research/blob/c405adc4795154334d9d50950795b4711f00445d/neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02.md
3. Historical baseline/leaderboard archive：https://github.com/HCH725/validated-survivor-research/tree/15c0a95162b60a664b43ac60157225c7300ad789；commit 及 per-baseline raw digests 以上述 Provenance/Evidence 為準，並未聲稱所有 reference 可供匿名讀者直接下載。
