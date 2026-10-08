---
schema: strategy-research-record-v1
hb_ready_status: NOT_LOSSLESS
title: 'Microstructure Alpha: Hierarchical Learning and Cross-Asset Transfer in Cryptocurrency Markets'
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
- https://www.frontiersin.org/journals/blockchain/articles/10.3389/fbloc.2026.1811716/full
- https://github.com/HCH725/alpha-strategy-research/blob/c405adc4795154334d9d50950795b4711f00445d/crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01.md
- HCH725/validated-survivor-research commit 15c0a95162b60a664b43ac60157225c7300ad789
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Microstructure Alpha: Hierarchical Learning and Cross-Asset Transfer in Cryptocurrency Markets

## Provenance

- Family identity：`crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01`；本次 consolidation 只按原 baseline family_id，不依 Sharpe 重新排名／挑選。
- Primary source：https://www.frontiersin.org/journals/blockchain/articles/10.3389/fbloc.2026.1811716/full。
- 既有 source-backed 研究紀錄：commit `c405adc4795154334d9d50950795b4711f00445d`，`crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01.md`，Git blob `f5977d4486cda13ac31ba6d00fdac3cd4bfa5f55`。 Wiki 明列這組 reviewed_commit/reviewed_blob；本輪已核對原 Git object。
- `quant/crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01.md` 的 raw SHA-256 為 `35d0f5af70659b17e6b6195e46a9d412f448da26921a4e5f66fefce506d4b0db`；它在 review-state 的 `ingested_wiki_records` 中，state 最後審查 commit 為 `2799e34c5c7f8d6f7036e35d9ae7468832712c97`。這是 ingestion provenance，不是本輪 source parity 或逐檔新審查；Wiki bytes 不冒稱與原 Git blob 相同。
- Historical input：`HCH725/validated-survivor-research` commit `15c0a95162b60a664b43ac60157225c7300ad789` 的 `survivors/<survivor_id>/baseline.json`，本家族 6 筆，cohorts：`BNBUSDT/1d`, `ETHUSDT/1d`, `ETHUSDT/1h`, `ETHUSDT/5m`, `SOLUSDT/30m`, `SOLUSDT/5m`。
- Derived leaderboard：同一 repo `leaderboard/leaderboard.json`，raw SHA-256 `e8fdd38c8468960eee5b574e93d27615635bcb266fe481ab8c1409720d96c42e`；它不是 frozen bundle 本身，也不是採用 gate。

- Source-to-legacy-Qlib mapping gap：family 名称、strategy flags/case IDs 或舊 PASS 不證明原文 source-native signal、模型 weights、universe、因果時序與執行機制一致。除本紀錄明列已釘選的程式規則外，沒有補造代碼對照。paper方法、研究解讀與historical DCA分層保留；尚未證明多個 legacy codes 對應不同完整 core mechanisms，故不任意拆成新策略。

## Economic mechanism

### Source-reported

來源檢驗 minute-level microstructure features 的弱預測力與 cross-asset / same-asset cross-venue transfer；經 leakage controls 與 retail fees 後，沒有策略保留可交易優勢。

### Research interpretation

這是方法／假說的普通研究封存，不是把歷史 survivor 標籤當成新 alpha。機制層分類與單筆 cohort 的 DCA 收益不同；statistical forecast、risk allocator 或負面 study 均不得被默換成已驗證的 crypto 交易規則。

## Signal

來源 full page §1／Table 4 將目標明列為 5-minute forward log return，並評估 forecast-based long/short policies；不是舊 Wiki 所述完全沒有任何策略評估。九種 microstructure measures、hierarchical models/stability selection/gradient boosting/transfer learning 是研究 pipeline，尚未恢復各 policy 的完整 causal trade rules。baseline model_* 與 dir_* 保留，不以這些 flags 補造模型。

## Required data

本輪讀取來源 full page，§1 明列 Bitcoin、Ethereum、Solana、Avalanche、Chainlink、Polkadot 的 Binance Spot/perpetual minute data，August 2025–February 2026；舊 Wiki 未具名的六幣與完整本文不可得只是當時 retrieval gap。

Historical cohort resolution、parameters 與 data cutoff 以 Evidence 的原 JSON 為準，不補齊不存在的字段，不降採樣、不改 symbol。baseline 不含完整行情 manifest、signal arrays、model checkpoints 或逐筆 trade ledger；它不是可直接執行的策略定義。

## Execution assumptions

來源摘要與 Table 4 指出扣除 exchange fees 後的策略結果為負；確切 policy execution/cost schedule 尚未本輪方法級核對。不能把六筆 historical survivors 稱為該文 replication。

Historical DCA 參數只代表當時研究配置，並非 paper 原生規則，也不是目前 house overlay。未重新量測 fees、funding、margin/liquidation、slippage、intrabar path 或 fills；hash references 不是原資料 bytes 已重新驗證的宣告。

## Evidence

### Source-reported

本輪直接讀取 Frontiers full page 的 abstract、§1 與 Table 4 caption，修正舊摘要對六幣名稱及 policy evaluation 的 retrieval gaps；尚未對全部交易 methods 作逐式重現。原文經濟負面結果不是下列 historical survivor metrics。

### Independently reproduced

Not independently reproduced. 本輪只驗 source identity／文件轉錄，沒有 Qlib rerun、Hummingbot reproduction、Paper 或 Testnet。

### Negative evidence

原文 cross-coin transfer 失效、same-asset spot/perpetual transfer 較好，但 none survives realistic fees。原文目標與 minute inputs 不因舊 1d cohort 而變為 daily source signal。

### HISTORICAL QLIB SURVIVOR EVIDENCE — 非目前 Hummingbot reproduction

以下每個 baseline JSON 保留全部原鍵／數值／null／巢狀結構，唯一刪除 top-level `bundle_path` 的機器絕對路徑。bundle 邏輯定位仍可由 family_id / round_id / run_id 與 survivor ID 找到；不假裝本輪讀取已退役結果盤。每筆獨立列 raw baseline-file SHA-256，它與 `params_sha256`、`bundle_sha256`（檔案 bytes）、`bundle_identity_sha256`（歷史 identity recipe）互不相同。

鍵名 `net_pnl` / `sharpe` / `max_dd_pct` / `annualized_return` 原樣保留，不重命名成 ROI、不對 MDD 改 sign／比例／百分點、不跨 lineage 默認同一 annualization。baseline 欄位缺席不同於 null；不從另一層悄悄補值。`source_verdict: PASS` 與 `neighbourhood.passed` 都是 HISTORICAL，不能解讀成今日 efficacy、source parity 或 HB_READY PASS。

每筆另列 `leaderboard_snapshot`：`additional_fields` 為 derived index 額外欄位，`baseline_field_overrides` 為該 index 與 baseline 不同的完整 top-level 值；空 object 明示無差異。兩者都不回寫 baseline。僅非 null 的 `evidence_manifest_path` 去除原 results-root 絕對前綴，保留 `_survivors/...` 相對 locator；null 留 null。rank / top10 / package PRESENT / FROZEN_ONLY 只是當時 derived state，不能解讀為今天 evidence package bytes 存在或新 forward evidence。

#### sv-0ba274ac9ddf153c — HISTORICAL

Baseline file SHA-256：`44785cb7ce5efbfd7149044d4e1c9762783d17a53518ba73b70da78065fe5ed0`；archive locator：`survivors/sv-0ba274ac9ddf153c/baseline.json`。

```json
{"survivor_id":"sv-0ba274ac9ddf153c","family_id":"crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01","round_id":"crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01-r1","run_id":"crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01-r1-u3","kanban_task_id":null,"cohort":"ETHUSDT/1d","symbol":"ETHUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"dir_long_only":0,"dir_long_short":1,"model_lightgbm":0,"model_sklearn":1},"dca_params":{"spacing_pct":0.04,"size_multiplier":1.1,"breakeven_tp_pct":0.03,"invalidation_pct":0.1},"params_sha256":"sha256:90977e4edce65ed6c21ccb1cccbe921a43a52599f06c4c349e3404ccbd5b7ec8","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:481d3c431f8d527474cf93d5169f2226a7393d41beecce59aa3e31649fb3f5cf","bundle_identity_sha256":"sha256:c3ceb743dcf33f5e2893426a4cab26133bbf72068de56844cd7395617e5809ab","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":17855.381362980974,"sharpe":0.983210620209068,"episodes":158,"max_dd_pct":10.739960751563709},"oos":{"net_pnl":363.99257217436246,"sharpe":0.06163238668878138,"episodes":58,"max_dd_pct":19.49583871436529},"full":{"net_pnl":18219.37393515534,"sharpe":0.7527902455833507,"episodes":216,"max_dd_pct":12.7898289398166,"annualized_return":null,"avg_trades_per_year":46.00233236151603},"robustness":{"fee_2x":{"net_pnl":14748.547663572646,"sharpe":0.6081834551431925,"max_dd_pct":14.513749792412181},"funding_2x":{"net_pnl":18738.284706757608,"sharpe":0.7717496817512183,"max_dd_pct":12.693276652983787},"entry_delay_1_bar":{"net_pnl":12439.56323968905,"sharpe":0.5405771818251353,"max_dd_pct":25.58574331597515},"slippage_2ticks":{"net_pnl":18197.455194301292,"sharpe":0.751834028126923,"max_dd_pct":12.800481292801003}},"robustness_stress_floor_net_pnl":12439.56323968905,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":4,"agreeing":4}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-0ba274ac9ddf153c","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":91,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-46a5e66d310d80d0 — HISTORICAL

Baseline file SHA-256：`bc8cb848899ea00d742ac4cd6d9326cbfec10cc287e975b40e6b35a2fcd52925`；archive locator：`survivors/sv-46a5e66d310d80d0/baseline.json`。

```json
{"survivor_id":"sv-46a5e66d310d80d0","family_id":"crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01","round_id":"crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01-r1","run_id":"crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01-r1-u3","kanban_task_id":null,"cohort":"SOLUSDT/5m","symbol":"SOLUSDT","timeframe":"5m","challenger_of":null,"strategy_params":{"dir_long_only":0,"dir_long_short":1,"model_lightgbm":0,"model_sklearn":1},"dca_params":{"spacing_pct":0.04,"size_multiplier":1.0,"breakeven_tp_pct":0.02,"invalidation_pct":0.1},"params_sha256":"sha256:45785eaf6223dbbbf399c164d635b295ba19c479adc1f2ca76b95ba6a8d12198","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:481d3c431f8d527474cf93d5169f2226a7393d41beecce59aa3e31649fb3f5cf","bundle_identity_sha256":"sha256:c3ceb743dcf33f5e2893426a4cab26133bbf72068de56844cd7395617e5809ab","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":56820.685085162804,"sharpe":1.6445909719230838,"episodes":550,"max_dd_pct":13.411149568659884},"oos":{"net_pnl":10623.753469341242,"sharpe":0.9653626097147666,"episodes":206,"max_dd_pct":20.430309459130815},"full":{"net_pnl":67444.43855450413,"sharpe":1.4737810968401293,"episodes":756,"max_dd_pct":13.411149568659884,"annualized_return":null,"avg_trades_per_year":161.0081632653061},"robustness":{"fee_2x":{"net_pnl":55931.98317593461,"sharpe":1.2216085339169318,"max_dd_pct":15.974262345755111},"funding_2x":{"net_pnl":67534.83999741162,"sharpe":1.4753649084575933,"max_dd_pct":13.285429278965779},"entry_delay_1_bar":{"net_pnl":28158.43448574602,"sharpe":0.5111704480758105,"max_dd_pct":31.588982824309493},"slippage_2ticks":{"net_pnl":65793.31621345812,"sharpe":1.4510265725449167,"max_dd_pct":14.079391574536377}},"robustness_stress_floor_net_pnl":28158.43448574602,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":0.8,"passed":true,"neighbours":5,"agreeing":4}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-46a5e66d310d80d0","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":67,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-68148c39a4b40e15 — HISTORICAL

Baseline file SHA-256：`5649d21412e01df641d116ead1c735610400c4ba1c22fb849ceb2ac68925df55`；archive locator：`survivors/sv-68148c39a4b40e15/baseline.json`。

```json
{"survivor_id":"sv-68148c39a4b40e15","family_id":"crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01","round_id":"crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01-r1","run_id":"crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01-r1-u3","kanban_task_id":null,"cohort":"ETHUSDT/1h","symbol":"ETHUSDT","timeframe":"1h","challenger_of":null,"strategy_params":{"dir_long_only":0,"dir_long_short":1,"model_lightgbm":1,"model_sklearn":0},"dca_params":{"spacing_pct":0.02,"size_multiplier":1.1,"breakeven_tp_pct":0.02,"invalidation_pct":0.05},"params_sha256":"sha256:95be9c21a87c39c244dee7b83d8e2637d13b5502e13c7441210cc8d16668ab44","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:481d3c431f8d527474cf93d5169f2226a7393d41beecce59aa3e31649fb3f5cf","bundle_identity_sha256":"sha256:c3ceb743dcf33f5e2893426a4cab26133bbf72068de56844cd7395617e5809ab","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":43915.66452806147,"sharpe":1.1277899501654431,"episodes":700,"max_dd_pct":33.388013282062026},"oos":{"net_pnl":4126.770688039682,"sharpe":0.34064367539166907,"episodes":269,"max_dd_pct":40.96748531825053},"full":{"net_pnl":46611.58896911353,"sharpe":0.9074920210862696,"episodes":968,"max_dd_pct":33.388013282062026,"annualized_return":null,"avg_trades_per_year":206.15860058309036},"robustness":{"fee_2x":{"net_pnl":27294.570459880302,"sharpe":0.528771705011781,"max_dd_pct":42.963823182976775},"funding_2x":{"net_pnl":47595.155425676516,"sharpe":0.9269556163251246,"max_dd_pct":33.044083714673114},"entry_delay_1_bar":{"net_pnl":13097.652870875027,"sharpe":0.249345808368649,"max_dd_pct":69.32389184775435},"slippage_2ticks":{"net_pnl":44821.55948724265,"sharpe":0.8665103474593645,"max_dd_pct":34.6249817205764}},"robustness_stress_floor_net_pnl":13097.652870875027,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":0.6666666666666666,"passed":true,"neighbours":6,"agreeing":4}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-68148c39a4b40e15","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":83,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-6e773c7f2dabff04 — HISTORICAL

Baseline file SHA-256：`f8195d509747ae2f20288c55a401f69059f71c28914edb95c8875be2b2d5e143`；archive locator：`survivors/sv-6e773c7f2dabff04/baseline.json`。

```json
{"survivor_id":"sv-6e773c7f2dabff04","family_id":"crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01","round_id":"crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01-r1","run_id":"crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01-r1-u3","kanban_task_id":null,"cohort":"BNBUSDT/1d","symbol":"BNBUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"dir_long_only":1,"dir_long_short":0,"model_lightgbm":1,"model_sklearn":0},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.1,"breakeven_tp_pct":0.03,"invalidation_pct":0.05},"params_sha256":"sha256:2eadc2f23e1c0e9afd12101d767e6e1ba1c766276561554b96854b5ed835766e","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:481d3c431f8d527474cf93d5169f2226a7393d41beecce59aa3e31649fb3f5cf","bundle_identity_sha256":"sha256:c3ceb743dcf33f5e2893426a4cab26133bbf72068de56844cd7395617e5809ab","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":40996.04235317043,"sharpe":2.3371550856499645,"episodes":106,"max_dd_pct":5.805942616828931},"oos":{"net_pnl":3833.8884492527577,"sharpe":0.6890907368292473,"episodes":33,"max_dd_pct":14.6942136147513},"full":{"net_pnl":44829.93080242318,"sharpe":1.9310805017239414,"episodes":139,"max_dd_pct":6.3683889435842165,"annualized_return":null,"avg_trades_per_year":29.603352769679297},"robustness":{"fee_2x":{"net_pnl":40902.37371392583,"sharpe":1.7863671514030661,"max_dd_pct":7.134063116432833},"funding_2x":{"net_pnl":46183.643698654814,"sharpe":1.9772914784701994,"max_dd_pct":6.216986404057594},"entry_delay_1_bar":{"net_pnl":33545.926154949324,"sharpe":1.2899359862574924,"max_dd_pct":12.875397502425828},"slippage_2ticks":{"net_pnl":44700.53215210321,"sharpe":1.9260418747918748,"max_dd_pct":6.388694537080587}},"robustness_stress_floor_net_pnl":33545.926154949324,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":4,"agreeing":4}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-6e773c7f2dabff04","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":72,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-6f27a7cd96f739e3 — HISTORICAL

Baseline file SHA-256：`e4d3ccdcf835fb5756f215f194fde11ca5e9e92ad21e61b50eb107928b3185a4`；archive locator：`survivors/sv-6f27a7cd96f739e3/baseline.json`。

```json
{"survivor_id":"sv-6f27a7cd96f739e3","family_id":"crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01","round_id":"crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01-r1","run_id":"crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01-r1-u3","kanban_task_id":null,"cohort":"SOLUSDT/30m","symbol":"SOLUSDT","timeframe":"30m","challenger_of":null,"strategy_params":{"dir_long_only":1,"dir_long_short":0,"model_lightgbm":0,"model_sklearn":1},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.1,"breakeven_tp_pct":0.01,"invalidation_pct":0.1},"params_sha256":"sha256:852bde4cdacc543a1d14bac64dafbac812dc7a8f6246d5ccdf1f43eb64383704","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:481d3c431f8d527474cf93d5169f2226a7393d41beecce59aa3e31649fb3f5cf","bundle_identity_sha256":"sha256:c3ceb743dcf33f5e2893426a4cab26133bbf72068de56844cd7395617e5809ab","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":93525.42292066877,"sharpe":1.3050679208207894,"episodes":691,"max_dd_pct":26.642670346173563},"oos":{"net_pnl":7940.45060886848,"sharpe":0.28837236337477945,"episodes":247,"max_dd_pct":47.268271389765864},"full":{"net_pnl":101465.87352953726,"sharpe":1.0054128241438949,"episodes":938,"max_dd_pct":26.642670346173563,"annualized_return":null,"avg_trades_per_year":199.76938775510203},"robustness":{"fee_2x":{"net_pnl":74999.08208807406,"sharpe":0.7413903898289868,"max_dd_pct":29.36320605405819},"funding_2x":{"net_pnl":101390.88046834416,"sharpe":1.0034099437156443,"max_dd_pct":26.893241084517634},"entry_delay_1_bar":{"net_pnl":112059.99836673576,"sharpe":1.1573336561082053,"max_dd_pct":24.93538929756731},"slippage_2ticks":{"net_pnl":101771.13697354596,"sharpe":1.006208650623804,"max_dd_pct":26.893613414105044}},"robustness_stress_floor_net_pnl":74999.08208807406,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":4,"agreeing":4}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-6f27a7cd96f739e3","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":85,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-e1af21785ce6cffa — HISTORICAL

Baseline file SHA-256：`cd3e47e6979ebc12373465139f7e4401420c85cd5bbf28086c2635972342ac6b`；archive locator：`survivors/sv-e1af21785ce6cffa/baseline.json`。

```json
{"survivor_id":"sv-e1af21785ce6cffa","family_id":"crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01","round_id":"crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01-r1","run_id":"crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01-r1-u3","kanban_task_id":null,"cohort":"ETHUSDT/5m","symbol":"ETHUSDT","timeframe":"5m","challenger_of":null,"strategy_params":{"dir_long_only":1,"dir_long_short":0,"model_lightgbm":0,"model_sklearn":1},"dca_params":{"spacing_pct":0.02,"size_multiplier":1.1,"breakeven_tp_pct":0.02,"invalidation_pct":0.1},"params_sha256":"sha256:cb7eeea2f44068f4933017bc3353d4adf383abc3fe72a640b346b53ac94f2cb1","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:481d3c431f8d527474cf93d5169f2226a7393d41beecce59aa3e31649fb3f5cf","bundle_identity_sha256":"sha256:c3ceb743dcf33f5e2893426a4cab26133bbf72068de56844cd7395617e5809ab","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":50053.895322929115,"sharpe":1.2077839899347598,"episodes":264,"max_dd_pct":25.104166272042804},"oos":{"net_pnl":7938.656741797338,"sharpe":0.36442788332568804,"episodes":126,"max_dd_pct":56.637980350326366},"full":{"net_pnl":57992.55206472642,"sharpe":0.8646755863040968,"episodes":390,"max_dd_pct":25.596415832737172,"annualized_return":null,"avg_trades_per_year":83.05976676384839},"robustness":{"fee_2x":{"net_pnl":47876.80980799568,"sharpe":0.7130588870515803,"max_dd_pct":28.597776193871947},"funding_2x":{"net_pnl":56001.72774471984,"sharpe":0.8339207308806886,"max_dd_pct":26.32296111821243},"entry_delay_1_bar":{"net_pnl":48339.97823448533,"sharpe":0.775960175940317,"max_dd_pct":37.40543308093306},"slippage_2ticks":{"net_pnl":58133.80615310412,"sharpe":0.8669092583666944,"max_dd_pct":25.556108558451214}},"robustness_stress_floor_net_pnl":47876.80980799568,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":6,"agreeing":6}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-e1af21785ce6cffa","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":81,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
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

`hb_ready_status: NOT_LOSSLESS`。minute microstructure/forward target、cross-asset/venue transfer 與未恢復的 causal policy mapping 均不可默轉 single-pair candle-only PASS。

Research-only、not-approved；不能進目前 Hummingbot/Qlib 績效下游，不是 Paper/Testnet/Live approval。普通 non-Scout reconstruction 紀錄可經獨立 provenance/research review 保留，並非 Scout one-file PASS admission。

## Related Wiki records

`quant/crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01.md` — 本紀錄上列 hash 的原研究 provenance，未修改 Wiki。

## Sources

1. Primary：https://www.frontiersin.org/journals/blockchain/articles/10.3389/fbloc.2026.1811716/full
2. Pinned historical source：https://github.com/HCH725/alpha-strategy-research/blob/c405adc4795154334d9d50950795b4711f00445d/crypto-microstructure-alpha-hierarchical-cross-asset-transfer-2026-09-01.md
3. Historical baseline/leaderboard archive：https://github.com/HCH725/validated-survivor-research/tree/15c0a95162b60a664b43ac60157225c7300ad789；commit 及 per-baseline raw digests 以上述 Provenance/Evidence 為準，並未聲稱所有 reference 可供匿名讀者直接下載。
