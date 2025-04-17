🐚 Bash Module

這是學習 Bash 與指令操作的模組。

將透過任務與筆記熟悉常用指令、檔案系統操作與指令練習。

# 🐚 Bash Module



這個模組專注於學習 Linux 終端機操作與 Bash 指令。  

從最基本的目錄操作到腳本撰寫，逐步強化命令列技能。



---



## 📌 基礎任務一：檔案與資料夾操作



| 任務編號 | 主題             | 指令範例                       | 狀態 |

|----------|------------------|--------------------------------|------|

| 1        | 查看目前位置     | `pwd`                          | ⬜️   |

| 2        | 查看資料夾內容   | `ls -l`、`ls -a`               | ⬜️   |

| 3        | 切換目錄         | `cd ~/Downloads`              | ⬜️   |

| 4        | 建立資料夾       | `mkdir my_folder`             | ⬜️   |

| 5        | 建立檔案         | `touch note.txt`              | ⬜️   |

| 6        | 移動檔案         | `mv note.txt my_folder/`      | ⬜️   |

| 7        | 刪除檔案與資料夾 | `rm note.txt`、`rm -r my_folder/` | ⬜️   |



✅ 完成後可以在表格旁邊打勾、加筆記或錯誤紀錄。



---



## 🧠 小挑戰（選擇題）



1. 哪個指令能建立一個空白檔案？

   - A. `c`  

   - B. `touch`  

   - C. `ls


2. 要回到上一層資料夾可以用哪個指令？

   - A. `cd ..`  

   - B. `ls -a`  

   - C. `pwd`


## 📂 目錄操作練習：Linux 檔案導航迷宮

🧩 迷宮第一關：
🎯 任務目標：為了練習 cd、mkdir、pwd、mv 等基礎指令，建立以下資料夾結構並完成任務。
🏗️ 建立資料夾結構：
mkdir -p dungeon/level1/level2/treasure
🚶 進入最深層資料夾：
cd dungeon/level1/level2/treasure
🪙 建立寶藏檔案：
echo "GOLD" > gold.txt
📍 確認目前位置：
pwd
🔙 回到根目錄（cs-adventure）：
cd ../../../..
📦 移動 gold.txt 到根目錄：
mv dungeon/level1/level2/treasure/gold.txt .

🧩 迷宮第二關：任務「拯救 README」
🎯 任務目標：
拯救一份錯放在深層資料夾中的備份檔 readme_backup.md，將它移動並重新命名為 bash_module/README.md。

📁 操作流程筆記：
1️⃣ 建立錯綜的資料夾結構：
mkdir -p labyrinth/zoneA/zoneB/zoneC
2️⃣ 建立被困的檔案：
echo "I am the lost README..." > labyrinth/zoneA/zoneB/zoneC/readme_backup.md
3️⃣ 檢查檔案內:
cat labyrinth/zoneA/zoneB/zoneC/readme_backup.md
4️⃣ 回到專案根目錄：
cd ~/cs-adventure
5️⃣ 複製檔案並重新命名：
cp labyrinth/zoneA/zoneB/zoneC/readme_backup.md bash_module/README.md
6️⃣ （可選）刪除原始檔案模擬「救出」：
rm labyrinth/zoneA/zoneB/zoneC/readme_backup.md
