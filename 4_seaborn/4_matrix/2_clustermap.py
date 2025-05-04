import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Generate sample data
data = np.random.rand(10, 12)
df = pd.DataFrame(data, columns=[f'Var{i}' for i in range(1, 13)])

# Create a cluster map
sns.clustermap(df, cmap='viridis', standard_scale=1)

# Show the plot
plt.title('Cluster Map Example')
plt.show()