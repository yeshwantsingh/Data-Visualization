import pandas as pd
import numpy as np

# Create a sample sales DataFrame
print("Creating a sample sales DataFrame:")
data = {
    'Date': pd.date_range(start='2023-01-01', periods=20),
    'Product': np.random.choice(['Laptop', 'Phone', 'Tablet', 'Monitor'], 20),
    'Category': np.random.choice(['Electronics', 'Computers', 'Accessories'], 20),
    'Store': np.random.choice(['North', 'South', 'East', 'West'], 20),
    'Sales': np.random.randint(1000, 5000, 20),
    'Units': np.random.randint(1, 10, 20)
}

df = pd.DataFrame(data)
print(df.head())

# Basic groupby
# print("\n1. Total sales by product:")
# product_sales = df.groupby('Product')['Sales'].sum()
# print(product_sales)

# # Multiple aggregations
# print("\n2. Multiple aggregations on sales by store:")
# store_stats = df.groupby('Store').agg({
#     'Sales': ['sum', 'mean', 'std'],
#     'Units': ['sum', 'mean']
# })
# print(store_stats)

# # Custom aggregation functions
# print("\n3. Custom aggregation - percentage of total sales:")
# total_sales = df['Sales'].sum()
# pct_by_category = df.groupby('Category')['Sales'].sum() / total_sales * 100
# print(pct_by_category)

# # Groupby with transformation
# print("\n4. Calculating % contribution within each store:")
# df['Store_Total'] = df.groupby('Store')['Sales'].transform('sum')
# df['Contribution_Pct'] = df['Sales'] / df['Store_Total'] * 100
# print(df[['Store', 'Product', 'Sales', 'Store_Total', 'Contribution_Pct']].head(10))

# # Multiple groupby levels
# print("\n5. Sales by Store and Product:")
# multi_group = df.groupby(['Store', 'Product'])['Sales'].sum().unstack()
# print(multi_group)

# # Using pivot_table
# print("\n6. Pivot table of average sales by Store and Category:")
# print(df.head())
# pivot = pd.pivot_table(
#     df, 
#     values='Sales', 
#     index='Store', 
#     columns='Category', 
#     aggfunc='mean',
#     fill_value=0
# )
# print(pivot)

# Computing pairwise correlation
# print("\n7. Correlation between sales and units by product:")
# product_corr = df.groupby('Product')[['Sales', 'Units']].corr()
# print(product_corr)

# # Filtering groups
# print("\n8. Stores with total sales > 15000:")
# store_filter = df.groupby('Store').filter(lambda x: x['Sales'].sum() > 15000)
# print(store_filter['Store'].unique())
