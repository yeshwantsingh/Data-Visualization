import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load example dataset
iris = sns.load_dataset("iris")

# Create pair plot
def create_pair_plot():
    sns.pairplot(iris, hue='species', markers=["o", "s", "D"])
    plt.title("Pair Plot of Iris Dataset")
    plt.show()

if __name__ == "__main__":
    create_pair_plot()