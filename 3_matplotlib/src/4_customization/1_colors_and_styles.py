import matplotlib.pyplot as plt

def plot_with_custom_colors():
    # Example of a simple line plot with custom colors
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]
    
    plt.plot(x, y, color='purple', linewidth=2, marker='o', markersize=8)
    plt.title('Line Plot with Custom Color')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show()

def plot_with_custom_styles():
    # Example of a scatter plot with custom styles
    x = [1, 2, 3, 4, 5]
    y = [5, 7, 8, 5, 6]
    
    plt.scatter(x, y, color='orange', s=100, edgecolor='black', alpha=0.7)
    plt.title('Scatter Plot with Custom Styles')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show()

def plot_with_custom_palette():
    # Example of a bar chart with a custom color palette
    categories = ['A', 'B', 'C', 'D']
    values = [4, 7, 1, 8]
    
    colors = ['red', 'blue', 'green', 'yellow']
    plt.bar(categories, values, color=colors)
    plt.title('Bar Chart with Custom Color Palette')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.show()

if __name__ == "__main__":
    plot_with_custom_colors()
    plot_with_custom_styles()
    plot_with_custom_palette()