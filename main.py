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
import indicators.MACD_code as MACD_code
import plots.macd_plot as mp
from datetime import datetime,timedelta,date
import plots.volatility_plot as vp
import features.target as target
from ml.train import train_model_random_forest,train_model_linear_regression
import sys
print(sys.executable)
print(sys.path)

today = date.today()
yesterday = today - timedelta(days=1)
company = dd.data('KRU.WA','2016-01-01',yesterday,'1d') 
#print(company)
#company =  company[['Date','Close']]
company = company.reset_index()
#company.columns = [col[0] if isinstance(col, tuple) else col for col in company.columns]
company =  company[['Date','Close']]
#tickers = company.columns.levels[1][0]
#print(tickers)
#print(company)    

#wykres 
plots = lineplot.plots(company)
plt.title("Price plot")
plt.show()


#SMA (simple moving average)
company  = SMA_code.SMA(company,50)
#print(company)

company  = SMA_code.SMA(company,200)
#print(company )

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

#print(company[company["signal"] != 0][
#   ["Date","Close","SMA_50","SMA_200","signal"]
#])

#rysujemy to na wykresie (dla Apple nie ma ale dla innych spółek może już być)
gp.gpp(company)
plt.show()


#EMA dla 60 dni 
company = EMA_code.EMA(company,50)
company = EMA_code.EMA(company,200)
#print (company)

#RSI
company = RSI_code.RSI(company, 14)
#print(company[["Date","Close","RSI_14"]])

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

#print(company) 

fig, (ax1, ax2) = plt.subplots(2,1, figsize=(12,8), sharex=True)
# wykres ceny
ax1.plot(company["Date"], company["Close"])
ax1.set_title("Price")
# wykres RSI
ax2.plot(company["Date"], company["RSI_14"])
ax2.axhline(70, color = "red")
ax2.axhline(50, color = "yellow")
ax2.axhline(30, color = "green")
ax2.set_title("RSI")

plt.show()
#wykres wskaźnika MACD
company = MACD_code.MACD(company,12,26,9)
#print(company)

mp.plot_macd(company)

#dodaję returns jako zwrot
company['returns'] = company['Close'].pct_change()

#dodaję zmienność
company['volatility'] = company['returns'].rolling(20).std()
#print(company)

vp.volatility_plot(company) 
#print(company.info())
for lag in [1, 2, 3, 5]:
    company[f"returns_lag_{lag}"] = company["returns"].shift(lag)
#dodajemy target
company = target.add_target(company, 5)

#czyścimy dane by model mógł lepiej działać
company = company.dropna()
print(company)
#print(company.isna().sum())

#pierwsze ML

#lista cech


features = [
    "SMA_50",
    "SMA_200",
    "EMA_50",
    "RSI_14",
    "MACD",
    "MACD_signal",
    "MACD_hist",
    "returns",
    "volatility"
]
#X = macierz cech
X = company[features]

# y = target
y = company["target"]
split_date = "2024-01-01"

X_train = X[company["Date"] < split_date]
X_test  = X[company["Date"] >= split_date]

y_train = y[company["Date"] < split_date]
y_test  = y[company["Date"] >= split_date]

print("Train shape:", X_train.shape)
print("Test shape:", X_test.shape)
print("Train target distribution:\n", y_train.value_counts())
print("Test target distribution:\n", y_test.value_counts())

model_random_forest = train_model_random_forest(X_train, y_train, X_test, y_test)
model_linear_regression = train_model_linear_regression(X_train, y_train,X_test)
