import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# # Sample data
# data = pd.DataFrame({
#     'Year': [2015, 2016, 2017, 2018, 2019, 2020],
#     'Sales': [150, 200, 250, 300, 350, 400]
# })

# # Basic line plot
# plt.figure(figsize=(10, 6))
# sns.lineplot(x='Year', y='Sales', data=data, marker='o')
# plt.title('Sales Over Years')
# plt.xlabel('Year')
# plt.ylabel('Sales')
# plt.grid(True)
# plt.show()

# Multiple lines example
data2 = pd.DataFrame({
    'Year': [2015, 2016, 2017, 2018, 2019, 2020],
    'Product A': [150, 200, 250, 300, 350, 400],
    'Product B': [100, 150, 200, 250, 300, 350]
})

plt.figure(figsize=(10, 6))
sns.lineplot(x='Year', y='Product A', data=data2, marker='o', label='Product A')
sns.lineplot(x='Year', y='Product B', data=data2, marker='o', label='Product B')
plt.title('Sales of Products A and B Over Years')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.grid(True)
plt.legend()
plt.show()