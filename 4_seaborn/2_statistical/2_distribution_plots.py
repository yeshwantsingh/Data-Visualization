import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Example 1: Distribution Plot with Histogram and KDE
def distribution_plot_example_1():
    data = np.random.normal(size=1000)
    sns.histplot(data, kde=True)
    plt.title('Distribution Plot with Histogram and KDE')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()

# Example 2: Distribution Plot with Multiple Distributions
def distribution_plot_example_2():
    data1 = np.random.normal(loc=0, scale=1, size=1000)
    data2 = np.random.normal(loc=2, scale=1.5, size=1000)
    sns.histplot(data1, kde=True, color='blue', label='Data 1', stat='density', alpha=0.5)
    sns.histplot(data2, kde=True, color='orange', label='Data 2', stat='density', alpha=0.5)
    plt.title('Distribution Plot with Multiple Distributions')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.legend()
    plt.show()

# Example 3: Customizing the Distribution Plot
def distribution_plot_example_3():
    data = np.random.normal(size=1000)
    sns.histplot(data, kde=True, color='green', bins=30, alpha=0.6)
    plt.title('Customized Distribution Plot')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

# Run examples
if __name__ == "__main__":
    distribution_plot_example_1()
    # distribution_plot_example_2()
    # distribution_plot_example_3()