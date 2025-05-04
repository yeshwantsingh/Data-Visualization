import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Generate sample data
np.random.seed(0)
x = np.random.normal(size=100)
y = np.random.normal(size=100)
data = pd.DataFrame({'x': x, 'y': y})

# Create a joint plot
sns.jointplot(x='x', y='y', data=data, kind='scatter', color='blue')
plt.title('Joint Plot of X and Y')
plt.show()

# Create a joint plot with a regression line
sns.jointplot(x='x', y='y', data=data, kind='reg', color='green')
plt.title('Joint Plot with Regression Line')
plt.show()

# Create a joint plot with marginal histograms
sns.jointplot(x='x', y='y', data=data, kind='hist', color='orange')
plt.title('Joint Plot with Marginal Histograms')
plt.show()