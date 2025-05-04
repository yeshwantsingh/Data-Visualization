import numpy as np

# Create sample data
data = np.array([
    [5, 10, 15, 20],
    [25, 30, 35, 40],
    [45, 50, 55, 60],
    [65, 70, 75, 80]
])


print("Original data:")
print(data)

# Indexing and slicing
print("\nIndexing and slicing:")
print(f"First row: {data[0]}")
print(f"Last column: {data[:, -1]}")
print(f"2x2 submatrix from top-left:\n{data[:2, :2]}")
print(f"2x2 submatrix from bottom-right:\n{data[2:, 2:]}")

# Filtering data
print("\nFiltering data:")
print(f"Values greater than 50: {data[data > 50]}")
mask = (data > 30) & (data < 60)
print(f"Values between 30 and 60:\n{data[mask]}")

# Reshaping and stacking
print("\nReshaping and stacking:")
flattened = data.flatten()
print(f"Flattened array: {flattened}")

# Stack arrays horizontally and vertically
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(f"\nArray a: {a}")
print(f"Array b: {b}")

print(f"Horizontal stack: {np.hstack((a, b))}")
print(f"Vertical stack:\n{np.vstack((a, b))}")

# Splitting arrays
print("\nSplitting arrays:")
arr = np.arange(16).reshape(4, 4)
print("Array to split:")
print(arr)

print("\nHorizontal split (by columns):")
h_splits = np.hsplit(arr, 2)
for i, split in enumerate(h_splits):
    print(f"Split {i+1}:\n{split}")

print("\nVertical split (by rows):")
v_splits = np.vsplit(arr, 2)
for i, split in enumerate(v_splits):
    print(f"Split {i+1}:\n{split}")

# Statistical operations
print("\nStatistical operations:")
print(f"Mean of each column: {data.mean(axis=0)}")
print(f"Sum of each row: {data.sum(axis=1)}")
print(f"Overall standard deviation: {data.std()}")
print(f"Minimum value: {data.min()}")
print(f"Maximum value: {data.max()}")
print(f"Value ranges (max-min) in each column: {data.ptp(axis=0)}")
