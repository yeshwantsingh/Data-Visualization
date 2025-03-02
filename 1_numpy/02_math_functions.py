import numpy as np

# Create a sample array
arr = np.array([1, 2, 3, 4, 5])
print(f"Original array: {arr}")

# Basic arithmetic
print("\nBasic arithmetic:")
print(f"Add 2: {arr + 2}")
print(f"Multiply by 3: {arr * 3}")
print(f"Square: {arr ** 2}")
print(f"Sine: {np.sin(arr)}")
print(f"Cosine: {np.cos(arr)}")
print(f"Log (natural): {np.log(arr)}")
print(f"Exponent (e^x): {np.exp(arr)}")

# Array arithmetic
arr2 = np.array([5, 4, 3, 2, 1])
print(f"\nSecond array: {arr2}")
print(f"arr + arr2: {arr + arr2}")
print(f"arr * arr2: {arr * arr2}")
print(f"arr / arr2: {arr / arr2}")

# Aggregation functions
print("\nAggregation functions:")
print(f"Sum: {arr.sum()}")
print(f"Min: {arr.min()}")
print(f"Max: {arr.max()}")
print(f"Mean: {arr.mean()}")
print(f"Standard deviation: {arr.std()}")

# Cumulative functions
print("\nCumulative functions:")
print(f"Cumulative sum: {np.cumsum(arr)}")
print(f"Cumulative product: {np.cumprod(arr)}")

# Rounding functions
random_array = np.random.random(5) * 10
print(f"\nRandom array: {random_array}")
print(f"Rounded: {np.round(random_array)}")
print(f"Ceiling: {np.ceil(random_array)}")
print(f"Floor: {np.floor(random_array)}")
