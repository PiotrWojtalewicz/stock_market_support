import pandas as pd 
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import download_data as dd

def volume_shock (df,period):
    colume_col = df['Volume']
    return colume_col/colume_col.rolling(window = period).mean()