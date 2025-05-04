import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'A', 'B', 'C'],
    'value': [1, 3, 2, 4, 5, 6]
})

# Example 1: Basic point plot
plt.figure(figsize=(8, 5))
sns.pointplot(x='category', y='value', data=data)
plt.title('Basic Point Plot')
plt.show()

# Example 2: Point plot with error bars
plt.figure(figsize=(8, 5))
sns.pointplot(x='category', y='value', data=data, ci='sd')
plt.title('Point Plot with Error Bars')
plt.show()

# Example 3: Point plot with hue
plt.figure(figsize=(8, 5))
sns.pointplot(x='category', y='value', data=data, hue='category', dodge=True)
plt.title('Point Plot with Hue')
plt.show()