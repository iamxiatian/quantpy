# coding: utf-8

import pandas as pd
import numpy as np

from mongoengine import connect
from mongoengine import Document
from mongoengine import DateTimeField, DecimalField, LongField, StringField

MONGODB_DB_NAME = 'stock'
MONGODB_USER_NAME = 'stock_admin'
MONGODB_PASSWORD = 'SstIq4r80iHMK7Xd'
MONGODB_HOST = '202.112.114.3'
MONGODB_PORT = 27017


class MongoData():
    def __init__(self):
        connect(MONGODB_DB_NAME, host=MONGODB_HOST, port=MONGODB_PORT,
                username=MONGODB_USER_NAME, password=MONGODB_PASSWORD)

    def read(self, code, days=180):
        '''
        读取指定股票代码下的基本数据，返回dataframe，没一行数据包括：日期(date)、
        开盘价(open)、收盘价(close)、最高价(high)、最低价(low)、量(volume)
        '''
        if code is None or code == '':
            return
        shList = []
        columns = ['Code', 'Date', 'Open', 'Close', 'High', 'Low', 'Volume']
        for stock in StockHistoryByDay.objects(code=code):
            shList.append([stock.code,
                           stock.date,
                           stock.open,
                           np.float(stock.close),
                           np.float(stock.high),
                           np.float(stock.low),
                           np.int64(stock.volume)])
        df = pd.DataFrame(shList, columns=columns)
        return df


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


if __name__ == '__main__':
    mongo_data = MongoData()
    df = mongo_data.read(code='300425')
    print(df)