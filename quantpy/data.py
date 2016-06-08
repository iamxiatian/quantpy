#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from mongoengine import *
import sys
import os
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from domain import story_history_by_day
from orm import mongodb_connect

'''
股票数据读写模块
'''

def read(code,days = 180):
    if code is None or code == '':
        return
    '''
	读取指定股票代码下的基本数据，返回dataframe，没一行数据包括：日期(date)、开盘价(open)、收盘价(close)、最高价(high)、最低价(low)、量(volume)
	'''
    mongodb_connect.get_mongodb_connection()
    sh=story_history_by_day.StockHistoryByDay.objects(code=code)
    shList=[]
    for i in sh:
        shList.append(i.to_mongo())
    return pd.DataFrame(shList)



if __name__ == '__main__':
    print(read('300425'))
