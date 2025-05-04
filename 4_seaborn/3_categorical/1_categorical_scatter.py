import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
tips = sns.load_dataset("tips")

# Scatter plot with categorical variables
def scatter_plot_with_categorical():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day", style="time", size="size", sizes=(20, 200))
    plt.title("Scatter Plot of Total Bill vs Tip with Categorical Variables")
    plt.xlabel("Total Bill")
    plt.ylabel("Tip")
    plt.legend(title="Day/Time")
    plt.show()

if __name__ == "__main__":
    scatter_plot_with_categorical()