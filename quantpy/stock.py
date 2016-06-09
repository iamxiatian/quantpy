# coding: utf-8

'''股票的常用指标分析'''

from quantpy import ta
from quantpy import mongoclient
import pandas as pd


class Stock(object):
    '''
    单只股票的指标分析
    '''

    def __init__(self, code='300425', days=180):
        self.code = code
        self.days = days
        mongo_data = mongoclient.MongoData()
        self.df = mongo_data.read(self.code, days)

    def get_frame(self):
        return self.df
        
    def MA(self, window=5):
        '''
        计算均线，默认为5日线，即window＝5, 返回df
        '''
        self.df['MA_' + str(window)] = ta.MA(self.df['Close'], window)
        return self

    def EMA(self, window=5):
        '''
        计算指数平滑移动均线，默认为5日线，返回df
        '''
        self.df['EMA_' + str(window)] = ta.EMA(self.df['Close'], window)
        return self

    def MACD(self):
        DIF, DEA, MACD = ta.MACD(self.df['Close'])
        self.df['MACD_DIF'] = DIF
        self.df['MACD_DEA'] = DEA
        self.df['MACD'] = MACD
        return self

    def macd_cross(self):
        '''
        找出所有的金叉, 返回金叉的日期、类型、当时的MACD信息
        http://stockcharts.com/school/doku.php?id=chart_school:technical_indicators:moving_average_convergence_divergence_macd
        '''
        if('MACD' not in self.df.columns):
            self.MACD()
            
        for stock in self.df:
            pass
        crosses = []
        return crosses

        
if __name__ == '__main__':
    stock = Stock()
    df = stock.MA(5).EMA(5).MACD().get_frame()
    print(df[['Date', 'Close', 'MA_5', 'MACD_DIF', 'MACD_DEA', 'MACD']])
