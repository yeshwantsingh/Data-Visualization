import pandas as pd
import numpy as np

# Create a sample DataFrame
print("Creating a sample DataFrame:")
df = pd.DataFrame({
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Bob'],
    'Age': [28, 34, 29, 42, 37],
    'City': ['New York', 'Paris', 'Berlin', 'London', 'Tokyo'],
    'Salary': [65000, 75000, 62000, 84000, 78000],
    'Department': ['HR', 'IT', 'Sales', 'IT', 'HR']
})

print(df)

print(df['Age'] > 30)

# Basic filtering with conditions
# print("\n1. Employees older than 30:")
# print(df[df['Age'] > 30])

# # Multiple conditions
# print("\n2. Employees in IT with salary over 70000:")
# print(df[(df['Department'] == 'IT') & (df['Salary'] > 70000)])

# # Using query method
# print("\n3. Using query method - HR employees:")
# print(df.query('Department == "HR"'))

# String operations
# print("\n4. Names starting with 'P':")
# print(df[df['Name'].str.startswith('P')])

# # Selecting specific columns
# print("\n5. Only Name and Salary columns:")
# print(df[['Name', 'Salary']])

# # iloc for integer-location based indexing
# print("\n6. First 2 rows, columns 1-3 using iloc:")
# print(df.iloc[0:2, 1:4])

# loc for label-based indexing
# print("\n7. Specific rows and columns using loc:")
# print(df.loc[1:3, ['Name', 'Department']])

# Selecting with isin
# print("\n8. Employees in HR or Sales departments:")
# print(df[df['Department'].isin(['HR', 'Sales'])])

# # Boolean indexing with notna
# df.loc[0, 'Age'] = None
# print("\n9. Rows with non-null Age:")
# print(df[df['Age'].notna()])

# # Masking
# print("\n10. Masking salaries for privacy:")
# masked_df = df.copy()
# masked_df['Salary'] = masked_df['Salary'].apply(lambda x: '****')
# print(masked_df)
