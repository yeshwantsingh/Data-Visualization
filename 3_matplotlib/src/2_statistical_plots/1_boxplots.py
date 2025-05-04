import matplotlib.pyplot as plt
import numpy as np

# Example 1: Basic Boxplot
data = [np.random.normal(0, std, 100) for std in range(1, 4)]
plt.boxplot(data, vert=True, patch_artist=True)
plt.title('Basic Boxplot')
plt.xlabel('Distribution')
plt.ylabel('Values')
plt.xticks([1, 2, 3], ['Std 1', 'Std 2', 'Std 3'])
plt.show()

# Example 2: Boxplot with Notches
data = [np.random.normal(0, std, 100) for std in range(1, 4)]
plt.boxplot(data, notch=True, vert=True, patch_artist=True)
plt.title('Boxplot with Notches')
plt.xlabel('Distribution')
plt.ylabel('Values')
plt.xticks([1, 2, 3], ['Std 1', 'Std 2', 'Std 3'])
plt.show()

# Example 3: Boxplot with Custom Colors
data = [np.random.normal(0, std, 100) for std in range(1, 4)]
box = plt.boxplot(data, vert=True, patch_artist=True, 
                  boxprops=dict(facecolor='lightblue', color='blue'),
                  medianprops=dict(color='red'))
plt.title('Boxplot with Custom Colors')
plt.xlabel('Distribution')
plt.ylabel('Values')
plt.xticks([1, 2, 3], ['Std 1', 'Std 2', 'Std 3'])
plt.show()