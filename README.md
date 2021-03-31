[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/Naereen/)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-367/)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)



## 🛠 Developer 開發者

<img src="https://upload.cc/i1/2019/11/19/9kz7Yw.gif" width=150> 　　　　<img src="https://upload.cc/i1/2019/11/19/WwHIZS.gif" width=114.5>

**Proladon #7525**　　　　　 　[![discord](https://lihi1.cc/7CBE7)](https://lihi1.cc/j2C5r)

## ⚡ Introduction 簡介

### **Discord Python Bot BackBone**

**Discord Pyhon Bot 骨架**

整體架構是參考並簡化改進先前於 Discord Hack Week 19 共同開發的 [Libereus](https://github.com/Tansc161/Libereus)

旨在提供一個乾淨的基本骨架，快速的開始一隻新的機器人開發

- For (初學者/開發者)
- Cog 架構
- Bot指令/類別/功能 分離
- Error Handler 、 Logger 、 Gloable Function 、 Checker

<br>

## 📥 Installation 安裝指南
> 運行環境 建議 `Python 3.6` 以上 / `discord.py 1.5` 以上

1. 下載整個專案  
2.  解壓後將 `example_setting.json` 重新命名為 `setting.json` ; 自行修改設定檔裡的資料  
3. 運行 `bot.py` 即可

<br>

## 🔩 Folder structure 資料夾結構
```
/ # 根目錄
------------------------------------
- bot.py # bot 啟動主文件
- example_setting.json # 設定檔


/cmds # 放置所有 Cog 指令
------------------------------------
- main.py  #主要指令區
- event.py # 所有 event 觸發性事件指令區
- mod.py # 管理、控制類指令區
- owner.py # 擁有者權限指令區


/core  #放置類別、核心通用功能
------------------------------------
- classes.py # 主要類別區
- check.py # 自定全域指令檢查器
- error.py # 預設、自訂 錯誤管理器
```
