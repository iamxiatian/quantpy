#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import numpy as np
import pandas as pd
from matplotlib import pyplot 


#filename = '/home/xiatian/workspace/quantpy/data/AAPL_GOOGL_IBM_20140101_20141201.xls'
#d = pd.read_excel(filename, sheetname=None)



def main():
    basepath = os.path.dirname(__file__)
    sys.path.append(os.path.join(basepath, ''))
    csv_file = '/home/xiatian/workspace/quantpy/data/AAPL_20140101_20141201.csv'
    df = pd.read_csv(csv_file)
    series = pd.Series.rolling(df['Close'], window=5).mean() 
    series.plot()
    pyplot.show()

if __name__ == '__main__':
    main()
