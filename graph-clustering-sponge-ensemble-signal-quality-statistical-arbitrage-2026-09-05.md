---
schema: strategy-research-record-v1
hb_ready_status: NOT_LOSSLESS
title: 'Statistical Arbitrage via SPONGE Signed Graph Clustering and Machine Learning Ensemble Signal Quality Filtering: Dynamic Kelly Sizing
  and Time-Decaying Risk Barriers in US Equities'
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
- https://arxiv.org/abs/2406.10695v1
- https://github.com/HCH725/alpha-strategy-research/blob/b53f1eb9c15990756b3eb9eca8e51b90f55ef5e2/graph-clustering-sponge-ensemble-signal-quality-statistical-arbitrage-2026-09-05.md
- HCH725/validated-survivor-research commit 15c0a95162b60a664b43ac60157225c7300ad789
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Statistical Arbitrage via SPONGE Signed Graph Clustering and Machine Learning Ensemble Signal Quality Filtering: Dynamic Kelly Sizing and Time-Decaying Risk Barriers in US Equities

## Provenance

- Family identity：`graph-clustering-sponge-ensemble-signal-quality-statistical-arbitrage-2026-09-05`；本次 consolidation 只按原 baseline family_id，不依 Sharpe 重新排名／挑選。
- Primary source：https://arxiv.org/abs/2406.10695v1。
- 既有 source-backed 研究紀錄：commit `b53f1eb9c15990756b3eb9eca8e51b90f55ef5e2`，`graph-clustering-sponge-ensemble-signal-quality-statistical-arbitrage-2026-09-05.md`，Git blob `c7eb38ca97a74d81bc3a274cbe0896703813f86a`。 本紀錄未捏造不存在的逐檔 reviewed_commit；採可回收的最初 root-record commit。
- `quant/graph-clustering-sponge-ensemble-signal-quality-statistical-arbitrage-2026-09-05.md` 的 raw SHA-256 為 `ace93d9fb1332c40c755d9ea4212bebffa088b6eecbaabc1b96bab3fd51bb734`；它在 review-state 的 `ingested_wiki_records` 中，state 最後審查 commit 為 `2799e34c5c7f8d6f7036e35d9ae7468832712c97`。這是 ingestion provenance，不是本輪 source parity 或逐檔新審查；Wiki bytes 不冒稱與原 Git blob 相同。
- Historical input：`HCH725/validated-survivor-research` commit `15c0a95162b60a664b43ac60157225c7300ad789` 的 `survivors/<survivor_id>/baseline.json`，本家族 2 筆，cohorts：`BNBUSDT/1d`, `ETHUSDT/1d`。
- Derived leaderboard：同一 repo `leaderboard/leaderboard.json`，raw SHA-256 `e8fdd38c8468960eee5b574e93d27615635bcb266fe481ab8c1409720d96c42e`；它不是 frozen bundle 本身，也不是採用 gate。

- Source-to-legacy-Qlib mapping gap：family 名称、strategy flags/case IDs 或舊 PASS 不證明原文 source-native signal、模型 weights、universe、因果時序與執行機制一致。除本紀錄明列已釘選的程式規則外，沒有補造代碼對照。paper方法、研究解讀與historical DCA分層保留；尚未證明多個 legacy codes 對應不同完整 core mechanisms，故不任意拆成新策略。

## Economic mechanism

### Source-reported

來源以 signed graph clustering 找多股票相對偏離，結合 ensemble signal-quality classifiers、Kelly risk allocation 及 adaptive TP/SL functions 改善 statistical arbitrage。

### Research interpretation

這是方法／假說的普通研究封存，不是把歷史 survivor 標籤當成新 alpha。機制層分類與單筆 cohort 的 DCA 收益不同；statistical forecast、risk allocator 或負面 study 均不得被默換成已驗證的 crypto 交易規則。

## Signal

S&P 500 cross-sectional return correlations → SPONGE signed graph clusters → relative cluster deviation / trade candidates → classifier filter → dynamic Kelly and time-varying risk barriers。原研究紀錄列 30-day formation / 10th-day cadence，但 baseline signal_rule_version=1 尚未逐式對應完整 graph/model/risk pipeline。不能改成單幣均線差而保留原文 efficacy 宣告。

## Required data

來源需要 point-in-time 多股票 universe、adjusted returns、cross-sectional graph、trained ensemble features 及 cluster membership；crypto per-cohort baseline 只是一筆歷史證據。

Historical cohort resolution、parameters 與 data cutoff 以 Evidence 的原 JSON 為準，不補齊不存在的字段，不降採樣、不改 symbol。baseline 不含完整行情 manifest、signal arrays、model checkpoints 或逐筆 trade ledger；它不是可直接執行的策略定義。

## Execution assumptions

多 pair positions、共享 capital、Kelly sizing 與 time-decaying barriers 都是來源事件語意，不能將它們當 source-neutral DCA overlay。

Historical DCA 參數只代表當時研究配置，並非 paper 原生規則，也不是目前 house overlay。未重新量測 fees、funding、margin/liquidation、slippage、intrabar path 或 fills；hash references 不是原資料 bytes 已重新驗證的宣告。

## Evidence

### Source-reported

本輪讀取 versioned primary landing 的 abstract，確認上述 method-level 主張；更細的 signal 配置以釘選原研究紀錄為轉錄來源，未宣稱已重新逐式審閱整篇 methods 或 source code。原文績效不是下列 crypto baseline metrics。

### Independently reproduced

Not independently reproduced. 本輪只驗 source identity／文件轉錄，沒有 Qlib rerun、Hummingbot reproduction、Paper 或 Testnet。

### Negative evidence

原文摘要指出對重要 parameters 敏感。舊研究紀錄另警示 distressed-stock concentration 與 borrow/impact gaps；這些詳細量化未在本輪重新核對，故不加入新的 paper performance 數字。

### HISTORICAL QLIB SURVIVOR EVIDENCE — 非目前 Hummingbot reproduction

以下每個 baseline JSON 保留全部原鍵／數值／null／巢狀結構，唯一刪除 top-level `bundle_path` 的機器絕對路徑。bundle 邏輯定位仍可由 family_id / round_id / run_id 與 survivor ID 找到；不假裝本輪讀取已退役結果盤。每筆獨立列 raw baseline-file SHA-256，它與 `params_sha256`、`bundle_sha256`（檔案 bytes）、`bundle_identity_sha256`（歷史 identity recipe）互不相同。

鍵名 `net_pnl` / `sharpe` / `max_dd_pct` / `annualized_return` 原樣保留，不重命名成 ROI、不對 MDD 改 sign／比例／百分點、不跨 lineage 默認同一 annualization。baseline 欄位缺席不同於 null；不從另一層悄悄補值。`source_verdict: PASS` 與 `neighbourhood.passed` 都是 HISTORICAL，不能解讀成今日 efficacy、source parity 或 HB_READY PASS。

每筆另列 `leaderboard_snapshot`：`additional_fields` 為 derived index 額外欄位，`baseline_field_overrides` 為該 index 與 baseline 不同的完整 top-level 值；空 object 明示無差異。兩者都不回寫 baseline。僅非 null 的 `evidence_manifest_path` 去除原 results-root 絕對前綴，保留 `_survivors/...` 相對 locator；null 留 null。rank / top10 / package PRESENT / FROZEN_ONLY 只是當時 derived state，不能解讀為今天 evidence package bytes 存在或新 forward evidence。

#### sv-1d8f53ca1142eaf1 — HISTORICAL

Baseline file SHA-256：`5519a22e186496a485644520b6a198d5912bc5b693224a5d02d16ca8c934ed3f`；archive locator：`survivors/sv-1d8f53ca1142eaf1/baseline.json`。

```json
{"survivor_id":"sv-1d8f53ca1142eaf1","family_id":"graph-clustering-sponge-ensemble-signal-quality-statistical-arbitrage-2026-09-05","round_id":"graph-clustering-sponge-ensemble-signal-quality-statistical-arbitrage-2026-09-05-r1","run_id":"graph-clustering-sponge-ensemble-signal-quality-statistical-arbitrage-2026-09-05-r1-u2","kanban_task_id":null,"cohort":"ETHUSDT/1d","symbol":"ETHUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"signal_rule_version":1},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.1,"breakeven_tp_pct":0.01,"invalidation_pct":0.05},"params_sha256":"sha256:065b6a5b08aa17a165232194fb2be06f55e35a8c2556648ea95fb61c2654f711","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:abcda8b4470f38ccd870a3f5d9e9b5367a715cbf739e35516d4c08bda870bdc9","bundle_identity_sha256":"sha256:434c431cbb378e19ec4372ae46d3244c32b2d548b0d32787a9c16e1f788ef8a6","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":737.4131847844276,"sharpe":23.68192738474268,"episodes":43,"max_dd_pct":0.0},"oos":{"net_pnl":44.138435917400564,"sharpe":0.5465492684680175,"episodes":25,"max_dd_pct":0.9677922407924835},"full":{"net_pnl":781.5516207018281,"sharpe":5.530565675664367,"episodes":68,"max_dd_pct":0.9447798366515109,"annualized_return":0.00548855050689645,"avg_trades_per_year":14.482215743440232},"robustness":{"fee_2x":{"net_pnl":650.8719756612735,"sharpe":4.5645352736990965,"max_dd_pct":0.9794314288111127},"funding_2x":{"net_pnl":766.5897729619222,"sharpe":5.444673389657311,"max_dd_pct":0.947297663198676},"entry_delay_1_bar":{"net_pnl":435.73214804870383,"sharpe":1.0210489412999024,"max_dd_pct":3.1221141489387336},"slippage_2ticks":{"net_pnl":780.8895997620948,"sharpe":5.523677518419169,"max_dd_pct":0.9453380302404933}},"robustness_stress_floor_net_pnl":435.73214804870383,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":0.75,"passed":true,"neighbours":4,"agreeing":3}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-1d8f53ca1142eaf1","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":75,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-d0c1ef48e53d6982 — HISTORICAL

Baseline file SHA-256：`abdb8e9a3fa6302d74aeb8591219f44a835f7bde312787981920cdfc71ac8620`；archive locator：`survivors/sv-d0c1ef48e53d6982/baseline.json`。

```json
{"survivor_id":"sv-d0c1ef48e53d6982","family_id":"graph-clustering-sponge-ensemble-signal-quality-statistical-arbitrage-2026-09-05","round_id":"graph-clustering-sponge-ensemble-signal-quality-statistical-arbitrage-2026-09-05-r1","run_id":"graph-clustering-sponge-ensemble-signal-quality-statistical-arbitrage-2026-09-05-r1-u2","kanban_task_id":null,"cohort":"BNBUSDT/1d","symbol":"BNBUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"signal_rule_version":1},"dca_params":{"spacing_pct":0.03,"size_multiplier":1.1,"breakeven_tp_pct":0.02,"invalidation_pct":0.1},"params_sha256":"sha256:acb22a89790216f64755e80c616ab019cad58bdd4c088b65191cae93e492ceca","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:abcda8b4470f38ccd870a3f5d9e9b5367a715cbf739e35516d4c08bda870bdc9","bundle_identity_sha256":"sha256:434c431cbb378e19ec4372ae46d3244c32b2d548b0d32787a9c16e1f788ef8a6","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":425.2538387657986,"sharpe":19.814199546209306,"episodes":15,"max_dd_pct":0.0},"oos":{"net_pnl":167.54500565711479,"sharpe":32.55385568894279,"episodes":10,"max_dd_pct":0.0},"full":{"net_pnl":592.7988444229134,"sharpe":19.8798154469316,"episodes":25,"max_dd_pct":0.0,"annualized_return":0.004173145648615151,"avg_trades_per_year":5.324344023323615},"robustness":{"fee_2x":{"net_pnl":561.9837942810497,"sharpe":19.826146243702112,"max_dd_pct":0.0},"funding_2x":{"net_pnl":601.6318613612898,"sharpe":18.938846850221037,"max_dd_pct":0.0},"entry_delay_1_bar":{"net_pnl":162.2732735509923,"sharpe":2.756582867236545,"max_dd_pct":0.5166053907581987},"slippage_2ticks":{"net_pnl":592.1121343478296,"sharpe":19.884417874075883,"max_dd_pct":0.0}},"robustness_stress_floor_net_pnl":162.2732735509923,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":6,"agreeing":6}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-d0c1ef48e53d6982","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":6,"in_top10":true,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
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

`hb_ready_status: NOT_LOSSLESS`。signed cross-asset graphs、multi-pair positions、portfolio allocation 與 adaptive barrier execution 不符合單 pair lossless lane。

Research-only、not-approved；不能進目前 Hummingbot/Qlib 績效下游，不是 Paper/Testnet/Live approval。普通 non-Scout reconstruction 紀錄可經獨立 provenance/research review 保留，並非 Scout one-file PASS admission。

## Related Wiki records

`quant/graph-clustering-sponge-ensemble-signal-quality-statistical-arbitrage-2026-09-05.md` — 本紀錄上列 hash 的原研究 provenance，未修改 Wiki。

## Sources

1. Primary：https://arxiv.org/abs/2406.10695v1
2. Pinned historical source：https://github.com/HCH725/alpha-strategy-research/blob/b53f1eb9c15990756b3eb9eca8e51b90f55ef5e2/graph-clustering-sponge-ensemble-signal-quality-statistical-arbitrage-2026-09-05.md
3. Historical baseline/leaderboard archive：https://github.com/HCH725/validated-survivor-research/tree/15c0a95162b60a664b43ac60157225c7300ad789；commit 及 per-baseline raw digests 以上述 Provenance/Evidence 為準，並未聲稱所有 reference 可供匿名讀者直接下載。
