import numpy as np # np is an alias for the numpy package

# # Creating arrays
# print("Basic array creation:")
# arr1 = np.array([1, 2, 3, 4, 5])
# print(f"1D array: {arr1}")


# arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# print(f"2D array:\n{arr2}")

# # Array properties
# print("\nArray properties:")
# print(f"Shape: {arr2.shape}")
# print(f"Dimensions: {arr2.ndim}")
# print(f"Data type: {arr2.dtype}")
# print(f"Size: {arr2.size}")

# # Special arrays
# print("\nSpecial arrays:")
# zeros = np.zeros((3, 3))
# print(f"Zeros:\n{zeros}")

# ones = np.ones((2, 4))
# print(f"Ones:\n{ones}")

# twoes = 2*np.ones((2, 4))
# print(f"Twoes:\n{twoes}")

# my_mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(f"My matrix:\n{my_mat}")

# my_mat_times_2 = 2*np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(f"My matrix times 2:\n{my_mat_times_2}")

# identity = np.eye(5) # 5x5 identity matrix
# print(f"Identity matrix:\n{identity}")


# Array range
print("\nArray ranges:")
range_arr = np.arange(0, 10, 2)
print(f"Range array: {range_arr}")

linspace = np.linspace(0, 100, 5)
print(f"Linspace array: {linspace}")

# Reshaping arrays
print("\nReshaping arrays:")
arr = np.arange(10)
print(f"Original: {arr}")
print(f"Reshaped to 2x5:\n{arr.reshape(5, 2)}")
