import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Sample data
data = np.random.normal(loc=0, scale=1, size=100)
data2 = np.random.normal(loc=1, scale=1.5, size=100)

# Create a violin plot
plt.figure(figsize=(8, 6))
sns.violinplot(data=[data, data2], inner='quartile')
plt.title('Violin Plot Example')
plt.xlabel('Groups')
plt.ylabel('Values')
plt.xticks([0, 1], ['Group 1', 'Group 2'])
plt.grid(True)
plt.show()