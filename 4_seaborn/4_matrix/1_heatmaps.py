import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Example 1: Basic Heatmap
data = np.random.rand(10, 12)
sns.heatmap(data)
plt.title('Basic Heatmap')
plt.show()

# Example 2: Heatmap with Annotations
data = np.random.rand(10, 12)
sns.heatmap(data, annot=True, fmt=".2f")
plt.title('Heatmap with Annotations')
plt.show()

# Example 3: Heatmap with Custom Color Palette
data = np.random.rand(10, 12)
sns.heatmap(data, cmap='coolwarm')
plt.title('Heatmap with Custom Color Palette')
plt.show()

# Example 4: Heatmap with a Mask
data = np.random.rand(10, 12)
mask = np.zeros_like(data)
mask[data < 0.5] = True
sns.heatmap(data, mask=mask, cmap='viridis')
plt.title('Heatmap with Mask')
plt.show()

# Example 5: Heatmap with Custom Tick Labels
data = np.random.rand(10, 12)
sns.heatmap(data, xticklabels=np.arange(1, 13), yticklabels=np.arange(1, 11))
plt.title('Heatmap with Custom Tick Labels')
plt.show()