import seaborn as sns
import matplotlib.pyplot as plt

def correlation_heatmap(df) :
    plt.figure(figsize = (12,10))
    sns.heatmap(df,annot = True,cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title("Heatmapa korelacji cech giełdowych")
    plt.show()
    return 