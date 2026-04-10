import pandas as pd 
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import download_data as dd


plt.figure(figsize=(12,6))

def gpp (df):
    plt.plot(df["Close"], label = "Price")
    plt.plot(df.iloc[:,3], label = df.columns[3])
    plt.plot(df.iloc[:,4], label = df.columns[4])

    golden = df[df["signal"] == 1]
    death = df[df["signal"] == -1]
    plt.scatter(golden.index, golden.iloc[:,3], marker="^",color = 'gold',edgecolors='black',label="Golden cross")
    plt.scatter(death.index, death.iloc[:,3], marker="v",color= 'red',edgecolors = 'darkred' ,label="Death cross", )
    plt.grid(True,linestyle = '--',alpha = 0.6)
    plt.legend()
    return
