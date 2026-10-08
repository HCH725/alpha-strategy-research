---
schema: strategy-research-record-v1
hb_ready_status: NOT_LOSSLESS
title: 'Cross-Sectional Volatility Forecasting via Regime-Gated Residual Mixture-of-Experts (RG-ResMoE): Frozen Base Anchoring, Soft State-Dependent
  Routing, and Downside VaR Calibration'
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
- https://arxiv.org/abs/2608.12251v1
- https://github.com/HCH725/alpha-strategy-research/blob/c405adc4795154334d9d50950795b4711f00445d/cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02.md
- HCH725/validated-survivor-research commit 15c0a95162b60a664b43ac60157225c7300ad789
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Cross-Sectional Volatility Forecasting via Regime-Gated Residual Mixture-of-Experts (RG-ResMoE): Frozen Base Anchoring, Soft State-Dependent Routing, and Downside VaR Calibration

## Provenance

- Family identity：`cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02`；本次 consolidation 只按原 baseline family_id，不依 Sharpe 重新排名／挑選。
- Primary source：https://arxiv.org/abs/2608.12251v1。
- 既有 source-backed 研究紀錄：commit `c405adc4795154334d9d50950795b4711f00445d`，`cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02.md`，Git blob `e14e1285d19a9a847304d29be77017e5af0e4ea2`。 Wiki 明列這組 reviewed_commit/reviewed_blob；本輪已核對原 Git object。
- `quant/cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02.md` 的 raw SHA-256 為 `7161860351502a09b3ca1efaa49f2c209cedc39c186e78403e60f1af94efd0c7`；它在 review-state 的 `ingested_wiki_records` 中，state 最後審查 commit 為 `2799e34c5c7f8d6f7036e35d9ae7468832712c97`。這是 ingestion provenance，不是本輪 source parity 或逐檔新審查；Wiki bytes 不冒稱與原 Git blob 相同。
- Historical input：`HCH725/validated-survivor-research` commit `15c0a95162b60a664b43ac60157225c7300ad789` 的 `survivors/<survivor_id>/baseline.json`，本家族 5 筆，cohorts：`BTCUSDT/1d`, `ETHUSDT/30m`, `ETHUSDT/4h`, `ETHUSDT/5m`, `SOLUSDT/4h`。
- Derived leaderboard：同一 repo `leaderboard/leaderboard.json`，raw SHA-256 `e8fdd38c8468960eee5b574e93d27615635bcb266fe481ab8c1409720d96c42e`；它不是 frozen bundle 本身，也不是採用 gate。

- Source-to-legacy-Qlib mapping gap：family 名称、strategy flags/case IDs 或舊 PASS 不證明原文 source-native signal、模型 weights、universe、因果時序與執行機制一致。除本紀錄明列已釘選的程式規則外，沒有補造代碼對照。paper方法、研究解讀與historical DCA分層保留；尚未證明多個 legacy codes 對應不同完整 core mechanisms，故不任意拆成新策略。

## Economic mechanism

### Source-reported

RG-ResMoE 將 regime variables 僅送進 residual-expert routing，而不直接拼接到 forecasting inputs，研究 nonstationary regime information 如何影響 volatility forecast 與 VaR calibration。

### Research interpretation

這是方法／假說的普通研究封存，不是把歷史 survivor 標籤當成新 alpha。機制層分類與單筆 cohort 的 DCA 收益不同；statistical forecast、risk allocator 或負面 study 均不得被默換成已驗證的 crypto 交易規則。

## Signal

Stock-level historical features → frozen/base predictor；regime state → soft gating weights → residual corrections → five-day volatility forecast。Volatility forecast 不是天然 long/short return forecast。baseline model_code=0 尚未與原文 matched MLP / RG-ResMoE branches 逐式核對；此處不創造 forecast-to-trade threshold。

## Required data

原文美股 1,027 stocks 的 daily panel、rolling walk-forward folds、regime/market and idiosyncratic-vol inputs、matched capacity/seeds 與另有日本 panel 對照。

Historical cohort resolution、parameters 與 data cutoff 以 Evidence 的原 JSON 為準，不補齊不存在的字段，不降採樣、不改 symbol。baseline 不含完整行情 manifest、signal arrays、model checkpoints 或逐筆 trade ledger；它不是可直接執行的策略定義。

## Execution assumptions

來源方法重點是 forecast accuracy/stability/VaR，而不是明定 entries、exits 或 DCA。從 forecast 轉成交易 allocation 必須另立可反證假說。

Historical DCA 參數只代表當時研究配置，並非 paper 原生規則，也不是目前 house overlay。未重新量測 fees、funding、margin/liquidation、slippage、intrabar path 或 fills；hash references 不是原資料 bytes 已重新驗證的宣告。

## Evidence

### Source-reported

本輪讀取 versioned primary landing 的 abstract，確認上述 method-level 主張；更細的 signal 配置以釘選原研究紀錄為轉錄來源，未宣稱已重新逐式審閱整篇 methods 或 source code。原文績效不是下列 crypto baseline metrics。

### Independently reproduced

Not independently reproduced. 本輪只驗 source identity／文件轉錄，沒有 Qlib rerun、Hummingbot reproduction、Paper 或 Testnet。

### Negative evidence

原文摘要報告 hard routing 劣於 soft routing；直接 concatenation 會使 forecast/stability 劣化。舊 crypto survivor 值不能證明較好的 volatility model 就有方向 alpha。

### HISTORICAL QLIB SURVIVOR EVIDENCE — 非目前 Hummingbot reproduction

以下每個 baseline JSON 保留全部原鍵／數值／null／巢狀結構，唯一刪除 top-level `bundle_path` 的機器絕對路徑。bundle 邏輯定位仍可由 family_id / round_id / run_id 與 survivor ID 找到；不假裝本輪讀取已退役結果盤。每筆獨立列 raw baseline-file SHA-256，它與 `params_sha256`、`bundle_sha256`（檔案 bytes）、`bundle_identity_sha256`（歷史 identity recipe）互不相同。

鍵名 `net_pnl` / `sharpe` / `max_dd_pct` / `annualized_return` 原樣保留，不重命名成 ROI、不對 MDD 改 sign／比例／百分點、不跨 lineage 默認同一 annualization。baseline 欄位缺席不同於 null；不從另一層悄悄補值。`source_verdict: PASS` 與 `neighbourhood.passed` 都是 HISTORICAL，不能解讀成今日 efficacy、source parity 或 HB_READY PASS。

每筆另列 `leaderboard_snapshot`：`additional_fields` 為 derived index 額外欄位，`baseline_field_overrides` 為該 index 與 baseline 不同的完整 top-level 值；空 object 明示無差異。兩者都不回寫 baseline。僅非 null 的 `evidence_manifest_path` 去除原 results-root 絕對前綴，保留 `_survivors/...` 相對 locator；null 留 null。rank / top10 / package PRESENT / FROZEN_ONLY 只是當時 derived state，不能解讀為今天 evidence package bytes 存在或新 forward evidence。

#### sv-17cd98de303a5df8 — HISTORICAL

Baseline file SHA-256：`7e94eb805919f8bafa226e3a60ffdaf6d8579b928a6f2fe7ba37cd1f4488b45a`；archive locator：`survivors/sv-17cd98de303a5df8/baseline.json`。

```json
{"survivor_id":"sv-17cd98de303a5df8","family_id":"cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02","round_id":"cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02-r3","run_id":"cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02-r3-u4","kanban_task_id":"t_0fba9abc","cohort":"ETHUSDT/5m","symbol":"ETHUSDT","timeframe":"5m","challenger_of":null,"strategy_params":{"model_code":0},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.1,"breakeven_tp_pct":0.02,"invalidation_pct":0.05},"params_sha256":"sha256:5021d81e56f44aaa3a0b59d173d3da955434b3fcea30a9f00f6f4fffe1db1a84","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:0cdac0c9ca80911f3b4a041bb9bc5200d2f9f45935b3bb8aa1c4d6e52aecfd32","bundle_identity_sha256":"sha256:2640db851d33f0f1c5841a77b24c0c56aa6c5ddd76d41d17de34176c934c5ea5","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":107826.36302109176,"sharpe":0.8593174369417075,"episodes":1101,"max_dd_pct":53.87189533531947},"oos":{"net_pnl":10275.229975098135,"sharpe":0.2984241970591236,"episodes":287,"max_dd_pct":67.70323515765264},"full":{"net_pnl":114909.93879585894,"sharpe":0.7188858462720151,"episodes":1388,"max_dd_pct":53.87189533531947,"annualized_return":null,"avg_trades_per_year":295.6075801749271},"robustness":{"fee_2x":{"net_pnl":57065.045323755134,"sharpe":0.35404943493451646,"max_dd_pct":58.485092759562626},"funding_2x":{"net_pnl":117766.16772279146,"sharpe":0.7366703814761238,"max_dd_pct":53.895787031848066},"entry_delay_1_bar":{"net_pnl":21267.515873871842,"sharpe":0.12813836950293134,"max_dd_pct":95.13633345944578},"slippage_2ticks":{"net_pnl":113152.11117444417,"sharpe":0.7059239897978422,"max_dd_pct":53.88824072755022}},"robustness_stress_floor_net_pnl":21267.515873871842,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":0.8,"passed":true,"neighbours":5,"agreeing":4}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-17cd98de303a5df8","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":84,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-745d59cc05667723 — HISTORICAL

Baseline file SHA-256：`e1d897c483db284b47c29f80fe23fc2d72811fca7404c3572c413ad5fec9291b`；archive locator：`survivors/sv-745d59cc05667723/baseline.json`。

```json
{"survivor_id":"sv-745d59cc05667723","family_id":"cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02","round_id":"cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02-r3","run_id":"cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02-r3-u4","kanban_task_id":"t_0fba9abc","cohort":"ETHUSDT/4h","symbol":"ETHUSDT","timeframe":"4h","challenger_of":null,"strategy_params":{"model_code":0},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.0,"breakeven_tp_pct":0.03,"invalidation_pct":0.05},"params_sha256":"sha256:a5f212090575dda175cb93880f41e77038c6230986944edfc80782a93b00ba96","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:0cdac0c9ca80911f3b4a041bb9bc5200d2f9f45935b3bb8aa1c4d6e52aecfd32","bundle_identity_sha256":"sha256:2640db851d33f0f1c5841a77b24c0c56aa6c5ddd76d41d17de34176c934c5ea5","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":42069.630859759774,"sharpe":0.8637882733691942,"episodes":316,"max_dd_pct":54.93711700088689},"oos":{"net_pnl":18863.94737694768,"sharpe":1.5906072303576426,"episodes":92,"max_dd_pct":17.726623326262647},"full":{"net_pnl":61255.75145521252,"sharpe":1.0060973466791239,"episodes":408,"max_dd_pct":54.93711700088689,"annualized_return":null,"avg_trades_per_year":86.89329446064139},"robustness":{"fee_2x":{"net_pnl":47922.9106638553,"sharpe":0.7853043739815687,"max_dd_pct":56.971447373477076},"funding_2x":{"net_pnl":60964.84605588181,"sharpe":1.0023880655441406,"max_dd_pct":55.16606242416265},"entry_delay_1_bar":{"net_pnl":33050.79047868761,"sharpe":0.5488379381594065,"max_dd_pct":34.38713318696998},"slippage_2ticks":{"net_pnl":61177.59887269329,"sharpe":1.0047973616653292,"max_dd_pct":54.94428708408067}},"robustness_stress_floor_net_pnl":33050.79047868761,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":0.75,"passed":true,"neighbours":4,"agreeing":3}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-745d59cc05667723","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":55,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-91457e9b54b07faf — HISTORICAL

Baseline file SHA-256：`7bf55681c2222f4e186d34ea06efcf0e4af8a2aa8332a47a5e7f030fed961542`；archive locator：`survivors/sv-91457e9b54b07faf/baseline.json`。

```json
{"survivor_id":"sv-91457e9b54b07faf","family_id":"cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02","round_id":"cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02-r3","run_id":"cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02-r3-u4","kanban_task_id":"t_0fba9abc","cohort":"ETHUSDT/30m","symbol":"ETHUSDT","timeframe":"30m","challenger_of":null,"strategy_params":{"model_code":0},"dca_params":{"spacing_pct":0.03,"size_multiplier":1.1,"breakeven_tp_pct":0.03,"invalidation_pct":0.05},"params_sha256":"sha256:4d46f6b5ebc36b505977497715d404535d088dde93dcf179c18e7bcb9c5d81ae","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:0cdac0c9ca80911f3b4a041bb9bc5200d2f9f45935b3bb8aa1c4d6e52aecfd32","bundle_identity_sha256":"sha256:2640db851d33f0f1c5841a77b24c0c56aa6c5ddd76d41d17de34176c934c5ea5","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":21691.470943157914,"sharpe":0.7470416011482166,"episodes":454,"max_dd_pct":28.14689474315637},"oos":{"net_pnl":1148.5188523775785,"sharpe":0.16557330916085858,"episodes":124,"max_dd_pct":18.492782589569522},"full":{"net_pnl":22839.98979553551,"sharpe":0.6348847249339196,"episodes":578,"max_dd_pct":28.14689474315637,"annualized_return":null,"avg_trades_per_year":123.09883381924197},"robustness":{"fee_2x":{"net_pnl":13270.710261369844,"sharpe":0.36796893214643284,"max_dd_pct":30.53929221071646},"funding_2x":{"net_pnl":23080.737823611405,"sharpe":0.6414027698691088,"max_dd_pct":28.347663446901855},"entry_delay_1_bar":{"net_pnl":12073.838718424364,"sharpe":0.32627193827722456,"max_dd_pct":39.40997909251428},"slippage_2ticks":{"net_pnl":22789.370113847577,"sharpe":0.6334664903122759,"max_dd_pct":28.155393891211833}},"robustness_stress_floor_net_pnl":12073.838718424364,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":5,"agreeing":5}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-91457e9b54b07faf","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":90,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-c173301310892776 — HISTORICAL

Baseline file SHA-256：`80edb391da534837d11ae9a9cd5f08e0ed2181f0a92b888f21f647cd3c1e49a0`；archive locator：`survivors/sv-c173301310892776/baseline.json`。

```json
{"survivor_id":"sv-c173301310892776","family_id":"cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02","round_id":"cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02-r3","run_id":"cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02-r3-u4","kanban_task_id":"t_0fba9abc","cohort":"SOLUSDT/4h","symbol":"SOLUSDT","timeframe":"4h","challenger_of":null,"strategy_params":{"model_code":0},"dca_params":{"spacing_pct":0.03,"size_multiplier":1.1,"breakeven_tp_pct":0.01,"invalidation_pct":0.1},"params_sha256":"sha256:c3ab85859950bd4a54fe5dd7d5eb4b4051be0bf4cc9f5d3d8c5ce7e8faebdb5a","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:0cdac0c9ca80911f3b4a041bb9bc5200d2f9f45935b3bb8aa1c4d6e52aecfd32","bundle_identity_sha256":"sha256:2640db851d33f0f1c5841a77b24c0c56aa6c5ddd76d41d17de34176c934c5ea5","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":5394.324606629748,"sharpe":0.3457427595323271,"episodes":160,"max_dd_pct":17.544922720461933},"oos":{"net_pnl":2925.579780074182,"sharpe":0.6654165706895689,"episodes":99,"max_dd_pct":16.408196092979566},"full":{"net_pnl":8319.904386703935,"sharpe":0.4157233284653222,"episodes":259,"max_dd_pct":17.544922720461933,"annualized_return":null,"avg_trades_per_year":55.16020408163265},"robustness":{"fee_2x":{"net_pnl":4722.380238170046,"sharpe":0.23516778360640334,"max_dd_pct":20.10783374204368},"funding_2x":{"net_pnl":8408.180885985432,"sharpe":0.41979561044083286,"max_dd_pct":17.5831126393859},"entry_delay_1_bar":{"net_pnl":6934.998440615858,"sharpe":0.43118248315596613,"max_dd_pct":17.47162251288564},"slippage_2ticks":{"net_pnl":8268.555944181051,"sharpe":0.4130875520168592,"max_dd_pct":17.560910202445214}},"robustness_stress_floor_net_pnl":4722.380238170046,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":0.8,"passed":true,"neighbours":5,"agreeing":4}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-c173301310892776","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":73,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-d20242c49017f353 — HISTORICAL

Baseline file SHA-256：`a50c18821b8fe98d49f31d1b63424d52477b2648de0af613465f4fc363486f0e`；archive locator：`survivors/sv-d20242c49017f353/baseline.json`。

```json
{"survivor_id":"sv-d20242c49017f353","family_id":"cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02","round_id":"cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02-r3","run_id":"cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02-r3-u4","kanban_task_id":"t_0fba9abc","cohort":"BTCUSDT/1d","symbol":"BTCUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"model_code":0},"dca_params":{"spacing_pct":0.03,"size_multiplier":1.1,"breakeven_tp_pct":0.03,"invalidation_pct":0.05},"params_sha256":"sha256:4d46f6b5ebc36b505977497715d404535d088dde93dcf179c18e7bcb9c5d81ae","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:0cdac0c9ca80911f3b4a041bb9bc5200d2f9f45935b3bb8aa1c4d6e52aecfd32","bundle_identity_sha256":"sha256:2640db851d33f0f1c5841a77b24c0c56aa6c5ddd76d41d17de34176c934c5ea5","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":14037.681851946381,"sharpe":1.0794900404379908,"episodes":184,"max_dd_pct":7.545815313548573},"oos":{"net_pnl":1297.944224584665,"sharpe":0.4017861835502513,"episodes":49,"max_dd_pct":8.688403107196395},"full":{"net_pnl":15335.626076531049,"sharpe":0.9447852197940744,"episodes":233,"max_dd_pct":7.545815313548573,"annualized_return":null,"avg_trades_per_year":49.62288629737609},"robustness":{"fee_2x":{"net_pnl":12034.331030536629,"sharpe":0.7430850600278356,"max_dd_pct":8.254046492166227},"funding_2x":{"net_pnl":16276.691286067737,"sharpe":1.0015902393605784,"max_dd_pct":7.308350386353213},"entry_delay_1_bar":{"net_pnl":9274.31051804889,"sharpe":0.6318737537361676,"max_dd_pct":14.680583568307526},"slippage_2ticks":{"net_pnl":15325.531916566653,"sharpe":0.9441631864729861,"max_dd_pct":7.5476308132098255}},"robustness_stress_floor_net_pnl":9274.31051804889,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":5,"agreeing":5}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-d20242c49017f353","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":79,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
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

`hb_ready_status: NOT_LOSSLESS`。cross-sectional/regime state、trained forecasting weights 與未定義的 forecast-to-order mapping 不符合 lossless single-pair event semantics。

Research-only、not-approved；不能進目前 Hummingbot/Qlib 績效下游，不是 Paper/Testnet/Live approval。普通 non-Scout reconstruction 紀錄可經獨立 provenance/research review 保留，並非 Scout one-file PASS admission。

## Related Wiki records

`quant/cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02.md` — 本紀錄上列 hash 的原研究 provenance，未修改 Wiki。

## Sources

1. Primary：https://arxiv.org/abs/2608.12251v1
2. Pinned historical source：https://github.com/HCH725/alpha-strategy-research/blob/c405adc4795154334d9d50950795b4711f00445d/cross-sectional-volatility-regime-gated-residual-mixture-of-experts-2026-09-02.md
3. Historical baseline/leaderboard archive：https://github.com/HCH725/validated-survivor-research/tree/15c0a95162b60a664b43ac60157225c7300ad789；commit 及 per-baseline raw digests 以上述 Provenance/Evidence 為準，並未聲稱所有 reference 可供匿名讀者直接下載。
