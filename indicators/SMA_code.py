import pandas as pd 
import numpy as np



 #Simple moving average
#def SMA(df,day):
    # obliczamy 60-dniową średnią kroczącą
  #  df[f"SMA_{day}"] = df["Close"].rolling(day).mean()
 #   return df

def add_sma(df, period):
   
    df = df.copy()

    if len(df) < period:
        print(f"Błąd: Za mało danych, by policzyć SMA_{period}")
        df[f"SMA_{period}"] = np.nan 
        return df

    # 3. Obliczamy średnią
    # Używamy .iloc, żeby mieć pewność, że pracujemy na wartościach
    df[f"SMA_{period}"] = df["Close"].rolling(window=period).mean()
    
    return df