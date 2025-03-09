import pandas as pd
import numpy as np

# Create a simple DataFrame
print("Creating a basic DataFrame:")
df = pd.DataFrame({
    'A': np.random.rand(5),
    'B': np.random.randint(0, 10, size=5),
    'C': pd.date_range(start='2023-01-01', periods=5),
    'D': pd.Series(['apple', 'banana', 'cherry', 'date', 'elderberry'])
})

# Display the DataFrame
print("\nDataFrame:")
print(df)

# Basic information about the DataFrame
print("\nDataFrame info:")
print(df.info())

# Statistical summary
print("\nDataFrame summary statistics:")
print(df.describe(include='all'))

# Basic operations
print("\nSelecting column 'A':")
print(df['A'])

print("\nFirst 2 rows:")
print(df.head(2))

print("\nAdding a new column 'E':")
df['E'] = df['B'] * 2
print(df)

print("\nRenaming columns:")
df = df.rename(columns={'A': 'Random', 'B': 'Integer'})
print(df)

# Save to CSV
df.to_csv('2_pandas/sample_data.csv', index=False)
print("\nDataFrame saved to CSV file.")
