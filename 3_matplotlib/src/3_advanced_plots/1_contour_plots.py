import numpy as np
import matplotlib.pyplot as plt

# Create a grid of points
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Define a function for the contour plot
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create the contour plot
plt.figure()
contour = plt.contour(X, Y, Z, levels=20, cmap='viridis')
plt.colorbar(contour)

# Add titles and labels
plt.title('Contour Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()