import pandas as pd 
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import download_data as dd
import indicators.SMA_code as SMA_code 
import plots.lineplot as lineplot
import plots.golden_point_plot as gp


company = dd.data('AAPL','2014-01-01','2025-12-31','1d') 
print(company)
#company =  company[['Date','Close']]
company = company.reset_index()
company =  company[['Date','Close']]
#tickers = company.columns.levels[1][0]
#print(tickers)
print(company)    

#wykres 
plots = lineplot.plots(company)
plt.title("Price plot")
plt.show()

#SMA (simple moving average)
company  = SMA_code.SMA(company,50)
print(company)

company  = SMA_code.SMA(company,200)
print(company )

# death/golden cross - moment przecięcia SMA50 vs SMA200
company["signal"] = 0

# golden cross
company.loc[
    (company["SMA_50"] > company["SMA_200"]) &
    (company["SMA_50"].shift(1) <= company["SMA_200"].shift(1)),
    "signal"
] = 1

# death cross
company.loc[
    (company["SMA_50"] < company["SMA_200"]) &
    (company["SMA_50"].shift(1) >= company["SMA_200"].shift(1)),
    "signal"
] = -1

print(company[company["signal"] != 0][
    ["Date","Close","SMA_50","SMA_200","signal"]
])

#rysujemy to na wykresie (dla Apple nie ma ale dla innych spółek może już być)
gp.gpp(company)
plt.show()
