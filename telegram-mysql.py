#!/usr/bin/python
# -*- coding: utf8 -*-

import sys
import time
import datetime
import telepot
import uniout
import MySQLdb
from ConfigParser import SafeConfigParser

def handle(msg):
    #pprint.pprint(msg[from'])
    chat_id = msg['chat']['id']
    command = msg['text']
    user_id = msg['from']['id']
    username = msg['from']['first_name']
    fullname = msg['from']['last_name']+msg['from']['first_name']

    b = (u'你的Telegram ID是：' + str(user_id))
    h = ( '嗨' + str(username.encode('utf-8')) + '主人')
    why =('為什麼要用Telegram?!')
    content = str(username.encode('utf-8'))+'說：'+str(command.encode('utf-8'))
    f = open('log.txt', 'a')
    f.write(content+'\n')

    print content
    f.close()

    if command == '/talk':
        bot.sendMessage(chat_id, '主人先看看指令吧？')
    else:
        reps_content = query(command)
        bot.sendMessage(chat_id, reps_content)

def query(requ):
    cursor = db.cursor()
    sql = "SELECT * FROM resp \
       WHERE requ = '" + str(requ.encode('utf-8')) +"'"
    try:
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()

        if len(results)>0:
            output = ''
            for row in results:
               row_id = row[0]
               row_requ = row[1]
               row_reps = row[2]

               # Now print fetched result
               output = output+row_reps
        else: 
            output = '就是這樣，喵～'
    except:
        output = '程式出錯'


    return output

# 取得設定檔資訊
parser = SafeConfigParser()
parser.read('config.txt')
telepot_token = parser.get('apitoken', 'token')
db_host = parser.get('db', 'host')
db_uid = parser.get('db', 'user')
db_pass = parser.get('db', 'password')
db_name = parser.get('db', 'dbname')

# 連接MySQL資料庫
db = MySQLdb.connect(db_host, db_uid, db_pass, db_name, charset='utf8', init_command='SET NAMES UTF8')

bot = telepot.Bot(telepot_token)
bot.notifyOnMessage(handle)
print '監聽中 ...'

while 1:
    time.sleep(10)
