import pandas as pd 
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import download_data as dd
import indicators.SMA_code as SMA_code 
import plots.lineplot as lineplot
import plots.golden_point_plot as gp
import indicators.EMA_code as EMA_code
import indicators.RSI_code as RSI_code

company = dd.data('AAPL','2014-01-01','2026-03-14','1d') 
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


#EMA dla 60 dni 
company = EMA_code.EMA(company,50)
company = EMA_code.EMA(company,200)
print (company)

#RSI
company = RSI_code.RSI(company, 14)
print(company[["Date","Close","RSI_14"]])

# RSI interpretation
company["RSI_interpretation"] = np.nan
for i, rsi_value in enumerate(company["RSI_14"]):
    if rsi_value >= 70:
        company.loc[i, "RSI_interpretation"] = "overbought"
    elif 50 <= rsi_value < 70:
        company.loc[i, "RSI_interpretation"] = "growing momentum"
    elif 30 <= rsi_value < 50:
        company.loc[i, "RSI_interpretation"] = "lowing momentum"
    else:
        company.loc[i, "RSI_interpretation"] = "oversold"

print(company)