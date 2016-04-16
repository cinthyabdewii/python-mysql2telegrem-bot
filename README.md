python-mysql2telegrem-bot
===

# 環境安裝

	pip install telepot
	pip install uniout
	pip install MySQL-python
	
# 資料庫匯入
請將內附的`telepot.sql`檔案匯入進MySQL資料庫以後，在`resp`建立所需要的內容。

# 設定檔案
請將`config.sample.txt`檔複製為`config.txt`，並依照實際情況更改參數內容

#啟動機器人

啟動從資料庫取得該回應內容的機器人

	python telegram-mysql.py
	
啟動測試用機器人

	python telegram\ check\ system.py