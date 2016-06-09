# coding: utf-8

'''股票的常用指标分析'''

from quantpy import ta
from quantpy import mongoclient


class Stock(object):
    '''
    单只股票的指标分析
    '''

    def __init__(self, code='300425', days=180):
        self.code = code
        self.days = days
        mongo_data = mongoclient.MongoData()
        self.df = mongo_data.read(self.code, days)

    def MA(self, window=5):
        '''
        计算均线，默认为5日线，即window＝5, 返回df
        '''
        series_data = ta.MA(self.df['Close'], window)
        self.df['MA_' + str(window)] = series_data
        return df


if __name__ == '__main__':
    stock = Stock()
    df = stock.MA(5)
    print(df)
