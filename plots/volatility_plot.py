import matplotlib.pyplot as plt

def volatility_plot(df):
    plt.figure(figsize=(12,6))
    plt.plot(df["Date"], df["volatility"])
    plt.title("Volatility")
    plt.show()