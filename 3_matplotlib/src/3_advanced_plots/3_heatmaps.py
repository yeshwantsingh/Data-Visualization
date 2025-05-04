import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
data = np.random.rand(10, 12)

# Create a heatmap
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar(label='Intensity')

# Add titles and labels
plt.title('Heatmap Example')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')

# Show the plot
plt.show()