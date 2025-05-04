import numpy as np

# Creating matrices
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)


# Matrix operations
print("\nMatrix operations:")
print("A + B:")
print(A + B)

print("\nA - B:")
print(A - B)

print("\nMatrix multiplication (A @ B):")
print(A @ B)  # Matrix multiplication

print("\nElement-wise multiplication (A * B):")
print(A * B)  # Element-wise multiplication

# Transpose
print("\nTranspose of A:")
print(A.T)

# Determinant
C = np.array([[1, 2], [3, 4]])
print("\nMatrix C:")
print(C)
print(f"Determinant of C: {np.linalg.det(C)}")

# Inverse of a matrix
print("\nInverse of C:")
try:
    C_inv = np.linalg.inv(C)
    print(C_inv)
    print("\nVerification (C @ C_inv should be identity):")
    print(C @ C_inv)
except np.linalg.LinAlgError as e:
    print(f"Error: {e}")

# Eigenvalues and eigenvectors
print("\nEigenvalues and Eigenvectors of C:")
eigenvalues, eigenvectors = np.linalg.eig(C)
print(f"Eigenvalues: {eigenvalues}")
print("Eigenvectors:")
print(eigenvectors)

# Solving linear equations: Ax = b
b = np.array([1, 2])
print("\nSolving linear equation Cx = b where b =", b)
x = np.linalg.solve(C, b)
print("Solution x =", x)
print("Verification (C @ x should equal b):")
print(C @ x)
