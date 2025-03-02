import numpy as np
from numpy import random

# Set seed for reproducibility
np.random.seed(42)
print("Random number generation with NumPy (seed=42)")

# Random samples from uniform distribution
print("\nUniform distribution:")
uniform_samples = random.random(5)  # 5 random numbers between 0 and 1
print(f"Random samples (0 to 1): {uniform_samples}")

uniform_range = random.uniform(10, 20, 5)  # 5 random numbers between 10 and 20
print(f"Random uniform (10 to 20): {uniform_range}")

# Random integers
print("\nRandom integers:")
random_ints = random.randint(1, 100, 5)  # 5 random integers between 1 and 100
print(f"Random integers (1 to 100): {random_ints}")

# Random from normal distribution
print("\nNormal distribution:")
normal_samples = random.normal(loc=0, scale=1, size=5)  # 5 samples from normal distribution with mean 0, std 1
print(f"Normal distribution (mean=0, std=1): {normal_samples}")

# Random shuffling
print("\nRandom shuffling:")
arr = np.arange(10)
print(f"Original array: {arr}")
random.shuffle(arr)
print(f"Shuffled array: {arr}")

# Random choice
print("\nRandom choice:")
choices = random.choice(["apple", "banana", "cherry", "date", "elderberry"], size=3)
print(f"Random choices: {choices}")

# Random permutation
print("\nRandom permutation:")
original = np.arange(5)
print(f"Original: {original}")
permuted = random.permutation(original)
print(f"Permuted: {permuted}")

# Generating a random 2D array
print("\n2D random array:")
random_2d = random.rand(3, 3)  # 3x3 array of random numbers between 0 and 1
print(random_2d)
