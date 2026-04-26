

def candle_body_strength(df):
    df = (df['Close'] - df['Low'])/(df['High'] - df['Low'])
    return df