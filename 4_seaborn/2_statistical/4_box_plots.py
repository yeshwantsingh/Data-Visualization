import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = pd.DataFrame({
    "Category": ["A", "B", "C", "A", "B", "C", "A", "B", "C"],
    "Values": [1, 2, 3, 4, 5, 6, 7, 8, 9]
})

# Example 1: Basic Box Plot
plt.figure(figsize=(8, 6))
sns.boxplot(x="Category", y="Values", data=data)
plt.title("Basic Box Plot")
plt.show()

# Example 2: Box Plot with Notches
plt.figure(figsize=(8, 6))
sns.boxplot(x="Category", y="Values", data=data, notch=True)
plt.title("Box Plot with Notches")
plt.show()

# Example 3: Box Plot with Hue
plt.figure(figsize=(8, 6))
sns.boxplot(x="Category", y="Values", data=data, hue="Category")
plt.title("Box Plot with Hue")
plt.show()

# Example 4: Box Plot with Swarm Plot Overlay
plt.figure(figsize=(8, 6))
sns.boxplot(x="Category", y="Values", data=data)
sns.swarmplot(x="Category", y="Values", data=data, color=".25")
plt.title("Box Plot with Swarm Plot Overlay")
plt.show()