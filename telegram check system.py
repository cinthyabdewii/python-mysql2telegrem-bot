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
    f = open('Lchat.txt', 'a')
    f.write(content+'\n')

    print content
    f.close()

    if command == '/talk':
        bot.sendMessage(chat_id, '主人先看看指令吧？')

bot = telepot.Bot(token)
bot.notifyOnMessage(handle)
print '監聽中 ...'

while 1:
    time.sleep(10)
