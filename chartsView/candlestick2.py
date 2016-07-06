import plotly.plotly as py
from plotly.tools import FigureFactory as FF
from plotly.graph_objs import *
from quantpy.stock import Stock

"""
基于plotly实现k线
"""

py.sign_in('zhongkai', 'zhbqhgis5n')
# Create Candlestick
stock = Stock()
df = stock.get_frame()
df = df[:50]
fig = FF.create_candlestick(df.Open, df.High, df.Low, df.Close, dates=df.Date)

# Create Line of open values
add_line = Scatter(
    x=df.Date,
    y=df.Open,
    name='Open Vals',
    line=Line(color='black')
    )

fig['data'].extend([add_line])
py.iplot(fig, filename='candlestick_and_trace', validate=False)