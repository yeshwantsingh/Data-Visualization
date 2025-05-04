import seaborn as sns
import matplotlib.pyplot as plt

# Example 1: Basic Bar Plot
def basic_bar_plot():
    data = {'Category': ['A', 'B', 'C', 'D'],
            'Values': [4, 7, 1, 8]}
    sns.barplot(x='Category', y='Values', data=data)
    plt.title('Basic Bar Plot')
    plt.show()

# Example 2: Horizontal Bar Plot
def horizontal_bar_plot():
    data = {'Category': ['A', 'B', 'C', 'D'],
            'Values': [4, 7, 1, 8]}
    sns.barplot(x='Values', y='Category', data=data)
    plt.title('Horizontal Bar Plot')
    plt.show()

# Example 3: Bar Plot with Error Bars
def bar_plot_with_error_bars():
    data = {'Category': ['A', 'B', 'C', 'D'],
            'Values': [4, 7, 1, 8],
            'Errors': [[0.5, 0.7, 0.2, 0.6]]}
    sns.barplot(x='Category', y='Values', data=data, yerr=data['Errors'])
    plt.title('Bar Plot with Error Bars')
    plt.show()

# Example 4: Stacked Bar Plot (using pandas)
def stacked_bar_plot():
    import pandas as pd
    data = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D'],
        'Group1': [4, 7, 1, 8],
        'Group2': [2, 3, 5, 1]
    })
    data.set_index('Category').plot(kind='bar', stacked=True)
    plt.title('Stacked Bar Plot')
    plt.ylabel('Values')
    plt.show()

if __name__ == "__main__":
    # basic_bar_plot()
    # horizontal_bar_plot()
    # bar_plot_with_error_bars()
    stacked_bar_plot()