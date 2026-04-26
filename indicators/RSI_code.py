
#Relative Strength Index

def RSI(df, period):
    delta = df["Close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()

    RS = avg_gain / avg_loss
    RSI = 100 - (100 / (1 + RS))
    df[f"RSI_{period}"] = RSI
    return df
        

