import pandas as pd 
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import download_data as dd


#Exponential Moving Average
# Kupno, gdy cena jest powyżej EMA; sprzedaż, gdy poniżej.
def EMA(df,window):
    column_name = f"Ema_{window}"
    df[column_name] = df["Close"].ewm(span=window, adjust = "False").mean()
    return df