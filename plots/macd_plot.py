import matplotlib.pyplot as plt

def plot_macd(df):

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12,8), sharex=True)

    # wykres ceny
    ax1.plot(df["Date"], df["Close"])
    ax1.set_title("Price")

    # MACD
    ax2.plot(df["Date"], df["MACD"], label="MACD")
    ax2.plot(df["Date"], df["MACD_signal"], label="Signal")

    # histogram
    colors = ["green" if val >= 0 else "red" for val in df["MACD_hist"]]
    ax2.bar(df["Date"], df["MACD_hist"], color=colors)

    ax2.set_title("MACD")
    ax2.legend()

    plt.show()