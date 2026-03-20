

def add_target(df,days):
    df["future_return"] = df["Close"].shift(-days)/df["Close"] -1
    df["target"] = (df["future_return"] > 0).astype(int)

    return df
 