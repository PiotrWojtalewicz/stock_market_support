import pandas as pd 
import numpy as np


def volume_shock (df,period):
    colume_col = df['Volume']
    return colume_col/colume_col.rolling(window = period).mean()