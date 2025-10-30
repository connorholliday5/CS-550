import numpy as np

# Define matrices
A = np.array([[1, 4],
              [2, 3]])

B = np.array([[5, 19],
              [-2, 5]])

C = np.array([[2, 1, 9],
              [5, 7, 1],
              [4, 7, 1]])

# Compute determinants
det_A = np.linalg.det(A)
det_B = np.linalg.det(B)
det_C = np.linalg.det(C)

# Compute L1 norms (maximum absolute column sum)
norm_A = np.linalg.norm(A, 1)
norm_B = np.linalg.norm(B, 1)
norm_C = np.linalg.norm(C, 1)

# Print results
print("Matrix A:")
print(A)
print(f"Determinant: {det_A:.2f}")
print(f"L1 Norm: {norm_A:.2f}\n")

print("Matrix B:")
print(B)
print(f"Determinant: {det_B:.2f}")
print(f"L1 Norm: {norm_B:.2f}\n")

print("Matrix C:")
print(C)
print(f"Determinant: {det_C:.2f}")
print(f"L1 Norm: {norm_C:.2f}")
