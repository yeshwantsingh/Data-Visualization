import matplotlib.pyplot as plt

# Example 1: Basic Scatter Plot
def basic_scatter_plot():
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]
    plt.scatter(x, y)
    plt.title('Basic Scatter Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

# Example 2: Scatter Plot with Custom Markers and Colors
def custom_marker_scatter_plot():
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]
    sizes = [20, 50, 80, 200, 500]  # Marker sizes
    colors = ['red', 'blue', 'green', 'purple', 'orange']  # Marker colors
    plt.scatter(x, y, s=sizes, c=colors, alpha=0.5)
    plt.title('Scatter Plot with Custom Markers and Colors')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

# Example 3: Scatter Plot with Transparency
def transparent_scatter_plot():
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]
    plt.scatter(x, y, alpha=0.5)  # Set transparency
    plt.title('Scatter Plot with Transparency')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

if __name__ == "__main__":
    basic_scatter_plot()
    custom_marker_scatter_plot()
    transparent_scatter_plot()