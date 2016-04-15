python-mysql2telegrem-bot
===

# 環境安裝

	pip install telepot
	pip install uniout
	pip install MySQL-python
	
# 資料庫匯入
請將內附的`telepot.sql`檔案匯入進MySQL資料庫以後，在`resp`建立所需要的內容。

#啟動機器人

啟動從資料庫取得該回應內容的機器人

	python telegram-mysql.py