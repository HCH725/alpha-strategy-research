---
schema: strategy-research-record-v1
hb_ready_status: NOT_LOSSLESS
title: 'FinPILOT: Inference-Time MPC Plugin for RL Portfolio Management with XGBoost Price Forecasting'
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
- https://arxiv.org/abs/2605.12653v1
- https://github.com/HCH725/alpha-strategy-research/blob/41bbd39e0f9ea364663d2882d1a5313cf5492bfd/inference-time-mpc-rl-portfolio-xgboost-forecast-2026-09-05.md
- HCH725/validated-survivor-research commit 15c0a95162b60a664b43ac60157225c7300ad789
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# FinPILOT: Inference-Time MPC Plugin for RL Portfolio Management with XGBoost Price Forecasting

## Provenance

- Family identity：`inference-time-mpc-rl-portfolio-xgboost-forecast-2026-09-05`；本次 consolidation 只按原 baseline family_id，不依 Sharpe 重新排名／挑選。
- Primary source：https://arxiv.org/abs/2605.12653v1。
- 既有 source-backed 研究紀錄：commit `41bbd39e0f9ea364663d2882d1a5313cf5492bfd`，`inference-time-mpc-rl-portfolio-xgboost-forecast-2026-09-05.md`，Git blob `ab2670173ee69102842bcb2cb20d31383ad9f765`。 本紀錄未捏造不存在的逐檔 reviewed_commit；採可回收的最初 root-record commit。
- `quant/inference-time-mpc-rl-portfolio-xgboost-forecast-2026-09-05.md` 的 raw SHA-256 為 `310d75f7fffd15e75d4776cac59b72af2f89b3a50e002d12620bde18534f22ab`；它在 review-state 的 `ingested_wiki_records` 中，state 最後審查 commit 為 `2799e34c5c7f8d6f7036e35d9ae7468832712c97`。這是 ingestion provenance，不是本輪 source parity 或逐檔新審查；Wiki bytes 不冒稱與原 Git blob 相同。
- Historical input：`HCH725/validated-survivor-research` commit `15c0a95162b60a664b43ac60157225c7300ad789` 的 `survivors/<survivor_id>/baseline.json`，本家族 1 筆，cohorts：`ETHUSDT/1d`。
- Derived leaderboard：同一 repo `leaderboard/leaderboard.json`，raw SHA-256 `e8fdd38c8468960eee5b574e93d27615635bcb266fe481ab8c1409720d96c42e`；它不是 frozen bundle 本身，也不是採用 gate。

- Source-to-legacy-Qlib mapping gap：family 名称、strategy flags/case IDs 或舊 PASS 不證明原文 source-native signal、模型 weights、universe、因果時序與執行機制一致。除本紀錄明列已釘選的程式規則外，沒有補造代碼對照。paper方法、研究解讀與historical DCA分層保留；尚未證明多個 legacy codes 對應不同完整 core mechanisms，故不任意拆成新策略。

## Economic mechanism

### Source-reported

FPILOT（舊研究紀錄稱 FinPILOT）在 inference time 使用 price forecasts 形成 imagined return objective、調整已訓練 RL policy，並只執行當次首個 allocation；是 MPC-like portfolio controller，不是獨立單幣 indicator。

### Research interpretation

這是方法／假說的普通研究封存，不是把歷史 survivor 標籤當成新 alpha。機制層分類與單筆 cohort 的 DCA 收益不同；statistical forecast、risk allocator 或負面 study 均不得被默換成已驗證的 crypto 交易規則。

## Signal

歷史研究紀錄列 XGBoost forecast、H=50、risk penalty、K noisy trajectories、gradient steps 與 daily receding horizon。H/λ/η/E/γ 是原研究轉錄的配置候選，不能由 baseline strategy_case=29 反推確切 chosen model/hyperparameters 或完整 RL weights。

## Required data

來源 TradeMaster DJ30 portfolio benchmark；歷史研究紀錄亦提 daily FX panel。需要 pretrained actor、forecaster、features、weights 與 frozen training/test boundaries。

Historical cohort resolution、parameters 與 data cutoff 以 Evidence 的原 JSON 為準，不補齊不存在的字段，不降採樣、不改 symbol。baseline 不含完整行情 manifest、signal arrays、model checkpoints 或逐筆 trade ledger；它不是可直接執行的策略定義。

## Execution assumptions

Forecast trajectory 中的 imagined allocations 不等於真實 fills；執行首個 action 再計畫，跨資產 rebalance、portfolio costs 及 held state 有實質語意。

Historical DCA 參數只代表當時研究配置，並非 paper 原生規則，也不是目前 house overlay。未重新量測 fees、funding、margin/liquidation、slippage、intrabar path 或 fills；hash references 不是原資料 bytes 已重新驗證的宣告。

## Evidence

### Source-reported

本輪讀取 versioned primary landing 的 abstract，確認上述 method-level 主張；更細的 signal 配置以釘選原研究紀錄為轉錄來源，未宣稱已重新逐式審閱整篇 methods 或 source code。原文績效不是下列 crypto baseline metrics。

### Independently reproduced

Not independently reproduced. 本輪只驗 source identity／文件轉錄，沒有 Qlib rerun、Hummingbot reproduction、Paper 或 Testnet。

### Negative evidence

摘要表示 gains 隨 forecaster quality 改變；no retraining 不代表沒有 inference optimization。舊紀錄警示 perfect fills、single-year evaluation 與部分最佳 policy 的 drawdown 反而增加，均非本輪 replication。

### HISTORICAL QLIB SURVIVOR EVIDENCE — 非目前 Hummingbot reproduction

以下每個 baseline JSON 保留全部原鍵／數值／null／巢狀結構，唯一刪除 top-level `bundle_path` 的機器絕對路徑。bundle 邏輯定位仍可由 family_id / round_id / run_id 與 survivor ID 找到；不假裝本輪讀取已退役結果盤。每筆獨立列 raw baseline-file SHA-256，它與 `params_sha256`、`bundle_sha256`（檔案 bytes）、`bundle_identity_sha256`（歷史 identity recipe）互不相同。

鍵名 `net_pnl` / `sharpe` / `max_dd_pct` / `annualized_return` 原樣保留，不重命名成 ROI、不對 MDD 改 sign／比例／百分點、不跨 lineage 默認同一 annualization。baseline 欄位缺席不同於 null；不從另一層悄悄補值。`source_verdict: PASS` 與 `neighbourhood.passed` 都是 HISTORICAL，不能解讀成今日 efficacy、source parity 或 HB_READY PASS。

每筆另列 `leaderboard_snapshot`：`additional_fields` 為 derived index 額外欄位，`baseline_field_overrides` 為該 index 與 baseline 不同的完整 top-level 值；空 object 明示無差異。兩者都不回寫 baseline。僅非 null 的 `evidence_manifest_path` 去除原 results-root 絕對前綴，保留 `_survivors/...` 相對 locator；null 留 null。rank / top10 / package PRESENT / FROZEN_ONLY 只是當時 derived state，不能解讀為今天 evidence package bytes 存在或新 forward evidence。

#### sv-fe1e49c613b16bb2 — HISTORICAL

Baseline file SHA-256：`b40748b9dea3e8784670126b180466eca7a50725171a3bf927e6a1d7056156b2`；archive locator：`survivors/sv-fe1e49c613b16bb2/baseline.json`。

```json
{"survivor_id":"sv-fe1e49c613b16bb2","family_id":"inference-time-mpc-rl-portfolio-xgboost-forecast-2026-09-05","round_id":"inference-time-mpc-rl-portfolio-xgboost-forecast-2026-09-05-r1","run_id":"inference-time-mpc-rl-portfolio-xgboost-forecast-2026-09-05-r1-u3","kanban_task_id":null,"cohort":"ETHUSDT/1d","symbol":"ETHUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"strategy_case":29},"dca_params":{"spacing_pct":0.04,"size_multiplier":1.0,"breakeven_tp_pct":0.01,"invalidation_pct":0.1},"params_sha256":"sha256:f811a8f87b7414a68f9eb7fe4ebd40f653e2605b764791c3214ead0e1cc802ad","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:d1a25074825ba4a7ed45c301afbc65d01c0e05e0bd0eb1c1b6052b82113b50ef","bundle_identity_sha256":"sha256:71bfec3fac2d1c58ae6e530a6df6697e3b9dd7d7fb8f116a828d9a6597e5ae05","source_disposition_band":"SURVIVOR_FOUND","source_verdict":"PASS","historical":{"net_pnl":205.10257468199526,"sharpe":8.671917535516716,"episodes":21,"max_dd_pct":0.0},"oos":{"net_pnl":88.63380495524147,"sharpe":3.8960487636939893,"episodes":10,"max_dd_pct":0.03296310803913238},"full":{"net_pnl":1139.0231712370196,"sharpe":0.8323996931372992,"episodes":189,"max_dd_pct":1.9356754028690561,"annualized_return":0.007967918923670547,"avg_trades_per_year":40.25204081632653},"robustness":{"fee_2x":{"net_pnl":887.0008255716538,"sharpe":0.6447022403401145,"max_dd_pct":1.9650940626459472},"funding_2x":{"net_pnl":1160.7914618660066,"sharpe":0.8478931145801375,"max_dd_pct":1.9344489674418215},"entry_delay_1_bar":{"net_pnl":817.1549952452684,"sharpe":0.603419985566487,"max_dd_pct":1.9607522821481527},"slippage_2ticks":{"net_pnl":1137.8133371856543,"sharpe":0.8314995833909008,"max_dd_pct":1.9357773556139286}},"robustness_stress_floor_net_pnl":817.1549952452684,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":0.8333333333333334,"passed":true,"neighbours":6,"agreeing":5}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-fe1e49c613b16bb2","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":27,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
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

`hb_ready_status: NOT_LOSSLESS`。trained model/controller identity、shared portfolio allocation 與未恢復的 case-to-policy mapping 不能無損成為單 pair OHLCV rule。

Research-only、not-approved；不能進目前 Hummingbot/Qlib 績效下游，不是 Paper/Testnet/Live approval。普通 non-Scout reconstruction 紀錄可經獨立 provenance/research review 保留，並非 Scout one-file PASS admission。

## Related Wiki records

`quant/inference-time-mpc-rl-portfolio-xgboost-forecast-2026-09-05.md` — 本紀錄上列 hash 的原研究 provenance，未修改 Wiki。

## Sources

1. Primary：https://arxiv.org/abs/2605.12653v1
2. Pinned historical source：https://github.com/HCH725/alpha-strategy-research/blob/41bbd39e0f9ea364663d2882d1a5313cf5492bfd/inference-time-mpc-rl-portfolio-xgboost-forecast-2026-09-05.md
3. Historical baseline/leaderboard archive：https://github.com/HCH725/validated-survivor-research/tree/15c0a95162b60a664b43ac60157225c7300ad789；commit 及 per-baseline raw digests 以上述 Provenance/Evidence 為準，並未聲稱所有 reference 可供匿名讀者直接下載。
