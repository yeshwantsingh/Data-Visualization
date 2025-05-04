import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Generate sample data
np.random.seed(0)
x = np.random.rand(100)
y = 2 * x + np.random.normal(0, 0.1, 100)

# Create a DataFrame
data = pd.DataFrame({'x': x, 'y': y})

# # Simple regression plot
# plt.figure(figsize=(10, 6))
# sns.regplot(x='x', y='y', data=data)
# plt.title('Simple Regression Plot')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.show()

# Regression plot with confidence interval
# plt.figure(figsize=(10, 6))
# sns.regplot(x='x', y='y', data=data, ci=95)
# plt.title('Regression Plot with Confidence Interval')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.show()

# # Polynomial regression plot
# plt.figure(figsize=(10, 6))
# sns.regplot(x='x', y='y', data=data, order=2)
# plt.title('Polynomial Regression Plot')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.show()

# # Regression plot with additional variables
# Generate more sample data
data['category'] = np.random.choice(['A', 'B'], size=100)

plt.figure(figsize=(10, 6))
sns.regplot(x='x', y='y', data=data, scatter_kws={'s': 50}, line_kws={'color': 'red'})
plt.title('Regression Plot with Additional Variables')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()