---
schema: strategy-research-record-v1
hb_ready_status: NOT_LOSSLESS
title: 'Structural Limits of OHLCV-Based Intraday Signals in MNQ Futures: Gross Edge Ceiling and Friction-Aware Falsification'
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
- https://arxiv.org/abs/2605.04004v1
- https://github.com/HCH725/alpha-strategy-research/blob/f76d7f8e947fc27d07a3ee6436c1419da11bd648/mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05.md
- HCH725/validated-survivor-research commit 15c0a95162b60a664b43ac60157225c7300ad789
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Structural Limits of OHLCV-Based Intraday Signals in MNQ Futures: Gross Edge Ceiling and Friction-Aware Falsification

## Provenance

- Family identity：`mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05`；本次 consolidation 只按原 baseline family_id，不依 Sharpe 重新排名／挑選。
- Primary source：https://arxiv.org/abs/2605.04004v1。
- 既有 source-backed 研究紀錄：commit `f76d7f8e947fc27d07a3ee6436c1419da11bd648`，`mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05.md`，Git blob `b7bf0019c5a92f329241a7ee5bfcdb50feace669`。 本紀錄未捏造不存在的逐檔 reviewed_commit；採可回收的最初 root-record commit。
- `quant/mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05.md` 的 raw SHA-256 為 `72786ec649a77ca4201ddafdd29f2ef3b84fac92aaaedc90cbf8c41cb8c765ba`；它在 review-state 的 `ingested_wiki_records` 中，state 最後審查 commit 為 `2799e34c5c7f8d6f7036e35d9ae7468832712c97`。這是 ingestion provenance，不是本輪 source parity 或逐檔新審查；Wiki bytes 不冒稱與原 Git blob 相同。
- Historical input：`HCH725/validated-survivor-research` commit `15c0a95162b60a664b43ac60157225c7300ad789` 的 `survivors/<survivor_id>/baseline.json`，本家族 4 筆，cohorts：`BNBUSDT/15m`, `ETHUSDT/15m`, `ETHUSDT/5m`, `SOLUSDT/15m`。
- Derived leaderboard：同一 repo `leaderboard/leaderboard.json`，raw SHA-256 `e8fdd38c8468960eee5b574e93d27615635bcb266fe481ab8c1409720d96c42e`；它不是 frozen bundle 本身，也不是採用 gate。

- Source-to-legacy-Qlib mapping gap：family 名称、strategy flags/case IDs 或舊 PASS 不證明原文 source-native signal、模型 weights、universe、因果時序與執行機制一致。除本紀錄明列已釘選的程式規則外，沒有補造代碼對照。paper方法、研究解讀與historical DCA分層保留；尚未證明多個 legacy codes 對應不同完整 core mechanisms，故不任意拆成新策略。

## Economic mechanism

### Source-reported

來源系統反證 MNQ retail OHLCV intraday signal lore：next-open 可取得的 gross edge 常小於 round-trip friction。兩個另來自 separate research program 的 positive controls 不可混稱為十四個被否證的訊號。

### Research interpretation

這是方法／假說的普通研究封存，不是把歷史 survivor 標籤當成新 alpha。機制層分類與單筆 cohort 的 DCA 收益不同；statistical forecast、risk allocator 或負面 study 均不得被默換成已驗證的 crypto 交易規則。

## Signal

研究涵蓋 ORB、gap、volume、session、liquidity-grab、regime/news 等十四家族；另有 RTH confluence 與 London transition controls。baseline strategy_case=6/9 等編號尚未證實對應哪一 signal/control；本紀錄保留 study-family umbrella，並不聲稱所有 legacy cases 核心機制相同。未證明有可精確分離的 survivor-source mapping，故不任意拆檔。

## Required data

來源 MNQ continuous front-month 5-minute data、session calendars，部分 controls 有 MGC 或 macro-event data。crypto 5m/15m cohort 不是原文 MNQ contract identity。

Historical cohort resolution、parameters 與 data cutoff 以 Evidence 的原 JSON 為準，不補齊不存在的字段，不降採樣、不改 symbol。baseline 不含完整行情 manifest、signal arrays、model checkpoints 或逐筆 trade ledger；它不是可直接執行的策略定義。

## Execution assumptions

來源 next-bar-open 與 fixed two-point round-trip cost；正對照還可能有 pullback limit / session-close rules，不可用 same-bar-close 替代。

Historical DCA 參數只代表當時研究配置，並非 paper 原生規則，也不是目前 house overlay。未重新量測 fees、funding、margin/liquidation、slippage、intrabar path 或 fills；hash references 不是原資料 bytes 已重新驗證的宣告。

## Evidence

### Source-reported

本輪讀取 versioned primary landing 的 abstract，確認上述 method-level 主張；更細的 signal 配置以釘選原研究紀錄為轉錄來源，未宣稱已重新逐式審閱整篇 methods 或 source code。原文績效不是下列 crypto baseline metrics。

### Independently reproduced

Not independently reproduced. 本輪只驗 source identity／文件轉錄，沒有 Qlib rerun、Hummingbot reproduction、Paper 或 Testnet。

### Negative evidence

原文摘要的十四訊號 none satisfies all institutional criteria；positive controls 是方法檢測力對照而非原文普遍可交易性。舊 Wiki 寫 source_as_of=2026-05-15，而 pinned v1 landing submission 為 2026-05-05；此處保留 version pin，不繼承舊日期。

### HISTORICAL QLIB SURVIVOR EVIDENCE — 非目前 Hummingbot reproduction

以下每個 baseline JSON 保留全部原鍵／數值／null／巢狀結構，唯一刪除 top-level `bundle_path` 的機器絕對路徑。bundle 邏輯定位仍可由 family_id / round_id / run_id 與 survivor ID 找到；不假裝本輪讀取已退役結果盤。每筆獨立列 raw baseline-file SHA-256，它與 `params_sha256`、`bundle_sha256`（檔案 bytes）、`bundle_identity_sha256`（歷史 identity recipe）互不相同。

鍵名 `net_pnl` / `sharpe` / `max_dd_pct` / `annualized_return` 原樣保留，不重命名成 ROI、不對 MDD 改 sign／比例／百分點、不跨 lineage 默認同一 annualization。baseline 欄位缺席不同於 null；不從另一層悄悄補值。`source_verdict: PASS` 與 `neighbourhood.passed` 都是 HISTORICAL，不能解讀成今日 efficacy、source parity 或 HB_READY PASS。

每筆另列 `leaderboard_snapshot`：`additional_fields` 為 derived index 額外欄位，`baseline_field_overrides` 為該 index 與 baseline 不同的完整 top-level 值；空 object 明示無差異。兩者都不回寫 baseline。僅非 null 的 `evidence_manifest_path` 去除原 results-root 絕對前綴，保留 `_survivors/...` 相對 locator；null 留 null。rank / top10 / package PRESENT / FROZEN_ONLY 只是當時 derived state，不能解讀為今天 evidence package bytes 存在或新 forward evidence。

#### sv-79cf8b0b5da3835c — HISTORICAL

Baseline file SHA-256：`445a01e02f896d91c9026dad2ee157f69bf9814e44c39238ca775b3f780e609b`；archive locator：`survivors/sv-79cf8b0b5da3835c/baseline.json`。

```json
{"survivor_id":"sv-79cf8b0b5da3835c","family_id":"mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05","round_id":"mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05-r1","run_id":"mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05-r1-u2","kanban_task_id":null,"cohort":"ETHUSDT/15m","symbol":"ETHUSDT","timeframe":"15m","challenger_of":null,"strategy_params":{"strategy_case":9},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.1,"breakeven_tp_pct":0.01,"invalidation_pct":0.05},"params_sha256":"sha256:c3cfb0562233435babcacbeacaef93aa57bb801327228c5b2ff61a38e088fec1","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:9cc17bf56e42ca5e01db62bb3d0037632db20f3c5da302de77262f93b840e7c1","bundle_identity_sha256":"sha256:c00ee9d22bee800d85e6b8e7923da16633dcf6cb04808a94f9c86a9fe065fb63","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":2986.896665770994,"sharpe":3.1475094973616575,"episodes":1164,"max_dd_pct":0.5680274032244472},"oos":{"net_pnl":293.6419582445854,"sharpe":1.371001227261897,"episodes":303,"max_dd_pct":0.6405249761550413},"full":{"net_pnl":3280.5386240155794,"sharpe":2.81352332916423,"episodes":1467,"max_dd_pct":0.749297360794873,"annualized_return":0.022332021836912963,"avg_trades_per_year":312.4325072886297},"robustness":{"fee_2x":{"net_pnl":1157.2199663537588,"sharpe":0.9917547629016087,"max_dd_pct":1.9177714029033592},"funding_2x":{"net_pnl":3267.3177840519115,"sharpe":2.8012686912727904,"max_dd_pct":0.7563057058868625},"entry_delay_1_bar":{"net_pnl":2728.2331131249152,"sharpe":2.7130058145018765,"max_dd_pct":0.8065932286606683},"slippage_2ticks":{"net_pnl":3263.5649343992186,"sharpe":2.7981250154346897,"max_dd_pct":0.7565963160484944}},"robustness_stress_floor_net_pnl":1157.2199663537588,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":1.0,"passed":true,"neighbours":6,"agreeing":6}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-79cf8b0b5da3835c","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":57,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-c636b17d54245b90 — HISTORICAL

Baseline file SHA-256：`71f35e999bc4d71ceac16668fb463876702c34170ed8de574901e78b5b5b3d0f`；archive locator：`survivors/sv-c636b17d54245b90/baseline.json`。

```json
{"survivor_id":"sv-c636b17d54245b90","family_id":"mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05","round_id":"mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05-r1","run_id":"mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05-r1-u2","kanban_task_id":null,"cohort":"ETHUSDT/5m","symbol":"ETHUSDT","timeframe":"5m","challenger_of":null,"strategy_params":{"strategy_case":6},"dca_params":{"spacing_pct":0.04,"size_multiplier":1.1,"breakeven_tp_pct":0.01,"invalidation_pct":0.05},"params_sha256":"sha256:2849116fab453ec276ac622b5a145bad54abf4869344e18e0b8f486e09c76b64","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:9cc17bf56e42ca5e01db62bb3d0037632db20f3c5da302de77262f93b840e7c1","bundle_identity_sha256":"sha256:c00ee9d22bee800d85e6b8e7923da16633dcf6cb04808a94f9c86a9fe065fb63","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":85.2702043091915,"sharpe":11.751499917209145,"episodes":15,"max_dd_pct":0.07964594037293954},"oos":{"net_pnl":7.242963861192204,"sharpe":9.802778272858468,"episodes":3,"max_dd_pct":0.005827859022723378},"full":{"net_pnl":92.51316817038371,"sharpe":11.237430535657353,"episodes":18,"max_dd_pct":0.07962214301258827,"annualized_return":0.0006555179228882047,"avg_trades_per_year":3.8335276967930025},"robustness":{"fee_2x":{"net_pnl":73.44383038609946,"sharpe":9.018402549617061,"max_dd_pct":0.08295391834263868},"funding_2x":{"net_pnl":92.50934534530904,"sharpe":11.23675085788476,"max_dd_pct":0.07962214301258827},"entry_delay_1_bar":{"net_pnl":81.91955114900681,"sharpe":11.92219002255347,"max_dd_pct":0.07023783057225064},"slippage_2ticks":{"net_pnl":92.37062331100435,"sharpe":11.217977563271766,"max_dd_pct":0.07967618802408127}},"robustness_stress_floor_net_pnl":73.44383038609946,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":0.6666666666666666,"passed":true,"neighbours":6,"agreeing":4}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-c636b17d54245b90","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":8,"in_top10":true,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-f3e014df86c8ba9a — HISTORICAL

Baseline file SHA-256：`92f8fc9b6009e81da7db8cb1f5e283cddb3598ecbeb6c3d296b8809fa44e8093`；archive locator：`survivors/sv-f3e014df86c8ba9a/baseline.json`。

```json
{"survivor_id":"sv-f3e014df86c8ba9a","family_id":"mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05","round_id":"mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05-r1","run_id":"mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05-r1-u2","kanban_task_id":null,"cohort":"SOLUSDT/15m","symbol":"SOLUSDT","timeframe":"15m","challenger_of":null,"strategy_params":{"strategy_case":9},"dca_params":{"spacing_pct":0.02,"size_multiplier":1.1,"breakeven_tp_pct":0.01,"invalidation_pct":0.1},"params_sha256":"sha256:197b6356d936977819470604bd3cb839d6bbfefae1af230d54d951746456f962","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:9cc17bf56e42ca5e01db62bb3d0037632db20f3c5da302de77262f93b840e7c1","bundle_identity_sha256":"sha256:c00ee9d22bee800d85e6b8e7923da16633dcf6cb04808a94f9c86a9fe065fb63","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":3149.4525996821953,"sharpe":3.4104889019369073,"episodes":1294,"max_dd_pct":0.5874265458028007},"oos":{"net_pnl":133.14401943738338,"sharpe":0.878431783705429,"episodes":303,"max_dd_pct":0.7071429887202002},"full":{"net_pnl":3282.596619119579,"sharpe":3.024667225689794,"episodes":1597,"max_dd_pct":0.6405381785343135,"annualized_return":0.0223454762304085,"avg_trades_per_year":340.1190962099125},"robustness":{"fee_2x":{"net_pnl":1371.435338611023,"sharpe":1.2797847114936434,"max_dd_pct":1.14673149386055},"funding_2x":{"net_pnl":3275.9809036361403,"sharpe":3.0179473935072907,"max_dd_pct":0.6397590997536374},"entry_delay_1_bar":{"net_pnl":2770.2961796035243,"sharpe":3.0631601866876914,"max_dd_pct":0.5177466915375281},"slippage_2ticks":{"net_pnl":2570.590555885521,"sharpe":2.351544266220589,"max_dd_pct":0.7617075330417303}},"robustness_stress_floor_net_pnl":1371.435338611023,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":0.8571428571428571,"passed":true,"neighbours":7,"agreeing":6}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-f3e014df86c8ba9a","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":68,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-fcd3036f73e61d9f — HISTORICAL

Baseline file SHA-256：`afeb35f8af2a742ca8b3f415e76a19cf105cc8d792c5e478d424b059ebd89260`；archive locator：`survivors/sv-fcd3036f73e61d9f/baseline.json`。

```json
{"survivor_id":"sv-fcd3036f73e61d9f","family_id":"mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05","round_id":"mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05-r1","run_id":"mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05-r1-u2","kanban_task_id":null,"cohort":"BNBUSDT/15m","symbol":"BNBUSDT","timeframe":"15m","challenger_of":null,"strategy_params":{"strategy_case":9},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.1,"breakeven_tp_pct":0.01,"invalidation_pct":0.05},"params_sha256":"sha256:c3cfb0562233435babcacbeacaef93aa57bb801327228c5b2ff61a38e088fec1","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:9cc17bf56e42ca5e01db62bb3d0037632db20f3c5da302de77262f93b840e7c1","bundle_identity_sha256":"sha256:c00ee9d22bee800d85e6b8e7923da16633dcf6cb04808a94f9c86a9fe065fb63","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":1903.8121025491298,"sharpe":2.267577032966297,"episodes":1158,"max_dd_pct":0.6900292517969648},"oos":{"net_pnl":318.793509111431,"sharpe":1.9027005814040838,"episodes":277,"max_dd_pct":0.38071957345474067},"full":{"net_pnl":2222.605611660561,"sharpe":2.201623388656203,"episodes":1435,"max_dd_pct":0.6859524038567197,"annualized_return":0.015327275895957948,"avg_trades_per_year":305.6173469387755},"robustness":{"fee_2x":{"net_pnl":289.0680651380457,"sharpe":0.2922781430013452,"max_dd_pct":2.166846869752891},"funding_2x":{"net_pnl":2219.8859692136225,"sharpe":2.198465600863153,"max_dd_pct":0.6930009704052531},"entry_delay_1_bar":{"net_pnl":1404.8613573372158,"sharpe":1.7255389533490513,"max_dd_pct":0.7043220620515117},"slippage_2ticks":{"net_pnl":2145.846328105904,"sharpe":2.1221957968173477,"max_dd_pct":0.7003497993465504}},"robustness_stress_floor_net_pnl":289.0680651380457,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":0.8333333333333334,"passed":true,"neighbours":6,"agreeing":5}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-fcd3036f73e61d9f","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"ABSENT","evidence_manifest_path":null,"evidence_manifest_sha256":null,"rank":48,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{},"baseline_fields_absent_in_leaderboard":[]}}
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

`hb_ready_status: NOT_LOSSLESS`。MNQ sessions、5m/15m、next-open/limit-touch 與未解 case mapping 均不可 losslessly 轉成當前 crypto 單 pair lane。

Research-only、not-approved；不能進目前 Hummingbot/Qlib 績效下游，不是 Paper/Testnet/Live approval。普通 non-Scout reconstruction 紀錄可經獨立 provenance/research review 保留，並非 Scout one-file PASS admission。

## Related Wiki records

`quant/mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05.md` — 本紀錄上列 hash 的原研究 provenance，未修改 Wiki。

## Sources

1. Primary：https://arxiv.org/abs/2605.04004v1
2. Pinned historical source：https://github.com/HCH725/alpha-strategy-research/blob/f76d7f8e947fc27d07a3ee6436c1419da11bd648/mnq-intraday-ohlcv-signals-gross-edge-ceiling-falsification-2026-09-05.md
3. Historical baseline/leaderboard archive：https://github.com/HCH725/validated-survivor-research/tree/15c0a95162b60a664b43ac60157225c7300ad789；commit 及 per-baseline raw digests 以上述 Provenance/Evidence 為準，並未聲稱所有 reference 可供匿名讀者直接下載。
