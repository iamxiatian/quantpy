from mongoengine import *

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
