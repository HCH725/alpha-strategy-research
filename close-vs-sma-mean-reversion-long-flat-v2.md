---
schema: strategy-research-record-v1
hb_ready_status: NOT_LOSSLESS
title: Close-vs-SMA mean reversion LONG/FLAT v2 — 折價事件與 position-dependent DCA
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
- https://github.com/HCH725/quant-runtime-pipeline/blob/0363011bbab4c48aefc2913a6b61a509980b80b4/container/scripts/20_strategy_a_run.py
- https://github.com/HCH725/quant-runtime-pipeline/blob/0363011bbab4c48aefc2913a6b61a509980b80b4/container/scripts/20_strategy_a_run.py
- HCH725/validated-survivor-research commit 15c0a95162b60a664b43ac60157225c7300ad789
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Close-vs-SMA mean reversion LONG/FLAT v2 — 折價事件與 position-dependent DCA

## Provenance

- Family identity：`close-vs-sma-mean-reversion-long-flat-v2`；本次 consolidation 只按原 baseline family_id，不依 Sharpe 重新排名／挑選。
- Primary source：https://github.com/HCH725/quant-runtime-pipeline/blob/0363011bbab4c48aefc2913a6b61a509980b80b4/container/scripts/20_strategy_a_run.py。
- 原始 executable source：`container/scripts/20_strategy_a_run.py`，commit `0363011bbab4c48aefc2913a6b61a509980b80b4`，Git blob `77d418b4047ac8ad34681a6195a507e2cb82b9b5`；raw SHA-256 `c4f9a216ce424a6c0c34379f29a74d0b348da9036818b0b590bfcaeba853b40f`。
- 精確 Wiki record 缺席。本輪只用與原 launch digest 相符的程式／run evidence 還原，沒有新增 Wiki 或推測 paper。
- Historical input：`HCH725/validated-survivor-research` commit `15c0a95162b60a664b43ac60157225c7300ad789` 的 `survivors/<survivor_id>/baseline.json`，本家族 2 筆，cohorts：`BTCUSDT/1h`, `SOLUSDT/4h`。
- Derived leaderboard：同一 repo `leaderboard/leaderboard.json`，raw SHA-256 `e8fdd38c8468960eee5b574e93d27615635bcb266fe481ab8c1409720d96c42e`；它不是 frozen bundle 本身，也不是採用 gate。

- 原 launch evidence：`evidence/strategy-a-v2-launch-record-20260913.json`，commit `4266546346f4e3bfad93354875792d6522269d29`，精確 family/round/run 與 runner digest 對齊；spec/bundle/source data 的原始 bytes 未重新取得。本輪只做 static read，沒有啟動 runner。

- Source-to-legacy-Qlib mapping gap：family 名称、strategy flags/case IDs 或舊 PASS 不證明原文 source-native signal、模型 weights、universe、因果時序與執行機制一致。除本紀錄明列已釘選的程式規則外，沒有補造代碼對照。paper方法、研究解讀與historical DCA分層保留；尚未證明多個 legacy codes 對應不同完整 core mechanisms，故不任意拆成新策略。

## Economic mechanism

### Source-reported

此家族的 primary source 是可釘選的原始歷史研究程式，不是 paper：當收盤價首次落到自己 trailing SMA 的折價門檻之下，做 long/flat mean-reversion hypothesis，再以 position-dependent DCA / TP / invalidation 執行。沒有精確 Wiki，但不需要由名稱猜規則。

### Research interpretation

這是方法／假說的普通研究封存，不是把歷史 survivor 標籤當成新 alpha。本家族原始程式的精確 mean-reversion / entry / exit 對照如下，但語意可追溯不等於結果已復驗。

## Signal

釘選 runner 的 rolling_sma (lines 370–376) 為包含當前 close 的 trailing arithmetic SMA；slice 前 window-1 bars 未定義。simulate (lines 415–421) 計算 b[t] = close[t] < SMA_window[t] * (1-discount)，entry event 是 b[t] AND NOT b[t-1]，slice 初始 predecessor=false。LONG only、無 short；已有 episode 時略過其終了之前的 entry edges (line 562)。SMA 回升不是 signal exit。baseline 的 BTCUSDT/1h 為 window=20、discount=0.03；SOLUSDT/4h 為 window=100、discount=0.03，詳見無損 JSON。

## Required data

歷史程式依賴每 cohort 的 OHLCV、instrument tick/taker-fee/margin/leverage metadata 及 funding observations。需先定位價格、funding、calendar/day-index 與 evaluation slices；本輪沒有讀取或補建已退役結果盤。

Historical cohort resolution、parameters 與 data cutoff 以 Evidence 的原 JSON 為準，不補齊不存在的字段，不降採樣、不改 symbol。baseline 不含完整行情 manifest、signal arrays、model checkpoints 或逐筆 trade ledger；它不是可直接執行的策略定義。

## Execution assumptions

source simulate (lines 478–562) 的 baseline entry 是 event bar close 加 adverse tick，不是 next open；entry_delay_1_bar 使用下一 close。position-dependent fills 由 OHLC low-first/trigger ordering 模擬；DCA levels 以初次 entry price 及 spacing 決定，新增 quantity 依 base_quote、leverage、size_multiplier，TP/stop 依 average cost；另有 margin backstop、slice-end close、capital-exhaustion halt。START_EQUITY=30000；base_quote/leverage 來自 registered run inputs，不能默換目前 6%+6%+6%／3×/5× overlay。DCA loop 的 k 每 bar 重設為 1，未見跨 bar 的 filled-level occupancy guard，不能聲稱最多十次累計加倉已被證實。

Historical DCA 參數只代表當時研究配置，並非 paper 原生規則，也不是目前 house overlay。未重新量測 fees、funding、margin/liquidation、slippage、intrabar path 或 fills；hash references 不是原資料 bytes 已重新驗證的宣告。

## Evidence

### Source-reported

上述 primary source 是研究作者的歷史程式規則，不是外部論文的績效主張。其 launch/terminal evidence 中的 DONE 或 self-check PASS 為當時狀態，非今日 rerun。

### Independently reproduced

Not independently reproduced. 本輪只驗 source identity／文件轉錄，沒有 Qlib rerun、Hummingbot reproduction、Paper 或 Testnet。

### Negative evidence

baseline 中 historical/OOS/full 不是可以假定相加的相同連續帳本。BTC 的 OOS Sharpe=0.536464、full=0.588432；SOL entry_delay_1_bar Sharpe=0.637267，均照原值保存，不升格為 current filters PASS。source max_dd_pct 實際以 dd/peak 輸出負的 fraction（lines 582–597），不改寫成百分點或正數。annualized_return 在 baseline 是 null，leaderboard 補算值另列。sparse daily equity marking、intrabar path、funding attribution 及 repeated-level risk 都需要獨立 event-level audit，尚未本輪驗證。

SOL 的 `slippage_2ticks.net_pnl=62226.3253` 高於 `full.net_pnl=60695.711357`；不能直接解讀為更多 adverse slippage 改善策略。position-dependent triggers/fills、重複 level、slice accounting 或 historical summary provenance 需事件層回收才能判斷；本輪不修正或合理化原值。

### HISTORICAL QLIB SURVIVOR EVIDENCE — 非目前 Hummingbot reproduction

以下每個 baseline JSON 保留全部原鍵／數值／null／巢狀結構，唯一刪除 top-level `bundle_path` 的機器絕對路徑。bundle 邏輯定位仍可由 family_id / round_id / run_id 與 survivor ID 找到；不假裝本輪讀取已退役結果盤。每筆獨立列 raw baseline-file SHA-256，它與 `params_sha256`、`bundle_sha256`（檔案 bytes）、`bundle_identity_sha256`（歷史 identity recipe）互不相同。

鍵名 `net_pnl` / `sharpe` / `max_dd_pct` / `annualized_return` 原樣保留，不重命名成 ROI、不對 MDD 改 sign／比例／百分點、不跨 lineage 默認同一 annualization。baseline 欄位缺席不同於 null；不從另一層悄悄補值。`source_verdict: PASS` 與 `neighbourhood.passed` 都是 HISTORICAL，不能解讀成今日 efficacy、source parity 或 HB_READY PASS。

每筆另列 `leaderboard_snapshot`：`additional_fields` 為 derived index 額外欄位，`baseline_field_overrides` 為該 index 與 baseline 不同的完整 top-level 值；空 object 明示無差異。兩者都不回寫 baseline。僅非 null 的 `evidence_manifest_path` 去除原 results-root 絕對前綴，保留 `_survivors/...` 相對 locator；null 留 null。rank / top10 / package PRESENT / FROZEN_ONLY 只是當時 derived state，不能解讀為今天 evidence package bytes 存在或新 forward evidence。

#### sv-904822905a811669 — HISTORICAL

Baseline file SHA-256：`fef85326fcceb75b0cb5b2f7eb081962a0b84a0257762bed93956aeaed9fd476`；archive locator：`survivors/sv-904822905a811669/baseline.json`。

```json
{"survivor_id":"sv-904822905a811669","family_id":"close-vs-sma-mean-reversion-long-flat-v2","round_id":"close-vs-sma-mean-reversion-long-flat-v2-r1","run_id":"close-vs-sma-mean-reversion-long-flat-v2-r1-u1","kanban_task_id":"t_1f97bf6b","cohort":"BTCUSDT/1h","symbol":"BTCUSDT","timeframe":"1h","challenger_of":null,"strategy_params":{"window":20,"discount":0.03},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.0,"breakeven_tp_pct":0.01,"invalidation_pct":0.1},"params_sha256":"sha256:09343579c45d15a94ab81d2be2e7f61a9814a728d533fe6197f6c6b582f74cf6","research_data_cutoff":"2026-09-10","bundle_sha256":"sha256:4638885f5f3787ee947d860a1fe48627de9802c2e9adb1d13f62a6917240eb53","bundle_identity_sha256":"sha256:c051759fdf8291f66bce8f7249cb226b856c04de2ad78a8d055fdb4657543363","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":14790.093348,"sharpe":0.676463,"episodes":170,"max_dd_pct":-0.199943},"oos":{"net_pnl":6016.344052,"sharpe":0.536464,"episodes":34,"max_dd_pct":-0.150469},"full":{"net_pnl":14913.47311,"sharpe":0.588432,"episodes":204,"max_dd_pct":-0.21656,"annualized_return":null},"robustness":{"fee_2x":{"net_pnl":11353.765787,"sharpe":0.475937,"max_dd_pct":-0.342882},"funding_2x":{"net_pnl":14701.443429,"sharpe":0.580853,"max_dd_pct":-0.218248},"entry_delay_1_bar":{"net_pnl":12210.28144,"sharpe":0.483266,"max_dd_pct":-0.257778},"slippage_2ticks":{"net_pnl":14876.072721,"sharpe":0.587101,"max_dd_pct":-0.216737}},"robustness_stress_floor_net_pnl":11353.765787,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":0.833333,"passed":true,"neighbours":6,"agreeing":5}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-904822905a811669","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"PRESENT","evidence_manifest_path":"_survivors/evidence/sv-904822905a811669/manifest.json","evidence_manifest_sha256":"sha256:1dc0db9ddf54fe1697eae5737bb59eb31b2f2059330a2b51c77a256e2b65a7ae","rank":76,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{"full":{"net_pnl":14913.47311,"sharpe":0.588432,"episodes":204,"max_dd_pct":-0.21656,"annualized_return":null,"avg_trades_per_year":43.47199533255542}},"baseline_fields_absent_in_leaderboard":[]}}
```

#### sv-f762a1da8909a5bf — HISTORICAL

Baseline file SHA-256：`5865d4f59aa1b7f3e96be74432e9702146d8dffdff63994168b697a6670f649e`；archive locator：`survivors/sv-f762a1da8909a5bf/baseline.json`。

```json
{"survivor_id":"sv-f762a1da8909a5bf","family_id":"close-vs-sma-mean-reversion-long-flat-v2","round_id":"close-vs-sma-mean-reversion-long-flat-v2-r1","run_id":"close-vs-sma-mean-reversion-long-flat-v2-r1-u1","kanban_task_id":"t_1f97bf6b","cohort":"SOLUSDT/4h","symbol":"SOLUSDT","timeframe":"4h","challenger_of":null,"strategy_params":{"window":100,"discount":0.03},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.1,"breakeven_tp_pct":0.01,"invalidation_pct":0.1},"params_sha256":"sha256:95ca1f1622d9d9138685d8e5d7786d7e13562a1fc969a440e563c384b54e609c","research_data_cutoff":"2026-09-10","bundle_sha256":"sha256:4638885f5f3787ee947d860a1fe48627de9802c2e9adb1d13f62a6917240eb53","bundle_identity_sha256":"sha256:c051759fdf8291f66bce8f7249cb226b856c04de2ad78a8d055fdb4657543363","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":51035.16769,"sharpe":4.017045,"episodes":184,"max_dd_pct":-0.009704},"oos":{"net_pnl":8485.605171,"sharpe":2.17438,"episodes":41,"max_dd_pct":-0.003455},"full":{"net_pnl":60695.711357,"sharpe":4.396559,"episodes":226,"max_dd_pct":-0.009704,"annualized_return":null},"robustness":{"fee_2x":{"net_pnl":53716.312365,"sharpe":4.390801,"max_dd_pct":-0.010831},"funding_2x":{"net_pnl":60649.53634,"sharpe":4.399323,"max_dd_pct":-0.009713},"entry_delay_1_bar":{"net_pnl":17375.485091,"sharpe":0.637267,"max_dd_pct":-0.412841},"slippage_2ticks":{"net_pnl":62226.3253,"sharpe":4.379434,"max_dd_pct":-0.009619}},"robustness_stress_floor_net_pnl":17375.485091,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":0.857143,"passed":true,"neighbours":7,"agreeing":6}}
```

```json
{"leaderboard_snapshot":{"survivor_id":"sv-f762a1da8909a5bf","additional_fields":{"forward":{"has_forward":false,"slices":0},"evidence_state":"FROZEN_ONLY","last_evidence_end":null,"evidence_package_status":"PRESENT","evidence_manifest_path":"_survivors/evidence/sv-f762a1da8909a5bf/manifest.json","evidence_manifest_sha256":"sha256:87f1bd035ff80285398aa63fc0e335ddffa7618e30eb16d84e34e43b4df5052d","rank":43,"in_top10":false,"champion_candidate":false},"baseline_field_overrides":{"full":{"net_pnl":60695.711357,"sharpe":4.396559,"episodes":226,"max_dd_pct":-0.009704,"annualized_return":null,"avg_trades_per_year":48.160151691948656}},"baseline_fields_absent_in_leaderboard":[]}}
```

## Falsification plan

1. 先恢復 exact source-to-case / model / signal / timing 對照，若不能證明便維持 source-mapping gap；不得以調參 rescue 或另寫 proxy 宣稱復現原文。
2. 若將來另獲執行授權，先用 prefix/suffix perturbation、landed-label checks、formation-to-order timestamps 與 universe alignment 反證 look-ahead；再以同一事件模型核對 fills、funding、fee、margin 及 parameter sensitivity。
3. 保留負面 controls、成本壓力、完整 denominator 與未觀測欄位。對 forecasting / risk-control 主張，須各有 baseline/ablation，不能單靠一個 per-coin Sharpe 認定方法有效。
4. 以上僅是未來 research tests，不是這張 archival PR 已跑過的測試，也不授權 backtest、pipeline 或交易。

## Crypto portability

原始研究程式本身使用 crypto cohorts，但 source mapping 可追溯不等於 event-level reproduction 或 current eligibility。

## Limitations

- baseline 與 leaderboard 是 frozen/derived archival summaries，不包含完整 robustness grid 的所有未勝出 cases、鄰居逐筆結果、source-native code/model 或事件序列；現存四 stress grids 和 neighborhood summary 全保留，缺失資料不捏造。
- historical/OOS/full 的細分日期與 split recipe 未隨 baseline 提供；只保留 exact data cutoff 與原 identity，除有已回收 source 證據外不推論 slice endpoints。
- 存在 survivor selection、搜尋過的 evaluation periods、樣本數不足、資料／成本／模型身份尚未回收的限制；不因 baseline 帶 PASS 而移除。
- Metric definitions/units 可跨 engine lineage 不同；baseline 与 derived leaderboard 的補算差異各自保留，不混寫成新的績效真值。

## Implementation status

Not implemented in the current research/runtime stack. Historical code / baselines 在此只作 Provenance/Evidence；本輪未實作、修復、採用或部署策略。

## Adoption boundary

`hb_ready_status: NOT_LOSSLESS`。intrabar touch/path order、position-dependent DCA/margin 與 repeated-level semantics 不可由 pinned same-bar-close candle simulator 無損代替。過去其他 SMA/EMA parity 案例不等於此 frozen v2 runner 的 lossless proof。

Research-only、not-approved；不能進目前 Hummingbot/Qlib 績效下游，不是 Paper/Testnet/Live approval。普通 non-Scout reconstruction 紀錄可經獨立 provenance/research review 保留，並非 Scout one-file PASS admission。

## Related Wiki records

精確 `quant/close-vs-sma-mean-reversion-long-flat-v2.md` 不存在；不建立虛構 Wiki link。

## Sources

1. Primary：https://github.com/HCH725/quant-runtime-pipeline/blob/0363011bbab4c48aefc2913a6b61a509980b80b4/container/scripts/20_strategy_a_run.py
2. Pinned historical source：https://github.com/HCH725/quant-runtime-pipeline/blob/0363011bbab4c48aefc2913a6b61a509980b80b4/container/scripts/20_strategy_a_run.py
3. Historical baseline/leaderboard archive：https://github.com/HCH725/validated-survivor-research/tree/15c0a95162b60a664b43ac60157225c7300ad789；commit 及 per-baseline raw digests 以上述 Provenance/Evidence 為準，並未聲稱所有 reference 可供匿名讀者直接下載。
4. Historical launch evidence：https://github.com/HCH725/quant-runtime-pipeline/blob/4266546346f4e3bfad93354875792d6522269d29/evidence/strategy-a-v2-launch-record-20260913.json
