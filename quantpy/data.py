#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
# from ..orm import mongodb_connect
# from ..domain import story_history_by_day
import sys,pprint
from mongoengine import *

MONGODB_DB_NAME='stock'
MONGODB_USER_NAME='stock_admin'
MONGODB_PASSWORD='SstIq4r80iHMK7Xd'
MONGODB_HOST='202.112.114.3'
MONGODB_PORT=27017


def get_mongodb_connection():
    connect(MONGODB_DB_NAME,host=MONGODB_HOST, port=MONGODB_PORT, username=MONGODB_USER_NAME, password=MONGODB_PASSWORD)


class StockHistoryByDay(Document):
    # 交易日期
    date = DateTimeField(max_length=200, required=True)
    # 开盘价
    open = DecimalField(max_length=200, required=False)
    # 最高价
    high = DecimalField(max_length=200, required=False)
    # 最低价
    low = DecimalField(max_length=200, required=False)
    # 收盘价
    close = DecimalField(max_length=200, required=False)
    # 成交量
    volume = LongField(max_length=200, required=False)
    # 成交金额
    amount = LongField(max_length=200, required=False)
    name = StringField(max_length=200, required=False)
    code = StringField(max_length=200, required=True)



'''
股票数据读写模块
'''

def read(code,days = 180):
    if code is None or code == '':
        return
    '''
	读取指定股票代码下的基本数据，返回dataframe，没一行数据包括：日期(date)、开盘价(open)、收盘价(close)、最高价(high)、最低价(low)、量(volume)
	'''
    get_mongodb_connection()
    sh=StockHistoryByDay.objects(code=code)
    shList=[]
    for i in sh:
        shList.append(i.to_mongo())
    return pd.DataFrame(shList)



if __name__ == '__main__':

    print(read('300425'))
