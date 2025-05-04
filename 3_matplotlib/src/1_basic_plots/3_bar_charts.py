import matplotlib.pyplot as plt
import numpy as np

# Example 1: Vertical Bar Chart
def vertical_bar_chart():
    categories = ['A', 'B', 'C', 'D']
    values = [4, 7, 1, 8]

    plt.bar(categories, values)
    plt.title('Vertical Bar Chart Example')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.show()

# Example 2: Horizontal Bar Chart
def horizontal_bar_chart():
    categories = ['A', 'B', 'C', 'D']
    values = [4, 7, 1, 8]

    plt.barh(categories, values)
    plt.title('Horizontal Bar Chart Example')
    plt.xlabel('Values')
    plt.ylabel('Categories')
    plt.show()

# Example 3: Customized Bar Chart
def customized_bar_chart():
    categories = ['A', 'B', 'C', 'D']
    values = [4, 7, 1, 8]
    colors = ['red', 'blue', 'green', 'orange']

    plt.bar(categories, values, color=colors, edgecolor='black')
    plt.title('Customized Bar Chart Example')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.show()

if __name__ == "__main__":
    vertical_bar_chart()
    horizontal_bar_chart()
    customized_bar_chart()