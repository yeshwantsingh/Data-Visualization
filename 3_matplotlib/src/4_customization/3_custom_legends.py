import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 10)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a plot
plt.figure()

# Plotting the data
plt.plot(x, y1, label='Sine Wave', color='blue', marker='o')
plt.plot(x, y2, label='Cosine Wave', color='red', marker='x')

# Customizing the legend
plt.legend(loc='lower left', title='Trigonometric Functions', fontsize='medium', title_fontsize='large', shadow=True)

# Adding titles and labels
plt.title('Custom Legends Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()