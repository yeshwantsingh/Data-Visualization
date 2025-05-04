import matplotlib.pyplot as plt
import numpy as np

# Example 1: Basic Histogram
data1 = np.random.randn(1000)
plt.figure(figsize=(10, 6))
plt.hist(data1, bins=30, color='blue', alpha=0.7)
plt.title('Basic Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show()

# Example 2: Histogram with Custom Bin Sizes
data2 = np.random.randn(1000)
plt.figure(figsize=(10, 6))
plt.hist(data2, bins=np.arange(-4, 4, 0.5), color='green', alpha=0.7)
plt.title('Histogram with Custom Bin Sizes')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show()

# Example 3: Overlaying Histograms
data3 = np.random.randn(1000)
data4 = np.random.randn(1000) + 1  # Shifted data
plt.figure(figsize=(10, 6))
plt.hist(data3, bins=30, color='blue', alpha=0.5, label='Data 1')
plt.hist(data4, bins=30, color='red', alpha=0.5, label='Data 2')
plt.title('Overlaying Histograms')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.grid(axis='y', alpha=0.75)
plt.show()

# Example 4: Normalized Histogram
data5 = np.random.randn(1000)
plt.figure(figsize=(10, 6))
plt.hist(data5, bins=30, color='purple', alpha=0.7, density=True)
plt.title('Normalized Histogram')
plt.xlabel('Value')
plt.ylabel('Density')
plt.grid(axis='y', alpha=0.75)
plt.show()