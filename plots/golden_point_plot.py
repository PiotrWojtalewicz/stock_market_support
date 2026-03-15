import pandas as pd 
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import download_data as dd


plt.figure(figsize=(12,6))

def gpp (df):
    plt.plot(df["Close"], label = "Price")
    plt.plot(df.iloc[:,2], label = df.columns[2])
    plt.plot(df.iloc[:,3], label = df.columns[3])

    golden = df[df["signal"] == 1]
    death = df[df["signal"] == -1]
    plt.scatter(golden.index, golden.iloc[:,2], marker="^", label="Golden cross")
    plt.scatter(death.index, death.iloc[:,2], marker="v", label="Death cross")
    plt.legend()
    return
