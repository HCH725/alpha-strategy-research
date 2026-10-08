---
schema: strategy-research-record-v1
hb_ready_status: NOT_LOSSLESS
title: "AEAP/SEADS — 公式化 Alpha 發掘與流動性 Rank-Product 家族"
created: 2026-10-08
updated: 2026-10-08
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2026-09-01
sources:
  - "Pan, Ding, Giesecke. Agentic Empirical Asset Pricing: Methodological Foundations. arXiv:2609.00731v1. https://arxiv.org/html/2609.00731v1"
  - "HCH725/alpha-strategy-research: 9d96854831d392523a42135165780f4ab26b1642, aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03.md, blob 147879ac9c9893e54acef12264e9d2a875d59cec"
  - "HCH725/quant-runtime-pipeline: c993096b9f583a2d760fd52d52dfb0b8938d63d2, container/scripts/320_aeap_seads_run.py"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions:
  - "舊 Wiki 與歷史 runner 的流動性公式未保留論文 Appendix L 的三個 1-rank 補數。"
  - "歷史 runner 的次月開盤時序宣告與實際同月 direction 索引不一致。"
---

# AEAP/SEADS — 公式化 Alpha 發掘與流動性 Rank-Product 家族

## Provenance

- **Family identity:** `aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03`。
- **Primary source:** Yingjian Pan、Xiaowei Ding、Kay Giesecke，*Agentic Empirical Asset Pricing: Methodological Foundations*，`arXiv:2609.00731v1`，2026-09-01。本輪直接查讀 §3.1、§3.3、Appendices E、K、L，而不是將舊摘要當作原文。
- **既有研究紀錄：** 原 repo commit `9d96854831d392523a42135165780f4ab26b1642` 的同名 root-level Markdown，Git blob `147879ac9c9893e54acef12264e9d2a875d59cec`；對照 `quant/aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03.md`。兩者只有舊 implementation-stack 名稱的文字差異，不能把目前 Wiki 稱為逐位元相同 blob。
- **正式 intake 線索：** review-state 的 `ingested_wiki_records` 包含上述精確 Wiki identity；該 state 最後審查的 repo commit 為 `2799e34c5c7f8d6f7036e35d9ae7468832712c97`。這是收錄 provenance，不是本家族新的獨立驗證，也不是逐檔 `reviewed_commit` 證明。
- **歷史實驗來源：** validated survivor research 的四份 `baseline.json`，同一 family、round `...-r1`、run `...-r1-u1`。四份策略參數僅有 `lookback_scale` 差異；回收 runner 顯示它們屬同一流動性 rank-product 機制，沒有證據顯示四個 survivor 分屬不同核心機制。
- **可追溯 preparation/run 證據：** `evidence/320_aeap_seads-r1-run-20260928.json` 明確引用同一 family/round/run，釘選 runner commit `c993096b9f583a2d760fd52d52dfb0b8938d63d2`。本輪靜態讀取該歷史程式並核對 SHA-256 `3bb7c938a770aa08a2bce2b10585f3a44bcd1eb7d751d369a08dd064ec2bf165`，與 run 證據釘選值相同；未啟動 runner、Qlib、container 或 backtest。
- **Source-to-run mapping gap：** 可還原舊 runner 的明確改寫，不代表論文原生機制已被無損重現。原文的補數 rank、股市特徵定義、股票 universe、發掘流程及組合模型，與舊 crypto proxy/執行程式不同；另存在下述交易時序矛盾。未重新驗證 baseline 指向的 bundle 內容、逐筆交易或資料身份。舊績效只作歷史實驗證據。

## Economic mechanism

### Source-reported

AEAP 將假說、公式化、資料執行與評估交由代理閉環完成；SEADS 是其因子發掘實例。原文以生產力、績效與新穎性共同評估因子。Appendix L 的流動性範例結合低交易摩擦、低交易不活躍與穩定成交額；不是單幣 DCA 系統。[1]

### Research interpretation

本家族保留「因子發掘方法 → 流動性互動因子 → 舊 crypto 改寫」的關係，但不將三者宣稱為同一已驗證交易策略。其他論文示例涉及財務困境及現金獲利，未被下列四個 survivor 的 runner 採用，因此不擅自把它們拆成新策略紀錄或附會到舊績效。

## Signal

### 原文流動性範例

Appendix L 明列：[1]

```text
(1-rank(bidaskhl_21d))
* (1-rank(zero_trades_126d))
* (1-rank(dolvol_var_126d / (1+trail12m_mean)))
```

rank 是橫斷面運算；原文 §3.1 採月度特徵對下一期報酬，§3.3.5／Appendix E 的組合層使用 `Ridge(alpha=1)` 對 admitted library 評分，再形成月度多空組合。Appendix K 的因子 Sharpe 則用月度十分位多空報酬；不可把不同評估層混為一談。[1]

### 歷史 runner 的實際改寫（非 source-native）

來源 [3] 的 `factor_components`、`average_rank_percentile`、`build_case_signal` 定義：

- 固定 cross-section：`BNBUSDT`、`BTCUSDT`、`ETHUSDT`、`SOLUSDT`。
- 每個執行 timeframe 皆以日線形成月底分數。以 `lookback_scale=s` 對 `(21,126,365)` 日套用 `floor(x*s+0.5)`；365 日是舊程式對 12 個月的改寫，不是原文定義的證明。
- `a` 為 `(high-low)/((high+low)/2)` 的 trailing mean；`b` 為 trailing 視窗內零成交量日數；`c` 為 `Var_pop(volume*close)/(1+Mean_trailing(volume*close))`。
- `score=rank(a)*rank(b)*rank(c)`，**缺少原文三個 `1-rank` 補數**；bid-ask 特徵亦被替換為高低價 range proxy。不得把此式寫成原文精確實作。
- rank 採 ties 平均名次，再轉為 `(rank-1)/(n-1)`；以 `(score 降序,a 的 rank 降序,symbol 升序)` 排序，最高一名 long、最低一名 short、另外兩名 flat。
- 日線時間軸須四幣一致；月底任何特徵非有限值時跳過該月。充分 warmup 由 scaled 日數決定，不能沿用舊摘要的「126 日即足夠」。

### 時序矛盾

來源 [3] lines 810–861 將月底計算的方向寫入 `dirs[int(month)]`，再以 `directions` 鍵回傳；lines 878–885 直接按交易 bar 的**同月**取該方向；lines 1934–1937 未加月度 lag；`simulate` lines 1082–1096 則在該月第一個 bar 開盤使用方向。這與 docstring／`signal_constants` 宣稱「次月開盤」不一致。靜態流程顯示月底資訊被同月月初使用的因果性問題；對 formation 之後資料的 suffix-perturbation 檢查不能證明交易當下沒有此洩漏。本輪未修正舊程式、未重算或替換 baseline 數值。

## Required data

- 原文使用美股月度橫斷面特徵與報酬，JKP、CRSP/Compustat panels；資料不是四個 crypto symbols。[1]
- 歷史改寫依賴四幣共同日線 OHLCV、月底 cross-section，以及各 survivor cohort 的執行 Kline；不是單幣獨立訊號。
- 舊 runner 另外讀取 instrument tick/taker-fee metadata 與歷史 funding observations 作執行會計；本輪沒有要求目前 Qlib runtime 或資料 filesystem 存在。
- run 證據釘選的資料截止為 `2026-09-11`，但本輪未獨立核對原始行情、完整 funding coverage 或逐筆交易。

## Execution assumptions

以下僅還原 [3] 的歷史研究設定，**不是原文規則，也不是目前 house overlay**：

- 註解宣稱月底 formation／次月首 bar open 入場／持有月份末 bar close 出場；實際同月索引矛盾以上述 Signal 為準，不能直接採信註解。
- `START_EQUITY=30000`、`BASE_QUOTE=1000`、`LEVERAGE=10`；初始 notional 受當時 equity 限制。最多 10 次 adverse-price scale-in，共 11 routine active levels，第 12 tranche reserve。
- 加倉觸價以首次 entry price、`spacing_pct*k` 決定；新增 notional 依 `size_multiplier**k`。TP 與 invalidation 隨平均成本變動，月末／樣本窗界線平倉；提早結束後不在同月任意重入。
- 既定 bar 內流程包含 open actions、funding、gap stop、margin guard、scale-ins、stop-before-adds、resting invalidation、TP、month exit。這些 OHLC 觸價順序不是目前 same-bar-close 模型的無損替代。
- taker fees 來自舊 metadata，每腿一個 adverse tick；stress grids 增加 fees、funding、entry delay 或 slippage。程式對缺漏 funding 區間以零處理，不能稱為完整歷史實際 funding 成本。
- [3] 的樣本切分為 historical `2022-01-01..2025-09-30`、OOS `2025-10-01..2026-09-11`、full `2022-01-01..2026-09-11`。這是程式內設定，不是本輪實證重現。

## Evidence

### Source-reported

Appendix L／Table 12 的流動性範例 OOS Sharpe 為 `0.89`、OOS 年化報酬 `13.1%`；作者明示示例經挑選，並非平均 admitted-factor 表現。這些是股市因子結果，非以下 crypto survivor 結果。[1]

### Independently reproduced

Not independently reproduced. 本輪只核對 provenance、runner bytes 與 baseline 轉錄；沒有重新跑研究或 Hummingbot reproduction。

### Negative evidence

- 原文流動性因子的三個補數 rank 在舊 Wiki 與舊 runner 中遺失，資料欄位也被 proxy 化。[1][2][3]
- 回收程式的 direction 月份對齊存在明確靜態矛盾；既有 `PASS_NO_LOOKAHEAD` 字串或 historical PASS 不足以排除此問題。
- BNBUSDT 三個 timeframe 共有相同 historical metrics，1h 與 5m 甚至共享 OOS/full metrics；保留原值，不據此宣稱獨立重現或偽造，須在逐筆資料可回收時另驗。
- ETHUSDT/1d 的 `entry_delay_1_bar` baseline Sharpe 為 `0.5480660853135894`、`max_dd_pct=9.176207177630953`，顯示舊實驗對 entry timing 的敏感性。
- 四份 baseline 未攜帶完整 signal arrays、trade ledgers 或 falsification battery 結果。run 啟動證據中的 self-check／smoke 宣告不是本輪重跑結果。

### HISTORICAL QLIB SURVIVOR EVIDENCE — 非目前 Hummingbot reproduction

四筆以下 JSON 均直接保留 baseline 數值與鍵名，只排除機器特定 `bundle_path`，不重新換算、篩選或修補。`source_verdict: PASS` 是舊歷史 verdict，與 `hb_ready_status` 不同。[4]

共享 round/run identity 為各筆所列值；run 證據另提供 round-spec SHA-256 `0898189925c0f73cfc99534e4efffd217bebace2e99292197f4aa1624ca0ecb9`、run-spec SHA-256 `2c0aaec52e04d0f06d5dca29ede47b7e1a99f607109b0d4bbd49c6e7da906959` 與 self-check SHA-256 `7ed45c1511e878471dfeb64aa2e1c7746b61c0c26bba8f8e73b653fec6cc33a7`。[5] 本輪核對的是 runner digest，未聲稱重新核對所有 spec、self-check、bundle 或 execution data bytes。

#### sv-53fe722d6f03c724 — HISTORICAL QLIB SURVIVOR EVIDENCE

```json
{"survivor_id":"sv-53fe722d6f03c724","family_id":"aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03","round_id":"aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03-r1","run_id":"aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03-r1-u1","kanban_task_id":null,"cohort":"BNBUSDT/4h","symbol":"BNBUSDT","timeframe":"4h","challenger_of":null,"strategy_params":{"lookback_scale":1.0},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.1,"breakeven_tp_pct":0.01,"invalidation_pct":0.05},"params_sha256":"sha256:97acc3efbc27a72a5d44f48fa3195c3d7e0ead5e2b8f49422831eaeccadc9c5f","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:cfc8f125d2b2547fecf92dbe41135af0b8910acba6f90f5c12c461015ecfa65a","bundle_identity_sha256":"sha256:643e9e2e06dacb37261ecf5f5076674d9bb5dd26b92a5cd160b1dadd30495d70","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":2282.9017813938185,"sharpe":1.632614139952619,"episodes":13,"max_dd_pct":0.18840941685921375},"oos":{"net_pnl":854.9432253061568,"sharpe":2.098389580329782,"episodes":5,"max_dd_pct":0.0},"full":{"net_pnl":3137.8450066999753,"sharpe":1.7328978738425476,"episodes":18,"max_dd_pct":0.18840941685921375,"annualized_return":0.02139754390248849,"avg_trades_per_year":3.8335276967930025},"robustness":{"fee_2x":{"net_pnl":2789.9786038246016,"sharpe":1.687354677237496,"max_dd_pct":0.22285687253605796},"funding_2x":{"net_pnl":3137.7379079433763,"sharpe":1.7328309588342363,"max_dd_pct":0.18840941685921375},"entry_delay_1_bar":{"net_pnl":2272.2221335653835,"sharpe":1.170229694668302,"max_dd_pct":0.6277543443083645},"slippage_2ticks":{"net_pnl":3129.6595538444153,"sharpe":1.730541464504112,"max_dd_pct":0.18987669917223704}},"robustness_stress_floor_net_pnl":2272.2221335653835,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":0.6666666666666666,"passed":true,"neighbours":6,"agreeing":4}}
```

#### sv-5d4ae68942e18632 — HISTORICAL QLIB SURVIVOR EVIDENCE

```json
{"survivor_id":"sv-5d4ae68942e18632","family_id":"aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03","round_id":"aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03-r1","run_id":"aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03-r1-u1","kanban_task_id":null,"cohort":"BNBUSDT/5m","symbol":"BNBUSDT","timeframe":"5m","challenger_of":null,"strategy_params":{"lookback_scale":1.0},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.1,"breakeven_tp_pct":0.01,"invalidation_pct":0.05},"params_sha256":"sha256:97acc3efbc27a72a5d44f48fa3195c3d7e0ead5e2b8f49422831eaeccadc9c5f","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:cfc8f125d2b2547fecf92dbe41135af0b8910acba6f90f5c12c461015ecfa65a","bundle_identity_sha256":"sha256:643e9e2e06dacb37261ecf5f5076674d9bb5dd26b92a5cd160b1dadd30495d70","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":2282.9017813938185,"sharpe":1.632614139952619,"episodes":13,"max_dd_pct":0.18840941685921375},"oos":{"net_pnl":756.087496220631,"sharpe":2.018438412676417,"episodes":5,"max_dd_pct":0.0},"full":{"net_pnl":3038.9892776144497,"sharpe":1.711544026381988,"episodes":18,"max_dd_pct":0.18840941685921375,"annualized_return":0.020748294351800922,"avg_trades_per_year":3.8335276967930025},"robustness":{"fee_2x":{"net_pnl":2702.06797432474,"sharpe":1.6649936245502268,"max_dd_pct":0.22285687253605796},"funding_2x":{"net_pnl":3038.8821788578507,"sharpe":1.7114757777218883,"max_dd_pct":0.18840941685921375},"entry_delay_1_bar":{"net_pnl":2841.2776275826645,"sharpe":1.7162334590425288,"max_dd_pct":0.16150528220851013},"slippage_2ticks":{"net_pnl":3031.0031101784384,"sharpe":1.7091376397347267,"max_dd_pct":0.18987669917223704}},"robustness_stress_floor_net_pnl":2702.06797432474,"robustness_stress_floor_grid":"fee_2x","neighbourhood":{"same_sign_fraction":0.8333333333333334,"passed":true,"neighbours":6,"agreeing":5}}
```

#### sv-7ad562240e7a6075 — HISTORICAL QLIB SURVIVOR EVIDENCE

```json
{"survivor_id":"sv-7ad562240e7a6075","family_id":"aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03","round_id":"aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03-r1","run_id":"aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03-r1-u1","kanban_task_id":null,"cohort":"BNBUSDT/1h","symbol":"BNBUSDT","timeframe":"1h","challenger_of":null,"strategy_params":{"lookback_scale":1.0},"dca_params":{"spacing_pct":0.01,"size_multiplier":1.1,"breakeven_tp_pct":0.01,"invalidation_pct":0.05},"params_sha256":"sha256:97acc3efbc27a72a5d44f48fa3195c3d7e0ead5e2b8f49422831eaeccadc9c5f","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:cfc8f125d2b2547fecf92dbe41135af0b8910acba6f90f5c12c461015ecfa65a","bundle_identity_sha256":"sha256:643e9e2e06dacb37261ecf5f5076674d9bb5dd26b92a5cd160b1dadd30495d70","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":2282.9017813938185,"sharpe":1.632614139952619,"episodes":13,"max_dd_pct":0.18840941685921375},"oos":{"net_pnl":756.087496220631,"sharpe":2.018438412676417,"episodes":5,"max_dd_pct":0.0},"full":{"net_pnl":3038.9892776144497,"sharpe":1.711544026381988,"episodes":18,"max_dd_pct":0.18840941685921375,"annualized_return":0.020748294351800922,"avg_trades_per_year":3.8335276967930025},"robustness":{"fee_2x":{"net_pnl":2702.06797432474,"sharpe":1.6649936245502268,"max_dd_pct":0.22285687253605796},"funding_2x":{"net_pnl":3038.8821788578507,"sharpe":1.7114757777218883,"max_dd_pct":0.18840941685921375},"entry_delay_1_bar":{"net_pnl":2317.2337954613804,"sharpe":1.716836842741777,"max_dd_pct":0.13628187006426842},"slippage_2ticks":{"net_pnl":3031.0031101784384,"sharpe":1.7091376397347267,"max_dd_pct":0.18987669917223704}},"robustness_stress_floor_net_pnl":2317.2337954613804,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":0.6666666666666666,"passed":true,"neighbours":6,"agreeing":4}}
```

#### sv-832b7378d571a18f — HISTORICAL QLIB SURVIVOR EVIDENCE

```json
{"survivor_id":"sv-832b7378d571a18f","family_id":"aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03","round_id":"aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03-r1","run_id":"aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03-r1-u1","kanban_task_id":null,"cohort":"ETHUSDT/1d","symbol":"ETHUSDT","timeframe":"1d","challenger_of":null,"strategy_params":{"lookback_scale":0.5},"dca_params":{"spacing_pct":0.02,"size_multiplier":1.0,"breakeven_tp_pct":0.01,"invalidation_pct":0.1},"params_sha256":"sha256:d9d6ead96e1b6097aca965db7497aed969fae42784db9d4fed658a9b2967e6b1","research_data_cutoff":"2026-09-11","bundle_sha256":"sha256:cfc8f125d2b2547fecf92dbe41135af0b8910acba6f90f5c12c461015ecfa65a","bundle_identity_sha256":"sha256:643e9e2e06dacb37261ecf5f5076674d9bb5dd26b92a5cd160b1dadd30495d70","source_disposition_band":"MULTIPLE_SURVIVORS","source_verdict":"PASS","historical":{"net_pnl":5348.599533887829,"sharpe":2.4472019028957424,"episodes":29,"max_dd_pct":0.1707069365976209},"oos":{"net_pnl":1879.3655262816817,"sharpe":2.6333641742150524,"episodes":10,"max_dd_pct":0.0},"full":{"net_pnl":7227.965060169513,"sharpe":2.485720695138435,"episodes":39,"max_dd_pct":0.1707069365976209,"annualized_return":0.0470133214942241,"avg_trades_per_year":8.305976676384839},"robustness":{"fee_2x":{"net_pnl":6413.916865762904,"sharpe":2.4782374300919554,"max_dd_pct":0.1875468662370767},"funding_2x":{"net_pnl":7173.589501527937,"sharpe":2.477353021624868,"max_dd_pct":0.1707069365976209},"entry_delay_1_bar":{"net_pnl":3629.501621875839,"sharpe":0.5480660853135894,"max_dd_pct":9.176207177630953},"slippage_2ticks":{"net_pnl":7224.355924771648,"sharpe":2.4856124246510536,"max_dd_pct":0.17087700903160535}},"robustness_stress_floor_net_pnl":3629.501621875839,"robustness_stress_floor_grid":"entry_delay_1_bar","neighbourhood":{"same_sign_fraction":0.8333333333333334,"passed":true,"neighbours":6,"agreeing":5}}
```

## Falsification plan

- 先將原文公式、舊 Wiki 轉錄、crypto proxies 與 runner 實際規則分別釘選，拒絕用單幣 proxy 成績證明原生股票因子或發掘方法有效。
- 若歷史資料與逐筆事件另獲授權回收，首驗 formation-to-order 的月份 lag；在因果性未釐清前，舊績效不作 source-faithful 或可交易 alpha 宣告。此處沒有批准修復／執行 backtest。
- 另外核對 bidaskhl 等特徵定義、rank 補數、零成交量 component 的區分力、cross-sectional universe 與 ties；維持獨立樣本、成本壓力及 lookback 擾動測試。
- 對發掘流程的主張另需完整 rolling re-execution 與對照；只保留一個公式及四份 baseline 不足以評估整個發掘系統。

## Crypto portability

未證實。歷史 runner 提供一個可追溯、但經改寫且存在時序矛盾的 crypto 實驗。不能由 four-survivor 標籤推論原文特徵、股市結果或 SEADS 系統可無損移植。

## Limitations

- 原文、舊研究摘要、歷史程式與 baseline 分屬不同證據層；歷史 runner 的 digest 對齊不等於 source-to-run 語意對齊。
- 四筆 survivor 同屬 liquidity proxy，並未實作論文的完整 LLM 發掘流程、財務特徵示例或 admitted-library Ridge 組合。
- 同月索引問題、缺漏 funding 零成本處理與未核對的逐筆資料限制了歷史績效的可主張程度。
- 資料與機制需要橫斷面多幣 state；不能以局部改寫移除它而宣稱 HB_READY。

## Implementation status

目前研究/runtime stack 為 `not-implemented`。舊 runner 與 baseline 在此僅作歷史 provenance／Evidence；本輪未導入或修復任何策略、pipeline、Qlib 或 Hummingbot 程式。

## Adoption boundary

`hb_ready_status: NOT_LOSSLESS`。依目前 pinned Hummingbot `20260920`／`dev-2.17.0` contract：來源橫斷面 rank／月度多空 portfolio 違反單 pair 限制；舊改寫還需要多幣／日線 alignment、非同 bar close 的入場，以及 intrabar 觸價與 position-dependent DCA。另有明確來源公式差異與 causal timing 矛盾，不能靠 house overlay 或 survivor PASS 消除。這是普通研究紀錄，可在獨立 provenance／research review 後保留於 main；不得進入目前 Hummingbot/Qlib 績效下游，也沒有 Paper、Testnet 或 Live 授權。

## Related Wiki records

- `quant/aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03` — 原研究 provenance；本輪未修改 Wiki。

## Sources

1. Pan, Y., Ding, X., & Giesecke, K. (2026). *Agentic Empirical Asset Pricing: Methodological Foundations*. arXiv:2609.00731v1, 2026-09-01；§3.1、§3.3.5、Appendices E、K、L／Table 12。https://arxiv.org/html/2609.00731v1
2. 歷史一般策略紀錄，commit `9d96854831d392523a42135165780f4ab26b1642`，blob `147879ac9c9893e54acef12264e9d2a875d59cec`。https://github.com/HCH725/alpha-strategy-research/blob/9d96854831d392523a42135165780f4ab26b1642/aeap-seads-llm-agentic-factor-discovery-formulaic-alpha-2026-09-03.md 。另對照 Provenance 所列精確 Wiki record 與 review-state 的 ingestion membership。
3. 歷史 runner，commit `c993096b9f583a2d760fd52d52dfb0b8938d63d2`，`container/scripts/320_aeap_seads_run.py`，上述完整 SHA-256。https://github.com/HCH725/quant-runtime-pipeline/blob/c993096b9f583a2d760fd52d52dfb0b8938d63d2/container/scripts/320_aeap_seads_run.py
4. validated survivor research 的四份 `baseline.json`，以本紀錄列出的 family／survivor／bundle digests 定位；不公開機器特定絕對路徑，未聲稱本輪重現。
5. 歷史 run 證據 `evidence/320_aeap_seads-r1-run-20260928.json`，`written_at_utc=2026-09-28T15:17:07Z`，明列同一 family／round／run 與 runner、spec、self-check digests；僅作可回收的 preparation/runtime provenance，不採用其執行權限或狀態宣告。
