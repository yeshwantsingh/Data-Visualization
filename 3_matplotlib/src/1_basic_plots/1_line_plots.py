import matplotlib.pyplot as plt

# Example 1: Basic Line Plot
def basic_line_plot():
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]
    
    plt.plot(x, y, label='Line 1', color='blue', marker='o')
    plt.title('Basic Line Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid()
    plt.show()

# Example 2: Multiple Lines
def multiple_lines_plot():
    x = [1, 2, 3, 4, 5]
    y1 = [2, 3, 5, 7, 11]
    y2 = [1, 4, 6, 8, 10]
    
    plt.plot(x, y1, label='Line 1', color='blue', marker='o')
    plt.plot(x, y2, label='Line 2', color='red', marker='x')
    plt.title('Multiple Lines Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid()
    plt.show()

# Example 3: Line Plot with Customizations
def customized_line_plot():
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]
    
    plt.plot(x, y, label='Line 1', color='green', linestyle='--', linewidth=2, marker='s', markersize=8)
    plt.title('Customized Line Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    basic_line_plot()
    multiple_lines_plot()
    customized_line_plot()