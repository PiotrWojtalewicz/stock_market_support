import matplotlib.pyplot as plt

def volatility_plot(df):
    plt.figure(figsize=(12,6))
    plt.plot(df["Date"], df["volatility"])
    plt.title("Volatility",fontsize = 16,loc ='center',fontweight="bold")
    plt.grid(True,linestyle = '--',alpha = 0.6)
    plt.show()