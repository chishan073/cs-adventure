# 🐍 Python Module

這個模組將帶你進入 Python 的世界，從基礎語法開始，逐步學習檔案操作、API 應用、Flask 專案實作等實用技能。

---

## 📌 主題規劃

| 主題編號 | 主題內容                     | 狀態 |
|----------|------------------------------|------|
| 1        | 基礎語法（變數、流程、函式） | ⬜️   |
| 2        | pip 套件管理與虛擬環境       | ⬜️   |
| 3        | 檔案操作與例外處理           | ⬜️   |
| 4        | requests / API 操作          | ⬜️   |
| 5        | Flask 初步入門與簡單專案     | ⬜️   |

✅ 完成後可以在表格旁邊打勾、加筆記或錯誤紀錄。

---

## ✨ 學習筆記區

可以在這裡撰寫各主題對應的筆記、重點整理與範例程式碼。
✅ 第一個任務：BMI 計算器（練習輸入、變數、條件、函式）
---

## 🧩 任務與練習

未來可新增任務區，例如寫一個 BMI 計算器、API 資料爬取、建立 Flask 小網站等。
✅ 任務內容：
請使用 Python 撰寫以下功能：

使用者輸入身高（公分）與體重（公斤）

計算 BMI（公式：體重 / 身高²（公尺））

判斷 BMI 類別並印出提示：


BMI 數值	結果判斷
< 18.5	過輕
18.5 - 24	正常
> 24	過重
📁 額外挑戰：
把程式寫成函式 def calculate_bmi(height_cm, weight_kg):

加上錯誤處理，例如輸入不是數字時提醒使用者
---
📦 任務二：pip 套件與虛擬環境
🎯 學習目標
使用 pip 安裝第三方套件（如 requests）

建立虛擬環境，隔離開發環境與依賴

用 requirements.txt 管理套件清單

🔧 基本操作整理

指令/動作	說明
python3 -m venv venv	建立虛擬環境
source venv/bin/activate	啟用虛擬環境
deactivate	離開虛擬環境
pip install requests	安裝 requests 套件
pip freeze > requirements.txt	輸出目前套件到 requirements.txt
pip install -r requirements.txt	根據清單安裝套件
🧪 任務：建立並測試虛擬環境

📁 本模組檔案位於：`python_module/README.md`

可搭配虛擬環境與 pip 套件進行練習與版本管理。

