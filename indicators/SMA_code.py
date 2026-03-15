import pandas as pd 
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import download_data as dd



 
def SMA(df,day):
    # obliczamy 60-dniową średnią kroczącą
    df[f"SMA_{day}"] = df["Close"].rolling(day).mean()
    return df

