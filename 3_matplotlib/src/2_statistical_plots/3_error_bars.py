import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 10)
y = np.sin(x)

# Error values
error = np.random.normal(0.1, 0.02, size=y.shape)

# Create a plot with error bars
plt.errorbar(x, y, yerr=error, fmt='o', label='Data with error bars', capsize=5)

# Adding titles and labels
plt.title('Error Bars Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Show the plot
plt.show()