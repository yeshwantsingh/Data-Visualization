import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create sample data
print("Creating sample data for visualization:")
dates = pd.date_range(start='2023-01-01', periods=100)
df = pd.DataFrame({
    'A': np.random.randn(100).cumsum(),
    'B': np.random.randn(100).cumsum(),
    'C': np.random.randn(100).cumsum(),
    'D': np.random.choice(['X', 'Y', 'Z'], 100)
}, index=dates)

print(df.head())

# # Set the plotting style
plt.style.use('ggplot')
plt.figure(figsize=(15, 15))

# 1. Line plot
print("\nGenerating visualizations...")
plt.subplot(3, 2, 1)
df[['A', 'B', 'C']].plot(title="Line Plot of A, B, C", ax=plt.gca())

plt.show()

# # 2. Bar plot
# plt.subplot(3, 2, 2)
# df[['A', 'B']].iloc[::10].plot.bar(title="Bar Plot (every 10th record)", ax=plt.gca())

# # 3. Histogram
# plt.subplot(3, 2, 3)
# df['A'].plot.hist(bins=20, alpha=0.5, title="Histogram of A", ax=plt.gca())

# # 4. Scatter plot
# plt.subplot(3, 2, 4)
# df.plot.scatter(x='A', y='B', c='C', cmap='viridis', 
#                 title="Scatter Plot A vs B (colored by C)", 
#                 ax=plt.gca())

# # 5. Box plot
# plt.subplot(3, 2, 5)
# df.boxplot(column=['A', 'B', 'C'], ax=plt.gca())
# plt.title("Box Plot")

# # 6. Area plot
# plt.subplot(3, 2, 6)
# df[['A', 'B', 'C']].iloc[::3].plot.area(alpha=0.4, title="Area Plot", ax=plt.gca())

# plt.tight_layout()
# plt.savefig('pandas_visualizations.png')
# print("All plots saved to 'pandas_visualizations.png'")

# # Additional visualization examples

# # 7. Create a grouped bar chart
# plt.figure(figsize=(10, 6))
# grouped = df.groupby('D').mean()
# grouped.plot.bar(title="Average Values by Category")
# plt.tight_layout()
# plt.savefig('grouped_bar.png')

# # 8. Create a pie chart
# plt.figure(figsize=(8, 8))
# category_counts = df['D'].value_counts()
# plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%')
# plt.title("Distribution of Category D")
# plt.tight_layout()
# plt.savefig('pie_chart.png')

# print("Additional plots saved to 'grouped_bar.png' and 'pie_chart.png'")

# print("\nAll visualizations complete!")
