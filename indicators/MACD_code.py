import pandas as pd 
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import download_data as dd

def MACD(df,fast,slow,signal):
    df["EMA_fast"] = df["Close"].ewm(span = fast).mean()
    df["EMA_slow"] = df["Close"].ewm(span = slow).mean()

    df["MACD"] = df["EMA_fast"] - df["EMA_slow"]  

    df["MACD_signal"] = df["MACD"].ewm(span = signal).mean()
    df["MACD_hist"] = df["MACD"] - df["MACD_signal"]

    return df    