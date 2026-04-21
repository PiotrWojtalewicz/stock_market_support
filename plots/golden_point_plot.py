import pandas as pd 
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import download_data as dd


plt.figure(figsize=(12,6))

def gpp (df):
    plt.plot(df["Close"], label = "Price")
    plt.plot(df.iloc[:,5], label = df.columns[5])
    plt.plot(df.iloc[:,6], label = df.columns[6])

    golden = df[df["signal"] == 1]
    death = df[df["signal"] == -1]
    plt.scatter(golden.index, golden.iloc[:,5], marker="^",color = 'gold',edgecolors='black',label="Golden cross")
    plt.scatter(death.index, death.iloc[:,5], marker="v",color= 'red',edgecolors = 'darkred' ,label="Death cross", )
    plt.grid(True,linestyle = '--',alpha = 0.6)
    plt.legend()
    return
