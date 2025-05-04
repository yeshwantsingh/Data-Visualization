import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load a sample dataset
df = sns.load_dataset('iris')

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Create a correlation plot
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', square=True, cbar_kws={"shrink": .8})
plt.title('Correlation Plot of Iris Dataset')
plt.show()