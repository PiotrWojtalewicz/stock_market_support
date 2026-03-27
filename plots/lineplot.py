import pandas as pd 
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import download_data as dd


def plots(df):
   df = df.reset_index()
   ypoints = df['Close']
   xpoints = df['Date']
   plt.plot(xpoints,ypoints)
   plt.grid(True,linestyle = '--',alpha = 0.6)
   plt.scatter(df.loc[df["Close"].idxmax(), "Date"],
           df["Close"].max(),
           color="green", label="Max")
   return df

