import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Example 1: Basic Scatter Plot
def basic_scatter_plot():
    # Create a simple dataset
    data = pd.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [2, 3, 5, 7, 11]
    })
    
    # Create a scatter plot
    sns.scatterplot(data=data, x='x', y='y')
    plt.title('Basic Scatter Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

# Example 2: Scatter Plot with Hue
def scatter_plot_with_hue():
    # Load the tips dataset
    tips = sns.load_dataset('tips')
    
    # Create a scatter plot with hue
    sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day')
    plt.title('Scatter Plot with Hue')
    plt.xlabel('Total Bill')
    plt.ylabel('Tip')
    plt.show()

# Example 3: Scatter Plot with Size
def scatter_plot_with_size():
    # Load the tips dataset
    tips = sns.load_dataset('tips')
    
    # Create a scatter plot with size
    sns.scatterplot(data=tips, x='total_bill', y='tip', size='size', hue='day', sizes=(20, 200))
    plt.title('Scatter Plot with Size')
    plt.xlabel('Total Bill')
    plt.ylabel('Tip')
    plt.show()

# Example 4: Scatter Plot with Regression Line
def scatter_plot_with_regression():
    # Load the tips dataset
    tips = sns.load_dataset('tips')
    
    # Create a scatter plot with a regression line
    sns.regplot(data=tips, x='total_bill', y='tip')
    plt.title('Scatter Plot with Regression Line')
    plt.xlabel('Total Bill')
    plt.ylabel('Tip')
    plt.show()

if __name__ == "__main__":
    # basic_scatter_plot()
    # scatter_plot_with_hue()
    # scatter_plot_with_size()
    scatter_plot_with_regression()