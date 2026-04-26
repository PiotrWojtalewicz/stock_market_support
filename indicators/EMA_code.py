


#Exponential Moving Average
# Kupno, gdy cena jest powyżej EMA; sprzedaż, gdy poniżej.
def EMA(df,window):
    column_name = f"EMA_{window}"
    df[column_name] = df["Close"].ewm(span=window, adjust = "False").mean()
    return df