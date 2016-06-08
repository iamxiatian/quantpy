#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import numpy as np
import pandas as pd


def main():
    basepath = os.path.dirname(__file__)
    sys.path.append(os.path.join(basepath, ''))
    filename = '/home/xiatian/workspace/quantpy/data/AAPL_GOOGL_IBM_20140101_20141201.xls'
    # filename = os.path.join(basepath, "..", "data", "AAPL_GOOGL_IBM_20140101_20141201.xls")

    d = pd.read_excel(filename, sheetname=None)
    print(d)

if __name__ == '__main__':
    main()
