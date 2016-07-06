from math import pi
import pandas as pd
import datetime

from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, Range1d, LinearAxis, ColumnDataSource, Line

from quantpy.stock import Stock

"""
基于bokeh实现k线
"""

def create_data_source(data_frame):
    '''
    Reference here: https://github.com/bokeh/bokeh/issues/1239
    '''
    return ColumnDataSource(
        data=dict(
            Date=[x.strftime("%Y-%m-%d") for x in data_frame['Date']],
            Open=data_frame['Open'],
            Close=data_frame['Close'],
            High=data_frame['High'],
            Low=data_frame['Low'],
            Volume=data_frame['Volume']
        )
    )

stock = Stock()
df = stock.get_frame()
df = df[:50]
# df["Date"] = pd.to_datetime(df["Date"])

# tip坐标说明
ht = HoverTool(
    tooltips=[
            ("Date", "@Date"),
            ("Open", "@Open"),
            ("Close", "@Close"),
            ("High", "@High"),
            ("Low", "@Low"),
            ("Volume", "@Volume")
        ]
    )

# 判断盈亏
inc = df.Close > df.Open
dec = df.Open > df.Close

# 时间间隔
w = 12*60*60*1000  # half day in ms

# 工具栏
TOOLS = [ht, "pan,wheel_zoom,box_zoom,reset,save"]

# 蜡烛图
mids = (df.Open + df.Close)/2
spans = abs(df.Close-df.Open)

# 获取y轴左边的坐标数值
max_px = max(df['High'])
min_px = min(df['Low'])
px_range = max_px - min_px
primary_y_range = (min_px - px_range / 2.0, max_px + px_range * 0.1)

p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1200, toolbar_location="left", y_range=primary_y_range)

p.title = "Candlestick"
p.xaxis.major_label_orientation = pi/4
p.grid.grid_line_alpha = 0.3

px_rect_inc_src = create_data_source(df[inc])
px_rect_dec_src = create_data_source(df[dec])

# 绘制蜡烛图
p.segment(df.Date, df.High, df.Date, df.Low, color="black")
p.rect(df.Date[inc], mids[inc], w, spans[inc], fill_color="#D5E1DD",
       line_color="black", source=px_rect_inc_src)
p.rect(df.Date[dec], mids[dec], w, spans[dec], fill_color="#F2583E",
       line_color="black", source=px_rect_dec_src)

# ---------------辅助线---------------
line_x = ['2015-03-12', '2015-03-24']
line_y = [21.0, 27.0]
# 任意画线还没实现--!
p.line(df.Date, df.Open, legend="Open", line_color="grey", line_width=1)

# ---------------柱状图---------------
# 计算成交量
vol_mids = df.Volume / 2.0
vol_spans = df.Volume
max_vol = max(df.Volume)

# 添加y轴右边坐标
p.extra_y_ranges = {"Volume": Range1d(start=0, end=max_vol * 5)}
p.add_layout(LinearAxis(y_range_name="Volume"), 'right')

# 绘制柱状图
p.rect(df.Date[inc], vol_mids[inc], w, vol_spans[inc], fill_color="#D5E1DD", color="#D5E1DD",
       y_range_name="Volume")
p.rect(df.Date[dec], vol_mids[dec], w, vol_spans[dec], fill_color="#F2583E", color="#F2583E",
       y_range_name="Volume")
# ---------------柱状图---------------

output_file("candlestick.html", title="candlestick example")

show(p)  # open a browser
